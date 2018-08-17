from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'description']

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        phone_number = cleaned_data.get("phone_number")
        description = cleaned_data.get("description")
        
        if name and email and phone_number and description:
            pass
        else:
            raise forms.ValidationError(
                    "Enter all the required fields"
                )
        


    def save(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone_number = self.cleaned_data["phone_number"]
        description = self.cleaned_data["description"]
        new = Contact.objects.create(name=name, email = email, phone_number=phone_number, description=description)
        new.save()
        