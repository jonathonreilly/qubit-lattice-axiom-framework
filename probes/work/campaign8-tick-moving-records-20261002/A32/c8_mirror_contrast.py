"""
A32 check C8: do A15's mirror walls survive under Option R?

Supplied toys, one excitation on an open chain of 400 sites; region A = sites 0..199, region B = 200..399;
B's record ticks are out of step with A's.
 (i)  A15's ticked change: brickwork pair gates exp(-i theta SWAP) on even/odd bonds, each region on its own
      phase (B one sub-step ahead); handshake rule: a bond acts only when both ends name it.
 (ii) Option R: the possibilities change smoothly under the hopping H everywhere; weak detectors (one-site
      formation weights, chance c = gamma*tau per own tick) at sites 190, 195 (A) and 205, 210 (B), with
      B's ticks in phase with A's, or offset by tau/2.
Readout: weight that ends in B (unrecorded there, or recorded by a B detector).
"""
import signal
import numpy as np
signal.alarm(55)
L, seam = 400, 200
x = np.arange(L)
k0, x0, s = np.pi / 2, 120.0, 12.0
psi0 = np.exp(1j * k0 * x - (x - x0) ** 2 / (4 * s ** 2)); psi0 /= np.linalg.norm(psi0)

# (i) A15 ticked change with handshake seam
theta = np.pi / 4
def substep(psi, t, offB=1):
    psi = psi.copy()
    for i in range(L - 1):
        par = i % 2                      # bond (i,i+1) lives in layer par
        nameA = (t % 2 == par)
        nameB = ((t + offB) % 2 == par)
        ends = (i < seam, i + 1 < seam)
        if ends == (True, True):
            act = nameA
        elif ends == (False, False):
            act = nameB
        else:
            act = nameA and nameB         # seam bond: handshake
        if act:
            a, b = psi[i], psi[i + 1]
            ph = np.exp(1j * theta)
            psi[i] = ph * (np.cos(theta) * a - 1j * np.sin(theta) * b)
            psi[i + 1] = ph * (np.cos(theta) * b - 1j * np.sin(theta) * a)
    return psi
psi = psi0.copy()
for t in range(400):
    psi = substep(psi, t)
wB = np.sum(np.abs(psi[seam:]) ** 2)
wA = np.sum(np.abs(psi[:seam]) ** 2)
print(f"     initial Gaussian tail already in B: {np.sum(np.abs(psi0[seam:]) ** 2):.3e}")
print(f"(i)  A15 ticked change, handshake seam, theta=pi/4, 400 sub-steps: weight in B = {wB:.3e}, in A = {wA:.12f}")
psi_c = psi0.copy()
for t in range(400):
    psi_c = substep(psi_c, t, offB=0)     # control: B on A's phase (no seam)
print(f"     control, B in step with A: weight in B = {np.sum(np.abs(psi_c[seam:]) ** 2):.6f}")

# (ii) Option R
J = 1.0
H = np.zeros((L, L))
for i in range(L - 1):
    H[i, i + 1] = H[i + 1, i] = -J
E, V = np.linalg.eigh(H)
def evolve(psi, dt):
    return V @ (np.exp(-1j * E * dt) * (V.conj().T @ psi))

def option_R(phase_B, tau, gamma, T):
    c = gamma * tau
    dets = [(190, 0.0), (195, 0.0), (205, phase_B), (210, phase_B)]
    events = []
    for d, ph in dets:
        n = 0
        while ph + n * tau < T - 1e-12:
            events.append((ph + n * tau, d)); n += 1
    events.sort()
    psi = psi0.astype(complex).copy(); tnow = 0.0
    rec = {d: 0.0 for d, _ in dets}
    sq = np.sqrt(1 - c)
    for (t, d) in events:
        if t > tnow:
            psi = evolve(psi, t - tnow); tnow = t
        rec[d] += c * abs(psi[d]) ** 2
        psi[d] *= sq
    psi = evolve(psi, T - tnow)
    inB = np.sum(np.abs(psi[seam:]) ** 2) + rec[205] + rec[210]
    inA = np.sum(np.abs(psi[:seam]) ** 2) + rec[190] + rec[195]
    return inB, inA, rec

T = 60.0
free = evolve(psi0.astype(complex), T)
print(f"(ii) Option R, smooth hopping, no detectors: weight in B after t=60 = {np.sum(np.abs(free[seam:])**2):.6f}")
for tau in [0.2, 0.1, 0.05]:
    g = 0.2
    b0, a0, r0 = option_R(0.0, tau, g, T)
    b1, a1, r1 = option_R(tau / 2, tau, g, T)
    pB0 = r0[205] + r0[210]; pB1 = r1[205] + r1[210]
    print(f"     tau={tau:<5} gamma={g}: in B (B in step) = {b0:.6f}, in B (B offset tau/2) = {b1:.6f}, |diff| = {abs(b0-b1):.2e}; "
          f"recorded by B detectors {pB0:.8f} vs {pB1:.8f} (|diff| {abs(pB0-pB1):.1e}); totals {a0+b0:.12f} / {a1+b1:.12f}")
print("     (the seam is not a wall: what reaches B is set by the smooth change and the detectors' chances; the tick offset")
print("      only re-times the detectors, an O(tau) effect)")
