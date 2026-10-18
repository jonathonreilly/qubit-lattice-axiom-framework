#!/usr/bin/env python3
"""Independent check of item 6 (B1).  Own Bloch construction from a cell gauge;
imports only the PSG module's combinatorial definitions (corners, rotations,
gf2_solve, psg_sign) for the torus symmetry check."""
import itertools, os, sys
import numpy as np
import sympy as sp
from scipy.linalg import expm
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), *[os.pardir] * 5))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
import corner_fermion_projective_symmetry_group_class_and_site_shell_2026_10_17 as M
C = M._run_reviewed_program(definitions_only=True)
rng = np.random.default_rng(12345)
s3 = np.sqrt(3)

# ======================= (a) D'Ariano-Perinotti Weyl automaton, built as a matrix
print("== (a) DP Weyl automaton")
PA = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
def U_dp(k, sg=-1):
    c, s = np.cos(k / s3), np.sin(k / s3)
    d = c[0]*c[1]*c[2] + sg*s[0]*s[1]*s[2]
    n = [s[0]*c[1]*c[2] - sg*c[0]*s[1]*s[2], c[0]*s[1]*c[2] + sg*s[0]*c[1]*s[2], c[0]*c[1]*s[2] - sg*s[0]*s[1]*c[2]]
    return d*np.eye(2) - 1j*sum(ni*P for ni, P in zip(n, PA))
ks = rng.uniform(-6, 6, (200, 3))
print(" unitary:", max(np.abs(U_dp(k) @ U_dp(k).conj().T - np.eye(2)).max() for k in ks))
# Fourier support: sample on a grid and fit with the 8 BCC neighbours h=(+-1,+-1,+-1)/sqrt3
H8 = np.array(list(itertools.product((1, -1), repeat=3))) / s3
A = np.array([[np.exp(-1j * k @ h) for h in H8] for k in ks])
for sgn in (-1, 1):
    Y = np.array([U_dp(k, sgn).ravel() for k in ks]); coef, res, *_ = np.linalg.lstsq(A, Y, rcond=None)
    print(f" sign {sgn:+d}: residual of 8-neighbour BCC fit {np.abs(A @ coef - Y).max():.1e}; transfer matrices rank",
          [np.linalg.matrix_rank(coef[i].reshape(2, 2), 1e-10) for i in range(8)])
om = lambda k: np.arccos(np.clip(np.cos(k[0]/s3)*np.cos(k[1]/s3)*np.cos(k[2]/s3) - np.prod(np.sin(k/s3)), -1, 1))
print(" eigenphases of U equal +-arccos(ccc - sss) (sign -1 branch):",
      max(abs(np.sort(np.abs(np.angle(np.linalg.eigvals(U_dp(k)))))[0] - om(k)) for k in ks))
# group velocity: max |v| and max per component (causal cone of BCC step is the cube |x_i| <= 1/sqrt3)
def grad(k, h=1e-6): return np.array([(om(k + h*e) - om(k - h*e)) / (2*h) for e in np.eye(3)])
G = np.array([grad(k) for k in rng.uniform(-np.pi*s3, np.pi*s3, (8000, 3))])
G = G[np.all(np.isfinite(G), 1)]
print(f" max |v| = {np.linalg.norm(G, axis=1).max():.4f}; max |v_i| = {np.abs(G).max():.4f} (cube bound 1/sqrt3 = {1/s3:.4f}); "
      f"max |v|_1 = {np.abs(G).sum(1).max():.4f}")
# symmetry group of omega among 48 signed permutations
SP = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Mx = np.zeros((3, 3)); Mx[range(3), p] = sg; SP.append(Mx)
inv = [g for g in SP if all(abs(om(g @ k) - om(k)) < 1e-12 for k in ks[:30])]
print(f" signed perms leaving omega invariant: {len(inv)}, of which proper: {sum(np.linalg.det(g) > 0 for g in inv)}, "
      f"contains inversion: {any(np.allclose(g, -np.eye(3)) for g in inv)}")
for q in (0.02, 0.01, 0.005):
    dd = rng.normal(size=(2000, 3)); dd /= np.linalg.norm(dd, axis=1)[:, None]
    v = np.array([om(q*d)/q for d in dd]); print(f"  |k|={q}: mean phase speed {v.mean():.7f}, rel spread {np.ptp(v)/v.mean():.5f}")

# ======================= (b) corner step, own cell gauge and Bloch matrices
print("== (b) corner step")
DIRS = C['DIRS']; CORN = C['CORNERS']; CI = {c: i for i, c in enumerate(CORN)}
neg = lambda d: tuple(-x for x in d); perp = lambda d, e: sum(a*b for a, b in zip(d, e)) == 0 and d != e
Z = (0, 0, 0)
# edge types in the one-site cell: (c1, c2, shift); on-site and link
ET = {}; ETL = []
def addt(c1, c2, sh, kind):
    if (c1, c2, sh) in ET: return
    ET[(c1, c2, sh)] = ET[(c2, c1, neg(sh))] = len(ETL); ETL.append((c1, c2, sh, kind))
for c in CORN:
    d, e = tuple(c)
    for a, b in ((d, e), (e, d)):
        for f in DIRS:
            if perp(f, a) and perp(f, b) and f != neg(b) and f != neg(a): addt(c, frozenset((a, f)), Z, 'on')
        addt(c, frozenset((neg(a), b)), a, 'link')
print(" cell edge types:", len(ETL), {k: sum(t[3] == k for t in ETL) for k in ('on', 'link')})
add3 = lambda a, b: tuple(x+y for x, y in zip(a, b))
def cyc(seq): return [ET[(c1, c2, tuple(y-x for x, y in zip(p1, p2)))] for (c1, p1), (c2, p2) in zip(seq, seq[1:] + seq[:1])]
cyc_all = []
for d in DIRS:   # squares and tubes
    ring = [f for f in DIRS if perp(f, d)]; r0 = ring[0]; r1 = [f for f in ring if perp(f, r0) and f != neg(r0)][0]
    ring = [r0, r1, neg(r0), neg(r1)]
    cyc_all.append((cyc([(frozenset((d, r)), Z) for r in ring]), 1))
    for i in range(4):
        p, q = ring[i], ring[(i+1) % 4]
        cyc_all.append((cyc([(frozenset((d, p)), Z), (frozenset((neg(d), p)), d), (frozenset((neg(d), q)), d), (frozenset((d, q)), Z)]), 1))
for s in itertools.product((1, -1), repeat=3):
    x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
    cyc_all.append((cyc([(frozenset((x, y)), Z), (frozenset((y, z)), Z), (frozenset((z, x)), Z)]), 0))
plaq = []
for d in DIRS:
    for e in DIRS:
        if perp(d, e):
            cy = cyc([(frozenset((d, e)), Z), (frozenset((neg(d), e)), d), (frozenset((neg(d), neg(e))), add3(d, e)), (frozenset((d, neg(e))), e)])
            cyc_all.append((cy, 1)); plaq.append(cy)
ug = C['gf2_solve']([c for c, _ in cyc_all], [f for _, f in cyc_all], len(ETL))
assert ug is not None
sgn = (-1.0) ** np.array(ug, float)
print(" all 24 link 4-cycles (plaquettes) have flux pi:", all(sum(ug[j] for j in c) % 2 == 1 for c in plaq))
def bloch(kind, t, k):
    H = np.zeros((12, 12), complex)
    for i, (c1, c2, sh, kd) in enumerate(ETL):
        if kd != kind: continue
        a = -t * sgn[i]; ph = np.exp(1j * np.dot(k, sh))
        H[CI[c2], CI[c1]] += a * ph; H[CI[c1], CI[c2]] += a * np.conj(ph)
    return H
HL = lambda k: bloch('link', 1.0, k)
print(" max |H_link(k)^2 - 2| over 500 random k:", max(np.abs(HL(k) @ HL(k) - 2*np.eye(12)).max() for k in rng.uniform(-9, 9, (500, 3))))
print(" diag of H_link(k) zero (trace 0):", np.allclose(np.diag(HL(np.array([.3, .7, -1.1]))), 0))
Hon = bloch('on', 1.0, np.zeros(3)).real
w, V = np.linalg.eigh(Hon); print(" on-site hopping eigenvalues:", np.round(w, 4))
P2 = V[:, np.abs(w - 2) < 1e-8]; Uc = np.eye(12) - 2 * P2 @ P2.T
Wk = lambda k: HL(k) / np.sqrt(2) @ Uc
kst = np.pi / 2 * np.array([1, -1, 1])
# symmetry: the commutant at k*.  Build the torus PSG Bloch reps using module combinatorics + my gauge
L = C['L']; VERTS = C['VERTS']; nV = len(VERTS); dm = lambda x: ((x + 1) % L) - 1
u = np.zeros(C['nE'], np.uint8)
for key, i in C['EID'].items():
    a, b = tuple(key); (v, c), (w_, c2) = VERTS[a], VERTS[b]; u[i] = ug[ET[(c, c2, tuple(dm(y - x) for x, y in zip(v, w_)))]]
rotsP = [C['psg_sign'](lambda q, R=R: C['rot_vert'](R, q), u) for R in C['ROTS']]
assert all(s is not None for _, s in rotsP)
def mono(P, s): Mx = np.zeros((nV, nV)); Mx[P, np.arange(nV)] = (-1.0) ** np.array(s, float); return Mx
Mrot = [mono(P, s) for P, s in rotsP]
def Bl(k):
    B = np.zeros((nV, 12), complex)
    for a, (v, c) in enumerate(VERTS): B[a, CI[c]] = np.exp(1j * np.dot(k, v)) / np.sqrt(L ** 3)
    return B
Bs = Bl(kst)
rho = [Bs.conj().T @ Mg @ Bs for Mg in Mrot]
print(" PSG rotations map k*-space to itself (unitary 12x12):", all(np.allclose(r @ r.conj().T, np.eye(12)) for r in rho))
print(" commutant dim at k* = (1/24) sum |chi|^2 =", np.sum([abs(np.trace(r))**2 for r in rho]) / 24, "(E1/2+E5/2+2G3/2 -> 6)")
print(" W(k*) commutes with all 24 rho:", all(np.allclose(r @ Wk(kst), Wk(kst) @ r) for r in rho))
# real-space torus check of W symmetry (own real-space construction from cell types)
def real(kind, t):
    H = np.zeros((nV, nV))
    for v in C['SITES']:
        for i, (c1, c2, sh, kd) in enumerate(ETL):
            if kd != kind: continue
            a = C['VID'][(v, c1)]; b = C['VID'][(tuple((x + y) % L for x, y in zip(v, sh)), c2)]
            H[b, a] = H[a, b] = -t * sgn[i]
    return H
RL = real('link', 1.0) / np.sqrt(2); Uon = np.kron(np.eye(L**3), Uc)  # VERTS ordered site-major, corner-minor
assert [VERTS[i][1] for i in range(12)] == CORN
Wr = RL @ Uon
transP = [C['psg_sign'](lambda q, t=t: C['trans_vert'](t, q), u) for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
print(" real-space W unitary, commutes with 24 PSG rotations and 3 translations:", np.allclose(Wr @ Wr.T, np.eye(nV)),
      all(np.allclose(Mg @ Wr, Wr @ Mg) for Mg in Mrot + [mono(P, s) for P, s in transP]))
# exact node analysis with sympy at k*
def exact(Mnum): return sp.Matrix(12, 12, lambda i, j: sp.nsimplify(round(Mnum[i, j].real, 9)) + sp.I*sp.nsimplify(round(Mnum[i, j].imag, 9)))
HLs = exact(HL(kst)); Ucs = exact(Uc)
assert (HLs*HLs - 2*sp.eye(12)).is_zero_matrix and (Ucs*Ucs - sp.eye(12)).is_zero_matrix
qx, qy, qz = sp.symbols('q_x q_y q_z', real=True)
dH = [exact((HL(kst + 1e-7*e) - HL(kst - 1e-7*e)) / 2e-7) for e in np.eye(3)]  # entries are 0, +-1, +-i
Wst = HLs*Ucs/sp.sqrt(2); dW = (qx*dH[0] + qy*dH[1] + qz*dH[2])*Ucs/sp.sqrt(2)
N = (Wst - sp.eye(12)).nullspace(); Nm = sp.Matrix.hstack(*N)
print(" exact node dimension:", Nm.shape[1])
# W^H dW = Uc H^H dH Uc / 2 : rational Gaussian, no sqrt2
Gi = (Nm.H*Nm).inv()
Mi = [sp.expand(Gi*Nm.H*(-sp.I)*Ucs*HLs.H*dH[i]*Ucs*Nm/2) for i in range(3)]
qv = (qx, qy, qz); Mq = sum((qv[i]*Mi[i] for i in range(3)), sp.zeros(6, 6))
print(" exact: M(q)^3 - (|q|^2/3) M(q) == 0:", sp.expand(Mq**3 - (qx**2+qy**2+qz**2)/3*Mq).is_zero_matrix,
      "; tr M(q)^2 =", sp.factor(sp.expand((Mq**2).trace())), "; tr M(q) =", sp.expand(Mq.trace()))
# flat bands and Jordan count
print(" eigenvalue-1 multiplicity at random k:", [int(np.sum(np.abs(np.linalg.eigvals(Wk(k)) - 1) < 1e-9)) for k in rng.uniform(-3, 3, (5, 3))],
      "; +1 dims of R1,R2:", int(round((12 + np.trace(HL(np.ones(3)) / np.sqrt(2)).real) / 2)), int(round((12 + np.trace(Uc)) / 2)))
# doublet inside the node: E1/2 = 2-dim eigenspace of a random commutant element restricted to node
X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = sum(r @ X @ r.conj().T for r in rho); X = X + X.conj().T
Nn, _ = np.linalg.qr(np.array(Nm.evalf(), complex))
ev, vv = np.linalg.eigh(Nn.conj().T @ X @ Nn); print(" commutant restricted to node, eigenvalues:", np.round(ev, 4))
grp = [np.where(np.abs(ev - x) < 1e-6)[0] for x in ev]; dbl = [g for g in grp if len(g) == 2][0]
D = Nn @ vv[:, dbl]; Gs = Nn @ vv[:, [i for i in range(6) if i not in dbl]]
for e in np.eye(3):
    dWn = (Wk(kst + 1e-6*e) - Wk(kst - 1e-6*e)) / 2e-6; T = -1j * Wk(kst).conj().T @ dWn
    print(f"  dir {e}: ||P_D T P_D|| = {np.abs(D.conj().T @ T @ D).max():.1e}, ||P_D T P_G|| = {np.abs(D.conj().T @ T @ Gs).max():.3f}")
# speed beyond first order: exactness test of 1/sqrt3 along directions
for d in (np.array([1, 0, 0]), np.ones(3)/s3, np.array([1, 2, 0])/np.sqrt(5)):
    for q in (1e-2, 1e-3):
        ph = np.sort(np.abs(np.angle(np.linalg.eigvals(Wk(kst + q*d))))); print(f"  d={np.round(d,3)} q={q}: |phase|/q {np.round(ph[:6]/q, 9)}")

# ======================= (c) no-go lemma tests
print("== (c) no-go lemma")
def sym_onsite(n=1):
    out = []
    for _ in range(n):
        A = rng.normal(size=(12, 12)) + 1j*rng.normal(size=(12, 12)); A = A + A.conj().T
        # on-site symmetric: average over the on-site part of rho at k=0
        out.append(A)
    return out
def rand_sym_onsite_unitary():
    A = rng.normal(size=(12, 12)) + 1j*rng.normal(size=(12, 12)); A = A + A.conj().T
    Af = np.kron(np.eye(L**3), A); S = sum(Mg @ Af @ Mg.T for Mg in Mrot) / 24
    blk = S[:12, :12]; Sf = np.kron(np.eye(L**3), blk)
    assert all(np.allclose(Mg @ Sf, Sf @ Mg) for Mg in Mrot[:24:5])
    return expm(1j * blk)
def iso_doublet_velocity(Wf):
    W0 = Wf(kst); e0, v0 = np.linalg.eig(W0); ph = np.angle(e0); res = []
    for i in range(12):
        same = np.where(np.abs(np.exp(1j*(ph - ph[i])) - 1) < 1e-8)[0]
        if len(same) == 2 and i == same[0]:
            sp_ = 0
            for d in rng.normal(size=(6, 3)):
                d /= np.linalg.norm(d); e = np.angle(np.linalg.eigvals(Wf(kst + 1e-4*d)) * np.exp(-1j*ph[i])); e = np.sort(e[np.abs(e) < 1e-2])
                sp_ = max(sp_, (e[-1] - e[0]) / 2e-4)
            res.append(sp_)
    return res
RLk = lambda k: HL(k) / np.sqrt(2)
out = []
for t in range(4):
    U1, U2, U3 = rand_sym_onsite_unitary(), rand_sym_onsite_unitary(), rand_sym_onsite_unitary()
    th = rng.uniform(0, 2*np.pi)
    F3 = lambda k: RLk(k) @ U3 @ RLk(k)             # conjugated on-site unitary: many-valued constant spectrum
    for Wf in (lambda k: RLk(k) @ U1, lambda k: expm(1j*th*RLk(k)) @ U1 @ F3(k) @ U2, lambda k: F3(k) @ U1 @ RLk(k) @ U2 @ F3(k)):
        out += iso_doublet_velocity(Wf)
print(f" constant-spectrum symmetric factors: {len(out)} isolated doublets, max half-splitting/q = {max(out):.1e}")
# hypothesis necessity: symmetric factor with k-dependent spectrum (exp of a symmetric hopping Hamiltonian with flux-odd term)
Hs = lambda k: bloch('on', -1.0, k) + bloch('link', 0.2, k) + 0.3j*(HL(k) @ Hon - Hon @ HL(k))
Kr = 0.3j*(real('link', 1.0) @ np.kron(np.eye(L**3), Hon) - np.kron(np.eye(L**3), Hon) @ real('link', 1.0))
print(" i[H_link, H_on] commutes with PSG rotations (real space):", all(np.allclose(Mg @ Kr, Kr @ Mg) for Mg in Mrot), np.abs(Kr).max())
out2 = []
for th in (0.7, 1.3):
    out2 += iso_doublet_velocity(lambda k: expm(-1j*th*(Hs(k) + 0.3*Yodd)) @ rand_sym_onsite_unitary())
print(f" k-dependent-spectrum factor exp(-i th H(k)): isolated doublet speeds {np.round(out2, 4)}")
