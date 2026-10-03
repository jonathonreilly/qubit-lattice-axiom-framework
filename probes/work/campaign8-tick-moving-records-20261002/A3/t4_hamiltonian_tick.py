"""Check 4: a tick made of continuous star-local change, U = exp(-i H tau), H = NN hopping (d=1).

exp(-iH tau) is not strictly range 1, so a record that may move at most one site per tick
cannot follow the possibilities' odds in general.  We compute the least probability mass
that would have to jump two or more sites (LP), for
  (a) a just-formed record (point mass) -- exact value P_{t+1}(distance >= 2),
  (b) random possibility states,
  (c) a 20-tick history from a point mass,
and the small-tau scaling (expected ~ tau^4/2 for the point mass).
Also (d): R1 (re-formation every tick) vs R3 (guided record) spreading on a long chain
under the Dirac-type brickwork -- diffusive vs ballistic.
"""
import numpy as np
from scipy.linalg import expm
from common import rand_state, ring_allowed, min_long_jump

N = 8
rng = np.random.default_rng(2)
allowed = ring_allowed(N)
H = np.zeros((N, N))
for x in range(N):
    H[x, (x + 1) % N] = H[(x + 1) % N, x] = -1.0

print("(a) record formed at site 0, one tick U = exp(-i H tau):")
for tau in (1.0, 0.5, 0.25, 0.1, 0.05):
    U = expm(-1j * H * tau)
    psi = U[:, 0]
    Pn = np.abs(psi) ** 2
    P = np.zeros(N); P[0] = 1
    far = sum(Pn[y] for y in range(N) if not allowed[0, y])
    lj = min_long_jump(P, Pn, allowed)
    print(f"   tau={tau:5.2f}: P(dist>=2) = {far:.3e}; LP least long-jump mass = {lj:.3e}; "
          f"tau^4/2 = {tau**4/2:.3e}")

print("(b) random possibility states, tau = 1 and 0.25:")
for tau in (1.0, 0.25):
    U = expm(-1j * H * tau)
    infeas, worst = 0, 0.0
    for k in range(300):
        psi = rand_state(N, rng)
        P = np.abs(psi) ** 2
        Pn = np.abs(U @ psi) ** 2
        lj = min_long_jump(P, Pn, allowed)
        infeas += lj > 1e-9
        worst = max(worst, lj)
    print(f"   tau={tau}: states with no NN-only coupling: {infeas}/300; largest least long-jump mass = {worst:.3e}")

print("(c) 20 ticks from a point mass, tau = 1: least long-jump mass per tick")
U = expm(-1j * H * 1.0)
psi = np.zeros(N, complex); psi[0] = 1
vals = []
for t in range(20):
    P = np.abs(psi) ** 2
    psin = U @ psi
    Pn = np.abs(psin) ** 2
    vals.append(min_long_jump(P, Pn, allowed))
    psi = psin
print("   " + " ".join(f"{v:.3f}" for v in vals))

print("(d) spreading of the record on an open chain of 201 sites, Dirac-type brickwork theta=pi/4:")
L = 201
c, s = np.cos(np.pi / 4), np.sin(np.pi / 4)
psi = np.zeros(L, complex); psi[L // 2] = 1
Pcl = np.zeros(L); Pcl[L // 2] = 1
xs = np.arange(L) - L // 2
out = []
for t in range(1, 81):
    start = 0 if t % 2 == 1 else 1
    new = psi.copy(); newcl = Pcl.copy()
    for a in range(start, L - 1, 2):
        b = a + 1
        new[a] = c * psi[a] - 1j * s * psi[b]
        new[b] = -1j * s * psi[a] + c * psi[b]
        newcl[a] = c * c * Pcl[a] + s * s * Pcl[b]
        newcl[b] = s * s * Pcl[a] + c * c * Pcl[b]
    psi, Pcl = new, newcl
    if t in (10, 20, 40, 80):
        P = np.abs(psi) ** 2
        out.append((t, float((P * xs ** 2).sum()), float((Pcl * xs ** 2).sum())))
for t, v3, v1 in out:
    print(f"   tick {t:3d}: variance R3 (guided, = Born odds) = {v3:8.2f};   R1 (re-formed each tick) = {v1:6.2f}")
