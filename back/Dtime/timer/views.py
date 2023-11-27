from django.shortcuts import render
from django.http import JsonResponse
from .models import User, User_Data, Timer_Ssesion
from django.views.decorators.csrf import csrf_exempt
from timer.json_view import Simple_View
import datetime

class helper:
    def Timer_Ssesion_Encode(object):
        data = {
            "id" : object.id,
            "datatime_start" : object.datatime_start,
            "timer_time" : object.timer_time,
            "name" : object.name,
            "creator" : object.creator
        } 
        return JsonResponse(data=data)


class timer_ssesion(Simple_View):

    def get(self,request):
        ssesion_id = request.GET.get("ssesion_id")

        ssesion = Timer_Ssesion.objects.get(id=ssesion_id)
        
        difference = ssesion.datatime_start - datetime.datetime.now(datetime.timezone.utc)

        return JsonResponse({"status" : True, "datatime_start" : difference.seconds})

    def post(self,request):
        creator_id = int(request.GET.get("user_id"))
        timer_time = request.GET.get("timer_time")
        datatime_start = datetime.datetime.now(datetime.timezone.utc)
        name = request.GET.get("name")

        if creator_id and timer_time:
            new_obj = Timer_Ssesion.objects.create(
                datatime_start = datatime_start,
                timer_time = timer_time,
                name = str(name),
                creator = User.objects.get(id=creator_id)
            ).save()

            return JsonResponse({"status" : True})
        return JsonResponse({"status" : False})