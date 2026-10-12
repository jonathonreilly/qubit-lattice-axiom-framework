"""R2-3 lemma checks (numerical sanity only; the proofs are in the report).

L-B  (closedness of a jump-type source): on a (1+2)D lattice, a 1-form J that
     lives on one layer of temporal edges (t0 -> t0+1) plus spatial edges on the
     slices t0 and t0+1, with compact spatial support, and is closed (dJ = 0 on
     every plaquette), must vanish.  Contrast: allowing two temporal layers
     (a delta'-type source, energy injected and withdrawn) gives closed forms.
L-T  (decoherence/heat trade-off): for a normalized real envelope f on R^3
     (Kraus family f(x-X), int f^2 = 1), 1 - C(d) <= (d^2/2) int |d.grad f|^2,
     and heating per flash = (hbar^2/2m) int |grad f|^2.  Checked for Gaussian,
     flat-top (tanh edge) and a ring-shaped envelope, in 1D and 3D (separable
     check via the 1D factor for product envelopes).
L-H  (state independence of mean heating): GRW Lindblad dissipator on a 1D
     grid; d<H>/dt computed for two different states equals the c-number.
"""
import numpy as np

np.set_printoptions(linewidth=140)

# ---------------------------------------------------------------- L-B
def closedness_nullity(Lx, Ly, layers, box):
    """Count closed 1-forms supported on given temporal layers / slices.
    Lattice: times 0..T-1, sites (x,y) in an Lx*Ly open grid.
    Variables: temporal edges (t->t+1) at sites in box for t in layers;
               spatial edges at slices in slices_allowed within box.
    Constraint: dJ = 0 on all plaquettes (t-x, t-y, x-y) of the full lattice.
    """
    T = max(layers) + 3
    slices_allowed = sorted(set([t for t in layers] + [t + 1 for t in layers]))
    var = {}
    def add(key):
        if key not in var:
            var[key] = len(var)
    inbox = lambda x, y: box[0] <= x <= box[1] and box[0] <= y <= box[1]
    for t in layers:
        for x in range(Lx):
            for y in range(Ly):
                if inbox(x, y):
                    add(('t', t, x, y))
    for t in slices_allowed:
        for x in range(Lx - 1):
            for y in range(Ly):
                if inbox(x, y) and inbox(x + 1, y):
                    add(('x', t, x, y))
        for x in range(Lx):
            for y in range(Ly - 1):
                if inbox(x, y) and inbox(x, y + 1):
                    add(('y', t, x, y))
    rows = []
    def J(key):
        return var.get(key)
    # t-x plaquettes: J_t(t,x+1,y) - J_t(t,x,y) - J_x(t+1,x,y) + J_x(t,x,y)
    for t in range(T - 1):
        for x in range(Lx - 1):
            for y in range(Ly):
                r = {}
                for k, s in ((('t', t, x + 1, y), 1), (('t', t, x, y), -1),
                             (('x', t + 1, x, y), -1), (('x', t, x, y), 1)):
                    if J(k) is not None:
                        r[J(k)] = r.get(J(k), 0) + s
                if r:
                    rows.append(r)
        for x in range(Lx):
            for y in range(Ly - 1):
                r = {}
                for k, s in ((('t', t, x, y + 1), 1), (('t', t, x, y), -1),
                             (('y', t + 1, x, y), -1), (('y', t, x, y), 1)):
                    if J(k) is not None:
                        r[J(k)] = r.get(J(k), 0) + s
                if r:
                    rows.append(r)
    for t in range(T):
        for x in range(Lx - 1):
            for y in range(Ly - 1):
                r = {}
                for k, s in ((('x', t, x, y), 1), (('y', t, x + 1, y), 1),
                             (('x', t, x, y + 1), -1), (('y', t, x, y), -1)):
                    if J(k) is not None:
                        r[J(k)] = r.get(J(k), 0) + s
                if r:
                    rows.append(r)
    A = np.zeros((len(rows), len(var)))
    for i, r in enumerate(rows):
        for j, v in r.items():
            A[i, j] = v
    rank = np.linalg.matrix_rank(A)
    return len(var), rank, len(var) - rank

print("L-B: closed 1-forms with compact spatial support (box 2..6 in an 9x9 grid)")
for layers in ([2], [2, 3], [2, 3, 4]):
    nv, rk, nul = closedness_nullity(9, 9, layers, (2, 6))
    print(f"  temporal layers {layers}: variables {nv}, rank {rk}, closed (nullity) {nul}")
print("  expected: one layer (jump type) -> nullity 0; k layers -> nullity = (k-1) x #interior-free scalars Q")

# ---------------------------------------------------------------- L-T
def envelope_1d(kind, x, rc):
    if kind == 'gauss':
        return np.exp(-x**2 / (2 * rc**2))
    if kind == 'flattop':
        R, w = 2.0 * rc, 0.3 * rc
        return 0.5 * (1 - np.tanh((np.abs(x) - R) / w))
    if kind == 'ring':
        return np.exp(-(np.abs(x) - 1.5 * rc)**2 / (2 * (0.4 * rc)**2))
    raise ValueError

print("\nL-T: decoherence/heat trade-off, 1D, units hbar = m = 1, r_C = 1")
x = np.linspace(-40, 40, 160001)
dx = x[1] - x[0]
for kind in ('gauss', 'flattop', 'ring'):
    f = envelope_1d(kind, x, 1.0)
    f /= np.sqrt(np.sum(f**2) * dx)
    gp = np.gradient(f, dx)
    G = np.sum(gp**2) * dx           # int |f'|^2  (heating per flash = G/2 in these units)
    worst = 0.0
    for d in (0.1, 0.5, 1.0, 2.0, 4.0, 8.0):
        n = int(round(d / dx))
        C = np.sum(f[:-n] * f[n:]) * dx
        lhs = 1 - C
        rhs = 0.5 * d**2 * G
        worst = max(worst, lhs / rhs)
        print(f"  {kind:8s} d={d:4.1f}: 1-C(d)={lhs:.6f}  (d^2/2)int|f'|^2={rhs:.6f}  ratio={lhs/rhs:.4f}")
    print(f"  {kind:8s} max ratio {worst:.4f} (must be <= 1); heating per flash hbar^2/(2m) int|f'|^2 = {G/2:.4f}")
print("  Gaussian 1D check: int|f'|^2 for exp(-x^2/2rc^2) normalized = 1/(2 rc^2) -> per flash 1/(4) per axis; 3 axes -> 3/4 hbar^2/(m rc^2): GRW value")

# ---------------------------------------------------------------- L-H
print("\nL-H: GRW dissipator heating is state independent (1D grid, hbar=m=1, rc=1, lambda=1)")
N = 1200
xg = np.linspace(-30, 30, N)
h = xg[1] - xg[0]
# kinetic H with periodic finite differences
lap = (np.diag(-2 * np.ones(N)) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1))
lap[0, -1] = lap[-1, 0] = 1
H = -0.5 * lap / h**2
def dHdt(psi):
    rho = np.outer(psi, psi.conj())
    # Lindblad: L(rho) = int dX K_X rho K_X - rho ; d<H>/dt = Tr(H L(rho))
    Xs = xg[::4]
    dX = Xs[1] - Xs[0]
    acc = 0.0
    norm = 0.0
    for X in Xs:
        K = np.exp(-(xg - X)**2 / 2.0)
        K = K / np.sqrt(np.sqrt(np.pi))   # int K^2 dX = 1
        Kr = K[:, None] * rho * K[None, :]
        acc += np.real(np.trace(H @ Kr)) * dX
    return acc - np.real(np.trace(H @ rho))
for name, psi in (("narrow packet", np.exp(-(xg - 3)**2 / (2 * 0.6**2)) * np.exp(1j * 1.3 * xg)),
                  ("cat state", np.exp(-(xg + 6)**2 / 2) + np.exp(-(xg - 6)**2 / 2)),
                  ("wide packet", np.exp(-(xg)**2 / (2 * 4.0**2)))):
    psi = psi / np.sqrt(np.sum(np.abs(psi)**2))
    print(f"  {name:13s}: d<H>/dt = {dHdt(psi):.5f}   (continuum c-number hbar^2/(2m) int|f'|^2 = 1/4 = 0.25)")
