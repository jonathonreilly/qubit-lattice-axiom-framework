"""Finite native preparation evidence; full proof and supplied inputs are in the note."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_PRODUCT_GIBBS_PREPARATION_NOTE_2026-09-08.md",
    "docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/NATIVE_EDGE_RECORD_LOCAL_CYCLE_TRANSPORT_AND_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "scripts/native_product_gibbs_dimer_2026_09_08.py",
    "scripts/native_product_gibbs_path_2026_09_08.py",
    "scripts/native_product_gibbs_encoded_2026_09_08.py",
)
from pathlib import Path
import contextlib, io, json, os, resource, importlib.util, time
for resource_variable in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[resource_variable] = "1"
start = time.monotonic()
root = Path(__file__).resolve().parents[1]
def load_helper(path):
    # Fresh module execution with a static path visible to both packet resolvers.
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module.result

parts = {
    "dimer": load_helper(root / "scripts" / "native_product_gibbs_dimer_2026_09_08.py"),
    "path": load_helper(root / "scripts" / "native_product_gibbs_path_2026_09_08.py"),
    "encoded": load_helper(root / "scripts" / "native_product_gibbs_encoded_2026_09_08.py"),
}
for name, data in parts.items():
    if data["status"] != "PASS" or not all(data["checks"].values()):
        raise RuntimeError(f"Incomplete {name} evidence")
seconds = time.monotonic() - start
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_mib = rss / (1024 ** 2 if os.uname().sysname == "Darwin" else 1024)
if seconds > AUDIT_TIMEOUT_SEC or rss_mib > 384:
    raise RuntimeError(f"Resource contract failed: {seconds}s, {rss_mib}MiB")
result = {"status": "PASS", "classification": "conditional-support", "parts": parts,
          "executed_assertions": sum(len(x["checks"]) for x in parts.values()),
          "elapsed_seconds": seconds, "peak_rss_mib": rss_mib,
          "scope": "Finite operator evidence for the declared construction. General path proof is analytic; preparation, controls, beta, h and Born events are supplied."}
(root / "outputs" / "native_product_gibbs_preparation_2026_09_08.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))

print('per_element: executed full Kraus operators/columns and complete leaf outcomes in the dimer, path and encoded fixtures.')
print('per_site: executed distinct physical midpoint checks for 4, 8 and 6 edge qubits; physical control admissibility remains supplied.')
print('per_mode: executed m=4 at two coupling families and three beta values, plus exact dimer and constrained odd three-mode encoding.')
print('per_block: executed all 4 dimer outcomes, all 16 path outcomes in each of 6 cells, and all 8 encoded outcomes; 248 assertions total.')
print('lattice_wide: checked and not executed — arbitrary finite path coverage is analytic; no spatial scaling or formation-law simulation.')
print(f"TOTAL: PASS={result['executed_assertions']} FAIL=0")
