from django.views.decorators.csrf import csrf_exempt

class Simple_View:
    @csrf_exempt
    def route(self,request):
        if request.method == "GET":
            return self.get(request)
        elif request.method == "POST":
            return self.post(request)