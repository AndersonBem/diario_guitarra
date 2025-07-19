# 🎸 Diário de Guitarra

Um sistema web feito em Django para ajudar guitarristas a registrarem e organizarem seus treinos diários, músicas praticadas, tempo de execução e evolução ao longo do tempo.

🔗 **Acesse o sistema online:**  
[https://andersonalexandrebem.pythonanywhere.com/](https://andersonalexandrebem.pythonanywhere.com/)

---

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


