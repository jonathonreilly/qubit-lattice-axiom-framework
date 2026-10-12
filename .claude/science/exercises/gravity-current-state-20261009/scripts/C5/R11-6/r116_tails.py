"""R11-6 large-r subtracted-tail components (lab chart at fixed P, R9-3 conventions B_c = R_0^dag R_M; d = 1).

Polar Sokolov packing B = A (A^dag A)^(-1/2), A = B_a + E, E = (B_b - 1) + (B_c - 1).  Proved bound (report Sec. 3):
   ||(B - B_a) psi|| <= e1 + (1+||E||)/(s(1+s)) * [ (1+||E||) e1 + e2 ],   s = s_min(A),
   e1 = ||E psi|| <= ||(B_b-1)psi|| + ||(B_c-1)psi||,   e2 = ||E^dag B_a psi|| <= ||(B_b^dag-1)B_a psi|| + ||(B_c^dag-1)B_a psi||.
Generator part: also e3 = ||D psi'|| for D = Lambda (M_(b)-M0 + M_(c)-M0) Lambda^dag on the a-cluster state B_a psi.
State (channel a = (12)(3)): psi_r(k3, q12) = chi_b(q12) G(k3) exp(-i k3 r)  [bound dimer (x) spectator packet], an
exact product state of H_a = H_12 + eps_3 in the lab a-chart; B_a psi_r is evaluated analytically.
Each operator is evaluated on the odd-G sector of its own chart (exact reduction Bc - 1 = Q_G (Bc - 1) Q_G, vR9-3:1).
"""
import numpy as np, sys, time
from scipy.interpolate import CubicSpline
args = dict(a.split('=') for a in sys.argv[1:])
m = 0.3; KAP = 0.25; LAM = -3.0*float(dict(a.split("=") for a in sys.argv[1:]).get("lamfac", 1.0))
P = float(args.get('P', 0.4))
rs = [float(x) for x in args.get('rs', '20,40,80,160,320,640').split(',')]
ch = args.get('ch', 'b')                 # channel whose packing is applied: 'b' (pair 23, spec 1) or 'c' (pair 31, spec 2)
op = args.get('op', 'B')                 # 'B': (B_c-1) psi ; 'Bdag': (B_c^dag-1) B_a psi ; 'D': D_c B_a psi ; 'BH': (B_c-1)(H_a psi)
ppo = float(args.get('ppo', 12.0)); HFAC = float(args.get('hfac', 0.03))
k3c = float(args.get('k3c', 0.040)); sig = float(args.get('sig', 0.08))
tag = args.get('tag', '')

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def g(q): return q*sstep(1.0 - (q/KAP)**2)/KAP
def eps(k): return np.sqrt(m*m + k*k)
def M0f(q): return 2*np.sqrt(m*m + q*q)
def phi(k, mu):          # lab spectator k -> rest-frame u (pair lab momentum P-k, pair mass mu)
    E = np.sqrt(mu*mu + (P-k)**2) + eps(k); Th = np.arctanh(P/E)
    return m*np.sinh(np.arcsinh(k/m) - Th)
def dphi(k, mu):
    Ep = np.sqrt(mu*mu + (P-k)**2); E = Ep + eps(k); Th = np.arctanh(P/E)
    dE = -(P-k)/Ep + k/eps(k); dTh = -P*dE/(E*E - P*P)
    return m*np.cosh(np.arcsinh(k/m) - Th)*(1/eps(k) - dTh)
def phiinv(u, mu):
    Mr = np.sqrt(mu*mu + u*u) + eps(u); Th = np.arcsinh(P/Mr)
    return m*np.sinh(np.arcsinh(u/m) + Th)
def pair_momenta(Pp, q):
    v = np.arcsinh(q/m); Y = np.arcsinh(Pp/(2*m*np.cosh(v)))
    return m*np.sinh(Y+v), m*np.sinh(Y-v)
def q_of(kf, ks): return m*np.sinh(0.5*(np.arcsinh(kf/m) - np.arcsinh(ks/m)))
def J(kspec, q):         # |d k_f / d q| at fixed spectator lab momentum and total P
    Pp = P - kspec; kf, ks = pair_momenta(Pp, q); v = np.arcsinh(q/m)
    return 1.0/(0.5*m*np.cosh(v)*(1/eps(kf) + 1/eps(ks)))

# continuum dimer (odd sector): chi_b(q) = N g(q)/(M0(q) - mu_b), mu_b from a fine quadrature
qq = (np.arange(40000)+0.5)*KAP/40000; dqq = KAP/40000
from scipy.optimize import brentq
mub = brentq(lambda mu: 1 + LAM*np.sum(2*dqq*g(qq)**2/(M0f(qq) - mu)), 0.2, 2*m - 1e-9)
Nb = 1.0/np.sqrt(np.sum(2*dqq*(g(qq)/(M0f(qq) - mub))**2))   # norm over full line (odd)
def chib(q): return Nb*g(q)/(M0f(q) - mub)
def Eb(k): return np.sqrt(mub*mub + (P-k)**2) + eps(k)

def G(k, r): return np.exp(-(k - k3c)**2/(4*sig*sig))*np.exp(-1j*k*r)
def psi_a(k3, q, r, mult=None):
    v = chib(q)*G(k3, r)
    return v if mult is None else v*mult(k3)
def Bapsi_a(k3, q, r, mult=None):
    """(B_a psi)(k3, q) = chi_b(q) (R_{mu_b} G)(phi_nu(k3)) sqrt(phi_nu'(k3)),  nu = M0(q)."""
    nu = M0f(q); u = phi(k3, nu); kk = phiinv(u, mub)
    Gv = G(kk, r)*(1.0 if mult is None else mult(kk))
    return chib(q)*Gv/np.sqrt(dphi(kk, mub))*np.sqrt(dphi(k3, nu))
def eval_in_chart(fa, ks, q, r, mult=None):
    """chart (ch) point (k_spec, q) -> a-chart value with half-density factor sqrt(J_c/J_a)."""
    kf, kss = pair_momenta(P - ks, q)
    if ch == 'b': k1, k2, k3 = ks, kf, kss
    else:         k2, k3, k1 = ks, kf, kss
    q12 = q_of(k1, k2)
    return fa(k3, q12, r, mult)*np.sqrt(J(ks, q)/J(k3, q12))

# total norm of psi (a-chart quadrature)
def norm_a(fa, r, mult=None):
    k = np.linspace(k3c - 9*sig, k3c + 9*sig, 3001); q = (np.arange(4000)+0.5)*KAP/4000
    K, Q = np.meshgrid(k, q, indexing='ij')
    v = fa(K, Q, r, mult); return np.sqrt(2*np.sum(np.abs(v)**2)*(k[1]-k[0])*(q[1]-q[0]))

# spectator range of the chosen channel on the state's support
Ks, Qs = np.meshgrid(np.linspace(k3c - 7*sig, k3c + 7*sig, 201), np.linspace(-KAP, KAP, 201), indexing='ij')
k1s, k2s = pair_momenta(P - Ks, Qs)
spec = k1s if ch == 'b' else k2s
klo, khi = spec.min() - 0.06, spec.max() + 0.06

out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)
pr('R11-6 tails: ch=%s op=%s P=%.2f mu_b=%.8f k3c=%.3f sig=%.3f spectator range [%.3f, %.3f] ppo=%.1f hfac=%.3f'
   % (ch, op, P, mub, k3c, sig, klo, khi, ppo, HFAC))
t0 = time.time()
fa = Bapsi_a if op in ('Bdag', 'D') else psi_a
mult = Eb if op == 'BH' else None
for r in rs:
    nrm = norm_a(psi_a, r, mult)
    Nq = int(max(60, ppo*KAP*(r + 40)/(2*np.pi)))
    dq = KAP/Nq; q = (np.arange(Nq) + 0.5)*dq
    Mo = np.diag(M0f(q)) + LAM*2*dq*np.outer(g(q), g(q))
    mu, chi = np.linalg.eigh(Mo); nu = M0f(q)
    om = max(r, 20) + 40
    hf = min(2e-3, HFAC/om); kf_ = np.arange(klo - 0.10, khi + 0.10 + hf, hf)
    ho = min(4e-3, 0.25/om); ko = np.arange(klo, khi + ho, ho)
    Q, Kf = np.meshgrid(q, kf_, indexing='ij')
    f_o = (eval_in_chart(fa, Kf, Q, r, mult) - eval_in_chart(fa, Kf, -Q, r, mult))/np.sqrt(2)*np.sqrt(dq)   # (Nq, Nkf)
    Qo, Ko = np.meshgrid(q, ko, indexing='ij')
    f_out = (eval_in_chart(fa, Ko, Qo, r, mult) - eval_in_chart(fa, Ko, -Qo, r, mult))/np.sqrt(2)*np.sqrt(dq)
    res = np.zeros((Nq, len(ko)), complex)
    if op in ('B', 'BH'):
        # (B f)_i(k) = sum_n chi_n(q_i) [R_{nu_i}^dag R_{mu_n} c_n](k),  c_n = sum_j chi_n(q_j) f_j
        c = chi.T @ f_o
        Qn = np.array([phi(kf_, mun) for mun in mu])
        Tj = np.array([phi(ko, nuj) for nuj in nu]); dTj = np.array([dphi(ko, nuj) for nuj in nu])
        for n in range(Nq):
            kp = np.interp(Tj, Qn[n], kf_); kp = kp - (phi(kp, mu[n]) - Tj)/dphi(kp, mu[n])
            jac = np.sqrt(dTj/dphi(kp, mu[n]))
            cs = CubicSpline(kf_, c[n])
            res += chi[:, n][:, None]*cs(kp)*jac
        diff = res - f_out
    elif op == 'Bdag':
        # (B^dag f)_i(k) = sum_n chi_n(q_i) sum_j chi_n(q_j) [R_{mu_n}^dag R_{nu_j} f_j](k);
        # (R_mu^dag R_nu f)(k) = f(k'') sqrt(phi_mu'(k)/phi_nu'(k'')),  phi_nu(k'') = phi_mu(k)
        Qnu = np.array([phi(kf_, nuj) for nuj in nu])
        S = np.zeros((Nq, len(ko)), complex)
        splines = [CubicSpline(kf_, f_o[j]) for j in range(Nq)]
        for n in range(Nq):
            tn = phi(ko, mu[n]); dtn = dphi(ko, mu[n])
            acc = np.zeros(len(ko), complex)
            for j in range(Nq):
                kpp = np.interp(tn, Qnu[j], kf_); kpp = kpp - (phi(kpp, nu[j]) - tn)/dphi(kpp, nu[j])
                acc += chi[j, n]*splines[j](kpp)*np.sqrt(dtn/dphi(kpp, nu[j]))
            S[n] = acc
        res = chi @ S
        diff = res - f_out
    elif op == 'D':
        # Lambda (M_(c) - M0) Lambda^dag in the lab chart = R_0^dag F R_0, F(u) = sum_n chi_n chi_n^T sqrt(mu_n^2+u^2) - diag sqrt(nu^2+u^2)
        # step 1: R_0: g_j(u) = f_j(phiinv_nu_j(u)) / sqrt(phi_nu_j'(k)), on a u-grid; step 2: F(u); step 3: R_0^dag to k_out
        ulo = min(phi(np.array([klo - 0.1]), nuj)[0] for nuj in nu); uhi = max(phi(np.array([khi + 0.1]), nuj)[0] for nuj in nu)
        ug = np.arange(ulo, uhi + hf, hf)
        gj = np.zeros((Nq, len(ug)), complex)
        for j in range(Nq):
            kk = phiinv(ug, nu[j]); gj[j] = CubicSpline(kf_, f_o[j])(kk)/np.sqrt(dphi(kk, nu[j]))
        # F(u) g(u): sum_n chi_n (chi_n . g) sqrt(mu_n^2+u^2) - sqrt(nu^2+u^2) g
        cn = chi.T @ gj
        Fg = chi @ (cn*np.sqrt(mu[:, None]**2 + ug[None, :]**2)) - gj*np.sqrt(nu[:, None]**2 + ug[None, :]**2)
        for i in range(Nq):
            uo = phi(ko, nu[i]); res[i] = CubicSpline(ug, Fg[i])(uo)*np.sqrt(dphi(ko, nu[i]))
        diff = res
    rn = np.sqrt(np.sum(np.abs(diff)**2)*ho)/nrm
    wG = np.sqrt(np.sum(np.abs(f_out)**2)*ho)/nrm
    pr('r = %6.1f  Nq = %4d  Nkf = %6d  Nko = %5d : ||(%s_%s) f_r||/||psi|| = %.4e   [odd-G_%s weight %.3e]  [%.0f s]'
       % (r, Nq, len(kf_), len(ko), {'B': 'B-1', 'Bdag': 'B^dag-1 on B_a', 'D': 'D on B_a', 'BH': 'B-1 on H_a'}[op], ch, rn, ch, wG, time.time()-t0))
fn = __file__.replace('.py', '_%s_%s_P%.2f%s.out' % (ch, op, P, tag))
open(fn, 'w').write('\n'.join(out) + '\n')
