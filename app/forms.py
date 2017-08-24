# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

#from flask.ext.wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
#from flask.ext.wtf import Required

from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, PasswordField, SubmitField, Form, DateTimeField
from wtforms.validators import DataRequired, ValidationError


class ExampleForm(Form):
    title = TextField(u'Título', validators=[DataRequired()])
    content = TextAreaField(u'Conteúdo')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')


# recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
    user = TextField(u'Usuário', validators=[DataRequired()])
    password = PasswordField(u'Senha', validators=[DataRequired()])
