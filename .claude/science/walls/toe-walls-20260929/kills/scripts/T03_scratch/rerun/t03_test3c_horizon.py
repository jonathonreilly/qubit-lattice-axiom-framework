"""T03 Test 3c: permanence horizon versus reservoir length (pre-registered in the report's test section before the run):
Prediction: the time at which P(ever fell) first exceeds 5% scales linearly with the chain length n (light-crossing recurrence),
t_5%(n) / n in [0.8, 1.6] for n = 100, 200, 400 (the excitation must reach the far end and come back: 2n / v_max, v_max = 2 => n).
FAIL: t_5%/n varies by more than a factor 1.5 across n, or P(ever fell) > 5% before t = 0.5 n.
"""
import sys, io, contextlib
import numpy as np
import t03_test3_permanence as T

res = {}
for n in (100, 200, 400):
    psi0 = np.zeros(n + 1); psi0[0] = 1.0
    cps = list(range(10, int(1.8 * n) + 1, 10))
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rec, caps = T.bell_chain(n, 0.2, psi0, 1.8 * n, 0.05, 2000, f"n={n}", cps)
    t5 = next((r[0] for r in rec if r[2] > 0.05), None)
    early = max(r[2] for r in rec if r[0] <= 0.5 * n)
    res[n] = (t5, early, rec[-1][2])
    print(f"n = {n:4d}:  t_5% = {t5}   t_5%/n = {t5/n:.2f}   max P(fell) before 0.5 n = {early:.4f}   P(fell) at 1.8 n = {rec[-1][2]:.3f}", flush=True)
ratios = [res[n][0] / n for n in res]
ok1 = all(0.8 <= r <= 1.6 for r in ratios)
ok2 = max(ratios) / min(ratios) <= 1.5
ok3 = all(res[n][1] <= 0.05 for n in res)
print("[%s] t_5%%/n in [0.8, 1.6] for all n: %s" % ("PASS" if ok1 else "FAIL", ["%.2f" % r for r in ratios]))
print("[%s] t_5%%/n varies by less than 1.5x" % ("PASS" if ok2 else "FAIL"))
print("[%s] no early falls before 0.5 n" % ("PASS" if ok3 else "FAIL"))
print("TOTAL: PASS=%d FAIL=%d" % (ok1 + ok2 + ok3, 3 - ok1 - ok2 - ok3))
