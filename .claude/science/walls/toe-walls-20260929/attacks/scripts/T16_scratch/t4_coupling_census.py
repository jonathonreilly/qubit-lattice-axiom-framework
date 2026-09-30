#!/usr/bin/env python3
"""T16 test 4: which physical arrow is free, and under which coupling of records to the wave?
8-qubit chain.  Branch PASSIVE: records are sampled from the z-marginal and never act on the wave.
Branch ACTIVE: a birth is a projective z-lock (Born outcome); the site is then frozen (XX+YY on
its bonds removed).  6 births at unit spacing.  Observables: count n, half-chain entanglement S,
energy <H_orig>."""
import numpy as np

rng = np.random.default_rng(1604)
N = 8
I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0, -1.0]).astype(complex)


def op(pauli, sites):
    out = np.array([[1.0 + 0j]])
    for i in range(N):
        out = np.kron(out, pauli[i] if i in pauli else I2) if False else out
    return None


def site_op(d):  # d: {site: matrix}
    out = np.array([[1.0 + 0j]])
    for i in range(N):
        out = np.kron(out, d.get(i, I2))
    return out


XX = {i: site_op({i: sx, i + 1: sx}) for i in range(N - 1)}
YY = {i: site_op({i: sy, i + 1: sy}) for i in range(N - 1)}
ZZ = {i: site_op({i: sz, i + 1: sz}) for i in range(N - 1)}
Z1 = {i: site_op({i: sz}) for i in range(N)}
ZZ2 = {i: site_op({i: sz, i + 2: sz}) for i in range(N - 2)}
Delta, h, J2 = 0.5, 0.7, 0.3
Zdiag = {i: np.real(np.diag(Z1[i])) for i in range(N)}


def H_of(locked):
    H = np.zeros((2 ** N, 2 ** N), complex)
    for i in range(N - 1):
        if i not in locked and (i + 1) not in locked:
            H += XX[i] + YY[i]
        H += Delta * ZZ[i]
    for i in range(N):
        H += h * (-1) ** i * Z1[i]
    for i in range(N - 2):
        H += J2 * ZZ2[i]
    return H


H0 = H_of(set())
w0, V0 = np.linalg.eigh(H0)
E0, Emax = w0[0], w0[-1]
cache = {}


def evolve(psi, locked, t):
    key = frozenset(locked)
    if key not in cache:
        w, V = np.linalg.eigh(H_of(set(locked)))
        cache[key] = (w, V)
    w, V = cache[key]
    return V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))


def S_half(psi):
    M = psi.reshape(2 ** (N // 2), 2 ** (N // 2))
    s = np.linalg.svd(M, compute_uv=False)
    p = s ** 2
    p = p[p > 1e-14]
    return float(-(p * np.log(p)).sum())


def energy(psi):
    return float(np.real(psi.conj() @ H0 @ psi))


def haar():
    v = rng.normal(size=2 ** N) + 1j * rng.normal(size=2 ** N)
    return v / np.linalg.norm(v)


neel_idx = int("01" * (N // 2), 2)
neel = np.zeros(2 ** N, complex)
neel[neel_idx] = 1
ground = V0[:, 0].astype(complex)
Trev = 1.8
reversed_start = np.conj(evolve(neel, set(), Trev))

# entropy curve of the Neel start (to justify Trev)
curve = [S_half(evolve(neel, set(), t)) for t in (0, 0.6, 1.2, 1.8, 3, 6, 8, 10)]
print("Neel S_half(t) at t=0,.6,1.2,1.8,3,6,8,10:", np.round(curve, 3), " (max ln 16 = %.3f)" % np.log(16))
print("energies: E0 = %.3f, Emax = %.3f, spectrum mean = %.3f; Neel E = %.3f; ground E = %.3f\n" % (
    E0, Emax, np.trace(H0).real / 2 ** N, energy(neel), energy(ground)))

nb, tau = 6, 0.3


def zprob(psi, x):
    idx = np.arange(2 ** N)
    bit = (idx >> (N - 1 - x)) & 1
    p1 = float(np.sum(np.abs(psi[bit == 1]) ** 2))
    return 1 - p1, p1, bit


def passive(psi0, rng_):
    psi = psi0.copy()
    free = list(range(N))
    n = 0
    for j in range(nb):
        psi = evolve(psi, set(), tau)
        x = free.pop(rng_.integers(len(free)))
        p0, p1, _ = zprob(psi, x)
        _ = rng_.random() < p1  # sampled record value; the wave is not touched
        n += 1
    return n, S_half(psi) - S_half(psi0), energy(psi) - energy(psi0)


def active(psi0, rng_):
    psi = psi0.copy()
    locked = []
    free = list(range(N))
    n = 0
    for j in range(nb):
        psi = evolve(psi, set(locked), tau)
        x = free.pop(rng_.integers(len(free)))
        p0, p1, bit = zprob(psi, x)
        val = 1 if rng_.random() < p1 else 0
        psi = np.where(bit == val, psi, 0)
        psi = psi / np.linalg.norm(psi)
        locked.append(x)
        n += 1
    return n, S_half(psi) - S_half(psi0), energy(psi) - energy(psi0)


starts = {"ground": [ground], "Neel": [neel], "Haar": [haar() for _ in range(6)], "reversed Neel": [reversed_start]}
NT = 60
print(f"{'start':14s} | {'branch':7s} | {'dn':>3s} | {'dS_half':>9s} | {'dE':>8s}")
res = {}
for name, lst in starts.items():
    for br, fn, ntraj in (("passive", passive, 1), ("active", active, NT)):
        dn = []
        dS = []
        dE = []
        for psi0 in lst:
            for _ in range(ntraj):
                a, b, c = fn(psi0, rng)
                dn.append(a); dS.append(b); dE.append(c)
        res[(name, br)] = (np.mean(dn), np.mean(dS), np.mean(dE), np.std(dS), np.std(dE))
        print(f"{name:14s} | {br:7s} | {np.mean(dn):3.0f} | {np.mean(dS):+9.3f} | {np.mean(dE):+8.3f}   "
              f"(sd dS {np.std(dS):.3f}, sd dE {np.std(dE):.3f})")

pg = res[("ground", "passive")]
print()
ok = []
ok.append(("count rises in all 8 cases", all(v[0] == nb for v in res.values())))
ok.append(("passive ground: dS = 0 and dE = 0", abs(pg[1]) < 1e-9 and abs(pg[2]) < 1e-9))
ok.append(("passive Neel dS > 0", res[("Neel", "passive")][1] > 0.3))
ok.append(("passive Haar |dS| < 0.15", abs(res[("Haar", "passive")][1]) < 0.15))
ok.append(("passive reversed dS < 0", res[("reversed Neel", "passive")][1] < -0.3))
ok.append(("active: <E> moves toward 0 for Neel, reversed, ground", res[('ground','active')][2] > 0 and res[('Neel','active')][2] < 0 and res[('reversed Neel','active')][2] < 0))
ok.append(("active ground dE > 0.5", res[("ground", "active")][2] > 0.5))
ok.append(("active Haar dS < 0", res[("Haar", "active")][1] < 0))
for k, v in ok:
    print(f"  {'PASS' if v else 'FAIL'}: {k}")
print("RESULT 4:", all(v for _, v in ok))

# 4b: microcanonical-window starts
print("\n4b: active/passive dE versus starting energy (window states, 40 trajectories each)")
viol = 0
rows = []
for Et in (-10, -7, -4, -2, 0, 2, 4, 6, 8):
    sel = np.where(np.abs(w0 - Et) < 0.8)[0]
    if len(sel) < 3:
        continue
    starts_b = []
    for _ in range(4):
        c = rng.normal(size=len(sel)) + 1j * rng.normal(size=len(sel))
        c /= np.linalg.norm(c)
        starts_b.append(V0[:, sel] @ c)
    Es = np.mean([energy(p) for p in starts_b])
    dEa = np.mean([active(p, rng)[2] for p in starts_b for _ in range(40)])
    dEp = np.mean([passive(p, rng)[2] for p in starts_b])
    rows.append((Es, dEa, dEp))
    bad = abs(Es) > 1.5 and np.sign(dEa) != -np.sign(Es)
    viol += bad
    print(f"  E_start = {Es:+6.2f}: active dE = {dEa:+7.3f}   passive dE = {dEp:+.1e}   {'VIOLATION' if bad else ''}")
print("RESULT 4b: sign(dE_active) = -sign(E_start) whenever |E_start|>1.5, passive dE = 0:",
      viol == 0 and all(abs(r[2]) < 1e-9 for r in rows))
