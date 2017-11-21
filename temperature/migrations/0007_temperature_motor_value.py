from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature','0006_temperature_water_value')
    ]

    operations = [
        migrations.AddField(
            model_name='temperature',
            name='motor_value',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
    ]
