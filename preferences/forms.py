from django import forms
from .models import Preferences



class PreferencesTemplateForm(forms.Form):

	model = Preferences
	
	name = forms.CharField()
	list_fields = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple, choices='')

	def __init__(self, *args, **kwargs):
		super(PreferencesTemplateForm, self).__init__(*args, **kwargs)
		field_touples = self.get_model_field()
		self.fields['list_fields'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices = self.get_model_field() )
	
	def get_model_field(self):
		field_names = self.model._meta.get_all_field_names()

		field_touples =( (name, name) for name in field_names )


		return field_touples

