#!/usr/bin/env python3
"""Class-A exact verification for the source note

    docs/DOPED_FLUX_RESPONSE_NO_UNIFORM_SIGN_REGION_BOUNDED_THEOREM_NOTE_2026-06-12.md

Statuses are pipeline-derived; the audit lane grades.

Run: python3 scripts/frontier_doped_flux_response_alternation_fate_2026_06_12.py
"""
import sys

import numpy as np


NS = (8, 10, 12, 14, 16)
MS = (0.0, 0.4)
TS = (0.3, 0.6)
MUS = (0.25, 0.5, 1.0, 1.5)
DEGEN_TOL = 1.0e-12


pass_count = 0
fail_count = 0


def check(name, condition, detail):
    global pass_count, fail_count
    if bool(condition):
        pass_count += 1
        status = "PASS"
    else:
        fail_count += 1
        status = "FAIL"
    print(f"[{status}] {name}: {detail}")


def build_hamiltonian(n, mass, phi, gauge="uniform"):
    if n % 2 != 0:
        raise ValueError("staggered ring requires even N")

    h = np.zeros((n, n), dtype=np.complex128)
    for site in range(n):
        h[site, site] = mass * ((-1.0) ** site)

    if gauge == "uniform":
        phase = np.exp(1j * phi / n)
        for site in range(n):
            nxt = (site + 1) % n
            h[site, nxt] += -phase
            h[nxt, site] += -np.conjugate(phase)
    elif gauge == "boundary":
        for site in range(n - 1):
            h[site, site + 1] += -1.0
            h[site + 1, site] += -1.0
        phase = np.exp(1j * phi)
        h[n - 1, 0] += -phase
        h[0, n - 1] += -np.conjugate(phase)
    else:
        raise ValueError(f"unknown gauge: {gauge}")

    return h


def derivative_matrices(n, gauge="uniform"):
    v = np.zeros((n, n), dtype=np.complex128)
    w = np.zeros((n, n), dtype=np.complex128)

    if gauge == "uniform":
        for site in range(n):
            nxt = (site + 1) % n
            v[site, nxt] += -1j / n
            v[nxt, site] += 1j / n
            w[site, nxt] += 1.0 / (n * n)
            w[nxt, site] += 1.0 / (n * n)
    elif gauge == "boundary":
        v[n - 1, 0] += -1j
        v[0, n - 1] += 1j
        w[n - 1, 0] += 1.0
        w[0, n - 1] += 1.0
    else:
        raise ValueError(f"unknown gauge: {gauge}")

    return v, w


def fermi(energies, temp, mu_ch):
    x = (np.asarray(energies, dtype=np.float64) - mu_ch) / temp
    out = np.empty_like(x, dtype=np.float64)
    positive = x >= 0.0
    exp_neg = np.exp(-x[positive])
    out[positive] = exp_neg / (1.0 + exp_neg)
    exp_pos = np.exp(x[~positive])
    out[~positive] = 1.0 / (1.0 + exp_pos)
    return out


def fermi_prime(energies, temp, mu_ch):
    occ = fermi(energies, temp, mu_ch)
    return -(occ * (1.0 - occ)) / temp


def fermi_divided_difference(energies, temp, mu_ch):
    occ = fermi(energies, temp, mu_ch)
    divided = np.empty((len(energies), len(energies)), dtype=np.float64)
    for row, erow in enumerate(energies):
        for col, ecol in enumerate(energies):
            delta = erow - ecol
            if abs(delta) <= DEGEN_TOL:
                divided[row, col] = fermi_prime(np.array([0.5 * (erow + ecol)]), temp, mu_ch)[0]
            else:
                divided[row, col] = (occ[row] - occ[col]) / delta
    return divided


def omega_value(n, mass, temp, mu_ch, phi, gauge="uniform"):
    energies = np.linalg.eigvalsh(build_hamiltonian(n, mass, phi, gauge=gauge))
    return float(-temp * np.sum(np.logaddexp(0.0, -(energies - mu_ch) / temp)))


def omega_second(n, mass, temp, mu_ch, gauge="uniform"):
    h0 = build_hamiltonian(n, mass, 0.0, gauge=gauge)
    energies, vecs = np.linalg.eigh(h0)
    v, w = derivative_matrices(n, gauge=gauge)
    v_e = vecs.conjugate().T @ v @ vecs
    w_e = vecs.conjugate().T @ w @ vecs

    occ = fermi(energies, temp, mu_ch)
    divided = fermi_divided_difference(energies, temp, mu_ch)

    hf_term = np.sum(occ * np.real(np.diag(w_e)))
    sos_term = np.sum(divided * (np.abs(v_e) ** 2))
    return float(np.real(hf_term + sos_term))


def omega_second_fd(n, mass, temp, mu_ch, step=1.0e-3):
    plus = omega_value(n, mass, temp, mu_ch, step)
    zero = omega_value(n, mass, temp, mu_ch, 0.0)
    minus = omega_value(n, mass, temp, mu_ch, -step)
    return (plus - 2.0 * zero + minus) / (step * step)


def sign_char(value):
    if value > 0.0:
        return "+"
    if value < 0.0:
        return "-"
    return "0"


def classify_pattern(values):
    signs = tuple(sign_char(value) for value in values)
    alternating = all(signs[idx] != signs[idx - 1] and "0" not in (signs[idx], signs[idx - 1])
                      for idx in range(1, len(signs)))
    uniform_positive = all(sign == "+" for sign in signs)
    uniform_negative = all(sign == "-" for sign in signs)

    if alternating:
        label = "sign-alternating"
    elif uniform_positive:
        label = "uniform-positive"
    elif uniform_negative:
        label = "uniform-negative"
    else:
        label = "mixed-nonalternating"

    return "".join(signs), label


print("SCOPE: abelian U(1) flux, free rings, finite T, mu_ch grid; "
      "the alternation-fate table is the datum; NOT claimed: b3, non-abelian, "
      "gauge self-energy (named gap), thermodynamic-limit asymptotics, d=3. "
      "(X3-import) used nowhere.")

print("\nX2b THE TABLE: exact Omega_second(0)")
table = {}
for mu_ch in MUS:
    for mass in MS:
        for temp in TS:
            row = []
            for n in NS:
                value = omega_second(n, mass, temp, mu_ch)
                table[(n, mass, temp, mu_ch)] = value
                row.append(f"N={n}: {value:+.16e}")
            print(f"mu_ch={mu_ch:.2f} m={mass:.1f} T={temp:.1f} | " + " | ".join(row))

print("\nX2c ALTERNATION FATE: full tested grid")
expected_patterns = {
    (0.0, 0.3, 0.25): ("-+--+", "mixed-nonalternating"),
    (0.0, 0.3, 0.5): ("+-+-+", "sign-alternating"),
    (0.0, 0.3, 1.0): ("+--+-", "mixed-nonalternating"),
    (0.0, 0.3, 1.5): ("-++--", "mixed-nonalternating"),
    (0.0, 0.6, 0.25): ("-+-+-", "sign-alternating"),
    (0.0, 0.6, 0.5): ("--+-+", "mixed-nonalternating"),
    (0.0, 0.6, 1.0): ("+-++-", "mixed-nonalternating"),
    (0.0, 0.6, 1.5): ("++-++", "mixed-nonalternating"),
    (0.4, 0.3, 0.25): ("-+-++", "mixed-nonalternating"),
    (0.4, 0.3, 0.5): ("+-+-+", "sign-alternating"),
    (0.4, 0.3, 1.0): ("+--+-", "mixed-nonalternating"),
    (0.4, 0.3, 1.5): ("-++-+", "mixed-nonalternating"),
    (0.4, 0.6, 0.25): ("-+-+-", "sign-alternating"),
    (0.4, 0.6, 0.5): ("--+-+", "mixed-nonalternating"),
    (0.4, 0.6, 1.0): ("+-++-", "mixed-nonalternating"),
    (0.4, 0.6, 1.5): ("++-++", "mixed-nonalternating"),
}
observed_patterns = {}
for mass in MS:
    for temp in TS:
        for mu_ch in MUS:
            values = [table[(n, mass, temp, mu_ch)] for n in NS]
            signs, label = classify_pattern(values)
            observed_patterns[(mass, temp, mu_ch)] = (signs, label)
            formatted_values = ", ".join(f"{value:+.6e}" for value in values)
            print(
                f"m={mass:.1f} T={temp:.1f} mu_ch={mu_ch:.2f} "
                f"signs={signs} classification={label} values=[{formatted_values}]"
            )

mean_abs_by_mu = {
    mu_ch: float(np.mean([abs(table[(n, 0.4, 0.3, mu_ch)]) for n in NS]))
    for mu_ch in MUS
}
max_abs_by_mu = {
    mu_ch: float(np.max([abs(table[(n, 0.4, 0.3, mu_ch)]) for n in NS]))
    for mu_ch in MUS
}
trend_report = "; ".join(
    f"mu_ch={mu_ch:.2f}: mean_abs={mean_abs_by_mu[mu_ch]:.6e}, "
    f"max_abs={max_abs_by_mu[mu_ch]:.6e}"
    for mu_ch in MUS
)
print("\nX2d MAGNITUDE TREND: " + trend_report)

fd_cases = (
    ("N=8 m=0.4 T=0.3 mu_ch=0.5", 8, 0.4, 0.3, 0.5),
    ("N=10 m=0.4 T=0.3 mu_ch=1.0", 10, 0.4, 0.3, 1.0),
)
for label, n, mass, temp, mu_ch in fd_cases:
    analytic = omega_second(n, mass, temp, mu_ch)
    finite_difference = omega_second_fd(n, mass, temp, mu_ch)
    rel = abs(analytic - finite_difference) / max(abs(finite_difference), 1.0e-15)
    check(
        "X2a analytic-vs-FD " + label,
        rel < 1.0e-4,
        f"analytic={analytic:+.16e}, fd={finite_difference:+.16e}, rel={rel:.3e}, gate rel<1e-4",
    )

for key in sorted(expected_patterns):
    mass, temp, mu_ch = key
    expected_signs, expected_label = expected_patterns[key]
    observed_signs, observed_label = observed_patterns[key]
    check(
        f"X2c alternation fate m={mass:.1f} T={temp:.1f} mu_ch={mu_ch:.2f}",
        observed_signs == expected_signs and observed_label == expected_label,
        f"observed signs={observed_signs}, classification={observed_label}; "
        f"expected signs={expected_signs}, classification={expected_label}",
    )

uniform_labels = {"uniform-positive", "uniform-negative"}
uniform_region_absent = all(label not in uniform_labels for _, label in observed_patterns.values())
check(
    "X2d no uniform-sign N-sequence on full tested grid",
    uniform_region_absent,
    "no (m,T,mu_ch) in the tested grid has a uniform N-sequence; "
    + trend_report,
)

ph_diffs = []
for n in NS:
    for mass in MS:
        for temp in TS:
            for mu_ch in MUS:
                positive = omega_second(n, mass, temp, mu_ch)
                negative = omega_second(n, mass, temp, -mu_ch)
                ph_diffs.append(abs(positive - negative))
max_ph_diff = max(ph_diffs)
check(
    "X2e particle-hole relation Omega_second(mu_ch)=Omega_second(-mu_ch)",
    max_ph_diff < 1.0e-10,
    f"max_abs_diff over table grid={max_ph_diff:.3e}, gate <1e-10",
)

gauge_cases = (
    (12, 0.4, 0.3, 0.5),
    (16, 0.0, 0.6, 0.5),
)
gauge_diffs = []
for n, mass, temp, mu_ch in gauge_cases:
    uniform = omega_second(n, mass, temp, mu_ch, gauge="uniform")
    boundary = omega_second(n, mass, temp, mu_ch, gauge="boundary")
    gauge_diffs.append(abs(uniform - boundary))
max_gauge_diff = max(gauge_diffs)
check(
    "X2f gauge invariance at mu_ch=0.5",
    max_gauge_diff < 1.0e-10,
    f"max_abs_diff uniform-vs-boundary gauge={max_gauge_diff:.3e}, gate <1e-10",
)

hot_values = []
for n in NS:
    for mass in MS:
        for mu_ch in (0.0,) + MUS:
            hot_values.append(abs(omega_second(n, mass, 50.0, mu_ch)))
max_hot = max(hot_values)
check(
    "X2f T=50 kills the response",
    max_hot < 1.0e-12,
    f"max_abs Omega_second over N,m,mu_ch grid at T=50 is {max_hot:.3e}, gate <1e-12",
)

zero_doping_refs = (
    ("zero-doping predecessor value, N=8 m=0.4 T=0.3 mu_ch=0", 8, -2.4525291422948042e-02),
    ("zero-doping predecessor value, N=10 m=0.4 T=0.3 mu_ch=0", 10, 8.6569530669922956e-03),
)
for label, n, expected in zero_doping_refs:
    observed = omega_second(n, 0.4, 0.3, 0.0)
    diff = abs(observed - expected)
    check(
        "X2f mu_ch=0 cross-reference " + label,
        diff < 1.0e-10,
        f"observed={observed:+.16e}, reference={expected:+.16e}, abs_diff={diff:.3e}, gate <1e-10",
    )

print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")
if fail_count:
    sys.exit(1)
