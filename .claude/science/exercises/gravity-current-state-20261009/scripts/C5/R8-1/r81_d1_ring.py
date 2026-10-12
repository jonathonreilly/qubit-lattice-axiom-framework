"""R8-1, script 2 (d = 1): the repaired interacting two-body box law on a ring of L sites, with
the boost CONSTRUCTED as a lattice operator and every d = 1 Poincare commutator checked in real space.

Law (one complex fermion per site; graded CAR; two-particle sector, first-quantized on ordered pairs):
  eps(k) = sqrt(m^2 + s(k)^2), s = k on |k| <= B (R7-1's box law), P = s(k1) + s(k2),
  W(P; k1', k1) = c(P) w(P; q', q) sqrt(q_k(k1') q_k(k1)) * (2 pi / L)  [smooth BT kernel, r81_common]
  H = H0 + W ;  X_P = sum_i (1/2){eps_i/H0, X_i}  (X_i = lattice site positions) ;
  K = (1/2){H, X_P}   (globally symmetric; = K0 + (1/2){W, X_P}, K0 = sum_i (1/2){eps_i, X_i})
Second-quantized: H_int = (1/2) sum W a+ a+ a a and K_W = (1/2) sum <k1'k2'|(1/2){W,X_P}|k1k2> a+ a+ a a
(product-basis kernels; the prefactor is decided in r81_fock_norm.out).
Checks: [K,P] = iH, [K,H] = iP, [H,P] = 0 on antisymmetric packets inside the plateau, as
lattice operators (FFT for momentum symbols, diagonal site positions).  Comparators:
  (c1) R7-1's printed sign K = -(1/2){H, X_P};  (c2) the free boost K0 with the interacting H;
  (c3) the unsymmetrised cutoff c(P) * (1/2){W_1, X_P} vs (1/2){c W_1, X_P} (hermiticity).
  (d) invariant mass E(P)^2 - P^2 of the bound state on the ring (rep-independent test).
"""
import numpy as np, time, sys
from r81_common import sstep, wrap, BoxLaw, BTKernel, lam_for_mass

L = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
m, KAP, MU_B = 0.5, 0.4, 0.85
PI1, PI2 = 0.6, 1.2
lam = lam_for_mass(m, KAP, 1, MU_B)
law = BoxLaw(m, B=2.6, B2=3.0)
K = BTKernel(m, KAP, lam, 1)
cP = lambda P: sstep((PI2 - np.abs(P))/(PI2 - PI1))

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

n = np.arange(L); k = wrap(2*np.pi*n/L)
e = law.eps(k); s = law.s(k)
E1, E2 = np.meshgrid(e, e, indexing='ij'); S1, S2 = np.meshgrid(s, s, indexing='ij')
H0k = E1 + E2; Pk = S1 + S2; f1 = E1/H0k; f2 = E2/H0k
x = np.where(n < L//2, n, n - L).astype(float)
X1, X2 = np.meshgrid(x, x, indexing='ij')

def chart(k1, k2):
    th1, th2 = np.arcsinh(k1/m), np.arcsinh(k2/m); v = 0.5*(th1 - th2)
    q = m*np.sinh(v)
    J = 0.5*m*np.cosh(v)*(1/np.sqrt(m*m + k1**2) + 1/np.sqrt(m*m + k2**2))   # dq/dk1 at fixed P
    return q, J

# ---- build W blocks: for each lattice total momentum nP, the pairs (n1, nP - n1) in supp
t0 = time.time()
blocks = []
for nP in range(L):
    P = wrap(2*np.pi*nP/L)
    if abs(P) >= PI2: continue
    k1 = k; n2 = (nP - n) % L; k2 = k[n2]
    ok = (np.abs(k1) < 2.0) & (np.abs(k2) < 2.0) & (np.abs(k1 + k2 - P) < 1e-9)   # no umklapp
    q, J = chart(k1, k2)
    sel = ok & (np.abs(q) < KAP)
    if not sel.any(): continue
    qs, Js = q[sel], J[sel]
    w = K.g1(qs)[:, None]*K.g1(qs)[None, :]*K.Omega(P*P, qs, qs)
    Wb = (2*np.pi/L)*cP(P)*w*np.sqrt(Js[:, None]*Js[None, :])
    blocks.append((n[sel], n2[sel], Wb, P))
pr('L = %d, m = %.2f, kappa = %.2f, lam = %.6f (M_b = %.4f), plateau |P| <= %.2f, c = 0 at |P| >= %.2f; %d W blocks built in %.1fs'
   % (L, m, KAP, lam, MU_B, PI1, PI2, len(blocks), time.time() - t0))

def Wk(ph, cut=True, unc=False):
    o = np.zeros_like(ph)
    for i1, i2, Wb, P in blocks:
        Wuse = Wb if cut else Wb/max(cP(P), 1e-300)
        o[i1, i2] += Wuse @ ph[i1, i2]
    return o

F = np.fft.fft2; IF = np.fft.ifft2
def Hop(p):  return IF(H0k*F(p) + Wk(F(p)))
def H0op(p): return IF(H0k*F(p))
def Wop(p):  return IF(Wk(F(p)))
def Pop(p):  return IF(Pk*F(p))
def XP(p):
    return 0.5*(IF(f1*F(X1*p)) + X1*IF(f1*F(p)) + IF(f2*F(X2*p)) + X2*IF(f2*F(p)))
def Kop(p):  return 0.5*(Hop(XP(p)) + XP(Hop(p)))
def K0op(p): return 0.5*(H0op(XP(p)) + XP(H0op(p)))
nrm = lambda v: np.sqrt(np.sum(np.abs(v)**2))

# ---- packets: psi^(k1,k2) = A(P) phi(q) sqrt(J) (half-density), antisymmetric
def packet(P0, sigP, phi, boost_phase=0.0):
    K1, K2 = np.meshgrid(k, k, indexing='ij')
    q, J = chart(K1, K2)
    Ptot = K1 + K2
    ok = (np.abs(K1) < 2.0) & (np.abs(K2) < 2.0)
    A = np.exp(-(Ptot - P0)**2/(4*sigP**2))
    ph = np.where(ok, A*phi(q)*np.sqrt(J), 0.0)
    p = IF(ph); return p/nrm(p)

# bound state of M: phi_b ~ g/(mu_b - M0) (exact rank-one eigenfunction), odd, supp |q| < kappa
phi_b = lambda q: K.g1(q)/(MU_B - K.M0(q))
phi_s = lambda q: (q/0.15)*np.exp(-q**2/(2*0.15**2))
phi_mix = lambda q: phi_b(q)/np.sqrt(np.sum(K.g1(K.qg)**2/(MU_B - K.M0g)**2*K.wq)) + 0.8*phi_s(q)

def residuals(p, Kf, label):
    Hp, Pp, Kp = Hop(p), Pop(p), Kf(p)
    r_KP = nrm(Kf(Pp) - Pop(Kp) - 1j*Hp)/nrm(Hp)
    r_KH = nrm(Kf(Hp) - Hop(Kp) - 1j*Pp)/max(nrm(Pp), 1e-300)
    r_HP = nrm(Hop(Pp) - Pop(Hp))/nrm(Hp)
    pr('  %-34s  |[K,P]-iH|/|H| = %.2e   |[K,H]-iP|/|P| = %.2e   |[H,P]|/|H| = %.2e' % (label, r_KP, r_KH, r_HP))
    return r_KP, r_KH

for name, P0, sig, phi in [('bound state, P0 = 0.15', 0.15, 0.06, phi_b),
                           ('bound+scattering mix, P0 = -0.2', -0.2, 0.06, phi_mix),
                           ('scattering Gaussian, P0 = 0.3', 0.3, 0.05, phi_s)]:
    p = packet(P0, sig, phi)
    asym = nrm(p + p.T)/nrm(p)
    wfrac = nrm(Wop(p))/nrm(Hop(p))
    pr('packet: %s (antisymmetry defect %.1e; |W psi|/|H psi| = %.3f; sym. check of K: |<a|Kb>-<Ka|b>| below)' % (name, asym, wfrac))
    residuals(p, Kop, 'repaired K = (1/2){H, X_P}')
    residuals(p, lambda v: -Kop(v), '(c1) R7-1 printed sign -(1/2){H,X_P}')
    residuals(p, K0op, '(c2) free K0 with interacting H')

# hermiticity of K (global symmetric) vs unsymmetrised cutoff c(P)*(1/2){W1, X_P}; test states in the transition shell
pa = packet(0.85, 0.08, phi_b); pb = packet(0.95, 0.08, phi_mix)
inner = lambda a, b: np.vdot(a, b)
def Kunsym(p):   # K0 + c(P) * (1/2){W1, X_P}  with W1 = uncut kernel (multiply AFTER the anticommutator)
    W1 = lambda v: IF(Wk(F(v), cut=False))
    t = 0.5*(W1(XP(p)) + XP(W1(p)))
    cmul = lambda v: IF(cP(Pk)*F(v))
    return K0op(p) + cmul(t)
for lab, Kf in [('repaired (1/2){c W1, X_P}', Kop), ('(c3) unsymmetrised c(P)(1/2){W1,X_P}', Kunsym)]:
    d = inner(pa, Kf(pb)) - inner(Kf(pa), pb)
    pr('hermiticity in the c<1 shell: %-40s |<a,Kb> - <Ka,b>| = %.2e  (|<a,Kb>| = %.2e)' % (lab, abs(d), abs(inner(pa, Kf(pb)))))

# ---- (d) invariant mass of the lowest odd state on the ring, per lattice P (rep-independent test)
pr('(d) bound-state invariant mass on the ring, sqrt(E_min(P)^2 - P^2), odd sector at fixed lattice P:')
mb = []
for nP in [0, 10, 25, 50, 75, 97, 120, 150, 180]:
    P = wrap(2*np.pi*nP/L)
    n2 = (nP - n) % L
    Hm = np.diag(e + e[n2]).astype(float)
    for i1, i2, Wb, PP in blocks:
        if abs(PP - P) < 1e-12:
            Hm[np.ix_(i1, i1)] += Wb
    Xm = np.zeros((L, L)); Xm[n, n2] = 1
    Ho = 0.25*(Hm - Hm@Xm - Xm@Hm + Xm@Hm@Xm)
    ev = np.linalg.eigvalsh(0.5*(Ho + Ho.T)); ev = ev[np.abs(ev) > 1e-12]
    Mb = np.sign(ev.min()**2 - P**2)*np.sqrt(abs(ev.min()**2 - P**2)); mb.append((P, cP(P), Mb))
    pr("    P = %+.4f  c = %.3f  E_min = %.10f  sign(E^2-P^2) sqrt|E^2-P^2| = %.12f%s" % (P, cP(P), ev.min(), Mb, "  (E < |P|: lattice edge pairs, outside the box)" if Mb < 0 else ""))
pl = np.array([r[2] for r in mb if r[1] == 1.0])
pr('(d) plateau spread of M_b = %.2e (target M_b = %.4f; finite-L ring discretisation of the continuum M)' % (pl.max() - pl.min(), MU_B))
with open(__file__.replace('.py', '_L%d.out' % L), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
