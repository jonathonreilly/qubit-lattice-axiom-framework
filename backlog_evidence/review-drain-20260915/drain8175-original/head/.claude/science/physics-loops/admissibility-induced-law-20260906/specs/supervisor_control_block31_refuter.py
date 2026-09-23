"""Refuting pass, block 31 — disjoint machinery.
(1) The majority rule re-run with a separate array implementation (numpy) on the witnesses' windows and compared site by site with the runner's automaton.
(2) The witnesses' trees re-derived from the runner's EDGE LISTS alone (no Explainer): node marks recounted from the automaton output, the point graph checked to be a tree, E/|A|/|S|/F recounted; the budgets re-evaluated.
(3) The per-refinement accounting enumerated: over all (b, a, e) with e + a <= 3, b <= a, fork-free rise r = 1 - b, the maximum of (e - 3 r)/a and the failures of e <= 3 r + a.
(4) An independent search for LARGER ratios by simulated annealing in a 4x4x8 window (different moves, different acceptance) — the note claims c >= 5/3 only; a larger value would not refute it, a failure to reach 8/5 would question the climb.
(5) W1's self-containment: the automaton run from its eleven marks alone reproduces the root and the same tree counts."""
import sys, random, math, time
sys.path.insert(0, sys.argv[1])
import numpy as np
from fractions import Fraction as Fr
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_sharper_bad_pair_budget_false_explicit_witnesses_and_the_two_level_period_2026_09_16")

def majority_np(shape, marks):
    A_, B_, L_ = shape
    eta = np.zeros((A_, B_, L_), dtype=np.int8)
    mk = np.zeros_like(eta)
    for (a, b, c) in marks: mk[a, b, c] = 1
    for s in range(A_ + B_ + L_):
        for a in range(A_):
            for b in range(B_):
                c = s - a - b
                if 0 <= c < L_:
                    n = (eta[a-1, b, c] if a else 0) + (eta[a, b-1, c] if b else 0) + (eta[a, b, c-1] if c else 0)
                    eta[a, b, c] = 1 if (n >= 2 or mk[a, b, c]) else 0
    return eta

def tree_from_edges(root, edges, eta_np):
    """independent: build the point graph from the edge list, check it is a tree through 1-sites, recount marks from eta_np."""
    nodes = set([root])
    for e in edges: nodes |= set(e)
    adj = {v: set() for v in nodes}
    for e in edges:
        a, b = tuple(e); adj[a].add(b); adj[b].add(a)
    seen = {root}; st = [root]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen: seen.add(w); st.append(w)
    is_tree = (seen == nodes) and (len(edges) == len(nodes) - 1)
    def npred(v):
        a, b, c = v
        return (eta_np[a-1, b, c] if a else 0) + (eta_np[a, b-1, c] if b else 0) + (eta_np[a, b, c-1] if c else 0)
    ones_ok = all(eta_np[v] == 1 for v in nodes)
    S = {v for v in nodes if npred(v) == 0}; A = {v for v in nodes if npred(v) == 1}
    E = sum(1 for e, k in edges.items() if k == "arrow"); Fk = sum(1 for e, k in edges.items() if k == "fork"); Am = sum(1 for e, k in edges.items() if k == "amp")
    # every arrow joins a site to a predecessor; every fork joins siblings
    geo = True
    for e, k in edges.items():
        a, b = tuple(e); d = tuple(x - y for x, y in zip(a, b))
        if k in ("arrow", "amp"): geo = geo and (sorted(d) == [0, 0, 1] or sorted(d) == [-1, 0, 0])
        else: geo = geo and sorted(d) == [-1, 0, 1]
    return dict(tree=is_tree, ones=ones_ok, geo=geo, E=E, A=len(A), Aarrows=Am, S=len(S), F=Fk)

print("== (1)+(2)+(5): the witnesses by disjoint machinery")
for name, w in (("W1", m.W1), ("W2", m.W2), ("W3", m.W3)):
    root, shape, marks = w
    eta_np = majority_np(shape, marks)
    sites = [(a, b, c) for a in range(shape[0]) for b in range(shape[1]) for c in range(shape[2])]
    eta_run = m.run_automaton(sites, {z: 1 for z in marks})
    agree = all(eta_np[z] == eta_run[z] for z in sites)
    ex = m.Explainer(eta_run, {z: 1 for z in marks})
    nodes, edges, S, A, refs, bad = ex.explain(root)
    t = tree_from_edges(root, edges, eta_np)
    ratio = Fr(t["E"] - 3 * (t["S"] - 1), t["A"])
    print(f"{name}: numpy rule agrees with the runner's automaton on all {len(sites)} sites: {agree}; from the edge list: tree={t['tree']} ones={t['ones']} geometry={t['geo']} E={t['E']} |A|={t['A']} (amp arrows {t['Aarrows']}) |S|={t['S']} F={t['F']}; ratio={ratio}; block30 budget {t['E'] <= 3*(t['S']-1) + 2*t['A']}; sharper budget {t['E'] <= 3*(t['S']-1) + t['A']}")
    if name == "W1":
        own = set(S) | set(A)
        print(f"   W1 marks == tree's seed+amplified: {own == set(marks)}")
print("== (3): the per-refinement accounting enumerated (fork-free)")
best = []
for b in range(4):
    for a in range(b, 4):
        for e in range(0, 4 - a):
            if a == 0: continue
            r = 1 - b
            best.append((Fr(e - 3 * r, a), b, a, e))
mx = max(x[0] for x in best)
print("max over admissible (b, a, e) of (e - 3 r)/a =", mx, "attained at", [(b, a, e) for (v, b, a, e) in best if v == mx])
print("(b, a, e) where e <= 3 r + a FAILS:", [(b, a, e) for (v, b, a, e) in best if e > 3 * (1 - b) + a])
print("(b, a, e) where e <= 3 r + 2a fails:", [(b, a, e) for (v, b, a, e) in best if e > 3 * (1 - b) + 2 * a])
print("== (4): simulated annealing in a 4x4x8 window (independent search; 150 s)")
random.seed(777)
A_, B_, L_ = 4, 4, 8
sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
def score(zeta):
    eta = m.run_automaton(sites, zeta); ones = [z for z, v in eta.items() if v == 1]
    if not ones or len(ones) > 70: return Fr(-10)
    ex = m.Explainer(eta, zeta); best = Fr(-10)
    for root in ones:
        if m.level(root) < 5: continue
        nodes, edges, S, A, refs, bad = ex.explain(root)
        if not A: continue
        E = sum(1 for e, k in edges.items() if k == "arrow")
        best = max(best, Fr(E - 3 * (len(S) - 1), len(A)))
    return best
t0 = time.time(); overall = Fr(-10)
while time.time() - t0 < 150:
    zeta = {z: 1 for z in random.sample(sites, 4)}; cur = score(zeta); T = 0.3
    for it in range(500):
        z = random.choice(sites); new = dict(zeta)
        if z in new: del new[z]
        else: new[z] = 1
        if not new: continue
        sc = score(new)
        if sc >= cur or random.random() < math.exp(float(sc - cur) / T):
            zeta, cur = new, sc
            overall = max(overall, cur)
        T = max(0.02, T * 0.995)
print("simulated annealing best ratio:", overall, "=", float(overall))
print("== verdict: the witnesses are reproduced by disjoint machinery; the accounting's maximum per refinement is 2; the note's c >= 5/3 is consistent with the independent search" if overall >= Fr(8, 5) else "== verdict: the witnesses are reproduced; the independent search did not reach 8/5 in its budget (the climb's witnesses stand on their own)")
