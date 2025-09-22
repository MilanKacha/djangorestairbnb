from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import PropertyForm
from .models import Property
from .serializers import PropertiesListSerializer, PropertiesDetailSerializer


@api_view(['GET'])
@authentication_classes([]) #meaning no authentication check
@permission_classes([]) #meaning no permission check 
def property_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)
    
    return JsonResponse({
        'data': serializer.data
    })
    
    
    
@api_view(['GET'])
@authentication_classes([]) #meaning no authentication check
@permission_classes([]) #meaning no permission check
def properties_detail(request, pk):
    property = Property.objects.get(pk=pk)
    serializer = PropertiesDetailSerializer(property, many=False)
    
    return JsonResponse(serializer.data)
    
    
@api_view(['POST'])
def create_property(request):
    # request.POST = all data for img request.FILES
    form = PropertyForm(request.POST, request.FILES)  
    print("re",request.POST)
    
    if form.is_valid():
        property = form.save(commit=False) #from property modal not feel landlord so commit=False
        property.landlord = request.user   # need landlord meaning user email
        property.save()
        
        return JsonResponse({'success': True})
    else:
     print('error', form.errors, form.non_field_errors)
    return JsonResponse({'errors': form.errors.as_json()}, status=400)
    