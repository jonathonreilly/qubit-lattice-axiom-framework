"""Author controls for two successive formations in the supplied rotor model.

Build physical legal-hop matrices without importing the ring factorization.
For the cube also enumerate the complete integer Laurent polynomial of the
two-mark squared norm. Numerical fibers are not normalizable physical states.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/second_event_probe.py',)
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import hashlib
import json
import numpy as np
from scipy.linalg import eigh, expm


def graph(name):
    if name == "ring8":
        return [(a, (a + 1) % 8) for a in range(8)], (0, 2, 4, 6)
    if name == "cube":
        return [(a, a ^ (1 << b)) for a in range(8) for b in range(3)
                if a < (a ^ (1 << b))], (0, 3, 5, 6)
    raise ValueError(name)


def charges(number, total=4):
    minus_count = (number - total) // 2
    assert 2 * minus_count == number - total
    result = []
    for occupied in combinations(range(8), number):
        for minus in combinations(occupied, minus_count):
            result.append(tuple(0 if a not in occupied else -1 if a in minus else 1
                                for a in range(8)))
    return sorted(result)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def legal_hops(q, edges):
    """Yield (new charges, integer electric shift), with T coefficient -1."""
    for e, (u, v) in enumerate(edges):
        for source, dest, sign in [(u, v, -1), (v, u, 1)]:
            if q[source] and not q[dest]:
                qq, shift = list(q), [0] * len(edges)
                charge = qq[source]
                qq[source], qq[dest] = 0, charge
                shift[e] = sign * charge
                yield tuple(qq), tuple(shift)


def create(q, edges, edge, sigma):
    u, v = edges[edge]
    if q[u] or q[v]:
        return None
    qq, shift = list(q), [0] * len(edges)
    qq[u], qq[v] = sigma, -sigma
    shift[edge] = sigma
    return tuple(qq), tuple(shift)


def gauss_difference(q, out, shift, edges):
    div = [0] * 8
    for change, (u, v) in zip(shift, edges):
        div[u] += change
        div[v] -= change
    return tuple(div) == tuple(b - a for a, b in zip(q, out))


def effective_paths(q, edges, aset, edge, signs):
    """B=-j Pi1 T P: all one-hop-then-create paths, each coefficient +1."""
    assert all(q[a] for a in aset)
    for mid, hop_shift in legal_hops(q, edges):
        assert sum(mid[a] == 0 for a in aset) == 1
        for sigma in signs:
            formed = create(mid, edges, edge, sigma)
            if formed:
                out, birth_shift = formed
                shift = add(hop_shift, birth_shift)
                assert all(out[a] for a in aset)
                assert gauss_difference(q, out, shift, edges)
                yield out, shift


def target_matrices(name, theta):
    edges, aset = graph(name)
    words = charges(6)
    ix = {q: k for k, q in enumerate(words)}
    W = np.array([sum(q[a] == 0 for a in aset) for q in words])
    sectors = [np.flatnonzero(W == w) for w in range(3)]
    assert list(map(len, sectors)) == [36, 96, 36]
    T = np.zeros((len(words), len(words)), complex)
    for k, q in enumerate(words):
        for out, shift in legal_hops(q, edges):
            assert gauss_difference(q, out, shift, edges)
            T[ix[out], k] -= np.exp(1j * np.dot(theta, shift))
    assert np.linalg.norm(T - T.conj().T) < 1e-12
    A = T[np.ix_(sectors[1], sectors[0])]
    Z = T[np.ix_(sectors[2], sectors[1])] @ A
    M = A.conj().T @ A
    H2, H4 = -M, M @ M - Z.conj().T @ Z / 2
    pwords = [words[i] for i in sectors[0]]
    terminal = charges(8)
    terminal_ix = {q: i for i, q in enumerate(terminal)}
    jumps = {}
    for edge in range(len(edges)):
        for sigma in [-1, 1]:
            j = np.zeros((28, len(sectors[1])), complex)
            for k, i in enumerate(sectors[1]):
                formed = create(words[i], edges, edge, sigma)
                if formed:
                    out, shift = formed
                    j[terminal_ix[out], k] += np.exp(1j * np.dot(theta, shift))
            jumps[edge, sigma] = -j @ A
    gamma = sum(B.conj().T @ B for B in jumps.values())
    gamma_coherent = sum((jumps[e, 1] + jumps[e, -1]).conj().T @
                         (jumps[e, 1] + jumps[e, -1]) for e in range(len(edges)))
    assert np.linalg.norm(gamma - gamma_coherent) < 1e-12
    # Cross-check every jump against an independent direct path enumeration.
    for (edge, sigma), B in jumps.items():
        direct = np.zeros_like(B)
        for col, q in enumerate(pwords):
            for out, shift in effective_paths(q, edges, aset, edge, [sigma]):
                direct[terminal_ix[out], col] += np.exp(1j * np.dot(theta, shift))
        assert np.linalg.norm(direct - B) < 1e-12
    return pwords, H2, H4, jumps, gamma


def first_output(name, theta, pwords, coherent):
    edges, aset = graph(name)
    edge = edges.index((0, 1))
    initial = tuple(int(a in aset) for a in range(8))
    ix = {q: k for k, q in enumerate(pwords)}
    psi = np.zeros(36, complex)
    for out, shift in effective_paths(initial, edges, aset, edge,
                                      [-1, 1] if coherent else [1]):
        psi[ix[out]] += np.exp(1j * np.dot(theta, shift))
    norm2 = float(np.vdot(psi, psi).real)
    assert abs(norm2 - (2 if name == "cube" else 1) * (2 if coherent else 1)) < 1e-12
    return psi / np.sqrt(norm2), norm2


def spectrum_blocks(H, tolerance=1e-9):
    ev, vec = eigh(H)
    groups = []
    for i, value in enumerate(ev):
        if not groups or abs(value - ev[groups[-1][0]]) > tolerance:
            groups.append([i])
        else:
            groups[-1].append(i)
    return [(float(ev[g[0]]), vec[:, g]) for g in groups]


def compress(blocks, operator):
    return sum(v @ (v.conj().T @ operator @ v) @ v.conj().T for _, v in blocks)


def squared_norm_polynomial(paths):
    """Exact Laurent coefficients of J*J on the initial field space."""
    by_charge = defaultdict(lambda: defaultdict(int))
    for q, shift in paths:
        by_charge[q][shift] += 1
    result = defaultdict(int)
    for terms in by_charge.values():
        for left, nl in terms.items():
            for right, nr in terms.items():
                result[tuple(b - a for a, b in zip(left, right))] += nl * nr
    return dict(result)


def polynomial_rows(poly):
    return [{"electric_shift": list(shift), "coefficient": coefficient}
            for shift, coefficient in sorted(poly.items()) if coefficient]


def cube_composition():
    edges, aset = graph("cube")
    initial = tuple(int(a in aset) for a in range(8))
    first_edge = edges.index((0, 1))
    square = [0] * len(edges)
    for u, v in [(0, 2), (2, 6), (6, 4), (4, 0)]:
        e = edges.index((min(u, v), max(u, v)))
        square[e] = 1 if u < v else -1
    square = tuple(square)
    zero = (0,) * len(edges)
    rows = []
    for coherent in [False, True]:
        first = list(effective_paths(initial, edges, aset, first_edge,
                                     [-1, 1] if coherent else [1]))
        first_norm = squared_norm_polynomial(first)
        assert first_norm == {zero: 4 if coherent else 2}
        total = defaultdict(int)
        marked = []
        for edge in range(len(edges)):
            for sigma in [-1, 1]:
                second = [(out, add(shift1, shift2)) for mid, shift1 in first
                          for out, shift2 in effective_paths(mid, edges, aset, edge, [sigma])]
                poly = squared_norm_polynomial(second)
                for shift, coefficient in poly.items():
                    total[shift] += coefficient
                    assert gauss_difference(initial, initial, shift, edges)
                if poly:
                    marked.append({"edge": list(edges[edge]), "sigma": sigma,
                                   "raw_two_mark_norm_polynomial": polynomial_rows(poly)})
        divisor = first_norm[zero]
        prediction = {zero: 8 * divisor, square: divisor, tuple(-x for x in square): divisor}
        actual = dict(total)
        rows.append({"coherent_first": coherent, "first_norm_squared": divisor,
                     "square_shift": list(square), "marked": marked,
                     "raw_total_norm_polynomial": polynomial_rows(actual),
                     "predicted_polynomial_equal": actual == prediction})
    return {"edges": [list(e) for e in edges], "rows": rows}


def ring_controls():
    results = []
    for theta in [0, .17, .41, np.pi / 2, 1.71, 2.7]:
        angle = np.zeros(8)
        angle[-1] = theta
        words, H, H4, jumps, G = target_matrices("ring8", angle)
        adjacent = []
        for q in words:
            b = [j for j in range(4) if q[2 * j + 1]]
            adjacent.append((b[1] - b[0]) % 4 in [1, 3])
        Qadj = np.diag(np.array(adjacent, float))
        identity_error = float(np.linalg.norm(G - 4 * Qadj))
        blocks = spectrum_blocks(H)
        flat = next(v for value, v in blocks if abs(value + 4) < 1e-8)
        Pflat = flat @ flat.conj().T
        Gbar = compress(blocks, G)
        secular_error = float(np.linalg.norm(Gbar - (2 * np.eye(36) + 2 * Pflat)))
        outputs = []
        for coherent in [False, True]:
            psi, _ = first_output("ring8", angle, words, coherent)
            kappa, delta = .7, 1.3
            Fbar = compress(blocks, delta * H4 - .5j * kappa * G)
            rows = []
            for t in [.1, .5, 1., 2.]:
                approximate = float(np.linalg.norm(expm(-1j * t * Fbar) @ psi)**2)
                proposed = .5 * (np.exp(-2 * kappa * t) + np.exp(-4 * kappa * t))
                actual = []
                for eta in [10, 100, 1000]:
                    state = expm(-1j * t * (eta * H + delta * H4 - .5j * kappa * G)) @ psi
                    actual.append({"eta": eta, "survival": float(np.vdot(state, state).real)})
                rows.append({"t": t, "averaged_survival": approximate,
                             "proposed_survival": float(proposed), "finite_eta": actual})
            outputs.append({"coherent": coherent,
                            "flat_weight": float(np.vdot(psi, Pflat @ psi).real),
                            "initial_hazard_over_kappa": float(np.vdot(psi, G @ psi).real),
                            "rows": rows})
        assert identity_error < 1e-10
        results.append({"theta": float(theta), "Gamma_identity_error": identity_error,
                        "distinct_energy_count": len(blocks), "flat_dimension": flat.shape[1],
                        "secular_Gamma_proposed_error": secular_error, "outputs": outputs})
    return results


def cube_controls():
    edges, aset = graph("cube")
    rows = []
    for phi in [0, .37, 1.1, np.pi, 2 * np.pi]:
        theta = np.zeros(len(edges))
        theta[edges.index((0, 2))] = phi
        words, H, H4, jumps, G = target_matrices("cube", theta)
        blocks = spectrum_blocks(H)
        Gbar = compress(blocks, G)
        outputs = []
        for coherent in [False, True]:
            psi, _ = first_output("cube", theta, words, coherent)
            outputs.append({"coherent": coherent,
                            "hazard": float(np.vdot(psi, G @ psi).real),
                            "proposed_hazard": float(8 + 2 * np.cos(phi)),
                            "averaged_initial_hazard": float(np.vdot(psi, Gbar @ psi).real),
                            "H2_mean": float(np.vdot(psi, H @ psi).real),
                            "Gamma_extrema": [float(x) for x in np.linalg.eigvalsh(G)[[0, -1]]],
                            "secular_Gamma_extrema": [float(x) for x in np.linalg.eigvalsh(Gbar)[[0, -1]]]})
        rows.append({"phi": float(phi), "distinct_energy_count": len(blocks),
                     "block_dimensions": [v.shape[1] for _, v in blocks],
                     "commutator_H2_H4_norm": float(np.linalg.norm(H @ H4 - H4 @ H)),
                     "outputs": outputs})
    return rows


def main():
    result = {"status": "author exploratory controls, predictions recorded before this runner",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "cube_exact_composition": cube_composition(),
              "ring_controls": ring_controls(), "cube_controls": cube_controls(),
              "scope": "Supplied unit-rotor model; no finite-spin joint field limit or native axiom derivation."}
    target = Path(__file__).with_name("SECOND_EVENT_PROBE_RESULTS.json")
    assert not target.exists()
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
