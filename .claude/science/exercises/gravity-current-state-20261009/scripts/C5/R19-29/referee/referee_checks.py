"""Independent referee checks for C5 R19-29.

This deliberately uses a bracketed determinant root (not the worker's secant)
and derives the P1 contact identities symbolically before probing the supplied
five-dimensional scalar A1 kernel.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "scripts"))

from a1lib import E1F, NN, TRP, Scalar, gauge, n3, root_scalar_law, ultralocal_seagull  # noqa: E402
import kernels as KR  # noqa: E402


def symbolic_contacts() -> None:
    """Contract abstract real-symmetric Gram data through the two P1 orderings."""
    E, w, s, x_ee, x_en, x_nn = sp.symbols(
        "E w s Gamma_ee Gamma_en Gamma_nn", nonzero=True, real=True
    )

    # Amplitude coefficients relative to spatial e1 and nn amplitudes.
    e_a = e_b = 1
    g0_a = 2 * s**2 * (E - w) / E**2
    g0_b = -2 * s**2 * (E + w) / E**2
    gn_a = 2 * s * (E - w) / E
    gn_b = 2 * s * (E + w) / E

    def bubble(a1, b1, a2, b2, gram):
        return sp.simplify(-(a1 * a2 * gram / (E - w) + b1 * b2 * gram / (E + w)))

    results = {
        "Pi(e1,g0)": bubble(e_a, e_b, g0_a, g0_b, x_en),
        "Pi(e1,gn)": bubble(e_a, e_b, gn_a, gn_b, x_en),
        "Pi(g0,g0)": bubble(g0_a, g0_b, g0_a, g0_b, x_nn),
        "Pi(g0,gn)": bubble(g0_a, g0_b, gn_a, gn_b, x_nn),
        "Pi(gn,gn)": bubble(gn_a, gn_b, gn_a, gn_b, x_nn),
    }
    print("symbolic P1 contacts")
    for key, value in results.items():
        print(f"  {key} = {sp.factor(value)}")


def exact_poles() -> None:
    law, _ = root_scalar_law()
    scalar = Scalar(law, m=0.3, N=40)
    t4 = np.array([1.0, 0.0, 0.0, 0.0])
    nx = np.r_[0.0, n3]
    h00 = np.outer(t4, t4)
    h0n = 0.5 * (np.outer(t4, nx) + np.outer(nx, t4))
    basis = [E1F, h00, h0n, NN, TRP]
    q = 0.02
    qvec = q * n3

    def kmat(w):
        p = np.r_[-w, qvec]
        kernel = KR.kernel(0 * KR.Ab[0], KR.Beh, p)
        return KR.s_EH * np.array(
            [[np.einsum("ij,ijkl,kl->", a, kernel, b) for b in basis] for a in basis]
        )

    def tensor_overlap(coeff):
        tensor = sum(c * b for c, b in zip(coeff, basis))
        return abs(np.einsum("ij,ij->", tensor, E1F)) / (
            np.linalg.norm(tensor) * np.linalg.norm(E1F)
        )

    print("full 5x5 A1 determinant roots (Brent brackets in y=(w^2-q^2)/(eps*q^2))")
    for lam in (0.0, 0.01):
        sea = ultralocal_seagull(scalar, lam)

        def pi(w):
            return scalar.block(qvec, w, basis, seagull=sea)

        on_shell_pols = [E1F, gauge(t4, q, qvec), gauge(nx, q, qvec)]
        p_on = scalar.block(qvec, q, on_shell_pols, seagull=sea)
        schur = p_on[0, 1:] @ np.linalg.solve(p_on[1:, 1:], p_on[0, 1:])
        predicted = (p_on[0, 0] - schur) / q**2

        for eps in (1.0e-6, 1.0e-7):
            def matrix_y(y):
                w2 = q**2 * (1 + eps * y)
                return kmat(np.sqrt(w2)) - eps * pi(np.sqrt(w2))

            def det_y(y):
                return np.linalg.det(matrix_y(y) / (eps * q**2))

            # The physical root is tightly bracketed around the first-order
            # Schur prediction, then certified by its TT overlap.
            half_width = 2.0e-5
            left, right = predicted - half_width, predicted + half_width
            while det_y(left) * det_y(right) > 0:
                half_width *= 2
                left, right = predicted - half_width, predicted + half_width
                if half_width > 0.02:
                    raise RuntimeError("failed to bracket physical determinant root")
            root = brentq(det_y, left, right, xtol=1e-14, rtol=1e-13)
            _, _, vh = np.linalg.svd(matrix_y(root))
            overlap = tensor_overlap(vh[-1])
            print(
                f"  lam={lam:g} eps={eps:.0e}: exact={root:+.9e} "
                f"Schur={predicted:+.9e} delta={root-predicted:+.2e} "
                f"TT-overlap={overlap:.8f}"
            )


if __name__ == "__main__":
    symbolic_contacts()
    exact_poles()
