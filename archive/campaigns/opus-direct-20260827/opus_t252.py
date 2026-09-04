"""
T252 - are the framework's particles bosons or fermions?

R164: the framework contains a genuine localised topological particle.
R165: it is Planck-scale everywhere, so it cannot be ordinary matter.
R163's remaining question: does it carry FERMIONIC statistics?

Soliton statistics is not free.  A topological defect in a bosonic field is a
BOSON unless the action carries a topological term contributing a PHASE -- a
Wess-Zumino or Hopf term -- which is what makes a Skyrmion a fermion.  Such a
term is an IMAGINARY contribution to the Euclidean action.

The framework's record measure is
        mu = prod over edges of Tr(P_x P_y)
and Tr(P P') = tr(U^dag U) with U = P_x^dag P_y is a squared norm.  So mu is
manifestly REAL and NON-NEGATIVE, its action S = -log mu is real, and there is
no phase anywhere for a topological term to live in.

Checked here: positivity and reality of the edge weight, at every rank, and that
the total measure carries no imaginary part.
"""
import numpy as np
rng = np.random.default_rng(271)

def frame(n,k):
    A = rng.normal(size=(n,k)) + 1j*rng.normal(size=(n,k))
    Q,_ = np.linalg.qr(A); return Q
P = lambda Q: Q @ Q.conj().T

print("=== 1. is the edge weight real and non-negative, at every rank? ===")
for n,k in ((4,1),(4,2),(8,2),(12,3)):
    mn, mx, mi = np.inf, -np.inf, 0.0
    for _ in range(20000):
        Qa, Qb = frame(n,k), frame(n,k)
        z = np.trace(P(Qa) @ P(Qb))
        mi = max(mi, abs(z.imag)); mn = min(mn, z.real); mx = max(mx, z.real)
    print(f"   M{n}(C) rank {k}: Tr(PP') in [{mn:.6f}, {mx:.6f}]   "
          f"max |imaginary part| = {mi:.2e}")

print("\n=== 2. so the measure on a whole lattice is real and non-negative ===")
L, n, k = 6, 4, 1
Q = np.stack([np.stack([np.stack([frame(n,k) for _ in range(L)])
                        for _ in range(L)]) for _ in range(L)])
tot_im, tot_min = 0.0, np.inf
logmu = 0.0
for ax in range(3):
    Qb = np.roll(Q, -1, ax)
    for i in range(L):
        for j in range(L):
            for m in range(L):
                z = np.trace(P(Q[i,j,m]) @ P(Qb[i,j,m]))
                tot_im = max(tot_im, abs(z.imag)); tot_min = min(tot_min, z.real)
                logmu += np.log(max(z.real, 1e-300))
print(f"   over all {3*L**3} edges: max |Im| = {tot_im:.2e},  "
      f"min Re = {tot_min:.6f},  log mu = {logmu:.3f} (real)")

print("""
=== the argument ===
  The record measure is a product of squared norms, hence real and non-negative
  at every rank.  Its Euclidean action S = -log mu is therefore REAL, and a
  topological term of Wess-Zumino / Hopf type -- the only known mechanism that
  makes a soliton in a bosonic field carry fermionic statistics -- is an
  IMAGINARY contribution to that action.  There is nowhere for it to live.

  => the framework's topological particles are BOSONS.

  This closes R163's fermion route structurally, and more strongly than R165's
  mass bound did: not "they exist but are too heavy" but "they are not fermions".""")
