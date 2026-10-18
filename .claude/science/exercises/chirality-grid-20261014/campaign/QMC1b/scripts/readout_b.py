"""QMC-1b readout: tables and the FIXED readings (PREREG sections 6-7).  python3 readout_b.py"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_b import load_all, ratio, summarize
RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")
res = load_all(RUNS)

print("### Free references (W = 0, one exact sweep)")
free = {}
for f in ("f2", "fG"):
    v = {}
    for L in (4, 6):
        p = os.path.join(RUNS, f"L{L}_{f}_W0.npz")
        if os.path.exists(p):
            v[L] = summarize(p)["S"]
    if len(v) == 2:
        free[f] = v
        print(f"{f}: S10/L^2 L4 {v[4]:.4f}, L6 {v[6]:.4f}, ratio {v[6] / v[4]:.3f}")

print("\n### Runs")
print("| filter | L | W | n | acc | s/sweep | S10/L^2 | tau_int | thirds | frac(9,10) | S(pi,pi)/L^2 | E3w primary | E3w s-block | "
      "E3w by corner | max phase | light dev | wrap dev |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for k in sorted(res):
    r = res[k]
    corner = "; ".join(f"{c[4:]} {r[c]:.4f}" for c in ("E3w_00", "E3w_pp", "E3w_p0") if c in r)
    print(f"| {r['filt']} | {r['L']} | {r['W']:g} | {r['n']} | {r['acc']:.2f} | {r['sec']:.1f} | {r['S']:.4f}({r['Se']:.4f}) | "
          f"{r['tau_int']:.1f} | {', '.join(f'{t:.3f}' for t in r['thirds'])} | {r['frac910']:.2f} | "
          f"{r['Spi']:.4f}({r['Spie']:.4f}) [n={r['nSpi']}] | {r['E3w']:.4f}({r['E3we']:.4f}) | {r['E3w_s']:.4f}({r['E3w_se']:.4f}) | "
          f"{corner} | {r['maxphase']:.1e} | {r['light_dev']:.1e} | {r['maxdev']:.1e} |")

print("\n### Gates monitored in production")
bad = [k for k, r in res.items() if not (r["maxphase"] <= 1e-8 and r["light_dev"] <= 1e-8)]
print(f"(ii-b) max phase <= 1e-8 and (iv) light dev <= 1e-8 in every run: {not bad} {bad}")

print("\n### Ratios and windows")
win, R = {"fG": [], "f2": []}, {}
unknown = {"fG": [], "f2": []}
for f in ("fG", "f2"):
    for W in (2.0, 4.0):
        r4, r6 = res.get((f, 4, W)), res.get((f, 6, W))
        if r4 is None or not r4["complete"]:
            print(f"{f} W{W:g}: L4 missing"); unknown[f].append(W); continue
        if r4["E3w"] > 0.1:
            print(f"{f} W{W:g}: L4 E3w {r4['E3w']:.4f} > 0.1: not a window"); continue
        if r6 is None or not r6["complete"]:
            print(f"{f} W{W:g}: L4 E3w {r4['E3w']:.4f}; L6 run {'missing' if r6 is None else 'incomplete (n=%d)' % r6['n']}: unknown")
            unknown[f].append(W)
            if r6 is not None and r6["n"] >= 20:
                q, qe = ratio(r4, r6)
                print(f"   (information only, incomplete) ratio {q:.3f}({qe:.3f}); L6 E3w {r6['E3w']:.4f}")
            continue
        q, qe = ratio(r4, r6)
        isw = r6["E3w"] <= 0.1
        print(f"{f} W{W:g}: E3w L4 {r4['E3w']:.4f}({r4['E3we']:.4f}) L6 {r6['E3w']:.4f}({r6['E3we']:.4f}) window={isw}; "
              f"S10/L^2 L4 {r4['S']:.4f}({r4['Se']:.4f}) L6 {r6['S']:.4f}({r6['Se']:.4f}); ratio {q:.3f}({qe:.3f}); "
              f"(1-R)/sigma {(1 - q) / qe:.2f}" + (f"; free ratio {free[f][6] / free[f][4]:.3f}" if f in free else ""))
        if isw:
            win[f].append(W); R[(f, W)] = (q, qe)

def reading(win, R):
    f2ok = bool(win["f2"]) and all(R[("f2", W)][0] >= 0.85 for W in win["f2"])
    sens = any(R[("fG", W)][0] <= 0.75 and (1 - R[("fG", W)][0]) / R[("fG", W)][1] >= 2 for W in win["fG"]) and f2ok
    rob = bool(win["fG"]) and bool(win["f2"]) and all(R[(f, W)][0] >= 0.85 for f in ("fG", "f2") for W in win[f])
    return "FILTER-SENSITIVE" if sens else ("FILTER-ROBUST" if rob else "OPEN")

rd = reading(win, R)
# unknown runs: the reading stands only if it holds for every possible value of the unknown runs (PREREG 7)
nunk = sum(len(v) for v in unknown.values())
if nunk:
    import itertools
    outs = set()
    cases = [("win", 0.5, 0.1), ("win", 1.0, 0.05), ("win", 0.8, 0.05), ("nowin", None, None)]
    keys = [(f, W) for f in unknown for W in unknown[f]]
    for combo in itertools.product(cases, repeat=len(keys)):
        w2 = {f: list(v) for f, v in win.items()}; R2 = dict(R)
        for (f, W), (t, q, qe) in zip(keys, combo):
            if t == "win":
                w2[f].append(W); R2[(f, W)] = (q, qe)
        outs.add(reading(w2, R2))
    print(f"\nunknown (incomplete/missing) points {keys}: possible readings {sorted(outs)}")
    if len(outs) > 1:
        rd = f"OPEN (budget: depends on {keys})"
f2same = None
print(f"\nwindows: fG {win['fG']}, f2 {win['f2']}")
for W in win["fG"]:
    if ("f2", W) in R:
        print(f"same-W comparison at W = {W:g}: fG {R[('fG', W)][0]:.3f}, f2 {R[('f2', W)][0]:.3f} (f2 >= 0.85: {R[('f2', W)][0] >= 0.85})")
print(f"READING (mechanical, PREREG section 7): {rd}")

print("\n### SUPPLEMENTARY (PREREG follow-ups B, C): W = 8, outside the fixed W set; cannot change the fixed reading")
for f in ("fG", "f2"):
    r4, r6 = res.get((f, 4, 8.0)), res.get((f, 6, 8.0))
    if r4 is None or r6 is None:
        print(f"{f} W8: missing"); continue
    q, qe = ratio(r4, r6)
    print(f"{f} W8: n {r4['n']}/{r6['n']}; E3w L4 {r4['E3w']:.4f}({r4['E3we']:.4f}) L6 {r6['E3w']:.4f}({r6['E3we']:.4f}) "
          f"window={r4['E3w'] <= 0.1 and r6['E3w'] <= 0.1}; S10/L^2 L4 {r4['S']:.4f}({r4['Se']:.4f}) L6 {r6['S']:.4f}({r6['Se']:.4f}); "
          f"ratio {q:.3f}({qe:.3f}); (1-R)/sigma {(1 - q) / qe:.2f}")
