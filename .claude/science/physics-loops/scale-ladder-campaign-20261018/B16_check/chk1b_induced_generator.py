"""B16 check, item 1b/2/3: the relabelling generator INDUCED by a bond-supported timing.

For a bond-supported timing, {H(N),H(M)} = sum_b xi~_b X_b with xi~_(s,i) = N_{s+i} M_s - N_s M_{s+i};
define G'[xi] = sum_b xi_b X_b / (-c), so {H(N),H(M)} = G'[-c xi~] holds by construction.
Then the physics is in G': (i) gauge invariance, (ii) action of G'[uniform e0] on A (normalisation),
(iii) {G'[e0], H(1)} (uniform-shift defect).

Timings: FWD (B16's tail/c00), STAG (links at even endpoint, plaquettes at mean of odd corners).
Exact Fractions throughout.
"""
from fractions import Fraction as Fr
import random

import numpy as np

from chk_lat import Lat, em_pair_coeffs, uniform_timing
from chk1_timing import staggered

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def induced_generator(lat, u, w, c=Fr(1)):
    co = em_pair_coeffs(lat, u, w, c)
    X = {}
    for (s, t), d in co.items():
        if s == t:
            continue
        assert lat.is_bond(s, t)
        # identify bond b = (base, i) with t = base or s
        for i in range(3):
            if lat.sh(s, i) == t:  # pair (t, s) = (s+i, s): X_b = Q_{s+i,s} = co[(t,s)]
                X[(s, i)] = {k: v / (-c) for k, v in co[(t, s)].items()}
    return X  # bond -> dict (Eidx, Aidx) -> coeff of G' per unit xi_b


def gen_matrix(lat, X, xi):
    nL = len(lat.links)
    G = np.zeros((nL, nL), dtype=object)
    G[:, :] = Fr(0)
    for b, d in X.items():
        if xi.get(b, 0) == 0:
            continue
        for (k, a), v in d.items():
            G[k, a] += xi[b] * v
    return G  # G'[xi] = sum_{k,a} G[k,a] E_k A_a


def fwd_GA(lat):
    """B16's stated G_A[xi] = sum xi_(y,i) sum_{j!=i} E_(y+i,j) F_ij(y) (with F_ji = -F_ij), as bond dicts."""
    X = {}
    for y in lat.sites:
        for i in range(3):
            d = {}
            for j in range(3):
                if j == i:
                    continue
                ij = (min(i, j), max(i, j))
                sgn = 1 if i < j else -1
                p = lat.pidx[(y, ij)]
                k = lat.lidx[(lat.sh(y, i), j)]
                for a, f in lat.Fp[p].items():
                    d[(k, a)] = d.get((k, a), 0) + sgn * f
            X[(y, i)] = {kk: Fr(v) for kk, v in d.items() if v}
    return X


def div_rows(lat):
    rows = []
    for x in lat.sites:
        d = {}
        for j in range(3):
            d[lat.lidx[(x, j)]] = d.get(lat.lidx[(x, j)], 0) + 1
            km = lat.lidx[(lat.sh(x, j, -1), j)]
            d[km] = d.get(km, 0) - 1
        rows.append(d)
    return rows


def analyse(name, lat, X, c_test=Fr(3, 2)):
    nL = len(lat.links)
    xi_u = {(y, i): Fr(1) if i == 0 else Fr(0) for y in lat.sites for i in range(3)}
    G = gen_matrix(lat, X, xi_u)  # E^T G A
    Gf = G.astype(float)
    # (i) gauge invariance of G'[xi] for random xi: A -> A + grad theta leaves E^T G A unchanged, i.e. G @ grad = 0
    rng = random.Random(3)
    xi_r = {b: Fr(rng.randint(-2, 2)) for b in xi_u}
    Gr = gen_matrix(lat, X, xi_r).astype(float)
    grad = np.zeros((nL, len(lat.sites)))
    for k, (x, j) in enumerate(lat.links):
        grad[k, lat.sidx[lat.sh(x, j)]] += 1
        grad[k, lat.sidx[x]] -= 1
    gauge_inv = np.abs(Gr @ grad).max() < 1e-12
    # (ii) action on F of G'[e0]: delta A = dG/dE = G A ; delta F_p = sum sigma delta A
    Fm = np.zeros((len(lat.plaqs), nL))
    for p, d in enumerate(lat.Fp):
        for a, s in d.items():
            Fm[p, a] = s
    dF = Fm @ Gf  # rows: delta F_p as linear form in A
    # compare with backward / forward / central differences of F along e0
    def shiftF(sgn):
        S = np.zeros((len(lat.plaqs), len(lat.plaqs)))
        for p, (y, ij) in enumerate(lat.plaqs):
            S[p, lat.pidx[(lat.sh(y, 0, sgn), ij)]] = 1
        return S
    I = np.eye(len(lat.plaqs))
    cands = {"backward F_p - F_(p-e0)": (I - shiftF(-1)) @ Fm, "forward F_(p+e0) - F_p": (shiftF(1) - I) @ Fm,
             "central (F_(p+e0) - F_(p-e0))/2": 0.5 * (shiftF(1) - shiftF(-1)) @ Fm}
    match = [k for k, v in cands.items() if np.abs(v - dF).max() < 1e-12]
    # least squares: dF = alpha * central + rest
    cen = cands["central (F_(p+e0) - F_(p-e0))/2"]
    alpha = float(np.sum(dF * cen) / np.sum(cen * cen))
    # (iii) uniform-shift defect {G'[e0], H(1)} = sum_k [dG/dA_k dH/dE_k - dG/dE_k dH/dA_k]
    # G = E^T G A: dG/dA = G^T E, dG/dE = G A ; H(1) = g2/2 E.E + c/(2g2) A^T Fm^T Fm A
    g2 = 0.8
    c = float(c_test)
    # bracket quadratic forms: EE part: (G^T E).(g2 E) -> g2 E^T G^T E ; AA part: -(G A).(c/g2 Fm^T Fm A)
    EE = g2 * Gf.T
    AA = -(c / g2) * (Fm.T @ Fm) @ Gf
    EEs = 0.5 * (EE + EE.T)
    AAs = 0.5 * (AA + AA.T)
    # mod Gauss for EE part: restrict to transverse E
    D = np.zeros((len(lat.sites), nL))
    for x_i, d in enumerate(div_rows(lat)):
        for k, v in d.items():
            D[x_i, k] = v
    Pt = np.eye(nL) - D.T @ np.linalg.pinv(D @ D.T) @ D
    EEt = Pt @ EEs @ Pt
    print(f"  [{name}] G' gauge invariant: {gauge_inv}; delta F under G'[e0] matches: {match or 'none'}; "
          f"projection on central difference alpha={alpha:.6f}; |defect EE| (transverse) = {np.abs(EEt).max():.3e}, |defect AA| = {np.abs(AAs).max():.3e}")
    return dict(gauge_inv=gauge_inv, match=match, alpha=alpha, EEt=np.abs(EEt).max(), AA=np.abs(AAs).max(), G=Gf, Fm=Fm, dF=dF)


if __name__ == "__main__":
    lat = Lat(4)
    # forward timing
    u, w = uniform_timing(lat, {j: (Fr(1), Fr(0)) for j in range(3)}, {ij: {"00": Fr(1)} for ij in lat.pairs})
    Xf = induced_generator(lat, u, w, Fr(3, 2))
    Xb = fwd_GA(lat)
    same = all(Xf.get(b, {}) == Xb.get(b, {}) for b in set(Xf) | set(Xb))
    check("C2a", same, "forward timing: induced generator G' (bracket / (-c)) equals B16's stated G_A[xi] = sum xi E_(y+i,j) F_ij(y) bond by bond, exactly (L=4)")
    rf = analyse("FWD", lat, Xf)
    check("C2b", rf["gauge_inv"] and rf["match"] == ["backward F_p - F_(p-e0)"] and rf["EEt"] > 1e-6 and rf["AA"] > 1e-6,
          "forward G_A: gauge invariant; G_A[e0] acts on F as the unit BACKWARD difference (non-antisymmetric operator); hence {G_A[e0],H(1)} != 0 even on transverse E and in the pure-A sector")
    # staggered
    u, w = staggered(lat, 0)
    Xs = induced_generator(lat, u, w, Fr(3, 2))
    rs = analyse("STAG", lat, Xs)
    check("C2c", rs["gauge_inv"],
          f"staggered timing: induced G' is gauge invariant; delta F under G'[e0] matches {rs['match'] or 'no single difference'}, central-difference projection {rs['alpha']:.4f}")
    check("C2d", rs["EEt"] < 1e-10 and rs["AA"] < 1e-10,
          f"staggered timing: uniform-shift defect {{G'[e0], H(1)}} vanishes on transverse E and in the A-sector (|EE|={rs['EEt']:.1e}, |AA|={rs['AA']:.1e}) -- the B16 T6 O(a) defect is an artefact of the one-sided timing, not of Maxwell")
    # report full defect for staggered including Gauss part
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
