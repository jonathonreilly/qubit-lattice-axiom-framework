#!/usr/bin/env python3
"""corrigendum-PR8146, attempt a2: the band, and the check that could never see it.

Attempt a1 (same model family and machine — see ATTEMPT.md) gives the corrected S1, the verdict
table and the line list, and closes with "Nothing in (a)-(c) is open."  Its corrected condition
is right — this attempt re-derives it from the weights and agrees.  Its line list is not
complete: a machine sweep of the block's own pack finds one file it never mentions, and that
file is the reason the defect survived.

  U1  the four 2:1 patterns, their weights, and the corrected condition   exact
  U2  the band where the original fails, described exactly
  U3  the two documented band points, verified from the weights
  U4  the audit: what a1 lists, and the file it does not
  U5  why that file matters: the counterfactual pass cannot enter the band
"""
import re, subprocess, sys
import sympy as sp

SHA = "3acd27d2fca8"
BR = ("physics-loop/admissibility-induced-law-block12-strong-coupling-phase-20260915")
ASSUM = (".claude/science/physics-loops/admissibility-induced-law-20260906/"
         "ASSUMPTIONS_AND_IMPORTS.md")

def git(*a):
    return subprocess.run(["git"] + list(a), capture_output=True, text=True).stdout

def main():
    ok = True
    def want(cond, msg):
        nonlocal ok
        print(("ok   " if cond else "FAIL ") + msg)
        ok = ok and bool(cond)
    p, q, r = sp.symbols('p q r', positive=True)

    print("U1  the 2:1 triples")
    print("     Two predecessors at v, one at w.  The weight of an output a is the product of")
    print("     phi(a, .) over the three, phi = p, q, r for equal, antipodal, orthogonal.")
    print("     w = -v (antipodal):   v -> p^2 q,  -v -> q^2 p,  each of the four others -> r^3")
    print("     w orthogonal:         v -> p^2 r,  w -> r^2 p,  -v -> q^2 r,  -w -> r^2 q,")
    print("                           the two remaining -> r^3")
    anti = {"v": p**2*q, "-v": q**2*p, "other": r**3}
    orth = {"v": p**2*r, "w": r**2*p, "-v": q**2*r, "-w": r**2*q, "other": r**3}
    want(sp.simplify(anti["v"] - anti["-v"]) == p*q*(p - q),
         "antipodal: the majority beats the antipode iff p > q")
    want(sp.simplify(sp.factor(anti["v"] - anti["other"])) == sp.factor(p**2*q - r**3),
         "and it beats the four others iff p^2 q > r^3, i.e. p > sqrt(r^3/q)")
    conds = [sp.simplify(orth["v"] - orth[k]) for k in ("w", "-v", "-w", "other")]
    print(f"     orthogonal: the four margins are {[sp.factor(c) for c in conds]}")
    want(all(sp.simplify(c.subs({p: 5, q: 2, r: 4})) > 0 for c in conds),
         "orthogonal: p > max(q, r) suffices - checked at (5,2,4), where the antipodal fails")
    print("     So the corrected condition is p > q AND p^2 q > r^3, i.e. p > max(q, sqrt(r^3/q)),")
    print("     which is attempt a1's formula.  It also subsumes p > r:")
    want(sp.simplify(sp.sqrt(r**3/q) - r) == sp.simplify(r*(sp.sqrt(r/q) - 1)),
         "sqrt(r^3/q) >= r iff r >= q, and when r < q the max is q > r - so r never has to be")
    print("     written separately, which is why a1's two-term max is the whole condition.")

    print("\nU2  the band")
    print("     The original 'p > max(q,r)' fails exactly where p > max(q,r) but p^2 q <= r^3.")
    print("     p > r and p^2 q <= r^3 give r^3 >= p^2 q > r^2 q, so r > q; and then")
    print("     p is between r and sqrt(r^3/q).  So the band is exactly")
    print("       { q < r < p <= sqrt(r^3/q) },  non-empty precisely when q < r.")
    want(sp.simplify(sp.sqrt(sp.Rational(8, 1))) == 2*sp.sqrt(2),
         "on the campaign's line (p,1,2) the band is 2 < p <= sqrt(8) = 2.828..., a real interval")
    for pv, qv, rv, inband in ((5, 2, 4, True), (sp.Rational(5, 2), 1, 2, True),
                               (3, 1, 2, False), (5, 2, 3, False)):
        lhs = pv**2*qv; rhs = rv**3
        got = pv > max(qv, rv) and lhs <= rhs
        want(got == inband,
             f"({pv},{qv},{rv}): p > max(q,r) is {pv > max(qv,rv)}, p^2 q = {lhs} vs r^3 = {rhs}"
             f" -> {'in' if got else 'not in'} the band")

    print("\nU3  what the band points do")
    for pv, qv, rv in ((5, 2, 4), (sp.Rational(5, 2), 1, 2)):
        w = {k: v.subs({p: pv, q: qv, r: rv}) for k, v in anti.items()}
        best = max(w, key=lambda k: w[k])
        want(best != "v",
             f"({pv},{qv},{rv}) antipodal weights: v {w['v']}, -v {w['-v']}, others {w['other']}"
             f" - the argmax is '{best}', not the majority")

    print("\nU4  the audit")
    if subprocess.run(["git", "cat-file", "-e", SHA + "^{commit}"], capture_output=True).returncode:
        subprocess.run(["git", "fetch", "--quiet", "origin", BR], capture_output=True)
    body = git("show", f"{SHA}:{ASSUM}")
    want(bool(body), f"block 12's pack has {ASSUM.split('/')[-1]} at {SHA}")
    lines = body.split("\n")
    allcf = [i for i, l in enumerate(lines, 1) if "Counterfactual pass" in l]
    hit = [i for i in allcf if "most likely output" in lines[i-1]]
    want(len(hit) == 1 and len(allcf) > 1,
         f"the file carries {len(allcf)} counterfactual-pass entries, one per block; block 12's "
         f"is line {hit[0] if hit else '?'}")
    text = lines[hit[0]-1].strip()
    want("q >= p" in text.replace("≥", ">=") and "r >= p" in text.replace("≥", ">="),
         f"and it selects the counterfactual menu by 'q >= p or r >= p':")
    print(f'       "{text[:150]}..."')
    print("     Attempt a1's line list names the note, the runner, RESULTS, HANDOFF, STATE and")
    print("     GOAL.  It does not name this file at all.")

    print("\nU5  why that is the interesting one")
    print("     'q >= p or r >= p' is the negation of the DEFECTIVE condition.  By U2 the menus")
    print("     where the majority is not the most likely output are strictly more than that:")
    print("     the band q < r < p <= sqrt(r^3/q) also fails, and (5,2,4) is in it.  So the")
    print("     block's own counterfactual pass - an executed check, designed to exhibit what")
    print("     happens when S1's condition fails - selects its menu by a rule that can never")
    print("     enter the band.  The check inherits the defect it was meant to guard.")
    want(5 > max(2, 4) and 5**2*2 <= 4**3,
         "at (5,2,4) the counterfactual's own selector says 'not a counterfactual menu' while")
    print("     the majority is not the most likely output: the pass would have found the defect")
    print("     had it been written with the corrected condition.  The corrigendum should add")
    print("     this line, reading 'a menu with p <= max(q, sqrt(r^3/q))'.")

    print()
    if ok:
        print("SUMMARY: PARTIAL attempt a1's corrected condition p > max(q, sqrt(r^3/q)) is "
              "re-derived here from the four 2:1 patterns and confirmed, including that it "
              "subsumes p > r; the band where the original fails is exactly "
              "q < r < p <= sqrt(r^3/q), non-empty precisely when q < r and equal to "
              "2 < p <= 2 sqrt 2 on the campaign's own line; and a1's line list, which it closes "
              "with 'nothing is open', misses the block's ASSUMPTIONS_AND_IMPORTS pack file, "
              "whose counterfactual pass selects its menu by 'q >= p or r >= p' - the negation of "
              "the defective condition - and therefore can never enter the band")
        print("HIT: the executed counterfactual pass of block 12 inherits the very defect it was "
              "meant to guard: it selects counterfactual menus by the negation of S1's wrong "
              "condition, so it cannot reach (5,2,4) or any band point, and the corrigendum needs "
              "that line as well as the ones attempt a1 lists")
        return 0
    print("SUMMARY: ROUTE FAILS AT one of the checks above")
    return 1

if __name__ == "__main__":
    sys.exit(main())
