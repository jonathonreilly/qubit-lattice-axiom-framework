#!/usr/bin/env python3
"""(5.5) on long sheets of intermediate flux, the target lead's second question, Text 3.5.

Map: the final map D3 of hard-core--independent_field_ineq.py, reused unchanged. Coarse 01-plaquette at the corner of the torus.
THIN(a, b, th): V = q on links along 0 at x_0 = a, x_1 >= b, one thin 2-sheet with holonomy q = rot(th), that is f_p = 2 sin(th / 2) on its plaquettes.
FAT(a, b, w, th): the same holonomy spread over a core of w x w plaquettes, by the links along 0 at a <= x_0 < a + w, with angle th * clip((x_1 - b + 1) / w, 0, 1) / w, so flux about th / w^2 per plaquette.
PRE-STATED CRITERIA, written before the first run. eps_0 = 0.05 and the right side as in that script.
  PASS-SCAN: max Ratio <= 12 sqrt(log L), its earlier bound, at L = 3, 5, for th in 0.02, 0.06, 0.2, 0.5, 1, 1.5, 2, 2.5, 3.1 and all positions a, b tried. FAIL-SCAN otherwise.
  The output that matters is the maximum of Ratio against th: a value above 1 by a clear margin would raise the lower bound on C_OS, which so far is 1, reached on the centre sheet.
  This can falsify (5.5) on this family. It cannot confirm it.
  ADDED BEFORE ANY RESULT WAS SEEN. The first run was stopped after 16 minutes with nothing read, its output buffered by a pipe. An evaluation takes 0.2 s at L = 3 and 13 s at L = 5, so at L = 5 the grid is cut to th in 0.06, 0.5, 1.5, 3.1,
  16 thin positions and 8 fat ones. The criteria are unchanged.
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import importlib.util, json, math, resource, sys

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("field_ineq", os.path.join(here, "hard-core--independent_field_ineq.py"))
fi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fi)


def fat_field(a, b, w, q_th):
    def link(s, mu):
        if mu == 0 and a <= s[0] < a + w:
            frac = min(1.0, max(0.0, (s[1] - b + 1) / w))
            return fi.rot(q_th * frac / w)
        return fi.ONE
    return fi.Field(link)


def ratio(field, L):
    curv, m = fi.plaquette_W(field, L, "rule")
    r, l1, l2 = fi.rhs(field, L)
    return (curv / r if r > 1e-14 else 0.0), curv, m, l1, l2


def main():
    out = []
    ths3 = [0.02, 0.06, 0.2, 0.5, 1.0, 1.5, 2.0, 2.5, 3.1]
    ths5 = [0.06, 0.5, 1.5, 3.1]
    for L, ths, positions, fats in ((3, ths3, [(a, b) for a in range(-1, 5) for b in range(-1, 5)], [2, 3, 5]),
                                    (5, ths5, [(a, b) for a in (0, 1, 2, 5) for b in (1, 2, 3, 6)], [3, 5])):
        for th in ths:
            best = (0.0, None)
            for a, b in positions:
                rr = ratio(fi.sheet_field(a, b, fi.rot(th)), L)
                if rr[0] > best[0]:
                    best = (rr[0], ("thin", a, b) + rr[1:])
            bestf = (0.0, None)
            for w in fats:
                for a, b in positions[:: max(1, len(positions) // (12 if L == 3 else 4))]:
                    rr = ratio(fat_field(a, b, w, th), L)
                    if rr[0] > bestf[0]:
                        bestf = (rr[0], ("fat", w, a, b) + rr[1:])
            print(f"L={L} th={th:.2f} f={2 * math.sin(th / 2):.3f}  thin max Ratio {best[0]:.3f} {best[1][1:3] if best[1] else ''}; fat max Ratio {bestf[0]:.3f} {bestf[1][1:4] if bestf[1] else ''}", flush=True)
            out.append({"L": L, "th": th, "thin": best[0], "fat": bestf[0]})
            fi.check_rss()
    bound = {3: 12 * math.sqrt(math.log(3)), 5: 12 * math.sqrt(math.log(5))}
    worst = max(max(r["thin"], r["fat"]) / bound[r["L"]] for r in out)
    verdict = "PASS-SCAN" if worst <= 1 else "FAIL-SCAN"
    top = max(max(r["thin"], r["fat"]) for r in out)
    print(verdict, f"largest Ratio seen {top:.3f}", flush=True)
    with open(os.path.join(here, "hard-core--independent_sheet_scan_results.json"), "w") as fh:
        json.dump({"rows": out, "verdict": verdict, "top": top}, fh, indent=1)
    print("rss GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 ** 3, flush=True)


if __name__ == "__main__":
    main()
