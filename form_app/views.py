from django.shortcuts import render ,redirect ,get_object_or_404
from .models import DanceLessonContact ,DanceWork ,DanceEvent ,DanceEventRegistration ,Contact
from .forms import ContactForm ,DanceWorkForm ,DanceLessonContactForm ,DanceEventForm,DanceEventRegistrationForm
from login_app.models import ChildUser
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
import requests
from django.contrib.auth.decorators import login_required

LINE_ACCESS_TOKEN = settings.LINE_ACCESS_TOKEN
LINE_USER_ID = settings.LINE_ID
LINE_MESSAGING_API_URL = settings.LINE_MESSAGING_API_URL



def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['contact_data'] = form.cleaned_data
            return redirect('form_app:contact_confirm_view')
    else:
        form = ContactForm()

    return render(request, 'form_app/contact/contact_form.html', {'form': form})

def contact_confirm_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['contact_data'] = form.cleaned_data
        else:
            return render(request, 'form_app/contact/contact_form.html', {'form': form})
    else:
        contact_data = request.session.get('contact_data')
        if not contact_data:
            return redirect('form_app:contact_view')
        form = ContactForm(initial=contact_data)
    return render(request, 'form_app/contact/contact_confirm.html', {'form': form})
   
def contact_complete_view(request):
    contact_data = request.session.pop('contact_data', None)
    if not contact_data:
        return redirect('form_app:contact_view')

    Contact.objects.create(**contact_data)

    # LINE Messaging APIを使用してフォームの内容をユーザーに送信する
    message = f"お問い合わせがありました。\n名前: {contact_data['last_name']} {contact_data['first_name']}\n電話番号: {contact_data['telphone_number']}\nメールアドレス: {contact_data['email']}\n内容: {contact_data['content']}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }

    data = {
        'to': LINE_USER_ID,
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }

    response = requests.post(LINE_MESSAGING_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        error_message = f"Failed to send message. Error message: {response.text}"
        print(error_message)
        return render(request, 'form_app/contact/contact_complete.html', {'error_message': error_message})

    return render(request, 'form_app/contact/form_complete.html')

def dance_lesson_contact_view(request):
    if request.method == 'POST':
        form = DanceLessonContactForm(request.POST)
        if form.is_valid():
            contact_data = form.cleaned_data
            contact_data['desired_date'] = str(contact_data['desired_date'])
            request.session['contact_data'] = contact_data
            request.session['contact_data'] = form.cleaned_data
            return redirect('form_app:dance_lesson_contact_confirm_view')
    else:
        form = DanceLessonContactForm()
    return render(request, 'form_app/lesson_contact/lesson_contact.html', {'form': form,'gender_choices':DanceLessonContact.GENDER_CHOICES,'class_choices':DanceLessonContact.CLASS_CHOICES})

def dance_lesson_contact_confirm_view(request):
    contact_data = request.session.get('contact_data')
    if not contact_data:
        return redirect('form_app:dance_lesson_contact_view')

    if request.method == 'POST':
        form = DanceLessonContactForm(request.POST, instance=DanceLessonContact(**contact_data))
        if form.is_valid():
            request.session['contact_data'] = form.cleaned_data
            return redirect('form_app:dance_lesson_contact_complete_view')
    else:
        form = DanceLessonContactForm(initial=contact_data)

    return render(request, 'form_app/lesson_contact/lesson_contact_confirm.html', {'form': form})

def dance_lesson_contact_complete_view(request):
    contact_data = request.session.get('contact_data')
    if contact_data:
        contact_data['desired_date'] = datetime.strptime(contact_data['desired_date'], '%Y-%m-%d')


    contact_data = request.session.pop('contact_data', None)
    if not contact_data:
        return redirect('form_app:dance_lesson_contact_view')

    DanceLessonContact.objects.create(**contact_data)


    # LINE Messaging APIを使用してフォームの内容をユーザーに送信する
    desired_date_str = contact_data['desired_date'].strftime('%Y-%m-%d')
    message = f"ダンスの体験レッスンお問い合わせがありました。\n体験者名: {contact_data['name']}\n体験者の年齢: {contact_data['age']}\n体験者の性別: {dict(DanceLessonContact.GENDER_CHOICES)[contact_data['gender']]}\n保護者名: {contact_data['parent_name']}\n体験希望日: {desired_date_str}\n体験希望クラス: {dict(DanceLessonContact.CLASS_CHOICES)[contact_data['desired_class']]}\n電話番号: {contact_data['telphone_number']}\nメールアドレス: {contact_data['email']}\n内容: {contact_data['content']}"


    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_ACCESS_TOKEN}'
    }

    data = {
        'to': LINE_USER_ID,
        'messages': [
            {
                'type': 'text',
                'text': message
            }
        ]
    }

    response = requests.post(LINE_MESSAGING_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        error_message = f"Failed to send message. Error message: {response.text}"
        print(error_message)
        return render(request, 'form_app/lesson_contact/lesson_contact_complete.html', {'error_message': error_message})

    return render(request, 'form_app/lesson_contact/lesson_contact_complete.html')


@login_required
def dancework_list(request):
    danceworks = DanceWork.objects.all()
    return render(request, 'form_app/dancework/dancework_list.html', {'danceworks': danceworks})

@login_required
def dancework_new(request):
    if request.method == 'POST':
        form = DanceWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form_app:dancework_list')
    else:
        form = DanceWorkForm()
    return render(request, 'form_app/dancework/dancework_new.html', {'form': form})

@login_required
def danceevent_list(request):
    danceevents = DanceEvent.objects.all()
    return render(request, 'form_app/danceevent/danceevent_list.html', {'danceevents': danceevents})

@login_required
def danceevent_new(request):
    if request.method == 'POST':
        form = DanceEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danceevent_list')
    else:
        form = DanceEventForm()
    return render(request, 'form_app/danceevent/danceevent_new.html', {'form': form})

@login_required
def register_dance_event(request):
    events = DanceEvent.objects.all()
    dance_works = DanceWork.objects.all()
    user = ChildUser.objects.filter(parent=request.user.pk)
    for num in range(len(dance_works)):
        dance_works[num]
        print(dance_works[num].rehearsal_cost)

    if request.method == 'POST':
        form = DanceEventRegistrationForm(request.POST,request=request)
        if form.is_valid():
            # Get checkbox values
            child_users = request.POST.getlist('child_users')
            dance_works = request.POST.getlist('dance_works')

            registration = form.save(commit=False)

            # Save registration data in session
            request.session['registration_data'] = {
                'event_id': registration.event.pk,
                'child_users': child_users,
                'dance_works': dance_works,
            }

            return redirect('form_app:register_dance_event_confirm')
    else:
        form = DanceEventRegistrationForm(request=request)

    return render(request, 'form_app/danceevent/danceevent_register.html', {'form': form,'events': events,'dance_works':dance_works,'user':user})

@login_required
def edit_dance_event_registration(request, registration_id):
    registration = get_object_or_404(DanceEventRegistration, pk=registration_id)
    
    # 必要な処理

    if request.method == 'POST':
        form = DanceEventRegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            registration = form.save(commit=False)

            # Save registration data in session
            request.session['registration_data'] = {
                'event_id': registration.event.pk,
                'child_users': request.POST.getlist('child_user'),
                'dance_works': request.POST.getlist('dance_work'),
            }

            registration.save()
            return redirect('form_app:register_dance_event_confirm')
    else:
        if request is not None:  # make sure request is not None
            form = DanceEventRegistrationForm(instance=registration, request=request)
        else:
            form = DanceEventRegistrationForm(instance=registration)

    return render(request, 'form_app/danceevent/danceevent_register_edit.html', {'form': form, 'registration': registration})

@login_required
def confirm_dance_event_registration(request):
    registration_data = request.session.get('registration_data')
    if not registration_data:
        return redirect('form_app:register_dance_event')
    
    event = DanceEvent.objects.get(pk=registration_data['event_id'])
    child_users = ChildUser.objects.filter(pk__in=registration_data['child_users'])
    dance_works = DanceWork.objects.filter(pk__in=registration_data['dance_works'])




    return render(request, 'form_app/danceevent/danceevent_register_confirm.html',  {'event': event, 'child_users': child_users, 'dance_works': dance_works ,'registration_data':registration_data})

@login_required
def delete_dance_event_registration(request, registration_id):
    registration = get_object_or_404(DanceEventRegistration, pk=registration_id)

    if request.method == 'POST':
        registration.delete()
        return redirect('form_app:register_dance_event_list')

    return render(request, 'form_app/danceevent/danceevent_register_delete.html', {'registration': registration})

@login_required
def complete_dance_event_registration(request):
    registration_data = request.session.pop('registration_data', None)

    if not registration_data:
        return redirect('form_app:register_dance_event')

    event_id = registration_data['event_id']
    child_users = registration_data['child_users']
    dance_works = registration_data['dance_works']

    event = get_object_or_404(DanceEvent, pk=event_id)

    registration = DanceEventRegistration.objects.create(event=event)

    # ManyToMany フィールドに関する値をセット
    registration.child_users.set(ChildUser.objects.filter(pk__in=child_users))
    registration.dance_works.set(DanceWork.objects.filter(pk__in=dance_works))

    return render(request, 'form_app/danceevent/danceevent_register_complete.html', {'registration': registration})

@login_required
def dance_event_registration_home(request):
    registrations = DanceEventRegistration.objects.filter(child_users=request.user.pk).distinct()
    return render(request, 'form_app/danceevent/danceevent_register_home.html', {'registrations': registrations})