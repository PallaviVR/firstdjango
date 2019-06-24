from django import forms



class CustomForms(forms.Form):
    username= forms.CharField(
        label = ' Username ',
        widget=forms.TextInput(attrs=
            {'placeholder':'Your Username','class':'form-control'}))

    email = forms.EmailField(
        label=' Your Email',
        widget=forms.EmailInput(attrs=
            {'placeholder':'ac@email.com','class':'form-control'}))
    password = forms.CharField(
        label=' Your Password',
        widget=forms.PasswordInput(attrs=
            {'placeholder':'','class':'form-control'}))
    confirm_password = forms.CharField(
        label='Password again',
        widget=forms.PasswordInput(attrs=
            {'placeholder':'','class':'form-control'}))