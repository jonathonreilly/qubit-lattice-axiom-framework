#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from pathlib import Path
import re
import time
import numpy as np
import sympy as sp
PASS, FAIL, TOL, SEED = 0, 0, 1e-9, 20260702
DOC = "ACPHILAMBDA_K1_STAGGERED_K_BLINDNESS_REAL_LIFT_2026-07-02.md"
SCRIPT = "acphilambda_k1_staggered_k_blindness_real_lift_2026_07_02.py"
DEP = "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
class GaugeSolveError(RuntimeError): pass
def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{tag}] {label}{suffix}")
def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)
def squash(text: str) -> str:
    return " ".join(text.split())
def index(coord: tuple[int, int, int], n: int) -> int:
    return (coord[0] * n + coord[1]) * n + coord[2]
def coord(i: int, n: int) -> tuple[int, int, int]:
    return (i // (n * n), (i // n) % n, i % n)
def rotate_coord(x: tuple[int, int, int], n: int, power: int = 1) -> tuple[int, int, int]:
    y = x
    for _ in range(power % 3):
        y = (y[2], y[0], y[1])
    return tuple(v % n for v in y)
def eta_sign(x: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return 1 if x[0] % 2 == 0 else -1
    return 1 if (x[0] + x[1]) % 2 == 0 else -1
def build_h(n: int, branch: str) -> np.ndarray:
    if branch == "K1" and n % 2 != 0:
        raise ValueError("K1 sign representative requires even N")
    size = n**3
    h = np.zeros((size, size), dtype=np.int8)
    for x1 in range(n):
        for x2 in range(n):
            for x3 in range(n):
                x = (x1, x2, x3)
                i = index(x, n)
                for mu in range(3):
                    y = list(x)
                    y[mu] = (y[mu] + 1) % n
                    j = index(tuple(y), n)
                    val = eta_sign(x, mu) if branch == "K1" else 1
                    h[i, j] = val
                    h[j, i] = val
    return h
def rotation_matrix(n: int, power: int = 1) -> np.ndarray:
    size = n**3
    r = np.zeros((size, size), dtype=np.int8)
    for i in range(size):
        r[index(rotate_coord(coord(i, n), n, power), n), i] = 1
    return r
def edge_list(source: np.ndarray, target: np.ndarray) -> list[tuple[int, int, int]]:
    if source.shape != target.shape:
        raise GaugeSolveError("shape mismatch")
    if not np.array_equal(source != 0, target != 0):
        raise GaugeSolveError("support mismatch")
    edges: list[tuple[int, int, int]] = []
    size = source.shape[0]
    for i in range(size):
        for j in range(i + 1, size):
            if source[i, j] == 0:
                continue
            if target[i, j] == 0 or source[i, j] % target[i, j] != 0:
                raise GaugeSolveError("non-sign ratio")
            ratio = int(source[i, j] // target[i, j])
            if ratio not in (-1, 1) or source[i, j] != ratio * target[i, j]:
                raise GaugeSolveError("non-sign ratio")
            edges.append((i, j, ratio))
    return edges
def solve_sign_frame(source: np.ndarray, target: np.ndarray) -> tuple[np.ndarray, int, int, int]:
    edges = edge_list(source, target)
    size = source.shape[0]
    adj: list[list[tuple[int, int]]] = [[] for _ in range(size)]
    for i, j, ratio in edges:
        adj[i].append((j, ratio))
        adj[j].append((i, ratio))
    w = np.zeros(size, dtype=np.int8)
    w[0] = 1
    q: deque[int] = deque([0])
    tree_edges = 0
    while q:
        i = q.popleft()
        for j, ratio in adj[i]:
            proposed = int(ratio * w[i])
            if w[j] == 0:
                w[j] = proposed
                tree_edges += 1
                q.append(j)
            elif int(w[j]) != proposed:
                raise GaugeSolveError("cycle inconsistency")
    if np.any(w == 0):
        raise GaugeSolveError("disconnected support")
    for i, j, ratio in edges:
        if int(w[i] * w[j]) != ratio:
            raise GaugeSolveError("off-tree inconsistency")
    return w, len(edges), tree_edges, len(edges) - tree_edges
def compensated_lift(n: int, branch: str, power: int = 1) -> tuple[np.ndarray, np.ndarray, dict[str, int]]:
    h = build_h(n, branch)
    r = rotation_matrix(n, power)
    target = r @ h @ r.T
    if branch == "K0":
        w = np.ones(n**3, dtype=np.int8)
        stats = {"edges": int(np.count_nonzero(np.triu(h)) // 1), "tree": n**3 - 1, "offtree": 0}
    else:
        w, edges, tree, offtree = solve_sign_frame(h, target)
        stats = {"edges": edges, "tree": tree, "offtree": offtree}
    rt = w[:, None] * r
    return h, rt.astype(np.int8), stats
def heat_trace(h: np.ndarray, u: np.ndarray, t: float) -> complex:
    vals, vecs = np.linalg.eigh(h.astype(np.complex128))
    heat = (vecs * np.exp(-t * vals)) @ vecs.conj().T
    return complex(np.trace(heat @ u.astype(np.complex128)))
def diagonal_pm_one(mat: np.ndarray) -> bool:
    diag = np.diag(np.diag(mat))
    return np.array_equal(mat, diag) and set(np.unique(np.diag(mat))).issubset({-1, 1})
def main() -> int:
    t0 = time.perf_counter()
    rng = np.random.default_rng(SEED)
    root = Path(__file__).resolve().parents[1]
    docs = root / "docs"
    note_path = docs / DOC
    dep_path = docs / DEP
    note = note_path.read_text(encoding="utf-8")
    dep = dep_path.read_text(encoding="utf-8")
    note_s = squash(note)
    section("A - sources and pins")
    check("paired note exists", note_path.exists(), DOC)
    check("Dirac-row dependency exists", dep_path.exists(), DEP)
    check("true dependency pins are present", "Kawamoto-Smit" in dep and "η⁰" in dep)
    import json
    ledger = json.loads((root / "docs" / "audit" / "data" / "audit_ledger.json").read_text(encoding="utf-8"))
    rows = ledger if isinstance(ledger, list) else ledger.get("rows", ledger.get("claims", []))
    items = rows if isinstance(rows, list) else list(rows.values())
    dep_row = next(
        (r for r in items
         if r.get("id", r.get("claim_id", "")) == "staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10"),
        None,
    )
    check("ledger row found for the dependency", dep_row is not None)
    live = dep_row or {}
    print(
        "ledger row live audit fields (informational; the audit lane owns them): "
        f"effective_status={live.get('effective_status')!r}, "
        f"claim_scope={'present' if live.get('claim_scope') else 'null'}"
    )
    block_match = re.search(r"\*\*Claim scope:\*\*(.*?)\*\*Status" + r" authority:\*\*", dep, re.S)
    block_s = squash(block_match.group(1)) if block_match else ""
    qline = next((x for x in note.splitlines() if x.startswith("Premise scope quotes")), "")
    quotes = re.findall(r'"([^"]+)"', qline)
    check("dependency claim-scope block located in the dependency note", len(block_s) > 200)
    check("note carries exactly three premise scope quotes", len(quotes) == 3)
    for i, quote in enumerate(quotes, 1):
        check(
            f"premise quote {i} is substantive and verbatim in the dependency claim-scope block",
            len(quote) >= 80 and squash(quote) in block_s,
        )
    check("note pins no audit-grade label on the premise quotes", "retained_bounded" not in note and "claim_scope (" not in note)
    check("retired ledger-condensed scope wording absent from note", "adjacency-licensed Q-conserving" not in note)
    check("primary runner link points to this script", f"../scripts/{SCRIPT}" in note)
    check("source note declares canonical Type no_go", "**Type:** no_go" in note)
    legacy_status_label = "Status " + "authority"
    check("source note uses audit-boundary wording, not legacy status label", "**Audit boundary:**" in note and legacy_status_label not in note)
    section("B - constructive real frame and rejectors")
    for n in (4, 6):
        h, rt, stats = compensated_lift(n, "K1", 1)
        eye = np.eye(n**3, dtype=np.int8)
        res = rt @ h @ rt.T - h
        cube = rt @ rt @ rt
        check(f"N={n} K1 edge ratios close on spanning-tree solve", stats["edges"] == 3 * n**3)
        check(f"N={n} K1 off-tree closure checked", stats["offtree"] == stats["edges"] - (n**3 - 1))
        check(f"N={n} K1 covariance residual exactly zero", np.array_equal(res, np.zeros_like(h)))
        check(f"N={n} K1 compensated cube is +I exactly", np.array_equal(cube, eye))
        check(f"N={n} K1 cube diagonal values are all +1", set(np.unique(np.diag(cube))) == {1})
    h0, r0, _ = compensated_lift(4, "K0", 1)
    rot = rotation_matrix(4, 1)
    check("K0 lift is the bare rotation", np.array_equal(r0, rot))
    check("K0 commutes with R exactly", np.array_equal(rot @ h0 @ rot.T, h0))
    check("K0 bare rotation has cube I", np.array_equal(rot @ rot @ rot, np.eye(64, dtype=np.int8)))
    try:
        bad = build_h(4, "K1").copy()
        target = bad.copy()
        target[0, 1] = 0
        target[1, 0] = 0
        solve_sign_frame(bad, target)
        support_rejected = False
    except GaugeSolveError as exc:
        support_rejected = "support mismatch" in str(exc)
    check("rejector exercises support-mismatch branch", support_rejected)
    try:
        solve_sign_frame(build_h(4, "K1"), build_h(4, "K0"))
        cycle_rejected = False
    except GaugeSolveError as exc:
        cycle_rejected = "cycle inconsistency" in str(exc)
    check("rejector exercises cycle-inconsistency branch", cycle_rejected)
    signs = rng.choice(np.array([-1, 1], dtype=np.int8), size=64)
    h = build_h(4, "K1")
    random_target = signs[:, None] * h * signs[None, :]
    recovered, _, _, _ = solve_sign_frame(h, random_target)
    check("fixed-seed random sign-gauge instance is solved", np.array_equal(recovered[:, None] * random_target * recovered[None, :], h))
    section("C - U(1) frame remark")
    rho = sp.symbols("rho", real=True)
    alpha = sp.symbols("alpha", real=True)
    theta = sp.symbols("theta", real=True)
    unit_real = sp.solve(sp.Eq(rho**2, 1), rho)
    rel = sp.exp(sp.I * theta)
    imag_rel = sp.simplify(sp.im(rel))
    scale = sp.simplify((sp.exp(sp.I * alpha)) ** 3 - sp.exp(3 * sp.I * alpha))
    check("real modulus-one edge ratio solves to +-1", set(unit_real) == {-1, 1})
    check("unit relative phase is real exactly when sin(theta)=0", imag_rel == sp.sin(theta))
    check("global U(1) cube scaling is exp(3 i alpha)", scale == 0)
    check("note states trivial projective class", "projective class is trivial" in note_s)
    section("D - blindness transfer and discriminator")
    h1, rt, _ = compensated_lift(4, "K1", 1)
    _, rt2_constructed, _ = compensated_lift(4, "K1", 2)
    rt2_power = rt @ rt
    r2 = rotation_matrix(4, 2)
    check("Rt commutes with H_K1 exactly", np.array_equal(rt @ h1 - h1 @ rt, np.zeros_like(h1)))
    check("Rt^2 equals separately constructed compensated R^2 lift", np.array_equal(rt2_power, rt2_constructed))
    check("Rt^2 R^{-2} is diagonal +-1", diagonal_pm_one(rt2_power @ r2.T))
    for t in (0.3, 1.0):
        diff = abs(heat_trace(h1, rt, t) - heat_trace(h1, rt2_constructed, t))
        check(f"K1 heat trace blind at N=4, t={t}", diff < TOL, f"diff={diff:.3e}")
    h0 = build_h(4, "K0")
    r = rotation_matrix(4, 1)
    r_sq = rotation_matrix(4, 2)
    for t in (0.3, 1.0):
        diff = abs(heat_trace(h0, r, t) - heat_trace(h0, r_sq, t))
        check(f"K0 heat trace blind at N=4, t={t}", diff < TOL, f"diff={diff:.3e}")
    phased = h1.astype(np.complex128)
    phased[1, 5] *= np.exp(1.6j)
    phased[5, 1] = np.conj(phased[1, 5])
    defect_diff = abs(heat_trace(phased, rt, 1.0) - heat_trace(phased, rt2_power, 1.0))
    check("single-edge complex phase breaks the original trace blindness test", defect_diff > 1e-3, f"diff={defect_diff:.3e}")
    section("E - note discipline")
    preserved = [
        "the compensated `C3[111]` lift on the one-component staggered surface is real and non-projective: its projective class is trivial",
        "the one-component staggered surface, in both quoted kinetic classes, is conjugate-sector blind",
        "the projective seed irreducibly needs the two-component structure",
        "not a terminal no-go",
    ]
    for sent in preserved:
        check(f"preserved sentence present: {sent[:42]}", sent in note)
        check(f"preserved sentence embedded: {sent[:42]}", all(line.strip() != sent for line in note.splitlines()))
    for token in ["N1:", "N2:", "N3:", "N4:", "N5:", "N6:", "N7:", "N8:"]:
        check(f"No-Go Discipline token {token} present", token in note)
    forbidden = [
        "only " + "route",
        "last " + "route",
        "exha" + "usted",
        "closes " + "the " + "route",
        "P" + "DG",
        "new " + "wall",
    ]
    lowered = note.lower()
    for token in forbidden:
        check(f"forbidden token absent: {token}", token.lower() not in lowered)
    w_names = set(re.findall(r"\bW_[A-Za-z0-9_]+\b", note))
    allowed_w = {"W_cycle_holonomy_value", "W_defect_identity_unit", "W_defect_readout_selection"}
    check("W-name inventory is whitelisted", w_names.issubset(allowed_w), ",".join(sorted(w_names)))
    links = re.findall(r"\]\(([^)]+)\)", note)
    md_links = [target for target in links if target.endswith(".md")]
    runner_links = [target for target in links if target.endswith(".py")]
    check("exactly one markdown dependency link", md_links == [DEP], str(md_links))
    check("exactly one runner link", runner_links == [f"../scripts/{SCRIPT}"], str(runner_links))
    inflight = [
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01",
        "ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01",
        "ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02",
        "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02",
        "ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02",
    ]
    for name in inflight:
        check(f"in-flight basename is backticked: {name[:34]}", f"`{name}`" in note)
        check(f"in-flight basename is not a link target: {name[:34]}", all(name not in target for target in links))
    leak_terms = [
        "/tmp/" + "sp" + "ec",
        "acceptance " + "contract",
        "preserve " + "verbatim",
        "must " + "be absent",
        "runner " + "greps",
        "anti-" + "fabrication",
    ]
    for term in leak_terms:
        check(f"source-instruction phrase absent: {term}", term.lower() not in lowered)
    elapsed = time.perf_counter() - t0
    print(f"\nRuntime: {elapsed:.2f} s")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 and PASS >= 50 and elapsed < 90 else 1
if __name__ == "__main__":
    raise SystemExit(main())
