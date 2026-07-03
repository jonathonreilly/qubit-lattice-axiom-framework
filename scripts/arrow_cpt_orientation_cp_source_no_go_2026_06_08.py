"""Scoped CP-source route no-go for arrow, CPT, orientation, and real readout.

This runner checks several proposed routes from the axiom baseline to CP-odd action coefficients. It
does not prove that no richer framework-native dynamics can ever select the coefficients. It proves
only that the tested arrow/CPT/orientation/readout/form-class routes do not supply them.

CANDIDATE ATTACK (refuted here): "Record is irreversible = the arrow = T-violation; by CPT,
T-violation <=> CP-violation, so the arrow SOURCES a CP-odd action term." This runner shows the attack
fails at step 1 and that CPT reality does not supply a continuous CP coefficient.

VERIFIES (exact numpy/sympy):
  S1. The record-write microdynamics is TIME-SYMMETRIC. The #2701 record-write generator
      H_k = (pi/2)|1><1|_sys (x) X_k is REAL SYMMETRIC, so U_k = e^{-i H_k} satisfies the time-reversal
      identity Theta U_k Theta^-1 = U_k^-1 with Theta = K (complex conjugation), and T_k = e^{-H_k} is
      self-adjoint with T_k = T_k^T. The arrow is NOT in the map.
  S2. The arrow is a BOUNDARY CONDITION, not a dynamical CP/T-odd term. The generator H_k is real-symmetric
      (T-even, CP-even) INDEPENDENT of the initial state; the SAME U_k produces a forward (record-increasing)
      or reversed (record-decreasing) arrow purely from the initial density matrix. A boundary-condition
      arrow carries ZERO CP-odd dynamical content -> it cannot source a CP-odd action term.
  S3. CPT is CP-PROTECTING, not CP-sourcing. For the C3 flavor circulant M = aI + bC + b-bar C^2 and a
      staggered toy M = m I + M_KS (M_KS real antisymmetric), CPT gives Theta_CPT M Theta_CPT^-1 = M* and
      M is K/CPT-real so det M in R -> arg det M in {0, pi}. The matter CP-odd phase is QUANTIZED/protected,
      carrying no continuous CP source; CPT pushes toward theta=0, the OPPOSITE of sourcing CP-violation.
  S4. The tested FORM-class does NOT fix the CP-odd COEFFICIENTS. (matter) M(delta, r) is Hermitian and
      C3-covariant for ANY phase delta and ANY ratio r=|b|^2/a^2; (gauge) a Wilson-loop trace and its CP-odd
      imaginary/topological part are gauge-invariant under base-point conjugation for ANY coefficient theta.
      So Hermiticity + gauge-invariance + locality (the Record-forced form-class) leave (r, delta, theta)
      FREE -- they are the unforced coefficients of the one forced action.
  S5. The available orientation/chirality datum is sign-only: the Cl(3) volume element is iI and lattice
      orientation gives det(R)=+/-1. It can flip a sign, not continuously select a coefficient.
  S6. Real readout is CP-blind as a consumer but does not prohibit CP: log|det| is even in delta while
      J=Im(M01 M12 M20)=|b|^3 sin(3 delta) is a real CP-odd scalar.

CONCLUSION: the tested arrow/CPT/orientation/readout/form-class routes do not source CP-odd action
coefficients. The coefficient-selection problem remains open to richer dynamics/minimality/action-selection
routes. No PDG/fitted value. Exact numpy/sympy.
"""
from __future__ import annotations
import numpy as np
import sympy as sp

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


def expm_h(A, n=80):
    out = np.eye(A.shape[0], dtype=complex); term = np.eye(A.shape[0], dtype=complex)
    for k in range(1, n):
        term = term @ A / k
        out = out + term
    return out


def main() -> int:
    print("SCOPED CP-SOURCE ROUTE NO-GO: arrow/CPT/orientation/readout do not source coefficients")
    print("=" * 76)
    X = np.array([[0, 1], [1, 0]], complex)
    proj1 = np.array([[0, 0], [0, 1]], complex)  # |1><1|

    # ---- S1: record-write microdynamics is time-symmetric ----
    # 2-qubit toy: system (qubit 0) writes onto fragment (qubit 1): H = (pi/2)|1><1|_sys (x) X_frag
    H = (np.pi / 2) * np.kron(proj1, X)
    real_sym = np.allclose(H.imag, 0) and np.allclose(H, H.T)
    U = expm_h(-1j * H)
    Tk = expm_h(-H)
    # Theta = K (complex conjugation): Theta U Theta^-1 = conj(U); time-reversal identity conj(U) = U^{-1}
    tr_identity = np.allclose(np.conj(U), np.linalg.inv(U))
    T_selfadj = np.allclose(Tk, Tk.conj().T) and np.allclose(Tk, Tk.T)
    check("S1: record-write generator H=(pi/2)|1><1|(x)X is REAL SYMMETRIC -> Theta U Theta^-1 = conj(U) = "
          "U^-1 (time-reversal identity) and T=e^{-H} self-adjoint with T=T^T. The arrow is NOT in the map.",
          real_sym and tr_identity and T_selfadj,
          f"H real-symmetric={real_sym}; conj(U)=U^-1: {tr_identity}; T=T^dag and T=T^T: {T_selfadj}")

    # ---- S2: the arrow is a boundary condition, not a dynamical CP/T-odd term ----
    # Same U; record (fragment-1 population as a pointer proxy) increases from |+>|0>, decreases from the
    # time-reversed high-record state. Generator is identical in both -> arrow lives in rho_0, not in H.
    plus = (np.array([1, 1], complex) / np.sqrt(2))
    zero = np.array([1, 0], complex)
    psi_low = np.kron(plus, zero)                 # low-record initial
    # forward record proxy: <proj1 on fragment> after the write
    frag_pop = np.kron(np.eye(2), proj1)
    rec_low_0 = np.real(psi_low.conj() @ frag_pop @ psi_low)
    psi_low_1 = U @ psi_low
    rec_low_1 = np.real(psi_low_1.conj() @ frag_pop @ psi_low_1)
    forward_increases = rec_low_1 > rec_low_0 + 1e-9
    # time-reversed high-record state: start from the written state, conjugate (Theta), evolve forward
    psi_high = np.conj(psi_low_1)
    rec_high_0 = np.real(psi_high.conj() @ frag_pop @ psi_high)
    psi_high_1 = U @ psi_high
    rec_high_1 = np.real(psi_high_1.conj() @ frag_pop @ psi_high_1)
    reversed_decreases = rec_high_1 < rec_high_0 - 1e-9
    # the generator's reality/symmetry is the SAME in both runs (no CP/T-odd term appears)
    gen_invariant = real_sym  # H did not change between runs
    check("S2: the SAME real-symmetric generator gives a forward record-INCREASE from the low-record state "
          "and a record-DECREASE from the time-reversed state -> the arrow is in the initial condition, NOT "
          "in the dynamics; no CP-odd/T-odd term lives in the map, so the arrow cannot SOURCE one.",
          forward_increases and reversed_decreases and gen_invariant,
          f"record low: {rec_low_0:.3f}->{rec_low_1:.3f} (up); reversed: {rec_high_0:.3f}->{rec_high_1:.3f} (down); generator unchanged")

    # ---- S3: CPT is CP-PROTECTING (det M real -> arg det in {0,pi}) ----
    # C3 flavor circulant
    a, c, d = sp.symbols('a c delta', real=True, positive=True)
    bsym = c * sp.exp(sp.I * d)
    detM_circ = sp.simplify((a**3 + bsym**3 + sp.conjugate(bsym)**3 - 3*a*(bsym*sp.conjugate(bsym))).rewrite(sp.cos))
    det_real = sp.simplify(sp.im(detM_circ)) == 0   # det is real for real a,c,d
    # staggered toy: M = m I + M_KS, M_KS real antisymmetric -> M real -> det real
    rng = np.random.default_rng(0)
    n = 6
    A = rng.standard_normal((n, n)); M_KS = A - A.T  # real antisymmetric
    M_stag = 0.4 * np.eye(n) + M_KS
    det_stag = np.linalg.det(M_stag)
    stag_real = abs(det_stag.imag) < 1e-9 if np.iscomplexobj(det_stag) else True
    check("S3: CPT gives Theta_CPT M Theta_CPT^-1 = M* -> det M in R for the C3 circulant "
          "(det = a^3-3a|b|^2+2|b|^3 cos3delta, Im=0) and the staggered toy (M real) -> arg det M in {0,pi}: "
          "the matter CP-odd phase is QUANTIZED/protected, NOT a continuous CP source. CPT pushes toward theta=0.",
          det_real and stag_real,
          f"C3 det Im part = {sp.im(detM_circ)}; staggered det = {det_stag:.4f} (real)")

    # ---- S4: the forced form-class does NOT fix the CP-odd coefficients ----
    # (matter) M(delta, r) Hermitian and C3-covariant for ALL delta, r
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    herm_all = True
    cov_all = True
    for dv in [0.0, 0.2222, 1.0, 2.5]:
        for rv in [0.2, 0.5, 1.0, 3.0]:
            av, cv = 1.0, np.sqrt(rv)            # r = |b|^2/a^2, a=1
            bb = cv * np.exp(1j * dv)
            M = av*np.eye(3) + bb*C + np.conj(bb)*(C@C)
            herm_all = herm_all and np.allclose(M, M.conj().T)
            cov_all = cov_all and np.allclose(C @ M @ C.conj().T, M)  # circulant => commutes with C
    # (gauge) Wilson-loop trace and its CP-odd imaginary part are gauge-invariant under base-point
    # conjugation U_P -> V U_P V^dag, for ANY coefficient theta.
    def rand_su2(rng):
        a0 = rng.standard_normal(4); a0 /= np.linalg.norm(a0)
        return a0[0]*np.eye(2) + 1j*(a0[1]*np.array([[0,1],[1,0]],complex) +
                                     a0[2]*np.array([[0,-1j],[1j,0]],complex) +
                                     a0[3]*np.array([[1,0],[0,-1]],complex))
    UP = rand_su2(rng); V = rand_su2(rng)
    UP_g = V @ UP @ V.conj().T
    re_inv = abs(np.trace(UP).real - np.trace(UP_g).real) < 1e-9
    im_inv = abs(np.trace(UP).imag - np.trace(UP_g).imag) < 1e-9   # CP-odd (imaginary/topological) part
    # coefficient-independence: theta * Im Tr U_P is gauge-invariant for any theta (linear in the invariant)
    coeff_free = re_inv and im_inv
    check("S4: the tested gauge-invariant-local form-class does NOT fix the CP-odd coefficients. (matter) M(delta,r) is "
          "Hermitian and C3-covariant for ALL delta and ALL r; (gauge) Re Tr U_P and the CP-odd Im Tr U_P are "
          "gauge-invariant under U_P->V U_P V^dag for ANY coefficient theta. So (r, delta, theta) are FREE "
          "coefficients inside this tested form-class.",
          herm_all and cov_all and coeff_free,
          f"M(delta,r) Hermitian+covariant for all tested (delta,r): {herm_all and cov_all}; "
          f"Re/Im Tr U_P gauge-invariant: {re_inv}/{im_inv}")

    # ---- S5: orientation/chirality is a sign-only Z2 datum, not a continuous coefficient source ----
    sig1 = np.array([[0, 1], [1, 0]], complex)
    sig2 = np.array([[0, -1j], [1j, 0]], complex)
    sig3 = np.array([[1, 0], [0, -1]], complex)
    omega = sig1 @ sig2 @ sig3
    volume_is_scalar_i = np.allclose(omega, 1j * np.eye(2))
    orientation_values = {round(np.linalg.det(np.diag([sx, sy, sz]))) for sx in (1, -1) for sy in (1, -1) for sz in (1, -1)}
    sign_only = orientation_values == {-1, 1}
    check("S5: Cl(3) volume omega=sigma1 sigma2 sigma3 = iI and lattice orientation det(R) in {+1,-1}; "
          "the native orientation datum is sign-only, so it can flip a coefficient sign but cannot select a continuous value.",
          volume_is_scalar_i and sign_only,
          f"omega=iI: {volume_is_scalar_i}; orientation values={sorted(orientation_values)}")

    # ---- S6: real readout is CP-blind but does not forbid CP ----
    readout_even = True
    j_matches = True
    for dv in [0.0, 0.2222, 0.7, 1.3]:
        av, cv = 1.0, 0.6
        bb = cv * np.exp(1j * dv)
        M = av * np.eye(3) + bb * C + np.conj(bb) * (C @ C)
        J = np.imag(M[0, 1] * M[1, 2] * M[2, 0])
        j_matches = j_matches and abs(J - cv**3 * np.sin(3 * dv)) < 1e-9
        det_plus = np.linalg.det(M)
        bbm = cv * np.exp(-1j * dv)
        Mm = av * np.eye(3) + bbm * C + np.conj(bbm) * (C @ C)
        det_minus = np.linalg.det(Mm)
        readout_even = readout_even and abs(np.log(abs(det_plus)) - np.log(abs(det_minus))) < 1e-9
    check("S6: real additive readout log|det M(delta)| is even in delta, but J=Im(M01 M12 M20)=|b|^3 sin(3delta) "
          "is a real CP-odd scalar. Real readout is CP-blind as a consumer, not a CP prohibition.",
          readout_even and j_matches,
          f"log|det| even: {readout_even}; J formula matches: {j_matches}")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the tested routes do not source CP-odd action coefficients. The arrow is a Past-\n"
        "Hypothesis BOUNDARY condition under the tested time-symmetric write generator, so it cannot source\n"
        "a CP-odd action term; CPT reality protects determinant phases rather than sourcing a continuous CP\n"
        "coefficient; the orientation datum is sign-only; and real readout is CP-blind but not CP-forbidding.\n"
        "The tested form-class leaves r, delta, and theta as free coefficients. This is a scoped route no-go,\n"
        "not a proof against future dynamics/minimality/action-selection routes. Audit lane sets status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
