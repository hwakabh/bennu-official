from typing import Any
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse

from bennuhp.models.music import Music
from bennuhp.models.movie import Movie
from bennuhp.models.liveschedule import LiveSchedule


class HealthzView(View):
    def get(self, request):
        return JsonResponse(
            data={
                "status": "ok"
            },
            status=200
        )


class AppRootTemplateView(TemplateView):
    template_name = 'bennuhp/home.html'


class BioTemplateView(TemplateView):
    template_name = 'bennuhp/biography.html'


class DiscoListView(ListView):
    model = Music
    context_object_name = 'musics'
    template_name = 'bennuhp/discography.html'

    def get_context_data(self):
        ctx = super().get_context_data()
        # Bind multiple models into single template
        ctx.update({
            'movies': Movie.objects.all()
        })
        return ctx


class LivesListView(ListView):
    # Use `queryset` for reverse sorting, instead of using `model` variables
    queryset = LiveSchedule.objects.order_by('-date')
    context_object_name = 'lives'
    template_name = 'bennuhp/lives.html'



class NotFoundTemplateView(TemplateView):
    template_name = 'bennuhp/common/404_not_found.html'

    # def get(self, request, *args, **kwargs):
    #     ctx = self.get_context_data(**kwargs)
    #     return self.render_to_response(ctx, status=404)


class ServerErrorTemplateView(TemplateView):
    template_name = 'bennuhp/common/500_server_error.html'

    # def get(self, request, *args, **kwargs):
    #     ctx = self.get_context_data(**kwargs)
    #     return self.render_to_response(ctx, status=500)
