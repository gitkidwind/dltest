from django.db import models
from django.core.validators import RegexValidator, EmailValidator, MaxLengthValidator , MinValueValidator
from django.utils.translation import gettext_lazy as _
from login_app.models import ChildUser


class DanceWork(models.Model):
    name = models.CharField(max_length=32, verbose_name="作品名")
    rehearsal_time = models.PositiveIntegerField(verbose_name="リハーサル時間（分）", validators=[MinValueValidator(0)])
    rehearsal_cost = models.PositiveIntegerField(verbose_name="リハーサル代（円）", validators=[MinValueValidator(0)])
    class Meta:
        verbose_name = "ダンス作品"
        verbose_name_plural = "ダンス作品"

    def __str__(self):
        return self.name


class DanceEvent(models.Model):
    event_title = models.CharField(max_length=30, verbose_name=_("イベント名"), unique=True)
    event_day = models.DateField(verbose_name=_("イベント日"), blank=True)
    start_time = models.DateTimeField(verbose_name=_("開始時間"))
    place = models.CharField(max_length=30, verbose_name=_("会場"))
    address = models.CharField(max_length=30, verbose_name=_("住所"))
    ticket_info = models.IntegerField(verbose_name=_("チケット"))
    entry_fee = models.IntegerField(verbose_name=_("参加費"))
    dance_works = models.ManyToManyField(DanceWork, verbose_name=_("ダンス作品"), related_name="dance_events")

    class Meta:
        verbose_name = _("ダンスイベント")
        verbose_name_plural = _("ダンスイベント")

    def __str__(self):
        return self.event_title
    

class DanceEventRegistration(models.Model):
    event = models.ForeignKey(DanceEvent, on_delete=models.CASCADE, verbose_name=_("イベント"), related_name='event_registrations')
    child_users = models.ManyToManyField(ChildUser, verbose_name=_("申し込み者"), related_name='child_user_registrations')
    dance_works = models.ManyToManyField(DanceWork, verbose_name=_("ダンス作品"), related_name='dance_work_registrations')

    class Meta:
        verbose_name = _("ダンスイベント申し込み")
        verbose_name_plural = _("ダンスイベント申し込み")

    def __str__(self):
        return f"{', '.join(str(child) for child in self.child_users.all())} - {', '.join(str(work) for work in self.dance_works.all())} ({self.event})"




class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel_number_regex = RegexValidator(
        regex=r'^[0-9]+$',
        message='電話番号は数字のみで入力してください。'
    )
    telphone_number = models.CharField(
        validators=[tel_number_regex],
        max_length=15
    )
    email_validator = EmailValidator(
        message='正しい形式でメールアドレスを入力してください。'
    )
    email = models.EmailField(
        validators=[email_validator],
        max_length=255
    )
    content_validator = MaxLengthValidator(
        limit_value=1000,
        message='内容は1000文字以内で入力してください。'
    )
    content = models.CharField(
        validators=[content_validator],
        max_length=1000
    )

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'お問い合わせ'
        verbose_name_plural = 'お問い合わせ'



class DanceLessonContact(models.Model):
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    name = models.CharField(verbose_name='体験者名', max_length=50)
    age = models.PositiveIntegerField(verbose_name='体験者の年齢')
    GENDER_CHOICES = (
        ('Man', '男'),
        ('Women', '女'),
        ('Not specified', '指定しない')
    )
    gender = models.CharField(verbose_name='体験者の性別', max_length=20, choices=GENDER_CHOICES)
    parent_name = models.CharField(verbose_name='保護者名', max_length=50, blank=True, null=True)
    desired_date = models.DateField(verbose_name='体験希望日')
    CLASS_CHOICES = (
        ('キッズクラス', 'キッズクラス'),
        ('OPENクラス', 'OPENクラス'),
        ('初級クラス', '初級クラス')
    )
    desired_class = models.CharField(verbose_name='体験希望クラス', max_length=20, choices=CLASS_CHOICES)
    tel_number_regex = RegexValidator(
        regex=r'^[0-9]+$',
        message='電話番号は数字のみで入力してください。'
    )
    telphone_number = models.CharField(
        validators=[tel_number_regex],
        max_length=15
    )
    email_validator = EmailValidator(
        message='正しい形式でメールアドレスを入力してください。'
    )
    email = models.EmailField(
        validators=[email_validator],
        max_length=255
    )
    content = models.TextField(verbose_name='内容',blank=True, max_length=1000)

    class Meta:
        verbose_name = '体験レッスンお問い合わせ'
        verbose_name_plural = '体験レッスンお問い合わせ'








