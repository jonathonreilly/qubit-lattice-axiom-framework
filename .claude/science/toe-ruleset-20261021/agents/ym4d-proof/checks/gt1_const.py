#!/usr/bin/env python3
# gt1_const.py -- evaluates the EXPLICIT constants of GREENT.md section G2 (Theorem GT-1/GT-2)
# and the carry-through arithmetic of section G3.  Scalar float arithmetic only (no arrays, no numpy,
# no BLAS, single process, milliseconds).  It NEVER reads a Green's function: it only evaluates the
# elementary functions that the proof's inequalities define.  This is the code path that gt1-C compares
# against gt1_green.py's exact maxima.
import math, sys

SQPI = math.sqrt(math.pi)
A0 = SQPI / 4.0                      # sup_s q_t  <=  1/R + A0 t^{-1/2}
A1 = math.pi / 8.0                   # sup_s |grad q_t| <= A1/t + B1/(R sqrt t)
B1 = math.pi / math.sqrt(2.0 * math.e)
A2 = SQPI * math.pi ** 2 / 32.0      # sup_s |grad^2 q_t| <= A2 t^{-3/2} + B2/(R t)
B2 = math.pi ** 2 / (2.0 * math.e)
XI = math.cosh(1.0) - 1.0            # cosh(lam)-1 <= XI lam^2 for 0<=lam<=1

def U_sup(t, R):
    "upper bound for sup_s q_t^R(s)"
    g = math.exp(-8.0 * t / (R * R)) if 8.0 * t / (R * R) < 700 else 0.0
    return min(1.0, 1.0 / R + A0 / math.sqrt(t), 1.0 / R + math.sqrt(2.0) * A0 * g / math.sqrt(t))

def V_sup(t, R):
    "upper bound for sup_s |grad q_t^R(s)|"
    g = math.exp(-8.0 * t / (R * R)) if 8.0 * t / (R * R) < 700 else 0.0
    return min(2.0, A1 / t + B1 / (R * math.sqrt(t)),
               g * (2.0 * A1 / t + math.sqrt(2.0) * B1 / (R * math.sqrt(t))))

def W_sup(t, R):
    "upper bound for sup_s |grad^2 q_t^R(s)|"
    g = math.exp(-8.0 * t / (R * R)) if 8.0 * t / (R * R) < 700 else 0.0
    return min(4.0, A2 / t ** 1.5 + B2 / (R * t),
               g * (2.0 ** 1.5 * A2 / t ** 1.5 + 2.0 * B2 / (R * t)))

def lamgrid(scale):
    "finite lambda grid: ANY lambda gives a valid bound, so a finite grid still yields a valid UPPER bound."
    lo = 1e-4 / max(1.0, scale)
    out = []
    l = lo
    while l <= 30.0:
        out.append(l); l *= 1.25
    return out

def tilt(t, R, a, kind, LAMS):
    """inf over the lambda grid of the periodised tilt bound, for exponent offset a >= 0.
    kind 0 = q, 1 = grad q, 2 = grad^2 q."""
    best = float('inf')
    for lam in LAMS:
        ch = math.cosh(lam)
        ex = 2.0 * t * (ch - 1.0) - lam * a
        if ex > 700.0:
            continue
        T = t * ch
        dl = 1.0 - math.exp(-lam)
        if kind == 0:
            pre = A0 / math.sqrt(T)
        elif kind == 1:
            pre = A1 / T + dl * A0 / math.sqrt(T)
        else:
            pre = A2 / T ** 1.5 + 2.0 * dl * A1 / T + dl * dl * A0 / math.sqrt(T)
        lr = lam * R
        if lr > 700.0:
            om = 3.0
        else:
            om = 1.0 + 2.0 / (1.0 - math.exp(-lr)) if lr > 1e-12 else float('inf')
        v = om * pre * math.exp(ex)
        if v < best:
            best = v
    return best

def Us(t, R, s, LG):  return min(U_sup(t, R), tilt(t, R, s, 0, LG))
def Vs(t, R, s, LG):  return min(V_sup(t, R), tilt(t, R, s - 1.0, 1, LG))
def Ws(t, R, s, LG):  return min(W_sup(t, R), tilt(t, R, s - 2.0, 2, LG))

def Vcal(t, R, s, d, LG):
    U = U_sup(t, R)
    return max(Vs(t, R, s, LG) * U ** (d - 1), V_sup(t, R) * Us(t, R, s, LG) * U ** (d - 2))

def Wcal(t, R, s, d, LG):
    U = U_sup(t, R); V = V_sup(t, R)
    c = [Ws(t, R, s, LG) * U ** (d - 1),
         W_sup(t, R) * Us(t, R, s, LG) * U ** (d - 2),
         Vs(t, R, s, LG) * V * U ** (d - 2)]
    if d >= 3:
        c.append(V * V * Us(t, R, s, LG) * U ** (d - 3))
    return max(c)

def integrate(f, s, nper=70):
    """upper estimate of int_0^inf f(t) dt on a log grid anchored at scale s^2, with a per-interval
    sup taken over the two endpoints and the midpoint, times the interval length (a Riemann UPPER sum
    up to the resolution of the grid)."""
    lo, hi = math.log(1e-7 * max(s * s, 1.0)), math.log(1e6 * max(s * s, 1.0))
    n = int(nper * (hi - lo) / math.log(10.0))
    tot = 0.0
    prev_t = math.exp(lo)
    tot += prev_t * f(prev_t)           # the (0, t_lo) stub, integrand <= cap there
    fprev = f(prev_t)
    for i in range(1, n + 1):
        t = math.exp(lo + (hi - lo) * i / n)
        tm = math.sqrt(prev_t * t)
        fm = f(tm); fc = f(t)
        tot += (t - prev_t) * max(fprev, fm, fc)
        prev_t, fprev = t, fc
    return tot

def const(d, kind, slist=None, rfac=(1.0, 2.0, 16.0, 1e4)):
    "sup over s and R of s^(d-1) int Vcal  (kind=1)  or  s^d int Wcal  (kind=2)"
    if slist is None:
        slist = [1, 2, 3, 4, 5, 6, 8, 10, 14, 20, 40, 100, 1000, 100000]
    best = 0.0; arg = None
    p = d - 1 if kind == 1 else d
    for s in slist:
        for fr in rfac:
            R = max(3.0, 2.0 * s * fr)
            LG = lamgrid(s)
            g = (lambda t, R=R, s=s, LG=LG: Vcal(t, R, s, d, LG)) if kind == 1 else (lambda t, R=R, s=s, LG=LG: Wcal(t, R, s, d, LG))
            v = (s ** p) * integrate(g, s)
            if v > best:
                best, arg = v, (s, R)
    return best, arg

def main():
    out = []
    P = out.append
    P("gt1_const.py -- explicit constants of GREENT.md Theorem GT-1/GT-2, and the section-G3 price.")
    P("Scalar IEEE-double arithmetic; no arrays; no BLAS; single process.  Grid-evaluated upper sums.")
    P("a0=%.10f a1=%.10f b1=%.10f a2=%.10f b2=%.10f xi=%.10f" % (A0, A1, B1, A2, B2, XI))
    P("")
    for d in (3, 4):
        c1h, a = const(d, 1)
        c2h, b = const(d, 2)
        C1 = d ** ((d - 1) / 2.0) * c1h
        C2 = d ** (d / 2.0) * c2h
        P("d=%d :  Chat_1 = %.6f (worst s=%s R=%.0f)   ->  C_1 = d^((d-1)/2) Chat_1 = %.4f" % (d, c1h, a[0], a[1], C1))
        P("d=%d :  Chat_2 = %.6f (worst s=%s R=%.0f)   ->  C_2 = d^(d/2)     Chat_2 = %.4f" % (d, c2h, b[0], b[1], C2))
        if d == 4:
            P("d=4 : REPORTED (rounded up) C_1 = %.1f , C_2 = %.1f" % (math.ceil(C1 * 10) / 10 + 0.0, math.ceil(C2 * 10) / 10))
        P("")
    # profile of s^(d-1) int Vcal in s, to show whether the sup is attained or creeps (log-creep check)
    P("creep check (d=4, R=1e3*2s): s , s^3*int Vcal , s^4*int Wcal")
    for s in [1, 2, 4, 8, 16, 64, 256, 2048, 16384, 131072]:
        R = max(3.0, 2.0 * s * 1e3)
        LG = lamgrid(s)
        v1 = s ** 3 * integrate(lambda t: Vcal(t, R, s, 4, LG), s)
        v2 = s ** 4 * integrate(lambda t: Wcal(t, R, s, 4, LG), s) if s >= 2 else float('nan')
        P("   s=%7d : %.6f , %.6f" % (s, v1, v2))
    txt = "\n".join(out)
    print(txt)
    with open(sys.argv[1] if len(sys.argv) > 1 else "gt1_const_out.txt", "w") as f:
        f.write(txt + "\n")

if __name__ == "__main__":
    main()
