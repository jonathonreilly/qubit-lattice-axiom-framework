"""A53 t3_once16: 16-site and 24-site wrap diagnostics.  (1) 16 sites: GS and parton under the 'pair-once' bilinear
convention (shortest displacement, counted once; star four-spin terms as wrapped).  (2) Duplicate star four-sets on
16 / 24 sites (count distinct vs 35 N).  Usage: t3_once16.py"""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(250)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
t0 = time.time()
for nm, T in (("16", [[2, 2, 0], [2, 0, 2], [0, 2, 2]]), ("24", [[2, 0, 2], [-2, 2, 2], [0, -2, 2]])):
    cl = Cluster(np.array(T)); N = cl.N; X = [np.array(s) for s in cl.sites]; f = periodic_index(cl)
    ks, J, c4 = load_rule(6, "B4_r4")
    print(f"[{nm}] distinct star four-sets {len(four_sets(X, f, c4))} of 35N = {35*N}; pairs wrapped {len(bilinear_pairs(X, f, ks, J))}, once {len(bilinear_pairs_once(X, f, ks, J))}", flush=True)
    if nm != "16": continue
    S = Sector(N, flip=False); p = parton_vector(cl, S).real; p /= np.linalg.norm(p)
    for once in (False, True):
        H = Ham(X, f, ks, J, c4, once=once); mv = make_mv(H, S)
        op = sla.LinearOperator((S.D, S.D), matvec=mv, dtype=float); w, U = sla.eigsh(op, k=3, which='SA', tol=1e-10)
        o = np.argsort(w); w, U = w[o], U[:, o]; g = U[:, 0]; C = paircorr(g, S)
        print(f"  once={once}: E0/N {w[0]/N:+.5f} (next {w[1]/N:+.5f}); parton <H>/N {p @ mv(p)/N:+.5f}; gap {p @ mv(p)/N - w[0]/N:+.4f}; "
              f"|<GS|parton>|^2 {(g @ p)**2:.3e}; GS S check {C.sum()/4:.1e}  [{time.time()-t0:.0f}s]", flush=True)
