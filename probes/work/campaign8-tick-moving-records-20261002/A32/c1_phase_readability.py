"""
A32 check C1: how readable are record-tick phases (global vs neighbourhood) under Option R?

Supplied toy (not framework content):
- possibilities: one excitation hopping on a ring of L sites, H = -J sum (|x><x+1| + h.c.),
  changing smoothly at all times (Option R's between-tick change; no compression is needed
  before the first record because the toy ends at the first record);
- record events: detector sites d apply, at their own ticks, a linear local formation instrument
  with one-site weight F = c|1><1|_d (Kraus sqrt(c)|d><d| = "record 1 at d", and the no-record
  update sqrt(1-c) on the d-amplitude);  c = gamma*tau (chance per tick scaled with the tick);
- readable outcome: which detector holds the record by time T (or none).

Compared:
- global tick (all detectors tick together), neighbourhood ticks (different phases),
  and the continuous-time limit (formation at rate gamma |psi_d|^2, exact non-Hermitian integral).
Expected (EXACT lemma in the report): differences are O(tau) and vanish as tau -> 0.
"""
import signal, sys
import numpy as np
signal.alarm(55)
np.set_printoptions(precision=6, suppress=False)

def ring_H(L, J=1.0):
    H = np.zeros((L, L))
    for x in range(L):
        H[x, (x + 1) % L] = -J
        H[(x + 1) % L, x] = -J
    return H

def ticked(H, psi0, dets, phases, tau, c, T):
    """dets: list of sites; phases: list of offsets in [0,tau). Ticks at phase + n*tau < T."""
    E, V = np.linalg.eigh(H)
    events = []
    for d, ph in zip(dets, phases):
        n = 0
        while True:
            t = ph + n * tau
            if t >= T - 1e-12:
                break
            events.append((t, d))
            n += 1
    events.sort()
    psi = psi0.astype(complex).copy()
    t_now = 0.0
    P = {d: 0.0 for d in dets}
    sq = np.sqrt(1.0 - c)
    for (t, d) in events:
        dt = t - t_now
        if dt > 0:
            psi = V @ (np.exp(-1j * E * dt) * (V.conj().T @ psi))
            t_now = t
        p = c * abs(psi[d]) ** 2
        P[d] += p
        psi[d] *= sq
    dt = T - t_now
    psi = V @ (np.exp(-1j * E * dt) * (V.conj().T @ psi))
    P['none'] = float(np.vdot(psi, psi).real)
    return P

def continuous(H, psi0, dets, gamma, T):
    L = H.shape[0]
    Heff = H.astype(complex).copy()
    for d in dets:
        Heff[d, d] += -0.5j * gamma
    lam, R = np.linalg.eig(Heff)
    Rinv = np.linalg.inv(R)
    alpha = Rinv @ psi0.astype(complex)
    P = {}
    for d in dets:
        u = alpha * R[d, :]            # psi_d(t) = sum_j u_j e^{-i lam_j t}
        mu = lam[:, None] - lam.conj()[None, :]
        with np.errstate(divide='ignore', invalid='ignore'):
            I = np.where(np.abs(mu) > 1e-14, (1 - np.exp(-1j * mu * T)) / (1j * mu), T)
        val = gamma * np.sum(np.outer(u, u.conj()) * I)
        P[d] = float(val.real)
    psiT = R @ (np.exp(-1j * lam * T) * alpha)
    P['none'] = float(np.vdot(psiT, psiT).real)
    return P

def tv(P, Q):
    keys = P.keys()
    return 0.5 * sum(abs(P[k] - Q[k]) for k in keys)

J, gamma, T = 1.0, 0.5, 10.0
L = 12
H = ring_H(L, J)
psi0 = np.zeros(L); psi0[0] = 1.0

print("C1a. Two detectors, ring L=12, start at site 0, gamma=0.5, T=10, c = gamma*tau")
for (a, b, label) in [(3, 4, "adjacent detectors a=3, b=4"), (3, 9, "far detectors a=3, b=9")]:
    print(f"\n  {label}")
    Pc = continuous(H, psi0, [a, b], gamma, T)
    print(f"    continuous-time limit: P(a)={Pc[a]:.8f} P(b)={Pc[b]:.8f} P(none)={Pc['none']:.8f} sum={Pc[a]+Pc[b]+Pc['none']:.12f}")
    print("    tau      c        TV(global vs b shifted tau/2)  ratio/tau   TV(global vs continuous)  ratio/tau   bound(shift)")
    for tau in [0.4, 0.2, 0.1, 0.05, 0.025, 0.0125]:
        c = gamma * tau
        Pg = ticked(H, psi0, [a, b], [0.0, 0.0], tau, c, T)
        Pn = ticked(H, psi0, [a, b], [0.0, tau / 2], tau, c, T)
        d1 = tv(Pg, Pn); d2 = tv(Pg, Pc)
        # exact lemma bound for re-timing every b instrument by delta = tau/2 (ring hopping: ||[H,|b><b|]|| = sqrt(2) J)
        delta = tau / 2; nb = int(round(T / tau))
        cH1 = np.sqrt(2 * c) * J; k1 = np.sqrt(c)
        cH0 = (1 - np.sqrt(1 - c)) * np.sqrt(2) * J; k0 = 1.0
        per = 2 * delta * (cH1 * k1 + cH0 * k0) + delta ** 2 * (cH1 ** 2 + cH0 ** 2)
        bound = 0.5 * nb * per
        print(f"    {tau:<8.4g} {c:<8.4g} {d1:<30.3e} {d1/tau:<11.4e} {d2:<25.3e} {d2/tau:<11.4e} {bound:.3e}")

print("\nC1b. Regime M (dose per tick 2*J*tau = 1, i.e. tau = 0.5; chance per tick O(1)), adjacent detectors")
a, b = 3, 4
for c in [0.25, 0.5, 1.0]:
    tau = 0.5
    Pg = ticked(H, psi0, [a, b], [0.0, 0.0], tau, c, T)
    for frac in [0.25, 0.5, 0.75]:
        Pn = ticked(H, psi0, [a, b], [0.0, frac * tau], tau, c, T)
        print(f"    c={c:<5} b phase={frac:<5}*tau  TV(global vs shifted) = {tv(Pg, Pn):.4f}   P_global={Pg[a]:.4f},{Pg[b]:.4f},{Pg['none']:.4f}")

print("\nC1c. Six detectors (sites 5..10) on a ring L=16; global vs ramp vs i.i.d. random phases; c = gamma*tau")
L2 = 16
H2 = ring_H(L2, J)
psi2 = np.zeros(L2); psi2[0] = 1.0
dets = list(range(5, 11))
rng = np.random.default_rng(32)
u = rng.random(len(dets))
Pc2 = continuous(H2, psi2, dets, gamma, T)
print("    tau      TV(global,ramp)  TV(global,random)  TV(global,cont)   [each /tau]")
for tau in [0.4, 0.2, 0.1, 0.05, 0.025]:
    c = gamma * tau
    Pg = ticked(H2, psi2, dets, [0.0] * 6, tau, c, T)
    Pr = ticked(H2, psi2, dets, [k * tau / 6 for k in range(6)], tau, c, T)
    Pu = ticked(H2, psi2, dets, list(u * tau), tau, c, T)
    a1, a2, a3 = tv(Pg, Pr), tv(Pg, Pu), tv(Pg, Pc2)
    print(f"    {tau:<8.4g} {a1:<16.3e} {a2:<18.3e} {a3:<17.3e} [{a1/tau:.3e}, {a2/tau:.3e}, {a3/tau:.3e}]")
print("    probabilities sum check (global, tau=0.025):", sum(ticked(H2, psi2, dets, [0.0]*6, 0.025, gamma*0.025, T).values()))

print("\nC1d. Stationary start (ring L=12 plane wave k=0, an eigenstate): a GLOBAL shift of every tick is a time")
print("     translation (exactly unreadable); a RELATIVE shift between two detectors is readable at O(tau).")
psis = np.ones(L) / np.sqrt(L)
for (a, b, label) in [(3, 4, "adjacent a=3,b=4"), (3, 9, "far a=3,b=9")]:
    print(f"  {label}")
    print("    tau      TV(global, global shifted tau/2)   TV(global, b alone shifted tau/2)  [/tau]")
    for tau in [0.4, 0.2, 0.1, 0.05, 0.025]:
        c = gamma * tau
        Pg = ticked(H, psis, [a, b], [0.0, 0.0], tau, c, T)
        Pgs = ticked(H, psis, [a, b], [tau / 2, tau / 2], tau, c, T)
        Pn = ticked(H, psis, [a, b], [0.0, tau / 2], tau, c, T)
        print(f"    {tau:<8.4g} {tv(Pg, Pgs):<34.3e} {tv(Pg, Pn):<34.3e} [{tv(Pg, Pn)/tau:.3e}]")
