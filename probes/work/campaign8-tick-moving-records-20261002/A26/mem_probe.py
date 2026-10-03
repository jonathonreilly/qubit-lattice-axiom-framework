import os, resource, signal
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"): os.environ[_v]="1"
signal.alarm(58)
def rss(tag): print("%-28s maxrss %.0f MB" % (tag, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576))
import numpy as np; rss("numpy")
from rs2d import Walk2D, packet, centroid; rss("import rs2d (scipy)")
Lx, Ly = 480, 640
U = 2e-4*(np.ones((Lx,1))*(np.arange(Ly)[None,:]/2.0) - 160)
W = Walk2D(Lx, Ly, 0.4, N=1-U, hxx=2*U, hyy=2*U, mu=0.15, rule='field'); rss("Walk2D init")
psi = packet(Lx, Ly, (120,160), (0.29,0), 36.0, 0.4, mu=0.15); rss("packet")
for t in range(20): psi = W.step(psi)
rss("20 steps")
