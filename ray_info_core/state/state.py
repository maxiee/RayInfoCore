from pathlib import Path

class State:
    data_path = None
    config = None
    db_filename = 'RayInfoCore.db'

    def get_db_path(self):
        db_path = Path(self.data_path) \
            .joinpath(self.db_filename) \
            .expanduser()
        return str(db_path)

app_state = State()
