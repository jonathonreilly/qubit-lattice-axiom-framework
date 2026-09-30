"""T46 kill check K1: independent re-derivation of the QCD transport m_s(2 GeV) -> m_s(m_b) and of
R_common = m_s(mu)/m_b(mu), using
  * coefficients typed from the PDG 2024 quark-mass review (gamma_r, in (alpha_s/4pi)^r) and PDG QCD review (b_i),
    NOT copied from the attacker's qcdrun.py,
  * a fixed-step RK4 in ln mu^2 written here (attacker used scipy DOP853),
  * mass evolution as an integral in coupling space  ln m(a1)/m(a0) = int gamma(a)/beta(a) da (attacker integrated the ODE in mu),
  * decoupling at general mu_b with the log terms of Chetyrkin-Kniehl-Steinhauser (2-loop alpha, 2-loop mass),
    so the threshold-scale dependence can be scanned (attacker fixed mu_b = m_b(m_b)).
Everything in the region 2 GeV -> m_b is nf = 4; only alpha_s(2 GeV) and alpha_s(m_b) depend on the threshold treatment.
"""
import numpy as np
from functools import lru_cache
from scipy.integrate import quad

z3 = 1.2020569031595942
z4 = 1.0823232337111382     # zeta(4) = pi^4/90 (attacker: same)
z5 = 1.0369277551433699

# PDG: mu^2 dm/dmu^2 = -gamma m,  gamma = sum_r gamma_r (a_s/4pi)^r ; mu^2 d a_s/dmu^2 = -sum b_i a_s^(i+2)  (a_s = alpha_s)
def gam_pdg(nl):
    return [4.0,
            202/3 - 20*nl/9,
            1249 + (-2216/27 - 160*z3/3)*nl - 140*nl**2/81,
            4603055/162 + 135680*z3/27 - 8800*z5
            + (-91723/27 - 34192*z3/9 + 880*z4 + 18400*z5/9)*nl
            + (5242/243 + 800*z3/9 - 160*z4/3)*nl**2
            + (-332/243 + 64*z3/27)*nl**3]

def beta_pdg(nl):
    # PDG QCD review (9.2)-(9.3) form: b0=(33-2nf)/(12pi), b1=(153-19nf)/(24pi^2),
    # b2=(2857-5033nf/9+325nf^2/27)/(128pi^3), b3 from the 4-loop numerical PDG expression 29243.0-6946.30nf+405.089nf^2+1.49931nf^3
    b0 = (33-2*nl)/(12*np.pi)
    b1 = (153-19*nl)/(24*np.pi**2)
    b2 = (2857 - 5033*nl/9 + 325*nl**2/27)/(128*np.pi**3)
    b3 = (29243.0 - 6946.30*nl + 405.089*nl**2 + 1.49931*nl**3)/(256*np.pi**4)   # (4pi)^4 -> 256 pi^4 with a_s=alpha_s/(4pi)*... see note
    return [b0, b1, b2, b3]

# work in x = alpha_s/pi.   d x/d ln mu^2 = -sum B_i x^(i+2),  B_i = b_i pi^(i+1)
@lru_cache(None)
def B(nl):
    b = beta_pdg(nl)
    return [b[i]*np.pi**(i+1) for i in range(4)]
# d ln m / d ln mu^2 = -sum G_r x^r, G_r = gamma_r / 4^r
@lru_cache(None)
def G(nl):
    g = gam_pdg(nl)
    return [g[r]/4**(r+1) for r in range(4)]

def dx(x, nl):
    b = B(nl)
    return -(b[0]*x**2 + b[1]*x**3 + b[2]*x**4 + b[3]*x**5)

def run_x(x0, mu0, mu1, nl, n=4000):
    """RK4 in t = ln mu^2"""
    t0, t1 = np.log(mu0**2), np.log(mu1**2)
    h = (t1-t0)/n
    x = x0
    for _ in range(n):
        k1 = dx(x, nl); k2 = dx(x+h*k1/2, nl); k3 = dx(x+h*k2/2, nl); k4 = dx(x+h*k3, nl)
        x += h*(k1+2*k2+2*k3+k4)/6
    return x

def mass_factor(x0, x1, nl):
    """m(x1)/m(x0) = exp( int_{x0}^{x1} gamma(x)/beta(x) dx ), coupling-space integral"""
    Bs, Gs = B(nl), G(nl)
    f = lambda x: sum(Gs[r]*x**(r+1) for r in range(4))/sum(Bs[i]*x**(i+2) for i in range(4))
    val, _ = quad(f, x0, x1, epsabs=1e-13, epsrel=1e-13)
    return np.exp(val)

def decouple_down(x_nf, L):
    """alpha^(nl) = alpha^(nf) * zeta_g^2 ; x=alpha/pi ; L = ln(mu^2/mh(mu)^2). 2-loop, MS-bar heavy mass."""
    return x_nf*(1 - x_nf*L/6 + x_nf**2*(11/72 - 11/24*L + L**2/36))

def mass_decouple_down(x_nf, L):
    """m_l^(nl)/m_l^(nf) 2-loop, MS-bar heavy mass"""
    return 1 + x_nf**2*(89/432 - 5/36*L + L**2/12)

def alpha_low(asMZ=0.1180, MZ=91.1876, mub_over_mb=1.0, mb=4.18):
    """x^(4)(mu) function: run nf=5 from MZ down to mu_b, decouple, return (x4 at mu_b, mu_b)"""
    mub = mub_over_mb*mb
    x5 = run_x(asMZ/np.pi, MZ, mub, 5)
    # heavy mass at mu_b (MS-bar, nf=5 running):
    Lmb = mass_factor(run_x(asMZ/np.pi, MZ, mb, 5), x5, 5)   # m_b(mu_b)/m_b(mb)
    mb_mub = mb*Lmb
    L = np.log(mub**2/mb_mub**2)
    x4 = decouple_down(x5, L)
    return x4, mub

def transport(asMZ=0.1180, mub_over_mb=1.0, mb=4.18, mus=2.0, mut=4.18):
    """T = m_s(mus)/m_s(mut) in the nf=4 theory (no thresholds between 2 GeV and m_b)."""
    x4, mub = alpha_low(asMZ, mub_over_mb=mub_over_mb, mb=mb)
    x_s = run_x(x4, mub, mus, 4)
    x_t = run_x(x4, mub, mut, 4)
    return mass_factor(x_t, x_s, 4), x_s*np.pi, x_t*np.pi

if __name__ == "__main__":
    # sanity: coefficients vs attacker's
    print("B(nl=4) =", B(4), " G(nl=4) =", G(4))
    T, a2, ab = transport()
    print(f"default (as(MZ)=0.1180, mu_b=m_b=4.18): alpha_s^(4)(2 GeV)={a2:.5f} alpha_s^(4)(m_b)={ab:.5f}  T=m_s(2)/m_s(m_b)={T:.5f}")
    print("attacker: alpha_s(2)=0.3014, alpha_s(mb)=0.2246, T=1.18387")
    print("\nthreshold-scale scan (mu_b / m_b), as(MZ)=0.1180:")
    for r in (0.5, 0.7, 1.0, 1.4, 2.0):
        T, a2, ab = transport(mub_over_mb=r)
        print(f"  mu_b={r:3.1f} m_b : alpha_s^(4)(2)={a2:.5f}  alpha_s^(4)(m_b)={ab:.5f}  T={T:.5f}")
    print("\nalpha_s(MZ) scan:")
    for a in (0.1171, 0.1180, 0.1184, 0.1189):
        T, a2, ab = transport(asMZ=a)
        print(f"  as(MZ)={a}: alpha_s^(4)(2)={a2:.5f}  T={T:.5f}")
    # pure one-loop-exponent with the correct alphas, and truncations of the gamma series (same alpha)
    T, a2, ab = transport()
    print(f"\none-loop exponent 12/25 with the 4-loop alpha_s pair: {(a2/ab)**(12/25):.5f}  (lane: 1.138 from 0.2965/0.2265)")
