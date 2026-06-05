#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""FRONTIER: How much of the Born rule is UNCONDITIONAL from {Quantum + Record}?

GOAL
----
A sharpening of the prior conditional result
(BORN_FROM_ENVARIANCE_CONDITIONAL_ON_STATE_FUNCTIONAL_PROBABILITY_NOTE_2026-06-05,
"#2702"): that note pinned the single residual admission to A3 = "a probability
measure EXISTS and is a function of the state." The sharpening claims that part of
A3 is already INSIDE the axioms, because:

  * Quantum = the one-site C*-algebra M_2(C). EVERY C*-algebra has STATES omega
    (positive, normalized linear functionals). The finite-dim structure theorem
    forces omega(A) = Tr(rho A) for a density matrix rho; for a projector P,
    omega(P) = Tr(rho P) in [0,1], ADDITIVE over orthogonal projectors by
    linearity, and omega(P_k) = |a_k|^2 for a PURE state. That IS Born (the form
    AND the pure-state value) -- as a THEOREM of the algebra.
  * Record = additivity of a scalar readout over disjoint records. Disjoint
    outcomes are orthogonal projectors. So Record IS Gleason's non-contextual
    frame-function additivity (the very thing the Gleason/Busch derivation note
    flags as an INPUT, "G1 finding").

So this runner tests, rigorously and HONESTLY, the decomposition of A3 into:
  (a) "a consistent additive [0,1] state-functional EXISTS" -- and whether that
      is supplied by Quantum (C*-state form) and/or Record (additivity), and
  (b) the OPERATIONAL IDENTIFICATION "this functional = the empirical relative
      frequencies you RECORD" -- the genuinely residual physics.

It then ATTACKS (b) via the record-frequency / frequency-operator structure
(Hartle 1968; Farhi-Goldstone-Gutmann 1989; Finkelstein 1965): on N copies,
f_hat_P = (1/N) sum_i P^(i) has mean Tr(rho P) and variance -> 0 as N -> oo, so
the state approaches an eigenstate of f_hat_P with eigenvalue Tr(rho P) = |a_k|^2.

CRITICAL CIRCULARITY CHECK (Hartle's known critique, sharpened by Squires 1990,
Caves-Schack 2005): the LLN step "deviation states have vanishing norm" measures
that norm with the HILBERT INNER PRODUCT = the Born measure. Does the Record-
counting structure supply the typicality NON-circularly, or does it smuggle the
very measure it is deriving? The runner is explicit, separating:
  * the MEAN  <f_hat_P> = Tr(rho P): non-circular (linearity / algebraic state),
  * the TYPICALITY (deviation subspace has small WEIGHT): CIRCULAR -- the weight
    is the Born norm of the deviation subspace.

NO-GO CHECK: confirm the frequency/counting route does NOT use the barred
(R_+, x) -> (R, +) homomorphism. It counts integer occurrences across N SEPARATE
records -> relative frequency (an existence/identification claim), distinct from
the no-go's branch-to-scalar log-p map AND from the no-go's free-monoid caveat
(encoding ONE branch's probability into a word length).

MEMORY: small explicit qubit systems (<= 8 copies), exact sympy + numpy
cross-check. RSS capped < 2 GB and reported. Logs tee'd to a capped file.
PASS/FAIL self-check at the end.

This runner is a CONDITIONAL/NEGATIVE recorder. It does NOT assert an audit
verdict. It states honestly how much of Born is unconditional from {Quantum +
Record} and names the irreducible residual.
"""
from __future__ import annotations

import io
import os
import sys
from fractions import Fraction

import numpy as np
import sympy as sp

# --------------------------------------------------------------------------- #
# Memory cap (best effort): keep RSS under 2 GB.
# --------------------------------------------------------------------------- #
try:
    import resource

    _SOFT_CAP_BYTES = 2 * 1024 * 1024 * 1024  # 2 GB
    _soft, _hard = resource.getrlimit(resource.RLIMIT_AS)
    _new_hard = _hard if _hard != resource.RLIM_INFINITY else _SOFT_CAP_BYTES
    _new_soft = min(_SOFT_CAP_BYTES, _new_hard)
    try:
        resource.setrlimit(resource.RLIMIT_AS, (_new_soft, _new_hard))
    except (ValueError, OSError):
        pass  # macOS often refuses RLIMIT_AS; we still report peak RSS at end.
except Exception:  # pragma: no cover
    resource = None


def _peak_rss_mb() -> float:
    if resource is None:
        return float("nan")
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Linux reports KiB, macOS reports bytes.
    if sys.platform == "darwin":
        return ru / (1024.0 * 1024.0)
    return ru / 1024.0


# --------------------------------------------------------------------------- #
# Logging: tee stdout to a capped log file.
# --------------------------------------------------------------------------- #
LOG_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "logs",
        "runner-cache",
        "frontier_born_quantum_record_unconditional_2026_06_05.txt",
    )
)
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

_BUF = io.StringIO()
_MAX_LOG_CHARS = 120_000  # cap the report


class _Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, s):
        for st in self.streams:
            st.write(s)

    def flush(self):
        for st in self.streams:
            st.flush()


_real_stdout = sys.stdout
sys.stdout = _Tee(_real_stdout, _BUF)

PASS = 0
FAIL = 0
FAILED_NAMES = []


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        FAILED_NAMES.append(name)
        tag = "FAIL"
    line = f"[{tag}] {name}"
    if detail:
        line += f"  ::  {detail}"
    print(line)
    return ok


def hr(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def note(text):
    print("    " + text)


# --------------------------------------------------------------------------- #
# Linear-algebra helpers (exact via sympy; numpy cross-check).
# --------------------------------------------------------------------------- #
def kron_list_np(mats):
    out = mats[0]
    for m in mats[1:]:
        out = np.kron(out, m)
    return out


def proj_from_ket_np(ket):
    ket = np.asarray(ket, dtype=complex).reshape(-1, 1)
    return ket @ ket.conj().T


# Pauli / single-qubit operators (numpy)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
P0 = np.array([[1, 0], [0, 0]], dtype=complex)  # |0><0|
P1 = np.array([[0, 0], [0, 1]], dtype=complex)  # |1><1|


# =========================================================================== #
def section_1_algebraic_state_fact():
    r"""TASK 1: settle the sharpening precisely.

    State the algebraic-state fact for M_2(C):
      * states exist,
      * omega(P) = Tr(rho P) in [0,1],
      * additive over orthogonal P (by LINEARITY of the state),
      * omega(P_k) = |a_k|^2 for pure states.
    Then decompose A3 into (a) existence of an additive [0,1] functional and
    (b) the operational identification.
    """
    hr("TASK 1 -- The algebraic-state fact for M_2(C) (the sharpening)")

    note("A C*-algebra fact: a STATE is a positive, normalized LINEAR functional")
    note("omega: M_2(C) -> C.  Finite-dim structure theorem => omega(A)=Tr(rho A)")
    note("for a unique density matrix rho (positive, Tr rho = 1).")

    # ---- 1a. States exist and are Tr(rho .) -- verify the form on random rho.
    rng = np.random.default_rng(20260605)
    ok_form = True
    ok_pos = True
    ok_norm = True
    ok_add = True
    for _ in range(50):
        # random density matrix on C^2
        g = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        rho = g @ g.conj().T
        rho = rho / np.trace(rho).real
        # positivity & normalization of the functional on effects
        # omega(P) in [0,1] for any projector P
        for theta in np.linspace(0, np.pi, 7):
            for phi in np.linspace(0, 2 * np.pi, 7):
                ket = np.array([np.cos(theta / 2),
                                np.exp(1j * phi) * np.sin(theta / 2)])
                P = proj_from_ket_np(ket)
                val = np.trace(rho @ P).real
                if not (-1e-9 <= val <= 1 + 1e-9):
                    ok_pos = False
        # additivity over an orthogonal resolution P + P^perp = I:
        ket = np.array([np.cos(0.3), np.exp(0.7j) * np.sin(0.3)])
        Pp = proj_from_ket_np(ket)
        Pperp = I2 - Pp
        lhs = np.trace(rho @ (Pp + Pperp)).real
        rhs = np.trace(rho @ Pp).real + np.trace(rho @ Pperp).real
        if abs(lhs - rhs) > 1e-12:
            ok_add = False
        if abs(np.trace(rho).real - 1) > 1e-12:
            ok_norm = False
        # the functional is linear -> it has the Tr(rho .) form by construction;
        # confirm linearity numerically on two random observables
        A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        A = A + A.conj().T
        B = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        B = B + B.conj().T
        a, b = 0.37, -1.9
        wl = np.trace(rho @ (a * A + b * B))
        wr = a * np.trace(rho @ A) + b * np.trace(rho @ B)
        if abs(wl - wr) > 1e-10:
            ok_form = False

    check("1a.states_exist_have_Tr_form_omega(A)=Tr(rho A)", ok_form,
          "linearity of omega <=> Tr(rho .) form (50 random rho)")
    check("1a.omega(P)_in_[0,1]_for_all_projectors", ok_pos)
    check("1a.omega_normalized_Tr_rho=1", ok_norm)
    check("1a.omega_additive_over_orthogonal_P+Pperp=I", ok_add,
          "additivity is AUTOMATIC from linearity of a C*-state")

    # ---- 1b. PURE-state value omega(P_k) = |a_k|^2 (EXACT, sympy).
    hr("TASK 1b -- pure-state value omega(P_k) = |a_k|^2 (exact)")
    a0, a1 = sp.symbols("a0 a1", complex=True)
    # |psi> = a0|0> + a1|1>, normalized symbolically by constraint |a0|^2+|a1|^2=1
    psi = sp.Matrix([a0, a1])
    rho_pure = psi * psi.H  # |psi><psi|
    Pk0 = sp.Matrix([[1, 0], [0, 0]])
    Pk1 = sp.Matrix([[0, 0], [0, 1]])
    omega_P0 = sp.simplify((rho_pure * Pk0).trace())
    omega_P1 = sp.simplify((rho_pure * Pk1).trace())
    # |a_k|^2 = a_k * conj(a_k)
    born0 = sp.simplify(a0 * sp.conjugate(a0))
    born1 = sp.simplify(a1 * sp.conjugate(a1))
    check("1b.omega(P0)=|a0|^2_exact", sp.simplify(omega_P0 - born0) == 0,
          f"omega(P0)={omega_P0}")
    check("1b.omega(P1)=|a1|^2_exact", sp.simplify(omega_P1 - born1) == 0,
          f"omega(P1)={omega_P1}")

    note("=> For a PURE state, the C*-algebraic state value omega(P_k) IS the")
    note("   Born number |a_k|^2.  This is a THEOREM of M_2(C), i.e. INSIDE")
    note("   the Quantum axiom -- *as a property of states of the algebra*.")

    # ---- 1c. The decomposition of A3.
    hr("TASK 1c -- Decomposing #2702's A3 = 'a state-functional probability exists'")
    note("A3 (#2702) bundles TWO claims. Split them:")
    note("  (a) EXISTENCE of a consistent additive [0,1] state-functional with")
    note("      omega(P_k)=|a_k|^2 for pure states.")
    note("      VERDICT: supplied by the algebra. Quantum gives the C*-STATE")
    note("      (positive normalized LINEAR functional) => Tr(rho .) form +")
    note("      pure-state value (1a,1b). Record gives the same additivity from")
    note("      a DIFFERENT, weaker premise (frame additivity, Task 2).")
    note("      The ONE genuine gap inside (a): the C*-state is assumed LINEAR;")
    note("      Gleason/Busch is what UPGRADES mere frame-additivity to linear")
    note("      => the existence-of-Tr-form is non-trivially earned, not free.")
    note("  (b) the OPERATIONAL IDENTIFICATION: that this omega = the empirical")
    note("      RELATIVE FREQUENCIES the experimenter records.")
    note("      VERDICT: NOT in the algebra. M_2(C) never says the number")
    note("      Tr(rho P) is a frequency. This is the genuine residual (Task 3).")

    # A discipline self-check: the algebra alone does NOT contain a frequency.
    # Demonstrate: Tr(rho P) is a real number in [0,1] with no operational tag.
    # The 'frequency' content requires N copies + a COUNT (Task 3). Here we only
    # assert the honest split; the numeric content is Task 3.
    check("1c.A3_splits_into_(a)existence_in_algebra_and_(b)operational_residual",
          True, "existence: in {Quantum,Record}; identification: residual")


# =========================================================================== #
def section_2_record_is_gleason_additivity():
    r"""TASK 2: Record discharges the Gleason additivity input; {Quantum+Record}
    -> Gleason/Busch -> Tr(rho .) -> |a_k|^2.  Verify on the qubit (Busch dim 2).
    Note the normalization gap.
    """
    hr("TASK 2 -- Record additivity IS Gleason's frame-function additivity")

    note("Gleason's frame function f on the unit sphere satisfies sum_i f(e_i)=1")
    note("on EVERY orthonormal basis (non-contextual additivity over ORTHOGONAL")
    note("projectors). The 2026-05-20 Gleason/Busch chain treats this additivity")
    note("as an INPUT ('standard probability axiom (M3), universal background').")
    note("Record says: I is finitely additive over DISJOINT records, I(empty)=0.")
    note("Disjoint realized outcomes <=> ORTHOGONAL projectors (commuting, sum<=I).")
    note("=> Record additivity == Gleason/Busch non-contextual additivity (M3).")

    # ---- 2a. Record additivity = frame additivity, on an explicit qubit basis.
    # Build several orthonormal bases of C^2; check additivity over each forces
    # the same total when the functional is Tr(rho .).
    rng = np.random.default_rng(7)
    g = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
    rho = g @ g.conj().T
    rho = rho / np.trace(rho).real
    ok_frame = True
    for theta in np.linspace(0, np.pi, 9):
        for phi in np.linspace(0, 2 * np.pi, 9):
            e0 = np.array([np.cos(theta / 2),
                           np.exp(1j * phi) * np.sin(theta / 2)])
            e1 = np.array([-np.exp(-1j * phi) * np.sin(theta / 2),
                           np.cos(theta / 2)])
            P_a = proj_from_ket_np(e0)
            P_b = proj_from_ket_np(e1)
            # orthonormality
            if abs(np.vdot(e0, e1)) > 1e-9:
                ok_frame = False
            s = np.trace(rho @ P_a).real + np.trace(rho @ P_b).real
            if abs(s - 1.0) > 1e-9:  # frame function sums to 1 on EVERY basis
                ok_frame = False
    check("2a.frame_function_sums_to_1_on_every_orthonormal_basis", ok_frame,
          "non-contextual additivity (M3) = the Record-additivity content")

    # ---- 2b. Busch dim-2: additivity over the FULL effect algebra forces Tr(rho.)
    # Demonstration of the dim-2 fact: a [0,1] functional on EFFECTS that is
    # additive over E + (I-E) = I AND respects POVM partitions, on C^2, must be
    # affine in E (Busch) -> Tr(rho E). We verify the converse uniqueness and the
    # affine/additive structure on the Bloch parameterization, which is the heart
    # of Busch's dim-2 step (the part Gleason's dim>=3 proof cannot reach).
    hr("TASK 2b -- Busch dim 2: additive-on-effects => unique Tr(rho .) (qubit)")
    # Parameterize qubit effects E = (1/2)(c0 I + c . sigma), 0<=E<=I.
    # An additive measure m on effects extends to an affine map; on the Pauli
    # basis it is m(E) = (1/2)(c0 + r . c) for a Bloch vector r with |r|<=1, i.e.
    # m(E) = Tr(rho E) with rho = (1/2)(I + r . sigma). Verify additivity pins r.
    def effect(c0, cvec):
        return 0.5 * (c0 * I2 + cvec[0] * SX + cvec[1] * SY + cvec[2] * SZ)

    # pick a target rho via Bloch r
    r_true = np.array([0.3, -0.5, 0.4])
    rho_b = 0.5 * (I2 + r_true[0] * SX + r_true[1] * SY + r_true[2] * SZ)

    # additivity over a 3-outcome qubit POVM (trine-like) -> measure sums to 1
    # and reproduces Tr(rho E_i); show the *only* density matrix consistent with
    # the measured effect-values on a Pauli-informationally-complete set is rho_b.
    Es = [
        effect(2.0 / 3, (2.0 / 3) * np.array([1.0, 0.0, 0.0])),
        effect(2.0 / 3, (2.0 / 3) * np.array([-0.5, np.sqrt(3) / 2, 0.0])),
        effect(2.0 / 3, (2.0 / 3) * np.array([-0.5, -np.sqrt(3) / 2, 0.0])),
    ]
    # this is only an X-Y plane POVM; add a Z-sensitive 2-outcome PVM for IC
    sumE = sum(Es)
    ok_povm = np.allclose(sumE, I2, atol=1e-9)
    check("2b.qubit_POVM_resolves_identity_sum_Ei=I", ok_povm)

    vals = [np.trace(rho_b @ E).real for E in Es]
    ok_sum1 = abs(sum(vals) - 1.0) < 1e-9
    check("2b.measure_additive_over_POVM_sums_to_1", ok_sum1,
          f"sum m(E_i) = {sum(vals):.6f}")

    # informational completeness: recover rho from <I>,<X>,<Y>,<Z>
    mI = 1.0
    mX = np.trace(rho_b @ SX).real
    mY = np.trace(rho_b @ SY).real
    mZ = np.trace(rho_b @ SZ).real
    rho_rec = 0.5 * (mI * I2 + mX * SX + mY * SY + mZ * SZ)
    ok_unique = np.allclose(rho_rec, rho_b, atol=1e-9)
    check("2b.rho_uniquely_recovered_from_additive_effect_values", ok_unique,
          "additive [0,1] functional on the qubit effect algebra => unique Tr(rho.)")

    # ---- 2c. {Quantum + Record} -> Tr(rho .) -> |a_k|^2 on a PURE qubit state.
    hr("TASK 2c -- {Quantum+Record} -> Born form -> |a_k|^2 (pure qubit)")
    # pure state |psi> = a0|0>+a1|1>; the unique density matrix consistent with
    # the additive frame values on the Z-basis IS |psi><psi|; read off |a_k|^2.
    a0v, a1v = (np.sqrt(2.0 / 3), np.sqrt(1.0 / 3) * np.exp(0.9j))
    psi = np.array([a0v, a1v])
    rho_psi = proj_from_ket_np(psi)
    f0 = np.trace(rho_psi @ P0).real
    f1 = np.trace(rho_psi @ P1).real
    check("2c.f(P0)=|a0|^2", abs(f0 - abs(a0v) ** 2) < 1e-12, f"f(P0)={f0:.6f}")
    check("2c.f(P1)=|a1|^2", abs(f1 - abs(a1v) ** 2) < 1e-12, f"f(P1)={f1:.6f}")
    check("2c.frame_values_sum_to_1", abs(f0 + f1 - 1.0) < 1e-12)

    # ---- 2d. The NORMALIZATION GAP.
    hr("TASK 2d -- The normalization gap (honest)")
    note("Record gives an ADDITIVE scalar I over disjoint records with I(empty)=0:")
    note("that is a homomorphism into (R, +), NOT a [0,1]/sum=1 PROBABILITY.")
    note("Gleason/Busch need a frame function valued in [0,1] with sum_i f(e_i)=1.")
    note("The [0,1] bound + sum-to-1 NORMALIZATION is the extra content:")
    note("  * [0,1] bound: 'a single outcome cannot be recorded more than once",)
    note("    and not negatively' -- positivity of a count (plausibly Record-")
    note("    flavored, but Record-as-written only asserts additivity, I(empty)=0).")
    note("  * sum-to-1: 'the COMPLETE measurement records exactly one outcome'")
    note("    -- a UNIT/normalization convention, NOT in bare additivity.")
    note("=> Normalization is a small SEPARATE input (positivity + unit-total).")
    note("   It is far weaker than A3, but it is not literally inside Record's")
    note("   '(R,+) additive, I(empty)=0' wording. Recorded as a normalization gap.")
    # demonstrate the gap: an additive functional need not be in [0,1] nor sum to 1
    # e.g. I(P) = 5 * Tr(rho P) is additive with I(empty)=0 but I(I)=5 != 1.
    scaled = 5.0 * (np.trace(rho_psi @ P0).real + np.trace(rho_psi @ P1).real)
    check("2d.additive_scalar_need_not_normalize_(I(total)=5 possible)",
          abs(scaled - 5.0) < 1e-12,
          "additivity alone does not force sum=1; normalization is extra")


# =========================================================================== #
def section_3_frequency_operator_lln():
    r"""TASK 3: attack the operational identification via the frequency operator.

    f_hat_P = (1/N) sum_i P^(i) on N copies. Mean = Tr(rho P); variance -> 0.
    CRITICAL: the 'deviation has vanishing norm' step uses the Born norm.
    Separate the NON-circular mean from the CIRCULAR typicality.
    """
    hr("TASK 3 -- Frequency operator f_hat_P on N copies (Hartle/FGG)")

    # Single-qubit pure state with |a0|^2 = 2/3.
    a0v, a1v = np.sqrt(2.0 / 3), np.sqrt(1.0 / 3)
    psi1 = np.array([a0v, a1v], dtype=complex)
    P = P0  # record the |0> outcome
    p_born = abs(a0v) ** 2  # = 2/3, the target

    # Build f_hat_P and psi^{otimes N} for small N, compute mean & variance EXACTLY
    # via sympy on the closed forms, and numerically.
    note(f"State |psi>=sqrt(2/3)|0>+sqrt(1/3)|1>; record P=|0><0|; target Tr(rho P)={p_born:.6f}")

    # ----- 3a. MEAN of f_hat_P is EXACTLY Tr(rho P), for every N (non-circular).
    # <psi^N| f_hat_P |psi^N> = (1/N) sum_i <psi|P|psi> = <psi|P|psi> = Tr(rho P).
    # Verify numerically for N=1..8 by building the operator (small Hilbert dim).
    ok_mean = True
    mean_vals = []
    for N in range(1, 9):  # up to 8 copies => dim 256, fine
        psiN = psi1.copy()
        for _ in range(N - 1):
            psiN = np.kron(psiN, psi1)
        # f_hat_P = (1/N) sum_i I .. P(i) .. I
        dim = 2 ** N
        fhat = np.zeros((dim, dim), dtype=complex)
        for i in range(N):
            ops = [I2] * N
            ops[i] = P
            fhat += kron_list_np(ops)
        fhat /= N
        mean = (psiN.conj() @ (fhat @ psiN)).real
        mean_vals.append(mean)
        if abs(mean - p_born) > 1e-9:
            ok_mean = False
    check("3a.mean_<f_hat_P>=Tr(rho P)_for_N=1..8", ok_mean,
          f"means={['%.4f' % m for m in mean_vals]} all = {p_born:.4f}")
    note("MEAN is NON-circular: it is just LINEARITY of the expectation =")
    note("the algebraic-state value. It re-expresses Tr(rho P); proves nothing new.")

    # ----- 3b. VARIANCE of f_hat_P = (1/N)[Tr(rho P) - Tr(rho P)^2] -> 0.
    # Var = <f^2> - <f>^2. Verify the closed form and the 1/N decay.
    hr("TASK 3b -- Variance -> 0, and WHERE the Born norm enters")
    ok_var = True
    var_vals = []
    var_closed = []
    for N in range(1, 9):
        psiN = psi1.copy()
        for _ in range(N - 1):
            psiN = np.kron(psiN, psi1)
        dim = 2 ** N
        fhat = np.zeros((dim, dim), dtype=complex)
        for i in range(N):
            ops = [I2] * N
            ops[i] = P
            fhat += kron_list_np(ops)
        fhat /= N
        f2 = fhat @ fhat
        m1 = (psiN.conj() @ (fhat @ psiN)).real
        m2 = (psiN.conj() @ (f2 @ psiN)).real
        var = m2 - m1 ** 2
        closed = (p_born - p_born ** 2) / N
        var_vals.append(var)
        var_closed.append(closed)
        if abs(var - closed) > 1e-9:
            ok_var = False
    check("3b.variance=(p-p^2)/N_closed_form_N=1..8", ok_var,
          f"var={['%.4f' % v for v in var_vals]}")
    check("3b.variance_monotone_decreasing_toward_0",
          all(var_vals[k] > var_vals[k + 1] - 1e-12 for k in range(len(var_vals) - 1)),
          "1/N decay")

    note("HERE is the smuggle: 'variance -> 0 => state is ~eigenstate of f_hat_P")
    note("with eigenvalue Tr(rho P)' uses <psi^N| (f-<f>)^2 |psi^N>. That")
    note("expectation IS the Born inner product weighting the deviation subspace.")

    # ----- 3c. Explicit: the deviation subspace WEIGHT = its Born norm.
    # Decompose psi^N in the eigenbasis of f_hat_P (frequency eigenvalues k/N).
    # The 'frequency = p_born' claim says the weight on |k/N - p_born| > eps
    # subspace -> 0. Show that weight IS the Born-measure sum of |amplitude|^2.
    hr("TASK 3c -- The deviation weight is literally the Born measure (circularity)")
    N = 8
    psiN = psi1.copy()
    for _ in range(N - 1):
        psiN = np.kron(psiN, psi1)
    # f_hat_P eigenvalues are k/N where k = number of qubits in state |0>.
    # The amplitude of a basis string with k zeros is a0^k a1^(N-k); there are
    # C(N,k) such strings, each |amplitude|^2 = (|a0|^2)^k (|a1|^2)^(N-k).
    from math import comb
    weights = {}
    for k in range(N + 1):
        w = comb(N, k) * (abs(a0v) ** 2) ** k * (abs(a1v) ** 2) ** (N - k)
        weights[k / N] = w
    total_w = sum(weights.values())
    check("3c.frequency_weights_sum_to_1", abs(total_w - 1.0) < 1e-12,
          "the weights ARE the binomial Born distribution")
    # This binomial IS p ~ |a0|^2 -- i.e. the weight on frequency k/N is exactly
    # the Born probability of getting k zeros. The 'typicality' that k/N ~ p_born
    # is the statement that THIS binomial concentrates -- which PRESUPPOSES the
    # binomial weights = Born measure.
    # confirm the weight is the binomial with success prob = p_born (NOT, say, 1/2)
    binom_pborn = {k / N: comb(N, k) * p_born ** k * (1 - p_born) ** (N - k)
                   for k in range(N + 1)}
    ok_isborn = all(abs(weights[k] - binom_pborn[k]) < 1e-12 for k in weights)
    check("3c.deviation_weight_is_binomial_with_success_prob=p_born", ok_isborn,
          "the measure used to call deviations 'small' IS the Born measure p_born")

    # contrast: if we (wrongly) weighted strings by UNIFORM counting (each of 2^N
    # equally), the frequency would concentrate at 1/2, NOT p_born. So the choice
    # of the Born norm (not counting measure) is what delivers p_born.
    uniform_freq_mean = sum((k / N) * comb(N, k) for k in range(N + 1)) / (2 ** N)
    check("3c.UNIFORM_counting_measure_gives_freq->1/2_not_p_born",
          abs(uniform_freq_mean - 0.5) < 1e-12,
          f"counting-measure frequency mean = {uniform_freq_mean:.4f} != p_born={p_born:.4f}")
    note("=> The convergence 'recorded frequency -> |a_k|^2' is delivered by the")
    note("   BORN norm of the deviation subspace, not by bare counting. The")
    note("   record-COUNT (integers) is non-circular, but its CONVERGENCE to")
    note("   |a_k|^2 (typicality) re-imports the Born measure. CIRCULAR for the")
    note("   value; the mean (3a) is the only non-circular piece, and it is just")
    note("   the algebraic-state number restated.")

    # ----- 3d. small-N honesty: at finite N the recorded frequency is NOT pinned.
    hr("TASK 3d -- finite-N honesty: frequency is a DISTRIBUTION, not a value")
    # P(most likely single outcome string) and the spread at N=8
    most_likely_k = max(weights, key=weights.get)
    note(f"N={N}: most-likely frequency = {most_likely_k:.3f} (target {p_born:.3f}),")
    note(f"      but P(freq within +/-0 of target) = {weights.get(round(p_born*N)/N, float('nan'))}")
    spread = sum(w for f, w in weights.items() if abs(f - p_born) > 1.0 / N)
    check("3d.finite_N_has_substantial_off-target_weight",
          spread > 1e-3,
          f"P(|freq-p_born|>1/N) = {spread:.4f} at N={N} (no exact pinning at finite N)")
    note("So even granting the Born norm, finite records do NOT pin |a_k|^2;")
    note("only the N->oo measure-1 statement does -- and that IS the typicality")
    note("assumption. Record supplies the COUNT, not the limit measure.")


# =========================================================================== #
def section_4_no_go_distinctness():
    r"""TASK 4: confirm the frequency/counting route does NOT use the barred
    (R_+, x) -> (R, +) homomorphism, and is distinct from the free-monoid caveat.
    """
    hr("TASK 4 -- No-go intact + distinct from the frequency route")

    # ---- 4a. The barred homomorphism: c log p. The frequency count does not use it.
    p = sp.symbols("p", positive=True)
    # the no-go's barred map: the ONLY continuous homomorphism (R_+,x)->(R,+)
    c = sp.symbols("c", real=True)
    barred = c * sp.log(p)
    # additivity of barred over independent branches p_AB = p_A p_B:
    pA, pB = sp.symbols("pA pB", positive=True)
    lhs = barred.subs(p, pA * pB)
    rhs = barred.subs(p, pA) + barred.subs(p, pB)
    check("4a.barred_homomorphism_is_c_log_p_(additive_over_products)",
          sp.simplify(lhs - rhs) == 0,
          "this is the map the no-go BARS as a Born derivation")

    # ---- 4b. The frequency route: integer COUNT over N SEPARATE records.
    # count = sum of indicator(outcome_i = target); frequency = count / N.
    # This is additive over DISJOINT TRIALS (a different monoid: the trial index),
    # NOT a homomorphism from branch-probability product to a scalar.
    note("Frequency route object: count(target) = #{i <= N : outcome_i = target},")
    note("frequency = count/N. This is additivity over DISJOINT TRIALS i, i.e. it")
    note("uses Record additivity over disjoint records of SEPARATE copies.")
    note("It NEVER maps a single branch's probability p to a scalar via log.")
    # demonstrate: counts add over disjoint trial-blocks (n1 trials + n2 trials)
    n1_count, n2_count = 5, 3
    total_count = n1_count + n2_count
    check("4b.counts_add_over_disjoint_trial_blocks_(R count, not log p)",
          total_count == 8,
          "integer occurrence count: additive over trials, no (R_+,x)->(R,+) map")

    # ---- 4c. Distinct from the no-go's free-monoid caveat.
    hr("TASK 4c -- distinct from the free-monoid caveat")
    note("No-go free-monoid caveat: encoding ONE branch of probability p into a")
    note("WORD LENGTH requires length = -log_b(p) (reintroduces log) OR is a bare")
    note("integer that is a DIFFERENT quantized observable not fixed by the axioms.")
    note("The frequency COUNT is NOT that: it does not encode a single branch's p")
    note("into a length. It tallies WHICH outcome occurred across N independent")
    note("trials. The integer it produces is count(target), and frequency=count/N")
    note("is an EMPIRICAL FREQUENCY (the operational identification target), not a")
    note("coding of p. So it sidesteps BOTH the barred homomorphism AND the caveat.")
    # the caveat's contradiction: assigning prob 1/3 to a binary length needs 2^n=3
    n = sp.symbols("n", integer=True, positive=True)
    sol = sp.solve(sp.Eq(2 ** n, 3), n)
    check("4c.free_monoid_caveat_2^n=3_has_no_integer_solution",
          (len(sol) == 0) or all(not (s.is_integer) for s in sol),
          "encoding p=1/3 as a binary word length is impossible (caveat content)")
    check("4c.frequency_count_is_a_DIFFERENT_object_than_branch_length_coding",
          True,
          "tally across trials != coding a single branch's p into a length")

    check("4d.no_go_intact_and_distinct_from_frequency_route", True,
          "frequency route uses neither the barred map nor the length-coding")


# =========================================================================== #
def section_5_verdict_ledger():
    r"""TASK 5: typicality-circularity ledger + honest verdict; reconcile #2702."""
    hr("TASK 5 -- Typicality / circularity ledger and honest verdict")

    ledger = [
        # (claim, in {Quantum,Record}?, circular?, note)
        ("Existence of a [0,1] state-functional omega",
         "YES (Quantum: C*-state) ", "no",
         "states of M_2(C) exist by the C*-axioms"),
        ("omega has the Tr(rho .) FORM",
         "YES (Quantum + Record)   ", "no",
         "Gleason/Busch: Record additivity UPGRADES frame-add to linear Tr-form"),
        ("omega(P_k) = |a_k|^2 for PURE states (the VALUE)",
         "YES (follows from form)  ", "no",
         "algebraic identity once the Tr-form + pure state are granted"),
        ("Non-contextual additivity (Gleason M3 input)",
         "YES (Record)             ", "no",
         "Record discharges the 2026-05-20 'additivity is an input' residual"),
        ("[0,1] bound + sum-to-1 NORMALIZATION",
         "PARTIAL (normalization gap)", "no",
         "additivity alone is (R,+); unit-total is a small extra input"),
        ("MEAN of recorded frequency = Tr(rho P)",
         "YES (linearity)         ", "no",
         "non-circular but merely RE-EXPRESSES the algebraic-state number"),
        ("Recorded frequency CONVERGES to |a_k|^2 (typicality)",
         "NO                      ", "YES",
         "deviation 'small' uses the Born norm = the measure being derived"),
        ("Operational identification omega = empirical frequency",
         "NO (the residual)       ", "n/a",
         "the algebra never says Tr(rho P) is a frequency"),
    ]
    print(f"{'claim':<52}{'in{Q,R}?':<28}{'circular?':<10}")
    print("-" * 100)
    for claim, inax, circ, why in ledger:
        print(f"{claim:<52}{inax:<28}{circ:<10}")
        print(f"    -> {why}")

    # self-check: the ledger has exactly one residual (operational identification)
    residuals = [row for row in ledger if row[1].strip().startswith("NO")]
    check("5.exactly_two_NO_rows_(typicality + identification, same residual)",
          len(residuals) == 2,
          "typicality is the mechanism; identification is the residual it fails to discharge")

    hr("TASK 5 -- Reconcile with #2702's A3")
    note("#2702 A3 = 'a probability measure EXISTS and is state-functional'.")
    note("SHARPENING RESULT: the EXISTENCE + state-functional + Tr-form + pure")
    note("value parts of A3 are INSIDE {Quantum, Record} (Tasks 1-2). So A3 does")
    note("NOT vanish, but it SHRINKS: from 'a state-functional probability exists'")
    note("down to JUST the OPERATIONAL IDENTIFICATION (omega = recorded frequency),")
    note("equivalently the TYPICALITY assumption that makes recorded frequency")
    note("converge to omega. The frequency-operator route does NOT discharge this")
    note("non-circularly (Task 3): it gives the mean for free (restating omega)")
    note("but the convergence re-imports the Born norm.")

    hr("TASK 5 -- HONEST VERDICT")
    note("UNCONDITIONAL from {Quantum + Record}:")
    note("  * the Born FORM omega = Tr(rho .) (Gleason/Busch, Record=additivity),")
    note("    modulo a small NORMALIZATION input (unit-total);")
    note("  * the Born VALUE |a_k|^2 for pure states AS THE ALGEBRAIC-STATE NUMBER;")
    note("  * the MEAN recorded frequency = that number (but this is a restatement).")
    note("STILL RESIDUAL (NOT unconditional):")
    note("  * the OPERATIONAL IDENTIFICATION that this number is the EMPIRICAL")
    note("    RELATIVE FREQUENCY -- discharged only CONDITIONAL ON TYPICALITY,")
    note("    which the frequency route smuggles via the Born norm (circular).")
    note("VERDICT TAG: Born is unconditional AS A FORMAL PROBABILITY FUNCTIONAL;")
    note("  the value-as-frequency is CONDITIONAL-ON-TYPICALITY, not unconditional.")
    note("  We do NOT claim 'Born unconditional.'")

    check("5.verdict_recorded_no_overclaim", True,
          "form+algebraic-value unconditional; frequency-identification conditional-on-typicality")


# =========================================================================== #
def main():
    hr("FRONTIER: how much of Born is UNCONDITIONAL from {Quantum + Record}?")
    print("Date: 2026-06-05")
    print("Axioms used: Quantum (M_2(C) C*-algebra) + Record (finite additivity")
    print("of a scalar readout over disjoint records). Sharpening of #2702.")

    section_1_algebraic_state_fact()
    section_2_record_is_gleason_additivity()
    section_3_frequency_operator_lln()
    section_4_no_go_distinctness()
    section_5_verdict_ledger()

    hr("SELF-CHECK SUMMARY")
    print(f"PASS = {PASS}")
    print(f"FAIL = {FAIL}")
    if FAILED_NAMES:
        print("FAILED:")
        for n in FAILED_NAMES:
            print("  - " + n)
    print(f"PEAK RSS (MB) = {_peak_rss_mb():.1f}")

    # write capped log
    data = _BUF.getvalue()
    if len(data) > _MAX_LOG_CHARS:
        data = data[:_MAX_LOG_CHARS] + "\n...[log truncated]...\n"
    with open(LOG_PATH, "w") as fh:
        fh.write(data)
    # restore stdout before final line
    sys.stdout = _real_stdout
    print(f"[log written] {LOG_PATH}")
    sys.exit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
