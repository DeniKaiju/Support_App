from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Issue
from .serializers import IssueSerializer


@api_view(["GET"])
def get_issues(request):
    issues = Issue.objects.all()
    serializer = IssueSerializer(issues, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_issue(request):
    serializer = IssueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
