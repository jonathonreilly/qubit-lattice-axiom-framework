#!/bin/sh
# Run from the ym4d-proof folder. A rejected preflight never starts numerics.
uptime > checks/hrp_preflight.txt
memory_pressure >> checks/hrp_preflight.txt
python3 - <<'PY'
import os,re
from pathlib import Path
s=Path('checks/hrp_preflight.txt').read_text()
m=re.search(r'System-wide memory free percentage:\s*(\d+)%',s)
load=os.getloadavg()[0]
print('Preflight: load=',load,'free_memory_percent=',m.group(1) if m else 'unavailable')
if not m or int(m.group(1)) < 30 or load >= 8:
    raise SystemExit(4)
PY
preflight_status=$?
if [ "$preflight_status" -ne 0 ]; then
    exit "$preflight_status"
fi
until mkdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-hrp/.locks_hrp_numeric 2>/dev/null; do sleep 20; done
# Recheck after any lock wait. The only cleanup path is the single rmdir below.
memory_pressure >> checks/hrp_preflight.txt
python3 - <<'PY'
import os,re
from pathlib import Path
s=Path('checks/hrp_preflight.txt').read_text()
m=re.findall(r'System-wide memory free percentage:\s*(\d+)%',s)
if not m or int(m[-1]) < 30 or os.getloadavg()[0] >= 8:
    raise SystemExit(4)
PY
numeric_status=$?
if [ "$numeric_status" -eq 0 ]; then
    /usr/bin/time -p env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 10 /bin/sh -c 'exec python3 -u checks/hrp_exact.py 2> checks/hrp_err.txt' > checks/hrp_out.txt 2> checks/hrp_time.txt
    numeric_status=$?
fi
rmdir /Users/jonreilly/Projects/Physics/.claude/worktrees/ym4d-hrp/.locks_hrp_numeric
cleanup_status=$?
printf 'numeric_exit=%s cleanup_exit=%s\n' "$numeric_status" "$cleanup_status" >> checks/hrp_time.txt
if [ "$cleanup_status" -ne 0 ]; then
    exit "$cleanup_status"
fi
exit "$numeric_status"
