from django import forms
from django.contrib.auth.models import User
from ..models import CustomUser, Case, Review, ChatMessage
from django.forms import ModelForm
import os
import uuid

class CustomUserForm(forms.ModelForm):
    # Fields for the CustomUser model
    user_type = forms.ChoiceField(choices=CustomUser.USER_TYPES)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    specialization = forms.CharField(max_length=100, required=False)
    location = forms.CharField(max_length=100, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)

        # Save the User model first
        if commit:
            user.save()

        # Now, update the CustomUser model
        custom_user, created = CustomUser.objects.get_or_create(user=user)
        custom_user.user_type = self.cleaned_data['user_type']
        custom_user.bio = self.cleaned_data['bio']
        custom_user.specialization = self.cleaned_data['specialization']
        custom_user.location = self.cleaned_data['location']

        if self.cleaned_data['image']:
            if custom_user.image.name != 'account.png':
                # Delete the old image
                if os.path.isfile(custom_user.image.path):
                    os.remove(custom_user.image.path)

            # Generate a UUID-based filename for the new image
            image_extension = os.path.splitext(self.cleaned_data['image'].name)[1]
            image_filename = f"{uuid.uuid4()}{image_extension}"
            custom_user.image.save(image_filename, self.cleaned_data['image'])

        if commit:
            custom_user.save()

        return user



class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_detail']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_score', 'review_detail']


class LawyerSearchForm(forms.Form):
    specialization = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type='Lawyer').values_list('specialization', flat=True).distinct(),
        required=False,
        empty_label="Select specialization"
    )
    location = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(user_type='Lawyer').values_list('location', flat=True).distinct(),
        required=False,
        empty_label="Select location"
    )



class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "Type message here"}))
    class Meta:
        model = ChatMessage
        fields = ["body",]



class UpdateCaseStatusForm(forms.Form):
    STATUS_CHOICES = (
        ('change_status', 'Change The Case Status...'),
        ('waiting_for_approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    new_status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))
