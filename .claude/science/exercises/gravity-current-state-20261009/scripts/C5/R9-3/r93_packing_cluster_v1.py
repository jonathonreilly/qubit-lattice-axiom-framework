"""R9-3 script 1 (d = 1, fixed total momentum P; by R7-6 Lemma L3 the box sector equals the continuum fibre).

The packing operator for pair b = (23) with spectator 1 (R7-6 convention, `r76_packing_range.py`):
   B_b = R0^dag R_M ,   R_M = sum_n |chi_n><chi_n| (x) R_{mu_n},   R0 = sum_j |q_j><q_j| (x) R_{M0(q_j)}
   R_mu : k1 -> q1(P, k1; mu) = rest-frame momentum of particle 1 when the (23) cluster has mass mu.
   (R_nu^dag R_mu f)(k) = f(k') sqrt(dk'/dk),   q1(P, k'; mu) = q1(P, k; nu).
Exact reduction used (R8-1 referee identity): G = supp g reduces M0 and M = M0 + lam|g><g|, so
   B_b - 1 = (B_b - 1) Q_G  on the odd (fermionic) sector of q23 in (0, kappa); B_b = 1 elsewhere.

Test states (lab momenta, fixed P): product Gaussian packets, particle 2 at x2 = 0, particle 3 at x3 = D,
particle 1 at x1 = y(D).  Configurations:
   '2+1'   : y = 0      (1 next to 2; 3 recedes)  -> the cluster limit a = (12)(3) that Sokolov needs: B_b -> 1 ?
   'centre': y = D/2    (spectator at the (23) centre; R7-6's test (A) geometry)
   'far1'  : y = -D     (all three apart, 1 on the other side)
Also B_a (pair 12, spectator 3) on the 2+1 state: expected NOT to decay (BT long range, R7-6 (B)).
Output: ||(B - 1) psi_D|| / ||psi_D|| against D.
"""
import numpy as np, sys, time
from scipy.interpolate import CubicSpline

args = dict(a.split('=') for a in sys.argv[1:])
m = float(args.get('m', 0.3)); KAP = float(args.get('kap', 0.25)); LAM = float(args.get('lam', -3.0))
P = float(args.get('P', 0.4))
Ds = [int(x) for x in args.get('Ds', '10,20,40,80,160,320,640').split(',')]
conf = args.get('conf', '2+1')
pair = args.get('pair', 'b')          # 'b' = (23) packing with spectator 1 ; 'a' = (12) packing with spectator 3
ppo = float(args.get('ppo', 14.0))    # q-grid points per oscillation
kc = [float(x) for x in args.get('kc', '0.10,0.15,0.15').split(',')]   # packet centres k1,k2,k3 (sum need not be P)
sk = float(args.get('sk', 0.05))
tag = args.get('tag', '')

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def g(q): return q*sstep(1.0 - (q/KAP)**2)/KAP
def M0f(q): return 2*np.sqrt(m*m + q*q)
def eps(k): return np.sqrt(m*m + k*k)

# ---- spectator rest-frame momentum and its k-derivative -------------------------------------------
def q1f(k, mu):
    """rest-frame momentum of the spectator (lab momentum k) when the pair (lab momentum P-k) has mass mu."""
    E = np.sqrt(mu*mu + (P-k)**2) + eps(k)
    Th = np.arctanh(P/E)
    return m*np.sinh(np.arcsinh(k/m) - Th)
def dq1f(k, mu):
    Ep = np.sqrt(mu*mu + (P-k)**2); E = Ep + eps(k)
    Th = np.arctanh(P/E)
    dE = -(P-k)/Ep + k/eps(k)
    dTh = -P*dE/(E*E - P*P)
    return m*np.cosh(np.arcsinh(k/m) - Th)*(1/eps(k) - dTh)

# ---- pair chart: (Ppair, q) <-> (k_first, k_second) -----------------------------------------------
def pair_momenta(Pp, q):
    v = np.arcsinh(q/m); Y = np.arcsinh(Pp/(2*m*np.cosh(v)))
    return m*np.sinh(Y+v), m*np.sinh(Y-v)
def dq_dk_second(Pp, q):
    """|dq/dk_second| at fixed pair momentum (q = m sinh((th_f - th_s)/2))."""
    kf, ks = pair_momenta(Pp, q); v = np.arcsinh(q/m)
    return 0.5*m*np.cosh(v)*(1/eps(kf) + 1/eps(ks))

# ---- test state: lab product packets at fixed P, in variables (k_spec, q_pair) of the chosen pair ----
def psi_lab(k1, k2, k3, D, y):
    G = np.exp(-((k1-kc[0])**2 + (k2-kc[1])**2 + (k3-kc[2])**2)/(4*sk*sk))
    return G*np.exp(-1j*(k1*y + k3*D))
def psi_pair(kspec, q, D, y):
    """state in (k_spec, q) for pair b=(23) [spectator 1] or a=(12) [spectator 3]; half-density in q."""
    Pp = P - kspec
    kf, ks = pair_momenta(Pp, q)
    J = 1.0/np.sqrt(dq_dk_second(Pp, q))
    if pair == 'b':   # k1 = kspec, (k2, k3) = (kf, ks)
        return psi_lab(kspec, kf, ks, D, y)*J
    else:             # k3 = kspec, (k1, k2) = (kf, ks)
        return psi_lab(kf, ks, kspec, D, y)*J

def norm_full(D, y):
    """||psi||^2 on the fibre (Lebesgue dk1 dk3), independent of D, y."""
    k = np.linspace(-1.2, 1.2, 1601); h = k[1]-k[0]
    K1, K3 = np.meshgrid(k, k, indexing='ij')
    return np.sum(np.abs(psi_lab(K1, P-K1-K3, K3, D, y))**2)*h*h

out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

pr('R9-3 script 1: packing operator B_%s on cluster-translated states; m=%.2f kappa=%.2f lam=%.2f P=%.2f conf=%s kc=%s sk=%.3f'
   % (pair, m, KAP, LAM, P, conf, kc, sk))
t0 = time.time()
# spectator k-range (packet support, padded)
ks_c = kc[0] if pair == 'b' else kc[2]
klo, khi = ks_c - 7*sk - 0.08, ks_c + 7*sk + 0.08
nrm0 = None
for D in Ds:
    y = {'2+1': 0.0, 'centre': D/2.0, 'far1': -float(D)}[conf] if pair == 'b' else 0.0
    if nrm0 is None: nrm0 = np.sqrt(norm_full(D, y))
    # q-grid on (0, kappa): resolve oscillation ~ e^{i q D}
    Nq = int(max(60, ppo*KAP*(D + 30)/(2*np.pi)))
    dq = KAP/Nq; q = (np.arange(Nq) + 0.5)*dq
    Mo = np.diag(M0f(q)) + LAM*2*dq*np.outer(g(q), g(q))
    mu, chi = np.linalg.eigh(Mo)
    nu = M0f(q)
    # fine spectator grid; oscillation frequency in k_spec up to ~ D (conservative)
    om = max(D, 20) + 30
    hf = min(2e-3, 0.08/om); kf_ = np.arange(klo - 0.12, khi + 0.12 + hf, hf)
    # odd part of state on G, rows = q_i, cols = k
    Q, Kf = np.meshgrid(q, kf_, indexing='ij')
    psi_o = (psi_pair(Kf, Q, D, y) - psi_pair(Kf, -Q, D, y))/np.sqrt(2)*np.sqrt(dq)
    c = chi.T @ psi_o                          # c_n(k)
    # output grid
    ho = min(4e-3, 0.25/om); ko = np.arange(klo, khi + ho, ho)
    Qn = np.array([q1f(kf_, mun) for mun in mu])          # (n, k_fine) tabulated q1 for each mu_n
    Tj = np.array([q1f(ko, nuj) for nuj in nu])           # (j, k_out) targets
    dTj = np.array([dq1f(ko, nuj) for nuj in nu])
    res = np.zeros((Nq, len(ko)), complex)
    for n in range(Nq):
        # invert q1(P, k'; mu_n) = T_j(k): interp + one Newton step
        kp = np.interp(Tj, Qn[n], kf_)
        kp = kp - (q1f(kp, mu[n]) - Tj)/dq1f(kp, mu[n])
        jac = np.sqrt(dTj/dq1f(kp, mu[n]))
        csr = CubicSpline(kf_, c[n].real); csi = CubicSpline(kf_, c[n].imag)
        val = (csr(kp) + 1j*csi(kp))*jac
        res += chi[:, n][:, None]*val
    # identity part evaluated on the output grid directly (exact, no interpolation)
    Qo, Ko = np.meshgrid(q, ko, indexing='ij')
    psi_out = (psi_pair(Ko, Qo, D, y) - psi_pair(Ko, -Qo, D, y))/np.sqrt(2)*np.sqrt(dq)
    diff = res - psi_out
    rn = np.sqrt(np.sum(np.abs(diff)**2)*ho)/nrm0
    wG = np.sqrt(np.sum(np.abs(psi_out)**2)*ho)/nrm0
    # bound-state component weight of the odd-G part
    pr('D = %4d  Nq = %4d  Nkf = %6d  Nko = %5d : ||(B_%s - 1)psi_D||/||psi|| = %.4e   [odd-G weight %.3e; mu_b = %.8f]  [%.0f s]'
       % (D, Nq, len(kf_), len(ko), pair, rn, wG, mu[0], time.time()-t0))
fn = __file__.replace('.py', '_%s_%s_P%.2f%s.out' % (pair, conf, P, tag))
open(fn, 'w').write('\n'.join(out) + '\n')
