#!/usr/bin/env python3
"""Mechanical own-evidence binding and complete serialized-path correspondence."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time

here = Path(__file__).resolve().parent
started = datetime.now(timezone.utc).isoformat()
timer = time.perf_counter()
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
read = lambda name: json.loads((here / name).read_text())
execution = read("EXECUTION.json")
assert execution["runner_sha256"] == sha(here / "run_controls.py")
assert execution["source_manifest_sha256"] == sha(here / "SOURCE_PINS.json")
for run in execution["runs"]:
    assert run["exit_code"] == 0
    assert run["script_sha256"] == sha(here / run["script"])
    for key in ("stdout", "stderr"):
        assert run[key + "_sha256"] == sha(here / run[key])
    assert (here / run["stderr"]).read_bytes() == b""
sources = read("SOURCE_VERIFICATION.json")
source_lines = [json.loads(line) for line in (here / "source_verification.stdout.txt").read_text().splitlines()]
assert source_lines == sources["sources"]
result = read("CONTROL_RESULTS.json")
lines = [json.loads(line) for line in (here / "readout_control.stdout.txt").read_text().splitlines()]
assert lines[:-1] == result["checks"]
assert lines[-1] == {"completed": True, "check_count": result["check_count"]}
assert result["all_checks_satisfied"] and result["check_count"] == 40
assert all(row["satisfied"] for row in result["checks"])


def field(items):
    return tuple(sorted(((tuple(item["start"]), item["axis"]), item["value"]) for item in items))


def difference(ket, bra):
    ans = dict(ket)
    for edge, value in bra:
        ans[edge] = ans.get(edge, 0) - value
    return tuple(sorted((edge, value) for edge, value in ans.items() if value))


def matter(items):
    return tuple(sorted((tuple(item["vertex"]), item["initial"], item["final"]) for item in items))


correspondence = []
certificates = read("PATH_CERTIFICATES.json")
assert len(certificates) == len(result["paths"]) == 9
for cert, expected in zip(certificates, result["paths"]):
    assert (cert["first"], cert["second"]) == (expected["first"], expected["second"])
    assert len(cert["paths"]) == expected["path_count"]
    for dephase in (False, True):
        groups = defaultdict(list)
        for path in cert["paths"]:
            final = matter(path["final_matter_changes"])
            key = (final, matter(path["intermediate_matter_changes"])) if dephase else final
            groups[key].append(field(path["electric_translation"]))
        poly = Counter()
        for members in groups.values():
            for bra in members:
                for ket in members:
                    poly[difference(ket, bra)] += 1
        key = "dephased_effect" if dephase else "effect"
        expected_poly = Counter({field(term["translation"]): term["coefficient"]
                                 for term in expected[key]})
        assert poly == expected_poly
    correspondence.append({"first": cert["first"], "second": cert["second"],
                           "paths": len(cert["paths"]),
                           "both_serialized_effects_match": True})

out = {"scope": __doc__, "started_utc": started,
       "elapsed_seconds": time.perf_counter() - timer,
       "command": [sys.executable, str(Path(__file__).resolve())],
       "script_sha256": sha(Path(__file__).resolve()),
       "execution_hashes_valid": True, "source_stdout_result_equal": True,
       "scientific_stdout_result_equal": True,
       "all_serialized_paths_parsed": sum(row["paths"] for row in correspondence),
       "case_correspondence": correspondence,
       "evidence_sha256": {name: sha(here / name) for name in
                           ("EXECUTION.json", "SOURCE_PINS.json", "SOURCE_VERIFICATION.json",
                            "CONTROL_RESULTS.json", "PATH_CERTIFICATES.json")}}
(here / "EVIDENCE_VERIFICATION.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, sort_keys=True), flush=True)
