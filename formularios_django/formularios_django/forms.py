from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=30, label='Escribe tu nombre:')
    url = forms.URLField(label='Tu sitio web', required=False, initial='http://')
    comment = forms.CharField(max_length=250)


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.CharField(label='Mensaje',widget=forms.Textarea(attrs={'class':'form-control'}))

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != 'Open':
            raise forms.ValidationError("Su nombre debe ser Open")
        else:
            return name
            # Exito