"""Execution/mutation receipt driver; run under preflight and a numeric lease."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "scripts"))
from runner_cache import execute_and_write_cache, cache_identity_status

PRIMARY = "scripts/gb1_cf_two_plaquette_s1_2026_11_07.py"
CHECKER = "scripts/gb1_cf_two_plaquette_haar_check_2026_11_07.py"
source = (ROOT / PRIMARY).read_text()
before = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
          for p in (PRIMARY, CHECKER)}
for runner, timeout in ((PRIMARY, 80), (CHECKER, 85)):
    result, cache = execute_and_write_cache(runner, timeout_sec=timeout)
    row = {"runner": runner, "status": result.get("status"),
           "exit_code": result.get("exit_code"), "cache": str(cache),
           "cache_identity_status": cache_identity_status(runner)}
    print(json.dumps(row), flush=True)
    if result.get("status") != "ok" or result.get("exit_code") != 0 or cache is None:
        raise RuntimeError("canonical execution failed; inspect full cache")

mutations = (
    ("local_coordinate_normalization", "p[mu][mu][0] = p[mu][0][mu] = G(F(1, 2))",
     "p[mu][mu][0] = p[mu][0][mu] = G(F(1, 1))"),
    ("incoming_outgoing_Gauss_assignment", "matrix = minus[a]", "matrix = plus[a]"),
    ("magnetic_trace_plus_adjoint", "apply_terms(terms[name], v, F(2)) for v in vectors",
     "apply_terms(terms[name], v, F(1)) for v in vectors"),
    ("geometric_link_inversions", "if old in (0, 1, 2, 3) and state[old] in (1, 2, 3):",
     "if old in () and state[old] in (1, 2, 3):"),
    ("Strang_half_step", "ea_half = exp_series(a, order, -I / 2)",
     "ea_half = exp_series(a, order, -I)"),
    ("logical_magnetic_encoding", "mmul(xl, madd(mscale(3, ident(4)), zr))",
     "mmul(xl, madd(mscale(2, ident(4)), zr))"),
    ("electric_normalization_and_encoding",
     "F(3, 4) * sum(mu != 0 for mu in state)",
     "F(1, 1) * sum(mu != 0 for mu in state)"),
)
env = dict(os.environ, PYTHONPATH=str(ROOT / "scripts"))
for name, old, new in mutations:
    if source.count(old) != 1:
        raise RuntimeError(f"ambiguous mutation anchor: {name}")
    with tempfile.TemporaryDirectory(prefix="gb1cf-mutation-") as folder:
        path = Path(folder) / "mutant.py"
        path.write_text(source.replace(old, new))
        result = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT,
                                env=env, text=True, capture_output=True, timeout=80)
    rejected = result.returncode == 1 and "AssertionError" in result.stderr
    print(json.dumps({"mutation": name, "old": old, "new": new,
                      "rejected_by_assertion": rejected, "exit_code": result.returncode,
                      "stdout": result.stdout, "stderr": result.stderr}), flush=True)
    if not rejected:
        raise RuntimeError(f"mutation not rejected by a scientific check: {name}")
after = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in before}
if after != before:
    raise RuntimeError("production source changed during integration checks")
print(json.dumps({"production_sources_unchanged": before,
                  "scratch_mutations_rejected": len(mutations)}), flush=True)
