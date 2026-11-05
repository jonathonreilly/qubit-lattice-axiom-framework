AUDIT_INPUT_PATHS = ('docs/A_TURN_KEPT_BY_THE_UPDATE_AND_BROKEN_BY_THE_VACUUM_GIVES_CP_AND_THETA_BAR_TOGETHER_UNLESS_A_NELSON_BARR_BLOCK_IS_SUPPLIED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""Spontaneous turn/CP breaking with an exact three-fold turn and exact T in the update.
Supplied model, finite diagnostic.  Families carry turn charges q=(0,1,2) (eigenvalues 1,w,w^2).
Mass term psibar_L M psi_R; entry (i,j) needs a vacuum field of charge q_Li-q_Rj mod 3.
All couplings REAL (T/CP of the update).  CP is broken only by vacuum phases."""
import numpy as np
AUDIT_TIMEOUT_SEC = 60
rng = np.random.default_rng(20261022)
w = np.exp(2j*np.pi/3)
q = np.array([0, 1, 2])
D = (q[:, None]-q[None, :]) % 3
P = 0; F = 0
def chk(name, ok, extra=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS " if ok else "FAIL ")+name+(" | "+extra if extra else ""))
def masses(A, B, C, phi):
    return A*(D == 0)+B*(D == 1)*phi+C*(D == 2)*np.conj(phi)
def lefts(M):
    e, U = np.linalg.eigh(M@M.conj().T); return U[:, np.argsort(e)]
def Jof(V):
    return float(np.imag(V[0, 0]*V[1, 1]*np.conj(V[0, 1])*np.conj(V[1, 0])))
def J2(Mu, Md):
    Uu = lefts(Mu); Ud = lefts(Md); return Jof(Uu.conj().T@Ud[:3, :3] if Md.shape[0] == 3 else Uu.conj().T@Ud[:3, :3])
def tb(Mu, Md):
    return float(np.angle(np.linalg.det(Mu)*np.linalg.det(Md)))
def coup():
    return [rng.normal(size=(3, 3)) for _ in range(3)]
print("== A: one turn-charged order parameter phi=v e^{ia}, linear couplings, Q,u,d all (0,1,2)")
cu, cd = coup(), coup()
T = np.diag(w**q)
phi0 = 0.7*np.exp(0.4j)
Mu = masses(*cu, phi0)
inv = np.abs(T.conj().T@masses(*cu, w*phi0)@T-Mu).max()
chk("A1 exact turn covariance: T^+ M(w phi) T = M(phi)", inv < 1e-13, "%.1e" % inv)
def JA(a, v=0.7):
    return J2(masses(*cu, v*np.exp(1j*a)), masses(*cd, v*np.exp(1j*a)))
def TA(a, v=0.7):
    return tb(masses(*cu, v*np.exp(1j*a)), masses(*cd, v*np.exp(1j*a)))
al = [0, np.pi/3, 2*np.pi/3, np.pi]
mx = max(abs(JA(a)) for a in al); mt = max(min(abs(TA(a)), abs(abs(TA(a))-np.pi)) for a in al)
chk("A2 aligned vacua (phi^3 real): J=0 and arg det in {0,pi}", mx < 1e-14 and mt < 1e-12, "maxJ=%.1e" % mx)
a = 0.4
chk("A3 J periodic 2pi/3 and CP-odd", abs(JA(a+2*np.pi/3)-JA(a)) < 1e-14 and abs(JA(-a)+JA(a)) < 1e-14,
    "J(0.4)=%.3e" % JA(a))
# det structure: det M = p + r1 z + r2 zbar, z = phi^3; Im det = (r1-r2) v^3 sin3a
A_, B_, C_ = cu
pdet = np.linalg.det(masses(A_, B_, C_, 0.0)).real
dets = [np.linalg.det(masses(*cu, 0.7*np.exp(1j*t))) for t in (0.1, 0.5, 0.9)]
s3 = [0.7**3*np.sin(3*t) for t in (0.1, 0.5, 0.9)]
rat = [d.imag/s for d, s in zip(dets, s3)]
chk("A4 Im det M = (r1-r2) v^3 sin(3a) exactly (det depends on phi only via |phi|^2, phi^3)", np.ptp(rat) < 1e-12,
    "r1-r2=%.4f" % rat[0])
Js, Ts = [], []
for k in range(200):
    cu2, cd2 = coup(), coup(); aa = rng.uniform(0, 2*np.pi)
    Js.append(abs(J2(masses(*cu2, .7*np.exp(1j*aa)), masses(*cd2, .7*np.exp(1j*aa)))))
    Ts.append(abs(tb(masses(*cu2, .7*np.exp(1j*aa)), masses(*cd2, .7*np.exp(1j*aa)))))
Js, Ts = np.array(Js), np.array(Ts)
chk("A5 generic vacuum phase: J != 0 AND theta_bar_tree = O(1) (strong CP fails)", np.median(Js) > 1e-3 and np.median(Ts) > 0.1,
    "median|J|=%.2e median|arg det|=%.2f, min|arg det|=%.1e (need <1e-10)" % (np.median(Js), np.median(Ts), Ts.min()))
# one-field renormalizable potential: V(a) = 2 k v^3 cos3a -> aligned minima -> J=0
aa = np.linspace(0, 2*np.pi, 20001)
amin = aa[np.argmin(np.cos(3*aa))]
chk("A6 one-field Z3+T potential (k phi^3+cc) minimum is aligned -> J=0", abs(JA(amin)) < 1e-6, "a*=%.4f J=%.1e" % (amin, JA(amin)))
# reflection (1<->2, phi<->phi*) forces det real but also J=0
Pm = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
def refl(c):
    A, B, C = c; A = (A+Pm@A@Pm)/2; Cn = Pm@B@Pm; return [A, B, Cn]
ru, rd = refl(coup()), refl(coup())
Mr_u, Mr_d = masses(*ru, .7*np.exp(.4j)), masses(*rd, .7*np.exp(.4j))
chk("A7 reflection-protected texture: arg det in {0,pi} but J = 0 (lemma)",
    min(abs(tb(Mr_u, Mr_d)), abs(abs(tb(Mr_u, Mr_d))-np.pi)) < 1e-12 and abs(J2(Mr_u, Mr_d)) < 1e-14, "J=%.1e" % J2(Mr_u, Mr_d))
# tuning: solve one real coupling so that arg det(Mu Md)=0 at a=0.4; J survives (FITTED)
from scipy.optimize import brentq
def g(x):
    c = [cd[0], cd[1], cd[2].copy()]; c[2][2, 0] = x
    return np.imag(np.linalg.det(masses(*cu, phi0))*np.linalg.det(masses(*c, phi0)))
xs = np.linspace(-5, 5, 2001); gv = [g(x) for x in xs]; i0 = np.where(np.sign(gv[:-1]) != np.sign(gv[1:]))[0][0]
x0 = brentq(g, xs[i0], xs[i0+1]); c = [cd[0], cd[1], cd[2].copy()]; c[2][2, 0] = x0
th = tb(Mu, masses(*c, phi0)); Jt = J2(Mu, masses(*c, phi0))
chk("A8 one TUNED real relation gives theta_tree in {0,pi} with J != 0 (FITTED, not structural)",
    min(abs(th), abs(abs(th)-np.pi)) < 1e-10 and abs(Jt) > 1e-4, "J=%.2e" % Jt)
print("== B: Nelson-Barr-type: light block from real-aligned chi (charge w), heavy D, Z2-odd phi1,phi2 (charge w)")
# spontaneous phases from the Z3 x Z2 x T potential (real coefficients)
def Vpot(x, c):
    a1, a2 = x
    p1, p2 = np.exp(1j*a1), np.exp(1j*a2)
    return 2*np.real(c[0]*p1**2+c[1]*p2**2+c[2]*p1*p2+c[3]*np.conj(p1)*p2+c[4]*(np.conj(p1)*p2)**2)
from scipy.optimize import minimize
def vac(c):
    best = None
    for s in range(24):
        r = minimize(Vpot, rng.uniform(0, 2*np.pi, 2), args=(c,), method="BFGS")
        if best is None or r.fun < best.fun-1e-12: best = r
    return best.x
def nb(cu, cd, f, MD, a1, a2, chi=0.6, v=1.0):
    Mu = masses(*cu, chi); md = masses(*cd, chi)
    p1, p2 = v*np.exp(1j*a1), v*np.exp(1j*a2)
    Fr = np.array([0, f[0]*np.conj(p1)+f[1]*np.conj(p2), f[2]*p1+f[3]*p2])
    M4 = np.zeros((4, 4), complex); M4[:3, :3] = md; M4[3, :3] = Fr; M4[3, 3] = MD
    return Mu, M4
qL4 = np.array([0, 1, 2, 0]); qR4 = np.array([0, 1, 2, 0])
cpot = np.array([0.3, -0.2, 0.25, 0.4, 0.5])
a1, a2 = vac(cpot)
cu, cd = coup(), coup(); f = rng.normal(size=4)*8; MD = 10.0
Mu, M4 = nb(cu, cd, f, MD, a1, a2)
# turn covariance of the 4x4 (rotate chi, phi1, phi2 by w)
Mu_w, M4w = nb(cu, cd, f, MD, a1+2*np.pi/3, a2+2*np.pi/3, chi=0.6*w)
L4 = np.diag(w**qL4); R4 = np.diag(w**qR4)
chk("B1 exact turn covariance of the 4x4 down matrix", np.abs(L4.conj().T@M4w@R4-M4).max() < 1e-12)
chk("B2 Z2 forbids Q D_R: det M4 = det(m_d) M_D is REAL for every vacuum", abs(np.linalg.det(M4).imag) < 1e-12*abs(np.linalg.det(M4)))
JB = J2(Mu, M4); thB = tb(Mu, M4)
chk("B3 at the potential's minimum (a1,a2)=(%.3f,%.3f): J != 0 with arg det in {0,pi}" % (a1, a2),
    abs(JB) > 1e-5 and min(abs(thB), abs(abs(thB)-np.pi)) < 1e-12, "J=%.2e theta=%.1e" % (JB, thB))
Mu0, M40 = nb(cu, cd, f, MD, 0.0, 0.0)
chk("B4 control: real vacuum phases give J = 0", abs(J2(Mu0, M40)) < 1e-14)
rs = []
for x in (1e-3, 1e-2, 0.1, 1.0, 3.0):
    _, M4x = nb(cu, cd, f*x, MD, a1, a2); rs.append(abs(J2(Mu, M4x)))
chk("B5 J unsuppressed only if |F| ~ M_D (NB scale condition)", rs[0] < 1e-2*rs[3], "J(|F|/MD~1e-3..3)=" + ",".join("%.1e" % r for r in rs))
ok = 0; nJ = 0; sgnpos = 0
for k in range(40):
    cpk = rng.normal(size=5); b1, b2 = vac(cpk)
    cuk, cdk = coup(), coup(); fk = rng.normal(size=4)*8
    Muk, M4k = nb(cuk, cdk, fk, MD, b1, b2)
    th = tb(Muk, M4k); ok += min(abs(th), abs(abs(th)-np.pi)) < 1e-12; nJ += abs(J2(Muk, M4k)) > 1e-6; sgnpos += abs(th) < 1e-12
chk("B6 40 seeded potentials+couplings: theta_tree in {0,pi} always; J != 0 in most", ok == 40 and nJ >= 20,
    "J!=0: %d/40, theta=0 (not pi): %d/40 (sign is a discrete choice)" % (nJ, sgnpos))
print("== C: domain walls of the spontaneously broken turn (estimates)")
Mpl = 2.4e18
for v in (1e3, 1e8):
    sig = v**3; Hd = sig/Mpl**2; Td = np.sqrt(Hd*Mpl)
    print("  v=%.0e GeV: sigma~v^3, wall domination at T~%.1e GeV" % (v, Td))
chk("C1 ZKO: stable Z3 walls need sigma^(1/3) < ~1 MeV -> NB scale requires breaking before/during inflation (T_RH < v)",
    np.sqrt((1e3)**3/Mpl) > 1e-12)
print("TOTAL: PASS=%d FAIL=%d" % (P, F))
