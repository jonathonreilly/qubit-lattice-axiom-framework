"""R3 finite instance: which planar rotations preserve the p-norm of real 2-vectors? (Lamperti 1958 / Aaronson 2004 instance)
Amplitude-vector reading: probabilities |a_i|^p / sum |a_j|^p need a norm-preserving linear continuous evolution."""
import numpy as np
th = np.deg2rad(np.arange(0, 360, 0.5))
rng = np.random.default_rng(1)
V = rng.normal(size=(2, 400))
for p in (1.0, 1.5, 2.0, 3.0, 4.0):
    dev = []
    for t in th:
        Rm = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
        W = Rm @ V
        dev.append(np.max(np.abs((np.abs(W) ** p).sum(0) ** (1 / p) / (np.abs(V) ** p).sum(0) ** (1 / p) - 1)))
    dev = np.array(dev)
    good = np.deg2rad(0.5) * 0 + np.where(dev < 1e-9)[0]
    print(f"p={p}: rotation angles (deg, step 0.5) preserving the p-norm: {sorted((good*0.5).tolist())}")
