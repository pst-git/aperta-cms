#coding=utf-8

from django.db.models import Model, EmailField, DateField, IntegerField, CharField, ForeignKey
from django.contrib.auth.models import User

class Member(Model):
  ACT = 0
  HON = 1
  WBE = 2
  STB = 3
  STATUSES = (
    (ACT, 'actif'),
    (HON, 'honoraire'),
    (WBE, 'aspirant (wouldbe)'),
    (STB, 'inactif (standby)'),
  )

  first_name    = CharField(verbose_name=u'Prénom',max_length=100)
  last_name	= CharField(verbose_name=u'Nom',max_length=100)
  email		= EmailField()
  start_date    = DateField(verbose_name=u'Date de début')
  end_date      = DateField(verbose_name=u'Date de fin',blank=True,null=True) 
  status      	= IntegerField(verbose_name=u'Statut',choices=STATUSES,default=ACT) 
  user		= ForeignKey(User,verbose_name=u'Utilisateur',blank=True,null=True) 

  def __unicode__(self):
    return unicode(self.first_name) + ' ' + unicode.upper(self.last_name)

class Role(Model):
  title		= CharField(verbose_name=u'Titre',max_length=100)
  desc		= CharField(verbose_name=u'Description',max_length=500,blank=True,null=True)
  member      	= ForeignKey(Member) 
  start_date    = DateField(verbose_name=u'Date de début',)
  end_date      = DateField(verbose_name=u'Date de fin',blank=True,null=True) 

  def __unicode__(self):
    return self.title + ' : ' + unicode(self.member)

  class Meta:
    unique_together = ( 'member', 'title', )
