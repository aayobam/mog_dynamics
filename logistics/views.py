from django.urls.base import reverse_lazy
import time
from .models import Logistic
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView
from django.db.models import Q


# end users items tracking
class SearchPageView(TemplateView):
    template_name = "logistics/logistic_page.html"


class SearchResultView(ListView):
    model = Logistic
    template_name = "logistics/logistic_result.html"
    context_object_name = "logistics"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            logistics = Logistic.objects.filter(
                Q(tracking_no__icontains=query)
            )
            return logistics
        return False


# for dispatch riders views and updates

class DispatchRiderSearchView(TemplateView):
    template_name = "logistics/dispatch_search.html"


class DispatchRiderListView(ListView):
    model = Logistic
    template_name = "logistics/dispatch_result.html"
    context_object_name = "logistics"


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            logistics = Logistic.objects.filter(
                Q(tracking_no__icontains=query)
            )
            messages.info(self.request, f"Record Found")
            return logistics
        return False


class DispatchRiderUpdateView(UpdateView):
    template_name = "logistics/dispatch_update.html"
    model = Logistic
    fields = ["status"]
    success_url = reverse_lazy('dispatch_search')

    def form_valid(self, form):
        messages.success(self.request, f"delivery info updated successfully")
        return super().form_valid(form)



def dispatch_login(request):
    template_name = "logistics/dispatch_login.html"
    if request.method == "POST":
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"You are logged in as {user.first_name} {user.last_name} and your activities are been recorded")
            return redirect("dispatch_search")
        else:
            messages.warning(request, f"Invalid user or pass, Try again")
            return redirect("dispatch_login")
    else:
        template_name = "logistics/dispatch_login.html"
    login_form = AuthenticationForm()
    context = {"login_form":login_form}
    return render(request, template_name, context)
    

def dispatch_logout(request):
    logout(request)
    messages.success(request, f"you have been logged out")
    return redirect("dispatch-login")