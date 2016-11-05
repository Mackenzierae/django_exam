from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt
import dateutil
from dateutil import parser

class UserManager(models.Manager):
    def validate_user_info(self, post, date_hired):
        errors = []

        if len(post['name']) == 0:
            errors.append('Name cannot be blank!')
        if len(post['username']) == 0:
            errors.append('Username cannot be blank!')
        if len(post['name']) < 3:
            errors.append('Name must contain at least 3 characters!')
        if len(post['username']) < 3:
            errors.append('Username must contain at least 3 characters!')

        if len(post['password']) < 8:
            errors.append('Your password must contain at least 8 characters!')
        if post['password'] != post['confpass']:
            errors.append('Your confirmation password must match your password!')

        if len(date_hired)==0:
            errors.append("Please enter your date-of-hire")
        else:
            try:
                hired = datetime.datetime.strptime(date_hired, '%Y-%m-%d')
                if hired.date() > datetime.date.today():
                    errors.append("Your date-of-hire cannot be in the future")
            except:
                errors.append("Please enter a valid date-of-hire")

        return errors

    def login(self, post):
        user_list = User.objects.filter(username=post['username'])
        if user_list:
            user = user_list[0]
            if bcrypt.hashpw(post['password'].encode(), user.password.encode()) == user.password:
                return user
        return None

    def register(self, post):
        encrypted_password = bcrypt.hashpw(post['password'].encode(), bcrypt.gensalt())
        User.objects.create(name=post['name'], username=post['username'], password=encrypted_password, date_hired=post['date_hired'])

class WishManager(models.Manager):
    def validate_wish(self, post):
        errors = []

        if len(post['item']) == 0:
            errors.append('Item/Product cannot be empty!')
        if len(post['item']) < 4:
            errors.append('Item/Product must contain more than 3 characters')

        return errors

class User(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Wish(models.Model):
    wish_creator = models.ForeignKey(User)
    item = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishManager()

class Added(models.Model):
    wish_adder = models.ForeignKey(User)
    wish = models.ForeignKey(Wish)
