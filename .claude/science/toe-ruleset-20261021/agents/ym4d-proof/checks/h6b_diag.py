#!/usr/bin/env python3
"""h6b: POST HOC diagnostic, written after h6 A2/A3 FAILED (smooth seed 2). Not a criterion change; the h6 FAIL stands.
Question: is the A2/A3 failure a near-cancellation artefact of the RELATIVE deviation |R_NA/R_lin - 1| (R_lin small), and
does the quantity (AE) actually uses, the additive error |log U_2(P) - dB_2(P)|_HS / sqrt(E), vanish linearly in t?
Reuses h6_msg_cone.py's functions (its module-level run is skipped by exec of the function section only).
"""
import os
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1")
import time, numpy as np
AUDIT_TIMEOUT_SEC = 900
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "h6_msg_cone.py")).read()
exec(src.split("# ================= Part A + B")[0])
T1 = time.time(); d, k = 4, 2; G, IDX = setup(d, k)
for sd in (1, 2, 3):
    rng = np.random.default_rng(sd); H = smooth_field(G[0].S, rng, d); res = {i: np.zeros((d,) + G[i].S + (3,)) for i in (1, 2)}
    rows = []
    for t in (1e-4, 3e-4, 1e-3, 2.5e-3, 1e-2):
        Us, Ws, Ms, As = build_chain(d, k, t * H, res, t, IDX, G); E, _ = energy_terms(Us, Ws, Ms, G, k, res, t)
        X = su2_log(topP(Us[k])); B = topdB(As[k]); Rna = 0.5 * np.sum(X ** 2) / E
        Elin = np.sum(dflux(As[0], G[0]) ** 2) * 0.5 / (2 * NC); Rlin = 0.5 * np.sum(B ** 2) / Elin
        Dabs = np.sqrt(0.5 * np.sum((X - B) ** 2) / E); rows.append((t, Rna, Rlin, abs(Rna / Rlin - 1), Dabs))
    sl = np.polyfit(np.log([r[0] for r in rows]), np.log([r[4] for r in rows]), 1)[0]
    print(f"smooth seed {sd}: additive-error slope {sl:.3f}")
    for (t, a, b, Dr, Da) in rows: print(f"  t={t:<7g} R_NA={a:.6f} R_lin={b:.6f} D_rel={Dr:.3e} |X-dB|_HS/sqrt(E)={Da:.3e} (/t = {Da / t:.3f})")
print(f"runtime {time.time() - T1:.1f} s")
