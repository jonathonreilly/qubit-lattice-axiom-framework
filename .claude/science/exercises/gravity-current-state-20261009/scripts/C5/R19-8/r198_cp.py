#!/usr/bin/env python3
"""R19-8 [C]: CP of an E2-type instrument (toy, illustrative; the structural proof is Kraus U_r A_r, vR18-7:11).
Qubit, 6 steps. Each step: weak sigma_z measurement whose strength depends on the classical metric variable h (a = 2 adaptive meter),
record r = +-1; classical readout = DAMPED filter (telegraph: v <- v + dt (r - gam v) - dt k2 h ; h <- h + dt v), a deterministic
'sink' variable E_s <- E_s + dt gam v^2 (energy taken by the friction); feedback unitary exp(-i th sigma_x) with th a nonlinear
function of (h, E_s). Compare: (i) noiseless sink (h, E_s functionals of records), (ii) a classical noisy sink (h kicked by an
independent +-xi coin each step): still CP (mixture), but h is no longer a functional of records (AX:82-83), (iii) mean-field
feedback (th depends on the conditional state): not linear in rho.
Subtraction: none.  Run: OMP_NUM_THREADS=2 python3 r198_cp.py
"""
import numpy as np, itertools
sx = np.array([[0, 1], [1, 0]], complex); sz = np.diag([1.0, -1.0]).astype(complex); I2 = np.eye(2)
def Ux(th): return np.cos(th)*I2 - 1j*np.sin(th)*sx
gam, dt, k2 = 0.7, 0.5, 0.3
def run(rho, mode='noiseless', nsteps=6):
    br = [(rho, 0.0, 0.0, 0.0, ())]          # state, h, v, E_s, record history
    for n in range(nsteps):
        nb = []
        for (sig, h, v, Es, hist) in br:
            eps = 0.4*np.tanh(1 + h**2)
            kicks = (+0.2, -0.2) if mode == 'noisy' else (0.0,)
            for r in (+1, -1):
                A = np.sqrt(np.diag([(1 + r*eps)/2, (1 - r*eps)/2])).astype(complex)
                s2 = A @ sig @ A.conj().T
                for xi in kicks:
                    w_ = 1.0/len(kicks)
                    v2 = v + dt*(r - gam*v) - dt*k2*h + xi
                    h2 = h + dt*v2
                    Es2 = Es + dt*gam*v2**2
                    if mode == 'meanfield':
                        pr = np.real(np.trace(s2)); mz = np.real(np.trace(sz @ s2))/pr if pr > 0 else 0
                        th = 0.9*np.sin(h2) + 0.5*Es2 + 1.3*mz
                    else:
                        th = 0.9*np.sin(h2) + 0.5*Es2 + 0.3*h2**2
                    U = Ux(th); nb.append((w_*(U @ s2 @ U.conj().T), h2, v2, Es2, hist + (r,)))
        br = nb
    return br
def chan(rho, mode): return sum(b[0] for b in run(rho, mode))
def choi(mode):
    C = np.zeros((4, 4), complex)
    for i in range(2):
        for j in range(2):
            E = np.zeros((2, 2), complex); E[i, j] = 1; C += np.kron(E, chan(E, mode))
    return C
r1 = np.diag([1.0, 0.0]).astype(complex); r2 = 0.5*np.array([[1, 1], [1, 1]], complex)
for mode in ('noiseless', 'noisy', 'meanfield'):
    C = choi(mode); ev = np.linalg.eigvalsh((C + C.conj().T)/2)
    lin = np.abs(chan(0.5*r1 + 0.5*r2, mode) - 0.5*chan(r1, mode) - 0.5*chan(r2, mode)).max()
    tp = abs(np.trace(chan(r1, mode)) - 1)
    # is h a function of the record history alone?
    br = run(r1, mode); d = {}
    for b in br: d.setdefault(b[4], set()).add(round(b[1], 12))
    func = all(len(s) == 1 for s in d.values())
    print("[C] %-9s: Choi eigenvalues %s ; min %.2e ; TP err %.1e ; linearity defect %.1e ; h a function of records alone: %s"
          % (mode, np.round(ev, 5), ev.min(), tp, lin, func))
print("    => friction + deterministic sink inside the classical readout keeps a linear CP instrument with h = functional of records;")
print("       sink noise is not required by CP; it is excluded by record-only readout (AX:82-83), not by positivity.")
