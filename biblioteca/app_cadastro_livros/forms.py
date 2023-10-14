from django import forms


class BuscaLivroForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=255)



class BuscaAutorForm(forms.Form):
    autor = forms.CharField(label='Autor', max_length=255)


