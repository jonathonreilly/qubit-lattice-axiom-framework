AUDIT_INPUT_PATHS = ('docs/THE_GAPPED_MIRROR_KEEPS_ONLY_A_NUMBER_SHARED_WITH_LIGHT_MATTER_AND_ITS_LIGHTEST_STATE_IS_CHARGED_SO_IT_GIVES_NO_DARK_MATTER_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""mirror-dark-matter: does the symmetric-gapped (SMG) mirror 16 give a stable, neutral dark-matter state?
 A  exact symmetries of one mirror 16 + Spin(10) pair square + species-diagonal hops + SM gauging (species-phase lattice,
    Smith normal form), with and without light-mirror mixing; anomaly of the surviving number
 B  CL-1 cube tick: no cell-local one-body label (copy, turn or mirror number) commutes with the moving-state tick
 C  quantum numbers of the cell spectrum (10, 16, 45, 54): SM singlets, X, Z4; Wigner-Eckart for gauge currents
 D  atomic-limit energies from the cited so(12) Jacobi chains: which mirror state is lightest
 E  estimates against measurement (supplied inputs named; cited bounds approximate)
Supplied: one mirror 16 x 2 spin per cell, the pair square alone (smg-verify), SM embedding Y = diag(-1/3,-1/3,-1/3,1/2,1/2)
on C^5, the CL-1 tick parameters (b, mu, M) = (0.3, 0.4, 0.5), the Jacobi-chain coefficients (cited from smg-verify),
unit map and measured bounds. Seeded (numpy default_rng(20261022)).
"""
import itertools, os, signal, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb, gcd
from functools import reduce
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
from scipy.linalg import expm
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  | {detail}" if detail else ''))
def nullity(A, tol=1e-9):
    return A.shape[1] - int((np.linalg.svd(A, compute_uv=False) > tol).sum())
def lattice_group(Mint):
    """invariant phase group {theta: m.theta in Z for all rows m}: U(1)^(cols - rank) x prod Z_d (torsion of Z^cols / rows)"""
    Ms = sp.Matrix(Mint); r = Ms.rank()
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(Ms, domain=sp.ZZ); d = [abs(int(S[i, i])) for i in range(min(S.shape)) if S[i, i] != 0]
    return Ms.shape[1] - r, [x for x in d if x > 1]
# ------------------------------------------------ Spin(10) on 2^5 (Jordan-Wigner), the 16 = even occupation
n5 = 5; Zm = np.diag([1., -1]); am = np.array([[0, 1], [0, 0.]]); I2 = np.eye(2)
def kr(ms): return reduce(np.kron, ms)
A_ = [kr([Zm]*i + [am] + [I2]*(n5 - i - 1)) for i in range(n5)]
Gam = []
for i in range(n5):
    Gam += [A_[i] + A_[i].T, -1j*(A_[i] - A_[i].T)]
occ = np.array([[(s >> (n5 - 1 - i)) & 1 for i in range(n5)] for s in range(32)])
E = [s for s in range(32) if occ[s].sum() % 2 == 0]; occE = occ[E]
yv = np.array([-1/3, -1/3, -1/3, 1/2, 1/2])
Yd = (occE - 0.5)@yv; Xd = -2*(occE - 0.5).sum(1); BLd = (Xd + 4*Yd)/5
def species(o):
    k, c, w = o.sum(), o[:3].sum(), o[3:].sum()
    return {(0, 0, 0): 'nu^c', (2, 1, 1): 'Q', (2, 2, 0): 'u^c', (2, 0, 2): 'e^c', (4, 2, 2): 'd^c', (4, 3, 1): 'L'}[(k, c, w)]
SPEC = ['Q', 'u^c', 'd^c', 'L', 'e^c', 'nu^c']; spE = [species(o) for o in occE]
Cc = Gam[1]@Gam[3]@Gam[5]@Gam[7]@Gam[9]; Ci = np.linalg.inv(Cc)
cdev = max(np.abs(Cc@g@Ci + g.T).max() for g in Gam)
K = [(Cc@g)[np.ix_(E, E)] for g in Gam]
Sig = [(1j/4)*(Gam[a]@Gam[b] - Gam[b]@Gam[a]) for a in range(10) for b in range(a + 1, 10)]
SigE = [S[np.ix_(E, E)] for S in Sig]
T4 = sum(np.einsum('ab,cd->abcd', k, k) for k in K)
inv = 0.
for S in SigE:
    d = (np.einsum('ABCD,Ax->xBCD', T4, S) + np.einsum('ABCD,Bx->AxCD', T4, S) + np.einsum('ABCD,Cx->ABxD', T4, S) + np.einsum('ABCD,Dx->ABCx', T4, S))
    inv = max(inv, np.abs(d).max())
print("== A. symmetries of mirror 16 + pair square + species-diagonal hops + SM gauging")
symK = max(np.abs(k - k.T).max() for k in K)
check("A1 [T] C Gamma_a C^-1 = -Gamma_a^T; M_a = C Gamma_a on the 16 is symmetric; the quartic tensor sum_a M_a x M_a is Spin(10) invariant (45 generators)",
      cdev < 1e-12 and symK < 1e-12 and inv < 1e-12 and max(np.abs(k).max() for k in K) > 0.5, f"devs {cdev:.0e}, {symK:.0e}, {inv:.0e}")
# effective monomials of Omega = sum T[A,B,C,D] c_{A up} c_{B dn} c_{C up} c_{D dn}  (up pair {A,C}, down pair {B,D})
mon = []
for A, C in itertools.combinations(range(16), 2):
    for B, D in itertools.combinations(range(16), 2):
        co = T4[A, B, C, D] - T4[C, B, A, D] - T4[A, D, C, B] + T4[C, D, A, B]
        if abs(co) > 1e-9:
            v = np.zeros(16, int); v[[A, B, C, D]] += 1; mon.append(v)
mon = np.unique(np.array(mon), axis=0)
cs16, tor16 = lattice_group(mon)
spmat = np.array([[1 if spE[i] == s else 0 for s in SPEC] for i in range(16)])
monS = np.unique(mon@spmat, axis=0); cS, torS = lattice_group(monS)
Ysp = np.array([Fr(1, 6), Fr(-2, 3), Fr(1, 3), Fr(-1, 2), Fr(1), Fr(0)]); Xsp = np.array([1, 1, -3, -3, 1, 5]); BLsp = np.array([Fr(1, 3), Fr(-1, 3), Fr(-1, 3), -1, 1, 1])
okYX = all(sum(m*y for m, y in zip(r, Ysp)) == 0 and int(r@Xsp) == 0 for r in monS)
chkX = all(int(Xsp[SPEC.index(spE[i])]) == int(round(Xd[i])) and abs(float(Ysp[SPEC.index(spE[i])]) - Yd[i]) < 1e-12 and abs(float(BLsp[SPEC.index(spE[i])]) - BLd[i]) < 1e-12 for i in range(16))
check("A2 [T] diagonal phases of the 16 weight states keeping every pair-square monomial: U(1)^5 (the Spin(10) torus), no torsion", cs16 == 5 and tor16 == [], f"{len(mon)} monomials; continuous {cs16}, torsion {tor16}")
check("A3 [T] species phases (the commutant of SM gauging and species-diagonal hops, U(1)^6) keeping the pair square: exactly U(1)_Y x U(1)_X, X = 5(B-L) - 4Y = (1,1,-3,-3,1,5) on (Q,u^c,d^c,L,e^c,nu^c), no discrete remnant",
      cS == 2 and torS == [] and okYX and chkX, f"{len(monS)} species monomials; continuous {cS}, torsion {torS}")
dN = sorted(set(int(r.sum()) for r in monS)); B3 = np.array([1, -1, -1, 0, 0, 0]); Lsp = np.array([0, 0, 0, 1, -1, -1])
g3B = reduce(gcd, [abs(int(r@B3)) for r in monS]); gL = reduce(gcd, [abs(int(r@Lsp)) for r in monS]); dBL = set(sum(m*x for m, x in zip(r, BLsp)) for r in monS)
z4in = np.allclose(np.exp(1j*np.pi*Xd/2), 1j)
check("A4 [T] mode number N changes by 4 only (Z4 survives), and i^N = exp(i pi X/2) on every mirror state (X = 1 mod 4 per mode): the Z4 is the Spin(10) centre, inside U(1)_X; B' and L' are broken (in integer steps: only the Z3 of 3B' that colour already contains remains, L' fully), B'-L' is exact",
      dN == [4] and z4in and dBL == {0}, f"dN {dN}; 3B' -> Z{g3B}, L' -> Z{gL}; d(B-L) {[str(x) for x in dBL]}")
mult = {'Q': 6, 'u^c': 3, 'd^c': 3, 'L': 2, 'e^c': 1, 'nu^c': 1}; col = {'Q': 2, 'u^c': 1, 'd^c': 1, 'L': 0, 'e^c': 0, 'nu^c': 0}; wk = {'Q': 3, 'u^c': 0, 'd^c': 0, 'L': 1, 'e^c': 0, 'nu^c': 0}
an = {'SU3^2 X': sum(col[s]*int(Xsp[i]) for i, s in enumerate(SPEC)), 'SU2^2 X': sum(wk[s]*int(Xsp[i]) for i, s in enumerate(SPEC)),
      'Y^2 X': sum(mult[s]*Ysp[i]**2*int(Xsp[i]) for i, s in enumerate(SPEC)), 'Y X^2': sum(mult[s]*Ysp[i]*int(Xsp[i])**2 for i, s in enumerate(SPEC)),
      'X^3': sum(mult[s]*int(Xsp[i])**3 for i, s in enumerate(SPEC)), 'grav X': sum(mult[s]*int(Xsp[i]) for i, s in enumerate(SPEC))}
check("A5 [T] U(1)_X has no anomaly with SM gauge fields, itself or gravity on one 16: the mirror's X is exact, also under electroweak instantons", all(v == 0 for v in an.values()), ', '.join(f"{k} {v}" for k, v in an.items()))
# light (left 16) + mirror (right 16): mixing psi_L^dag chi_R per species conserves phi_light = phi_mirror
monLM = np.hstack([np.zeros_like(monS), monS]); mixrows = np.hstack([np.eye(6, dtype=int), -np.eye(6, dtype=int)])
c0, t0 = lattice_group(monLM); c1, t1 = lattice_group(np.vstack([monLM, mixrows]))
check("A6 [T] light + mirror: without mixing U(1)^6_light x U(1)_Y x U(1)_X^mirror (8); with any species-diagonal light-mirror bilinear only U(1)_Y x U(1)_X^total (2): mirror number then shared with light B-L",
      (c0, t0, c1, t1) == (8, [], 2, []), f"no mixing {c0} {t0}; mixing {c1} {t1}")
print("== B. CL-1 cube tick: is any one-body mirror (copy, turn) label conserved for moving states?")
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def coh(nv):
    th, ph = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0])
    return np.array([np.sqrt(comb(3, k))*np.cos(th/2)**(3 - k)*np.sin(th/2)**k*np.exp(1j*(k - 1.5)*ph) for k in range(4)])
XI = [coh((2*c - 1)/np.sqrt(3)) for c in CORN]; Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for s_, t_ in itertools.product(range(8), repeat=2):
    d = np.abs(CORN[s_] - CORN[t_])
    if d.sum() == 1:
        g = XI[s_].conj()@XI[t_]; Wax[int(np.argmax(d))][s_, t_] = -g/abs(g)/np.sqrt(3)
Ri = [np.sqrt(3)*w for w in Wax]; I8 = np.eye(8); G5 = 1j*Ri[0]@Ri[1]@Ri[2]
lab = lambda x: 4*(x[0] % 2) + 2*(x[1] % 2) + x[2] % 2
def bloch(b, mu, M, Kv):
    e = np.pi/2 - b; Rc = sum(Ri)/np.sqrt(3); s = G5@Rc; Cm = expm(1j*(M/4)*(I8 - s)@Rc)
    We = Cm@expm(-1j*(e - mu/2)*Rc)@Cm; Wo = expm(1j*(e + mu/2)*Rc); Uo = np.zeros((8, 8), complex)
    st = [np.array([1, 1, 1]) + cc for cc in CORN]
    for xa in st:
        for xb in st:
            Uo[lab(xa), lab(xb)] += Wo[lab(xa), lab(xb)]*np.exp(1j*np.dot(Kv, xa//2 - xb//2))
    return Uo, We, s
def comm_dim(mats):
    return nullity(np.vstack([np.kron(np.eye(8), X) - np.kron(X.T, np.eye(8)) for X in mats]))
Uo0, We0, s0 = bloch(0.3, 0.4, 0.5, np.zeros(3)); d0 = comm_dim([Uo0, We0])
ms = []; [ms.extend(bloch(0.3, 0.4, 0.5, rng.uniform(-np.pi, np.pi, 3))[:2]) for _ in range(3)]; d3 = comm_dim(ms)
check("B1 [F] cell-local one-body operators commuting with both half-ticks: 16-dim at K = 0 (copy sign and turn labels exact at rest), 1-dim (identity) at three random K: no mirror, copy or turn number when moving (rederives dark-matter-candidate A5)",
      d0 > 1 and d3 == 1, f"commutant dims K=0 {d0}, 3 random K {d3}")
# Nielsen-Ninomiya in a conserved sector (1D): a periodic band restricted to a conserved sector has zero net chirality
nets = []
for _ in range(20):
    cf = rng.normal(size=(2, 4)); kk = np.linspace(-np.pi, np.pi, 4001)
    Ek = sum(cf[0, j]*np.cos(j*kk) + cf[1, j]*np.sin(j*kk) for j in range(4))
    sgn = np.sign(Ek); idx = np.where(sgn[:-1]*sgn[1:] < 0)[0]; nets.append(int(np.sign(Ek[idx + 1] - Ek[idx]).sum()))
check("B2 [T] Nielsen-Ninomiya per sector (1D witness): in 20 random periodic bands right- minus left-movers at E = 0 is 0; so an exact one-body mirror number makes the light sector a lattice theory by itself, vector-like",
      all(x == 0 for x in nets), f"net chiralities {sorted(set(nets))}")
print("== C. quantum numbers of the cell spectrum (Spin(10) irreps -> SM)")
# SM generators in the spinor: E_ij = a_i^dag a_j (U(5) in so(10))
Eij = lambda i, j: A_[i].T@A_[j]
def herm_gens(idx):
    gs = []
    for i, j in itertools.combinations(idx, 2):
        gs += [Eij(i, j) + Eij(j, i), 1j*(Eij(i, j) - Eij(j, i))]
    for i, j in zip(idx[:-1], idx[1:]):
        gs.append(Eij(i, i) - Eij(j, j))
    return gs
GC, GW = herm_gens([0, 1, 2]), herm_gens([3, 4]); YS = sum(yv[i]*(Eij(i, i) - 0.5*np.eye(32)) for i in range(5)); XS = -2*sum(Eij(i, i) - 0.5*np.eye(32) for i in range(5))
SMs = GC + GW + [YS]
def vec(G):   # vector-rep matrix: [G, Gamma_c] = sum_d Gamma_d L_dc
    return np.array([[np.trace(Gam[d_]@(G@Gam[c_] - Gam[c_]@G))/32 for c_ in range(10)] for d_ in range(10)])
VS, VX = [vec(G) for G in SMs], vec(XS)
basis45 = [];
for a_, b_ in itertools.combinations(range(10), 2):
    Bm = np.zeros((10, 10)); Bm[a_, b_], Bm[b_, a_] = 1, -1; basis45.append(Bm)
B45 = np.array([m.ravel() for m in basis45]).T
basis54 = []
for a_ in range(10):
    for b_ in range(a_, 10):
        Sm = np.zeros((10, 10)); Sm[a_, b_] = Sm[b_, a_] = 1; basis54.append(Sm)
B55 = np.array([m.ravel() for m in basis54]).T
def rep(L, which):
    if which == 10: return L
    act = lambda Mx: L@Mx + Mx@L.T
    Bs = B45 if which == 45 else B55
    return np.linalg.lstsq(Bs, np.array([act(Bs[:, k].reshape(10, 10)).ravel() for k in range(Bs.shape[1])]).T, rcond=None)[0]
def sm_singlets(which):
    if which == 16:
        mats, Xm = [G[np.ix_(E, E)] for G in SMs], XS[np.ix_(E, E)]
    else:
        mats, Xm = [rep(L, which) for L in VS], rep(VX, which)
    if which == 54:   # 54 = sym traceless: exclude the invariant trace by one extra row
        mats = mats + [np.array([[1.0 if a_ == b_ else 0. for a_ in range(10) for b_ in range(a_, 10)]])]
    A = np.vstack(mats); _, s_, Vh = np.linalg.svd(A); sf = np.zeros(Vh.shape[0]); sf[:s_.size] = s_; ns = Vh[sf < 1e-9]
    xs = sorted(set((np.round(np.real(np.diag(ns.conj()@Xm@ns.T)/np.diag(ns.conj()@ns.T)), 6) + 0.).tolist())) if len(ns) else []
    return len(ns), xs
res = {w: sm_singlets(w) for w in (10, 16, 45, 54)}
check("C1 [T] SM-singlet content (colour, SU(2)_L and Y all zero): 10 none, 16 one (nu'^c, X = 5, B-L = 1), 45 two (the Y and X generators), 54 one (X = 0)",
      res[10][0] == 0 and res[16] == (1, [5.0]) and res[45][0] == 2 and res[54][0] == 1 and res[54][1] == [0.0], ', '.join(f"{w}: {r[0]} {r[1]}" for w, r in res.items()))
gens16 = [S for S in SigE]; C16 = np.kron(sum(S@S for S in gens16), np.eye(16)) + np.kron(np.eye(16), sum(S.T@S.T for S in gens16)) - 2*sum(np.kron(S, S.T) for S in gens16)
ev = np.round(np.linalg.eigvalsh(C16), 6); mul16 = sorted(np.unique(ev, return_counts=True)[1].tolist())
Sv = [vec(G) for G in Sig]; C10 = sum(np.kron(L, np.eye(10)) @ np.kron(L, np.eye(10)) + 2*np.kron(L, L) + np.kron(np.eye(10), L)@np.kron(np.eye(10), L) for L in Sv)
mul10 = sorted(np.unique(np.round(np.linalg.eigvalsh((C10 + C10.conj().T)/2), 6), return_counts=True)[1].tolist())
check("C2 [T] 16 x 16bar = 1 + 45 + 210 and 10 x 10 = 1 + 45 + 54 (Casimir multiplicities): the 45 occurs once, so in the Spin(10)-symmetric phase every gauge-current matrix element inside a 16 or 10 band is one form factor times the generator's own eigenvalue (Wigner-Eckart)",
      mul16 == [1, 45, 210] and mul10 == [1, 45, 54], f"16x16bar {mul16}; 10x10 {mul10}")
nuE = [i for i in range(16) if spE[i] == 'nu^c'][0]; T3S = 0.5*(Eij(3, 3) - Eij(4, 4)); QS = T3S + YS
nuq = [float(np.real(G[np.ix_(E, E)][nuE, nuE])) for G in (T3S, QS, YS)]
VQ, VT3 = vec(QS), vec(T3S); wq, vq = np.linalg.eigh(VQ); neut = vq[:, np.abs(wq) < 1e-9]
t3n = np.round(np.linalg.eigvalsh(neut.conj().T@VT3@neut), 6).tolist()
check("C3 [T] so nu'^c (T3 = Q = Y = 0) has zero photon and Z couplings to all orders in the mirror dynamics (charge radius, magnetic moment, anapole all vanish in the Spin(10) limit); the 10's neutral members have T3 = +-1/2: a vector Z coupling",
      np.allclose(nuq, 0) and sorted(t3n) == [-0.5, 0.5], f"nu'^c (T3,Q,Y) {nuq}; T3 on the two Q=0 states of the 10 {sorted(t3n)}")
print("== D. atomic-limit cell energies (Jacobi chains cited from smg-verify; H/g has off-diagonals beta_k)")
def chain_min(f, n):
    bk = np.sqrt([f(k) for k in range(1, n)]); return np.linalg.eigvalsh(np.diag(bk, 1) + np.diag(bk, -1))[0]
lam = {'1': chain_min(lambda k: 16*k*(9 - k)*(k + 4)*(13 - k), 9), '10': chain_min(lambda k: 16*k*(8 - k)*(k + 5)*(13 - k), 8),
       '16': chain_min(lambda k: 16*k*(8 - k)*(k + 4)*(13 - k), 8), '54': chain_min(lambda k: 16*k*(7 - k)*(k + 6)*(13 - k), 7)}
gap = {r: lam[r] - lam['1'] for r in ('10', '16', '54')}; E0 = lam['1']
check("D1 [T] chains reproduce E0 = -2 sqrt(11088 + 48 sqrt 21081) g and the gaps: 10 (spin 0, X = +-2) at 19.07 g, 16 + 16bar (spin 1/2) at 33.58 g, 54 at 42.33 g",
      abs(E0 + 2*np.sqrt(11088 + 48*np.sqrt(21081))) < 1e-9 and abs(gap['10'] - 19.0715) < 1e-3 and abs(gap['16'] - 33.5804) < 1e-3 and abs(gap['54'] - 42.330) < 1e-3,
      f"E0 {E0:.5f} g; gaps {gap['10']:.4f}, {gap['16']:.4f}, {gap['54']:.4f} g")
Db, Df = gap['10'], gap['16']; r_ = Db/Df
check("D2 [F] ordering (atomic limit): the lightest mirror excitation is the SM-charged 10 (Delta_b = 0.568 Delta_f, X = +-2, no SM singlet); the lightest SM singlet is nu'^c at Delta_f, below the two-cell 10 x 10 singlets (2 Delta_b, X = 0) and the 54 singlet (X = 0)",
      Db < Df < 2*Db < gap['54'], f"Delta_b/Delta_f {r_:.4f}; 2 Delta_b/Delta_f {2*r_:.4f}; 54/Delta_f {gap['54']/Df:.4f}")
c16 = np.real(np.trace(sum(S@S for S in SigE)))/16; c10 = np.real(np.trace(sum(L@L for L in Sv)))/10
check("D3 [F] with X exact every (X, fermion parity, SM charge) sector's lightest state is stable: nu'^c (fermion-odd, X = 5) cannot reach another 16 member (Delta X = 4 costs >= 2 Delta_b > 0) and the 10 (X = +-2) is the absolute lightest; a Casimir term lam C_Spin(10) raises the 16 faster than the 10, so it never lifts the 10 above the 16",
      2*Db > 0 and Db < Df and c16 > c10, f"C(16)/C(10) = {c16/c10:.4f}")
print("== E. estimates against measurement (supplied: unit map, freeze-out formula, sigma v ~ 4 pi kappa/m^2, bounds approximate)")
lP, hb = 1.616255e-35, 6.582119569e-25; a = np.sqrt(8*np.pi)*lP; tau = 2*a/(np.sqrt(3)*2.99792458e8); E1 = hb/tau; Mb = 2.435e18; MP = 1.22e19
def omega(m, kap, gst=106.75, g=4):
    sv = 4*np.pi*kap/m**2; xf = 20.
    for _ in range(50): xf = np.log(0.038*g/np.sqrt(gst)*MP*m*sv) - 0.5*np.log(xf)
    return 2*2.74e8*m*3.79*xf/(np.sqrt(gst)*MP*m*sv), xf
def m_for(kap):
    lo, hi = 1e2, 1e8
    for _ in range(100):
        mid = np.sqrt(lo*hi); lo, hi = (mid, hi) if omega(mid, kap)[0] < 0.12 else (lo, mid)
    return mid
m1, m01 = m_for(1.0), m_for(0.1)
print(f"  thermal freeze-out (strong annihilation, unitarity-saturating kappa = 1; kappa = 0.1): Omega h^2 = 0.12 at m = {m1/1e3:.0f} TeV ({m01/1e3:.0f} TeV)")
print(f"  law-fixed gap: smg-verify window g tau in (eps/(3.65 sqrt3), 0.0117) puts Delta_f near the cell (1 rad/tick = {E1:.1e} GeV): if ever thermal,")
print(f"    Omega h^2 >~ 0.12 (m/{m1/1e3:.0f} TeV)^2 = {0.12*(1e18/m1)**2:.0e} at 1e18 GeV (unitarity-limited; overclosure); a stable relic there needs T_RH << Delta and a supplied abundance Y m = 4.4e-10 GeV")
g1 = 0.30/np.sqrt(2); tg = lambda m: hb/(g1**2*m**3/(32*np.pi*Mb**2))
print(f"  with the tick's light-mirror mixing (B1; vertex O(1) at recoil, dark-matter-candidate A6 g >= 0.30, quasi-particle weight 1/2):")
print(f"    nu'^c -> nu^c + graviton: tau ~ {tg(1.5e3):.0e} s at 1.5 TeV, {tg(m1):.0e} s at {m1/1e3:.0f} TeV, {tg(1e18):.0e} s at 1e18 GeV; DM needs > 1e26 s")
print(f"    (> 8e18 s invisible) -> m < {((hb*32*np.pi*Mb**2/(g1**2*8e18))**(1/3))*1e3:.0f} MeV, against the mirror's >= 1.5 TeV (mirror-condensate-ew): excluded at every gap")
sZ = (1.1664e-5**2*0.939**2/(8*np.pi))*(0.59)**2*0.3894e-27
print(f"  if a mirror number were supplied: the stable 10's neutral complex doublet member couples to Z (C3): sigma_n ~ {sZ:.0e} cm^2 vs ~1e-46 (m/TeV) cm^2 (LZ-type,")
print(f"    approximate): excluded below m ~ {sZ/1e-46:.0e} TeV; charged members (Q = +-1, colour triplets) are stable CHAMPs/heavy hadrons")
print(f"  nu'^c itself: Z/photon couplings zero (C3), induced at O(alpha/4pi) by Spin(10)-breaking gauge loops; self-interaction 4 pi/m^3 = {4*np.pi/m1**3*2.18e-4:.0e} cm^2/g at {m1/1e3:.0f} TeV (bound ~1)")
print("  N_eff: no massless mirror state, so Delta N_eff = 0 below Delta (massless far layers: 2.25); empty start -> T_RH << Delta if stable")
print("theorems: A1-A6, B2, C1-C3, D1; finite: B1, D2, D3; estimates: E. cited: chains (smg-verify), copy vertex g (dark-matter-candidate)")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
