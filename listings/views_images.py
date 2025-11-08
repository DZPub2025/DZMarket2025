from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Ad, AdImage
from .serializers import AdImageSerializer
import cloudinary.uploader

class AdImageUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, ad_id, format=None):
        # Expect either 'image' file in multipart or 'image_url' in data
        ad = get_object_or_404(Ad, pk=ad_id)
        # Only seller can add images to their ad
        if ad.seller != request.user:
            return Response({'detail':'Only seller can add images'}, status=status.HTTP_403_FORBIDDEN)

        image_file = request.FILES.get('image')
        image_url = request.data.get('image_url')

        if not image_file and not image_url:
            return Response({'detail':'Provide image file or image_url'}, status=status.HTTP_400_BAD_REQUEST)

        if image_file:
            # upload to Cloudinary if configured
            try:
                upload_res = cloudinary.uploader.upload(image_file)
                url = upload_res.get('secure_url') or upload_res.get('url')
            except Exception as e:
                return Response({'detail': 'Cloudinary upload failed', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            url = image_url

        order = request.data.get('order', 0)
        img = AdImage.objects.create(ad=ad, image=url, order=order)
        return Response(AdImageSerializer(img).data, status=status.HTTP_201_CREATED)

class AdImageDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, ad_id, pk, format=None):
        ad = get_object_or_404(Ad, pk=ad_id)
        if ad.seller != request.user:
            return Response({'detail':'Only seller can delete images'}, status=status.HTTP_403_FORBIDDEN)
        img = get_object_or_404(AdImage, pk=pk, ad=ad)
        img.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
