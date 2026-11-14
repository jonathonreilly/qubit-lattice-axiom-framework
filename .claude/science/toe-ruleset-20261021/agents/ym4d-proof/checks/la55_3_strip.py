# la55_3: exact rational interval check of LP Theorem 4.2's strip conditions (EXP-strip P1-P7 + N2-exp's eta_* definition).
# Criteria: la55_3_criteria.md (written first). Fractions only.
from fractions import Fraction as F
from math import factorial, isqrt
import sys
PI_LO = F(314159265358979, 10**14); PI_UP = F(314159265358980, 10**14)
def exp_encl(x, M=20):
    x = F(x); lo = sum(x**m / factorial(m) for m in range(M+1)); return lo, lo + 2*x**(M+1)/factorial(M+1)
def sqrt_encl(q, D=10**18):
    # rational lower/upper bounds of sqrt(q) for rational q >= 0
    q = F(q); num = q.numerator * D * D // q.denominator
    a = isqrt(num); lo = F(a, D)
    while lo*lo > q: lo -= F(1, D)
    up = lo + F(1, D)
    while up*up < q: up += F(1, D)
    return lo, up
def quantities(kappa, khat, L, eta, r0, side):
    # side='up' gives upper bounds of the perturbation quantities; 'lo' gives lower bounds (formula at lower inputs)
    E_lo, E_up = exp_encl(eta)
    C_lo = (E_lo + 1/E_up)/2; C_up = (E_up + 1/E_lo)/2
    if side == 'up': E, C, pi, piR = E_up, C_up, PI_UP, PI_LO
    else:            E, C, pi, piR = E_lo, C_lo, PI_LO, PI_UP
    eps = E - 1; epsp = (pi**2/4)*eps; e5 = (1 + epsp)**5 - 1
    Rbar = 1 + F(khat)/(L*L - 1) + F(kappa)/9
    # b_* = min(kappa, 24/pi^2): for an upper bound of rho use the smaller b_* (pi upper), for a lower bound the larger
    bpi = 24/(pi**2) if side == 'up' else 24/(pi**2)
    bstar = min(F(kappa), bpi)
    sb_lo, sb_up = sqrt_encl(bstar)
    sb = sb_lo if side == 'up' else sb_up
    lam = 1 - 4*F(eta)**2*C**2/9 if side == 'up' else 1 - 4*F(eta)**2*C**2/9
    eZ = (4*F(eta)**2/9 + 4*F(eta)/3)*C
    cZ = (eps*E**4 + 4*E**3*eps*(1 + E))/(9*lam) + eZ/(9*lam)
    eR = F(khat)*eps/(L*L - 1) + F(kappa)*cZ
    rho = e5 + (4*F(eta)**2/bstar + 4*F(eta)/sb)*C*(Rbar + eR) + eR
    return dict(eps=eps, e5=e5, Rbar=Rbar, bstar=bstar, sb=sb, lam=lam, eZ=eZ, cZ=cZ, eR=eR, rho=rho, C=C, pi=pi)
def check_pair(kappa, khat, L, eta, r0):
    kappa, khat, eta, r0 = F(kappa), F(khat), F(eta), F(r0)
    U = quantities(kappa, khat, L, eta, r0, 'up'); Lw = quantities(kappa, khat, L, eta, r0, 'lo')
    Rbar = U['Rbar']
    Gam_up = max(PI_UP**2/4, Rbar); Gam_lo = max(PI_LO**2/4, Rbar)
    PsiU = kappa*(1 - r0**2/6)/(kappa + r0**2*Rbar)
    rho_up, rho_lo = U['rho'], Lw['rho']
    ePsi_up = ((4*eta**2 + 4*eta*r0)*U['C']*(Rbar + U['eR']) + r0**2*U['eR'])/((1 - rho_up)*U['bstar']) + rho_up/(1 - rho_up)
    f0_up = (eta**2*PI_UP**2/r0**2 + 2*eta*PI_UP/r0)*U['C']
    brV_lo = 1/((1 + rho_up)*Gam_up) - f0_up/(1 - rho_up)
    rhs_up = F(1, 2)/((1 + rho_lo)*Gam_lo)
    S1 = rho_up <= F(1, 2); S2 = ePsi_up <= PsiU/2; S3 = brV_lo >= rhs_up; S4 = f0_up <= F(15, 100)
    info = (f"rho_up={float(rho_up):.5f} ePsi_up={float(ePsi_up):.5f} PsiU/2={float(PsiU/2):.5f} "
            f"brV_lo={float(brV_lo):.5f} rhs_up={float(rhs_up):.5f} f0_up={float(f0_up):.5f}")
    return S1 and S2 and S3 and S4, (S1, S2, S3, S4), info
pairs = [(1, 1, F(111, 10000), F(57, 100)), (F(1, 4), 1, F(77, 10000), F(37, 100)), (4, 1, F(117, 10000), F(65, 100)),
         (F(1, 4), 16, F(37, 10000), F(1, 4)), (4, 16, F(82, 10000), F(3, 5))]
allok = True
for (ka, kh, et, r0) in pairs:
    ok, S, info = check_pair(ka, kh, 3, et, r0)
    allok = allok and ok
    print(f"pair kappa={ka} khat={kh} eta={et} r0={r0}: {'PASS' if ok else 'FAIL'} S1..S4={S}  [{info}]")
okc, Sc, infoc = check_pair(1, 1, 3, F(200, 10000), F(57, 100))
print(f"CONTROL kappa=1 khat=1 eta=0.02 r0=0.57: {'PASS' if okc else 'FAIL'} S1..S4={Sc} (designed to FAIL)  [{infoc}]")
print("SUMMARY: all printed pairs PASS =", allok, "| control failed as designed =", not okc)
sys.exit(0 if allok and not okc else 1)
