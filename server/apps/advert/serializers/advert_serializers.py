from rest_framework import serializers

from user.models import CustomUser
from advert.serializers.promote_serializers import PromoteSerializer
from advert.models import (
    Advert,
    AdvertContact,
    AdvertImage,
    Category,
    SubCategory,
    City,
    AdvertView,
)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')


class AdvertContactSerailzer(serializers.ModelSerializer):
    class Meta:
        model = AdvertContact
        fields = ("phone_number",)


class AdvertViewSerailzer(serializers.ModelSerializer):
    class Meta:
        model = AdvertView
        fields = ("view", "users")


class AdvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertImage
        fields = ["image"]


class AdvertCreateSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="email", queryset=CustomUser.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )
    sub_category = serializers.SlugRelatedField(
        slug_field="name", queryset=SubCategory.objects.all()
    )
    promote = PromoteSerializer(many=True, required=False)
    city = serializers.SlugRelatedField(slug_field="name", queryset=City.objects.all())

    class Meta:
        model = Advert

        exclude = ("created_date", "status")


class AdvertListSerializer(serializers.ModelSerializer):
    promote = PromoteSerializer(many=True)
    sub_category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    advert_contact = AdvertContactSerailzer(many=True)
    advert_image = AdvertImageSerializer(many=True)
    city = serializers.SlugRelatedField(slug_field="name", read_only=True)
    advert_image_count = serializers.IntegerField(
        source="advert_image.count", read_only=True
    )

    class Meta:
        model = Advert
        fields = "__all__"


class AdvertDetailSerializer(serializers.ModelSerializer):
    promote = PromoteSerializer(many=True)
    advert_contact = AdvertContactSerailzer(many=True)
    city = serializers.SlugRelatedField(slug_field="name", read_only=True)
    advert_image = AdvertImageSerializer(many=True)
    advert_view = AdvertViewSerailzer()

    class Meta:
        model = Advert
        exclude = ("email",)
