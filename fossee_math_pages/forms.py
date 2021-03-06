from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm

from .models import (UserDetails, Internship, Topic, Subtopic, Contributor, Data, ImageFormatting, Messages)

INTERN_STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
)

STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
    ("COMPLETED", "COMPLETED"),
)

DATA_STATUS = (
    ("ACCEPTED", "ACCEPTED"),
    ("REJECTED", "REJECTED"),
    ("WAITING", "WAITING"),
    ("UNDER REVIEW", "UNDER REVIEW"),
)


class AddUserForm1(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class AddUserForm2(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_phone', 'user_role', 'user_college']


class EditUserForm1(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class EditUserForm2(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_phone', 'user_college', 'user_bio']


class EditBio(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_bio']


class AddInternship(ModelForm):
    class Meta:
        model = Internship
        fields = ['internship_topic', 'internship_quote', 'internship_quote_author', 'internship_thumbnail',
                  'internship_status']


class ManageInternship(ModelForm):
    class Meta:
        model = Internship
        fields = ['internship_status']


class AproveContents(ModelForm):
    class Meta:
        model = Subtopic
        fields = ['subtopic_status']


class AddContributor(ModelForm):
    class Meta:
        model = Contributor
        fields = ['mentor', 'professor']


class EditMedia(ModelForm):
    class Meta:
        model = Data
        fields = ['data_image', 'data_video', 'data_caption']


class ManageIntern(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_status']


class topicOrder(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_order']


class subtopicOrder(ModelForm):
    class Meta:
        model = Subtopic
        fields = ['subtopic_order']


class data(ModelForm):
    class Meta:
        model = Data
        fields = ['data_content']
        labels = {
            'data_content': "",
        }


class change_image(ModelForm):
    class Meta:
        model = Data
        fields = ['data_image', 'data_caption']  # 'data_video',
        labels = {
            'data_image': "Image",
            # 'data_video': "<br>OR<br><br>Video",
            'data_caption': "<br>Caption",
        }


class change_video(ModelForm):
    class Meta:
        model = Data
        fields = ['data_video', 'data_caption']  # 'data_image',
        labels = {
            'data_video': "Video",
            # 'data_image': "<br>OR<br><br>Image",
            'data_caption': "<br>Caption",
        }


class imageFormatting(ModelForm):
    class Meta:
        model = ImageFormatting
        fields = ['image_height', 'image_width']


class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
    )

    def clean(self):
        user = self.authenticate_via_email()
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

        return user


class add_topic(forms.Form):
    topic = forms.CharField(max_length=255, widget=forms.TextInput())


class add_subtopic(forms.Form):
    subtopic = forms.CharField(max_length=255, widget=forms.TextInput())


class addContributor(ModelForm):
    class Meta:
        model = Contributor
        fields = ['mentor', 'professor']


class sendMessage(ModelForm):
    class Meta:
        model = Messages
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 80, 'placeholder': "Send Message"}),

        }
        fields = ['message']
        labels = {"message": ""}
