# A39 c1: loophole (a). A product vacuum |0>^N that is stationary but NOT the
# ground state (pi-flux hopping, Dirac-like one-flip bands at E=0 with negative
# states below) versus the same vacuum made the ground state by a uniform field.
# Supplied toy: 4x3 torus, 12 qubits, flip = |1>. Perturbation: delta*sum X
# (a generic off-axis field, e.g. an off-axis record's field; breaks flip number).
# Measures: survival |<Omega|psi(t)>|^2, flip density, and the chance that the
# (supplied, z-privileging) quiet star weight F_x = 1 - prod_{y in star}|0><0|_y fires.
import signal, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply
signal.alarm(55)
Lx, Ly, t = 4, 3, 1.0
N = Lx*Ly; D = 1 << N
idx = lambda x, y: (x % Lx) + Lx*(y % Ly)
bonds = []
for y in range(Ly):
    for x in range(Lx):
        bonds.append((idx(x, y), idx(x+1, y), 1.0))            # x-bonds
        bonds.append((idx(x, y), idx(x, y+1), (-1.0)**x))      # y-bonds: pi flux
# plaquette flux check
eta = {}
for (i, j, e) in bonds:
    eta[(i, j)] = e; eta[(j, i)] = e
fl = []
for y in range(Ly):
    for x in range(Lx):
        a, b, c, d = idx(x, y), idx(x+1, y), idx(x+1, y+1), idx(x, y+1)
        fl.append(eta[(a, b)]*eta[(b, c)]*eta[(c, d)]*eta[(d, a)])
assert all(abs(f+1) < 1e-12 for f in fl), fl
print("pi flux through all", len(fl), "plaquettes: OK")
states = np.arange(D, dtype=np.int64)
nflip = np.array([bin(s).count("1") for s in range(D)], dtype=float)

def hop(eta_on):
    rows, cols, vals = [], [], []
    for (i, j, eta) in bonds:
        e = eta if eta_on else 1.0
        bi, bj = (states >> i) & 1, (states >> j) & 1
        m = bi != bj
        s = states[m]; tgt = s ^ ((1 << i) | (1 << j))
        rows.append(tgt); cols.append(s); vals.append(np.full(s.size, -t*e))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(D, D))

def xfield():
    rows, cols = [], []
    for i in range(N):
        rows.append(states ^ (1 << i)); cols.append(states)
    r = np.concatenate(rows); c = np.concatenate(cols)
    return sp.csr_matrix((np.ones(r.size), (r, c)), shape=(D, D))

Hpi, H0, X = hop(True), hop(False), xfield()
Nop = sp.diags(nflip)
# one-flip bands
one = [1 << i for i in range(N)]
T = Hpi[one][:, one].toarray(); T0 = H0[one][:, one].toarray()
e1 = np.linalg.eigvalsh(T); e10 = np.linalg.eigvalsh(T0)
print("one-flip energies, pi flux:", np.round(e1, 4))
print("one-flip energies, zero flux:", np.round(e10, 4))
W = np.max(np.abs(e1))
print(f"pi-flux one-flip band: min {e1.min():.4f} max {e1.max():.4f}; #negative = {(e1 < -1e-12).sum()} of {N}")
# star weight: F_x fires unless x and its 4 neighbours are all |0>
def star_mask(x, y):
    m = 0
    for (a, b) in [(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        m |= 1 << idx(a, b)
    return m
smask = [star_mask(x, y) for y in range(Ly) for x in range(Lx)]
Fdiag = np.mean([((states & m) != 0).astype(float) for m in smask], axis=0)


v0 = np.zeros(D, complex); v0[0] = 1.0
# (1) Resonant manifold: unperturbed states within |E - E_Omega| < w, by flip-number block.
def count_res(Hd, w):
    tot = 0
    for n in range(1, N+1):
        sel = np.where(nflip == n)[0]
        ev = np.linalg.eigvalsh(Hd[sel][:, sel].toarray())
        tot += int((np.abs(ev) < w).sum())
    return tot
HB0 = (Hpi + (W+0.5)*Nop).tocsr()
for w in (0.05, 0.2):
    print(f"states with |E - E_Omega| < {w}: pi-flux (Omega not ground) {count_res(Hpi.tocsr(), w)};"
          f" with field (Omega ground) {count_res(HB0, w)}  [of {D-1}]")
# (2) Slow switch-on/off cycle of an off-axis field: delta(t) = dmax*sin^2(pi t / Ttot).
def cycle(H0m, dmax, Ttot=400.0, dt=0.5):
    v = v0.copy(); steps = int(Ttot/dt)
    for k in range(steps):
        d = dmax*np.sin(np.pi*(k+0.5)*dt/Ttot)**2
        v = expm_multiply(-1j*dt*(H0m + d*X), v)
    p = np.abs(v)**2
    return p[0], p @ nflip / N, p @ Fdiag
for dmax in (0.03, 0.10):
    for name, H0m in (("pi-flux, Omega not ground", Hpi.tocsr()), ("pi-flux + field, Omega ground", HB0)):
        s, nd, fx = cycle(H0m, dmax)
        print(f"cycle dmax={dmax}: {name:32s} back-to-vacuum prob {s:.4f}; flip density {nd:.2e}; star-weight chance {fx:.2e}")
