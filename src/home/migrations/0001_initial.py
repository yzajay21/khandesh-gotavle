# Generated by Django 2.1.2 on 2018-10-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=64)),
                ('middle_name', models.CharField(db_index=True, max_length=64)),
                ('last_name', models.CharField(db_index=True, max_length=64)),
                ('mobile_no', models.CharField(db_index=True, max_length=64)),
                ('description', models.TextField(max_length=200)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('pan', models.CharField(blank=True, max_length=200, null=True)),
                ('aadhar', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('permanent_address', models.TextField()),
                ('name_of_relative', models.CharField(max_length=200)),
                ('mobile_no_of_relative', models.CharField(max_length=13)),
                ('emergency_contact', models.CharField(max_length=13)),
                ('blood_group', models.CharField(max_length=10)),
                ('Profession', models.CharField(choices=[('Job', 'job'), ('Buisness', 'buisness')], max_length=10)),
            ],
        ),
    ]
