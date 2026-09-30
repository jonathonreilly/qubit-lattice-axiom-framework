#!/usr/bin/env python3
"""Kill-check controls for attack T16 test 4 (active branch).  Independent re-implementation of the
attack's 8-qubit chain.  Questions:
 K1a  Is 'energy runs toward equilibrium from every start' specific to Born outcomes, or does an
      outcome-blind lock (fair-coin outcomes, no state dependence) give the same dE?
 K1b  Does the sign rule survive a different lock basis (x instead of z)?
 K1c  Is the final energy a single equilibrium value, or a contraction E' = c E + d (memory kept)?
 K1d  Does the wave's entropy go toward equilibrium (up) or away (down) in the active branch?
      (final half-chain S vs start S over the nine window starts and Haar)
 K1e  Scaling with number of births (2,4,6) -- 6 of 8 sites locked is 75% of the system.
"""
import numpy as np

rng = np.random.default_rng(2016)
N = 8
I2 = np.eye(2)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]])
sz = np.diag([1.0, -1.0]).astype(complex)


def site_op(d):
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
cache = {}


def evolve(psi, locked, t):
    key = frozenset(locked)
    if key not in cache:
        cache[key] = np.linalg.eigh(H_of(set(locked)))
    w, V = cache[key]
    return V @ (np.exp(-1j * w * t) * (V.conj().T @ psi))


def S_half(psi):
    s = np.linalg.svd(psi.reshape(16, 16), compute_uv=False)
    p = s ** 2
    p = p[p > 1e-14]
    return float(-(p * np.log(p)).sum())


def energy(psi):
    return float(np.real(psi.conj() @ H0 @ psi))


# basis-change unitary for x-locks: Hadamard on every site maps x eigenbasis to z
Hd = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
Hall = np.array([[1.0 + 0j]])
for _ in range(N):
    Hall = np.kron(Hall, Hd)


def lock_run(psi0, nb, tau, basis="z", outcome="born"):
    psi = psi0.copy()
    locked, free = [], list(range(N))
    for _ in range(nb):
        psi = evolve(psi, set(locked), tau)
        x = free.pop(rng.integers(len(free)))
        phi = Hall @ psi if basis == "x" else psi
        idx = np.arange(2 ** N)
        bit = (idx >> (N - 1 - x)) & 1
        p1 = float(np.sum(np.abs(phi[bit == 1]) ** 2))
        p1 = min(max(p1, 0.0), 1.0)
        if outcome == "born":
            val = 1 if rng.random() < p1 else 0
        else:  # outcome-blind fair coin, retry if the branch has zero amplitude
            val = int(rng.random() < 0.5)
            if (val == 1 and p1 < 1e-12) or (val == 0 and 1 - p1 < 1e-12):
                val = 1 - val
        phi = np.where(bit == val, phi, 0)
        phi = phi / np.linalg.norm(phi)
        psi = Hall @ phi if basis == "x" else phi
        locked.append(x)
    return psi


def window_start(Et, ncomb=1):
    sel = np.where(np.abs(w0 - Et) < 0.8)[0]
    if len(sel) < 3:
        return None
    c = rng.normal(size=len(sel)) + 1j * rng.normal(size=len(sel))
    c /= np.linalg.norm(c)
    return V0[:, sel] @ c


tau = 0.3
Es_list = (-10, -7, -4, -2, 0, 2, 4, 6, 8)
starts = []
for Et in Es_list:
    for _ in range(3):
        p = window_start(Et)
        if p is not None:
            starts.append(p)
print("number of window starts:", len(starts))
Es = np.array([energy(p) for p in starts])
Ss = np.array([S_half(p) for p in starts])


def summarize(label, nb, basis, outcome, ntraj=25):
    Ef = np.zeros(len(starts))
    Sf = np.zeros(len(starts))
    for i, p in enumerate(starts):
        e = s = 0.0
        for _ in range(ntraj):
            q = lock_run(p, nb, tau, basis, outcome)
            e += energy(q)
            s += S_half(q)
        Ef[i] = e / ntraj
        Sf[i] = s / ntraj
    dE = Ef - Es
    big = np.abs(Es) > 1.5
    sign_ok = np.all(np.sign(dE[big]) == -np.sign(Es[big]))
    c, d = np.polyfit(Es, Ef, 1)
    dSmean = np.mean(Sf - Ss)
    print(f"{label:38s}: sign(dE)=-sign(E) for |E|>1.5: {sign_ok!s:5s}; "
          f"E_final = {c:+.2f} E_start {d:+.2f}; mean dS_half = {dSmean:+.2f}; "
          f"final E range [{Ef.min():+.2f},{Ef.max():+.2f}]; final S mean {Sf.mean():.2f}")
    return sign_ok, c, d, dSmean


print("\n-- K1a/K1c/K1d: 6 births --")
r_born = summarize("z-lock, Born outcomes, nb=6", 6, "z", "born")
r_blind = summarize("z-lock, outcome-blind coin, nb=6", 6, "z", "blind")
print("\n-- K1b: lock basis --")
r_x = summarize("x-lock, Born outcomes, nb=6", 6, "x", "born")
print("\n-- K1e: number of births --")
r2 = summarize("z-lock, Born, nb=2", 2, "z", "born")
r4 = summarize("z-lock, Born, nb=4", 4, "z", "born")

print("\nStart entropies range [%.2f, %.2f], mean %.2f" % (Ss.min(), Ss.max(), Ss.mean()))
print("\nREADINGS:")
print(" K1a outcome-blind lock reproduces the sign rule:", r_blind[0])
print(" K1b x-lock sign rule:", r_x[0])
print(" K1c contraction slope/intercept (born, nb=6): c=%.2f d=%.2f  (single equilibrium would be c~0)" % (r_born[1], r_born[2]))
print(" K1d mean change of half-chain entropy, born nb=6: %+.2f  (thermodynamic arrow would be > 0)" % r_born[3])
