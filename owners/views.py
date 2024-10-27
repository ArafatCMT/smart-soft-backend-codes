from django.shortcuts import render, redirect
from rest_framework.views import APIView
from . import serializers
from owners.models import Owner
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from . import permissions

# Create your views here.
class RegistrationView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            # print(user)
            # print(request.user)

            # confirmation mail ta ke strong korar jonno token and uid user korta ci 
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))

            verification_link = f"https://smart-soft-gold.vercel.app/owners/verify/{uid}/{token}"

            email_subject = "Verify Your Account"
            email_body = render_to_string('verification_mail.html', {'verification_link': verification_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response("Check your email for confirmation", status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
def is_active(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid) # decode korar por jei uid ta pelam ei uid ta kon user er primary_key oi user ta ke get kortaci
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        print(user)
        user.is_active = True
        user.save()
        return redirect('https://arafatcmt.github.io/smart_soft-frontend-codes/login.html')
    return redirect('register')

class LoginView(APIView):
    permission_classes = [permissions.IsNotAuthenticated]
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data = self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
         

            user = authenticate(username=username, password=password)
            # print(user)
            # p

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                # print('get',token)
                

                login(request, user)
                owner = Owner.objects.get(user=request.user)
                print(owner.id)
                return Response({'token': token.key, 'owner_id': owner.id})
            else:
                return Response({'error': "Invalid Credential"})
        return Response(serializer.errors)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # print('logout',request.user)
        request.user.auth_token.delete()
        logout(request)
        return Response({'details': 'logout successfully'})
    

class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.OwnerSerializer

    def get(self, request, id, format=None):
        owner = Owner.objects.get(id=id)
        serializer = self.serializer_class(owner)
        return Response(serializer.data)
    
    def put(self,request, id, format=None):
        owner = Owner.objects.get(id=id)
        serializer = self.serializer_class(owner, data= request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(APIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get(self, request, id, format=None):
        owner = Owner.objects.get(id=id)
        user = User.objects.get(id=owner.user.id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
