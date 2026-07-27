#!/usr/bin/env python3
"""Emit the five live-output resolution classes required by N5 audits."""

from __future__ import annotations


Resolution = tuple[bool, str]


def emit_n5_resolution_certificate(
    *,
    per_element: Resolution,
    per_site: Resolution,
    per_mode: Resolution,
    per_block: Resolution,
    lattice_wide: Resolution,
) -> None:
    """Print claim-bound predicates without changing the caller's exit semantics."""
    rows = (
        ("per_element", per_element),
        ("per_site", per_site),
        ("per_mode", per_mode),
        ("per_block", per_block),
        ("lattice_wide", lattice_wide),
    )
    for label, (passed, evidence) in rows:
        detail = " ".join(str(evidence).split())
        if len(detail) < 40:
            raise ValueError(f"{label} evidence is too short for an N5 certificate")
        print(f"{label}: {'PASS' if bool(passed) else 'FAIL'} | {detail}")
