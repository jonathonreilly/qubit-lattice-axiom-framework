#!/usr/bin/env python3
"""rel-phi-c: identity checks and kernel norms for the composite contour average.

Guidance only. No statement of library/rel-phi-c.md rests on a run: the proofs
there are by hand. A failed identity, or an annular norm above the hand
constant C_A(L) = 3.4 L + 1, would refute; bounded values prove nothing.

Conventions (match library/rel-phi-c.md Sections 1-3 and checks/seamqc/seamqc.py):
fine torus Z_N^4; level-k sites at fine indices multiple of L^k; block of a
level-k site = level-(k-1) sites at offsets L^(k-1) * {-m..m}^4; contours are
axial staircases in the axis order 0,1,2,3 (contour_steps, copied from
seamqc.py); a 1-form is a list of 4 arrays, theta[mu][z] on bond [z, z+e_mu].
"""
import sys, json, time, resource, itertools, math
import numpy as np

def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1e9 if sys.platform == "darwin" else r / 1e6

def guard():
    if rss_gb() > 2.0:
        print("RSS above 2 GB; stopping", flush=True)
        sys.exit(3)

# ---------------------------------------------------------------- torus tools
def contour_steps(delta):           # copied from checks/seamqc/seamqc.py
    steps = []
    pos = [0, 0, 0, 0]
    for ax in range(4):
        n = delta[ax]
        for _ in range(abs(n)):
            if n > 0:
                steps.append((tuple(pos), ax, +1)); pos[ax] += 1
            else:
                pos[ax] -= 1; steps.append((tuple(pos), ax, -1))
    return steps

def shift(arr, pos):                # shift(arr,pos)[y] = arr[y+pos]
    return np.roll(arr, shift=tuple(-p for p in pos), axis=(0, 1, 2, 3))

def offsets(L):
    m = (L - 1) // 2
    return list(itertools.product(range(-m, m + 1), repeat=4))

def contour_sums(theta, L):
    """cont[delta][y] = theta(Gamma_{y, y+delta}) on the torus of theta."""
    cont = {}
    for dlt in offsets(L):
        acc = np.zeros(theta[0].shape)
        for (pos, ax, sg) in contour_steps(dlt):
            acc += sg * shift(theta[ax], pos)
        cont[dlt] = acc
    return cont

def phi_one(theta, L):
    """One-step contour average at the coarse sites (every L-th index)."""
    cont = contour_sums(theta, L)
    acc = sum(cont.values()) / len(cont)
    return acc[::L, ::L, ::L, ::L]

def balaban_Q(theta, L):
    """One linearized step from its definition (as in seamqc.py)."""
    cont = contour_sums(theta, L)
    offs = offsets(L)
    out = []
    for mu in range(4):
        e = [0, 0, 0, 0]; e[mu] = L
        acc = np.zeros(theta[0].shape)
        for dlt in offs:
            line = np.zeros(theta[0].shape)
            for s in range(L):
                p = list(dlt); p[mu] += s
                line += shift(theta[mu], p)
            acc += cont[dlt] + line - shift(cont[dlt], e)
        acc /= len(offs)
        out.append(acc[::L, ::L, ::L, ::L])
    return out

def path_avg(theta, s):
    """Q_path^(s) theta on the level with spacing s (s odd)."""
    h = (s - 1) // 2
    offs = list(itertools.product(range(-h, h + 1), repeat=4))
    out = []
    for mu in range(4):
        line = np.zeros(theta[0].shape)
        for t in range(s):
            p = [0, 0, 0, 0]; p[mu] = t
            line += shift(theta[mu], p)
        acc = np.zeros(theta[0].shape)
        for o in offs:
            acc += shift(line, o)
        out.append((acc / len(offs))[::s, ::s, ::s, ::s])
    return out

def block_avg(f, s):
    h = (s - 1) // 2
    offs = list(itertools.product(range(-h, h + 1), repeat=4))
    acc = np.zeros(f.shape)
    for o in offs:
        acc += shift(f, o)
    return (acc / len(offs))[::s, ::s, ::s, ::s]

def grad0(f):
    return [np.roll(f, -1, axis=mu) - f for mu in range(4)]

def rel(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    return float(np.abs(a - b).max() / max(1e-300, np.abs(b).max(), np.abs(a).max()))

# ---------------------------------------------------------------- N1 identities
def identities(rng, L=3, M=2):
    B = L * L
    N = B * M
    theta = [rng.standard_normal((N,) * 4) for _ in range(4)]
    out = {}
    # recursion of seam-quadratic-c 2.2(d): Phi_2 = Av^(2) Phi_1 + Phi^(2) Q_1
    q1 = balaban_Q(theta, L)                      # level-1 field, torus side N/L
    phi1 = phi_one(theta, L)                      # level-1 sites
    phi2_rec = block_avg(phi1, L) + phi_one(q1, L)
    # Lemma 1: Phi_2(y) = Phi^(1) theta (y) + Phi^(2) Q_path^(L) theta (y)
    qp1 = path_avg(theta, L)
    phi2_l1 = phi1[::L, ::L, ::L, ::L] + phi_one(qp1, L)
    out["Lemma 1 vs recursion 2.2(d)"] = rel(phi2_l1, phi2_rec)
    # composite: Q_2 = Q_path^(B) - d' Phi_2 (level-2 gradient)
    q2 = balaban_Q(q1, L)
    qpB = path_avg(theta, B)
    d2 = grad0(phi2_rec)
    out["Q_2 = Q_path^(B) - d'Phi_2"] = max(rel(q2[mu], qpB[mu] - d2[mu]) for mu in range(4))
    # Lemma 2: gauge law
    lam = rng.standard_normal((N,) * 4)
    g = grad0(lam)
    pg = phi_one(g, L)[::L, ::L, ::L, ::L] + phi_one(path_avg(g, L), L)
    out["Lemma 2 gauge law"] = rel(pg, block_avg(lam, B) - lam[::B, ::B, ::B, ::B])
    # Lemma 3: constants
    a = rng.standard_normal(4)
    cst = [np.full((N,) * 4, a[mu]) for mu in range(4)]
    pc = phi_one(cst, L)[::L, ::L, ::L, ::L] + phi_one(path_avg(cst, L), L)
    out["Lemma 3 constants (abs max)"] = float(np.abs(pc).max())
    return out, theta, phi2_rec

# ---------------------------------------------------------------- N4 kernel
def kernel(L, n):
    """Fine-bond kernel W[mu] of theta -> Phi_n theta(0), on the box [-Rb, Rb]^4,
    built from Lemma 1: sum_k (Q_path^(L^(k-1)))^* (staircase weights at level k)."""
    B = L ** n
    m = (L - 1) // 2
    Rb = (B - 1) // 2 + B // L + 1
    side = 2 * Rb + 1
    W = [np.zeros((side,) * 4) for _ in range(4)]
    per_level = []
    for k in range(1, n + 1):
        s = L ** (k - 1)
        cw = [np.zeros((L,) * 4) for _ in range(4)]   # lower endpoints u in {-m..m}^4
        for dlt in offsets(L):
            for (pos, ax, sg) in contour_steps(dlt):
                idx = tuple(p + m for p in pos)
                cw[ax][idx] += sg / L ** 4
        Wk = [np.zeros((side,) * 4) for _ in range(4)]
        for mu in range(4):
            G = np.kron(cw[mu], np.ones((s,) * 4)) / s ** 4   # fine sites [-(L^k-1)/2, (L^k-1)/2]^4
            h = (L ** k - 1) // 2
            for t in range(s):
                lo = [Rb - h] * 4
                lo[mu] += t
                sl = tuple(slice(lo[i], lo[i] + G.shape[i]) for i in range(4))
                Wk[mu][sl] += G
            guard()
        per_level.append(sum(float((np.abs(Wk[mu]) ** (4 / 3)).sum()) for mu in range(4)) ** 0.75)
        for mu in range(4):
            W[mu] += Wk[mu]
        del Wk
    return W, per_level, Rb

def bond_dist(Rb, mu):
    side = 2 * Rb + 1
    c = (np.arange(side) - Rb).astype(np.int16)
    out = None
    for ax in range(4):
        v = np.abs(c)
        if ax == mu:
            v = np.maximum(v, np.abs(c + 1))
        shp = [1, 1, 1, 1]; shp[ax] = side
        v = v.reshape(shp)
        out = v if out is None else np.maximum(out, v)
    return out

def norms(L, n):
    W, per_level, Rb = kernel(L, n)
    rho = [None] + [(L ** j + 2 * L ** (j - 1)) / 2 for j in range(1, n + 1)]
    tot = sum(float((np.abs(W[mu]) ** (4 / 3)).sum()) for mu in range(4)) ** 0.75
    ann = []
    mean_zero = max(abs(float(W[mu].sum())) for mu in range(4))
    dists = [bond_dist(Rb, mu) for mu in range(4)]
    for j in range(1, n + 1):
        lo = -1 if j == 1 else rho[j - 1]
        acc = 0.0
        for mu in range(4):
            mask = (dists[mu] > lo) & (dists[mu] <= rho[j])
            acc += float((np.abs(W[mu][mask]) ** (4 / 3)).sum())
        ann.append(acc ** 0.75)
    outside = 0.0
    for mu in range(4):
        outside += float((np.abs(W[mu][dists[mu] > rho[n]]) ** (4 / 3)).sum())
    lev = per_level
    guard()
    return {"L": L, "n": n, "N_tot": tot, "N_ann": ann, "max N_ann": max(ann),
            "C_A(L)": 3.4 * L + 1, "per-level l43": lev,
            "mass outside R_n": outside, "max |sum_mu W|": mean_zero,
            "N_tot / n^(3/4)": tot / n ** 0.75}

def kernel_vs_torus(theta, phi2, L=3):
    W, _, Rb = kernel(L, 2)
    N = theta[0].shape[0]
    val = 0.0
    c = (np.arange(2 * Rb + 1) - Rb) % N
    ix = np.ix_(c, c, c, c)
    for mu in range(4):
        val += float((W[mu] * theta[mu][ix]).sum())
    return rel(val, phi2[0, 0, 0, 0])

# ---------------------------------------------------------------- N5 example E
def example_E(L, n):
    """Exact sums for lambda = a * phi(|z|_inf), phi = log(1+r)/log(1+R), R = floor((B-1)/4).
    Returns Psi/a, ||d lambda||_4/a, ||B d lambda||_(L^2(Q))/a in top units."""
    B = L ** n
    R = (B - 1) // 4
    if R < 1:
        return None
    phi = lambda r: math.log(1 + r) / math.log(1 + R) if r < R else 1.0
    def n_sph(r):
        return 1 if r == 0 else (2 * r + 1) ** 4 - (2 * r - 1) ** 4
    def n_out(r):                    # bonds from |z|=r to |z|=r+1
        if r == 0:
            return 8
        return sum(math.comb(4, k) * 2 ** k * k * (2 * r - 1) ** (4 - k) for k in range(1, 5))
    s4 = sum(n_out(r) * (phi(r + 1) - phi(r)) ** 4 for r in range(R))
    s2 = sum(n_out(r) * (phi(r + 1) - phi(r)) ** 2 for r in range(R))
    defect = sum(n_sph(r) * (1 - phi(r)) for r in range(R + 1)) / B ** 4
    psi = 1 - defect
    l4 = s4 ** 0.25
    l2 = (s2 / B ** 2) ** 0.5
    return {"n": n, "B": B, "R": R, "Psi/a": psi, "||dl||_4/a": l4,
            "Psi/||dl||_4": psi / l4, "(log B)^(3/4)": math.log(B) ** 0.75,
            "ratio/(logB)^(3/4)": psi / l4 / math.log(B) ** 0.75,
            "||Bdl||_2/||dl||_4": l2 / l4}

def main():
    t0 = time.time()
    rng = np.random.default_rng(20261102)
    res = {}
    ids, theta, phi2 = identities(rng)
    ids["kernel (Lemma 1 adjoint) vs torus Phi_2"] = kernel_vs_torus(theta, phi2)
    res["identities"] = ids
    print("identities", {k: f"{v:.2e}" for k, v in ids.items()}, round(time.time() - t0, 1), "s", flush=True)
    res["kernel norms"] = []
    for (L, n) in [(3, 1), (3, 2), (5, 1), (5, 2), (3, 3)]:
        r = norms(L, n)
        res["kernel norms"].append(r)
        print("norms", r, round(time.time() - t0, 1), "s; RSS GB", round(rss_gb(), 3), flush=True)
    res["example E"] = [example_E(3, n) for n in range(2, 13)]
    for r in res["example E"]:
        print("E", r, flush=True)
    with open(sys.argv[1] if len(sys.argv) > 1 else "relphi_results.json", "w") as fh:
        json.dump(res, fh, indent=1)
    print("done", round(time.time() - t0, 1), "s; RSS GB", round(rss_gb(), 3), flush=True)

if __name__ == "__main__":
    main()
