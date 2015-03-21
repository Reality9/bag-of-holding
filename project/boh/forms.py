from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from boh.models import Organization, DataElement, Application, Environment, EnvironmentLocation, Engagement, EngagementComment, Activity, ActivityComment, Person, ThreadFix


# User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# Organization

class OrganizationAddForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class OrganizationSettingsGeneralForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class OrganizationDeleteForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = []


# ThreadFix

class ThreadFixForm(forms.ModelForm):
    class Meta:
        model = ThreadFix
        fields = ['name', 'host', 'api_key']
        widgets = {
            'api_key': forms.PasswordInput(render_value = True)
        }


class ThreadFixDeleteForm(forms.ModelForm):
    class Meta:
        model = ThreadFix
        fields = []


# Application

class ApplicationAddForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['organization', 'name', 'description']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class ApplicationSettingsGeneralForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class ApplicationSettingsOrganizationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['organization']


class ApplicationSettingsMetadataForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['platform', 'lifecycle', 'origin', 'business_criticality', 'user_records', 'revenue', 'external_audience', 'internet_accessible']


class ApplicationSettingsTagsForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['tags']


class ApplicationSettingsDataElementsForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['data_elements']
        widgets = {
            'data_elements': forms.SelectMultiple(attrs = {'size': 15})
        }


class ApplicationSettingsDCLOverrideForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['override_dcl', 'override_reason']
        labels = {
            'override_dcl': 'Override data classification level'
        }
        widgets = {
            'override_reason': forms.Textarea(attrs = {'rows': 3})
        }


class ApplicationSettingsThreadFixForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['threadfix', 'threadfix_organization_id', 'threadfix_application_id']
        labels = {
            'threadfix': 'Server',
            'threadfix_organization_id': 'Organization identifier',
            'threadfix_application_id': 'Application identifier'
        }


class ApplicationDeleteForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []


# Environment

class EnvironmentAddForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['environment_type', 'description', 'testing_approved']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class EnvironmentEditForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['environment_type', 'description', 'testing_approved']
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class EnvironmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = []


class EnvironmentLocationAddForm(forms.ModelForm):
    class Meta:
        model = EnvironmentLocation
        fields = ['location', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs = {'rows': 3})
        }


class EnvironmentLocationEditForm(forms.ModelForm):
    class Meta:
        model = EnvironmentLocation
        fields = ['location', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs = {'rows': 3})
        }


# Engagement

class EngagementAddForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = ['start_date', 'end_date', 'description', 'requestor']
        labels = {
            'start_date': 'Scheduled start date',
            'end_date': 'Scheduled end date'
        }
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }

    def clean(self):
        cleaned = super(EngagementAddForm, self).clean()
        start_date = cleaned.get('start_date')
        end_date = cleaned.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                self.add_error('end_date', "End date cannot be before start date.")


class EngagementEditForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = ['status', 'start_date', 'end_date', 'description', 'requestor']
        labels = {
            'start_date': 'Scheduled start date',
            'end_date': 'Scheduled end date'
        }
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }

    def clean(self):
        cleaned = super(EngagementEditForm, self).clean()
        start_date = cleaned.get('start_date')
        end_date = cleaned.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                self.add_error('end_date', "End date cannot be before start date.")


class EngagementStatusForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = ['status']


class EngagementDeleteForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = []


class EngagementCommentAddForm(forms.ModelForm):
    class Meta:
        model = EngagementComment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs = {'rows': 3})
        }


# Activity

class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'description', 'users']
        labels = {
            'users': 'Assigned users'
        }
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['status', 'activity_type', 'description', 'users']
        labels = {
            'users': 'Assigned users'
        }
        widgets = {
            'description': forms.Textarea(attrs = {'rows': 3})
        }


class ActivityStatusForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['status']


class ActivityCommentAddForm(forms.ModelForm):
    class Meta:
        model = ActivityComment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs = {'rows': 3})
        }


class ActivityDeleteForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = []


# Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone_work', 'phone_mobile', 'job_title', 'role']


class PersonDeleteForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = []
