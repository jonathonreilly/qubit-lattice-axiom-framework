"""R19-15 probe (d): radiative stability of a one-loop shear zero, in one stated model.
Model: NN lattice scalar, eps^2 = m^2 + sum 2(1 - cos k_i), on-site (lambda/4!) phi^4, strain-blind vertex,
strain acting on the one-particle dispersion by the SF pullback eps_t = eps o Phi_t (R14-3 / RN-L1 flow,
v = (1/2) h.f, f = sin k). Vacuum energy per site to O(lambda^2):
  E0(t)  = (1/2) < eps_t >                                  (one loop; its Hessian is the archived mu)
  E1(t)  = (lambda/8) G_t^2,  G_t = < 1/(2 eps_t) >          (figure-eight / Hartree)
  E2b(t) = -(lambda^2/48) int dtau sum_x G_t(x,tau)^4        (basketball; the only O(lambda^2) piece that
                                                              is not a single-momentum functional of eps_t)
Claims tested:
 (i)  T2g: E0, E1 and every single-momentum functional of eps_t are t-independent (Liouville);
      the basketball is not, because momentum conservation k1+..+k4 = 0 is not preserved by a nonlinear flow.
 (ii) E_g: E1's Hessian is (lambda/4) G G''; at fixed unstrained PHYSICAL mass it cancels against the
      mass-counterterm term -(lambda/4) G(0) G''  (Hartree shift = mass renormalization).
"""
import sys, time, numpy as np
T0 = time.time()

def disp(kx, ky, kz, m):
    return np.sqrt(m*m + 6 - 2*np.cos(kx) - 2*np.cos(ky) - 2*np.cos(kz))

def flowE(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    def one(x, s):
        h = s/nst
        for _ in range(nst):
            a = F(x); b = F(x + 0.5*h*a); c = F(x + 0.5*h*b); d = F(x + h*c)
            x = x + h*(a + 2*b + 2*c + d)/6
        return x
    return one(kx, t), one(ky, -t)

def flowT(kx, ky, t, nst=20):
    F = lambda y: 0.5*np.sin(y)
    h = t/nst; x, y = kx.copy(), ky.copy()
    for _ in range(nst):
        a1, a2 = F(y), F(x)
        b1, b2 = F(y + 0.5*h*a2), F(x + 0.5*h*a1)
        c1, c2 = F(y + 0.5*h*b2), F(x + 0.5*h*b1)
        d1, d2 = F(y + h*c2), F(x + h*c1)
        x, y = x + h*(a1 + 2*b1 + 2*c1 + d1)/6, y + h*(a2 + 2*b2 + 2*c2 + d2)/6
    return x, y

def eps_t(N, m, t, chan):
    k = 2*np.pi*np.arange(N)/N
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    if t != 0.0:
        KX, KY = (flowE if chan == 'E' else flowT)(KX, KY, t)
    return disp(KX, KY, KZ, m)

# Gauss-Legendre in u on [0,1], tau = -ln(u)/a  (a = decay scale), fixed for all t
def tau_nodes(nq, a):
    x, w = np.polynomial.legendre.leggauss(nq)
    u = 0.5*(x + 1); wu = 0.5*w
    return -np.log(u)/a, wu/(a*u)

def pieces(N, m, t, chan, taus, wts):
    e = eps_t(N, m, t, chan)
    E0 = 0.5*e.mean(); G = (1/(2*e)).mean()
    B = 0.0
    for tau, w in zip(taus, wts):
        Gx = np.fft.ifftn(np.exp(-e*tau)/(2*e)).real      # G_t(x, tau), x on the lattice
        B += w*(Gx**4).sum()
    return E0, G, 2*B   # 2B: tau over (-inf, inf)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 20
nq = int(sys.argv[2]) if len(sys.argv) > 2 else 120
for m in (1.0, 0.6):
    taus, wts = tau_nodes(nq, 2.0*m)
    print('N=%d nq=%d m=%.2f' % (N, nq, m), flush=True)
    for chan in ('E', 'T'):
        res = {}
        for d in (0.04, 0.02):
            vals = [pieces(N, m, s, chan, taus, wts) for s in (-d, 0.0, d)]
            res[d] = [(vals[2][i] - 2*vals[1][i] + vals[0][i])/d**2 for i in range(3)]
            base = vals[1]
        rich = [(4*res[0.02][i] - res[0.04][i])/3 for i in range(3)]
        E0pp, Gpp, Bpp = rich
        G0, B0 = base[1], base[2]
        print('  %s: E0\'\' = %+.6e   G = %.8f  G\'\' = %+.6e   B = %.6e  B\'\' = %+.6e' % (chan, E0pp, G0, Gpp, B0, Bpp))
        print('      O(lambda) Hessian, bare-mass convention  (lambda/4) G G\'\' = lambda * %+.6e' % (0.25*G0*Gpp))
        print('      O(lambda) Hessian, physical-mass convention (G\'^2 term only) = 0 at t=0 (G\'(0)=0 by cubic symmetry)')
        print('      O(lambda^2) basketball Hessian  -(1/48) B\'\' = lambda^2 * %+.6e' % (-Bpp/48), flush=True)
print('runtime %.1fs' % (time.time() - T0))
