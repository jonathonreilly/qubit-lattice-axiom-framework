#!/usr/bin/env python3
"""Independent finite gauge/conditional-Haar diagnostics; not SU(N) proof.

The 2x2 periodic Z2 model checks penalty interpolation. The separate two-loop
Z2 slice has four interior variables, an exterior variable, actual normalized
arithmetic-mean soft kernels, and a correlated hard insertion. All sums are
direct enumeration. No author code is imported.
"""
import cmath
import itertools as it
import json
import math
import time
from collections import defaultdict

start = time.time()
signs = (-1, 1)
checks, controls = {}, {}

# Actual periodic two-dimensional Z2 lattice: positive links stay labelled,
# including the two distinct positive edges when the side is 2.
sites = list(it.product(range(2), repeat=2))
edges = [(x, d) for x in sites for d in range(2)]
index = {e: i for i, e in enumerate(edges)}
step = lambda x, d: tuple((v+int(k == d)) % 2 for k, v in enumerate(x))
patterns = defaultdict(float)
u = 0.7
for state in it.product(signs, repeat=len(edges)):
    bad = frozenset(i for i, x in enumerate(sites) if
                    state[index[(x, 0)]]*state[index[(step(x, 0), 1)]]*
                    state[index[(step(x, 1), 0)]]*state[index[(x, 1)]] == -1)
    patterns[bad] += math.exp(-2*u*len(bad))/2**len(edges)
z_delta = patterns[frozenset()]
q = math.exp(-2*u)
subsets = [frozenset(i for i in range(4) if mask & 1 << i) for mask in range(16)]
penalty_runs = []
for h in [0, .2, 1.3, 5, 15]:
    zh = sum(w*math.exp(-h*len(A)) for A, w in patterns.items())
    full = patterns[frozenset(range(4))]*math.exp(-4*h)/zh
    max_chess = 0.
    for A in subsets:
        moment = sum(w*math.exp(-h*len(B)) for B, w in patterns.items() if A <= B)/zh
        bound = full**(len(A)/4)
        assert moment <= bound+1e-14
        assert moment <= (q*math.exp(-h))**len(A)+1e-14
        max_chess = max(max_chess, moment/(bound or 1))
    penalty_runs.append({'h': h, 'Z_h': zh, 'max_chessboard_ratio': max_chess})
A = frozenset([0, 1])
limit_numerator = sum(w*math.exp(-30*len(B-A)) for B, w in patterns.items() if A <= B)
assert abs(limit_numerator-patterns[A]) < 1e-14
for H in subsets:
    ratio = sum(w for A, w in patterns.items() if A <= H)/z_delta
    assert ratio <= (1+q)**len(H)+1e-13
checks['periodic_Z2_penalty_chessboard_reference_and_holes'] = True
controls['remove_penalty_before_infinite_limit_rejected'] = abs(sum(w for B, w in patterns.items() if A <= B)-patterns[A]) > 1e-6
controls['raw_probability_is_not_reference_ratio'] = abs(patterns[A]/sum(patterns.values())-patterns[A]/z_delta) > 1e-4

# Two-loop finite slice. p0=aby, p1=cdy, p2=y, p3=a, p4=c. Last two
# Wilson plaquettes come from fixed exterior transporters; all are explicit.
u, t = 1.1, 2.4
eps = [.08+.11j, -.05+.07j, .04-.09j, -.02+.03j, .06-.04j]
groups = list(it.product(signs, repeat=2))
Vstates = list(it.product(signs, repeat=2))
Xstates = list(it.product(signs, repeat=4))


def action(x, y):
    a, b, c, d = x
    return [1-a*b*y, 1-c*d*y, 1-y, 1-a, 1-c]


def kernel(v, mean, normalized=True):
    value = math.exp(-t*(1-v*mean))
    norm = (math.exp(-t*(1-mean))+math.exp(-t*(1+mean)))/2
    return value/norm if normalized else value


def local(pair, y, v, j, source=False, normalized=True):
    a, b = pair
    acts = (1-a*b*y, 1-a)
    ix = (j, 3+j)
    exponent = -u*sum(s*(1+eps[k] if source else 1) for s, k in zip(acts, ix))
    return cmath.exp(exponent)*kernel(v, (a+b)/2, normalized)


def weight(x, y, V, source=False, normalized=True):
    return cmath.exp(-u*(1-y)*(1+eps[2] if source else 1))*local(x[:2], y, V[0], 0, source, normalized)*local(x[2:], y, V[1], 1, source, normalized)


def label(x, y, V):
    acts = action(x, y)
    A = tuple(j for j, s in enumerate(acts) if s)
    dirty = {j for j in range(2) if j in A or 3+j in A or 2 in A}
    C = tuple(j for j in range(2) if j not in dirty and V[j] != x[2*j])
    F = tuple(j for j in range(2) if j in A and V[j] != y)
    return A, C, F


def correlated(x):
    return int(x[0] == x[2])


def cut(x, y):
    return x[0]*x[1]*y == 1 and x[2]*x[3]*y == 1


zcutV = {V: sum(weight(x, y, V).real/32 for y in signs for x in Xstates if cut(x, y)) for V in Vstates}
zcut = sum(zcutV.values())/4
z_allgood = sum(weight(x, y, V).real/128 for V in Vstates for y in signs for x in Xstates if not any(action(x, y)))
zW = sum(math.exp(-u*sum(action(x, y)))/32 for y in signs for x in Xstates)
zjoint = sum(weight(x, y, V).real/128 for V in Vstates for y in signs for x in Xstates)
assert 0 < z_allgood <= zcut <= zW
assert abs(zW-zjoint) < 1e-14
checks['normalized_fine_marginal_and_original_integrated_reference'] = True
assert max(zcutV.values())-min(zcutV.values()) > .01

direct = defaultdict(complex)
for V in Vstates:
    for y in signs:
        for x in Xstates:
            direct[label(x, y, V)] += weight(x, y, V, True)*correlated(x)/(128*zcut)


def replacement(wrong_insertion=False, uniform_reference=False):
    out = defaultdict(complex)
    for V in Vstates:
        for y in signs:
            Dj = [sum(local(g, y, V[j], j) for g in groups if g[0]*g[1]*y == 1)/4 for j in range(2)]
            for sea in Xstates:
                if not cut(sea, y):
                    continue
                denominator = zcutV[V] if uniform_reference else zcut
                outside = weight(sea, y, V)*cmath.exp(-u*sum(e*s for e, s in zip(eps, action(sea, y))))/(128*denominator)
                for mask in range(4):
                    B = [j for j in range(2) if mask & (1 << j)]
                    compensation = 1
                    for j in B:
                        acts = action(sea, y)
                        compensation *= cmath.exp(u*(eps[j]*acts[j]+eps[3+j]*acts[3+j]))/Dj[j]
                    for gs in it.product(groups, repeat=len(B)):
                        hat = list(sea)
                        inner = 1
                        for j, g in zip(B, gs):
                            if g[0]*g[1]*y != -1:
                                inner = 0
                                break
                            hat[2*j:2*j+2] = g
                            inner *= local(g, y, V[j], j, True)/4
                        if inner:
                            xi_x = sea if wrong_insertion else tuple(hat)
                            out[label(xi_x, y, V)] += outside*compensation*inner*correlated(xi_x)
    return out


replaced = replacement()
keys = direct.keys() | replaced.keys()
max_error = max(abs(direct[k]-replaced[k]) for k in keys)
assert max_error < 5e-14
checks['joint_refinement_with_correlated_insertion_and_original_sources'] = True
bad_xi, bad_ref = replacement(wrong_insertion=True), replacement(uniform_reference=True)
xi_gap = max(abs(direct[k]-bad_xi[k]) for k in direct.keys() | bad_xi.keys())
ref_gap = max(abs(direct[k]-bad_ref[k]) for k in direct.keys() | bad_ref.keys())
controls['unreplaced_sea_history_rejected'] = xi_gap > 1e-4
controls['uniform_coarse_reference_rejected'] = ref_gap > 1e-4
unnormalized = sum(weight(x, y, V, normalized=False).real/128 for V in Vstates for y in signs for x in Xstates)
controls['dropped_kernel_normalizer_rejected'] = abs(unnormalized-zW) > .01

# Independently sum the exact (A,C) refinement without the insertion. No product
# approximation to the fine field is taken. Only the conditional V law factors.
fine = defaultdict(float)
histories = defaultdict(float)
for y in signs:
    for x in Xstates:
        A = tuple(j for j, s in enumerate(action(x, y)) if s)
        fine[A] += math.exp(-u*sum(action(x, y)))/32
        for V in Vstates:
            AA, C, _ = label(x, y, V)
            histories[(AA, C)] += weight(x, y, V).real/128
pclean = 1/(1+math.exp(2*t))
max_refinement = 0
for (A, C), value in histories.items():
    bound = fine[A]*pclean**len(C)
    assert value <= bound+1e-14
    max_refinement = max(max_refinement, value/(bound or 1))
checks['clean_mismatch_conditional_product_with_dirty_unrestricted'] = True
dirty_mismatch = sum(kernel(v, 0)/2 for v in signs if v != 1)
controls['dirty_link_clean_tail_rejected'] = dirty_mismatch > pclean*10
assert all(checks.values()) and all(controls.values())
print(json.dumps({'checks': checks, 'negative_controls': controls,
                  'periodic_Z2': {'configurations': 256, 'realized_patterns': len(patterns), 'Z_delta': z_delta, 'penalty_runs': penalty_runs},
                  'refinement': {'joint_states': 128, 'bins_with_insertion': len(direct), 'max_replacement_error': max_error,
                                 'unreplaced_history_gap': xi_gap, 'uniform_reference_gap': ref_gap,
                                 'Z_cut_V': {str(k): v for k, v in zcutV.items()}, 'Z_delta': z_allgood,
                                 'Z_cut': zcut, 'Z_W': zW, 'normalizer_omission_gap': zW-unnormalized,
                                 'max_clean_refinement_ratio': max_refinement, 'clean_mismatch_probability': pclean,
                                 'dirty_mismatch_probability': dirty_mismatch},
                  'scope': 'finite Z2 gauge/conditional slice diagnostics, not SU(N), 4D RP, or continuum proofs',
                  'seconds': time.time()-start}, indent=2))
