
from django import forms
from student.models import Students
from student.models import Teacher



class Studentform(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'


class Teacherform(forms.ModelForm):
    class Meta:
        model=Teacher
        fields='__all__'