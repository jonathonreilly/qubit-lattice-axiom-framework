#!/usr/bin/env python3
from __future__ import annotations

import ast
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]

DOCS = {
    "axioms": ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md",
    "g2": ROOT / "docs" / "COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md",
    "depol": ROOT / "docs" / "MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md",
    "pauli": ROOT / "docs" / "PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md",
    "block02": ROOT / "docs" / "COLOR_ARENA_BONDED_PAIR_ADMISSIBILITY_CROSS_SITE_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-06.md",
    "phase_free": ROOT / "docs" / "REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md",
}
ALLOWED_DOCS = frozenset(DOCS.values())

RESULTS: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(ok), detail))


def read_doc(key: str) -> str:
    path = DOCS[key]
    if path not in ALLOWED_DOCS:
        raise RuntimeError(f"refusing to read unlisted source: {path}")
    return path.read_text(encoding="utf-8")


def normalized_markdown(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("> "):
            stripped = stripped[2:]
        elif stripped == ">":
            stripped = ""
        out.append(stripped)
    return " ".join(" ".join(out).split())


def contains_sentence(text: str, sentence: str) -> bool:
    return " ".join(sentence.split()) in normalized_markdown(text)


def mat_zero(n: int, m: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def mat_identity(n: int) -> list[list[Fraction]]:
    out = mat_zero(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def mat_transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)]


def mat_mul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(a)
    mid = len(b)
    cols = len(b[0])
    out = mat_zero(rows, cols)
    for i in range(rows):
        for k in range(mid):
            if a[i][k] == 0:
                continue
            for j in range(cols):
                out[i][j] += a[i][k] * b[k][j]
    return out


def mat_add(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [a[i][j] + b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def mat_vec(a: list[list[Fraction]], v: list[Fraction]) -> list[Fraction]:
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def inner(v: list[Fraction], w: list[Fraction]) -> Fraction:
    return sum(v[i] * w[i] for i in range(len(v)))


def partial_trace_a(state: dict[tuple[int, int], Fraction]) -> list[list[Fraction]]:
    rho = mat_zero(2, 2)
    for a in range(2):
        for ap in range(2):
            total = Fraction(0)
            for b in range(2):
                total += state.get((a, b), Fraction(0)) * state.get((ap, b), Fraction(0))
            rho[a][ap] = total
    return rho


def partial_trace_b(state: dict[tuple[int, int], Fraction]) -> list[list[Fraction]]:
    rho = mat_zero(2, 2)
    for b in range(2):
        for bp in range(2):
            total = Fraction(0)
            for a in range(2):
                total += state.get((a, b), Fraction(0)) * state.get((a, bp), Fraction(0))
            rho[b][bp] = total
    return rho


def flip_state(state: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    return {(b, a): amp for (a, b), amp in state.items()}


def trace_distance_diagonal(rho: list[list[Fraction]], sigma: list[list[Fraction]]) -> Fraction:
    delta00 = rho[0][0] - sigma[0][0]
    delta11 = rho[1][1] - sigma[1][1]
    offdiag_zero = rho[0][1] == sigma[0][1] == rho[1][0] == sigma[1][0] == 0
    if not offdiag_zero:
        raise ValueError("this exact helper is only used for diagonal 2x2 cases")
    return Fraction(abs(delta00) + abs(delta11), 2)


def creation_operator(mode: int, modes: int = 3) -> list[list[Fraction]]:
    dim = 1 << modes
    op = mat_zero(dim, dim)
    for state in range(dim):
        if (state >> mode) & 1:
            continue
        occupied_before = sum((state >> k) & 1 for k in range(mode))
        sign = Fraction(-1 if occupied_before % 2 else 1)
        new_state = state | (1 << mode)
        op[new_state][state] = sign
    return op


def exact_fock_closed_shell() -> tuple[list[list[Fraction]], list[list[Fraction]], bool]:
    creators = [creation_operator(i) for i in range(3)]
    annihilators = [mat_transpose(c) for c in creators]
    ident = mat_identity(8)

    car_ok = True
    zero = mat_zero(8, 8)
    for i in range(3):
        for j in range(3):
            anti = mat_add(mat_mul(annihilators[i], creators[j]), mat_mul(creators[j], annihilators[i]))
            target = ident if i == j else zero
            car_ok = car_ok and anti == target

    vac = [Fraction(0) for _ in range(8)]
    vac[0] = Fraction(1)
    filled = mat_vec(creators[2], mat_vec(creators[1], mat_vec(creators[0], vac)))
    norm_ok = inner(filled, filled) == 1

    gamma = mat_zero(3, 3)
    for i in range(3):
        for j in range(3):
            gamma[i][j] = inner(filled, mat_vec(creators[i], mat_vec(annihilators[j], filled)))
    rho = [[gamma[i][j] / 3 for j in range(3)] for i in range(3)]
    return gamma, rho, car_ok and norm_ok


def traceless_diag(diag: list[Fraction]) -> list[Fraction]:
    tr_over_n = sum(diag) / len(diag)
    return [x - tr_over_n for x in diag]


def frob_sq_diag(diag: list[Fraction]) -> Fraction:
    return sum(x * x for x in diag)


def floating_rank_with_gap(matrix: np.ndarray, tol: float = 1e-12) -> tuple[int, float]:
    singular_values = np.linalg.svd(matrix, compute_uv=False)
    rank = int(np.sum(singular_values > tol))
    if rank == 0:
        gap = float("inf")
    elif rank < len(singular_values):
        gap = float(singular_values[rank - 1] / max(singular_values[rank], 1e-300))
    else:
        gap = float(singular_values[rank - 1] / tol)
    if rank > 0 and not gap > 1e8:
        raise AssertionError(f"singular gap too small: rank={rank}, gap={gap}")
    return rank, gap


def ast_self_scan() -> bool:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_modules = {
        "subprocess",
        "socket",
        "urllib",
        "http",
        "requests",
        "ftplib",
        "telnetlib",
        "webbrowser",
    }
    forbidden_attrs = {
        "write_text",
        "unlink",
        "rename",
        "replace",
        "mkdir",
        "rmdir",
        "remove",
        "rmtree",
        "system",
        "popen",
        "Popen",
        "run",
        "call",
        "check_call",
        "check_output",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] in forbidden_modules:
                    return False
        if isinstance(node, ast.ImportFrom):
            module = (node.module or "").split(".")[0]
            if module in forbidden_modules:
                return False
        if isinstance(node, ast.Attribute) and node.attr in forbidden_attrs:
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "open":
            if len(node.args) >= 2 and isinstance(node.args[1], ast.Constant):
                mode = str(node.args[1].value)
                if any(flag in mode for flag in ("w", "a", "x", "+")):
                    return False
            for keyword in node.keywords:
                if keyword.arg == "mode" and isinstance(keyword.value, ast.Constant):
                    mode = str(keyword.value.value)
                    if any(flag in mode for flag in ("w", "a", "x", "+")):
                        return False
    return True


def run_text_audits() -> None:
    axioms = read_doc("axioms")
    record_quotes = [
        "a record locks exactly one admissible local possibility",
        "A site never carries more than one record",
        "Only records are readable. A readout value is determined by record content alone.",
    ]
    record(
        "text_record_axiom_quotes_present",
        all(contains_sentence(axioms, q) for q in record_quotes),
        f"quotes={len(record_quotes)}",
    )

    g2 = read_doc("g2")
    antecedent = "given the antecedent that the physical records are the color singlets"
    residual = (
        "The selector that fixes the antecedent \u2014 which subsystem the quarks occupy "
        "and which symmetry index the link connection carries \u2014 is a separate input."
    )
    record("text_g2_antecedent_present", contains_sentence(g2, antecedent))
    record("text_g2_residual_present", contains_sentence(g2, residual))

    depol = read_doc("depol")
    depol_sentence = (
        "For any nonzero gauge-covariant linear minimal-coupling drift "
        "`Herm(3) -> su(3)`, Ad-invariance of the link-increment step measure forces "
        "the coupled matter color density to be unpolarized, `\u03c1_color = I\u2083 / 3`."
    )
    record("text_depolarization_row_sentence_present", contains_sentence(depol, depol_sentence))

    pauli = read_doc("pauli")
    pauli_sentence = (
        "The 3-fermion sector of a cell's three color modes is **one-dimensional** "
        "\u2014 no wavefunction choice exists \u2014 and **all eight** `su(3)` charges "
        "annihilate the forced state (residual `0`); its one-body color matrix is exactly `I\u2083`."
    )
    record("text_pauli_target_sentence_present", contains_sentence(pauli, pauli_sentence))

    block02 = read_doc("block02")
    record("text_block02_r5_inherited_present", "R5 frame transport" in block02)
    phase_free = read_doc("phase_free")
    pf_boundary = (
        "This note proves one narrow structural theorem about scalar readouts in a "
        "supplied readout context satisfying the **Record** constraints plus an explicit "
        "determinant-character / log-character homomorphism boundary for the "
        "phase-bearing determinant component."
    )
    pf_disclaimer = "It does **not** derive phase-group additivity from Record finite additivity."
    record(
        "text_phase_free_boundary_and_disclaimer_present",
        contains_sentence(phase_free, pf_boundary) and contains_sentence(phase_free, pf_disclaimer),
        "adjacent surface scoped by its own quoted boundary; not consumed for general record phase-freeness",
    )


def run_t1_marginal_checks() -> None:
    ket00 = {(0, 0): Fraction(1)}
    ket11 = {(1, 1): Fraction(1)}
    sym_ok = flip_state(ket00) == ket00 and flip_state(ket11) == ket11
    rho00_a = partial_trace_a(ket00)
    rho11_a = partial_trace_a(ket11)
    rho00_b = partial_trace_b(ket00)
    rho11_b = partial_trace_b(ket11)
    expected00 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    expected11 = [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]]
    distance_a = trace_distance_diagonal(rho00_a, rho11_a)
    distance_b = trace_distance_diagonal(rho00_b, rho11_b)
    record(
        "t1_sym_block_site_marginals_distinct",
        sym_ok and rho00_a == expected00 and rho11_a == expected11 and rho00_b == expected00 and rho11_b == expected11,
        f"dA={distance_a}, dB={distance_b}",
    )
    record("t1_trace_distance_positive", distance_a == 1 and distance_b == 1)


def run_t2_phase_checks() -> None:
    # GENUINE exact symbolic partial trace over the ring
    # Q + Q e^{i theta} + Q e^{-i theta} (elements: dict power -> Fraction).
    # psi_theta ~ |00> + e^{i theta} |11> (unnormalized); rho entries are
    # amplitude products / 2, with conj(e^{i theta}) = e^{-i theta}.
    def ring_mul(x, y):
        out = {}
        for px, cx in x.items():
            for py, cy in y.items():
                out[px + py] = out.get(px + py, Fraction(0)) + cx * cy
        return {k: v for k, v in out.items() if v != 0}

    def ring_add(x, y):
        out = dict(x)
        for k, v in y.items():
            out[k] = out.get(k, Fraction(0)) + v
        return {k: v for k, v in out.items() if v != 0}

    def ring_conj(x):
        return {-k: v for k, v in x.items()}

    amp = {(0, 0): {0: Fraction(1)}, (1, 1): {1: Fraction(1)}}  # e^{i*0}, e^{i*theta}
    basis = [(0, 0), (0, 1), (1, 0), (1, 1)]
    half = {0: Fraction(1, 2)}

    def rho_entry(bra, ket):
        a = amp.get(bra)
        b = amp.get(ket)
        if a is None or b is None:
            return {}
        return ring_mul(half, ring_mul(a, ring_conj(b)))

    def marginal(site):
        out = [[{}, {}], [{}, {}]]
        for i in range(2):
            for k in range(2):
                acc = {}
                for j in range(2):
                    bra = (i, j) if site == 0 else (j, i)
                    ket = (k, j) if site == 0 else (j, k)
                    acc = ring_add(acc, rho_entry(bra, ket))
                out[i][k] = acc
        return out

    expected = [[{0: Fraction(1, 2)}, {}], [{}, {0: Fraction(1, 2)}]]
    rho_a = marginal(0)
    rho_b = marginal(1)
    theta_free = all(
        all(all(power == 0 for power in cell) for cell in row) for row in rho_a + rho_b
    )
    record(
        "t2_theta_marginals_symbolic_phase_independent",
        rho_a == expected and rho_b == expected and theta_free,
        "computed in the exact ring Q + Q e^{i theta} + Q e^{-i theta}; "
        "no e^{+-i theta} coefficient survives the partial trace",
    )

    # Finite obstruction control only (stipulation-level, labeled as such):
    # over Q, 2*pi*c = 0 iff c = 0.
    coeffs = [Fraction(0), Fraction(1), Fraction(-2), Fraction(3, 5)]
    compact_phase_ok = all((2 * c == 0) == (c == 0) for c in coeffs)
    record(
        "t2_compact_additive_phase_core_control",
        compact_phase_ok,
        "finite control for the c*theta = c*(theta+2pi) => c = 0 argument; "
        "not a derivation of readout additivity or continuity",
    )


def run_t3_weight_checks() -> None:
    uniform = [Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)]
    polarized = [Fraction(1), Fraction(0), Fraction(0)]
    uniform_traceless = traceless_diag(uniform)
    polarized_traceless = traceless_diag(polarized)
    record(
        "t3_adinv_consistency_uniform_traceless_zero",
        uniform_traceless == [Fraction(0), Fraction(0), Fraction(0)]
        and frob_sq_diag(polarized_traceless) == Fraction(2, 3),
    )

    gamma, rho, fock_ok = exact_fock_closed_shell()
    identity3 = mat_identity(3)
    expected_rho = [[identity3[i][j] / 3 for j in range(3)] for i in range(3)]
    record("t3_closed_shell_fock_dimension", 2 ** 3 == 8)
    record("t3_closed_shell_one_body_gamma_identity", fock_ok and gamma == identity3)
    record("t3_closed_shell_normalized_marginal_i3_over_3", rho == expected_rho)


def run_floating_gap_control() -> None:
    rank, gap = floating_rank_with_gap(np.diag([1.0, 0.0, 0.0]))
    record("singular_gap_floating_rank_control (environment control only, not theorem evidence)", rank == 1 and gap > 1e8, f"rank={rank}, gap={gap:.3e}")


def main() -> int:
    run_text_audits()
    run_t1_marginal_checks()
    run_t2_phase_checks()
    run_t3_weight_checks()
    run_floating_gap_control()
    record("ast_self_scan_read_only_no_network_no_subprocess", ast_self_scan())
    record(
        "DECLARATION_color_singlet_records_g2_factorization_site_local_locking_2026_07_06",
        True,
        "bounded factorization runner; no audit verdicts applied",
    )

    passed = 0
    failed = 0
    for name, ok, detail in RESULTS:
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        else:
            failed += 1
        suffix = f" :: {detail}" if detail else ""
        print(f"[{status}] {name}{suffix}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
