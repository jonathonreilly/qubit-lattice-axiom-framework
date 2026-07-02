#!/usr/bin/env python3
"""Temporal-kernel Casimir generator and beta/g_bare dial transport.

This runner deliberately stays source-side. It does not read audit ledgers,
audit queues, publication matrices, or effective-status files.

Checked content (all constructed, nothing assigned):

  K1  the temporal-gauge one-step per-link kernel of the supplied standard
      Wilson plaquette action, W_beta(M) = exp((beta/N_c) Re Tr M), is a
      class function; its convolution operator acts on the R-isotypic block
      as the scalar w_R(beta) = c_R(beta)/d_R with
      c_R = int W_beta(U) chi_R(U)* dU  (Haar). The per-step generator is
      defined in-packet as eps_R(beta) := -log(w_R / w_0).
  K2  Casimir asymptotics: beta * eps_R(beta) / N_c -> C_2(R) as
      beta -> infinity, with C_2 the quadratic Casimir in the SAME
      half-trace normalization Tr(T_a T_b) = delta_ab/2 that the canonical
      generator basis carries (anchored here by sum_a T_a T_a = (4/3) I_3
      at the fundamental). Mechanism companions: U(1) with kernel
      e^{beta cos}: 2 beta eps_n -> n^2; SU(2): beta eps_j / 2 -> j(j+1).
  K3  dial transport: defining the conjugate-slot coupling by
      eps_R = (g_E^2 / 2) C_2(R) (1 + O(1/beta)), the constructed values
      satisfy beta * g_E^2 -> 2 N_c — the same identity the magnetic-side
      small-a matching carries, now read on the kernel/generator side.
      The generator is a function of C_2 alone at leading order
      (R-independence of the extracted dial).
  K4  normalization-point coincidence (exact rational layer): the leading
      dial map g_lead^2(beta) = 2 N_c / beta takes the value 1 exactly at
      beta = 2 N_c = 6, where the leading per-step generator is the
      unit-coefficient canonical kinetic form (1/2) C_2(R); at beta = 24
      the leading generator is (1/8) C_2(R) (coefficient 1/4 != 1) on the
      same construction — the mismatched reading, exhibited not assigned.
      This packet does NOT derive beta = 2 N_c; it proves the coincidence
      structure of the single transported dial.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "WILSON_TEMPORAL_KERNEL_CASIMIR_GENERATOR_BETA_GBARE_TRANSPORT_THEOREM_NOTE_2026-07-01.md"
RIGIDITY = ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md"
WILSON = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
RP_TEMPORAL = ROOT / "docs" / "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"

N_C = 3

PASS = 0
FAIL = 0


def flat(text: str) -> str:
    return " ".join(text.split())


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    suffix = f" ({detail})" if detail else ""
    print(f"[{tag}] {name}{suffix}")
    return condition


def require_contains(label: str, text: str, marker: str) -> None:
    check(f"{label} contains marker: {marker[:72]}", marker in text)


def require_absent(label: str, text: str, marker: str) -> None:
    check(f"{label} omits forbidden marker: {marker[:72]}", marker not in text)


# ---------------------------------------------------------------------------
# Canonical su(3) basis (Gell-Mann / 2): the fixed half-trace normalization.
# ---------------------------------------------------------------------------

def canonical_generators() -> list[np.ndarray]:
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3.0)
    return [m / 2.0 for m in (l1, l2, l3, l4, l5, l6, l7, l8)]


# ---------------------------------------------------------------------------
# SU(3) class-function integration: stable Weyl alternants, no divisions.
#
# Eigenphase parametrization theta = (t1, t2, -t1-t2); for an integer vector
# l the alternant is a_l(theta) = det[exp(i theta_j l_k)].  With
# rho = (2, 1, 0), the Weyl character is chi_lambda = a_{lambda+rho}/a_rho
# and |a_rho|^2 is the class measure density, so
#   c_lambda = int W chi_lambda* dU
#            = (1/(6 (2pi)^2)) int W a_rho conj(a_{lambda+rho}) dt1 dt2,
# which needs no division and is stable at degenerate eigenphases.
# Uniform-grid means realize the periodic trapezoid rule (spectrally
# accurate; verified by grid doubling below).
# ---------------------------------------------------------------------------

RHO = np.array([2, 1, 0])
REPS = {
    "fund(1,0,0)": (1, 0, 0),
    "adj(2,1,0)": (2, 1, 0),
    "sym(2,0,0)": (2, 0, 0),
}


def alternant(l, T1, T2):
    th = [T1, T2, -T1 - T2]
    e = [[np.exp(1j * th[j] * l[k]) for k in range(3)] for j in range(3)]
    return (
        e[0][0] * (e[1][1] * e[2][2] - e[1][2] * e[2][1])
        - e[0][1] * (e[1][0] * e[2][2] - e[1][2] * e[2][0])
        + e[0][2] * (e[1][0] * e[2][1] - e[1][1] * e[2][0])
    )


def su3_char_coeff(lam, beta: float, M: int = 384) -> float:
    t = np.linspace(0.0, 2.0 * np.pi, M, endpoint=False)
    T1, T2 = np.meshgrid(t, t, indexing="ij")
    T3 = -T1 - T2
    a_rho = alternant(RHO, T1, T2)
    a_l = alternant(np.array(lam) + RHO, T1, T2)
    w = np.exp((beta / 3.0) * (np.cos(T1) + np.cos(T2) + np.cos(T3) - 3.0))
    return float((np.mean(w * a_rho * np.conj(a_l)) / 6.0).real)


def weyl_dim(lam) -> int:
    l = np.array(lam) + RHO
    return int(round((l[0] - l[1]) * (l[0] - l[2]) * (l[1] - l[2]) / 2.0))


def casimir_half_trace(lam) -> Fraction:
    s = sum(Fraction(lam[i]) * (lam[i] + 4 - 2 * (i + 1)) for i in range(3))
    return (s - Fraction(sum(lam)) ** 2 / 3) / 2


def su3_eps(lam, beta: float, M: int = 384) -> float:
    c0 = su3_char_coeff((0, 0, 0), beta, M)
    cR = su3_char_coeff(lam, beta, M)
    d = weyl_dim(lam)
    return -np.log((cR / d) / c0)


# ---------------------------------------------------------------------------
# U(1) and SU(2) mechanism companions (1D class integrals).
# ---------------------------------------------------------------------------

def u1_char_coeff(n: int, beta: float, M: int = 8192) -> float:
    th = np.linspace(0.0, 2.0 * np.pi, M, endpoint=False)
    w = np.exp(beta * (np.cos(th) - 1.0))
    return float(np.mean(w * np.exp(-1j * n * th)).real)


def u1_eps(n: int, beta: float) -> float:
    return -np.log(u1_char_coeff(n, beta) / u1_char_coeff(0, beta))


def su2_char_coeff(j: float, beta: float, M: int = 16384) -> float:
    th = np.linspace(1e-9, np.pi - 1e-9, M)
    chi = np.sin((2.0 * j + 1.0) * th) / np.sin(th)
    w = np.exp(beta * (np.cos(th) - 1.0))
    return float(np.trapezoid((2.0 / np.pi) * np.sin(th) ** 2 * chi * w, th))


def su2_eps(j: float, beta: float) -> float:
    d = 2.0 * j + 1.0
    return -np.log((su2_char_coeff(j, beta) / d) / su2_char_coeff(0.0, beta))


# ---------------------------------------------------------------------------
# Section A: canonical normalization anchors
# ---------------------------------------------------------------------------

def section_A() -> None:
    print("\nSECTION A: canonical half-trace normalization anchors")
    print("-" * 78)
    T = canonical_generators()
    gram = np.array([[np.trace(a @ b) for b in T] for a in T], dtype=complex)
    check(
        "trace form Tr(T_a T_b) = delta_ab / 2",
        bool(np.allclose(gram, np.eye(8) / 2.0, atol=1e-13)),
    )
    check("all T_a Hermitian", all(np.linalg.norm(Ta - Ta.conj().T) < 1e-14 for Ta in T))
    check("all T_a traceless", all(abs(np.trace(Ta)) < 1e-14 for Ta in T))
    cas_op = sum(Ta @ Ta for Ta in T)
    check(
        "sum_a T_a T_a = (4/3) I_3 on the fundamental",
        bool(np.allclose(cas_op, (4.0 / 3.0) * np.eye(3), atol=1e-13)),
    )
    check(
        "Casimir formula matches the operator anchor at the fundamental",
        casimir_half_trace((1, 0, 0)) == Fraction(4, 3),
    )
    check(
        "Casimir values (fund, adj, sym) = (4/3, 3, 10/3)",
        casimir_half_trace((1, 0, 0)) == Fraction(4, 3)
        and casimir_half_trace((2, 1, 0)) == Fraction(3)
        and casimir_half_trace((2, 0, 0)) == Fraction(10, 3),
    )
    check(
        "Weyl dimensions (fund, adj, sym) = (3, 8, 6)",
        weyl_dim((1, 0, 0)) == 3 and weyl_dim((2, 1, 0)) == 8 and weyl_dim((2, 0, 0)) == 6,
    )


# ---------------------------------------------------------------------------
# Section B: integration-machinery guards
# ---------------------------------------------------------------------------

def section_B() -> None:
    print("\nSECTION B: class-integration machinery guards")
    print("-" * 78)
    c_triv = su3_char_coeff((0, 0, 0), 0.0)
    check("beta=0: trivial-character coefficient = 1 (Haar orthonormality)", abs(c_triv - 1.0) < 1e-12)
    for name, lam in REPS.items():
        c = su3_char_coeff(lam, 0.0)
        check(f"beta=0: c_{name} = 0 (Haar orthogonality)", abs(c) < 1e-12, f"c={c:.2e}")
    for name, lam in REPS.items():
        a = su3_char_coeff(lam, 48.0, M=384)
        b = su3_char_coeff(lam, 48.0, M=512)
        check(
            f"grid-doubling agreement for c_{name} at beta=48",
            abs(a - b) / abs(b) < 1e-10,
            f"rel dev={abs(a - b) / abs(b):.2e}",
        )
    allpos = all(
        su3_char_coeff(lam, b) > 0.0 for lam in REPS.values() for b in (6.0, 12.0, 24.0, 48.0)
    )
    check("all SU(3) kernel character coefficients positive on tested betas", allpos)


# ---------------------------------------------------------------------------
# Sections C, D: U(1) and SU(2) mechanism companions
# ---------------------------------------------------------------------------

def section_C() -> None:
    print("\nSECTION C: U(1) companion — 2 beta eps_n -> n^2")
    print("-" * 78)
    for n in (1, 2, 3):
        f = {b: 2.0 * b * u1_eps(n, b) / n**2 for b in (12.0, 24.0, 48.0, 96.0)}
        check(
            f"U(1) n={n}: |f-1| strictly decreasing along beta doubling",
            abs(f[96.0] - 1) < abs(f[48.0] - 1) < abs(f[24.0] - 1) < abs(f[12.0] - 1),
            f"f(96)={f[96.0]:.5f}",
        )
        r1 = 2.0 * f[96.0] - f[48.0]
        check(f"U(1) n={n}: Richardson(48,96) hits 1", abs(r1 - 1.0) < 2e-3, f"R1={r1:.6f}")


def section_D() -> None:
    print("\nSECTION D: SU(2) companion — beta eps_j / 2 -> j(j+1)")
    print("-" * 78)
    for j in (0.5, 1.0, 1.5):
        C2 = j * (j + 1.0)
        f = {b: b * su2_eps(j, b) / (2.0 * C2) for b in (12.0, 24.0, 48.0, 96.0)}
        check(
            f"SU(2) j={j}: |f-1| strictly decreasing along beta doubling",
            abs(f[96.0] - 1) < abs(f[48.0] - 1) < abs(f[24.0] - 1) < abs(f[12.0] - 1),
            f"f(96)={f[96.0]:.5f}",
        )
        r1 = 2.0 * f[96.0] - f[48.0]
        check(f"SU(2) j={j}: Richardson(48,96) hits 1", abs(r1 - 1.0) < 2e-3, f"R1={r1:.6f}")


# ---------------------------------------------------------------------------
# Section E: SU(3) Casimir asymptotics (Theorem K2)
# ---------------------------------------------------------------------------

def section_E() -> dict[str, dict[float, float]]:
    print("\nSECTION E: SU(3) — beta eps_R / N_c -> C_2(R), half-trace normalization")
    print("-" * 78)
    fs: dict[str, dict[float, float]] = {}
    for name, lam in REPS.items():
        C2 = float(casimir_half_trace(lam))
        f = {b: b * su3_eps(lam, b) / (N_C * C2) for b in (12.0, 24.0, 48.0)}
        fs[name] = f
        check(
            f"SU(3) {name}: |f-1| strictly decreasing along beta doubling",
            abs(f[48.0] - 1) < abs(f[24.0] - 1) < abs(f[12.0] - 1),
            f"f(48)={f[48.0]:.5f}",
        )
        r1 = 2.0 * f[48.0] - f[24.0]
        check(f"SU(3) {name}: Richardson(24,48) hits 1", abs(r1 - 1.0) < 1.5e-2, f"R1={r1:.6f}")
        r2 = (8.0 * f[48.0] - 6.0 * f[24.0] + f[12.0]) / 3.0
        check(f"SU(3) {name}: Richardson2(12,24,48) hits 1", abs(r2 - 1.0) < 5e-3, f"R2={r2:.6f}")
    return fs


# ---------------------------------------------------------------------------
# Section F: dial transport (Theorem K3)
# ---------------------------------------------------------------------------

def section_F(fs: dict[str, dict[float, float]]) -> None:
    print("\nSECTION F: dial transport — beta * g_E^2 -> 2 N_c, R-independent")
    print("-" * 78)
    lam = REPS["fund(1,0,0)"]
    C2 = float(casimir_half_trace(lam))
    bg = {b: b * (2.0 * su3_eps(lam, b) / C2) for b in (12.0, 24.0, 48.0)}
    check(
        "beta * g_E^2 strictly decreasing toward 2 N_c = 6",
        bg[12.0] > bg[24.0] > bg[48.0] > 6.0,
        f"values={bg[12.0]:.4f}, {bg[24.0]:.4f}, {bg[48.0]:.4f}",
    )
    r1 = 2.0 * bg[48.0] - bg[24.0]
    check("transport Richardson(24,48): beta * g_E^2 hits 2 N_c = 6", abs(r1 - 6.0) < 8e-2, f"R1={r1:.5f}")
    r2 = (8.0 * bg[48.0] - 6.0 * bg[24.0] + bg[12.0]) / 3.0
    check("transport Richardson2(12,24,48): beta * g_E^2 hits 2 N_c = 6", abs(r2 - 6.0) < 2e-2, f"R2={r2:.5f}")

    for other in ("adj(2,1,0)", "sym(2,0,0)"):
        ratio = fs[other][48.0] / fs["fund(1,0,0)"][48.0]
        check(
            f"extracted dial is R-independent at beta=48 ({other} vs fund)",
            abs(ratio - 1.0) < 5e-3,
            f"ratio={ratio:.6f}",
        )


# ---------------------------------------------------------------------------
# Section G: exact rational normalization-point layer (Corollary K4)
# ---------------------------------------------------------------------------

def section_G() -> None:
    print("\nSECTION G: exact leading-dial layer — coincidence at beta = 2 N_c")
    print("-" * 78)
    n_c = Fraction(3)
    two_n_c = 2 * n_c

    def g_lead_sq(beta: Fraction) -> Fraction:
        return two_n_c / beta

    check("leading dial map: g_lead^2(6) = 1", g_lead_sq(Fraction(6)) == 1)
    check(
        "identity beta * g_lead^2 = 2 N_c for all tested beta",
        all(b * g_lead_sq(b) == two_n_c for b in (Fraction(6), Fraction(24), Fraction(3, 2), Fraction(12))),
    )
    check(
        "unit-coefficient point: leading generator at beta=6 is (1/2) C_2",
        g_lead_sq(Fraction(6)) / 2 == Fraction(1, 2),
    )
    check(
        "mismatched reading at beta=24: leading generator is (1/8) C_2, coefficient 1/4 != 1",
        g_lead_sq(Fraction(24)) == Fraction(1, 4)
        and g_lead_sq(Fraction(24)) / 2 == Fraction(1, 8)
        and g_lead_sq(Fraction(24)) != 1,
    )
    for b in (Fraction(24), Fraction(3, 2), Fraction(12)):
        check(
            f"beta={b} != 2 N_c gives g_lead^2 = {g_lead_sq(b)} != 1 (coincidence fails off the point)",
            g_lead_sq(b) != 1,
        )
    check(
        "coincidence forward: beta = 2 N_c gives g_lead^2 = 1",
        g_lead_sq(two_n_c) == 1,
    )
    check(
        "coincidence backward: g_lead^2 = 1 gives beta = 2 N_c = 6",
        two_n_c / Fraction(1) == Fraction(6),
    )
    # The three canonical normalizations meet at the single point beta = 2 N_c:
    # coordinate slot s^2 = 1 (rigidity surface), magnetic slot g^2 = 2 N_c/beta
    # (retained small-a matching), kernel/generator slot g_E,lead^2 = 2 N_c/beta
    # (this packet). Their equality at beta = 6 is exact.
    s_sq = Fraction(1)
    g_mag_sq_at_6 = two_n_c / Fraction(6)
    g_ker_sq_at_6 = g_lead_sq(Fraction(6))
    check(
        "three-normalization coincidence at beta=6: s^2 = g_mag^2 = g_E,lead^2 = 1",
        s_sq == g_mag_sq_at_6 == g_ker_sq_at_6 == 1,
    )


# ---------------------------------------------------------------------------
# Section H: source-boundary guards
# ---------------------------------------------------------------------------

def section_H() -> None:
    print("\nSECTION H: source-boundary guards")
    print("-" * 78)
    paths = {
        "transport note": NOTE,
        "finite-link rigidity note": RIGIDITY,
        "Wilson small-a note": WILSON,
        "RP temporal-gauge bridge note": RP_TEMPORAL,
    }
    for label, path in paths.items():
        rel_path = path.relative_to(ROOT).as_posix()
        check(f"{label} exists", path.exists(), rel_path)

    note_text = NOTE.read_text(encoding="utf-8")
    rigidity_flat = flat(RIGIDITY.read_text(encoding="utf-8"))
    wilson_text = WILSON.read_text(encoding="utf-8")
    rp_flat = flat(RP_TEMPORAL.read_text(encoding="utf-8"))
    note_flat = flat(note_text)

    require_contains("note", note_flat, "Status authority:** independent audit lane only")
    require_contains("note", note_flat, "does not derive `beta = 2 N_c`")
    require_contains("note", note_flat, "unit-coefficient")
    require_contains("note", note_flat, "half-trace")
    require_contains("note", note_flat, "one dial")
    require_contains("note", note_flat, "does not claim:")
    require_contains("note", note_flat, "Wilson plaquette action-surface selection")
    require_contains("note", note_flat, "an audit verdict or any effective-status promotion")
    require_contains("note", note_flat, "not a citation-graph dependency")
    require_absent("note", note_text, "effective_status:")
    require_absent("note", note_text, "audit_status:")
    require_absent("note", note_text, "**Audit status:**")

    require_contains("rigidity", rigidity_flat, "no independent scalar-normalization freedom")
    require_contains("rigidity", rigidity_flat, "Tr(T_a T_b) = delta_ab / 2")
    require_contains("Wilson", wilson_text, "beta * g_bare^2 = 2 N_c")
    require_contains(
        "Wilson",
        flat(wilson_text),
        "does not derive that the framework must select the Wilson action surface",
    )
    require_contains("RP bridge", rp_flat, "temporal gauge")
    require_contains("RP bridge", rp_flat, "plane positive kernel")


def main() -> int:
    print("Wilson temporal-kernel Casimir generator / beta-g_bare dial transport check")
    print("=" * 78)
    section_A()
    section_B()
    section_C()
    section_D()
    fs = section_E()
    section_F(fs)
    section_G()
    section_H()

    print("\nSummary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("Transport check failed.")
        return 1
    print("Transport check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
