from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from movie.serializers import MovieListSerializer, RecommendListSerializer
from movie.models import Movie, Genre, Actor, Director
from random import sample
from django.db.models import Count
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
  # 영화 추천 페이지: random 영화 목록 20개
  if request.method == 'GET':
    movies = Movie.objects.all()
    random_movies = sample(list(movies), 24)
    serializer = MovieListSerializer(random_movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
# 요청 받은 영화 목록을 바탕으로 추천 영화 응답
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def genre(request):
  if request.method == 'POST':
    # user가 선택한 영화 목록 받음 -> 추후 저장할 것
    like_movies = request.data.get('userLikeMovies')
    like_movies_query = Movie.objects.filter(movie_id__in=like_movies)
    
    # user = request.user
    user = request.user

    # user가 선택한 영화 목록 추가함
    for like_movies in like_movies_query:
      user.user_liked_movie.add(like_movies)

    # 사용자가 선호하는 장르 2가지 
    genres = like_movies_query.values('genres').annotate(total=Count('id')).order_by('-total')[:2]
    
    if len(genres) < 2:
      return Response({"error": "Not enough data to make recommendations"}, status=status.HTTP_400_BAD_REQUEST)
    
    recommendations = {}
    for genre in genres:
        genre_pk = genre.get('genres')
        genre = Genre.objects.get(pk=genre_pk)
        genre_movies = Movie.objects.filter(genres=genre).order_by('-popularity')[:5]
        genre_serializer = RecommendListSerializer(genre_movies, many=True, context={'recommend': genre.genre_name})
        recommendations[genre.genre_name] = genre_serializer.data
    return Response(recommendations, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def actor(request):
  if request.method == 'POST':
    like_movies = request.data.get('userLikeMovies')

    # 사용자가 선호하는 배우 2명 선정
    movies = Movie.objects.filter(movie_id__in=like_movies)
    actors_query = Actor.objects.filter(movie__in=movies).distinct().annotate(total=Count('id')).order_by('-actor_popularity', '-total')[:2]
    if len(actors_query) < 2:
        return Response({"error": "Not enough data to make recommendations"}, status=status.HTTP_400_BAD_REQUEST)

    recommendations = {}

    for actor in actors_query:
        actor_movies = Movie.objects.filter(actors=actor).order_by('-popularity')[:5]
        actor_serializer = RecommendListSerializer(actor_movies, many=True, context={'recommend': actor.actor_name})
        recommendations[actor.actor_name] = actor_serializer.data
    return Response(recommendations, status=status.HTTP_200_OK)
  
@api_view(['POST'])
def director(request):
  # user가 선택한 영화 목록 받음 -> 추후 저장할 것
  like_movies = request.data.get('userLikeMovies')
  
  # 영화 추천 알고리즘 짜기
  # 사용자가 선호하는 배우 2명 선정
  directors_query = Director.objects.filter(movie__movie_id__in=like_movies).distinct().annotate(total=Count('id')).order_by('-total', '-actor_popularity')
  
  first_director = directors_query[0]
  second_director = directors_query[1]
  pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_movie(request):
  serializer = MovieListSerializer(request.user.user_liked_movie, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like(request):
  # print(request.query_params)
  print(request.data)
  if request.data.get('movie_pk'):
    movie_pk = request.data.get('movie_pk')
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user
    
    if movie in user.user_liked_movie.all():
      user.user_liked_movie.remove(movie)
      print('t')
      print(user.user_liked_movie.all())
    else:
      user.user_liked_movie.add(movie)
      print('a')
      print(user.user_liked_movie.all())
    return Response({'message': '성공'}, status=status.HTTP_200_OK)
  return Response({'error': '지원되지 않는 메서드'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    # if request.method == 'GET':
    #     movie_pk = request.query_params.get('movie_pk')  # Get 'movie_pk' from query parameters
    #     if movie_pk:
    #         try:
    #             movie = Movie.objects.get(pk=movie_pk)
    #         except Movie.DoesNotExist:
    #             return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    #         user = request.user
    #         if movie in user.user_liked_movie.all():
    #             user.user_liked_movie.remove(movie)
    #             message = 'Movie unliked successfully'
    #         else:
    #             user.user_liked_movie.add(movie)
    #             message = 'Movie liked successfully'
            
    #         return Response({'message': message}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'error': 'movie_pk parameter is required'}, status=status.HTTP_400_BAD_REQUEST)