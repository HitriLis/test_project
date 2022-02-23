from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=54, unique=True, default="")
    email = models.EmailField(max_length=54, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=254, default="")
    players = models.ManyToManyField(Player, blank=True, related_name='player_games')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_players(self):
        return ",".join([p.name for p in self.players.all()])

    def players_count(self):
        return self.players.count()