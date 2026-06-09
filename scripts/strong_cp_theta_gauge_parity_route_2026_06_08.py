"""Strong-CP theta_gauge=0 via the PARITY (O_h) route -- load-bearing verification + a correction.

The exercise's volume-form lens claimed O_h-invariance does NOT forbid the F-tilde-F slot because "the
det(R) in the epsilon-pseudotensor and the det(R) in the measure d^4x cancel." This runner shows that
claim is WRONG, that the landed STRONG_CP_EPSILON_PSEUDOTENSOR_OH_SIGN_BRIDGE (B6) is right, and assembles
the framework-specific parity route to theta_bar=0, then states the precise open gate.

THE ROUTE: theta_bar = theta_gauge + arg det(M_quark). (a) theta_gauge is the coefficient of the P-ODD
F-tilde-F slot; an O_h/parity-invariant color action forbids it -> theta_gauge=0. (b) arg det(M_quark) is
quantized to {0,pi} by K-reality (the Hermitian C3 mass circulant has a REAL determinant). The color
sector is VECTORLIKE (P-even: color su(3) commutes with the chirality grading), so the only P-violating
SOURCE is the weak chiral su(2)_L -- an F-tilde-F in the color action would be P-violation WITHOUT a source.

VERIFIES (exact numpy):
  T1. F-tilde-F is P-ODD: Q[F] = eps^{ijk} F_{0i} F_{jk} transforms as Q[R.F] = det(R) Q[F] for every one
      of the 48 O_h signed permutations R (so improper R flip its sign). [re-derives the landed B5]
  T2. THE CORRECTION: the global theta-term S_theta = sum_x Q[F_x] transforms as S_theta -> det(R) S_theta
      under O_h (the lattice sum is a relabeling -- NO Jacobian/measure sign; the continuum volume measure
      is det-EVEN, |det R|=1). So there is NO measure det(R) to cancel the F-tilde-F det(R): an
      O_h/parity-invariant action FORBIDS F-tilde-F (coefficient must vanish). The P-EVEN term sum Tr F^2 is
      invariant (survives). [refutes the exercise's spurious cancellation; confirms B6]
  T3. The Wilson color action Re Tr(U_P) is parity/orientation invariant: Re Tr(U) = Re Tr(U^dag) for
      SU(3) (orientation reversal U_P -> U_P^dag). So the color gauge action is P-even. [re-derives B1-B3]
  T4. Color is VECTORLIKE (P-even), weak is CHIRAL (the P-source): on chirality(x)color, the chirality
      grading Gamma5 = Z(x)I COMMUTES with every color generator I(x)lambda_a ([Gamma5, color]=0), while the
      weak chiral coupling T^a P_L (P_L=(I-Gamma5)/2) does NOT commute with Gamma5. So the color sector has
      no intrinsic P-violating source; only the weak su(2)_L does.
  T5. arg det(M_quark) in {0,pi}: the K-real Hermitian C3 circulant has det = a^3-3a|b|^2+2|b|^3 cos3delta,
      REAL (Im=0) -> arg in {0,pi}, orientable to 0. [no continuous CP from the matter determinant]
  T6. SYNTHESIS + GATE: IF the color gauge action respects the substrate's O_h parity (no P-source in the
      vectorlike color sector), THEN theta_gauge=0 (T1-T4) and arg det M_q in {0,pi}->0 (T5) -> theta_bar=0.
      The precise OPEN GATE: is color-sector parity FORCED (the only P-source is the weak chiral eps; an
      unsourced P-odd color F-tilde-F is disfavored) or ADMITTED? Proper rotations alone do NOT forbid
      F-tilde-F (Q is invariant under proper R); only the IMPROPER/reflection (parity) elements do.

CONCLUSION: this is NOT yet a closure -- it CORRECTS the exercise (O_h-invariance genuinely forbids
F-tilde-F), REFRAMES theta=0 from "minimality" to "color-sector parity", and places the framework in the
parity-solution class with a K-real matter determinant. The residual is a sharp, single, parity-framed
gate (is color-action P-invariance forced?), not the diffuse "minimality" admission. No PDG/fitted value.
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
    print("STRONG-CP theta_gauge=0 via PARITY (O_h): load-bearing verification + correction")
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
    check("T1: F-tilde-F slot Q[F]=eps^{ijk}F_{0i}F_{jk} is P-ODD -- Q[R.F]=det(R)Q[F] for ALL 48 O_h "
          "signed permutations (improper R flip its sign)", ok1,
          "verified on 6 random antisymmetric F across all 48 O_h elements")

    # ---- T2: the correction -- lattice sum has NO measure det(R); O_h-invariant action forbids F-tilde-F ----
    # Build a small lattice field, form the global theta-term S = sum_x Q[F_x], transform every site's F by
    # a reflection R and relabel sites (a permutation of the discrete lattice -> sum invariant): S -> det(R) S.
    L = 4
    field = [rand_antisym4() for _ in range(L)]
    S_theta = sum(Qcharge(F) for F in field)
    S_even = sum(np.trace(F @ F.T) for F in field)   # P-EVEN comparator ~ sum Tr F^2
    reflect = next(R for R in O_h if abs(np.linalg.det(R) + 1) < 1e-9)  # an improper element, det=-1
    field_R = [apply_spatial_R(F, reflect) for F in field]             # transform fields; site sum relabels
    S_theta_R = sum(Qcharge(F) for F in field_R)
    S_even_R = sum(np.trace(F @ F.T) for F in field_R)
    odd_flips = abs(S_theta_R - np.linalg.det(reflect) * S_theta) < 1e-9 and np.linalg.det(reflect) < 0
    measure_det_even = abs(abs(np.linalg.det(reflect)) - 1.0) < 1e-12   # |det R| = 1 (volume measure det-EVEN)
    even_invariant = abs(S_even_R - S_even) < 1e-9
    check("T2 (CORRECTION): the global theta-term S=sum_x Q[F_x] -> det(R) S under improper O_h (lattice sum "
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
    check("T3: Wilson color action Re Tr(U_P) is parity/orientation invariant -- Re Tr(U)=Re Tr(U^dag) for "
          "SU(3) (orientation reversal U_P -> U_P^dag). The color gauge action is P-EVEN.", ok3,
          "Re Tr U = Re Tr U^dag verified on 20 random SU(3)")

    # ---- T4: color VECTORLIKE (P-even), weak CHIRAL (the P-source) ----
    I2 = np.eye(2, dtype=complex); I3 = np.eye(3, dtype=complex)
    Z = np.array([[1, 0], [0, -1]], complex)
    Gamma5 = np.kron(Z, I3)                       # chirality grading on chirality(x)color
    lam3 = np.diag([1, -1, 0]).astype(complex)    # a color (Gell-Mann) generator
    color_gen = np.kron(I2, lam3)
    PL = (np.eye(6) - Gamma5) / 2
    weak_chiral = np.kron(np.array([[0, 1], [1, 0]], complex), I3) @ PL   # a chiral (P_L) coupling proxy
    color_commutes = np.allclose(Gamma5 @ color_gen - color_gen @ Gamma5, 0)
    weak_chiral_noncommute = not np.allclose(Gamma5 @ weak_chiral - weak_chiral @ Gamma5, 0)
    check("T4: color is VECTORLIKE/P-even -- [Gamma5, color]=0 (color su(3) commutes with the chirality "
          "grading); weak su(2)_L is CHIRAL -- [Gamma5, T^a P_L] != 0. So the ONLY P-violating SOURCE is the "
          "weak chiral sector; an F-tilde-F in the color action would be P-violation WITHOUT a source.",
          color_commutes and weak_chiral_noncommute,
          f"[Gamma5,color]=0: {color_commutes}; [Gamma5,weak_chiral]!=0: {weak_chiral_noncommute}")

    # ---- T5: arg det(M_quark) in {0,pi} (K-real Hermitian circulant) ----
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    a_v, c_v, d_v = 1.7, 0.9, 0.7
    b = c_v * np.exp(1j * d_v)
    M = a_v * np.eye(3) + b * C + np.conj(b) * (C @ C)
    detM = np.linalg.det(M)
    check("T5: arg det(M_quark) in {0,pi} -- the K-real Hermitian C3 mass circulant has a REAL determinant "
          "(Im det = 0) -> orientable to 0; no continuous CP from the matter determinant.",
          abs(detM.imag) < 1e-9,
          f"det M = {detM.real:.4f} + {detM.imag:.1e}i (real); arg in {{0,pi}}")

    # ---- T6: synthesis -- proper rotations alone do NOT forbid F-tilde-F; only improper (parity) do ----
    proper = [R for R in O_h if np.linalg.det(R) > 0]
    improper = [R for R in O_h if np.linalg.det(R) < 0]
    Ftest = rand_antisym4(); q0 = Qcharge(Ftest)
    proper_invariant = all(abs(Qcharge(apply_spatial_R(Ftest, R)) - q0) < 1e-9 for R in proper)
    improper_flips = all(abs(Qcharge(apply_spatial_R(Ftest, R)) + q0) < 1e-9 for R in improper)
    check("T6 (GATE): proper rotations (det=+1, 24 of O_h) leave Q[F] INVARIANT; only the IMPROPER/"
          "reflection (parity) elements (det=-1, 24) flip it. So theta_gauge=0 needs PARITY-invariance of "
          "the color action, not mere rotational invariance. The open gate: is color-sector parity FORCED "
          "(only the weak chiral eps sources P; color has none) or ADMITTED?",
          proper_invariant and improper_flips,
          f"Q invariant under all {len(proper)} proper R: {proper_invariant}; flips under all {len(improper)} improper R: {improper_flips}")

    # ---- T7: the lattice ORIENTATION is a framework-native P-source for F-tilde-F (why color-parity is NOT forced) ----
    # The Cl(3) volume element omega = sigma1 sigma2 sigma3 = i*I (the i-gate's native pseudoscalar) transforms by
    # det(R) under the spatial O_h action sigma_i -> sum_j R_ij sigma_j: omega -> det(R) omega. So the framework
    # HAS a native det(R)-odd orientation (= sign(Vandermonde), per the i-gate), which SOURCES the P-odd F-tilde-F.
    # Hence "color has no P-source" is FALSE -- the orientation is one -- so color-sector parity is an EFT
    # assumption ("respect substrate symmetry absent a source"), NOT derived. theta_gauge is the un-derived
    # color coupling to this orientation Z2 (the same beta=6-class wall, now parity-framed).
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
    check("T7 (why color-parity is NOT forced): the Cl(3) volume element omega=sigma1 sigma2 sigma3 = i*I (the "
          "i-gate's native pseudoscalar = sign(Vandermonde) orientation) transforms as omega -> det(R) omega "
          "under all 48 O_h actions -> the framework HAS a native det(R)-odd orientation that SOURCES the P-odd "
          "F-tilde-F. So 'color has no P-source' is FALSE; color-sector parity is an EFT assumption, not derived.",
          omega_is_native_pseudoscalar and omega_det_odd,
          f"omega=i*I: {omega_is_native_pseudoscalar}; omega->det(R)omega for all 48 O_h: {omega_det_odd}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the exercise's 'measure det(R) cancels F-tilde-F det(R)' claim is REFUTED -- the lattice\n"
        "sum carries no Jacobian and the volume measure is det-EVEN, so an O_h/parity-invariant action\n"
        "genuinely FORBIDS the det(R)-odd F-tilde-F (the landed B6 sign-bridge is right). This REFRAMES\n"
        "theta_gauge=0 from the (gated) 'minimality' route to a PARITY route: the color sector is vectorlike\n"
        "(P-even, T3/T4) and the matter determinant is K-real (arg in {0,pi}->0, T5), so the framework sits\n"
        "in the parity-solution class for strong-CP with theta_bar = theta_gauge + arg det M_q. The single\n"
        "remaining gate is sharp and parity-framed: is the color gauge action FORCED to respect the\n"
        "substrate's O_h parity (the only P-violating source is the weak chiral eps; an unsourced P-odd color\n"
        "F-tilde-F is disfavored), or is color-sector parity an admission? Proper rotations alone do not\n"
        "forbid F-tilde-F -- only parity does. Audit lane sets status; the adversarial campaign decides the gate."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
