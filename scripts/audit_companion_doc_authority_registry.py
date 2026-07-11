#!/usr/bin/env python3
"""Mechanical checks for the document-authority policy and registry.

Class E infrastructure: proves nothing about physics. Verifies that the
policy's class definitions exist, the registry is well-formed, landed Class F
documents carry the no-weight formula,
and no Class F/G path is cited by the axiom/approved-primitive registry.
"""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "docs" / "audit" / "DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "doc_authority_registry.json"
PREMISE_NODES = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMALITY = ROOT / "docs" / "audit" / "AXIOM_MINIMALITY_POLICY.md"
METHOD_README = ROOT / "docs" / "ai_methodology" / "README.md"

FORMULA = "no premise or interpretive weight"
CLASSES = {"A", "C", "D", "E", "F", "G"}
CLASS_NEEDLES = [
    ("Class A — foundational notes.", "A"),
    ("Class C — runner-carried claim notes.", "C"),
    ("Class D — proposals.", "D"),
    ("Class E — process policies.", "E"),
    ("Class F — orientation memos (thinking banks).", "F"),
    ("Class G — operational surfaces.", "G"),
]


def main():
    results = []

    def check(label, ok, detail=""):
        results.append((label, bool(ok), detail))

    policy = POLICY.read_text(encoding="utf-8") if POLICY.exists() else ""
    check("policy document exists", POLICY.exists(), str(POLICY))
    for needle, cls in CLASS_NEEDLES:
        check(f"policy defines class {cls}", needle in policy, needle)
    check("policy states the Class F formula verbatim", FORMULA in policy)
    check(
        "policy names the shadow-premise failure it prevents",
        "shadow premise channel" in policy,
    )
    check(
        "policy links the axiom-channel policy and methodology front door",
        "AXIOM_MINIMALITY_POLICY.md" in policy and "ai_methodology/README.md" in policy,
    )
    check(
        "policy registers this runner",
        "scripts/audit_companion_doc_authority_registry.py" in policy,
    )

    registry_ok = True
    rows = []
    try:
        registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        rows = registry.get("rows", [])
    except Exception as exc:  # noqa: BLE001
        registry_ok = False
        check("registry parses as JSON", False, repr(exc))
    if registry_ok:
        check("registry parses as JSON", True)
        check("registry has rows", bool(rows))
        check(
            "registry uses only allowed classes",
            all(r.get("class") in CLASSES for r in rows),
        )
        check(
            "registry statuses are landed or in_flight_pr",
            all(r.get("status") in {"landed", "in_flight_pr"} for r in rows),
        )
        check(
            "in-flight rows carry a positive integer pr field",
            all(
                isinstance(r.get("pr"), int) and r.get("pr") > 0
                for r in rows
                if r.get("status") == "in_flight_pr"
            ),
        )
        landed_missing = [
            r.get("path")
            for r in rows
            if r.get("status") == "landed" and not (ROOT / r.get("path", "")).exists()
        ]
        check(
            "landed registry rows exist on disk",
            not landed_missing,
            ", ".join(landed_missing),
        )
        check(
            "registry registers the motivating Class F memo",
            any(
                r.get("class") == "F"
                and "GRADED_CONSTRAINT_PROGRAM_AND_RECORD_INFLUENCE_CRITERION" in r.get("path", "")
                for r in rows
            ),
        )
        check(
            "registry registers the axiom memo as Class A",
            any(
                r.get("class") == "A" and r.get("path") == "docs/MINIMAL_AXIOMS_2026-06-29.md"
                for r in rows
            ),
        )
        primitive_paths = {
            "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
            "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
            "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        }
        check(
            "registry registers approved primitive notes as Class A",
            primitive_paths.issubset(
                {r.get("path") for r in rows if r.get("class") == "A"}
            ),
        )
        check(
            "registry registers this policy as Class E",
            any(
                r.get("class") == "E"
                and r.get("path") == "docs/audit/DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md"
                for r in rows
            ),
        )

        landed_f_missing = []
        for r in rows:
            if r.get("class") == "F":
                p = ROOT / r.get("path", "")
                if p.exists() and FORMULA not in p.read_text(encoding="utf-8"):
                    landed_f_missing.append(r.get("path"))
        check(
            "every present Class F document carries the formula",
            not landed_f_missing,
            ", ".join(landed_f_missing),
        )

        premise_text = PREMISE_NODES.read_text(encoding="utf-8") if PREMISE_NODES.exists() else ""
        offenders = [
            r.get("path")
            for r in rows
            if r.get("class") in {"F", "G"}
            and (
                r.get("path", "") in premise_text
            )
        ]
        check(
            "no Class F/G path appears in the axiom/primitive registry",
            not offenders,
            ", ".join(offenders),
        )

    minimality = MINIMALITY.read_text(encoding="utf-8") if MINIMALITY.exists() else ""
    check(
        "axiom-channel policy links back to this policy",
        "DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md" in minimality,
    )
    method_readme = METHOD_README.read_text(encoding="utf-8") if METHOD_README.exists() else ""
    check(
        "methodology front door links to this policy",
        "DOCUMENT_AUTHORITY_AND_CITATION_POLICY.md" in method_readme,
    )

    passed = failed = 0
    for index, (label, ok, detail) in enumerate(results, start=1):
        status = "PASS" if ok else "FAIL"
        passed += ok
        failed += not ok
        suffix = f" -- {detail}" if detail and not ok else ""
        print(f"CHECK {index:02d}: {status} - {label}{suffix}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
