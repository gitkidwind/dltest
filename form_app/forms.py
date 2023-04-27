from django import forms
from .models import Contact ,DanceLessonContact ,DanceWork ,DanceEvent ,DanceEventRegistration ,ChildUser

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'telphone_number', 'email', 'content']
        labels = {
            'first_name': '姓',
            'last_name': '名',
            'telphone_number': '電話番号',
            'email': 'メールアドレス',
            'content': '内容',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

class DanceLessonContactForm(forms.ModelForm):
    class Meta:
        model = DanceLessonContact
        fields = ['name', 'age', 'gender', 'parent_name', 'desired_date', 'desired_class', 'telphone_number', 'email', 'content']
        labels = {
            'name': '体験者名',
            'age': '体験者の年齢',
            'gender': '体験者の性別',
            'parent_name': '保護者名',
            'desired_date': '体験希望日',
            'desired_class': '体験希望クラス',
            'telphone_number': '電話番号',
            'email': 'メールアドレス',
            'content': '内容',
        }
        widgets = {
            'desired_date': forms.DateInput(attrs={'type': 'date'}),
            'telphone_number': forms.TextInput(attrs={'pattern': '[0-9]{11}', 'placeholder': '09012345678'}),
        }

class DanceWorkForm(forms.ModelForm):
    class Meta:
        model = DanceWork
        fields = ('name', 'rehearsal_time', 'rehearsal_cost')



class DanceEventForm(forms.ModelForm):
    class Meta:
        model = DanceEvent
        fields = '__all__'
        labels = {
            'event_title': 'イベント名',
            'event_day': 'イベント日',
            'start_time': '開始時間',
            'place': '会場',
            'address': '住所',
            'ticket_info': 'チケット',
            'entry_fee': '参加費',
            'dance_works': 'ダンス作品',
        }


class DanceEventRegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['child_users'].queryset = ChildUser.objects.filter(parent=self.request.user.pk)
        self.fields['dance_works'].queryset = DanceWork.objects.all()

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request is not None and request.user is not None:
            self.fields['child_users'].queryset = ChildUser.objects.filter(parent=request.user.pk)

    class Meta:
        model = DanceEventRegistration
        fields = ('event', 'child_users', 'dance_works',)
        labels = {
            'event': 'イベント',
        }
        widgets = {
            'child_users': forms.CheckboxSelectMultiple(attrs={'class': 'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300'}),
            'dance_works': forms.CheckboxSelectMultiple(attrs={'class': 'w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300'}),
        }
