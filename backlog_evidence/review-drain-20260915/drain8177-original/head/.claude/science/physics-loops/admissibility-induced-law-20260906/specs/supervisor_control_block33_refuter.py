"""Refuting pass, block 33 — disjoint machinery.
(1) The rooted values at the tight roots of Z_A, Z_B and at their 1-predecessors recomputed by the INTEGER PROGRAM with a level cap
    (scipy milp, floating point) against the runner's exact single-seed program with a level cap.
(2) The seed lemma's construction re-checked with a separate tree verifier on tiny realizations: for every processed z with a seed
    1-predecessor s and another 1-predecessor w, the tree {z, w, s} + an optimal rooted tree of a predecessor p of w (from the integer
    program) with arrows z->w, w->p and the fork s-w is verified as a member of the family and its cost equals v(p) - 1.
(3) The restricted count's fixed point at (2921,1,2), c = 2, t = 121/1000 iterated in floating point by the eight-variable kind-typed
    recursion and by the three-variable recursion, compared to the exact certificate's R-bar (the certificate must dominate).
(4) The extension lemma probed adversarially: a climb maximizing v(z) - 1 - min_u v(u) over sites (must stay <= 0) for 120 s."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, sys.argv[1])
import numpy as np
from fractions import Fraction as Fr
from scipy.optimize import milp, LinearConstraint, Bounds
from supervisor_control_block33_mintree import MinTree, run_automaton, level, preds
import importlib
m = importlib.import_module("admissibility_rule_six_axis_formation_threshold_rooted_inequality_reduces_the_unit_budget_to_the_tight_sibling_lemma_and_the_one_processed_child_count_2026_09_17")
import supervisor_control_block33_restricted_count as rc
from supervisor_control_block33_kind_certs import KEYS

def image(G, xP, xA, eS, yF, variant, root=False):
    """the eight-variable kind-typed map with the restriction (at most one processed child) applied at EVERY node kind, seeds included
    — the family of the note; kind_certs.image restricts processed and amplified nodes only."""
    Dsum = sum(G[("D", k)] for k in "PAS"); Fsum = sum(G[("F", k)] for k in "PAS")
    UP, UA = xP * G[("U", "P")], xA * G[("U", "A")]
    out = {}
    for e in "DUF" + ("R" if root else ""):
        nup = 2 if e == "D" else 3; nfork = 5 if e == "F" else 6
        for k in "PAS":
            if e == "U" and k == "S": continue
            own = 1 if k == "S" else (3 * (xP if k == "P" else xA) * Dsum if e != "U" else 1)
            up = (1 + UA) ** nup + nup * UP * (1 + UA) ** (nup - 1)
            fk = (1 + yF * Fsum) ** nfork
            out[(e, k)] = (eS if k == "S" else 1) * own * up * fk
    return out

def rooted_ilp(eta, z, c=1.0):
    mt = MinTree(eta, z)
    cost = np.zeros(mt.nvar)
    for w in mt.V: cost[mt.idx[w]] = {"proc": 1.0, "amp": -c, "seed": -3.0}[mt.kind[w]]
    ub = mt.bounds.ub.copy(); lb = mt.bounds.lb.copy()
    for w in mt.V:
        if level(w) > level(z): ub[mt.idx[w]] = 0
    res = milp(cost, constraints=[LinearConstraint(mt.A, mt.lo, mt.hi)], integrality=mt.integrality, bounds=Bounds(lb, ub), options={"disp": False, "time_limit": 60})
    if res.status != 0: return None, None
    xv = res.x
    nodes = [w for w in mt.V if xv[mt.idx[w]] > 0.5]
    arrows = [(a, b) for k, (a, b) in enumerate(mt.arrows) if xv[mt.off_a + k] > 0.5]
    forks = [(a, b) for k, (a, b) in enumerate(mt.forks) if xv[mt.off_f + k] > 0.5]
    E = sum(1 for w in nodes if mt.kind[w] == "proc"); A = sum(1 for w in nodes if mt.kind[w] == "amp"); Sn = sum(1 for w in nodes if mt.kind[w] == "seed")
    return E - 3 * (Sn - 1) - A, (nodes, arrows, forks)

print("== (1): rooted values at the tight roots, integer program vs the exact program")
for name, Z in (("Z_A", m.Z_A), ("Z_B", m.Z_B)):
    root, (A_, B_, L_), marks = Z
    sites = [(a, b, c) for a in range(A_) for b in range(B_) for c in range(L_)]
    eta = run_automaton(sites, {z: 1 for z in marks}); ones, npred, kind = m.kinds(eta)
    vi = rooted_ilp(eta, root)[0]; ve = m.single_seed_min_capped(eta, root, Fr(1), level(root))[0]
    pi = [rooted_ilp(eta, u)[0] for u in npred[root]]; pe = [m.single_seed_min_capped(eta, u, Fr(1), level(u))[0] for u in npred[root]]
    print(f"{name}: root {root}: integer program {vi} / exact {ve}; predecessors: integer program {pi} / exact {[str(x) for x in pe]}")
print("== (2): the seed lemma's construction verified by the runner's tree verifier on tiny realizations")
random.seed(77); sites = [(a, b, c) for a in range(3) for b in range(3) for c in range(5)]
checked = bad = 0; t0 = time.time()
while checked < 25 and time.time() - t0 < 240:
    zeta = {z: 1 for z in random.sample(sites, random.randint(1, 6))}
    eta = run_automaton(sites, zeta); ones, npred, kind = m.kinds(eta)
    for z in ones:
        if kind[z] != "proc": continue
        seeds = [u for u in npred[z] if kind[u] == "seed"]; others = [u for u in npred[z] if kind[u] != "seed"]
        if not seeds or not others: continue
        s, w = seeds[0], others[0]
        p = npred[w][0]
        vp, tree = rooted_ilp(eta, p)
        if tree is None: continue
        nodes, arrows, forks = tree
        nodes2 = set(nodes) | {z, w, s}; arrows2 = list(arrows) + [(z, w), (w, p)]; forks2 = list(forks) + [(s, w)]
        ok = m.verify_tree(eta, z, nodes2, arrows2, forks2)
        E, A, Sn = m.tree_counts(eta, nodes2)
        cost = E - 3 * (Sn - 1) - A
        expected = vp + (1 if kind[w] == "proc" else -1) + 1 - 3
        checked += 1
        if not ok or cost != expected: bad += 1
print(f"seed-lemma constructions verified: {checked}, failures {bad}")
print("== (3): the restricted count at (2921,1,2), c=2, t=121/1000: eight-variable and three-variable iterations vs the exact certificate")
d1, d2, d3 = rc.devs(2921, 1, 2); e1, e2 = float(d1), float(max(d2, d3)); t = 0.121
xP, xA, eS, yF = t, e2 / t**2, e1, 1 / t**3
G = {k: 0.0 for k in KEYS}
for it in range(60000):
    Gn = image(G, xP, xA, eS, yF, "R1")
    if max(abs(Gn[k] - G[k]) / max(1e-300, abs(Gn[k])) for k in KEYS) < 1e-13: G = Gn; break
    G = Gn
imr = image(G, xP, xA, eS, yF, "R1", root=True); R8 = (imr[("R","P")] + imr[("R","A")] + imr[("R","S")]) / e1
D = U = Fv = 1.0
for it in range(60000):
    D2, U2, F2 = m.rhs(xP, xA, e1 / t**3, D, U, Fv, True)
    if abs(D2 - D) + abs(U2 - U) + abs(F2 - Fv) < 1e-14: D, U, Fv = D2, U2, F2; break
    D, U, Fv = D2, U2, F2
R3 = m.upf(3, xP, xA, U, True) * (1 + 3 * (xP + xA) * D) * (1 + (e1 / t**3) * Fv) ** 6
Db, Ub, Fb = Fr(38819515651721, 125000000000), Fr(2614495936247, 1000000000000), Fr(411275330287659, 1000000000000)
Rc = float(m.upf(3, Fr(121, 1000), max(d2, d3) / Fr(121, 1000)**2, Ub, True) * (1 + 3 * (Fr(121, 1000) + max(d2, d3) / Fr(121, 1000)**2) * Db) * (1 + d1 / Fr(121, 1000)**3 * Fb) ** 6)
print(f"eight-variable R/eps1 = {R8:.4f}; three-variable R = {R3:.4f}; exact certificate R-bar = {Rc:.4f} (must be >= the fixed points): {Rc >= R8 - 1e-6 and Rc >= R3 - 1e-6}")
print("== (4): adversarial climb on v(z) - 1 - min_u v(u) (120 s; must stay <= 0)")
random.seed(4343); sites = [(a, b, c) for a in range(4) for b in range(4) for c in range(6)]
def score(zeta):
    eta = run_automaton(sites, zeta); ones, npred, kind = m.kinds(eta)
    if len(ones) < 5 or len(ones) > 45: return -99
    vc = {}
    def v(z):
        if z not in vc: vc[z] = rooted_ilp(eta, z)[0]
        return vc[z]
    best = -99
    for z in ones:
        if kind[z] == "seed" or level(z) < 2: continue
        best = max(best, v(z) - 1 - min(v(u) for u in npred[z]))
    return best
t0 = time.time(); overall = -99
while time.time() - t0 < 120:
    zeta = {z: 1 for z in random.sample(sites, random.randint(2, 7))}; cur = score(zeta)
    for it in range(150):
        if time.time() - t0 > 120: break
        z = random.choice(sites); new = dict(zeta)
        if z in new: del new[z]
        else: new[z] = 1
        if not new: continue
        sc = score(new)
        if sc >= cur: zeta, cur = new, sc; overall = max(overall, cur)
print("largest v(z) - 1 - min_u v(u) found:", overall)
print("== verdict:", "consistent — nothing refuted" if overall <= 0 and bad == 0 else "INCONSISTENCY FOUND")
