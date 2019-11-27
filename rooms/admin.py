from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    search_fields = [
        "city",
        "^host__username",
    ]

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "city", "price")}),
        ("Time", {"fields": ("check_in", "check_out")}),
        ("Spaces", {"fields": ("guests", "beds", "baths", "bedrooms")}),
        (
            "More About Space",
            {
                "classes": ("collapse",),
                "fields": ("room_type", "amenities", "facilities", "house_rules"),
            },
        ),
        ("Details", {"fields": ("host",)}),
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "photos"

    inlines = [
        PhotoInline,
    ]


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
