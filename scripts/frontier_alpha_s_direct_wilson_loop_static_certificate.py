#!/usr/bin/env python3
"""Finite Wilson-loop/static-potential certificate gate.

This runner deliberately avoids the physical alpha_s(M_Z), PDG-window,
Sommer-scale, continuum-running, threshold, and full-QCD bridge gates from the
historical broad runner. It certifies only the finite certificate surface that
is proposed for re-audit.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = REPO_ROOT / "outputs" / "alpha_s_direct_wilson_loop_certificate_2026-04-30.json"

FORBIDDEN_AUTHORITY_KEYS = {
    "alpha_bare_over_u0_squared",
    "alpha_lm",
    "u0",
    "mean_link",
    "plaquette_authority",
    "alpha_s_v_definition",
}


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" ({detail})" if detail else ""
        print(f"  [{status}] {name}{suffix}")


def positive_finite(x: Any) -> bool:
    return isinstance(x, (int, float)) and math.isfinite(float(x)) and float(x) > 0.0


def load_certificate(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("certificate root must be a JSON object")
    return data


def collect_forbidden_paths(obj: Any, prefix: str = "$") -> list[str]:
    hits: list[str] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_l = str(key).lower()
            if key_l in FORBIDDEN_AUTHORITY_KEYS:
                hits.append(f"{prefix}.{key}")
            hits.extend(collect_forbidden_paths(value, f"{prefix}.{key}"))
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            hits.extend(collect_forbidden_paths(value, f"{prefix}[{i}]"))
    return hits


def volume_key(ensemble: dict[str, Any]) -> tuple[int, ...] | None:
    dims = ensemble.get("dims")
    if isinstance(dims, list) and dims and all(isinstance(v, int) and v > 0 for v in dims):
        return tuple(dims)
    return None


def validate_metadata(gate: Gate, data: dict[str, Any]) -> None:
    metadata = data.get("metadata", {})
    ensembles = data.get("ensembles", [])
    betas = {
        float(e.get("beta"))
        for e in ensembles
        if isinstance(e, dict) and isinstance(e.get("beta"), (int, float))
    }
    gate.check(
        "certificate declares Wilson-loop/static-potential authority",
        isinstance(metadata, dict) and metadata.get("authority") == "wilson_loop_static_potential",
        f"authority={metadata.get('authority')!r}" if isinstance(metadata, dict) else "metadata missing",
    )
    gate.check(
        "certificate is on the configured beta=6 Wilson surface",
        isinstance(metadata, dict)
        and metadata.get("action") in {"SU3_Wilson", "Cl3Z3_SU3_Wilson"}
        and abs(float(metadata.get("g_bare", float("nan"))) - 1.0) < 1e-12
        and betas == {6.0},
        f"action={metadata.get('action')!r}, g_bare={metadata.get('g_bare')!r}, betas={sorted(betas)}"
        if isinstance(metadata, dict)
        else "metadata missing",
    )
    gate.check(
        "certificate disallows alpha_LM/u0/plaquette authority flags",
        isinstance(metadata, dict)
        and metadata.get("uses_alpha_lm_chain") is False
        and metadata.get("uses_alpha_bare_over_u0_squared") is False
        and metadata.get("uses_plaquette_as_running_coupling_input") is False,
        "all three flags must be false",
    )
    forbidden = collect_forbidden_paths(data)
    gate.check(
        "certificate exposes no forbidden authority keys",
        not forbidden,
        ", ".join(forbidden[:5]) if forbidden else "no forbidden keys",
    )


def validate_ensembles(gate: Gate, data: dict[str, Any]) -> None:
    ensembles = data.get("ensembles")
    gate.check("certificate contains three ensembles", isinstance(ensembles, list) and len(ensembles) == 3)
    if not isinstance(ensembles, list):
        return

    volumes: set[tuple[int, ...]] = set()
    min_cfg_ok = True
    qualified_loops = 0
    plateau_ok = 0
    plateau_total = 0
    force_points = 0
    local_alpha_points = 0

    for ensemble in ensembles:
        if not isinstance(ensemble, dict):
            min_cfg_ok = False
            continue
        key = volume_key(ensemble)
        if key is not None:
            volumes.add(key)
        min_cfg_ok = min_cfg_ok and isinstance(ensemble.get("n_cfg"), int) and ensemble["n_cfg"] >= 500

        for loop in ensemble.get("wilson_loops", []):
            if not isinstance(loop, dict):
                continue
            mean = loop.get("mean")
            stderr = loop.get("stderr")
            n_cfg = loop.get("n_cfg", ensemble.get("n_cfg"))
            if positive_finite(mean) and positive_finite(stderr) and isinstance(n_cfg, int):
                rel = abs(float(stderr) / float(mean))
                if n_cfg >= 500 and rel <= 0.05:
                    qualified_loops += 1

        for point in ensemble.get("static_potential", []):
            if not isinstance(point, dict):
                continue
            plateau_total += 1
            if (
                positive_finite(point.get("R_over_a"))
                and positive_finite(point.get("V_lattice"))
                and point.get("plateau_pass") is True
                and float(point.get("plateau_chi2_dof", 99.0)) <= 2.0
            ):
                plateau_ok += 1

        for point in ensemble.get("running_coupling", []):
            if not isinstance(point, dict):
                continue
            if positive_finite(point.get("R_over_a")) and positive_finite(point.get("alpha_qq")):
                local_alpha_points += 1

        cornell = ensemble.get("cornell_fit", {})
        if isinstance(cornell, dict) and positive_finite(cornell.get("sigma")) and positive_finite(cornell.get("e")):
            force_points += 1

    gate.check("certificate uses three distinct lattice volumes", len(volumes) == 3, f"volumes={sorted(volumes)}")
    gate.check("each ensemble has at least 500 saved configurations", min_cfg_ok)
    gate.check("Wilson-loop means and errors pass finite statistics checks", qualified_loops >= 12, f"qualified={qualified_loops}")
    gate.check("static-potential plateaus pass finite diagnostics", plateau_ok >= 12 and plateau_total >= plateau_ok, f"{plateau_ok}/{plateau_total}")
    gate.check("per-volume Cornell force fits are finite", force_points == 3, f"finite fits={force_points}")
    gate.check("local force-scheme alpha_qq values are finite at multiple points", local_alpha_points >= 12, f"points={local_alpha_points}")


def validate_global_static_fit(gate: Gate, data: dict[str, Any]) -> None:
    scale = data.get("scale_setting", {})
    fit = scale.get("global_cornell_fit", {}) if isinstance(scale, dict) else {}
    r0_values = scale.get("per_volume_r0_over_a_diagnostic", []) if isinstance(scale, dict) else []
    gate.check(
        "global Cornell fit has finite static-potential parameters",
        isinstance(fit, dict)
        and positive_finite(fit.get("sigma"))
        and positive_finite(fit.get("e"))
        and positive_finite(fit.get("r0_over_a"))
        and int(fit.get("fit_points", 0)) >= 12,
        f"sigma={fit.get('sigma') if isinstance(fit, dict) else None}, e={fit.get('e') if isinstance(fit, dict) else None}",
    )
    gate.check(
        "per-volume r0/a diagnostics are finite certificate diagnostics",
        isinstance(r0_values, list) and len(r0_values) == 3 and all(positive_finite(x) for x in r0_values),
        f"r0/a={r0_values}",
    )


def validate_firewall(gate: Gate, data: dict[str, Any]) -> None:
    metadata = data.get("metadata", {})
    cross = data.get("consistency_cross_check", {})
    result = data.get("result", {})
    gate.check(
        "physical scale and running fields are quarantined as context",
        isinstance(metadata, dict)
        and isinstance(metadata.get("scale_anchor"), str)
        and isinstance(metadata.get("running_bridge"), str)
        and isinstance(result, dict)
        and "alpha_s_MZ" in result,
        "present but not used by this runner as pass/fail evidence",
    )
    gate.check(
        "existing alpha_LM/u0 chain is cross-check only",
        isinstance(cross, dict) and cross.get("used_as_authority") is False,
        f"used_as_authority={cross.get('used_as_authority')!r}" if isinstance(cross, dict) else "missing",
    )


def main() -> int:
    cert = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_CERTIFICATE
    gate = Gate()
    print("Direct Wilson-loop static-potential certificate")
    print(f"certificate: {cert}")
    try:
        data = load_certificate(cert)
    except Exception as exc:
        gate.check("certificate can be loaded", False, repr(exc))
        print(f"PASS={gate.pass_count} FAIL={gate.fail_count}")
        return 1
    gate.check("certificate can be loaded", True)

    validate_metadata(gate, data)
    validate_ensembles(gate, data)
    validate_global_static_fit(gate, data)
    validate_firewall(gate, data)

    ok = gate.fail_count == 0
    print(f"\nDirect Wilson-loop static-potential certificate: {'PASS' if ok else 'FAIL'}")
    print(f"PASS={gate.pass_count} FAIL={gate.fail_count}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
