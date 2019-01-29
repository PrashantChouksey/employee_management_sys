from .models import Qus

def polls_count(request):
    count = Qus.objects.count()
    return {'polls_count':count}