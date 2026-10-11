"""Build only the externally authorized rigidity publication candidate."""
from pathlib import Path
import gzip
import hashlib
import json

D = Path(__file__).resolve().parent
S = D.parent
assert str(S) == "/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011"


def sha(b):
    return hashlib.sha256(b).hexdigest()


def record(p):
    b = p.read_bytes()
    return {"path": str(p), "sha256": sha(b), "bytes": len(b),
            "logical_lines": len(b.splitlines())}


expected = {
    "INTERSPECIES_CURRENT_RIGIDITY_PROBE.md": "ca44d1c852e6cd0437cf9e98913fb5fb106abb1b42567c68fb6bf3e9a60c80b8",
    "INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md": "78c3bc3c8f223b988713cb5bd5210c1a801e8cdc5f428ee648d6284c400d97d6",
    "LEAN_RIGIDITY_STATEMENT_REVIEW.md": "14d5a11bf7476975b8067fd5d9c7f9e91381804a1b926fb324ff5b9bfd57b519",
    "interspecies_current_rigidity/rigidity_controls.py": "9fd94231d6336964e5b6556396d31363c9ab5aaf4f17298d73d8ad5c3afa3b4e",
    "interspecies_rigidity_lean/RigidityGeometry.lean": "c72e7a9a961d1eec1ff60842ac3e8a5530c8b71dfc1505dc098d7cab780044df",
    "interspecies_current_rigidity/receipt.json": "283511b410dafa614c1e4453483b540e744604e66b538a803516c8294379267f",
    "interspecies_current_rigidity_review/receipt.json": "1c3c02926c6c35277fdde7a4b174b85d2471c3c3ec4da9d39681a3c9f2f68de7",
    "interspecies_rigidity_lean/receipt.json": "4f1512919a9e4aa41cac168882d3975e4b95f72cd4620876aa7cc959201c9048",
    "interspecies_rigidity_lean_review/receipt.json": "974549d47ca67a1f82591d5cef2ab3fa3a2d5854b3b2404dfa58f265364c00a6",
    "EXCLUDED_WALK_BOOST_CURRENT_PROBE.md": "903261f54d72d6e81d0c82d5cd976bd4dd46a55c1dd4567fe23d8bce07fe1923",
}
for name, digest in expected.items():
    assert sha((S / name).read_bytes()) == digest, name

receipt_specs = [
    ("interspecies_current_rigidity", ["protected_sources", "artifacts"]),
    ("interspecies_current_rigidity_review", ["sources", "artifacts"]),
    ("interspecies_rigidity_lean", ["protected_sources", "artifacts"]),
    ("interspecies_rigidity_lean_review", ["sources", "artifacts"]),
]
verified = []
copies = set(expected) - {"EXCLUDED_WALK_BOOST_CURRENT_PROBE.md"}
omitted = []
for folder, groups in receipt_specs:
    receipt = json.loads((S / folder / "receipt.json").read_text())
    for group in groups:
        for item in receipt[group]:
            p = Path(item["path"])
            actual = sha(p.read_bytes())
            assert actual == item["sha256"], str(p)
            verified.append({"receipt": folder + "/receipt.json", "group": group,
                             "path": str(p), "sha256": actual})
            if group == "artifacts" and p.is_relative_to(S / folder):
                if p.suffix == ".olean":
                    omitted.append({"path": str(p), "sha256": actual,
                                    "reason": "Compiled object; source/log evidence is preserved, no runtime/dependency copying."})
                else:
                    assert p.suffix in {".md", ".json", ".py", ".lean", ".txt", ".log"}
                    copies.add(str(p.relative_to(S)))
copies.update([
    "repo_sync_rc_2045/agents/RC_C1_report.md",
    "repo_sync_rc_2045/agents/RC_C1_referee.md",
    "repo_sync_rc_2045/agents/RC_C1_referee_full.md",
    "repo_sync_rc_2045/SOURCE_IDENTITIES.json",
])

historical = []
for name in sorted(copies):
    p = S / name
    raw = p.read_bytes()
    rel = Path("historical") / name
    encoding = "identity"
    saved = raw
    if p.suffix == ".md":
        rel = Path(str(rel) + ".gz")
        encoding = "gzip-mtime-zero"
        saved = gzip.compress(raw, compresslevel=9, mtime=0)
        assert gzip.decompress(saved) == raw
    dst = D / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        assert dst.read_bytes() == saved, str(dst)
    else:
        dst.write_bytes(saved)
    historical.append({"original": record(p), "preserved_path": str(rel),
                       "encoding": encoding, "stored_sha256": sha(saved)})

manifest_by_original = {
    item["original"]["path"]: item["preserved_path"] for item in historical
}
source_path = "INTERSPECIES_CURRENT_RIGIDITY_PROBE.md"
original = (S / source_path).read_bytes()
original_lines = original.splitlines(keepends=True)
assert len(original_lines) == 559


def original_segment(a, z, purpose, replacements=()):
    raw = b"".join(original_lines[a-1:z])
    out = raw
    edits = []
    for old, new, reason in replacements:
        old, new = old.encode(), new.encode()
        assert out.count(old) == 1, old
        out = out.replace(old, new)
        edits.append({"old": old.decode(), "new": new.decode(), "count": 1,
                      "reason": reason})
    return out, {"kind": "historical_lines", "source": manifest_by_original[str(S / source_path)],
                 "source_sha256": sha(original), "lines_inclusive": [a, z],
                 "raw_fragment_sha256": sha(raw), "output_fragment_sha256": sha(out),
                 "edits": edits, "purpose": purpose}


def fragment(name, purpose):
    raw = (D / "fragments" / name).read_bytes()
    return raw, {"kind": "new_fragment", "source": "fragments/" + name,
                 "source_sha256": sha(raw), "output_fragment_sha256": sha(raw),
                 "purpose": purpose}


def join(parts):
    all_bytes = b""
    records = []
    for raw, item in parts:
        item["output_byte_range_half_open"] = [len(all_bytes), len(all_bytes) + len(raw)]
        first = all_bytes.count(b"\n") + 1
        item["output_lines_inclusive"] = [first, first + len(raw.splitlines()) - 1]
        all_bytes += raw
        records.append(item)
    return all_bytes, records


prefix = "../.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/"
edits = [
    ("## 10. Exact finite controls and remaining obligation",
     "## 10. Exact finite controls and publication replay", "Evidence heading only."),
    ("The first formal run completed successfully",
     "The original author helper's first formal run completed successfully",
     "Disambiguate preserved historical run from publication replay."),
]
for tail in ["rigidity_controls.py", "controls.log", "execution.json", "receipt.json"]:
    old = "(interspecies_current_rigidity/" + tail + ")"
    edits.append((old, "(" + prefix + "interspecies_current_rigidity/" + tail + ")",
                  "Relocate evidence link for intended canonical docs path."))
note_parts = [
    fragment("note_front.txt", "Replace original lines 1-56: publication metadata, exact conditional scope, completed review status and historical provenance."),
    original_segment(57, 513, "Entire Sections 2-9; all I1-I24 hypotheses, proofs, domain/sign restrictions and adverse cases; byte-identical."),
    original_segment(514, 551, "Preserve original finite-control explanation and table, with only heading, historical-run precision and evidence-link changes.", edits),
    fragment("note_tail.txt", "Replace original lines 552-559 and append source-bound mathematical/Lean review and publication evidence status; no new mathematics."),
]
note, note_map = join(note_parts)
note_name = "FINAL_INTERSPECIES_CURRENT_RIGIDITY_NOTE.md"
(S / note_name).write_bytes(note)

helper_name = "interspecies_current_rigidity/rigidity_controls.py"
helper = (S / helper_name).read_bytes()
helper_lines = helper.splitlines(keepends=True)
body = b"".join(helper_lines[8:])
assert body.startswith(b"from fractions import Fraction as Q\n")
primary, primary_map = join([
    fragment("primary_front.txt", "Replace original lines 1-8 with scripts-style scope docstring, timeout/input declaration and explicit assertion-enabled guard."),
    (body, {"kind": "historical_lines", "source": manifest_by_original[str(S / helper_name)],
            "source_sha256": sha(helper), "lines_inclusive": [9, 209],
            "raw_fragment_sha256": sha(body), "output_fragment_sha256": sha(body),
            "edits": [], "purpose": "Complete original executable author-helper body, byte-identical."}),
    fragment("primary_tail.txt", "Add scoped thirteen-family TOTAL output after the complete original body."),
])
primary_name = "interspecies_collision_current_rigidity_2026_10_11.py"
(S / primary_name).write_bytes(primary)

composition = {
    "schema": "literal-source-publication-composition-v1",
    "claim_id": "interspecies_collision_current_rigidity_bounded_theorem_note_2026-10-11",
    "proposed_base": "a13caa4885f547c8d206265b031ba7649e539fd9",
    "historical_provenance_revision": "d009fb786d36a6cab4a7d410630b9382992faa08",
    "candidate_PR9476_role": "Motivation only; no mathematical dependency.",
    "canonical_evidence_root": ".claude/science/physics-loops/toe-interspecies-rigidity-20261011",
    "canonical_note": "docs/INTERSPECIES_COLLISION_CURRENT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "canonical_primary": "scripts/" + primary_name,
    "outputs": [
        {"name": note_name, "sha256": sha(note), "bytes": len(note), "logical_lines": len(note.splitlines()), "parts": note_map},
        {"name": primary_name, "sha256": sha(primary), "bytes": len(primary), "logical_lines": len(primary.splitlines()), "parts": primary_map},
    ],
    "historical_files": historical,
    "omitted_compiled_artifacts": omitted,
    "coverage": {
        "proof": "Original lines 57-513 copied without any byte change; all I1-I24 retained.",
        "historical_status": "Every original source and pending-status sentence preserved in exact decoded historical bytes; updated only in new presentation.",
        "physical_scope": "No mathematical dependency on candidate-law C1, no supplied physical law adopted.",
        "Lean_scope": "Same-author six finite-geometry declarations plus completed independent statement/evidence review; no new compiler execution."
    },
}
(D / "SOURCE_COMPOSITION.json").write_text(json.dumps(composition, indent=2) + "\n")
(D / "source_binding_verification.json").write_text(json.dumps({
    "receipt_records_verified": len(verified),
    "distinct_paths_verified": len({x["path"] for x in verified}),
    "records": verified, "protected_guards": [
        {"path": str(S / p), "sha256": h} for p, h in expected.items()
    ],
}, indent=2) + "\n")
print(json.dumps({
    "note": record(S / note_name), "primary": record(S / primary_name),
    "composition": record(D / "SOURCE_COMPOSITION.json"),
    "source_binding_records": len(verified), "historical_files": len(historical),
    "compiled_artifacts_omitted": len(omitted),
}, indent=2))
