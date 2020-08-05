import json
from pathlib import Path

DB_FILENAME = 'RayInfoCore.db'

class AppConfig():

    def __init__(self) -> None:
        self.config = self._load_config()
        self._check_config()

        self.data_path = self.config['dataPath']
        print("dataPath = %s" % self.data_path)
        self.create_data_dir_if_not_exist()

    def get_db_path(self):
        return str(
            Path(self.data_path) \
                .joinpath(DB_FILENAME) \
                .expanduser()
        )


    def _load_config(self):
        # todo: search home dir if not assigned
        # todo: assign by cmd params
        # todo: exit app if config not found
        with open('./config.json', 'r') as f:
            return json.load(f)
    
    def _check_config(self):
        if self.config == None:
            print('Config.json not found')
            exit(0)
    
    def create_data_dir_if_not_exist(self):
        Path(self.data_path).expanduser().mkdir(parents=True, exist_ok=True)


