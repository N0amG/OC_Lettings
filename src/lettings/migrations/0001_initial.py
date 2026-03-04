import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunSQL(
                    sql='ALTER TABLE oc_lettings_site_address RENAME TO lettings_address;',
                    reverse_sql='ALTER TABLE lettings_address RENAME TO oc_lettings_site_address;',
                ),
                migrations.RunSQL(
                    sql='ALTER TABLE oc_lettings_site_letting RENAME TO lettings_letting;',
                    reverse_sql='ALTER TABLE lettings_letting RENAME TO oc_lettings_site_letting;',
                ),
            ],
            state_operations=[
                migrations.CreateModel(
                    name='Address',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                        ('street', models.CharField(max_length=64)),
                        ('city', models.CharField(max_length=64)),
                        ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                        ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                        ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                    ],
                    options={
                        'verbose_name_plural': 'addresses',
                    },
                ),
                migrations.CreateModel(
                    name='Letting',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('title', models.CharField(max_length=256)),
                        ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
                    ],
                ),
            ],
        ),
    ]
