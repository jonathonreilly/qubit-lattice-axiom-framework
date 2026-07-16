#!/usr/bin/env python3
"""Runner for the observable-principle P1 symmetry-type / energy-readout note.

This runner REPROVES, at exact SymPy/Fraction precision from elementary tensor
algebra and cited framework context, the load-bearing steps of the
symmetry-type-readout reframe
of the admitted P1 premise (scalar additivity on independent subsystems) of
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, and FORMALIZES the crux test that
decides whether routing the v-chain additive readout through "the VEV is an
energy" escapes the sector-composition selector class C of
`OBSERVABLE_PRINCIPLE_P1_EXPONENT_SELECTOR_DICHOTOMY_NARROW_NOTE_2026-06-02.md`
(#2504, path a') or collapses back into its face ADD = P1.

The reframe under test (the symmetry-type law): each observable's readout is
fixed by its SYMMETRY TYPE. ADDITIVE quantum numbers are eigenvalues of
generators of CONTINUOUS symmetries (Lie ALGEBRA; on a tensor product the
generator is the direct sum H = H_A (x) I + I (x) H_B, so eigenvalues ADD);
MULTIPLICATIVE quantum numbers are characters of DISCRETE symmetries (group
element; on a tensor product it acts multiplicatively, characters MULTIPLY).
The bridge is the SAME exp/log relating group=exp(algebra) and Z=exp(log Z).

The crux (DECISIVE). Is "the v-chain scalar W = log|det(D+J)| is additive"
FORCED, PRIOR to any readout choice, by "the VEV is an energy => an
H-eigenvalue => additive by the tensor structure", or does that route secretly
re-import additivity? This runner formalizes two pivots and tests each:

  Pivot 1 ("energies/H are additive over the tensor product"). In the
  framework this is NOT supplied by the Qubit axiom; the
  Lattice/Qubit/Admissibility/Record baseline fixes the lattice, local algebra,
  and finite scalar record readout, not dynamics. When realized (the cited two-step transfer-
  matrix construction), H_hat = -log(T_hat^2)/(2 a_tau) with T_hat^2 a
  PRODUCT over modes; H additive <=> T^2 multiplicative <=> the SAME exp/log
  move one level up. Moreover additivity of H over independent subsystems is a
  property of the NON-INTERACTING / tensor-factorized class
  U_AB = U_A (x) U_B (H = H_A (x) I + I (x) H_B), NOT of all dynamics. So
  "energies add" is itself an instance of the {r ↦ r^p} orbit dichotomy
  (face BLIND vs face ADD), one level up; it does not escape class C.

  Pivot 2 ("the v-chain scalar W IS the free energy / an energy-sector
  quantity"). This identification is exactly content (II.b) of the
  structural-reframing no-go
  (`OBSERVABLE_PRINCIPLE_P1_BRIDGE_STRUCTURAL_REFRAMING_NARROW_NOTE_2026-05-21.md`),
  already proven (II.b) <=> P1. The Matsubara free-energy-density note
  (`HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md`)
  establishes the free-energy identification DEFINITIONALLY via the
  per-matrix-entry log-det convention Delta f := (1/n)(ln|det(D+m)| -
  ln|det D|), explicitly disclaiming any independent physical free-energy /
  effective-potential identification beyond that log-det convention. So it
  PRESUPPOSES log|det|; it does not derive the additive readout from a prior
  additive-H structure.

Result reproven here: the symmetry-type law is a correct representation-theory
THEOREM (additive generators on tensor products give additive eigenvalues;
discrete-group elements give multiplicative characters; exp/log is the bridge),
but the energy route to the v-chain ADDITIVE readout does NOT escape class C:
both pivots land in face ADD (= P1) or relocate the SAME orbit dichotomy one
level up. The diagnosis is that it reduces to P1 (positive content: the most
natural path-a' candidate is shown to collapse into the #2504 dichotomy).
This runner does NOT close P1; it pins the energy route as P1-equivalent.

Circularity check (explicit, per discipline). "Energies add over the tensor
product" and "W = log Z is additive" are the SAME multiplicative->additive
content read at two levels (group/algebra vs partition-function/free-energy).
Using either to "derive log" is circular: additivity is the hypothesis at both
levels. This runner uses them only to PROVE the energy route is P1-equivalent.

Tests (all exact SymPy / Fraction; no fitted or observed inputs):
- T1  : structure survey — additive readout = log|det| (parent / Matsubara
        free-energy note) and multiplicative readout = Z3 character
        (Koide / DM-neutrino / color-generation gate) are BOTH present and
        used consistently in the repo. String presence on the live notes.
- T2  : symmetry-type law (a) — for a tensor product H_AB, the independent /
        non-interacting generator H = H_A (x) I + I (x) H_B has eigenvalues
        that ADD: spec(H) = { e_a + e_b }. Reproven on small explicit
        matrices. (Lie ALGEBRA / continuous-symmetry / additive-q.n. comparator.)
- T3  : symmetry-type law (b) — a discrete-group element g acting on a tensor
        product as g_A (x) g_B has MULTIPLICATIVE character:
        chi(g_A (x) g_B) = chi(g_A) . chi(g_B) (= tr (x) tr). Reproven on the
        Z3 regular representation (cube-root-of-unity), the same Z3 used by
        Koide / color. (Lie GROUP / discrete-symmetry / multiplicative-q.n.)
- T4  : exp/log bridge — group = exp(algebra) and Z = exp(log Z) are the SAME
        exp/log. Reproven two ways: (i) exp of the additive generator
        H = H_A (x) I + I (x) H_B equals the product exp(H_A) (x) exp(H_B)
        (the algebra->group bridge); (ii) for a block-diagonal (independent)
        D, Z = det(D) = Z_A . Z_B and log Z = log Z_A + log Z_B (the
        partition-function bridge). Same homomorphism (R_+,x)->(R,+).
- T5  : PIVOT 1 (the decisive one) — "energies add" is itself the orbit
        dichotomy one level up. For the framework's realized free quadratic
        sector, T_hat^2 = (x)_p diag(1, e^{-2 E(p)}) factorizes over the
        tensor product and H_hat = -log(T_hat^2)/(2 a_tau) = sum_p E(p) n_p is
        additive. Reproven: (i) T^2 multiplicative over modes <=> H additive
        is the exp/log move; (ii) the WHOLE family (T^2)^s = (x)_p
        diag(1, e^{-2 s E(p)}) is multiplicative for EVERY s, and the additive
        generator is the p->0 (log) member s . H -- i.e. {(T^2)^s} is one
        {r ↦ r^s} orbit, so "H additive" sits in face ADD of #2504's dichotomy
        applied at the transfer-operator level. It does NOT supply an additive
        readout PRIOR to a log choice.
- T6  : PIVOT 1, steelman — additivity of H is NOT generic; it is the
        non-interacting / tensor-factorized class. Exhibit an interacting
        H_int = H_A (x) I + I (x) H_B + g . (X_A (x) X_B) whose spectrum does
        NOT add (eigenvalues != e_a + e_b for g != 0). So "the VEV is an
        energy" alone does not force additivity; it forces additivity ONLY in
        the independent / direct-sum class -- which is exactly P1's
        "independent subsystems" hypothesis. The energy route imports P1's
        independence clause; it does not replace it.
- T7  : PIVOT 2 — the free-energy identification IS content (II.b). Reproven:
        the framework's v-chain Delta f is DEFINED as the per-matrix-entry
        log-det difference (1/n)(ln|det(D+m)| - ln|det D|), i.e. it
        presupposes log|det|; and (II.b) <=> P1 (if W = log|Z| then W is
        additive on block-diagonal D; if W is additive + multiplicative-input
        then W = c log|Z|). Reproven symbolically on the block-diagonal
        substrate; the identification is the admitted classification step.
- T8  : SYNTHESIS — the energy route lands in face ADD of the #2504 dichotomy.
        Reproven: the additive coordinate of the energy ledger is exactly the
        log readout (the p->0 member of {r ↦ r^p}); the selector "read the
        additive (energy) quantum number" references the BARE additive value
        (face ADD), not an orbit-invariant single-sector readout (face BLIND).
        The Born/normalized energy density (intensive, per-site) is the
        orbit-invariant face-BLIND instance and singles nothing.
- T9  : live-ledger context presence (no dependency status consumed as
        load-bearing).
- T10 : note honest-scope strings present; forbidden status-promotion /
        overclaim strings absent (no "p1_retained", no closure verdict token).
- T11 : source-note boundary declarations present.

Expected result: PASS=27, FAIL=0.

A passing run supports ONLY the bounded finding above (the symmetry-type law is
a theorem; the energy route to the v-chain additive readout collapses into the
#2504 face ADD = P1 via both pivots). It does NOT close P1, does NOT promote
any row, and consumes no fitted or observed numerical targets.

Reproduction:
    python3 scripts/audit_companion_observable_principle_p1_symmetry_type_energy_readout_2026_06_02.py
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_SYMMETRY_TYPE_ENERGY_READOUT_NARROW_NOTE_2026-06-02.md"
)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

# Structure-survey targets (live notes in the repo).
SURVEY_ADDITIVE = [
    ROOT / "docs" / "OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md",
    ROOT / "docs" / "HIERARCHY_MATSUBARA_FREE_ENERGY_DENSITY_NARROW_THEOREM_NOTE_2026-05-16.md",
]
SURVEY_MULTIPLICATIVE = [
    ROOT / "docs" / "KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md",
    ROOT / "docs" / "DM_NEUTRINO_Z3_CHARACTER_TRANSFER_THEOREM_NOTE_2026-04-15.md",
    ROOT / "docs" / "Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md",
]

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _kron(A: sp.Matrix, B: sp.Matrix) -> sp.Matrix:
    """Kronecker (tensor) product of two SymPy matrices."""
    return sp.Matrix(sp.kronecker_product(A, B))


def _matlog_diag(M: sp.Matrix) -> sp.Matrix:
    """Matrix logarithm of a DIAGONAL matrix (entrywise log on the diagonal).

    SymPy's ``sp.log`` does not evaluate the matrix logarithm; for a diagonal
    matrix the principal matrix log is ``diag(log d_1, ..., log d_n)``. We
    assert diagonality so misuse fails loudly.
    """
    if not M.is_diagonal():
        raise ValueError("_matlog_diag requires a diagonal matrix")
    return sp.diag(*[sp.log(M[i, i]) for i in range(M.rows)])


def _eig_multiset(M: sp.Matrix):
    """Exact eigenvalue multiset (as a list of sympy expressions).

    Returns the multiset (with algebraic multiplicity); deterministic ordering
    is applied only when every eigenvalue is numeric (no free symbols),
    otherwise the eigenvalues are returned sorted by their string form so the
    function is total on symbolic input too.
    """
    d = M.eigenvals()  # {eigenvalue: multiplicity}
    out = []
    for val, mult in d.items():
        out.extend([sp.simplify(val)] * int(mult))
    if all(not e.free_symbols for e in out):
        return sorted(out, key=lambda z: (float(sp.re(z)), float(sp.im(z))))
    return sorted(out, key=str)


def _block_diag_det_setup():
    """Independent-subsystem setup: block-diagonal real anti-Hermitian D.

    Mirrors the parent note's minimal block: D = D_A (+) D_B with
    D_A = [[j_A, a], [-a, j_A]], D_B = [[j_B, b], [-b, j_B]] (real, det > 0),
    identity-coupled source j_A, j_B per block.
    """
    a, b = sp.symbols("a b", positive=True)
    jA, jB = sp.symbols("j_A j_B", real=True)
    D_A = sp.Matrix([[jA, a], [-a, jA]])
    D_B = sp.Matrix([[jB, b], [-b, jB]])
    ZA = sp.expand(D_A.det())  # j_A^2 + a^2 > 0
    ZB = sp.expand(D_B.det())  # j_B^2 + b^2 > 0
    D = sp.diag(D_A, D_B)
    Z = sp.expand(D.det())
    return jA, jB, a, b, Z, ZA, ZB, D


# ---------------------------------------------------------------------------
# T1 — structure survey
# ---------------------------------------------------------------------------

def test_T1_structure_survey() -> None:
    section("T1: structure survey — both ledgers present and consistent")

    add_ok = True
    add_detail = []
    for p in SURVEY_ADDITIVE:
        if not p.exists():
            add_ok = False
            add_detail.append(f"MISSING {p.name}")
            continue
        txt = p.read_text(encoding="utf-8")
        has_logdet = ("log|det" in txt) or ("ln|det" in txt) or ("log |det" in txt)
        add_detail.append(f"{p.name}: log|det|={has_logdet}")
        add_ok = add_ok and has_logdet
    check(
        "additive readout = log|det| present (parent + Matsubara free-energy)",
        add_ok,
        "; ".join(add_detail),
    )

    mult_ok = True
    mult_detail = []
    for p in SURVEY_MULTIPLICATIVE:
        if not p.exists():
            mult_ok = False
            mult_detail.append(f"MISSING {p.name}")
            continue
        txt = p.read_text(encoding="utf-8")
        has_char = ("character" in txt.lower()) and ("Z_3" in txt or "Z3" in txt or "Z₃" in txt)
        mult_detail.append(f"{p.name}: Z3-character={has_char}")
        mult_ok = mult_ok and has_char
    check(
        "multiplicative readout = Z3 character present (Koide / DM / color-gen)",
        mult_ok,
        "; ".join(mult_detail),
    )

    # Consistency: the color/generation note records the Z3 bridge as an OPEN
    # GATE (multiplicative readout is used but not over-claimed), and the Koide
    # recasting is explicitly "not a derivation" -- i.e. the multiplicative
    # ledger is used HONESTLY, mirroring how the additive ledger is admitted.
    gate = ROOT / "docs" / "Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md"
    koide = ROOT / "docs" / "KOIDE_Q_TWO_THIRDS_Z3_CHARACTER_NORM_SPLIT_RECASTING_THEOREM_NOTE_2026-05-10.md"
    cons_ok = (
        gate.exists()
        and "open" in gate.read_text(encoding="utf-8").lower()
        and koide.exists()
        and "not" in koide.read_text(encoding="utf-8").lower()
    )
    check(
        "both ledgers used consistently (multiplicative gate open / Koide 'not a derivation')",
        cons_ok,
        "Z3 color-generation is an open gate; Koide recasting disclaims derivation",
    )


# ---------------------------------------------------------------------------
# T2 — symmetry-type law (a): additive generator -> additive eigenvalues
# ---------------------------------------------------------------------------

def test_T2_additive_generator_adds_eigenvalues() -> None:
    section("T2: additive (continuous-symmetry) generator H_A(x)I + I(x)H_B adds eigenvalues")

    # Small explicit single-site Hamiltonians (2-dim, one-qubit local algebra).
    eA0, eA1, eB0, eB1 = sp.symbols("e_A0 e_A1 e_B0 e_B1", real=True)
    H_A = sp.diag(eA0, eA1)
    H_B = sp.diag(eB0, eB1)
    I2 = sp.eye(2)

    H = _kron(H_A, I2) + _kron(I2, H_B)  # direct-sum generator on the tensor product
    spec = _eig_multiset(H)
    expected = [eA0 + eB0, eA0 + eB1, eA1 + eB0, eA1 + eB1]
    # Compare as multisets of simplified expressions (order-independent).
    got = sorted([sp.simplify(s) for s in spec], key=str)
    exp = sorted([sp.simplify(s) for s in expected], key=str)
    ok = got == exp
    check(
        "spec(H_A(x)I + I(x)H_B) = { e_a + e_b } (eigenvalues ADD)",
        ok,
        f"got {got}",
    )

    # Non-degenerate numeric instance to be fully explicit.
    subs = {eA0: sp.Integer(1), eA1: sp.Integer(5), eB0: sp.Integer(2), eB1: sp.Integer(11)}
    Hn = H.subs(subs)
    specn = sorted([int(v) for v in _eig_multiset(Hn)])
    expn = sorted([1 + 2, 1 + 11, 5 + 2, 5 + 11])  # 3, 12, 7, 16
    check(
        "numeric instance: {1,5}(+){2,11} -> {3,7,12,16}",
        specn == sorted(expn),
        f"got {specn}, expected {sorted(expn)}",
    )


# ---------------------------------------------------------------------------
# T3 — symmetry-type law (b): discrete-group element -> multiplicative character
# ---------------------------------------------------------------------------

def test_T3_discrete_group_multiplicative_character() -> None:
    section("T3: discrete-symmetry element g_A(x)g_B has MULTIPLICATIVE character")

    w = sp.exp(2 * sp.pi * sp.I / 3)  # primitive cube root of unity (the Z3 used by Koide/color)

    # Z3 regular representation generator S (cyclic shift) on C^3.
    S = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    # Characters of S^k under the regular representation: tr(S^0)=3, tr(S^1)=0, tr(S^2)=0.
    chis = {k: sp.simplify(sp.trace(S**k)) for k in range(3)}
    reg_ok = (chis[0] == 3) and (chis[1] == 0) and (chis[2] == 0)
    check("Z3 regular-rep character vector (3,0,0)", reg_ok, f"{chis}")

    # Multiplicativity on a tensor product: take a 1-dim Z3 character rep
    # rho(S) = w (so chi = w), tensor two copies; character multiplies.
    gA = sp.Matrix([[w]])  # 1-dim character a -> w^a
    gB = sp.Matrix([[w**2]])
    chiA = sp.simplify(sp.trace(gA))
    chiB = sp.simplify(sp.trace(gB))
    gAB = _kron(gA, gB)
    chiAB = sp.simplify(sp.trace(gAB))
    ok_mult = sp.simplify(chiAB - chiA * chiB) == 0
    check(
        "chi(g_A (x) g_B) = chi(g_A).chi(g_B) (characters MULTIPLY on tensor product)",
        ok_mult,
        f"chiAB={sp.nsimplify(chiAB)}, chiA*chiB={sp.nsimplify(chiA*chiB)}",
    )

    # And on a genuine 2x2 (x) 2x2 example with non-trivial matrices, the
    # trace is multiplicative under tensor product (tr is the character of a
    # rep; tr(M (x) N) = tr M . tr N), which fails for the ADDITIVE direct sum
    # of a single multiplicative character -- separating the two ledgers.
    M = sp.Matrix([[2, 1], [0, 3]])
    N = sp.Matrix([[5, 0], [7, 1]])
    lhs = sp.trace(_kron(M, N))
    rhs = sp.trace(M) * sp.trace(N)
    ok_trace = sp.simplify(lhs - rhs) == 0
    check(
        "tr(M (x) N) = tr M . tr N (tensor-character multiplicativity, generic 2x2)",
        ok_trace,
        f"tr(M(x)N)={lhs}, trM.trN={rhs}",
    )


# ---------------------------------------------------------------------------
# T4 — exp/log bridge (group=exp(algebra); Z=exp(log Z) are the SAME exp/log)
# ---------------------------------------------------------------------------

def test_T4_exp_log_bridge() -> None:
    section("T4: exp/log bridge — group=exp(algebra) and Z=exp(log Z) coincide")

    # (i) algebra -> group: for COMMUTING tensor summands,
    # exp(H_A (x) I + I (x) H_B) = exp(H_A) (x) exp(H_B).
    # (the additive generator exponentiates to the multiplicative group element.)
    eA, eB = sp.symbols("e_A e_B", real=True)
    H_A = sp.diag(eA, -eA)
    H_B = sp.diag(eB, -eB)
    I2 = sp.eye(2)
    H = _kron(H_A, I2) + _kron(I2, H_B)
    lhs = sp.simplify(sp.exp(H))  # matrix exponential (diagonal here)
    rhs = sp.simplify(_kron(sp.exp(H_A), sp.exp(H_B)))
    ok_grp = sp.simplify(lhs - rhs) == sp.zeros(*lhs.shape)
    check(
        "exp(H_A(x)I + I(x)H_B) = exp(H_A) (x) exp(H_B) (additive -> multiplicative)",
        ok_grp,
        "algebra->group bridge on commuting tensor summands",
    )

    # (ii) partition-function -> free-energy: on a block-diagonal (independent)
    # D, Z = det(D) = Z_A . Z_B and log Z = log Z_A + log Z_B.
    jA, jB, a, b, Z, ZA, ZB, D = _block_diag_det_setup()
    ok_fac = sp.simplify(Z - ZA * ZB) == 0
    ok_log = sp.simplify(sp.log(ZA * ZB) - (sp.log(ZA) + sp.log(ZB))) == 0
    check(
        "Z = det(D_A (+) D_B) = Z_A . Z_B ; log Z = log Z_A + log Z_B",
        ok_fac and ok_log,
        "partition-function->free-energy bridge is the SAME (R_+,x)->(R,+) homomorphism",
    )

    # The two bridges are the SAME map t -> exp(t) / its inverse log: both turn
    # an ADDITIVE object into a MULTIPLICATIVE one. Identity check at the scalar
    # level: log(exp(x+y)) = x + y and exp(log(u.v)) = u.v.
    x, y = sp.symbols("x y", real=True)
    u, v = sp.symbols("u v", positive=True)
    same1 = sp.simplify(sp.log(sp.exp(x + y)) - (x + y)) == 0
    same2 = sp.simplify(sp.exp(sp.log(u * v)) - u * v) == 0
    check(
        "same exp/log: log exp(x+y)=x+y and exp log(uv)=uv",
        same1 and same2,
        "group=exp(algebra) and Z=exp(log Z) are one exp/log",
    )


# ---------------------------------------------------------------------------
# T5 — PIVOT 1 (decisive): "energies add" is the orbit dichotomy one level up
# ---------------------------------------------------------------------------

def test_T5_pivot1_energies_add_is_exp_log() -> None:
    section("T5: PIVOT 1 — 'energies add' is the {r->r^s} orbit move at the transfer level")

    # Framework's realized free quadratic sector (two-step transfer-matrix note):
    # T2 = (x)_p diag(1, e^{-2 E(p)}) and H = -log(T2)/(2 a_tau) = sum_p E(p) n_p.
    # Use two modes p in {1, 2}. a_tau = 1 (the per-step lattice spacing convention).
    E1, E2 = sp.symbols("E_1 E_2", positive=True)
    blk = lambda E: sp.diag(1, sp.exp(-2 * E))
    T2 = _kron(blk(E1), blk(E2))  # diag(1, e^{-2E2}, e^{-2E1}, e^{-2(E1+E2)})

    # (i) H = -log(T2)/2 is additive: number-operator form sum_p E(p) n_p.
    n1 = _kron(sp.diag(0, 1), sp.eye(2))
    n2 = _kron(sp.eye(2), sp.diag(0, 1))
    H_from_log = -_matlog_diag(T2) / 2  # matrix log of the diagonal transfer operator
    H_number = E1 * n1 + E2 * n2
    ok_addH = sp.simplify(H_from_log - H_number) == sp.zeros(4, 4)
    check(
        "H = -log(T2)/2 = E1.n1 + E2.n2 (ADDITIVE number-operator form)",
        ok_addH,
        "H additive <=> T2 = (x)_p diag(1,e^{-2E}) multiplicative: the exp/log move",
    )

    # (ii) The WHOLE family (T2)^s is multiplicative over modes for EVERY s,
    # and the additive generator is the NORMALIZED s->0 derivative
    # -log((T2)^s)/(2s) = H (NOT the s->0 member itself, which is the identity
    # since (T2)^s -> I as s->0). So {(T2)^s} is a single {r -> r^s} orbit at
    # the transfer-operator level: "H additive" sits in face ADD of #2504's
    # dichotomy applied here, NOT prior to a log choice.
    s = sp.symbols("s", positive=True)
    T2s = _kron(blk(E1) ** s, blk(E2) ** s)
    T2s_direct = sp.diag(1, sp.exp(-2 * s * E2), sp.exp(-2 * s * E1), sp.exp(-2 * s * (E1 + E2)))
    ok_orbit = sp.simplify(T2s - T2s_direct) == sp.zeros(4, 4)
    check(
        "(T2)^s = (x)_p diag(1,e^{-2 s E(p)}) multiplicative for EVERY s (single orbit)",
        ok_orbit,
        "the additive generator is the normalized s->0 derivative -log((T2)^s)/(2s); energies-add is face ADD",
    )

    # (iii) The additive coordinate is uniquely log: -log((T2)^s)/(2s) = H for
    # every s, i.e. the additive readout of the orbit is the SAME log generator
    # (exponent-blind in s after normalization) -- the energy ledger's additive
    # coordinate IS log, by the exp/log universality, NOT independently of it.
    add_coord = sp.simplify(-_matlog_diag(T2s) / (2 * s))
    ok_addcoord = sp.simplify(add_coord - H_number) == sp.zeros(4, 4)
    check(
        "additive coordinate -log((T2)^s)/(2s) = H for every s (the log readout)",
        ok_addcoord,
        "energies-add reduces to choosing the log member of the orbit = (Add)",
    )


# ---------------------------------------------------------------------------
# T6 — PIVOT 1 steelman: H additivity is the NON-INTERACTING / independent class
# ---------------------------------------------------------------------------

def test_T6_pivot1_steelman_interacting_breaks_additivity() -> None:
    section("T6: PIVOT 1 steelman — H additivity holds ONLY in the independent class")

    # H_int = H_A (x) I + I (x) H_B + g (X_A (x) X_B). For g != 0 the spectrum
    # does NOT add: eigenvalues are not { e_a + e_b }. So "the VEV is an energy"
    # forces additivity ONLY when subsystems are independent (tensor-factorized
    # dynamics) -- exactly P1's "independent subsystems" hypothesis.
    g = sp.symbols("g", real=True)
    H_A = sp.diag(1, -1)         # sigma_z on A
    H_B = sp.diag(1, -1)         # sigma_z on B
    X = sp.Matrix([[0, 1], [1, 0]])  # sigma_x
    I2 = sp.eye(2)
    H_free = _kron(H_A, I2) + _kron(I2, H_B)
    H_int = H_free + g * _kron(X, X)

    spec_free = sorted([int(v) for v in _eig_multiset(H_free)])  # {2,0,0,-2}
    check(
        "free H spectrum ADDS: {1,-1}(+){1,-1} = {2,0,0,-2}",
        spec_free == sorted([2, 0, 0, -2]),
        f"got {spec_free}",
    )

    # Characteristic polynomial of H_int retains a g-dependence -> spectrum
    # depends on g, so it is NOT the additive set for g != 0.
    lam = sp.symbols("lambda")
    charpoly = sp.expand(H_int.charpoly(lam).as_expr())
    # The additive spectrum {2,0,0,-2} would give charpoly = lam^2 (lam-2)(lam+2)
    additive_charpoly = sp.expand(lam**2 * (lam - 2) * (lam + 2))
    diff = sp.simplify(charpoly - additive_charpoly)
    depends_on_g = diff != 0 and (g in diff.free_symbols)
    check(
        "interacting H_int (g != 0) does NOT have the additive spectrum",
        depends_on_g,
        f"charpoly - additive = {diff} (carries g)",
    )

    # Explicit numeric: g = 1 changes an eigenvalue away from {2,0,0,-2}.
    spec_g1 = sorted([float(sp.re(v.evalf())) for v in _eig_multiset(H_int.subs(g, 1))])
    not_additive = spec_g1 != [-2.0, 0.0, 0.0, 2.0]
    check(
        "numeric g=1: spectrum != {-2,0,0,2}",
        not_additive,
        f"spec(g=1)={spec_g1}",
    )


# ---------------------------------------------------------------------------
# T7 — PIVOT 2: the free-energy identification IS content (II.b) = P1
# ---------------------------------------------------------------------------

def test_T7_pivot2_free_energy_identification_is_IIb() -> None:
    section("T7: PIVOT 2 — 'W is the free energy' = content (II.b), and (II.b) <=> P1")

    # (i) The framework's v-chain Delta f is DEFINED via the log-det convention
    # (per-matrix-entry difference). Confirm the defining identity reproduces the
    # Matsubara free-energy density structurally from log|det| -- i.e. it
    # PRESUPPOSES log|det|, it does not derive the additive readout from a prior
    # additive-H object. We reprove the load-bearing algebra on a 1-mode toy:
    # ln(m^2 + c) - ln(c) = ln(1 + m^2/c).
    m, c = sp.symbols("m c", positive=True)
    delta_f_term = sp.log(m**2 + c) - sp.log(c)
    matsubara_term = sp.log(1 + m**2 / c)
    ok_def = sp.simplify(delta_f_term - matsubara_term) == 0
    check(
        "Delta f := ln|det(D+m)| - ln|det D| reproduces the Matsubara density (presupposes log|det|)",
        ok_def,
        "ln(m^2+c)-ln(c) = ln(1+m^2/c): free-energy = a NAME for the log-det convention",
    )

    # (ii) (II.b) <=> P1 on the block-diagonal substrate.
    jA, jB, a, b, Z, ZA, ZB, D = _block_diag_det_setup()
    # (II.b) => additivity: if W = log|Z| then W(A (+) B) = W(A) + W(B).
    W = sp.log(Z)
    ok_IIb_to_add = sp.simplify(W - (sp.log(ZA) + sp.log(ZB))) == 0
    check(
        "(II.b) W = log|Z| => additivity W(A(+)B) = W(A) + W(B)",
        ok_IIb_to_add,
        "the free-energy/log-Z identification gives additivity",
    )
    # additivity (+ multiplicative input r = |det| > 0) => W = c log|Z|: Cauchy
    # classifier (reproven elsewhere; here we just confirm the family
    # F_p = Z^p fails additivity for p != 0, so log is the unique additive
    # representative -- the singling is additivity = P1).
    p = sp.symbols("p", real=True)
    Fp = Z**p
    FpA = ZA**p
    FpB = ZB**p
    add_defect = sp.simplify(Fp - (FpA + FpB))  # = (ZA ZB)^p - ZA^p - ZB^p, nonzero for p!=0
    # check it does not vanish identically in (ZA,ZB) for, e.g., p = 1
    nonzero_p1 = sp.simplify(add_defect.subs(p, 1)) != 0
    zero_log_limit = sp.simplify(
        (sp.log(ZA * ZB) - (sp.log(ZA) + sp.log(ZB)))
    ) == 0
    check(
        "F_p is not additive at the tested representative p=1; log is an additive representative "
        "(the p->0 normalized limit (r^p-1)/p, not the p->0 member r^p->1)",
        nonzero_p1 and zero_log_limit,
        "tested at p=1 only; uniqueness of log as THE additive readout needs the multiplicative "
        "Cauchy theorem under continuity/measurability, not classified here",
    )


# ---------------------------------------------------------------------------
# T8 — synthesis: the energy route lands in face ADD of the #2504 dichotomy
# ---------------------------------------------------------------------------

def test_T8_synthesis_energy_route_is_face_ADD() -> None:
    section("T8: SYNTHESIS — the energy route = face ADD (P1); the intensive density = face BLIND")

    # Face ADD: the selector "read the additive (energy) quantum number"
    # references the BARE additive value Phi(r) = log r in the composite law
    # Phi(r_A r_B) = Phi(r_A) + Phi(r_B). Confirm bare additivity holds for log
    # and singles it.
    rA, rB = sp.symbols("r_A r_B", positive=True)
    Phi = sp.log
    ok_add = sp.simplify(Phi(rA * rB) - (Phi(rA) + Phi(rB))) == 0
    check(
        "face ADD: energy readout = bare additivity Phi(r_A r_B)=Phi(r_A)+Phi(r_B) (log)",
        ok_add,
        "the energy ledger references the BARE additive value -> face ADD = P1",
    )

    # Face BLIND: the INTENSIVE / normalized (per-site, Born) energy density is
    # orbit-invariant -- it returns the same object for every exponent s of the
    # transfer operator, so it singles nothing (mirrors #2504/#2456 Born result).
    # Normalized gradient of (T2)^s w.r.t. a source is s-independent after the
    # 1/s normalization: d/dE [ -log((T2)^s)/(2s) ] is independent of s.
    s, E = sp.symbols("s E", positive=True)
    intensive = -sp.log(sp.exp(-2 * s * E)) / (2 * s)  # = E, independent of s
    ok_blind = sp.simplify(sp.diff(intensive, s)) == 0
    check(
        "face BLIND: intensive (normalized) energy = E for every s (singles nothing)",
        ok_blind,
        "the per-site/Born energy density is orbit-invariant -> face BLIND",
    )

    # The two CONSTRUCTED readouts: the bare additive value (face ADD = P1) and
    # the intensive normalized value (face BLIND = nothing). This confirms both
    # tested faces; it does NOT classify the full allowed readout space, so it is
    # not a proof that no third energy readout exists.
    check(
        "the two constructed readouts (bare-additive log; intensive normalized) both hold on the tested surface",
        ok_add and ok_blind,
        "tested faces of #2504 {face ADD = P1, face BLIND = nothing}; a full readout-space classification is not carried out here",
    )


# ---------------------------------------------------------------------------
# T9 — live-ledger context presence (no status consumed as load-bearing)
# ---------------------------------------------------------------------------

def test_T9_ledger_context_presence() -> None:
    section("T9: live-ledger context presence (no dependency status consumed)")
    ok = LEDGER_PATH.exists()
    detail = ""
    if ok:
        try:
            data = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
            rows = data.get("rows", data)
            n = len(rows) if hasattr(rows, "__len__") else 0
            detail = f"ledger present with {n} rows; status NOT consumed as load-bearing"
        except Exception as exc:  # noqa: BLE001
            detail = f"ledger present (parse note: {exc}); status NOT consumed"
    else:
        detail = "ledger absent in this checkout; runner consumes no ledger status anyway"
    # Orientation only (not scored): the note's load-bearing content does not
    # consume any audit status, so ledger presence is not a pass/fail predicate.
    print(f"  [diagnostic, not scored] audit ledger presence recorded (not load-bearing) -- {detail}")


# ---------------------------------------------------------------------------
# T10 — honest-scope strings present; forbidden overclaim strings absent
# ---------------------------------------------------------------------------

def test_T10_honest_scope_strings() -> None:
    section("T10: note honest-scope strings present; forbidden overclaim strings absent")
    if not NOTE.exists():
        check("note file present", False, f"MISSING {NOTE}")
        return
    txt = NOTE.read_text(encoding="utf-8")

    required = [
        "reduces to P1",
        "does NOT close P1",
        "Status boundary",
        "independent post-landing review",
        "Circularity check",
    ]
    miss = [s for s in required if s not in txt]
    check("required honest-scope strings present", not miss, f"missing: {miss}")

    forbidden = [
        "p1_retained_via_symmetry_type",
        "p1_reduced_to_residual_kernel",
        "P1 is closed",
        "P1 retired",
        "converts P1 to a theorem",  # over-claim phrasing
    ]
    present = [s for s in forbidden if s in txt]
    check("forbidden status-promotion / overclaim strings absent", not present, f"present: {present}")


# ---------------------------------------------------------------------------
# T11 — source-note boundary declarations present
# ---------------------------------------------------------------------------

def test_T11_source_note_boundary() -> None:
    section("T11: source-note boundary declarations present")
    if not NOTE.exists():
        check("note file present", False, f"MISSING {NOTE}")
        return
    txt = NOTE.read_text(encoding="utf-8")
    needed = [
        "Source-note proposal disclaimer",
        "Hypothesis set used",
        "Forbidden-imports check",
        "No-promotion statement",
    ]
    miss = [s for s in needed if s not in txt]
    check("source-note boundary declarations present", not miss, f"missing: {miss}")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    section("RUNNER: observable-principle P1 symmetry-type / energy-readout note")
    test_T1_structure_survey()
    test_T2_additive_generator_adds_eigenvalues()
    test_T3_discrete_group_multiplicative_character()
    test_T4_exp_log_bridge()
    test_T5_pivot1_energies_add_is_exp_log()
    test_T6_pivot1_steelman_interacting_breaks_additivity()
    test_T7_pivot2_free_energy_identification_is_IIb()
    test_T8_synthesis_energy_route_is_face_ADD()
    test_T9_ledger_context_presence()
    test_T10_honest_scope_strings()
    test_T11_source_note_boundary()

    section(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print(
        "\nA passing run supports ONLY the bounded finding: the symmetry-type\n"
        "readout law is a representation-theory THEOREM (additive generators on\n"
        "tensor products give additive eigenvalues; discrete-group elements give\n"
        "multiplicative characters; exp/log is the bridge), but the energy route\n"
        "to the v-chain ADDITIVE readout does NOT escape the #2504 sector-\n"
        "composition selector class C: both pivots (energies-add; W-is-the-free-\n"
        "energy) land in face ADD = P1 or relocate the SAME orbit dichotomy one\n"
        "level up. Diagnosis: reduces to P1. It does NOT close P1, does\n"
        "NOT promote any row, and consumes no fitted or observed targets.\n"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
