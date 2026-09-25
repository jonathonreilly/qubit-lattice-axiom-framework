#!/usr/bin/env python3
"""Read-only source identity check; writes only inside this independent packet."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent / "campaign-working"
MAIN = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"
ROWS = (
    ("ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
     "af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718", MAIN,
     "Read completely in this PRE task; selected proof passages rechecked."),
    ("BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md",
     "f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9", MAIN,
     "Read completely in this PRE task; selected proof passages rechecked."),
    ("LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
     "c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b", MAIN,
     "Read completely in this PRE task; selected proof passages rechecked."),
    ("ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md",
     "4a484ec7403e3f2306454fe01cfb91cdf2a7f601d2e896aaef6307134deec28f",
     "c234d47c9d99b7fd5590957ec08d9083877d25e6",
     "Read completely in this PRE task; weighted section rechecked. Authorized reuse of PR9057."),
    ("ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
     "150bd5ba19195a55402d8f74112417f37e168bf50f50dc94d7dcab7d1d3a96a7",
     "e846ee9d4133f65d3778fa4dc36524a9ada6db6b",
     "Previously read completely during this same checker's publication comparison; identical bytes reused by explicit dispatch permission, with identity and relevant sections refreshed. No new complete reread claimed."),
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args], check=True, capture_output=True).stdout


def main():
    sources = []
    for name, expected, revision, read_scope in ROWS:
        relative = "docs/" + name
        frozen = ROOT / "sources" / name
        data = frozen.read_bytes()
        from_git = git("show", revision + ":" + relative)
        assert sha(data) == sha(from_git) == expected, name
        current = None
        if revision == MAIN:
            current_data = (REPO / relative).read_bytes()
            assert sha(current_data) == expected, name
            current = str(REPO / relative)
        sources.append({
            "snapshot": str(frozen.relative_to(ROOT)), "source_repository": str(REPO),
            "source_revision": revision, "source_path": relative,
            "current_file_checked": current, "sha256": expected, "bytes": len(data),
            "git_blob_oid": git("rev-parse", revision + ":" + relative).decode().strip(),
            "read_scope": read_scope,
            "authority": "Supplied conditional scientific premise/machinery; no retained or audit status imported",
        })

    instructions = []
    instruction_specs = (
        ("AGENTS_POINTER.md", "AGENTS.md", (REPO / "AGENTS.md").read_bytes(),
         "9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6"),
        ("SCIENCE_WORKFLOW.md", "docs/ai_methodology/SCIENCE_WORKFLOW.md",
         (REPO / "docs/ai_methodology/SCIENCE_WORKFLOW.md").read_bytes(),
         "d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4"),
        ("AGENTS_PLANNING.md", "origin/ai/execution:AGENTS.md", git("show", "origin/ai/execution:AGENTS.md"),
         "b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7"),
    )
    (ROOT / "instructions").mkdir(exist_ok=True)
    for name, origin, data, expected in instruction_specs:
        assert sha(data) == expected, name
        target = ROOT / "instructions" / name
        target.write_bytes(data)
        instructions.append({"snapshot": str(target.relative_to(ROOT)), "source": origin,
                             "sha256": expected, "bytes": len(data),
                             "read_scope": "Complete read; previously read same identities also reused"})

    pins = {
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "task": "Independent blind PRE: continuous cube N=4 no-first-birth fixed-time energetic coherence",
        "main_reference": MAIN,
        "planning_reference_at_pin": git("rev-parse", "origin/ai/execution").decode().strip(),
        "model_and_effort": "Inherited unchanged; no delegation",
        "scientific_sources": sources, "instruction_sources": instructions,
        "exclusions": ["continuous-coherence-personal", "averaged-variance-personal",
                       "integrated-variance-publication", "current campaign checkpoint"],
        "exclusions_read": False,
        "reuse_limits": "No author builder imported; unchanged large calculations not rerun; new control uses exact primitive words and an explicitly separate two-band toy",
        "authority_limit": "No publication, audit verdict, retained status, native selector or new axiom",
    }
    (ROOT / "SOURCE_PINS.json").write_text(json.dumps(pins, indent=2) + "\n")
    print(json.dumps(pins, indent=2))


if __name__ == "__main__":
    main()
