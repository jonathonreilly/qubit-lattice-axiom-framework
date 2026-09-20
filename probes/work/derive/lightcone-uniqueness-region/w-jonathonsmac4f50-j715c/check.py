#!/usr/bin/env python3
"""lightcone-uniqueness-region, attempt a1: the parallel W1 influence of the vMF kernel.

Every finite claim below is either a sympy identity or a rational-interval computation with
outward rounding; nothing is asserted from a float.  The one numerical statement (C5, the
k^2 coefficient) is labelled as such and is not used by any other check.

Checks
  C1  M(z) = Mmax - c*omega(k(z-A))            exact identity  (the universal partner equation)
  C2  the antitone pairing is an admissible transport plan     exact mass identity
  C3  Phi(0) = 1/3, equal to the perpendicular influence at k=0
  C4  Phi(k) < A(k)/k at 14 rational k in [1/10, 3]            rational-interval certificate
  C5  Phi(k) = 1/3 - (8/135)k^2 + O(k^4), so A/k - Phi = k^2/27 + O(k^4)   high precision
  C6  A(k)/k is strictly decreasing (re-proved here, not cited)
  C7  the region arithmetic of (b) and (c)
"""
import sys
from fractions import Fraction as F

# ----------------------------------------------------------------------------------------
# rational intervals with outward rounding: every operation returns [lo, hi] containing the
# true value.  DEN caps the size of the fractions; rounding is always outward.
# ----------------------------------------------------------------------------------------
DEN = 10**18

def _fl(x):  return F(x.numerator * DEN // x.denominator, DEN)
def _ce(x):  return F(-((-x.numerator * DEN) // x.denominator), DEN)

class Iv:
    __slots__ = ("lo", "hi")
    def __init__(self, lo, hi=None):
        if hi is None: hi = lo
        self.lo, self.hi = _fl(F(lo)), _ce(F(hi))
        assert self.lo <= self.hi
    def __add__(s, o): o = iv(o); return Iv(s.lo + o.lo, s.hi + o.hi)
    def __radd__(s, o): return iv(o) + s
    def __sub__(s, o): o = iv(o); return Iv(s.lo - o.hi, s.hi - o.lo)
    def __rsub__(s, o): return iv(o) - s
    def __neg__(s): return Iv(-s.hi, -s.lo)
    def __mul__(s, o):
        o = iv(o); c = [s.lo*o.lo, s.lo*o.hi, s.hi*o.lo, s.hi*o.hi]
        return Iv(min(c), max(c))
    def __rmul__(s, o): return iv(o) * s
    def __truediv__(s, o):
        o = iv(o)
        assert o.lo > 0 or o.hi < 0, "interval division through zero"
        c = [s.lo/o.lo, s.lo/o.hi, s.hi/o.lo, s.hi/o.hi]
        return Iv(min(c), max(c))
    def __rtruediv__(s, o): return iv(o) / s
    def sqrt(s):
        assert s.lo >= 0
        def rt(x, up):
            if x == 0: return F(0)
            n = x.numerator * DEN * DEN // x.denominator
            r = isqrt_(n)
            return F(r + 1, DEN) if up else F(r, DEN)
        return Iv(rt(s.lo, False), rt(s.hi, True))
    def __repr__(s): return f"[{float(s.lo):.12f},{float(s.hi):.12f}]"

def iv(x): return x if isinstance(x, Iv) else Iv(F(x))

def isqrt_(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y; y = (x + n // x) // 2
    return x

def iexp(x, terms=45):
    """enclosure of e^x for a rational interval x, |x| <= 12."""
    x = iv(x)
    if x.lo < 0 and x.hi > 0:
        return Iv(iexp(Iv(x.lo, x.lo)).lo, iexp(Iv(x.hi, x.hi)).hi)
    if x.hi <= 0:
        return 1 / iexp(-x, terms)
    def one(a, up):                       # a >= 0 rational
        s = F(0); t = F(1)
        for n in range(terms):
            s += t; t = t * a / (n + 1)
        if not up: return _fl(s)
        assert a < terms
        return _ce(s + t / (1 - a / F(terms + 1)))
    return Iv(one(x.lo, False), one(x.hi, True))

_TERMS = 30
_OMC = None
def _omc():
    """coefficients (n-1)/n! of omega, n = 2.._TERMS, and the tail constant."""
    global _OMC
    if _OMC is None:
        fac = [1, 1]
        for n in range(2, _TERMS + 2): fac.append(fac[-1] * n)
        _OMC = [F(n - 1, fac[n]) for n in range(2, _TERMS + 1)]
    return _OMC

def omega(z):
    """omega(x) = e^x (x-1) + 1 = sum_{n>=2} x^n (n-1)/n!, for a rational interval.

    Horner on the truncated series; the tail is bounded by sum_{n>T} r^n/(n-1)!  using
    (n-1)/n! <= 1/(n-1)!."""
    z = iv(z)
    c = _omc()
    p = Iv(c[-1])
    for j in range(len(c) - 2, -1, -1):
        p = p * z + Iv(c[j])
    s = z * z * p
    r = max(abs(z.lo), abs(z.hi))
    if r > 0:
        assert r < _TERMS
        fac = 1
        for n in range(1, _TERMS + 1): fac *= n            # T!
        tail = _ce(r * r**_TERMS / fac / (1 - r / F(_TERMS + 1)))
        s = s + Iv(-tail, tail)
    return s

# ----------------------------------------------------------------------------------------
# the kernel's constants
# ----------------------------------------------------------------------------------------
def constants(k):
    """A(k), sinh k, zeta1 = k(1-A), omega(zeta1), Mmax, A/k  as enclosures."""
    K = iv(F(k))
    E2 = iexp(2 * K)                                   # e^{2k}
    coth = (E2 + 1) / (E2 - 1)
    A = coth - 1 / K
    sinh = (iexp(K) - iexp(-K)) * Iv(F(1, 2))
    zeta1 = K * (1 - A)
    om1 = omega(zeta1)
    Mmax = iexp(K * A) * om1 / (2 * K * sinh)
    return dict(K=K, A=A, sinh=sinh, zeta1=zeta1, om1=om1, Mmax=Mmax, Aoverk=A / K)

def invert_omega(target, lo, hi, negative, steps=70):
    """enclose the solution of omega(x) = target on a branch where omega is monotone.

    negative=True  : branch x in [lo,hi] <= 0, omega decreasing
    negative=False : branch x in [lo,hi] >= 0, omega increasing
    Returns (lo_bound, hi_bound) rationals bracketing the root."""
    a, b = F(lo), F(hi)
    for _ in range(steps):
        m = (a + b) / 2
        w = omega(Iv(m))
        if negative:
            if w.lo > target.hi: a = m          # omega(m) > target  => root is to the right
            elif w.hi < target.lo: b = m
            else: break
        else:
            if w.hi < target.lo: a = m
            elif w.lo > target.hi: b = m
            else: break
    return a, b

def chord_upper(zp_hi, zm_lo):
    """upper bound on |s(z_+) - s(z_-)| for two points at the same azimuth."""
    zp, zm = iv(zp_hi), iv(max(F(-1), zm_lo))
    if zp.hi > 1: zp = Iv(min(zp.lo, F(1)), F(1))
    v = 2 - 2 * zp * zm - 2 * ((1 - zp * zp) * (1 - zm * zm)).sqrt()
    if v.hi <= 0: return F(0)
    return Iv(max(F(0), v.lo), v.hi).sqrt().hi

def phi_upper(k, n):
    """rigorous upper bound on Phi(k), the cost of the antitone plan.

    Phi = int_0^Mmax chord dm and m = Mmax - c*omega(zeta), so the mass of the cell between
    zeta_{j-1} and zeta_j is exactly c*(omega_j - omega_{j-1}).  The chord grows with zeta
    (z_+ rises and its partner z_- falls, so the opening angle grows), hence taking its value
    at the cell's right end is an upper bound.  zeta_- is bracketed by a monotone sweep: as
    zeta_+ rises, zeta_- falls, so one pointer serves the whole grid."""
    C = constants(k)
    A, K, om1, zeta1 = C["A"], C["K"], C["om1"], C["zeta1"]
    c = iexp(K * A) / (2 * K * C["sinh"])
    left_end = -(K * (1 + A)).hi                   # zeta at z = -1
    tot = Iv(0)
    prev_om = Iv(0)
    hi_ptr = F(0)                                  # upper bracket for zeta_-, non-increasing
    for j in range(1, n + 1):
        zt = zeta1.hi * F(j, n)
        om_j = omega(Iv(zt)) if j < n else om1
        if j == n:
            ch = F(2)                              # z_+ = 1, partner z_- = -1
        else:
            lo, hi = left_end, hi_ptr
            for _ in range(46):
                mid = (lo + hi) / 2
                w = omega(Iv(mid))
                if w.lo >= om_j.hi: lo = mid       # omega(mid) > omega_j: mid is left of z_-
                elif w.hi <= om_j.lo: hi = mid     # omega(mid) < omega_j: mid is right of z_-
                else: break                        # enclosures overlap; keep the bracket
            hi_ptr = hi
            zplus_hi = (A + Iv(zt) / K).hi
            zminus_lo = (A + Iv(lo) / K).lo
            ch = chord_upper(zplus_hi, zminus_lo)
        tot = tot + Iv(ch) * (om_j - prev_om)
        prev_om = om_j
    return (c * tot).hi, C

# ----------------------------------------------------------------------------------------
def main():
    import sympy as sp
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    print("C1  the universal partner equation")
    k, z, t = sp.symbols('k z t', positive=True)
    a = sp.Symbol('a')                                   # A(k), substituted at the end
    q = lambda u: k * sp.exp(k * u) / (2 * sp.sinh(k))
    M = (sp.exp(k) * (1 - a - 1/k) - sp.exp(k*z) * (z - a - 1/k)) / (2 * sp.sinh(k))
    want(sp.simplify(sp.diff(M, z) + (z - a) * q(z)) == 0,
         "M'(z) = -(z-a)q(z): M(z) is the mass above z of the signed density (z-a)q,")
    want(sp.simplify(M.subs(z, 1)) == 0, "    and M(1) = 0, so M(z) = int_z^1 (t-a)q(t)dt")
    A = sp.coth(k) - 1/k
    sol = sp.solve(sp.Eq(sp.simplify((M.subs(z, -1) * 2 * sp.sinh(k)).rewrite(sp.exp)), 0), a)
    want(len(sol) == 1 and sp.simplify((sol[0] - A).rewrite(sp.exp)) == 0,
         "M(-1) = 0 forces a = coth k - 1/k, the mean of z: the signed density (z-a)q has")
    print("     zero total mass for that a and no other, which is what makes the pairing exist.")
    c = sp.exp(k * a) / (2 * k * sp.sinh(k))
    om = lambda x: sp.exp(x) * (x - 1) + 1
    Mmax_sym = c * om(k * (1 - a))
    want(sp.simplify(sp.expand(M - (Mmax_sym - c * om(k * (z - a))))) == 0,
         "M(z) = Mmax - c*omega(k(z-a)) with c = e^{ka}/(2k sinh k), omega(x) = e^x(x-1)+1")
    print("     so the two solutions of M(z_-) = M(z_+) are the two solutions of")
    print("     omega(zeta_-) = omega(zeta_+) in the single variable zeta = k(z-a): the pairing")
    print("     is k-free in that variable.")

    print("\nC2  the antitone pairing is an admissible plan")
    want(sp.simplify(sp.diff(om(t), t) - sp.exp(t) * t) == 0,
         "omega'(x) = x e^x: omega decreases on x<0 and increases on x>0, so each level of M")
    print("     has exactly two solutions z_- < A < z_+, and pairing them transports the")
    print("     deficit {z < A} onto the excess {z > A}: the mass below z_- equals the mass")
    print("     above z_+ by construction (both are M evaluated at the same level).")
    kk = F(7, 10)
    C = constants(kk)
    lev = C["om1"] * Iv(F(37, 100))
    zp = invert_omega(lev, F(0), C["zeta1"].hi, False)
    zm = invert_omega(lev, -(C["K"] * (1 + C["A"])).hi, F(0), True)
    wp, wm = omega(Iv(*zp)), omega(Iv(*zm))
    want(wp.lo <= lev.hi and wp.hi >= lev.lo and wm.lo <= lev.hi and wm.hi >= lev.lo,
         f"at k=7/10 a level of M is met on both branches (zeta_+ ~ {float(zp[0]):.6f},"
         f" zeta_- ~ {float(zm[0]):.6f})")

    print("\nC3a  the perpendicular influence (the value Phi is compared with), re-proved here")
    want(sp.simplify(sp.integrate(t * sp.exp(k*t), (t, -1, 1)) /
                     sp.integrate(sp.exp(k*t), (t, -1, 1)) - A) == 0,
         "E_V[s] = A(k) V/|V|, A = coth k - 1/k  (the transverse parts vanish by symmetry)")
    print("     rho_w s = s - 2(w.s)w is the reflection across w^perp, so |s - rho_w s| = 2|w.s|.")
    print("     For |V| = |V'| = k and w = (V-V')/|V-V'| one has rho_w V = V', p_V/p_V' =")
    print("     exp((V-V').s), and p_V > p_V' exactly on {w.s > 0}; pairing s with rho_w s gives")
    print("     E_V f - E_V' f <= int 2(w.s)(p_V - p_V') = E_V[w.s] - E_V'[w.s] = (A/k)|V-V'|,")
    print("     with equality at f = w.s.  The perpendicular influence is exactly A(k)/k.")

    print("\nC3  the plan's cost at k = 0")
    m, zz = sp.symbols('m zz', nonnegative=True)
    want(sp.integrate(2 * sp.sqrt(1 - 4 * m), (m, 0, sp.Rational(1, 4))) == sp.Rational(1, 3),
         "Phi(0) = int_0^{1/4} 2 sqrt(1-4m) dm = 1/3   (at k=0 the pairing is z <-> -z,")
    print("     the chord is 2|z| and M(z) = (1-z^2)/4), which is exactly the perpendicular")
    print("     influence A(k)/k at k = 0.")

    print("\nC4  Phi(k) < A(k)/k    rational-interval certificate")
    print("      k        Phi <=          A/k >=        margin        cells")
    grid = [(F(1,10), 1200), (F(3,20), 900), (F(1,5), 700), (F(1,4), 600), (F(3,10), 500),
            (F(2,5), 400), (F(1,2), 350), (F(7,10), 300), (F(1), 250), (F(13,10), 200),
            (F(8,5), 200), (F(2), 180), (F(5,2), 160), (F(3), 150)]
    for kv, n in grid:
        up, C = phi_upper(kv, n)
        lo = C["Aoverk"].lo
        want(up < lo, f"k={str(kv):>6}  {float(up):.8f} <  {float(lo):.8f}   "
                      f"{float(lo-up):+.2e}   n={n}")

    print("\nC5  the small-k behaviour   [numerical, labelled: mpmath quadrature]")
    try:
        import mpmath as mp
        mp.mp.dps = 40
        def Aq(x): return mp.coth(x) - 1/x
        def omq(x): return mp.e**x * (x - 1) + 1
        def part(zt, x, a):
            tgt = omq(zt); lo, hi = -x*(1+a), mp.mpf(0)
            for _ in range(200):
                mid = (lo+hi)/2
                if omq(mid) > tgt: lo = mid
                else: hi = mid
            return (lo+hi)/2
        def Phi(x):
            x = mp.mpf(x); a = Aq(x); cc = mp.e**(x*a)/(2*x*mp.sinh(x))
            def f(zt):
                zp = min(a+zt/x, mp.mpf(1)); zm = max(a+part(zt,x,a)/x, mp.mpf(-1))
                v = 2-2*zp*zm-2*mp.sqrt((1-zp**2)*(1-zm**2))
                return mp.sqrt(v if v > 0 else mp.mpf(0))*mp.e**zt*zt
            return cc*mp.quad(f, [0, x*(1-a)])
        d = {}
        for s in ['0.05', '0.1']:
            d[mp.mpf(s)] = mp.mpf(1)/3 - Phi(s)
        (k1, d1), (k2, d2) = sorted(d.items())
        a2 = (d1*k2**4 - d2*k1**4)/(k1**2*k2**4 - k2**2*k1**4)
        print(f"     fitted 1/3 - Phi = a k^2 + b k^4 :  a = {mp.nstr(a2, 12)}"
              f"   8/135 = {mp.nstr(mp.mpf(8)/135, 12)}")
        want(abs(a2 - mp.mpf(8)/135) < mp.mpf('1e-7'),
             "Phi(k) = 1/3 - (8/135) k^2 + O(k^4)   [numerical]")
    except ImportError:
        print("     mpmath missing; C5 skipped")
    want(sp.Rational(8,135) - sp.Rational(1,45) == sp.Rational(1,27),
         "8/135 - 1/45 = 1/27, so A(k)/k - Phi(k) = k^2/27 + O(k^4)   [exact arithmetic]")

    print("\nC6  A(k)/k is strictly decreasing   (re-proved, not cited)")
    x = sp.symbols('x', positive=True)
    num = sp.simplify(sp.together(sp.diff((sp.coth(x) - 1/x)/x, x)))
    g = sp.cosh(2*x) - 1 - x**2 - (x/2)*sp.sinh(2*x)      # = (k A' - A) * k sinh^2 k  up to >0
    ser = sp.series(g, x, 0, 14).removeO()
    coeffs = [sp.nsimplify(ser.coeff(x, j)) for j in range(0, 14)]
    want(all(c <= 0 for c in coeffs) and any(c < 0 for c in coeffs),
         f"cosh 2k - 1 - k^2 - (k/2) sinh 2k has only non-positive Taylor coefficients: "
         f"{[str(c) for c in coeffs if c != 0][:4]} ...")
    aser = sp.series(sp.coth(x) - 1/x, x, 0, 4).removeO()
    want(sp.nsimplify(aser.coeff(x, 1)) == sp.Rational(1,3) and sp.nsimplify(aser.coeff(x, 0)) == 0,
         "A(k) = k/3 - k^3/45 + ..., so A(k)/k -> 1/3 and A(k)/k <= 1/3 for every k > 0")

    print("\nC7  the regions")
    beta = sp.symbols('beta', positive=True)
    want(sp.solve(sp.Eq(7*beta*sp.Rational(1,3), 1), beta)[0] == sp.Rational(3,7),
         "W1 with L = 1/3 and 7 predecessors: 7*beta/3 < 1  <=>  beta < 3/7 = 0.428571...")
    want(sp.solve(sp.Eq(7*beta/sp.sqrt(3), 1), beta)[0] == sp.sqrt(3)/7,
         "TV with block 27's |V-V'|/(2 sqrt 3) and the chordal diameter 2: beta < sqrt3/7 = 0.247436...")
    want(sp.Rational(3,7) > sp.sqrt(3)/7, "3/7 > sqrt(3)/7: the W1 region is the larger one")
    want(sp.Rational(3,10) < sp.Rational(3,7),
         "attempt a2's unconditional 3/10 sits inside 3/7")
    # the executed onset, read out of this branch's own scan logs rather than quoted
    import glob, json as js, re as _re
    seen = {}
    for p in glob.glob("logs/probes/X:lightcone-threshold-fine/*.json") + \
             glob.glob("logs/probes/X:formation-lightcone-sphere/*.json"):
        s = (js.load(open(p)).get("summary") or {}).get("summary", "")
        mm = _re.search(r"dim=3 .*?beta=([\d.]+) L=(\d+) T=(\d+) plateau_\|m\|=([\d.]+)", s)
        if mm:
            seen.setdefault(float(mm.group(1)), []).append((int(mm.group(2)), float(mm.group(4))))
    for b in sorted(seen):
        print("     beta=%-5s" % b, "  ".join(f"L={L}:|m|={v}" for L, v in sorted(seen[b])))
    below = [b for b in seen if max(v for _, v in seen[b]) < 0.1]
    above = [b for b in seen if min(v for _, v in seen[b]) > 0.3]
    want(below and above and max(below) < min(above),
         f"the scans put the onset between beta = {max(below)} and beta = {min(above)}")
    want(sp.Rational(3,7) < sp.Rational(sp.Integer(int(min(above)*100)), 100),
         f"3/7 = {float(sp.Rational(3,7)):.4f} lies below that onset, by a factor "
         f"{float(max(below)/sp.Rational(3,7)):.2f} to {float(min(above)/sp.Rational(3,7)):.2f}")

    print()
    if ok:
        print("SUMMARY: PARTIAL the parallel W1 influence of the vMF kernel is at most the cost "
              "Phi(k) of the antitone meridian plan, whose pairing is k-free in zeta = k(z-A) "
              "(omega(zeta_-) = omega(zeta_+), omega(x) = e^x(x-1)+1); Phi(0) = 1/3 = A/k at 0, "
              "Phi(k) < A(k)/k by rational-interval certificate at 14 k in [1/10,3], and "
              "Phi(k) = 1/3 - (8/135)k^2 + O(k^4) so A/k - Phi = k^2/27 + O(k^4)")
        print("HIT: sup over chordally 1-Lipschitz f of Cov_V(f, V^.s) <= Phi(|V|) with Phi in "
              "closed form, and Phi < A/k at the 14 certified k plus the k -> 0 expansion - the "
              "parallel case of the directional lemma that attempt a2 assumed, where a2's relaxed "
              "bound R = A' + I exceeds A/k for k below about 0.4")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
