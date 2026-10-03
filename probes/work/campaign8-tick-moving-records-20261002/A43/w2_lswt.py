"""A43 w2: linear spin waves (Holstein-Primakoff, S=1/2) over classical backgrounds of the
three fully soldered pair couplings H = sum_{x,a} s_x^T J_a s_{x+e_a} (Pauli units):
Heisenberg J s.s, compass K (e.s)(e.s), Moriya D e.(s x s). Supplied toys."""
import itertools, numpy as np
rng = np.random.default_rng(4343)
S = 0.5
E3 = np.eye(3)
def cross_mat(e):
    return np.array([[0, -e[2], e[1]], [e[2], 0, -e[0]], [-e[1], e[0], 0]])
def couplings(J=0., K=0., D=0.):
    # s_x^T M s_y with M = J 1 + K e e^T + D [e]  where s_x^T [e] s_y = e.(s_x x s_y)
    out = []
    for a in range(3):
        e = E3[a]
        Me = J * np.eye(3) + K * np.outer(e, e) + D * cross_mat(e).T  # x^T [e]^T y = (e x x).y = e.(x x y)
        out.append(Me)
    return out
# check the Moriya matrix convention: x^T M y = e.(x cross y)
x, y = rng.normal(size=3), rng.normal(size=3)
for a in range(3):
    M = couplings(D=1.)[a]
    assert abs(x @ M @ y - E3[a] @ np.cross(x, y)) < 1e-12

def frame(m):
    m = m / np.linalg.norm(m)
    t = np.array([1., 0, 0]) if abs(m[0]) < 0.9 else np.array([0, 1., 0])
    u = np.cross(t, m); u /= np.linalg.norm(u); v = np.cross(m, u)
    return u + 1j * v

class Lattice:
    def __init__(self, B, tau, mvec, Ja):
        self.B = np.array(B, float); self.Binv = np.linalg.inv(self.B)
        self.tau = np.array(tau, float); self.n = len(tau)
        self.m = np.array([v / np.linalg.norm(v) for v in mvec])
        self.Ja = Ja; self.bonds = []
        for r in range(self.n):
            for a in range(3):
                yv = self.tau[r] + E3[a]
                for rp in range(self.n):
                    nn = self.Binv @ (yv - self.tau[rp])
                    if np.allclose(nn, np.round(nn)):
                        self.bonds.append((r, rp, self.B @ np.round(nn), 4 * Ja[a])); break
                else:
                    raise ValueError("neighbour not found")
    def energy(self):  # classical energy per site, Pauli units (unit vectors)
        return sum(self.m[r] @ (Jm / 4) @ self.m[rp] for r, rp, D, Jm in self.bonds) / self.n
    def stationarity(self):
        h = np.zeros((self.n, 3))
        for r, rp, D, Jm in self.bonds:
            h[r] += Jm @ self.m[rp]; h[rp] += Jm.T @ self.m[r]
        return max(np.linalg.norm(np.cross(h[r], self.m[r])) for r in range(self.n))
    def blocks(self, k):
        n = self.n; A = np.zeros((n, n), complex); Bm = np.zeros((n, n), complex)
        e = [frame(mm) for mm in self.m]
        for r, rp, D, Jm in self.bonds:
            ph = np.exp(1j * k @ D)
            on = -S * (self.m[r] @ Jm @ self.m[rp])
            A[r, r] += on; A[rp, rp] += on
            c = (S / 2) * (e[r] @ Jm @ e[rp].conj())
            b = (S / 2) * (e[r] @ Jm @ e[rp])
            A[r, rp] += c * ph; A[rp, r] += np.conj(c) * np.conj(ph)
            Bm[r, rp] += b * ph; Bm[rp, r] += b * np.conj(ph)
        return A, Bm
    def M(self, k):
        A, Bm = self.blocks(k); Am, _ = self.blocks(-k)
        return np.block([[A, Bm], [Bm.conj().T, Am.T]])
    def omega(self, k):
        Mk = self.M(k); n = self.n
        eta = np.diag(np.r_[np.ones(n), -np.ones(n)])
        ev = np.linalg.eigvals(eta @ Mk)
        evs = ev[np.argsort(ev.real)]
        return evs[n:]  # upper half (positive branch if stable)

def report(name, lat, grid=10):
    print(f"--- {name} ---")
    print(f"  cell sites {lat.n}; classical energy/site {lat.energy():+.6f}; stationarity defect |h x m| = {lat.stationarity():.1e}")
    A0, B0 = lat.blocks(np.zeros(3))
    pair = max(np.abs(lat.blocks(kk)[1]).max() for kk in rng.uniform(-np.pi, np.pi, (20, 3)))
    print(f"  pair-creation block max|B(k)| = {pair:.3f}  ({'product state NOT an eigenstate' if pair > 1e-9 else 'product state is an exact eigenstate at harmonic order'})")
    g = np.linspace(-np.pi, np.pi, grid + 1)[:-1] + 1e-3
    mins = []; minM = np.inf; imag = 0.
    for kx, ky, kz in itertools.product(g, g, g):
        k = np.array([kx, ky, kz]); w = lat.omega(k)
        imag = max(imag, np.abs(w.imag).max()); mins.append(np.abs(w.real).min())
        minM = min(minM, np.linalg.eigvalsh(lat.M(k)).min())
    mins = np.array(mins)
    print(f"  over {grid}^3 grid: min eig of BdG matrix {minM:+.2e} ({'stable' if minM > -1e-9 else 'UNSTABLE'}); max|Im w| {imag:.1e}; "
          f"fraction of k with lowest w < 1e-3: {np.mean(mins < 1e-3):.4f}")
    w0 = np.sort(np.abs(lat.omega(np.zeros(3)).real))
    nz = int(np.sum(w0 < 1e-6)); print(f"  zero modes at k=0: {nz}; w(0) = {np.round(w0, 4)}")
    dirs = rng.normal(size=(60, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    dirs = np.vstack([dirs, [[1, 0, 0], [0, 1, 0], [0, 0, 1], np.array([1, 1, 1]) / np.sqrt(3), np.array([1, 1, 0]) / np.sqrt(2), np.array([1, -1, 0]) / np.sqrt(2)]])
    sl, ex = [], []
    for d in dirs:
        t = 1e-3
        w1 = np.sort(np.abs(lat.omega(t * d).real))[:max(nz, 1)]
        w2 = np.sort(np.abs(lat.omega(2 * t * d).real))[:max(nz, 1)]
        sl.append(w1 / t); ex.append(np.log2(np.maximum(w2, 1e-14) / np.maximum(w1, 1e-14)))
    sl, ex = np.array(sl), np.array(ex)
    for j in range(sl.shape[1]):
        print(f"  soft branch {j}: slope w/|k| over 66 directions {sl[:, j].min():.4f}..{sl[:, j].max():.4f}; local exponent {ex[:, j].min():.2f}..{ex[:, j].max():.2f}")
    for lab, d in [("(100)", dirs[-6]), ("(111)", dirs[-3]), ("(110)", dirs[-2]), ("(1-10)", dirs[-1])]:
        print(f"    along {lab}: slopes {np.round(sl[list(map(tuple, dirs)).index(tuple(d))], 4)}")
    return lat

# 1. Heisenberg ferromagnet J<0 (control: quadratic)
report("Heisenberg J=-1, uniform along z (control)", Lattice(np.eye(3), [[0, 0, 0]], [[0, 0, 1]], couplings(J=-1.)))
# 2. Heisenberg antiferromagnet J=+1, Neel along z, 2x2x2 cell
cell = [list(p) for p in itertools.product([0, 1], repeat=3)]
neel = lambda n: [((-1) ** sum(p)) * np.array(n, float) for p in cell]
lat = report("Heisenberg J=+1, Neel along z", Lattice(2 * np.eye(3), cell, neel([0, 0, 1]), couplings(J=1.)))
print(f"  LSWT formula check: slope 8*sqrt(3)*J = {8*np.sqrt(3):.4f}; w(k) vs 24 sqrt(1-g^2) at random k: max dev "
      f"{max(abs(np.sort(np.abs(lat.omega(k).real)).min() - min(24*np.sqrt(max(0,1-(np.sum(np.cos(k+np.pi*np.array(s)))/3)**2)) for s in itertools.product([0,1],repeat=3))) for k in rng.uniform(-np.pi,np.pi,(30,3))):.1e}")
report("Heisenberg J=+1, Neel along (111)", Lattice(2 * np.eye(3), cell, neel([1, 1, 1]), couplings(J=1.)))
# 3. compass K: K<0 uniform (classical ground manifold: every uniform direction); K>0 staggered
for n in ([0, 0, 1], [1, 1, 1], [1, 1, 0]):
    report(f"compass K=-1, uniform along {n}", Lattice(np.eye(3), [[0, 0, 0]], [n], couplings(K=-1.)))
for n in ([0, 0, 1], [1, 1, 1]):
    report(f"compass K=+1, Neel-type along {n}", Lattice(2 * np.eye(3), cell, neel(n), couplings(K=1.)))
cw = [np.array([(-1) ** p[0], (-1) ** p[1], (-1) ** p[2]]) / np.sqrt(3) for p in cell]
report("compass K=+1, component-wise staggered (m_a alternates along a)", Lattice(2 * np.eye(3), cell, cw, couplings(K=1.)))
# 4. Moriya D=+1: Luttinger-Tisza minimum -sqrt(3)|D| at q=(pi/2)(+-1,+-1,+-1); period-4 spiral, 4-site cell
Bsp = np.array([[1, 1, 1], [-1, 0, 1], [0, -1, 2]], float)
tau = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]
w = -np.array([1, 1, 1]) / np.sqrt(3)  # spiral normal for D>0
u = np.array([1, -1, 0]) / np.sqrt(2); v = np.cross(w, u)
for phase in (0.0, 0.37):
    msp = [u * np.cos(np.pi / 2 * sum(t) + phase) + v * np.sin(np.pi / 2 * sum(t) + phase) for t in tau]
    report(f"Moriya D=+1, period-4 spiral q=(pi/2)(1,1,1), in-plane phase {phase}", Lattice(Bsp, tau, msp, couplings(D=1.)))
# Luttinger-Tisza bound: lowest eigenvalue of Lambda(q) = i D [sin q]_x over q
qs = rng.uniform(-np.pi, np.pi, (20000, 3))
lt = min(np.linalg.eigvalsh(1j * cross_mat(np.sin(q))).min() for q in qs)
print(f"Moriya Luttinger-Tisza: min over 20000 q of lowest eig of i[sin q]x = {lt:.4f} (bound -sqrt(3) = {-np.sqrt(3):.4f})")
