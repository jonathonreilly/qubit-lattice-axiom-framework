"""Direct two-hop record graph versus the proposed one-birth ring spectrum.

Exploratory author check. No imported model builder or claim of a laboratory-
time field limit. Each Fourier fiber is a finite representation of the full
integer-flux rotor sector, not a normalizable fixed-flux-angle preparation.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import hashlib
import json
import numpy as np
from scipy.linalg import eigh


def physical_words(L):
    """All P words after one birth: N=L+2, Q=L, one minus record."""
    words = []
    for occupied_b in combinations(range(L), 2):
        occupied = sorted(list(range(0, 2 * L, 2)) + [2 * b + 1 for b in occupied_b])
        for minus in occupied:
            q = [0] * (2 * L)
            for a in occupied:
                q[a] = -1 if a == minus else 1
            words.append(tuple(q))
    return sorted(words)


def hop(q, source, dest):
    assert q[source] and not q[dest]
    qq = list(q)
    charge = qq[source]
    qq[source], qq[dest] = 0, charge
    # E_(2L-1) is the independent Gauss-law circulation coordinate.
    change = charge if source == 0 and dest == len(q) - 1 else 0
    if source == len(q) - 1 and dest == 0:
        change = -charge
    return tuple(qq), change


def direct_terms(L, words):
    """Integer Laurent coefficients of -P T Pi_1 T P, from legal hops."""
    ix = {q: i for i, q in enumerate(words)}
    terms = defaultdict(int)
    for col, q in enumerate(words):
        for a in range(0, 2 * L, 2):
            for b in [(a - 1) % (2 * L), (a + 1) % (2 * L)]:
                if q[b]:
                    continue
                mid, k1 = hop(q, a, b)
                for c in [(a - 1) % (2 * L), (a + 1) % (2 * L)]:
                    if mid[c]:
                        out, k2 = hop(mid, c, a)
                        terms[ix[out], col, k1 + k2] -= 1
    return dict(terms)


def factors(L, words):
    """Label the B holes and the cyclic charge word starting at A site zero."""
    holes = sorted(combinations(range(L), L - 2))
    hx = {h: i for i, h in enumerate(holes)}
    labels = []
    for q in words:
        h = tuple(i for i in range(L) if q[2 * i + 1] == 0)
        sequence = [c for c in q if c]
        labels.append((hx[h], sequence.index(-1)))
    assert len(set(labels)) == len(words)
    return holes, labels


def factor_terms(L, words):
    """Independent vacancy-chain construction with a charge-word shift at the cut."""
    holes, labels = factors(L, words)
    lookup = {label: i for i, label in enumerate(labels)}
    hx = {h: i for i, h in enumerate(holes)}
    N = L + 2
    terms = defaultdict(int)
    for col, (hi, r) in enumerate(labels):
        h = set(holes[hi])
        terms[col, col, 0] = -2 * len(h)
        for source in h:
            for target in [(source - 1) % L, (source + 1) % L]:
                if target in h:
                    continue
                new_h = tuple(sorted((h - {source}) | {target}))
                new_r, exponent = r, 0
                if source == L - 1 and target == 0:
                    # The hole crosses A0 to the right; the first charge
                    # moves through the circulation cut and the word rotates.
                    new_r = (r - 1) % N
                    exponent = -1 if r == 0 else 1
                elif source == 0 and target == L - 1:
                    new_r = (r + 1) % N
                    exponent = 1 if r == N - 1 else -1
                row = lookup[hx[new_h], new_r]
                terms[row, col, exponent] -= 1
    return dict(terms)


def matrix(terms, size, theta):
    H = np.zeros((size, size), complex)
    for (r, c, k), coefficient in terms.items():
        H[r, c] += coefficient * np.exp(1j * k * theta)
    assert np.max(np.abs(H - H.conj().T)) < 1e-13
    return H


def proposed_spectrum(L, theta):
    N, h = L + 2, L - 2
    result = []
    for s in range(N):
        alpha = (L * theta + 2 * np.pi * s) / N
        momenta = (2 * np.pi * np.arange(L) + alpha + np.pi * (h - 1)) / L
        for filled in combinations(range(L), h):
            result.append(-2 * h - 2 * sum(np.cos(momenta[a]) for a in filled))
    return np.sort(result)


def formation_outputs(L, words):
    """First resolved/coherent mark on (A0,B0), after A0 moves to B_(L-1)."""
    ix = {q: i for i, q in enumerate(words)}
    q = [1 if a % 2 == 0 else 0 for a in range(2 * L)]
    q[2 * L - 1] = 1
    q[1] = -1
    resolved = np.zeros(len(words), complex)
    resolved[ix[tuple(q)]] = 1
    q[0], q[1] = -1, 1
    other = np.zeros(len(words), complex)
    other[ix[tuple(q)]] = 1
    return resolved, (resolved + other) / np.sqrt(2)


def main():
    rows = []
    for L in range(3, 9):
        words = physical_words(L)
        direct = direct_terms(L, words)
        factored = factor_terms(L, words)
        assert direct == factored, (L, set(direct.items()) ^ set(factored.items()))
        for (r, c, k), value in direct.items():
            assert direct.get((c, r, -k)) == value
        exact = {"L": L, "sites": 2 * L, "P_dimension": len(words),
                 "integer_Laurent_entries": len(direct),
                 "word_and_vacancy_factorization_exact": True}
        angles = []
        for theta in [0, np.pi / 11, np.pi / 3, np.pi]:
            H = matrix(direct, len(words), theta)
            ev = eigh(H, eigvals_only=True, driver="evd")
            expected = proposed_spectrum(L, theta)
            error = float(np.max(np.abs(ev - expected)))
            assert error < 2e-12, (L, theta, error)
            angles.append({"theta": float(theta), "max_spectrum_error": error,
                           "bottom": float(ev[0]), "top": float(ev[-1])})
        H = matrix(direct, len(words), 0)
        ev, vectors = eigh(H, driver="evd")
        assert ev[1] - ev[0] > 1e-7
        expected_ground = -2 * (L - 2) - 4 * np.cos(np.pi / L)
        assert abs(ev[0] - expected_ground) < 1e-12
        outputs = []
        for instrument, psi, factor in zip(["resolved", "coherent"], formation_outputs(L, words), [1, 2]):
            mean = float(np.vdot(psi, H @ psi).real)
            variance = float(np.vdot(H @ psi, H @ psi).real - mean**2)
            weight = float(abs(np.vdot(vectors[:, 0], psi))**2)
            prediction = factor * 4 * np.sin(np.pi / L)**2 / (L**2 * (L + 2))
            assert abs(mean + 2 * (L - 2)) < 2e-12
            assert abs(variance - 2) < 2e-12
            assert abs(weight - prediction) < 1e-12, (L, instrument, weight, prediction)
            outputs.append({"instrument": instrument, "mean_H2": mean,
                            "variance_H2": variance, "ground_weight_theta_zero": weight,
                            "ground_weight_formula": float(prediction)})
        exact.update({"angles": angles, "ground_energy_theta_zero_formula": float(expected_ground),
                      "formation_outputs": outputs})
        rows.append(exact)
    out = {"status": "author exploratory calculation, all stated assertions passed",
           "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "model": "unit rotor, 2L ring, first-birth P sector, supplied Gauss background",
           "rows": rows,
           "scope": "Exact factorization coefficients; floating spectral and overlap controls. No laboratory-time rotor/field convergence or subsequent-formation law is proved by this runner."}
    target = Path(__file__).with_name("RING_SPECTRUM_PROBE_RESULTS.json")
    assert not target.exists()
    target.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
