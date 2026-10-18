"""M2 check on the L=128 run (addendum 2). Reads complete records only, so it can run on a partial file."""
import numpy as np, io, contextlib, sys
import mcrg
raw=np.fromfile('data/s4_L128.bin'); rec=4+15*4; n=(raw.size//rec)//mcrg.NJ*mcrg.NJ
raw[:n*rec].tofile('data/s4_L128_cut.bin'); print('measurements used:',n)
mcrg.run('data/s4_L128_cut.bin',4,[1,2,3],'L128')
