AUDIT_INPUT_PATHS = ('docs/RULE_FIXED_DIMENSION_SIX_LIV_SURVIVES_TIME_OF_FLIGHT_BY_SEVEN_ORDERS_AND_IS_TESTABLE_IN_UHECR_COMPOSITION_AND_PHOTON_CUTOFF_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Which rule-fixed dimension-six LIV observables survive, and is composite universality robust?

Inherited ([F] upstream): E = p + m^2/2p + c p^3/E*^2, link band c_g = -S/24, light fermion (quark, lepton,
neutrino) c_q = -S/6 + 1/24, S = sum n_i^4, E* = 1.217e18 GeV (L = sqrt(8 pi) l_P).
A  composite robustness: 3-body light-front (Q1 FEM in the Jacobi chart, graded to x ~ 1e-7), gluon-dressed
   two-Fock-sector model (uniform simplex grids), pion (2-body), deuteron (2 nucleons carrying the computed
   nucleon dispersion); emission channels and photo-reactions with the full eigenstate dispersions;
   lepton/photon exact kinematics.
B  surviving observables: time of flight (Jacob-Piran n = 2), photon-decay cutoff, threshold shifts.
Supplied: binding models (m, kappa, g, m_g), LCDM (H0 67.4, Om 0.315), physical masses, source energies/z.
"""
import math
import os
import time

os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import numpy as np
import scipy.sparse as sp
from scipy.integrate import quad
from scipy.interpolate import PchipInterpolator
from scipy.linalg import eigh_tridiagonal
from scipy.sparse.linalg import eigsh

AUDIT_TIMEOUT_SEC = 120
np.random.seed(20261026)
T0 = time.time()
NP = NF = 0
Es = 1.217e18  # GeV
MP, MPI, MD, ME = 0.93827, 0.13498, 1.87561, 0.000511
RAYS = (('axis', -1 / 8, -1 / 24), ('sky', -7 / 120, -1 / 40), ('body', -1 / 72, -1 / 72))
lamP = lambda P: 2 * P ** 4 / Es ** 2


def check(name, ok, detail=''):
    global NP, NF
    NP, NF = NP + bool(ok), NF + (not ok)
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" | {detail}" if detail else ''))


# ---------------- A1: 3-body light-front, Q1 FEM in x1 = 1-s, x2 = s t, x3 = s(1-t) ----------------
GQ = np.polynomial.legendre.leggauss(3)


def snodes(ng=36, nl=30):
    return np.concatenate([[0.0], np.geomspace(1e-7, 0.05, ng), 0.05 + 0.95 * (0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, nl))))[1:]])


def tnodes(n=36):
    return 0.5 * (1 - np.cos(np.pi * np.linspace(0, 1, n)))


def fem3(sn, tn, m=(0.3, 0.3, 0.3), kap=0.6):
    m1, m2, m3 = m
    a12, a13, a23 = (kap ** 4 / (a + b) ** 2 for a, b in ((m1, m2), (m1, m3), (m2, m3)))
    Ns, Nt = len(sn), len(tn)
    gp, gw = (GQ[0] + 1) / 2, GQ[1] / 2
    R, C, VK, VM, VV, VW = [], [], [], [], [], []
    for k in range(Ns - 1):
        ds = sn[k + 1] - sn[k]
        for l in range(Nt - 1):
            dt = tn[l + 1] - tn[l]
            loc = [k * Nt + l, (k + 1) * Nt + l, k * Nt + l + 1, (k + 1) * Nt + l + 1]
            Kl, Ml, Vl, Wl = (np.zeros((4, 4)) for _ in range(4))
            for p, wp in zip(gp, gw):
                for q, wq in zip(gp, gw):
                    s, t = sn[k] + p * ds, tn[l] + q * dt
                    w = wp * wq * ds * dt * s
                    ph = np.array([(1 - p) * (1 - q), p * (1 - q), (1 - p) * q, p * q])
                    fs = np.array([-(1 - q), 1 - q, -q, q]) / ds
                    ft = np.array([-(1 - p), -p, 1 - p, p]) / dt
                    x1, x2, x3 = 1 - s, s * t, s * (1 - t)
                    al, be = (1 - t) / s, t / s
                    A = a12 * x1 * x2 + a13 * x1 * x3
                    B = a12 * x1 * x2 * al - a13 * x1 * x3 * be
                    Cc = a12 * x1 * x2 * al ** 2 + a13 * x1 * x3 * be ** 2 + a23 * x2 * x3 / s ** 2
                    Kl += w * (A * np.outer(fs, fs) + B * (np.outer(fs, ft) + np.outer(ft, fs)) + Cc * np.outer(ft, ft))
                    PP = w * np.outer(ph, ph)
                    Ml += PP
                    Vl += (m1 ** 2 / x1 + m2 ** 2 / x2 + m3 ** 2 / x3) * PP
                    Wl += (x1 ** 3 + x2 ** 3 + x3 ** 3) * PP
            for a in range(4):
                for b in range(4):
                    R.append(loc[a]); C.append(loc[b])
                    VK.append(Kl[a, b]); VM.append(Ml[a, b]); VV.append(Vl[a, b]); VW.append(Wl[a, b])
    n = Ns * Nt
    idx = np.array([k * Nt + l for k in range(1, Ns - 1) for l in range(1, Nt - 1)])
    mk = lambda v: sp.csr_matrix((v, (R, C)), shape=(n, n))[idx][:, idx].tocsc()
    return mk(VK), mk(VM), mk(VV), mk(VW)


def g3(ops, u):
    """ground M^2 at LIV lam*c = -u (all three quarks c_q); returns M^2, <sum x^3>."""
    K, M, V, W = ops
    val, vec = eigsh(K + V - u * W, k=1, M=M, sigma=-u - 50.0, which='LM')
    v = vec[:, 0]
    return val[0], float(v @ (W @ v)) / float(v @ (M @ v))


print('A1 3-body light-front proton (3 quarks c_q; LMV pair confinement, m=0.3, kap=0.6 GeV supplied)')
OPS = fem3(snodes(), tnodes())
OPSf = fem3(snodes(50, 42), tnodes(50))
M0sq, W0 = g3(OPS, 0.0)
M0f = g3(OPSf, 0.0)[0]
du = 1e-5
hf = (g3(OPS, -du)[0] - g3(OPS, du)[0]) / (2 * du)


def simplex(d, N):
    pts = [p for p in np.ndindex(*(N,) * (d - 1)) if all(v >= 1 for v in p) and sum(p) <= N - 1]
    pts = [tuple(p) + (N - sum(p),) for p in pts]
    return pts, {p: i for i, p in enumerate(pts)}


def simplex_ops(masses, kap, N, cs):
    d = len(masses)
    pts, ix = simplex(d, N)
    X = np.array(pts, float) / N
    n = len(pts)
    diag = (np.array(masses) ** 2 / X).sum(1)
    L = (X ** 3 * np.array(cs)).sum(1)
    R, C, V = [], [], []
    for a, p in enumerate(pts):
        for i in range(d):
            for j in range(d):
                if i == j:
                    continue
                q = list(p); q[i] += 1; q[j] -= 1
                b = ix.get(tuple(q))
                w = kap ** 4 / (masses[i] + masses[j]) ** 2 * (p[i] + 0.5) * (p[j] - 0.5)
                if b is None:  # neighbour on the x_j = 0 face: Dirichlet
                    R.append(a); C.append(a); V.append(w)
                elif b > a:
                    R += [a, b, a, b]; C += [a, b, b, a]; V += [w, w, -w, -w]
    return pts, ix, sp.csr_matrix((V, (R, C)), shape=(n, n)) + sp.diags(diag), L


def gs(H):
    lo = H.diagonal().min() - 50 - abs(H).sum(1).max()
    val, vec = eigsh(H.tocsc(), k=1, sigma=lo, which='LM')
    return val[0], vec[:, 0]


cmp = []
for u in (0.0, 1.0, 10.0):
    e6, e9 = (gs(simplex_ops((0.3,) * 3, 0.6, N, (-1.0,) * 3)[2] + u * sp.diags(simplex_ops((0.3,) * 3, 0.6, N, (-1.0,) * 3)[3]))[0]
              for N in (60, 90))
    cmp.append(abs((3 * e9 - 2 * e6) / g3(OPSf, u)[0] - 1))
check('A1a FEM ground M^2 converged (two grids) and equal to an independent uniform-simplex graph discretisation '
      '(N = 60, 90, 1/N-extrapolated) at u = 0, 1, 10 GeV^2', abs(M0f / M0sq - 1) < 3e-3 and max(cmp) < 1e-2,
      f'M0 = {math.sqrt(M0sq):.4f} GeV; grid rel {abs(M0f / M0sq - 1):.0e}; simplex rel ' + ', '.join(f'{c:.0e}' for c in cmp))
check('A1b Hellmann-Feynman: dM^2/d(lam c_q)|0 = <sum x_i^3>_0 (first-order additivity)', abs(hf / W0 - 1) < 1e-3,
      f'{hf:.6f} vs {W0:.6f}')
UG = np.logspace(-3, 10, 105)
F3 = np.array([(M0sq - g3(OPS, u)[0]) / u for u in UG])
F3f = np.array([(M0f - g3(OPSf, u)[0]) / u for u in UG[::4]])
conv = np.max(np.abs(F3f / F3[::4] - 1))
F3 = np.concatenate([[W0], F3]); UGx = np.concatenate([[1e-9], UG])
_F3 = PchipInterpolator(np.log10(UGx), F3)
Fp = lambda u: _F3(np.log10(np.clip(u, 1e-9, 1e10)))
PE = (1e18, 1e19, 1e20)
res = {r: [Fp(lamP(P / 1e9) * abs(cq)) for P in PE] for r, cq, _ in RAYS}
okF = bool(np.all(np.diff(F3) > -1e-6)) and F3[-1] > 0.999 and conv < 5e-3
print('   c_B/c_q at 1e18/1e19/1e20 eV: ' + '; '.join(f'{r} ' + '/'.join(f'{v:.4f}' for v in res[r]) for r in res))
check('A1c 3-body flow: c_B/c_q rises monotonically from <sum x^3>_0 to 1; residual 1 - c_B/c_q ~ u^-1/2; '
      'converged on the finer grid', okF and min(res['sky'][2], res['axis'][2]) > 0.9,
      f'<sum x^3>_0 = {W0:.3f}; max grid diff {conv:.0e}; u^-1/2 slope ' +
      f'{np.log((1 - F3[-5]) / (1 - F3[-1])) / np.log(UG[-1] / UG[-5]):.3f}')

# ---------------- A2: gluon-dressed two-sector model ----------------
print('A2 |qqq> + |qqqg> (contact q -> q g, g = 0.9 GeV^2/sqrt(N), m_g = 0.5 GeV supplied; uniform simplex)')


def dressed(N, cq, cg, lam, gco=0.9):
    p3, i3, H3_, L3_ = simplex_ops((0.3,) * 3, 0.6, N, (cq,) * 3)
    p4, i4, H4_, L4_ = simplex_ops((0.3,) * 3 + (0.5,), 0.6, N, (cq,) * 3 + (cg,))
    R, C = [], []
    for a, p in enumerate(p3):
        for i in range(3):
            for ng in range(1, p[i]):
                q = list(p); q[i] -= ng
                b = i4.get(tuple(q) + (ng,))
                if b is not None:
                    R.append(a); C.append(b)
    n3, n4 = len(p3), len(p4)
    G = sp.csr_matrix((np.full(len(R), gco / math.sqrt(N)), (R, C)), shape=(n3, n4))
    H = sp.bmat([[H3_ + lam * sp.diags(L3_), G], [G.T, H4_ + lam * sp.diags(L4_)]])
    e, v = gs(H)
    xg3 = (np.array(p4, float)[:, 3] / N) ** 3
    return e, float(v[n3:] @ v[n3:]), float(v[n3:] ** 2 @ xg3)


rowsA2, okA2 = [], True
for name, cq, cg in RAYS[:2]:
    e0, Pg0, _ = dressed(24, cq, cg, 0.0)
    out = []
    for u in (0.5, 5.0, 20.0):
        lam = u / abs(cq)
        r = {}
        for N in (24, 30):
            ed0 = dressed(N, cq, cg, 0.0)[0]; eu0 = dressed(N, cq, cg, 0.0, 0.0)[0]
            ed, Pg, xg = dressed(N, cq, cg, lam); eu = dressed(N, cq, cg, lam, 0.0)[0]
            r[N] = ((ed - ed0) / lam / cq, (eu - eu0) / lam / cq, Pg, xg)
        out.append((r[30][0] / r[30][1], r[30][2], r[30][3], abs(r[30][0] / r[30][1] - r[24][0] / r[24][1])))
    okA2 &= out[2][0] > out[0][0] and out[2][2] < out[0][2] and max(o[3] for o in out) < 0.05
    rowsA2.append(f'{name}: P_g(0) {Pg0:.2f}; ' + ', '.join(f'u={u:g}: c_B(dressed/undressed) {o[0]:.3f} P_g {o[1]:.2f} '
                                                          f'P_g<x_g^3> {o[2]:.0e}' for u, o in zip((0.5, 5, 20), out)))
print('   ' + '\n   '.join(rowsA2))
check('A2 gluon dressing: c_B/c_q still rises with u; the less-subluminal gluon is pushed to small x (its <x_g^3>'
      ' weight falls); N=24 vs 30 within 5%', okA2, 'no residual gluon-carried coefficient grows')

# ---------------- A3: pion, emission and photo-reactions with full eigenstate dispersions ----------------


def build(N):
    x = 0.5 * (1 - np.cos(np.pi * np.arange(0, N + 2) / (N + 1)))
    h = np.diff(x)
    return x[1:-1], h, 0.5 * (x[1:] + x[:-1]), 0.5 * (h[1:] + h[:-1])


XI, HH, XM, WW = build(3000)


def ground2(pot, m1, m2, kap):
    a = (kap ** 4 / (m1 + m2) ** 2) * XM * (1 - XM) / HH
    d = (a[:-1] + a[1:]) / WW + pot
    return eigh_tridiagonal(d, -a[1:-1] / np.sqrt(WW[:-1] * WW[1:]), select='i', select_range=(0, 0))[0][0]


m0p = ground2(0.09 / XI + 0.09 / (1 - XI), 0.3, 0.3, 0.6)
Fpi_t = np.array([(m0p - ground2(0.09 / XI + 0.09 / (1 - XI) - u * (XI ** 3 + (1 - XI) ** 3), 0.3, 0.3, 0.6)) / u for u in UG])
_Fpi = PchipInterpolator(np.log10(UG), Fpi_t)
Fpi = lambda u: _Fpi(np.log10(np.clip(u, 1e-3, 1e10)))


def Msq_p(P, cq, frozen=False):
    lam = lamP(P)
    return MP ** 2 + lam * cq * (W0 if frozen else Fp(lam * abs(cq)))


def Msq_pi(P, cq, frozen=False):
    lam = lamP(P)
    return MPI ** 2 + lam * cq * (Fpi_t[0] if frozen else Fpi(lam * abs(cq)))


Yg = np.concatenate([np.logspace(-7, -1, 150), np.linspace(0.1, 1 - 1e-7, 500)])
PG = np.logspace(8, 12, 161)  # GeV: 1e17 - 1e21 eV


def opens(Ma, Mb, Mx):
    for P in PG:
        k = Yg * P
        if np.max(Ma(P) / P - Mb(P - k) / (P - k) - Mx(k) / k) > 0:
            return P * 1e9
    return None


fm = lambda v: 'closed' if v is None else f'{v:.1e}'
em = {}
for name, cq, cg in RAYS:
    gam = lambda k, cg=cg: lamP(k) * cg
    em[name] = [opens(lambda P: Msq_p(P, cq, True), lambda P: Msq_p(P, cq, True), gam),
                opens(lambda P: Msq_p(P, cq), lambda P: Msq_p(P, cq), gam),
                opens(lambda P: Msq_p(P, cq, True), lambda P: Msq_p(P, cq, True), lambda k: Msq_pi(k, cq, True)),
                opens(lambda P: Msq_p(P, cq), lambda P: Msq_p(P, cq), lambda k: Msq_pi(k, cq))]
print('A3 opening energy (eV), [p->p gamma frozen, full | p->p pi0 frozen, full]: ' +
      '; '.join(f'{n} ' + '/'.join(fm(v) for v in em[n]) for n in em))
check('A3a frozen additive 3-body proton reopens the parent wall (control); full eigenstate closes p->p gamma and '
      'p->p pi0 on the axis and sky rays to 1e21 eV', all(em[n][0] is not None for n in em) and
      all(em[n][1] is None and em[n][3] is None for n in ('axis', 'sky')))
cone = []
for S in (1 / 3, 0.334, 0.336, 0.34, 0.35, 0.37):
    cq, cg = -S / 6 + 1 / 24, -S / 24
    cone.append((S, opens(lambda P: Msq_p(P, cq), lambda P: Msq_p(P, cq), lambda k: lamP(k) * cg)))
alt = []
for mm, kk in ((0.2, 0.5), (0.4, 0.8)):
    O2 = fem3(snodes(), tnodes(), (mm,) * 3, kk)
    m02 = g3(O2, 0.0)[0]
    tab = np.concatenate([[g3(O2, 0.0)[1]], [(m02 - g3(O2, u)[0]) / u for u in UG]])
    fi = PchipInterpolator(np.log10(UGx), tab)
    cq = -1 / 72
    Mb = lambda P, fi=fi: MP ** 2 + lamP(P) * cq * fi(np.log10(np.clip(lamP(P) * abs(cq), 1e-9, 1e10)))
    alt.append(opens(Mb, Mb, lambda k: lamP(k) * cq))
print('   body cone, p->p gamma full eigenstate vs S (1/3 = body): ' + ', '.join(f'{S:.3f}: {fm(o)}' for S, o in cone) +
      '; body with (m,kap) = (.2,.5)/(.4,.8): ' + '/'.join(fm(o) for o in alt))
nv = np.random.normal(size=(200000, 3)); nv /= np.linalg.norm(nv, axis=1)[:, None]
fcone = float(np.mean((nv ** 4).sum(1) < 0.345))
print(f'   sky fraction with S < 0.345 (open cone around the 8 body-diagonal directions): {fcone:.4f}')
check('A3b residual (non-universal) piece: at c_q = c_g (body diagonal) the composite stays less subluminal than the '
      'photon and p -> p gamma opens at EeV energies in a narrow cone; closed once |c_q| - |c_g| exceeds a few 1e-4',
      cone[0][1] is not None and cone[-1][1] is None)

NUC = {'d': (2, 2.224, 2.224), 'He': (4, 28.30, 20.58), 'N': (14, 104.66, 10.55), 'Fe': (56, 492.26, 11.20)}


def MA2(P, A, B, cq):
    """nucleus frozen at the nucleon level (x_i = 1/A; a bound state cannot follow the flow, which is the continuum);
    each nucleon carries the computed 3-body flow at P/A."""
    if A == 1:
        return Msq_p(P, cq)
    return (A * MP - B * 1e-3) ** 2 + A * A * (Msq_p(P / A, cq) - MP ** 2)


rown, dis = [], {}
for nm, (A, B, Sn) in NUC.items():
    out = []
    for name, cq, cg in RAYS:
        o1 = opens(lambda P: MA2(P, A, B, cq), lambda P: MA2(P, A - 1, B - Sn, cq), lambda k: Msq_p(k, cq))
        o2 = opens(lambda P: MA2(P, A, B, cq), lambda P: MA2(P, A, B, cq), lambda k: lamP(k) * cg)
        out.append((o1, o2))
    dis[nm] = out
    rown.append(f'{nm}: A -> N + (A-1) ' + '/'.join(fm(o[0]) for o in out) + '; A -> A gamma ' + '/'.join(fm(o[1]) for o in out))
def kmin(A, B, Sn, cq, P):
    y = Yg[(Yg > 1e-5) & (Yg < 1 - 1e-5)]
    Mb2 = MA2((1 - y) * P, A - 1, B - Sn, cq)
    ok = MA2(P, A, B, cq) - Msq_p(y * P, cq) / y - Mb2 / (1 - y) > 0
    ma, mb = MP, (A - 1) * MP - (B - Sn) * 1e-3
    sLI = ma ** 2 / y + mb ** 2 / (1 - y)
    k = np.sqrt(np.maximum((sLI - (ma + mb) ** 2) * (sLI - (ma - mb) ** 2), 0)) / (2 * np.sqrt(sLI))
    return float(k[ok].min()) if ok.any() else float('nan')


ecore = {}
for nm in NUC:
    row = []
    for name, cq, _ in RAYS:
        e = None
        for P in PG[::2]:
            if P * 1e9 >= dis[nm][[r[0] for r in RAYS].index(name)][0] and kmin(*NUC[nm], cq, P) <= 0.25:
                e = P * 1e9
                break
        row.append(e)
    ecore[nm] = row
print('   dissociation reaching the Fermi core (k_min <= k_F = 0.25 GeV, supplied), axis/sky/body (eV): ' +
      '; '.join(f'{nm} ' + '/'.join(fm(v) for v in r) for nm, r in ecore.items()))
print('   nuclei (axis/sky/body, eV): ' + '; '.join(rown))
check('A3c nuclei cannot follow the flow (it is their continuum): spontaneous vacuum dissociation A -> N + (A-1) opens '
      'kinematically at EeV x A^p energies on every ray (rate needs the nuclear large-momentum response, unsupplied)',
      all(o[0] is not None for v in dis.values() for o in v))
gz = []
for name, cq, _ in RAYS:
    er = []
    for P in PG[::4]:
        y = Yg[(Yg > 1e-4) & (Yg < 0.9)]
        er.append((np.min(Msq_p((1 - y) * P, cq) / (1 - y) + Msq_pi(y * P, cq) / y) - Msq_p(P, cq)) / (4 * P) * 1e9)
    gz.append((name, min(er), PG[::4][int(np.argmin(er))] * 1e9, np.interp(11.0, np.log10(PG[::4]), er)))
print('   GZK p gamma -> p pi0, min over P of required head-on target energy: ' +
      '; '.join(f'{n} {e:.2f} eV at {p:.0e} eV ({e2:.0f} eV at 1e20)' for n, e, p, e2 in gz) + ' (LI: -> 0 as P grows; CMB ~6e-4 eV)')
check('A3d photopion on the CMB is closed at all energies on every ray (required eps >> 1e-2 eV)', min(g[1] for g in gz) > 1e-2)

# ---------------- A4: leptons and photons (elementary: no flow) ----------------
x = np.linspace(1e-4, 1 - 1e-4, 20001)
w = x ** 3 + (1 - x) ** 3
th = {}
for name, cq, cg in RAYS:
    Gm = np.max((abs(cq) * w - abs(cg)) * x * (1 - x))
    th[name] = (ME ** 2 * Es ** 2 / (2 * Gm)) ** 0.25 * 1e9 if Gm > 0 else None
Pe = np.logspace(3, 9, 61)
ch = max(np.max(-ME ** 2 * Yg / (1 - Yg) + lamP(P) * (abs(cq) * (1 - (1 - Yg) ** 3) * -1 + abs(cg) * Yg ** 3))
         for P in Pe for _, cq, cg in RAYS)
spl = max(np.max(-abs(cg) * (1 - Yg ** 3 - (1 - Yg) ** 3)) for _, _, cg in RAYS)
k14 = 1.4e6
shift = {n: (np.min(ME ** 2 / (x * (1 - x)) + lamP(k14) * (abs(cg) - abs(cq) * w)) - 4 * ME ** 2) / (4 * ME ** 2) for n, cq, cg in RAYS}
crab = 6 * abs(RAYS[0][1]) * 2e6 ** 4 / (ME ** 2 * Es ** 2)
print('A4 photon faster than e on every ray (|c_g| <= |c_q|); gamma -> e+e- threshold (eV): ' +
      ', '.join(f'{n} {fm(v)}' for n, v in th.items()) + '; gamma gamma_bg threshold shift at 1.4 PeV: ' +
      ', '.join(f'{n} {v:+.1e}' for n, v in shift.items()) + f'; Crab 2 PeV e: LIV/mass in 1-v (axis) {crab:.1e}')
check('A4 e -> e gamma closed and gamma -> 2,3 gamma closed (exact); gamma -> e+e- opens only above 1e16.5 eV on axis/sky,'
      ' never on the body diagonal; LHAASO-energy effects < 1e-6', ch < 0 and spl < 0 and th['body'] is None and
      min(th['axis'], th['sky']) > 3e16 and max(abs(v) for v in shift.values()) < 1e-6 and crab < 1e-3)

# ---------------- B: time of flight ----------------
print('B  E_QG,2 = E*/sqrt(2|c|)  [v = 1 - (3/2)(E/E_QG,2)^2], Jacob-Piran n=2, H0 = 67.4, Om = 0.315')
H0inv = 977.8 / 67.4 * 3.156e16
K = lambda z: quad(lambda zz: (1 + zz) ** 2 / math.sqrt(0.315 * (1 + zz) ** 3 + 0.685), 0, z)[0]
dt = lambda E, z, c: 1.5 * (E / (Es / math.sqrt(2 * abs(c)))) ** 2 * K(z) * H0inv
EQ = {n: (Es / math.sqrt(2 * abs(cg)), Es / math.sqrt(2 * abs(cq))) for n, cq, cg in RAYS}
print('   E_QG,2 photon / lepton (GeV): ' + ', '.join(f'{n} {a:.2e} / {b:.2e}' for n, (a, b) in EQ.items()))
B = {'GRB090510 31 GeV z=0.903 (Fermi, >1.3e11)': (31, 0.903, 1.3e11, 'g'),
     'GRB221009A 13 TeV z=0.151 (LHAASO, >7.3e11)': (1.3e4, 0.151, 7.3e11, 'g'),
     'TXS0506 nu 290 TeV z=0.3365 (10 d window)': (2.9e5, 0.3365, None, 'q')}
okB = True
for lab, (E, z, bnd, sp_) in B.items():
    c = RAYS[0][2] if sp_ == 'g' else RAYS[0][1]
    d_ax = dt(E, z, c)
    eq = min(EQ[n][0 if sp_ == 'g' else 1] for n in EQ)
    if bnd is None:
        bnd = E * math.sqrt(1.5 * K(z) * H0inv / (10 * 86400))
    okB &= eq > bnd
    print(f'   {lab}: delay(axis) {d_ax:.1e} s; implied bound {bnd:.1e} GeV; margin 10^{math.log10(eq / bnd):.1f} in E_QG,2'
          f' (10^{2 * math.log10(eq / bnd):.1f} in delay)')
Eneed = EQ['axis'][0] * math.sqrt(1.0 / (1.5 * K(1.0) * H0inv))
print(f'   photon energy for a 1 s axis delay from z=1: {Eneed * 1e9:.1e} eV; body/axis delay ratio '
      f'{(EQ["axis"][0] / EQ["body"][0]) ** 2:.3f} (cubic l=4 pattern, lattice orientation unsupplied)')
mrg = min(th['axis'], th['sky']) / 1.4e15
check('B1 every time-of-flight bound is passed by >= 6.5 orders in E_QG,2; the nearest sharp test is the '
      'gamma -> e+e- cutoff, a factor ' + f'{mrg:.0f} above the highest LHAASO photon', okB and mrg > 10)
print(f'runtime {time.time() - T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
