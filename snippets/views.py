from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer
from rest_framework.response import Response
# Create your views here.


"""
View to create and list Snippet with tag.
"""
class SnippetListCreateView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]
  
    def list(self, request, *args, **kwargs):
        snippets = self.get_queryset()
        total_snippets = snippets.count()
        serializer = self.get_serializer(snippets, many=True)
        data = {
            'total_snippets': total_snippets,
            'snippets': serializer.data
        }
        return Response(data)

"""
View to display,update and delete Snippet.
"""
class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [IsAuthenticated]

"""
View to list Tags.
"""
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

"""
View to return snippets linked to the selected tag.
"""
class TagDetailView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]