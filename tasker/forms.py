from django import forms as f
from django.forms import widgets as w


class EmailForm(f.Form):
    subject = f.CharField(max_length=256)
    message = f.CharField(widget=w.Textarea)
    from_ = f.EmailField(label='from')
    to = f.EmailField()
