from django.contrib import admin
<<<<<<< HEAD
from problems.models import Problem, Test, Code

admin.site.register(Problem)
admin.site.register(Test)
admin.site.register(Code)
=======
from problems.models import Problem, Test, ProblemTest, Code, ProblemCode

admin.site.register(Problem)
admin.site.register(Test)
admin.site.register(ProblemTest)
admin.site.register(Code)
admin.site.register(ProblemCode)
>>>>>>> eb2e0ae (PYT-21: Craeted problems app and problem models)
