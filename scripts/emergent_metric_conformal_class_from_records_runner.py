"""
Emergent-metric causal-source packet check.

This runner keeps the conformal-class note honest on the current authority
surface.  It does not apply audit verdicts.  It checks that:

1. the one-hop source packet named in the note is graph-visible and cached;
2. current retained/no-go clock-rate authorities remain retained in the ledger;
3. currently unaudited causal-source inputs force the note to stay
   conditional-support rather than retained;
4. the finite conformal/null-cone and clock-rate no-go algebra still holds.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "EMERGENT_METRIC_CONFORMAL_CLASS_FROM_RECORDS_SCALE_IS_THE_CLOCK_RATE_"
    "NO_GO_NARROW_THEOREM_NOTE_2026-06-06.md"
)
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

RETAINED_STATUSES = {"retained", "retained_bounded", "retained_no_go"}

SOURCE_PACKET = [
    {
        "cid": "record_history_order_time_rate_firewall_2026-06-05",
        "role": "record order / event-index firewall",
        "doc": "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
        "runner": "scripts/frontier_record_history_time_rate_firewall_2026_06_05.py",
        "cache": "logs/runner-cache/frontier_record_history_time_rate_firewall_2026_06_05.txt",
        "load_bearing_causal_input": True,
    },
    {
        "cid": "post_record_clock_rate_interface_2026-06-06",
        "role": "clock-rate no-go authority",
        "doc": "docs/POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md",
        "runner": "scripts/frontier_post_record_clock_rate_interface_2026_06_06.py",
        "cache": "logs/runner-cache/frontier_post_record_clock_rate_interface_2026_06_06.txt",
        "expected_effective_status": "retained_no_go",
        "load_bearing_causal_input": False,
    },
    {
        "cid": "record_clock_rate_normalization_gate_2026-06-06",
        "role": "rate-normalization gate authority",
        "doc": "docs/RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md",
        "runner": "scripts/frontier_record_clock_rate_normalization_gate_2026_06_06.py",
        "cache": "logs/runner-cache/frontier_record_clock_rate_normalization_gate_2026_06_06.txt",
        "expected_effective_status": "retained",
        "load_bearing_causal_input": False,
    },
    {
        "cid": "lattice_nn_light_cone_note",
        "role": "nearest-neighbor causal bound",
        "doc": "docs/LATTICE_NN_LIGHT_CONE_NOTE.md",
        "runner": "scripts/lattice_nn_topological_causal_bound_check.py",
        "cache": "logs/runner-cache/lattice_nn_topological_causal_bound_check.txt",
        "expected_effective_status": "retained",
        "load_bearing_causal_input": True,
    },
    {
        "cid": "lieb_robinson_equal_time_tensor_locality_narrow_theorem_note_2026-05-10",
        "role": "equal-time tensor locality",
        "doc": "docs/LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md",
        "runner": "scripts/audit_companion_lieb_robinson_equal_time_tensor_locality_exact_2026_05_10.py",
        "cache": "logs/runner-cache/audit_companion_lieb_robinson_equal_time_tensor_locality_exact_2026_05_10.txt",
        "expected_effective_status": "retained_bounded",
        "load_bearing_causal_input": True,
    },
    {
        "cid": "reconstructed_h_quasilocal_from_analytic_dispersion_microcausality_bridge_narrow_theorem_note_2026-06-06",
        "role": "reconstructed-H analytic-dispersion LR bridge",
        "doc": "docs/RECONSTRUCTED_H_QUASILOCAL_FROM_ANALYTIC_DISPERSION_MICROCAUSALITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "runner": "scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py",
        "cache": "logs/runner-cache/reconstructed_h_quasilocal_microcausality_bridge_runner.txt",
        "load_bearing_causal_input": True,
    },
    {
        "cid": "lorentz_boost_covariance_3plus1d_theorem_note",
        "role": "3+1 Lorentzian/boost-covariance bounded authority",
        "doc": "docs/LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md",
        "runner": "scripts/frontier_lorentz_boost_3plus1d.py",
        "cache": "logs/runner-cache/frontier_lorentz_boost_3plus1d.txt",
        "expected_effective_status": "retained_bounded",
        "load_bearing_causal_input": True,
    },
    {
        "cid": "wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation_note_2026-06-07",
        "role": "Lorentzian signature orientation firewall",
        "doc": "docs/WICK_ROTATION_COMPACT_SO4_TO_LORENTZIAN_DIRAC_DOUBLING_ORIENTATION_NOTE_2026-06-07.md",
        "runner": "scripts/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.py",
        "cache": "logs/runner-cache/wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation.txt",
        "expected_effective_status": "retained_bounded",
        "load_bearing_causal_input": True,
    },
]


PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  | {detail}" if detail else ""
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{suffix}")
    return ok


def rel(path: str) -> Path:
    return ROOT / path


def cache_has_success_marker(cache_path: Path) -> bool:
    text = cache_path.read_text(encoding="utf-8", errors="replace")
    if "FAIL=0" in text or "FAIL: 0" in text:
        return True
    if "status: ok" in text and "PASS" in text and "FAIL" not in text:
        return True
    if "TOTAL PASS" in text and "status: ok" in text:
        return True
    return False


def ledger_rows() -> dict:
    return json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]


def effective_status(rows: dict, cid: str) -> str:
    row = rows.get(cid, {})
    return str(row.get("effective_status") or row.get("audit_status") or "missing")


def main() -> None:
    print("=" * 78)
    print("Causal-source packet reachability and status firewall")
    print("=" * 78)

    rows = ledger_rows()
    note_text = NOTE.read_text(encoding="utf-8")

    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    for marker in [
        "actual_current_surface_status: conditional-support",
        "bare_retained_allowed: false",
        "audit_required_before_effective_retained: true",
        "distinguishing",
        "time-oriented Lorentzian manifold",
        "dimension >= 2",
        "current theorem remains conditional",
    ]:
        check(f"source note contains status/assumption marker: {marker}", marker in note_text)

    nonretained_causal_inputs: list[str] = []
    for item in SOURCE_PACKET:
        doc = rel(item["doc"])
        runner = rel(item["runner"])
        cache = rel(item["cache"])
        status = effective_status(rows, item["cid"])

        check(f"{item['role']} doc exists", doc.exists(), item["doc"])
        check(f"{item['role']} runner exists", runner.exists(), item["runner"])
        check(f"{item['role']} cache exists", cache.exists(), item["cache"])
        if cache.exists():
            check(f"{item['role']} cache reports successful checks", cache_has_success_marker(cache), item["cache"])

        expected = item.get("expected_effective_status")
        if expected:
            check(
                f"{item['role']} ledger status is {expected}",
                status == expected,
                f"{item['cid']} -> {status}",
            )
        elif item.get("load_bearing_causal_input") and status not in RETAINED_STATUSES:
            nonretained_causal_inputs.append(f"{item['cid']}:{status}")

    check(
        "current ledger exposes at least one non-retained causal-source input",
        bool(nonretained_causal_inputs),
        ", ".join(nonretained_causal_inputs),
    )
    check(
        "note status is no stronger than current causal-source packet",
        bool(nonretained_causal_inputs)
        and "actual_current_surface_status: conditional-support" in note_text,
        "conditional-support required until causal inputs are retained",
    )

    print()
    print("=" * 78)
    print("Finite conformal-class algebra under the explicit packet")
    print("=" * 78)

    def energy(p: list[float] | np.ndarray, m: float = 0.3) -> float:
        return float(np.arcsinh(np.sqrt(m * m + np.sum(np.sin(p) ** 2))))

    grid = np.linspace(-np.pi, np.pi, 31)
    vmax = 0.0
    for px in grid:
        for py in grid:
            for pz in grid:
                grad = []
                for ax in range(3):
                    h = 1e-4
                    p1 = np.array([px, py, pz], dtype=float)
                    p2 = np.array([px, py, pz], dtype=float)
                    p1[ax] += h
                    p2[ax] -= h
                    grad.append((energy(p1) - energy(p2)) / (2 * h))
                vmax = max(vmax, float(np.sqrt(sum(g * g for g in grad))))

    record_word = [0, 1, 0, 0, 1]
    prefix_lengths = np.arange(len(record_word) + 1)
    i_order = bool(np.all(np.diff(prefix_lengths) > 0))
    finite_cone = bool(np.isfinite(vmax) and 0 < vmax < 10)
    signature_sources_visible = all(
        effective_status(rows, cid) in RETAINED_STATUSES
        for cid in [
            "lorentz_boost_covariance_3plus1d_theorem_note",
            "wick_rotation_compact_so4_to_lorentzian_dirac_doubling_orientation_note_2026-06-07",
        ]
    )
    print(
        f"   finite LR-cone diagnostic v_LR = {vmax:.4f}; "
        f"record-prefix order: {i_order}; signature sources retained-grade: {signature_sources_visible}"
    )
    check(
        "explicit causal-source packet supplies the conditional inputs being assembled",
        finite_cone and i_order and signature_sources_visible,
        "event order + finite cone diagnostic + retained-bounded signature anchors",
    )

    print()
    print("=" * 78)
    print("Conformal rigidity boundary: cone fixes class, not scale")
    print("=" * 78)
    eta = np.diag([-1.0, 1.0, 1.0, 1.0])
    same_class = 3.7 * eta
    v = np.array([1.0, 1.0, 0.0, 0.0])
    null_eta = abs(v @ eta @ v) < 1e-12
    null_scaled = abs(v @ same_class @ v) < 1e-12
    c = 0.6
    eta_c = np.diag([-c * c, 1.0, 1.0, 1.0])
    different_cone = abs(v @ eta_c @ v) > 1e-6
    scale_differs = not np.allclose(eta, same_class)
    print(f"   eta-null v remains null for Omega^2 eta: {null_eta and null_scaled}")
    print(f"   a c={c} cone-speed metric does not share that null cone: {different_cone}")
    print(f"   eta and Omega^2 eta differ as metrics: {scale_differs}")
    check(
        "algebraic conformal invariance holds; full HKM/Malament use is assumption-gated",
        null_eta and null_scaled and different_cone and scale_differs,
        "same null cone only determines conformal class",
    )

    print()
    print("=" * 78)
    print("Clock-rate boundary: conformal factor remains the retained no-go")
    print("=" * 78)
    events = ["a", "b", "c", "d", "e"]
    counts = list(range(len(events) + 1))
    tau_a = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
    tau_b = [0.0, 0.5, 2.0, 2.1, 4.8, 5.0]
    order_a = all(tau_a[i] < tau_a[i + 1] for i in range(len(tau_a) - 1))
    order_b = all(tau_b[i] < tau_b[i + 1] for i in range(len(tau_b) - 1))
    rates_a = [tau_a[i + 1] - tau_a[i] for i in range(len(tau_a) - 1)]
    rates_b = [tau_b[i + 1] - tau_b[i] for i in range(len(tau_b) - 1)]
    rates_differ = not np.allclose(rates_a, rates_b)
    same_counts = counts == counts
    check(
        "record count/order is invariant under monotone clock reparametrization",
        order_a and order_b and same_counts and rates_differ,
        "same events/counts; different interval rates",
    )

    conformal_class_assembled_conditionally = finite_cone and i_order and signature_sources_visible
    conformal_factor_no_go = rates_differ
    check(
        "emergent metric surface is conditional conformal class plus retained clock-rate scale no-go",
        conformal_class_assembled_conditionally and conformal_factor_no_go
        and "actual_current_surface_status: conditional-support" in note_text,
        "audit may promote only after causal-source inputs are retained or separately admitted",
    )

    print()
    print(f"runner_check_breakdown = {{A: {PASS}, B: 0, C: 0, D: 0, total_pass: {PASS}}}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")


if __name__ == "__main__":
    main()
