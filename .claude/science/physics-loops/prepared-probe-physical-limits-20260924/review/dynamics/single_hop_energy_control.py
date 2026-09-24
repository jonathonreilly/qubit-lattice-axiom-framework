"""Independent exact initial M=sum F_a^* F_a polynomial, with no H4 rerun.

This small extra check supports the explicitly separate bare-P microscopic
ordinary-energy identity. It does not compute a microscopic post-jump state.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from hashlib import sha256
import json
import time
import primitive_dynamics_control as p


def one(side):
    vertices, index, aset, neighbors, edges, edge_id, axes = p.graph(side)
    def vertex(x):
        return index[tuple(t % side for t in x)]
    a, d, h, c, e, b, v1, v2, v3 = map(vertex, [(0,0,0), (1,1,0), (2,2,0),
        (1,0,0), (0,1,0), (-1,0,0), (0,-1,0), (0,0,1), (0,0,-1)])
    word = [int(i in set(aset)) for i in range(len(vertices))]
    word[d] = word[h] = -1
    word[v1] = word[v2] = word[v3] = 1
    wc = word.copy(); wc[c] = 1
    we = word.copy(); we[e] = 1
    initial = {(tuple(wc), ((edge_id[d,c], -1),)): 1,
               (tuple(we), ((edge_id[d,e], -1),)): -1}
    polynomial = defaultdict(Fraction)
    path_count = 0
    for x in aset:
        out = defaultdict(int)
        for (w, flow), coefficient in initial.items():
            for w1, ed, k in p.outward(w, x, neighbors, edge_id):
                out[w1, p.shifted(flow, ed, k)] += coefficient
                path_count += 1
        by_word = defaultdict(list)
        for (w, flow), coefficient in out.items():
            if coefficient:
                by_word[w].append((flow, coefficient))
        for terms in by_word.values():
            for left, lc in terms:
                for right, rc in terms:
                    diff = right
                    for ed, k in left:
                        diff = p.shifted(diff, ed, -k)
                    polynomial[diff] += Fraction(lc * rc, 2)
    polynomial = {flow: value for flow, value in polynomial.items() if value}
    loop = ()
    for ed, k in [(edge_id[d,c], -1), (edge_id[a,e], -1),
                  (edge_id[d,e], 1), (edge_id[a,c], 1)]:
        loop = p.shifted(loop, ed, k)
    reverse_loop = tuple((ed, -k) for ed, k in loop)
    assert polynomial == {(): Fraction(len(edges)-24), loop: Fraction(-1,2),
                          reverse_loop: Fraction(-1,2)}
    assert p.harmonic_signature(loop, axes) == (0,0,0)
    rows = []
    for flow, coefficient in sorted(polynomial.items()):
        rows.append({"coefficient": p.fraction(coefficient), "shifts": [
            {"A": vertices[edges[ed][0]], "B": vertices[edges[ed][1]], "power": k}
            for ed, k in flow]})
    return {"side": side, "edges": len(edges), "outward_paths_from_two_branches": path_count,
            "polynomial": rows, "flat_mean_M": len(edges)-25,
            "selected_output_mean_M": len(edges)-36,
            "flat_output_minus_input_M": -11}


def main():
    start = time.perf_counter()
    here = Path(__file__).resolve().parent
    print(json.dumps({"scope": __doc__, "rows": [one(6), one(8)],
                      "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                      "primitive_source_sha256": sha256((here / "primitive_dynamics_control.py").read_bytes()).hexdigest(),
                      "elapsed_seconds": time.perf_counter()-start}, indent=2))


if __name__ == "__main__":
    main()
