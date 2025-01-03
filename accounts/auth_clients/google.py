import requests
from django.contrib.auth import get_user_model

User = get_user_model()


class Google:

    def __init__(self, token, provider, *args, **kwargs):
        self.token = token
        self.provider = provider

    def login(self):
        try:
            response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {self.token}"},
            )
            response_data = response.json()
            breakpoint()
            if response_data:
                user = User.objects.filter(email=response_data["email"]).first()
                if user:
                    return user
                else:
                    user = User.objects.create(
                        emial=response_data["email"],
                        display_name=response_data["family_name"],
                        image=response_data["pitcher"],
                        prvider=self.provider
                    )
                    return user
        except Exception:
            raise Exception(response_data)
