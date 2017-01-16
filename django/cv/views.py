from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm

from django.contrib import messages
# Create your views here.
def home(request):
	context={}
	return render(request , 'home.html' , context)


def me(request):
	context={}
	return render(request , 'aboutme.html' , context)

def exp(request):
	context={}
	return render(request , 'exp.html' , context)

def Contact(request):
	form_class=ContactForm
	context={'form': form_class}
	if request.method== 'POST':
		form=form_class(data=request.POST)
		if form.is_valid():
			name=request.POST.get('Name')
			email=request.POST.get('Email')
			subject=request.POST.get('Subject')
			message=request.POST.get('Message')
			form_content=request.POST.get('content' , '')
			template=get_template('contact_template.txt')
			context=Context({
				'name':name,
				'email':email,
				'subject':subject,
				'message':message,
				})	
			content=template.render(context)
			# email=EmailMessage("New contact form submission", content ,"navindjnago@gmail.com" , reply_to=['navinnarshetty@gmail.com'] )
			send_mail('JOB', content, 'Your website', ['navinnarshetty@gmail.com']  , fail_silently=False)
			# email.send()
			messages.success(request , 'Your message has been sent')
			return redirect('contact')
		

	return render (request , 'contact.html' , context)			



# send_mail('<Your subject>', '<Your message>', 'from@example.com', ['to@example.com'])