from django.shortcuts import render
from .models import *
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib.auth.models import User

def ticket_gen():
		import random
		id = request.user.id
		rand = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]
		char_1 = random.choice(rand)
		char_2 = random.choice(rand)
		char_3 = random.choice(rand)
		char_4 = random.choice(rand)
		char_5 = random.choice(rand)
		char_6 = random.choice(rand)
		phone_1 = random.choice(phone_no)
		phone_2 = random.choice(phone_no)
		phone_3 = random.choice(phone_no)
		ticket_raw = [char_1, char_2, char_3, char_4, char_5, char_6, phone_3, phone_2, phone_1, id]
		ticket_r_1 = random.choice(ticket_raw)
		ticket_r_2 = random.choice(ticket_raw)
		ticket_r_3 = random.choice(ticket_raw)
		ticket_r_4 = random.choice(ticket_raw)
		ticket_r_5 = random.choice(ticket_raw)
		ticket_r_6 = random.choice(ticket_raw)
		ticket_r_7 = random.choice(ticket_raw)
		ticket_r_8 = random.choice(ticket_raw)
		ticket_r_9 = random.choice(ticket_raw)
		ticket_r_10 = random.choice(ticket_raw)
		ticket_no = ticket_r_10 + ticket_r_9 + ticket_r_8 + ticket_r_7 + ticket_r_6 + ticket_r_5 + ticket_r_3 + ticket_r_4 + ticket_r_1 + ticket_r_2  

		def __str__(self):
			return self.ticket_no

#first the shitty post request for registration and login
	def register():
		if method.request == POST
			for i in request.POST:
			if request.POST[i] == "":
				return render(request, 'registrations/error.html', {'error_heading' : 'Missing Details', 'error_message' : 'Please fill the form correctly.<br><a href="."><button>Register Here</button></a>'})
		prod = request.POST['prod']
		Cons_name = request.POST['Cons_name']
		gender = request.POST['gender']
		if gender == 'male'
			gender = 'male'
		else gender = 'female'
			gender = 'female'
		Age = request.POST['Age']
		add = request.POST['add']
		prov = request.POST['prov']
		zip_c = request.POST['zip_c']
		country = request.POST['country']
		phone_no = request.POST['phone_no']
		Ext = request.POST['Ext']
		reciept = request.POST['reciept']
		email_id = request.POST['email_id']

		try:
			already_reg = customers.objects.get(email_id=email_id)
			return render(request, 'main/error.html', {'error_heading': 'User alredy registered', 'error_message': 'The email id is already registered'})
		except:		
			pass

		try:
			member.user = User.objects.create_user(email_id, phone_no, #details to be asked)
		except:
			return render(request, 'main/error.html')
		member.user.save()
		member.prod = prod
		member.Cons_name = Cons_name
		member.gender = gender
		menber.Age = Age
		member.add = add
		member.prov = prov
		member.zip_c = zip_c
		member.country = country
		member.phone_no = phone_no
		member.Ext = Ext
		member.reciept = reciept
		member.email_id = email_id
		member.ticket_no = ticket_no
		member.save()

		body = unicode(u'''
			Dear %s,
				Your order has been recieved with the following information:
				Order No: %s
				Product Name: %s
				Address: %s, %s, %s, %s
				%s
				''') % (Cons_name, ticket_no, prod, add, prov, zip_c, country, phone_no)
				send_to = email_id

				try:
					email = EmailMessage('Your order has been placed')

					

	def login_check():
	def ticket_history():
	def dashboard():
		#call ticket_history
		#messages to be displayed

