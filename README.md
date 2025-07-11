<div align="center">
  <svg width="100%" height="120" viewBox="0 0 800 120">
    <defs>
      <linearGradient id="grad" x1="0" x2="1" y1="0" y2="1">
        <stop offset="0%" stop-color="#5865F2"/>
        <stop offset="100%" stop-color="#23272A"/>
      </linearGradient>
    </defs>
    <rect width="800" height="120" fill="url(#grad)" rx="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="48" fill="#fff" font-family="Segoe UI, sans-serif" style="letter-spacing:2px;">
      <tspan>OAuth Discord Bot</tspan>
    </text>
  </svg>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-%23000?logo=flask" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/Discord%20API-%235865F2?logo=discord&logoColor=white" alt="Discord Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License Badge"/>
</p>

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/discordjs/discordjs-original.svg" width="60" style="animation: float 2s infinite alternate;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60" style="animation: float 2s 0.5s infinite alternate;"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="60" style="animation: float 2s 1s infinite alternate;"/>
</div>

---

## Sobre o Projeto

Este bot permite que usuários entrem automaticamente em um servidor Discord e recebam um cargo específico após autenticação via OAuth2. Ideal para comunidades, cursos, ou qualquer aplicação que precise de integração rápida e segura com Discord.

---

## Funcionalidades

- **Login seguro** via OAuth2 do Discord
- **Adiciona usuários automaticamente** ao servidor
- **Atribui cargos** personalizados ao entrar
- **Solicita e-mail** do usuário (opcional)
- **Rápido e fácil de configurar**

---

## Tecnologias Utilizadas

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="24"/> **Python 3.8+**
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="24"/> **Flask**
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/discordjs/discordjs-original.svg" width="24"/> **Discord API**
- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="24"/> **Docker** (opcional)

---

## Instalação

```bash
git clone https://github.com/171ntw/oauth-discord-bot.git
cd oauth-discord-bot

pip install -r requirements.txt
```

---

## Configuração do .env

```env
client_id=SEU_CLIENT_ID
client_secret=SEU_CLIENT_SECRET
redirect_uri=SEU_REDIRECT_URI
bot_token=SEU_BOT_TOKEN
guild_id=SEU_GUILD_ID
role_id=SEU_ROLE_ID
secret_key=UMA_SECRET_KEY_ALEATORIA
```

---

## Como Usar

```bash
python main.py
```

Acesse [http://localhost:5000](http://localhost:5000) e clique em **Entrar com Discord**.

---

## Estrutura do Projeto

```text
OAuth Bot/
├── main.py
├── requirements.txt
└── README.md
```

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## Licença

Este projeto está sob a licença MIT.

---

<div align="center">
  <sub>Feito com ❤️ por <a href="https://github.com/171ntw">Nathan</a></sub>
</div>
