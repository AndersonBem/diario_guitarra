# 🎸 Diário de Guitarra

Um sistema web feito em Django para ajudar guitarristas a registrarem e organizarem seus treinos diários, músicas praticadas, tempo de execução e evolução ao longo do tempo.

🔗 **Acesse o sistema online:**  
[https://andersonalexandrebem.pythonanywhere.com/](https://andersonalexandrebem.pythonanywhere.com/)

---
## 👨‍💻 Como testar o sistema online
Você pode testar o sistema gratuitamente acessando a versão hospedada no PythonAnywhere:

# 🔗 [Acesse o sistema](https://andersonalexandrebem.pythonanywhere.com/)

## 👉 Passo a passo para testar:
  ### 1. Adicione músicas

  - Vá para Músicas e clique em "Adicionar Música".

  - Use qualquer música que conheça. Para tablaturas, recomendo https://www.songsterr.com.

  ### 2. Crie um treino

  - No menu, clique em "Novo Treino".

  - Dê um nome, descreva o foco do treino e selecione as músicas que você (ou outros usuários) adicionaram.

  ### 3. Visualize o treino

  - Vá na seção "Treinos", escolha um e clique em "Ver Músicas".

  ### 4. Registre o tempo de prática

  - Cada música do treino terá um link para a tablatura, além de um cronômetro e timer lateral para controle do tempo de execução.



## 🧠 Funcionalidades

- Cadastro de músicas com afinação e nível de dificuldade.
- Registro de treinos e descrição dos focos do dia.
- Associação de músicas a treinos.
- Registro de tempo de prática por música.
- Cronômetro e timer com alerta sonoro.
- Visualização de execuções anteriores.

---

## 🖼️ Capturas de tela



---

## 🚀 Como rodar localmente

### Pré-requisitos

- Python 3.10+
- pip
- Virtualenv (opcional, mas recomendado)

### Passos:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/diario_guitarra.git
cd diario_guitarra

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Faça as migrações
python manage.py migrate

# Crie um superusuário
python manage.py createsuperuser

# Rode o servidor
python manage.py runserver
```

## 📌 Tecnologias utilizadas
Django 4.x

HTML + CSS + JS

SQLite (default)

PythonAnywhere (deploy gratuito)

## 📋 Futuras melhorias
Dashboard com estatísticas de prática.

Ranking de músicas mais praticadas.

Exportação dos treinos.

Modo escuro 🌓

## 🤝 Contribuição

Sinta-se livre para abrir issues ou fazer um fork e contribuir com pull requests!

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


