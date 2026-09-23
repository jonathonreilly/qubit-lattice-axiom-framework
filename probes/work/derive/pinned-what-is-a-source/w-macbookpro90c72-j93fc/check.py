#!/usr/bin/env python3
"""J:derive:pinned-what-is-a-source:a3 -- worker w-macbookpro90c72-j93fc.

Sphere menu at the pinned scale c0 = beta/sinh(beta) (blocks 39-41, PRs #8530 #8546 #8547):
a site is empty or holds a record s in S^2 (uniform probability measure), a record weighs z,
a bond between records weighs c0 exp(beta s.s'), a bond with an empty end weighs 1; formation at
an empty site x at rate z Z_x, Z_x = int dOmega/4pi prod_{y~x occupied} W(s, s_y) (block 39 T4).

  E  exact (sympy): the formation factor, the neutral mean, log-convexity, the tree field
  C  capacity of a pinned set: exact Dirichlet-principle bound (Fractions); executed massless Z^3 values
  P  production of a held aligned lump: exact pocket rule for boxes and balls; tree-level face excess
See ATTEMPT.md.
"""
import itertools
from fractions import Fraction as Fr
from collections import Counter
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import ive

NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


b, x, th, rho, z = sp.symbols('beta x theta rho z', positive=True)
c0 = b / sp.sinh(b)


def Zk(k):                     # aligned formation factor, k >= 1; Z_0 = 1
    return sp.Integer(1) if k == 0 else c0**k * sp.sinh(k * b) / (k * b)


# ------------------------------------------------------------------ E family
def E1():
    F = -sp.exp(b * sp.cos(th)) / b                      # antiderivative of e^{b cos th} sin th
    ok_anti = sp.simplify(sp.diff(F, th) - sp.exp(b * sp.cos(th)) * sp.sin(th)) == 0
    I = (F.subs(th, sp.pi) - F.subs(th, 0)) / 2           # int dOmega/4pi e^{b s.e}
    ok_c0 = sp.simplify((c0 * I - 1).rewrite(sp.exp)) == 0
    rep("E1 pinned scale", ok_anti and ok_c0,
        "int dOmega/4pi e^(beta s.e) = sinh(beta)/beta, so c0 = beta/sinh beta makes every record-to-record bond average to "
        "the weight 1 of a bond with an empty end")


def E2():
    # Z(s_1..s_k) = c0^k int dOmega/4pi e^{b s.S} = c0^k sinh(b|S|)/(b|S|)   (E1 with b -> b|S|)
    ok_vals = (sp.simplify(Zk(1) - 1) == 0 and sp.simplify((Zk(2) - b * sp.cosh(b) / sp.sinh(b)).rewrite(sp.exp)) == 0
               and sp.limit(sp.sinh(x) / x, x, 0) == 1)
    phi2 = sp.diff(sp.log(sp.sinh(x) / x), x, 2)
    ok_conv = sp.simplify((phi2 - (1 / x**2 - 1 / sp.sinh(x)**2)).rewrite(sp.exp)) == 0
    bv = sp.Rational(2)
    vals = [float(Zk(k).subs(b, bv)) for k in range(0, 7)]
    ok_num = all(vals[k + 1] > vals[k] for k in range(1, 6)) and abs(vals[1] - 1) < 1e-15
    opp = float((c0**2).subs(b, bv))
    rep("E2 formation factor", ok_vals and ok_conv and ok_num and opp < 1,
        "Z = c0^k sinh(beta|S|)/(beta|S|), S = sum of the neighbours' contents; mean 1 over independent contents (neutral); "
        "aligned Z_k = c0^k sinh(k beta)/(k beta): Z_0 = Z_1 = 1, Z_2 = beta coth beta, log Z_k convex in k "
        f"((log(sinh x/x))'' = 1/x^2 - 1/sinh^2 x > 0), so Z_k > 1 for k >= 2; beta=2: Z_2..Z_6 = "
        + ", ".join(f"{v:.3f}" for v in vals[2:]) + f"; opposite pair c0^2 = {opp:.3f}")
    return vals


def E3():
    comp = sp.integrate(c0 * sp.exp(b * sp.cos(th)) * sp.cos(th) * sp.sin(th), (th, 0, sp.pi)) / 2
    L = sp.cosh(b) / sp.sinh(b) - 1 / b
    ok_L = sp.simplify((comp - L).rewrite(sp.exp)) == 0
    phi = sp.symbols('phi')
    ok_tr = sp.integrate(sp.cos(phi), (phi, 0, 2 * sp.pi)) == 0 and sp.integrate(sp.sin(phi), (phi, 0, 2 * sp.pi)) == 0
    Lv = float(L.subs(b, 2))
    field = [(0.5 * Lv)**d for d in range(1, 5)]
    rep("E3 tree field", ok_L and ok_tr,
        "one step: int dOmega/4pi c0 e^(beta a.s) s = L(beta) a, L = coth beta - 1/beta; on a window without a cycle "
        "occupancies are independent (density z/(1+z)) and <n_y e(s_y) | s_x = a> = (rho L)^d e(a) at path distance d; "
        "beta=2, rho=1/2: " + ", ".join(f"{v:.4f}" for v in field))


# ------------------------------------------------------------------ C family
def C1():
    ok = True
    for m in range(0, 7):
        cnt = 0
        for p in itertools.product(range(-m, m + 1), repeat=3):
            for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                q = (p[0] + d[0], p[1] + d[1], p[2] + d[2])
                if max(abs(v) for v in q) > m:
                    cnt += 1
        ok &= cnt == 6 * (2 * m + 1)**2
    mm = sp.symbols('m', positive=True)
    ok &= sp.simplify((1 / mm - 1 / (mm + 1)) * (2 * mm + 1) - (1 / mm + 1 / (mm + 1))) == 0
    rep("C1 shells", ok, "edges leaving [-m,m]^3: 6(2m+1)^2 (m=0..6, enumerated); (1/m-1/(m+1))(2m+1) = 1/m+1/(m+1)")


def trial_energy(R, M=20000):
    """E(f_R) for f = min(1, R/|x|_inf): exact partial sum to M plus the tail bound sum_{m>M} 4/m^2 <= 4/M."""
    s = sum((Fr(1, m) + Fr(1, m + 1))**2 for m in range(R, M + 1))
    return 6 * R * R * s, 6 * R * R * (s + Fr(4, M))


def C2():
    rows = []
    ok = True
    for R in range(1, 9):
        lo, hi = trial_energy(R, 4000)
        ok &= hi <= 24 + 24 * R <= 48 * R
        rows.append(float(hi) / R)
    rep("C2 Dirichlet bound", ok,
        "Cap(S) <= E(f_R) <= 6R^2 * 4(1/R^2 + 1/R) <= 48R for S inside [-R,R]^3 (f = min(1,R/|x|_inf), exact Fractions); "
        "E(f_R)/R for R=1..8: " + ", ".join(f"{v:.2f}" for v in rows))


CACHE = {}


def Gz3(d):
    k = tuple(sorted(abs(v) for v in d))
    if k in CACHE:
        return CACHE[k]
    a, bb, c = k
    f = lambda t: ive(a, 2 * t) * ive(bb, 2 * t) * ive(c, 2 * t)
    r2 = a * a + bb * bb + c * c
    pts = sorted(set([0, 0.5, 2, max(4, r2 / 6), max(10, r2 / 2), 60, 400, 4000]))
    tot = sum(quad(f, lo, hi, limit=400, epsabs=1e-15, epsrel=1e-13)[0] for lo, hi in zip(pts[:-1], pts[1:]))
    tot += quad(f, 4000, np.inf, limit=200)[0]
    CACHE[k] = tot
    return tot


def cap(S):
    S = list(S)
    Mt = np.array([[Gz3((p[0] - q[0], p[1] - q[1], p[2] - q[2])) for q in S] for p in S])
    return np.linalg.solve(Mt, np.ones(len(S))).sum()


def C3():
    g0, g1 = Gz3((0, 0, 0)), Gz3((1, 0, 0))
    ok_g = abs(g1 - (g0 - 1 / 6)) < 1e-12 and abs(g0 - 0.2527310098) < 1e-9
    caps = [cap(itertools.product(range(L), repeat=3)) for L in range(1, 9)]
    bound_ok = all(caps[L - 1] <= float(trial_energy(max(1, L // 2), 4000)[1]) for L in range(1, 9))   # side L inside [-R,R]^3
    inc = np.diff(caps)
    lines = [cap([(i, 0, 0) for i in range(L)]) / L for L in (2, 4, 8, 16, 32)]
    pairs = [cap([(0, 0, 0), (d, 0, 0)]) * g0 / 2 for d in (1, 2, 4, 8, 16)]
    ok = ok_g and bound_ok and all(np.diff(inc) > 0) and inc[-1] < 8.31 and all(np.diff(lines) < 0) \
        and all(np.diff(pairs) > 0) and pairs[-1] > 0.98
    rep("C3 massless Z^3 (executed)", ok,
        f"G(0)={g0:.10f}, G(1)=G(0)-1/6; Cap(cube L)/L = " + ", ".join(f"{c/L:.3f}" for L, c in enumerate(caps, 1))
        + f" (increments -> {inc[-1]:.3f}, below 4pi*0.6607=8.30); Cap/(N/G(0)) at L=8: {caps[-1]*g0/512:.4f}; "
        "lines Cap/L = " + ", ".join(f"{v:.3f}" for v in lines) + "; pair at d=1,2,4,8,16: Cap/(2/G(0)) = "
        + ", ".join(f"{v:.4f}" for v in pairs))
    return g0, caps


# ------------------------------------------------------------------ P family
NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def profile(S):
    S = set(S)
    out = {(p[0] + d[0], p[1] + d[1], p[2] + d[2]) for p in S for d in NB} - S
    return Counter(sum(((y[0] + d[0], y[1] + d[1], y[2] + d[2]) in S) for d in NB) for y in out)


def P1():
    bad = sum(1 for a, bb, c in itertools.product(range(1, 7), repeat=3)
              if set(profile(itertools.product(range(a), range(bb), range(c)))) != {1})
    rep("P1 boxes", bad == 0,
        "every empty site next to an a x b x c box (a,b,c <= 6, all 216) touches exactly one of its records: an aligned box "
        "held in vacuum produces at the void rate everywhere (Z_1 = 1): no excess, no transit halo")


def P2():
    rows = []
    for R2 in (4, 9, 16, 25, 36, 49, 64, 81, 100, 144):
        R = int(np.ceil(np.sqrt(R2)))
        S = [p for p in itertools.product(range(-R, R + 1), repeat=3) if p[0]**2 + p[1]**2 + p[2]**2 <= R2]
        pr = profile(S)
        rows.append((R2, len(S), pr.get(2, 0), pr.get(3, 0), max(pr)))
    pk = [(r[2] + r[3]) / r[0] for r in rows]
    ok = all(r[4] <= 3 for r in rows) and 3.5 <= min(pk) and max(pk) <= 6 and (rows[-1][2] + rows[-1][3]) / rows[-1][1] < 0.12
    rep("P2 balls", ok,
        "discrete balls |x|^2 <= R^2: sites touching 2 or 3 records (P2,P3) = " + ", ".join(f"R^2={r[0]}:{r[2]},{r[3]}" for r in rows[::3])
        + f"; pockets/R^2 in [{min(pk):.2f},{max(pk):.2f}] (surface), pockets/N {(rows[0][2]+rows[0][3])/rows[0][1]:.2f} -> "
        f"{(rows[-1][2]+rows[-1][3])/rows[-1][1]:.3f}; excess production at R^2=144: z[{rows[-1][2]}(Z_2-1) + {rows[-1][3]}(Z_3-1)]")


def P3():
    D = sum(sp.binomial(5, k) * rho**k * (1 - rho)**(5 - k) * (Zk(k + 1) - Zk(k)) for k in range(0, 6))
    lead = sp.series(D, rho, 0, 2).removeO()
    ok_lead = sp.simplify((lead - 5 * rho * (Zk(2) - 1)).rewrite(sp.exp)) == 0
    grid = [float(D.subs({b: bv, rho: rv})) for bv in (sp.Rational(1, 2), 2, 5) for rv in (sp.Rational(1, 10), sp.Rational(1, 2), sp.Rational(9, 10))]
    rep("P3 face excess (tree level)", ok_lead and min(grid) > 0,
        "ordered medium, perfect alignment, independent occupancies: excess production at an empty face site = "
        "z(1-rho)^2 D, D = E[Z(1+B5) - Z(B5)] = 5 rho (beta coth beta - 1) + O(rho^2) > 0: a box's halo grows like its surface")


def main():
    E1(); E2(); E3()
    C1(); C2(); C3()
    P1(); P2(); P3()
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL at the pinned scale c0 = beta/sinh beta no candidate gives a far field proportional to N for a "
              "compact source: (a),(b) in the quadratic stand-in a pinned set is a Dirichlet condition with far field theta0 Cap(S) "
              "G(r), Cap(S) <= 48R inside a cube of half-side R (exact; executed Cap(cube L) ~ 8.3 L), additive only for dilute "
              "pinned records (theta0/G(0) each, signed); (b) unpinned, (c), (d) put nothing into the transverse channel (symmetry, "
              "all orders); (d) the transit halo is Q G(r)/kappa, and a lump held in empty surroundings has excess production only "
              "at sites touching >= 2 of its records, Z_k - 1 = (beta/sinh beta)^k sinh(k beta)/(k beta) - 1: none for a box, "
              "~5.5 R^2 sites for a ball; in an ordered medium (tree level) the excess is per face site")
        print("HIT: at the pinned scale the formation factor next to records of contents s_j is (beta/sinh beta)^k "
              "sinh(beta|sum s_j|)/(beta|sum s_j|), log-convex in k for agreeing contents; a lump held in empty surroundings "
              "therefore produces excess records only at empty sites touching two or more of its records (none next to a box, "
              "about 5.5 R^2 next to a ball of radius R), and in the quadratic stand-in a pinned set's far field is theta0 Cap(S) "
              "G(r) with Cap(S) <= 48R for S inside a cube of half-side R: no compact source of N records gives a far field "
              "proportional to N in these channels")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
