#!/usr/bin/env python3
"""Bounded source-level bridge for the propagator-family synthesis note.

This runner does not re-audit the parent physics rows and does not promote the
synthesis note. It checks the narrow bridge needed by
docs/PROPAGATOR_FAMILY_UNIFICATION_NOTE.md: the cited wavefield,
complex-action, and electrostatics lanes all use a factorized edge-update
scaffold in which a scalar field sampled at the edge endpoints modifies a
geometry-first path-sum transport rule.

The strongest exact same-row statement remains the existing
FIXED_FIELD_FAMILY_UNIFICATION runner: signed-source and complex-action are
checked on the same grown row. This runner is the lightweight bridge
that keeps the cross-lane synthesis honest and audit-ready.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Check:
    tag: str
    label: str
    ok: bool
    detail: str


def read(rel: str) -> str:
    return (REPO / rel).read_text(encoding="utf-8")


def has(text: str, needle: str) -> bool:
    return needle in text


def rex(text: str, pattern: str) -> bool:
    return re.search(pattern, text, flags=re.MULTILINE | re.DOTALL) is not None


def record(checks: list[Check], tag: str, label: str, ok: bool, detail: str) -> None:
    checks.append(Check(tag=tag, label=label, ok=ok, detail=detail))


def main() -> int:
    files = {
        "wave_kernel": "scripts/minimal_source_driven_field_probe.py",
        "wave_mechanism": "scripts/source_resolved_wavefield_mechanism.py",
        "complex": "scripts/complex_action_grown_companion.py",
        "electro": "scripts/electrostatics_card.py",
        "fixed": "scripts/FIXED_FIELD_FAMILY_UNIFICATION.py",
        "note": "docs/PROPAGATOR_FAMILY_UNIFICATION_NOTE.md",
    }
    src = {key: read(path) for key, path in files.items()}
    checks: list[Check] = []

    print("=" * 92)
    print("PROPAGATOR FAMILY SCAFFOLD BRIDGE")
    print("  bounded source-level certificate for a scalar edge-update scaffold")
    print("  no audit verdicts; independent audit lane remains authoritative")
    print("=" * 92)
    print()

    # Wavefield: source fields are built separately, then consumed by the same
    # exact-lattice path-sum propagator through an endpoint-averaged scalar.
    record(
        checks,
        "W1",
        "wavefield uses endpoint-averaged scalar field",
        has(src["wave_kernel"], "lf = 0.5 * (sf[si] + df[di])"),
        files["wave_kernel"],
    )
    record(
        checks,
        "W2",
        "wavefield phase action is L times scalar deformation",
        has(src["wave_kernel"], "act = L * (1.0 - lf)"),
        files["wave_kernel"],
    )
    record(
        checks,
        "W3",
        "wavefield update factorizes phase and geometry prefactor",
        has(src["wave_kernel"], "complex(math.cos(k * act), math.sin(k * act)) * w / (L * L)"),
        files["wave_kernel"],
    )
    record(
        checks,
        "W4",
        "mechanism runner feeds instantaneous, same-site, and finite-speed fields to same propagator",
        all(
            has(src["wave_mechanism"], needle)
            for needle in [
                "inst_amps = lat.propagate(inst_field, esc.m.K)",
                "same_amps = lat.propagate([[gain * v for v in row] for row in same_field], esc.m.K)",
                "wave_amps = lat.propagate([[gain * v for v in row] for row in wave_field], esc.m.K)",
            ]
        ),
        files["wave_mechanism"],
    )

    # Complex action: same scalar endpoint average, with real phase and
    # imaginary attenuation separated but still edge-local and multiplicative.
    record(
        checks,
        "C1",
        "complex-action uses endpoint-averaged scalar field",
        has(src["complex"], "lf = 0.5 * (field[i] + field[j])"),
        files["complex"],
    )
    record(
        checks,
        "C2",
        "complex-action real phase is L times scalar deformation",
        has(src["complex"], "s_real = L * (1.0 - lf)"),
        files["complex"],
    )
    record(
        checks,
        "C3",
        "complex-action imaginary part is scalar edge attenuation",
        has(src["complex"], "s_imag = gamma * L * lf")
        and has(src["complex"], "amp_factor = math.exp(max(min(decay, 50.0), -50.0))"),
        files["complex"],
    )
    record(
        checks,
        "C4",
        "complex-action update factorizes phase, attenuation, and geometry prefactor",
        has(
            src["complex"],
            "amps[j] += amps[i] * complex(math.cos(phase), math.sin(phase)) * amp_factor * w * h2 / (L * L)",
        ),
        files["complex"],
    )

    # Electrostatics: signed scalar coupling changes the same phase-action
    # slot; q_test = 0 is the neutral reduction.
    record(
        checks,
        "E1",
        "electrostatics source field is scalar charge superposition",
        has(src["electro"], "field += src.charge * SOURCE_STRENGTH / (r ** power)"),
        files["electro"],
    )
    record(
        checks,
        "E2",
        "electrostatics uses endpoint-averaged scalar field",
        has(src["electro"], "lf = 0.5 * (sf[si[nz]] + df[di[nz]])"),
        files["electro"],
    )
    record(
        checks,
        "E3",
        "electrostatics signed phase action is L times scalar deformation",
        has(src["electro"], "act = L * (1 + q_test * lf)")
        and has(src["electro"], "q_test = 0 is the neutral control"),
        files["electro"],
    )
    record(
        checks,
        "E4",
        "electrostatics update factorizes phase and geometry prefactor",
        has(src["electro"], "np.exp(1j * K * act) * w * lat._hm / (L * L)"),
        files["electro"],
    )

    # Same-row sign/complex evidence: the fixed-field runner is the stronger
    # sibling bridge for two lanes on exactly the same grown row.
    record(
        checks,
        "F1",
        "fixed-field runner feeds sign and complex summaries from the same grown row",
        all(
            has(src["fixed"], needle)
            for needle in [
                "pos, adj, layers = grow(DRIFT, RESTORE, seed)",
                "sign_summaries.append(_sign_summary(pos, adj, layers))",
                "complex_summaries.append(_complex_summary(pos, adj, layers))",
            ]
        ),
        files["fixed"],
    )
    record(
        checks,
        "F2",
        "fixed-field sign branch uses the same scalar edge-action slot",
        has(src["fixed"], "act = L * (1.0 + q_test * lf)"),
        files["fixed"],
    )
    record(
        checks,
        "F3",
        "fixed-field complex branch uses the same scalar edge-action slot",
        has(src["fixed"], "s_real = L * (1.0 - lf)")
        and has(src["fixed"], "s_imag = gamma * L * lf"),
        files["fixed"],
    )

    # Note metadata/status firewall.
    record(
        checks,
        "N1",
        "synthesis note declares this primary runner",
        "**Primary runner:** `scripts/propagator_family_scaffold_bridge.py`" in src["note"],
        files["note"],
    )
    record(
        checks,
        "N2",
        "synthesis note links the paired cache",
        "logs/runner-cache/propagator_family_scaffold_bridge.txt" in src["note"],
        files["note"],
    )
    record(
        checks,
        "N3",
        "synthesis note preserves the bounded non-closure firewall",
        all(
            phrase in src["note"]
            for phrase in [
                "bounded scaffold bridge",
                "not a continuum theorem",
                "not a full electromagnetism derivation",
                "independent audit lane",
            ]
        ),
        files["note"],
    )

    print("Certified bridge surface")
    print("- scalar fields are built outside the propagator, then sampled at edge endpoints")
    print("- edge updates keep a geometry-first path-sum prefactor")
    print("- the scalar enters only the edge action/attenuation slot")
    print("- exact same-row sign/complex sharing is delegated to FIXED_FIELD_FAMILY_UNIFICATION")
    print("- no continuum, full-EM, self-gravity, or geometry-generic conclusion is certified")
    print()

    failures = 0
    for check in checks:
        status = "PASS" if check.ok else "FAIL"
        if not check.ok:
            failures += 1
        print(f"[{status}] {check.tag} {check.label} :: {check.detail}")

    print()
    print(f"SUMMARY: PASS={len(checks) - failures} FAIL={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
