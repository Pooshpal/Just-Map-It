from django.http import JsonResponse
from backend import getMap, getMetadata, getItems, getDirections
from .models import Item, ReceivedList

def get_map(request):
    print(f"User ID: {request.user.id} Request Type: getMap")
    data = getMap()
    return JsonResponse(data)

def get_metadata(request):
    print(f"User ID: {request.user.id} Request Type: getMetadata")
    data = getMetadata()
    return JsonResponse(data)

def get_items(request):
    print(f"User ID: {request.user.id} Request Type: getItems")
    data = getItems()
    return JsonResponse(data)

def get_directions(request):
    if request.method == 'POST':
        received_data = request.POST.get('msg')
        print(f"User ID: {request.user.id} Request Type: getDirections")
        print(f"Received List: {received_data}")
        data = getDirections(received_data)

        # Save received_data to the database
        user = request.user
        received_list = ReceivedList.objects.create(user=user)
        for item_name in received_data:
            item, created = Item.objects.get_or_create(name=item_name)
            received_list.items.add(item)

        return JsonResponse(data)
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