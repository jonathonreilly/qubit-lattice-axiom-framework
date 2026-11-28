# Guide only (no proof step uses it). Pure-Python importance sampling of
# J_+(s) = int_{SU(2)^4} exp(-s sum_{i<j} a([h_i,h_j])) dh, a([h,k]) = 2|u x v|^2.
# J_+ = 4 int_0^1 w(r) psi(r,s) dr, u_1 = r e_z the largest vector part, w(r) = 4r^2/(pi sqrt(1-r^2)).
# Prediction from the scaling limit: s^3 J_+(s) = kappa log s + O(1), kappa = I_b/(2 pi^4),
# I_b = int_{[-1,1]^3} (1+|b|^2)^(-2) db.  Also prints J_+/R(s), R the 1D reduction of (2).
import math, random, sys
rng = random.Random(20261118)

def psi(r, s, N):
    tau2 = min(1.0/(4*s*r*r), r*r); tau = math.sqrt(tau2)
    c0 = math.log(4*math.pi*r*tau2) - 2*math.log(math.pi)
    k = -2*s*r*r + 1.0/(2*tau2)
    r2 = r*r; acc = 0.0; acc2 = 0.0
    U = rng.uniform; G = rng.gauss; L1 = math.log1p; E = math.exp
    for _ in range(N):
        lw = 0.0; us = []
        for j in range(3):
            a = U(-r, r); vx = G(0.0, tau); vy = G(0.0, tau)
            n2 = a*a + vx*vx + vy*vy
            if n2 > r2:
                us = None; break
            lw += c0 - 0.5*L1(-n2) + k*(vx*vx + vy*vy)
            us.append((vx, vy, a))
        if us is None:
            continue
        e = 0.0
        for (p, q) in ((0, 1), (0, 2), (1, 2)):
            A = us[p]; B = us[q]
            cx = A[1]*B[2]-A[2]*B[1]; cy = A[2]*B[0]-A[0]*B[2]; cz = A[0]*B[1]-A[1]*B[0]
            e += cx*cx + cy*cy + cz*cz
        val = E(lw - 2.0*s*e); acc += val; acc2 += val*val
    m = acc/N
    return m, math.sqrt(max(acc2/N - m*m, 0.0)/N)

def simpson_nodes(a, b, n):
    h = (b - a)/n
    return [(a + i*h, h/3*(1 if i in (0, n) else (4 if i % 2 else 2))) for i in range(n+1)]

def J(s, N):
    tot = 0.0; var = 0.0
    for (l, wq) in simpson_nodes(math.log(2.0), math.log(2.0) + 0.25*math.log(s) + 6.0, 32):
        r = math.exp(-l); jac = 4*r**3/(math.pi*math.sqrt(1 - r*r))
        m, se = psi(r, s, N); tot += wq*jac*m; var += (wq*jac*se)**2
    for (th, wq) in simpson_nodes(math.asin(0.5), math.pi/2, 12):
        r = min(math.sin(th), 1 - 1e-9); jac = 4*math.sin(th)**2/math.pi
        m, se = psi(r, s, N); tot += wq*jac*m; var += (wq*jac*se)**2
    return 4*tot, 4*math.sqrt(var)

def R(s):
    tot = 0.0
    for (th, wq) in simpson_nodes(0.0, math.pi/2, 4000):
        r = math.sin(th); tot += wq*r**11/(1 + s*r**4)**3
    return tot

n = 80; h = 1.0/n; Ib = 0.0
for i in range(n):
    x = (i + 0.5)*h
    for j in range(n):
        y = (j + 0.5)*h; xy = 1 + x*x + y*y
        for kk in range(n):
            z = (kk + 0.5)*h; Ib += 1.0/(xy + z*z)**2
Ib *= 8*h**3
kappa = Ib/(2*math.pi**4)
print(f"I_b = {Ib:.5f}; kappa = I_b/(2 pi^4) = {kappa:.5e}", flush=True)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
data = []
for s in [1e2, 1e3, 1e4, 1e5, 1e6, 1e8]:
    j, se = J(s, N); data.append((s, j, se))
    print(f"s={s:.0e}  J+={j:.4e} (se {se:.1e})  s^3 J+={s**3*j:.4e}  kappa*log s={kappa*math.log(s):.4e}  J+/R={j/R(s):.3f}", flush=True)
(s1, j1, _), (s2, j2, _) = data[2], data[-1]
print(f"slope of s^3 J+ against log s between s=1e4 and 1e8: {(s2**3*j2 - s1**3*j1)/math.log(s2/s1):.4e} (kappa {kappa:.4e})")
