"""Coordinator check of A55, from scratch.  Coarse corner lattice, eps(v) = (-1)^(v1+v2+v3), records f_v in {+-1}^3.
(a) h_v = sum_{d = +-e_a} (f_v.d) [d.(f_v x f_{v+d})]: cyclic texture f_i = (-1)^{v_{i+1}} gives -12 eps; mirror
    f_i = (-1)^{v_{i-1}} gives +12 eps; uniform and hedgehog f_i = (-1)^{v_i} give 0 staggered part.
(b) covariance: h_{g v}[g.f] = h_v[f] for the 24 turns about a corner and about a cube centre (records turned too).
(c) pi-flux KS hopping + mu h_v n_v (mu = 0.25 on the cyclic texture) on 8^3: |E| = sqrt(4 sum cos^2 k + 9), gap 6;
    control: uniform texture, gap 0."""
import itertools
import numpy as np
par = lambda n: 1 - 2 * (int(n) % 2)
O = [np.array(M) for M in {tuple(map(tuple, s[:, None] * np.eye(3, dtype=int)[list(p)]))
     for p in itertools.permutations(range(3)) for s in map(np.array, itertools.product((1, -1), repeat=3))}
     if round(np.linalg.det(np.array(M))) == 1]
D = [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)]
textures = {"cyclic": lambda v: np.array([par(v[1]), par(v[2]), par(v[0])]),
            "mirror": lambda v: np.array([par(v[2]), par(v[0]), par(v[1])]),
            "uniform": lambda v: np.array([1, 1, 1]),
            "hedgehog": lambda v: np.array([par(v[0]), par(v[1]), par(v[2])])}
def h(F, v):
    fv = F(v)
    return sum(np.dot(fv, d) * np.dot(d, np.cross(fv, F(tuple(np.add(v, d))))) for d in D)
eps = lambda v: par(sum(v))
ok = True
for name, F in textures.items():
    vals = {v: h(F, v) for v in itertools.product(range(4), repeat=3)}
    stag = sum(vals[v] * eps(v) for v in vals) / len(vals)
    mean = sum(vals.values()) / len(vals)
    exact = all(vals[v] == stag * eps(v) + mean for v in vals)
    print(f"(a) {name:8s}: staggered part {stag:+.1f}, mean {mean:+.1f}, h = stag*eps + mean everywhere: {exact}")
    want = {"cyclic": -12, "mirror": 12, "uniform": 0, "hedgehog": 0}[name]
    ok &= abs(stag - want) < 1e-12 and abs(mean) < 1e-12
rng = np.random.default_rng(7)
rec = {v: rng.choice([-1, 1], 3) for v in itertools.product(range(-3, 4), repeat=3)}
Frand = lambda v: rec[tuple(v)]
bad = 0; tot = 0
for c in (np.zeros(3), np.array([0.5, 0.5, 0.5])):
    for R in O:
        img = {}
        for v, f in rec.items():
            w = c + R @ (np.array(v) - c)
            if np.allclose(w, np.round(w)): img[tuple(np.round(w).astype(int))] = R @ f
        G = lambda v: img[tuple(v)]
        for v in itertools.product(range(-1, 2), repeat=3):
            w = tuple(np.round(c + R @ (np.array(v) - c)).astype(int))
            try:
                tot += 1; bad += abs(h(G, w) - h(Frand, v)) > 1e-12
            except KeyError:
                tot -= 1
ok &= bad == 0 and tot > 0
print(f"(b) covariance over 48 turns (corner and cube-centre) on a random background: {bad}/{tot} failures")
L = 8; sites = list(itertools.product(range(L), repeat=3)); sid = {x: i for i, x in enumerate(sites)}
def gap(F, mu):
    H = np.zeros((L**3, L**3))
    for x in sites:
        for a in range(3):
            y = list(x); y[a] = (y[a] + 1) % L
            eta = par(sum(x[:a])); H[sid[x], sid[tuple(y)]] += eta; H[sid[tuple(y)], sid[x]] += eta
        H[sid[x], sid[x]] += mu * h(F, x)
    ev = np.linalg.eigvalsh(H)
    return ev[L**3 // 2] - ev[L**3 // 2 - 1], ev
g, ev = gap(textures["cyclic"], 0.25)
ks = 2 * np.pi * np.arange(L) / L
pred = np.sort(np.concatenate([s * np.sqrt(4 * np.array([sum(np.cos(k)**2 for k in kk) for kk in itertools.product(ks, repeat=3)]) + 9) for s in (1, -1)]))
pred = np.sort(np.concatenate([pred[::2], pred[1::2]]))
match = np.allclose(np.sort(np.unique(np.round(np.abs(ev), 8))), np.sort(np.unique(np.round(np.abs(pred), 8))))
g0, _ = gap(textures["uniform"], 0.25)
ok &= abs(g - 6) < 1e-9 and match and abs(g0) < 1e-9
print(f"(c) cyclic texture, mu = 0.25: gap {g:.6f} (A55: 6.000), |E| set matches sqrt(4 sum cos^2 + 9): {match}; uniform control gap {g0:.1e}")
print("TOTAL:", "PASS" if ok else "FAIL")
