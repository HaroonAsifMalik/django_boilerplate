from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import SignUpSerializer
from accounts.utils import get_tokens_for_user


class SignUp(APIView):
    def post(self, requset):
        serializer = SignUpSerializer(data=requset.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {
                    "message": "User registered successfully",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                    },
                    **token,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
