from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class StatusView(APIView):
    def get(self, request):
        return Response({'result': 'Server is running and ok'}, status=status.HTTP_200_OK)
