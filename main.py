from flask import Flask, redirect, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = os.getenv("redirect_uri")
bot_token = os.getenv("bot_token")
guild_id = os.getenv("guild_id")
role_id = os.getenv("role_id")
api_base_url = "https://discord.com/api"

@app.route("/")
def home():
    return '<a href="/login">Entrar com Discord</a>'

@app.route("/login")
def login():
    return redirect(
        f"{api_base_url}/oauth2/authorize"
        f"?client_id={client_id}"
        f"&redirect_uri={redirect_uri}"
        f"&response_type=code"
        f"&scope=identify%20guilds.join%20email"
    )

@app.route("/callback")
def callback():
    code = request.args.get("code")
    if not code:
        return "Erro: Código de autorização não encontrado."

    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "scope": "identify guilds.join"
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    token_res = requests.post(f"{api_base_url}/oauth2/token", data=data, headers=headers)

    if token_res.status_code != 200:
        return f"Erro ao obter token: {token_res.text}"

    token_json = token_res.json()
    access_token = token_json.get("access_token")

    user_res = requests.get(
        f"{api_base_url}/users/@me",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    if user_res.status_code != 200:
        return f"Erro ao obter usuário: {user_res.text}"

    user = user_res.json()

    add_member_url = f"{api_base_url}/guilds/{guild_id}/members/{user['id']}"
    bot_headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }

    body = {
        "access_token": access_token,
        "roles": [role_id] if role_id else []
    }

    add_res = requests.put(add_member_url, headers=bot_headers, json=body)

    if add_res.status_code in (201, 204):
        return user
    else:
        return f"❌ Falha ao adicionar usuário ao servidor: {add_res.text}"

if __name__ == "__main__":
    app.run(debug=True)