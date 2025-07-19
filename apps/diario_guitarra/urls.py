from django.urls import path
from apps.diario_guitarra.views import index,listar_musicas, adicionar_musica, editar_musica, deletar_musica, listar_treinos, adicionar_treino, detalhar_treino,registrar_execucao,remover_musica_treino,registrar_execucao_treino,deletar_treino, editar_treino

urlpatterns = [
    # rotas
    # index
    path('', index, name='index'),
    # lista musicas
    path('musicas/', listar_musicas, name='listar_musicas'),
    # Add Musica
    path('adicionar_musica/', adicionar_musica, name='adicionar_musica'),
    # Alterar musica
    path('musicas/<int:musica_id>/editar/', editar_musica, name='editar_musica'),
    # deletar musica
    path('musicas/<int:musica_id>/deletar/', deletar_musica, name = 'deletar_musica'),
    # Listar treinos
    path('treinos/', listar_treinos, name='listar_treinos'),
    # Add treinos
    path('treinos/adicionar/', adicionar_treino, name='adicionar_treino'),
    # Detalhes treinos
    path('treinos/<int:treino_id>/', detalhar_treino, name='detalhar_treino'),
    # execução musica
    path('treino/<int:treino_id>/musica/<int:musica_id>/registrar_execucao/',registrar_execucao, name='registrar_execucao'),
    # Remover musica treino
    path('treinos/<int:treino_id>/remover-musica/<int:musica_id>/', remover_musica_treino, name='remover_musica_treino'),
    # Registrar treino realizado
    path('treinos/<int:treino_id>/executar/', registrar_execucao_treino, name='registrar_execucao_treino'),
    # Excluir o treino inteiro
    path('treinos/<int:treino_id>/deletar/', deletar_treino, name='deletar_treino'),
    # Editar Treino
    path('treino/<int:treino_id>/editar/', editar_treino, name='editar_treino'),



]