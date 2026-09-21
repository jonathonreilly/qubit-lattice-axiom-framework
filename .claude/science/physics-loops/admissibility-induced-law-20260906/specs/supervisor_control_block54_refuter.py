"""Block 54 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic algebra with explicit 2x2 unitaries, symbolic calculus for a
general energy function, dense matrix exponentials, a sparse propagation against a cloud of rays).
W1  the general nearest-neighbour generator with seven symbolic 2x2 matrices: covariance under the explicit unitaries exp(-i pi sigma_z/4) and
    exp(-i pi sigma_x/4) (acting on the content) together with the quarter turns they induce on directions, plus hermiticity, leaves three real
    parameters and the symbol a_0 + 2a sum cos k_j + beta sum sigma_j sin k_j; adding inversion as a symmetry of the evolution with the content
    reversed (the antiunitary i sigma_y K) leaves beta alone; with the content untouched it removes beta.
W2  for a general energy function eps(k) and rate field w(x) = exp(u(x)), the ray equations of E = w eps give
    dv_j/dt = -w^2 sum_l d_j d_l (eps^2/2) d_l u + 2 (v . grad u) v_j  identically; for the walk the matrix is diag(cos 2 k_j) whatever the rest energy.
W3  a random rate field on a 3x3x3 torus: exp(-i w H t) keeps sum |psi|^2 / w and not sum |psi|^2; w H has the real spectrum of sqrt(w) H sqrt(w).
W4  a slab with a uniform gradient (reduced walk, open line): U(t) T_a = T_a U(lambda_a t), and <T_a>(t) = <psi| T_a exp(i (lambda_a - 1) H_w t) |psi>.
W5  the reduced walk against a cloud of rays: two rest energies at rest and one moving packet."""
import sys

import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
s0 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]]); sy = sp.Matrix([[0, -sp.I], [sp.I, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
sig = [sx, sy, sz]
dirs = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
syms = {}
mats = {}
for e in dirs:
    entries = []
    for a in range(2):
        for b in range(2):
            re, im = sp.symbols(f"r_{dirs.index(e)}_{a}{b} i_{dirs.index(e)}_{a}{b}", real=True)
            syms[(e, a, b)] = (re, im)
            entries.append(re + sp.I * im)
    mats[e] = sp.Matrix(2, 2, entries)
unknowns = [v for pair in syms.values() for v in pair]


def induced_rotation(u):
    r = sp.zeros(3, 3)
    for k in range(3):
        for j in range(3):
            r[k, j] = sp.simplify((sig[k] * u * sig[j] * u.H).trace() / 2)
    return r


def equations_from(matrix):
    out = []
    for entry in matrix:
        entry = sp.expand(entry)
        out += [sp.re(entry), sp.im(entry)]
    return out


eqs = []
for axis in (sz, sx):
    u = (s0 - sp.I * axis) / sp.sqrt(2)                                      # exp(-i pi axis / 4)
    rot = induced_rotation(u)
    for e in dirs:
        re_ = tuple(int(v) for v in (rot * sp.Matrix(e)))
        eqs += equations_from(u * mats[e] * u.H - mats[re_])
for e in dirs:
    me = tuple(-c for c in e)
    eqs += equations_from(mats[me] - mats[e].H)
base = [q for q in eqs if q != 0]
sol = sp.solve(base, unknowns, dict=True)[0]
free = [v for v in unknowns if v not in sol]
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
ks = (k1, k2, k3)
symbol = sp.zeros(2, 2)
for e in dirs:
    symbol += mats[e].subs(sol) * sp.exp(-sp.I * sum(e[j] * ks[j] for j in range(3)))          # (T_e psi)(x) = psi(x - e): symbol exp(-i k.e)
symbol = sp.simplify(symbol.applyfunc(lambda z: sp.simplify(z.rewrite(sp.cos))))
coef_id = sp.simplify((symbol.trace() / 2))
coef_sig = [sp.simplify((sig[j] * symbol).trace() / 2) for j in range(3)]
shape_ok = all(sp.simplify(sp.diff(coef_sig[j], ks[l])) == 0 for j in range(3) for l in range(3) if l != j) and all(sp.simplify(coef_sig[j].subs(ks[j], 0)) == 0 for j in range(3))
ratio = [sp.simplify(coef_sig[j] / sp.sin(ks[j])) for j in range(3)]
shape_ok = shape_ok and sp.simplify(ratio[0] - ratio[1]) == 0 and sp.simplify(ratio[0] - ratio[2]) == 0 and not ratio[0].has(k1, k2, k3)


def with_inversion(antiunitary, sign):
    extra = []
    for e in dirs:
        me = tuple(-c for c in e)
        if antiunitary:
            image = sy * mats[me].conjugate() * sy                           # Theta A Theta^-1 with Theta = i sigma_y K
        else:
            image = mats[me]
        extra += equations_from(image - sign * mats[e])
    allq = [q for q in base + extra if q != 0]
    s = sp.solve(allq, unknowns, dict=True)[0]
    left = [v for v in unknowns if v not in s]
    beta_alive = any(sp.simplify((sig[2] * mats[(0, 0, 1)].subs(s)).trace()) != 0 for _ in (0,))
    return len(left), beta_alive


n_rev, beta_rev = with_inversion(True, -1)       # content reversed; symmetry of the evolution: Theta H Theta^-1 = -H
n_same, beta_same = with_inversion(False, +1)    # content untouched; symmetry of the evolution: P H P^-1 = +H
report("W1", len(free) == 3 and shape_ok and (n_rev, beta_rev) == (1, True) and (n_same, beta_same) == (2, False),
       f"explicit unitaries: {len(free)} free real parameters; the content part of the symbol is {ratio[0]} * sigma_j sin k_j and the scalar part {coef_id}; inversion with the content reversed leaves {n_rev} parameter (the walk survives: {beta_rev}); with the content untouched {n_same} parameters (the walk survives: {beta_same})")

# ------------------------------------------------------------------------------------------------ W2
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
xs = (x1, x2, x3)
eps = sp.Function("eps")(k1, k2, k3)
u = sp.Function("u")(x1, x2, x3)
w = sp.exp(u)
v = [w * sp.diff(eps, ks[j]) for j in range(3)]
xdot = [w * sp.diff(eps, ks[l]) for l in range(3)]
kdot = [-eps * sp.diff(w, xs[l]) for l in range(3)]
worst = 0
for j in range(3):
    acc = sum(sp.diff(v[j], xs[l]) * xdot[l] + sp.diff(v[j], ks[l]) * kdot[l] for l in range(3))
    law = -w ** 2 * sum(sp.diff(eps ** 2 / 2, ks[j], ks[l]) * sp.diff(u, xs[l]) for l in range(3)) + 2 * sum(v[l] * sp.diff(u, xs[l]) for l in range(3)) * v[j]
    if sp.simplify(sp.expand(acc - law)) != 0:
        worst += 1
m = sp.symbols("m", positive=True)
lattice = sp.sqrt(m ** 2 + sum(sp.sin(kk) ** 2 for kk in ks))
hess = sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.diff(lattice ** 2 / 2, ks[i], ks[j])))
hess_ok = all(sp.simplify(hess[i, j] - (sp.cos(2 * ks[i]) if i == j else 0)) == 0 for i in range(3) for j in range(3))
report("W2", worst == 0 and hess_ok, "symbolic, general eps(k) and u(x): dv_j/dt = -w^2 sum_l d_j d_l (eps^2/2) d_l u + 2 (v . grad u) v_j identically; for eps^2 = m^2 + sum sin^2 k_j the matrix is diag(cos 2 k_j), free of m")

# ------------------------------------------------------------------------------------------------ W3
rng = np.random.default_rng(54)
side = 3
sites = [(a, b, c) for a in range(side) for b in range(side) for c in range(side)]
index = {s: i for i, s in enumerate(sites)}
npm = [np.array(sp.matrix2numpy(mm, dtype=complex)) for mm in sig]
n = 2 * len(sites)
ham = np.zeros((n, n), complex)
for s in sites:
    for j in range(3):
        for sign in (+1, -1):
            t = list(s); t[j] = (t[j] + sign) % side; t = tuple(t)
            ham[2 * index[t]:2 * index[t] + 2, 2 * index[s]:2 * index[s] + 2] += sign * 0.5j * npm[j]
rate = np.repeat(np.exp(rng.normal(0, 0.5, len(sites))), 2)
gen = rate[:, None] * ham
psi = rng.normal(size=n) + 1j * rng.normal(size=n)
out = expm(-1j * gen * 3.7) @ psi
weighted = abs((np.abs(out) ** 2 / rate).sum() / (np.abs(psi) ** 2 / rate).sum() - 1)
plain = abs((np.abs(out) ** 2).sum() / (np.abs(psi) ** 2).sum() - 1)
ev_gen = np.sort(np.linalg.eigvals(gen).real)
ev_sym = np.sort(np.linalg.eigvalsh(np.sqrt(rate)[:, None] * ham * np.sqrt(rate)[None, :]))
report("W3", weighted < 1e-12 and plain > 1e-3 and np.max(np.abs(np.linalg.eigvals(gen).imag)) < 1e-10 and np.max(np.abs(ev_gen - ev_sym)) < 1e-10,
       f"random rate field on the 3x3x3 torus: exp(-i w H t) changes sum |psi|^2 / w by {weighted:.1e} and sum |psi|^2 by {plain:.1e}; the spectrum of w H is real and equals that of sqrt(w) H sqrt(w) to {np.max(np.abs(ev_gen - ev_sym)):.1e}")


# ------------------------------------------------------------------------------------------------ W4, W5: the reduced walk on an open line
def line(n_sites, g, m):
    z = np.arange(n_sites, dtype=float)
    rt = np.exp(0.5 * g * (z - n_sites / 2))
    rows, cols, vals = [], [], []
    for s1, s2, c in ((0, 1, m), (1, 0, m)):
        rows.append(2 * np.arange(n_sites) + s1); cols.append(2 * np.arange(n_sites) + s2); vals.append(rt * rt * c + 0j)
    amp = rt[1:] * rt[:-1]
    up, dn = np.arange(1, n_sites), np.arange(0, n_sites - 1)
    for s, c in ((0, 1.0), (1, -1.0)):
        rows.append(2 * up + s); cols.append(2 * dn + s); vals.append(0.5j * amp * c)
        rows.append(2 * dn + s); cols.append(2 * up + s); vals.append(-0.5j * amp * c)
    return coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 * n_sites, 2 * n_sites)).tocsr()


def gaussian(n_sites, z0, width, k0, m):
    k = 2 * np.pi * np.fft.fftfreq(n_sites)
    gk = np.exp(-(np.angle(np.exp(1j * (k - k0))) ** 2) * width ** 2) * np.exp(-1j * k * z0)
    e = np.sqrt(m * m + np.sin(k) ** 2)
    # positive-energy spinor of m sigma_x + sin k sigma_z, smooth in k
    upc = (e + np.sin(k)); dnc = m * np.ones_like(k)
    norm = np.sqrt(upc ** 2 + dnc ** 2); norm[norm == 0] = 1.0
    psi = np.stack([np.fft.ifft(gk * upc / norm), np.fft.ifft(gk * dnc / norm)], axis=1).reshape(-1)
    return psi / np.linalg.norm(psi)


n_sites, g, m = 2400, 0.002, 0.3
hw = line(n_sites, g, m)
psi = gaussian(n_sites, n_sites / 2 - 40, 25.0, 0.1, m)
a, t = 37, 50.0
lam = np.exp(g * a)
shift = lambda v, by: np.roll(v.reshape(n_sites, 2), by, axis=0).reshape(-1)
left = expm_multiply(-1j * hw * t, shift(psi, a))
right = shift(expm_multiply(-1j * hw * (lam * t), psi), a)
psi_t = expm_multiply(-1j * hw * t, psi)
lhs = np.vdot(psi_t, shift(psi_t, a))
rhs = np.vdot(psi, shift(expm_multiply(1j * hw * ((lam - 1) * t), psi), a))
report("W4", np.linalg.norm(left - right) < 1e-10 and abs(lhs - rhs) < 1e-10,
       f"slab with a uniform gradient: |U(t) T_a psi - T_a U(lambda_a t) psi| = {np.linalg.norm(left - right):.1e}; <T_a>(t) against <psi| T_a exp(i (lambda_a - 1) H_w t) |psi>: difference {abs(lhs - rhs):.1e} (a = {a}, lambda_a = {lam:.4f})")


def cloud(g, zc, m, z0, width, k0, t_end, n=30000, steps=1500):
    r = np.random.default_rng(7)
    dz = width * r.standard_normal(n); dk = r.standard_normal(n) / (2 * width)
    z = z0 + np.concatenate([dz, -dz, dz, -dz]); k = k0 + np.concatenate([dk, dk, -dk, -dk])
    start = z.mean()
    f = lambda z, k: (np.exp(g * (z - zc)) * np.sin(k) * np.cos(k) / np.sqrt(m * m + np.sin(k) ** 2), -np.sqrt(m * m + np.sin(k) ** 2) * g * np.exp(g * (z - zc)))
    h = t_end / steps
    for _ in range(steps):
        a1, b1 = f(z, k); a2, b2 = f(z + h * a1 / 2, k + h * b1 / 2); a3, b3 = f(z + h * a2 / 2, k + h * b2 / 2); a4, b4 = f(z + h * a3, k + h * b3)
        z = z + h * (a1 + 2 * a2 + 2 * a3 + a4) / 6; k = k + h * (b1 + 2 * b2 + 2 * b3 + b4) / 6
    return z.mean() - start


rows = []
zs = np.arange(3000, dtype=float)
for m, k0 in ((0.2, 0.0), (0.6, 0.0), (0.2, 0.15)):
    hw = line(3000, 0.002, m)
    psi = gaussian(3000, 1500.0, 40.0, k0, m)
    start = ((np.abs(psi) ** 2).reshape(3000, 2).sum(axis=1) * zs).sum()
    out = expm_multiply(-1j * hw * 100.0, psi)
    walk = ((np.abs(out) ** 2).reshape(3000, 2).sum(axis=1) * zs).sum() - start
    rays = cloud(0.002, 1500.0, m, start, 40.0, k0, 100.0)
    rows.append((m, k0, walk, rays))
report("W5", all(abs(wk / ry - 1) < 2e-3 for _, _, wk, ry in rows) and abs(rows[0][2] / rows[1][2] - 1) < 0.01,
       "reduced walk against a cloud of rays (g = 0.002, T = 100): " + "; ".join(f"rest energy {m}, k0 {k0}: walk {wk:+.3f}, rays {ry:+.3f}" for m, k0, wk, ry in rows) + f"; the two packets at rest fall alike to {abs(rows[0][2] / rows[1][2] - 1):.1e}")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
