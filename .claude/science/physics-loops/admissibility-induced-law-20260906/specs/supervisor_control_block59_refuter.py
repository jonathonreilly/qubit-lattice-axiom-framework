"""Block 59 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic calculus, a transform solve on a large torus, dense random
matrices).
W1  symbolic rays of E = sqrt(a(x)^2 m^2 + c(x)^2 k^2): a slow body falls at -c^2 grad log a; a ray crossing the gradient bends at -c^2 grad log c.
W2  the covariant law for log c_b with symbolic alpha, beta, delta: eigenvalues at zero wave vector {0, -12 beta, -12 beta}; the isotropic mode's
    second order is -(alpha + 2 beta + 2 delta) k^2.
W3  the static field of an isotropic source on a 48^3 torus: the anisotropic parts u_j - mean are of the size of the scalar's second differences
    times (alpha - delta + beta/2)/(12 beta), and fall off faster than the scalar.
W4  a random complex amplitude on a 4^3 torus with random bond and site rates: hop energies plus on-site energies equal <H>; finite-difference
    derivatives of <H> with respect to log c_b and log w_x equal t_b and r_x; a body at rest has no hop energy.
W5  an algebraic clause for a length under a change of the unit of rate: only ratios survive; l = wbar/w does with the reference.
W6  a cross term in the field's quadratic energy between the differences of log l and of u: log l = -(kappa/S) u for a body at rest."""
import sys

import numpy as np
import sympy as sp

results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
x, y, z, kx, ky, kz, m = sp.symbols("x y z k_x k_y k_z m", real=True)
a = sp.Function("a")(x, y, z); c = sp.Function("c")(x, y, z)
E = sp.sqrt(a ** 2 * m ** 2 + c ** 2 * (kx ** 2 + ky ** 2 + kz ** 2))
X, K = (x, y, z), (kx, ky, kz)
v = [sp.diff(E, q) for q in K]; kd = [-sp.diff(E, q) for q in X]
acc = [sum(sp.diff(v[j], X[l]) * v[l] + sp.diff(v[j], K[l]) * kd[l] for l in range(3)) for j in range(3)]
slow = sp.simplify(acc[2].subs({kx: 0, ky: 0, kz: 0}) + c ** 2 * sp.diff(a, z) / a)
light = sp.simplify(acc[2].subs({m: 0, ky: 0, kz: 0}) + c * sp.diff(c, z))
report("W1", slow == 0 and light == 0, "symbolic rays of E = sqrt(a^2 m^2 + c^2 k^2): slow body -c^2 dlog a; ray crossing the gradient -c^2 dlog c")

# ------------------------------------------------------------------------------------------------ W2
k1, k2, k3, al, be, de, eps = sp.symbols("k1 k2 k3 alpha beta delta epsilon", real=True)
ks = (k1, k2, k3)
c0 = -2 * al - 8 * be - 4 * de
M = sp.zeros(3, 3)
for j in range(3):
    M[j, j] = c0 + 2 * al * sp.cos(ks[j]) + 2 * de * sum(sp.cos(ks[l]) for l in range(3) if l != j)
    for l in range(3):
        if l != j:
            M[j, l] = 4 * be * sp.cos(ks[j] / 2) * sp.cos(ks[l] / 2)
ev = M.subs({k1: 0, k2: 0, k3: 0}).eigenvals()
iso = sp.Matrix([1, 1, 1])
quad = sp.series(sp.simplify((iso.T * M * iso)[0, 0]).subs({k1: eps * k1, k2: eps * k2, k3: eps * k3}), eps, 0, 3).removeO().coeff(eps, 2)
rowsum = sp.series((M * iso)[0].subs({k1: eps * k1, k2: eps * k2, k3: eps * k3}), eps, 0, 3).removeO().coeff(eps, 2)
slave = sp.simplify(rowsum + (de + be / 2) * (k1 ** 2 + k2 ** 2 + k3 ** 2) + (al - de + be / 2) * k1 ** 2)
ok = ev == {sp.Integer(0): 1, -12 * be: 2} and sp.simplify(quad + (al + 2 * be + 2 * de) * (k1 ** 2 + k2 ** 2 + k3 ** 2)) == 0 and slave == 0
report("W2", ok, f"symbolic law for log c_b: eigenvalues at zero wave vector {ev}; isotropic mode at second order: -(alpha + 2 beta + 2 delta) k^2; the law applied to the isotropic vector is -(delta + beta/2) k^2 - (alpha - delta + beta/2) k_j^2: its direction-dependent part drives the anisotropic modes at second order")

# ------------------------------------------------------------------------------------------------ W3
side = 48
kk = 2 * np.pi * np.fft.fftfreq(side)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing="ij")
kv = (KX, KY, KZ)
alpha, beta, delta = 1.0, 0.25, 0.2
c0n = -2 * alpha - 8 * beta - 4 * delta
Mk = np.zeros((side, side, side, 3, 3))
for j in range(3):
    Mk[..., j, j] = c0n + 2 * alpha * np.cos(kv[j]) + 2 * delta * sum(np.cos(kv[l]) for l in range(3) if l != j)
    for l in range(3):
        if l != j:
            # bond midpoints sit half a site along their own axis: phases exp(i (k_j - k_l)/2) are carried by the transform of bond fields indexed at their base site
            Mk[..., j, l] = beta * (1 + np.exp(1j * kv[j])).real * 0 + beta * np.real((1 + np.exp(-1j * kv[l])) * (1 + np.exp(1j * kv[j])))
src = np.zeros((side, side, side, 3)); src[0, 0, 0, :] = 1.0                        # an ISOTROPIC source: the three bonds that leave one site
sh = np.fft.fftn(src, axes=(0, 1, 2))
# bond fields are indexed at their base sites, so the coupling between directions carries phases: M_jl(k) = beta (1 + e^{-i k_l})(1 + e^{+i k_j})
Mc = np.zeros((side, side, side, 3, 3), complex)
for j in range(3):
    Mc[..., j, j] = Mk[..., j, j]
    for l in range(3):
        if l != j:
            Mc[..., j, l] = beta * (1 + np.exp(-1j * kv[l])) * (1 + np.exp(1j * kv[j]))
Mc[0, 0, 0] = np.eye(3)
sh[0, 0, 0] = 0
uh = np.linalg.solve(Mc, sh[..., None])[..., 0]
uh[0, 0, 0] = 0
u = np.real(np.fft.ifftn(uh, axes=(0, 1, 2)))
# centre each bond field on the sites: average the two bonds along j that touch a site (removes the half-site offsets between the three fields)
uc = np.stack([0.5 * (u[..., j] + np.roll(u[..., j], 1, axis=j)) for j in range(3)], axis=3)
mean = uc.mean(axis=3)
coef = (alpha - delta + beta / 2) / (12 * beta) + 1.0 / 8                              # the slaving coefficient, plus 1/8 from the centring
rows = []
for pt in ((6, 3, 0), (9, 0, 5), (10, 6, 3)):
    d2 = [np.roll(mean, 1, ax)[pt] + np.roll(mean, -1, ax)[pt] - 2 * mean[pt] for ax in range(3)]
    lap = sum(d2)
    got = [uc[pt][j] - mean[pt] for j in range(3)]
    want = [coef * (d2[j] - lap / 3) for j in range(3)]
    rows.append((pt, mean[pt], got, want))
size = max(abs(g_) for _, _, got, _ in rows for g_ in got)
err = max(abs(g_ - w_) for _, _, got, want in rows for g_, w_ in zip(got, want))
falloff = abs(rows[0][1] / rows[2][1])
aniso_falloff = max(abs(v) for v in rows[0][2]) / max(abs(v) for v in rows[2][2])
report("W3", err < 0.25 * size and aniso_falloff > 2 * falloff, "an isotropic source on a 48^3 torus: " + "; ".join(f"at {pt}: scalar {mn:+.3e}, anisotropic parts ({', '.join(f'{v:+.2e}' for v in got)}) against the slaved form ({', '.join(f'{v:+.2e}' for v in want)})" for pt, mn, got, want in rows) + f": the anisotropic parts are of the size of the scalar's second derivatives and fall off faster than it ({aniso_falloff:.1f} against {falloff:.1f} between the first and the last point)")

# ------------------------------------------------------------------------------------------------ W4
rng = np.random.default_rng(59)
s4 = 4
sites = [(p, q, r) for p in range(s4) for q in range(s4) for r in range(s4)]
index = {s: i for i, s in enumerate(sites)}
pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
bonds = [(s, tuple((s[i] + (1 if i == j else 0)) % s4 for i in range(3)), j) for s in sites for j in range(3)]
logc = rng.normal(0, 0.3, len(bonds)); logw = rng.normal(0, 0.3, len(sites)); mrest = 0.7


def ham(logc, logw):
    h = np.zeros((2 * len(sites),) * 2, complex)
    for b, (s, t, j) in enumerate(bonds):
        blk = 0.5j * np.exp(logc[b]) * pauli[j]
        h[2 * index[t]:2 * index[t] + 2, 2 * index[s]:2 * index[s] + 2] += blk
        h[2 * index[s]:2 * index[s] + 2, 2 * index[t]:2 * index[t] + 2] += blk.conj().T
    for s in sites:
        h[2 * index[s]:2 * index[s] + 2, 2 * index[s]:2 * index[s] + 2] += np.exp(logw[index[s]]) * mrest * pauli[0]
    return h


chi = rng.normal(size=2 * len(sites)) + 1j * rng.normal(size=2 * len(sites))
energy = lambda lc, lw: float(np.real(np.vdot(chi, ham(lc, lw) @ chi)))
e0 = energy(logc, logw)
hh = 1e-6
t_fd = [(energy(logc + hh * np.eye(len(bonds))[b], logw) - energy(logc - hh * np.eye(len(bonds))[b], logw)) / (2 * hh) for b in range(0, len(bonds), 17)]
t_direct = []
for b in range(0, len(bonds), 17):
    s, t, j = bonds[b]
    blk = 0.5j * np.exp(logc[b]) * pauli[j]
    t_direct.append(2 * np.real(np.vdot(chi[2 * index[t]:2 * index[t] + 2], blk @ chi[2 * index[s]:2 * index[s] + 2])))
tot_t = sum(2 * np.real(np.vdot(chi[2 * index[t]:2 * index[t] + 2], 0.5j * np.exp(logc[b]) * pauli[j] @ chi[2 * index[s]:2 * index[s] + 2])) for b, (s, t, j) in enumerate(bonds))
tot_r = sum(np.exp(logw[index[s]]) * mrest * np.real(np.vdot(chi[2 * index[s]:2 * index[s] + 2], pauli[0] @ chi[2 * index[s]:2 * index[s] + 2])) for s in sites)
rest = np.zeros(2 * len(sites), complex)
envr = rng.uniform(0.5, 1.5, len(sites))
rest[0::2] = envr; rest[1::2] = envr
hop_rest = max(abs(2 * np.real(np.vdot(rest[2 * index[t]:2 * index[t] + 2], 0.5j * pauli[j] @ rest[2 * index[s]:2 * index[s] + 2]))) for s, t, j in bonds)
report("W4", abs(tot_t + tot_r - e0) < 1e-9 * abs(e0) and max(abs(np.array(t_fd) - np.array(t_direct))) < 1e-6 and hop_rest < 1e-12,
       f"random amplitude, bond rates and site rates on a 4^3 torus: hop plus on-site energies against <H>: {abs(tot_t + tot_r - e0):.1e}; finite-difference d<H>/dlog c_b against t_b on twelve bonds: {max(abs(np.array(t_fd) - np.array(t_direct))):.1e}; largest hop energy of a body at rest {hop_rest:.1e}")

# ------------------------------------------------------------------------------------------------ W5
w1, w2, wb, tt = sp.symbols("w1 w2 wbar t", positive=True)
clauses = {"ratio": sp.sqrt(w1 / w2), "depth": 1 / sp.sqrt(w1 * w2), "depth against ambient": wb / sp.sqrt(w1 * w2)}
inv = {k: sp.simplify(v.subs({w1: tt * w1, w2: tt * w2, wb: tt * wb}, simultaneous=True) - v) == 0 for k, v in clauses.items()}
report("W5", inv == {"ratio": True, "depth": False, "depth against ambient": True}, f"a length under a change of the unit of rate: {inv}: a local clause can follow the ratio of neighbouring rates only; the depth needs the ambient rate")

# ------------------------------------------------------------------------------------------------ W6
nb = 7
inner = [(p_, q_, r_) for p_ in range(1, nb - 1) for q_ in range(1, nb - 1) for r_ in range(1, nb - 1)]
ix = {s_: i for i, s_ in enumerate(inner)}
lamm = np.zeros((len(inner),) * 2)
for s_, i in ix.items():
    lamm[i, i] = 6
    for d_ in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
        t_ = (s_[0] + d_[0], s_[1] + d_[1], s_[2] + d_[2])
        if t_ in ix:
            lamm[i, ix[t_]] -= 1
su, sl, kap = 2.0, 3.0, 1.4
big = np.block([[su * lamm, kap * lamm], [kap * lamm, sl * lamm]])                     # the field's quadratic energy in (u, log l), walls held
rhs = np.zeros(2 * len(inner)); rhs[ix[(3, 3, 3)]] = -0.4                              # a body at rest sources u only
sol = np.linalg.solve(big, rhs)
uu, ll = sol[:len(inner)], sol[len(inner):]
report("W6", np.max(np.abs(ll + kap / sl * uu)) < 1e-12 and su * sl > kap ** 2, f"a cross term between the differences of log l and of u (7^3 box, walls held, a body at rest sourcing u only): log l = -(kappa/S) u to {np.max(np.abs(ll + kap / sl * uu)):.1e}; the bending of a ray is then 1 + kappa/S = {1 + kap / sl:.3f} times the fall of a slow body; kappa is a free number (below sqrt(S_u S))")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
