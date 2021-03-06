# Generated by Django 3.2.4 on 2021-09-24 10:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=200)),
                ('employment_status', models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Freelance', 'Freelance')], max_length=10)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30, null=True)),
                ('category', models.CharField(choices=[('Accountancy', 'Accountancy'), ('Bar && Restaurant', 'Bar && Restaurant'), ('Agriculture', 'Agriculture'), ('Banking && Finance', 'Banking && Finance'), ('Education', 'Education'), ('Engineering', 'Engineering'), ('Graphic Design', 'Graphic Design'), ('Health', 'Health'), ('Hospitality', 'Hospitality'), ('HR', 'HR'), ('Human Resource', 'IT && Telecoms'), ('Legal', 'Legal'), ('Manufacturing', 'Manufacturing'), ('Marketing', 'Marketing'), ('Public Office', 'Public Office'), ('Public Relations', 'Public Relations'), ('Retail && Sales', 'Retail && Sales'), ('Software Engineering', 'Software Engineering'), ('Transport && Logistics', 'Transport && Logistics'), ('Web Design', 'Web Design'), ('Web Developing', 'Web Developing')], max_length=30)),
                ('description', models.TextField()),
                ('responsibilities', models.TextField()),
                ('experience', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=120)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logos')),
                ('Salary', models.CharField(blank=True, max_length=100, null=True)),
                ('application_deadline', models.DateTimeField()),
                ('published_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
