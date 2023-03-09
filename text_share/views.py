from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TextSerializer
from .models import Text


# Create your views here.
class TextView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        _text = request.data.get('text')
        _code_lang = request.data.get('code_lang') or 'latex'
        if not _text:
            return Response({"detail": "未填写内容"}, status=status.HTTP_400_BAD_REQUEST)
        Text.objects.create(text=_text, code_lang=_code_lang)
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)

    def delete(self, request):
        _tid = request.data.get('tid')
        if not _tid:
            return Response({"detail": "未获取到编号"}, status=status.HTTP_400_BAD_REQUEST)
        Text.objects.filter(id=_tid).delete()
        return Response({"detail": "ok"}, status=status.HTTP_200_OK)


class TextViews(APIView):
    def get(self, request):
        return Response(TextSerializer(Text.objects.all().order_by("-create_time"), many=True).data)
