"""Kill check k2: (a) is the sum of chirality != 0 at range 3 really 'missed nodes'?  Re-run the attacker's
finder on the same symbol with finer seed grids and see whether sum(chi) -> 0.
(b) does removing the pin leave a 'triplet' of nodes?  C3 (body-diagonal, spinor-lift/vector rep) covariant
nearest-neighbour and box-range-1 symbols: distribution of node counts and chirality by orbit."""
import sys, itertools
import numpy as np
sys.path.insert(0, "rerun")
import A_pin as A

# (a) range 3 finer seeds
A.rng = np.random.default_rng(5)
print("(a) range-3 O-covariant symbols: sum(chi) with seed grid 14 / 20 / 26 (time-limited: 3 samples)")
for s in range(3):
    const, C = A.random_coeffs(3)
    cav, tab = A.average(const, C, A.rot("O"), "full")
    row = []
    for ns in [14, 20, 26]:
        A.rng = np.random.default_rng(100 + s)
        nodes = A.find_nodes(cav, tab, nseed=ns)
        row.append((len(nodes), sum(c for _, c in nodes), sum(1 for _, c in nodes if c == 0)))
    print(f"   sample {s}: (nodes, sum chi, #chi=0 degenerate) at nseed 14/20/26 = {row}")

# (b) C3 group: cyclic permutation of axes (x->y->z), det +1
P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
C3 = [np.eye(3, dtype=int), P, P @ P]
def nn_random_coeffs(rng_):
    ws = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    C = {w: (rng_.normal(size=4), rng_.normal(size=4)) for w in ws}
    return rng_.normal(size=4), C
A.rng = np.random.default_rng(31)
print("(b) C3-covariant (vector coin), no other symmetry: node counts and per-sample chirality sum")
for label, gen in [("NN", nn_random_coeffs), ("box range 1", lambda r: A.random_coeffs(1))]:
    counts = {}
    ex = None
    for s in range(60):
        rg = np.random.default_rng(1000 + s)
        A.rng = rg
        const, C = gen(rg) if label == "NN" else A.random_coeffs(1)
        cav, tab = A.average(const, C, C3, "full")
        nodes = A.find_nodes(cav, tab, nseed=12)
        key = (len(nodes), sum(c for _, c in nodes))
        counts[key] = counts.get(key, 0) + 1
        if len(nodes) == 6 and ex is None:
            ex = nodes
    print("  ", label, "(nodes, sum chi) -> samples:", dict(sorted(counts.items())))
    if ex:
        print("   example with 6 nodes:", [(np.round(k, 3).tolist(), c) for k, c in ex])
