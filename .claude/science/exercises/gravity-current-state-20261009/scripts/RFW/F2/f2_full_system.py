"""F2 (lane RFW), part 2: the FULL finite-momentum O(kappa^2) Noether system in the
translation-Killing sector, with explicit range-r unknowns for the field-dependent generator
A_c (dh = kappa A_c h, includes D lambda(c,h)) and the matter-dependent graviton shift
X_c (dh = kappa^2 X_c(phi,phi), includes D lambda(c,phi phi)); no jet reduction used.
B (dphi = kappa^2 B(h,phi)) drops exactly on the complex shell E(k1)=E(k2)=0 (it multiplies E).
Seagull drops exactly for constant xi (delta0 h = 0).

Equation, coefficient of h(q) phi(k1) phi(k2), q = -k1-k2, k1,k2 independent on shell:
  i (f_c(k1)+f_c(k2)) WT(k1,k2) + A_c(q)^T WT(k1,k2) + K(q)^T X_c(k1,k2) = 0      (10 comps)
Lattice ansatz (range r, l1-ball offsets o in base-point labels):
  A_c(q)[b,a] = sum_o alpha[b,a,o] z_q^o ;  X_c[b](k1,k2) = sum_{o1<=o2} chi[b,o1,o2](z1^o1 z2^o2 + z1^o2 z2^o1)
Continuum control: A_c(q) = alpha0 + alpha_mu q_mu ; X_c = chi0 + chi_mu (k1+k2)_mu  (polynomial).
"""
import numpy as np, time
from f2_common import *

rng = np.random.default_rng(77)
c_dir = 0


def offsets(r):
    o = [np.array(x) - r for x in np.ndindex(*(2 * r + 1,) * D) if np.sum(np.abs(np.array(x) - r)) <= r]
    return np.array(o)


def shell_near(k1, m2, lattice, s):
    """k2 on the shell with k2 = -k1 - q, |q| ~ s (small momentum transfer)."""
    tgt = -k1
    k2 = tgt.copy()
    k2[:3] = tgt[:3] + s * (rng.normal(size=3) + 0.3j * rng.normal(size=3))
    if lattice:
        c3 = 1 + 0.5 * (np.sum(2 - 2 * np.cos(k2[:3])) + m2)
        cand = [np.arccos(c3 + 0j), -np.arccos(c3 + 0j)]
        cand = [c + 2 * np.pi * n for c in cand for n in (-1, 0, 1)]
    else:
        r = np.sqrt(-(np.sum(k2[:3] ** 2) + m2) + 0j); cand = [r, -r]
    k2[3] = min(cand, key=lambda c: abs(c - tgt[3]))
    return k2


def build_lattice(m2, rA, rX, nsamp, useX=True, small=None):
    oA, oX = offsets(rA), offsets(rX)
    pairs = [(i, j) for i in range(len(oX)) for j in range(i, len(oX))]
    nA = NC * NC * len(oA)
    nX = NC * len(pairs) if useX else 0
    G = np.zeros((NC * nsamp, nA + nX), dtype=complex)
    b = np.zeros(NC * nsamp, dtype=complex)
    for s in range(nsamp):
        k1 = shell_point(rng, m2, True)
        k2 = shell_point(rng, m2, True) if small is None else shell_near(k1, m2, True, small)
        q = -(k1 + k2)
        WT = W * T_lat_cross(k1, k2, m2)
        sc = 1 / np.linalg.norm(WT)
        zq = np.exp(1j * oA @ q)                       # z_q^o for each offset
        KT = K_symbol(q, True).T
        if useX:
            e1, e2 = np.exp(1j * oX @ k1), np.exp(1j * oX @ k2)
            pb = np.array([e1[i] * e2[j] + e1[j] * e2[i] for (i, j) in pairs])
        for a in range(NC):
            row = s * NC + a
            # A part: sum_b alpha[b,a,o] z^o WT_b  ; index (b,a,o) -> (b*NC + a)*len(oA) + o
            for bb in range(NC):
                st = (bb * NC + a) * len(oA)
                G[row, st:st + len(oA)] = WT[bb] * zq * sc
            if useX:
                for bb in range(NC):
                    st = nA + bb * len(pairs)
                    G[row, st:st + len(pairs)] = KT[a, bb] * pb * sc
            b[row] = -1j * (np.sin(k1[c_dir]) + np.sin(k2[c_dir])) * WT[a] * sc
    return G, b


def build_continuum(m2, nsamp, useX=True, small=None):
    nA = NC * NC * 5
    nX = NC * 5 if useX else 0
    G = np.zeros((NC * nsamp, nA + nX), dtype=complex)
    b = np.zeros(NC * nsamp, dtype=complex)
    for s in range(nsamp):
        k1 = shell_point(rng, m2, False)
        k2 = shell_point(rng, m2, False) if small is None else shell_near(k1, m2, False, small)
        q = -(k1 + k2)
        WT = W * T_con_cross(k1, k2, m2)
        sc = 1 / np.linalg.norm(WT)
        basisA = np.concatenate([[1.0], q])
        basisX = np.concatenate([[1.0], k1 + k2])
        KT = K_symbol(q, False).T
        for a in range(NC):
            row = s * NC + a
            for bb in range(NC):
                st = (bb * NC + a) * 5
                G[row, st:st + 5] = WT[bb] * basisA * sc
            if useX:
                for bb in range(NC):
                    st = nA + bb * 5
                    G[row, st:st + 5] = KT[a, bb] * basisX * sc
            b[row] = -1j * (k1[c_dir] + k2[c_dir]) * WT[a] * sc
    return G, b


def report(name, G, b):
    t0 = time.time()
    u, _, rank, sv = np.linalg.lstsq(G, b, rcond=None)
    rel = np.linalg.norm(G @ u - b) / np.linalg.norm(b)
    print(f"{name:58s} unknowns={G.shape[1]:5d} rows={G.shape[0]:5d} rank={rank:5d} "
          f"rel.residual={rel:.3e}  ({time.time()-t0:.1f}s)", flush=True)
    return rel


if __name__ == "__main__":
    print("== F2 full finite-q system, translation-Killing sector, k1,k2 independent on the complex shell ==")
    for m2 in (0.25, 1.0):
        report(f"continuum control m2={m2} (A deg<=1, X deg<=1)", *build_continuum(m2, 300))
        report(f"continuum control m2={m2} (A deg<=1, X = 0)", *build_continuum(m2, 300, useX=False))
    for m2 in (0.25, 1.0):
        report(f"K2 lattice m2={m2}: rA=1, X = 0", *build_lattice(m2, 1, 1, 300, useX=False))
        report(f"K2 lattice m2={m2}: rA=1, rX=1", *build_lattice(m2, 1, 1, 400))
    m2 = 1.0
    report(f"K2 lattice m2={m2}: rA=2, X = 0", *build_lattice(m2, 2, 1, 700, useX=False))
    report(f"K2 lattice m2={m2}: rA=2, rX=1", *build_lattice(m2, 2, 1, 800))

    print("\n== small momentum transfer |q| ~ s (both legs on shell): residual floor vs range r ==")
    print("   (b = O(s); K X = O(s^2); the floor as s -> 0 is the r-independent 1-jet obstruction)")
    for s_ in (0.3, 0.1, 0.03):
        report(f"continuum control m2=1 s={s_}", *build_continuum(1.0, 300, small=s_))
        report(f"K2 lattice m2=1 s={s_}: rA=1, rX=1", *build_lattice(1.0, 1, 1, 400, small=s_))
        report(f"K2 lattice m2=1 s={s_}: rA=2, rX=1", *build_lattice(1.0, 2, 1, 600, small=s_))
