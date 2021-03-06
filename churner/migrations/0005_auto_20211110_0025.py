# Generated by Django 3.2.9 on 2021-11-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churner', '0004_auto_20211110_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='Contacts_Count_12_mon',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Customer_Age',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Dependent_count',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Education_Level',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Gender',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Income_Category',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Months_on_book',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Total_Relationship_Count',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='Total_Trans_Amt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresults',
            name='result',
            field=models.FloatField(),
        ),
    ]
