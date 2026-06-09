"""Strong-CP theta_gauge parity gate: finite O_h checks plus a correction.

The runner verifies the narrow gate landed in the companion source note:

* the topological-charge slot Q[F] = eps^{ijk} F_{0i} F_{jk} is det(R)-odd
  under spatial O_h;
* the lattice sum and volume measure do not supply a second det(R) sign, so a
  parity-invariant color action would forbid this slot;
* proper rotations alone do not forbid it;
* the local Cl(3) pseudoscalar line has the same det(R) character, so the
  baseline does not derive zero coupling to the lattice-orientation character.

This does not solve strong CP, derive the gauge action, or transfer mass-side
determinant-reality facts to theta_gauge.
"""
from __future__ import annotations
import numpy as np
import itertools

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def signed_perms_3():
    """The 48 elements of O_h as 3x3 signed permutation matrices."""
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            out.append(R)
    return out


def Qcharge(F):
    """Topological-charge density slot Q[F] = eps^{ijk} F_{0i} F_{jk}, spatial i,j,k in {1,2,3}
    (0 = Euclidean time). F is a 4x4 antisymmetric matrix."""
    eps = np.zeros((3, 3, 3))
    for i, j, k in itertools.permutations(range(3)):
        sign = np.sign((j - i) * (k - i) * (k - j))
        eps[i, j, k] = sign
    s = 0.0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                s += eps[i, j, k] * F[0, i + 1] * F[j + 1, k + 1]
    return s


def apply_spatial_R(F, R):
    """Transform the 4x4 antisymmetric F by a spatial O(3) R (time index 0 fixed): F'_{mu nu} with spatial
    block rotated by R, time-space block F_{0i} rotated as a spatial vector."""
    Fp = np.array(F, dtype=float)
    # spatial-spatial block F_{jk}, j,k in 1..3 -> R F R^T
    sp = F[1:4, 1:4]
    Fp[1:4, 1:4] = R @ sp @ R.T
    # time-space F_{0i} -> R F_{0i}
    Fp[0, 1:4] = R @ F[0, 1:4]
    Fp[1:4, 0] = -Fp[0, 1:4]
    return Fp


def main() -> int:
    print("STRONG-CP parity gate: O_h sign checks plus measure-cancellation correction")
    print("=" * 80)
    rng = np.random.default_rng(0)
    O_h = signed_perms_3()

    # ---- T1: F-tilde-F is P-odd (Q[R.F] = det(R) Q[F]) ----
    def rand_antisym4():
        A = rng.standard_normal((4, 4)); return A - A.T
    ok1 = True
    for _ in range(6):
        F = rand_antisym4()
        q0 = Qcharge(F)
        for R in O_h:
            ok1 = ok1 and abs(Qcharge(apply_spatial_R(F, R)) - np.linalg.det(R) * q0) < 1e-9
    check("F-tilde-F slot Q[F]=eps^{ijk}F_{0i}F_{jk} is P-odd: Q[R.F]=det(R)Q[F] for all 48 O_h "
          "signed permutations (improper R flip its sign)", ok1,
          "verified on 6 random antisymmetric F across all 48 O_h elements")

    # ---- T2: the correction -- lattice sum has NO measure det(R); O_h-invariant action forbids F-tilde-F ----
    # Build a small lattice field, form the global theta-term S = sum_x Q[F_x], transform every site's F by
    # a reflection R and relabel sites (a permutation of the discrete lattice -> sum invariant): S -> det(R) S.
    L = 4
    field = [rand_antisym4() for _ in range(L)]
    S_theta = sum(Qcharge(F) for F in field)
    S_even = sum(np.trace(F @ F.T) for F in field)   # P-even control ~ sum Tr F^2
    reflect = next(R for R in O_h if abs(np.linalg.det(R) + 1) < 1e-9)  # an improper element, det=-1
    field_R = [apply_spatial_R(F, reflect) for F in field]             # transform fields; site sum relabels
    S_theta_R = sum(Qcharge(F) for F in field_R)
    S_even_R = sum(np.trace(F @ F.T) for F in field_R)
    odd_flips = abs(S_theta_R - np.linalg.det(reflect) * S_theta) < 1e-9 and np.linalg.det(reflect) < 0
    measure_det_even = abs(abs(np.linalg.det(reflect)) - 1.0) < 1e-12   # |det R| = 1 (volume measure det-EVEN)
    even_invariant = abs(S_even_R - S_even) < 1e-9
    check("measure-cancellation correction: S=sum_x Q[F_x] -> det(R) S under improper O_h (lattice sum "
          "is a relabeling; |det R|=1 so the measure is det-EVEN and supplies NO cancelling sign) -> an "
          "O_h/parity-invariant action FORBIDS F-tilde-F. The P-EVEN sum Tr F^2 is invariant (survives). "
          "[refutes the exercise's measure-cancellation; confirms B6]",
          odd_flips and measure_det_even and even_invariant,
          f"S_theta: {S_theta:.4f} -> {S_theta_R:.4f} (= -S_theta); |det R|={abs(np.linalg.det(reflect)):.0f}; "
          f"S_even invariant: {even_invariant}")

    # ---- T3: Wilson color action Re Tr U_P is parity/orientation invariant ----
    def rand_su3():
        A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Q, R_ = np.linalg.qr(A)
        Q = Q @ np.diag(np.exp(-1j * np.angle(np.diag(R_))))
        return Q / np.linalg.det(Q) ** (1 / 3)
    ok3 = True
    for _ in range(20):
        U = rand_su3()
        ok3 = ok3 and abs(np.real(np.trace(U)) - np.real(np.trace(U.conj().T))) < 1e-9
    check("Wilson color action Re Tr(U_P) is parity/orientation invariant: Re Tr(U)=Re Tr(U^dag) for "
          "SU(3) (orientation reversal U_P -> U_P^dag). The color gauge action is P-EVEN.", ok3,
          "Re Tr U = Re Tr U^dag verified on 20 random SU(3)")

    # ---- Color vectorlike contrast; this is context, not a gauge-action derivation. ----
    I2 = np.eye(2, dtype=complex); I3 = np.eye(3, dtype=complex)
    Z = np.array([[1, 0], [0, -1]], complex)
    Gamma5 = np.kron(Z, I3)                       # chirality grading on chirality(x)color
    lam3 = np.diag([1, -1, 0]).astype(complex)    # a color (Gell-Mann) generator
    color_gen = np.kron(I2, lam3)
    PL = (np.eye(6) - Gamma5) / 2
    weak_chiral = np.kron(np.array([[0, 1], [1, 0]], complex), I3) @ PL   # a chiral (P_L) coupling proxy
    color_commutes = np.allclose(Gamma5 @ color_gen - color_gen @ Gamma5, 0)
    weak_chiral_noncommute = not np.allclose(Gamma5 @ weak_chiral - weak_chiral @ Gamma5, 0)
    check("color is vectorlike in this finite chirality-color test: [Gamma5, color]=0, while a chiral weak "
          "proxy does not commute with Gamma5. This is a contrast check, not a proof of the full gauge action.",
          color_commutes and weak_chiral_noncommute,
          f"[Gamma5,color]=0: {color_commutes}; [Gamma5,weak_chiral]!=0: {weak_chiral_noncommute}")

    # ---- Mass-side determinant context; this does not transfer to theta_gauge. ----
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    a_v, c_v, d_v = 1.7, 0.9, 0.7
    b = c_v * np.exp(1j * d_v)
    M = a_v * np.eye(3) + b * C + np.conj(b) * (C @ C)
    detM = np.linalg.det(M)
    check("mass-side context: the Hermitian C3 circulant determinant is real (Im det = 0), "
          "so its argument is in {0, pi}; this does not transfer to theta_gauge.",
          abs(detM.imag) < 1e-9,
          f"det M = {detM.real:.4f} + {detM.imag:.1e}i (real); arg in {{0,pi}}")

    # ---- Proper rotations alone do not forbid F-tilde-F; improper parity elements do. ----
    proper = [R for R in O_h if np.linalg.det(R) > 0]
    improper = [R for R in O_h if np.linalg.det(R) < 0]
    Ftest = rand_antisym4(); q0 = Qcharge(Ftest)
    proper_invariant = all(abs(Qcharge(apply_spatial_R(Ftest, R)) - q0) < 1e-9 for R in proper)
    improper_flips = all(abs(Qcharge(apply_spatial_R(Ftest, R)) + q0) < 1e-9 for R in improper)
    check("parity gate: proper rotations (det=+1, 24 of O_h) leave Q[F] invariant; only the improper/"
          "reflection (parity) elements (det=-1, 24) flip it. So theta_gauge=0 needs PARITY-invariance of "
          "the color action, not mere rotational invariance. The open gate is whether a parity-even color "
          "action is independently derived.",
          proper_invariant and improper_flips,
          f"Q invariant under all {len(proper)} proper R: {proper_invariant}; flips under all {len(improper)} improper R: {improper_flips}")

    # ---- The lattice orientation line has the same det(R) character as F-tilde-F. ----
    # The Cl(3) volume element omega = sigma1 sigma2 sigma3 = i*I (the i-gate's native pseudoscalar) transforms by
    # det(R) under the spatial O_h action sigma_i -> sum_j R_ij sigma_j: omega -> det(R) omega.
    # This does not create a gauge action term by itself. It blocks only the shortcut from
    # vectorlike color to "there is no determinant-odd structure available."
    sx = np.array([[0, 1], [1, 0]], complex)
    sy = np.array([[0, -1j], [1j, 0]], complex)
    sz = np.array([[1, 0], [0, -1]], complex)
    sig = [sx, sy, sz]
    omega = sx @ sy @ sz  # = i*I_2 (Cl(3) pseudoscalar)
    omega_is_native_pseudoscalar = np.allclose(omega, 1j * I2)
    omega_det_odd = True
    for R in O_h:
        sig_R = [sum(R[i, j] * sig[j] for j in range(3)) for i in range(3)]
        omega_R = sig_R[0] @ sig_R[1] @ sig_R[2]
        omega_det_odd = omega_det_odd and np.allclose(omega_R, np.linalg.det(R) * omega)
    check("orientation gate: the Cl(3) volume element omega=sigma1 sigma2 sigma3 = i*I transforms as "
          "omega -> det(R) omega under all 48 O_h actions. This shows a native determinant-odd line exists; "
          "it does not by itself derive a gauge action coupling.",
          omega_is_native_pseudoscalar and omega_det_odd,
          f"omega=i*I: {omega_is_native_pseudoscalar}; omega->det(R)omega for all 48 O_h: {omega_det_odd}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the measure-cancellation objection is refuted: the lattice sum carries no Jacobian and\n"
        "the volume measure is det-even, so a parity-invariant action would forbid the det(R)-odd F-tilde-F\n"
        "slot. Proper rotations alone do not forbid it. The local Cl(3) pseudoscalar line has the same\n"
        "det(R) character, so zero coupling to the lattice-orientation character is not derived here.\n"
        "This is a sharpened gauge-action parity gate, not a strong-CP closure."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
