#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Tipodocente

class TipodocenteForm(ModelForm):
	class Meta:
		model = Tipodocente
			
		