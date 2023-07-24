
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import User

def get_users(request):
    # Get all users from the database
    users = User.objects.all()

    # Serialize user data to JSON format
    # Here we've decided to serialize our information into json instead of opening a serializer file
    user_data = [
        {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'bio': user.bio,
            'slug': user.slug,
            'position': user.position,
            'image': user.get_image(),
            'thumbnail': user.get_thumbnail(),
            'date_added': user.date_added,
        }
        for user in users
    ]

    return JsonResponse(user_data, safe=False)

def get_user_by_id(request, user_id):
    try:
        # Get a specific user by the given user_id
        user = get_object_or_404(User, id=user_id)

        # Serialize user data to JSON format
        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name,
            'bio': user.bio,
            'slug': user.slug,
            'position': user.position,
            'image': user.get_image(),
            'thumbnail': user.get_thumbnail(),
            'date_added': user.date_added,
        }

        return JsonResponse(user_data)

    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
