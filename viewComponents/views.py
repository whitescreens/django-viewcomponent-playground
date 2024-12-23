
from django.urls import reverse
from django.shortcuts import render, redirect

from django.views import View
from .models import Fruits

class FruitsView(View):
    def get(self, request, *args, **kwargs):
        print("FruitsView get")
        # user = self.request.user
        # organizations = user.get_organizations_im_member()
        fruits = Fruits.objects.all()
        context = {
            "title": "Organizations",
            "fruits": fruits,
        }
        return render(request, "viewComponents/fruits.html", context)