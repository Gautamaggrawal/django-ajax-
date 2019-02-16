from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request, 'core/signup.html')


class LoginUserView(APIView):
	def post(self,request):
		print(request.data)
		print("aaaaaaaaaaaaaaaa")
		username=request.data.get('username')
		password=request.data.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return Response({"message": "Success"})
			else:
				return Response({"message": "inactive"})
		else:
			return Response({"message": "invalid"})
		return Response({"message": "denied"})

class SignupUserView(APIView):
	def post(self,request):
		print(request.data)
		print("aaaaaaaaaaaaaaaa")
		username=request.data.get('username')
		email=request.data.get('email')
		firstname=request.data.get('firstname')
		lastname=request.data.get('lastname')
		password2=request.data.get('password2')
		password=request.data.get('password')

		if username and email and firstname and lastname and password and password2:
			if password2!=password:
				return Response({"error":"passwords not matched"})
			elif password==password2:
				if User.objects.filter(username=username).exists():
					return Response({"error":"User already exists"})

				usr=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
				usr.save()
				return Response({"message":"created"})


class ProfileDetails(APIView):
	def get(self,request):
		details=Profile.objects.filter(user=request.user).values('user__first_name','user__email',"college_name",'age','summary')
		print(details)
		return Response({"details":details})

	
	def post(self,request):
		collegename=request.data.get("collegename")
		age=request.data.get("age")
		summary=request.data.get("summary")
		profileobj=Profile.objects.filter(user=request.user)
		if profileobj.exists():
			profileobj.update(college_name=collegename,age=age,summary=summary)
		else:
			pobj=Profile.objects.create(user=request.user,college_name=collegename,age=age,summary=summary)
			pobj.save()

		profileobj[0].save()
		return Response({"message":"saved"})

