# nr55_1.py -- exact checks for NODEA_RES55 (criteria: checks/nr55_1_criteria.md, written first).
# Plain python, fractions.Fraction for every verdict. No float in any PASS/FAIL condition.
from fractions import Fraction as Fr
import math

results = []
def gate(name, ok, detail):
    results.append((name, ok))
    print(f"{name}: {'PASS' if ok else 'FAIL'} | {detail}")

# ---------------- G1: GAUSS arithmetic ----------------
def ln2_enclosure(J=40):
    # ln 2 = 2*atanh(1/3) = 2*sum_{j>=0} 3^{-(2j+1)}/(2j+1); tail after J terms <= 2*3^{-(2J+1)}/((2J+1)*(1-1/9))
    s = Fr(0)
    for j in range(J):
        s += Fr(1, 3**(2*j+1)*(2*j+1))
    lo = 2*s
    tail = Fr(2, 3**(2*J+1)*(2*J+1)) / (1 - Fr(1, 9))
    return lo, lo + tail

n_link = 4*8*9**3
r = 3*n_link
h = Fr(r, 2)
lo, hi = ln2_enclosure()
enc = (h*lo, h*hi)
ok = (n_link == 23328 and r == 69984 and h == 34992 and enc[0] >= Fr(242545, 10) and enc[1] <= Fr(242547, 10))
gate("G1", ok, f"n_link={n_link} r={r} h={h} h*ln2 in [{float(enc[0]):.6f}, {float(enc[1]):.6f}]")
n_int = 4*2*3**3
hp = Fr(3*n_int*81, 2)
encp = (hp*lo, hp*hi)
inside = (encp[0] >= Fr(242545, 10) and encp[1] <= Fr(242547, 10))
gate("G1n (control: PLD count must NOT land in the window)", not inside,
     f"n_int={n_int} h'={hp} h'*ln2 in [{float(encp[0]):.4f}, {float(encp[1]):.4f}] (control fires = window rejects it)")

# ---------------- G2: diamond counterexample ----------------
def integ_poly_times_minfun(a):
    # returns (I0, I2, J0, J2) exactly.
    # I0 = int_D 1 = int_{-1}^{1} 2(1-|x|) dx ; I2 = int x^2 2(1-|x|)
    # J0 = int 2 min(a, 1-|x|) dx ; J2 = int x^2 2 min(a, 1-|x|) dx ; by symmetry 2*int_0^1
    def int_pow(p, lo, hi):  # int_lo^hi x^p dx
        return (Fr(hi)**(p+1) - Fr(lo)**(p+1)) / (p+1)
    I0 = 2*2*(int_pow(0, 0, 1) - int_pow(1, 0, 1))
    I2 = 2*2*(int_pow(2, 0, 1) - int_pow(3, 0, 1))
    a = Fr(a)
    if a >= 1:
        J0, J2 = I0, I2
    else:
        c = 1 - a  # on [0, c]: min = a ; on [c, 1]: min = 1 - x
        J0 = 2*2*(a*int_pow(0, 0, c) + (int_pow(0, c, 1) - int_pow(1, c, 1)))
        J2 = 2*2*(a*int_pow(2, 0, c) + (int_pow(2, c, 1) - int_pow(3, c, 1)))
    return I0, I2, J0, J2

I0, I2, J0, J2 = integ_poly_times_minfun(Fr(1, 2))
Delta = J2/J0 - I2/I0
x = Fr(1, 9)
U = 1 + x + x*x
cert = J2/J0 > U*(I2/I0)
ok = ((I0, I2, J0, J2) == (2, Fr(1, 3), Fr(3, 2), Fr(5, 16)) and Delta == Fr(1, 24) and Delta > 0 and cert)
gate("G2", ok, f"I0={I0} I2={I2} J0={J0} J2={J2} Delta={Delta} ; J2/J0={J2/J0} vs U*I2/I0={U*(I2/I0)} (U=1+x+x^2, x=1/9)")
I0a, I2a, J0a, J2a = integ_poly_times_minfun(Fr(1))
Da = J2a/J0a - I2a/I0a
gate("G2n-a (control a=1: Delta>0 must fail)", not (Da > 0), f"Delta(a=1)={Da}")
x2 = Fr(1, 4)
Lb = 1 + x2 + x2*x2/2
cert_b = J2/J0 > Lb*(I2/I0)
gate("G2n-b (control s^2=4: certificate must fail)", not cert_b, f"J2/J0={J2/J0} vs Lb*I2/I0={Lb*(I2/I0)} (Lb=1+x+x^2/2<=e^(1/4))")

# ---------------- G3: Gaussian n=1 derivative-sign certificate ----------------
def exp_lower(y):   # y >= 0 : e^y >= 1 + y + y^2/2
    y = Fr(y); return 1 + y + y*y/2
def expneg_upper(y):  # y >= 0: e^{-y} <= 1/(1 + y + y^2/2)
    return 1/exp_lower(y)
def expneg_lower(y):  # y >= 0: e^{-y} >= 1 - y  (useful only for y<1); also >= 0
    y = Fr(y); return max(Fr(0), 1 - y)

def certificate(eps, sig):
    eps = Fr(eps); sig = Fr(sig)
    # need: e^{-2eps^2} > e^{-eps^2/(2 sig^2)} * (1 + e^{-2 eps^2})
    # multiply by e^{2eps^2}: 1 > e^{2eps^2 - eps^2/(2sig^2)} * (1 + e^{-2eps^2})
    z = eps*eps/(2*sig*sig) - 2*eps*eps  # if z > 0: e^{-z} <= expneg_upper(z)
    if z <= 0:
        return False, "z<=0: certificate not available"
    rhs_upper = expneg_upper(z) * (1 + expneg_upper(2*eps*eps))
    return (rhs_upper < 1), f"z={z} rhs_upper={rhs_upper}"

okc, det = certificate(1, Fr(1, 4))
gate("G3", okc, f"(eps,sig)=(1,1/4): {det}")
# control at (1,1): show certificate fails via a LOWER bound on the RHS >= LHS upper bound
eps, sig = Fr(1), Fr(1)
lhs_upper = expneg_upper(2*eps*eps)                  # e^{-2} <= 1/(1+2+2) = 1/5
rhs_lower = expneg_lower(eps*eps/(2*sig*sig)) * 1     # e^{-1/2} >= 1/2 ; times (1 + e^{-2}) >= 1
cert_fail = rhs_lower >= lhs_upper
gate("G3n (control (1,1): certificate must fail)", cert_fail, f"LHS<= {lhs_upper}, RHS>= {rhs_lower}")
# exact grid identity
viol = 0; viol_ctrl = 0
grid = [Fr(k, 40) for k in range(-120, 121)]
for hh in grid:
    if abs(hh) >= 1:
        continue
    for gg in grid:
        lhs = (abs(gg+hh) >= 1) and (abs(gg-hh) >= 1)
        rhs = abs(gg) >= 1 + abs(hh)
        if lhs != rhs: viol += 1
        rhs2 = abs(gg) >= 1
        if lhs != rhs2: viol_ctrl += 1
gate("G3g", viol == 0, f"violations={viol}")
gate("G3g-n (control must show >=1 violation)", viol_ctrl >= 1, f"control violations={viol_ctrl}")
# CONFIRMATORY float quadrature (no verdict)
def Phibar(x): return 0.5*math.erfc(x/math.sqrt(2))
def phi_of_h(h, e=1.0):
    h = abs(h)
    if h < e: return 2*Phibar(e+h)
    return 1 - 2*((1-Phibar(h+e)) - (1-Phibar(h-e)))
def P_both(sig, e=1.0, n=20001, zmax=10.0):
    s = 0.0; dz = 2*zmax/(n-1)
    for i in range(n):
        z = -zmax + i*dz
        w = math.exp(-z*z/2)/math.sqrt(2*math.pi)
        s += w*phi_of_h(sig*z, e)
    return s*dz
p0, p1 = P_both(0.10), P_both(0.15)
print(f"CONFIRMATORY (float, no verdict): P(both defective) sigma=0.10 -> {p0:.10f}, sigma=0.15 -> {p1:.10f}; decreased: {p1 < p0}")

# ---------------- G4: cubic vertex ----------------
# Gaussian rationals as (re, im) Fractions; 2x2 matrices as tuples; polynomials in t up to degree 3.
def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cscale(s, a): return (s*a[0], s*a[1])
Z = (Fr(0), Fr(0)); O = (Fr(1), Fr(0)); I_ = (Fr(0), Fr(1))
def madd(A, B): return tuple(cadd(A[k], B[k]) for k in range(4))
def mmul(A, B):
    return (cadd(cmul(A[0], B[0]), cmul(A[1], B[2])), cadd(cmul(A[0], B[1]), cmul(A[1], B[3])),
            cadd(cmul(A[2], B[0]), cmul(A[3], B[2])), cadd(cmul(A[2], B[1]), cmul(A[3], B[3])))
def mscale(s, A): return tuple(cscale(s, A[k]) for k in range(4))
ID = (O, Z, Z, O); ZM = (Z, Z, Z, Z)
s1 = (Z, O, O, Z); s2 = (Z, (Fr(0), Fr(-1)), (Fr(0), Fr(1)), Z); s3 = (O, Z, Z, (Fr(-1), Fr(0)))
def imul(A): return tuple(cmul(I_, A[k]) for k in range(4))
X_1, X_2, X_3 = imul(s1), imul(s2), imul(s3)
D = 3
def pexp(X, sign=1):
    # truncated e^{sign*t X}: [I, sX, X^2/2, sX^3/6]
    X2 = mmul(X, X); X3 = mmul(X2, X)
    return [ID, mscale(Fr(sign), X), mscale(Fr(1, 2), X2), mscale(Fr(sign, 6), X3)]
def pmul(P, Qp):
    R = [ZM]*(D+1)
    for i in range(D+1):
        for j in range(D+1-i):
            R[i+j] = madd(R[i+j], mmul(P[i], Qp[j]))
    return R
def ptr(P): return [cadd(P[d][0], P[d][3]) for d in range(D+1)]
def odd_part_coeffs(Xs):
    # U(t) = e^{tX1} e^{tX2} e^{-tX3} e^{-tX4}
    def U(sgn):
        P = pexp(Xs[0], sgn)
        P = pmul(P, pexp(Xs[1], sgn)); P = pmul(P, pexp(Xs[2], -sgn)); P = pmul(P, pexp(Xs[3], -sgn))
        return ptr(P)
    tp, tm = U(1), U(-1)
    return [cadd(tp[d], cscale(Fr(-1), tm[d])) for d in range(D+1)]
c = odd_part_coeffs([X_1, X_2, X_3, ZM])
ok = (c[1] == Z and c[2] == Z and c[3] != Z)
gate("G4", ok, f"odd part coefficients [t^1,t^2,t^3] = {[(str(z[0]), str(z[1])) for z in c[1:]]}")
cab = odd_part_coeffs([X_3, mscale(Fr(2), X_3), mscale(Fr(-1), X_3), X_3])
gate("G4n (control abelian: c3 != 0 must fail)", not (cab[3] != Z), f"abelian c3 = {(str(cab[3][0]), str(cab[3][1]))}")

print("SUMMARY:", sum(1 for _, o in results if o), "/", len(results), "gates report PASS (controls PASS = fired as designed)")
