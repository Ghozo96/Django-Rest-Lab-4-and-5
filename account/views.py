
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,BasePermission
from account.serializers import UserSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])

def register(request):
    serialized_user=UserSerializer(data=request.data)

    if serialized_user.is_valid():
        serialized_user.save()
    else:
        return Response(data=serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'firstname': serialized_user.data.get('first_name'),
        'token' : Token.objects.get(user__username=serialized_user.data.get('username')).key,
        'id': serialized_user.data.get('id')
    }
    
    return Response(data=data, status=status.HTTP_201_CREATED)