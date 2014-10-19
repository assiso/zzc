#! /usr/bin/env python
# -*- coding: utf-8 -*-

# URLconf
from django.conf.urls import patterns ,url ,include

from adam2014 import views

urlpatterns = patterns("", 
 	url(r'^hello/$',views.helloworld,name='helloworld'),
 	# url(r'^ueditor/',include('DjangoUeditor.urls' )),
 	# url(r'^ueditor/$',views.get_editor,name="geteditor"),
	)


