from django.contrib import admin
from .models import Test
from .models import QuestionType
from .models import Question
from .models import Answer

admin.site.register(Test)
admin.site.register(QuestionType)
admin.site.register(Question)
admin.site.register(Answer)
