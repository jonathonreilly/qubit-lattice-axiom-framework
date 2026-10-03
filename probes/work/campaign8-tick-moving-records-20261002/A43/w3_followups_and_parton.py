"""A43 w3: (i) Neel LSWT closed form, (ii) Moriya period-4 spiral at other momenta and its
classical degeneracy, (iii) parton mean field with the soldered hopping f^dag (i s.e) f at half
filling (unprojected; supplied toy)."""
import itertools, numpy as np, importlib.util, sys, io, contextlib
spec = importlib.util.spec_from_file_location("w2", __file__.replace("w3_followups_and_parton.py", "w2_lswt.py"))
src = open(spec.origin).read().split("# 1. Heisenberg ferromagnet")[0]   # library part only
ns = {}; exec(compile(src, "w2lib", "exec"), ns)
Lattice, couplings = ns["Lattice"], ns["couplings"]
rng = np.random.default_rng(7)

# (i) Neel: w(k) = J' S z sqrt(1-g^2) = 12 J sqrt(1-g^2) (Pauli J; J'=4J, S=1/2, z=6); slope 4 sqrt(3) J
cell = [list(p) for p in itertools.product([0, 1], repeat=3)]
neel = [((-1) ** sum(p)) * np.array([0, 0, 1.]) for p in cell]
lat = Lattice(2 * np.eye(3), cell, neel, couplings(J=1.))
dev = 0.
for k in rng.uniform(-np.pi, np.pi, (40, 3)):
    num = np.sort(np.abs(lat.omega(k).real))
    ana = np.sort(np.repeat([12 * np.sqrt(max(0., 1 - (np.sum(np.cos(k + np.pi * np.array(s))) / 3) ** 2))
                             for s in itertools.product([0, 1], repeat=3) if sum(s) % 2 == 0], 2))
    dev = max(dev, np.abs(num - ana).max())
print(f"[i] Neel LSWT vs 12 J sqrt(1-g^2) (g = mean cos), all 8 folded bands at 40 random k: max dev {dev:.1e}; slope 4 sqrt(3) = {4*np.sqrt(3):.4f}")
# leading anisotropy of the Neel branch: w/|k| at |k| = 0.2 along three directions
for d in [np.array([1, 0, 0.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, 1, 0.]) / np.sqrt(2)]:
    t = 0.2; print(f"    w/|k| at |k|=0.2 along {np.round(d,3)}: {np.sort(np.abs(lat.omega(t*d).real))[0]/t:.5f}")

# (ii) Moriya spiral: soft modes at other momenta? classical degeneracy direction
Bsp = np.array([[1, 1, 1], [-1, 0, 1], [0, -1, 2]], float); tau = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]
w = -np.array([1, 1, 1]) / np.sqrt(3); u = np.array([1, -1, 0]) / np.sqrt(2); v = np.cross(w, u)
msp = [u * np.cos(np.pi / 2 * sum(t)) + v * np.sin(np.pi / 2 * sum(t)) for t in tau]
sp = Lattice(Bsp, tau, msp, couplings(D=1.))
pts = {"(0,0,pi)": [0, 0, np.pi], "(pi,0,0)": [np.pi, 0, 0], "(0,pi,pi)": [0, np.pi, np.pi], "(pi,pi,pi)": [np.pi] * 3,
       "(pi/2,pi/2,pi/2)": [np.pi / 2] * 3, "(pi/2,pi/2,-pi/2)": [np.pi / 2, np.pi / 2, -np.pi / 2], "(pi,pi,0)": [np.pi, np.pi, 0]}
for lab, k in pts.items():
    print(f"[ii] spiral w at k={lab}: {np.round(np.sort(np.abs(sp.omega(np.array(k, float)).real)), 4)}")
# finer search for the global minimum of the lowest branch
best = (np.inf, None)
for k in rng.uniform(-np.pi, np.pi, (4000, 3)):
    wl = np.sort(np.abs(sp.omega(k).real))[0]
    if wl < best[0]: best = (wl, k)
print(f"[ii] lowest branch: min over 4000 random k = {best[0]:.4f} at k = {np.round(best[1],3)} (away from k=0 nothing soft)")
# classical degeneracy: energy of the spiral is flat in the in-plane phase and in the choice of diagonal
for ph in (0., 0.3, 1.1):
    m2 = [u * np.cos(np.pi / 2 * sum(t) + ph) + v * np.sin(np.pi / 2 * sum(t) + ph) for t in tau]
    print(f"[ii] in-plane phase {ph}: E/site = {Lattice(Bsp, tau, m2, couplings(D=1.)).energy():+.12f}")
# isotropy beyond leading order: w/|k| at |k|=0.2
for d in [np.array([1, 0, 0.]), np.array([1, 1, 1.]) / np.sqrt(3), np.array([1, -1, 0.]) / np.sqrt(2), np.array([1, 1, 0.]) / np.sqrt(2)]:
    t = 0.2; print(f"    spiral soft branch w/|k| at |k|=0.2 along {np.round(d,3)}: {np.sort(np.abs(sp.omega(t*d).real))[0]/t:.5f}")
# random-start classical minimization of the pure Moriya energy on a 4^3 torus: does anything beat -sqrt(3)?
L = 4; N = L ** 3
def idx(x): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
def Ecl(M):
    E = 0.
    for a in range(3):
        sh = np.roll(M.reshape(L, L, L, 3), -1, axis=a).reshape(N, 3)
        E += np.sum(np.cross(M, sh)[:, a])
    return E / N
best = 0.
for trial in range(6):
    M = rng.normal(size=(N, 3)); M /= np.linalg.norm(M, axis=1)[:, None]
    par = (np.indices((L, L, L)).sum(axis=0) % 2).reshape(N)
    for it in range(300):   # checkerboard local-field alignment (energy non-increasing)
        for s in (0, 1):
            Mr = M.reshape(L, L, L, 3); h = np.zeros_like(Mr)
            for a in range(3):
                e = np.eye(3)[a]
                fwd = np.roll(Mr, -1, axis=a); bwd = np.roll(Mr, 1, axis=a)
                h += np.cross(fwd, e)       # d/dm_x of e.(m_x x m_{x+e}) = m_{x+e} x e
                h += np.cross(e, bwd)       # d/dm_x of e.(m_{x-e} x m_x) = e x m_{x-e}
            h = h.reshape(N, 3); sel = par == s
            M[sel] = -h[sel] / np.maximum(np.linalg.norm(h[sel], axis=1)[:, None], 1e-12)
    best = min(best, Ecl(M))
print(f"[ii] greedy minimization of the pure Moriya energy, 6 random starts on 4^3: best E/site = {best:.5f} (spiral: {-np.sqrt(3):.5f})")

# (iii) parton mean field: H_MF = sum_x,a f_x^dag (i s_a) f_{x+e_a} + h.c.  -> h(k) = -2 sum_a s_a sin k_a
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]
def build(L, kind, tw=np.pi):
    N = L ** 3; H = np.zeros((2 * N, 2 * N), complex)
    for x in itertools.product(range(L), repeat=3):
        for a in range(3):
            y = list(x); y[a] += 1; ph = np.exp(1j * tw) if y[a] == L else 1.0
            i, j = idx_L(x, L), idx_L(y, L)
            t = 1j * SIG[a] if kind == "soldered" else -np.eye(2)
            H[2*i:2*i+2, 2*j:2*j+2] += t * ph; H[2*j:2*j+2, 2*i:2*i+2] += (t * ph).conj().T
    return H
def idx_L(x, L): return ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
L = 6; N = L ** 3
for kind in ("soldered", "singlet"):
    H = build(L, kind); ev, V = np.linalg.eigh(H)
    occ = V[:, :N]; G = (occ.conj() @ occ.T)   # G[(i,al),(j,be)] = <f^dag_{i al} f_{j be}>
    gap = ev[N] - ev[N - 1]
    x0 = (0, 0, 0); i0 = idx_L(x0, L)
    res = {}
    for a in range(3):
        y = [0, 0, 0]; y[a] = 1; j0 = idx_L(y, L)
        gxy = G[2*i0:2*i0+2, 2*j0:2*j0+2]; gyx = G[2*j0:2*j0+2, 2*i0:2*i0+2]
        gxx = G[2*i0:2*i0+2, 2*i0:2*i0+2]; gyy = G[2*j0:2*j0+2, 2*j0:2*j0+2]
        C = np.zeros((3, 3))
        for p in range(3):
            for q in range(3):
                disc = np.trace(SIG[p] @ gxx.T) * np.trace(SIG[q] @ gyy.T)
                conn = -np.trace(SIG[p] @ gyx.T @ SIG[q] @ gxy.T)
                C[p, q] = (disc + conn).real
        res[a] = C
    e = np.eye(3)
    heis = np.mean([np.trace(res[a]) for a in range(3)])
    comp = np.mean([res[a][a, a] for a in range(3)])
    mor = np.mean([sum(np.cross(e[p], e[q])[a] * res[a][p, q] for p in range(3) for q in range(3)) for a in range(3)])
    mag = max(abs(np.trace(SIG[p] @ G[2*i0:2*i0+2, 2*i0:2*i0+2].T)) for p in range(3))
    print(f"[iii] {kind:8s} ansatz, L={L} antiperiodic, half filling: gap at the filling level {gap:.3f}; |<s_x>| = {mag:.1e}; "
          f"per bond <s.s> = {heis:+.4f}, <(e.s)(e.s)> = {comp:+.4f}, <e.(s x s)> = {mor:+.1e}  (unprojected)")
# the soldered ansatz's Fermi level sits at the eight nodes: periodic L=6 has 16 exact zero modes
Hp = build(6, "soldered", tw=0.0); evp = np.linalg.eigvalsh(Hp)
print(f"[iii] periodic L=6: zero modes of the soldered hopping = {np.sum(np.abs(evp) < 1e-9)} (eight nodes x two), "
      f"filling level at E=0 (half filling = {N} of {2*N} states; levels below 0: {np.sum(evp < -1e-9)})")
