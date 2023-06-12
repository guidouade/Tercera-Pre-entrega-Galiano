from django import forms

class FormularioSugerencias (forms.Form):
    nombre= forms.CharField(label= "Nombre", required=True)
    email= forms.EmailField(label= "Email", required=True)
    sugerencia= forms.CharField(label= "Tus Sugerencias", widget=forms.Textarea)