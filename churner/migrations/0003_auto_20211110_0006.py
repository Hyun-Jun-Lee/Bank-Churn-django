# Generated by Django 3.2.9 on 2021-11-09 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churner', '0002_predresults_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predresults',
            old_name='Contact_cnt_12',
            new_name='Contacts_Count_12_mon',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Customer_age',
            new_name='Customer_Age',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Edu_level',
            new_name='Education_Level',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Month_on_book',
            new_name='Income_Category',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Total_relationship_cnt',
            new_name='Months_on_book',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Total_trant_Amt',
            new_name='Total_Relationship_Count',
        ),
        migrations.RenameField(
            model_name='predresults',
            old_name='Income',
            new_name='Total_Trans_Amt',
        ),
    ]