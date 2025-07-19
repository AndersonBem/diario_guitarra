from django import forms
from apps.diario_guitarra.models import Musica, Treino, ExecucaoTreino, ExecucaoMusica

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'


class TreinoForm(forms.ModelForm):
    musicas = forms.ModelMultipleChoiceField(
        queryset=Musica.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="🎶 Músicas para este treino"
    )

    class Meta:
        model = Treino
        fields = ['nome', 'descricao', 'musicas']

class ExecucaoTreinoForm(forms.ModelForm):
    class Meta:
        model = ExecucaoTreino
        fields = ['treino', 'observacoes']

class ExecucaoMusicaForm(forms.ModelForm):
    class Meta:
        model = ExecucaoMusica
        fields = ['musica','tempo_praticado', 'observacoes']

class MusicasNoTreinoForm(forms.Form):
    musicas = forms.ModelMultipleChoiceField(
        queryset=Musica.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Selecione as músicas para o treino"
    )