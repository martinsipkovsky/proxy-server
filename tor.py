import platform
import subprocess

PLATFORM = platform.system().upper()


class Tor():
    def __init__(self, logger):
        self.logger = logger
        self.logger.log(f'[TOR] Running TOR for {PLATFORM}')

        if PLATFORM == 'WINDOWS':
            pass
        elif PLATFORM == 'LINUX':
            pass
        else:
            self.logger.log(f"[TOR] {PLATFORM} is not supported by this version of software.")
    
    def start_tor(self):
        if PLATFORM == 'WINDOWS':
            # start tor service
            with subprocess.Popen(['start', 'tor/tor/tor.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p:
                out, err = p.communicate()
                for line in out:
                    self.logger.log('[TOR] ' + str(line.decode('utf-8')))
                for line in err:
                    self.logger.log('[TOR] ' + str(line.decode('utf-8')))
        elif PLATFORM == 'LINUX':
            # start tor service
            p = subprocess.Popen(['service', 'tor', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out, err = p.communicate()
            if out:
                self.logger.log('[TOR] ' + str(out.decode('utf-8')))
            if err:
                self.logger.log('[TOR] ' + str(err.decode('utf-8')))
        else:
            self.logger.log(f"[TOR] {PLATFORM} is not supported by this version of software.")