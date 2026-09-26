#!/usr/bin/env python3
"""Bounded post-seal checks. Never imports or executes an author runner.

Authenticate the authorized packet and frozen blind evidence; reassemble the
readout signs, test the author's analytic identity on the independently chosen
three-square component, and reconstruct the open-cube superoperator by its
action on matrix units (not the author's Kronecker implementation).
"""
from __future__ import annotations

import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path
import time

import numpy as np
import scipy.linalg as la
import sympy as s

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent
PRE_HASH = "99c8c68ce7803368e633fdf7f3d7314eb1f47f7ba3150a3fa732888e1f1a43b3"
AUTHOR_HASH = "d9ea3fc91a09aff6e197925cd2a37907217f4583a8bf29a9a871a64423c2b8fc"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def authenticate(path, expected):
    assert sha(path) == expected, str(path)
    seal = json.loads(path.read_text())
    rows = seal.get("sources", []) + seal["artifacts"]
    for row in rows:
        p = Path(row["path"])
        assert p.stat().st_size == row["bytes"], str(p)
        assert sha(p) == row["sha256"], str(p)
    return {"path": str(path), "sha256": expected,
            "matched_bindings": len(rows), "all_match": True}


def zero(m):
    return all(s.cancel(v) == 0 for v in m)


def readout():
    # Direct bit-word transition enumeration, with most-significant link 0.
    states = list(itertools.product((0, 1), repeat=4))
    w = s.zeros(16)
    for col, bits in enumerate(states):
        if bits == (0, 0, 1, 1):
            w[states.index((1, 1, 0, 0)), col] = 1
    x, y = w+w.T, -s.I*(w-w.T)
    p = w.T*w+w*w.T
    z = s.diag(*[2*bits[0]-1 for bits in states])
    eye = s.eye(16)
    pulses = {}
    for axis, op in (("Y", y), ("X", x)):
        for setting in (-1, 1):
            pulse = eye+(s.sqrt(2)/2-1)*p-s.I*setting*s.sqrt(2)*op/2
            target = z*(eye-p)+(-setting*x if axis == "Y" else setting*y)
            assert zero(pulse.H*z*pulse-target)
            pulses[axis, setting] = pulse
    # Independent X setting is the negative of the author's setting.
    own_x_plus = eye+(s.sqrt(2)/2-1)*p+s.I*s.sqrt(2)*y/2
    assert zero(own_x_plus-pulses["Y", -1])
    diagonal_phase = s.diag(*[s.exp(-s.I*s.pi*z[i, i]/4) for i in range(16)])
    assert zero(diagonal_phase*x*diagonal_phase.H-y)
    a, b = eye[:, 3], eye[:, 12]
    psi = {"real_plus": (a+b)/s.sqrt(2), "real_minus": (a-b)/s.sqrt(2),
           "imag_plus": (a+s.I*b)/s.sqrt(2)}
    result = json.loads((AUTHOR/"FRESH_CHARGED_RECORD_LOOP_READOUT_RESULTS.json").read_text())
    exact = result["exact_results"]
    assert exact["physical_flippable_doublet"] == {
        "source_basis": 3, "target_basis": 12, "all_divergences": 0}
    compared = 0
    for row in exact["phase_state_record_probabilities"]:
        v = psi[row["state"]]
        assert s.expand((v.H*x*v)[0]) == s.sympify(row["X"])
        assert s.expand((v.H*y*v)[0]) == s.sympify(row["Y"])
        for obs in row["outcomes"]:
            pulse = pulses[obs["axis"], obs["setting"]]
            q = obs["new_tail_charge"]
            value = s.expand((v.H*pulse.H*(eye-q*z)*pulse*v)[0]/2)
            assert value == s.sympify(obs["probability"])
            compared += 1
    for row in exact["nonflippable_bias_controls"]:
        i = row["basis"]
        assert p[i, i] == 0
        assert -z[i, i] == s.sympify(row["m_plus"]) == s.sympify(row["m_minus"])
    return {"author_phase_probabilities_recomputed_exactly": compared,
            "nonflippable_rows_recomputed_exactly": 14,
            "author_X_estimator": "s*q, pulse exp(-i*s*pi*Y/4)",
            "author_Y_estimator": "-s*q, pulse exp(-i*s*pi*X/4)",
            "setting_map_to_sealed_reconstruction": "s_author=-s_independent for X; equal for Y",
            "diagonal_phase_synthesis_exact": True,
            "imaginary_cat_Y": "-1"}


def analytic_identity():
    # Reuse only the frozen independently assembled component, not author geometry.
    own = json.loads((HERE/"COOLING_RESULTS.json").read_text())["physical_controls"]
    states = own["component"]
    pairs = own["oriented_pairs_by_plaquette"]
    # A different separating linear functional from the author's base-three F.
    f = states
    v = s.Matrix([s.Integer(2)**(a-min(f)) for a in f])
    assert len(set(f)) == len(f)
    rates = list(map(s.Rational, own["rates"]))
    h = list(map(s.Rational, own["Hamiltonian_coefficients"]))
    total = s.zeros(len(f), 1)
    rows = []
    for pp, gamma, hh in zip(pairs, rates, h):
        ell = s.zeros(len(f))
        delta = {f[b]-f[a] for a, b in pp}
        assert len(delta) == 1
        dd = next(iter(delta))
        for a, b in pp:
            ell[a, a] += s.Rational(1, 2)
            ell[b, a] += s.Rational(1, 2)
            ell[a, b] -= s.Rational(1, 2)
            ell[b, b] -= s.Rational(1, 2)
        pm = ell.H*ell
        # tanh(log(2)*delta/2), represented without transcendental arithmetic.
        th = (s.Integer(2)**dd-1)/(s.Integer(2)**dd+1)
        assert zero(pm*v+th*ell.H*v)
        total += (gamma/2-s.I*hh)*(pm*v+th*ell.H*v)
        rows.append({"delta_F": dd, "pair_count": len(pp), "identity_exact": True})
    assert zero(total)
    vandermonde = s.Matrix([[ff**k for k in range(len(f))] for ff in f])
    assert vandermonde.det() != 0
    return {"geometry": own["geometry"], "dimension": len(f),
            "separating_F": "integer bit-word; linear in all link bits",
            "t": "log(2)", "checks": rows,
            "R_dagger_identity_exact_for_inhomogeneous_signed_h": True,
            "Vandermonde_determinant": str(vandermonde.det()),
            "independent_polynomial_proof": "Preserved verbatim in sealed REPORT.md; not replaced."}


def modular_rank(matrix, prime=257):
    # Python-int row elimination, independent modulus and implementation.
    a = [[int(v) % prime for v in row] for row in matrix]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, prime)
        a[r] = [(v*inv) % prime for v in a[r]]
        for i in range(r+1, len(a)):
            mul = a[i][col]
            if mul:
                a[i] = [(v-mul*w) % prime for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def cube():
    vertices = list(itertools.product((0, 1), repeat=3))
    edges = []
    for v in vertices:
        for axis in range(3):
            if v[axis] == 0:
                w = tuple(v[i]+(i == axis) for i in range(3))
                edges.append((v, w))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    faces = []
    for v in vertices:
        for i, j in itertools.combinations(range(3), 2):
            if v[i] or v[j]:
                continue
            vi = tuple(v[k]+(k == i) for k in range(3))
            vj = tuple(v[k]+(k == j) for k in range(3))
            vij = tuple(v[k]+(k in (i, j)) for k in range(3))
            raise_edges = [edge_index[v, vi], edge_index[vi, vij]]
            lower_edges = [edge_index[vj, vij], edge_index[v, vj]]
            faces.append((sum(1 << a for a in raise_edges), sum(1 << a for a in lower_edges)))
    seed = 476  # Explicitly selected after reading the author's reported cube fixture.
    reached = {seed}
    todo = [seed]
    while todo:
        word = todo.pop()
        for r, l in faces:
            mask = r+l
            if word & mask in (r, l):
                other = word ^ mask
                if other not in reached:
                    reached.add(other)
                    todo.append(other)
    words = sorted(reached)
    d = len(words)
    assert (len(edges), len(faces), d) == (12, 6, 9)
    matrices = []
    pair_counts = []
    for r, l in faces:
        m = np.zeros((d, d), dtype=np.int64)
        count = 0
        for a, word in enumerate(words):
            if word & (r+l) == l:
                b = words.index(word ^ (r+l))
                m[a, a] += 1; m[b, a] += 1; m[a, b] -= 1; m[b, b] -= 1
                count += 1
        matrices.append(m)
        pair_counts.append(count)
    # 8*G assembled column by column from action on E_rc, row-major vectorization.
    real = np.zeros((d*d, d*d), dtype=np.int64)
    imag = np.zeros_like(real)
    loss = np.zeros((d, d), dtype=float)
    for p, m in enumerate(matrices):
        pm4 = m.T@m
        gamma, hh = p+1, (-1)**p*(p+2)
        loss += gamma*pm4/4
        for r, c in itertools.product(range(d), repeat=2):
            unit = np.zeros((d, d), dtype=np.int64); unit[r, c] = 1
            real[:, d*r+c] += (gamma*(2*m@unit@m.T-pm4@unit-unit@pm4)).reshape(-1)
            imag[:, d*r+c] += (-2*hh*(pm4@unit-unit@pm4)).reshape(-1)
    assert np.all(real@np.ones(d*d, dtype=np.int64) == 0)
    assert np.all(imag@np.ones(d*d, dtype=np.int64) == 0)
    assert 16*16 % 257 == 256
    rank = modular_rank(real+16*imag)
    assert rank == d*d-1
    gen = (real+1j*imag)/8
    identity_vec = np.eye(d).reshape(-1)
    target = np.ones(d*d)/d
    assert np.max(abs(identity_vec@gen)) < 1e-12
    reward = la.solve(-gen.T+np.outer(identity_vec, target), loss.T.reshape(-1))
    eigenvalues = la.eigvals(gen)
    nonzero = abs(eigenvalues) > 1e-8
    gap = float(-max(eigenvalues[nonzero].real))
    starts = {"basis0": np.diag([1]+[0]*(d-1)), "mixed": np.eye(d)/d,
              "target": np.ones((d, d))/d}
    expectations = {name: float((reward@rho.reshape(-1)).real) for name, rho in starts.items()}
    author = json.loads((AUTHOR/"LOCAL_GAUGE_RECORD_COOLING_RESULTS.json").read_text())
    geo = next(row for row in author["geometries"] if row["shape"] == [2, 2, 2] and not row["periodic"])
    assert hashlib.sha256(json.dumps(words).encode()).hexdigest() == geo["component_states_sha256"]
    assert pair_counts == [p["pairs"] for p in geo["local_controls"]]
    data = next(row for row in author["small_dynamics"] if row["dimension"] == 9)
    assert rank == data["rank_of_8G_mod65537"]
    assert abs(gap-data["numerical_Liouvillian_decay_gap"]) < 1e-11
    errors = {row["initial"]: abs(expectations[row["initial"]]-row["expected_total_jumps"])
              for row in data["results"]}
    assert max(errors.values()) < 1e-11
    # Compare one late row for each preparation, without rerunning all trajectories.
    endpoint_errors = {}
    for row in data["results"]:
        name = row["initial"]
        end = row["transients"][-1]
        rho = (la.expm(end["time"]*gen)@starts[name].reshape(-1)).reshape(d, d)
        u = np.ones(d)/np.sqrt(d)
        values = {"target_infidelity": float((1-u@rho@u).real),
                  "half_trace_distance": float(np.abs(la.eigvalsh(rho-np.ones((d, d))/d)).sum()/2),
                  "jump_intensity": float(np.trace(loss@rho).real)}
        endpoint_errors[name] = max(abs(v-end[k]) for k, v in values.items())
    assert max(endpoint_errors.values()) < 1e-10
    return {"geometry": "open 2x2x2 cube, post-comparison seed 476", "dimension": d,
            "independently_assembled_component": words, "pair_counts": pair_counts,
            "row_major_matrix_unit_superoperator": True,
            "alternative_exact_certificate": {"prime": 257, "image_of_i": 16,
                                               "rank": rank, "target_nullvector_exact": True},
            "gap_numeric": gap, "expected_total_jumps_numeric": expectations,
            "maximum_mean_difference_from_author": max(errors.values()),
            "maximum_late_row_difference_from_author": max(endpoint_errors.values()),
            "coverage_limit": "No periodic 864-state traversal or complete author suite replay."}


def main():
    start = time.monotonic()
    auth = authenticate(AUTHOR/"GAUGE_READOUT_AND_RK_COOLING_AUTHOR_SEAL.json", AUTHOR_HASH)
    pre = authenticate(HERE/"PRE_COMPARISON_SEAL.json", PRE_HASH)
    for stem in ("FRESH_CHARGED_RECORD_LOOP_READOUT", "LOCAL_GAUGE_RECORD_COOLING"):
        assert (AUTHOR/(stem+"_RUN.log")).read_bytes() == (AUTHOR/(stem+"_RESULTS.json")).read_bytes()
        assert not (AUTHOR/(stem+"_RUN.stderr")).read_bytes()
        receipt = json.loads((AUTHOR/(stem+"_RUN_RECEIPT.json")).read_text())
        assert receipt["returncode"] == 0
        assert sha(Path(receipt["command"][-1])) == receipt["script_sha256"]
    result = {"created_utc": datetime.now(timezone.utc).isoformat(), "script_sha256": sha(Path(__file__)),
              "authentication": [auth, pre], "stdout_result_identity_and_receipts": True,
              "readout_sign_comparison": readout(), "analytic_vector_comparison": analytic_identity(),
              "cube_normalization_control": cube(),
              "author_scripts_imported_or_executed": False, "failures": [],
              "runtime_seconds": time.monotonic()-start}
    text = json.dumps(result, indent=2)+"\n"
    (HERE/"COMPARISON_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
