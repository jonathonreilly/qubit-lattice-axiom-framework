#!/usr/bin/env python3
"""Guard audit-model slug normalization against the apply-audit family gate."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import codex_audit_runner as runner


def load_apply_audit_module():
    path = ROOT / "docs" / "audit" / "scripts" / "apply_audit.py"
    spec = importlib.util.spec_from_file_location("apply_audit_guard_target", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    apply_audit = load_apply_audit_module()
    cases = {
        "gpt-5.5": "codex-gpt-5.5",
        "gpt-5.6": "codex-gpt-5.6",
        "gpt-5.6-sol": "codex-gpt-5.6",
        "gpt-6": "codex-gpt-6",
    }
    for model, expected_family in cases.items():
        model_info = {
            "slug": model,
            "reasoning_levels": [{"effort": runner.AUDIT_REASONING_EFFORT}],
        }
        if not runner._is_full_gpt_audit_model(model_info):
            raise RuntimeError(f"{model}: accepted full model was not selectable")
        actual_family = runner.codex_family_for_model(model)
        if actual_family != expected_family:
            raise RuntimeError(
                f"{model}: expected {expected_family}, got {actual_family}"
            )
        if not apply_audit._family_meets_floor(actual_family):
            raise RuntimeError(
                f"{model}: normalized family {actual_family} failed apply-audit floor"
            )
        provenance_error = apply_audit.validate_auditor_provenance(
            {
                "auditor_model": model,
                "auditor_family": actual_family,
                "auditor_reasoning_effort": runner.AUDIT_REASONING_EFFORT,
            }
        )
        if provenance_error:
            raise RuntimeError(f"{model}: provenance rejected: {provenance_error}")

    rejected_models = (
        "gpt-5.6-mini",
        "gpt-5.6-auto-review",
        "gpt-5.6foo",
        "gpt-5.6-sol-preview",
    )
    for model in rejected_models:
        model_info = {
            "slug": model,
            "reasoning_levels": [{"effort": runner.AUDIT_REASONING_EFFORT}],
        }
        if runner._is_full_gpt_audit_model(model_info):
            raise RuntimeError(f"{model}: unsupported cache model was selectable")
        family = runner.codex_family_for_model(model)
        if runner._meets_floor(model):
            raise RuntimeError(f"{model}: unsupported audit model passed runner floor")
        if apply_audit._family_meets_floor(family):
            raise RuntimeError(f"{model}: unsupported family {family} passed apply floor")
        for declared_family in (family, "human", "codex-current"):
            provenance_error = apply_audit.validate_auditor_provenance(
                {
                    "auditor_model": model,
                    "auditor_family": declared_family,
                    "auditor_reasoning_effort": runner.AUDIT_REASONING_EFFORT,
                }
            )
            if not provenance_error:
                raise RuntimeError(
                    f"{model}: unsupported model passed provenance as "
                    f"{declared_family}"
                )

    if (
        runner.canonicalize_existing_auditor_family("codex-gpt-5.6-sol")
        != "codex-gpt-5.6"
    ):
        raise RuntimeError("existing Sol family did not canonicalize for role comparison")

    first = {
        "auditor": "first-auditor",
        "auditor_family": "codex-gpt-5.6-sol",
    }
    second = {
        "auditor": "second-auditor",
        "auditor_family": "codex-gpt-5.6",
        "independence": "cross_family",
    }
    if not apply_audit.cross_confirmation_error(first, second):
        raise RuntimeError("legacy Sol family bypassed same-family second-pass gate")
    second["independence"] = "fresh_context"
    if apply_audit.cross_confirmation_error(first, second):
        raise RuntimeError("fresh-context Sol-family second pass was rejected")

    cross_confirmation = {
        "first_audit": first,
        "second_audit": {
            "auditor": "other-auditor",
            "auditor_family": "codex-gpt-5.5",
        },
    }
    third = {
        "auditor": "third-auditor",
        "auditor_family": "codex-gpt-5.6",
        "independence": "cross_family",
    }
    if not apply_audit.third_confirmation_error(cross_confirmation, third):
        raise RuntimeError("legacy Sol family bypassed same-family third-pass gate")
    third["independence"] = "fresh_context"
    if apply_audit.third_confirmation_error(cross_confirmation, third):
        raise RuntimeError("fresh-context Sol-family third pass was rejected")
    print("audit_model_family_normalization_guard: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
