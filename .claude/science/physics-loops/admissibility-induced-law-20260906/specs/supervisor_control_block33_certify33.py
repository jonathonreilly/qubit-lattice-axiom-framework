"""Exact rational super-solutions for the restricted count (at most one processed up-child at every node): block 25's recursion with
the up-factor (1 + xU)^n replaced by U_n := (1 + xA U)^n + n xP U (1 + xA U)^(n-1), xP = t, xA = eps2/t^c, y = eps1/t^3:
D = U_2 (1 + 3xD)(1 + yF)^6, U = U_3 (1 + yF)^6, F = U_3 (1 + 3xD)(1 + yF)^5, R = U_3 (1 + 3xD)(1 + yF)^6, x = xP + xA.
'none' restores (1 + xU)^n (block 25/30's recursion)."""
import sys, numpy as np
from fractions import Fraction as F
def devs(p, q, r):
    p, q, r = F(p), F(q), F(r)
    return (1 - p**3/(p**3+q**3+4*r**3), 1 - p**2*q/(p*q*(p+q)+4*r**3), 1 - p**2*r/(r*(p**2+q**2)+r**2*(p+q)+2*r**3))
def upf(n, xP, xA, U, variant):
    if variant == "none": return (1 + (xP + xA) * U) ** n
    return (1 + xA * U) ** n + n * xP * U * (1 + xA * U) ** (n - 1)
def rhs(xP, xA, y, D, U, Fv, variant):
    x = xP + xA
    return (upf(2, xP, xA, U, variant) * (1 + 3 * x * D) * (1 + y * Fv) ** 6,
            upf(3, xP, xA, U, variant) * (1 + y * Fv) ** 6,
            upf(3, xP, xA, U, variant) * (1 + 3 * x * D) * (1 + y * Fv) ** 5)
def certificate(xP, xA, y, variant):
    xp, xa, yf = float(xP), float(xA), float(y); D = U = Fv = 1.0
    for i in range(40000):
        D2, U2, F2 = rhs(xp, xa, yf, D, U, Fv, variant)
        if max(D2, U2, F2) > 1e9: return None
        if abs(D2 - D) + abs(U2 - U) + abs(F2 - Fv) < 1e-14: D, U, Fv = D2, U2, F2; break
        D, U, Fv = D2, U2, F2
    v = np.array([D, U, Fv]); h = 1e-7; J = np.zeros((3, 3))
    rf = lambda w: np.array(rhs(xp, xa, yf, w[0], w[1], w[2], variant))
    for j in range(3):
        e = np.zeros(3); e[j] = h; J[:, j] = (rf(v + e) - rf(v - e)) / (2 * h)
    w, V = np.linalg.eig(J); k = np.argmax(w.real); vec = np.abs(V[:, k].real); vec /= vec.max()
    for dl in (1e-5, 3e-5, 1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1):
        cand = v + dl * vec
        Db, Ub, Fb = (F(round(cc * 10**12), 10**12) for cc in cand)
        r = rhs(xP, xA, y, Db, Ub, Fb, variant)
        if Db >= r[0] and Ub >= r[1] and Fb >= r[2]:
            x = xP + xA
            Rbar = upf(3, xP, xA, Ub, variant) * (1 + 3 * x * Db) * (1 + y * Fb) ** 6
            return (Db, Ub, Fb, Rbar, w.real[k])
    return None
def best(p, q, r, c, variant, tgrid=range(40, 200)):
    d1, d2, d3 = devs(p, q, r); e1, e2 = d1, max(d2, d3)
    for tn in tgrid:
        t = F(tn, 1000); xP, xA, y = t, e2 / t**c, e1 / t**3
        cert = certificate(xP, xA, y, variant)
        if cert: return t, cert
    return None
if __name__ == "__main__":
    print("sanity (block 30's point, unrestricted):", (lambda b: (b[0], float(b[1][3]), b[1][4]) if b else None)(best(4165, 1, 2, 2, "none")))
    print("sanity (block 31's stake, unrestricted, c=1):", (lambda b: (b[0], float(b[1][3])) if b else None)(best(453, 1, 2, 1, "none")))
    for c, pts in ((2, ((2921, 1, 2), (1464, 1, 1), (5842, 2, 4), (4380, 1, 3))), (1, ((407, 1, 2), (209, 1, 1), (813, 2, 4), (608, 1, 3)))):
        for (p, q, r) in pts:
            lo, hi = p - 60, p + 60
            # least p on the line with a certificate on the grid
            while lo < hi:
                mid = (lo + hi) // 2
                if best(mid, q, r, c, "R1"): hi = mid
                else: lo = mid + 1
            b = best(lo, q, r, c, "R1"); d1 = devs(lo, q, r)[0]
            t, (Db, Ub, Fb, Rbar, rho) = b
            print(f"R1 c={c} ({lo},{q},{r}): t={t} rho={rho:.4f} R-bar={float(Rbar):.3f} eps1*R-bar={float(d1*Rbar):.3e}  D,U,F = {Db}, {Ub}, {Fb}")
