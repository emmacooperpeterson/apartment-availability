from check_availabilities import *
from config import CONFIG
from datetime import date
import json

filename = f"availabilities_{date.today().strftime('%Y-%m-%d')}.json"

availabilities = {}

for name, info in CONFIG.items():
    fn_string = f"{info['function']}(**{info['args']})"
    is_any_available = eval(fn_string)
    availabilities[name] = is_any_available

with open(filename, "w") as f:
    json.dump(availabilities, f)
