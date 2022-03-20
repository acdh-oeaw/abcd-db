# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup
from dal import autocomplete
from gnd.forms import GndModelForm

from . models import (
    Event,
    Work,
    Person,
    Place,
    Institution,
    Wab
)


class InstitutionForm(forms.ModelForm):

    class Meta:
        model = Institution
        fields = [
            'title',
        ]

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class InstitutionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InstitutionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'title',
                    css_id="more"
                )
            )
        )


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = [
            'title',
        ]

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PlaceFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PlaceFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'title',
                    css_id="more"
                )
            )
        )


class PersonForm(GndModelForm):

    class Meta:
        model = Person
        fields = [
            'title',
            'gnd_gnd_id',
            'gnd_pref_name'
        ]

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class PersonFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PersonFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'title',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'gnd_gnd_id',
                    'ablo_uri',
                    'oeml_uri',
                    'bruckner_entity',
                    css_id="more"
                )
            )
        )


class EventFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(EventFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Volltext und Werke',
                    'main_text',
                    'wab',
                    css_id="basic_search_fields"
                )
            ),
            Accordion(
                AccordionGroup(
                    'Personen, Orte, Institutionen',
                    'person',
                    'place',
                    'institution',
                    css_id="entities"
                ),
                AccordionGroup(
                    'weitere Suchoptionen',
                    'work',
                    'date_written',
                    'not_before',
                    'not_after',
                    'notes_lit',
                    'notes_img',
                    'notes_facs',
                    'notes_archive',
                    'notes_text',
                    'key_word',
                    'note',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    'id',
                    css_id="admin_search"
                ),
            )
        )


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = [
            'legacy_id',
            'orig_data_csv',
            'full_text'
        ]
        widgets = {
            'work': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:work-autocomplete'
            ),
            'person': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:person-autocomplete'
            ),
            'place': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:place-autocomplete'
            ),
            'institution': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:institution-autocomplete'
            ),
            'wab': autocomplete.ModelSelect2Multiple(
                url='archiv-ac:wab-autocomplete'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class WorkFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WorkFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'order_code',
                    'author_name',
                    'full_quote',
                    css_id="more"
                ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                ),
            )
        )


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class WabForm(forms.ModelForm):

    class Meta:
        model = Wab
        exclude = [
            'wab_xml',
        ]

    def __init__(self, *args, **kwargs):
        super(WabForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class WabFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(WabFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    'title',
                    css_id="more"
                )
            )
        )
