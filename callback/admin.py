from django.contrib import admin

from .models import Player, Game

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_created', 'date_update')
    search_fields = ('name', 'email')
class PlayersInline(admin.TabularInline):
    model = Game.players.through
    max_num = 5
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_players', 'date_created', 'date_update')
    fields = ('name',)
    inlines = (PlayersInline,)
    
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
