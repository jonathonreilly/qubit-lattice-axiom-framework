#!/usr/bin/env python3
"""C1, C2 of CRITERIA.md: tree coefficients on a contractible box from exact group elements.

Open box of n^4 sites. U_b = exp(i A_b . sigma / 2). Action weight exp(-beta sum s_p), s_p = 1 - Tr U_p / 2.
Written for this gate. No witness script was opened or reused.
"""
import itertools
import json
import resource
import sys

import numpy as np

RSS_LIMIT_BYTES = 2 * 10**9


def check_rss():
    # macOS reports ru_maxrss in bytes
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        sys.exit("RSS limit reached")


n = 3
d = 4
sites = list(itertools.product(range(n), repeat=d))
sidx = {s: i for i, s in enumerate(sites)}
links = []
lidx = {}
for s in sites:
    for mu in range(d):
        t = list(s)
        t[mu] += 1
        if t[mu] < n:
            lidx[(s, mu)] = len(links)
            links.append((s, mu))
nl = len(links)
ns = len(sites)


def step(s, mu, sgn=1):
    t = list(s)
    t[mu] += sgn
    return tuple(t)


def path_links(start, moves):
    """moves = list of (mu, +1/-1). Returns list of (link index, eps)."""
    out = []
    x = start
    for mu, sg in moves:
        if sg > 0:
            out.append((lidx[(x, mu)], +1))
            x = step(x, mu, 1)
        else:
            x = step(x, mu, -1)
            out.append((lidx[(x, mu)], -1))
    assert x == start
    return out


plaqs = []
for s in sites:
    for mu in range(d):
        for nu in range(mu + 1, d):
            if s[mu] + 1 < n and s[nu] + 1 < n:
                plaqs.append(path_links(s, [(mu, 1), (nu, 1), (mu, -1), (nu, -1)]))
np_ = len(plaqs)

D = np.zeros((np_, nl))
for p, pl in enumerate(plaqs):
    for b, e in pl:
        D[p, b] += e
D0 = np.zeros((nl, ns))
for b, (s, mu) in enumerate(links):
    D0[b, sidx[step(s, mu)]] += 1
    D0[b, sidx[s]] -= 1

o = (1, 1, 1, 1)


def corner(mu, nu, start=o):
    return path_links(start, [(mu, 1), (nu, 1), (mu, -1), (nu, -1)])


paths = [corner(0, 1), corner(1, 2), corner(2, 0)]
J = [np.zeros(nl) for _ in paths]
for j, pa in zip(J, paths):
    for b, e in pa:
        j[b] += e

K2 = D.T @ D


def chart_landau():
    u, s, vt = np.linalg.svd(D0.T, full_matrices=True)
    rank = (s > 1e-10).sum()
    return vt[rank:].T  # orthonormal basis of ker d0^T


def tree_links(order_seed):
    rng = np.random.default_rng(order_seed)
    parent = list(range(ns))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    tree = []
    for b in rng.permutation(nl):
        s, mu = links[b]
        a, c = find(sidx[s]), find(sidx[step(s, mu)])
        if a != c:
            parent[a] = c
            tree.append(b)
    return set(tree)


def chart_tree(seed):
    tree = tree_links(seed)
    free = [b for b in range(nl) if b not in tree]
    S = np.zeros((nl, len(free)))
    for i, b in enumerate(free):
        S[b, i] = 1.0
    return S


def cov_chart(S):
    """one-colour covariance of X under exp(-F_2), F_2 = (1/8) |dX|^2, so C = 4 (S^T K S)^-1 in the chart."""
    H = S.T @ K2 @ S
    return 4 * S @ np.linalg.inv(H) @ S.T


def lvy(path, e, f):
    """A_Gamma(E, F) = sum_(s<t) eps_s eps_t [E(b_s) F(b_t) - E(b_t) F(b_s)]."""
    tot = 0.0
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            bi, ei = path[i]
            bj, ej = path[j]
            tot += ei * ej * (e[bi] * f[bj] - e[bj] * f[bi])
    return tot


def k_formulas(E):
    """Proposition 2.1 with E_i = G-normalised, d^T d E_i = J_i."""
    kc = -12 * (lvy(paths[0], E[1], E[2]) + lvy(paths[1], E[2], E[0]) + lvy(paths[2], E[0], E[1]))
    vv = 0.0
    P = [D @ e for e in E]
    for p, pl in enumerate(plaqs):
        for i in range(4):
            for j in range(i + 1, 4):
                bi, ei = pl[i]
                bj, ej = pl[j]
                m = np.array([[P[k][p], E[k][bi], E[k][bj]] for k in range(3)])
                vv += ei * ej * np.linalg.det(m)
    return kc, 12 * vv


# Exact SU(2), arrays of quaternions (w, x, y, z): U = w + i v.sigma
def q_exp(a):
    # a[..., 3]; U = exp(i a.sigma/2)
    th = np.linalg.norm(a, axis=-1) / 2
    sc = np.where(th > 1e-12, np.sin(th) / np.where(th > 0, th, 1), 1 - th**2 / 6) / 2
    return np.concatenate([np.cos(th)[..., None], sc[..., None] * a], axis=-1)


def q_mul(p, q):
    # (a + i u.s)(b + i v.s) = ab - u.v + i (a v + b u - u x v) . s
    a, u = p[..., 0], p[..., 1:]
    b, v = q[..., 0], q[..., 1:]
    w = a * b - np.sum(u * v, axis=-1)
    vec = a[..., None] * v + b[..., None] * u - np.cross(u, v)
    return np.concatenate([w[..., None], vec], axis=-1)


def q_inv(p):
    out = p.copy()
    out[..., 1:] *= -1
    return out


def holonomy(U, path):
    """U[batch, link, 4]; product in path order."""
    b0, e0 = path[0]
    W = U[:, b0] if e0 > 0 else q_inv(U[:, b0])
    for b, e in path[1:]:
        W = q_mul(W, U[:, b] if e > 0 else q_inv(U[:, b]))
    return W


def T_exact(U):
    v = [holonomy(U, pa)[:, 1:] for pa in paths]
    return 2 * np.sum(v[0] * np.cross(v[1], v[2]), axis=-1)


# plaquettes grouped by 4 link arrays for speed
pl_arr = np.array([[b for b, e in pl] for pl in plaqs])
pl_eps = np.array([[e for b, e in pl] for pl in plaqs])


def F_exact(A):
    """Sum_p s_p, exact; A[batch, nl, 3]."""
    U = q_exp(A)
    tot = np.zeros(A.shape[0])
    for start in range(0, np_, 256):
        idx = pl_arr[start:start + 256]
        eps = pl_eps[start:start + 256]
        Q = None
        for k in range(4):
            Uk = U[:, idx[:, k]].copy()
            Uk[..., 1:] *= eps[:, k][None, :, None]
            Q = Uk if Q is None else q_mul(Q, Uk)
        tot += np.sum(1 - Q[..., 0], axis=1)
    return tot


def sample(L, N, rng):
    """L: Cholesky-like factor nl x r; returns X[N, nl, 3]."""
    z = rng.standard_normal((N, L.shape[1], 3))
    return np.einsum("ij,njc->nic", L, z)


def factor(C):
    w, v = np.linalg.eigh(C)
    keep = w > 1e-10
    return v[:, keep] * np.sqrt(w[keep])


def jets(X, gam=0.02):
    tp = T_exact(q_exp(gam * X))
    tm = T_exact(q_exp(-gam * X))
    fp = F_exact(gam * X)
    fm = F_exact(-gam * X)
    t3 = (tp - tm) / (2 * gam**3)
    t4 = (tp + tm) / (2 * gam**4)
    f3 = (fp - fm) / (2 * gam**3)
    return t3, t4, f3


def mc_K(C, N=120000, batch=4000, seed=1):
    rng = np.random.default_rng(seed)
    L = factor(C)
    a, b = [], []
    for _ in range(N // batch):
        X = sample(L, batch, rng)
        t3, t4, f3 = jets(X)
        a.append(t4)
        b.append(-t3 * f3)
        check_rss()
    a = np.concatenate(a)
    b = np.concatenate(b)
    se = lambda x: x.std() / np.sqrt(len(x))
    return (a.mean(), se(a)), (b.mean(), se(b))


def grad_F3(a, C):
    """Polarised gradient of the cubic F_3 = (1/4) sum_p Phi_p . Q_p on batch a[N, nl, 3]."""
    g = np.zeros_like(a)
    for pl in plaqs:
        idx = [b for b, e in pl]
        eps = np.array([e for b, e in pl], float)
        phi = np.sum(eps[None, :, None] * a[:, idx], axis=1)
        q = np.zeros_like(phi)
        # dQ/dA and dPhi/dA
        for i in range(4):
            for j in range(i + 1, 4):
                q += -0.5 * eps[i] * eps[j] * np.cross(a[:, idx[i]], a[:, idx[j]])
        for i, b in enumerate(idx):
            g[:, b] += 0.25 * eps[i] * q
        for i in range(4):
            for j in range(i + 1, 4):
                c = -0.5 * eps[i] * eps[j]
                # d/dA_i of phi . (A_i x A_j) = A_j x phi ; d/dA_j = phi x A_i
                g[:, idx[i]] += 0.25 * c * np.cross(a[:, idx[j]], phi)
                g[:, idx[j]] += 0.25 * c * np.cross(phi, a[:, idx[i]])
    return g


def F3_formula(a):
    tot = np.zeros(a.shape[0])
    for pl in plaqs:
        idx = [b for b, e in pl]
        eps = np.array([e for b, e in pl], float)
        phi = np.sum(eps[None, :, None] * a[:, idx], axis=1)
        q = np.zeros_like(phi)
        for i in range(4):
            for j in range(i + 1, 4):
                q += -0.5 * eps[i] * eps[j] * np.cross(a[:, idx[i]], a[:, idx[j]])
        tot += 0.25 * np.sum(phi * q, axis=1)
    return tot


def t3_formula(a):
    ph = [np.sum(np.array([e for b, e in pa], float)[None, :, None] * a[:, [b for b, e in pa]], axis=1) for pa in paths]
    return 0.25 * np.sum(ph[0] * np.cross(ph[1], ph[2]), axis=-1), ph


def Dt3_dot_B(a, B):
    t, ph = t3_formula(a)
    dph = [np.sum(np.array([e for b, e in pa], float)[None, :, None] * B[:, [b for b, e in pa]], axis=1) for pa in paths]
    return 0.25 * (np.sum(dph[0] * np.cross(ph[1], ph[2]), axis=-1)
                   + np.sum(ph[0] * np.cross(dph[1], ph[2]), axis=-1)
                   + np.sum(ph[0] * np.cross(ph[1], dph[2]), axis=-1))


def c2(C, N=20000, batch=2000, seed=5):
    """C2a at rho = 1; C2b with C_rho = C^(1/2) f(C) C^(1/2) type multiplier."""
    rng = np.random.default_rng(seed)
    w, v = np.linalg.eigh(C)
    keep = w > 1e-10
    w, v = w[keep], v[:, keep]
    rho = 1.0 / (1.0 + 0.4 * np.log1p(1.0 / w))  # a slowly varying multiplier on the spectrum
    Lu = v * np.sqrt(w)
    Lr = v * np.sqrt(w * rho)
    Crho = (v * (w * rho)) @ v.T
    out = {}
    # C2a
    lhs, rhs = [], []
    for _ in range(N // batch):
        a = sample(Lu, batch, rng)
        B = -(1 / 3) * np.einsum("ij,njc->nic", C, grad_F3(a, C))
        lhs.append(Dt3_dot_B(a, B))
        rhs.append(-t3_formula(a)[0] * F3_formula(a))
        check_rss()
    lhs, rhs = np.concatenate(lhs), np.concatenate(rhs)
    d = lhs - rhs
    out["C2a"] = {"lhs": lhs.mean(), "rhs": rhs.mean(), "diff": d.mean(), "se": d.std() / np.sqrt(len(d))}
    # C2b: Monte Carlo of E[D t_3 . B] with covariance C_rho, B from unit C
    vals = []
    for _ in range(N // batch):
        a = sample(Lr, batch, rng)
        B = -(1 / 3) * np.einsum("ij,njc->nic", C, grad_F3(a, C))
        vals.append(Dt3_dot_B(a, B))
        check_rss()
    vals = np.concatenate(vals)
    # Wick prediction: mean over legs of the vertex with E_i weighted
    E = [C @ j / 4 for j in J]
    Er = [Crho @ j / 4 for j in J]
    pred = 0.0
    for leg in range(3):
        F = [E[k] if k == leg else Er[k] for k in range(3)]
        pred += k_formulas(F)[1] / 3
    out["C2b"] = {"mc": vals.mean(), "se": vals.std() / np.sqrt(len(vals)), "pred": pred}
    return out


def main():
    res = {"box": {"sites": ns, "links": nl, "plaquettes": np_}}
    charts = {"landau": chart_landau(), "tree1": chart_tree(11), "tree2": chart_tree(22)}
    Es = {}
    for name, S in charts.items():
        C = cov_chart(S)
        E = [C @ j / 4 for j in J]
        for e, j in zip(E, J):
            assert np.max(np.abs(K2 @ e - j)) < 1e-8
        kc, kv = k_formulas(E)
        Es[name] = E
        res[name] = {"K_comp": kc, "K_vert": kv, "K_T": kc + kv}
        print(name, res[name], flush=True)
    # C1a: exact group functions, Landau and tree1
    for name in ["landau", "tree1"]:
        C = cov_chart(charts[name])
        (m4, s4), (mv, sv) = mc_K(C)
        res[name]["mc_K_comp"] = (m4, s4)
        res[name]["mc_K_vert"] = (mv, sv)
        print(name, "mc", res[name]["mc_K_comp"], res[name]["mc_K_vert"], flush=True)

    # C1d: explicit linear slice with K_vert(tau_*) = 0
    E = Es["landau"]
    C = cov_chart(charts["landau"])
    P = np.array([[J[i] @ E[j] for j in range(3)] for i in range(3)])
    coeff = np.linalg.solve(P.T, np.array([0.0, 0.0, 1.0]))  # J' with <J',E_1>=<J',E_2>=0, <J',E_3>=1
    Jp = sum(c * j for c, j in zip(coeff, J))
    # bump theta at the base point neighbourhood; choose t to null K_vert
    th0 = np.zeros(ns)
    th0[sidx[(1, 1, 1, 1)]] = 1.0
    th0[sidx[(2, 1, 1, 1)]] = 0.5
    ths = [th0, np.roll(th0, 7), np.roll(th0, 13)]
    best = None
    for th in ths:
        s = D0 @ th
        kc0, kv0 = k_formulas([E[0], E[1], E[2] + s])
        kc00, kv00 = k_formulas(E)
        slope = kv0 - kv00
        if best is None or abs(slope) > abs(best[1]):
            best = (th, slope, kv00)
    th, slope, kv00 = best
    t = -kv00 / slope
    # Slice projection: Pi = Pi_L + t (d0 th) tensor J'
    PiL = charts["landau"] @ charts["landau"].T
    Pi = PiL + t * np.outer(D0 @ th, Jp)
    idem = np.max(np.abs(Pi @ Pi - Pi))
    grad_kill = np.max(np.abs(Pi @ D0))
    Ep = [Pi @ e for e in E]
    kc1, kv1 = k_formulas(Ep)
    res["rank_one_chart"] = {
        "t": t, "slope": slope, "idempotence_error": idem, "gradient_kill_error": grad_kill,
        "E_shifts": [float(np.max(np.abs(Ep[k] - E[k] - (t * (J[0] * 0) if k < 2 else t * D0 @ th)))) for k in range(3)],
        "K_comp": kc1, "K_vert": kv1, "K_T": kc1 + kv1,
        "same_K_T_as_landau": abs((kc1 + kv1) - res["landau"]["K_T"]),
        "curl_of_E_unchanged": float(max(np.max(np.abs(D @ (Ep[k] - E[k]))) for k in range(3))),
    }
    print(res["rank_one_chart"], flush=True)
    res["transport"] = c2(cov_chart(charts["landau"]))
    print(res["transport"], flush=True)
    with open(__file__.replace("nt2_box.py", "nt2_box.json"), "w") as f:
        json.dump(res, f, indent=1, default=float)


if __name__ == "__main__":
    main()
