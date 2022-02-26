# generated by appcreator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView


from . filters import (
    EventListFilter,
    WorkListFilter,
    PersonListFilter,
    PlaceListFilter,
    InstitutionListFilter
)
from . forms import (
    EventForm, EventFilterFormHelper,
    WorkForm, WorkFilterFormHelper,
    PersonForm, PersonFilterFormHelper,
    PlaceForm, PlaceFilterFormHelper,
    InstitutionForm, InstitutionFilterFormHelper
)
from . tables import (
    EventTable,
    WorkTable,
    PersonTable,
    PlaceTable,
    InstitutionTable
)
from . models import (
    Event,
    Work,
    Person,
    Place,
    Institution
)
from browsing.browsing_utils import (
    GenericListView, BaseCreateView, BaseUpdateView, BaseDetailView
)


class PersonListView(GenericListView):

    model = Person
    filter_class = PersonListFilter
    formhelper_class = PersonFilterFormHelper
    table_class = PersonTable
    init_columns = [
        'id', 'title',
    ]
    enable_merge = True


class PersonDetailView(BaseDetailView):

    model = Person
    template_name = 'browsing/generic_detail.html'


class PersonCreate(BaseCreateView):

    model = Person
    form_class = PersonForm
    template_name = 'archiv/person_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonCreate, self).dispatch(*args, **kwargs)


class PersonUpdate(BaseUpdateView):

    model = Person
    form_class = PersonForm
    template_name = 'archiv/person_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonUpdate, self).dispatch(*args, **kwargs)


class PersonDelete(DeleteView):
    model = Person
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:person_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PersonDelete, self).dispatch(*args, **kwargs)


class PlaceListView(GenericListView):

    model = Place
    filter_class = PlaceListFilter
    formhelper_class = PlaceFilterFormHelper
    table_class = PlaceTable
    init_columns = [
        'id', 'title',
    ]
    enable_merge = True


class PlaceDetailView(BaseDetailView):

    model = Place
    template_name = 'browsing/generic_detail.html'


class PlaceCreate(BaseCreateView):

    model = Place
    form_class = PlaceForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceCreate, self).dispatch(*args, **kwargs)


class PlaceUpdate(BaseUpdateView):

    model = Place
    form_class = PlaceForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceUpdate, self).dispatch(*args, **kwargs)


class PlaceDelete(DeleteView):
    model = Place
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:place_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PlaceDelete, self).dispatch(*args, **kwargs)


class InstitutionListView(GenericListView):

    model = Institution
    filter_class = InstitutionListFilter
    formhelper_class = InstitutionFilterFormHelper
    table_class = InstitutionTable
    init_columns = [
        'id', 'title',
    ]
    enable_merge = True


class InstitutionDetailView(BaseDetailView):

    model = Institution
    template_name = 'browsing/generic_detail.html'


class InstitutionCreate(BaseCreateView):

    model = Institution
    form_class = InstitutionForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionCreate, self).dispatch(*args, **kwargs)


class InstitutionUpdate(BaseUpdateView):

    model = Institution
    form_class = InstitutionForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionUpdate, self).dispatch(*args, **kwargs)


class InstitutionDelete(DeleteView):
    model = Institution
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:institution_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(InstitutionDelete, self).dispatch(*args, **kwargs)


class EventListView(GenericListView):

    model = Event
    filter_class = EventListFilter
    formhelper_class = EventFilterFormHelper
    table_class = EventTable
    init_columns = [
        'id', 'main_text'
    ]
    enable_merge = False


class EventDetailView(BaseDetailView):

    model = Event
    template_name = 'browsing/generic_detail.html'


class EventCreate(BaseCreateView):

    model = Event
    form_class = EventForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventCreate, self).dispatch(*args, **kwargs)


class EventUpdate(BaseUpdateView):

    model = Event
    form_class = EventForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventUpdate, self).dispatch(*args, **kwargs)


class EventDelete(DeleteView):
    model = Event
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:event_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EventDelete, self).dispatch(*args, **kwargs)


class WorkListView(GenericListView):

    model = Work
    filter_class = WorkListFilter
    formhelper_class = WorkFilterFormHelper
    table_class = WorkTable
    init_columns = [
        'id', 'author_name', 'order_code',
    ]
    enable_merge = False


class WorkDetailView(BaseDetailView):

    model = Work
    template_name = 'browsing/generic_detail.html'


class WorkCreate(BaseCreateView):

    model = Work
    form_class = WorkForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkCreate, self).dispatch(*args, **kwargs)


class WorkUpdate(BaseUpdateView):

    model = Work
    form_class = WorkForm
    template_name = 'browsing/generic_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkUpdate, self).dispatch(*args, **kwargs)


class WorkDelete(DeleteView):
    model = Work
    template_name = 'webpage/confirm_delete.html'
    success_url = reverse_lazy('archiv:work_browse')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WorkDelete, self).dispatch(*args, **kwargs)
