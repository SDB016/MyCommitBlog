from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','password','password2','github','token']
