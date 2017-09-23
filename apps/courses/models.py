# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['course_name']) < 5:
            errors.append("Name field must be 5 characters or more")
        if len(post_data['desc']) < 15:
            errors.append("Description field must be 15 characters or more")
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
