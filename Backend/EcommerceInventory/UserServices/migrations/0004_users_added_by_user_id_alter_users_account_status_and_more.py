# Generated by Django 5.0.6 on 2024-07-30 08:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserServices', '0003_alter_modules_module_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='added_by_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='users',
            name='account_status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Blocked', 'Blocked')], default='Active', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='country',
            field=models.CharField(blank=True, choices=[('India', 'India'), ('USA', 'USA'), ('UK', 'UK'), ('Australia', 'Australia'), ('Canada', 'Canada'), ('Germany', 'Germany'), ('France', 'France'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('China', 'China'), ('Russia', 'Russia'), ('Brazil', 'Brazil'), ('South Africa', 'South Africa'), ('Nigeria', 'Nigeria'), ('Mexico', 'Mexico'), ('Argentina', 'Argentina'), ('Spain', 'Spain'), ('Portugal', 'Portugal'), ('Greece', 'Greece'), ('Sweden', 'Sweden'), ('Norway', 'Norway'), ('Finland', 'Finland'), ('Denmark', 'Denmark'), ('Netherlands', 'Netherlands'), ('Belgium', 'Belgium'), ('Switzerland', 'Switzerland'), ('Austria', 'Austria'), ('Poland', 'Poland'), ('Czech Republic', 'Czech Republic'), ('Turkey', 'Turkey'), ('Ukraine', 'Ukraine'), ('Hungary', 'Hungary'), ('Romania', 'Romania'), ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'), ('Slovenia', 'Slovenia'), ('Slovakia', 'Slovakia'), ('Lithuania', 'Lithuania'), ('Latvia', 'Latvia'), ('Estonia', 'Estonia'), ('Ireland', 'Ireland'), ('Scotland', 'Scotland'), ('Wales', 'Wales'), ('Northern Ireland', 'Northern Ireland'), ('New Zealand', 'New Zealand'), ('Singapore', 'Singapore'), ('Malaysia', 'Malaysia'), ('Thailand', 'Thailand'), ('Indonesia', 'Indonesia'), ('Philippines', 'Philippines'), ('Vietnam', 'Vietnam'), ('South Korea', 'South Korea'), ('North Korea', 'North Korea'), ('Taiwan', 'Taiwan'), ('Hong Kong', 'Hong Kong'), ('Macau', 'Macau'), ('Bangladesh', 'Bangladesh'), ('Pakistan', 'Pakistan'), ('Sri Lanka', 'Sri Lanka'), ('Nepal', 'Nepal'), ('Bhutan', 'Bhutan'), ('Maldives', 'Maldives'), ('Afghanistan', 'Afghanistan'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Syria', 'Syria'), ('Lebanon', 'Lebanon')], default='India', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='currency',
            field=models.CharField(blank=True, choices=[('USD', 'USD'), ('INR', 'INR'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('AUD', 'AUD'), ('CAD', 'CAD'), ('JPY', 'JPY'), ('CNY', 'CNY'), ('RUB', 'RUB'), ('BRL', 'BRL'), ('ZAR', 'ZAR'), ('NGN', 'NGN'), ('MXN', 'MXN'), ('ARS', 'ARS'), ('CHF', 'CHF'), ('SEK', 'SEK'), ('NOK', 'NOK'), ('DKK', 'DKK'), ('PLN', 'PLN'), ('CZK', 'CZK'), ('TRY', 'TRY'), ('UAH', 'UAH'), ('HUF', 'HUF'), ('RON', 'RON'), ('BGN', 'BGN'), ('HRK', 'HRK'), ('SLO', 'SLO'), ('SK', 'SK'), ('LT', 'LT'), ('LV', 'LV'), ('EE', 'EE'), ('IE', 'IE'), ('SC', 'SC'), ('WL', 'WL'), ('NI', 'NI'), ('NZ', 'NZ'), ('SGD', 'SGD'), ('MYR', 'MYR'), ('THB', 'THB'), ('IDR', 'IDR'), ('PHP', 'PHP'), ('VND', 'VND'), ('KRW', 'KRW'), ('KPW', 'KPW'), ('TWD', 'TWD'), ('HKD', 'HKD'), ('MOP', 'MOP'), ('BDT', 'BDT'), ('PKR', 'PKR'), ('LKR', 'LKR'), ('NPR', 'NPR'), ('BTN', 'BTN'), ('MVR', 'MVR'), ('AFN', 'AFN'), ('IRR', 'IRR'), ('IQD', 'IQD'), ('SYP', 'SYP'), ('LBN', 'LBN')], default='INR', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Hindi', 'Hindi'), ('Spanish', 'Spanish'), ('French', 'French'), ('German', 'German'), ('Italian', 'Italian'), ('Portuguese', 'Portuguese'), ('Russian', 'Russian'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Arabic', 'Arabic'), ('Turkish', 'Turkish'), ('Dutch', 'Dutch'), ('Polish', 'Polish'), ('Swedish', 'Swedish'), ('Danish', 'Danish'), ('Norwegian', 'Norwegian'), ('Finnish', 'Finnish'), ('Greek', 'Greek'), ('Czech', 'Czech'), ('Hungarian', 'Hungarian'), ('Romanian', 'Romanian'), ('Bulgarian', 'Bulgarian'), ('Croatian', 'Croatian'), ('Slovak', 'Slovak'), ('Slovenian', 'Slovenian'), ('Lithuanian', 'Lithuanian'), ('Latvian', 'Latvian'), ('Estonian', 'Estonian'), ('Ukrainian', 'Ukrainian'), ('Belarusian', 'Belarusian'), ('Serbian', 'Serbian'), ('Macedonian', 'Macedonian'), ('Bosnian', 'Bosnian'), ('Albanian', 'Albanian'), ('Montenegrin', 'Montenegrin'), ('Catalan', 'Catalan'), ('Basque', 'Basque'), ('Galician', 'Galician'), ('Welsh', 'Welsh'), ('Irish', 'Irish'), ('Scots Gaelic', 'Scots Gaelic'), ('Manx', 'Manx'), ('Cornish', 'Cornish'), ('Breton', 'Breton')], default='English', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='plan_type',
            field=models.CharField(blank=True, choices=[('Free', 'Free'), ('Basic', 'Basic'), ('Standard', 'Standard'), ('Premium', 'Premium'), ('Enterprise', 'Enterprise')], default='Free', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Staff', 'Staff')], default='Admin', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='time_zone',
            field=models.CharField(blank=True, choices=[('UTC-12:00', 'UTC-12:00'), ('UTC-11:00', 'UTC-11:00'), ('UTC-10:00', 'UTC-10:00'), ('UTC-09:30', 'UTC-09:30'), ('UTC-09:00', 'UTC-09:00'), ('UTC-08:00', 'UTC-08:00'), ('UTC-07:00', 'UTC-07:00'), ('UTC-06:00', 'UTC-06:00'), ('UTC-05:00', 'UTC-05:00'), ('UTC-04:00', 'UTC-04:00'), ('UTC-03:30', 'UTC-03:30'), ('UTC-03:00', 'UTC-03:00'), ('UTC-02:00', 'UTC-02:00'), ('UTC-01:00', 'UTC-01:00'), ('UTC', 'UTC'), ('UTC+01:00', 'UTC+01:00'), ('UTC+02:00', 'UTC+02:00'), ('UTC+03:00', 'UTC+03:00'), ('UTC+03:30', 'UTC+03:30'), ('UTC+04:00', 'UTC+04:00'), ('UTC+04:30', 'UTC+04:30'), ('UTC+05:00', 'UTC+05:00'), ('UTC+05:30', 'UTC+05:30'), ('UTC+05:45', 'UTC+05:45'), ('UTC+06:00', 'UTC+06:00'), ('UTC+06:30', 'UTC+06:30'), ('UTC+07:00', 'UTC+07:00'), ('UTC+08:00', 'UTC+08:00'), ('UTC+08:45', 'UTC+08:45'), ('UTC+09:00', 'UTC+09:00'), ('UTC+09:30', 'UTC+09:30'), ('UTC+10:00', 'UTC+10:00'), ('UTC+10:30', 'UTC+10:30'), ('UTC+11:00', 'UTC+11:00'), ('UTC+12:00', 'UTC+12:00'), ('UTC+12:45', 'UTC+12:45'), ('UTC+13:00', 'UTC+13:00'), ('UTC+14:00', 'UTC+14:00')], default='UTC+05:30', max_length=50, null=True),
        ),
    ]
