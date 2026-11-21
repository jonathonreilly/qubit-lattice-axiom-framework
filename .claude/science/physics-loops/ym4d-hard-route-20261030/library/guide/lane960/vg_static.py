# GUIDE run for library/gap-vargeom-opus.md Step 6 (row 960). Refutes or guides only; proves nothing.
# Lattice free massive scalar on periodic tori (in the class of gap-seed-shape.md).
# C0: torus symmetry and E2 sanity; C1: slack budget of Lemma E2 (4.1); C2: (T) multiplicity loss;
# C4: smallest a with S(a; (2a)^3) <= 1/550, 1/1650, 1/3500.
import sys, resource, math
import numpy as np

LIMIT = 2 * 1024**3


def rss_check():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS
    if r > LIMIT:
        print("RSS above 2 GB, stopping", r)
        sys.exit(3)


def eps_grid(m, sides):
    # eps_k for all lattice momenta of the spatial box with the given sides
    s = np.zeros(1)
    for n in sides:
        k = 2 * np.pi * np.arange(n) / n
        s = (s[:, None] + 4 * np.sin(k / 2) ** 2).ravel()
    return np.arccosh(1 + (m * m + s) / 2)


def logZ(m, t, sides):
    e = eps_grid(m, sides)
    return np.sum(0.5 * t * np.log(2 * np.pi) - 0.5 * t * e - np.log1p(-np.exp(-t * e)))


def e0(m, sides):
    e = eps_grid(m, sides)
    return np.sum(0.5 * np.log(2 * np.pi) - 0.5 * e)


def g(m, t, sides):
    e = eps_grid(m, sides)
    return -np.sum(np.log1p(-np.exp(-t * e)))


def ell(m, c, d, N=4096):
    # ell = lim e(y)/y for boxes (y, c, d); integral over k_1 by the periodic trapezoid rule (exponential convergence)
    et = eps_grid(m, (c, d))
    k = 2 * np.pi * (np.arange(N) + 0.5) / N
    tot = 0.0
    for s in et:
        # eps(k1, k') with cosh eps(k') known: 2cosh eps = 2 + m^2 + 4 sin^2(k1/2) + transverse part
        trans = 2 * (np.cosh(s) - 1) - m * m  # transverse 4 sin^2 sum
        e = np.arccosh(1 + (m * m + trans + 4 * np.sin(k / 2) ** 2) / 2)
        tot += 0.5 * np.log(2 * np.pi) - 0.5 * np.mean(e)
    return tot


def kappa(m, y, c, d, L=None):
    if L is None:
        L = ell(m, c, d)
    return e0(m, (y, c, d)) - L * y


def main():
    np.set_printoptions(precision=6)
    print("== C0: torus symmetry Z(t,y,c,d) via time-transfer vs via direction-1 transfer")
    worst = 0.0
    for m in (1.0, 0.5, 0.25):
        for (t, y, c, d) in [(3, 5, 4, 4), (4, 7, 3, 5), (6, 6, 4, 3), (5, 9, 4, 4)]:
            a = logZ(m, t, (y, c, d))
            b = logZ(m, y, (t, c, d))
            worst = max(worst, abs(a - b) / abs(a))
    print("worst relative mismatch", worst, "PASS" if worst < 1e-9 else "FAIL")

    print("== C1: slack budget of Lemma E2 for (b,c,c) -> (h,c,c); columns: m t t' b h c | g_true U | N D X | (N+D)/X | sum check")
    bad = 0
    rows = []
    for m in (1.0, 0.5, 0.25):
        for c in (4, 6):
            L = ell(m, c, c)
            for (t, b) in [(3, 8), (4, 12), (6, 12), (5, 20), (8, 24)]:
                if m * b < 4:
                    continue
                for h in (2 * b, 4 * b):
                    best = None
                    for tp in range(3, b):
                        gb = g(m, t, (b, c, c))
                        gtp = g(m, tp, (b, c, c))
                        U = (h / b) * (gb + t / (b - tp) * gtp)
                        if best is None or U < best[0]:
                            best = (U, tp, gb, gtp)
                    U, tp, gb, gtp = best
                    gh = g(m, t, (h, c, c))
                    kb = kappa(m, b, c, c, L)
                    kh = kappa(m, h, c, c, L)
                    N = t * ((h / b) * kb - kh) + (h / b) * gb - gh
                    D = t * kh
                    X = (h / b) * t * (gtp / (b - tp) - kb)
                    chk = (N + D + X) - (U - gh)
                    ratio = (N + D) / X if X > 0 else float('nan')
                    if not (U >= gh * (1 - 1e-12)):
                        bad += 1
                    if ratio > 0.1:
                        bad += 1
                    rows.append((m, t, tp, b, h, c, gh, U, N, D, X, ratio, chk))
                    print("%5.2f %2d %2d %3d %3d %2d | %.3e %.3e | %.2e %.2e %.2e | %.2e | %.1e" % rows[-1])
                    rss_check()
    print("C1 verdict:", "PASS" if bad == 0 else "FAIL (%d)" % bad)

    print("== C2: (T) loss on cubes b^3 at time a: ratio log(1+s^q)/g(qa) for q = 1.5, 2, 3 (s = S(a; b^3))")
    for m in (1.0, 0.5, 0.25):
        for (a, b) in [(4, 8), (6, 12), (8, 16), (10, 40)]:
            if 3 * a >= 4 * b:
                continue
            s = math.expm1(g(m, a, (b, b, b)))
            out = []
            for q in (1.5, 2.0, 3.0):
                tq = q * a
                if abs(tq - round(tq)) > 1e-9:
                    out.append(float('nan'))
                    continue
                gq = g(m, int(round(tq)), (b, b, b))
                out.append(math.log1p(s ** q) / gq)
            print("m %.2f a %2d b %2d  s %.3e  ratios %s" % (m, a, b, s, np.array(out)))
            rss_check()

    print("== Lemma Q spot check: S(tau) <= S(a)^(tau/a) for tau in a+1..3a on cubes (b,b,b)")
    viol = 0
    for m in (1.0, 0.5):
        for (a, b) in [(3, 6), (4, 8), (5, 10)]:
            sa = math.expm1(g(m, a, (b, b, b)))
            for tau in range(a + 1, 3 * a + 1):
                st = math.expm1(g(m, tau, (b, b, b)))
                if st > sa ** (tau / a) * (1 + 1e-12):
                    viol += 1
    print("Lemma Q violations:", viol, "PASS" if viol == 0 else "FAIL")

    print("== C4: smallest a with S(a; (2a)^3) <= threshold; columns m thr a m*a m*b")
    for m in (1.0, 0.5, 0.25):
        for thr in (1 / 550, 1 / 1650, 1 / 3500):
            a = 3
            while True:
                s = math.expm1(g(m, a, (2 * a, 2 * a, 2 * a)))
                if s <= thr:
                    break
                a += 1
                if a > 200:
                    break
                rss_check()
            print("m %.3f thr 1/%d a %3d  m a %.2f  m b %.2f  (S = %.3e)" % (m, round(1 / thr), a, m * a, 2 * m * a, s))


if __name__ == "__main__":
    main()
