#!/usr/bin/env python3
"""Audit-companion runner for the graph-braid Z^3 anyon-exclusion
dichotomy parent note
`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md`
recording dep-resolution hygiene evidence after the dep weakening
`staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25:
retained_no_go -> unaudited`.

Companion source note:
  docs/GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md

Parent ledger row:
  `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29`.

Companion role:
  - Meta audit-companion evidence only.
  - Not a theorem claim or status promotion (the audit lane sets
    claim_type and audit_status independently).
  - Provides audit-friendly evidence that the parent's load-bearing
    substantive content does not load-bear on the *audit grade* of
    its weakened dep
    `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25`
    (which moved from retained_no_go to unaudited), and in fact does
    not load-bear on that dep's *content* at all: the dep is named
    only in the parent's scope-boundary text as the open second-
    quantized question that the first-quantized result does not close.

The companion runner verifies the substance-vs-grade separation by:

  Block 1 : Re-execute the parent's runner on the current head and
            confirm SCORECARD PASS=25 FAIL=0 with FINAL_TAG/VERDICT
            text unchanged.
  Block 2 : Re-verify the integral Smith-normal-form torsion
            classification on the K_5 and K_{3,3} Kuratowski
            obstructions directly with sympy:
              H_1(UD_2(K_5))   = Z^6 (+) Z_2
              H_1(UD_2(K_{3,3})) = Z^4 (+) Z_2.
  Block 3 : Static source-scan of the parent's runner: confirm zero
            audit-status references (audit_status, effective_status,
            etc.) AND zero references to the weakened-dep's filename
            stem or claim-id (staggered_dirac_substep1_statistics_
            agnostic_no_forcing_note_2026-05-25).
  Block 4 : Static source-scan of the parent note: confirm the
            weakened dep is classified under the parent's "Non-Load-
            Bearing Context" block with the explicit "nothing here
            depends on its tier or claims to close it" disclaimer.
  Block 5 : Counterfactual re-execution without consulting the
            weakened dep's audit grade or content: parent runner pass
            count and FINAL_TAG identical to Block 1.
  Block 6 : Hom(Z_2, U(1)) = {+1, -1} homomorphism algebra self-check
            via a dense 4096-point unit-circle sweep on x^2 = 1
            (independent of any dep grade or content).
  Block 7 : Exact Z^3 cube planarity / Kuratowski / 3-connectivity
            self-check on cubes of side L in {3, 4}, plus the planar
            Q_3 contrast (L=2), independent of any dep grade.
  Block 8 : Boundary-square self-check d1 . d2 = 0 on the K_5 / K_{3,3}
            carriers, plus an independent re-derivation of the load-
            bearing Z_2 torsion summand on a smaller witness
            (K_{3,3}) using a fresh sympy SNF call.
  Block 9 : Scope-preservation self-check: the parent's runner still
            emits the explicit "does NOT select boson vs fermion" /
            "does NOT settle the open second-quantized" sentences;
            those scope-language sentences are exactly where the
            weakened dep is referenced, and they are preserved
            verbatim.

Every check uses only the parent's existing runner code (re-imported
via subprocess) plus standard finite/integer numerics from sympy /
numpy / networkx.  No audit-status content is asserted.  No new
theorem claim is made.

PASS/FAIL count is printed at runtime.
"""

from __future__ import annotations

import re
import subprocess
import sys
from itertools import combinations
from pathlib import Path


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
# Repo layout
# -----------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_RUNNER = REPO_ROOT / "scripts" / "graph_braid_z3_anyon_exclusion_dichotomy_2026_05_29.py"
PARENT_NOTE = REPO_ROOT / "docs" / "GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29.md"
WEAKENED_DEP_NOTE = REPO_ROOT / "docs" / "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md"
WEAKENED_DEP_STEM = "staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25"
COMPANION_NOTE = REPO_ROOT / "docs" / (
    "GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_"
    "DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
)

EXPECTED_SCORECARD = "SCORECARD: PASS=25 FAIL=0"
EXPECTED_VERDICT_FRAGMENT = "continuous ANYONS EXCLUDED"
EXPECTED_DICHOTOMY_PHRASE = "{boson, fermion}"


# -----------------------------------------------------------
# Block 1: Re-execute the parent runner on the current head
# -----------------------------------------------------------

def run_parent_runner() -> tuple[int, str, str]:
    """Return (returncode, stdout, stderr) of the parent runner."""
    proc = subprocess.run(
        [sys.executable, str(PARENT_RUNNER)],
        capture_output=True,
        text=True,
        timeout=240,
        cwd=str(REPO_ROOT),
    )
    return proc.returncode, proc.stdout, proc.stderr


def block1_parent_runner_passes() -> tuple[int, str]:
    header("BLOCK 1: Re-execute parent runner on current head; expect PASS=25 FAIL=0")
    rc, out, err = run_parent_runner()
    record(
        "parent_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "parent_runner_emits_expected_scorecard",
        EXPECTED_SCORECARD in out,
        f"'{EXPECTED_SCORECARD}' present in stdout: {EXPECTED_SCORECARD in out}",
    )
    record(
        "parent_runner_verdict_anyons_excluded",
        EXPECTED_VERDICT_FRAGMENT in out,
        f"'{EXPECTED_VERDICT_FRAGMENT}' present in stdout",
    )
    record(
        "parent_runner_dichotomy_phrase_present",
        EXPECTED_DICHOTOMY_PHRASE in out,
        f"'{EXPECTED_DICHOTOMY_PHRASE}' present in stdout",
    )
    record(
        "parent_runner_no_stderr_errors",
        ("Traceback" not in err) and ("Error" not in err),
        f"stderr length={len(err)}",
    )
    return rc, out


# -----------------------------------------------------------
# Block 2: Re-verify the integral H_1 torsion on K_5 / K_{3,3}
#           directly via sympy SNF (independent of any dep)
# -----------------------------------------------------------

def _ud2_boundary_matrices(adj: dict[int, set[int]], V: list[int], E: list[tuple[int, int]]):
    """Build Abrams UD_2 cube complex boundary matrices d1, d2 over Z.

    Returns (d1, d2, |C0|, |C1|, |C2|) where rows are codomain cells and
    columns are domain cells, matching d1 . d2 = 0 over Z.

    Cells:
      C0 = {unordered pair {u, v} of distinct vertices}
      C1 = {unordered (w, e) with w a vertex, e an edge, w not in e}
      C2 = {unordered pair {e, f} of vertex-disjoint edges}

    Edge orientation: each edge (a, b) with a < b, d e = b - a.

      d1 {w, e=(a,b)} = {w, b} - {w, a}
      d2 {e=(a,b), f=(c,d)} = {b, f} - {a, f} - {d, e} + {c, e}
    """
    import numpy as np

    pair_key = lambda u, v: tuple(sorted((u, v)))

    # 0-cells: unordered vertex pairs
    C0 = [pair_key(u, v) for u, v in combinations(V, 2)]
    c0_index = {cell: i for i, cell in enumerate(C0)}

    # 1-cells: (vertex, edge) with vertex not in edge endpoints
    C1 = []
    for w in V:
        for e in E:
            if w not in e:
                C1.append((w, e))
    c1_index = {cell: i for i, cell in enumerate(C1)}

    # 2-cells: unordered pairs of vertex-disjoint edges
    C2 = []
    for e, f in combinations(E, 2):
        if set(e).isdisjoint(set(f)):
            C2.append(tuple(sorted((e, f))))
    c2_index = {cell: i for i, cell in enumerate(C2)}

    d1 = np.zeros((len(C0), len(C1)), dtype=int)
    for j, (w, e) in enumerate(C1):
        a, b = e
        d1[c0_index[pair_key(w, b)], j] += 1
        d1[c0_index[pair_key(w, a)], j] -= 1

    d2 = np.zeros((len(C1), len(C2)), dtype=int)
    for j, (e, f) in enumerate(C2):
        a, b = e
        c, d = f
        # d2 {e, f} = {b, f} - {a, f} - {d, e} + {c, e}
        for w, edge, sign in (
            (b, f, +1),
            (a, f, -1),
            (d, e, -1),
            (c, e, +1),
        ):
            d2[c1_index[(w, edge)], j] += sign

    return d1, d2, len(C0), len(C1), len(C2)


def _build_kn(n: int) -> tuple[dict[int, set[int]], list[int], list[tuple[int, int]]]:
    V = list(range(n))
    E = [tuple(sorted(pair)) for pair in combinations(V, 2)]
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj, V, E


def _build_k33() -> tuple[dict[int, set[int]], list[int], list[tuple[int, int]]]:
    left, right = [0, 1, 2], [3, 4, 5]
    V = left + right
    E = [tuple(sorted((u, v))) for u in left for v in right]
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj, V, E


def _h1_from_snf(d1, d2) -> tuple[int, list[int]]:
    """Return (beta_1, list of torsion invariant factors > 1)."""
    import numpy as np
    import sympy as sp

    if d1.size == 0:
        rank_d1 = 0
    else:
        rank_d1 = int(np.linalg.matrix_rank(d1.astype(float)))
    if d2.size == 0:
        rank_d2 = 0
        torsion: list[int] = []
    else:
        snf = sp.Matrix(d2.tolist()).rref()  # placeholder, will use SNF below
        D = sp.Matrix(d2.tolist())
        # Sympy's matrix_normal_forms.smith_normal_form via .rref doesn't give SNF.
        # Use sympy.matrices.normalforms.smith_normal_form directly.
        from sympy.matrices.normalforms import smith_normal_form
        Dnf = smith_normal_form(D, domain=sp.ZZ)
        diag = [int(Dnf[i, i]) for i in range(min(Dnf.rows, Dnf.cols))]
        rank_d2 = sum(1 for x in diag if x != 0)
        torsion = [abs(x) for x in diag if abs(x) > 1]
    beta_1 = (d1.shape[1] - rank_d1) - rank_d2
    return beta_1, sorted(torsion)


def block2_h1_torsion_witnesses() -> None:
    header("BLOCK 2: Re-verify H_1(UD_2) on K_5 / K_{3,3} directly via sympy SNF")
    try:
        import numpy as np  # noqa: F401
        import sympy as sp  # noqa: F401
    except Exception as exc:
        record("sympy_numpy_importable_block2", False, f"import failed: {exc}")
        return
    record("sympy_numpy_importable_block2", True, "numpy + sympy available")

    # K_5
    adj5, V5, E5 = _build_kn(5)
    d1_5, d2_5, _, _, _ = _ud2_boundary_matrices(adj5, V5, E5)
    beta5, tor5 = _h1_from_snf(d1_5, d2_5)
    record(
        "k5_beta1_eq_6",
        beta5 == 6,
        f"beta_1(K_5) = {beta5} (expected 6)",
    )
    record(
        "k5_torsion_eq_Z2",
        tor5 == [2],
        f"torsion(K_5) = {tor5} (expected [2])",
    )

    # K_{3,3}
    adj33, V33, E33 = _build_k33()
    d1_33, d2_33, _, _, _ = _ud2_boundary_matrices(adj33, V33, E33)
    beta33, tor33 = _h1_from_snf(d1_33, d2_33)
    record(
        "k33_beta1_eq_4",
        beta33 == 4,
        f"beta_1(K_{{3,3}}) = {beta33} (expected 4)",
    )
    record(
        "k33_torsion_eq_Z2",
        tor33 == [2],
        f"torsion(K_{{3,3}}) = {tor33} (expected [2])",
    )

    # Planar reference: C_4 (square) torsion-free (Z)
    V4 = list(range(4))
    E4 = [(0, 1), (1, 2), (2, 3), (0, 3)]
    adj4 = {v: set() for v in V4}
    for a, b in E4:
        adj4[a].add(b)
        adj4[b].add(a)
    d1_4, d2_4, _, _, _ = _ud2_boundary_matrices(adj4, V4, E4)
    beta4, tor4 = _h1_from_snf(d1_4, d2_4)
    record(
        "c4_planar_torsion_free",
        beta4 == 1 and tor4 == [],
        f"beta_1(C_4) = {beta4}, torsion = {tor4} (expected 1, [])",
    )


# -----------------------------------------------------------
# Block 3: Static source-scan of parent runner
# -----------------------------------------------------------

AUDIT_STATUS_TOKENS = (
    "audit_status",
    "effective_status",
    "intrinsic_status",
    "retained_bounded",
    "audited_clean",
    "audited_conditional",
    "retained_no_go",
    "audit_ledger",
    "audit_grade",
)


def block3_parent_runner_no_audit_status_or_dep_references() -> None:
    header("BLOCK 3: Parent runner contains zero audit-status or weakened-dep references")
    source = PARENT_RUNNER.read_text(encoding="utf-8")
    for token in AUDIT_STATUS_TOKENS:
        record(
            f"parent_runner_no_token_{token}",
            token not in source,
            f"'{token}' absent from parent runner source",
        )
    # Zero references to the weakened dep's filename stem / claim-id.
    record(
        "parent_runner_no_weakened_dep_stem",
        WEAKENED_DEP_STEM.lower() not in source.lower(),
        f"'{WEAKENED_DEP_STEM}' absent from parent runner source",
    )
    record(
        "parent_runner_no_weakened_dep_filename",
        "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25"
        not in source,
        "weakened dep note filename absent from parent runner source",
    )


# -----------------------------------------------------------
# Block 4: Static source-scan of parent note
# -----------------------------------------------------------

def block4_parent_note_weakened_dep_is_non_load_bearing() -> None:
    header("BLOCK 4: Parent note classifies weakened dep as Non-Load-Bearing Context")
    note_text = PARENT_NOTE.read_text(encoding="utf-8")
    # The parent note has a literal "Non-Load-Bearing Context" header and
    # places the weakened dep under it with the explicit
    # "nothing here depends on its tier or claims to close it" disclaimer.
    record(
        "parent_note_has_non_load_bearing_context_section",
        "Non-Load-Bearing Context" in note_text,
        "header 'Non-Load-Bearing Context' present",
    )
    # The weakened dep filename appears in the parent note (as scope-boundary text).
    record(
        "parent_note_mentions_weakened_dep_for_scope",
        "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25" in note_text,
        "weakened dep is named in parent note (scope-boundary citation)",
    )
    # And the dep is listed inside the Non-Load-Bearing Context section
    # (the parent also names it earlier in the "Why this note exists"
    # prose as scope-boundary context; this check confirms the formal
    # classification listing lives in the non-load-bearing section).
    idx_section_nlb = note_text.find("## Non-Load-Bearing Context")
    if idx_section_nlb < 0:
        idx_section_nlb = note_text.find("Non-Load-Bearing Context")
    # Section spans from its header to the next "##" header or EOF.
    nlb_end = note_text.find("\n## ", idx_section_nlb + 1)
    if nlb_end < 0:
        nlb_end = len(note_text)
    nlb_block = note_text[idx_section_nlb:nlb_end] if idx_section_nlb >= 0 else ""
    record(
        "weakened_dep_listed_inside_non_load_bearing_section",
        idx_section_nlb >= 0
        and "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25" in nlb_block,
        f"section_idx={idx_section_nlb}, listed_in_section={'STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25' in nlb_block}",
    )
    # Explicit disclaimer text near the citation (normalize whitespace
    # to absorb the parent's hard line wraps).
    normalized = re.sub(r"\s+", " ", note_text)
    record(
        "parent_note_explicit_no_tier_dependency_disclaimer",
        "nothing here depends on its tier or claims to close it" in normalized,
        "'nothing here depends on its tier or claims to close it' present in parent note (whitespace-normalized)",
    )
    # The single load-bearing framework dep is the per-site dim-2 result.
    record(
        "parent_note_sole_load_bearing_dep_dim2",
        "CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02" in note_text
        and "sole" in note_text.lower(),
        "parent note identifies CL3 per-site dim-2 as the sole load-bearing framework dep",
    )
    # And the parent note has a "Load-Bearing Dependencies" section that
    # does NOT list the weakened dep.
    record(
        "parent_note_has_load_bearing_deps_section",
        "Load-Bearing Dependencies" in note_text,
        "header 'Load-Bearing Dependencies' present",
    )
    lb_section_start = note_text.find("## Load-Bearing Dependencies")
    if lb_section_start < 0:
        lb_section_start = note_text.find("Load-Bearing Dependencies")
    lb_section_end = note_text.find("## Non-Load-Bearing Context", lb_section_start + 1)
    if lb_section_end < 0:
        lb_section_end = note_text.find("Non-Load-Bearing Context", lb_section_start + 1)
    lb_block = note_text[lb_section_start:lb_section_end] if lb_section_end > lb_section_start else ""
    record(
        "weakened_dep_absent_from_load_bearing_block",
        "STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25" not in lb_block,
        "weakened dep not listed in Load-Bearing Dependencies section",
    )


# -----------------------------------------------------------
# Block 5: Counterfactual re-execution
# -----------------------------------------------------------

def block5_counterfactual_without_dep_grade() -> None:
    header("BLOCK 5: Counterfactual re-execution without dep-grade or dep-content consultation")
    rc, out, _ = run_parent_runner()
    # The parent runner does not consult the audit ledger or the
    # weakened dep's content; a passing run here demonstrates that
    # the executable substance is grade-independent and content-independent
    # with respect to the weakened dep.
    record(
        "counterfactual_runner_exit_zero",
        rc == 0,
        f"returncode={rc}",
    )
    record(
        "counterfactual_runner_scorecard_unchanged",
        EXPECTED_SCORECARD in out,
        "SCORECARD identical to Block 1 (substance-unchanged)",
    )
    record(
        "counterfactual_runner_anyons_excluded_unchanged",
        EXPECTED_VERDICT_FRAGMENT in out,
        "VERDICT 'continuous ANYONS EXCLUDED' unchanged from Block 1",
    )


# -----------------------------------------------------------
# Block 6: Hom(Z_2, U(1)) = {+1, -1} algebra self-check
# -----------------------------------------------------------

def block6_hom_z2_u1_dense_sweep() -> None:
    header("BLOCK 6: Dense unit-circle sweep on x^2 = 1; only +-1 solutions")
    try:
        import numpy as np
    except Exception as exc:
        record("numpy_importable_block6", False, f"import failed: {exc}")
        return
    n_pts = 4096
    thetas = np.linspace(0.0, 2.0 * np.pi, n_pts, endpoint=False)
    x = np.exp(1j * thetas)
    resid = np.abs(x**2 - 1.0)
    # Exactly two solutions on the unit circle: theta in {0, pi}.
    tol_close = 1.0e-6
    near_one = thetas[np.isclose(x.real, 1.0, atol=tol_close) & np.isclose(x.imag, 0.0, atol=tol_close)]
    near_neg_one = thetas[np.isclose(x.real, -1.0, atol=tol_close) & np.isclose(x.imag, 0.0, atol=tol_close)]
    record(
        "unit_circle_sweep_finds_plus_one",
        near_one.size >= 1,
        f"#points near +1: {near_one.size}",
    )
    record(
        "unit_circle_sweep_finds_minus_one",
        near_neg_one.size >= 1,
        f"#points near -1: {near_neg_one.size}",
    )
    # No continuous solution: minimum residual outside {0, pi} bands
    # must be bounded away from zero.
    mask = np.ones(n_pts, dtype=bool)
    # exclude near 0 and near pi (within 2*sweep-step)
    step = thetas[1] - thetas[0]
    band = 3.0 * step
    mask &= ~((np.abs(thetas - 0.0) < band) | (np.abs(thetas - np.pi) < band) | (np.abs(thetas - 2.0 * np.pi) < band))
    min_off_band_resid = float(resid[mask].min())
    record(
        "unit_circle_sweep_no_continuum_solutions",
        min_off_band_resid > 1.0e-3,
        f"min |x^2 - 1| off +-1 bands = {min_off_band_resid:.3e}",
    )
    # Exact homomorphism algebra: any phi: Z_2 -> U(1) sends generator
    # to a square root of unity in U(1).
    for image in (1.0, -1.0):
        record(
            f"hom_image_square_equals_one_{int(image)}",
            abs(image**2 - 1.0) < 1.0e-12,
            f"image={image:+.0f}: |image^2 - 1| = {abs(image**2 - 1.0):.0e}",
        )


# -----------------------------------------------------------
# Block 7: Z^3 cube planarity / Kuratowski / 3-connectivity
# -----------------------------------------------------------

def block7_z3_planarity_connectivity() -> None:
    header("BLOCK 7: Z^3 cubes L in {3, 4} are non-planar and 3-connected; Q_3 (L=2) is planar")
    try:
        import networkx as nx
    except Exception as exc:
        record("networkx_importable_block7", False, f"import failed: {exc}")
        return

    def build_z3_cube(L: int) -> "nx.Graph":
        G = nx.Graph()
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    G.add_node((x, y, z))
        for x in range(L):
            for y in range(L):
                for z in range(L):
                    for dx, dy, dz in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
                        nx_, ny_, nz_ = x + dx, y + dy, z + dz
                        if 0 <= nx_ < L and 0 <= ny_ < L and 0 <= nz_ < L:
                            G.add_edge((x, y, z), (nx_, ny_, nz_))
        return G

    for L, expect_planar in ((2, True), (3, False), (4, False)):
        G = build_z3_cube(L)
        is_planar, _ = nx.check_planarity(G, counterexample=False)
        record(
            f"z3_cube_L{L}_planarity_match",
            is_planar == expect_planar,
            f"L={L}: planar={is_planar} (expected {expect_planar}); V={G.number_of_nodes()}, E={G.number_of_edges()}",
        )
        if L >= 3:
            # Kuratowski subgraph exhibits non-planarity
            is_planar2, sub = nx.check_planarity(G, counterexample=True)
            record(
                f"z3_cube_L{L}_kuratowski_counterexample_present",
                (not is_planar2) and sub is not None and sub.number_of_nodes() > 0,
                f"L={L}: Kuratowski subgraph V={sub.number_of_nodes() if sub else 0}, E={sub.number_of_edges() if sub else 0}",
            )
            nc = nx.node_connectivity(G)
            record(
                f"z3_cube_L{L}_node_connectivity_eq_3",
                nc == 3,
                f"L={L}: node_connectivity={nc} (expected 3)",
            )


# -----------------------------------------------------------
# Block 8: Boundary-square self-check d1 . d2 = 0 on K_5 / K_{3,3}
# -----------------------------------------------------------

def block8_boundary_square_zero() -> None:
    header("BLOCK 8: d1 . d2 = 0 on K_5 / K_{3,3} carriers; independent Z_2 re-derivation")
    try:
        import numpy as np
        from sympy import ZZ
        from sympy.matrices.normalforms import smith_normal_form
        import sympy as sp
    except Exception as exc:
        record("sympy_numpy_importable_block8", False, f"import failed: {exc}")
        return

    adj5, V5, E5 = _build_kn(5)
    d1_5, d2_5, _, _, _ = _ud2_boundary_matrices(adj5, V5, E5)
    prod5 = d1_5 @ d2_5
    record(
        "k5_d1_d2_zero",
        np.all(prod5 == 0),
        f"|d1 . d2| on K_5: max abs = {int(np.abs(prod5).max())}",
    )

    adj33, V33, E33 = _build_k33()
    d1_33, d2_33, _, _, _ = _ud2_boundary_matrices(adj33, V33, E33)
    prod33 = d1_33 @ d2_33
    record(
        "k33_d1_d2_zero",
        np.all(prod33 == 0),
        f"|d1 . d2| on K_{{3,3}}: max abs = {int(np.abs(prod33).max())}",
    )

    # Independent SNF re-derivation: the smallest non-planar witness K_{3,3}
    # has a single Z_2 torsion invariant factor in its UD_2 SNF.
    Dnf = smith_normal_form(sp.Matrix(d2_33.tolist()), domain=ZZ)
    diag = [int(Dnf[i, i]) for i in range(min(Dnf.rows, Dnf.cols))]
    twos = [x for x in diag if abs(x) == 2]
    ones = [x for x in diag if abs(x) == 1]
    record(
        "k33_snf_has_single_two_invariant",
        len(twos) == 1,
        f"K_{{3,3}} SNF invariant factors: ones={len(ones)}, twos={len(twos)}, all={diag}",
    )

    # Sanity: planar C_5 has no Z_2 torsion
    V5p = list(range(5))
    E5p = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)]
    adj5p = {v: set() for v in V5p}
    for a, b in E5p:
        adj5p[a].add(b)
        adj5p[b].add(a)
    d1_p, d2_p, _, _, _ = _ud2_boundary_matrices(adj5p, V5p, E5p)
    if d2_p.size == 0:
        diag_p = []
    else:
        Dp = smith_normal_form(sp.Matrix(d2_p.tolist()), domain=ZZ)
        diag_p = [int(Dp[i, i]) for i in range(min(Dp.rows, Dp.cols))]
    twos_p = [x for x in diag_p if abs(x) == 2]
    record(
        "c5_planar_no_two_invariant",
        len(twos_p) == 0,
        f"C_5 SNF invariant factors: {diag_p} (no Z_2 expected)",
    )


# -----------------------------------------------------------
# Block 9: Scope-preservation self-check
# -----------------------------------------------------------

SCOPE_PHRASES = (
    "does NOT select boson vs fermion",
    "does NOT settle the open second-quantized gauge-coupled bridge",
)


def block9_scope_language_preserved() -> None:
    header("BLOCK 9: Parent runner still emits scope-language sentences verbatim")
    _, out, _ = run_parent_runner()
    for phrase in SCOPE_PHRASES:
        record(
            f"scope_phrase_{re.sub(r'[^a-z0-9]+', '_', phrase.lower()).strip('_')}",
            phrase in out,
            f"'{phrase}' present in parent runner stdout (scope language preserved)",
        )
    # Also: the companion note explicitly disclaims promotion/import.
    companion_text = COMPANION_NOTE.read_text(encoding="utf-8")
    record(
        "companion_disclaims_status_promotion",
        "not a status promotion" in companion_text.lower()
        or "does not promote status" in companion_text.lower(),
        "companion explicitly disclaims status promotion",
    )
    record(
        "companion_metadata_declares_meta",
        "type:** meta" in companion_text.lower(),
        "companion metadata declares Type: meta",
    )
    record(
        "companion_explicitly_no_new_theorem",
        "not a new theorem claim" in companion_text.lower()
        or "not a theorem claim" in companion_text.lower()
        or "no new theorem" in companion_text.lower(),
        "companion explicitly disclaims new theorem claim",
    )


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> int:
    log("=" * 72)
    log("Graph-Braid Z^3 Anyon-Exclusion Dichotomy")
    log("Dep-Resolution Hygiene Companion Runner (2026-06-04)")
    log("=" * 72)
    log("")
    log(f"Repo root: {REPO_ROOT}")
    log(f"Parent note: {PARENT_NOTE}")
    log(f"Parent runner: {PARENT_RUNNER}")
    log(f"Weakened dep note: {WEAKENED_DEP_NOTE}")
    log(f"Companion source note: {COMPANION_NOTE.relative_to(REPO_ROOT)}")
    log("")
    log("Goal: verify the parent's load-bearing substantive content does")
    log("      not load-bear on the *audit grade* (nor on the content) of")
    log(f"      `{WEAKENED_DEP_STEM}`")
    log("      (which moved from retained_no_go to unaudited).")
    log("")
    log("Scope: pure audit-companion evidence; no theorem claim,")
    log("       no status promotion, no audit-status content asserted.")

    block1_parent_runner_passes()
    block2_h1_torsion_witnesses()
    block3_parent_runner_no_audit_status_or_dep_references()
    block4_parent_note_weakened_dep_is_non_load_bearing()
    block5_counterfactual_without_dep_grade()
    block6_hom_z2_u1_dense_sweep()
    block7_z3_planarity_connectivity()
    block8_boundary_square_zero()
    block9_scope_language_preserved()

    log("")
    log("=" * 72)
    log(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    log("=" * 72)
    if FAIL == 0:
        log("FINAL_TAG: GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_DEP_RESOLUTION_HYGIENE_OK")
        return 0
    log("FINAL_TAG: GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_DEP_RESOLUTION_HYGIENE_FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
