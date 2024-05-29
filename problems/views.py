from django.shortcuts import render, get_object_or_404
from .models import Problem, Code, Test, CompletedProblem
from django.views.generic import DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


def index(request):
    problems = Problem.objects.all()
    completed_problems = CompletedProblem.objects.filter(user=request.user) if request.user.is_authenticated else []
    completed_problem_ids = [cp.problem_id for cp in completed_problems]
    return render(request, 'problems/index.html', {'problems': problems, 'completed_problem_ids': completed_problem_ids})



class ProblemDetailView(DetailView):
    model = Problem
    template_name = 'problems/detail.html'
    context_object_name = 'problem'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            code_obj, created = Code.objects.get_or_create(problem=self.object, user=self.request.user)
            context['user_code'] = code_obj.content
        return context


@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        input_data = request.POST.get('input_data', '')
        try:
            result = subprocess.run(['python', '-c', code], input=input_data, capture_output=True, text=True,
                                    check=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = e.stderr
        return JsonResponse({'output': output})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def save_code(request):
    if request.method == 'POST' and request.user.is_authenticated:
        problem_id = request.POST.get('problem_id')
        code_content = request.POST.get('code')
        problem = get_object_or_404(Problem, pk=problem_id)
        code_obj, created = Code.objects.get_or_create(problem=problem, user=request.user)
        code_obj.content = code_content
        code_obj.save()
        return JsonResponse({'status': 'Code saved successfully'})
    return JsonResponse({'error': 'Invalid request method or user not authenticated'}, status=400)


@csrf_exempt
def check_code(request):
    if request.method == 'POST' and request.user.is_authenticated:
        problem_id = request.POST.get('problem_id')
        code_content = request.POST.get('code')
        problem = get_object_or_404(Problem, pk=problem_id)
        tests = Test.objects.filter(problem=problem)

        all_passed = True
        results = []
        for test in tests:
            try:
                result = subprocess.run(
                    ['python', '-c', code_content],
                    input=test.input,
                    capture_output=True,
                    text=True,
                    check=True
                )
                output = result.stdout.strip()
                passed = (output == test.output.strip())
                if not passed:
                    all_passed = False
                results.append({
                    'input': test.input,
                    'expected_output': test.output,
                    'actual_output': output,
                    'passed': passed
                })
            except subprocess.CalledProcessError as e:
                all_passed = False
                results.append({
                    'input': test.input,
                    'expected_output': test.output,
                    'actual_output': e.stderr,
                    'passed': False
                })

        if all_passed:
            CompletedProblem.objects.get_or_create(user=request.user, problem=problem)

        return JsonResponse({'results': results, 'all_passed': all_passed})
    return JsonResponse({'error': 'Invalid request method or user not authenticated'}, status=400)
