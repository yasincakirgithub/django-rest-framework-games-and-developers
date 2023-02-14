from rest_framework import status
from rest_framework.response import Response 

from games.models import Developer, Game
from games.api.serializers import GameSerializer, DeveloperSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404



class DeveloperListCreateAPIView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True, context={'request': request}) 
        return Response(serializer.data)


    def post(self, request):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GameListCreateAPIView(APIView):
    def get(self, request):
        games = Game.objects.filter(status=True) 
        serializer = GameSerializer(games, many=True) 
        return Response(serializer.data)


    def post(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameDetailAPIView(APIView):

    def get_object(self, pk):
        game_instance = get_object_or_404(Game, pk=pk)
        return game_instance

    def get(self, request, pk):
        game = self.get_object(pk=pk)
        serializer = GameSerializer(game) 
        return Response(serializer.data)       

    def put(self, request, pk):
        game = self.get_object(pk=pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

    def delete(self, request, pk):
        game = self.get_object(pk=pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



