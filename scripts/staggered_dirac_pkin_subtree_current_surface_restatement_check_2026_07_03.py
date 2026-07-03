#!/usr/bin/env python3
import json
import math
import os
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

import numpy as np


NOTE_PATH = Path("docs/STAGGERED_DIRAC_PKIN_SUBTREE_CURRENT_SURFACE_RESTATEMENT_NOTE_2026-07-03.md")
AX_PATH = Path("docs/MINIMAL_AXIOMS_2026-06-29.md")
LEDGER_PATH = Path("docs/audit/data/audit_ledger.json")

KS_ID = "staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07"
KINETIC_ID = "staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10"
REALIZED_IDS = [
    "realized_kinetic_branch_discriminator_dichotomy_narrow_theorem_note_2026-07-02",
    "realized_kinetic_branch_selected_by_admissibility_variation_narrow_theorem_note_2026-07-02",
    "realized_kinetic_branch_selection_frame_class_transport_narrow_theorem_note_2026-07-02",
    "realized_kinetic_branch_selection_gauged_background_invariance_narrow_theorem_note_2026-07-02",
    "realized_kinetic_branch_conditional_record_registration_narrow_theorem_note_2026-07-02",
]

EXPECTED_KS_SCOPE = (
    "Under the declared nearest-neighbor P-KIN plus site-local unitary P-SD surface "
    "on simply connected Z^3 regions, scalarizable phase systems are exactly the "
    "Clifford -1 cocycle solutions and form one local Z2/U(1) gauge class containing "
    "the Kawamoto-Smit representative."
)

VARIATION_CLAUSE = (
    "the available possibilities are determined by, and vary with, the "
    "nearest-neighbor conditions"
)
NON_SELECTION_SENTENCE = (
    "It does not choose a Hamiltonian or transfer operator, supply transition "
    "probabilities or weights, select a scalar or nonzero kinetic branch, assert a "
    "Dirac-square carrier, define a time metric, or provide a record-production "
    "process or physical persistence dynamics."
)
DOWNSTREAM_CONTENT_CLAUSE = (
    "A realized kinetic branch, if proposed, is downstream content: it needs "
    "derivation, bridge, explicit admission, or approved primitive registry update "
    "before audit rows may use it as load-bearing content."
)
RECORD_PERMANENCE_SENTENCE = (
    "When present, a record locks exactly one local possibility from the subset "
    "available at that site under Admissibility; records are permanent."
)

KINETIC_FIRST = (
    "On the adjacency-licensed, charge-conserving nearest-neighbor bilinear surface "
    "over the qubit-reframe-closed per-site `C²` (cited authorities in §4), "
    "covariance under the lattice automorphisms (translations and the 24 proper "
    "cubic rotations, each up to site-local `U(1)` frame) collapses the kinetic "
    "family to EXACTLY TWO frame classes on simply connected regions: `K0` = "
    "uniform plaquette flux `+1` (representative `t ≡ 1`, scalar tight-binding) "
    "and `K1` = uniform plaquette flux `−1` (representative the Kawamoto-Smit sign "
    "system `η⁰`) — Two-flux-class theorem."
)
DISCRIMINATOR_FIRST = (
    "On the parent two-flux-class kinetic surface, the two representatives are "
    "separated by four computable representative-level discriminators: D1, "
    "internal-factor load and grade-1 Clifford capacity; D2, first-order "
    "Dirac-square dispersion versus scalar perfect-square dispersion; D3, isolated "
    "zero points versus an extensive zero surface; and D4, nonvacuous "
    "per-direction qubit-factor admissibility algebras versus the scalar vacuous "
    "algebra."
)
VARIATION_FIRST = (
    "On the parent two-flux-class kinetic surface, the current minimal-axiom "
    "Admissibility wording supplies a load-bearing variation premise for the "
    "nearest-neighbor availability rule."
)
TRANSPORT_FIRST = (
    "On the parent licensed two-flux-class kinetic surface, the representative-level "
    "Admissibility-variation selection is transported through the full local `U(1)` "
    "frame action."
)
GAUGE_FIRST = (
    "On the parent two-flux-class kinetic surface enlarged by fixed gauge-link "
    "backgrounds that act on the lattice/color tensor factor of each "
    "nearest-neighbor hop, the qubit-factor availability selector is unchanged "
    "under the legal tensor-factor premise."
)
RECORD_FIRST = (
    "On the parent two-flux-class kinetic surface, K0 has exact record-availability "
    "vacuity: every covariant availability map realized by its nearest-neighbor "
    "coefficient structure is neighbor-constant because each per-direction algebra "
    "is `C * I`."
)
TRANSPOSITION_FIRST = (
    "On finite U(1)-link lattice patches (open patches and the 2x2 torus) with "
    "Q-conserving nearest-neighbor matter hopping in a fixed kinetic phase class "
    "(K0 or K1): the per-edge Haar substitution w_e = t_e u_e makes the "
    "link-integrated theory with matter phase system t and plaquette coupling beta "
    "exactly equal to the trivial-phase theory with per-plaquette couplings "
    "beta*Phi_P(t)."
)
SELECTOR_CLAUSE = (
    "a dynamical/spectral principle requiring point-like zero sets (relativistic cones)"
)
FIREWALL_SENTENCE = (
    "This restatement does not itself select K1 over K0 and proposes no Tier-A status movement."
)

CHAIN_SOURCES = [
    (
        "kinetic_class",
        Path("docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"),
        KINETIC_FIRST,
    ),
    (
        "discriminator",
        Path("docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md"),
        DISCRIMINATOR_FIRST,
    ),
    (
        "variation",
        Path("docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md"),
        VARIATION_FIRST,
    ),
    (
        "transport",
        Path("docs/REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md"),
        TRANSPORT_FIRST,
    ),
    (
        "gauged_background",
        Path("docs/REALIZED_KINETIC_BRANCH_SELECTION_GAUGED_BACKGROUND_INVARIANCE_NARROW_THEOREM_NOTE_2026-07-02.md"),
        GAUGE_FIRST,
    ),
    (
        "record_registration",
        Path("docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md"),
        RECORD_FIRST,
    ),
    (
        "transposition",
        Path("docs/STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md"),
        TRANSPOSITION_FIRST,
    ),
]

KS_NOTE_PATH = Path("docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md")
OLD_STATUS_FILES = [
    Path("docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"),
    Path("docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md"),
    Path("docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md"),
    Path("docs/REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md"),
    Path("docs/REALIZED_KINETIC_BRANCH_SELECTION_GAUGED_BACKGROUND_INVARIANCE_NARROW_THEOREM_NOTE_2026-07-02.md"),
    Path("docs/REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md"),
    KS_NOTE_PATH,
]

DEPENDENCY_MD_BASENAMES = {
    "MINIMAL_AXIOMS_2026-06-29.md",
    "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
    "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
    "REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md",
    "REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md",
    "REALIZED_KINETIC_BRANCH_SELECTION_FRAME_CLASS_TRANSPORT_NARROW_THEOREM_NOTE_2026-07-02.md",
    "REALIZED_KINETIC_BRANCH_SELECTION_GAUGED_BACKGROUND_INVARIANCE_NARROW_THEOREM_NOTE_2026-07-02.md",
    "REALIZED_KINETIC_BRANCH_CONDITIONAL_RECORD_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-02.md",
    "STAGGERED_DIRAC_LINK_INTEGRATION_CLASS_COUPLING_TRANSPOSITION_NARROW_THEOREM_NOTE_2026-07-02.md",
}
RUNNER_BASENAME = "staggered_dirac_pkin_subtree_current_surface_restatement_check_2026_07_03.py"
BLOCK_A_BASENAME = "STAGGERED_DIRAC_COUPLING_SIGN_CHANNEL_REGISTRATION_NARROW_THEOREM_NOTE_2026-07-03"

norm = lambda s: " ".join(s.split())
RESULTS = []


def check(gate_id, description, ok, detail=""):
    RESULTS.append((gate_id, description, bool(ok), detail))


def read_text(path):
    return path.read_text(encoding="utf-8")


def site_index(x, L):
    return (x[0] * L + x[1]) * L + x[2]


def step(x, mu, L):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    return tuple(y)


def eta(mu, x):
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x[0] % 2 else 1
    if mu == 2:
        return -1 if (x[0] + x[1]) % 2 else 1
    raise ValueError(mu)


def coeff(kind, mu, x, overrides=None):
    overrides = overrides or {}
    key = (mu, tuple(x))
    if key in overrides:
        return overrides[key]
    if kind == "k0":
        return 1
    if kind == "eta":
        return eta(mu, x)
    raise ValueError(kind)


def plaquette_flux(kind, x, i, j, L, overrides=None):
    xi = step(x, i, L)
    xj = step(x, j, L)
    return (
        coeff(kind, i, x, overrides)
        * coeff(kind, j, xi, overrides)
        * coeff(kind, i, xj, overrides)
        * coeff(kind, j, x, overrides)
    )


def all_sites(L):
    for x0 in range(L):
        for x1 in range(L):
            for x2 in range(L):
                yield (x0, x1, x2)


def hopping_matrix(L, kind):
    n = L ** 3
    h = np.zeros((n, n), dtype=float)
    for x in all_sites(L):
        a = site_index(x, L)
        for mu in range(3):
            y = step(x, mu, L)
            b = site_index(y, L)
            c = coeff(kind, mu, x)
            h[b, a] += c
            h[a, b] += c
    return h


def momentum_values(L, formula):
    values = []
    for n1 in range(L):
        for n2 in range(L):
            for n3 in range(L):
                ks = [2 * math.pi * n / L for n in (n1, n2, n3)]
                values.append(formula(ks))
    return np.array(sorted(values), dtype=float)


def span_dimension(mats):
    arr = np.array([m.reshape(-1) for m in mats], dtype=complex)
    return int(np.linalg.matrix_rank(arr, tol=1e-10))


def algebra_dimension(generator):
    identity = np.eye(generator.shape[0], dtype=complex)
    mats = [identity, generator.astype(complex), generator.conj().T.astype(complex)]
    last_dim = -1
    while True:
        dim = span_dimension(mats)
        if dim == last_dim:
            return dim
        last_dim = dim
        current = list(mats)
        for a in current:
            for b in current:
                mats.append(a @ b)


def run_text_and_ledger_gates(note_text, ax_text, ledger):
    rows = ledger["rows"]
    ks_row = rows.get(KS_ID)
    check(
        "G1.1",
        "ledger contains Kawamoto-Smit row with non-null claim_scope",
        bool(ks_row and ks_row.get("claim_scope")),
        f"present={bool(ks_row)}",
    )
    ks_scope = ks_row.get("claim_scope") if ks_row else None
    check(
        "G1.2",
        "Kawamoto-Smit ledger claim_scope equals expected pin",
        ks_scope is not None and norm(ks_scope) == norm(EXPECTED_KS_SCOPE),
        f"status={ks_row.get('effective_status') if ks_row else None}",
    )
    check(
        "G1.3",
        "note quotes the Kawamoto-Smit ledger claim_scope",
        norm(EXPECTED_KS_SCOPE) in norm(note_text),
        "",
    )

    reverse = defaultdict(list)
    for row_id, row in rows.items():
        for dep in row.get("deps") or []:
            reverse[dep].append(row_id)

    def closure(root):
        seen = set()
        queue = deque(reverse[root])
        while queue:
            row_id = queue.popleft()
            if row_id in seen or row_id == root:
                continue
            seen.add(row_id)
            queue.extend(reverse[row_id])
        return seen

    ks_closure = closure(KS_ID)
    kinetic_closure = closure(KINETIC_ID)
    union_count = len((ks_closure | kinetic_closure) - {KS_ID, KINETIC_ID})
    status_bits = [f"{r}={rows.get(r, {}).get('effective_status')}" for r in [KS_ID, KINETIC_ID] + REALIZED_IDS]
    check(
        "G1.4",
        "reverse-dependency transitive closure count from roots is at least 1000",
        union_count >= 1000,
        f"union={union_count}; statuses: {', '.join(status_bits)}",
    )

    check("G2.1", "variation clause present in axiom text", norm(VARIATION_CLAUSE) in norm(ax_text), "")
    check("G2.2", "variation clause present in note", norm(VARIATION_CLAUSE) in norm(note_text), "")
    check("G2.3", "non-selection sentence present in axiom text", norm(NON_SELECTION_SENTENCE) in norm(ax_text), "")
    check("G2.4", "non-selection sentence present in note", norm(NON_SELECTION_SENTENCE) in norm(note_text), "")
    check("G2.5", "downstream-content clause present in axiom text", norm(DOWNSTREAM_CONTENT_CLAUSE) in norm(ax_text), "")
    check("G2.6", "downstream-content clause present in note", norm(DOWNSTREAM_CONTENT_CLAUSE) in norm(note_text), "")
    check(
        "G2.7",
        "record-permanence sentence present in axiom text and note",
        norm(RECORD_PERMANENCE_SENTENCE) in norm(ax_text) and norm(RECORD_PERMANENCE_SENTENCE) in norm(note_text),
        "",
    )

    existence_paths = [path for _, path, _ in CHAIN_SOURCES] + [KS_NOTE_PATH]
    check(
        "G3.1",
        "all seven chain source files and the Kawamoto-Smit note file exist",
        all(path.exists() for path in existence_paths),
        ", ".join(str(path) for path in existence_paths if not path.exists()),
    )
    for idx, (name, path, quote) in enumerate(CHAIN_SOURCES, start=2):
        source_text = read_text(path) if path.exists() else ""
        ok = norm(quote) in norm(source_text) and norm(quote) in norm(note_text)
        check(
            f"G3.{idx}",
            f"{name} first-sentence quote present in source and note",
            ok,
            str(path),
        )

    old_status_ok = True
    missing_status = []
    for path in OLD_STATUS_FILES:
        text = read_text(path) if path.exists() else ""
        if "independent audit lane" not in text:
            old_status_ok = False
            missing_status.append(str(path))
    check(
        "G3.9",
        "independent audit lane status authority appears in old-format sources and Kawamoto-Smit note",
        old_status_ok,
        ", ".join(missing_status),
    )
    kinetic_text = read_text(Path("docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"))
    check(
        "G3.10",
        "section-7 selector clause present in kinetic-class source and note",
        norm(SELECTOR_CLAUSE) in norm(kinetic_text) and norm(SELECTOR_CLAUSE) in norm(note_text),
        "",
    )


def run_math_gates():
    L = 4
    k0_fluxes = [plaquette_flux("k0", x, i, j, L) for x in all_sites(L) for i in range(3) for j in range(i + 1, 3)]
    eta_fluxes = [plaquette_flux("eta", x, i, j, L) for x in all_sites(L) for i in range(3) for j in range(i + 1, 3)]
    check("G4.1", "K0 plaquette flux is +1 on every 4x4x4 plaquette", all(v == 1 for v in k0_fluxes), "")
    check("G4.2", "Kawamoto-Smit eta plaquette flux is -1 on every 4x4x4 plaquette", all(v == -1 for v in eta_fluxes), "")

    flipped = {(0, (1, 1, 1)): -eta(0, (1, 1, 1))}
    flipped_fluxes = [plaquette_flux("eta", x, i, j, L, flipped) for x in all_sites(L) for i in range(3) for j in range(i + 1, 3)]
    check(
        "G4.3",
        "single-edge sign-flip rejector breaks all-minus plaquette property",
        not all(v == -1 for v in flipped_fluxes) and any(v == 1 for v in flipped_fluxes),
        f"plus_count={sum(1 for v in flipped_fluxes if v == 1)}",
    )

    anti_ok = True
    for x in all_sites(L):
        for i in range(3):
            for j in range(i + 1, 3):
                lhs = eta(i, x) * eta(j, step(x, i, L))
                rhs = eta(j, x) * eta(i, step(x, j, L))
                anti_ok = anti_ok and (lhs == -rhs)
    check("G4.4", "eta satisfies the Clifford -1 cocycle anticommutation identity", anti_ok, "")

    plus_count = 0
    minus_count = 0
    total = 0
    for x in all_sites(L):
        for i in range(3):
            for j in range(i + 1, 3):
                lhs = coeff("k0", i, x) * coeff("k0", j, step(x, i, L))
                rhs = coeff("k0", j, x) * coeff("k0", i, step(x, j, L))
                plus_count += int(lhs == rhs)
                minus_count += int(lhs == -rhs)
                total += 1
    check(
        "G4.5",
        "t == 1 satisfies the +1 relation everywhere and the -1 relation nowhere",
        plus_count == total and minus_count == 0,
        f"plus={plus_count}/{total}; minus={minus_count}/{total}",
    )

    sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)
    identity = np.eye(2, dtype=complex)
    dims = [algebra_dimension(g) for g in (sigma_x, sigma_y, sigma_z)]
    scalar_dim = algebra_dimension(identity)
    check(
        "G4.6",
        "unital *-algebra dimensions give [2,2,2] for Pauli generators and 1 for identity",
        dims == [2, 2, 2] and scalar_dim == 1,
        f"pauli={dims}; identity={scalar_dim}",
    )

    generic_dim = algebra_dimension(np.array([[1, 2], [3, 4]], dtype=complex))
    check("G4.7", "generic nonnormal 2x2 matrix generates full M2(C)", generic_dim == 4, f"dim={generic_dim}")

    pair_gap_ok = True
    gap_details = []
    for a, b in ((sigma_x, sigma_y), (sigma_x, sigma_z), (sigma_y, sigma_z)):
        square_dev = np.linalg.norm((a - b) @ (a - b) - 2 * identity)
        op_norm = np.linalg.svd(a - b, compute_uv=False)[0]
        gap_details.append(op_norm)
        pair_gap_ok = pair_gap_ok and square_dev < 1e-12 and abs(op_norm - math.sqrt(2)) < 1e-12
    check(
        "G4.8",
        "anticommuting Hermitian-unitary pair gaps equal sqrt(2) exactly within tolerance",
        pair_gap_ok,
        "gaps=" + ",".join(f"{v:.15g}" for v in gap_details),
    )

    gap_same = np.linalg.svd(sigma_z - sigma_z, compute_uv=False)[0]
    gap_opposite = np.linalg.svd(sigma_z - (-sigma_z), compute_uv=False)[0]
    check(
        "G4.9",
        "commuting Hermitian-unitary rejectors give gaps 0 and 2, not sqrt(2)",
        abs(gap_same - math.sqrt(2)) > 0.5 and abs(gap_opposite - math.sqrt(2)) > 0.5,
        f"same={gap_same}; opposite={gap_opposite}",
    )

    h0_4 = hopping_matrix(4, "k0")
    heta_4 = hopping_matrix(4, "eta")
    h0_expected_4 = momentum_values(4, lambda ks: 2 * sum(math.cos(k) for k in ks))
    heta2_expected_4 = momentum_values(4, lambda ks: 4 * sum(math.cos(k) ** 2 for k in ks))
    h0_dev_4 = np.max(np.abs(np.sort(np.linalg.eigvalsh(h0_4)) - h0_expected_4))
    heta2_dev_4 = np.max(np.abs(np.sort(np.linalg.eigvalsh(heta_4 @ heta_4)) - heta2_expected_4))
    check(
        "G4.10",
        "dense L=4 spectra match K0 and K1 squared momentum formulas",
        h0_dev_4 < 1e-10 and heta2_dev_4 < 1e-10,
        f"K0_dev={h0_dev_4:.3g}; K1sq_dev={heta2_dev_4:.3g}",
    )

    h0_8 = hopping_matrix(8, "k0")
    heta_8 = hopping_matrix(8, "eta")
    heta_6 = hopping_matrix(6, "eta")
    ev_k1_4 = np.linalg.eigvalsh(heta_4)
    ev_k1_8 = np.linalg.eigvalsh(heta_8)
    ev_k1_6 = np.linalg.eigvalsh(heta_6)
    ev_k0_4 = np.linalg.eigvalsh(h0_4)
    ev_k0_8 = np.linalg.eigvalsh(h0_8)
    z_k1_4 = int(np.sum(np.abs(ev_k1_4) < 1e-8))
    z_k1_8 = int(np.sum(np.abs(ev_k1_8) < 1e-8))
    z_k0_4 = int(np.sum(np.abs(ev_k0_4) < 1e-8))
    z_k0_8 = int(np.sum(np.abs(ev_k0_8) < 1e-8))
    z_k1_6 = int(np.sum(np.abs(ev_k1_6) < 1e-8))
    min_k1_6 = float(np.min(np.abs(ev_k1_6)))
    check(
        "G4.11",
        "zero-count anchors and L=6 K1 gap match exact values",
        z_k1_4 == 8
        and z_k1_8 == 8
        and z_k0_4 == 20
        and z_k0_8 == 68
        and z_k1_6 == 0
        and abs(min_k1_6 - math.sqrt(3)) < 1e-10,
        f"K1 L4={z_k1_4}, L8={z_k1_8}, L6={z_k1_6}, gap6={min_k1_6:.15g}; K0 L4={z_k0_4}, L8={z_k0_8}",
    )

    wrong_l6 = momentum_values(6, lambda ks: 4 * sum(math.sin(k) ** 2 for k in ks))
    true_l6 = np.sort(np.linalg.eigvalsh(heta_6 @ heta_6))
    wrong_dev_l6 = np.max(np.abs(true_l6 - wrong_l6))
    check(
        "G4.12",
        "wrong sin-squared L=6 anchor is rejected by true H[eta]^2 eigenvalues",
        wrong_dev_l6 > 2.9,
        f"wrong_dev={wrong_dev_l6:.15g}",
    )


def run_language_and_link_gates(note_text):
    check("G5.1", "firewall sentence present verbatim in note", norm(FIREWALL_SENTENCE) in norm(note_text), "")
    lower_note = note_text.lower()
    forbidden_language = ["only route", "last route", "exhausted", "closes the"]
    hits = [s for s in forbidden_language if s in lower_note]
    check("G5.2", "forbidden closure rhetoric is absent", not hits, ", ".join(hits))
    forbidden_grades = [
        "should be retained",
        "will be retained",
        "should be promoted",
        "will pass audit",
        "we predict the audit",
    ]
    grade_hits = [s for s in forbidden_grades if s in lower_note]
    check("G5.3", "grade-authoring and audit-prediction strings are absent", not grade_hits, ", ".join(grade_hits))

    body = note_text.split("---", 2)[2] if note_text.startswith("---") else note_text
    links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", body)
    linked_md = {os.path.basename(target) for _, target in links if os.path.basename(target).endswith(".md")}
    check(
        "G6.1",
        "markdown-linked .md basenames equal exactly the dependency inventory",
        linked_md == DEPENDENCY_MD_BASENAMES,
        f"linked={sorted(linked_md)}",
    )
    linked_py = [os.path.basename(target) for _, target in links if os.path.basename(target).endswith(".py")]
    check(
        "G6.2",
        "exactly one linked .py basename equals the runner basename",
        linked_py == [RUNNER_BASENAME],
        f"linked_py={linked_py}",
    )
    block_link_hits = [(label, target) for label, target in links if BLOCK_A_BASENAME in label or BLOCK_A_BASENAME in target]
    outside_backticks = re.sub(r"`[^`]*`", "", note_text)
    check(
        "G6.3",
        "Block A basename appears only outside markdown links and only inside backticks",
        not block_link_hits and BLOCK_A_BASENAME not in outside_backticks,
        f"markdown_hits={len(block_link_hits)}; outside_backticks={BLOCK_A_BASENAME in outside_backticks}",
    )


def main():
    note_text = read_text(NOTE_PATH)
    ax_text = read_text(AX_PATH)
    ledger = json.loads(read_text(LEDGER_PATH))

    run_text_and_ledger_gates(note_text, ax_text, ledger)
    run_math_gates()
    run_language_and_link_gates(note_text)

    passes = 0
    fails = 0
    for gate_id, description, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        if ok:
            passes += 1
        else:
            fails += 1
        detail_suffix = f" :: {detail}" if detail else ""
        print(f"{gate_id} {status}: {description}{detail_suffix}")
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
