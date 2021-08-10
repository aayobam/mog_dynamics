from django.urls.base import reverse_lazy
from django.contrib.auth.models import User
from .models import Logistic
from .forms import LogisticForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class DispatchRiderSearchView(LoginRequiredMixin,TemplateView):
    login_url = 'dispatch_login'
    redirect_field_name = 'dispatch_search'
    template_name = "logistics/dispatch_search.html"


class DispatchRiderListView(LoginRequiredMixin, ListView):
    login_url = 'dispatch_login'
    redirect_field_name = 'dispatch_result'
    model = Logistic
    template_name = "logistics/dispatch_result.html"
    context_object_name = "logistics"


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            logistics = Logistic.objects.filter(
                Q(tracking_no__icontains=query)
            )
            return logistics
        return False


class DispatchRiderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'dispatch_login'
    redirect_field_name = 'dispatch_result'
    template_name = "logistics/dispatch_update.html"
    form_class = LogisticForm
    success_url = reverse_lazy('dispatch_search')
    
    def get_queryset(self):
        logistic = Logistic.objects.all()
        return logistic
    

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        messages.success(self.request, f"Delivery info updated successfully")
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
    return redirect("dispatch_login")