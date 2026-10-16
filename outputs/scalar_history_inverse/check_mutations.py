#!/usr/bin/env python3
"""Challenge exact control families in isolated temporary copies."""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
FILES = (
    "docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md",
    "scripts/scalar_history_inverse.py",
    "scripts/scalar_history_inverse_math.py",
)
MUTATIONS = (
    ("particle action source sign", "- N*rho0*A(ph)", "+ N*rho0*A(ph)",
     "scalar variation fixes density and coupling normalization"),
    ("dust exchange sign in velocity flow", "-al*d*x-3*h*x*x", "+al*d*x-3*h*x*x",
     "dust conservation solves first-order velocity equation"),
    ("response curvature in degree-six constraint", "+6*hd+4*mu", "+6*hd+3*mu",
     "expanded curvature polynomial agrees with differentiated KG"),
    ("forward potential slope", ")*s.exp(-2*s.Symbol(\"z\")/c)", ")*s.exp(-3*s.Symbol(\"z\")/c)",
     "forward power-law scalar equation"),
    ("density derivative in polynomial constant", "v-(3*d*h+e)**2)", "v-(3*d*h+3*e)**2)",
     "unique-fixture curvature factorization"),
    ("uncoupled scaling curvature", "8/t**4,0,0,2/t**2))", "8/t**4,0,0,3/t**2))",
     "uncoupled dust-era curvature polynomial is identically zero"),
    ("registered density curvature source", "-3*hh*s.diff(kk,t)/(2*kk)-3*s.diff(hh,t)+3*hh*rr*qq/kk)", "-3*hh*s.diff(kk,t)/(2*kk)-3*s.diff(hh,t)+2*hh*rr*qq/kk)",
     "registered-density curvature identity"),
    ("field reflection incorrectly negates potential", "V_ref=V_old.subs(z,-psi)", "V_ref=-V_old.subs(z,-psi)",
     "field reflection preserves potential along reflected history"),
    ("exceptional continuum curvature", "mu:(9*h**2-6*j)/4", "mu:(9*h**2-6*j)/3",
     "exceptional coefficients all vanish"),
    ("near-degenerate family mismatch", "pp=(2+eps)/3", "pp=(3+eps)/3",
     "near-degenerate family preserves exact velocity"),
)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    original = {name: (ROOT/name).read_bytes() for name in FILES}
    text = original[FILES[2]].decode()
    records = []
    for label, old, new, target in MUTATIONS:
        count = text.count(old)
        if count != 1:
            raise RuntimeError(f"{label}: expected one mutation site, found {count}")
        mutated = text.replace(old, new)
        with tempfile.TemporaryDirectory(prefix="scalar-history-mutation-") as directory:
            copy = Path(directory)
            for name, data in original.items():
                destination = copy/name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(mutated.encode() if name == FILES[2] else data)
            environment = os.environ.copy()
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            run = subprocess.run([sys.executable, "-B", FILES[1]], cwd=copy,
                                 env=environment, capture_output=True, text=True, timeout=120)
            result_path = copy/"outputs/scalar_history_inverse/result.json"
            result = json.loads(result_path.read_text()) if result_path.exists() else None
            failed = [row["name"] for row in result["checks"] if not row["pass"]] if result else []
            detected = run.returncode != 0 and target in failed
            records.append({
                "label": label, "original": old, "replacement": new,
                "target": target, "detected": detected, "exit_code": run.returncode,
                "failed_assertions": failed, "stderr": run.stderr,
                "mutated_helper_sha256": sha(mutated.encode()),
                "result": result,
            })
            print(("PASS" if detected else "FAIL")+": "+label)
    result = {"schema": "scalar-history-mutations-v1",
              "source_sha256": {name: sha(data) for name, data in original.items()},
              "mutation_runner_sha256": sha(Path(__file__).read_bytes()),
              "method": "Isolated source mutation; a crash without the targeted failed assertion does not count",
              "passed": sum(row["detected"] for row in records),
              "failed": sum(not row["detected"] for row in records), "mutations": records}
    (ROOT/"outputs/scalar_history_inverse/mutations.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    return int(result["failed"] != 0)


if __name__ == "__main__":
    raise SystemExit(main())
