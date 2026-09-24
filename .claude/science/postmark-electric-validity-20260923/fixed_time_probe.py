#!/usr/bin/env python3
"""Fixed-time finite-spin versus proposed rotor-generator probe.

All operators are assembled from the root lane's physical charge/E hop
representation.  The rotor comparison uses finite path truncations solely as
a numerical diagnostic; no cutoff is treated as a proof of tail control.
"""
from __future__ import annotations
from collections import defaultdict
import importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("core", HERE / "core_derivation.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
INITIAL = core.INITIAL


def path_basis(radius):
    nodes = core.walk_nodes(radius)
    inv = {state: n for n, state in nodes.items()}
    assert len(inv) == 2 * radius + 1
    return nodes, inv


def m_row(state, spin):
    """One row of M=A* A; use independent explicit P-Q1-P composition."""
    out = defaultdict(float)
    for q1, a, *_ in core.all_hops(state, spin):
        if core.count_empty_A(q1) != 1:
            continue
        for p2, b, *_ in core.all_hops(q1, spin):
            if core.count_empty_A(p2) == 0:
                out[p2] += a * b
    return dict(out)


def z_row(state, spin):
    """One column of Z=Pi2 T Pi1 T P, keyed by physical Q2 states."""
    out = defaultdict(float)
    for q1, a, *_ in core.all_hops(state, spin):
        if core.count_empty_A(q1) != 1:
            continue
        for q2, b, *_ in core.all_hops(q1, spin):
            if core.count_empty_A(q2) == 2:
                out[q2] += b * a
    return dict(out)


def h4_rows(states, inv, spin):
    """Construct M^2 - Z*Z/2 from physical intermediate states."""
    mrows = {}
    zrows = {}
    for n, st in states.items():
        mrows[n] = {inv[t]: v for t, v in m_row(st, spin).items() if t in inv}
        zrows[n] = z_row(st, spin)
    # M^2. Intermediate P states are exactly the physical two-hop neighbors.
    m2 = {n: defaultdict(float) for n in states}
    for n, row in mrows.items():
        for k, x in row.items():
            if k not in mrows:
                continue
            for j, y in mrows[k].items():
                if j in states:
                    m2[n][j] += x * y
    # Z*Z by joining columns on their common physical Q2 endpoint.
    reverse = defaultdict(list)
    for n, row in zrows.items():
        for q2, z in row.items():
            reverse[q2].append((n, z))
    h4 = {n: defaultdict(float, m2[n]) for n in states}
    for related in reverse.values():
        for n, a in related:
            for j, b in related:
                h4[n][j] -= 0.5 * a * b
    return {n: dict(row) for n, row in h4.items()}


def h2_rows(states, inv, spin):
    rows = {}
    for n, st in states.items():
        vals = defaultdict(float)
        for target, amp, *_ in core.two_hop_paths(st, spin):
            if target in inv:
                vals[inv[target]] += amp
        rows[n] = dict(vals)
    return rows


def d_rows(states, inv):
    rows = {}
    for n, st in states.items():
        vals = defaultdict(float)
        for target, _amp, coeff, _data in core.two_hop_paths(st):
            if target in inv:
                vals[inv[target]] += float(coeff)
        rows[n] = dict(vals)
    return rows


def sparse_from_rows(rows, domain):
    index = {n: i for i, n in enumerate(domain)}
    rr, cc, vv = [], [], []
    for n in domain:
        for j, value in rows.get(n, {}).items():
            if j in index and value:
                rr.append(index[n]); cc.append(index[j]); vv.append(value)
    return coo_matrix((vv, (rr, cc)), shape=(len(domain), len(domain)), dtype=np.complex128).tocsr()


def max_hermitian_defect(mat):
    delta = mat - mat.getH()
    return float(np.max(np.abs(delta.data))) if delta.nnz else 0.0


def vacancy_probability(state_list, psi):
    return float(sum(abs(psi[i]) ** 2 for i, st in enumerate(state_list) if st[0][3] == 0))


def run_exact_spin(spin, radius):
    nodes, inv = path_basis(radius)
    valid_ns = [n for n, st in nodes.items() if max(abs(e) for e in st[1]) <= spin]
    valid_ns.sort()
    assert valid_ns and 0 in valid_ns
    assert valid_ns == list(range(valid_ns[0], valid_ns[-1] + 1)), (spin, valid_ns[:3], valid_ns[-3:])
    states = {n: nodes[n] for n in valid_ns}
    h2 = h2_rows(states, inv, spin)
    h4 = h4_rows(states, inv, spin)
    h2mat = sparse_from_rows(h2, valid_ns)
    h4mat = sparse_from_rows(h4, valid_ns)
    assert max_hermitian_defect(h2mat) < 1e-12
    assert max_hermitian_defect(h4mat) < 1e-10
    C = spin * (spin + 1)
    exact = C * h2mat + h4mat
    psi0 = np.zeros(len(valid_ns), dtype=np.complex128)
    psi0[valid_ns.index(0)] = 1
    p = []
    state_list = [states[n] for n in valid_ns]
    for t in (0.25, 0.5, 1.0):
        psi = expm_multiply((-1j * t) * exact, psi0)
        p.append(vacancy_probability(state_list, psi))
    return {"S": spin, "C": C, "epsilon": 1 / math.sqrt(C), "P_dimension_in_component": len(valid_ns),
            "path_domain": [valid_ns[0], valid_ns[-1]], "H2_hermitian_defect": max_hermitian_defect(h2mat),
            "H4_hermitian_defect": max_hermitian_defect(h4mat), "observable": p, "tail_probability_outside_physical_domain": [0.0, 0.0, 0.0]}


def run_candidate(spin, cutoff, radius):
    nodes, inv = path_basis(radius)
    domain = list(range(-cutoff, cutoff + 1))
    states = {n: nodes[n] for n in domain}
    h2 = h2_rows(states, inv, None)
    d = d_rows(states, inv)
    h4 = h4_rows(states, inv, None)
    h2mat = sparse_from_rows(h2, domain)
    dmat = sparse_from_rows(d, domain)
    h4mat = sparse_from_rows(h4, domain)
    assert max_hermitian_defect(h2mat) < 1e-12
    assert max_hermitian_defect(dmat) < 1e-10
    assert max_hermitian_defect(h4mat) < 1e-9
    C = spin * (spin + 1)
    candidate = C * h2mat + dmat + h4mat
    psi0 = np.zeros(len(domain), dtype=np.complex128)
    psi0[cutoff] = 1
    state_list = [states[n] for n in domain]
    p = []
    tail = []
    allowed = [n for n, st in nodes.items() if max(abs(e) for e in st[1]) <= spin]
    lo, hi = min(allowed), max(allowed)
    for t in (0.25, 0.5, 1.0):
        psi = expm_multiply((-1j * t) * candidate, psi0)
        p.append(vacancy_probability(state_list, psi))
        tail.append(float(sum(abs(psi[i]) ** 2 for i, n in enumerate(domain) if n < lo or n > hi)))
    return {"S": spin, "C": C, "rotor_path_cutoff": cutoff, "candidate_H2_hermitian_defect": max_hermitian_defect(h2mat),
            "candidate_D_hermitian_defect": max_hermitian_defect(dmat), "candidate_H4_hermitian_defect": max_hermitian_defect(h4mat),
            "observable": p, "tail_probability_outside_physical_domain": tail, "physical_spin_path_domain": [lo, hi]}


def main():
    results = []
    for spin in (2, 3, 4, 6, 8, 10, 12, 16):
        max_cut = max(30, 12 * spin)
        radius = max(400, 5 * max_cut + 20)
        exact = run_exact_spin(spin, radius)
        candidates = [run_candidate(spin, cutoff, radius) for cutoff in (max(20, 3 * spin), max(40, 6 * spin), max(80, 12 * spin))]
        results.append({"exact": exact, "candidate_cutoffs": candidates,
                        "candidate_cutoff_spread_by_time": [max(r["observable"][i] for r in candidates) - min(r["observable"][i] for r in candidates) for i in range(3)]})
    out = {
        "status": "floating-point fixed-time diagnostic only; not a certified discrepancy or tail theorem",
        "observable": "probability that the vacancy is at B site 3",
        "times": [0.25, 0.5, 1.0],
        "parameters": {"K": 1, "delta": 1, "C": "S(S+1)", "epsilon": "1/sqrt(C)"},
        "exact_operator": "C H2,S + H4,S; physical finite-spin legal hops",
        "candidate_operator": "C H2,infinity + D + H4,infinity; rotor path principal truncations, cutoff varied",
        "results": results,
        "limits": "No interval arithmetic, no proof of candidate domain/self-adjointness, and no uniform electric-tail control. A stable gap is only a warning until certified.",
    }
    payload = json.dumps(out, indent=2) + "\n"
    (HERE / "FIXED_TIME_PROBE_RESULTS.json").write_text(payload)
    print(payload, end="")

if __name__ == "__main__":
    main()
