import numpy as np, sys
sys.path.insert(0, '.')
from f5_t2_lossy_far_wall import strip_h
m = -1.5
for Ly in (12, 20, 30):
    P = np.zeros((2*Ly, 2*Ly)); P[-2:, -2:] = np.eye(2)
    for Gam in (0.3, 1.0, 3.0):
        decs = []
        for kx in np.linspace(-np.pi, np.pi, 121, endpoint=False):
            E = np.linalg.eigvals(strip_h(kx, Ly, m) - 0.5j*Gam*P)
            decs.extend(list(-2*E.imag[E.real < -0.4]))
        decs = np.array(decs)
        print(f"Ly={Ly:2d} Gamma={Gam:3.1f}: valence states={decs.size}, min decay={decs.min():.2e}, "
              f"median={np.median(decs):.2e}, frac<1e-6={np.mean(decs<1e-6):.3f}, frac<1e-4={np.mean(decs<1e-4):.3f}")
