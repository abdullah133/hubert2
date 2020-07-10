from django import forms


class KontaktForm(forms.Form):
    user_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': '', 'placeholder':'Deine E-Mail Adresse'}), required=True, label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Dein Name'}), required=True, label='')
    betreff = forms.CharField(widget=forms.TextInput(attrs={'class': '', 'placeholder':'Betreff'}), required=True, label='')
    nachricht = forms.CharField(widget=forms.Textarea(attrs={'class': '', 'placeholder':'Schreibe mir eine Nachricht...'}), required=True, label= '', max_length=900)
