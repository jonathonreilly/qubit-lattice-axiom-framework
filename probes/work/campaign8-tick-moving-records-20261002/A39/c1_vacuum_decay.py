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
cases = {
  "A0 pi-flux hopping, no perturbation (stationary, not ground)": Hpi,
  "A  pi-flux hopping + 0.10 X (not ground)": Hpi + 0.10*X,
  "A' pi-flux hopping + 0.03 X (not ground)": Hpi + 0.03*X,
  f"B  pi-flux + h={W+0.5:.3f} n + 0.10 X (ground, gapped)": Hpi + (W+0.5)*Nop + 0.10*X,
  f"B' pi-flux + h={W+0.5:.3f} n + 0.03 X (ground, gapped)": Hpi + (W+0.5)*Nop + 0.03*X,
}
# check Omega's place in the unperturbed many-body spectrum of pi-flux hopping (flip-number blocks)
for n in range(0, N+1):
    sel = np.where(nflip == n)[0]
    if sel.size > 800:  # only report small blocks exactly
        continue
    ev = np.linalg.eigvalsh(Hpi[sel][:, sel].toarray())
    if n <= 2:
        print(f"  pi-flux block n={n}: lowest {ev.min():.4f}, #states with E<0: {(ev < -1e-9).sum()} of {sel.size}")
tgrid_stop, num = 80.0, 161
for name, H in cases.items():
    H = H.tocsr()
    psi = expm_multiply(-1j*H, v0, start=0.0, stop=tgrid_stop, num=num, endpoint=True)
    surv = np.abs(psi[:, 0])**2
    p = np.abs(psi)**2
    nd = p @ nflip / N
    Fx = p @ Fdiag
    late = slice(num//2, num)
    print(f"{name}\n   survival: min {surv.min():.4f}, mean over t in [40,80] {surv[late].mean():.4f}; "
          f"flip density mean [40,80] {nd[late].mean():.4f} (max {nd.max():.4f}); "
          f"star-weight chance mean [40,80] {Fx[late].mean():.4f} (max {Fx.max():.4f})")
