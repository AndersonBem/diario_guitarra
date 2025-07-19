from django.contrib import admin
from apps.diario_guitarra.models import Musica, Treino, MusicaTreino, ExecucaoTreino, ExecucaoMusica

# Register your models here.

@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'duracao_treino', 'link_partitura')
    search_fields = ('nome',)

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(MusicaTreino)
class MusicaTreinoAdmin(admin.ModelAdmin):
    list_display = ('treino', 'musica', 'ordem')
    list_filter = ('treino',)
    ordering = ('treino','ordem')

@admin.register(ExecucaoTreino)
class ExecucaoTreinoAdmin(admin.ModelAdmin):
    list_display = ('treino', 'data_execucao')
    list_filter = ('treino', 'data_execucao')

@admin.register(ExecucaoMusica)
class ExecucaoMusicaAdmin(admin.ModelAdmin):
    list_display = ('musica', 'data_execucao', 'tempo_praticado')
    list_filter = ('musica', 'data_execucao')


