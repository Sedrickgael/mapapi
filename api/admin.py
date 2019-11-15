from django.contrib import admin

#importation des models
from . import models
from django.utils.safestring import mark_safe


@admin.register(models.Coordinate)
class CoordinateAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'longitude',
        'lagitude',
        'status',
        'date_add',
        'date_upd',        
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'longitude',
        'lagitude',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['longitude', 'lagitude']
    
    list_per_page = 3

    ordering = ['longitude',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Coordonnées sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Coordonnées sélectionnées'

    
@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'coordonnees',
        'nom',
        'status',
        'date_add',
        'date_upd',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = (
        'nom',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['nom',]
    
    list_per_page = 7

    ordering = ['nom',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Salons sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Salons sélectionnées'

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    
    #les champs à afficher dans la table
    list_display = (
        'salon',
        'nom',
        'status',
        'date_add',
        'date_upd',
            
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
        'salon',
    )

    search_fields = (
        'salon',
        'nom',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')

    list_display_links = ['nom']
    
    list_per_page = 7

    ordering = ['nom',]

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les Services sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les Services sélectionnées'

    
    
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    #les champs à afficher dans la table
    list_display = (
        'salon',
        'date_add',
        'date_upd',
        'view_image',
        )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    date_hierarchy = 'date_add'

    actions = ('active', 'desactive')
    
    list_per_page = 7

    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "La sélection a été activée avec succès")
    active.short_description = 'Activez les photos sélectionnées'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "La sélection a été désactivée avec succès")
    desactive.short_description = 'Désactivez les photos sélectionnées'

    def view_image(self, obj):
        return mark_safe('<img src="{img_url}" width="100px" height="50" />'.format(img_url=obj.image.url))
