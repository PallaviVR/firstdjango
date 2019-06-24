from django import forms


class BookForms(forms.Form):
    name=forms.CharField(label='BookName',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Name of Book'}))

    purchase_date=forms.DateField(label='Date Of Purchase',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Purchase Date'}))

    genre=forms.CharField(label='Genre Of Book',
        widget=forms.TextInput(attrs={'maxlength':'30','placeholder':'Genre of Book'}))

