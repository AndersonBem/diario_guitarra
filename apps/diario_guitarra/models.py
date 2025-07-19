from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length =255)
    link_partitura = models.URLField(blank=True, null=True)
    duracao_treino = models.PositiveIntegerField(help_text="Duração sugerida do treino em minutos")

    def __str__(self):
        return self.nome
    
class Treino(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class MusicaTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete = models.CASCADE)
    musica = models.ForeignKey(Musica, on_delete= models.CASCADE)
    ordem = models.PositiveIntegerField(blank=True, null=True, help_text="Ordem da música no treino")

    class Meta:
        unique_together = ('treino', 'musica')
        ordering= ['ordem']

    def __str__(self):
        return f"{self.treino.nome} - {self.musica.nome}"

class ExecucaoTreino(models.Model):
    treino = models.ForeignKey(Treino, on_delete = models.CASCADE)
    data_execucao = models.DateField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.treino.nome} em {self.data_execucao}"
    
class ExecucaoMusica(models.Model):
    musica = models.ForeignKey(Musica, on_delete=models.CASCADE)
    data_execucao = models.DateField(auto_now_add=True)
    tempo_praticado = models.PositiveIntegerField(blank=True,null=True, help_text="Tempo praticado em minutos")
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.musica.nome} em {self.data_execucao}" 
    
