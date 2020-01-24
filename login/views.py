from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class Login(LoginView):
    template_name = "autch/login.html"
    redirect_authenticated_user = True

    # metods  return  url redirection
    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.is_superuser:
            return reverse("admin:index")
        else:
            return reverse("dashBourdPage")


class Logout(LogoutView):
    template_name = "autch/logout.html"
