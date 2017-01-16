from django import forms


class ContactForm(forms.Form):
	Name=forms.CharField(max_length=120 , required=True , error_messages={'required':'This field is required'}, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	Email=forms.EmailField(required =True ,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	#Subject=forms.CharField(max_length=120 , required=True ,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	Message=forms.CharField( required=True ,widget=forms.Textarea(attrs={'placeholder': 'Message'}))