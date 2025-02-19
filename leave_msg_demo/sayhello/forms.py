# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class HelloForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField(u'留言', validators=[DataRequired(), Length(1, 200)])
    # photo = FileField('附件图片', validators=[FileRequired(message=u"未选择文件"),
    #                                           FileAllowed(["jpg", "png"], message=u"文件类型异常")])
    submit = SubmitField()
