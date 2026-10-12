"""F2 (lane RFW), part 4: witness for the analytic proof of the 1-jet obstruction (K2 scalar).

Proof skeleton (see F2_report.md section 3): with T0 = 2 v(x)v, v = sin p, the tangent
condition with constant M_mu forces, on the shell,
     cos p_0 * v_1 * v_2^2 = P(v)     (P a fixed homogeneous cubic built from M_0, M_1),
so cos p_0 = P(v)/(v_1 v_2^2) is homogeneous of degree 0 in v: it must take the same value at any
two shell points whose v are proportional.  Witness: two points p, p' on the complex shell
sum_mu (2 - 2 cos p_mu) + m2 = 0 with sin p' = s sin p (s != 0, +-1 allowed) and cos p'_0 != cos p_0.
Construction: fix a direction u in C^4; along v = s u, cos p_mu = eps_mu sqrt(1 - s^2 u_mu^2);
solve  sum_mu eps_mu sqrt(1 - s^2 u_mu^2) = 4 + m2/2  for s over sign patterns eps (mpmath, 40 digits).
"""
import mpmath as mp
import itertools, random

mp.mp.dps = 40
random.seed(5)


def find_roots(u, m2, eps):
    C = 4 + mp.mpf(m2) / 2
    F = lambda s: sum(e * mp.sqrt(1 - s * s * ui * ui) for e, ui in zip(eps, u)) - C
    roots = []
    for _ in range(60):
        s0 = mp.mpc(random.uniform(-3, 3), random.uniform(-3, 3))
        try:
            r = mp.findroot(F, s0, tol=mp.mpf(10) ** -35, maxsteps=200)
        except (ValueError, ZeroDivisionError):
            continue
        if abs(F(r)) < mp.mpf(10) ** -30 and abs(r) > mp.mpf(10) ** -6:
            if all(abs(r - q) > 1e-20 and abs(r + q) > 1e-20 for q in roots):
                roots.append(r)
    return roots


for m2 in (mp.mpf("0.25"), mp.mpf(1)):
    u = [mp.mpc(random.uniform(0.3, 1.2), random.uniform(-0.4, 0.4)) for _ in range(4)]
    pts = []
    for eps in itertools.product((1, -1), repeat=4):
        for s in find_roots(u, m2, eps):
            v = [s * ui for ui in u]
            c = [e * mp.sqrt(1 - vi * vi) for e, vi in zip(eps, v)]
            shell = sum(2 - 2 * ci for ci in c) + m2
            pts.append((s, eps, c, shell, v))
    print(f"m2 = {m2}: direction u = {[mp.nstr(x, 6) for x in u]}")
    print(f"  shell points on the ray v = s u found: {len(pts)}")
    shown = 0
    for s, eps, c, shell, v in pts[:6]:
        print(f"   s = {mp.nstr(s, 12):>34s}  eps = {eps}  |shell| = {mp.nstr(abs(shell), 3)}  "
              f"cos p_0 = {mp.nstr(c[0], 15)}  |v1 v2^2| = {mp.nstr(abs(v[1] * v[2] ** 2), 4)}")
    c0s = [p[2][0] for p in pts]
    spread = max(abs(a - b) for a in c0s for b in c0s) if len(c0s) > 1 else 0
    print(f"  max |cos p_0 - cos p'_0| among proportional-v shell points = {mp.nstr(spread, 10)}"
          f"  (> 0 => cos p_0 is not homogeneous of degree 0 in v on the shell => no constant M)")
