from django import forms
from employee.models import EmployeeProfile,Skill,Training,Experience,Degree,Cv
from company.models import CompanyProfile,Application,Vacancy

class EmployeeCreateForm(forms.ModelForm):

	class Meta:
		model=EmployeeProfile
		exclude=['user']


class SkillForm(forms.ModelForm):

	class Meta:
		model=Skill
		exclude=['employee']


class TrainingForm(forms.ModelForm):

	class Meta:
		model=Training
		exclude=['employee']

class ExperienceForm(forms.ModelForm):

	class Meta:
		model=Experience
		exclude=['employee']


class DegreeForm(forms.ModelForm):

	class Meta:
		model=Degree
		exclude=['employee']

class CvForm(forms.ModelForm):

	class Meta:
		model=Cv
		exclude=['employee']

class CompanyCreateForm(forms.ModelForm):

	class Meta:
		model=CompanyProfile
		exclude=['user']


class VacancyForm(forms.ModelForm):

	class Meta:
		model=Vacancy
		exclude=['company']



class ApplicationForm(forms.ModelForm):

	class Meta:
		model=Application
		exclude=['vacancy',]
