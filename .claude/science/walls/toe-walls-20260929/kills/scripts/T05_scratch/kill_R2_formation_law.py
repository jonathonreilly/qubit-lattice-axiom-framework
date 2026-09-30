"""Kill test for R2: is the Born-form parent claim valid for the FORMATION law (the object R1 calibrates to),
or only for the STATIC law (what rk_parent.py tested)?

Windows: cycle4 (one plaquette) and cube8 (open 2x2x2). Rule: block-01 product rule (p,q,r)=(3,1,2), records-only reading.
mu   = static law (full conditionals = rule with all neighbours recorded)
mu_s = formation law along a fixed order sigma: prod_k r(v_k | v on earlier neighbours)
A_x^NN = projector onto sqrt of the rule's conditional given ALL nearest neighbours (the RK operator of rk_parent.py)
"""
import itertools, numpy as np
P_, Q_, R_ = 3.0, 1.0, 2.0
PHI = np.zeros((6, 6))
for s in range(6):
    for t in range(6):
        PHI[s, t] = P_ if s == t else (Q_ if s // 2 == t // 2 else R_)

def build(nsite, edges):
    nbrs = [[] for _ in range(nsite)]
    for i, j in edges:
        nbrs[i].append(j); nbrs[j].append(i)
    return nbrs

def rule(s_axis_nbrs_vals):  # vals: list of neighbour values recorded -> prob vector over 6
    w = np.ones(6)
    for v in s_axis_nbrs_vals:
        w = w * PHI[:, v]
    return w / w.sum()

def joint_static(n, edges):
    mu = np.ones((6,) * n)
    for i, j in edges:
        sh = [1] * n; sh[i] = 6; sh[j] = 6
        T = PHI if i < j else PHI.T
        mu = mu * T.reshape(sh)
    return mu / mu.sum()

def joint_formation(n, nbrs, order):
    # mu_sigma(v) = prod_k r(v_{x_k} | recorded nbrs)
    mu = np.ones((6,) * n)
    pos = {x: k for k, x in enumerate(order)}
    for x in range(n):
        earlier = [y for y in nbrs[x] if pos[y] < pos[x]]
        # tensor over axes [x] + earlier
        T = np.ones([6] + [6] * len(earlier))
        for idx in itertools.product(range(6), repeat=len(earlier)):
            T[(slice(None),) + idx] = rule(list(idx))
        # broadcast into full joint
        axes = [x] + earlier
        sh = [1] * n
        for a in axes: sh[a] = 6
        # permute T's axes to sorted order of axes
        perm = np.argsort(axes)
        Tt = np.transpose(T, perm)
        shp = [1] * n
        for a in sorted(axes): shp[a] = 6
        mu = mu * Tt.reshape(shp)
    return mu / mu.sum()

def cond_given_rest(mu, x):
    """P(v_x | all others), array shape mu.shape with axis x conditional"""
    return mu / mu.sum(axis=x, keepdims=True)

def markov_defect(mu, nbrs, n):
    """max over sites x and configs of | P(v_x | rest) - P(v_x | NN of x) |  (NN-Markov property defect)"""
    worst = 0.0
    for x in range(n):
        full = cond_given_rest(mu, x)
        others = [a for a in range(n) if a != x and a not in nbrs[x]]
        # marginalise non-neighbours out of the joint: P(v_x, v_NN)
        m = mu.sum(axis=tuple(others), keepdims=True) if others else mu
        nn_cond = m / m.sum(axis=x, keepdims=True)
        worst = max(worst, np.abs(full - nn_cond).max())
    return worst

def rk_residual(mu, nbrs, n):
    """RK operator with the RULE's NN conditional: A_x psi vs psi, psi = sqrt(mu)"""
    psi = np.sqrt(mu)
    letters = "abcdefgh"[:n]
    worst = 0.0
    for x in range(n):
        nb = nbrs[x]
        w = np.ones([6] * (1 + len(nb)))
        for k in range(len(nb)):
            sh = [1] * (1 + len(nb)); sh[0] = 6; sh[1 + k] = 6
            w = w * PHI.reshape(sh)
        w = w / w.sum(axis=0, keepdims=True)
        sq = np.sqrt(w)
        sub = letters[x] + "".join(letters[y] for y in nb)
        rest = letters.replace(letters[x], "")
        c = np.einsum(f"{letters},{sub}->{rest}", psi, sq)
        A = np.einsum(f"{sub},{rest}->{letters}", sq, c)
        worst = max(worst, np.abs(A - psi).max() / psi.max())
    return worst

def report(tag, n, edges, orders):
    nbrs = build(n, edges)
    mu = joint_static(n, edges)
    print(f"[{tag}] static law: NN-Markov defect {markov_defect(mu, nbrs, n):.2e}; RK residual (rule's NN conditionals) {rk_residual(mu, nbrs, n):.2e}")
    mix = np.zeros_like(mu)
    for od in orders:
        m = joint_formation(n, nbrs, od)
        mix += m
        print(f"   formation order {od}: TV(formation, static) = {0.5*np.abs(m-mu).sum():.3e}; NN-Markov defect {markov_defect(m, nbrs, n):.3e}; RK residual (rule's NN conditionals) {rk_residual(m, nbrs, n):.3e}")
    mix /= len(orders)
    print(f"   uniform mixture over these {len(orders)} orders: TV to static = {0.5*np.abs(mix-mu).sum():.3e}; NN-Markov defect {markov_defect(mix, nbrs, n):.3e}; RK residual {rk_residual(mix, nbrs, n):.3e}")

# cycle4 = one plaquette
report("cycle4", 4, [(0,1),(1,2),(2,3),(3,0)], [(0,1,2,3),(0,1,3,2),(0,2,1,3)])
# all 24 orders mixture on cycle4
report("cycle4-all24", 4, [(0,1),(1,2),(2,3),(3,0)], list(itertools.permutations(range(4))))
# path (forest) control: theorem B says formation = static when <=1 recorded neighbour
report("path4-control(forest)", 4, [(0,1),(1,2),(2,3)], [(0,1,2,3),(1,0,2,3),(1,2,0,3)])
# cube8: two fixed orders
cube_sites = list(itertools.product((0,1), repeat=3))
sid = {c: i for i, c in enumerate(cube_sites)}
cube_edges = sorted({tuple(sorted((sid[c], sid[tuple(c[k]^(1 if k==j else 0) for k in range(3))]))) for c in cube_sites for j in range(3)})
report("cube8", 8, cube_edges, [tuple(range(8)), (0,3,5,6,1,2,4,7)])
