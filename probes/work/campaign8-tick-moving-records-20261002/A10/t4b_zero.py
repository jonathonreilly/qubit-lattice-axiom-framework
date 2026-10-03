"""t4b: where is quasienergy 0 (the K* value) or pi reached?  Strang-signed cycle, theta scan."""
import numpy as np
from vcyc import layers_U, strang9, plain6

pi = np.pi
Ks = np.array([pi, pi, pi])
N = 24
g = np.arange(N) * 2 * pi / N - pi
KK = np.array(np.meshgrid(g, g, g, indexing="ij")).reshape(3, -1).T
dist = np.linalg.norm(((KK - Ks) + pi) % (2 * pi) - pi, axis=1)

def scan(lay, signed, th):
    U0 = layers_U(Ks[None], lay, signed)[0]
    ref = np.exp(1j * np.angle(np.linalg.eigvals(U0)[0]))
    ph = np.angle(np.linalg.eigvals(layers_U(KK, lay, signed)) * np.conj(ref))
    f0 = np.abs(ph).min(1)                 # distance of nearest band to quasienergy 0
    fpi = (pi - np.abs(ph)).min(1)         # distance to quasienergy pi
    far = dist > 0.6
    # band-width of the upper group relative to the cone: max |phase|
    return f0[far].min(), fpi.min(), np.abs(ph).max()

print("theta   | min dist to qe 0 (|K-K*|>0.6) | min dist to qe pi | max |qe|   [Strang-signed]")
for th in np.linspace(0.1, 1.5, 15):
    a, b, c = scan(strang9(th), True, th)
    print(f"{th:.3f}  | {a:.4f} | {b:.4f} | {c:.4f}   (2 sqrt3 th = {2*np.sqrt(3)*th:.3f})")
print("theta   | same, plain-6")
for th in np.linspace(0.1, 1.5, 8):
    a, b, c = scan(plain6(th), False, th)
    print(f"{th:.3f}  | {a:.4f} | {b:.4f} | {c:.4f}")
