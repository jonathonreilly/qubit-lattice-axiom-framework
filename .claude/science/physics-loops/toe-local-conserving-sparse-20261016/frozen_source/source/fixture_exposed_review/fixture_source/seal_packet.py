#!/usr/bin/env python3
"""Deterministic source/receipt verification and final packet inventory only."""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
N = ROOT.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


parents = [
    (N / "local_conserving_sparse_compiler_candidate/DERIVATION.md",
     "6b1e1ecd6afcf53dd05411493c18ceb9db258fcc279dc3c24072a516a5a76c3b",
     "sparse_DERIVATION.md", "Complete source refreshed/read in this task; authored previously."),
    (N / "local_conserving_sparse_compiler_candidate/FREEZE.json",
     "1fd6b69f78b2b9e270e1dc4655ef9c6da9c6d4290a3e2867ebfac42fc23ac0c9",
     "sparse_FREEZE.json", "Identity refreshed; existing freeze was not changed."),
    (N / "local_conserving_control_candidate/DERIVATION.md",
     "c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60",
     "control_DERIVATION.md", "Sections 4-6 relevant generators, phases, timing and work reread; full source authored/read previously."),
]
(ROOT / "sources").mkdir(exist_ok=True)
manifest = []
for path, expected, name, coverage in parents:
    actual = sha(path)
    assert actual == expected, (str(path), actual, expected)
    copied = ROOT / "sources" / name
    shutil.copyfile(path, copied)
    assert sha(copied) == actual
    manifest.append({"original_path": str(path), "packet_copy": str(copied.relative_to(ROOT)),
                     "bytes": path.stat().st_size, "sha256": actual, "coverage": coverage})

run = ROOT / "runs/attempt_01"
receipt = json.loads((run / "EXECUTION.json").read_text())
assert receipt["returncode"] == 0
for key in ("source", "launcher", "stdout", "stderr"):
    entry = receipt[key]
    path = Path(entry["path"])
    assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
assert sha(ROOT / "emitted_word_fixture.py") == sha(run / "source_at_launch.py")
assert sha(ROOT / "run_fixture.py") == sha(run / "launcher_at_launch.py")
assert (run / "stderr.txt").stat().st_size == 0
result = json.loads((run / "output/RESULT.json").read_text())
for key, info in result["words"].items():
    path = run / "output" / info["path"]
    assert path.stat().st_size == info["bytes"] and sha(path) == info["sha256"]
    if key != "segments":
        word = json.loads(path.read_text())
        assert dict(collections.Counter(g["kind"] for g in word)) == result["counts"]["by_kind"][key]
        if "routed" in key:
            assert all(g["kind"] == "Z" or abs(g["sites"][0] - g["sites"][1]) == 1 for g in word)

save(ROOT / "SOURCE_MANIFEST.json", {
    "scope": "One exposed author-produced numerical emitted-word fixture; no general certification.",
    "parents": manifest,
    "primary_literature": {
        "title": "Bai and Marvian, Synthesis of Energy-Conserving Quantum Circuits with XY interaction",
        "url": "https://arxiv.org/pdf/2309.11051v3",
        "use": "Indirect mathematical parent via pinned source; relevant arguments read in the preceding author tasks, not newly reread/downloaded here.",
        "previously_pinned_pdf_sha256": "add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8"
    },
    "execution": "runs/attempt_01/EXECUTION.json",
    "execution_count": 1,
    "scientific_source_sha256": receipt["source"]["sha256"],
    "scientific_launcher_sha256": receipt["launcher"]["sha256"],
    "review_exposure": "Same author and inherited model/reasoning; root independent review directories unread; sparse source not promoted.",
    "mutations_outside_new_packet": [],
    "editable_prompt_files_changed": [],
})

files = []
for path in sorted(ROOT.rglob("*")):
    if path.is_file() and path.name != "FREEZE.json":
        files.append({"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size,
                      "sha256": sha(path)})
freeze = {
    "frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "Frozen numerical evidence only; parent source unchanged and sparse acceptance pending.",
    "members": files,
}
save(ROOT / "FREEZE.json", freeze)
for entry in files:
    path = ROOT / entry["path"]
    assert path.stat().st_size == entry["bytes"] and sha(path) == entry["sha256"]
print(json.dumps({"member_count": len(files), "FREEZE_sha256": sha(ROOT / "FREEZE.json"),
                  "REVIEW_sha256": sha(ROOT / "REVIEW.md"),
                  "source_manifest_sha256": sha(ROOT / "SOURCE_MANIFEST.json"),
                  "frozen_utc": freeze["frozen_utc"]}, indent=2))
