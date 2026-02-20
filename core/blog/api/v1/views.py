from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter , OrderingFilter

from django.shortcuts import get_object_or_404

from blog.models import Post , Category
from .serializers import PostSerializer , CategorySerializer
from .pagination import DefaultPagination


"""
@api_view(["GET","POST"])
def post_list_api(request) :
    if request.method == "GET" :
        posts = Post.objects.select_related("author","category").filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "POST" :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""

"""
@api_view(["GET","PUT","DELETE"])
def post_detail_api(request,pk) :
    if request.method == "GET" :
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == "PUT" :
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE" :
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

# APIView
"""
class PostListApi(APIView) :
    def get(self,request) :
        posts = Post.objects.select_related("author","category").filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request) :
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
"""

"""
class PostDetailApi(APIView) :
    def get(self,request,pk) :
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk) :
        post = get_object_or_404(Post,pk=pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk) :
        post = get_object_or_404(Post,pk=pk)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

# GenericsAPIView
"""
class PostListApi(GenericAPIView) :
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)

    def get(self,request) :
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""

"""
class PostDetailApi(GenericAPIView) :
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)

    def get(self,request,pk) :
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk) :
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk) :
        post = get_object_or_404(self.queryset,pk=pk)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

# mixins
"""
class PostListApi(GenericAPIView,ListModelMixin,CreateModelMixin) :
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)

    def get(self,request,*args,**kwargs) :
        return self.list(request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs) :
        return self.create(request,*args,**kwargs)
"""

"""
class PostDetailApi(RetrieveUpdateDestroyAPIView) :
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)

    def get(self,request,*args,**kwargs) :
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
"""

# viewsets
"""
class PostViewSets(viewsets.ViewSet) :
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)

    def list(self,request) :
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request) :
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None) :
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None) :
        post = get_object_or_404(self.queryset,pk=pk)
        serializer = self.serializer_class(post,data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None) :
        post = get_object_or_404(self.queryset,pk=pk)
        post.delete()
        return Response({"detail":"item removed successfully"},status=status.HTTP_204_NO_CONTENT)
"""

class PostModelViewSets(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author","category").filter(status=True)
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ["category","author","status"]
    ordering_fields = ["id"]
    search_fields = ["title"]

class CategoryModelViewSets(viewsets.ModelViewSet) :
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()