from django.forms import ModelForm, CharField, TextInput, ModelChoiceField
from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(max_length=50, required=False, widget=TextInput())
    born_location = CharField(max_length=150, required=False, widget=TextInput())
    description = CharField(required=False, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.fullname

class QuoteForm(ModelForm):
    quote = CharField(max_length=500, required=True, widget=TextInput())
    author = MyModelChoiceField(queryset=Author.objects.all(), required=False, to_field_name="fullname")

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']
