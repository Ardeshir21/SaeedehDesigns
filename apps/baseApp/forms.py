from django import forms
# from phonenumber_field.formfields import PhoneNumberField
from django.core.mail import send_mail
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Invisible



class ContactForm(forms.Form):
    # captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
    name = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Your Name*'})
                            )
    message = forms.CharField(max_length=2500,
                                widget=forms.Textarea(attrs={'placeholder': 'Message*',
                                                                'rows': '10',
                                                                'cols':'40'}))
    client_email = forms.EmailField(
                                widget=forms.EmailInput(attrs={'placeholder': 'Your email*'})
                                )
    subject = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Subject*'})
                            )
    # client_phone = PhoneNumberField(required=False,
    #                                 widget=forms.TextInput(attrs={'placeholder': 'Phone Number',
    #                                                                 'class': 'form-control'})
    #                                 )

    def send_email(self, current_url):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']
        client_email = self.cleaned_data['client_email']
        # client_phone = self.cleaned_data['client_phone']
        client_subject = self.cleaned_data['subject']
        recipients = ['contact@saeedehdesigns.com', client_email]
        mail_subject = 'Saeedeh Received Your Message - {}'.format(client_subject)

        message_edited = '''

Thank you for writing to us.
We have successfully received your message and we will be in touch soon.

Saeedeh Designs Team
https://www.saeedehdesigns.com
___________________________________________

{}
email: {}

Your message:
{}

___________________________________________

'''
        message_edited = message_edited.format(name, client_email, message)
        send_mail(mail_subject, message_edited, 'contact@saeedehdesigns.com', recipients)
        pass
