
from rest_framework.response import Response
from rest_framework import status
from pintrest.models import Movie,Actor
from pintrest.api.v1.serializers import MovieSerializer, ActorSerializer
from rest_framework.decorators import api_view,permission_classes,authentication_classes

from rest_framework.permissions import IsAuthenticated, BasePermission


class UserCanDeleteMovie(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name= 'can-delete').exists():
            return True
        return False

@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def actors(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(instance=actors, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_actors(request,**kwargs):
    pk = kwargs.get('id')

    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message':'Movie does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    serialized_movie=MovieSerializer(instance=movie)

    return Response(data=serialized_movie.data.get('actors'), status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_details(request,**kwargs):
    pk = kwargs.get('id')

    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message':'Movie does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    serialized_movie = MovieSerializer(instance=movie)

    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_movie(request):
    serialized_movie=MovieSerializer(data=request.POST)

    if serialized_movie.is_valid():
        serialized_movie.save()
        response_data={
            'message':'Successfully created a movie!',
            'data': {'id': serialized_movie.data.get('id')}
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
    else:
        return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'PUT'])
def edit_movie(request, **kwargs):
    pk = kwargs.get('id')

    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message':'Movie does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serialized_movie = MovieSerializer(instance=movie,data=request.data)
    elif request.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie,data=request.data,partial=True)

    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data={'message':'Wrong data'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([UserCanDeleteMovie])
def delete_movie(request,**kwargs):
    pk = kwargs.get('id')

    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message':'Movie does not exist!'}, status=status.HTTP_400_BAD_REQUEST)

    movie.delete()
    return Response(data={'{} deleted successfully!'.format(movie.name)}, status=status.HTTP_200_OK)
