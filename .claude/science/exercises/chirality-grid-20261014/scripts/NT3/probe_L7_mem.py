import resource, time, numpy as np
from ed_core import Model, ring, lowest
from filters import ring_fvals
def rss(): return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6
L=7; m = Model(ring(L), ring_fvals("F_star", L)); print("model", rss(), "MB", flush=True)
t=time.time(); b = m.chain_sector((0,0,0,0), 0); print("dim", len(b), "rss", rss(), time.time()-t, flush=True)
t=time.time(); H = m.build_H(b); print("nnz", H.nnz, "rss", rss(), time.time()-t, flush=True)
t=time.time(); e,v = lowest(H, k=4); print("e", e, "rss", rss(), time.time()-t, flush=True)
