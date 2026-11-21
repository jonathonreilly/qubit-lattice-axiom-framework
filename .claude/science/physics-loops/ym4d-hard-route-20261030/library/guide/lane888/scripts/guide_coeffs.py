# GUIDE only: arithmetic check of Theorem 3.3 constants (pure python, no external data)
import math
def I(nu, x, terms=60):
    s = 0.0
    for k in range(terms):
        s += (x/2)**(2*k+nu) / (math.factorial(k)*math.factorial(k+nu))
    return s
def r(j2, beta):  # j2 = 2j ; r_j = I_{2j+1}/I_1
    return I(j2+1, beta)/I(1, beta)
def rV2T(beta):
    return (2*math.sinh(beta)+8*math.sinh(beta/2))/(2*math.cosh(beta)+6+16*math.cosh(beta/2))
v = lambda x: (1+x)/(1-x)
print("beta  r12      qS       gamma    S        D12      D52      4(D52-D12)  bstar   dsig12/b^2 dsig52/b^2")
for beta in (2.3, 2.4, 2.5, 2.6):
    r12 = r(1, beta); r1 = r(2, beta); r2 = r(4, beta); r3 = r(6, beta); r52 = r(5, beta)
    qS = rV2T(beta); gam = math.log(qS/r12); S = qS/r52
    rho = r12**4
    D12 = v(r12**2)/16 + 3*v(r1*r12**2)/16 - v(rho)/4
    x2 = r2*r12**3/qS; x3 = r3*r12**3/qS
    D52 = 5*v(x2)/48 + 7*v(x3)/48 - v(rho)/4
    bst = math.sqrt(gam/(2*(D12-D52)))
    print(f"{beta:.1f}  {r12:.5f}  {qS:.5f}  {gam:.5f}  {S:7.1f}  {D12:+.5f} {D52:+.5f} {4*(D52-D12):+.4f}    {bst:.4f}  {-2*D12:+.5f}  {-2*D52:+.5f}")
