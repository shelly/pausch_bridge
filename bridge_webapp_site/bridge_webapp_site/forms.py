import requests 

from django import forms

class TextForm(forms.Form):

	your_text = forms.CharField()
	your_color = forms.CharField()

	def submit_text(self): 
		print("Submit text called.")
		self.your_text = self.cleaned_data['your_text']
		self.your_color = self.cleaned_data['your_color']

		text = self.your_text 
		color = self.your_color 
		r, g, b = 0.5, 0.5, 0.5 
		side = '' 

		if color == 'light_pink':
			r, g, b = .98,.35,.48
			side = 'bot'
		elif color == 'orange':
			r, g, b = 1,.7,.11
			side = 'bot'
		elif color == 'yellow':
			r, g, b = 0.8,.78,.1
			side = 'bot'
		elif color == 'bright_pink':
			r, g, b = .98,.35,.73
			side = 'bot'
		elif color == 'purple':
			r, g, b = 0.82, 0.45, 0.98
			side = 'top' 
		elif color == 'violet':
			r, g, b = 0.48, 0.36, 0.9
			side = 'top'
		elif color == 'blue':
			r, g, b = 0.06, 0.27, 0.8
			side = 'top'
		else: # teal 
			r, g, b = 0.24, 0.9, 0.95
			side = 'top'

		print(text, color, r, g, b, side)
		# do something with text, r, g, b, and side 



