from django.db import models

class customer(models.Model):
	prod = models.CharField(max_length=300, is_required = True)
	Cons_name = models.CharField(max_length = 50, is_required = True)
	gender = models.ChoiceField(choices = Gender, is_required = True)
	Age = models.IntegerField(max_length = 2, is_required = True)
	add = models.CharField(max_length = 500, is_required = True)
	prov = models.CharField(max_length=30, is_required = True)
	zip_c = models.IntegerField(max_length=10, is_required = True)
	country = models.CharField(max_length=20, is_required = True)
	phone_no = models.IntegerField(max_length=15, is_required = True)
	Ext = models.IntegerField(max_length=4, is_required = True)
	receipt = models.FileField(upload_to=#dekhte hain, #to be completed)
	email_id = models.CharField(max_length=100, is_required = True)

	def __str__(self):
		return self.Cons_name

class ticket(models.Model):
	choice_ticket = {query = 'query',
					 order = 'order',
					}
	choice_temp = {
					#make a dict of templates used by agents
	}
	user = models.ForeignKey(customer)
	ticket = models.ChoiceField(choices = choice_ticket, is_required = True)
class agent(models.Model):
	#some shitty details

class message(models.Model):
	user = models.ForeignKey(customer)
	msg_text = models.CharField(max_length = 1000, is_required = True)

class reply(models.Model):
	rep_text = models.ForeignKey(message, max_length = 1000, is_required = True)
	templates = models.ChoiceField(choices = choice_temp)
