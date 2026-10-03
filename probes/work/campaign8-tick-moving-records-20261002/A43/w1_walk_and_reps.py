"""A43 w1: the two-part walk H = sum_a sigma_a sin k_a, its covariance under full
soldering, and the representation lemmas (spinor class; clean cones from linear reps).
Supplied model; finite exact/numeric checks. No repo access."""
import itertools, numpy as np
rng = np.random.default_rng(43)
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]

def h(k):
    return sum(np.sin(k[a]) * SIG[a] for a in range(3))

# ---------- 24 proper cubic rotations and SU(2) lifts ----------
ROT = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            ROT.append(R)
assert len(ROT) == 24

def su2(R):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(th, 0):
        return I2.copy()
    if np.isclose(th, np.pi):
        M = (R + np.eye(3)) / 2; i = np.argmax(np.diag(M)); n = M[:, i] / np.sqrt(M[i, i])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
    U = np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * sum(n[a] * SIG[a] for a in range(3))
    return U

lift_err = 0.0
for R in ROT:
    U = su2(R)
    for a in range(3):
        lhs = U @ SIG[a] @ U.conj().T
        rhs = sum(R[b, a] * SIG[b] for b in range(3))
        lift_err = max(lift_err, np.abs(lhs - rhs).max())
print(f"[A] SU(2) lifts: max |U s_a U^dag - sum_b R_ba s_b| over 24 turns = {lift_err:.1e}")

# ---------- Q1: nodes, hands, speeds, partners ----------
print("[B] nodes of h(k)=sum sin k_a s_a at the eight points k in {0,pi}^3")
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
chis = []
for n in itertools.product([0, 1], repeat=3):
    k0 = np.pi * np.array(n, float)
    Va = [np.cos(k0[a]) * SIG[a] for a in range(3)]                  # exact velocity matrices
    cliff = max(np.abs(Va[a] @ Va[b] + Va[b] @ Va[a] - 2 * (a == b) * I2).max() for a in range(3) for b in range(3))
    v = np.array([[0.5 * np.trace(Va[a] @ SIG[b]).real for b in range(3)] for a in range(3)])
    chi = int(np.sign(np.linalg.det(v))); chis.append(chi)
    sl = []
    for d in dirs:
        t = 1e-6
        e = np.linalg.eigvalsh(h(k0 + t * d)); sl.append(e / t)
    sl = np.array(sl)
    print(f"  n={n}: ||h(k0)||={np.abs(h(k0)).max():.1e}  Clifford defect {cliff:.1e}  velocity tensor diag {np.diag(v)}"
          f"  hand {chi:+d}  slopes over 300 dirs: lower {sl[:,0].min():.8f}..{sl[:,0].max():.8f}, upper {sl[:,1].min():.8f}..{sl[:,1].max():.8f}")
print(f"  hands: {chis}, sum {sum(chis)}, (+){chis.count(1)} (-){chis.count(-1)}")
# exact shape: |E|^2 = sum sin^2 q_a around every node -> identical higher-order shape
q = rng.normal(size=(50, 3)) * 0.3
shape = max(abs(np.linalg.eigvalsh(h(np.pi*np.array(n)+qq))[1] - np.sqrt(np.sum(np.sin(qq)**2)))
            for n in itertools.product([0,1],repeat=3) for qq in q)
print(f"  |E(k0+q)| = sqrt(sum sin^2 q_a) at all 8 nodes: max dev {shape:.1e} (same speed and same lattice corrections at every node)")
# leading anisotropy: E = |q| - (sum q^4)/(6|q|^... ) -> E/|q| along (100) vs (111) at |q|=0.2
for d in [np.array([1,0,0.]), np.array([1,1,1.])/np.sqrt(3), np.array([1,1,0.])/np.sqrt(2)]:
    t = 0.2; print(f"  E/|q| at |q|=0.2 along {np.round(d,3)}: {np.sqrt(np.sum(np.sin(t*d)**2))/t:.6f}")
# no other bands: the symbol is 2x2; gap away from nodes
g = np.linspace(-np.pi, np.pi, 41)[:-1]
KK = np.array(np.meshgrid(g, g, g, indexing='ij')).reshape(3, -1).T
dist = np.min([np.linalg.norm(((KK - np.pi*np.array(n)) + np.pi) % (2*np.pi) - np.pi, axis=1) for n in itertools.product([0,1],repeat=3)], axis=0)
E = np.sqrt(np.sum(np.sin(KK)**2, axis=1))
print(f"  bands: 2 in total (2x2 symbol); min |E| on a 40^3 grid at distance >=0.3 from every node: {E[dist>=0.3].min():.4f}")

# ---------- covariance under full soldering ----------
cov = 0.0
for R in ROT:
    U = su2(R)
    for _ in range(40):
        k = rng.uniform(-np.pi, np.pi, 3)
        cov = max(cov, np.abs(U @ h(k) @ U.conj().T - h(R @ k)).max())
print(f"[C] Bloch covariance U(R) h(k) U(R)^dag = h(Rk): max dev over 24 turns x 40 k = {cov:.1e}")
# real-space check on the 4^3 torus (128 states)
L = 4; N = L**3
idx = lambda x: ((x[0] % L) * L + (x[1] % L)) * L + (x[2] % L)
Hrs = np.zeros((2*N, 2*N), complex)
for x in itertools.product(range(L), repeat=3):
    for a in range(3):
        e = np.zeros(3, int); e[a] = 1
        i, j = idx(x), idx(np.array(x) + e)
        # (S_a psi)(x) = (psi(x+e_a) - psi(x-e_a))/(2i): term s_a/(2i) from x to x+e_a, plus h.c.
        Hrs[2*i:2*i+2, 2*j:2*j+2] += SIG[a] / (2j)
        Hrs[2*j:2*j+2, 2*i:2*i+2] += (SIG[a] / (2j)).conj().T
assert np.allclose(Hrs, Hrs.conj().T)
rs = 0.0
for R in ROT:
    U = su2(R); G = np.zeros((2*N, 2*N), complex)
    for x in itertools.product(range(L), repeat=3):
        y = (R @ np.array(x)).astype(int); i, j = idx(x), idx(y)
        G[2*j:2*j+2, 2*i:2*i+2] = U
    rs = max(rs, np.abs(G @ Hrs @ G.conj().T - Hrs).max())
ev = np.linalg.eigvalsh(Hrs)
print(f"[C] real-space covariance on the 4^3 torus (128 states), all 24 turns about a site: max dev {rs:.1e}; zero modes {np.sum(np.abs(ev)<1e-9)} (expect 16)")
# inversion with axial spins: P H P = -H; staggered sign eps: eps H eps = -H; so eps*P is a symmetry
P = np.zeros((2*N, 2*N)); EPS = np.zeros((2*N, 2*N))
for x in itertools.product(range(L), repeat=3):
    i, j = idx(x), idx(-np.array(x)); P[2*j:2*j+2, 2*i:2*i+2] = np.eye(2)
    EPS[2*i:2*i+2, 2*i:2*i+2] = (-1)**sum(x) * np.eye(2)
print(f"[C] inversion (spin axial): |PHP + H| = {np.abs(P@Hrs@P.T + Hrs).max():.1e};  |eps H eps + H| = {np.abs(EPS@Hrs@EPS + Hrs).max():.1e};"
      f"  |(eps P) H (eps P)^T - H| = {np.abs(EPS@P@Hrs@P.T@EPS - Hrs).max():.1e}")
TH = np.kron(np.eye(N), sy)
print(f"[C] time reversal s_y K: |s_y conj(H) s_y - H| = {np.abs(TH@Hrs.conj()@TH - Hrs).max():.1e}")

# ---------- representation lemmas ----------
# classes of O: E, 8C3, 3C2(=C4^2), 6C4, 6C2'
sizes = np.array([1, 8, 3, 6, 6])
CH = {'A1': [1,1,1,1,1], 'A2': [1,1,1,-1,-1], 'E': [2,-1,2,0,0], 'T1': [3,0,-1,1,-1], 'T2': [3,0,-1,-1,1]}
CH = {k: np.array(v, float) for k, v in CH.items()}
def mult(chi, irr):
    return np.sum(sizes * chi * CH[irr]) / 24
def chi_of(R):  # class index of a rotation
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(th, 0): return 0
    if np.isclose(th, 2*np.pi/3): return 1
    if np.isclose(th, np.pi/2): return 3
    # theta = pi: C4^2 (axis along a cube axis) or C2' (face diagonal)
    M = (R + np.eye(3)) / 2; n = M[:, np.argmax(np.diag(M))]
    return 2 if np.sum(np.abs(n) > 1e-9) == 1 else 4
cls = np.zeros(5, int)
for R in ROT: cls[chi_of(R)] += 1
print(f"[D] class sizes from the 24 turns: {cls} (expect [1 8 3 6 6])")
spin_half_abs2 = np.zeros(5)
for R in ROT: spin_half_abs2[chi_of(R)] = abs(np.trace(su2(R)))**2
print(f"[D] |chi_1/2|^2 per class = {spin_half_abs2}  -> End(spinor) contains T1 x{mult(spin_half_abs2,'T1'):.0f}, A1 x{mult(spin_half_abs2,'A1'):.0f}")
for name, chi in [('A1+A1', CH['A1']+CH['A1']), ('A1+A2', CH['A1']+CH['A2']), ('A2+A2', CH['A2']+CH['A2']), ('E', CH['E'])]:
    print(f"[D] linear 2-dim rep {name:6s}: End contains T1 x{mult(chi*chi,'T1'):.0f}  (no vector of internal operators -> no covariant k.Gamma term)")
for name, chi in [('T1', CH['T1']), ('A1+T1', CH['A1']+CH['T1'])]:
    print(f"[D] linear rep {name:6s}: End contains T1 x{mult(chi*chi,'T1'):.0f}")
# vacuum (+) doublet: the lift of the 2pi turn is diag(1,-1,-1), not a scalar -> no O-action on M_3
U4 = np.linalg.matrix_power(np.block([[np.eye(1), np.zeros((1,2))],[np.zeros((2,1)), su2(ROT[[chi_of(R) for R in ROT].index(3)])]]), 4)
print(f"[D] vacuum + spin-1/2 doublet (3 states): (lift of a quarter turn)^4 = diag{np.round(np.diag(U4).real,6)} -> conjugation by it is not the identity on M_3")

# spin-1 (T1) internal space: covariant linear term gamma k.S has a flat helicity-0 band
S1 = [np.array([[0,0,0],[0,0,-1j],[0,1j,0]]), np.array([[0,0,1j],[0,0,0],[-1j,0,0]]), np.array([[0,-1j,0],[1j,0,0],[0,0,0]])]
fl = max(np.abs(np.sort(np.linalg.eigvalsh(sum(np.sin(k[a])*S1[a] for a in range(3))))[1]) for k in rng.uniform(-np.pi,np.pi,(200,3)))
print(f"[E] spin-1 walk sum sin k_a S^a: middle band max |E| over 200 random k = {fl:.1e} (exactly flat)")
# general covariant NN triplet hop: M_e = p(1-ee^T) + r ee^T + q*i[e]x ; Bloch H = sum_a 2cos k_a (p(1-e e)+r e e) + 2 q sin k_a S^a
p, r, qq = 0.31, -0.47, 0.5
def HT(k):
    out = np.zeros((3,3), complex)
    for a in range(3):
        e = np.zeros(3); e[a] = 1
        out += 2*np.cos(k[a])*(p*(np.eye(3)-np.outer(e,e)) + r*np.outer(e,e)) + 2*qq*np.sin(k[a])*S1[a]
    return out
E0 = np.linalg.eigvalsh(HT(np.zeros(3)))
for d in [np.array([1,0,0.]), np.array([1,1,1.])/np.sqrt(3)]:
    for t in [1e-2, 2e-2]:
        e = np.sort(np.linalg.eigvalsh(HT(t*d))) - E0[0]
        print(f"[E] covariant triplet hop (p={p}, r={r}, q={qq}) at t={t} along {np.round(d,3)}: E-E(Gamma) = {np.round(e,6)}  (middle/t^2 = {e[1]/t**2:.4f})")
# A1+T1 (two spinors): covariant linear couplings alpha (e0 k^T + k e0^T) + beta i(e0 k^T - k e0^T) + gamma k.S
def H4(k, al, be, ga):
    M = np.zeros((4,4), complex)
    M[0,1:] = (al + 1j*be) * k; M[1:,0] = (al - 1j*be) * k
    M[1:,1:] = ga * sum(k[a]*S1[a] for a in range(3))
    return M
for (al, be, ga) in [(1.0, 0.0, 1.0), (0.6, 0.8, 1.0), (1.0, 0.0, 0.5), (1.0, 0.0, 0.0)]:
    ks = rng.normal(size=(100,3))
    dev = max(np.abs(H4(k,al,be,ga)@H4(k,al,be,ga) - (ga**2)*np.dot(k,k)*np.eye(4)).max() for k in ks)
    G = [H4(np.eye(3)[a], al, be, ga) for a in range(3)]
    vol = G[0]@G[1]@G[2]
    ev = np.linalg.eigvals(vol) if ga != 0 else np.array([np.nan])
    print(f"[E] A1+T1, |alpha+i beta|={abs(al+1j*be):.2f}, gamma={ga}: max|H^2 - gamma^2 k^2| = {dev:.2e}; "
          f"volume element G1G2G3 eigenvalues {np.round(ev,6)}")
# realization: two spinors, Gamma_a = s_a (x) 1 ; check covariance under U(x)U and the splitting by d s.s'
cov4 = max(np.abs(np.kron(su2(R),su2(R)) @ np.kron(h(k),I2) @ np.kron(su2(R),su2(R)).conj().T - np.kron(h(R@k),I2)).max()
           for R in ROT for k in rng.uniform(-np.pi,np.pi,(10,3)))
ss = sum(np.kron(SIG[a], SIG[a]) for a in range(3))
print(f"[E] walk (x) inert spinor: covariance under U(x)U max dev {cov4:.1e}; spectrum at k=0 with d*s.s' (d=0.1): "
      f"{np.round(np.linalg.eigvalsh(0.1*ss),6)} (singlet/triplet split) -> the doubled cone needs d=0 or a flavour symmetry")
