"""C5 R18-12 (a), all channels: which single quanta lie on the lower envelope of their (charge, crystal momentum) sector?

On an N = 24 grid (spacing 0.262, contains 0 and the corners) for one charged species f (+ its antiparticle, same band)
and one photon:
  neutral one/two-body: Omega1 = min(omega, pair = eps (+) eps), multi-body: Omega = min(Omega1, Omega1 (+) Omega1, ... (+) Omega1)
  (min-plus convolutions on the torus, the trivial Q = 0 / zero-energy emission removed).
  A quantum f(K) is grid-stable iff eps(K) <= min_k' [eps(k') + Omega(K - k')]  (no emission of any neutral set).
  A photon gamma(Q) is grid-stable iff omega(Q) <= min(pair(Q), (omega (+) Omega)(Q))  (no decay into >= 2 bodies).
Grid-stable is necessary-side evidence only (finer final states could open a channel); grid-OPEN is certified.
m = 0.01 stands for a physical light mass (m a << 1; m = 0 makes zero-energy pairs at k = 0 degenerate).
"""
import os, sys, time
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r1812_laws import Matter, omega, photon_delta, B, wrap

N = 24; H = N // 2
kg = -np.pi + 2*np.pi*np.arange(N)/N
KK = np.stack(np.meshgrid(kg, kg, kg, indexing='ij'), -1).reshape(-1, 3)
ar = np.arange(N)
lines = []
def pr(s=""):
    print(s, flush=True); lines.append(s)

def minplus(A, Bm):
    """C[i] = min_j A[j] + Bm[i - j]  (momentum index of k_i - k_j is (i - j + H) mod N)."""
    C = np.empty((N, N, N))
    for i0 in range(N):
        s0 = (i0 - ar + H) % N
        for i1 in range(N):
            s1 = (i1 - ar + H) % N
            for i2 in range(N):
                s2 = (i2 - ar + H) % N
                C[i0, i1, i2] = (A + Bm[np.ix_(s0, s1, s2)]).min()
    return C

zero = (H, H, H)
t0 = time.time()
for mname, ph, m in (('G', 'R85', 0.01), ('D1', 'R85', 0.01), ('G', 'std', 0.01), ('D1', 'std', 0.01), ('S', 'R85', 0.01), ('G', 'R85', 0.3)):
    mat = Matter(mname, m)
    Ef = mat.eps(KK).reshape(N, N, N); Wg = omega(ph, KK).reshape(N, N, N)
    P = minplus(Ef, Ef)                                    # f fbar pair with total momentum Q
    W1 = Wg.copy(); W1[zero] = np.inf                      # no zero-momentum photon
    Om1 = np.minimum(W1, P); Om1[zero] = min(P[zero], np.inf)
    Om2 = np.minimum(Om1, minplus(Om1, Om1))
    Om = np.minimum(Om2, minplus(Om2, Om1))                # up to 3+ neutral bodies (iterated)
    Om[zero] = np.min([Om[zero], P[zero]])
    F = minplus(Ef, Om)                                    # cheapest  f + neutral set
    G2 = np.minimum(P, minplus(W1, Om))                    # photon -> >= 2 bodies
    stab_f = (Ef <= F + 1e-12).reshape(-1); stab_g = (Wg <= G2 + 1e-12).reshape(-1)
    edge_f = (np.abs(KK) > B + 1e-9).any(1); edge_g = (np.abs(KK) > 1.0 + 1e-9).any(1)
    df = np.abs(mat.delta(KK)).max(1) > 1e-6; dg = np.abs(photon_delta(ph, KK)).max(1) > 1e-6
    ef = Ef.reshape(-1); wg = Wg.reshape(-1)
    sel_f = edge_f & df & stab_f; sel_g = edge_g & dg & stab_g
    pr("world %-2s + %-3s m=%.2f:" % (mname, ph, m))
    pr("   matter edge states: %d; grid-stable %d; defect-carrying & stable %d; lightest such eps = %s at K = %s"
       % (edge_f.sum(), (edge_f & stab_f).sum(), sel_f.sum(),
          ("%.4f" % ef[sel_f].min()) if sel_f.any() else "none", (np.round(KK[sel_f][np.argmin(ef[sel_f])], 3).tolist() if sel_f.any() else "-")))
    pr("   photon edge states: %d; grid-stable %d; defect-carrying & stable %d; lightest such omega = %s at Q = %s"
       % (edge_g.sum(), (edge_g & stab_g).sum(), sel_g.sum(),
          ("%.4f" % wg[sel_g].min()) if sel_g.any() else "none", (np.round(KK[sel_g][np.argmin(wg[sel_g])], 3).tolist() if sel_g.any() else "-")))
    corner = [(0, H, H), (0, 0, H), (0, 0, 0)]
    pr("   corner classes (pi,0,0),(pi,pi,0),(pi,pi,pi): eps_f %s stable_f %s | omega %s stable_g %s | neutral envelope %s"
       % ([round(Ef[c], 4) for c in corner], [bool(Ef[c] <= F[c] + 1e-12) for c in corner],
          [round(Wg[c], 4) for c in corner], [bool(Wg[c] <= G2[c] + 1e-12) for c in corner], [round(min(Om[c], Wg[c]), 4) for c in corner]))
    pr("   [%.0f s]" % (time.time() - t0))
open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w").write("\n".join(lines) + "\n")
