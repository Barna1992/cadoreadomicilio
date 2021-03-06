# Generated by Django 3.0.4 on 2020-04-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locali', '0002_auto_20200331_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComuneConsegna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comune', models.CharField(choices=[('1', 'Auronzo di Cadore (BL)'), ('2', 'Borca di Cadore (BL)'), ('3', 'Calalzo di Cadore (BL)'), ('4', 'Cibiana di Cadore (BL)'), ('5', 'Danta di Cadore (BL)'), ('6', 'Domegge di Cadore (BL)'), ('7', 'Lorenzago di Cadore (BL)'), ('8', 'Lozzo di Cadore (BL)'), ('9', 'Ospitale di Cadore (BL)'), ('10', 'Perarolo di Cadore (BL)'), ('11', 'Pieve di Cadore (BL)'), ('12', 'San Pietro di Cadore (BL)'), ('13', 'San Vito di Cadore (BL)'), ('14', 'Santo Stefano di Cadore (BL)'), ('15', 'Selva di Cadore (BL)'), ('16', 'Valle di Cadore (BL)'), ('17', 'Vigo di Cadore (BL)'), ('18', 'Vodo Cadore (BL)'), ('19', 'Zoppè di Cadore (BL)')], default='1', max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='locale',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='locale',
            name='massima_distanza',
        ),
        migrations.AddField(
            model_name='locale',
            name='consegno_a',
            field=models.ManyToManyField(to='locali.ComuneConsegna'),
        ),
    ]
