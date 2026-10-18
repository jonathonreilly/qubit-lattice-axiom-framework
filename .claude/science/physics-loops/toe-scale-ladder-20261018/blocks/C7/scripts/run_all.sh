#!/usr/bin/env bash
# Runs both C7 runners (light: one core) and sums their TOTAL lines.
set -u
D="$(cd "$(dirname "$0")/.." && pwd)"
if [ "${1:-}" != "--sum-only" ]; then  # --sum-only: re-sum existing logs without rerunning
  nice python3 "$D/scripts/c7_exact.py" > "$D/logs/c7_exact.log" 2>&1
  nice python3 "$D/scripts/c7_numeric.py" > "$D/logs/c7_numeric.log" 2>&1
fi
python3 - "$D" <<'PY' | tee "$D/logs/run_all.log"
import re, sys
D = sys.argv[1]; P = F = 0
for name in ("c7_exact", "c7_numeric"):
    last = open(f"{D}/logs/{name}.log").read().strip().splitlines()[-1]
    m = re.match(r"TOTAL: PASS=(\d+) FAIL=(\d+)", last)
    print(f"{name}: {last}")
    P += int(m.group(1)); F += int(m.group(2))
print(f"TOTAL: PASS={P} FAIL={F}")
PY
