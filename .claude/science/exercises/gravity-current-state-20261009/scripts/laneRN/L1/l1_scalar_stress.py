"""Lane RN / L1: free lattice scalar on Z^3 coupled to the exact-constraint VS (H_N) theory.

Checks (all on random phase-space points of a periodic L^3 torus; every density is a
quadratic form, so ddt f = (f(x+xdot) - f(x-xdot))/2 is EXACT, no step error):

 (E) energy continuity  dT00(x)/dt = sum_j [P_j(x) - P_j(x-e_j)]
     T00 at sites, P_j on edge (x,x+e_j)  -- same P_j that enters the momentum constraint
 (M) momentum continuity dP_j/dt = T_jj(x+e_j)-T_jj(x) + sum_{i!=j}[T_ij(x)-T_ij(x-e_i)]
     T_jj at sites, T_ij (=T_ji) on the ij face at x: exactly the 09-14 G-stencil
 gravity identities with the 09-14 integer stencils:  S(qdot) = -J div G(p),  G S^T = 0,
     S G^T = 0  (so lapse/shift terms preserve the constraints)
 -> first-class closure at O(sqrt kappa).
"""
import numpy as np

rng = np.random.default_rng(20261010)
L = 6
AX = (0, 1, 2)


def sh(f, j, s):
    """f(x + s e_j) on the torus."""
    return np.roll(f, -s, axis=j)


def d(f, j):
    return sh(f, j, 1) - f


def lap(f):
    return sum(sh(f, j, 1) + sh(f, j, -1) - 2 * f for j in AX)


def eom(phi, pi, m):
    return pi, lap(phi) - m * m * phi


def T00(phi, pi, m):
    t = 0.5 * pi**2 + 0.5 * m * m * phi**2
    for j in AX:
        dj = d(phi, j)
        t = t + 0.25 * (dj**2 + sh(dj, j, -1) ** 2)
    return t


def P(phi, pi, m):
    return [0.5 * (pi + sh(pi, j, 1)) * d(phi, j) for j in AX]


def Tdiag(phi, pi, m):
    out = []
    for j in AX:
        dj = d(phi, j)
        t = 0.5 * pi**2 - 0.5 * m * m * phi**2 + 0.5 * dj * sh(dj, j, -1)
        for i in AX:
            if i != j:
                di = d(phi, i)
                t = t - 0.25 * (di**2 + sh(di, i, -1) ** 2)
        out.append(t)
    return out


def Toff(phi, pi, m):
    """T_ij on face at x spanned by e_i,e_j (centre x+(e_i+e_j)/2); dict keyed (i,j), i<j."""
    out = {}
    for i in AX:
        for j in AX:
            if i < j:
                di, dj = d(phi, i), d(phi, j)
                out[(i, j)] = 0.25 * (di + sh(di, j, 1)) * (dj + sh(dj, i, 1))
    return out


def ddt(fun, phi, pi, m):
    """exact time derivative of a quadratic density (polarization identity)."""
    a, b = eom(phi, pi, m)
    fp = fun(phi + a, pi + b, m)
    fm = fun(phi - a, pi - b, m)
    if isinstance(fp, list):
        return [(x - y) / 2 for x, y in zip(fp, fm)]
    if isinstance(fp, dict):
        return {k: (fp[k] - fm[k]) / 2 for k in fp}
    return (fp - fm) / 2


def Gstencil(diag, off):
    """09-14 note: (G p)_j(x) = p_jj(x+e_j)-p_jj(x) + sum_{i!=j}[p_ij(x)-p_ij(x-e_i)]."""
    out = []
    for j in AX:
        g = sh(diag[j], j, 1) - diag[j]
        for i in AX:
            if i != j:
                pij = off[(min(i, j), max(i, j))]
                g = g + pij - sh(pij, i, -1)
        out.append(g)
    return out


def check_matter(m, ntrial=4):
    worstE = worstM = 0.0
    scale = 0.0
    for _ in range(ntrial):
        phi = rng.standard_normal((L, L, L))
        pi = rng.standard_normal((L, L, L))
        dT = ddt(T00, phi, pi, m)
        Pj = P(phi, pi, m)
        divP = sum(Pj[j] - sh(Pj[j], j, -1) for j in AX)
        worstE = max(worstE, np.max(np.abs(dT - divP)))
        dP = ddt(P, phi, pi, m)
        GT = Gstencil(Tdiag(phi, pi, m), Toff(phi, pi, m))
        worstM = max(worstM, max(np.max(np.abs(dP[j] - GT[j])) for j in AX))
        scale = max(scale, np.max(np.abs(dT)), max(np.max(np.abs(x)) for x in dP))
        # sum T00 = H_m
        Hm = 0.5 * np.sum(pi**2) + 0.5 * m * m * np.sum(phi**2) + 0.5 * sum(np.sum(d(phi, j) ** 2) for j in AX)
        assert abs(np.sum(T00(phi, pi, m)) - Hm) < 1e-10 * Hm
    return worstE, worstM, scale


print("=== (E),(M) exact lattice identities, free scalar, L=%d torus, random points ===" % L)
for m in (0.0, 0.7, 2.3):
    e, mm, s = check_matter(m)
    print(f"m={m:4.1f}: max|dT00/dt - div P| = {e:.2e}   max|dP/dt - G[T]| = {mm:.2e}   (field scale {s:.1f})")

# ---- a deliberately wrong placement to show the identities are not vacuous ----
def T00_bad(phi, pi, m):  # gradient energy of link (x,x+e_j) all on x
    return 0.5 * pi**2 + 0.5 * m * m * phi**2 + 0.5 * sum(d(phi, j) ** 2 for j in AX)


def P_fwd(phi, pi, m):  # pi_x * forward difference: a 'canonical' guess
    return [pi * d(phi, j) for j in AX]


phi = rng.standard_normal((L, L, L)); pi = rng.standard_normal((L, L, L)); m = 0.7
a, b = eom(phi, pi, m)
dPf = ddt(P_fwd, phi, pi, m)
tot = [np.sum(x) for x in dPf]
print("control: d/dt sum_x pi*forward-diff phi =", np.round(tot, 3), "(nonzero: not conserved, so no stress exists for it)")
dPs = ddt(P, phi, pi, m)
print("         d/dt sum_x P_j (ours)          =", [f"{np.sum(x):.1e}" for x in dPs])

# ---- angular momentum: implied by symmetric T; check d/dt sum (x_i P_j - x_j P_i) on an open patch is not needed;
# instead verify T_ij symmetric by construction (single face object) and print continuum limit check
print("\n=== continuum limit of T_ij on a smooth plane wave (k small) ===")
k = np.array([0.05, 0.03, -0.02])
X = np.indices((L, L, L)).astype(float)
# use a long torus for smooth field? just check symbols analytically:
s = 2 * np.sin(k / 2)
w2 = m * m + np.sum(s**2)
print("per-quantum T_jj symbol sin^2 k_j/omega vs continuum k_j^2/omega:",
      np.round(np.sin(k) ** 2 / np.sqrt(w2), 8), np.round(k**2 / np.sqrt(m * m + k @ k), 8))

# ---- gravity sector with the 09-14 integer stencils ----
print("\n=== gravity: 09-14 stencils (q diag at sites, q_ij doubled on faces) ===")
Lg = 5
def Sq(qd, qo):
    s = np.zeros((Lg,) * 3)
    for j in AX:
        for i in AX:
            if i != j:
                s = s + sh(qd[j], i, 1) + sh(qd[j], i, -1) - 2 * qd[j]
    for (i, j), q in qo.items():
        s = s - (q - sh(q, i, -1) - sh(q, j, -1) + sh(sh(q, i, -1), j, -1))
    return s

def Gp(pd, po):
    out = []
    for j in AX:
        g = sh(pd[j], j, 1) - pd[j]
        for i in AX:
            if i != j:
                pij = po[(min(i, j), max(i, j))]
                g = g + pij - sh(pij, i, -1)
        out.append(g)
    return out

Jc = 2.0  # J = 2 kappa with kappa = 1
pd = [rng.standard_normal((Lg,) * 3) for _ in AX]
po = {(i, j): rng.standard_normal((Lg,) * 3) for i in AX for j in AX if i < j}
trp = sum(pd)
qdot_d = [Jc * (pd[j] - 0.5 * trp) for j in AX]      # dq_ii/dt = dK/dp_ii
qdot_o = {k_: 2 * Jc * v for k_, v in po.items()}      # dq_ij/dt = 2 J p_ij (q_ij = 2h_ij)
lhs = Sq(qdot_d, qdot_o)
G = Gp(pd, po)
divG = sum(G[j] - sh(G[j], j, -1) for j in AX)
print("max|S(qdot) + J div G| =", f"{np.max(np.abs(lhs + Jc * divG)):.2e}", " (scale", f"{np.max(np.abs(lhs)):.1f})")

# build S and G as matrices to test G S^T = 0 and S G^T = 0
nsl = 6 * Lg**3
def unpack(v):
    v = v.reshape(6, Lg, Lg, Lg)
    return [v[0], v[1], v[2]], {(0, 1): v[3], (1, 2): v[4], (0, 2): v[5]}
Smat = np.zeros((Lg**3, nsl)); Gmat = np.zeros((3 * Lg**3, nsl))
for a_ in range(nsl):
    e = np.zeros(nsl); e[a_] = 1
    dd, oo = unpack(e)
    Smat[:, a_] = Sq(dd, oo).ravel()
    Gmat[:, a_] = np.concatenate([g.ravel() for g in Gp(dd, oo)])
print("max|G S^T| =", np.max(np.abs(Gmat @ Smat.T)), "  integer entries:", np.allclose(Smat, np.rint(Smat)))
print("=> d/dt[S/kappa + T00] = div(-2G + P) exactly at O(sqrt kappa); d/dt[-2G_j + P_j] = -G[T]_j + G[T]_j = 0;")
print("   lapse/shift terms drop by G S^T = 0; {G, V_N}=0 by the note's R2 G^T = 0 (stencil identity, not re-run here).")
