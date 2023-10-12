from django.http import JsonResponse
from backend import getMap, getMetadata, getDirections
from .models import Item, ReceivedList
import json
from django.contrib.auth.models import User

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

            print(received_data,request.user)
            save_record(received_data,request.user)
            
            data = getDirections(received_data["msg"])
            return JsonResponse(data)
        else:
            return JsonResponse({"error": "msg parameter missing"})
    else:
        return JsonResponse({"error": "Invalid Request"})
    
def save_record(received_data,user):
    # Save received_data to the database
        
        try:
            user = User.objects.get(username='pooshpal')
        except User.DoesNotExist:
            user = User.objects.create_superuser('pooshpal', 'pooshpal@example.com', 'password')
        
        received_list = ReceivedList.objects.create(user=user)
        for item_name in received_data:
            item, created = Item.objects.get_or_create(name=item_name)
            received_list.items.add(item)

def get_all_records(request):
    try:
        if request.method == 'GET':
            print(f"User ID: {request.user.id} Request Type: getAllRecords")
            records = ReceivedList.objects.all()
            data = [{'id': record.id, 'items': [item.name for item in record.items.all()]} for record in records]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({"error": "Invalid Request"})
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return JsonResponse({"error": "An error occurred"})
    

#save_record(["apple"],"pooshpal")0