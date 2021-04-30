# Generated by Django 3.1.6 on 2021-04-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coaching',
            name='header_heading',
            field=models.CharField(blank=True, max_length=60, verbose_name='Header Überschrift'),
        ),
        migrations.AlterField(
            model_name='coaching',
            name='header_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Header Text'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_address',
            field=models.CharField(blank=True, max_length=50, verbose_name='Adresse Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_emailphone',
            field=models.CharField(blank=True, max_length=50, verbose_name='E-Mail und Telefon Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_heading',
            field=models.CharField(blank=True, max_length=80, verbose_name='Kontakt Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_buttontext',
            field=models.CharField(blank=True, max_length=100, verbose_name='Formular Button Text'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_dataprotectiontext',
            field=models.CharField(blank=True, max_length=200, verbose_name='Formular Datenschutz Text'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_heading',
            field=models.CharField(blank=True, max_length=80, verbose_name='Formular Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_successheading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Formular Abgeschickt Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_successlink',
            field=models.CharField(blank=True, max_length=80, verbose_name='Formular Abgeschickt Linktext'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='form_successtext',
            field=models.CharField(blank=True, max_length=300, verbose_name='Formular Abgeschickt Text'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='header_heading',
            field=models.CharField(blank=True, max_length=60, verbose_name='Header Überschrift'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='header_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Header Text'),
        ),
        migrations.AlterField(
            model_name='general',
            name='address_city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Adresse Stadt'),
        ),
        migrations.AlterField(
            model_name='general',
            name='address_street',
            field=models.CharField(blank=True, max_length=100, verbose_name='Adresse Straße'),
        ),
        migrations.AlterField(
            model_name='general',
            name='company_name',
            field=models.CharField(blank=True, default='CoCoo GmbH', max_length=100, verbose_name='Unternehmensname'),
        ),
        migrations.AlterField(
            model_name='general',
            name='email',
            field=models.CharField(blank=True, max_length=100, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='general',
            name='phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='index',
            name='header_buttonleft',
            field=models.CharField(blank=True, max_length=50, verbose_name='Header Button Links'),
        ),
        migrations.AlterField(
            model_name='index',
            name='header_buttonright',
            field=models.CharField(blank=True, max_length=50, verbose_name='Header Button Rechts'),
        ),
        migrations.AlterField(
            model_name='index',
            name='header_heading',
            field=models.CharField(blank=True, max_length=60, verbose_name='Header Überschrift'),
        ),
        migrations.AlterField(
            model_name='index',
            name='header_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Header Text'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_leftbutton',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Button Links'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_leftheading',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Überschrift Links'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_pretitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Vorüberschrift'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_rightbutton',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Button Rechts'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_rightheading',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Überschrift Rechts'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_subtitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Unterüberschrift'),
        ),
        migrations.AlterField(
            model_name='index',
            name='intro_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Intro Überschrift'),
        ),
        migrations.AlterField(
            model_name='index',
            name='seminars_heading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Seminare Überschrift'),
        ),
        migrations.AlterField(
            model_name='index',
            name='testimonials_heading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Referenzen Überschrift'),
        ),
        migrations.AlterField(
            model_name='member',
            name='content_pretitle',
            field=models.CharField(blank=True, max_length=80, verbose_name='Inhalt Vortitel'),
        ),
        migrations.AlterField(
            model_name='member',
            name='content_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Inhalt Titel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='content_pretitle',
            field=models.CharField(blank=True, max_length=80, verbose_name='Inhalt Vortitel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='content_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Inhalt Titel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Formular Button'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_dataprotection',
            field=models.CharField(blank=True, max_length=200, verbose_name='Formular Datenschutz Text'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_requiredfields',
            field=models.CharField(blank=True, max_length=200, verbose_name='Formular Muss Felder Text'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_successbutton',
            field=models.CharField(blank=True, max_length=80, verbose_name='Formular Erfolg Button'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_successtitle',
            field=models.CharField(blank=True, max_length=80, verbose_name='Formular Erfolg Titel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_text',
            field=models.CharField(blank=True, max_length=140, verbose_name='Formular Text'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='form_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Formular Titel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='infos_subtitle1',
            field=models.CharField(blank=True, max_length=80, verbose_name='Infos Untertitel 1'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='infos_subtitle2',
            field=models.CharField(blank=True, max_length=80, verbose_name='Infos Untertitel 2'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='infos_subtitle3',
            field=models.CharField(blank=True, max_length=80, verbose_name='Infos Untertitel 3'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='infos_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Infos Titel'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='seminars_title',
            field=models.CharField(blank=True, max_length=80, verbose_name='Seminare Titel'),
        ),
        migrations.AlterField(
            model_name='seminars',
            name='header_heading',
            field=models.CharField(blank=True, max_length=60, verbose_name='Header Überschrift'),
        ),
        migrations.AlterField(
            model_name='seminars',
            name='header_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Header Text'),
        ),
        migrations.AlterField(
            model_name='team',
            name='about_heading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Über uns Überschrift'),
        ),
        migrations.AlterField(
            model_name='team',
            name='books_heading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Bücher Überschrift'),
        ),
        migrations.AlterField(
            model_name='team',
            name='books_subheading',
            field=models.CharField(blank=True, max_length=200, verbose_name='Bücher Unterüberschrift'),
        ),
        migrations.AlterField(
            model_name='team',
            name='header_heading',
            field=models.CharField(blank=True, max_length=60, verbose_name='Header Überschrift'),
        ),
        migrations.AlterField(
            model_name='team',
            name='header_text',
            field=models.CharField(blank=True, max_length=200, verbose_name='Header Text'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_heading',
            field=models.CharField(blank=True, max_length=100, verbose_name='Team Überschrift'),
        ),
    ]