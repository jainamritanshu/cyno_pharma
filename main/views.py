from django.shortcuts import render

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

	def login_check():
	def ticket_history():
	def dashboard():
		#call ticket_history
		#messages to be displayed

