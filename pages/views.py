from django.shortcuts import render

from django.core.mail import send_mail


# Create your views here.
def form(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        tel = request.POST.get('ftel')
        message = ('Имя: ' + str(name) + '\nТелефон: ' + str(tel))
        # send_mail(
        #     'Заявка на запись',
        #     message,
        #     'from@mail.com',
        #     ['to@gmail.com'],
        #     # fail_silently=False,
        # )

    return render(request, 'pages/index.html', locals())
