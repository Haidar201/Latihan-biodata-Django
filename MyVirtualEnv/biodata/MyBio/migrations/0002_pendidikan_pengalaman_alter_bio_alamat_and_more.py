# Generated by Django 4.1.5 on 2023-01-24 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyBio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendidikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sekolah', models.CharField(max_length=100, verbose_name='Nama Sekolah/Universitas')),
                ('Jurusan', models.CharField(max_length=20, verbose_name='Jurusan')),
                ('Masuk', models.IntegerField(verbose_name='Tahun masuk')),
                ('Keluar', models.IntegerField(verbose_name='Tahun keluar')),
            ],
        ),
        migrations.CreateModel(
            name='Pengalaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Perusahaan', models.CharField(max_length=100, verbose_name='Perusahaan')),
                ('Jabatan', models.CharField(max_length=20, verbose_name='Jabatan')),
                ('Duration', models.IntegerField(verbose_name='Tahun')),
                ('Keterangan', models.TextField(blank=True, null=True, verbose_name='Keterangan')),
            ],
        ),
        migrations.AlterField(
            model_name='bio',
            name='Alamat',
            field=models.TextField(blank=True, null=True, verbose_name='Alamat'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='Nama',
            field=models.CharField(max_length=30, verbose_name='Nama'),
        ),
        migrations.AlterField(
            model_name='bio',
            name='No_Ktp',
            field=models.CharField(max_length=16, verbose_name='No KTP'),
        ),
        migrations.AddField(
            model_name='bio',
            name='Pendidikan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyBio.pendidikan'),
        ),
        migrations.AddField(
            model_name='bio',
            name='Pengalaman_Kerja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyBio.pengalaman'),
        ),
    ]
