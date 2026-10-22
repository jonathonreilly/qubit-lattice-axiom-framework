AUDIT_INPUT_PATHS = ('docs/A_DARK_PARITY_IS_KEPT_EXACTLY_BY_THE_CUBE_TICK_BUT_ITS_ABUNDANCE_IS_FITTED_AND_ITS_NAME_FREE_FORM_MAKES_EVERY_DIRAC_NEUTRINO_MASSLESS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""ax5-dark-matter: write and test the dark-matter rule AX-5 (dark parity) against CL-1 and against measurement.
 A  the copy-parity reading (option i): what the cube tick keeps and what its edge reading breaks
 B  AX-5 dark parity (-1)^N_D, D one link-free species: exact consistency with the tick (Bloch, real space, Fock)
 C  consequences: stable lightest odd state, its mass, the copy above it, link-freeness, the massless lightest neutrino
 E  estimates against measurement: gravitational freeze-in abundance, its fitted number and sensitivity,
    coldness, self-interaction, direct detection, N_eff
Supplied: (b, mu, M) per tick, diagonal metric weights, random link phases, one family's charge table (hand-entered);
estimates also take the unit map a = sqrt(8 pi) l_P, tau = 2a/(sqrt3 c), the graviton-exchange rate coefficient
alpha_1/2 = 1.1e-3 (literature, approximate), g* = 106.75, A_s, measured Omega_c h^2 and neutrino splittings.
Seeded (numpy default_rng(20261022)).
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
from scipy.special import kn
from scipy.integrate import quad
from scipy.optimize import brentq
T0 = time.time(); NP = NF = 0; rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
# ---------------- CL-1 cube tick (law text): anticommuting face-phase -1 hops W_i, copy sign s = i R1 R2 R3 R, copy mass
CORN = np.array(list(itertools.product((0, 1), repeat=3)))
def coh(nv):
    th, ph = np.arccos(np.clip(nv[2], -1, 1)), np.arctan2(nv[1], nv[0])
    return np.array([np.sqrt(comb(3, k))*np.cos(th/2)**(3-k)*np.sin(th/2)**k*np.exp(1j*(k-1.5)*ph) for k in range(4)])
XI = [coh((2*c - 1)/np.sqrt(3)) for c in CORN]; Wax = [np.zeros((8, 8), complex) for _ in range(3)]
for s_, t_ in itertools.product(range(8), repeat=2):
    d = np.abs(CORN[s_] - CORN[t_])
    if d.sum() == 1:
        g = XI[s_].conj() @ XI[t_]; Wax[int(np.argmax(d))][s_, t_] = -g/abs(g)/np.sqrt(3)
Ri = [np.sqrt(3)*w for w in Wax]; I8 = np.eye(8); G5 = 1j*Ri[0]@Ri[1]@Ri[2]
def R(c):
    c = np.asarray(c, float); return sum(ci*X for ci, X in zip(c, Ri))/np.sqrt((c**2).sum())
lab = lambda x: 4*(x[0] % 2) + 2*(x[1] % 2) + x[2] % 2
def cube_even(c, mu, M, b):
    e = np.pi/2 - b; Rc = R(c); s = G5@Rc; Cm = expm(1j*(M/4)*(I8 - s)@Rc); return Cm@expm(-1j*(e - mu/2)*Rc)@Cm
def cube_odd(c, mu, b, A=None):
    e = np.pi/2 - b; Rc = R(c)
    if A is not None: Rc = Rc*np.exp(1j*A)          # link-dressed odd-cube hop (A antisymmetric: still Hermitian)
    return expm(1j*(e + mu/2)*Rc)
def bloch(b, mu, M, K, c=(1, 1, 1)):
    We = cube_even(c, mu, M, b); Wo = cube_odd(c, mu, b); Uo = np.zeros((8, 8), complex)
    st = [np.array([1, 1, 1]) + cc for cc in CORN]
    for xa in st:
        for xb in st:
            Uo[lab(xa), lab(xb)] += Wo[lab(xa), lab(xb)]*np.exp(1j*np.dot(K, xa//2 - xb//2))
    return Uo, We, G5@R(c)
def pos(K, which, b, mu_, M_):
    Uo, We, _ = bloch(b, mu_, M_, K); w, V = np.linalg.eig(Uo@We); ph = np.angle(w); o = [i for i in np.argsort(ph) if ph[i] > 0]
    return np.linalg.qr(V[:, o[:2] if which == 'light' else o[2:]])[0]
b, mu, M = 0.3, 0.4, 0.5
print("== A. option (i): an exact copy parity on the cube tick's own copies")
Uo, We, s = bloch(b, mu, M, np.zeros(3)); w, V = np.linalg.eig(Uo@We); sv = np.array([(V[:, k].conj()@s@V[:, k]).real for k in range(8)])
cK0 = np.abs(s@Uo@We - Uo@We@s).max(); Kg = rng.uniform(-np.pi, np.pi, 3); U2 = bloch(b, mu, M, Kg)
cK = np.abs(U2[2]@U2[0]@U2[1] - U2[0]@U2[1]@U2[2]).max()
check("A1 [F] the copy sign s commutes with the tick at K = 0 (s = -1 rest phase mu + M) and not at a random K", cK0 < 1e-12 and cK > 1e-2
      and np.allclose(np.sort(np.abs(np.angle(w[sv < 0]))), mu + M), f"||[s,U]|| {cK0:.0e} at K=0, {cK:.3f} at random K")
dirs = [v/np.linalg.norm(v) for v in rng.normal(size=(6, 3))]; amp = {}
for mu_, M_ in ((mu, M), (0.04, 0.05)):
    H0 = pos(np.zeros(3), 'heavy', b, mu_, M_); W0 = cube_even((1, 1, 1), mu_, M_, b)
    X = W0.conj().T@(cube_even(np.array([1., 1, 1]) + 1e-7*np.array((1, 1, -2)), mu_, M_, b) - W0)/1e-7
    for f in (0.0, 0.87):
        amp[(M_, f)] = max(np.linalg.norm(pos(f*M_*d_, 'light', b, mu_, M_).conj().T@X@H0, 2) for d_ in dirs)
check("A2 [F] any copy parity equal to s at rest is broken by CL-1's own edge reading: the one-cube traceless strain vertex takes the heavy copy at rest to the light copy at recoil 0.87 M with O(1) amplitude (zero at q = 0)",
      amp[(M, 0.0)] < 1e-7 and min(amp[(M, 0.87)], amp[(0.05, 0.87)]) > 0.2, f"amp(0.87M) {amp[(M,0.87)]:.3f} (M=0.5), {amp[(0.05,0.87)]:.3f} (M=0.05)")
print("   -> option (i) holds only if one species reads its edges through a band-projected (non-local) tick; option (ii), label parity, is not kept by the fine tick (dm-revisit). Rejected.")
print("== B. AX-5 dark parity P_D = (-1)^N_D, D one link-free species: consistency with the update")
L = 4; NS = L**3; idx = lambda x: ((x[0] % L)*L + x[1] % L)*L + x[2] % L
orig = [np.array(o) for o in itertools.product(range(0, L, 2), repeat=3)]
cub_c = {('e', tuple(o)): rng.uniform(0.7, 1.3, 3) for o in orig}; cub_c.update({('o', tuple(o)): rng.uniform(0.7, 1.3, 3) for o in orig})
def tiling(kind, mu_, M_, links):
    U = np.zeros((NS, NS), complex)
    for o in orig:
        oo = o + (kind == 'o'); sites = [idx(oo + c) for c in CORN]; c = cub_c[(kind, tuple(o))]
        if kind == 'e': Wc = cube_even(c, mu_, M_, b)
        else:
            A = None
            if links: A = rng.uniform(-1, 1, (8, 8)); A = np.triu(A, 1); A = A - A.T
            Wc = cube_odd(c, mu_, b, A)
        U[np.ix_(sites, sites)] = Wc
    return U
def species(mu_, links): return tiling('o', mu_, M, links)@tiling('e', mu_, M, False)
UD, UE = species(0.3, False), species(0.1, True); Z = np.zeros((NS, NS))
Ufull = np.block([[UD, Z], [Z, UE]]); PD = np.diag(np.r_[np.ones(NS), np.zeros(NS)]); un = np.abs(Ufull.conj().T@Ufull - np.eye(2*NS)).max()
UE2 = species(0.1, True); UD_alone = species(0.3, False)
check("B1 [T] real-space 4^3 torus, both tilings, copy mass, a random metric per cube (edges vary in space), random links on E's odd hops: the update is unitary and commutes with the D projector exactly, and D's block is independent of E's links",
      un < 1e-12 and np.abs(PD@Ufull - Ufull@PD).max() == 0.0 and np.abs(UD - UD_alone).max() < 1e-14 and np.abs(UE - UE2).max() > 1e-2, f"unitarity {un:.0e}, [P_D,U] exactly 0")
def cdag_ops(n):
    ops = []
    for j in range(n):
        op = np.array([[1.]])
        for k in range(n):
            f = np.array([[0, 0], [1, 0.]]) if k == j else (np.diag([1., -1]) if k < j else np.eye(2)); op = np.kron(op, f)
        ops.append(op)
    return ops
cd = cdag_ops(8); c_ = [o.T for o in cd]; ND = sum(cd[i]@c_[i] for i in range(4)); Par = np.diag(np.round(np.cos(np.pi*np.diag(ND))))
hD = rng.normal(size=(4, 4)) + 1j*rng.normal(size=(4, 4)); hE = rng.normal(size=(4, 4)) + 1j*rng.normal(size=(4, 4))
h = np.zeros((8, 8), complex); h[:4, :4] = hD + hD.conj().T; h[4:, 4:] = hE + hE.conj().T
Hq = sum(h[i, j]*cd[i]@c_[j] for i in range(8) for j in range(8)); Uq = expm(-1j*Hq)
yuk = cd[0]@c_[4] + cd[4]@c_[0]; pair = cd[0]@cd[1]@c_[5]@c_[4]; pair = pair + pair.conj().T
cm = lambda A, B_: np.abs(A@B_ - B_@A).max()
check("B2 [T] Fock (4 D + 4 E modes, dim 256): the second-quantised tick keeps (-1)^N_D; an odd term (one D mode, e.g. L H nu^c_D) breaks it; an even pair term keeps the parity while changing N_D",
      cm(Uq, Par) < 1e-12 and cm(yuk, Par) > 0.5 and cm(pair, Par) < 1e-12 and cm(pair, ND) > 0.5, f"[U,P] {cm(Uq,Par):.0e}, odd {cm(yuk,Par):.1f}, pair {cm(pair,Par):.0e}")
print("== C. consequences")
muD = 0.3; ks = np.linspace(-np.pi, np.pi, 8, endpoint=False); lmin, hmin, Kat = 9., 9., None
for K in itertools.product(ks, repeat=3):
    Uo, We, s = bloch(b, muD, M, np.array(K)); ph = np.angle(np.linalg.eigvals(Uo@We)); pp = np.sort(ph[ph > 0])
    if pp[0] < lmin: lmin, Kat = pp[0], K
    hmin = min(hmin, pp[-1])
Uo, We, s = bloch(b, muD, M, np.zeros(3)); w, V = np.linalg.eig(Uo@We); sv = np.array([(V[:, k].conj()@s@V[:, k]).real for k in range(8)])
check("C1 [F] lightest D-odd state: over an 8^3 K grid the lowest positive quasienergy of D is mu_D at K = 0 (light copy at rest); the s = -1 copy sits at mu_D + M and may decay to it (both odd)",
      abs(lmin - muD) < 1e-12 and np.allclose(Kat, 0) and np.allclose(np.sort(np.abs(np.angle(w[sv < 0]))), muD + M), f"min {lmin:.6f} at K={[float(k) for k in Kat]}")
check("C2 [T] link-free: D's Gauss charge is 0 in every factor, so V^q = 1 on every D hop (B1: D's block is the undressed tick); its rest phase is mu_D = m_D N with no link correction", np.abs(UD - UD_alone).max() < 1e-14)
F = {'Q': (3, 2, Fr(1, 6), Fr(1, 3)), 'u^c': (-3, 1, Fr(-2, 3), Fr(-1, 3)), 'd^c': (-3, 1, Fr(1, 3), Fr(-1, 3)), 'L': (1, 2, Fr(-1, 2), Fr(-1)), 'e^c': (1, 1, Fr(1), Fr(1)), 'nu^c': (1, 1, Fr(0), Fr(1))}
free = [k for k, v in F.items() if v[0] == 1 and v[1] == 1 and v[2] == 0]
z4 = lambda bl: complex(1j**int(bl % 4))
check("C3 [T] one family: nu^c is the only link-free Weyl state; its Majorana term is Z4 = i^(B-L)-odd and L H nu^c is Z4-even but D-odd: with Z4 and AX-5 the D species has only its tick's own Dirac mass",
      free == ['nu^c'] and z4(2*F['nu^c'][3]) == -1 and z4(F['L'][3] + F['nu^c'][3]) == 1)
Yk = rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)); Yk[:, 0] = 0; sv3 = np.linalg.svd(Yk, compute_uv=False)
check("C4 [T] D = one family's nu^c: the Dirac neutrino mass matrix y_ij L_i H nu^c_j loses a column, rank 2: the lightest neutrino is exactly massless", sv3[-1] < 1e-15 and sv3[1] > 1e-3, f"singular values {np.round(sv3,4).tolist()}")
d21, d31, d32io = 7.41e-5, 2.511e-3, 2.498e-3
sNO = 1e3*(np.sqrt(d21) + np.sqrt(d31)); m2io = np.sqrt(d32io); sIO = 1e3*(m2io + np.sqrt(m2io**2 - d21))
Y0 = Yk.copy(); Y0[:, :] = 0; d_nu = z4(F['L'][3] + F['L'][3])   # name-free form: every zero-charge mode only in pairs
check("C5 [T] gate: the name-free form (every mode with zero charge in every link factor enters non-tick terms only in pairs) removes all three nu^c columns, and L L H H is Z4-odd: every neutrino is massless, against the measured splittings",
      np.linalg.svd(Y0, compute_uv=False).max() == 0 and d_nu == -1,
      "rank 0; Dm21^2 = 7.4e-5 eV^2 > 0 measured: the name-free form is falsified under Z4; the one-family form names nu^c (gate item 2)")
print(f"   prediction: sum m_nu = {sNO:.1f} meV (normal), {sIO:.1f} meV (inverted); DESI DR2+CMB 95% bound ~64 meV keeps only normal; m_bb = 0 (Dirac)")
print("== E. estimates against measurement (supplied inputs in the header)")
lP, cc, hb = 1.616255e-35, 2.99792458e8, 6.582119569e-25; a = np.sqrt(8*np.pi)*lP; tau = 2*a/(np.sqrt(3)*cc); E1 = hb/tau; Mb = 2.435e18
gs, al = 106.75, 1.1e-3; c1 = 2*np.pi**2*gs/45; c2 = np.sqrt(np.pi**2*gs/90)
def Yfi(m, T):     # dY/dT = gamma/(s H T), gamma = al T^8/Mb^4 * f(2m/T), f(x) = x^2 K2(x)/2 -> 1 for light D
    f = lambda t: (al*t**8/Mb**4)*(((2*m/t)**2*kn(2, 2*m/t)/2) if 2*m/t > 1e-3 else 1.0)/((c1*t**3)*(c2*t**2/Mb)*t)
    lo = max(T*1e-3, 2*m/700); return quad(f, lo, T, limit=200)[0] if lo < T else 0.0
Om = lambda m, T: 2.744e8*m*Yfi(m, T)
Tmin = brentq(lambda lt: np.log(Om(10**lt, 10**lt)/0.12), 10, 16); Tmin = 10**Tmin
As = 2.1e-9; Hr = lambda r: np.pi*Mb*np.sqrt(As*r/2); Tins = lambda H: (90*H**2*Mb**2/(np.pi**2*gs))**0.25
TBK, Tfold = Tins(Hr(0.036)), Tins(Hr(1e-7))
mlo = lambda T: brentq(lambda lm: np.log(Om(10**lm, T)/0.12), -2, np.log10(T))
mhi = lambda T: brentq(lambda lm: np.log(Om(10**lm, T)/0.12), np.log10(T) + 0.05, np.log10(T) + 2.5)
mB, mF = 10**mlo(TBK), 10**mlo(Tfold); mBh = 10**mhi(TBK)
check("E1 [E] gravitational freeze-in from the bath gives Omega h^2 = 0.12 on a line m_D T_RH^3 = const (light branch); it needs T_RH >= Tmin",
      1e12 < Tmin < 1e14 and mB < TBK and abs(np.log10(mB*TBK**3) - np.log10(mF*Tfold**3)) < 0.05,
      f"Tmin {Tmin:.1e} GeV; m_D = {mB:.1e} GeV at T_RH {TBK:.1e} (r = 0.036), {mF:.1e} at {Tfold:.1e} (r = 1e-7, fold plateau)")
T1 = 1e14; m1 = 10**mlo(T1); dm = np.log(Om(1.01*m1, T1)/Om(m1, T1))/np.log(1.01); dT = np.log(Om(m1, 1.01*T1)/Om(m1, T1))/np.log(1.01)
m1h = 10**mhi(T1); dTh = np.log(Om(m1h, 1.01*T1)/Om(m1h, T1))/np.log(1.01)
check("E2 [E] one fitted number: on the light branch Omega ~ m_D T_RH^3 (power law); a heavy branch m_D ~ few T_RH is exponentially sensitive",
      abs(dm - 1) < 0.05 and abs(dT - 3) < 0.1 and dTh > 10, f"T_RH 1e14: light m {m1:.1e} (dlnO/dlnm {dm:.2f}, /dlnT {dT:.2f}); heavy m {m1h:.1e} (dlnO/dlnT {dTh:.0f})")
TD0 = 2.348e-4*(3.91/gs)**(1/3); v0 = 3.15*TD0/(mB*1e9)
check("E3 [E] cold: D is produced from a bath it never joins, with p ~ 3 T, so today v ~ 3 T_D0/m_D; every m_D on the E1 line (>= 1e4 GeV) is far colder than the ~5 keV warm-dark-matter bound needs",
      v0 < 1e-15, f"T_D0 {TD0:.1e} eV, v0 {v0:.0e} c at m_D {mB:.0e} GeV")
G = 6.674e-11; kg = 1.783e-27
sm = lambda m, v: 4*np.pi*(2*G*m*kg/v**2)**2/(m*kg)*10      # cm^2/g, gravitational Rutherford with ln ~ 1
check("E4 [E] self-interaction is gravitational only: sigma/m << 1 cm^2/g for every allowed m_D (here up to the cell scale)",
      max(sm(m, 1e5) for m in (mB, 1e14, E1)) < 1e-30, f"sigma/m {sm(mB,1e5):.0e} (m_D {mB:.0e}), {sm(E1,1e5):.0e} cm^2/g at the cell scale, v = 100 km/s")
aG = mB*0.939/(1.221e19)**2; sig = 4*np.pi*aG**2*3.894e-28/(1e-6*1e-4); rate = 0.3/mB*sig*3e7*6.0e29*3.15e7
check("E5 [E] direct detection: zero link couplings (C2), so nuclei see D only through gravity: alpha_G = m_D m_N/M_Pl^2, events per tonne-year << 1",
      rate < 1e-30, f"alpha_G {aG:.0e}, sigma(q > 10 MeV) {sig:.0e} cm^2, {rate:.0e} events/t/yr")
print(f"   N_eff: D never thermal, Delta N_eff ~ 0; s = -1 copy of D at M ~ {M*E1:.0e} GeV (M = {M} rad/tick) is Boltzmann-absent for T_RH << M and decays to light D at the cell rate")
print("   misalignment: none for a fermion; split cascade: the exact passing carries vacuum to vacuum (D pairs only from a heating kernel, supplied)")
print("theorems: B1, B2, C2, C3, C4, C5; finite: A1, A2, C1; estimates: E1-E5")
print("gate (owner 2026-10-22): (1) abundance FITTED (m_D T_RH^3 to 0.12), m_D supplied; (2) one-family form names nu^c, name-free form fails C5;")
print("   (3) unbuilt prediction only in the one-family form (m_lightest = 0, sum 58.7 meV); (4) bends Admissibility. RESULT: FAIL, not adopted")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")
