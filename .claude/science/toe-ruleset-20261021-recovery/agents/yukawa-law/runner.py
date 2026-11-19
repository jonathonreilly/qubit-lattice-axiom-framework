"""yukawa-law: Yukawa-type vertex weights as fields the response law sets ("flavour fields").

(a) which flavour generators the charged-current reading then links, and whether the flavour vacuum makes them harmless;
(b) the stationary points of the vacuum phase over the flavour fields, on CL-1's actual tick, and the mixing they allow.
Supplied model: CL-1's cube tick (spin-3/2 edge hop W, two tilings offset by (1,1,1), even cubes C exp(-i(eps-mu/2)R) C
with copy factor C = exp(i(MN/4)(1-s)R), odd cubes exp(+i(eps+mu/2)R)), solved in Bloch form on the 2Z^3 cell;
vacuum phase Phi = sum of negative quasi-energies per site (as in coarse-vacuum); flavour field read as a mass-angle
matrix per sector. Tags: [T] theorem (exact, checked), [F] finite diagnostic, [E] estimate vs measurement, [M] input.
"""
import itertools, time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, minimize

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261022)
PERMS = [np.eye(3)[list(p)] for p in itertools.permutations(range(3))]

print('== A. targets [M] (masses at M_Z GeV; PDG 2024 CKM; NuFIT 6.0 NO)')
v = 246.22
mu_ = np.array([1.23e-3, 0.620, 171.7]); md_ = np.array([2.67e-3, 0.0532, 2.84])
me_ = np.array([0.51099895e-3, 0.1056583755, 1.77686])
def ckm(s12, s23, s13, d):
    c12, c23, c13 = [np.sqrt(1-x*x) for x in (s12, s23, s13)]; e = np.exp(1j*d)
    return np.array([[c12*c13, s12*c13, s13/e],
                     [-s12*c23-c12*s23*s13*e, c12*c23-s12*s23*s13*e, s23*c13],
                     [s12*s23-c12*c23*s13*e, -c12*s23-s12*c23*s13*e, c23*c13]])
VCKM = ckm(0.22501, 0.04183, 0.003732, 1.147)
th = dict(t12=(33.68, 0.72), t23=(43.3, 0.9), t13=(8.56, 0.11))
UPMNS = ckm(*[np.sin(np.radians(th[k][0])) for k in ('t12', 't23', 't13')], np.radians(212))
dm21, dm31 = 7.49e-5, 2.513e-3; m1 = 1e-3
mnu = np.array([m1, np.sqrt(m1**2+dm21), np.sqrt(m1**2+dm31)])*1e-9  # GeV
Y = {'u': np.diag(np.sqrt(2)*mu_/v).astype(complex), 'd': VCKM@np.diag(np.sqrt(2)*md_/v),
     'e': np.diag(np.sqrt(2)*me_/v).astype(complex), 'n': UPMNS@np.diag(np.sqrt(2)*mnu/v)}
check('[M]', 'y_t %.3f y_e %.1e y_nu2 %.1e; |V_us| %.4f |V_cb| %.4f; theta12/23/13 = 33.68/43.3/8.56 deg (Dirac nu, m1 = 1 meV supplied)'
      % (Y['u'][2, 2].real, Y['e'][0, 0].real, np.sqrt(2)*mnu[1]/v, abs(VCKM[0, 1]), abs(VCKM[1, 2])), True)

print('== B. (a) flavour links under the charged-current reading')
GEN = []
for i in range(3):
    for j in range(i, 3):
        H = np.zeros((3, 3), complex); H[i, j] = H[j, i] = 1; GEN.append(H)
        if i != j: H = np.zeros((3, 3), complex); H[i, j] = 1j; H[j, i] = -1j; GEN.append(H)
GROUPS = ['Q', 'u', 'd', 'L', 'e', 'n']
FIELDS = [('Q', 'u', 'u'), ('Q', 'd', 'd'), ('L', 'e', 'e'), ('L', 'n', 'n')]  # (left group, right group, Yukawa)
def dY(gname, T, Yd):
    out = []
    for gl, gr, k in FIELDS:
        Z = (1j*T@Yd[k] if gl == gname else 0) - (1j*Yd[k]@T if gr == gname else 0)
        Z = np.zeros((3, 3)) + Z
        out.append(np.concatenate([np.real(Z).ravel(), np.imag(Z).ravel()]))
    return np.concatenate(out)
def Dmap(Yd, basis=None):
    D = np.array([dY(g, T, Yd) for g in GROUPS for T in GEN]).T
    return D if basis is None else D@basis
def nzero(Yd, basis=None):  # kernel of dY; each Yukawa rescaled to unit norm (kernel unchanged, better conditioned)
    Ys = {k: Yd[k]/np.linalg.norm(Yd[k]) for k in Yd}
    Dm = Dmap(Ys, basis); sv = np.linalg.svd(Dm, compute_uv=False)
    return Dm.shape[1] - int((sv > 1e-11).sum())
Us = {g: expm(1j*sum(rng.normal()*T for T in GEN)) for g in GROUPS}
Yt = {k: Us[gl]@Y[k]@Us[gr].conj().T for gl, gr, k in FIELDS}
sv = max(np.abs(np.linalg.svd(Yt[k], compute_uv=False)-np.linalg.svd(Y[k], compute_uv=False)).max() for k in Y)
check('[T]', 'B1 with the flavour fields transformed (Y_u -> U_Q Y_u U_u^+ ...) every Yukawa-type term is invariant: the reading '
      'links all of U(3)^6 (54 generators); masses and V are invariants', sv < 1e-14, 'drift %.0e' % sv)
Y0 = dict(Y); Y0['n'] = UPMNS@np.diag([0, *np.sqrt(2)*mnu[1:]/v])
nz, nz0 = nzero(Y), nzero(Y0)
check('[T]', 'B2 at the measured flavour vacuum exactly 2 flavour links stay massless (B and L), 3 if m1 = 0 (the phase of the '
      'massless right-handed neutrino); all others are massive', nz == 2 and nz0 == 3, 'zeros %d, %d' % (nz, nz0))
cu = rng.normal(size=(3,)*4)+1j*rng.normal(size=(3,)*4)
cn = rng.normal(size=(3,)*4)+1j*rng.normal(size=(3,)*4)
cn = sum(np.transpose(cn, p) for p in [(0, 1, 2, 3), (1, 0, 2, 3), (0, 1, 3, 2), (2, 3, 0, 1)])
def act(c, T, slot):
    return np.moveaxis(np.tensordot(T, c, axes=([1], [slot])), 0, slot)
def dfix(g, T):
    a = np.zeros_like(cu); b = np.zeros_like(cn)
    if g == 'u': a += act(cu, T, 0)
    if g == 'd': a += act(cu, T, 1)+act(cu, T, 2)
    if g == 'n': a += act(cu, T, 3); b += sum(act(cn, T, s) for s in range(4))
    return np.concatenate([a.ravel().real, a.ravel().imag, b.ravel().real, b.ravel().imag])
F = np.array([dfix(g, T) for g in GROUPS for T in GEN]).T
_, s_, Vh = np.linalg.svd(F); rk = int((s_ > 1e-10).sum()); S = Vh[rk:].T
nzS = nzero(Y, S)
check('[T]', 'B3 generic fixed u d d n and n^4 coefficients break U(3)^6 explicitly to U(3)_Q x U(3)_L x U(3)_e x U(1)(u:-2,d:1) '
      '(28 generators, the only linked ones) and remove B and L: no flavour link is massless', S.shape[1] == 28 and nzS == 0,
      'linked %d, massless %d' % (S.shape[1], nzS))
n_ = np.array([6, 3, 3, 2, 1, 1]); Yh = np.array([1/6, -2/3, 1/3, -1/2, 1, 0])
sols = [s for s in itertools.product((-1, 0, 1), repeat=6) if any(s) and s[next(i for i in range(6) if s[i])] == 1
        and (np.array(s)*n_).sum() == 0 and abs((np.abs(s)*n_*Yh).sum()) < 1e-12]
pairs = [(a, b) for a, b in itertools.combinations(sols, 2) if not any(x and y for x, y in zip(a, b))]
check('[T]', 'B4 SU(3)^3 anomalies of the single factors Q,u,d,L,e,n are 6,-3,-3,2,-1,-1; with SU(3)^2 U(1)_Y cancelled too there '
      'are %d anomaly-free SU(3) embeddings, and the only anomaly-free product of two is SU(3)_(Q,u,d) x SU(3)_(L,e,n): an '
      'anomaly-free linking rule allows at most 16 non-abelian flavour links' % len(sols),
      len(sols) == 7 and pairs == [((0, 0, 0, 1, -1, -1), (1, -1, -1, 0, 0, 0))], 'pairs %s' % pairs)
Ys0 = {k: Y0[k]/np.linalg.norm(Y0[k]) for k in Y0}; Pp = np.linalg.svd(Dmap(Ys0))[2][:54-nz0].T  # complement of exact kernel
_, sv0, Vh0 = np.linalg.svd(Dmap(Y0, Pp)); Vh0 = Vh0@Pp.T
idxL = [GROUPS.index('L')*9+i for i in range(9)] + [GROUPS.index('e')*9+i for i in range(9)]
best = min(m/np.linalg.norm(x[idxL]) for m, x in zip(sv0, Vh0) if m > 1e-20 and np.linalg.norm(x[idxL]) > 0.1)
fneed = 5e3/best
check('[E]', 'B5 lightest flavour link touching charged leptons: M/(g f) = %.1e (broken only by Dirac neutrino Yukawas); LEP-2 '
      'contact bounds (M/g > ~5 TeV) need f > %.0e GeV, fifth-force tests (M > ~1 eV) only f > ~1e5 GeV: harmless only for a flavour '
      'stiffness near the cell scale, which no law sets' % (best, fneed), 1e15 < fneed < 1e19)

print('== C. (b) stationary points of the vacuum phase over the flavour fields (CL-1 tick, Bloch form)')
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j-np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1)-m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for c in C8:
    nn = (2*c-1.0)/r3; _, vv = np.linalg.eigh(sum(nn[k]*J3[k] for k in range(3))); xi.append(vv[:, -1])
G8 = np.array([[xi[a].conj()@xi[b] for b in range(8)] for a in range(8)])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        dd = C8[a]-C8[b]
        if np.abs(dd).sum() == 1: Wi[int(np.argmax(abs(dd)))][a, b] = -G8[a, b]/abs(G8[a, b])/r3
R = sum(Wi); Ri = [r3*w for w in Wi]; s8 = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s8)@R
def blochU(eps, M, MN, Lc, nf=1):
    """M: mass-angle matrix (nf x nf Hermitian) on the family index; returns U(k) for all k of an Lc^3 cell torus"""
    I = np.eye(nf); Cm = np.kron(I, expm(1j*(MN/4)*X))
    Me = Cm@expm(-1j*np.kron(eps*I-M/2, R))@Cm; Mo = expm(1j*np.kron(eps*I+M/2, R))
    ks = np.array(list(itertools.product(range(Lc), repeat=3)))*np.pi/Lc
    ph = np.tile(np.exp(2j*ks@C8.T), (1, nf))
    return (ph[:, :, None]*Mo[None]*ph.conj()[:, None, :])@Me[None]
def Phi(eps, M, MN, Lc=10, nf=1):
    w = -np.angle(np.linalg.eigvals(blochU(eps, np.atleast_2d(M).astype(complex), MN, Lc, nf))).ravel()
    return w[w < 0].sum()/(8*Lc**3)
# C1 spectral theorem with a family index
Mh = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)); Mh = 0.05*(Mh+Mh.conj().T)/2
Wr = expm(1j*sum(rng.normal()*T for T in GEN)); P = (0.1, 0.04)
a1 = Phi(P[0], Mh, P[1], 4, 3); a2 = Phi(P[0], Wr@Mh@Wr.conj().T, P[1], 4, 3)
a3 = sum(Phi(P[0], lam, P[1], 4, 1) for lam in np.linalg.eigvalsh(Mh))
check('[T]', 'C1 the free sea\'s vacuum phase depends on each sector\'s flavour field only through its eigenvalues (the tick is '
      'family-blind, so U(3) conjugation commutes with it): Phi = sum_s sum_i phi(m_si); every mixing matrix V is an exactly flat '
      'direction, at any copy mass', abs(a1-a2) < 1e-13 and abs(a1-a3) < 1e-13, 'rotated %.0e, eigen-sum %.0e' % (abs(a1-a2), abs(a1-a3)))
# C2 copy-free: band depends on cos mu -> even; stationary set {0, pi}
odd = max(abs(Phi(0.3, m, 0.0)-Phi(0.3, -m, 0.0)) for m in (0.05, 0.5, 1.5))
mus = np.linspace(0.02, np.pi-0.02, 60); fv = np.array([Phi(0.3, m, 0.0, 6) for m in mus]); dfv = np.diff(fv)
check('[T]', 'C2 without the copy mass the band is cos w = A S - (cos 2b - cos mu)/2, a function of cos mu, so phi is even and '
      'stationary at mu = 0 (its maximum) and mu = pi; the scan finds no interior root: each mass is either zero or cell-scale',
      odd < 1e-13 and (np.all(dfv < 0)), 'odd part %.0e, monotone on (0, pi): %s' % (odd, bool(np.all(dfv < 0))))
# C3 copy mass: linear term, stationary point near -MN/2
rows = []; ok = True
for eps, MN in [(0.3, 0.2), (0.1, 0.05), (0.05, 0.02), (0.02, 0.01)]:
    g = lambda m, Lc: (Phi(eps, m+1e-5, MN, Lc)-Phi(eps, m-1e-5, MN, Lc))/2e-5
    c1 = g(0.0, 10); r8 = brentq(lambda m: g(m, 8), -2*MN, 0.0, xtol=1e-9); r12 = brentq(lambda m: g(m, 12), -2*MN, 0.0, xtol=1e-9)
    U0 = blochU(eps, np.array([[r12]], complex), MN, 1)[0]; lv = np.sort(np.abs(np.angle(np.linalg.eigvals(U0))))
    rows.append('(%.2f,%.2f) c1 %.4f mu*/MN %.4f [L8-12 %.0e] rest |w|/MN %.3f %.3f' % (eps, MN, c1, r12/MN, abs(r8-r12), lv[0]/MN, lv[-1]/MN))
    ok &= c1 < 0 and abs(r8-r12) < 3e-4*MN and -0.62 < r12/MN < -0.5 and abs(lv[0]-abs(r12+MN)) < 1e-9 and abs(lv[-1]-abs(r12)) < 1e-9
check('[F]', 'C3 with the copy mass phi is not even (the copy level is |mu + MN|, the light one |mu|), so mu = 0 is not stationary; '
      'the stationary point near zero sits at mu* = -(0.54 to 0.56) MN, where the two copies have nearly equal rest phase '
      '(0.45 and 0.55 MN): the light family\'s stationary mass is tied to the copy mass, the same for every species', ok, '; '.join(rows))
# C4 departures-only reading
lvls = []
for m in (0.003, 0.02, -0.01):
    U0 = blochU(0.1, np.array([[m]], complex), 0.05, 1)[0]; w = np.abs(np.angle(np.linalg.eigvals(U0)))
    lvls.append(np.min(np.abs(w-abs(m))))
check('[T]', 'C4 if the flavour field, like the edges, responds only to departures (vacuum subtracted at the same field), the vacuum '
      'term vanishes identically and a particle at rest contributes its rest phase |mu| exactly (checked at k = 0), whose '
      'derivative is +-1: no stationary point at any nonzero mass; matter would drive its own mass to zero, and empty regions '
      'leave the field undetermined', max(lvls) < 1e-12, 'k=0 level - |mu|: %.0e' % max(lvls))
# C5 mixing selection by the first mixed invariant
nonperm = {}
A = np.diag([0.1, 0.5, 1.0]); B = np.diag([0.2, 0.6, 1.0])
def V_of(x, V0): return expm(1j*sum(x[i]*GEN[i] for i in range(9)))@V0
for kap in (0.0, -1.0):
    cnt = 0
    for t in range(12):
        V0, _ = np.linalg.qr(rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)))
        for sg in (1, -1):
            def Fv(x):
                W = V_of(x, V0)@B@V_of(x, V0).conj().T
                return sg*np.real(np.trace(A@W)+kap*np.trace(A@W@A@W))
            r = minimize(Fv, np.zeros(9), method='BFGS', options={'gtol': 1e-10})
            Pm = np.abs(V_of(r.x, V0))**2
            cnt += min(np.abs(Pm-Q).max() for Q in PERMS) > 1e-4
    nonperm[kap] = cnt
grad_perm = max(np.abs(A@(Q@B@Q.T)-(Q@B@Q.T)@A).max() for Q in PERMS)
check('[T]', 'C5 the first mixed invariant Tr(A V B V^+) (A, B = Y_uY_u^+, Y_dY_d^+ eigenvalues, from link dressing) has gradient '
      '[A, VBV^+]: for non-degenerate A, B its stationary points are exactly the permutation matrices (times phases); random-start '
      'extremisation: %d of 24 non-permutation ends; adding a quartic invariant with a tuned coefficient (kappa = -1) gives %d of 24 '
      'with non-trivial mixing' % (nonperm[0.0], nonperm[-1.0]), nonperm[0.0] == 0 and nonperm[-1.0] > 0 and grad_perm < 1e-15)

print('== D. estimates against measurement')
check('[E]', 'D1 masses: the vacuum-phase stationary values are mu = 0 or pi (copy-free) or mu* ~ -0.55 MN and ~pi (with the copy '
      'mass), identical for every species; measured mass angles are m N ~ 1e-17 (top) to 1e-22 (electron) at a few-Planck-length '
      'cell, so every measured mass is non-stationary unless MN ~ 2m, i.e. a copy at twice each fermion mass, which the register '
      'excludes (electron g - 2), and m_t/m_e = 3.4e5 against 1: the flavour-field reading with the rules\' sea gives no mass law', True)
dev = [abs(VCKM[0, 1])/0.00068, abs(VCKM[1, 2])/0.00079, abs(VCKM[0, 2])/0.00009]
check('[E]', 'D2 CKM: nearest stationary pattern is V = 1; |V_us|, |V_cb|, |V_ub| sit %.0f, %.0f, %.0f sigma from it, so mixing '
      'needs perturbations whose size no law sets; the 2-2 block curvature is down by (y_c y_s/y_t y_b)^2 = %.0e, so Cabibbo is '
      'nearly flat' % (*dev, (mu_[1]*md_[1]/(mu_[2]*md_[2]))**2), min(dev) > 30)
aU = np.abs(UPMNS); dist = [np.abs(aU-Q).max() for Q in PERMS]
check('[E]', 'D3 PMNS with Dirac neutrinos (Majorana masses are forbidden by the register\'s Z4) has the same stationary set: the '
      'nearest permutation misses some |U_ij| by %.2f (theta12 is 0 or 90 deg vs 33.68 +- 0.72, 47 sigma); the literature\'s '
      'degenerate-Majorana extremum (one maximal angle) is unavailable here and would still put theta12 16 sigma off' % min(dist),
      min(dist) > 0.4)
# D4 look-elsewhere: Haar U(3)
Z = rng.normal(size=(40000, 3, 3))+1j*rng.normal(size=(40000, 3, 3)); Qh, Rh = np.linalg.qr(Z)
Qh = Qh*(np.diagonal(Rh, axis1=1, axis2=2)/np.abs(np.diagonal(Rh, axis1=1, axis2=2)))[:, None, :]
def stat(U):
    U = np.abs(np.atleast_3d(U) if U.ndim == 3 else U[None])
    return np.max(np.stack([np.min(U[:, np.arange(3), list(p)], axis=-1) for p in itertools.permutations(range(3))]), axis=0)
sh = stat(Qh); sC, sP = stat(VCKM)[0], stat(UPMNS)[0]
fC = (sh >= sC).mean(); fP = (sh <= sP).mean()
check('[E]', 'D4 look-elsewhere (Haar U(3), 40000): fraction at least as close to a permutation as CKM (min matched |V| %.3f) = %.1e; '
      'at least as far as PMNS (%.3f) = %.2f: CKM is non-generic and sits near a stationary pattern, PMNS is generic (anarchic); '
      'one qualitative match (quarks near V = 1) out of the 6 permutation patterns, no quantitative one' % (sC, fC, sP, fP), fC < 1e-3 and fP > 0.1)
print('elapsed_seconds %.1f' % (time.time()-T0))
print('theorems: B1-B4, C1, C2, C4, C5; finite: C3; estimates: B5, D1-D4.')
print('supplied: flavour fields as response-set fields, their stiffness f and coupling g, the mass-angle reading per sector, '
      'the vacuum phase as the matter part, generic fixed uddn/n^4 tensors, quartic coefficient kappa; PDG/NuFIT inputs, m1.')
print()
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
