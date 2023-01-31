from django.db import models
from django.utils.translation import activate

'''
validation by default
Null = If True, Django will store empty values as NULL in the database. Default is False.

Blank = If True, the field is allowed to be blank. Default is False.
'''
#model.CASCADE -> delete the same value from its children that reference from its parent
# Create your models here.

class Bio(models.Model):
    Nama = models.CharField('Nama',max_length=30)
    Alamat = models.TextField('Alamat', null = True, blank=True)
    No_Ktp = models.CharField('No KTP', max_length=16)

    def __str__(self):
        return self.Nama

class Pendidikan(models.Model):
    Nama = models.ForeignKey(Bio, on_delete = models.CASCADE, null = True, blank = True)
    Sekolah = models.CharField('Nama Sekolah/Universitas', max_length=100)
    Jurusan = models.CharField('Jurusan', max_length=20)
    Masuk = models.IntegerField('Tahun masuk' )
    Keluar = models.IntegerField('Tahun keluar')

    def __str__(self):
        return self.Sekolah

class Pengalaman(models.Model):
    Nama = models.ForeignKey(Bio, on_delete = models.CASCADE, null = True, blank = True)
    Perusahaan = models.CharField('Perusahaan', max_length=100)
    Jabatan = models.CharField('Jabatan', max_length = 20)
    Duration = models.IntegerField('Tahun')
    Keterangan = models.TextField('Keterangan', null=True, blank=True)
    def __str__(self):
        return self.Perusahaan#Menamakan view data ketika berada di database sesuai dengan field yang kita pilih

