#!/usr/bin/env python3
"""Y3 as registered needs an adversarial bond and colour at f <= 0.05; the k = 2 runs before this used one bond, at f >= 0.0508.
Sweep all 12 (mu, colour) at k = 1, amp 0.15 (f about 0.045), then k = 2 on the worst by b_1(V)/b_1(1). Each job starts only at 50 percent memory free or more."""
import glob, json, re, subprocess, time

LOG = "y_ex2_adv.log"

def mem():
    out = subprocess.run(["memory_pressure"], capture_output=True, text=True).stdout
    return int(re.search(r"percentage: (\d+)%", out).group(1))

def job(*args):
    for _ in range(40):
        m = mem()
        if m >= 50:
            with open(LOG, "a") as f:
                f.write(f"### start {time.strftime('%H:%MZ', time.gmtime())} mem_free={m}: y_ex2.py {' '.join(args)}\n")
                f.flush()
                r = subprocess.run(["nice", "-n", "10", "python3", "y_ex2.py", *args], stdout=f, stderr=subprocess.STDOUT)
                f.write(f"### end {time.strftime('%H:%MZ', time.gmtime())} exit={r.returncode}\n")
            return r.returncode
        time.sleep(60)
    with open(LOG, "a") as f:
        f.write(f"### SKIPPED, memory below 50 for 40 min: {args}\n")
    return None

for mu in range(4):
    for c in range(3):
        job("2", "3", "1", "const", "0.15", str(c), str(mu))
flat = json.load(open("y_2_3_1_flat_0.0_0_0.json"))["rows"][0]["b"]
rows = []
for fn in glob.glob("y_2_3_1_const_0.15_*_*.json"):
    r = json.load(open(fn))
    rows.append((r["rows"][0]["b"] / flat, r["args"][5], r["args"][6]))
rows.sort(reverse=True)
with open(LOG, "a") as f:
    f.write("SWEEP b_1(V)/b_1(1), colour, mu: " + str(rows) + "\n")
job("2", "3", "2", "const", "0.15", rows[0][1], rows[0][2])
open("y3.status", "w").write("done\n")
