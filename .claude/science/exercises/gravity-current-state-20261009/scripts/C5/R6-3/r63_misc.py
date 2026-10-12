"""R6-3 misc checks:
(1) elementary bound used in the proof: |D^|^2 <= (8pi/(k w))^2 (g(k+w)+g(|k-w|))^2/4, g(b)=min(1/8,1/|b|);
    and |D^| <= 64 pi/k^3 for |w| <= k/2.  Random-point check + integrated bound constant K in J <= K(1+ln m)/m^2.
(2) null reciprocal vectors of the isotropic Z^4 (form -x0^2+x1^2+x2^2+x3^2): count ~ b X^2 (no log) ->
    Lorentz-random isotropic lattice has Var N(D_T) >= rho^2 b J_D(0) T^6 (counterexample to literal (d)).
(3) fits of Var/(rho V) = F + (a + b lnT)/T^2 to the exact Haar values (T<=108 only, and T<=1e4).
(4) Lambda: delta Lambda / Lambda_obs under R4-5's premises (H1 kappa=1, H2, H4 rho = lbar_P^-4), V = V_lc."""
import numpy as np, sys
sys.path.insert(0, '.')
from r63_formfactor import D_abs2, J
rng = np.random.default_rng(5)

def g(b): return np.minimum(1/8, 1/np.abs(b))
print("(1) bound check on 2e5 random (w,k) in [0.01, 3e3]^2:")
w = 10**rng.uniform(-2, 3.5, 200000); k = 10**rng.uniform(-2, 3.5, 200000)
ex = D_abs2(w, k)
B1 = (8*np.pi/(k*w))**2*(g(k+w) + g(k-w))**2/4
B2 = np.where(w <= k/2, (64*np.pi/k**3)**2, np.inf)
print("    max |D^|^2 / B1 = %.4f ; max over w<=k/2 of |D^|^2/(64pi/k^3)^2 = %.4f" % (np.max(ex/B1), np.max((ex/B2)[w <= k/2])))
for m in (64.0, 1e3, 1e5, 1e7):
    for sgn in (-1, 1):
        e = np.linspace(1e-7, 0.5*np.log(m) + 25, 400001)
        sm = np.sqrt(m)
        if sgn < 0: ww, kk, wt = sm*np.cosh(e), sm*np.sinh(e), 4*np.pi*m*np.sinh(e)**2
        else:       ww, kk, wt = sm*np.sinh(e), sm*np.cosh(e), 4*np.pi*m*np.cosh(e)**2
        b = (8*np.pi/(kk*ww))**2*(g(kk+ww) + g(kk-ww))**2/4
        b = np.minimum(b, np.where(ww <= kk/2, (64*np.pi/kk**3)**2, np.inf))
        b = np.minimum(b, (np.pi/24)**2)
        Jb = np.trapezoid(wt*b, e)
        print("    m=%8.1e %s  J_bound*m^2/(1+ln m) = %8.2f   J_exact*m^2/(1+ln m) = %8.2f" %
              (m, 'tl' if sgn < 0 else 'sl', Jb*m*m/(1+np.log(m)), J(sgn*m, 'D')*m*m/(1+np.log(m))))

print("(2) null vectors of isotropic Z^4: N0(X) = #{n in Z^4\\0: n1^2+n2^2+n3^2 = n0^2, |n0| <= X}")
X = 1500; Nmax = X*X
r1 = np.zeros(Nmax+1); s = np.arange(0, X+1); np.add.at(r1, s*s, 2); r1[0] = 1
n2 = 1 << int(np.ceil(np.log2(3*(Nmax+1))))
R = np.fft.rfft(r1, n2); r3 = np.rint(np.fft.irfft(R**3, n2)[:Nmax+1])
cum = 0; rows = []
for n0 in range(1, X+1):
    cum += 2*r3[n0*n0]
    if n0 in (100, 200, 400, 800, 1500):
        mu0 = 2*np.pi*n0**2     # invariant measure int delta(q^2) d^4q over |q0|<=n0, both sheets
        rows.append((n0, cum, cum/mu0))
for n0, cnt, b in rows: print("    X=%5d  N0=%10d  N0/mu0(|q0|<=X) = %.5f" % (n0, cnt, b))
b_m = rows[-1][2]; J0 = J(-1e-6, 'D')
b_q = b_m/(2*np.pi)**2      # reciprocal lattice of Z^4 is 2 pi Z^4; mu0 scales as Q^2
print("    density b = %.5f per unit mu0 (in q units); J_D(0) = %.4f ; rho = 1 :  Var N(D_T) >= b J_D(0) T^6 = %.4f T^6" % (b_q, J0, b_q*J0))

print("(3) fits Var/(rho V) = F + (a + b ln T)/T^2 to exact Haar values")
d = np.load('r63_Jtable.npz')
exec(open('r63_variance.py').read().split("vol = {'D'")[0])
def VarD(T):
    s = np.sum(CC*Jfun('D', c*tt*T**2)); return rho**2*T**3*(s*T**3)
rho = 1/np.sqrt(7)
for Ts in ((13, 27, 54, 108), (13, 27, 54, 108, 216, 432, 1000, 3000, 10000)):
    Ts = np.array(Ts, float); y = np.array([VarD(T) for T in Ts])/(rho*np.pi*Ts**4/24)
    Amat = np.vstack([np.ones_like(Ts), 1/Ts**2, np.log(Ts)/Ts**2]).T
    sol = np.linalg.lstsq(Amat, y, rcond=None)[0]
    Amat2 = np.vstack([np.ones_like(Ts), 1/Ts**2]).T
    sol2 = np.linalg.lstsq(Amat2, y, rcond=None)[0]
    print("    T in %s: F + (a+b lnT)/T^2 -> F = %.2e ; F + A/T^2 -> F = %.2e" % (list(Ts.astype(int)), sol[0], sol2[0]))

print("(4) Lambda under R4-5 premises (kappa_u = 1, rho = lbar_P^-4, V = V_lc = 6.3894e242 l_P^4)")
lbar4 = (8*np.pi)**2                      # lbar_P^4 / l_P^4
V = 6.3894e242/lbar4                      # in lbar_P^4
Poisson_ratio = 1.389                     # R4-5 (refereed): Delta Lambda / Lambda_obs for Var = rho V
# lattice units a with rho = 1/(sqrt7 a^4) = lbar^-4  ->  V in a^4 = V*sqrt7
Va = V*np.sqrt(7)
Tp = (3*Va/np.pi)**0.25; Td = (24*Va/np.pi)**0.25
varP = 0.48473*Tp**3; rVP = rho*np.pi*Tp**4/3
VD = VarD(Td); rVD = rho*np.pi*Td**4/24
print("    past cone (flat base): T = %.3e a, Var/(rho V) = %.3e  ->  dLambda/Lambda_obs = %.2e" % (Tp, varP/rVP, Poisson_ratio/np.sqrt(varP/rVP)))
print("    diamond of equal 4-volume: T = %.3e a, Var/(rho V) = %.3e  ->  dLambda/Lambda_obs = %.2e" % (Td, VD/rVD, Poisson_ratio/np.sqrt(VD/rVD)))
print("    epoch scaling: dLambda ~ rho/sqrt(Var) ~ T^-1.5 (cone), ~ 1/(T sqrt(ln T)) (diamond), vs H^2 ~ T^-2")
