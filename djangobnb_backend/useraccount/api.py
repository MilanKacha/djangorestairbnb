from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import User
from .serializers import UserDetailSerializer


@api_view(['GET'])
@authentication_classes([])  # No authentication required
@permission_classes([])      # No permission required
def landlord_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    serializer = UserDetailSerializer(user, context={'request': request})
    print("Serializer data:", serializer.data)

    return JsonResponse(serializer.data, safe=False)
    

