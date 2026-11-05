AUDIT_INPUT_PATHS = ('docs/NO_STRUCTURE_OF_THE_UPDATE_PROTECTS_A_DARK_SPECIES_BECAUSE_THE_MIRROR_NUMBER_IS_SHARED_AT_EVERY_MOMENTUM_THE_BLOCK_PERIOD_BLOCKS_NO_COPY_DECAY_AND_THE_WINDOW_FLOOR_HOLDS_NO_ATOM_OR_REMNANT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""dm-from-structure: a dark-matter species protected by structure the laws already have (no added parity)?
 A  (a) a conserved charge of the update carried by no light state: mirror X with the light-mirror pairing, at every K
 B  (b) copy-sign states at rest: is their decay suppressed by the window / block structure? (Floquet umklapp)
 C  (c) a minimum-size 'atom' of geometry at the window floor; gravitational bound states against the floor
 D  (d) black-hole remnants stopped by the floor: mass, stability, abundance from measured A_s, n_s
Supplied: (b, mu, M) = (0.3, 0.4, 0.5) per tick, diagonal metric weights; mirror pair-square phase group U(1)_Y x U(1)_X
(cited, mirror-dark-matter); register s = 2, Delta = 0 for the tetrahedron register; b_e (>= ~40, register); unit map
a = sqrt(8 pi) l_P, 1 rad/tick = 2.1e18 GeV; A_s, n_s, delta_c, g*, T_eq. Seeded (numpy default_rng(20261022)).
"""
import itertools, os, signal, time
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from math import comb
import numpy as np
from scipy.linalg import expm
from scipy import sparse
from scipy.sparse.linalg import expm_multiply
from scipy import ndimage
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
# ---------------- CL-1 cube tick (law text; face phase -1 is this overlap field up to a site gauge)
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def coh(nv):
    th, ph = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0])
    return np.array([np.sqrt(comb(3, k))*np.cos(th/2)**(3-k)*np.sin(th/2)**k*np.exp(1j*(k-1.5)*ph) for k in range(4)])
XI = [coh((2*c - 1)/np.sqrt(3)) for c in CORN]; Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for s_, t_ in itertools.product(range(8), repeat=2):
    d = np.abs(CORN[s_] - CORN[t_])
    if d.sum() == 1:
        g = XI[s_].conj()@XI[t_]; Wax[int(np.argmax(d))][s_, t_] = -g/abs(g)/np.sqrt(3)
Ri = [np.sqrt(3)*w for w in Wax]; I8 = np.eye(8); G5 = 1j*Ri[0]@Ri[1]@Ri[2]
def R(c):
    c = np.asarray(c, float); return sum(ci*X for ci, X in zip(c, Ri))/np.sqrt((c**2).sum())
lab = lambda x: 4*(x[0] % 2) + 2*(x[1] % 2) + x[2] % 2
def We_of(c, mu_, M_, b_=0.3):
    e = np.pi/2 - b_; Rc = R(c); sc = G5@Rc; Cm = expm(1j*(M_/4)*(I8 - sc)@Rc); return Cm@expm(-1j*(e - mu_/2)*Rc)@Cm
def bloch(b_, mu_, M_, K, c=(1, 1, 1)):
    e = np.pi/2 - b_; Rc = R(c); s = G5@Rc; We = We_of(c, mu_, M_, b_); Wo = expm(1j*(e + mu_/2)*Rc); Uo = np.zeros((8, 8), complex)
    st = [np.array([1, 1, 1]) + cc for cc in CORN]
    for xa in st:
        for xb in st:
            Uo[lab(xa), lab(xb)] += Wo[lab(xa), lab(xb)]*np.exp(1j*np.dot(K, xa//2 - xb//2))
    return Uo, We, s
def nul(mats, n=8):
    A = np.vstack([np.kron(np.eye(n), X) - np.kron(X.T, np.eye(n)) for X in mats])
    return int((np.linalg.svd(A, compute_uv=False) < 1e-9).sum())
b, mu, M = 0.3, 0.4, 0.5
lP, cc, hb = 1.616255e-35, 2.99792458e8, 6.582119569e-25; a_cell = np.sqrt(8*np.pi)*lP; tau = 2*a_cell/(np.sqrt(3)*cc); E1 = hb/tau
MPl, Mbar, gram_per_GeV = 1.22089e19, 2.435e18, 1.78266e-24
print("== A. (a) a conserved charge carried by no light state?")
Kc = np.pi*np.ones(3); Kd = 0.7*np.ones(3); Kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)]
dims = {nm: nul(list(bloch(b, mu, M, K)[:2])) for nm, K in (('K=0', np.zeros(3)), ('corner pi(1,1,1)', Kc), ('diag 0.7(1,1,1)', Kd), ('random', Kr[0]))}
allK = []; [allK.extend(bloch(b, mu, M, K)[:2]) for K in [np.zeros(3), Kc, Kd] + Kr]; dall = nul(allK)
check("A1 [F] one-body commutant of the cube tick at single K and jointly (K = 0, corner, diagonal, 3 random): a charge kept for moving states must commute at every K; only the identity (species number) does",
      dall == 1 and dims['K=0'] > 1, ', '.join(f"{k} {v}" for k, v in dims.items()) + f"; joint {dall}")
Y6 = sp.Matrix([[1, -4, 2, -3, 6, 0]]); X6 = sp.Matrix([[1, 1, -3, -3, 1, 5]])   # 6Y and X = 5(B-L) - 4Y on (Q, u^c, d^c, L, e^c, nu^c)
nsp = sp.Matrix.vstack(Y6, X6).nullspace(); Cm_rows = []
for v in nsp:
    den = sp.ilcm(*[sp.fraction(x)[1] for x in v]); w = v*den; gg = sp.igcd(*[int(x) for x in w]); Cm_rows.append([int(x)//gg for x in w])
Cm = sp.Matrix(Cm_rows); snf_m = smith_normal_form(Cm, domain=sp.ZZ); inv_m = [abs(snf_m[i, i]) for i in range(min(snf_m.shape))]
Z6 = sp.zeros(Cm.rows, 6)
def group_info(C, n):   # phases theta in T^n with C theta = 0 mod 2pi: free rank and torsion from the Smith normal form
    S = smith_normal_form(C, domain=sp.ZZ); inv = [abs(S[i, i]) for i in range(min(S.shape)) if S[i, i] != 0]
    return n - len(inv), [d_ for d_ in inv if d_ > 1]
Cmir = sp.Matrix.hstack(Z6, Cm); Llock = sp.Matrix.hstack(sp.eye(6), sp.zeros(6, 6))   # dark subgroup: trivial on every light mode
r0, t0 = group_info(sp.Matrix.vstack(Cmir, Llock), 12)
res = []
for nm, sgn in (('psi^dag psi\'', -1), ('psi psi\'', 1)):
    Bl = sp.Matrix.hstack(sp.eye(6), sgn*sp.eye(6)); rg, tg_ = group_info(sp.Matrix.vstack(Cmir, Bl), 12); rd, td = group_info(sp.Matrix.vstack(Cmir, Bl, Llock), 12)
    res.append((nm, rg, tg_, rd, td))
check("A2 [T] species phases, light 16 + mirror 16 (mirror pair-square group U(1)_Y x U(1)_X, cited): with NO pairing the dark subgroup (trivial on light modes) is U(1)^2; with A1's light-mirror pairing (either form) it is trivial and the group is Y, X(total)",
      all(x == 1 for x in inv_m) and r0 == 2 and not t0 and all(r[1] == 2 and not r[2] and r[3] == 0 and not r[4] for r in res),
      f"no pairing: dark rank {r0} torsion {t0}; " + '; '.join(f"{r[0]}: group rank {r[1]}, dark rank {r[3]} torsion {r[4]}" for r in res))
Xl = [1, 1, -3, -3, 1, 5]
check("A3 [T] every light mode has X = 1 mod 4 and i^N = exp(i pi X/2): U(1)_X and its Z4 are carried by light states (lightest carrier: the neutrino, X = -3); CL-1's species numbers are carried by each light copy at rest",
      all(x % 4 == 1 for x in Xl) and all(abs(1j**(1) - np.exp(1j*np.pi*x/2)) < 1e-12 for x in Xl))
print("== B. (b) copy-sign states at rest: does the block / window structure suppress their decay?")
Uo, We, s = bloch(b, mu, M, np.zeros(3)); c0 = np.abs(s@Uo - Uo@s).max(); Ug, _, sg = bloch(b, mu, M, Kr[1]); cg = np.abs(sg@Ug - Ug@sg).max()
w, V = np.linalg.eig(Uo@We); sv = np.array([(V[:, k].conj()@s@V[:, k]).real for k in range(8)]); ph = np.angle(w)
check("B1 [F] the copy sign commutes with the tick at K = 0 only (rest phases mu + M for s = -1, mu for s = +1)", c0 < 1e-12 and cg > 1e-2 and np.allclose(np.abs(ph[sv < 0]), mu + M) and np.allclose(np.abs(ph[sv > 0]), mu),
      f"||[s,Uo]|| {c0:.0e} at K=0, {cg:.3f} at random K")
def pos(K, which):
    Uo_, We_, _ = bloch(b, mu, M, K); w_, V_ = np.linalg.eig(Uo_@We_); p_ = np.angle(w_); o = [i for i in np.argsort(p_) if p_[i] > 0]
    return np.linalg.qr(V_[:, o[:2] if which == 'light' else o[2:]])[0]
H0 = pos(np.zeros(3), 'heavy'); X = We_of((1, 1, 1), mu, M).conj().T@(We_of(np.array([1., 1, 1]) + 1e-7*np.array([1, 1, -2]), mu, M) - We_of((1, 1, 1), mu, M))/1e-7
dirs = [v/np.linalg.norm(v) for v in rng.normal(size=(6, 3))]; amp = {f: max(np.linalg.norm(pos(f*M*d_, 'light').conj().T@X@H0, 2) for d_ in dirs) for f in (0.0, 0.1, 0.87)}
check("B2 [F] traceless one-cube strain vertex heavy(rest) -> light(q): zero at q = 0, O(1) at a real decay's recoil q = 0.87 M (recomputes dark-matter-candidate A6)", amp[0.0] < 1e-7 and amp[0.87] > 0.2,
      f"amp q=0 {amp[0.0]:.0e}, 0.1M {amp[0.1]:.3f}, 0.87M {amp[0.87]:.3f}")
g1 = amp[0.87]; nk = 8; ks = 2*np.pi*np.arange(nk)/nk - np.pi; lo, hi = [], []
for K in itertools.product(ks, repeat=3):
    Uk, Wk, _ = bloch(b, mu, M, np.array(K)); p_ = np.sort(np.angle(np.linalg.eigvals(Uk@Wk))); pp = p_[p_ > 0]; lo.append(pp[0]); hi.append(pp[1])
Wl = max(hi) - min(lo)
bes = [40, 100, 1000]
check("B3 [T+F] a block half-tick is b_e cube half-ticks and edges repeat every b_e cells, so quasienergy is kept only mod 2 pi/b_e per tick and momentum mod 2 pi/b_e; the light band (8^3) and M exceed 2 pi/b_e for b_e >= 40, so the folded light band covers the circle: no kinematic block on heavy -> light + edge quanta",
      all(Wl > 2*np.pi/be and M > 2*np.pi/be for be in bes), f"light band [{min(lo):.3f}, {max(hi):.3f}] width {Wl:.3f}; 2pi/b_e = " + ', '.join(f"{2*np.pi/be:.4f}" for be in bes))
tg = lambda m: hb/(g1**2*m**3/(32*np.pi*Mbar**2)); mg = (hb*32*np.pi*Mbar**2/(g1**2*8e18))**(1/3)
check("B4 [E] graviton width g^2 M^3/(32 pi Mbar^2) at the O(1) vertex: at the law's M (one constant, all species) tau << 1 s; tau > 8e18 s needs M < ~0.1 GeV, excluded by a heavy electron copy",
      tg(M*E1) < 1e-30 and mg < 1.0, f"M = {M*E1:.1e} GeV: tau = {tg(M*E1):.0e} s; tau(1 TeV) = {tg(1e3):.0e} s; tau > 8e18 s needs M < {mg*1e3:.0f} MeV")
print("== C. (c) a minimum-size atom of geometry at the window floor; gravitational bound states")
sr, Dl = 2, 0; nl = (4 + Dl)*sr + 1; fac = (2.0**(np.arange(nl)/sr - 3))**2
def cm_ok(L2):
    a_, b_, c_, d_, e_, f_ = L2; g12, g13, g23 = (a_ + b_ - d_)/2, (a_ + c_ - e_)/2, (b_ + c_ - f_)/2
    det = a_*(b_*c_ - g23**2) - g12*(g12*c_ - g23*g13) + g13*(g12*g23 - b_*g13)
    return (a_ > 0) & (a_*b_ - g12**2 > 1e-12) & (det > 1e-12)
flat = [2]*6; L2 = [flat[k]*fac.reshape([nl if j == k else 1 for j in range(6)]) for k in range(6)]
ok = np.broadcast_to(cm_ok(L2), (nl,)*6).copy(); labs, ncomp = ndimage.label(ok, structure=ndimage.generate_binary_structure(6, 1))
nflat = (3*sr,)*6; floor = (0,)*6; comp = labs == labs[nflat]; idx = -np.ones((nl,)*6, int); pts = np.argwhere(comp); idx[tuple(pts.T)] = np.arange(len(pts)); D = len(pts)
rows, cols = [], []
for k in range(6):
    sh = pts.copy(); sh[:, k] += 1; inb = sh[:, k] < nl; tgt = np.full(D, -1); tgt[inb] = idx[tuple(sh[inb].T)]; m_ = tgt >= 0
    rows += list(np.arange(D)[m_]); cols += list(tgt[m_])
Hh = sparse.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(D, D)).tocsr(); Hh = Hh + Hh.T
check("C1 [F] tetrahedron register (s = 2, Delta = 0, regular): the all-floor state (every edge 1/8 of flat) lies in the one positive-volume component with the flat state: no frozen floor geometry",
      ncomp == 1 and comp[floor] and comp[nflat], f"{int(ok.sum())}/{nl**6} positive-volume states, {ncomp} component, D = {D}")
psi0 = np.zeros(D, complex); psi0[idx[floor]] = 1.0; nsum = pts.sum(1); shell = nsum <= 2
V0 = ((pts - 3*sr)**2).sum(1)/sr**2; P = expm_multiply(-1j*Hh, psi0, start=0, stop=200, num=201, endpoint=True)
retc = (np.abs(P[50:, idx[floor]])**2).mean(); shc = (np.abs(P[50:][:, shell])**2).sum(1).mean()
P = expm_multiply(-1j*(Hh + sparse.diags(V0)).tocsr(), psi0, start=0, stop=200, num=201, endpoint=True); retb = (np.abs(P[50:, idx[floor]])**2).mean()
check("C2 [F] pure register hop: the floor state leaves the floor (mean return and floor-shell weight, sum n <= 2, over t = 50..200 << 1)",
      retc < 0.1 and shc < 0.2, f"return {retc:.1e}, shell {shc:.1e}")
fq = {}
for lam in (0.25, 0.5, 1.0, 2.0, 3.0, 2*np.pi):   # the update's own form: hop, then departure phase lam*V0 per block tick (phase mod 2 pi)
    phs = np.exp(-1j*lam*V0); psi = psi0.copy(); r_ = []
    for _ in range(200):
        psi = phs*expm_multiply(-1j*Hh, psi); r_.append(abs(psi[idx[floor]])**2)
    fq[lam] = np.mean(r_[50:])
check("C3 [F] a stiff departure cost (quadratic bowl about flat) traps the floor state in continuous time (energy isolation, no number), but in the update's per-tick form the phase folds mod 2 pi: return <= 0.3 over the scan and < 0.1 at lam >= 2: no robust floor atom",
      retb > 0.3 and max(fq.values()) < 0.3 and all(v < 0.1 for k, v in fq.items() if k >= 2), f"continuous lam 1: {retb:.2f}; per-tick: " + ', '.join(f"{k:.2f}:{v:.3f}" for k, v in fq.items()))
nn = np.arange(0, 41); s5 = 5
check("C4 [T] passing: a split fires at mean edge value 4s (twice flat) and each child edge is the parent value minus s, exactly half the length: children start at flat, so the split cascade makes no floored cells",
      np.allclose(2.0**((nn - s5)/s5 - 3), 0.5*2.0**(nn/s5 - 3), rtol=1e-15, atol=0))
lfl = {be: be*a_cell/8 for be in bes}; mB = {be: (2*lP/lfl[be])**(1/3) for be in bes}   # m in M_Pl units with r_B = 2 l_P M_Pl^3/m^3 >= l_floor
check("C5 [T+E] gravitational atom (r_B = 2 l_P (M_Pl/m)^3) is resolved above the floor edge b_e a/8 only for m < (2 l_P/l_floor)^(1/3) M_Pl; its constituents must already be stable and dark: no new protection",
      all(mB[be] < 1 for be in bes), ', '.join(f"b_e {be}: l_floor {lfl[be]/lP:.0f} l_P, m < {mB[be]:.2f} M_Pl" for be in bes))
print("== D. (d) remnants stopped by the floor")
Mrem = {be: lfl[be]/(2*lP) for be in bes}   # r_s = 2 G M = l_floor, in M_Pl units
TH = {be: MPl/(8*np.pi*Mrem[be]) for be in bes}
check("D1 [T+E] r_s = 2GM = l_floor = b_e a/8 gives M_rem = (b_e sqrt(8 pi)/16) M_Pl; b_e is only bounded below, so the mass is supplied; T_H there is below the block band top pi/b_e: emission is not band-cut before the floor",
      all(TH[be] < np.pi*E1/be for be in bes), ', '.join(f"b_e {be}: {Mrem[be]:.1f} M_Pl = {Mrem[be]*MPl*gram_per_GeV:.1e} g, T_H {TH[be]:.0e} vs {np.pi*E1/be:.0e} GeV" for be in bes))
Kl = 9; hop = np.diag(np.ones(Kl - 1), 1) + np.diag(np.ones(Kl - 1), -1); nd = np.diag(np.arange(Kl, dtype=float))
check("D2 [T] an edge register keeps nothing (commutant of {hop, value} = 1) and the floor is connected to flat (C1): a floor-size lump carries no number; the floor removes the horizon rather than stopping the loss",
      nul([hop, nd], Kl) == 1 and ncomp == 1, f"register commutant {nul([hop, nd], Kl)}")
As, ns, dc, gst, Teq = 2.1e-9, 0.9649, 0.45, 106.75, 0.8e-9   # GeV
be = 40; Mi = Mrem[be]; Tf = MPl*np.sqrt(1/(2*1.66*np.sqrt(gst)*Mi))   # radiation era, M_H = M_Pl^2/(2H)
kf = 2.35e-13*1.66*np.sqrt(gst)*Tf/MPl*1.5637e38; lnk = np.log(kf/0.05)   # a_f H_f in Mpc^-1 over the pivot 0.05/Mpc (g* entropy factor dropped)
bneed = (Teq/Tf)*(Mi/Mrem[be])*0.84; s2_flat = 16/81*As; s2_tilt = s2_flat*np.exp((ns - 1)*lnk)
lnb_flat, lnb_tilt = -dc**2/(2*s2_flat), -dc**2/(2*s2_tilt); Pneed = dc**2/(2*(-np.log(bneed)))*81/16
check("D3 [E] holes of M_i ~ M_rem form at T_f; remnants as all dark matter need beta ~ (T_eq/T_f)(M_i/M_rem); measured A_s (n_s = 1, or the tilt carried down) gives ln beta <= -2.4e8; the needed power is ~1e6 A_s: abundance supplied",
      lnb_flat < -1e8 and Pneed/As > 1e5, f"b_e 40: T_f {Tf:.1e} GeV, ln(k_f/k*) {lnk:.0f}, beta needed {bneed:.1e}; ln beta (n_s=1) {lnb_flat:.2e}, (tilt) {lnb_tilt:.2e}; P_R needed {Pneed:.1e} = {Pneed/As:.0e} A_s")
print("verdict: (a) no charge outside light charges (A1-A3); (b) no kinematic suppression (B3), tau ~4e-39 s at the law's M (B4); (c) no floor atom (C1-C3),")
print("  none from splits (C4), bound states inherit constituents (C5); (d) remnant mass supplied by b_e, no number protects it (D2), beta ~exp(-2.4e8) (D3).")
print("GATE: no rule proposed passes. A 'floor lock' rule (a fully floored cube is not lowered/raised) would bend Admissibility/Record,")
print("  supply its mass through b_e and its abundance through supplied small-scale power: FAIL (items 1, 3). Dark matter stays open.")
print("theorems: A2, A3, B3, C4, D2; finite: A1, B1, B2, C1-C3; estimates: B4, C5, D1, D3")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
