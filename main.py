from web_server import app
import threading
from config_read import read_config

running = True



if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host=read_config()['web']['host'], port=read_config()['web']['port'], debug=True, use_reloader=False)).start()

    while running:
        pass