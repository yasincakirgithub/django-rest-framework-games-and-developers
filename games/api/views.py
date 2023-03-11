from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from games.models import Developer, Game
from games.api.serializers import GameSerializer, DeveloperSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from games.api.filters import DeveloperFilter, GameFilter


# API view olan hali

# class DeveloperListCreateAPIView(APIView):
#     def get(self, request):
#         developers = Developer.objects.all()
#         serializer = DeveloperSerializer(developers, many=True, context={'request': request})
#         return Response(serializer.data)
#
#
#     def post(self, request):
#         serializer = DeveloperSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeveloperDetailAPIView(APIView):
#
#     def get_object(self, pk):
#         developer_instance = get_object_or_404(Developer, pk=pk)
#         return developer_instance
#
#     def get(self, request, pk):
#         developer = self.get_object(pk=pk)
#         serializer = DeveloperSerializer(developer)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         developer = self.get_object(pk=pk)
#         serializer = DeveloperSerializer(developer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         developer = self.get_object(pk=pk)
#         developer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class GameListCreateAPIView(APIView):
#     def get(self, request):
#         games = Game.objects.filter(status=True)
#         serializer = GameSerializer(games, many=True)
#         return Response(serializer.data)
#
#
#     def post(self, request):
#         serializer = GameSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class GameDetailAPIView(APIView):
#
#     def get_object(self, pk):
#         game_instance = get_object_or_404(Game, pk=pk)
#         return game_instance
#
#     def get(self, request, pk):
#         game = self.get_object(pk=pk)
#         serializer = GameSerializer(game)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         game = self.get_object(pk=pk)
#         serializer = GameSerializer(game, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         game = self.get_object(pk=pk)
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Generic view olan hali #


class DeveloperListCreateAPIView(ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = DeveloperFilter


class DeveloperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAuthenticated]


class GameListCreateAPIView(ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = GameFilter

    def get_user(self):
        if self.request.user.is_authenticated:
            return self.request.user
        else:
            return None

    def get_queryset(self):
        user = self.get_user()
        queryset = Game.objects.all()
        if user:
            queryset = queryset.filter(creator=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=None)


class GameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]
