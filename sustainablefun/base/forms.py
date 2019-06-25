from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control",
                    "id": "inputNome",
                    "placeholder": "| Name*"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                    "class": "form-control",
                    "name": "email",
                    "id": "inputEmail",
                    "placeholder": "| Email*"
                }
            )
        )

    telefone = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "inputTelefone",
                "placeholder": "| Phone*"
            }
        )
    )

    mensagem = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control",
                    "name": "mensagem",
                    "rows": "5",
                    "cols" :"33",
                    "id": "inputMensagem",
                    "placeholder": "| Message*"
                }
            )
)