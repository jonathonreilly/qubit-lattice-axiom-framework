import numpy as np
exec(open('selftest.py').read().split('# 3. jam edge leak')[0].split('# 1. conservation')[0])
src = open('selftest.py').read()
part = src.split('# 3. jam edge leak, 2D square jam side 10 in empty 40x40, first tick only')[1].split('# 4. 3D cube')[0]
exec(part)
