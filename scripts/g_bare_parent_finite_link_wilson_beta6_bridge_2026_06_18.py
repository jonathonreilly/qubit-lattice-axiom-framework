#!/usr/bin/env python3
"""Check the finite-link/Wilson split-redundancy bounded theorem.

This runner deliberately stays source-side. It does not read audit ledgers,
audit queues, publication matrices, or effective-status files.

The runner constructs both scalar slots from the supplied link/plaquette data
and compares them without assigning ``g_wilson_sq = g_link_sq``. The checked
content is algebraic; the same-slot convention is guarded on a separate meta
surface:

  T1  plaquette exponent construction: for links built from canonical
      su(3) coordinates C at spacing a, the plaquette exponent is
      a^2 F[C;1] + O(a^3) with
      F[C;1] = D_mu C_nu - D_nu C_mu + i [C_mu, C_nu]
      and unit scalar coefficient in the canonical T_a basis
      (Richardson-verified with remainder-order scaling).
  T2  exact split redundancy: for every gamma != 0 the standard-convention
      split (g_bare, A) = (gamma, C/gamma) reproduces every link matrix,
      every plaquette matrix, and every Wilson action value identically,
      and gamma * F[C/gamma; gamma] = F[C; 1] exactly. The split scalar is
      not a function of the constructed surface data. Contrast: a genuine
      dilation exp(i a s C) with s != 1 CHANGES the link — that is the
      freedom the rigidity theorem removes; choosing the split freedom is
      outside this theorem.
  T3  matched slot, constructed: the Wilson small-a matching demand
      applied to the constructed plaquette action yields
      gamma*(beta)^2 = 2 N_c / beta for each tested beta (never assigned).
  T4  link slot, constructed: the canonical-coordinate readback of the
      constructed link via the principal logarithm gives s = 1.
  T5  comparison: the two constructed slots agree at beta = 2 N_c and
      disagree at beta in {24, 3/2, 12} on identical link/plaquette data
      (mismatched-slot exhibit; pin equivalence gamma* = s iff
      beta = 2 N_c).
  T6  source-boundary guards: convention content is absent from the bounded
      theorem. The separate meta convention surface is outside this theorem
      certificate's dependency set.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "docs" / "G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "G_BARE_DERIVATION_NOTE.md"
RIGIDITY = ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md"
WILSON = ROOT / "docs" / "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"

N_C = 3
SEED = 20260701

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
# Canonical su(3) basis: Gell-Mann matrices / 2, Tr(T_a T_b) = delta_ab / 2.
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


T_BASIS = canonical_generators()


def herm_from_coeffs(c: np.ndarray) -> np.ndarray:
    return sum(ci * Ti for ci, Ti in zip(c, T_BASIS))


def coeffs_from_herm(H: np.ndarray) -> np.ndarray:
    return np.array([2.0 * np.trace(Ti @ H).real for Ti in T_BASIS])


def expm_herm(H: np.ndarray) -> np.ndarray:
    w, V = np.linalg.eigh(H)
    return (V * np.exp(1j * w)) @ V.conj().T


def principal_log_unitary(U: np.ndarray) -> np.ndarray:
    """Hermitian H with U = exp(i H), principal eigenphase branch."""
    w, V = np.linalg.eig(U)
    theta = np.angle(w)
    H = (V * theta) @ np.linalg.inv(V)
    return (H + H.conj().T) / 2.0


def fro(M: np.ndarray) -> float:
    return float(np.linalg.norm(M))


# ---------------------------------------------------------------------------
# Linear canonical field configuration on a (u, v) plaquette plane.
# C_mu(x) = P_mu + u * S_mu + v * R_mu, Hermitian traceless su(3) values.
# Forward lattice differences of linear fields are exact:
#   D_u C_v = S_v,  D_v C_u = R_u.
# ---------------------------------------------------------------------------

class FieldConfig:
    def __init__(self, rng: np.random.Generator):
        def draw() -> np.ndarray:
            return herm_from_coeffs(rng.normal(size=8))

        self.P_u, self.S_u, self.R_u = draw(), draw(), draw()
        self.P_v, self.S_v, self.R_v = draw(), draw(), draw()
        self.u0, self.v0 = 0.3, 0.7

    def C_u(self, u: float, v: float) -> np.ndarray:
        return self.P_u + u * self.S_u + v * self.R_u

    def C_v(self, u: float, v: float) -> np.ndarray:
        return self.P_v + u * self.S_v + v * self.R_v

    def links(self, a: float, scale: float = 1.0, divide: float = 1.0):
        """Four plaquette links built as exp(i a scale (C / divide)).

        scale=divide=gamma realizes the standard-convention split
        (g_bare, A) = (gamma, C / gamma); scale != divide realizes a
        genuine dilation of the canonical data.
        """
        u0, v0 = self.u0, self.v0
        arg = scale / divide
        U1 = expm_herm(a * arg * self.C_u(u0, v0))
        U2 = expm_herm(a * arg * self.C_v(u0 + a, v0))
        U3 = expm_herm(a * arg * self.C_u(u0, v0 + a))
        U4 = expm_herm(a * arg * self.C_v(u0, v0))
        return U1, U2, U3, U4

    def plaquette(self, a: float, scale: float = 1.0, divide: float = 1.0) -> np.ndarray:
        U1, U2, U3, U4 = self.links(a, scale=scale, divide=divide)
        return U1 @ U2 @ U3.conj().T @ U4.conj().T

    def f_lattice(self) -> np.ndarray:
        """F[C;1] = D_u C_v - D_v C_u + i [C_u, C_v] at the base point."""
        Cu = self.C_u(self.u0, self.v0)
        Cv = self.C_v(self.u0, self.v0)
        return self.S_v - self.R_u + 1j * (Cu @ Cv - Cv @ Cu)


# ---------------------------------------------------------------------------
# Section A: canonical-basis guards
# ---------------------------------------------------------------------------

def section_A() -> None:
    print("\nSECTION A: canonical su(3) basis guards")
    print("-" * 78)
    gram = np.array(
        [[np.trace(Ta @ Tb) for Tb in T_BASIS] for Ta in T_BASIS], dtype=complex
    )
    check(
        "trace form Tr(T_a T_b) = delta_ab / 2",
        bool(np.allclose(gram, np.eye(8) / 2.0, atol=1e-13)),
        f"max dev={np.max(np.abs(gram - np.eye(8) / 2.0)):.2e}",
    )
    check(
        "all T_a Hermitian",
        all(fro(Ta - Ta.conj().T) < 1e-14 for Ta in T_BASIS),
    )
    check(
        "all T_a traceless",
        all(abs(np.trace(Ta)) < 1e-14 for Ta in T_BASIS),
    )
    check("basis has 8 generators on C^3", len(T_BASIS) == 8 and T_BASIS[0].shape == (3, 3))


# ---------------------------------------------------------------------------
# Section B: Theorem 1 — plaquette exponent construction
# ---------------------------------------------------------------------------

def section_B(configs: list[FieldConfig]) -> list[np.ndarray]:
    print("\nSECTION B: Theorem 1 — plaquette exponent = a^2 F[C;1] + O(a^3)")
    print("-" * 78)
    a1, a2 = 1e-2, 5e-3
    f_constructed = []
    for i, cfg in enumerate(configs):
        F_lat = cfg.f_lattice()
        E1 = principal_log_unitary(cfg.plaquette(a1)) / a1**2
        E2 = principal_log_unitary(cfg.plaquette(a2)) / a2**2
        E_rich = 2.0 * E2 - E1

        check(
            f"draw {i}: plaquette exponent Hermitian traceless",
            fro(E1 - E1.conj().T) < 1e-9 and abs(np.trace(E1)) < 1e-9,
        )
        rel = fro(E_rich - F_lat) / fro(F_lat)
        check(
            f"draw {i}: Richardson exponent matches F[C;1]",
            rel < 5e-3,
            f"rel err={rel:.2e}",
        )
        r1, r2 = fro(E1 - F_lat), fro(E2 - F_lat)
        ratio = r1 / r2 if r2 > 0 else float("inf")
        check(
            f"draw {i}: remainder is O(a) after /a^2 (ratio ~ 2)",
            1.6 < ratio < 2.4 or (r1 < 1e-10 and r2 < 1e-10),
            f"ratio={ratio:.3f}",
        )
        fhat = coeffs_from_herm(E_rich)
        flat_c = coeffs_from_herm(F_lat)
        crel = float(np.linalg.norm(fhat - flat_c) / np.linalg.norm(flat_c))
        check(
            f"draw {i}: canonical T_a coefficients of exponent match F^a[C]",
            crel < 5e-3,
            f"rel err={crel:.2e}",
        )
        span_res = fro(E_rich - herm_from_coeffs(coeffs_from_herm(E_rich))) / fro(E_rich)
        check(
            f"draw {i}: exponent lies in canonical generator span",
            span_res < 1e-8,
            f"residual={span_res:.2e}",
        )
        f_constructed.append(F_lat)
    return f_constructed


# ---------------------------------------------------------------------------
# Section C: Theorem 2 — exact split redundancy vs genuine dilation
# ---------------------------------------------------------------------------

def section_C(cfg: FieldConfig) -> None:
    print("\nSECTION C: Theorem 2 — exact split redundancy (gamma, C/gamma)")
    print("-" * 78)
    a = 1e-2
    base_links = cfg.links(a)
    base_plaq = cfg.plaquette(a)
    beta = 7.0
    base_action = beta * (1.0 - np.trace(base_plaq).real / N_C)
    F_lat = cfg.f_lattice()

    for gamma in (0.5, 2.0, 3.0, 1.4):
        split_links = cfg.links(a, scale=gamma, divide=gamma)
        dmax = max(fro(Ub - Us) for Ub, Us in zip(base_links, split_links))
        check(
            f"gamma={gamma}: all four link matrices identical under split",
            dmax < 1e-12,
            f"max dev={dmax:.2e}",
        )
        split_plaq = cfg.plaquette(a, scale=gamma, divide=gamma)
        check(
            f"gamma={gamma}: plaquette matrix identical under split",
            fro(base_plaq - split_plaq) < 1e-12,
        )
        split_action = beta * (1.0 - np.trace(split_plaq).real / N_C)
        check(
            f"gamma={gamma}: Wilson action value identical under split",
            abs(base_action - split_action) < 1e-12,
        )
        # gamma * F[C/gamma; gamma] with F[A; g] = DA - DA + i g [A, A]
        Au = cfg.C_u(cfg.u0, cfg.v0) / gamma
        Av = cfg.C_v(cfg.u0, cfg.v0) / gamma
        dA = (cfg.S_v - cfg.R_u) / gamma
        F_split = gamma * (dA + 1j * gamma * (Au @ Av - Av @ Au))
        check(
            f"gamma={gamma}: gamma * F[C/gamma; gamma] = F[C; 1] exactly",
            fro(F_split - F_lat) < 1e-12,
            f"dev={fro(F_split - F_lat):.2e}",
        )

    # Contrast: genuine dilation exp(i a s C) with s != 1 changes the data.
    a_dil = 5e-2
    U_base = expm_herm(a_dil * cfg.C_u(cfg.u0, cfg.v0))
    U_dil = expm_herm(a_dil * 2.0 * cfg.C_u(cfg.u0, cfg.v0))
    check(
        "genuine dilation s=2 changes the link matrix",
        fro(U_dil - U_base) > 1e-3,
        f"dev={fro(U_dil - U_base):.2e}",
    )
    plaq_base = cfg.plaquette(a_dil)
    plaq_dil = cfg.plaquette(a_dil, scale=2.0, divide=1.0)
    act_base = beta * (1.0 - np.trace(plaq_base).real / N_C)
    act_dil = beta * (1.0 - np.trace(plaq_dil).real / N_C)
    check(
        "genuine dilation s=2 changes the Wilson action value",
        abs(act_base - act_dil) > 1e-8,
        f"dev={abs(act_base - act_dil):.2e}",
    )


# ---------------------------------------------------------------------------
# Section D: Theorem 3 — matched slot constructed from the plaquette action
# ---------------------------------------------------------------------------

def matched_slot_sq(cfg: FieldConfig, beta: float, a: float, FF: float) -> float:
    """Construct gamma*(beta)^2 from the plaquette matrices.

    k(beta, a) = beta (1 - Re Tr U_P / N_c) / (a^4 F^a[C] F^a[C]) is the
    constructed coefficient of the canonical-coordinate quadratic form;
    the Wilson matching demand (coefficient 1/2 per unordered plane for
    the matched field A = C/gamma) fixes k * gamma*^2 = 1/2.
    """
    UP = cfg.plaquette(a)
    s_val = beta * (1.0 - np.trace(UP).real / N_C)
    k = s_val / (a**4 * FF)
    return 1.0 / (2.0 * k)


def section_D(cfg: FieldConfig, F_lat: np.ndarray) -> dict[float, float]:
    print("\nSECTION D: Theorem 3 — matched slot gamma*(beta)^2 = 2 N_c / beta")
    print("-" * 78)
    Fa = coeffs_from_herm(F_lat)
    FF = float(Fa @ Fa)
    a = 2e-3
    out: dict[float, float] = {}
    betas = (2.0 * N_C, 24.0, 1.5, 12.0)
    check(
        "tested Wilson matching domain has beta > 0",
        all(beta > 0.0 for beta in betas),
    )
    for beta in betas:
        UP = cfg.plaquette(a)
        s_val = beta * (1.0 - np.trace(UP).real / N_C)
        k = s_val / (a**4 * FF)
        k_pred = beta / (4.0 * N_C)
        check(
            f"beta={beta}: constructed action coefficient k -> beta/(4 N_c)",
            abs(k - k_pred) / k_pred < 5e-3,
            f"k={k:.6f}, pred={k_pred:.6f}",
        )
        g2 = matched_slot_sq(cfg, beta, a, FF)
        g2_pred = 2.0 * N_C / beta
        check(
            f"beta={beta}: constructed matched slot gamma*^2 -> 2 N_c / beta",
            abs(g2 - g2_pred) / g2_pred < 5e-3,
            f"gamma*^2={g2:.6f}, pred={g2_pred:.6f}",
        )
        gamma_star = math.sqrt(g2)
        check(
            f"beta={beta}: gamma* is the positive matched-coupling root",
            gamma_star > 0.0 and abs(gamma_star**2 - g2) < 1e-12,
            f"gamma*={gamma_star:.6f}",
        )
        check(
            f"beta={beta}: constructed product beta * gamma*^2 -> 2 N_c",
            abs(beta * g2 - 2.0 * N_C) / (2.0 * N_C) < 5e-3,
            f"beta*gamma*^2={beta * g2:.6f}",
        )
        out[beta] = g2

    # Convergence of the constructed matched slot at the algebraic pin
    # beta = 2 N_c. The trace-level
    # O(a) correction cancels by cyclicity (Tr(F [C, F]) = 0 for the linear
    # fields used here), so the remainder is higher order; the check asserts
    # strict convergence plus accuracy, not a specific remainder order.
    Fa2 = float(Fa @ Fa)
    e_a = abs(matched_slot_sq(cfg, 2.0 * N_C, 2e-3, Fa2) - 1.0)
    e_h = abs(matched_slot_sq(cfg, 2.0 * N_C, 1e-3, Fa2) - 1.0)
    ratio = e_a / e_h if e_h > 0 else float("inf")
    check(
        "matched-slot construction converges as a -> 0",
        ratio > 1.5 or (e_a < 1e-10 and e_h < 1e-10),
        f"error ratio={ratio:.3f}",
    )
    check(
        "matched-slot construction accurate at a = 1e-3",
        e_h < 1e-3,
        f"|gamma*^2 - 1|={e_h:.2e}",
    )
    return out


# ---------------------------------------------------------------------------
# Section E: Theorem 4 + comparison — link slot readback vs matched slot
# ---------------------------------------------------------------------------

def section_E(configs: list[FieldConfig], matched: dict[float, float]) -> None:
    print("\nSECTION E: link slot readback and slot COMPARISON (never assigned)")
    print("-" * 78)
    a = 1e-2
    s_readbacks = []
    for i, cfg in enumerate(configs):
        C = cfg.C_u(cfg.u0, cfg.v0)
        U = expm_herm(a * C)
        C_hat = principal_log_unitary(U) / a
        rel = fro(C_hat - C) / fro(C)
        check(
            f"draw {i}: canonical readback log(U)/(i a) reproduces C",
            rel < 1e-9,
            f"rel err={rel:.2e}",
        )
        s_read = float(np.trace(C_hat @ C).real / np.trace(C @ C).real)
        check(
            f"draw {i}: constructed link-canonical slot s = 1",
            abs(s_read - 1.0) < 1e-10,
            f"s={s_read:.12f}",
        )
        s_readbacks.append(s_read)
    s_link = s_readbacks[0]

    pin_beta = 2.0 * N_C
    gamma_pin = math.sqrt(matched[pin_beta])
    check(
        "positive slots agree at the algebraic pin beta = 2 N_c",
        abs(gamma_pin - s_link) < 5e-3,
        f"gamma*={gamma_pin:.6f}, s={s_link:.6f}",
    )
    gamma_24 = math.sqrt(matched[24.0])
    check(
        "mismatched-slot exhibit at beta = 24: gamma*(24) != s on identical data",
        abs(gamma_24 - s_link) > 0.49,
        f"gamma*={gamma_24:.6f} vs s={s_link:.6f}",
    )
    gamma_1p5 = math.sqrt(matched[1.5])
    check(
        "mismatched-slot exhibit at beta = 3/2: gamma*(3/2) != s",
        abs(gamma_1p5 - s_link) > 0.5,
        f"gamma*={gamma_1p5:.6f}",
    )
    gamma_12 = math.sqrt(matched[12.0])
    check(
        "mismatched-slot exhibit at beta = 12: gamma*(12) != s",
        abs(gamma_12 - s_link) > 0.25,
        f"gamma*={gamma_12:.6f}",
    )

# ---------------------------------------------------------------------------
# Section G: source-boundary guards
# ---------------------------------------------------------------------------

def section_G() -> None:
    print("\nSECTION G: source-boundary guards")
    print("-" * 78)
    paths = {
        "bounded theorem note": BRIDGE,
        "parent note": PARENT,
        "finite-link rigidity note": RIGIDITY,
        "Wilson small-a note": WILSON,
    }
    for label, path in paths.items():
        rel_path = path.relative_to(ROOT).as_posix()
        check(f"{label} exists", path.exists(), rel_path)

    bridge_text = BRIDGE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    rigidity_text = RIGIDITY.read_text(encoding="utf-8")
    wilson_text = WILSON.read_text(encoding="utf-8")
    bridge_flat = flat(bridge_text)
    parent_flat = flat(parent_text)
    rigidity_flat = flat(rigidity_text)
    wilson_flat = flat(wilson_text)

    require_contains("theorem", bridge_flat, "set only by the independent audit lane")
    require_contains("theorem", bridge_flat, "non-load-bearing convention context")
    require_contains("theorem", bridge_flat, "This theorem locates the pin but does not choose it")
    require_contains("theorem", bridge_text, "gamma*(beta) := +sqrt(2 N_c / beta) > 0")
    require_contains("theorem", bridge_flat, "equality of the squares is equivalent to equality of the slots themselves")
    require_contains("bridge", bridge_flat, "mismatched-slot")
    require_contains("bridge", bridge_flat, "does not claim:")
    require_contains("bridge", bridge_flat, "Wilson plaquette action-surface selection")
    require_contains("bridge", bridge_flat, "global logarithm-branch selection")
    require_contains("bridge", bridge_flat, "a dynamical fixed point")
    require_contains("bridge", bridge_flat, "an audit verdict or any effective-status promotion")
    require_contains("bridge", bridge_flat, "finite-link canonical Wilson surface")
    require_contains(
        "bridge",
        bridge_flat,
        "This note's audited claim surface is exactly",
    )
    require_contains(
        "bridge",
        bridge_flat,
        "2026-07-11 downstream hygiene.** This note's citable surface is Theorems 1–3 and the mismatched-slot exhibit",
    )
    require_contains("bridge", bridge_text, "## Repair Note")
    require_absent("bridge", bridge_text, "effective_status:")
    require_absent("bridge", bridge_text, "audit_status:")
    require_absent(
        "bridge", bridge_flat, "This note proves that the scalar in those two statements"
    )
    require_absent("theorem", bridge_text, "(SD)")
    require_absent("theorem", bridge_text, "A^a := C^a")
    require_absent("theorem", bridge_text, "g_bare := s")
    require_absent("theorem", bridge_text, "At `N_c = 3`, exact rational arithmetic gives `beta = 6`")

    require_contains(
        "parent", parent_text, "G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md"
    )
    require_contains("parent", parent_text, "G_BARE_RIGIDITY_THEOREM_NOTE.md")
    require_contains(
        "parent", parent_text, "WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md"
    )
    require_contains(
        "parent", parent_flat, "No step uses `beta = 6` as a premise for `g_bare = 1`."
    )
    require_absent("parent", parent_text, "beta_canonical")

    require_contains("rigidity", rigidity_flat, "finite-link")
    require_contains("rigidity", rigidity_flat, "no independent scalar-normalization freedom")
    require_contains("Wilson", wilson_text, "beta * g_bare^2 = 2 N_c")
    require_contains("Wilson", wilson_text, "beta = 2 N_c / g_bare^2")
    require_contains(
        "Wilson", wilson_flat, "does not derive that the framework must select the Wilson action surface"
    )


def main() -> int:
    print("G_BARE finite-link/Wilson split-redundancy theorem check")
    print("(algebraic theorem separated from same-slot convention metadata)")
    print("=" * 78)

    rng = np.random.default_rng(SEED)
    configs = [FieldConfig(rng) for _ in range(3)]

    section_A()
    f_constructed = section_B(configs)
    section_C(configs[0])
    matched = section_D(configs[0], f_constructed[0])
    section_E(configs, matched)
    section_G()

    print("\nSummary")
    print("-" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("Bridge check failed.")
        return 1
    print("Bridge check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
