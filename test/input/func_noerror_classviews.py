"""
Checks that Pylint does not complain about attributes and methods
when using Class-based Views
"""
#  pylint: disable=C0111,R0903,W0232

from django.views.generic import TemplateView


class BoringView(TemplateView):
    # ensure that args, kwargs and request are not thrown up as errors
    def get_context_data(self, **kwargs):
        return {
            'request': self.request,
            'args': self.args,
            'kwargs': self.kwargs
        }
