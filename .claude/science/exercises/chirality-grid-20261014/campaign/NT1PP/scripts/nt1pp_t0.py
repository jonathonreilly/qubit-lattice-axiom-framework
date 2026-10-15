"""NT-1'' T0: timing/memory probe at a given (Lx, T) on the F = 0 background; prints timing and gmin only (no physics numbers).
usage: python3 nt1pp_t0.py Lx T"""
import sys, time, resource
import numpy as np
from nt1pp_common import *
Lx, T = int(sys.argv[1]), int(sys.argv[2]); t0 = time.time()
S = Strip(Lx, T); t1 = time.time()
MS = Measure(S, '11112', Ns=8); A = uniformW(S, 0.3)
r = MS.ray(A, 8); t2 = time.time()
print(f"Lx={Lx} Lt={2*T} N={S.N} nl={S.nl}: Strip build {t1-t0:.1f}s, one 11112 ray (Ns=8, 1 config) {t2-t1:.1f}s; gmin {r['gmin']:.3f} idx_ok {r['idx_ok']}; "
      f"maxrss {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
