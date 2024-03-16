from django import forms 
import re 
from django.contrib.auth.models import User
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Tài khoản:')
    email = forms.EmailField(max_length=100, label='Email:')
    password1 = forms.CharField(label='Nhập mật khẩu:', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
            raise forms.ValidationError('Mật khẩu không trùng nhau')
    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError('Mật khẩu chứa kí tự đặc biệt')
        try: 
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Tài khoản đã toàn tại')
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])
class ParkingDataSearchForm(forms.Form):
        id = forms.IntegerField(label="Nhập id:", required=False)
        name = forms.CharField(label='Họ và tên:', max_length=100, required=False)
        biensoxe = forms.CharField(label="Biển số xe:", max_length=100, required=False)
        mobile = forms.CharField(label="Nhập số điện thoại", max_length=100, required=False)
        tinhtrang = forms.CharField(label="Tình trạng xe:", max_length=100,required=False)
        thanhtoan = forms.CharField(label="Tình trạng xe:", max_length=100,required=False)
