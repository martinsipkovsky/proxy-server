from datetime import datetime


class Logger():
    def __init__(self, path='logs/', debug=False):
        self.path = path
        self.init_datetime = self.get_datetime()
        self.debug = debug
        self.filename = self.path+self.init_datetime+'.log'

        # create new log file
        with open(self.filename, 'w') as logfilehandle:
            logfilehandle.write('LOG FILE FROM '+self.init_datetime)
            if self.debug:
                print(f'Created log file {self.path}{self.init_datetime}')
    
    def get_datetime(self):
        return str(datetime.now().strftime("%m%d%Y%H%M%S"))
    
    def get_datetime_for_log(self):
        return str(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

    def log(self, msg):
        with open(self.filename, 'a') as logfilehandle:
            logfilehandle.write(f'{self.get_datetime_for_log()} - {msg}\n')
            if self.debug:
                print(f'{self.get_datetime()} - {msg}')