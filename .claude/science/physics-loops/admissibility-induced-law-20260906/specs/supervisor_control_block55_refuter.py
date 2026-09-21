"""Block 55 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic calculus, transforms on a large torus, finite differences,
dense matrix exponentials).
W1  a ring of four sites with symbolic rates and a symbolic amplitude: d<H_w>/du_z = Re chi_z^dagger (H_w chi)_z, and the densities sum to <H_w>.
W2  a general field energy of weight one, sum over bonds of exp((u_x + u_y)/2) f(u_x - u_y) with f(d) = f2 d^2/2 + f4 d^4/24 + f6 d^6/720: the
    empty-space law in the bump test (two opposite neighbours at +-delta) gives u_x = delta^2/12 + c4 delta^4 with c4 depending on f4/f2; the power
    mean of order p gives p delta^2/6: the second order is that of p = 1/2 whatever f.
W3  ten bodies at random on a 16^3 torus: total pull zero to rounding for source strengths proportional to the energies, of order one otherwise.
W4  random rates and amplitude on a 3x3x3 torus: sum_x d(ledger)/du_x = ledger by finite differences, for two field energies of weight one; a field
    energy quadratic in u fails the identity.
W5  two walkers on a ring of 240 sites with dense exponentials: the ledger with the energy source, and its predicted rate with the probability source."""
import sys

import numpy as np
import sympy as sp
from scipy.linalg import expm

results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
n = 4
us = sp.symbols("u0:4", real=True)
ar = sp.symbols("a0:8", real=True)
br = sp.symbols("b0:8", real=True)
chi = sp.Matrix([ar[i] + sp.I * br[i] for i in range(8)])
m = sp.Rational(2, 5)
sx = sp.Matrix([[0, 1], [1, 0]]); sz = sp.Matrix([[1, 0], [0, -1]])
H = sp.zeros(8, 8)
for z in range(n):
    up = (z + 1) % n
    amp = sp.exp((us[z] + us[up]) / 2)
    for s1 in range(2):
        for s2 in range(2):
            H[2 * up + s1, 2 * z + s2] += sp.I / 2 * amp * sz[s1, s2]
            H[2 * z + s1, 2 * up + s2] += -sp.I / 2 * amp * sz[s1, s2]
            H[2 * z + s1, 2 * z + s2] += m * sp.exp(us[z]) * sx[s1, s2]
total = sp.re(sp.expand((chi.H * H * chi)[0, 0]))
hchi = H * chi
dens = [sp.re(sp.expand(sum(sp.conjugate(chi[2 * z + s]) * hchi[2 * z + s] for s in range(2)))) for z in range(n)]
ok = all(sp.simplify(sp.diff(total, us[z]) - dens[z]) == 0 for z in range(n)) and sp.simplify(sum(dens) - total) == 0
report("W1", ok, "symbolic rates and amplitude on a ring of four: d<H_w>/du_z = Re chi_z^dagger (H_w chi)_z at every site, and the densities sum to <H_w>")

# ------------------------------------------------------------------------------------------------ W2
d, f2, f4, f6, c2, c4, delta, p = sp.symbols("d f2 f4 f6 c2 c4 delta p")
f = f2 * d ** 2 / 2 + f4 * d ** 4 / 24 + f6 * d ** 6 / 720
ux = c2 * delta ** 2 + c4 * delta ** 4
law = 0
for uy in (delta, -delta, 0, 0, 0, 0):
    dd = ux - uy
    law += sp.exp((ux + uy) / 2) * (f.subs(d, dd) / 2 + sp.diff(f, d).subs(d, dd))         # d/du_x of exp((u_x+u_y)/2) f(u_x-u_y)
ser = sp.series(sp.expand(law), delta, 0, 6).removeO()
sol2 = sp.solve(sp.Eq(ser.coeff(delta, 2), 0), c2)[0]
sol4 = sp.simplify(sp.solve(sp.Eq(ser.coeff(delta, 4).subs(c2, sol2), 0), c4)[0])
power = sp.series(sp.log((sp.exp(p * delta) + sp.exp(-p * delta) + 4) / 6) / p, delta, 0, 4).removeO().coeff(delta, 2)
ok = sol2 == sp.Rational(1, 12) and sol4.has(f4) and sp.solve(sp.Eq(power, sol2), p) == [sp.Rational(1, 2)]
report("W2", ok, f"general weight-one bond energy: bump test gives u_x = delta^2/12 + ({sol4}) delta^4; the power mean of order p gives {power} delta^2: equal iff p = 1/2; the function f enters at the fourth order")

# ------------------------------------------------------------------------------------------------ W3
rng = np.random.default_rng(55)
side = 16
k = 2 * np.pi * np.fft.fftfreq(side)
kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
symbol = 1 - (np.cos(kx) + np.cos(ky) + np.cos(kz)) / 3
symbol[0, 0, 0] = 1.0
pos = [tuple(rng.integers(0, side, 3)) for _ in range(10)]
energies = rng.uniform(0.5, 3.0, 10)


def total_pull(strengths):
    fields = []
    for q, s in zip(pos, strengths):
        src = np.zeros((side,) * 3); src[q] = -0.1 * s
        sh = np.fft.fftn(src - src.mean()); sh[0, 0, 0] = 0
        fields.append(np.real(np.fft.ifftn(sh / symbol)))
    tot = np.zeros(3); scale = 0.0
    for a, (qa, ea) in enumerate(zip(pos, energies)):
        for b in range(10):
            if a == b:
                continue
            for j in range(3):
                upq = list(qa); upq[j] = (upq[j] + 1) % side; dnq = list(qa); dnq[j] = (dnq[j] - 1) % side
                pull = -ea * (fields[b][tuple(upq)] - fields[b][tuple(dnq)]) / 2
                tot[j] += pull; scale += abs(pull)
    return np.linalg.norm(tot) / scale


matched, count = total_pull(energies * 1.7), total_pull(np.ones(10))
report("W3", matched < 1e-12 and count > 1e-3, f"ten bodies on a 16^3 torus: |total pull| / sum |pulls| = {matched:.1e} with sources proportional to the energies, {count:.1e} with every body sourcing alike")

# ------------------------------------------------------------------------------------------------ W4
side3 = 3
sites = [(a, b, c) for a in range(side3) for b in range(side3) for c in range(side3)]
index = {s: i for i, s in enumerate(sites)}
pauli = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
bonds = [(s, tuple((s[i] + (1 if i == j else 0)) % side3 for i in range(3)), j) for s in sites for j in range(3)]
amp0 = rng.normal(size=54) + 1j * rng.normal(size=54)


def matter(u):
    h = np.zeros((54, 54), complex)
    for s, t, j in bonds:
        a = np.exp((u[index[s]] + u[index[t]]) / 2)
        h[2 * index[t]:2 * index[t] + 2, 2 * index[s]:2 * index[s] + 2] += 0.5j * a * pauli[j]
        h[2 * index[s]:2 * index[s] + 2, 2 * index[t]:2 * index[t] + 2] += -0.5j * a * pauli[j]
    return float(np.real(np.vdot(amp0, h @ amp0)))


def field_one(u):
    return sum((np.exp(u[index[s]] / 2) - np.exp(u[index[t]] / 2)) ** 2 for s, t, _ in bonds)


def field_two(u):
    return sum((np.exp(u[index[s]]) - np.exp(u[index[t]])) ** 2 / (np.exp(u[index[s]]) + np.exp(u[index[t]])) for s, t, _ in bonds)


def field_plain(u):
    return sum((u[index[s]] - u[index[t]]) ** 2 for s, t, _ in bonds)


u0 = rng.normal(0, 0.4, 27)
h = 1e-6


def euler_defect(fn):
    grad = sum((fn(u0 + h * np.eye(27)[i]) - fn(u0 - h * np.eye(27)[i])) / (2 * h) for i in range(27))
    return abs(grad - fn(u0)) / abs(fn(u0))


defects = [euler_defect(matter), euler_defect(field_one), euler_defect(field_two), euler_defect(field_plain)]
report("W4", max(defects[:3]) < 1e-6 and defects[3] > 0.5, f"sum_x d/du_x = identity (weight one) by finite differences: relative defect {defects[0]:.1e} for <H_w>, {defects[1]:.1e} and {defects[2]:.1e} for the two weight-one field energies, {defects[3]:.2f} for a field energy quadratic in u")

# ------------------------------------------------------------------------------------------------ W5
nr, gam = 240, 0.004
zs = np.arange(nr)


def ham(u, mm):
    rt = np.exp(u / 2)
    hh = np.zeros((2 * nr, 2 * nr), complex)
    for z in range(nr):
        up = (z + 1) % nr
        a = rt[z] * rt[up]
        hh[2 * up, 2 * z] += 0.5j * a; hh[2 * z, 2 * up] += -0.5j * a
        hh[2 * up + 1, 2 * z + 1] += -0.5j * a; hh[2 * z + 1, 2 * up + 1] += 0.5j * a
        hh[2 * z, 2 * z + 1] += mm * rt[z] ** 2; hh[2 * z + 1, 2 * z] += mm * rt[z] ** 2
    return hh


def gauss(z0, mm):
    env = np.exp(-((zs - z0) ** 2) / (4 * 12.0 ** 2))
    v = np.zeros(2 * nr, complex); v[0::2] = env; v[1::2] = env
    return v / np.linalg.norm(v)


def solve_field(s):
    kk = 2 * np.pi * np.fft.fftfreq(nr)
    sym = 2 - 2 * np.cos(kk); sym[0] = 1.0
    sh = np.fft.fft(-(s - s.mean())) * gam / sym; sh[0] = 0
    return np.real(np.fft.ifft(sh))


def dens_e(u, v, mm):
    return np.real((v.conj() * (ham(u, mm) @ v)).reshape(nr, 2).sum(axis=1))


out = {}
for source in ("energy", "probability"):
    ms = (0.3, 0.7)
    vs = [gauss(80.0, ms[0]), gauss(160.0, ms[1])]

    def src(vs, u):
        if source == "energy":
            return sum(dens_e(u, v, mm) for v, mm in zip(vs, ms))
        return 0.5 * sum((np.abs(v) ** 2).reshape(nr, 2).sum(axis=1) for v in vs)

    def settle(vs, u):
        for _ in range(8 if source == "energy" else 1):
            u = solve_field(src(vs, u))
        return u

    def ledger(vs, u):
        return sum(np.real(np.vdot(v, ham(u, mm) @ v)) for v, mm in zip(vs, ms)) + (u * (2 * u - np.roll(u, 1) - np.roll(u, -1))).sum() / (2 * gam)

    u = settle(vs, np.zeros(nr))
    start = ledger(vs, u)
    predicted = 0.0
    for _ in range(60):
        trial = [expm(-1j * ham(u, mm) * 1.0) @ v for v, mm in zip(vs, ms)]
        u_mid = 0.5 * (u + settle(trial, u))
        new = [expm(-1j * ham(u_mid, mm) * 1.0) @ v for v, mm in zip(vs, ms)]
        u_new = settle(new, u_mid)
        mis_old = sum(dens_e(u, v, mm) for v, mm in zip(vs, ms)) - src(vs, u)
        mis_new = sum(dens_e(u_new, v, mm) for v, mm in zip(new, ms)) - src(new, u_new)
        predicted += (0.5 * (mis_old + mis_new) * (u_new - u)).sum()
        vs, u = new, u_new
    out[source] = (ledger(vs, u) - start, predicted)
ok = abs(out["energy"][0]) < 1e-8 and abs(out["probability"][0]) > 1e-6 and abs(out["probability"][0] / out["probability"][1] - 1) < 0.02
report("W5", ok, f"two walkers on a ring of 240 (dense exponentials, 60 steps): ledger change {out['energy'][0]:+.1e} with the energy source; {out['probability'][0]:+.3e} with the probability source, against the predicted {out['probability'][1]:+.3e}")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
