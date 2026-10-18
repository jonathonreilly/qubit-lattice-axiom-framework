"""Probe A1 (record apparatus): EFT/naturalness of a weakly coupled mediated
emitter -> chain -> receiver transfer (single excitation, static Hamiltonian).
Toy, not the campaign device. Chain: N=10 sites (even, no E=0 mode), bonds
J(1+eps_i), J=1; emitter e -- chain[0] with lam, chain[-1] -- receiver r with lam.
Region-rung EFT: two-level e<->r with lam_eff = lam^2 |G_1N(0)| and detuning
Delta_eff = (d_e - d_r) + lam^2 (G_11(0) - G_NN(0)).
Measure worst-case (over 200 disorder draws) infidelity 1-|<r|U(t*)|e>|^2 at the
NOMINAL read time t* = pi/(2 lam_eff), and the tolerance x at which it reaches 1e-2.
Perturbation classes:
  bond      : relative bond errors eps_i on the chain (keeps chiral symmetry)
  chainsite : onsite errors on chain sites (breaks chiral symmetry)
  endpoint_diff : independent onsite errors on e and r
  endpoint_common: identical onsite error on e and r (covariant/translation-copied part)
Also: 'bond, adaptive read' = best time in [0.5t*,1.5t*] (latching/clock-free readout).
"""
import numpy as np
rng = np.random.default_rng(7)
N = 10

def H_of(lam, eps=None, mu=None, de=0.0, dr=0.0):
    n = N + 2
    H = np.zeros((n, n))
    for i in range(N - 1):
        b = 1.0 + (0 if eps is None else eps[i])
        H[1 + i, 2 + i] = H[2 + i, 1 + i] = -b
    if mu is not None:
        H[1:N + 1, 1:N + 1] += np.diag(mu)
    H[0, 1] = H[1, 0] = -lam
    H[N, N + 1] = H[N + 1, N] = -lam
    H[0, 0] += de; H[N + 1, N + 1] += dr
    return H

def fid(H, t):
    w, V = np.linalg.eigh(H)
    amp = V[-1, :] @ (np.exp(-1j * w * t) * V[0, :])
    return abs(amp) ** 2

def tstar(lam):
    H = H_of(lam)
    ts = np.linspace(0.5, 1.5, 801) * (np.pi / 2) / (lam ** 2)
    f = [fid(H, t) for t in ts]
    return ts[int(np.argmax(f))], max(f)

def worst(lam, t0, kind, x, draws=200, adaptive=False):
    out = 0.0
    for _ in range(draws):
        if kind == "bond":
            H = H_of(lam, eps=x * rng.uniform(-1, 1, N - 1))
        elif kind == "chainsite":
            H = H_of(lam, mu=x * rng.uniform(-1, 1, N))
        elif kind == "endpoint_diff":
            u = x * rng.uniform(-1, 1, 2); H = H_of(lam, de=u[0], dr=u[1])
        elif kind == "endpoint_common":
            u = x * rng.uniform(-1, 1); H = H_of(lam, de=u, dr=u)
        w, V = np.linalg.eigh(H)
        if adaptive:
            ts = np.linspace(0.5, 1.5, 401) * t0
            amp = (V[-1, :] * V[0, :]) @ np.exp(-1j * np.outer(w, ts))
            f = np.max(np.abs(amp) ** 2)
        else:
            f = abs((V[-1, :] * V[0, :]) @ np.exp(-1j * w * t0)) ** 2
        out = max(out, 1 - f)
    return out

def tolerance(lam, t0, kind, target=1e-2, adaptive=False, base=0.0):
    target = base + target
    lo, hi = 1e-14, 1.0
    for _ in range(40):
        mid = np.sqrt(lo * hi)
        if worst(lam, t0, kind, mid, draws=60, adaptive=adaptive) < target:
            lo = mid
        else:
            hi = mid
    return lo

print("lam   lam_eff   t*        ideal_infid  | tolerance x giving worst infidelity 1e-2")
print("                                     |  bond    bond(adapt) chainsite endpt_diff endpt_common")
rows = []
print("(target = ideal infidelity + 1e-2 excess)")
for lam in [0.04, 0.02, 0.01, 0.005]:
    t0, f0 = tstar(lam)
    b = 1 - f0
    tol = [tolerance(lam, t0, "bond", base=b), tolerance(lam, t0, "bond", adaptive=True, base=b),
           tolerance(lam, t0, "chainsite", base=b), tolerance(lam, t0, "endpoint_diff", base=b),
           tolerance(lam, t0, "endpoint_common", base=b)]
    rows.append((lam, tol))
    print(f"{lam:<5} {lam**2:<9.2e} {t0:<9.3e} {1-f0:<12.2e} | " + " ".join(f"{x:<10.2e}" for x in tol))
lams = np.log([r[0] for r in rows])
names = ["bond", "bond(adaptive)", "chainsite", "endpoint_diff", "endpoint_common"]
for k, nm in enumerate(names):
    slope = np.polyfit(lams, np.log([r[1][k] for r in rows]), 1)[0]
    print(f"scaling exponent of tolerance vs lam [{nm}]: {slope:.2f}")
