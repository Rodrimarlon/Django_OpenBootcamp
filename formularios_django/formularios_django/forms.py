from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=30, label='Escribe tu nombre:')
    url = forms.URLField(label='Tu sitio web', required=False, initial='http://')
    comment = forms.CharField(max_length=250)


