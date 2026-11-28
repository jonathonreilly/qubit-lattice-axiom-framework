# GUIDE: shape dependence (c, d up to 16 b) of sup over m of R1, R2 at a = b/2.
import sys, numpy as np
sys.argv = [sys.argv[0], "none"]
exec(open("guide_scan.py").read().split("models = sys.argv")[0])
for model in ["N", "P", "M", "D"]:
    ms = [0.0] if model == "M" else list(np.logspace(-4, 0, 13))
    for b in [12, 16]:
        for (c, d) in [(b, b), (b, 4*b), (b, 16*b), (4*b, 4*b), (8*b, 8*b)]:
            b1 = (0, None); b2 = (0, None)
            for m in ms:
                for a in range(max(3, b//4), b//2 + 1):
                    (aa, R1, R2, R2p, g, p, de), = analyse(model, m, b, c, d, [a])
                    if R1 > b1[0]: b1 = (R1, (round(m,5), a))
                    if R2 > b2[0]: b2 = (R2, (round(m,5), a))
            print(f"{model} b={b} c={c} d={d}: sup R1={b1[0]:.4f} at {b1[1]}; sup R2={b2[0]:.5f} at {b2[1]}", flush=True)
