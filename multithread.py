import datetime
import random
import sys
import math

from typing import List, Generator, NewType

repeat: int = 200

def convert_size(size_bytes: int) -> str:
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

start_time = datetime.datetime.now()

random_val = (random.randrange(1, 100) for i in range(repeat))
list_size = sys.getsizeof(random_val)
print('generator validation:')
for i in range(repeat):
   print(next(random_val))

end_time = datetime.datetime.now()

total_time = end_time - start_time
print('it took %s to complete the script' % (total_time))
print('list consumes %s of memory' % (convert_size(list_size)))