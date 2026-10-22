AUDIT_INPUT_PATHS = ('docs/THE_COPY_SIGN_IS_EXACT_ONLY_AT_REST_AND_NO_COPY_EDGE_OR_SPLIT_STRUCTURE_OF_THE_CANDIDATE_LAWS_GIVES_A_STABLE_COLD_LINK_FREE_SPECIES_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""dark-matter-candidate: is there a stable, cold, link-free species in CL-1..CL-3 (no axiom edits)?
 A  copy sector: the s = -1 copy of CL-1's cube tick (copy sign, copy mass), its charges, what conserves it
 B  nu^c: the only link-free Weyl state of one chiral family; Z4 of B - L and its masses
 C  edge registers: any conserved register number?
 D  split and geometry defects: is there a topological charge in the edge configuration space or the passing?
 E  estimates against measurement (supplied inputs named) and ranking
Supplied: (b, mu, M) = (0.3, 0.4, 0.5) per tick, diagonal metric weights, flat equal edges unless stated; one chiral
family's charge table (hand-entered); register step s = 2 and Delta = 0, 1 for the exhaustive tetrahedron scan;
unit map a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c). Seeded (numpy default_rng(20261022)).
"""
import itertools, os, signal, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm
from scipy import ndimage
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
# ------------------------------------------------ CL-1 cube tick (law text): spin-3/2 overlap hop, copy sign, copy mass
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def coh(nv):
    th, ph = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0])
    return np.array([np.sqrt(comb(3, k)) * np.cos(th/2)**(3-k) * np.sin(th/2)**k * np.exp(1j*(k-1.5)*ph) for k in range(4)])
XI = [coh((2*c - 1)/np.sqrt(3)) for c in CORN]; Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for s_, t_ in itertools.product(range(8), repeat=2):
    d = np.abs(CORN[s_] - CORN[t_])
    if d.sum() == 1:
        g = XI[s_].conj() @ XI[t_]; Wax[int(np.argmax(d))][s_, t_] = -g/abs(g)/np.sqrt(3)
Ri = [np.sqrt(3)*w for w in Wax]; I8 = np.eye(8)
def R(c):
    c = np.asarray(c, float); return sum(ci*X for ci, X in zip(c, Ri))/np.sqrt((c**2).sum())
G5 = 1j*Ri[0]@Ri[1]@Ri[2]
lab = lambda x: 4*(x[0] % 2) + 2*(x[1] % 2) + x[2] % 2
def bloch(b, mu, M, K, c=(1, 1, 1)):
    e = np.pi/2 - b; Rc = R(c); s = G5@Rc; Cm = expm(1j*(M/4)*(I8 - s)@Rc)
    We = Cm@expm(-1j*(e - mu/2)*Rc)@Cm; Wo = expm(1j*(e + mu/2)*Rc); Uo = np.zeros((8, 8), complex)
    st = [np.array([1, 1, 1]) + cc for cc in CORN]
    for xa in st:
        for xb in st:
            Uo[lab(xa), lab(xb)] += Wo[lab(xa), lab(xb)]*np.exp(1j*np.dot(K, xa//2 - xb//2))
    return Uo, We, s
def nul(mats, n=8):
    A = np.vstack([np.kron(np.eye(n), X) - np.kron(X.T, np.eye(n)) for X in mats])
    return int((np.linalg.svd(A, compute_uv=False) < 1e-9).sum())
b, mu, M = 0.3, 0.4, 0.5
print("== A. copy sector (CL-1 cube tick with copy mass)")
cl = max(np.abs(Ri[i]@Ri[j] + Ri[j]@Ri[i] - 2*(i == j)*I8).max() for i in range(3) for j in range(3))
c0 = rng.uniform(0.6, 1.4, 3); Rc = R(c0)
check("A1 [T] R_i = sqrt3 W_i are Clifford generators, so R(c)^2 = 1 for every diagonal metric", cl < 1e-12 and np.abs(Rc@Rc - I8).max() < 1e-12, f"max dev {cl:.1e}")
Gc = max(np.abs(G5@X - X@G5).max() for X in Ri); sc = G5@Rc
check("A2 [T] G = iR1R2R3 is central in Cl(3), so s = G R commutes with R: the even half-tick and copy mass keep s at every metric",
      Gc < 1e-12 and np.abs(sc@Rc - Rc@sc).max() < 1e-12 and np.abs(sc@sc - I8).max() < 1e-12, f"[G,R_i] {Gc:.1e}")
Uo, We, s = bloch(b, mu, M, np.zeros(3)); w, V = np.linalg.eig(Uo@We)
sv = np.array([(V[:, k].conj()@s@V[:, k]).real for k in range(8)]); ph = np.angle(w)
okA3 = np.allclose(np.sort(np.abs(ph[sv < 0])), mu + M) and np.allclose(np.abs(ph[sv > 0]), mu) and (sv < 0).sum() == 4
check("A3 [F] at K = 0 the s = -1 copy (4 states) has rest phase mu + M, the s = +1 copy mu", okA3,
      f"phases s=-1 {sorted(set(np.round(np.abs(ph[sv<0]),6).tolist()))}, s=+1 {sorted(set(np.round(np.abs(ph[sv>0]),6).tolist()))}")
c0K = np.abs(s@Uo - Uo@s).max(); Kg = rng.uniform(-np.pi, np.pi, 3); Uo2, We2, s2 = bloch(b, mu, M, Kg); cgK = np.abs(s2@Uo2 - Uo2@s2).max()
cm = tuple(rng.uniform(0.7, 1.3, 3)); Uo4, We4, s4 = bloch(b, mu, M, np.zeros(3), cm); cmK = np.abs(s4@Uo4 - Uo4@s4).max()
check("A4 [F] the odd half-tick keeps s exactly at K = 0 (flat and a random diagonal metric) and not at random K: s is exact for states at rest only",
      c0K < 1e-12 and cmK < 1e-12 and cgK > 1e-2, f"||[s,Uo]|| {c0K:.0e}, {cmK:.0e} (metric) at K=0; {cgK:.3f} at random K")
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)]; cs = [(1, 1, 1), tuple(rng.uniform(0.7, 1.3, 3)), tuple(rng.uniform(0.7, 1.3, 3))]
m1 = []; [m1.extend(bloch(b, mu, M, K)[:2]) for K in Ks]; m2 = []; [m2.extend(bloch(b, mu, M, K, c)[:2]) for K in Ks for c in cs]
d0 = nul(list(bloch(b, mu, M, np.zeros(3))[:2])); d1, d2 = nul(m1), nul(m2)
check("A5 [F] cell-local charges commuting with the tick at 3 random K (and 3 metrics): only the identity (particle number)", d1 == 1 and d2 == 1, f"commutant dims: K=0 {d0}, 3 K {d1}, 3 K x 3 metrics {d2}")
def We_of(c, mu_, M_):
    e = np.pi/2 - b; Rc = R(c); sc_ = G5@Rc; Cm = expm(1j*(M_/4)*(I8 - sc_)@Rc); return Cm@expm(-1j*(e - mu_/2)*Rc)@Cm
def pos(K, which, mu_, M_):   # orthonormal basis of the two light (or two heavy) positive-phase states at K
    Uo, We, _ = bloch(b, mu_, M_, K); w, V = np.linalg.eig(Uo@We); ph = np.angle(w); o = [i for i in np.argsort(ph) if ph[i] > 0]
    return np.linalg.qr(V[:, o[:2] if which == 'light' else o[2:]])[0]
dirs = [v/np.linalg.norm(v) for v in rng.normal(size=(6, 3))]; amp = {}
for mu_, M_ in ((mu, M), (0.04, 0.05), (1e-3, 0.05)):
    H0 = pos(np.zeros(3), 'heavy', mu_, M_)
    for nm, dc in (('conformal', (1, 1, 1)), ('traceless', (1, 1, -2))):
        X = We_of((1, 1, 1), mu_, M_).conj().T@(We_of(np.array([1., 1, 1]) + 1e-7*np.array(dc), mu_, M_) - We_of((1, 1, 1), mu_, M_))/1e-7   # one-cube strain vertex
        for f in (0.0, 0.1, 0.87):
            amp[(mu_, M_, nm, f)] = max(np.linalg.norm(pos(f*M_*d_, 'light', mu_, M_).conj().T@X@H0, 2) for d_ in dirs)
gs = [amp[(m_, M_, 'traceless', 0.87)] for m_, M_ in ((mu, M), (0.04, 0.05), (1e-3, 0.05))]; g1 = min(gs)
check("A6 [F] one-cube strain vertex, heavy copy at rest -> light copy at recoil q: zero at q = 0, ~ q/M below M, O(1) at a real decay's recoil q = 0.87 M for every M (no suppression); conformal strain zero",
      max(amp[k] for k in amp if k[3] == 0.0) < 1e-7 and g1 > 0.2 and max(amp[k] for k in amp if k[2] == 'conformal') < 1e-7,
      f"amp(q=0.1M, 0.87M): M=0.5 {amp[(mu,M,'traceless',0.1)]:.3f}, {gs[0]:.3f}; M=0.05 {amp[(0.04,0.05,'traceless',0.1)]:.3f}, {gs[1]:.3f}; M=0.05 mu=1e-3 {amp[(1e-3,0.05,'traceless',0.1)]:.3f}, {gs[2]:.3f}")
# Fock: second-quantised copy sign commutes with the cube's mode number (charge = q x number, so copies share charges)
cdag = []
for j in range(8):
    op = np.array([[1.]]);
    for k in range(8):
        f = np.array([[0, 0], [1, 0.]]) if k == j else (np.diag([1., -1]) if k < j else np.eye(2)); op = np.kron(op, f)
    cdag.append(op)
Nhat = sum(cd@cd.T for cd in cdag); Shat = sum(s[i, j]*cdag[i]@cdag[j].T for i in range(8) for j in range(8))
check("A7 [T] Fock (8 cube modes, dim 256): [S_hat, N_hat] = 0, so each copy carries its species' link charges (q x number)", np.abs(Shat@Nhat - Nhat@Shat).max() < 1e-12)
print("== B. nu^c (one chiral family, hand-entered table: SU3 dim, SU2 dim, Y, B-L)")
F = {'Q': (3, 2, Fr(1, 6), Fr(1, 3)), 'u^c': (-3, 1, Fr(-2, 3), Fr(-1, 3)), 'd^c': (-3, 1, Fr(1, 3), Fr(-1, 3)),
     'L': (1, 2, Fr(-1, 2), Fr(-1)), 'e^c': (1, 1, Fr(1), Fr(1)), 'nu^c': (1, 1, Fr(0), Fr(1))}
free = [k for k, v in F.items() if v[0] == 1 and v[1] == 1 and v[2] == 0]
sing = [(a, c) for a, c in itertools.combinations_with_replacement(F, 2) if F[a][0]*F[c][0] in (1, -9) and F[a][1] == F[c][1] and F[a][2] + F[c][2] == 0]
check("B1 [T] link-free Weyl state and gauge-singlet bilinear of one family", free == ['nu^c'] and sing == [('nu^c', 'nu^c')], f"{free}, {sing}")
z4 = lambda bl: complex(1j**int(bl % 4))
check("B2 [T] Z4 = i^(B-L): nu^c nu^c odd (i^2 = -1, no Majorana mass), L H nu^c and (nu^c)^4 even", z4(2*F['nu^c'][3]) == -1 and z4(F['L'][3] + F['nu^c'][3]) == 1 and z4(4*F['nu^c'][3]) == 1)
print("== C. edge registers")
Kl = 9; hop = np.diag(np.ones(Kl - 1), 1) + np.diag(np.ones(Kl - 1), -1); nd = np.diag(np.arange(Kl, dtype=float)); par = np.diag((-1.)**np.arange(Kl))
dh, dhn = nul([hop], Kl), nul([hop, nd], Kl)
check("C1 [T] on a 9-level register {hop, value} has trivial commutant: no conserved register number (hop alone: only its own functions)", dhn == 1 and dh == Kl, f"dims {dh}, {dhn}")
check("C2 [T] the hop anticommutes with (-1)^n: no register parity", np.abs(hop@par + par@hop).max() < 1e-12)
print("== D. split and geometry defects")
P = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1.]]); ed = list(itertools.combinations(range(4), 2))
Lmap = []
for (i, j) in ed:   # squared length = e^T G e with G the 3x3 Gram matrix in the frame of vertex 0
    v = np.zeros(3); v[i - 1] -= (i > 0); v[j - 1] += 1; Lmap.append([v[0]**2, v[1]**2, v[2]**2, 2*v[0]*v[1], 2*v[0]*v[2], 2*v[1]*v[2]])
rk = np.linalg.matrix_rank(np.array(Lmap))
check("D1 [T] squared edge lengths are a linear bijection of the tetrahedron's Gram matrix (rank 6): positive volume is a convex cone, the window a box, their intersection over all tetrahedra convex, the flat vacuum manifold PD(3) contractible: no topological geometry charge", rk == 6, f"rank {rk}")
def cm_ok(L2):  # Gram matrix of edges 01, 02, 03 from squared lengths (d01,d02,d03,d12,d13,d23); positive definite <=> V > 0
    a, b_, c, d_, e, f = L2; g12, g13, g23 = (a + b_ - d_)/2, (a + c - e)/2, (b_ + c - f)/2
    det = a*(b_*c - g23**2) - g12*(g12*c - g23*g13) + g13*(g12*g23 - b_*g13)
    return (a > 0) & (a*b_ - g12**2 > 1e-12) & (det > 1e-12)
res = []
for Delta in (0, 1):
    s_reg = 2; nl = (4 + Delta)*s_reg + 1; fac = (2.0**(np.arange(nl)/s_reg - 3))**2
    for name, flat in (('corner', [1, 1, 1, 2, 2, 2]), ('central', [2]*6)):
        L2 = [flat[k]*fac.reshape([nl if j == k else 1 for j in range(6)]) for k in range(6)]; ok = cm_ok(L2); ok = np.broadcast_to(ok, (nl,)*6).copy()
        lab_, ncomp = ndimage.label(ok, structure=ndimage.generate_binary_structure(6, 1)); del lab_
        res.append((Delta, name, int(ok.sum()), nl**6, ncomp, bool(ok[(3*s_reg,)*6])))
check("D2 [F] every positive-volume tetrahedron state (s = 2, Delta = 0, 1; corner and central) joins the flat state by single register steps: no frozen geometry",
      all(r[4] == 1 and r[5] for r in res), '; '.join(f"D{r[0]} {r[1]} {r[2]}/{r[3]} in {r[4]} comp" for r in res))
nn = np.arange(0, 41); s_reg = 5
check("D3 [T] passing: a child edge at the parent's value minus s is exactly half the parent's length, so a split's children in their vacuum read the parent's geometry (zero departure, no CL-3 source)",
      np.allclose(2.0**((nn - s_reg)/s_reg - 3), 0.5*2.0**(nn/s_reg - 3), rtol=1e-15, atol=0))
print("== E. estimates against measurement (supplied: unit map, M, y, alpha_s, b_e; cited bounds approximate)")
lP, cc, hb = 1.616255e-35, 2.99792458e8, 6.582119569e-25; a = np.sqrt(8*np.pi)*lP; tau = 2*a/(np.sqrt(3)*cc); E1 = hb/tau; Mb = 2.435e18
print(f"  cell unit: 1 rad/tick = {E1:.2e} GeV (tau = {tau:.2e} s); at the supplied M = {M}: heavy copy {M*E1:.1e} GeV, recoil q ~ 1, no suppression: tau ~ 1e-42 s")
print(f"  (a) N_c = s = -1 copy of nu^c: s is exact only at rest (A2-A4) and the copy-changing vertex is O(1) at real recoil for every M (A6, g >= {g1:.2f}):")
tg = lambda m: hb/(g1**2*m**3/(32*np.pi*Mb**2))
mg = (hb*32*np.pi*Mb**2/(g1**2*8e18))**(1/3)
print(f"      graviton channel Gamma ~ g^2 M^3/(32 pi Mbar^2): tau = {tg(1e3):.0e} s at 1 TeV, {tg(1e6):.0e} s at 1e6 GeV; tau > 8e18 s (invisible) needs M < {mg*1e3:.0f} MeV,")
print("      but M is one law-text constant for every copy, and a heavy electron copy below ~100 GeV is excluded (LEP); a Yukawa leg y ~ 3e-13")
print(f"      gives Gamma ~ y^2 g^2 M/(8 pi): tau = {hb/(9e-26*g1**2*1e3/(8*np.pi)):.0e} s at 1 TeV. Excluded at every M (scope: universal M, vertex read from the edge reading).")
sm = 0.07; yfi = 0.33*2*(3e-13**2*125/(8*np.pi))*1.221e19/(106.75**1.5*125**2)
print(f"  (c) Dirac nu^c: sum m < {sm} eV -> Omega h^2 <= {sm/93.14:.1e} even if thermal, and hot; freeze-in via h -> L nu^c: Y ~ {yfi:.0e}, Omega h^2 ~ {2.74e8*0.05e-9*yfi:.0e}")
print("      heavy reading: Majorana mass Z4-odd (B2); in a Z4-breaking vacuum it decays through L H nu^c. Excluded.")
print(f"  (b) edge quanta: lowest massive root 1.49 per block tick (cited, dm-revisit) -> {1.49*E1/40:.1e} GeV (b_e = 40), {1.49*E1/100:.1e} (b_e = 100);")
print("      no number or parity (C1, C2): decays to gravitons at the cell rate. Excluded.")
print("  (d) split bubbles: children read the parent's flat geometry (D3): zero departure, no gravitating mass; no geometry charge (D1, D2);")
print("      link monopoles: stable but magnetic (cited, dm-revisit). Excluded.")
print("  ranking: 1 N' (cited dm-revisit; needs a supplied label parity) > 2 N_c (needs a supplied copy parity: then the N' case)")
print("           > 3 Dirac nu^c (hot, < 1%) > 4 edge quanta > 5 split / geometry defects. Abundance from the rules: none.")
print("theorems: A1, A2, A7, B1, B2, C1, C2, D1, D3; finite: A3, A4, A5, A6, D2; estimates: E")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
