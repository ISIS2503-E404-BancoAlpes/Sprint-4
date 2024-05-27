import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno del archivo .env

from app import app

if __name__ == '__main__':
    app.run(debug=True)
