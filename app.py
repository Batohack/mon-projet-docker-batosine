from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Hacker's Terminal</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
                font-family: 'Courier New', Courier, monospace;
                overflow: hidden;
            }
            .message {
                color: #00ff00;
                font-size: 2.5em;
                text-align: center;
                text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
                padding: 20px;
                border: 2px solid #00ff00;
                border-radius: 10px;
                background: rgba(0, 0, 0, 0.8);
                animation: blurEffect 1s infinite alternate;
            }
            @keyframes blurEffect {
                0% {
                    filter: blur(0px);
                    text-shadow: 0 0 10px #00ff00;
                }
                100% {
                    filter: blur(5px);
                    text-shadow: 0 0 20px #00ff00, 0 0 30px #00ff00;
                }
            }
            .glitch {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: repeating-linear-gradient(
                    0deg,
                    transparent,
                    transparent 2px,
                    rgba(255, 255, 255, 0.1) 2px,
                    rgba(255, 255, 255, 0.1) 4px
                );
                opacity: 0.3;
                animation: glitchMove 0.5s infinite;
            }
            @keyframes glitchMove {
                0% { transform: translate(0, 0); }
                50% { transform: translate(2px, -2px); }
                100% { transform: translate(-2px, 2px); }
            }
        </style>
    </head>
    <body>
        <div class="glitch"></div>
        <div class="message">
            Accès non autorisé détecté... Bienvenue, BATO5INE, dans le réseau clandestin. Décryptez le code ou disparaissez.
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
