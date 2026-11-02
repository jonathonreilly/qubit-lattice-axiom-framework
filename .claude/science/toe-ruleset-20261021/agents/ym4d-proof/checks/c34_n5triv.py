"""c34: elementary constants and Lemma CT behind Theorem N5-triv (PROOF.md [S18]). Criteria: checks/c34_criteria.md."""
import sys, itertools
import numpy as np

L, d = 3, 4
c = (1, 1, 1, 1)


def axial_path(c, y, order):
    """links (x, mu, sign) of the complete-axial path from c to y moving in coordinates `order`."""
    x = list(c); out = []
    for mu in order:
        while x[mu] != y[mu]:
            s = 1 if y[mu] > x[mu] else -1
            if s == 1:
                out.append((tuple(x), mu, +1))
            else:
                xb = list(x); xb[mu] -= 1
                out.append((tuple(xb), mu, -1))
            x[mu] += s
    return out


def weight_vector(offset=(0, 0, 0, 0)):
    w = {}
    cc = tuple(ci + oi for ci, oi in zip(c, offset))
    block = [tuple(oi + t for oi, t in zip(offset, y)) for y in itertools.product(range(L), repeat=d)]
    for order in itertools.permutations(range(d)):
        for y in block:
            for (x, mu, s) in axial_path(cc, y, order):
                w[(x, mu)] = w.get((x, mu), 0.0) + s
    tot = 24 * L ** d
    return {k: v / tot for k, v in w.items() if v != 0}, block


def part_A():
    w, block = weight_vector()
    bset = set(block)
    vals = np.array(list(w.values()))
    n2 = float(np.sqrt((vals ** 2).sum())); l1 = float(np.abs(vals).sum()); mx = float(np.abs(vals).max())
    inside = all((x in bset) and (tuple(x[i] + (1 if i == mu else 0) for i in range(d)) in bset) for (x, mu) in w)
    b0 = w.get((c, 0), 0.0)
    ok = {"A1": n2 >= (L - 1) / (8 * L), "A2": l1 <= 2 * (L - 1), "A3": mx <= 1, "A4": inside}
    print(f"A: ||w|| = {n2:.6f} (bound {(L-1)/(8*L):.6f}); ||w||^2 = {n2**2:.6f}; sum|w| = {l1:.6f}; max|w| = {mx:.6f}; "
          f"w(b0) = {b0:.6f}; support {len(w)} links")
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("Part A:", "PASS" if all(ok.values()) else "FAIL")


def part_B():
    # B1: grid Laplacian on {0,1,2}^4
    pts = list(itertools.product(range(L), repeat=d)); idx = {p: i for i, p in enumerate(pts)}
    G = np.zeros((len(pts), len(pts)))
    for p in pts:
        for mu in range(d):
            q = list(p); q[mu] += 1; q = tuple(q)
            if q in idx:
                i, j = idx[p], idx[q]
                G[i, i] += 1; G[j, j] += 1; G[i, j] -= 1; G[j, i] -= 1
    ev = np.linalg.eigvalsh(G)
    nuN = ev[1]
    ok = {"B1": abs(nuN - 2 * (1 - np.cos(np.pi / L))) <= 1e-10}
    # B2: torus (Z/6)^4
    T = 6
    sites = list(itertools.product(range(T), repeat=d)); sid = {s: i for i, s in enumerate(sites)}
    links = [(s, mu) for s in sites for mu in range(d)]; lid = {l: i for i, l in enumerate(links)}
    Dm = np.zeros((len(links), len(sites)))  # d: sites -> links
    for (s, mu), i in lid.items():
        t = list(s); t[mu] = (t[mu] + 1) % T; t = tuple(t)
        Dm[i, sid[t]] += 1; Dm[i, sid[s]] -= 1
    Lap = Dm.T @ Dm
    # constraints: delta_c and 1_B per block
    C = []
    for X in itertools.product(range(T // L), repeat=d):
        base = tuple(L * x for x in X)
        cX = tuple(b + 1 for b in base)
        v = np.zeros(len(sites)); v[sid[cX]] = 1; C.append(v)
        u = np.zeros(len(sites))
        for y in itertools.product(range(L), repeat=d):
            u[sid[tuple(b + t for b, t in zip(base, y))]] = 1
        C.append(u)
    C = np.array(C)
    # orthonormal basis of Lambda_res = C^perp
    U, S, Vt = np.linalg.svd(C, full_matrices=True)
    r = int((S > 1e-10).sum())
    Bres = Vt[r:].T  # columns orthonormal, orthogonal to constraints
    Tm = Bres.T @ Lap @ Bres
    lam = np.linalg.eigvalsh(Tm)[0]
    ok["B2"] = lam >= 1 - 1e-10
    # B3
    w, _ = weight_vector()
    rng = np.random.default_rng(0)
    ok3 = True; worst_h = 0.0; worst_r = np.inf
    for _ in range(5):
        lamv = Bres @ rng.standard_normal(Bres.shape[1])
        dl = Dm @ lamv
        Pres_d = Bres @ (Bres.T @ (Lap @ lamv))
        ratio = (Pres_d @ Pres_d) / (dl @ dl)
        worst_r = min(worst_r, ratio)
        # h(d lambda) on each block: sum_b w(b - base) * (d lambda)(b)
        for X in itertools.product(range(T // L), repeat=d):
            base = tuple(L * x for x in X)
            hv = 0.0
            for (x, mu), val in w.items():
                xs = tuple((b + t) % T for b, t in zip(base, x))
                hv += val * dl[lid[(xs, mu)]]
            worst_h = max(worst_h, abs(hv))
        ok3 &= ratio >= 1 - 1e-10
    ok["B3"] = ok3 and worst_h <= 1e-12
    print(f"B: Neumann gap {nuN:.12f}; lambda_min(P_res Lap | Lambda_res) = {lam:.10f} (dim {Bres.shape[1]}); "
          f"min ||P_res d* d lambda||^2/||d lambda||^2 = {worst_r:.6f}; max |h(d lambda)| = {worst_h:.2e}")
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("Part B:", "PASS" if all(ok.values()) else "FAIL")


def part_C():
    found = 0; ok1 = ok2 = ok3 = True; n = 0
    for dim, side in ((1, 40), (2, 12)):
        pts = list(itertools.product(range(side), repeat=dim))
        P = np.array(pts)
        diff = np.abs(P[:, None, :] - P[None, :, :]); diff = np.minimum(diff, side - diff); D = diff.sum(-1)
        for g0 in (0.5, 1.0, 2.0):
            for seed in range(4):
                n += 1
                rng = np.random.default_rng(seed)
                U = rng.uniform(-1, 1, (len(pts), len(pts))); U = (U + U.T) / 2
                V = np.where(D <= 4, U * np.exp(-1.0 * D), 0.0); np.fill_diagonal(V, 0.0)
                lmin = np.linalg.eigvalsh(V)[0]
                if g0 + lmin < g0 / 2:
                    V = V * (g0 / 2) / (-lmin)
                K = g0 * np.eye(len(pts)) + V
                ev, Q = np.linalg.eigh(K); gam = ev[0]
                Ka = np.abs(K)
                ms = [m for m in np.arange(1, 101) / 100 if (Ka * (np.exp(m * D) - 1)).sum(1).max() <= gam / 2]
                if not ms:
                    continue
                m = max(ms); found += 1
                Ki = Q @ np.diag(1 / ev) @ Q.T
                Kh = Q @ np.diag(ev ** -0.5) @ Q.T
                r1 = (np.abs(Ki) * np.exp(m * D)).max() * gam / 2
                r2 = (np.abs(Kh) * np.exp(m * D)).max() * np.sqrt(gam) / 2
                ok1 &= r1 <= 1; ok2 &= r2 <= 1
                r3 = 0
                for t in (0.5, 2.0, 10.0):
                    Kt = Q @ np.diag(1 / (ev + t)) @ Q.T
                    r3 = max(r3, (np.abs(Kt) * np.exp(m * D)).max() * (gam + t) / 2)
                ok3 &= r3 <= 1
                print(f"  d={dim} g0={g0} seed={seed}: gamma={gam:.3f} m={m:.2f} ratios {r1:.3f} {r2:.3f} {r3:.3f}")
    ok = {"C1": ok1, "C2": ok2, "C3": ok3, "C4": found >= 20}
    print(f"C: m found in {found}/{n} instances")
    for k, v in ok.items():
        print(k, "PASS" if v else "FAIL")
    print("Part C:", "PASS" if all(ok.values()) else "FAIL")


if __name__ == "__main__":
    {"A": part_A, "B": part_B, "C": part_C}[sys.argv[1]]()
