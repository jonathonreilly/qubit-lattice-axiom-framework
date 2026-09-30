"""T24 test A: are the 8 corner crossings pinned for ANY range under covariance with a spinor coin?

Symbol H(k) = d0(k) + d(k).sigma with real trigonometric polynomials (Hermitian, translation-invariant).
Covariance under a rotation subgroup G with spinor lifts:  d(Rk) = R d(k),  d0(Rk) = d0(k).
Group averaging of random trigonometric coefficients gives the general covariant symbol of range r.
"""
import itertools
import sys
import numpy as np
from common import O, su2_of_rotation, SIG, I2

rng = np.random.default_rng(24)
CORNERS = [np.array(n) * np.pi for n in itertools.product([0, 1], repeat=3)]
HW = {tuple(n): sum(n) for n in itertools.product([0, 1], repeat=3)}


def rot(name):
    """named subgroups of the proper cubic group as lists of integer matrices"""
    def R(axis, quarter):
        th = quarter * np.pi / 2
        c, s = int(round(np.cos(th))), int(round(np.sin(th)))
        M = np.eye(3, dtype=int)
        i, j = [(1, 2), (2, 0), (0, 1)][axis]
        M[i, i] = c; M[i, j] = -s; M[j, i] = s; M[j, j] = c
        return M
    def close(gens):
        S = {tuple(np.eye(3, dtype=int).flatten())}
        frontier = [np.eye(3, dtype=int)]
        while frontier:
            new = []
            for g in frontier:
                for h in gens:
                    p = h @ g
                    t = tuple(p.flatten())
                    if t not in S:
                        S.add(t); new.append(p)
            frontier = new
        return [np.array(t).reshape(3, 3) for t in S]
    if name == "O":
        return list(O)
    if name == "D4":      # C4z + C2x
        return close([R(2, 1), R(0, 2)])
    if name == "D2":      # three perpendicular 2-fold axes (Klein four)
        return close([R(2, 2), R(0, 2)])
    if name == "C4z":
        return close([R(2, 1)])
    if name == "C2z":
        return close([R(2, 2)])
    if name == "trivial_group":
        return [np.eye(3, dtype=int)]
    raise ValueError(name)


def random_coeffs(r):
    """real coefficient dicts: for each displacement w in [-r,r]^3 minus origin (half set) and each of 4 components
    (d0, dx, dy, dz): cos and sin coefficient."""
    ws = [w for w in itertools.product(range(-r, r + 1), repeat=3) if w != (0, 0, 0)]
    half = []
    seen = set()
    for w in ws:
        if tuple(-np.array(w)) in seen:
            continue
        seen.add(w)
        half.append(w)
    C = {}
    for w in half:
        C[w] = (rng.normal(size=4), rng.normal(size=4))  # cos coeffs, sin coeffs
    const = rng.normal(size=4)
    return const, C


def average(const, C, group, kind="full"):
    """Return covariant coefficient table: dict w -> (cosC[4], sinC[4]), constant[4].
    kind full: d transforms as vector under G. kind trivial: coin does not rotate."""
    table = {}
    n = len(group)
    const_av = const.copy()
    if kind == "full":
        # average const vector part: (1/n) sum R^T c  ; scalar part unchanged
        v = np.zeros(3)
        for R in group:
            v += R.T @ const[1:]
        const_av[1:] = v / n
    for w, (cc, ss) in C.items():
        for R in group:
            wp = tuple(R.T @ np.array(w))    # d(Rk)=sum c cos(Rk.w)=sum c cos(k.R^T w)
            ccn = cc.copy(); ssn = ss.copy()
            if kind == "full":
                ccn[1:] = R.T @ cc[1:]
                ssn[1:] = R.T @ ss[1:]
            a = table.setdefault(wp, [np.zeros(4), np.zeros(4)])
            a[0] += ccn / n
            a[1] += ssn / n
    return const_av, table


def evaluate(const, table, K):
    """K: (N,3) momenta -> (N,4) values [d0,dx,dy,dz], and Jacobian (N,3,3) of d wrt k (vectorised)."""
    K = np.atleast_2d(K)
    if not hasattr(table, "_arr"):
        pass
    key = id(table)
    arr = _CACHE.get(key)
    if arr is None or arr[0] is not table:
        ws = list(table.keys())
        Wm = np.array(ws, float)
        CC = np.array([table[w][0] for w in ws])
        SS = np.array([table[w][1] for w in ws])
        arr = (table, Wm, CC, SS)
        _CACHE.clear()
        _CACHE[key] = arr
    _, Wm, CC, SS = arr
    ph = K @ Wm.T
    cph, sph = np.cos(ph), np.sin(ph)
    val = const[None, :] + cph @ CC + sph @ SS
    dcomp = -sph[:, :, None] * CC[None, :, 1:] + cph[:, :, None] * SS[None, :, 1:]
    J = np.einsum('nwi,wj->nij', dcomp, Wm)
    return val, J


_CACHE = {}


def corner_d(const, table):
    K = np.array(CORNERS)
    val, J = evaluate(const, table, K)
    return val[:, 1:], J


def find_nodes(const, table, nseed=14):
    """multi-start Newton for d(k)=0; returns list of (k, chirality)."""
    g = (np.arange(nseed) + rng.uniform(0.2, 0.8)) * 2 * np.pi / nseed
    K = np.array(list(itertools.product(g, g, g)))
    K = np.vstack([K, np.array(CORNERS)])
    for _ in range(60):
        val, J = evaluate(const, table, K)
        d = val[:, 1:]
        det = np.linalg.det(J)
        ok = np.abs(det) > 1e-10
        step = np.zeros_like(K)
        if ok.any():
            step[ok] = np.linalg.solve(J[ok], d[ok][..., None])[..., 0]
        nrm = np.linalg.norm(step, axis=1)
        scale = np.minimum(1.0, 0.5 / np.maximum(nrm, 1e-12))
        K = K - step * scale[:, None]
    val, J = evaluate(const, table, K)
    d = val[:, 1:]
    good = np.linalg.norm(d, axis=1) < 1e-9
    nodes = []
    for k, Jk in zip(K[good], J[good]):
        kk = (k + np.pi) % (2 * np.pi) - np.pi
        dup = False
        for k2, _c in nodes:
            dd = (kk - k2 + np.pi) % (2 * np.pi) - np.pi
            if np.linalg.norm(dd) < 1e-5:
                dup = True
                break
        if not dup:
            dt = np.linalg.det(Jk)
            chi = 0 if abs(dt) < 1e-7 else int(np.sign(dt))
            nodes.append((kk, chi))
    return nodes


def corner_pattern(nodes):
    """chirality by Hamming-weight class of the corner nodes (None if degenerate/missing)"""
    pat = {}
    for k, chi in nodes:
        for n in itertools.product([0, 1], repeat=3):
            c = np.array(n) * np.pi
            dd = (k - c + np.pi) % (2 * np.pi) - np.pi
            if np.linalg.norm(dd) < 1e-5:
                pat.setdefault(sum(n), set()).add(chi)
    return pat


def run():
    out = {}
    lines = []

    def log(s):
        print(s); lines.append(s)

    # ---- A1 pinning
    log("A1: max |d(pi n)| over corners and samples (spinor coin), per range and covariance group")
    for gname in ["O", "D4", "D2", "C4z", "C2z", "trivial_group"]:
        grp = rot(gname)
        for r in [1, 2, 3]:
            mx_all = []
            frac_unpinned = 0
            for s in range(200):
                const, C = random_coeffs(r)
                cav, tab = average(const, C, grp, "full")
                d, _ = corner_d(cav, tab)
                mx_all.append(np.abs(d).max())
                if np.abs(d).max() > 1e-6:
                    frac_unpinned += 1
            log(f"  G={gname:13s} |G|={len(grp):2d} range {r}: max|d(corner)| over 200 samples = {max(mx_all):.2e}; "
                f"median = {np.median(mx_all):.2e}; fraction with some corner unpinned = {frac_unpinned/200:.2f}")
            out[f"A1_{gname}_r{r}"] = dict(max=float(max(mx_all)), median=float(np.median(mx_all)), unpinned=frac_unpinned / 200)
    # which corners are unpinned under C4z, C2z
    for gname in ["C4z", "C2z"]:
        grp = rot(gname)
        cnt = np.zeros(8)
        for s in range(200):
            const, C = random_coeffs(2)
            cav, tab = average(const, C, grp, "full")
            d, _ = corner_d(cav, tab)
            cnt += (np.abs(d).max(axis=1) > 1e-6)
        log(f"  G={gname}: fraction unpinned at corners {list(itertools.product([0,1],repeat=3))} = {np.round(cnt/200,2).tolist()}")
    # trivial coin under O (not soldered): d invariant scalar-like
    mx = []
    for s in range(200):
        const, C = random_coeffs(2)
        cav, tab = average(const, C, rot("O"), "trivial")
        d, _ = corner_d(cav, tab)
        mx.append(np.abs(d).max())
    log(f"  O with trivial coin (no soldering), range 2: median max|d(corner)| = {np.median(mx):.2e}  (must be > 0.1 for a non-vacuous test)")
    out["A1_trivial_coin_O_median"] = float(np.median(mx))

    # ---- A3 Kramers only
    mxk = []
    for s in range(200):
        const, C = random_coeffs(3)
        # Theta: d odd (sin terms only), d0 even (cos terms only)
        tab = {}
        for w, (cc, ss) in C.items():
            c2 = np.zeros(4); s2 = np.zeros(4)
            c2[0] = cc[0]
            s2[1:] = ss[1:]
            tab[w] = [c2, s2]
        c0 = np.zeros(4); c0[0] = const[0]
        d, _ = corner_d(c0, tab)
        mxk.append(np.abs(d).max())
    log(f"A3: Kramers-only (d odd), range 3: max|d(TRIM)| over 200 samples = {max(mxk):.2e}")
    out["A3_kramers_max"] = float(max(mxk))

    # ---- A2 node census
    log("A2: node census for fully covariant symbols (group O), multi-start Newton")
    for r in [1, 2, 3]:
        tot_ok = 0; nsamp = 60
        sums = []
        counts = []
        pats = {}
        for s in range(nsamp):
            const, C = random_coeffs(r)
            cav, tab = average(const, C, rot("O"), "full")
            nodes = find_nodes(cav, tab)
            chis = [c for _, c in nodes]
            sums.append(sum(chis))
            counts.append(len(nodes))
            ncorner = sum(1 for k, _ in nodes if any(np.linalg.norm((k - c + np.pi) % (2*np.pi) - np.pi) < 1e-5 for c in CORNERS))
            pat = corner_pattern(nodes)
            key = tuple(sorted(next(iter(pat[h])) if h in pat and len(pat[h]) == 1 else 9 for h in range(4)) ) if False else tuple((next(iter(pat[h])) if (h in pat and len(pat[h]) == 1) else 9) for h in range(4))
            pats[(key, ncorner)] = pats.get((key, ncorner), 0) + 1
        bad = sum(1 for x in sums if x != 0)
        log(f"  range {r}: samples {nsamp}; nodes per sample min/median/max = {min(counts)}/{int(np.median(counts))}/{max(counts)}; "
            f"samples with sum(chirality) != 0: {bad}")
        log(f"     corner chirality pattern (hw0,hw1,hw2,hw3) [9=mixed] , #corner nodes -> count: {dict(sorted(pats.items(), key=lambda kv: -kv[1]))}")
        out[f"A2_r{r}"] = dict(nsamp=nsamp, sum_nonzero=bad, count_min=min(counts), count_max=max(counts),
                                patterns={str(k): v for k, v in pats.items()})

    # ---- A4 explicit 2-node symbol
    def d2(K):
        K = np.atleast_2d(K)
        return np.stack([np.sin(K[:, 0]), np.sin(K[:, 1]), 2 - np.cos(K[:, 0]) - np.cos(K[:, 1]) - np.cos(K[:, 2])], axis=1)
    g = np.linspace(-np.pi, np.pi, 33)[:-1] + 0.01
    K = np.array(list(itertools.product(g, g, g)))
    def jac(k):
        return np.array([[np.cos(k[0]), 0, 0], [0, np.cos(k[1]), 0], [np.sin(k[0]), np.sin(k[1]), np.sin(k[2])]])
    nodes = []
    for _ in range(1):
        Kc = K.copy()
        for it in range(60):
            d = d2(Kc)
            J = np.array([jac(k) for k in Kc])
            det = np.linalg.det(J)
            ok = np.abs(det) > 1e-10
            step = np.zeros_like(Kc)
            step[ok] = np.linalg.solve(J[ok], d[ok][..., None])[..., 0]
            nrm = np.linalg.norm(step, axis=1)
            Kc = Kc - step * np.minimum(1.0, 0.5 / np.maximum(nrm, 1e-12))[:, None]
        d = d2(Kc)
        good = np.linalg.norm(d, axis=1) < 1e-9
        for k in Kc[good]:
            kk = (k + np.pi) % (2 * np.pi) - np.pi
            if not any(np.linalg.norm((kk - k2 + np.pi) % (2*np.pi) - np.pi) < 1e-5 for k2, _ in nodes):
                nodes.append((kk, int(np.sign(np.linalg.det(jac(kk))))))
    log(f"A4: explicit symbol d=(sin kx, sin ky, 2-cos kx-cos ky-cos kz): nodes found = {[(np.round(k,4).tolist(), c) for k, c in nodes]}")
    # symmetries
    Kt = rng.uniform(-np.pi, np.pi, size=(50, 3))
    theta = np.abs(d2(-Kt) + d2(Kt)).max()             # Theta requires d(-k) = -d(k)
    C2x = np.abs(d2(Kt * np.array([1, -1, -1])) - d2(Kt) * np.array([1, -1, -1])).max()
    C4z_err = 0
    for k in Kt:
        kr = np.array([-k[1], k[0], k[2]])
        dk = d2(k)[0]
        C4z_err = max(C4z_err, np.abs(d2(kr)[0] - np.array([-dk[1], dk[0], dk[2]])).max())
    log(f"   Theta (d odd) violation = {theta:.3f} (broken); C2x covariance violation = {C2x:.3f} (broken); C4z covariance violation = {C4z_err:.1e} (kept)")
    out["A4"] = dict(nodes=[(np.round(k, 4).tolist(), c) for k, c in nodes], theta_violation=float(theta), C2x_violation=float(C2x), C4z_violation=float(C4z_err))
    return out, lines


if __name__ == "__main__":
    import json
    out, lines = run()
    json.dump(out, open("A_pin_results.json", "w"), indent=1, default=str)
