#!/usr/bin/env python3
"""Actual isolated source mutations; author validation, not a scientific helper.

Run only after the frozen primary. Each trial copies the primary and literal
inputs to a fresh temporary tree. It preserves stdout/stderr, exact mutant
diffs/hashes and result JSON here; it never edits the canonical runner or cache.
"""
from pathlib import Path
import ast
import difflib
import hashlib
import json
import os
import resource
import subprocess
import tempfile
import time

AUDIT_TIMEOUT_SEC = 60
PACK = Path(__file__).resolve().parent
ROOT = PACK.parents[3]
RUNNER = "scripts/uniform_autonomous_original_record_resource_density_2026_09_30.py"
source = (ROOT/RUNNER).read_text()
tree = ast.parse(source)
inputs = next(ast.literal_eval(n.value) for n in tree.body
              if isinstance(n, ast.Assign) and
              any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS" for t in n.targets))
CASES = [
    ("birth_orientation", "BIRTH_SHIFT = 1", "BIRTH_SHIFT = -1", "original_words_and_gain"),
    ("coherent_normalization", "COHERENT_FACTOR = 1.0", "COHERENT_FACTOR = 2**-0.5", "original_coherent_copy_and_Julia"),
    ("copy_hidden_sign", "COPY_SIGN = False", "COPY_SIGN = True", "original_coherent_copy_and_Julia"),
    ("internal_field_clip", "COMPRESS_INTERNAL = False", "COMPRESS_INTERNAL = True", "whole_magnetic_compression"),
    ("miss_overlap_edges", "COLOR_RADIUS = 2", "COLOR_RADIUS = 1", "local_geometry_and_colors"),
    ("word_reset", "RESET_ON_NOEVENT = False", "RESET_ON_NOEVENT = True", "per_center_append_near_identity"),
    ("short_clock_band", "CLOCK_BAND_SLACK = 0", "CLOCK_BAND_SLACK = -1", "finite_clock_prefix_and_Toeplitz"),
    ("cyclic_clock_wrap", "WRAP_CLOCK = False", "WRAP_CLOCK = True", "finite_clock_prefix_and_Toeplitz"),
    ("omit_interaction_energy", "INCLUDE_INTERACTION = True", "INCLUDE_INTERACTION = False", "positive_controller_and_postread_ledger"),
]
env = dict(os.environ, OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
           MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
rows = []
for name, old, new, expected in CASES:
    assert source.count(old) == 1
    mutant = source.replace(old, new)
    trial = PACK/"mutations"/name
    trial.mkdir(parents=True, exist_ok=True)
    (trial/"mutation.diff").write_text("".join(difflib.unified_diff(
        source.splitlines(keepends=True), mutant.splitlines(keepends=True),
        fromfile=RUNNER, tofile=RUNNER)))
    with tempfile.TemporaryDirectory(prefix="toe-density-mutation-") as tmp:
        temp = Path(tmp)
        for p in inputs:
            target = temp/p; target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT/p).read_bytes())
        target = temp/RUNNER; target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(mutant)
        before = resource.getrusage(resource.RUSAGE_CHILDREN); start=time.monotonic()
        result = subprocess.run(["python3",str(target)],cwd=temp,env=env,
                                capture_output=True,text=True,timeout=60)
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        (trial/"stdout.txt").write_text(result.stdout)
        (trial/"stderr.txt").write_text(result.stderr)
        output = temp/"outputs/uniform_autonomous_original_record_resource_density_2026_09_30.json"
        data=json.loads(output.read_text()) if output.exists() else {}
        (trial/"output.json").write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
        caught = result.returncode != 0 and expected in data.get("failures",[])
        rows.append({"name":name,"expected_family":expected,"detected":caught,
                     "exit_code":result.returncode,"actual_failures":data.get("failures"),
                     "mutant_sha256":hashlib.sha256(mutant.encode()).hexdigest(),
                     "wall_seconds":time.monotonic()-start,
                     "cpu_seconds":after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                     "max_child_rss_so_far_MiB":after.ru_maxrss/1024/1024})
        print(("PASS " if caught else "FAIL ")+name)
(PACK/"MUTATION_RESULTS.json").write_text(json.dumps(rows,indent=2,sort_keys=True)+"\n")
passed=sum(r["detected"] for r in rows)
print(f"TOTAL: PASS={passed} FAIL={len(rows)-passed}")
raise SystemExit(passed != len(rows))
