superuser
Email:dance@live.com
pass:dancelive

kidlaps
qazwsxedc
1900 380

{% if form.email.errors %}
    <div class="text-red-600">
        {% for error in form.email.errors %}
            <span>{{ error }}</span>
        {% endfor %}
    </div>
{% endif %}
$env:DJANGO_SETTINGS_MODULE = "dancelivepj.settings_dev"
