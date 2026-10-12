"""F2 (lane RFW), part 1: the O(kappa^2) Noether condition in the translation-Killing sector,
reduced exactly to its 1-jet at zero momentum transfer, solved as a linear system.

Setting: K2's Z^4 free scalar + lattice FP + -(kappa/2) sum h T (exact through O(kappa)).
Most general O(kappa^2) completion in the h*phi*phi sector (field-dependent generators):
  dh   = D xi + kappa A_xi h + kappa^2 X_xi(phi,phi) + ...      (A_xi includes D lambda(xi,h))
  dphi = kappa L_xi phi + kappa^2 B_xi(h,phi) + ...              (B includes L_lambda(xi,h) phi)
  S    = S_FP + S_m - (kappa/2) sum h T + kappa S_hhh + kappa^2 S_hhphiphi + ...
Order kappa^2, sector xi*h*phi*phi, xi = c (constant translation, a Killing field):
  - seagull: delta0 h = D c = 0  -> drops;
  - B: multiplies E(k1) or E(k2) -> vanishes on the complex shell E(k1)=E(k2)=0;
  - X: enters as K(q)^T X(k1,k2) = O(|q|^2) (K is a sum of products of two differences);
  - left: Y(q;p) = i c.(f(p)+f(k2)) WT(p,k2) + A_c(q)^T WT(p,k2),  k2 = -p-q, both on shell.
Necessary condition (any range r, any C^1 symbol A_c): Y = O(|q|^2) along the shell, i.e.
  (Z)  A0^T WT(p,-p) = 0
  (F)  sum_mu t_mu M_mu^T WT(p,-p) + A0^T dWT[t] = i (c.grad f(p) t) WT(p,-p)  for t . grad E(p) = 0
with A0 = A_c(0), M_mu = dA_c/dq_mu(0) arbitrary complex 10x10 matrices (relaxation: the
O(kappa) requirement that A_c be an FP symmetry is NOT imposed, which can only help existence).
The system decouples per output component a: unknowns A0[:,a], M_mu[:,a] (50 per a).
"""
import numpy as np
from f2_common import *

rng = np.random.default_rng(2026)
c_dir = 0          # translation direction (all axes equivalent on Z^4)


def build(lattice, m2, npts, kill_cos=False):
    Tc = T_lat_cross if lattice else T_con_cross
    dTc = dT_lat_dk2 if lattice else dT_con_dk2
    df = df_lat if lattice else df_con
    rows = [[] for _ in range(NC)]
    rhs = [[] for _ in range(NC)]
    for _ in range(npts):
        p = shell_point(rng, m2, lattice)
        n = 2 * np.sin(p) if lattice else 2 * p
        T0 = W * Tc(p, -p, m2)
        J = W[:, None] * dTc(p, -p, m2)          # d WT(p,k2)/dk2 at k2=-p
        scale = 1.0 / np.linalg.norm(T0)
        for a in range(NC):
            # zeroth order
            r = np.zeros(50, dtype=complex); r[:10] = T0
            rows[a].append(r * scale); rhs[a].append(0.0)
        for t in tangent_basis(n, rng):
            dT = -J @ t                           # d/ds WT(p, -p - s t)
            g = df(p)[:, c_dir] @ t               # c.grad f(p) t  with grad f_c
            if kill_cos:                          # diagnostic: replace cos p_c by 1 (no Leibniz defect)
                g = t[c_dir]
            for a in range(NC):
                r = np.zeros(50, dtype=complex)
                r[:10] = dT
                for mu in range(D):
                    r[10 + 10 * mu: 20 + 10 * mu] = t[mu] * T0
                rows[a].append(r * scale); rhs[a].append(1j * g * T0[a] * scale)
    return [np.array(R) for R in rows], [np.array(b) for b in rhs]


def solve(rows, rhs, mask=None):
    res, tot, ranks = 0.0, 0.0, []
    per = []
    for a in range(NC):
        G, b = rows[a], rhs[a]
        if mask is not None:
            G = G[:, mask]
        u, *_ = np.linalg.lstsq(G, b, rcond=None)
        ra = np.linalg.norm(G @ u - b)
        res += ra ** 2; tot += np.linalg.norm(b) ** 2
        per.append(ra / max(np.linalg.norm(b), 1e-300))
        ranks.append(np.linalg.matrix_rank(G, tol=1e-9 * np.linalg.norm(G, 2)))
    return np.sqrt(res / tot), per, ranks


print("== F2 jet system: O(kappa^2) translation-Killing sector, 1-jet at q=0 on the complex shell ==")
print("columns: relative residual min_u ||G u - b|| / ||b|| over all 10 output components;")
print("         rank of G per component (max 50 = 10 A0 + 40 M entries)\n")
NP = 200
for lattice, name in ((False, "continuum/SLAC control"), (True, "K2 lattice scalar")):
    for m2 in (0.0, 0.25, 1.0, 3.0):
        rows, rhs = build(lattice, m2, NP)
        full, per, ranks = solve(rows, rhs)
        mask0 = np.zeros(50, bool); mask0[:10] = True      # r = 0: on-site A only (M = 0)
        r0, _, _ = solve(rows, rhs, mask0)
        print(f"{name:24s} m2={m2:4.2f}: residual(any r>=1) = {full:.3e}   residual(r=0) = {r0:.3e}   "
              f"rank/50 per comp = {sorted(set(ranks))}")
        if lattice and m2 == 1.0:
            print("     per-component residuals (a=(m,n)):",
                  ", ".join(f"{COMPS[a]}:{per[a]:.2f}" for a in range(NC)))

print("\n== natural candidate (no fit): A_c with 1-jet = translation of h, i.e. A0 = 0, M_mu = i delta_{mu c} 1")
print("   (e.g. A_c = i sin q_c or exp(i q_c) - 1: identical 1-jets)")
for lattice in (False, True):
    rows, rhs = build(lattice, 1.0, 100)
    num = den = 0.0
    for a in range(NC):
        ua = np.zeros(50, dtype=complex); ua[10 + 10 * c_dir + a] = 1j
        num += np.linalg.norm(rows[a] @ ua - rhs[a]) ** 2; den += np.linalg.norm(rhs[a]) ** 2
    print(f"  {'lattice' if lattice else 'continuum':9s} m2=1: rel. residual = {np.sqrt(num/den):.3e}")

print("\n== diagnostic: lattice T and shell, but the Leibniz factor cos p_c in the defect replaced by 1 ==")
for m2 in (0.25, 1.0):
    rows, rhs = build(True, m2, NP, kill_cos=True)
    full, per, ranks = solve(rows, rhs)
    print(f"  m2={m2}: residual(any r>=1) = {full:.3e}  -> the cos k_c (Leibniz) factor is the whole obstruction")

print("\n== rank of the jet map  (range-r coefficients of A_c) -> (A0, M_mu) ==")
for r in range(0, 4):
    offs = [o for o in np.ndindex(*(2 * r + 1,) * D) if np.sum(np.abs(np.array(o) - r)) <= r]
    offs = np.array(offs) - r
    Jm = np.vstack([np.ones(len(offs))] + [1j * offs[:, mu] for mu in range(D)])
    print(f"  r={r}: l1-ball offsets {len(offs):4d}, unknowns per (b,a) entry {len(offs):4d}; "
          f"rank of jet map per entry = {np.linalg.matrix_rank(Jm)} (5 = surjective onto A0, M_0..M_3)")
print("=> for every r >= 1 the reachable jets are ALL (A0, M); the jet-system residual above is the")
print("   residual for every finite range r (and for any C^1 symbol); r = 0 reaches A0 only.")
