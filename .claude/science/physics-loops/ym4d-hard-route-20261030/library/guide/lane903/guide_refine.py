# GUIDE: refine sup of R2 = a delta_e/g at a = b/2 over m and shape, larger b.
import sys, numpy as np
sys.argv = [sys.argv[0], "none"]
exec(open("guide_scan.py").read().split("models = sys.argv")[0])
for model in ["N", "M", "P", "D"]:
    print("model", model)
    ms = [0.0] if model == "M" else list(np.logspace(-4, 0, 17))
    for b in [16, 32, 64, 96]:
        for (c, d) in [(b, b), (b, 2 * b), (2 * b, 2 * b)]:
            if c * d > 20000: continue
            best = (0, None)
            for m in ms:
                for a in sorted(set([b // 2, b // 2 - 1, max(3, b // 3)])):
                    (aa, R1, R2, R2p, g, p, de), = analyse(model, m, b, c, d, [a])
                    if R2 > best[0]: best = (R2, (round(m, 5), a, round(R1, 4)))
            print(f"  b={b} c={c} d={d}: max R2={best[0]:.5f} at (m,a,R1)={best[1]}", flush=True)
