# ru55_4: FI-1 algebra checks (criteria: checks/ru55_4_criteria.md, written first). Exact Fractions only.
from fractions import Fraction as F


def f1():
    ok = True
    for ell in (F(1, 10), F(1), F(7, 2), F(50)):
        for R in (F(0), F(1, 3), F(2), F(100)):
            for frac in (F(1, 1000), F(1, 4), F(1, 2)):
                Cg2 = frac * ell
                worst = max(-b - r for b in (ell - R, ell + R) for r in (-Cg2, Cg2))
                ok &= worst <= R - ell / 2
    return ok


def f2(shift=F(0)):
    ok_eq, below = True, False
    for ell in (F(1, 10), F(1), F(7, 2), F(50)):
        for R in (F(0), F(1, 3), F(2), F(100)):
            for kappa in (F(1), F(1, 4), F(4)):
                for frac in (F(1, 1000), F(1, 2)):
                    Cg2 = frac * ell
                    xlo = max(2 * R, 2 / min(F(1), kappa))
                    u = xlo + R + F(3, 2) * ell + shift
                    phimin = min(u - b - r for b in (ell - R, ell + R) for r in (-ell / 2, ell / 2))  # |rho| <= ell/2 (worst case)
                    left = u - F(3, 2) * ell - R
                    if shift == 0:
                        ok_eq &= (phimin == xlo) and (left == xlo)
                    else:
                        below |= phimin < xlo
    return ok_eq if shift == 0 else below


def ymin_steep(s, a):
    """smallest y with y - h(y) = s, h(y) = 2y (|y|<=a), 2a*sign(y) (|y|>a); exact on each branch"""
    sols = []
    y = s - 2 * a          # branch y < -a: y + 2a = s
    if y < -a:
        sols.append(y)
    y = -s                 # branch |y| <= a: y - 2y = s
    if -a <= y <= a:
        sols.append(y)
    y = s + 2 * a          # branch y > a: y - 2a = s
    if y > a:
        sols.append(y)
    return min(sols)


def y_contr(s, a):
    """unique y with y - h(y) = s, h(y) = y/2 (|y|<=a), (a/2)sign(y) beyond"""
    y = 2 * s
    if abs(y) <= a:
        return y
    return s + a / 2 if s > 0 else s - a / 2


def main():
    r1 = f1()
    print(f"F1 upper end (max(-b-rho) <= R - ell/2 on the grid): {'PASS' if r1 else 'FAIL'}")
    r2 = f2()
    print(f"F2 lower end at gamma^-2 = x_lo + R + (3/2)ell: min Phi == x_lo and left end == x_lo: {'PASS' if r2 else 'FAIL'}")
    c2 = f2(F(-1))
    print(f"F2-C (gamma^-2 one unit smaller): min Phi < x_lo somewhere: {c2} -> {'FAILS (as designed)' if c2 else 'CONTROL DOES NOT FIRE'}")
    eps = F(3, 1000)
    a = eps / 3
    d = F(1, 10 ** 6)
    j = abs(ymin_steep(a + d, a) - ymin_steep(a - d, a))
    bound = max(abs(-2 * (-a) - (a + d)), abs(2 * a + (a + d)))  # |rho| = |h(y)+s| <= 2a + |s|
    print(f"F4 steep family (slope 2, eps={eps}): y_min(a-1e-6) = {ymin_steep(a - d, a)}, y_min(a+1e-6) = {ymin_steep(a + d, a)}; "
          f"jump {j} (>= eps: {j >= eps}); |rho| <= {2 * a + a + d} (~eps)")
    jc = abs(y_contr(a + d, a) - y_contr(a - d, a))
    print(f"F4-K contraction family (slope 1/2): moves by {jc} <= 2|ds| = {4 * d}: {jc <= 4 * d}")
    ok = r1 and r2 and c2 and (j >= eps) and (jc <= 4 * d)
    print(f"VERDICT: {'all gates PASS, control fires' if ok else 'NOT all PASS'}")


if __name__ == "__main__":
    main()
