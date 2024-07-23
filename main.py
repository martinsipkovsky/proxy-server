from web_server import app
import threading
from config_read import read_config
from tor import Tor
from logger import Logger

running = True

#create LOGGER object
logger = Logger(debug=True)


# create TOR object
#tor = Tor(logger=logger)
#tor.start_tor()


if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(host=read_config()['web']['host'], port=read_config()['web']['port'], debug=True, use_reloader=False)).start()

    while running:
        pass