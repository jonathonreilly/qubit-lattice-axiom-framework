# R10-2: reflection-positivity (OS) tests for k4-slices of Euclidean Z^4 two-point functions.
# For a translation-invariant RP lattice measure, the time-correlator at fixed spatial momentum
# G(tau) = (1/2pi) int F(theta) e^{i theta tau} dtheta must be a moment sequence:
#   site RP:  G(tau) = int_{[-1,1]} lam^|tau| dmu,  mu >= 0   (Hausdorff on [-1,1])
#             necessary & sufficient: H0=[G(i+j)] >= 0 and H2=[G(i+j)-G(i+j+2)] >= 0
#   link RP:  [G(1+i+j)] >= 0 (necessary); with T >= 0 also [G(2+i+j)] >= 0.
# We print min-eig / max-eig of these Hankel matrices for sizes N+1.
import mpmath as mp
mp.mp.dps = 40

def psi(x):
    return mp.e**(-1/x) if x > 0 else mp.mpf(0)
def step(x):  # C^infty, 0 for x<=0, 1 for x>=1, non-analytic at 0 and 1
    a, b = psi(x), psi(1-x)
    return a/(a+b)
def rho(k, b, b2):
    k = abs(k)
    return step((b2 - k)/(b2 - b))
def s_box(k, b=mp.mpf(2.0), b2=mp.mpf(3.1)):       # R7-1/R8-2 matter symbol: = k on |k|<=b
    r = rho(k, b, b2); return r*k + (1-r)*mp.sin(k)
def d_box(k, c1=mp.mpf(1.0), c2=mp.mpf(2.5)):       # R8-5/R9-9 gauge/graviton symbol: = k on |k|<=c1
    r = rho(k, c1, c2); return r*k + (1-r)*2*mp.sin(k/2)

kspat = [mp.mpf('0.3'), mp.mpf('0.2'), mp.mpf('0.1')]
m = mp.mpf('0.5')
c_nn   = sum(4*mp.sin(k/2)**2 for k in kspat) + m**2
c_box  = sum(s_box(k)**2 for k in kspat) + m**2      # = |k|^2+m^2 (inside box)
c_grav = sum(d_box(k)**2 for k in kspat)             # = |q|^2 (massless TT, inside box)

cases = {
  'NN scalar (control, RP)':          (lambda t: 1/(4*mp.sin(t/2)**2 + c_nn), []),
  'box scalar s(k), b=2.0,b2=3.1':    (lambda t: 1/(s_box(t)**2 + c_box), [mp.mpf(2.0), mp.mpf(3.1)]),
  'box TT graviton d(q), c1=1,c2=2.5':(lambda t: 1/(d_box(t)**2 + c_grav), [mp.mpf(1.0), mp.mpf(2.5)]),
  'SLAC scalar 1/(th^2+c) on (-pi,pi]':(lambda t: 1/(t**2 + c_box), []),
  'SLAC TT graviton 1/(th^2+|q|^2)':  (lambda t: 1/(t**2 + c_grav), []),
}
for alpha in ['0.05', '0.5']:
    a = mp.mpf(alpha)
    cases['SLAC scalar + contact %s*th^2' % alpha] = ((lambda a: (lambda t: 1/(t**2 + c_box) + a*t**2))(a), [])

def G_of(F, brk, tmax):
    pts = [mp.mpf(0)] + brk + [mp.pi]
    return [mp.quad(lambda t: F(t)*mp.cos(n*t), pts)/mp.pi for n in range(tmax+1)]

def mineig(M):
    E = mp.eigsy(mp.matrix(M), eigvals_only=True)
    E = sorted([E[i] for i in range(len(E))])
    return E[0], E[-1]

Nmax = 9
print('fixed spatial momentum k=(0.3,0.2,0.1); m=0.5 (scalar), massless TT; mp.dps=40')
for name, (F, brk) in cases.items():
    G = G_of(F, brk, 2*Nmax+3)
    print('\n== %s ==' % name)
    print('  G(0..6) =', [mp.nstr(g, 8) for g in G[:7]])
    for N in [1, 2, 3, 5, 7, 9]:
        H0 = [[G[i+j] for j in range(N+1)] for i in range(N+1)]
        H2 = [[G[i+j]-G[i+j+2] for j in range(N+1)] for i in range(N+1)]
        L1 = [[G[1+i+j] for j in range(N+1)] for i in range(N+1)]
        L2 = [[G[2+i+j] for j in range(N+1)] for i in range(N+1)]
        out = []
        for lab, M in [('siteH0', H0), ('siteH2', H2), ('linkG1', L1), ('linkG2', L2)]:
            lo, hi = mineig(M)
            out.append('%s %s' % (lab, mp.nstr(lo/hi, 3)))
        print('  N=%d  min/max eig: ' % N + ' | '.join(out))
