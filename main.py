import streamlit as st
import websocket
import threading
import json
import time
import requests
from dotenv import load_dotenv
import os
import plotly.graph_objects as go
from datetime import datetime

# Charger les variables du fichier .env
load_dotenv()
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

# ---------------- Configuration ----------------
st.set_page_config(page_title="📈 Suivi Boursier Live", layout="centered")
st.title("📡 Visualisation en temps réel des actions")

# ---------------- Fonctions ----------------
@st.cache_data(ttl=3600)
def get_usd_to_eur_rate():
    try:
        r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=EUR")
        return r.json()["rates"]["EUR"]
    except:
        return 0.92  # fallback

# ---------------- UI ----------------
# Historique local du prix pour le graphique
historique = []

symbol = st.text_input("🎯 Symbole boursier (ex: NVDA, AAPL, TSLA)", "NVDA")
devise = st.selectbox("💱 Devise d'affichage :", ["USD ($)", "EUR (€)"])
start_button = st.button("🚀 Lancer la surveillance")

price_placeholder = st.empty()
status_placeholder = st.empty()
graph_placeholder = st.empty()

latest_price = {"value": None}
taux_eur = get_usd_to_eur_rate()

# ---------------- WebSocket ----------------
def on_message(ws, message):
    data = json.loads(message)
    if "data" in data:
        price = data["data"][0]["p"]
        latest_price["value"] = price

def on_open(ws):
    ws.send(json.dumps({
        "type": "subscribe",
        "symbol": symbol
    }))

def run_websocket():
    url = f"wss://ws.finnhub.io?token={FINNHUB_API_KEY}"
    ws = websocket.WebSocketApp(url, on_message=on_message, on_open=on_open)
    ws.run_forever()

# ---------------- Lancement ----------------
if start_button:
    ws_thread = threading.Thread(target=run_websocket)
    ws_thread.daemon = True
    ws_thread.start()

    while True:
        if latest_price["value"] is not None:
            prix = latest_price["value"]

            if devise == "USD ($)":
                display_price = f"${prix:.2f}"
                prix_plot = prix
            else:
                prix_plot = prix * taux_eur
                display_price = f"{prix_plot:.2f} €"

            # Stocker le point actuel
            historique.append((datetime.now(), prix_plot))

            # 🔄 Limiter à 100 points pour éviter lenteurs
            if len(historique) > 100:
                historique = historique[-100:]

            # Afficher le prix
            price_placeholder.metric(label=f"📊 Prix actuel de {symbol}", value=display_price)

            # 🔥 Afficher le graphique sexy avec Plotly (dézoomé)
            times, values = zip(*historique)
            ymin = min(values) * 0.995
            ymax = max(values) * 1.005

            fig = go.Figure(data=[go.Scatter(
                x=times,
                y=values,
                mode='lines+markers',
                line=dict(color='#00cc96')
            )])

            fig.update_layout(
                template="plotly_dark",
                margin=dict(l=30, r=30, t=30, b=30),
                xaxis_title="Heure",
                yaxis_title=f"Prix ({devise[-2:]})",
                height=400,
                font=dict(color="white"),
                yaxis=dict(range=[ymin, ymax])
            )

            graph_placeholder.plotly_chart(fig, use_container_width=True)
        else:
            price_placeholder.info("🔄 En attente de données...")

        time.sleep(1)
