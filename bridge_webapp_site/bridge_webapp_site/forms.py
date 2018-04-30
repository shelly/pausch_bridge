import requests 

from django import forms

class TextForm(forms.Form):

	your_text = forms.CharField()
	your_color = forms.CharField()

	def submit_text(self): 
		self.your_text = self.cleaned_data['your_text']
		self.your_color = self.cleaned_data['your_color']

		requests.get('http://192.168.1.13/trigger/')