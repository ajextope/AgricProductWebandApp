# core/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import AgriculturalData

class AgriculturalDataForm(forms.ModelForm):
    class Meta:
        model = AgriculturalData
        fields = [
            'country', 'crop', 'year', 'area_harvested_ha', 
            'rainfall_mm', 'temperature_c', 'policy_flag',
            'transport_cost_usd', 'demand_supply_gap'
        ]
        widgets = {
            'year': forms.NumberInput(attrs={
                'min': 2000, 
                'max': 2100,
                'class': 'form-control'
            }),
            'area_harvested_ha': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control'
            }),
            'rainfall_mm': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control'
            }),
            'temperature_c': forms.NumberInput(attrs={
                'step': '0.1',
                'class': 'form-control'
            }),
            'transport_cost_usd': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control'
            }),
            'demand_supply_gap': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control'
            }),
        }
        labels = {
            'area_harvested_ha': 'Area Harvested (ha)',
            'rainfall_mm': 'Rainfall (mm)',
            'temperature_c': 'Temperature (°C)',
            'transport_cost_usd': 'Transport Cost (USD)',
            'demand_supply_gap': 'Demand Supply Gap',
            'policy_flag': 'Policy Type',
        }

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }