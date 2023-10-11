from django.http import JsonResponse
from backend import getMap, getMetadata, getDirections
from .models import Item, ReceivedList
import json

def get_map(request):
    print(f"User ID: {request.user.id} Request Type: getMap")
    data = getMap()
    return JsonResponse(data)

def get_metadata(request):
    print(f"User ID: {request.user.id} Request Type: getMetadata")
    data = getMetadata()
    return JsonResponse(data)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def get_directions(request):
    if request.method == 'GET':
        received_data = request.GET.get('msg')
        if received_data:
            print(f"User ID: {request.user.id} Request Type: getDirections")
            print(f"Received List: {received_data}")
            received_data=json.loads(received_data)
            data = getDirections(received_data["msg"])

            

            return JsonResponse(data)
        else:
            return JsonResponse({"error": "msg parameter missing"})
    else:
        return JsonResponse({"error": "Invalid Request"})

def get_all_records(request):
    if request.method == 'GET':
        print(f"User ID: {request.user.id} Request Type: getAllRecords")
        records = ReceivedList.objects.filter(user=request.user)
        data = [{'id': record.id, 'items': [item.name for item in record.items.all()]} for record in records]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Invalid Request"})