"""
A32 check C3: lapse-paced possibilities (H_N = N * H, A26) with three pacings of the record ticks.

Supplied toy: one excitation on a ring (L=12), detectors at sites 3 and 4 with one-site weights
(as in C1). A uniform lapse N stands for "the same local experiment done at a place where the
lapse is N". Every run lasts the same PROPER time T_p = 10 (coordinate time T_p/N).

Schemes for the record ticks at lapse N:
 (a) ticks paced by the lapse: coordinate interval tau0/N, chance per tick c = g0*tau0;
 (b) global coordinate ticks: interval tau0, chance per tick c = g0*N*tau0 (lapse-weighted chance);
 (c) global coordinate ticks: interval tau0, fixed chance per tick c = g0*tau0.
Reference: N = 1 (all three coincide there).
Prediction (report, EXACT rescaling argument): (a) identical to the reference; (b) differs at O(J tau0 |1-N|);
(c) differs at O(|1-N|) however small tau0 is.

C3b: smooth lapse ramp, no instruments: a packet crosses with no measurable reflection, whatever the
record ticks do (the possibilities' change never depends on tick phases).
"""
import signal
import numpy as np
signal.alarm(55)
# --- routines copied verbatim from c1_phase_readability.py ---
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

# --- end copy ---

J, g0, Tp = 1.0, 0.5, 10.0
L = 12
H = ring_H(L, J)
psi0 = np.zeros(L); psi0[0] = 1.0
a, b = 3, 4

print("\nC3a. Same local experiment at lapse N, proper time 10. TV of record law vs the N=1 reference")
print("  tau0     N      (a) lapse-paced ticks   (b) global ticks, chance ~N   (c) global ticks, fixed chance   (b)/(tau0*|1-N|)")
for tau0 in [0.1, 0.05, 0.025, 0.0125]:
    ref = ticked(H, psi0, [a, b], [0.0, 0.0], tau0, g0 * tau0, Tp)
    for N in [0.8, 0.625, 0.5]:   # chosen so that T_p/(N*tau0) is a whole number of ticks
        HN = N * H
        Tc = Tp / N
        Pa = ticked(HN, psi0, [a, b], [0.0, 0.0], tau0 / N, g0 * tau0, Tc)
        Pb = ticked(HN, psi0, [a, b], [0.0, 0.0], tau0, g0 * N * tau0, Tc)
        Pc = ticked(HN, psi0, [a, b], [0.0, 0.0], tau0, g0 * tau0, Tc)
        da, db, dc = tv(ref, Pa), tv(ref, Pb), tv(ref, Pc)
        print(f"  {tau0:<8} {N:<6} {da:<23.2e} {db:<29.3e} {dc:<32.4f} {db/(tau0*(1-N)):.4f}")

print("\nC3b. Packet through a smooth lapse ramp (N: 1 -> 0.5 over sites 300..400), continuous flow H_N, no records")
Lc = 900
N = np.ones(Lc)
x = np.arange(Lc)
N = np.where(x < 300, 1.0, np.where(x > 400, 0.5, 1.0 - 0.5 * (x - 300) / 100.0))
for ramp_name, Nprof in [("smooth ramp (100 sites)", N),
                         ("sharp step at 350", np.where(x < 350, 1.0, 0.5))]:
    Hc = np.zeros((Lc, Lc))
    for i in range(Lc - 1):
        nb = 0.5 * (Nprof[i] + Nprof[i + 1])        # bond lapse (symmetric average)
        Hc[i, i + 1] = Hc[i + 1, i] = -J * nb
    E, V = np.linalg.eigh(Hc)
    k0, x0, s = 1.2, 150.0, 20.0
    psi = np.exp(1j * k0 * x - (x - x0) ** 2 / (4 * s ** 2)); psi /= np.linalg.norm(psi)
    t = 330.0
    psit = V @ (np.exp(-1j * E * t) * (V.T @ psi))
    w = np.abs(psit) ** 2
    print(f"  {ramp_name:<26} reflected weight (x<300) = {w[:300].sum():.3e}   transmitted (x>400) = {w[400:].sum():.6f}   norm = {w.sum():.12f}")
print("  (A15 S10, ticked change with rigid lapse-paced beats: transmission 0.021-0.157 through a gradient; here the")
print("   possibilities never see the record ticks, so the ramp is as transparent as the smooth change makes it)")
