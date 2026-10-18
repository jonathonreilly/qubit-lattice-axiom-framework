# family of class-weighted relative-strain readings: omega = (axis, face, body) per segment, in relative-strain units
from common import *
def reading(k, om):
    R, D, ls = segment_readings(Dc, k); cls = np.array([0]*4 + [1]*12 + [2]*8)
    W = np.diag(np.sqrt(np.array(om)[cls]) / ls ** 2); return np.linalg.pinv(W @ D) @ (W @ R)
dirs = [np.array(d, float) / np.linalg.norm(d) for d in ([0, 1, 0, 0], [0.3, -0.5, 0.6, 0.55], [1, 1, 1, 1], [0, 1, 0, 1])]
cache = {}
def preading(om, s=0.004):
    out = []
    for d in dirs:
        k = s * d
        if (tuple(k)) not in cache: cache[tuple(k)] = partners(k)
        P2 = cache[tuple(k)]; out.append(np.linalg.norm(reading(k, om) @ P2, axis=0).max() / s)
    return max(out)
print("relative strain uniform (1,1,1): partner reading / |k| =", round(preading((1, 1, 1)), 4))
print("uniform in delta l^2   (1,4,16):", round(preading((1, 4, 16)), 4))
for wf in (0.25, 0.5, 2.0, 4.0):
    print(f"axis = body = 1, face {wf}: partner reading / |k| = {preading((1, wf, 1)):.4f}")
for wb in (0.5, 2.0):
    print(f"axis = face = 1, body {wb}: partner reading / |k| = {preading((1, 1, wb)):.4f}")
