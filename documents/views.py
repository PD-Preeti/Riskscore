from django.shortcuts import render
from django.views import View

# Create your views here.
from documents.models import MyUser


class DocumentsVerification(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = MyUser()
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        user.dob = request.POST.get('dob')
        user.gender = request.POST.get('gender')
        user.issuing_authority_name = request.POST.get('authority name')
        user.issuing_authority_state = request.POST.get('authority state')
        user.country = request.POST.get('country')
        user.file = request.POST.get('file-upload')
        user.save()
