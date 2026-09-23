#!/usr/bin/env python3
"""Independent finite controls for a one-link exponential electric weight.

This reads only the permitted finite-path physical matrix and uses a separate
six-vertex tree construction for the pair-support counterexample.  The
all-graph moment claim rests on the written operator proof, not this scan.
"""

import hashlib
import json
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
FINITE_PATH = (
    HERE.parent / "formation_capacity_independent" / "FINITE_PATH_RESULTS.json"
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gauss(q, electric, edges, a_sites):
    div = {v: 0 for v in q}
    for edge, value in electric.items():
        u, v = edge
        div[u] += value
        div[v] -= value
    return all(div[v] == q[v] - (v in a_sites) for v in q)


def hop(q, electric, edge):
    a, b = edge
    assert q[a] in (-1, 1) and q[b] == 0
    qq, ee = q.copy(), electric.copy()
    old = qq[a]
    qq[a], qq[b] = 0, old
    ee[edge] -= old
    return qq, ee


def tree_witness():
    # All links point from A to B.  The shared neighbor is d, while the
    # monitored link a-b has a B endpoint not adjacent to c.
    edges = [("a", "b"), ("a", "d"), ("c", "d"),
             ("c", "x"), ("c", "y")]
    first_q = {"a": 1, "c": -1, "b": 0, "d": 1, "x": 0, "y": 1}
    second_q = {"a": 1, "c": -1, "b": 1, "d": 0, "x": 0, "y": 1}
    first_e = dict(zip(edges, [0, 0, -1, 0, -1]))
    second_e = dict(zip(edges, [-1, 1, -1, 0, -1]))
    assert gauss(first_q, first_e, edges, {"a", "c"})
    assert gauss(second_q, second_e, edges, {"a", "c"})
    fq, fe = hop(first_q, first_e, ("a", "b"))
    fq, fe = hop(fq, fe, ("c", "x"))
    sq, se = hop(second_q, second_e, ("a", "d"))
    sq, se = hop(sq, se, ("c", "x"))
    assert fq == sq and fe == se
    assert gauss(fq, fe, edges, {"a", "c"})
    assert second_e[("a", "b")] - first_e[("a", "b")] == -1
    return {
        "edges_A_to_B": edges,
        "first_input": {"q": first_q, "E": list(first_e.values())},
        "second_input": {"q": second_q, "E": list(second_e.values())},
        "common_two_hop_output": {"q": fq, "E": list(fe.values())},
        "pair_anchor_shared_B": "d",
        "monitored_B_not_adjacent_to_other_anchor": "b",
        "offdiagonal_SstarS_matrix_element_at_least": 1,
        "monitored_link_input_field_difference": -1,
    }


def finite_path_control(data):
    states = data["states"]
    edges = data["edges"]
    n = len(states)
    assert n == data["physical_dimension"]
    assert all(
        all(
            sum((value if u == v else -value if w == v else 0)
                for (u, w), value in zip(edges, st["E"]))
            == st["q"][v] - (v in data["A"])
            for v in range(data["vertices"])
        ) for st in states
    )
    matrices = {"H4": data["sparse_H4"]}
    matrices.update({"resolved_" + k: v for k, v in data["resolved_jumps"].items()})
    matrices.update({"coherent_" + k: v for k, v in data["coherent_jumps"].items()})
    support = {}
    for name, entries in matrices.items():
        delta = [
            [states[i]["E"][e] - states[j]["E"][e]
             for e in range(len(edges))]
            for i, j, value in entries if value != 0
        ]
        max_per_link = [max((abs(d[e]) for d in delta), default=0)
                        for e in range(len(edges))]
        assert max(max_per_link) <= 1
        support[name] = {
            "nonzero_entries": len(delta),
            "max_abs_single_link_shift": max(max_per_link),
            "max_abs_shift_by_edge": max_per_link,
        }
    h = np.zeros((n, n))
    for i, j, value in data["sparse_H4"]:
        h[i, j] += value
    assert np.array_equal(h, h.T)
    # This entry changes the leaf edge (1,0), yet its only possible pair
    # anchor (1,3) has 3 not adjacent to 0.  It corroborates the tree proof.
    outsider = next(
        (i, j, value) for i, j, value in data["sparse_H4"]
        if i != j and states[i]["E"][0] != states[j]["E"][0]
    )
    i, j, value = outsider
    assert edges[0] == [1, 0] and [1, 3] in data["pair_anchors"]
    assert 0 not in [b for a, b in edges if a == 3]

    # Direct generator form on the finite physical path at lambda=0.7.
    # The bound is deliberately much larger; the check tests signs and the
    # jump/Hamiltonian placement independently of the analytic estimate.
    lam = 0.7
    kappa = delta_coupling = 1.0
    w = np.exp(lam * np.abs([st["E"][0] for st in states]))
    v = np.sqrt(w)
    def generator_form(jump_dict):
        weighted = 1j * (h @ np.diag(w) - np.diag(w) @ h) * delta_coupling
        for entries in jump_dict.values():
            L = np.zeros((n, n))
            for i0, j0, value0 in entries:
                L[i0, j0] += value0
            gram = L.T @ L
            weighted += kappa * (
                L.T @ np.diag(w) @ L
                - (gram @ np.diag(w) + np.diag(w) @ gram) / 2
            )
        g = weighted / v[:, None] / v[None, :]
        assert np.max(np.abs(g - g.conj().T)) < 1e-12
        return g

    resolved_g = generator_form(data["resolved_jumps"])
    coherent_g = generator_form(data["coherent_jumps"])
    # On this diagonal electric probe, the cross-sign terms vanish because
    # opposite newborn signs occupy orthogonal final A charge words.
    assert np.max(np.abs(resolved_g - coherent_g)) < 1e-12
    measured = float(np.linalg.eigvalsh(resolved_g)[-1])
    z = 2
    c_bound = (4 * delta_coupling * z**5 * (z - 1)
               + 8 * kappa * z * (z - 1)**2) * (np.exp(lam) - 1)
    assert measured <= c_bound + 1e-10
    return {
        "matrix_source_sha256": sha256(FINITE_PATH),
        "graph": data["graph"],
        "physical_dimension": n,
        "support": support,
        "nonadjacent_anchor_link_witness": {
            "H4_matrix_entry": [i, j, value],
            "monitored_edge": edges[0],
            "other_anchor": 3,
            "input_field": states[j]["E"],
            "output_field": states[i]["E"],
        },
        "weighted_generator_control": {
            "instruments": "resolved and coherent, exactly equal on this probe",
            "link_index": 0,
            "lambda": lam,
            "delta": delta_coupling,
            "kappa": kappa,
            "max_eigenvalue_of_weighted_form": measured,
            "analytic_uniform_bound_at_z_2": float(c_bound),
        },
    }


def star_rate_control():
    out = []
    for z in (2, 3, 6, 12):
        # From all-A-plus, B-empty and E=0, the fixed edge changes in
        # 2(z-1) channels with its B site newborn and 2(z-1) with its B
        # site receiving the old A record.  Distinct paths within a channel
        # have distinct final B supports; opposite signs have distinct A q.
        affected = 4 * (z - 1)
        out.append({"degree": z,
                    "affected_resolved_path_norm_squared": affected,
                    "derivative_per_kappa_of_exp_abs_link_at_zero":
                    f"{affected}*(exp(lambda)-1)"})
    return out


def main():
    data = json.loads(FINITE_PATH.read_text())
    result = {
        "scope": "finite controls, not an all-graph proof",
        "tree_witness": tree_witness(),
        "finite_path_control": finite_path_control(data),
        "star_initial_rate_control": star_rate_control(),
    }
    out = HERE / "FIELD_EXPONENTIAL_PRE_RESULTS.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(out),
        "tree_witness": "PASS",
        "matrix_support": "PASS",
        "weighted_generator_control": "PASS",
        "source_sha256": result["finite_path_control"]["matrix_source_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
