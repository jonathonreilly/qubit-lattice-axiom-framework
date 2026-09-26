#!/usr/bin/env python3
"""Independent finite physical-component variational calculation.

Distinct positive-axis wrap links on the periodic 2x2x2 cell complex. The
variational optimization uses exact histogram polynomials and positive-root
isolation; the ground state is computed from the explicitly assembled finite
matrix. An exact rational Collatz bound authenticates its ground energy.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import itertools
import json
import time

import numpy as np
import scipy.linalg as la
import scipy.sparse as sparse
import sympy as s

HERE = Path(__file__).resolve().parent


def main():
    tic = time.monotonic()
    vertices = list(itertools.product((0, 1), repeat=3))
    links = [(v, a) for v in vertices for a in range(3)]
    index = {edge: i for i, edge in enumerate(links)}
    def step(v, a): return tuple((v[i]+(i == a)) % 2 for i in range(3))
    faces = []
    for v in vertices:
        for a, b in itertools.combinations(range(3), 2):
            raised = [index[v, a], index[step(v, a), b]]
            lowered = [index[step(v, b), a], index[v, b]]
            assert len(set(raised+lowered)) == 4
            faces.append({"origin": v, "axes": (a, b), "raised": raised, "lowered": lowered,
                          "r": sum(1 << j for j in raised), "l": sum(1 << j for j in lowered)})
    seed = sum(1 << j for j, (v, a) in enumerate(links) if sum(v[b] for b in range(3) if b != a) % 2 == 0)
    def available(word, face): return word & (face["r"]+face["l"]) in (face["r"], face["l"])
    reached, queue = {seed}, [seed]
    while queue:
        word = queue.pop()
        for face in faces:
            if available(word, face):
                other = word ^ (face["r"]+face["l"])
                if other not in reached:
                    reached.add(other); queue.append(other)
    words = sorted(reached); wi = {word: i for i, word in enumerate(words)}
    dim = len(words)
    pairs, neighbors, degree = [], [[] for _ in words], []
    for face in faces:
        pairs.append([(wi[word], wi[word ^ (face["r"]+face["l"])]) for word in words
                      if word & (face["r"]+face["l"]) == face["l"]])
    for i, word in enumerate(words):
        for face in faces:
            if available(word, face): neighbors[i].append(wi[word ^ (face["r"]+face["l"])])
        degree.append(len(neighbors[i]))
    assert sum(degree) == 2*sum(map(len, pairs))
    vi = {v: i for i, v in enumerate(vertices)}
    incidence = np.zeros((len(vertices), len(links)), dtype=np.int64)
    for j, (v, a) in enumerate(links):
        incidence[vi[v], j] += 1; incidence[vi[step(v, a)], j] -= 1
    charges, fluxes = set(), set()
    for word in words:
        twice_e = np.array([2*((word >> j) & 1)-1 for j in range(len(links))])
        charges.add(tuple(map(int, incidence@twice_e)))
        fluxes.add(tuple(int(sum(twice_e[j] for j, (v, axis) in enumerate(links)
                                 if axis == a and v[a] == 0)) for a in range(3)))
    assert charges == {(0,)*8} and fluxes == {(0, 0, 0)}
    # Directly confirm that every m is computed in the bounded overlapping-face neighborhood.
    local_groups = []
    for p, face in enumerate(faces):
        overlap = [k for k, other in enumerate(faces)
                   if (face["r"]+face["l"]) & (other["r"]+other["l"])]
        counts = Counter()
        for a, b in pairs[p]:
            m = degree[b]-degree[a]
            local_m = sum(int(available(words[b], faces[k]))-int(available(words[a], faces[k])) for k in overlap)
            assert local_m == m
            assert Fraction(2)**degree[b] == Fraction(2)**m*Fraction(2)**degree[a]
            counts[m] += 1
        local_groups.append({"p": p, "overlapping_plaquettes_including_self": len(overlap),
                             "m_pair_histogram": dict(sorted(counts.items()))})
    rows, cols = [], []
    for i, adjacent in enumerate(neighbors):
        rows.extend([i]*len(adjacent)); cols.extend(adjacent)
    adjacency = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(dim, dim))
    assert (adjacency-adjacency.T).nnz == 0
    j, delta = s.Integer(1), s.Rational(1, 5)
    h = float(j-delta)*sparse.diags(degree)-float(j)*adjacency
    evals, evecs = la.eigh(h.toarray(), subset_by_index=(0, 1), driver="evr")
    ground = evecs[:, 0]
    if ground.sum() < 0: ground = -ground
    assert np.min(ground) > 0
    ground_residual = float(la.norm(h@ground-evals[0]*ground))
    # The floating vector is also an EXACT strictly positive rational test vector.
    # Irreducible stoquastic H then has min(Hv/v) <= E0 <= max(Hv/v).
    rational_ground = [Fraction(float(x)) for x in ground]
    ratios = [(Fraction(4, 5)*degree[i]*v-sum((rational_ground[k] for k in neighbors[i]), Fraction(0)))/v
              for i, v in enumerate(rational_ground)]
    energy_lower, energy_upper = min(ratios), max(ratios)
    assert float(energy_lower)-1e-13 <= evals[0] <= float(energy_upper)+1e-13
    assert float(energy_upper-energy_lower) < 1e-10
    site_hist = Counter(degree)
    bond_hist = Counter(degree[a]+degree[b] for row in pairs for a, b in row)
    q = s.symbols("q", positive=True)
    norm_poly = sum(count*q**(2*d) for d, count in site_hist.items())
    degree_poly = sum(d*count*q**(2*d) for d, count in site_hist.items())
    edge_poly = sum(count*q**total for total, count in bond_hist.items())
    energy = s.cancel(((j-delta)*degree_poly-2*j*edge_poly)/norm_poly)
    num, den = map(s.expand, s.fraction(energy))
    critical = s.Poly(s.expand(s.diff(num, q)*den-num*s.diff(den, q)), q)
    intervals = s.polys.polytools.intervals(critical, eps=s.Rational(1, 10**32))
    candidates = []
    for (lo, hi), multiplicity in intervals:
        if hi <= 0: continue
        assert lo > 0
        midpoint = (lo+hi)/2
        val = s.N(energy.subs(q, midpoint), 70)
        candidates.append({"q_interval": [str(lo), str(hi)], "multiplicity": multiplicity,
                           "q_mid": str(s.N(midpoint, 70)), "theta_mid": str(s.N(2*s.log(midpoint), 70)),
                           "energy_mid": str(val), "midpoint_exact": midpoint})
    limits = {"theta_minus_infinity": s.limit(energy, q, 0, dir="+"),
              "theta_plus_infinity": s.limit(energy, q, s.oo)}
    assert candidates
    optimum = min(candidates, key=lambda row: float(row["energy_mid"]))
    assert float(optimum["energy_mid"]) < min(float(v) for v in limits.values())
    theta = float(optimum["theta_mid"])
    degree_np = np.array(degree, dtype=float)
    psi = np.exp(theta*(degree_np-max(degree_np))/2)
    psi /= la.norm(psi)
    var_energy = float(psi@(h@psi))
    assert abs(var_energy-float(optimum["energy_mid"])) < 1e-12
    fidelity = float((psi@ground)**2)
    var_residual = float(la.norm(h@psi-var_energy*psi))
    for row in candidates: del row["midpoint_exact"]
    np.savez_compressed(HERE/"VARIATIONAL_COMPONENT.npz", states=np.array(words, dtype=np.uint32),
                        degree=np.array(degree, dtype=np.int16), ground=ground,
                        variational=psi, eigenvalues=evals)
    result = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "geometry": {"periods": [2, 2, 2], "vertices": vertices,
                           "distinct_positive_axis_links": links, "plaquettes": faces,
                           "seed_bits": seed, "component_dimension": dim,
                           "component_states_sha256": hashlib.sha256(json.dumps(words).encode()).hexdigest(),
                           "Gauss_twice": list(next(iter(charges))), "flux_twice": list(next(iter(fluxes))),
                           "oriented_pairs_by_p": list(map(len, pairs))},
              "weighted_locality_controls": local_groups,
              "flippability_histogram": dict(sorted(site_hist.items())),
              "edge_endpoint_flippability_sum_histogram": dict(sorted(bond_hist.items())),
              "J": str(j), "delta": str(delta),
              "variational_energy_function_q_exp_theta_over_2": str(s.factor(energy)),
              "critical_polynomial_factorization": str(s.factor(critical.as_expr())),
              "all_positive_critical_intervals": candidates,
              "endpoint_energy_limits": {k: str(v) for k, v in limits.items()},
              "uniform_energy": str(energy.subs(q, 1)),
              "optimum_theta_numeric": theta, "optimum_energy_numeric": var_energy,
              "computed_lowest_two_eigenvalues": evals.tolist(),
              "ground_energy_exact_rational_lower": str(energy_lower),
              "ground_energy_exact_rational_upper": str(energy_upper),
              "ground_energy_enclosure_width": float(energy_upper-energy_lower),
              "ground_eigenvector_residual_norm": ground_residual,
              "variational_energy_excess": var_energy-float(evals[0]),
              "variational_fidelity_numeric": fidelity,
              "variational_eigenvector_residual_norm": var_residual,
              "mean_flippability_variational": float(psi@(degree_np*psi)),
              "mean_flippability_ground": float(ground@(degree_np*ground)),
              "data_artifact": {"path": str(HERE/"VARIATIONAL_COMPONENT.npz"),
                                "sha256": hashlib.sha256((HERE/"VARIATIONAL_COMPONENT.npz").read_bytes()).hexdigest()},
              "limits": "One finite fixed component. Eigenvector/fidelity numerical; ground energy bounded by exact rational Collatz inequalities. Root isolation covers the whole one-parameter family. No thermodynamic or phase conclusion.",
              "runtime_seconds": time.monotonic()-tic}
    text = json.dumps(result, indent=2)+"\n"
    (HERE/"VARIATIONAL_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__": main()
