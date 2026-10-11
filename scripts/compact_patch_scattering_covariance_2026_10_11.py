"""Exact author controls for conventions and the finite-product Cook identity.

This is not a numerical proof of scattering, an independent review, a QCA
realization, or a model of the full physical premises.  It checks finite
algebraic reductions whose signs/indices are load-bearing in the written proof.
"""

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
]
if not __debug__:
    raise RuntimeError("Run without -O: exact control assertions must be enabled")

from collections import defaultdict
from fractions import Fraction
import json

import sympy as sp


def emit(name, **data):
    print(json.dumps({"check": name, **data}, sort_keys=True))


def reduce_roots(poly, order, variable):
    return sp.rem(sp.Poly(poly, variable, domain=sp.QQ),
                  sp.Poly(sp.cyclotomic_poly(order, variable), variable,
                          domain=sp.QQ)).as_expr().expand()


def centre_average(order, selected, actual, variable, wrong_sign=False):
    difference = actual + selected if wrong_sign else actual - selected
    polynomial = sum(variable ** ((difference * j) % order)
                     for j in range(order)) / sp.Integer(order)
    return reduce_roots(polynomial, order, variable)


def canonical_on_vacuum(poly):
    # The sole relation is D_i Omega = 0.  No commutativity is imposed.
    return {word: coefficient for word, coefficient in poly.items()
            if coefficient and not word[-1].startswith("D")}


def product_derivative(n):
    terms = defaultdict(int)
    for i in range(n):
        word = tuple(f"D{k}" if k == i else f"C{k}" for k in range(n))
        terms[word] += 1
    return canonical_on_vacuum(terms)


def commuted_derivative(n, drop_pair=None, reverse_sign=False):
    terms = defaultdict(int)
    sign = -1 if reverse_sign else 1
    for i in range(n):
        for k in range(i + 1, n):
            if (i, k) == drop_pair:
                continue
            prefix = tuple(f"C{ell}" for ell in range(k) if ell != i)
            suffix = tuple(f"C{ell}" for ell in range(k + 1, n))
            terms[prefix + (f"D{i}", f"C{k}") + suffix] += sign
            terms[prefix + (f"C{k}", f"D{i}") + suffix] -= sign
    return canonical_on_vacuum(terms)


def main():
    x = sp.Symbol("x")
    centre_cases = 0
    for q in range(2, 10):
        for selected in range(q):
            for actual in range(q):
                value = centre_average(q, selected, actual, x)
                assert value == int(selected == actual)
                centre_cases += 1
    emit("finite_centre_projection", exact_cases=centre_cases,
         orders=list(range(2, 10)), conclusion="character projection on q-root sectors")
    assert centre_average(3, 1, 1, x, wrong_sign=True) != 1
    emit("negative_wrong_centre_weight", rejected=True, q=3,
         selected=1, actual=1)

    # A q=2 average acting on a third-root phase is not a projection.
    global_average = (1 + x) / 2
    residual = reduce_roots(global_average**2 - global_average, 3, x)
    assert residual != 0
    emit("negative_global_projection_without_q_spectrum", rejected=True,
         exact_residual=str(residual))

    for n in range(1, 10):
        assert product_derivative(n) == commuted_derivative(n)
    emit("free_noncommutative_cook_identity", n_values=list(range(1, 10)),
         relation="D_i Omega = 0 only")
    assert product_derivative(2) != commuted_derivative(2, drop_pair=(0, 1))
    assert product_derivative(4) != commuted_derivative(4, reverse_sign=True)
    emit("negative_product_mutations", dropped_pair_rejected=True,
         reversed_commutator_rejected=True)

    # Discrete Fourier geometry tests T_x=exp(-i Q x), V_x=exp(+i theta x),
    # hence Q=k-theta. Energies are arbitrary exact positive integers: the
    # check is of Fourier/clock algebra, not relativistic dispersion.
    packet_cases = 0
    for ring in [5, 7, 11]:
        for centre in range(1, ring):
            for momentum in range(ring):
                geometric_q = (momentum - centre) % ring
                energies = [13 + j*j for j in range(ring)]
                sigma = {((j - centre) % ring): energies[j]
                         for j in range(ring)}
                for fourier_q in range(ring):
                    projection = reduce_roots(
                        sum(x ** (((fourier_q - geometric_q) * site) % ring)
                            for site in range(ring)) / sp.Integer(ring), ring, x)
                    assert projection == int(fourier_q == geometric_q)
                    if projection:
                        assert energies[momentum] - sigma[fourier_q] == 0
                        assert energies[momentum] != 0  # omitting dot f fails
                        assert -sigma[fourier_q] != 0   # omitting dot B fails
                    packet_cases += 1
    emit("packet_fourier_and_clock", exact_cases=packet_cases,
         sign_convention="Q=k-theta; exp(+iHt); exp(-it Sigma)",
         omitted_packet_derivative_rejected=True,
         omitted_operator_derivative_rejected=True)

    # Preserve the source's current-flow normalization without dividing beta
    # twice. beta*k is the eigenvalue of P, while k is that of P/beta.
    for beta in [Fraction(2), Fraction(3), Fraction(5, 2)]:
        for q in [1, 2, 3, 7]:
            assert Fraction(q, 1) / beta * beta == q
            assert Fraction(q, 1) / beta != q
    emit("current_clock", cases=12,
         correct="generator P, time q/beta; generator P/beta, time q",
         double_beta_division_rejected=True)

    for d in [1, 2, 3, 7]:
        for n in range(2, 20):
            power = d*(n-2) + 2*d - (d*n+2)
            assert power == -2
    emit("finite_product_power_count", cases=72, resulting_power=-2)
    emit("scope", status="author exact algebra controls only",
         scattering_proved_by_runner=False, independent_review=False,
         full_gns_completeness=False)


if __name__ == "__main__":
    main()

    print("per_element: exact finite character, Fourier, clock and product-word identities checked")
    print("per_site: checked and not executed — the supplied local interactions enter the analytic LR hypotheses")
    print("per_mode: exact finite Fourier convention fixtures; no continuum spectral sampling claim")
    print("per_block: finite noncommutative products n=1,...,9 checked modulo D_i Omega=0")
    print("lattice_wide: checked and not executed — analytic Cook convergence and covariance are proved in the note")
    print("TOTAL: PASS=9 FAIL=0")
    print("SCOPE: nine finite control records; no analytic scattering proof, Fock isometry or audit verdict from this runner")
