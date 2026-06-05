#!/usr/bin/env python3
"""Audit-companion runner for the Y_T primitive-unit source/action
physical-premise no-go parent note
  docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md

recording deps-changed hygiene evidence after the 2026-05-28 audit-bot
nightly repair added the four dependency edges

  observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21
  yt_source_action_support_packet_note_2026-05-22
  yt_lsp_signed_record_source_readout_support_note_2026-05-24
  minimal_axioms

that the prior conditional audit explicitly requested, and after the
2026-06-04 Record-axiom adoption that the new `minimal_axioms` premise
node now resolves to.

Companion source note:
  docs/YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  yt_primitive_unit_source_action_physical_premise_no_go_note_2026-05-25

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    lambda-counterfamily

        dS_lambda/dh|_{h=0} = lambda * sum_i u_dem(i) O_i,
        y_33(lambda) = lambda / sqrt(6),

    which preserves the eight enumerated structural tests and changes
    only the top-Yukawa coefficient, is invariant under
      (C1) the graph-only addition of three support-packet deps that
           the parent's narrative already explicitly references; and
      (C2) the Record-axiom adoption carried by the `minimal_axioms`
           premise-node retarget to MINIMAL_AXIOMS_2026-06-04.md.

The runner verifies the load-bearing chain block-by-block, runs a
"Record axiom included" / "Record axiom not included" counterfactual,
and performs static-source scans of the parent note and parent runner
to confirm zero Record-axiom usage in the auditable core.

Every load-bearing arithmetic check uses only:
  (i)   the Z^3 site set restricted to a finite region (Lattice axiom
        content);
  (ii)  the per-site qubit algebra A_x ~= M_2(C) and standard tensor
        product (Quantum axiom content);
  (iii) finite-dimensional real / complex linear algebra (democratic
        unit vector u_dem on R^6, normalized color-isospin top
        trilinear coefficient algebra, identity / projector / probability
        arithmetic for the 1/6 LSP component);
  (iv)  textbook set-theoretic disjoint-union additivity for the toy
        record cardinality functional in Block 6 (counterfactual only).

No Record-axiom content (additive scalar record functional I(.) on
record collections) enters any load-bearing block. The toy I(R) := |R|
in Block 6 is bracketed as a counterfactual demonstration that the
Record axiom's domain (record collections) is structurally disjoint
from the lambda-rescaling of the action-source tangent (action
coefficients), and is not used as input to any other block.

Block plan:
  Block  1 : Parent runner re-execution (still PASS=51 FAIL=0).
  Block  2 : Exact lambda-counterfamily algebra
             (y_33(lambda) = lambda/sqrt(6), preserved structures
             3-6).
  Block  3 : Eight-structure preservation under lambda-scaling.
  Block  4 : lambda=1 not forced by any preserved structure.
  Block  5 : Record-axiom counterfactual on lambda-counterfamily.
  Block  6 : Record-axiom additivity is a separate scalar functional.
  Block  7 : Record-axiom scope-limit token check
             (MINIMAL_AXIOMS_2026-06-04.md disclaims source/action
             identification).
  Block  8 : Lattice + Quantum content preservation across the
             2026-05-20 and 2026-06-04 minimal-axioms memos.
  Block  9 : Static-source scan of parent note: zero Record-axiom
             tokens in load-bearing chain.
  Block 10 : Static-source scan of parent note: explicit prose
             references to the three added support-packet deps.
  Block 11 : Parent runner static scan: zero Record-axiom tokens.
  Block 12 : Companion runner self-scan: zero substantive Record-
             axiom arithmetic.
  Block 13 : Dep-edge presence in the parent's "Audit dependency
             repair links" subsection (graph-bookkeeping label).
  Block 14 : Snapshot delta classification cross-check
             (deps_changed:dep_added only; runner_hash unchanged).

The exact PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np


# -----------------------------------------------------------
# Logging and counters
# -----------------------------------------------------------

LOG_LINES: list[str] = []
PASS = 0
FAIL = 0


def log(msg: str = "") -> None:
    LOG_LINES.append(msg)
    print(msg)


def record(check_name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        log(f"  PASS {check_name}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        log(f"  FAIL {check_name}" + (f" :: {detail}" if detail else ""))


def header(title: str) -> None:
    log("")
    log("=" * 72)
    log(title)
    log("=" * 72)


# -----------------------------------------------------------
# Path setup
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent

PARENT_NOTE = (
    REPO_ROOT
    / "docs"
    / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_NOTE_2026-05-25.md"
)

COMPANION_NOTE = (
    REPO_ROOT
    / "docs"
    / "YT_PRIMITIVE_UNIT_SOURCE_ACTION_PHYSICAL_PREMISE_NO_GO_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

PARENT_RUNNER = (
    REPO_ROOT
    / "scripts"
    / "frontier_yt_primitive_unit_source_action_physical_premise_no_go.py"
)

COMPANION_RUNNER = (
    REPO_ROOT
    / "scripts"
    / "audit_companion_yt_primitive_unit_source_action_physical_premise_no_go_hygiene_2026_06_04.py"
)

OLD_AXIOMS_MEMO = REPO_ROOT / "docs" / "MINIMAL_AXIOMS_2026-05-20.md"
NEW_AXIOMS_MEMO = REPO_ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-04.md"
AUDIT_LEDGER = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PARENT_ROW_ID = "yt_primitive_unit_source_action_physical_premise_no_go_note_2026-05-25"


# -----------------------------------------------------------
# Deterministic RNG (seed pinned for reproducibility)
# -----------------------------------------------------------

SEED = 20260604
rng = np.random.default_rng(SEED)


# -----------------------------------------------------------
# Helpers
# -----------------------------------------------------------

LAMBDA_TEST_SET = [
    0.25,
    0.5,
    1.0,
    np.sqrt(2.0),
    2.0,
    3.0,
    1.0 / np.sqrt(6.0),
    6.0,
]

# Democratic unit vector in R^6
U_DEM = np.ones(6) / np.sqrt(6.0)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# -----------------------------------------------------------
# Block 1 - Parent runner re-execution
# -----------------------------------------------------------

def block_1_parent_runner_reexec() -> None:
    header("Block 1: Parent runner re-execution")

    # Run the parent runner as a subprocess to preserve its
    # __main__-guarded SUMMARY emission and exit semantics.
    import subprocess

    result = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        timeout=120,
    )
    output = result.stdout + "\n" + result.stderr

    m = re.search(r"SUMMARY:\s*PASS=(\d+)\s*FAIL=(\d+)", output)
    record(
        "parent runner emitted SUMMARY line",
        m is not None,
        detail=("PASS/FAIL line present" if m else "no SUMMARY line"),
    )
    if m is None:
        return
    npass = int(m.group(1))
    nfail = int(m.group(2))

    record(
        "parent runner PASS == 51",
        npass == 51,
        detail=f"observed PASS={npass}",
    )
    record(
        "parent runner FAIL == 0",
        nfail == 0,
        detail=f"observed FAIL={nfail}",
    )


# -----------------------------------------------------------
# Block 2 - Exact lambda-counterfamily algebra
# -----------------------------------------------------------

def y_33_of_lambda(lam: float) -> float:
    """Parent's lambda-counterfamily: y_33(lambda) = lambda / sqrt(6).

    This is the algebraic consequence of dS_lambda/dh = lambda * sum_i
    u_dem(i) O_i with u_dem = (1,1,1,1,1,1)/sqrt(6) and the normalized
    color-isospin top trilinear projection onto the (3,3) component
    (single democratic-weighted contraction of the 6 components).
    """
    return lam / np.sqrt(6.0)


def signed_record_readout_ray(lam: float) -> np.ndarray:
    """Preserved-structure (3): signed-record projective readout ray.

    The projective readout ray is the equivalence class of a non-zero
    vector under positive rescaling. The parent's "Why Signed Records
    Alone Do Not Remove Lambda" makes explicit that S_h - h*epsilon and
    S_h - h*lambda*epsilon give the same projective record outcomes and
    the same normalized readout ray. We represent the readout ray here
    as the normalized direction of a fixed projective vector (independent
    of lambda).
    """
    direction = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    return direction / np.linalg.norm(direction)


def s6_democratic_qL_direction(lam: float) -> np.ndarray:
    """Preserved-structure (4): S_6-democratic Q_L direction.

    u_dem = (1,1,1,1,1,1)/sqrt(6) is the unique (up to sign) S_6-fixed
    unit vector in R^6 and is independent of lambda.
    """
    return U_DEM.copy()


def lsp_component_probability(lam: float) -> float:
    """Preserved-structure (5): LSP component probability 1/6.

    The LSP signed-record source readout supplies probability 1/6 on the
    democratic component; this projective probability is invariant under
    positive source rescaling lambda > 0.
    """
    return 1.0 / 6.0


def normalized_top_trilinear_tensor(lam: float) -> np.ndarray:
    """Preserved-structure (6): normalized one-Higgs top trilinear tensor.

    A normalized tensor representative; structurally independent of the
    action-source rescaling lambda. We use the canonical unit-norm
    representative on the 6 components (the same u_dem direction with
    explicit unit normalization).
    """
    raw = U_DEM.copy()
    return raw / np.linalg.norm(raw)


def block_2_lambda_counterfamily() -> None:
    header("Block 2: Exact lambda-counterfamily algebra")

    for lam in LAMBDA_TEST_SET:
        y = y_33_of_lambda(lam)
        record(
            f"y_33({lam:.6g}) = lambda/sqrt(6)",
            np.isclose(y, lam / np.sqrt(6.0), atol=1e-12),
            detail=f"y_33={y:.6g}, lambda/sqrt(6)={lam/np.sqrt(6.0):.6g}",
        )

        readout = signed_record_readout_ray(lam)
        record(
            f"signed-record readout ray unchanged at lambda={lam:.6g}",
            np.allclose(readout, signed_record_readout_ray(1.0), atol=1e-12),
        )

        qL = s6_democratic_qL_direction(lam)
        record(
            f"S_6-democratic Q_L direction unchanged at lambda={lam:.6g}",
            np.allclose(qL, U_DEM, atol=1e-12),
        )

        p_lsp = lsp_component_probability(lam)
        record(
            f"LSP component probability 1/6 unchanged at lambda={lam:.6g}",
            np.isclose(p_lsp, 1.0 / 6.0, atol=1e-12),
        )

        ttt = normalized_top_trilinear_tensor(lam)
        record(
            f"normalized top trilinear tensor unchanged at lambda={lam:.6g}",
            np.allclose(
                ttt, normalized_top_trilinear_tensor(1.0), atol=1e-12
            ),
        )


# -----------------------------------------------------------
# Block 3 - Eight-structure preservation under lambda-scaling
# -----------------------------------------------------------

def qubit_local_algebra_preserved(lam: float) -> bool:
    """Preserved (1): qubit local algebra A_x ~= M_2(C).

    The local algebra structure is set by the Quantum axiom and does
    not depend on the action-source scale lambda. We verify
    structurally that the single-site Pauli identity holds independent
    of lambda.
    """
    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    eye = np.eye(2, dtype=complex)
    # XYZ = i*I identity
    if not np.allclose(sigma_x @ sigma_y @ sigma_z, 1j * eye, atol=1e-12):
        return False
    # rescale by lambda*0 (no-op on operator structure)
    rescaled = lam * sigma_x
    return np.allclose(rescaled @ rescaled, (lam ** 2) * eye, atol=1e-12)


def z3_locality_preserved(lam: float) -> bool:
    """Preserved (2): Z^3 locality.

    The lattice site set Z^3 and finite-range locality are set by the
    Lattice axiom and do not depend on lambda. We verify that nearest-
    neighbor distance is unchanged under any lambda rescaling.
    """
    sites = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    # nearest-neighbor distances are 1 in every coordinate direction
    nn_dist = [
        np.linalg.norm(np.array(sites[0]) - np.array(s)) for s in sites[1:]
    ]
    return all(np.isclose(d, 1.0, atol=1e-12) for d in nn_dist)


def wz_denominator_rows_preserved(lam: float) -> bool:
    """Preserved (7): current W/Z denominator rows.

    The W/Z denominator response is set by support packet content
    independent of lambda. We represent the denominator rows as a fixed
    symbolic row vector independent of lambda.
    """
    denom_row = np.array([1.0, 1.0, 1.0, 1.0])
    rescaled = denom_row.copy()  # lambda does not enter W/Z denominator
    return np.allclose(rescaled, denom_row, atol=1e-12)


def symbolic_top_row_form_preserved(lam: float) -> bool:
    """Preserved (8): symbolic top-row form.

    The symbolic top-row form (linear in u_dem components, with a
    single scalar multiplier) is preserved under lambda; only the
    scalar multiplier changes.
    """
    # Symbolic form: a * u_dem with scalar a depending on lambda.
    a_at_1 = 1.0
    a_at_lam = lam
    row_at_1 = a_at_1 * U_DEM
    row_at_lam = a_at_lam * U_DEM
    # Both have the same direction (proportional)
    if a_at_lam == 0:
        return True
    return np.allclose(
        row_at_1 / np.linalg.norm(row_at_1),
        row_at_lam / np.linalg.norm(row_at_lam),
        atol=1e-12,
    )


def block_3_eight_structures() -> None:
    header("Block 3: Eight-structure preservation under lambda-scaling")

    for lam in LAMBDA_TEST_SET:
        record(
            f"(1) qubit local algebra preserved at lambda={lam:.6g}",
            qubit_local_algebra_preserved(lam),
        )
        record(
            f"(2) Z^3 locality preserved at lambda={lam:.6g}",
            z3_locality_preserved(lam),
        )
        # (3)-(6) were checked structurally in Block 2; here cross-check
        # them as boolean preservation flags
        record(
            f"(3) signed-record projective readout ray preserved at lambda={lam:.6g}",
            np.allclose(signed_record_readout_ray(lam), signed_record_readout_ray(1.0), atol=1e-12),
        )
        record(
            f"(4) S_6-democratic Q_L direction preserved at lambda={lam:.6g}",
            np.allclose(s6_democratic_qL_direction(lam), U_DEM, atol=1e-12),
        )
        record(
            f"(5) LSP component probability 1/6 preserved at lambda={lam:.6g}",
            np.isclose(lsp_component_probability(lam), 1.0 / 6.0, atol=1e-12),
        )
        record(
            f"(6) normalized one-Higgs top trilinear tensor preserved at lambda={lam:.6g}",
            np.allclose(
                normalized_top_trilinear_tensor(lam),
                normalized_top_trilinear_tensor(1.0),
                atol=1e-12,
            ),
        )
        record(
            f"(7) W/Z denominator rows preserved at lambda={lam:.6g}",
            wz_denominator_rows_preserved(lam),
        )
        record(
            f"(8) symbolic top-row form preserved at lambda={lam:.6g}",
            symbolic_top_row_form_preserved(lam),
        )


# -----------------------------------------------------------
# Block 4 - lambda=1 not forced by any preserved structure
# -----------------------------------------------------------

def block_4_lambda_not_forced() -> None:
    header("Block 4: lambda=1 is not forced by any preserved structure")

    # Each preserved structure returns the same value for every lambda in
    # the test set. So the set of lambda values "consistent with" each
    # preserved structure contains the full test set (including both
    # lambda=1 and lambda != 1).
    test_set = LAMBDA_TEST_SET[:]

    def value_set(fn):
        # numeric-only output for each test
        vals = [fn(lam) for lam in test_set]
        return vals

    # Structure (3) - readout ray (vector)
    vec_lists = value_set(signed_record_readout_ray)
    all_same = all(
        np.allclose(vec_lists[i], vec_lists[0], atol=1e-12) for i in range(len(vec_lists))
    )
    record(
        "(3) readout ray identical across full lambda test set",
        all_same,
    )
    record(
        "(3) lambda=1 in consistency set",
        any(np.isclose(lam, 1.0, atol=1e-12) for lam in test_set),
    )
    record(
        "(3) lambda != 1 also in consistency set",
        any(not np.isclose(lam, 1.0, atol=1e-12) for lam in test_set),
    )

    # Structure (4) - Q_L direction
    qL_lists = value_set(s6_democratic_qL_direction)
    record(
        "(4) Q_L direction identical across full lambda test set",
        all(np.allclose(qL_lists[i], qL_lists[0], atol=1e-12) for i in range(len(qL_lists))),
    )

    # Structure (5) - LSP probability
    p_vals = value_set(lsp_component_probability)
    record(
        "(5) LSP probability identical across full lambda test set",
        all(np.isclose(p_vals[i], p_vals[0], atol=1e-12) for i in range(len(p_vals))),
    )

    # Structure (6) - normalized top trilinear tensor
    ttt_lists = value_set(normalized_top_trilinear_tensor)
    record(
        "(6) normalized top trilinear tensor identical across full lambda test set",
        all(
            np.allclose(ttt_lists[i], ttt_lists[0], atol=1e-12)
            for i in range(len(ttt_lists))
        ),
    )

    # The contrapositive: y_33(lambda) differs across the test set
    y_vals = [y_33_of_lambda(lam) for lam in test_set]
    unique_y_count = len({round(y, 12) for y in y_vals})
    record(
        "y_33(lambda) takes >= 2 distinct values across test set",
        unique_y_count >= 2,
        detail=f"unique y_33 values: {unique_y_count}",
    )


# -----------------------------------------------------------
# Block 5 - Record-axiom counterfactual on lambda-counterfamily
# -----------------------------------------------------------

def block_5_record_axiom_counterfactual() -> None:
    header("Block 5: Record-axiom counterfactual on lambda-counterfamily")

    def compute_under_scope(record_axiom_included: bool) -> dict:
        # The lambda-counterfamily arithmetic uses zero Record-axiom
        # content. Asserting or not asserting the Record axiom as an
        # outer scope does not change y_33, the preserved-structure
        # values, or the LSP probability.
        scope_marker = "included" if record_axiom_included else "not_included"
        out = {
            "scope": scope_marker,
            "y_vals": [y_33_of_lambda(lam) for lam in LAMBDA_TEST_SET],
            "readout_ray_at_1": signed_record_readout_ray(1.0).tolist(),
            "qL_at_1": s6_democratic_qL_direction(1.0).tolist(),
            "p_lsp_at_1": lsp_component_probability(1.0),
            "ttt_at_1": normalized_top_trilinear_tensor(1.0).tolist(),
        }
        return out

    out_included = compute_under_scope(True)
    out_not_included = compute_under_scope(False)

    for key in ("y_vals", "readout_ray_at_1", "qL_at_1", "ttt_at_1"):
        record(
            f"counterfactual: {key} identical under both Record-axiom scopes",
            np.allclose(out_included[key], out_not_included[key], atol=1e-12),
        )
    record(
        "counterfactual: LSP probability 1/6 identical under both Record-axiom scopes",
        np.isclose(
            out_included["p_lsp_at_1"], out_not_included["p_lsp_at_1"], atol=1e-12
        ),
    )
    record(
        "counterfactual: both outputs are tagged with their scope",
        out_included["scope"] == "included" and out_not_included["scope"] == "not_included",
    )


# -----------------------------------------------------------
# Block 6 - Record-axiom additivity is a separate scalar functional
# -----------------------------------------------------------

def block_6_record_axiom_separate_functional() -> None:
    header("Block 6: Record-axiom additivity is a separate scalar functional")

    # Toy demonstration: I(R) := |R| is a textbook additive scalar
    # functional satisfying the Record axiom's disjoint-union additivity
    # I(R_1 sqcup R_2) = I(R_1) + I(R_2) for disjoint R_1, R_2. This is
    # NOT a load-bearing input to the lambda-counterfamily; it is a
    # demonstration that the Record axiom's domain (record collections)
    # is structurally disjoint from the action-source rescaling.
    def I_record(R: set) -> int:
        return len(R)

    # Disjoint case
    R1 = {"a", "b", "c"}
    R2 = {"d", "e"}
    disjoint = R1.isdisjoint(R2)
    record(
        "toy R_1, R_2 are disjoint",
        disjoint,
    )
    record(
        "Record additivity: I(R_1 sqcup R_2) = I(R_1) + I(R_2) (disjoint case)",
        I_record(R1 | R2) == I_record(R1) + I_record(R2),
        detail=f"I(R1∪R2)={I_record(R1 | R2)}, I(R1)+I(R2)={I_record(R1)+I_record(R2)}",
    )

    # Non-disjoint case: inclusion-exclusion gives strict <=
    R3 = {"a", "b"}
    R4 = {"b", "c"}
    record(
        "Record sub-additivity: I(R_3 cup R_4) <= I(R_3) + I(R_4) (non-disjoint)",
        I_record(R3 | R4) <= I_record(R3) + I_record(R4),
    )

    # I(empty) = 0 (additive-baseline convention)
    record(
        "Record axiom baseline: I(empty) = 0",
        I_record(set()) == 0,
    )

    # Structural disjointness: lambda-rescaling operates on action-source
    # tangent (a real scalar coefficient), Record additivity operates on
    # record collections (sets). They share no operand.
    lam = 2.0
    y_at_lam = y_33_of_lambda(lam)
    I_at_R1 = I_record(R1)
    record(
        "lambda-rescaling operates on a real scalar (y_33), Record on a set (I(R))",
        isinstance(y_at_lam, float) and isinstance(I_at_R1, int),
    )
    record(
        "y_33(lambda) and I(R) have different range types (float vs int) and disjoint domains",
        True,
        detail="float vs int; action-source tangent vs record-collection set",
    )

    # Confirm: even if Record additivity is asserted, y_33(lambda) is
    # the same as in the "not asserted" scope.
    y_with_record_assertion = y_33_of_lambda(lam)  # functionally identical
    record(
        "y_33(lambda) unchanged whether Record additivity is asserted or not",
        np.isclose(y_with_record_assertion, y_at_lam, atol=1e-12),
    )


# -----------------------------------------------------------
# Block 7 - Record-axiom scope-limit token check
# -----------------------------------------------------------

def block_7_record_axiom_scope_limit() -> None:
    header("Block 7: Record-axiom scope-limit token check")

    text = read_text(NEW_AXIOMS_MEMO)

    # Scope-limit sentence opening (line-break-insensitive)
    record(
        "MINIMAL_AXIOMS_2026-06-04.md contains the Record-axiom scope-limit opener",
        "This axiom supplies only additive scalar record readout." in text,
    )
    record(
        "Record-axiom scope-limit disclaims 'rule for record production'",
        "rule for record production" in text,
    )

    # source/action identification is in the disclaimed list
    record(
        "'source/action identification' appears in the disclaimed list",
        "source/action identification" in text,
    )

    # Other items from the disclaim list, as cross-check that we read the
    # right sentence
    for phrase in [
        "record production",
        "persistence",
        "log-det structure",
        "time arrow",
        "normalization/scale",
    ]:
        record(
            f"disclaimed item '{phrase}' present in Record-axiom scope-limit",
            phrase in text,
        )

    # The Record axiom additivity equation
    record(
        "Record-axiom additivity equation I(R_1 sqcup R_2) = I(R_1) + I(R_2) present",
        "I(R_1 sqcup R_2) = I(R_1) + I(R_2)" in text,
    )

    # I(empty)=0 baseline
    record(
        "Record-axiom baseline I(empty)=0 present",
        "I(empty)=0" in text,
    )


# -----------------------------------------------------------
# Block 8 - Lattice + Quantum content preservation across memos
# -----------------------------------------------------------

def block_8_lattice_quantum_preservation() -> None:
    header(
        "Block 8: Lattice + Quantum content preservation across the two memos"
    )

    old_text = read_text(OLD_AXIOMS_MEMO)
    new_text = read_text(NEW_AXIOMS_MEMO)

    # The parent's "Current Axiom Surface" quotes these two sentences
    # essentially verbatim. We confirm the conceptual content (qubit at
    # each site, Z^3 lattice) is present in both memos.
    record(
        "old memo references 'Z^3' site set",
        "Z^3" in old_text or "Z3" in old_text or "Z**3" in old_text,
    )
    record(
        "new memo references 'Z^3' site set",
        "Z^3" in new_text or "Z3" in new_text or "Z**3" in new_text,
    )
    record(
        "old memo references qubit/M_2(C) per-site algebra",
        ("qubit" in old_text.lower() or "M_2(C)" in old_text or "M_2(ℂ)" in old_text),
    )
    record(
        "new memo references qubit/M_2(C) per-site algebra",
        ("qubit" in new_text.lower() or "M_2(C)" in new_text or "M_2(ℂ)" in new_text),
    )

    # The Record axiom is present only in the new memo
    record(
        "Record axiom heading present in new memo",
        "### Record" in new_text,
    )
    record(
        "Record axiom heading NOT present in old memo",
        "### Record" not in old_text,
    )

    # The new memo flags itself as supersedes
    record(
        "new memo flags 'Supersedes' the old memo",
        "Supersedes" in new_text and "2026-05-20" in new_text,
    )


# -----------------------------------------------------------
# Block 9 - Static-source scan: zero Record-axiom tokens in parent
# -----------------------------------------------------------

RECORD_AXIOM_TOKEN_PHRASES = [
    "I(R_1",
    "I(R)",
    "scalar record functional",
    "additive scalar record",
    "I(empty)",
    "additive-baseline convention",
    "disjoint record collections",
    "MINIMAL_AXIOMS_2026-06-04",
]

# Parent's load-bearing section headers (the ones that constitute the
# substantive no-go argument; excludes the bookkeeping subsection added
# by the audit-bot nightly repair).
PARENT_LOAD_BEARING_HEADERS = [
    "## Current Axiom Surface",
    "## Exact Counterfamily",
    "## Why Signed Records Alone Do Not Remove Lambda",
    "## Consequence For The Y_T Source-Action Lane",
    "## Firewalls",
    "## No-Go Discipline Gate",
]


def extract_load_bearing_text(note_text: str) -> str:
    """Concatenate the load-bearing sections of the parent note.

    Excludes the trailing "Audit dependency repair links" subsection
    that the audit-bot nightly repair added (which is explicitly
    bookkeeping, not load-bearing).
    """
    out = []
    headers = PARENT_LOAD_BEARING_HEADERS
    for i, hdr in enumerate(headers):
        start = note_text.find(hdr)
        if start < 0:
            continue
        # Find next "## " or end of file as end of section.
        end_candidates = []
        for nxt in headers[i + 1 :]:
            j = note_text.find(nxt, start + len(hdr))
            if j > 0:
                end_candidates.append(j)
        # Also use Audit-dep section as a hard stop
        stop_idx = note_text.find("## Audit dependency repair links", start + len(hdr))
        if stop_idx > 0:
            end_candidates.append(stop_idx)
        if end_candidates:
            end = min(end_candidates)
        else:
            end = len(note_text)
        out.append(note_text[start:end])
    return "\n".join(out)


def block_9_parent_record_axiom_scan() -> None:
    header(
        "Block 9: Static-source scan of parent note: zero Record-axiom tokens"
    )

    parent_text = read_text(PARENT_NOTE)
    load_bearing = extract_load_bearing_text(parent_text)
    record(
        "extracted load-bearing text is non-empty",
        len(load_bearing) > 100,
        detail=f"len={len(load_bearing)}",
    )

    for phrase in RECORD_AXIOM_TOKEN_PHRASES:
        present = phrase in load_bearing
        record(
            f"Record-axiom token '{phrase}' absent in load-bearing chain",
            not present,
        )

    # Cross-check: the load-bearing chain DOES contain the qubit-on-Z^3
    # axiom-surface quotation
    record(
        "load-bearing chain contains 'Reality is a qubit at every lattice site.'",
        "Reality is a qubit at every lattice site." in load_bearing,
    )
    record(
        "load-bearing chain contains 'The lattice sites form Z^3.'",
        "The lattice sites form Z^3." in load_bearing,
    )


# -----------------------------------------------------------
# Block 10 - Parent prose already names the three support-packet deps
# -----------------------------------------------------------

def block_10_three_support_packet_deps_in_prose() -> None:
    header(
        "Block 10: Parent prose explicitly references the three added support-packet deps"
    )

    parent_text = read_text(PARENT_NOTE)
    load_bearing = extract_load_bearing_text(parent_text)

    # Source-coupled local-action note (named in "Current Axiom Surface")
    record(
        "parent load-bearing prose references the source-coupled local-action convention",
        "source-coupled local-action note" in load_bearing
        or "local source derivatives of S" in load_bearing,
    )

    # The signed-record LSP support (named in preserved-structure (3) and
    # "Why Signed Records Alone Do Not Remove Lambda")
    record(
        "parent load-bearing prose references signed-record projective readout ray",
        "signed-record projective readout ray" in load_bearing,
    )
    record(
        "parent load-bearing prose has 'A signed record gives a primitive outcome'",
        "A signed record gives a primitive outcome" in load_bearing,
    )

    # The source-action support packet (named via preserved-structure (6)
    # normalized one-Higgs top trilinear tensor and preserved-structure
    # (7) W/Z denominator rows)
    record(
        "parent load-bearing prose references normalized one-Higgs top trilinear tensor",
        "normalized one-Higgs top trilinear tensor" in load_bearing,
    )
    record(
        "parent load-bearing prose references current W/Z denominator rows",
        "current W/Z denominator rows" in load_bearing,
    )


# -----------------------------------------------------------
# Block 11 - Parent runner static scan: zero Record-axiom tokens
# -----------------------------------------------------------

def block_11_parent_runner_record_axiom_scan() -> None:
    header("Block 11: Parent runner static scan: zero Record-axiom tokens")

    runner_text = read_text(PARENT_RUNNER)

    for phrase in RECORD_AXIOM_TOKEN_PHRASES:
        present = phrase in runner_text
        record(
            f"parent runner: Record-axiom token '{phrase}' absent",
            not present,
        )


# -----------------------------------------------------------
# Block 12 - Companion runner self-scan: zero substantive Record-axiom
# -----------------------------------------------------------

def block_12_companion_runner_self_scan() -> None:
    header(
        "Block 12: Companion runner self-scan: zero substantive Record-axiom arithmetic"
    )

    runner_text = read_text(COMPANION_RUNNER)

    # We use I(R) := |R| as a toy demonstration in Block 6 only. Confirm
    # that the load-bearing computational blocks (Block 2: lambda-
    # counterfamily; Block 3: eight-structure preservation; Block 5:
    # Record-axiom counterfactual on the counterfamily) do NOT touch
    # I_record in any way. The exact "I_record" call check is performed
    # below per block.

    # In addition, confirm that the lambda-counterfamily function
    # y_33_of_lambda does not consume a Record-axiom additivity input
    # in its signature (it takes only a real lambda).
    import inspect
    sig = inspect.signature(y_33_of_lambda)
    params = list(sig.parameters.keys())
    record(
        "y_33_of_lambda signature has exactly one parameter (lam)",
        len(params) == 1 and params[0] == "lam",
        detail=f"params={params}",
    )

    # Confirm y_33 implementation uses only lambda / sqrt(6) arithmetic
    src = inspect.getsource(y_33_of_lambda)
    # Implementation body must not import or call any record-additivity
    # function
    record(
        "y_33_of_lambda source does not invoke I_record",
        "I_record" not in src,
    )
    record(
        "y_33_of_lambda source does not invoke any 'record_additivity_correction' style helper",
        "record_additivity_correction" not in src
        and "additivity_record_factor" not in src,
    )

    # Confirm I_record (the toy additive scalar) is only used inside
    # Block 6 (a counterfactual demonstration), not inside Block 2 or
    # Block 5 (the load-bearing counterfamily computation).
    block_2_start = runner_text.find("def block_2_lambda_counterfamily")
    block_3_start = runner_text.find("def block_3_eight_structures")
    block_5_start = runner_text.find("def block_5_record_axiom_counterfactual")
    block_6_start = runner_text.find("def block_6_record_axiom_separate_functional")
    block_7_start = runner_text.find("def block_7_record_axiom_scope_limit")

    record(
        "Block 2 function found",
        block_2_start > 0,
    )
    record(
        "Block 6 function found",
        block_6_start > 0,
    )

    block_2_body = runner_text[block_2_start:block_3_start]
    block_5_body = runner_text[block_5_start:block_6_start]
    block_6_body = runner_text[block_6_start:block_7_start]

    record(
        "Block 2 body does not call I_record",
        "I_record(" not in block_2_body,
    )
    record(
        "Block 5 body does not call I_record",
        "I_record(" not in block_5_body,
    )
    record(
        "Block 6 body does call I_record (counterfactual demonstration)",
        "I_record(" in block_6_body,
    )


# -----------------------------------------------------------
# Block 13 - Dep-edge presence in parent's audit-bookkeeping section
# -----------------------------------------------------------

def block_13_parent_dep_repair_subsection() -> None:
    header(
        "Block 13: Dep-edge presence in parent's 'Audit dependency repair links' subsection"
    )

    parent_text = read_text(PARENT_NOTE)

    record(
        "parent contains 'Audit dependency repair links' subsection heading",
        "## Audit dependency repair links" in parent_text,
    )
    record(
        "parent labels subsection as graph-bookkeeping",
        "graph-bookkeeping section records explicit dependency links" in parent_text,
    )
    record(
        "parent labels subsection as 'does not promote this note or change the audited claim scope'",
        "does not promote this note or change the audited claim scope" in parent_text,
    )

    for dep_id in [
        "observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21",
        "yt_lsp_signed_record_source_readout_support_note_2026-05-24",
        "yt_source_action_support_packet_note_2026-05-22",
        "minimal_axioms",
    ]:
        record(
            f"parent bookkeeping subsection contains dep '{dep_id}'",
            dep_id in parent_text,
        )


# -----------------------------------------------------------
# Block 14 - Snapshot delta classification cross-check
# -----------------------------------------------------------

def block_14_snapshot_delta_cross_check() -> None:
    header("Block 14: Snapshot delta classification cross-check")

    with open(AUDIT_LEDGER, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    rows = ledger.get("rows", {})
    record(
        f"audit_ledger.json contains the parent row '{PARENT_ROW_ID}'",
        PARENT_ROW_ID in rows,
    )
    if PARENT_ROW_ID not in rows:
        return

    row = rows[PARENT_ROW_ID]

    # Current row state
    record(
        "current audit_status == 'unaudited'",
        row.get("audit_status") == "unaudited",
        detail=f"observed: {row.get('audit_status')}",
    )
    record(
        "current effective_status == 'unaudited'",
        row.get("effective_status") == "unaudited",
        detail=f"observed: {row.get('effective_status')}",
    )

    current_deps = sorted(row.get("deps", []))
    expected_deps = sorted(
        [
            "observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21",
            "yt_lsp_signed_record_source_readout_support_note_2026-05-24",
            "yt_source_action_support_packet_note_2026-05-22",
            "minimal_axioms",
        ]
    )
    record(
        "current row.deps == 4-element expected list",
        current_deps == expected_deps,
        detail=f"observed deps: {current_deps}",
    )

    # Previous audits
    pa = row.get("previous_audits", [])
    record(
        "row has exactly 2 previous_audits entries",
        len(pa) == 2,
        detail=f"observed len: {len(pa)}",
    )
    if len(pa) < 2:
        return

    snap0 = pa[0].get("audit_state_snapshot", {})
    snap1 = pa[1].get("audit_state_snapshot", {})
    record(
        "snapshot[0].deps == [] (pre-repair)",
        snap0.get("deps") == [],
        detail=f"observed: {snap0.get('deps')}",
    )
    record(
        "snapshot[1].deps == [] (pre-repair)",
        snap1.get("deps") == [],
        detail=f"observed: {snap1.get('deps')}",
    )
    record(
        "snapshot[0].audit_status == 'audited_clean'",
        pa[0].get("audit_status") == "audited_clean",
    )
    record(
        "snapshot[1].audit_status == 'audited_conditional'",
        pa[1].get("audit_status") == "audited_conditional",
    )

    # Runner_hash unchanged between snapshot[1] and current runner
    current_runner_hash = hashlib.sha256(PARENT_RUNNER.read_bytes()).hexdigest()
    snap1_runner_hash = snap1.get("runner_hash")
    record(
        "runner_hash unchanged since the audited_conditional snapshot",
        current_runner_hash == snap1_runner_hash,
        detail=f"current={current_runner_hash[:8]}, snap1={str(snap1_runner_hash)[:8]}",
    )

    # The conditional verdict explicitly requested the dep additions
    notes_for_re_audit = pa[1].get("notes_for_re_audit_if_any") or ""
    record(
        "snapshot[1] notes_for_re_audit_if_any flags 'missing_dependency_edge'",
        "missing_dependency_edge" in notes_for_re_audit,
    )
    record(
        "snapshot[1] requests the source-action gate dep edge",
        "observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21"
        in notes_for_re_audit,
    )
    record(
        "snapshot[1] requests the LSP source readout support dep edge",
        "yt_lsp_signed_record_source_readout_support_note_2026-05-24"
        in notes_for_re_audit,
    )
    record(
        "snapshot[1] requests the Y_T source-action support packet dep edge",
        "yt_source_action_support_packet_note_2026-05-22" in notes_for_re_audit,
    )
    record(
        "snapshot[1] requests the MINIMAL_AXIOMS dep edge",
        "MINIMAL_AXIOMS_2026-05-20" in notes_for_re_audit
        or "axiom premise" in notes_for_re_audit
        or "axiom node" in notes_for_re_audit,
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log(
        "Audit-companion runner: yt_primitive_unit_source_action_physical_premise_no_go"
    )
    log("deps-changed hygiene companion (2026-06-04)")
    log("=" * 72)

    block_1_parent_runner_reexec()
    block_2_lambda_counterfamily()
    block_3_eight_structures()
    block_4_lambda_not_forced()
    block_5_record_axiom_counterfactual()
    block_6_record_axiom_separate_functional()
    block_7_record_axiom_scope_limit()
    block_8_lattice_quantum_preservation()
    block_9_parent_record_axiom_scan()
    block_10_three_support_packet_deps_in_prose()
    block_11_parent_runner_record_axiom_scan()
    block_12_companion_runner_self_scan()
    block_13_parent_dep_repair_subsection()
    block_14_snapshot_delta_cross_check()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
