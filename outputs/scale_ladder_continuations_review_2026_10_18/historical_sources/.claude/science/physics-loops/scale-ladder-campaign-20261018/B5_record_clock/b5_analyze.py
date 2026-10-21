"""B5: fit tolerance scalings from scan_*.json and test predictions P1-P7.
Slopes are least-squares exponents of log(tolerance) against log(variable).
Scan E (fixed m_gp metric + first-crossing fallback) supersedes A/B for the
SB a_lit and all GC entries."""
import json, math
import numpy as np

def load(w):
    try:
        return json.load(open(f"scan_{w}.json"))
    except FileNotFoundError:
        return []

A, B, C, D, Ee = (load(w) for w in "ABCDE")
def key(r): return (r["cfg"]["dev"], r["cfg"]["lam"], round(r["cfg"]["T"]), r["cfg"]["M"], r["cfg"].get("n"), r["cls"])
sup = {key(r): r for r in Ee}

def tol(r, m):
    rr = sup.get(key(r), r) if (r["cls"] == "GC" or (r["cls"] == "SB" and m == "a_lit")) else r
    return rr["res"][m]["tol"], rr["res"][m]["ok"]

def series(rows, cls, var):
    pts = [(var(r), r) for r in rows if r["cls"] == cls]
    return sorted(pts, key=lambda p: p[0])

def slope(pts, m):
    xs, ys, oks = [], [], []
    for x, r in pts:
        t, ok = tol(r, m)
        xs.append(x); ys.append(t); oks.append(ok)
    if any(math.isinf(y) for y in ys):
        return float("inf"), ys, all(oks)
    if any(not np.isfinite(y) or y <= 0 for y in ys):
        return float("nan"), ys, False
    return float(np.polyfit(np.log(xs), np.log(ys), 1)[0]), ys, all(oks)

MET = ["a_lit", "a_act", "b_pop", "c_gp", "c_rel"]
table = {}
for name, rows, var in [("vs lam (T=25/lam, M~4.8T)", A, lambda r: r["cfg"]["lam"]),
                        ("vs T (lam=0.04, M~4.8T)", B + [r for r in A if r["cfg"]["lam"] == 0.04], lambda r: r["cfg"]["T"]),
                        ("vs M (lam=0.04, T=625)", C, lambda r: r["cfg"]["M"]),
                        ("D2 vs 2n+1 (T=25/lam)", [r for r in D if round(r["cfg"]["T"] * r["cfg"]["lam"]) == 25], lambda r: 2 * r["cfg"]["n"] + 1),
                        ("D2 vs T (n=3)", [r for r in D if r["cfg"]["n"] == 3], lambda r: r["cfg"]["T"])]:
    print(f"\n== tolerance exponents {name}")
    classes = sorted({r["cls"] for r in rows})
    for cls in classes:
        pts = series(rows, cls, var)
        if name.startswith("vs T"):   # de-duplicate the shared lam=0.04,T=625 point
            seen, uniq = set(), []
            for x, r in pts:
                if x not in seen: seen.add(x); uniq.append((x, r))
            pts = uniq
        cells = []
        for m in MET:
            s, ys, ok = slope(pts, m)
            table[(name, cls, m)] = (s, ys, ok)
            cells.append(f"{m}:{s:+.2f}" if np.isfinite(s) else f"{m}:{s}")
        print(f"  {cls:3s} n_pts={len(pts)}  " + "  ".join(cells))
        for m in MET:
            print(f"        {m:6s} tol = " + ", ".join(f"{y:.3g}" for y in table[(name, cls, m)][1]))

def g(name, cls, m): return table.get((name, cls, m), (float("nan"), [], False))
def chk(label, cond):
    print(f"{'PASS' if cond else 'FAIL'}  {label}")

print("\n== prediction checks (declared in b5_tolerance_scan.py docstring before first run)")
LA, TT, NN, NT = "vs lam (T=25/lam, M~4.8T)", "vs T (lam=0.04, M~4.8T)", "D2 vs 2n+1 (T=25/lam)", "D2 vs T (n=3)"
chk("P1 SB tolerance flat in lam and T for a_act,b_pop,c_gp,c_rel (|slope|<0.15)",
    all(abs(g(s, "SB", m)[0]) < 0.15 for s in (LA, TT) for m in ("a_act", "b_pop", "c_gp", "c_rel")))
chk("P2 SB a_lit ~ 1/T at fixed lam (slope in [-1.2,-0.8])", -1.2 <= g(TT, "SB", "a_lit")[0] <= -0.8)
chk("P3a SO a_act ~ lam (slope vs lam in [0.85,1.15])", 0.85 <= g(LA, "SO", "a_act")[0] <= 1.15)
chk("P3b SO a_act flat in T at fixed lam (|slope|<0.15)", abs(g(TT, "SO", "a_act")[0]) < 0.15)
chk("P4 SO b_pop tolerance > 3x a_act tolerance at every point",
    all(b > 3 * a for b, a in zip(g(LA, "SO", "b_pop")[1], g(LA, "SO", "a_act")[1])))
chk("P5a lead-bond a_act tolerance falls with T at fixed lam (slope<-0.2)", g(TT, "LB", "a_act")[0] < -0.2)
chk("P5b lead-onsite a_act tolerance falls with T at fixed lam (slope<-0.2)", g(TT, "LO", "a_act")[0] < -0.2)
chk("P5c lead errors exactly common-mode for co-transported reference (c_rel inf)",
    all(math.isinf(y) for c in ("LB", "LO") for y in g(LA, c, "c_rel")[1]))
chk("P6a GC a_lit ~ 1/T (slope vs T in [-1.1,-0.9])", -1.1 <= g(TT, "GC", "a_lit")[0] <= -0.9)
chk("P6b GC invisible to b_pop, c_gp, c_rel", all(math.isinf(y) for m in ("b_pop", "c_gp", "c_rel") for y in g(LA, "GC", m)[1]))
chk("P7a D2 mediator-bond a_act ~ 1/(2n+1) (slope in [-1.3,-0.7])", -1.3 <= g(NN, "MB", "a_act")[0] <= -0.7)
chk("P7b D2 mediator-bond a_act flat in T (|slope|<0.15)", abs(g(NT, "MB", "a_act")[0]) < 0.15)
allok = all(r["res"][m]["ok"] for rows in (A, B, C, D, Ee) for r in rows for m in MET
            if not (r["cls"] == "GC" or (r["cls"] == "SB" and m == "a_lit")) or rows is Ee)
chk("V  every reported tolerance re-verified at its own x* (metric in [0.8e,1.25e] or bracketed)", allok)
