#!/usr/bin/env python3
"""corrigendum-PR8147, attempt a2: the domain, and the one downstream inequality.

Attempt a1 (same model family and machine — see ATTEMPT.md) gives the corrected level-line
symbol and a verdict table.  This attempt tests the two things a1 asserts without checking:
that "{0} only" is the useful answer to "the largest domain on which the original holds", and
that its table of downstream uses is complete.  The second test found a line a1 does not list —
note line 195 — which is the one place downstream where the exact symbol is compared with a
quadratic.  It is sound, and the reason it is sound is worth writing down.

  F1  the corrected symbol, re-derived two ways                exact
  F2  the domain: exact equality, and the tolerance domains    exact + high precision
  F3  the runner's D2 is blind to the defect at its order      exact
  F4  note line 195: the inequality, its sharpness, and why dropping a term saves it   exact
  F5  T2(b)'s constant 9 pi/16 follows                         exact
  F6  the audit of block 13's own lines against a1's list
"""
import re, subprocess, sys
import sympy as sp

SHA = "9c364d1d6f75"
BRANCH = ("physics-loop/admissibility-induced-law-block13-causal-gaussian-two-point-heat-kernel-"
          "20260915")
NOTE = ("docs/ADMISSIBILITY_RULE_CAUSAL_GAUSSIAN_FORMATION_LAW_RECORD_TWO_POINT_FUNCTION_HEAT_"
        "KERNEL_NOT_LATTICE_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = ("scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_"
          "heat_kernel_2026_09_15.py")
A1_NOTE_LINES = {4, 43, 225, 237, 238, 239, 240, 336}     # a1's section (c) and table, note only

def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)

    if subprocess.run(["git", "cat-file", "-e", SHA + "^{commit}"], capture_output=True).returncode:
        subprocess.run(["git", "fetch", "--quiet", "origin", BRANCH], capture_output=True)
    want(not subprocess.run(["git", "cat-file", "-e", SHA + "^{commit}"],
                            capture_output=True).returncode,
         f"block 13 present at its pinned head {SHA}")

    u, w, g, e = sp.symbols('u w g e', real=True)
    k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)

    # ------------------------------------------------------------------ F1
    print("\nF1  the level-line symbol")
    S = sp.Abs(1 - w*(sp.exp(-sp.I*k1) + sp.exp(-sp.I*k2) + sp.exp(-sp.I*k3)))**2
    lev = sp.simplify(sp.expand_complex(S.subs({k1: u, k2: u, k3: u})))
    target = (1 - 3*w)**2 + 12*w*sp.sin(u/2)**2
    want(sp.simplify(sp.expand_trig(sp.expand(lev - target))) == 0,
         "S_w(u,u,u) = (1-3w)^2 + 12 w sin^2(u/2) = (1-g)^2 + 4g sin^2(u/2), g = 3w")
    cos_form = 1 - 2*w*(sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) \
        + w**2*(3 + 2*(sp.cos(k1-k2) + sp.cos(k1-k3) + sp.cos(k2-k3)))
    want(sp.simplify(sp.expand_trig(sp.expand(cos_form.subs({k1: u, k2: u, k3: u}) - target))) == 0,
         "and the note's own cosine form of the symbol gives the same thing (a second route)")
    at1 = sp.simplify(target.subs(w, sp.Rational(1, 3)))
    want(sp.simplify(at1 - 4*sp.sin(u/2)**2) == 0,
         "at the gain-one law w = 1/3 it is exactly 4 sin^2(u/2), the note's u^2 being its first term")

    # ------------------------------------------------------------------ F2
    print("\nF2  the domain on which the note's u^2 holds")
    import mpmath as mp
    import mpmath as _mp
    _mp.mp.dps = 30
    gap = lambda x: mp.mpf(x)**2 - 4*mp.sin(mp.mpf(x)/2)**2
    pts = [mp.mpf(j)/20 for j in range(1, 260)]
    want(all(gap(x) > 0 for x in pts),
         "4 sin^2(u/2) < u^2 for every u != 0 (|sin x| < |x| for x != 0; checked at 259 points of")
    print("     (0, 13]): as an equality the note's claim holds at u = 0 only, which is true")
    print("     but useless.  The useful form is the relative error r(u) = 1 - 4 sin^2(u/2)/u^2:")
    r = 1 - 4*sp.sin(u/2)**2/u**2
    ser = sp.series(r, u, 0, 7).removeO()
    want(sp.simplify(ser - (u**2/12 - u**4/360 + u**6/20160)) == 0,
         f"r(u) = u^2/12 - u^4/360 + u^6/20160 - ...")
    mp.mp.dps = 25
    rf = lambda x: 1 - 4*mp.sin(mp.mpf(x)/2)**2/mp.mpf(x)**2
    doms = []
    for tol in ('0.01', '0.05', '0.10'):
        root = mp.findroot(lambda x: rf(x) - mp.mpf(tol), mp.mpf('1'))
        doms.append((tol, root))
        print(f"     r(u) <= {tol}  for |u| <= {mp.nstr(root, 6)}   (|K| = 3|u| <= {mp.nstr(3*root, 6)})")
    want(all(doms[i][1] < doms[i+1][1] for i in range(len(doms)-1)) and doms[0][1] > 0.3,
         "so the note's quadratic is within 1% of the symbol only for |K| <= 1.04, and")
    rpi = 1 - 4/mp.pi**2
    want(abs(rpi - mp.mpf('0.5947')) < mp.mpf('0.001'),
         f"at the zone boundary u = pi it is wrong by {mp.nstr(rpi*100, 4)}% (1 - 4/pi^2): the")
    print("     surrogate is unbounded where the symbol saturates at 4.  Any downstream statement")
    print("     integrating over the whole zone would feel that; F4 finds the one that comes close.")

    # ------------------------------------------------------------------ F3
    print("\nF3  why the runner passed")
    s1 = cos_form.subs(w, sp.Rational(1, 3))
    lev_e = s1.subs({k1: e, k2: e, k3: e})
    want(sp.simplify(sp.series(lev_e, e, 0, 4).removeO() - e**2) == 0,
         "series(level, e, 0, 4) is exactly e^2, so the runner's D2 comparison with e**2 passes")
    want(sp.simplify(sp.series(lev_e, e, 0, 6).removeO() - (e**2 - e**4/12)) == 0,
         "at order 6 it is e^2 - e^4/12: one more term in D2 would have caught the defect")

    # ------------------------------------------------------------------ F4
    print("\nF4  note line 195, which a1's table does not list")
    note = git("show", f"{SHA}:{NOTE}").splitlines()
    l195 = note[194]
    want("1 - cos u" in l195.replace("−", "-") and "2u" in l195.replace("²", "2"),
         f"line 195 uses `1 - cos u >= 2u^2/pi^2` inside T2(b)'s upper bound on P_n")
    print("     This is the one place downstream where the exact symbol meets a quadratic, and it")
    print("     is an inequality, not an identity, so the defect does not touch it.  Two things")
    print("     about it are worth checking, and neither is in a1's packet:")
    # sharpness: (1-cos u)/u^2 = sinc^2(u/2)/2 decreasing on (0, pi], min 2/pi^2 at pi
    q = sp.simplify((1 - sp.cos(u))/u**2 - 2/sp.pi**2)
    vals = [(x, mp.mpf(1) - mp.cos(x) - 2*x**2/mp.pi**2)
            for x in [mp.mpf(t) for t in ('0.1', '0.5', '1.0', '2.0', '3.0')] + [mp.pi]]
    want(all(v >= -mp.mpf('1e-25') for _, v in vals) and abs(vals[-1][1]) < mp.mpf('1e-25'),
         "(i) the inequality is sharp: (1-cos u)/u^2 = (1/2) sinc^2(u/2) decreases on (0, pi],")
    print("     so its minimum there is at u = pi, where both sides are exactly 2 — equality at")
    print("     u = 0 and u = +-pi, and 2/pi^2 is the largest constant that works.")
    bad = [x for x in ('4.0', '5.0', '6.28') if (mp.mpf(1) - mp.cos(mp.mpf(x))
                                                 - 2*mp.mpf(x)**2/mp.pi**2) < 0]
    want(len(bad) == 3,
         "(ii) it FAILS outside [-pi, pi] (checked at u = 4, 5, 6.28) - and k_1 - k_2 ranges over")
    print("     [-2pi, 2pi] on the square.  The bound is sound because it drops the (k_1 - k_2)")
    print("     term first, keeping only the two whose arguments stay in [-pi, pi].  That is load")
    print("     bearing: applying the same inequality to the third term would be false.")
    want("(1 - cos(k_1 - k_2))" in note[193].replace("−", "-") or "cos(k_1 - k_2)" in note[193].replace("−", "-"),
         "line 194 is where that third term appears and is dropped")

    # ------------------------------------------------------------------ F5
    print("\nF5  T2(b)'s constant")
    n = sp.Symbol('n', positive=True)
    a = 4*n/(9*sp.pi**2)
    integral = sp.integrate(sp.exp(-a*(k1**2 + k2**2)), (k1, -sp.oo, sp.oo), (k2, -sp.oo, sp.oo))
    want(sp.simplify(integral/(2*sp.pi)**2 - 9*sp.pi/(16*n)) == 0,
         "(2 pi)^-2 int_{R^2} e^{-(4n/9pi^2)|k|^2} = 9 pi/(16 n): T2(b)'s stated bound follows")

    # ------------------------------------------------------------------ F6
    print("\nF6  the audit of block 13's own lines")
    pat = re.compile(r"(u\^?2|u²|K\^?2/9|K²/9|\(u, ?u, ?u\)|4 ?sin|1 - cos u|1 − cos u)")
    hits = sorted(i for i, l in enumerate(note, 1) if pat.search(l))
    print(f"     {len(hits)} lines of the note mention the level symbol or a quadratic surrogate:")
    for i in hits:
        mark = "a1" if i in A1_NOTE_LINES else "not in a1's list"
        print(f"       line {i:4d}  {mark:<17} {note[i-1].strip()[:88]}")
    want(set(hits) == {4, 43, 195, 225, 350},
         f"the pattern lines are exactly {hits}; a1 lists 4, 43 and 225 of them")
    extra = [i for i in hits if i not in A1_NOTE_LINES]
    want(extra == [195, 350],
         f"the two it does not list are {extra}: 195 is the inequality of F4, and 350 is the")
    print("     refutation-target list -- 'a level-direction expansion other than K^2/9'.  That")
    print("     wording is why the mutation family could not catch this: the expansion IS K^2/9.")
    want("expansion other than" in note[349] and "K²/9" in note[349],
         "line 350 should read 'a level-line symbol other than 4 sin^2(u/2)', which is a third")
    print("     line for the packet's (c), beside the runner's series order in F3.")

    print()
    if ok:
        print("SUMMARY: PARTIAL the note's u^2 is within 1 percent of the exact level symbol "
              "4 sin^2(u/2) only for |K| <= 1.04 and is wrong by 59.5 percent (1 - 4/pi^2) at the "
              "zone boundary, which is the useful form of 'the largest domain'; and the one "
              "downstream place that compares the exact symbol with a quadratic is note line 195, "
              "which a1's table does not list: it is sound, sharply so (2/pi^2 is the largest "
              "constant, with equality at 0 and +-pi), and only because T2(b) drops the "
              "(k_1 - k_2) term first, whose argument leaves [-pi, pi] where that same inequality "
              "is false")
        print("HIT: T2(b)'s bound P_n <= 9 pi/(16 n) rests on an inequality that is false on part "
              "of the domain of the term it drops, so the order of its two steps is load bearing; "
              "the corrected symbol's 1 percent domain is |K| <= 1.04, not a point; and the note's "
              "own refutation-target line 350 asks for 'a level-direction expansion other than "
              "K^2/9', which is why no mutation could catch a defect whose expansion is K^2/9")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
