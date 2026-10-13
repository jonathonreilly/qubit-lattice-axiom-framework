"""C5 R19-17 (c): the order-0 adiabatic vacuum as a MEDIUM on the lattice embedding X^I.
eps(b) = vacuum energy per physical volume of the NN scalar for a lattice with inverse spatial metric
b = diag(b1,b2,b3) in lattice labels (b_i = 1/l_i^2):  eps = sqrt(b1 b2 b3) * (1/2) < sqrt(sum_i b_i g_i + m^2) >,
g_i = 4 sin^2(k_i/2).  (Off-diagonal b, i.e. T2g strain, needs a non-NN stencil: not covered.)
Lagrangian L = -eps(b), b^{IJ} = g^{mu nu} d_mu X^I d_nu X^J.  Expanding X^I = x^I - xi^I about b = 1 (flat g):
  inertia W = 2 eps_{,1} (= rho + p),   longitudinal  c_L^2 = 1 + 4 eps_{,11}/W,
  [110]-transverse (pure E_g strain)  c_T^2 = 1 + 2 (eps_{,11} - eps_{,12})/W.
Checks: fluid limit eps(n) gives c_T^2 = 0 and c_L^2 = n eps''/eps' (sympy); massless NN: c_L^2 = 1/3 exactly."""
import numpy as np, sympy as sp
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

# sympy: fluid-limit check of the two formulas
b1, b2, b3, = sp.symbols('b1 b2 b3', positive=True); nn = sp.Symbol('n', positive=True)
f = sp.Function('f')
n = sp.sqrt(b1*b2*b3); eps = f(n)
d = lambda e, *v: sp.diff(e, *v).subs({b1: 1, b2: 1, b3: 1})
e1, e11, e12 = d(eps, b1), d(eps, b1, b1), d(eps, b1, b2)
W = sp.simplify(2*e1)
cT2 = sp.simplify(1 + 2*(e11 - e12)/W); cL2 = sp.simplify(1 + 4*e11/W)
pr('fluid check: W =', W, '; c_T^2 =', cT2, '; c_L^2 =', cL2, ' (expect 0 and f\'\'(1)/f\'(1))')

def stats(m, N=64):
    k = 2*np.pi*(np.arange(N)+0.5)/N; g = 4*np.sin(k/2)**2
    G1, G2, G3 = np.meshgrid(g, g, g, indexing='ij')
    Q = G1 + G2 + G3 + m*m; sQ = np.sqrt(Q)
    E = 0.5*sQ.mean(); E1 = 0.25*(G1/sQ).mean(); E11 = -0.125*(G1*G1/Q**1.5).mean(); E12 = -0.125*(G1*G2/Q**1.5).mean()
    # eps = n E(b); n_i = 1/2, n_11 = -1/4, n_12 = +1/4 at b = 1
    eps0 = E; eps1 = 0.5*E + E1
    eps11 = -0.25*E + 2*0.5*E1 + E11
    eps12 = 0.25*E + 0.5*E1 + 0.5*E1 + E12
    W = 2*eps1; p = W - eps0
    return eps0, p, W, 1 + 4*eps11/W, 1 + 2*(eps11 - eps12)/W

for m in (0.0, 0.1, 0.5, 1.0, 3.0):
    for N in (48, 64):
        rho, p, W, cL2, cT2 = stats(m, N)
        pr(f'm={m:3.1f} N={N}: rho={rho:.6f} p={p:.6f} w=p/rho={p/rho:.6f}  W={W:.6f}  c_L^2={cL2:.6f}  c_T^2([110],E_g)={cT2:.6f}')
# finite-difference cross-check of eps(b) second derivatives (massless, N=48)
def epsb(b, m=0.0, N=48):
    k = 2*np.pi*(np.arange(N)+0.5)/N; g = 4*np.sin(k/2)**2
    G1, G2, G3 = np.meshgrid(g, g, g, indexing='ij')
    return np.sqrt(b[0]*b[1]*b[2])*0.5*np.sqrt(b[0]*G1 + b[1]*G2 + b[2]*G3 + m*m).mean()
h = 1e-3; e0 = epsb([1, 1, 1])
f11 = (epsb([1+h, 1, 1]) - 2*e0 + epsb([1-h, 1, 1]))/h**2
f12 = (epsb([1+h, 1+h, 1]) - epsb([1+h, 1-h, 1]) - epsb([1-h, 1+h, 1]) + epsb([1-h, 1-h, 1]))/(4*h*h)
f1 = (epsb([1+h, 1, 1]) - epsb([1-h, 1, 1]))/(2*h)
pr(f'finite-difference (m=0,N=48): W={2*f1:.6f} c_L^2={1+4*f11/(2*f1):.6f} c_T^2={1+2*(f11-f12)/(2*f1):.6f}')
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
