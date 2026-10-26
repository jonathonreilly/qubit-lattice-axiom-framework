"""Supplied H1/H2 intertwiners: positive two-magnon sector witnesses only.

Exact sector-level statements checked here (torus L=4, N=64 sites; and exact Z^3 Bloch tables):
  1. H_2 = im(S^+|H_1) (+) (ker S^- cap H_2); dims N and N(N-1)/2 - N.
  2. If the H1/H2 lowering/raising intertwiners hold and U1 = e^{i phi} on H_1, then U|H_2 = e^{i phi} on im S^+ and is an
     ARBITRARY unitary on ker S^- cap H_2 (it only has to preserve it).  So the S^- constraint by
     itself only forbids motion of MONOMIAL (permutation-type) maps (C4f remark): S^-|x,y> = |x>+|y>
     determines {x,y}.
  3. Witness that the S^- constraint does NOT forbid sector-level pair motion:
     (a) psi = 6-cycle alternating sum of near pairs with pairwise +-distinct edge vectors:
         S^- psi = 0, translates orthonormal; W_g = sum_x |psi_{x+v}><psi_x| + (1 - proj) is a TI
         sector unitary, = 1 on im S^+ and on far pairs, intertwines S^-; psi glides at speed 1.
     (b) H = sum_{R in O} sum_x |pi_R psi_x><pi_R psi_x| (O-invariant, TI, range in ker S^-);
         W_O = exp(i theta H) is O-covariant (pi_R), TI, intertwines S^-, and has a DISPERSIVE
         pair band (Bloch eigenvalues of H(K) on exact Z^3 hopping table).
These are restricted-sector objects, NOT full SU(2) operators or QCAs.
No physical motion or extension to a full local automorphism is constructed.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = ["docs/TWO_MAGNON_SECTOR_CYCLE_AND_BLOCH_WITNESS_NOTE_2026-10-23.md", "scripts/su2_equivariant_one_qubit_qca_translation_rigidity_2026_10_21_helpers.py"]
AUDIT_TIMEOUT_SECONDS = 120

import itertools
import sys
import numpy as np
import scipy.linalg as sla

from su2_equivariant_one_qubit_qca_translation_rigidity_2026_10_21_helpers import Counter




def O_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if round(np.linalg.det(M)) == 1:
                mats.append(M)
    return mats


CYCLE = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1), (1, -1, 0)]


def psi_dict(cycle, shift=(0, 0, 0), R=None):
    """psi as dict frozenset{u,v} -> amplitude (Z^3, exact)."""
    pts = [np.array(p) for p in cycle]
    if R is not None:
        pts = [R @ p for p in pts]
    pts = [tuple(int(a) for a in (p + np.array(shift))) for p in pts]
    d = {}
    m = len(pts)
    for i in range(m):
        e = frozenset([pts[i], pts[(i + 1) % m]])
        d[e] = d.get(e, 0) + (-1) ** i / np.sqrt(m)
    return d


def main(logname=None):
    fh = open(logname, "x") if logname is not None else None
    C = Counter(fh)
    C.log("C9/02 two-magnon sector analysis (sector level only; not a QCA)")
    O = O_group()
    C.check(len(O) == 24, "O has 24 elements")

    # ---------------- exact Z^3 properties of psi
    m = len(CYCLE)
    edges = [tuple(int(a) for a in np.subtract(CYCLE[(i + 1) % m], CYCLE[i])) for i in range(m)]
    pm = set()
    distinct = True
    for e in edges:
        if e in pm or tuple(-np.array(e)) in pm:
            distinct = False
        pm.add(e)
    C.check(distinct and len(set(CYCLE)) == m and all(max(abs(a) for a in e) == 1 for e in edges),
            f"6-cycle: distinct vertices, edge vectors pairwise +-distinct, |rho|_inf = 1: {edges}")
    p0 = psi_dict(CYCLE)
    # S^- psi = 0 on Z^3
    sm = {}
    for e, a in p0.items():
        for x in e:
            sm[x] = sm.get(x, 0) + a
    C.check(max(abs(v) for v in sm.values()) < 1e-14, "S^- psi = 0 on Z^3 (zero row sums)")
    # orthonormal translates on Z^3 (only |t|_inf <= 2 can overlap)
    worst = 0.0
    for t in itertools.product(range(-2, 3), repeat=3):
        pt = psi_dict(CYCLE, t)
        ov = sum(a * pt.get(e, 0) for e, a in p0.items())
        target = 1.0 if t == (0, 0, 0) else 0.0
        worst = max(worst, abs(ov - target))
    C.check(worst < 1e-14, f"translates of psi orthonormal on Z^3 (max deviation {worst:.1e})")

    # ---------------- torus L = 4
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    sidx = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    pidx = {p: k for k, p in enumerate(pairs)}
    D2 = len(pairs)

    def wrap(p):
        return tuple(int(a) % L for a in p)

    def pair_key(u, v):
        i, j = sidx[wrap(u)], sidx[wrap(v)]
        return pidx[(min(i, j), max(i, j))]

    Sm = np.zeros((N, D2))
    for k, (i, j) in enumerate(pairs):
        Sm[i, k] += 1
        Sm[j, k] += 1
    rank = np.linalg.matrix_rank(Sm)
    C.check(rank == N, f"S^-: H_2 -> H_1 surjective on L=4 torus (rank {rank} = N = {N}); "
                       f"dim ker S^- cap H_2 = {D2 - rank} = N(N-1)/2 - N = {N*(N-1)//2 - N}")
    # monomial argument: S^-|p> distinct for distinct pairs (determines the pair)
    cols = {tuple(np.nonzero(Sm[:, k])[0]) for k in range(D2)}
    C.check(len(cols) == D2, "S^-|x,y> = |x>+|y> determines {x,y} (monomial pair maps fixing singles are static)")

    def psi_vec(shift, R=None):
        v = np.zeros(D2)
        for e, a in psi_dict(CYCLE, shift, R).items():
            u, w = tuple(e)
            v[pair_key(u, w)] += a
        return v

    Psi = np.array([psi_vec(s) for s in sites]).T  # D2 x N
    C.check(np.abs(Psi.T @ Psi - np.eye(N)).max() < 1e-13 and np.abs(Sm @ Psi).max() < 1e-13,
            "torus: psi_x orthonormal and in ker S^-")
    vshift = np.array([0, 0, 1])
    Psi_v = np.array([psi_vec(tuple(np.add(s, vshift))) for s in sites]).T
    Wg = Psi_v @ Psi.T + (np.eye(D2) - Psi @ Psi.T)
    C.check(np.abs(Wg.T @ Wg - np.eye(D2)).max() < 1e-12, "W_g unitary (orthogonal) on H_2")
    C.check(np.abs(Sm @ Wg - Sm).max() < 1e-12, "S^- W_g = S^- (intertwines S^- with U|H_1 = 1)")
    imSp = Sm.T  # columns = S^+|x>
    C.check(np.abs(Wg @ imSp - imSp).max() < 1e-12, "W_g = 1 on im S^+ (so W_g S^+ = S^+ U|H_1)")
    # far pairs fixed
    far_ok = True
    for k, (i, j) in enumerate(pairs):
        d = np.subtract(sites[i], sites[j]) % L
        d = np.minimum(d, L - d)
        if d.max() >= 2:
            col = Wg[:, k]
            if abs(col[k] - 1) > 1e-12 or np.abs(col).sum() - 1 > 1e-12:
                far_ok = False
    C.check(far_ok, "W_g fixes every pair with torus separation |rho|_inf >= 2")
    # glide: W_g^t psi_0 = psi_{t v}
    st = Psi[:, 0].copy()
    glide_ok = True
    for t in range(1, 5):
        st = Wg @ st
        target = psi_vec(tuple(t * vshift))
        glide_ok &= np.abs(st - target).max() < 1e-12
    C.check(glide_ok, "W_g^t psi_0 = psi_{t e3} for t=1..4 (sector-level speed-1 pair glider)")
    # translation invariance of W_g
    def trans_perm(t):
        P = np.zeros((D2, D2))
        for k, (i, j) in enumerate(pairs):
            P[pair_key(np.add(sites[i], t), np.add(sites[j], t)), k] = 1
        return P
    Tx = trans_perm((1, 0, 0))
    Ty = trans_perm((0, 1, 0))
    Tz = trans_perm((0, 0, 1))
    C.check(max(np.abs(T @ Wg - Wg @ T).max() for T in (Tx, Ty, Tz)) < 1e-12, "W_g translation invariant")

    # ---------------- O-covariant dispersive sector unitary
    Hm = np.zeros((D2, D2))
    for R in O:
        PR = np.array([psi_vec(s, R) for s in sites]).T
        Hm += PR @ PR.T
    C.check(np.abs(Sm @ Hm).max() < 1e-12 and np.abs(Hm - Hm.T).max() < 1e-12,
            "H_O symmetric, range in ker S^-")
    def rot_perm(R):
        P = np.zeros((D2, D2))
        for k, (i, j) in enumerate(pairs):
            P[pair_key(R @ np.array(sites[i]), R @ np.array(sites[j])), k] = 1
        return P
    covO = max(np.abs(rot_perm(R) @ Hm - Hm @ rot_perm(R)).max() for R in O)
    covT = max(np.abs(T @ Hm - Hm @ T).max() for T in (Tx, Ty, Tz))
    C.check(covO < 1e-12 and covT < 1e-12, f"H_O commutes with all 24 pi_R and translations (err {max(covO, covT):.1e})")
    theta = 0.3
    WO = sla.expm(1j * theta * Hm)
    C.check(np.abs(WO.conj().T @ WO - np.eye(D2)).max() < 1e-10 and np.abs(Sm @ WO - Sm).max() < 1e-10,
            "W_O = exp(i 0.3 H_O) unitary and S^- W_O = S^-")

    # exact Z^3 Bloch table for H_O on near pairs (no aliasing)
    half = []
    for r in itertools.product(range(-1, 2), repeat=3):
        if r != (0, 0, 0) and tuple(-np.array(r)) not in half:
            half.append(r)
    C.check(len(half) == 13, "13 near-pair relative-position representatives")
    # states: psi^R_x for R in O, x in Z^3 ; pair basis |{b, b+rho}>, rho in half
    def canon(e):
        u, w = sorted(tuple(e))
        r = tuple(np.subtract(w, u))
        if r in half:
            return u, r
        return w, tuple(-np.array(r))
    psiR = [psi_dict(CYCLE, (0, 0, 0), R) for R in O]
    # H(K)_{r', r} = sum_t e^{iK.t} <{t, t+r'}|H|{0, r}> ; H = sum_{R,x} |psi^R_x><psi^R_x|
    hop = {}
    for pr in psiR:
        items = [(canon(e), a) for e, a in pr.items()]
        for (b1, r1), a1 in items:
            for (b2, r2), a2 in items:
                # translate by -b2 so ket base is 0: <{b1-b2+..}| ... |{0, r2}>
                t = tuple(np.subtract(b1, b2))
                key = (t, r1, r2)
                hop[key] = hop.get(key, 0) + a1 * a2  # summing over x absorbed by translation
    ridx = {r: i for i, r in enumerate(half)}
    def HK(K):
        M = np.zeros((13, 13), dtype=complex)
        for (t, r1, r2), a in hop.items():
            M[ridx[r1], ridx[r2]] += a * np.exp(1j * np.dot(K, t))
        return M
    # consistency with torus: eigenvalues of H(K) on the 4^3 K-grid = spectrum of Hm on near pairs
    ev_bloch = []
    for k in itertools.product(range(L), repeat=3):
        K = 2 * np.pi * np.array(k) / L
        ev_bloch.extend(np.linalg.eigvalsh(HK(K)))
    near_idx = [k for k, (i, j) in enumerate(pairs)
                if np.minimum(np.subtract(sites[i], sites[j]) % L, L - np.subtract(sites[i], sites[j]) % L).max() <= 1]
    ev_torus = np.linalg.eigvalsh(Hm[np.ix_(near_idx, near_idx)])
    C.check(len(ev_torus) == len(ev_bloch) and np.abs(np.sort(ev_bloch) - np.sort(ev_torus)).max() < 1e-9,
            f"Z^3 Bloch table reproduces torus spectrum on near pairs ({len(ev_torus)} eigenvalues)")
    # dispersion along K = (k,0,0) and a random direction
    ks = np.linspace(0, np.pi, 41)
    bands = np.array([np.linalg.eigvalsh(HK(np.array([k, 0, 0]))) for k in ks])
    widths = bands.max(axis=0) - bands.min(axis=0)
    C.log("H_O band edges along (k,0,0): min " + " ".join(f"{x:.3f}" for x in bands.min(axis=0)))
    C.log("H_O band edges along (k,0,0): max " + " ".join(f"{x:.3f}" for x in bands.max(axis=0)))
    # group velocity (finite difference, theta * dlambda/dK) on a random grid
    rng = np.random.default_rng(7)
    vmax = 0.0
    for _ in range(200):
        K = rng.uniform(-np.pi, np.pi, 3)
        h = 1e-5
        e0 = np.linalg.eigvalsh(HK(K))
        for d in range(3):
            dK = np.zeros(3)
            dK[d] = h
            e1 = np.linalg.eigvalsh(HK(K + dK))
            vmax = max(vmax, theta * np.abs((e1 - e0) / h).max())
    C.check(widths.max() > 0.1, f"H_O has a dispersive near-pair band (max width along (k,0,0) = {widths.max():.3f})")
    C.log(f"W_O = exp(i 0.3 H_O): largest sampled absolute eigenphase-derivative component = {vmax:.3f} sites/tick (sector level)")

    C.total()
    if fh is not None:
        fh.close()
    return 1 if C.f else 0


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", help="Optional new log file; refuses an existing path")
    args = parser.parse_args()
    raise SystemExit(main(args.log))
