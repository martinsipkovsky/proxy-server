import yaml

def read_config():
    with open("./config.yml") as configfilehandle:
        return yaml.safe_load(configfilehandle)

def read_db():
    with open("./db.yml") as configfilehandle:
        return yaml.safe_load(configfilehandle)