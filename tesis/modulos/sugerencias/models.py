# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Sugerencias(models.Model): 
    Usuario = models.ForeignKey(User)
    Sugerencias = models.TextField(blank=True)

    def __unicode__(self):
        return '%s, coloco:  %s' %( self.Usuario, self.Sugerencias)
    