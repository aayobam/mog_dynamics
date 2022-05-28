from django import forms
from .models import Logistic




class LogisticForm(forms.ModelForm):

    class Meta:
        model = Logistic
        fields = '__all__'
        exclude = ["updated_by", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled=True
            self.fields["status"].disabled=False
        