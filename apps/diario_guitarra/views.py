from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from apps.diario_guitarra.models import Musica, Treino, MusicaTreino, ExecucaoMusica, ExecucaoTreino
from apps.diario_guitarra.forms import MusicaForm, TreinoForm, MusicasNoTreinoForm
from datetime import date
from django.db.models import Sum, Count

# index
def index(request):
    return render(request, 'index/index.html')

# Lista de musicas
def listar_musicas(request):
    musicas = Musica.objects.all()

    # Calcula o tempo total por música
    execucoes = ExecucaoMusica.objects.values('musica_id').annotate(total=Sum('tempo_praticado'))

    # Dicionários: id -> total min e texto hh:mm
    total_por_musica = {}
    tempo_hhmm_por_musica = {}

    for e in execucoes:
        total = e['total'] or 0
        musica_id = e['musica_id']
        total_por_musica[musica_id] = total
        horas = total // 60
        minutos = total % 60
        tempo_hhmm_por_musica[musica_id] = f"{horas}h{minutos:02d}min"
    for musica in musicas:
        musica.total_praticado = total_por_musica.get(musica.id, 0)
        musica.total_hhmm = tempo_hhmm_por_musica.get(musica.id, "0h00min")


    return render(request, 'listas/listar_musicas.html', {
        'musicas': musicas,
        'total_por_musica': total_por_musica,
        'tempo_hhmm_por_musica': tempo_hhmm_por_musica,
    })

# Adicionar musica
def adicionar_musica(request):
    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
    else:
        form= MusicaForm()
    
    return render(request,'add/adicionar_musica.html',{'form': form})

# Editar musica
def editar_musica(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)

    if request.method == 'POST':
        form = MusicaForm(request.POST, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('listar_musicas')
        else:
            print(form.errors)  # 👈 Isso mostra no terminal se tem erro de validação
    else:
        form = MusicaForm(instance=musica)
    
    return render(request, 'editar/editar_musica.html', {'form': form, 'musica':musica})

# Deletar musica
def deletar_musica(request, musica_id):
    musica = get_object_or_404(Musica, id=musica_id)

    if request.method == 'POST':
        musica.delete()
        messages.success(request, f"A música {musica.nome} foi deletada com sucesso.")
        return redirect('listar_musicas')

    return render(request, 'deletar/deletar_musica.html', {'musica':musica})

# Lista de Treinos
def listar_treinos(request):
    treinos = Treino.objects.all()

    execucoes_hoje = ExecucaoTreino.objects.filter(data_execucao=date.today()).values_list('treino_id', flat=True)

    # Contagem de execuções por treino
    execucoes = ExecucaoTreino.objects.values('treino_id').annotate(total=Count('id'))
    execucoes_dict = {e['treino_id']: e['total'] for e in execucoes}

    # Atribui o total diretamente a cada treino
    for treino in treinos:
        treino.qtd_execucoes = execucoes_dict.get(treino.id, 0)

    return render(request, 'listas/listar_treinos.html', {
        'treinos': treinos,
        'execucoes_hoje': execucoes_hoje,
    })

# Add treino
def adicionar_treino(request):
    if request.method =='POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            treino = form.save()
            musicas = form.cleaned_data['musicas']
            for musica in musicas:
                MusicaTreino.objects.create(treino=treino, musica=musica)
            return redirect('listar_treinos')
    else:
        form = TreinoForm()
    return render(request, 'add/adicionar_treino.html',{'form': form})

# Deletar treino
def deletar_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    if request.method == 'POST':
        treino.delete()
        messages.success(request, "Treino deletado com sucesso.")
        return redirect('listar_treinos')
    return redirect('detalhar_treino', treino_id=treino.id)


# Detalhes treino
def detalhar_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    musicas_treino = MusicaTreino.objects.filter(treino=treino).select_related('musica')
    execucoes = ExecucaoMusica.objects.filter(musica__in=[mt.musica for mt in musicas_treino])
    data_hoje = date.today()

    return render(request,'detalhes/detalhar_treino.html',{
        'treino':treino,
        'musicas_treino': musicas_treino,
        'execucoes': execucoes,
        'data_hoje': data_hoje,
    })

# Registrar execução
def registrar_execucao(request, musica_id, treino_id):
    if request.method == 'POST':
        tempo =request.POST.get('tempo_praticado')
        observacoes = request.POST.get('observacoes','')

        musica = get_object_or_404(Musica, id = musica_id)

        if tempo:
            ExecucaoMusica.objects.create(
                musica=musica,
                tempo_praticado= int(tempo),
                observacoes=observacoes
            )
        
    return redirect('detalhar_treino', treino_id=treino_id)

# Remover musica do treino
def remover_musica_treino(request, treino_id, musica_id):
    treino = get_object_or_404(Treino, id=treino_id)
    musica = get_object_or_404(Musica, id=musica_id)

    MusicaTreino.objects.filter(treino=treino, musica=musica).delete()

    return redirect('detalhar_treino', treino_id=treino.id)

#Registrar execução de treino
def registrar_execucao_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)
    
    if request.method == 'POST':
        observacoes = request.POST.get('observacoes')
        ExecucaoTreino.objects.create(treino=treino, observacoes=observacoes)
        messages.success(request, "Treino registrado com sucesso.")
        return redirect('listar_treinos')
    
    return redirect('detalhar_treino', treino_id=treino.id)

# Editar treino
def editar_treino(request, treino_id):
    treino = get_object_or_404(Treino, id=treino_id)

    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            treino = form.save(commit=False)
            treino.save()

            # Apaga os vínculos anteriores
            MusicaTreino.objects.filter(treino=treino).delete()

            # Cria os vínculos novos
            musicas = form.cleaned_data['musicas']
            for ordem, musica in enumerate(musicas):
                MusicaTreino.objects.create(
                    treino=treino,
                    musica=musica,
                    ordem=ordem  # ordem simples com base na posição
                )

            return redirect('detalhar_treino', treino_id=treino.id)
    else:
        # Pega só as músicas relacionadas via MusicaTreino
        musicas_relacionadas = Musica.objects.filter(musicatreino__treino=treino)
        form = TreinoForm(instance=treino, initial={'musicas': musicas_relacionadas})

    return render(request, 'editar/editar_treino.html', {'form': form, 'treino': treino})