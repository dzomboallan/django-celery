from app2.forms import Review
from django.views.generic.edit import FormView
from django.http import HttpResponse

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = Review

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"

        return HttpResponse(msg)