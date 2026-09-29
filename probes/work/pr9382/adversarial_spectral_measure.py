"""PR 9382 attack-e: SAMPLED EVIDENCE.  The note reads S/ceiling = 0.963 +- 0.034 and three weighted frequencies within 8 % as 'at k = pi/4 on 8^3 the transverse spectral weight is concentrated near omega ~ s;
a second mode carrying a small weight is not excluded'.  The estimates are three sampled numbers (S = 0.408 +- 0.014, chi = 1.064 +- 0.008, u = 0.2888).  Instead of more samples, an adversarial construction:

  find, by linear programming over a grid of frequencies omega_j in [0.05, 6], the nonnegative measures nu with EXACTLY the three moments m0 = S, m_-1 = chi/2, m1 = 2 u s^2 (and with the moments moved by up to
  +-1 and +-2 sigma of S and chi) that put the MOST weight far from s: below s/2, below 0.75 s, above 1.5 s, and that have the LOWEST atom (omega_min proxy) as small as possible with weight at least 1 % / 5 %;
  compare with the moment-certified Markov quantile bounds (weight below (1-eta) w_check <= eps (1-eta)/eta^2, above (1+eta) w_check <= eps (1+eta)/eta^2, eps = m1 m_-1/m0^2 - 1);
  and test the exactly solvable 2^3 case where the answer is known: the LP maximum against the true spectral weights.
"""
import sys
import numpy as np
from scipy.optimize import linprog

PASS = FAIL = 0
HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)

s = 2 * np.sin(np.pi / 8); u = 0.2888
S0, chi0 = (0.4058 + 0.4110) / 2, 1.064
grid = np.concatenate([np.linspace(0.05, 2.0, 400), np.linspace(2.0, 6.0, 120)[1:]])
def moments(S, chi): return S, chi / 2, 2 * u * s * s
def lp(m0, mm1, m1, objective, w_lo=None, atom_below=None, atom_weight=0.0):
    """maximise sum_j c_j w_j subject to the three moment equalities and w >= 0 (optionally: weight at least atom_weight on omega <= atom_below)"""
    A = np.vstack([np.ones_like(grid), 1 / grid, grid]); b = np.array([m0, mm1, m1])
    c = -objective
    Aub = None; bub = None
    if atom_below is not None:
        Aub = -(grid <= atom_below).astype(float)[None, :]; bub = np.array([-atom_weight])
    r = linprog(c, A_eq=A, b_eq=b, A_ub=Aub, b_ub=bub, bounds=(0, None), method="highs")
    return (r.x if r.status == 0 else None)
def markov(m0, mm1, m1, eta, side):
    eps = m1 * mm1 / m0 ** 2 - 1; wc = m0 / mm1
    return eps * (1 - eta) / eta ** 2 if side == "below" else eps * (1 + eta) / eta ** 2
res = {}
print("== 8^3, k = pi/4 (the note's inputs) ==")
print("   scenario          eps = m1 m_-1/m0^2 - 1   max weight fraction below s/2 | below 0.75 s | above 1.5 s   (Markov: below (1-eta) w_check, above (1+eta) w_check)")
for nm, (S, chi) in {"central": (S0, chi0), "S +1 sigma": (S0 + 0.014, chi0), "S -1 sigma": (S0 - 0.014, chi0), "chi +1 sigma": (S0, chi0 + 0.008), "chi -1 sigma": (S0, chi0 - 0.008), "S +2 sigma, chi -2 sigma": (S0 + 0.028, chi0 - 0.016)}.items():
    m0, mm1, m1 = moments(S, chi); eps = m1 * mm1 / m0 ** 2 - 1; wc = m0 / mm1
    row = []
    for thr, kind in ((0.5 * s, "below"), (0.75 * s, "below"), (1.5 * s, "above")):
        obj = (grid <= thr).astype(float) if kind == "below" else (grid >= thr).astype(float)
        w = lp(m0, mm1, m1, obj)
        row.append(float((obj * w).sum() / m0) if w is not None else float("nan"))
    res[nm] = (eps, row, wc)
    print(f"   {nm:24s}  {eps:8.4f}   {100*row[0]:6.2f}% | {100*row[1]:6.2f}% | {100*row[2]:6.2f}%   (w_check {wc:.4f} = {wc/s:.3f} s)")
eps, row, wc = res["central"]
# Markov bounds at the same thresholds expressed as fractions of the weight
def thr_eta(thr): return 1 - thr / wc
mk = [markov(*moments(S0, chi0), 1 - 0.5 * s / wc, "below"), markov(*moments(S0, chi0), 1 - 0.75 * s / wc, "below"), markov(*moments(S0, chi0), 1.5 * s / wc - 1, "above")]
print(f"   central Markov quantile bounds at the same thresholds (fraction of the weight): below s/2 <= {100*mk[0]:.1f}%, below 0.75 s <= {100*mk[1]:.1f}%, above 1.5 s <= {100*mk[2]:.1f}%")
check("the LP maxima never exceed the moment-certified Markov quantile bounds (consistency of the construction; the certified bound is a valid upper bound on what any measure can do)", all(r <= m + 1e-9 for r, m in zip(row, mk)), f"{[round(100*r,2) for r in row]} <= {[round(100*m,2) for m in mk]} %")
lowatom = {}
for thr, wt in ((0.3, 0.05), (0.15, 0.01), (0.15, 0.05), (0.08, 0.01)):
    m0, mm1, m1 = moments(S0, chi0)
    w = lp(m0, mm1, m1, np.zeros_like(grid), atom_below=thr, atom_weight=wt * m0)
    lowatom[(thr, wt)] = w is not None
print("   measures with EXACTLY the three moments and a weight fraction at omega <= thr:", {k_: ("exists" if v else "impossible") for k_, v in lowatom.items()}, "(thr in units of the frequency scale; s = %.4f)" % s)
check("the note's caveat is quantified: measures with exactly the note's three moments put a sizeable weight far from s (>= 5 % below 0.75 s) and can carry a 5 % atom at omega <= 0.3, so 'concentrated near s' is not implied at the 10 % level by the three moments alone", row[1] > 0.05 and lowatom[(0.3, 0.05)], f"max weight below 0.75 s: {100*row[1]:.1f} %, 5 % atom below 0.3: {lowatom[(0.3, 0.05)]}")
# what the ratio ~ 1 does imply: the weight-below-s/2 bound tightens with the sigma range
print(f"   across the sigma range the maximal weight below s/2 spans {100*min(r[1][0] for r in res.values()):.2f} .. {100*max(r[1][0] for r in res.values()):.2f} % and below 0.75 s spans {100*min(r[1][1] for r in res.values()):.2f} .. {100*max(r[1][1] for r in res.values()):.2f} %")

# exact 2^3 for reference: the true spectral weights (from the note's parent numbers reproduced in the sibling attacks): use the known chain 2.517 (lowest level, 24.9 % of m0) etc.
# the 2^3 chain values (own exact diagonalisation in the sibling scripts): m0 = 1.012148, m_-1 = 0.364691, m1 = 3.008907; lowest coupled level 2.5173 carrying 0.249 of m0
m0, mm1, m1 = 1.012148056, 0.36469063, 3.008906971
grid2 = grid * 4.0 / s / 2                               # rescale the grid to the 2^3 frequency scale (s = 2)
def lp2(objective):
    A = np.vstack([np.ones_like(grid2), 1 / grid2, grid2]); b = np.array([m0, mm1, m1]); r = linprog(-objective, A_eq=A, b_eq=b, bounds=(0, None), method="highs"); return r.x
w2 = lp2((grid2 <= 0.9 * 2.5173).astype(float))
print(f"   exact 2^3 (k = pi, s = 2): the three moments allow up to {100*float((grid2 <= 0.9*2.5173) @ w2)/m0:.1f}% of the weight below 0.9 x the lowest coupled level (2.5173); the true weight below 2.5 is 0 by construction")
check("on the exactly solvable 2^3 the same three-moment LP allows weight BELOW the true lowest level, so the moments alone cannot certify a gap or a concentration even when the exact answer is known", float((grid2 <= 0.9 * 2.5173) @ w2) / m0 > 0.001, f"{100*float((grid2 <= 0.9*2.5173) @ w2)/m0:.2f} %")

print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-e sampled evidence on PR 9382: with the note's three moments (S = 0.4084, chi = 1.064, m1 = 2 u s^2; eps = {res['central'][0]:.3f}) an LP over measures with exactly those moments puts up to {100*res['central'][1][0]:.1f}% of the weight below s/2, {100*res['central'][1][1]:.1f}% below 0.75 s and {100*res['central'][1][2]:.1f}% above 1.5 s (Markov-certified caps {100*mk[0]:.1f}/{100*mk[1]:.1f}/{100*mk[2]:.1f}%), and admits a 5% atom at omega <= 0.3: the note's 'concentrated near s' is an estimated reading, as it says, not implied by the moments at the 10% level; PASS={PASS} FAIL={FAIL}; no HIT (the note hedges this)")
sys.exit(1 if FAIL else 0)
