from django.contrib import admin
from problems.models import Problem, Test, ProblemTest, Code, ProblemCode

admin.site.register(Problem)
admin.site.register(Test)
admin.site.register(ProblemTest)
admin.site.register(Code)
admin.site.register(ProblemCode)
