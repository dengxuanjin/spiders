import time
from datetime import datetime
time_str = time.localtime(16637149730000//10000)
dt_time = datetime.fromtimestamp(16637149730000//10000)
print(dt_time)