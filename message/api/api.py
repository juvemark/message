from django.http import JsonResponse, HttpResponseNotAllowed

# echo message api
def echo_message(request):
    if request.method == 'GET':
        msg = request.GET.get('msg', '')
        return JsonResponse({'msg': msg})
    else:
        return HttpResponseNotAllowed(['GET'])

