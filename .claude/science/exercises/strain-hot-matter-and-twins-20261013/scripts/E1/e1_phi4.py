#!/usr/bin/env python3
"""E1 (B): 3D lattice phi^4, one loop (Hartree), hopping J_j = 1 + t_j, E_g stretch t = (t, -t, 0).
  m^2 = r + (lam/2) I(m^2, t),   I = < 1 / (m^2 + sum_j (1+t_j) e_j) >_BZ,   e_j = 2(1 - cos q_j).
Tree level / mean field: the critical point r_c = -(lam/2) I depends on sum_j J_j only through
the loop; sum_j t_j = 0, so the tree-level critical point does not move.
One loop: I(t) = I(0) + Q t^2 + O(t^4),  Q(m) = < (e1 - e2)^2 / (m^2 + E)^3 >  (first order vanishes
by the x<->y symmetry).  delta r_c = -(lam/2) Q(0) t^2;  at fixed bare r, delta m^2 = +(lam/2) Q(m) t^2.
Composite / block question: the share of Q from modes inside the block zone |q_j| < pi/b.
Midpoint grids N = 128, 256, 512 in q_x-slabs (memory: N^2 doubles per array), Richardson in 1/N.
"""
import numpy as np

def Qgrid(N, m2, bs=()):
    q = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    e = 2 * (1 - np.cos(q))
    e2 = e[:, None]; e3 = e[None, :]
    tot = 0.0; I0 = 0.0
    blk = {b: 0.0 for b in bs}
    inb = {b: (np.abs(q) < np.pi / b) for b in bs}
    for i in range(N):
        E = m2 + e[i] + e2 + e3                  # (N,N) slab: q1 fixed, q2 x q3
        num = (e[i] - e2) ** 2
        f = num / E**3
        tot += f.sum(); I0 += (1.0 / E).sum()
        for b in bs:
            if inb[b][i]:
                mk = inb[b][:, None] & inb[b][None, :]
                blk[b] += f[mk].sum()
    n3 = float(N) ** 3
    return tot / n3, I0 / n3, {b: v / n3 for b, v in blk.items()}

if __name__ == "__main__":
    bs = (2, 4, 8, 16, 32)
    print("(B1) critical point (m=0): Q(0) and block-zone shares; Richardson in h = 1/N (error ~ c1 h + c2 h^2)")
    res = {}
    for N in (128, 256, 512):
        res[N] = Qgrid(N, 0.0, bs)
        Q, I0, blk = res[N]
        print(f"  N={N}: Q={Q:.10f}  I(0)={I0:.10f}  " + "  ".join(f"Q_b{b}={blk[b]:.6e}" for b in bs))
    def rich(a1, a2, a4):   # values at h, h/2, h/4 with error c1 h + c2 h^2
        r1 = 2 * a2 - a1; r2 = 2 * a4 - a2
        return (4 * r2 - r1) / 3
    Qx = rich(res[128][0], res[256][0], res[512][0])
    Ix = rich(res[128][1], res[256][1], res[512][1])
    print(f"  extrapolated: Q(0) = {Qx:.8f}   I(0) = {Ix:.8f}  (Watson W = I(0)/... comparator: <1/E> = 0.252731 RECALLED)")
    print("  block-zone share of Q (fine modes carry the rest):  b, Q_block (extrap), share, b*Q_block")
    for b in bs:
        qb = rich(res[128][2][b], res[256][2][b], res[512][2][b])
        print(f"   b={b:2d}: {qb:.6e}   share={qb/Qx:.4e}   b*Q_block={b*qb:.6f}")
    print("  delta r_c(t) = -(lam/2) Q(0) t^2 = " + f"{-0.5*Qx:.6f} lam t^2 (lattice units a=1, J=1)")
    print("\n(B2) off-critical start m0 = 1/xi0: delta m^2 at fixed bare r = (lam/2) Q(m0) t^2;  N=256 and 512")
    for m in (0.3, 0.1, 0.03, 0.01):
        a = Qgrid(256, m * m)[0]; b_ = Qgrid(512, m * m)[0]
        print(f"   xi0={1/m:7.1f}: Q(m0) N256 {a:.8f}  N512 {b_:.8f}   (Q(0)-Q(m0))/m0 = {(Qx-b_)/m:.5f}   relative shift dm^2/(m0^2 t^2) = (lam/2)*{b_/m**2:.4e}")
