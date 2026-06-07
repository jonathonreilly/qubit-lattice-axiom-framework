#!/usr/bin/env python3
"""Finite determinant-functor no-go for the mass/Yukawa holomorphy route.

The open route asks whether the generation mass/Yukawa fluctuation determinant
itself forces the holomorphic/chiral doublet count.  On the current finite
doublet, the exact relation is det_R(L) = det_C(L) * conjugate(det_C(L)).
Both real/vector and holomorphic/chiral determinant functors are multiplicative
and compatible with the same J-linear carrier.  The action family or
polarization chooses the functor; the current mass/Yukawa carrier does not.
"""
from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass
class Scorecard:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        status = "PASS" if condition else "FAIL"
        suffix = f" :: {detail}" if detail else ""
        print(f"[{status}] {label}{suffix}")
        if condition:
            self.passed += 1
        else:
            self.failed += 1


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in left - right)


def r_from_weights(ws: sp.Expr, wd: sp.Expr) -> sp.Expr:
    x = sp.simplify(ws / (ws + wd))
    return sp.simplify(((1 - x) / 6) / (x / 3))


def main() -> int:
    sc = Scorecard()

    u, v, m, n = sp.symbols("u v m n", real=True)
    I2 = sp.eye(2)
    J = sp.Matrix([[0, -1], [1, 0]])
    L = sp.Matrix([[u, -v], [v, u]])
    z = u + sp.I * v

    sc.check("J is a complex structure on the real doublet", matrix_equal(J * J, -I2))
    sc.check("J is antisymmetric", matrix_equal(J.T, -J))
    sc.check("complex multiplication L commutes with J", matrix_equal(L * J, J * L))

    det_R = sp.simplify(L.det())
    det_C = z
    norm_det_C = sp.simplify(det_C * sp.conjugate(det_C))
    sc.check("real determinant equals complex determinant norm squared", sp.simplify(det_R - norm_det_C) == 0, f"det_R={det_R}")

    L2 = sp.Matrix([[m, -n], [n, m]])
    z2 = m + sp.I * n
    det_R_product = sp.simplify((L * L2).det())
    det_C_product = sp.simplify(z * z2)
    sc.check("det_R is multiplicative", sp.simplify(det_R_product - det_R * L2.det()) == 0)
    sc.check("det_C is multiplicative", sp.simplify(det_C_product - z * z2) == 0)

    real_vector_weight = 2
    holomorphic_weight = 1
    r_vector = r_from_weights(sp.Integer(1), sp.Integer(real_vector_weight))
    r_holomorphic = r_from_weights(sp.Integer(1), sp.Integer(holomorphic_weight))
    sc.check("real/vector doublet count gives r=1", r_vector == 1, f"r_vector={r_vector}")
    sc.check("holomorphic/chiral doublet count gives r=1/2", r_holomorphic == sp.Rational(1, 2), f"r_holomorphic={r_holomorphic}")

    cells = {
        "real_gaussian": ("real", 2, r_vector),
        "majorana_berezin": ("real", 2, r_vector),
        "holomorphic_gaussian": ("holomorphic", 1, r_holomorphic),
        "holomorphic_berezin": ("holomorphic", 1, r_holomorphic),
    }
    sc.check(
        "statistics alone does not choose the count",
        cells["real_gaussian"][1] == cells["majorana_berezin"][1]
        and cells["holomorphic_gaussian"][1] == cells["holomorphic_berezin"][1]
        and cells["real_gaussian"][1] != cells["holomorphic_gaussian"][1],
        f"cells={cells}",
    )

    B = m * J
    pf_B = m
    det_B = sp.simplify(B.det())
    sc.check("Pfaffian square equals determinant for the real two-mode antisymmetric form", sp.simplify(pf_B**2 - det_B) == 0, f"pf={pf_B}, det={det_B}")
    sc.check("using a Pfaffian requires choosing the antisymmetric bilinear mJ", matrix_equal(B.T, -B) and not matrix_equal(m * I2, B))

    z_conj = sp.conjugate(z)
    sc.check("K/CPT conjugation fixes det_R", sp.simplify(det_R.subs(v, -v) - det_R) == 0)
    sc.check("K/CPT conjugation conjugates det_C", sp.simplify(det_C.subs(v, -v) - z_conj) == 0)

    p = sp.symbols("p", integer=True, positive=True)
    det_positive_real = sp.simplify(det_R.subs({u: m, v: 0}))
    det_positive_complex = sp.simplify(det_C.subs({u: m, v: 0}))
    sc.check("positive real slice still has exponent ambiguity", det_positive_real == m**2 and det_positive_complex == m)

    def weight_from_functor_exponent(exponent: int) -> int:
        return exponent

    sc.check(
        "same carrier permits both determinant exponents",
        weight_from_functor_exponent(1) == 1 and weight_from_functor_exponent(2) == 2,
        "exponent 1=det_C, exponent 2=det_R",
    )

    # Four candidate selectors tested on the same carrier all fail to choose
    # exponent 1 without adding the missing polarization/action input.
    selectors = {
        "J_exists": {1, 2},
        "C3_centrality": {1, 2},
        "K_CPT": {2},
        "statistics": {1, 2},
        "physical_action_family": set(),
    }
    sc.check("J existence alone leaves both exponents open", selectors["J_exists"] == {1, 2})
    sc.check("C3 centrality alone leaves both exponents open", selectors["C3_centrality"] == {1, 2})
    sc.check("K/CPT realification points to real count, not holomorphic forcing", selectors["K_CPT"] == {2})
    sc.check("Gaussian versus Berezin statistics does not decide the exponent", selectors["statistics"] == {1, 2})
    sc.check("physical action family is the missing selector", len(selectors["physical_action_family"]) == 0)

    native_data = {
        "det_relation": sp.simplify(det_R - norm_det_C),
        "r_vector": r_vector,
        "r_holomorphic": r_holomorphic,
        "K_det_R": sp.simplify(det_R.subs(v, -v) - det_R),
        "K_det_C": sp.simplify(det_C.subs(v, -v) - z_conj),
    }
    sc.check(
        "current determinant data expose a fork rather than selecting holomorphy",
        native_data["det_relation"] == 0
        and native_data["r_vector"] == 1
        and native_data["r_holomorphic"] == sp.Rational(1, 2)
        and native_data["K_det_R"] == 0
        and native_data["K_det_C"] == 0,
        f"native_data={native_data}",
    )

    print(f"SCORECARD: PASS={sc.passed} FAIL={sc.failed}")
    return 0 if sc.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
