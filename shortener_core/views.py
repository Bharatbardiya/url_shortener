# url_app/views.py
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import URL
from .forms import URLSubmitForm, URLLookupForm


class HomeView(TemplateView):
    template_name = 'shortener_core/home.html'
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission

    def get_context_data(self, **kwargs):
        # breakpoint()
        context = super().get_context_data(**kwargs)
        context['submit_form'] = URLSubmitForm()
        context['lookup_form'] = URLLookupForm()
        return context
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        total_tries = 0
        if 'submit_url' in request.POST:
            submit_form = URLSubmitForm(request.POST)
            context['submit_form'] = submit_form
            
            if submit_form.is_valid():
                original_url = submit_form.cleaned_data['url']
                days = submit_form.cleaned_data['expiration_days']
                
                # Set expiration date if specified
                expires_at = None
                if days:
                    expires_at = timezone.now() + timedelta(days=days)
                
                # Generate short code and create URL object
                short_code = URL.generate_short_code(original_url)
                short_code_entry = URL.objects.filter(short_code=short_code).last()
                
                while short_code_entry and total_tries<100:
                    short_code = URL.generate_short_code(original_url)
                    short_code_entry = URL.objects.filter(short_code=short_code).last()
                    total_tries+=1
                
                if total_tries>=100:
                    return Response({"message": "unable to generate short code"}, status = status.HTTP_422_UNPROCESSABLE_ENTITY)
                
                url_obj = URL.objects.create(
                    original_url=original_url,
                    short_code=short_code,
                    expires_at=expires_at
                )
                
                # Generate the full shortened URL
                short_url = request.build_absolute_uri(
                    reverse('redirect_url', args=[short_code])
                )
                context['submit_result'] = {
                    'short_url': short_url,
                    'expires_at': expires_at
                }
        
        elif 'lookup_url' in request.POST:
            lookup_form = URLLookupForm(request.POST)
            context['lookup_form'] = lookup_form
            
            if lookup_form.is_valid():
                short_code = lookup_form.cleaned_data['short_code']
                try:
                    url_obj = URL.objects.get(short_code=short_code)
                    if url_obj.is_expired:
                        context['lookup_result'] = {'error': 'This URL has expired'}
                    else:
                        context['lookup_result'] = {
                            'original_url': url_obj.original_url,
                            'access_count': url_obj.access_count,
                            'expires_at': url_obj.expires_at
                        }
                except URL.DoesNotExist:
                    context['lookup_result'] = {'error': 'URL not found'}
        
        return self.render_to_response(context)

class URLRedirectView(RedirectView):
    permanent = False
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    def get_redirect_url(self, *args, **kwargs):
        # breakpoint()
        short_code = kwargs['short_code']
        url_obj = get_object_or_404(URL, short_code=short_code)
        
        if url_obj.is_expired:
            # Redirect to expired page instead
            return reverse('url_expired')
        
        url_obj.increment_access_count()
        return url_obj.original_url

class URLExpiredView(TemplateView):
    template_name = 'shortener_core/expired.html'