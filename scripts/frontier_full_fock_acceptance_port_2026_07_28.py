#!/usr/bin/env python3
"""Input port from the full-Fock support surface into the acceptance harness.

This is acceptance infrastructure only.  The full-Fock module is imported
under its main guard and queried through public, side-effect-free entry points
for data probes.  Its complete 8/8 certificate is run separately in a
subprocess.  No source, response, or gravity law is supplied here.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/FULL_FOCK_ACCEPTANCE_PORT_SUPPORT_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_source_acceptance_harness_2026_07_28.py",
    "scripts/frontier_full_fock_unit_weight_source_2026_07_28.py",
)

import ast
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from typing import Any

import numpy as np

import frontier_source_acceptance_harness_2026_07_28 as H
import frontier_full_fock_unit_weight_source_2026_07_28 as FF


ROOT = Path(__file__).resolve().parents[1]
PORT_PATH = "scripts/frontier_full_fock_acceptance_port_2026_07_28.py"
FULL_FOCK_PATH = AUDIT_INPUT_PATHS[1]
FULL_FOCK_SHA256 = "fe5ce8e2e993a1da5ff1b05f18706a62a44c3ad6d28347b28fa4493fd24ba8c9"
FULL_FOCK_TERMINAL_MARKER = "FINAL_JSON"
PROBE_FEED_SHAPE = (3, 6)
PROBE_MODE = (
    "in-process public calls after side-effect-free main-guarded import; "
    "complete certificate in subprocess"
)

SELF_RUN_LABELS = (
    "the landed coefficient-two diagonal splits exactly into mediator weight one plus auxiliary weight one",
    "the reused source preserves Q and local occupation number",
    "layer 1 reproduces all six landed U320 LinkState recoil rows",
    "every allowed channel through n_max has the exact landed unit-weight recoil ledger",
    "the two-cell truncated Fock space is exhaustively layer-independent",
    "reciprocity holds in every layer and on a coherent n=1 plus n=2 state",
    "a deliberate n=2 to n=1 mis-embedding breaks layer independence",
    "the byte-pinned Cycle-322 harness reruns unchanged",
)

FROZEN_EXPECTED = {
    "source_sha256": FULL_FOCK_SHA256,
    "self_run": {
        "fail": 0,
        "labels": SELF_RUN_LABELS,
        "pass": 8,
        "summary": {"fail": 0, "pass": 8},
        "terminal_marker": FULL_FOCK_TERMINAL_MARKER,
        "total": 8,
    },
    "accept": {
        "anchor": {
            "component_residual_upper_bound": 3e-10,
            "directions": 6,
            "emitted_weight": 0.1258992161287137,
            "weight_absolute_tolerance": 3e-10,
        },
        "layer_channels": {
            "active_channels": (0, 6, 24),
            "numbers": (0, 1, 2),
        },
        "recoil_triples": {
            "layers": (
                {
                    "active_channels": 0,
                    "direction_multiplicities": {},
                    "exact_triples": 0,
                    "number": 0,
                },
                {
                    "active_channels": 6,
                    "direction_multiplicities": {
                        "-1,0,0": 1,
                        "0,-1,0": 1,
                        "0,0,-1": 1,
                        "0,0,1": 1,
                        "0,1,0": 1,
                        "1,0,0": 1,
                    },
                    "exact_triples": 6,
                    "number": 1,
                },
                {
                    "active_channels": 24,
                    "direction_multiplicities": {
                        "-1,0,0": 4,
                        "0,-1,0": 4,
                        "0,0,-1": 4,
                        "0,0,1": 4,
                        "0,1,0": 4,
                        "1,0,0": 4,
                    },
                    "exact_triples": 24,
                    "number": 2,
                },
            ),
            "maximum_component_residual": 0.0,
            "multipliers": {
                "auxiliary": 1,
                "matter": -2,
                "mediator": 1,
            },
        },
        "probe_mode": PROBE_MODE,
    },
    "reject": {
        "malformed_feed": {
            "label": "port-schema",
            "signature": (
                "PORT_SCHEMA:MALFORMED_FEED_SHAPE:"
                "expected=[3, 6]:observed=[2, 6]"
            ),
        },
        "misembedded_layer": {
            "label": "landed-control",
            "signature": (
                "LANDED_CONTROL:MIS_EMBEDDING_DETECTED:number=2->1"
            ),
        },
        "out_of_domain": {
            "label": "port-schema",
            "signature": (
                "PORT_SCHEMA:N_MAX_OUT_OF_SCOPE:requested=3:declared=2"
            ),
        },
    },
}


_PASS = 0
_FAIL = 0


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _jsonable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _jsonable(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_jsonable(item) for item in value]
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return repr(value)


def _digest(value: Any) -> str:
    encoded = json.dumps(
        _jsonable(value),
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def check(label: str, condition: bool, detail: Any = "") -> bool:
    global _PASS, _FAIL
    if condition:
        _PASS += 1
        status = "PASS"
    else:
        _FAIL += 1
        status = "FAIL"
    rendered = json.dumps(_jsonable(detail), sort_keys=True, separators=(",", ":"))
    print(f"{status} {label} :: {rendered}")
    return condition


class FullFockAcceptance:
    """Byte-pinned, input-ported acceptance surface for the full-Fock runner."""

    SOURCE_PATH = FULL_FOCK_PATH
    LANDED_SHA256_PIN = FULL_FOCK_SHA256
    FROZEN_EXPECTED = FROZEN_EXPECTED

    def __init__(
        self,
        source_path: Path | None = None,
        expected_sha256: str | None = None,
    ) -> None:
        self.source_path = (
            source_path.resolve()
            if source_path is not None
            else (ROOT / self.SOURCE_PATH).resolve()
        )
        self.expected_sha256 = expected_sha256 or self.LANDED_SHA256_PIN
        self.actual_sha256 = _sha256(self.source_path)
        self.pin_verified = self.actual_sha256 == self.expected_sha256

    def frozen_expected(self) -> dict[str, Any]:
        return copy.deepcopy(self.FROZEN_EXPECTED)

    def _pin_still_verified(self) -> bool:
        self.actual_sha256 = _sha256(self.source_path)
        self.pin_verified = self.actual_sha256 == self.expected_sha256
        return self.pin_verified

    def _base_record(self) -> dict[str, Any]:
        return {
            "expected_sha256": self.expected_sha256,
            "pin_verified": self.pin_verified,
            "source_path": (
                self.SOURCE_PATH
                if self.source_path == (ROOT / self.SOURCE_PATH).resolve()
                else str(self.source_path)
            ),
            "source_sha256": self.actual_sha256,
        }

    def _drift_record(self) -> dict[str, Any]:
        return {
            **self._base_record(),
            "probes": {},
            "self_run": {},
        }

    def _reject_record(
        self,
        *,
        label: str,
        signature: str,
        evidence: Any,
    ) -> dict[str, Any]:
        return {
            **self._base_record(),
            "probes": {},
            "rejection": {
                "evidence": _jsonable(evidence),
                "label": label,
                "signature": signature,
            },
            "self_run": {},
        }

    def _run_self_certificate(self) -> dict[str, Any]:
        environment = os.environ.copy()
        scripts_path = str(ROOT / "scripts")
        environment["PYTHONPATH"] = (
            scripts_path
            if not environment.get("PYTHONPATH")
            else scripts_path + os.pathsep + environment["PYTHONPATH"]
        )
        started = time.monotonic()
        completed = subprocess.run(
            [sys.executable, str(self.source_path)],
            cwd=ROOT,
            env=environment,
            capture_output=True,
            check=False,
            text=True,
            timeout=AUDIT_TIMEOUT_SEC,
        )
        elapsed = time.monotonic() - started
        pattern = re.compile(r"^(PASS|FAIL) (.*?) ::")
        rows = []
        terminal_rows = []
        for line in completed.stdout.splitlines():
            match = pattern.match(line)
            if match:
                status, label = match.groups()
                rows.append({"label": label, "pass": status == "PASS"})
            if line.startswith(FULL_FOCK_TERMINAL_MARKER + " "):
                try:
                    terminal_rows.append(
                        json.loads(line[len(FULL_FOCK_TERMINAL_MARKER) + 1 :])
                    )
                except json.JSONDecodeError:
                    terminal_rows.append(None)
        terminal = terminal_rows[0] if len(terminal_rows) == 1 else None
        return {
            "fail": sum(not row["pass"] for row in rows),
            "labels": [row["label"] for row in rows],
            "pass": sum(row["pass"] for row in rows),
            "returncode": completed.returncode,
            "runtime_seconds": round(elapsed, 6),
            "stderr_empty": completed.stderr == "",
            "stdout_bytes": len(completed.stdout.encode("utf-8")),
            "summary": terminal.get("summary") if isinstance(terminal, dict) else None,
            "terminal_marker": (
                FULL_FOCK_TERMINAL_MARKER
                if isinstance(terminal, dict)
                and terminal.get("full_fock_construction_achieved") is True
                else None
            ),
            "total": len(rows),
        }

    @staticmethod
    def _anchor_probe(vertex: np.ndarray) -> dict[str, Any]:
        rows, maximum_component_residual = FF.landed_one_carrier_rows(vertex)
        return {
            "directions": len(rows),
            "emitted_weights": [
                float(row["emitted_weight"]) for row in rows
            ],
            "maximum_component_residual": float(maximum_component_residual),
        }

    @staticmethod
    def _layer_channel_probe(
        exchange: np.ndarray,
        vertex: np.ndarray,
    ) -> dict[str, Any]:
        rows, ledger_residual, _reciprocity_residual = (
            FF.per_layer_certificates(exchange, vertex)
        )
        return {
            "active_channels": [
                int(row["active_channels"]) for row in rows
            ],
            "maximum_generator_ledger_residual": float(ledger_residual),
            "numbers": [int(row["number"]) for row in rows],
        }

    @staticmethod
    def _recoil_triple_probe() -> dict[str, Any]:
        layers = []
        maximum_component_residual = 0.0
        for number in range(FF.N_MAX + 1):
            active_channels = 0
            exact_triples = 0
            multiplicities: dict[str, int] = {}
            for mask in FF.S322.LOCAL_MASKS:
                if mask.bit_count() != number:
                    continue
                for direction in range(6):
                    hopped = FF.S322.fermion_hop(
                        mask,
                        direction,
                        FF.U320.REVERSE[direction],
                    )
                    if hopped is None:
                        continue
                    target_mask, _sign = hopped
                    direction_vector = np.asarray(
                        FF.U320.c210.DIRECTIONS[direction],
                        dtype=int,
                    )
                    matter = FF.mask_vector(target_mask) - FF.mask_vector(mask)
                    mediator = direction_vector
                    auxiliary = direction_vector
                    residual = max(
                        float(np.max(abs(matter + 2 * direction_vector))),
                        float(np.max(abs(mediator - direction_vector))),
                        float(np.max(abs(auxiliary - direction_vector))),
                    )
                    maximum_component_residual = max(
                        maximum_component_residual,
                        residual,
                    )
                    exact_triples += int(residual == 0.0)
                    active_channels += 1
                    key = ",".join(str(int(value)) for value in direction_vector)
                    multiplicities[key] = multiplicities.get(key, 0) + 1
            layers.append(
                {
                    "active_channels": active_channels,
                    "direction_multiplicities": dict(sorted(multiplicities.items())),
                    "exact_triples": exact_triples,
                    "number": number,
                }
            )
        return {
            "layers": layers,
            "maximum_component_residual": maximum_component_residual,
            "multipliers": {
                "auxiliary": 1,
                "matter": -2,
                "mediator": 1,
            },
        }

    def accept(
        self,
        *,
        n_max: int = 2,
        layer_map: str = "canonical",
        feed: Any | None = None,
    ) -> dict[str, Any]:
        if not self._pin_still_verified():
            return self._drift_record()

        if n_max != FF.N_MAX:
            signature = (
                f"PORT_SCHEMA:N_MAX_OUT_OF_SCOPE:"
                f"requested={n_max}:declared={FF.N_MAX}"
            )
            return self._reject_record(
                label="port-schema",
                signature=signature,
                evidence={"declared_n_max": FF.N_MAX, "requested_n_max": n_max},
            )

        if feed is not None:
            try:
                observed_feed = np.asarray(feed)
            except Exception as exc:
                return self._reject_record(
                    label="port-schema",
                    signature=(
                        "PORT_SCHEMA:MALFORMED_FEED_SHAPE:"
                        "expected=[3, 6]:observed=unreadable"
                    ),
                    evidence=f"{type(exc).__name__}: {exc}",
                )
            if observed_feed.shape != PROBE_FEED_SHAPE:
                signature = (
                    "PORT_SCHEMA:MALFORMED_FEED_SHAPE:"
                    f"expected={list(PROBE_FEED_SHAPE)}:"
                    f"observed={list(observed_feed.shape)}"
                )
                return self._reject_record(
                    label="port-schema",
                    signature=signature,
                    evidence={
                        "expected_shape": list(PROBE_FEED_SHAPE),
                        "observed_shape": list(observed_feed.shape),
                    },
                )
            if not np.all(observed_feed == 1):
                return self._reject_record(
                    label="port-schema",
                    signature="PORT_SCHEMA:INCOMPLETE_PROBE_FEED",
                    evidence={"nonunit_entries": int(np.sum(observed_feed != 1))},
                )

        exchange, vertex, _charge, _number, _momenta = (
            FF.S322.local_source_blocks(FF.U320.ANGLE)
        )
        if layer_map == "misembedded":
            bad = FF.misembedding_control(exchange)
            detected = (
                bad["source_number"] == 2
                and bad["target_number"] == 1
                and bad["cross_layer_generator_amplitude"] == 1.0
                and bad["number_commutator_frobenius"] > 1.4
            )
            signature = (
                "LANDED_CONTROL:MIS_EMBEDDING_DETECTED:number=2->1"
                if detected
                else "LANDED_CONTROL:MIS_EMBEDDING_CONTROL_FAILED"
            )
            return self._reject_record(
                label="landed-control",
                signature=signature,
                evidence=bad,
            )
        if layer_map != "canonical":
            return self._reject_record(
                label="port-schema",
                signature=f"PORT_SCHEMA:UNSUPPORTED_LAYER_MAP:{layer_map}",
                evidence={"layer_map": layer_map},
            )

        probes = {
            "anchor": self._anchor_probe(vertex),
            "layer_channels": self._layer_channel_probe(exchange, vertex),
            "probe_mode": PROBE_MODE,
            "recoil_triples": self._recoil_triple_probe(),
        }
        return {
            **self._base_record(),
            "n_max": n_max,
            "probes": probes,
            "self_run": self._run_self_certificate(),
        }

    @staticmethod
    def _matches_expected(
        record: dict[str, Any],
        expected: dict[str, Any],
    ) -> bool:
        if (
            record.get("pin_verified") is not True
            or record.get("source_sha256") != expected["source_sha256"]
            or record.get("expected_sha256") != expected["source_sha256"]
        ):
            return False
        self_run = record.get("self_run", {})
        frozen_run = expected["self_run"]
        if not (
            self_run.get("returncode") == 0
            and self_run.get("stderr_empty") is True
            and self_run.get("pass") == frozen_run["pass"]
            and self_run.get("fail") == frozen_run["fail"]
            and self_run.get("total") == frozen_run["total"]
            and tuple(self_run.get("labels", ())) == tuple(frozen_run["labels"])
            and self_run.get("summary") == frozen_run["summary"]
            and self_run.get("terminal_marker")
            == frozen_run["terminal_marker"]
        ):
            return False

        probes = record.get("probes", {})
        frozen_accept = expected["accept"]
        anchor = probes.get("anchor", {})
        frozen_anchor = frozen_accept["anchor"]
        weights = anchor.get("emitted_weights", [])
        anchor_matches = (
            anchor.get("directions") == frozen_anchor["directions"]
            and len(weights) == frozen_anchor["directions"]
            and all(
                abs(float(weight) - frozen_anchor["emitted_weight"])
                <= frozen_anchor["weight_absolute_tolerance"]
                for weight in weights
            )
            and anchor.get("maximum_component_residual", float("inf"))
            < frozen_anchor["component_residual_upper_bound"]
        )
        channels = probes.get("layer_channels", {})
        frozen_channels = frozen_accept["layer_channels"]
        channels_match = (
            tuple(channels.get("numbers", ()))
            == tuple(frozen_channels["numbers"])
            and tuple(channels.get("active_channels", ()))
            == tuple(frozen_channels["active_channels"])
            and channels.get(
                "maximum_generator_ledger_residual",
                float("inf"),
            )
            == 0.0
        )
        recoil_matches = (
            probes.get("recoil_triples")
            == _jsonable(frozen_accept["recoil_triples"])
        )
        return (
            anchor_matches
            and channels_match
            and recoil_matches
            and probes.get("probe_mode") == frozen_accept["probe_mode"]
        )

    def verdict_against(
        self,
        record: dict[str, Any],
        expected: dict[str, Any],
    ) -> str:
        if (
            record.get("pin_verified") is not True
            or record.get("source_sha256") != record.get("expected_sha256")
        ):
            return "DRIFT"
        if "rejection" in record:
            return "REJECT"
        return "ACCEPT" if self._matches_expected(record, expected) else "REJECT"

    def verdict(self, record: dict[str, Any]) -> str:
        return self.verdict_against(record, self.FROZEN_EXPECTED)


ACCEPTANCE_SURFACE_REGISTRY = {
    "tensor_lift": H.TensorLiftAcceptance,
    "recoil_reciprocity": H.RecoilReciprocityAcceptance,
    "typed_bridge": H.TypedBridgeAcceptance,
    "full_fock": FullFockAcceptance,
}


def _attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def _qualified_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _qualified_name(node.value)
        return f"{parent}.{node.attr}" if parent else None
    return None


def firewall_ast_audit() -> dict[str, Any]:
    """Prove this port is data-only and never writes into either landed module."""
    source = (ROOT / PORT_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PORT_PATH)
    landed_roots = {"FF", "H"}
    attribute_writes = sorted(
        {
            f"{_attribute_root(node)}.{node.attr}"
            for node in ast.walk(tree)
            if isinstance(node, ast.Attribute)
            and isinstance(node.ctx, (ast.Store, ast.Del))
            and _attribute_root(node) in landed_roots
        }
    )

    forbidden_definition_names = {
        "C_source",
        "gravity_content",
        "gravity_law",
        "response_law",
        "source_law",
    }
    forbidden_definitions = sorted(
        {
            node.id
            for node in ast.walk(tree)
            if isinstance(node, ast.Name)
            and isinstance(node.ctx, ast.Store)
            and node.id in forbidden_definition_names
        }
        | {
            node.name
            for node in ast.walk(tree)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
            and node.name in forbidden_definition_names
        }
    )

    allowed_landed_calls = {
        "FF.S322.fermion_hop",
        "FF.S322.local_source_blocks",
        "FF.landed_one_carrier_rows",
        "FF.mask_vector",
        "FF.misembedding_control",
        "FF.per_layer_certificates",
    }
    landed_calls = sorted(
        {
            qualified
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            for qualified in [_qualified_name(node.func)]
            if qualified is not None
            and (
                qualified.startswith("FF.")
                or qualified.startswith("H.")
            )
        }
    )
    non_data_calls = sorted(set(landed_calls) - allowed_landed_calls)
    return {
        "attribute_writes": attribute_writes,
        "forbidden_definitions": forbidden_definitions,
        "landed_calls": landed_calls,
        "non_data_calls": non_data_calls,
        "passes": (
            not attribute_writes
            and not forbidden_definitions
            and not non_data_calls
        ),
        "policy": (
            "data-only public probes; no C_source/source/response/gravity law; "
            "zero attribute writes into H or FF"
        ),
    }


def drift_demo() -> dict[str, Any]:
    real_path = (ROOT / FULL_FOCK_PATH).resolve()
    real_before = _sha256(real_path)
    original = real_path.read_bytes()
    with tempfile.TemporaryDirectory(prefix="full_fock_port_drift_") as directory:
        sandbox_path = Path(directory) / real_path.name
        sandbox_path.write_bytes(original)
        mutated = bytearray(original)
        mutation_index = len(mutated) // 2
        mutated[mutation_index] ^= 1
        sandbox_path.write_bytes(mutated)
        differing_bytes = sum(
            before != after for before, after in zip(original, mutated)
        )
        sandbox_surface = FullFockAcceptance(source_path=sandbox_path)
        drift_record = sandbox_surface.accept()
        drift_verdict = sandbox_surface.verdict(drift_record)
        sandbox_sha256 = drift_record["source_sha256"]
    real_after = _sha256(real_path)
    return {
        "differing_bytes": differing_bytes,
        "detected": drift_verdict == "DRIFT",
        "real_sha256_after": real_after,
        "real_sha256_before": real_before,
        "real_unchanged": (
            real_before == FULL_FOCK_SHA256
            and real_after == FULL_FOCK_SHA256
        ),
        "sandbox_sha256": sandbox_sha256,
        "verdict": drift_verdict,
    }


def main() -> int:
    global _PASS, _FAIL
    _PASS = 0
    _FAIL = 0
    started = time.monotonic()

    surface = FullFockAcceptance()
    canonical = surface.accept()
    canonical_verdict = surface.verdict(canonical)
    self_run = canonical.get("self_run", {})
    a_pass = (
        surface.pin_verified
        and canonical_verdict == "ACCEPT"
        and self_run.get("pass") == 8
        and self_run.get("fail") == 0
        and self_run.get("total") == 8
        and self_run.get("terminal_marker") == FULL_FOCK_TERMINAL_MARKER
    )
    check(
        "A. byte pin and self-run frozen 8/8 reproduce",
        a_pass,
        {
            "pin_verified": surface.pin_verified,
            "self_run": self_run,
            "verdict": canonical_verdict,
        },
    )

    probes = canonical.get("probes", {})
    b_pass = (
        canonical_verdict == "ACCEPT"
        and set(probes)
        == {"anchor", "layer_channels", "probe_mode", "recoil_triples"}
    )
    check(
        "B. ACCEPT probes match frozen anchor, layers, and recoil triples",
        b_pass,
        {
            "anchor": probes.get("anchor"),
            "layer_channels": probes.get("layer_channels"),
            "recoil_triples": probes.get("recoil_triples"),
        },
    )

    reject_records = {
        "out_of_domain": surface.accept(n_max=3),
        "misembedded_layer": surface.accept(layer_map="misembedded"),
        "malformed_feed": surface.accept(feed=np.ones((2, 6), dtype=int)),
    }
    reject_results = {
        name: {
            "label": record.get("rejection", {}).get("label"),
            "signature": record.get("rejection", {}).get("signature"),
            "verdict": surface.verdict(record),
        }
        for name, record in reject_records.items()
    }
    c_pass = all(
        reject_results[name]
        == {
            **expected,
            "verdict": "REJECT",
        }
        for name, expected in FROZEN_EXPECTED["reject"].items()
    )
    check(
        "C. REJECT witnesses refuse with frozen honest signatures",
        c_pass,
        reject_results,
    )

    drift = drift_demo()
    check(
        "D. one-byte sandbox DRIFT is detected and real SHA is unchanged",
        (
            drift["detected"]
            and drift["differing_bytes"] == 1
            and drift["real_unchanged"]
        ),
        drift,
    )

    wrong_expected = surface.frozen_expected()
    wrong_expected["accept"]["anchor"]["emitted_weight"] = 0.2258992161287137
    wrong_verdict = surface.verdict_against(canonical, wrong_expected)
    adversary = {
        "canonical_verdict": canonical_verdict,
        "caught": wrong_verdict == "REJECT",
        "quarantined": (
            FROZEN_EXPECTED["accept"]["anchor"]["emitted_weight"]
            == 0.1258992161287137
        ),
        "wrong_expectation_digest": _digest(wrong_expected),
        "wrong_expectation_verdict": wrong_verdict,
    }
    check(
        "E. quarantined wrong expectation is caught",
        adversary["caught"] and adversary["quarantined"],
        adversary,
    )

    firewall = firewall_ast_audit()
    registry_ok = (
        ACCEPTANCE_SURFACE_REGISTRY.get("full_fock") is FullFockAcceptance
        and len(ACCEPTANCE_SURFACE_REGISTRY) == 4
    )
    check(
        "F. firewall AST passes with zero landed-module attribute writes",
        firewall["passes"] and registry_ok,
        {
            "firewall": firewall,
            "registry": sorted(ACCEPTANCE_SURFACE_REGISTRY),
        },
    )

    runtime = time.monotonic() - started
    final = {
        "adversary": adversary,
        "audit_input_paths": list(AUDIT_INPUT_PATHS),
        "checks": {"fail": _FAIL, "pass": _PASS, "total": _PASS + _FAIL},
        "drift": drift,
        "firewall": firewall,
        "frozen_expectation_digest": _digest(FROZEN_EXPECTED),
        "note_path": NOTE_PATH,
        "probe_census": {
            "ACCEPT": 3,
            "ADVERSARY": 1,
            "DRIFT": 1,
            "REJECT": 3,
        },
        "reject_witnesses": reject_results,
        "runtime_seconds": round(runtime, 6),
        "surface_registry": sorted(ACCEPTANCE_SURFACE_REGISTRY),
        "verdict": canonical_verdict,
    }
    print(json.dumps(final, separators=(",", ":"), sort_keys=True))
    return int(_FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
