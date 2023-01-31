from django import forms

from .models import Bio,Pendidikan,Pengalaman


class Bio_form(forms.ModelForm):
    class Meta:
        model = Bio
        fields = [
            'Nama',
            'Alamat',
            'No_Ktp', 
        ]

class Edu_form(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = [
            'Nama',
            'Sekolah',
            'Jurusan',
            'Masuk',
            'Keluar'  
        ]

class Exp_form(forms.ModelForm):
    class Meta:
        model = Pengalaman
        fields = [
            'Nama',
            'Perusahaan',
            'Jabatan',
            'Duration',
            'Keterangan'  
        ]