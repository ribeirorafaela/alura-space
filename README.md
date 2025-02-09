# Alura Space

Projeto desenvolvido durante o curso de Django da Alura, uma galeria de imagens do espaço.

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Django 5.1.6
- HTML5
- CSS3

## 📋 Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes do Python)

## 🚀 Configuração do Projeto

1. Clone o repositório:
```bash
git clone https://github.com/ribeirorafaela/alura-space.git
cd alura-space
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
- Crie um arquivo `.env` na raiz do projeto
- Adicione sua SECRET_KEY:
```
SECRET_KEY=sua-chave-secreta-aqui
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor:
```bash
python manage.py runserver
```

## 🌐 Acessando a Aplicação

Após iniciar o servidor, acesse:
- http://localhost:8000

## 👨‍💻 Desenvolvido por
Rafaela Silva Ribeiro

## 📝 Licença
Este projeto está sob a licença MIT.
