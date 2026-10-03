"""A27 check 5: how far a distant choice reaches record statistics per tick.
Supplied 1D single-excitation toy.  A's region: sites a-1, a, a+1; the possibility starts at a-1.
A's choice at tick 0: leave it, or move it to a+1 (a local operation inside A's region).  B at site a+L forms a
record with a linear instrument F = c|1><1|_B every tick (no-record branch sqrt(1-F)).
B's readable history = the tick of formation (or none by tick n).  TV between A's two choices.
  strict tick : one layer of partial swaps G(theta) per tick, alternating bond parity (exact cone)
  smooth tick : exp(-iH tau), H = -J sum(|i><i+1| + h.c.), dose x = 2 J tau per tick
Also: Debye asymptotics of the per-tick leak beyond the one-site-per-tick cone, 1D and 3D (L1 cone).
"""
import signal
import numpy as np
from scipy.special import jv
from scipy.linalg import expm

signal.alarm(55)
Nsite, a, L, c, nmax = 61, 20, 8, 0.5, 12
b = a + L

def strict_layers(theta):
    lay = []
    for par in (0, 1):
        M = np.eye(Nsite, dtype=complex)
        for i in range(par, Nsite-1, 2):
            M[i, i] = M[i+1, i+1] = np.cos(theta)
            M[i, i+1] = M[i+1, i] = -1j*np.sin(theta)
        lay.append(M)
    return lay

def history_law(step, phi):
    psi = np.zeros(Nsite, complex); psi[a+1 if phi else a-1] = 1.0
    law = []
    for k in range(1, nmax+1):
        psi = step(k) @ psi
        pk = c*abs(psi[b])**2               # formation at B this tick
        law.append(pk)
        psi[b] *= np.sqrt(1-c)              # no-record branch (unnormalized: survival weight kept)
    law.append(np.vdot(psi, psi).real)      # no record by tick nmax
    return np.array(law)

def tv_by_tick(step):
    l0, l1 = history_law(step, 0), history_law(step, 1)
    out = []
    for n in range(1, nmax+1):
        # law of the history truncated at tick n: formation ticks 1..n, or 'none by n'
        h0 = np.append(l0[:n], 1 - l0[:n].sum()); h1 = np.append(l1[:n], 1 - l1[:n].sum())
        out.append(0.5*np.abs(h0-h1).sum())
    return out

print(f"Nearest content A's choice can place is {L-1} sites from B.  TV of B's record history by tick n:")
lay = strict_layers(1.0)
rows = {"strict theta=1.0": tv_by_tick(lambda k: lay[(k+1) % 2])}
Hm = -(np.eye(Nsite, k=1) + np.eye(Nsite, k=-1))
for x in [0.5, 1.0, 2.0]:
    U = expm(-1j*Hm*(x/2))
    rows[f"smooth x={x}"] = tv_by_tick(lambda k, U=U: U)
print("   n: " + " ".join(f"{n:>8d}" for n in range(1, nmax+1)))
for k, v in rows.items():
    print(f"{k:>17}: " + " ".join(f"{t:8.1e}" for t in v))

print("\nPer-site leak beyond the record cone after n ticks, 1D: |J_{n+1}(n x)|^2 (Debye rate 2*eta(x) per tick)")
for x in [0.5, 0.9, 1.0, 1.2]:
    eta = np.log((1+np.sqrt(1-x*x))/x) - np.sqrt(1-x*x) if x < 1 else 0.0
    vals = [jv(n+1, n*x)**2 for n in [5, 10, 20, 40]]
    print(f"  x={x}: n=5,10,20,40 -> " + " ".join(f"{v:.2e}" for v in vals) + f"   eta={eta:.4f}")

print("\n3D, L1 cone (one grid space per tick): max over |d|_1 = n+1 of prod_a J_{d_a}(n x)^2")
for x in [0.2, 1/3, 0.5]:
    out = []
    for n in [6, 12, 24]:
        best = 0
        m = n+1
        for d1 in range(m+1):
            for d2 in range(m+1-d1):
                d3 = m-d1-d2
                best = max(best, (jv(d1, n*x)*jv(d2, n*x)*jv(d3, n*x))**2)
        out.append(best)
    print(f"  x={x:.3f} (L1 top speed 3x = {3*x:.2f} sites/tick): n=6,12,24 -> " + " ".join(f"{v:.2e}" for v in out))
