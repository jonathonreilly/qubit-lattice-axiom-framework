#!/usr/bin/env python3
"""Bounded check for the C_3 generation circulant.

For M(a,b) = a I + b C + conj(b) C^2, b -> conj(b) is a real-orthogonal
generation-transposition similarity. Spectral functionals on this
conjugate-symmetric surface are therefore conjugation-even, so this route does
not generate a conjugation-odd Berry/eta selector. The positive control confirms
the detector is sensitive when the conjugate-symmetric relation is broken.

Reproduces seven checks:
  1. multiset-even: M(b) eigenvalues real; the set is invariant under
     b -> conj(b); det M is real and even in Im(b).
  2. transposition similarity (exact): (I_L (x) P) H(b) (I_L (x) P) = H(conj b),
     P the 1<->2 generation transposition (real-orthogonal).
  3. Berry curl = 0 for ANY kernel g (symbolic): A = sum_k g(lam_k) d lam_k is
     an exact differential, so its curl vanishes identically.
  4. det real under arg(b) winding: det M(|b| e^{i theta}) is real for all
     theta, so arg det has no continuous Berry winding.
  5. positive control: spectral asymmetry eta = 0 for the conjugate-symmetric
     coupling, nonzero for the c-independent deformation.
  6. transpose-preserving real mixing keeps the spectrum even even when the
     explicit P witness is broken.
  7. i(C - C^2) is the arg(b) tangent inside the same conjugate-symmetric
     family.
"""

from __future__ import annotations

import numpy as np
from sympy import Function, cos, pi, simplify, sin, symbols

AUDIT_TIMEOUT_SEC = 120

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


# C_3 shift and transposition on the generation triplet.
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
C2 = C @ C
I3 = np.eye(3, dtype=complex)
P = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)  # swap 1<->2


def M(a: complex, b: complex) -> np.ndarray:
    return a * I3 + b * C + np.conj(b) * C2


def M_chi(a: complex, b: complex, c: complex) -> np.ndarray:
    return a * I3 + b * C + c * C2  # c independent of conj(b)


def main() -> int:
    section("Check 1 - multiset-even under b -> conj(b) (symbolic)")
    a, b1, b2 = symbols("a b1 b2", real=True)
    # real circulant eigenvalues lam_k = a + 2 Re(b w^k), b = b1 + i b2
    lam = [a + 2 * (b1 * cos(2 * pi * k / 3) - b2 * sin(2 * pi * k / 3)) for k in range(3)]
    detM = simplify(lam[0] * lam[1] * lam[2])
    det_odd = simplify(detM - detM.subs(b2, -b2))
    check("det M is even in Im(b) (odd part = 0)", det_odd == 0, f"odd={det_odd}")
    # under b -> conj(b): b2 -> -b2 maps {lam_0, lam_1, lam_2} onto itself (1<->2)
    swap_ok = simplify(lam[1].subs(b2, -b2) - lam[2]) == 0 and simplify(lam[2].subs(b2, -b2) - lam[1]) == 0
    check("eigenvalue multiset invariant under b -> conj(b) (k: 1<->2)", swap_ok)

    section("Check 2 - real-orthogonal transposition similarity (exact)")
    check("P is a real orthogonal permutation", np.allclose(P @ P.T, I3) and np.allclose(P.imag, 0))
    check("P C P = C^2 (P reflects the C_3 orbit)", np.allclose(P @ C @ P, C2))
    aN, bN = 1.0, 0.5 + 0.3j
    diff_gen = np.max(np.abs(P @ M(aN, bN) @ P - M(aN, np.conj(bN))))
    check("P M(b) P = M(conj b) on the generation triplet", diff_gen < 1e-12, f"max={diff_gen:.1e}")
    # full coupled operator H(b) = D (x) I3 + I_L (x) (i M(b)); I_L (x) P fixes its spectrum
    S = np.roll(np.eye(4), 1, axis=0)
    D = S - S.T  # real antisymmetric (anti-Hermitian) spatial operator
    IL = np.eye(4, dtype=complex)
    ILP = np.kron(IL, P)

    def H(b: complex) -> np.ndarray:
        return np.kron(D, I3) + np.kron(IL, 1j * M(aN, b))

    diff_full = np.max(np.abs(ILP @ H(bN) @ ILP - H(np.conj(bN))))
    check("(I_L (x) P) H(b) (I_L (x) P) = H(conj b)", diff_full < 1e-12, f"max={diff_full:.1e}")

    # The exact orthogonal similarity above already proves identical spectra.
    # A naive np.sort_complex comparison FAILS here on a lexsort-on-real-part
    # artifact (near-degenerate real parts mis-order); round-then-sort confirms
    # the true machine-zero multiset match.
    def spec(op: np.ndarray) -> np.ndarray:
        e = np.round(np.linalg.eigvals(op), 6)
        return np.array(sorted(e, key=lambda z: (z.real, z.imag)))

    sp_diff = float(np.max(np.abs(spec(H(bN)) - spec(H(np.conj(bN))))))
    check("spectrum of H(b) equals spectrum of H(conj b) (round-then-sort)", sp_diff < 1e-5,
          f"max={sp_diff:.1e}")

    section("Check 3 - Berry curl = 0 for ANY kernel g (symbolic)")
    g = Function("g")
    lam_b = [a + 2 * (b1 * cos(2 * pi * k / 3) - b2 * sin(2 * pi * k / 3)) for k in range(3)]
    A_b1 = sum(g(lk) * lk.diff(b1) for lk in lam_b)
    A_b2 = sum(g(lk) * lk.diff(b2) for lk in lam_b)
    curl = simplify(A_b2.diff(b1) - A_b1.diff(b2))
    check("curl( sum_k g(lam_k) d lam_k ) = 0 for arbitrary g", curl == 0, f"curl={curl}")

    section("Check 4 - det M real under arg(b) winding (no Berry winding)")
    max_im = 0.0
    for t in np.linspace(0, 2 * np.pi, 64, endpoint=False):
        bt = 0.7071 * np.exp(1j * t)  # Koide radius |b|/a = 1/sqrt(2)
        d = np.linalg.det(M(1.0, bt))
        max_im = max(max_im, abs(d.imag) / max(abs(d), 1e-12))
    check("det M(|b| e^{i theta}) is real for all theta", max_im < 1e-9, f"max|Im|/|det|={max_im:.1e}")

    section("Check 5 - positive control: detector is sensitive")

    def eta(H_op: np.ndarray, tol: float = 1e-9) -> int:
        re = np.linalg.eigvals(H_op).real
        return int(np.sum(re > tol) - np.sum(re < -tol))

    H_ret = np.kron(D, I3) + np.kron(IL, 1j * M(1.0, 0.5 + 0.3j))
    H_chi = np.kron(D, I3) + np.kron(IL, 1j * M_chi(1.0, 0.5 + 0.3j, 0.3 + 0.7j))
    e_ret, e_chi = eta(H_ret), eta(H_chi)
    check("conjugate-symmetric coupling: spectral asymmetry eta = 0", e_ret == 0, f"eta={e_ret}")
    check("c-independent deformation: spectral asymmetry eta != 0", e_chi != 0, f"eta={e_chi}")
    chi_is_nonherm = not np.allclose(M_chi(1.0, 0.5 + 0.3j, 0.3 + 0.7j),
                                     M_chi(1.0, 0.5 + 0.3j, 0.3 + 0.7j).conj().T)
    check("the control has coeff(C^2) != conj(coeff(C)) (non-Hermitian)", chi_is_nonherm)

    section("Check 6 - over-determination: reality forces even-ness even when P breaks")
    bb = 0.5 + 0.3j
    # deterministic O(1) real-symmetric structure that fully couples space (x) generation
    Wbase = np.cos(np.arange(144.0)).reshape(12, 12)
    Wmix = Wbase + Wbase.T  # real symmetric
    I4P = np.kron(np.eye(4), P)
    pbreak = float(np.max(np.abs(Wmix @ I4P - I4P @ Wmix)))
    check("W_mix explicitly breaks the transposition lift ([W_mix, I (x) P] != 0)", pbreak > 0.1,
          f"norm={pbreak:.2f}")

    def Oop(b: complex) -> np.ndarray:
        return np.kron(np.eye(4), M(1.0, b)) + Wmix  # M(conj b) = M(b)^T, Wmix^T = Wmix

    o_diff = float(np.max(np.abs(spec(Oop(bb)) - spec(Oop(np.conj(bb))))))
    check("spec(O(b)) = spec(O(conj b)) with P broken (reality: O(conj b) = O(b)^T)", o_diff < 1e-6,
          f"max={o_diff:.1e}")

    section("Check 7 - the odd generator i(C - C^2) is only the arg(b) tangent")
    G = 1j * (C - C2)
    check("i(C - C^2) is Hermitian", np.allclose(G, G.conj().T))
    check("i(C - C^2) is P-odd (P G P = -G)", np.allclose(P @ G @ P, -G))
    eps = 0.07
    check("M(b) + eps i(C - C^2) = M(b + i eps) (reparametrizes b; stays conjugate-symmetric)",
          np.allclose(M(1.0, bb) + eps * G, M(1.0, bb + 1j * eps)))

    section("Summary")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("Conjugation-odd Berry coefficient vanishes on the conjugate-symmetric")
    print("C_3 circulant and transpose-preserving real extensions.")
    print(f"Positive control eta_chi={e_chi}.")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
