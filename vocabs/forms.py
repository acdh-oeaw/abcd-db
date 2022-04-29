from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup

from . models import (
    SkosTechnicalCollection,
    SkosConcept,
    SkosCollection,
)


class SkosConceptForm(forms.ModelForm):

    class Meta:
        model = SkosConcept
        fields = [
            'pref_label',
            'collection',
        ]

    def __init__(self, *args, **kwargs):
        super(SkosConceptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SkosConceptFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkosConceptFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Suche',
                'id',
                'pref_label',
                css_id="basic_search_fields"
            ),
            Accordion(
                AccordionGroup(
                    'erweiterte Suchoptionen',
                    'collection',
                    css_id="more"
                )
            )
        )


class SkosCollectionForm(forms.ModelForm):

    class Meta:
        model = SkosCollection
        fields = [
            'pref_label',
        ]

    def __init__(self, *args, **kwargs):
        super(SkosCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SkosCollectionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkosCollectionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'pref_label',
                css_id="basic_search_fields"
            )
        )


class SkosTechnicalCollectionForm(forms.ModelForm):

    class Meta:
        model = SkosTechnicalCollection
        fields = [
            'pref_label',
        ]

    def __init__(self, *args, **kwargs):
        super(SkosTechnicalCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class SkosTechnicalCollectionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(SkosCollectionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                'pref_label',
                css_id="basic_search_fields"
            )
        )
