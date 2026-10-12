"""C5 R9-2 (b)-(c), d = 1: interacting stress on R8-1's repaired two-body BT box law, and the fall of
bound bodies in a uniform lapse.  Lattice operators throughout (R8-1's ring construction, reused).

Law (R8-1, refereed CWC): one CAR mode per site, two-particle sector (ordered-pair first quantisation),
  eps = sqrt(m^2 + s(k)^2), s = k on |k| <= B = 2.6;  W(P) = c(P)[sqrt(M^2+P^2) - sqrt(M0^2+P^2)],
  plateau c = 1 on |P| <= Pi1 = 0.6, c = 0 on |P| >= Pi2 = 1.2;  K = (1/2){H, X_P}, X_P = sum_i (1/2){eps_i/H0, X_i}.
Stress (constructed in the report): T00 = T00_A (R8-2 Construction A, first moment K0) + T00_W (Weyl-midpoint
density of W, first moment (1/2){W, X_P}).  So int T00 = H and the first energy moment is D1 = K globally.
Gravitating momentum J' := i[H, D1] (= int T^{01}).  Uniform lapse: H_g = H + g D1.  Exact identities:
  d<D1>/dt = <J'>,  d<J'>/dt = <N> - g<H + A>,  with  N := i[H, J'],  A := -i[K, J'] - H,
  d<H>/dt = -g<J'>,  so at O(g):  Xddot_E / g = -(1 + <A>/<H>) + 2 V^2 + <N>/(g<H>),  X_E = <D1>/<H>, V = <J'>/<H>.
Box sector (R8-1's domain): J' = P, A = N = 0 exactly -> Xddot_E = -g (1 - 2V^2) for every body.
Comparator (binding energy does not gravitate): D1 = K0 (stress = free part only): weight w = <H0>/<H>.
Checks: (1) weights at rest / moving, two (three) binding fractions; (2) eta between them; (3) the transition shell
(where A, N != 0); (4) the free region; (5) [real-time check in r92_fall_rt.py].
"""
import numpy as np, time, sys
from r81_common import sstep, wrap, BoxLaw, BTKernel, lam_for_mass
L = int(sys.argv[1]) if len(sys.argv) > 1 else 1024
m, KAP = 0.5, 0.4
PI1, PI2 = 0.6, 1.2
law = BoxLaw(m, B=2.6, B2=3.0)
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
F = np.fft.fft2; IF = np.fft.ifft2
def chart(k1, k2):
    th1, th2 = np.arcsinh(k1/m), np.arcsinh(k2/m); v = 0.5*(th1 - th2)
    q = m*np.sinh(v)
    J = 0.5*m*np.cosh(v)*(1/np.sqrt(m*m + k1**2) + 1/np.sqrt(m*m + k2**2))
    return q, J
def build(MU_B):
    lam = lam_for_mass(m, KAP, 1, MU_B); Kr = BTKernel(m, KAP, lam, 1)
    blocks = []
    for nP in range(L):
        P = wrap(2*np.pi*nP/L)
        if abs(P) >= PI2: continue
        k1 = k; n2 = (nP - n) % L; k2 = k[n2]
        ok = (np.abs(k1) < 2.0) & (np.abs(k2) < 2.0) & (np.abs(k1 + k2 - P) < 1e-9)
        q, J = chart(k1, k2); sel = ok & (np.abs(q) < KAP)
        if not sel.any(): continue
        qs, Js = q[sel], J[sel]
        w = Kr.g1(qs)[:, None]*Kr.g1(qs)[None, :]*Kr.Omega(P*P, qs, qs)
        blocks.append((n[sel], n2[sel], (2*np.pi/L)*cP(P)*w*np.sqrt(Js[:, None]*Js[None, :])))
    return lam, Kr, blocks
nrm = lambda v: np.sqrt(np.sum(np.abs(v)**2))
ip = lambda a, b: np.vdot(a, b)
def ops(blocks):
    def Wk(ph):
        o = np.zeros_like(ph)
        for i1, i2, Wb in blocks: o[i1, i2] += Wb @ ph[i1, i2]
        return o
    H = lambda p: IF(H0k*F(p) + Wk(F(p)))
    H0 = lambda p: IF(H0k*F(p))
    Pp = lambda p: IF(Pk*F(p))
    XP = lambda p: 0.5*(IF(f1*F(X1*p)) + X1*IF(f1*F(p)) + IF(f2*F(X2*p)) + X2*IF(f2*F(p)))
    K = lambda p: 0.5*(H(XP(p)) + XP(H(p)))
    K0 = lambda p: 0.5*(H0(XP(p)) + XP(H0(p)))
    return H, H0, Pp, K, K0
def bump(P, P0, w):
    z = (P - P0)/w
    with np.errstate(divide='ignore', over='ignore'):
        return np.where(np.abs(z) < 1, np.exp(-1.0/np.maximum(1 - z*z, 1e-300)), 0.0)
def packet(Kr, MU_B, P0, w, kind='bound'):
    # Gaussian total-momentum profile (sigma_P = w): real-space width 1/(2w) sites, so the ring seam is
    # negligible; plateau tails exp(-(Pi1-|P0|)^2/(4 w^2)) are quoted with each run.
    K1, K2 = np.meshgrid(k, k, indexing='ij'); q, J = chart(K1, K2)
    ok = (np.abs(K1) < 2.0) & (np.abs(K2) < 2.0)
    if kind == 'bound': phi = Kr.g1(q)/(MU_B - Kr.M0(q))
    else: phi = (q/0.15)*np.exp(-q**2/(2*0.15**2))
    ph = np.where(ok, np.exp(-(K1 + K2 - P0)**2/(4*w*w))*phi*np.sqrt(J), 0.0)
    p = IF(ph); return p/nrm(p)
def measure(p, H, H0, Pp, K, K0, D1='K'):
    Dop = K if D1 == 'K' else K0
    Hp = H(p); Dp = Dop(p)
    Jp = 1j*(H(Dp) - Dop(Hp))                 # J' psi = i[H, D1] psi
    eH = ip(p, Hp).real; eH0 = ip(p, H0(p)).real; eJ = ip(p, Jp).real; eP = ip(p, Pp(p)).real
    # <[D1, J']> = <D1 p|J' p> - <J' p|D1 p>  (both symmetric)
    cDJ = ip(Dp, Jp) - ip(Jp, Dp)
    w = (-1j*cDJ).real/eH                     # 1 + <A>/<H>
    # N = i[H, J'] : <N> = i(<H p|J' p> - <J' p|H p>)
    eN = (1j*(ip(Hp, Jp) - ip(Jp, Hp))).real
    nN = nrm(1j*(H(Jp) - 1j*(H(Dop(Hp)) - Dop(H(Hp)))))   # ||N psi|| = ||i(H J' - J' H) psi||
    wP = (-1j*(ip(Dp, Pp(p)) - ip(Pp(p), Dp))).real/eH  # -i<[D1, P]>/<H> (lattice-momentum weight)
    V = eJ/eH
    return dict(H=eH, H0=eH0, J=eJ, P=eP, w=w, wP=wP, V=V, a=-w + 2*V*V, N=eN, nN=nN/nrm(Hp),
                Jdev=nrm(Jp - Pp(p))/nrm(Pp(p)) if nrm(Pp(p)) > 1e-12 else nrm(Jp - Pp(p))/nrm(Hp))
T0 = time.time()
pr('L = %d ; m = %.2f, kappa = %.2f, plateau |P| <= %.2f (c = 0 beyond %.2f), box |k| <= 2.6' % (L, m, KAP, PI1, PI2))
res = {}
for MU_B in ([0.85, 0.95, 0.70] if L < 2048 else [0.85, 0.95]):
    lam, Kr, blocks = build(MU_B)
    H, H0, Pp, K, K0 = ops(blocks)
    fB = (2*m - MU_B)/(2*m)
    pr('--- M_b = %.2f (binding fraction f_B = (2m - M_b)/2m = %.3f), lam = %.6f ---' % (MU_B, fB, lam))
    PACK = [('bound, at rest  P0=0.00', 0.0, 0.06, 'bound'), ('bound, moving   P0=0.25', 0.25, 0.04, 'bound'),
            ('scatt, at rest  P0=0.00', 0.0, 0.06, 'scatt'), ('bound, SHELL    P0=0.90', 0.9, 0.04, 'bound'),
            ('bound-profile, FREE P0=1.60', 1.6, 0.04, 'bound')]
    if L >= 2048: PACK = PACK[:2]
    for lab, P0, w, kind in PACK:
        p = packet(Kr, MU_B, P0, w, kind)
        r = measure(p, H, H0, Pp, K, K0, 'K'); rc = measure(p, H, H0, Pp, K, K0, 'K0')
        res[(MU_B, lab)] = (r, rc)
        pr('  %-28s <H>=%.6f V=%+.5f | K-stress: w-1 = %+.2e, wP-1 = %+.2e, a/g - (-1+2V^2) = %+.2e, |N psi|/|H psi| = %.1e, |J\'psi - P psi|/|P psi| = %.1e'
           % (lab, r['H'], r['V'], r['w'] - 1, r['wP'] - 1, r['a'] - (-1 + 2*r['V']**2), r['nN'], r['Jdev']))
        pr('  %-28s comparator (free-only stress, D1 = K0): wP = %.6f  (<H0>/<H> = %.6f)' % ('', rc['wP'], r['H0']/r['H']))
    pr('  [M_b = %.2f done, %.0fs]' % (MU_B, time.time() - T0))
pr('=== Eotvos eta between binding fractions (linear order in g) ===')
for lab in ['bound, at rest  P0=0.00', 'bound, moving   P0=0.25']:
    for A_, B_ in ([(0.85, 0.95), (0.70, 0.95), (0.70, 0.85)] if L < 2048 else [(0.85, 0.95)]):
        rA, rcA = res[(A_, lab)]; rB, rcB = res[(B_, lab)]
        dA = rA['a'] - (-1 + 2*rA['V']**2); dB = rB['a'] - (-1 + 2*rB['V']**2)
        # comparator acceleration: -wP(K0) + 2V^2 using lattice momentum
        cA = -rcA['wP'] + 2*rA['V']**2; cB = -rcB['wP'] + 2*rB['V']**2
        pr('  %s  M_b %.2f vs %.2f: interacting stress eta = |delta_A - delta_B| = %.2e (deltas %+.1e, %+.1e) ; comparator (binding energy not gravitating) eta = %.4e'
           % (lab, A_, B_, abs(dA - dB), dA, dB, abs((-rcA['wP']) - (-rcB['wP']))/(0.5*(rcA['wP'] + rcB['wP']))))
pr('runtime %.0fs' % (time.time() - T0))
with open(__file__.replace('.py', '_L%d.out' % L), 'w') as fh: fh.write('\n'.join(out) + '\n')
