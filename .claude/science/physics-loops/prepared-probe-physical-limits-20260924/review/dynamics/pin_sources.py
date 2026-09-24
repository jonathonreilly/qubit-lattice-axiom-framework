"""Copy only the expressly authorized source bytes and verify their identities."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
REPO = BASE / "campaign-working"
REV = "0e6ad8285096ed668816f18caaa6fbbfbd9c50e8"
MAIN = {
    "AGENTS.md": "9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6",
    "docs/ai_methodology/SCIENCE_WORKFLOW.md": "d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4",
    "docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md": "9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455",
    "docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md": "b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0",
    "docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md": "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258",
    "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md": "c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b",
    "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md": "7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a",
    "docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md": "651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf",
}
EXTERNAL = {
    "prepared-matter-probe-personal/PREPARED_MATTER_INTERFERENCE_PROBE_ROOT.md": "ab3c1883b032e571efdeb52330d7665c262f70e3f303b3236f32f89accbcd7bf",
    "unrestricted-record-count-independent/PRE.md": "1fd58a66171c23568841d2527a2091f3992e584cbad970bdb8979a38e4c68e7e",
    "unrestricted-record-count-independent/PRE_SEAL.json": "b6e0c33fe1286a876f1230759cb62769d57475d76c2ea1a6aae633064e2ba9d0",
}


def main():
    records = []
    for relative, expected in MAIN.items():
        data = subprocess.check_output(["git", "-C", str(REPO), "show", f"{REV}:{relative}"])
        digest = sha256(data).hexdigest()
        assert digest == expected, (relative, digest, expected)
        target = HERE / "sources/main" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        records.append({"copy": str(target.relative_to(HERE)), "origin_repository": str(REPO),
                        "revision": REV, "git_path": relative,
                        "bytes": len(data), "sha256": digest})
    for relative, expected in EXTERNAL.items():
        origin = BASE / relative
        data = origin.read_bytes()
        digest = sha256(data).hexdigest()
        assert digest == expected, (relative, digest, expected)
        target = HERE / "sources/external" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        records.append({"copy": str(target.relative_to(HERE)), "origin": str(origin),
                        "bytes": len(data), "sha256": digest})
    pins = {"scope": "Authorized source snapshots only. Root22 is an admitted provisional preparation/effect; own20 PRE is reused only for its fixed-graph global Duhamel and count arguments. Applicable instructions were previously read at these unchanged bytes. No new dynamics/output candidate or other active checker packet was read.",
            "records": records,
            "pin_script_sha256": sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE / "SOURCE_PINS.json").write_text(json.dumps(pins, indent=2) + "\n")
    print(json.dumps(pins, indent=2))


if __name__ == "__main__":
    main()
