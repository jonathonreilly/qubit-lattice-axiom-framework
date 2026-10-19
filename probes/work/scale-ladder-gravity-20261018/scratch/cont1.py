"""C1/C2: continuous-time influence on the spatial grid (exact in Fourier).
 real wave with memory     u_tt = lap u           (omega^2 = sum 4 sin^2(k/2); speed 1, no stability limit)
 real first-order (no memory)  u_t = lap u        (diffusion)
 complex first-order (qubit-like, two components): i psi_t = H psi, H = sum_j sigma_j sin k_j (naive Dirac)
Point start; amplitude profile along the axis at time t; leakage beyond the cone r > t."""
import numpy as np
L = 128; c = L//2
k = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
ph = 4*(np.sin(KX/2)**2 + np.sin(KY/2)**2 + np.sin(KZ/2)**2); w = np.sqrt(ph)
d0 = np.zeros((L, L, L)); d0[0, 0, 0] = 1.0; F0 = np.fft.fftn(d0)
def axis_profile(field, t, rs):
    return np.array([abs(field[r % L, 0, 0]) for r in rs])
t = 30; rs = [10, 20, 25, 30, 33, 36, 40, 45]
u = np.real(np.fft.ifftn(np.cos(w*t)*F0))                     # wave with memory, released at rest
dif = np.real(np.fft.ifftn(np.exp(-ph*t)*F0))
sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]])
# exp(-i H t) with H = a.sigma : cos(|a|t) I - i sin(|a|t) (a.sigma)/|a|  ; start in component 0 at the origin
ax, ay, az = np.sin(KX), np.sin(KY), np.sin(KZ); A = np.sqrt(ax**2 + ay**2 + az**2) + 1e-300
c0 = np.cos(A*t) - 1j*np.sin(A*t)*az/A; c1 = -1j*np.sin(A*t)*(ax + 1j*ay)/A
psi0 = np.fft.ifftn(c0*F0); psi1 = np.fft.ifftn(c1*F0); dens = np.abs(psi0)**2 + np.abs(psi1)**2
for name, f in (('real wave (memory), continuous time', u), ('real first-order (diffusion)', dif), ('complex 2-component (qubit-like), first-order', np.sqrt(dens))):
    p = axis_profile(f, t, rs); p = p/p.max()
    print(f"{name:46s} t={t}: |amplitude| along axis at r = " + ", ".join(f"{r}:{v:.1e}" for r, v in zip(rs, p)))
# leakage fraction outside the cone for the two wave-carrying rules
X, Y, Z = np.meshgrid(*[np.minimum(np.arange(L), L - np.arange(L))]*3, indexing='ij'); R = np.sqrt(X**2 + Y**2 + Z**2)
for name, f in (('real wave', u**2), ('qubit-like', dens)):
    tot = f.sum(); print(f"{name:10s}: share of |amplitude|^2 beyond r > 1.1 t: {f[R > 1.1*t].sum()/tot:.2e}; beyond r > 1.3 t: {f[R > 1.3*t].sum()/tot:.2e}")
