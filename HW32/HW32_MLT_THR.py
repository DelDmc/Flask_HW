import matplotlib.pyplot as plt

import os
import time
import random
import string
import requests
from multiprocessing.pool import ThreadPool


def my_fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)


logger = {}


# context manager
class timer:
    def __init__(self, message, workers, data_size):
        self.message = message
        self.workers = workers
        self.data_size = data_size

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        logger[self.workers] = elapsed_time
        print(self.message.format(elapsed_time))


for i in range(1, 601):

    workers = i * 8
    if workers < 601:
        DATA_SIZE = 600
        with timer('Elapsed: {}s', workers, DATA_SIZE):
            with ThreadPool(workers) as pool:
                input_data = [DATA_SIZE // workers for _ in range(workers)]
                pool.map(my_fetch_pic, input_data)

print(logger)
data = logger
lists = sorted(data.items())

x, y = zip(*lists)
plt.plot(x, y)
plt.show()

"""
data = {
8: 11.01650881767273, 
16: 5.799861431121826, 
24: 5.237547397613525, 
32: 3.9622373580932617, 
40: 3.589170217514038, 
48: 3.879077196121216, 
56: 3.278630256652832, 
64: 4.327832221984863, 
72: 3.5521469116210938, 
80: 4.069812536239624, 
88: 4.500477313995361, 
96: 2.897660493850708, 
104: 2.977818489074707, 
112: 3.5874340534210205, 
120: 3.051974296569824, 
128: 2.732422351837158, 
136: 3.47836971282959, 
144: 3.1043858528137207, 
152: 2.2576863765716553, 
160: 2.5470077991485596, 
168: 2.4638760089874268, 
176: 2.61960768699646, 
184: 2.721304416656494, 
192: 2.863743782043457, 
200: 2.9785213470458984, 
208: 2.1105024814605713, 
216: 2.230379343032837, 
224: 2.55916428565979, 
232: 2.572206497192383, 
240: 2.627713680267334, 
248: 2.482638359069824, 
256: 2.6529314517974854, 
264: 2.5618598461151123, 
272: 2.7127575874328613, 
280: 2.7122926712036133, 
288: 2.7936458587646484, 
296: 3.082423686981201, 
304: 1.873159646987915, 
312: 2.173156499862671, 
320: 1.534827470779419, 
328: 1.5819697380065918, 
336: 2.001096725463867, 
344: 2.8030333518981934, 
352: 1.6946568489074707, 
360: 1.87898850440979, 
368: 1.7560734748840332, 
376: 1.8229405879974365, 
384: 1.898960828781128, 
392: 1.930208683013916, 
400: 2.418156623840332, 
408: 1.9993064403533936, 
416: 2.022893190383911, 
424: 2.8952083587646484, 
432: 2.946730852127075, 
440: 2.1946394443511963, 
448: 2.347318172454834, 
456: 2.4350407123565674, 
464: 2.308474063873291, 
472: 2.4871060848236084, 
480: 2.325098752975464, 
488: 2.364291191101074,
496: 2.612354278564453, 
504: 2.4603962898254395, 
512: 3.141721487045288, 
520: 2.5446617603302, 
528: 3.450773000717163, 
536: 2.624086618423462, 
544: 2.6526362895965576, 
552: 2.7570886611938477, 
560: 2.861103057861328, 
568: 2.8163833618164062, 
576: 2.8105547428131104, 
584: 2.929454803466797, 
592: 3.0075271129608154, 
600: 2.9513120651245117
}
"""
