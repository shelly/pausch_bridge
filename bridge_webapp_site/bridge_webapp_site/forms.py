import requests 

from django import forms

class TextForm(forms.Form):

	your_text = forms.CharField()
	your_color = forms.CharField()

	def submit_text(self): 
		self.your_text = self.cleaned_data['your_text']
		self.your_color = self.cleaned_data['your_color']

		r, g, b = 252, 91, 123 

		# if color == 'light_pink':
		# 	r, g, b = 252, 91, 123
		# elif color == 'orange':
		# 	r, g, b = 252, 91, 123
		# elif color == 'yellow':
		# 	r, g, b = 252, 91, 123
		# elif color == 'bright_pink':
		# 	r, g, b = 252, 91, 123
		# elif color == 'purple':
		# 	r, g, b = 252, 91, 252 
		# elif color == 'violet':
		# 	r, g, b = 123, 91, 252
		# elif color == 'blue':
		# 	r, g, b = 41, 119, 255
		# else: # teal 
		# 	r, g, b = 62, 230, 242
		url = 'http://192.168.1.13/trigger?var={0},{1},{2},{3}'.format(self.your_text, r, g, b)
		print(url)
		requests.get(url)

