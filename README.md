# Real-Time-Stock-Visualizer
This project allows you to see in real time the variation of your actions.

Real-Time Stock Visualizer 📈 — Tutoriel complet (type “Prédiction S&P”)
### Objectif

Application Streamlit pour visualiser en quasi temps réel le cours d’un titre (ex. NVDA, AAPL, ^FCHI) et afficher des indicateurs techniques (SMA, EMA, RSI, Bandes de Bollinger, MACD). Idéal pour montrer une démarche data + marchés.

### Prérequis

Python 3.10+
macOS / Linux / Windows
Connexion internet (données Yahoo Finance via yfinance)
(Optionnel) clé API si tu remplaces la source de données plus tard

### Installation

# 1) Cloner le repo

  ```bash
  git clone https://github.com/<TON-USER>/<TON-REPO>.git
  cd <TON-REPO>
  ```

# 2) Créer l'environnement virtuel
  
  ```bash
  python -m venv .venv
  # macOS/Linux
  source .venv/bin/activate
  # Windows (PowerShell)
  # .venv\Scripts\Activate.ps1
  ```

# 3) Installer les dépendances
  
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  # si pas de requirements.txt, par défaut :
  # pip install streamlit yfinance pandas numpy matplotlib ta plotly
  ```
