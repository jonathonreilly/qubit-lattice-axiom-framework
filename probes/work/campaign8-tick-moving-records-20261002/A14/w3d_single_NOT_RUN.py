"""A14 proposed check (NOT RUN: needs ~1-2 GB and minutes): single-wall forward
T-matrix of a 3D conveyor (Weyl-type) walk, to see whether the 2D results (log-running
velocity, mass at second order for r=+-i; 1/k gap-like shift for r=+-1) carry to 3D.
Walk: U = S_Z S_Y S_X, S_a moves the sigma_a eigencomponents +-1 along axis a;
U(k) = exp(-i kz sz) exp(-i ky sy) exp(-i kx sx), one Weyl cone at k=0 (plus doublers).
Wall: a component that would enter the wall stays and becomes the opposite mover, times r.
Usage: python3 w3d_single_NOT_RUN.py 128 64 1j     (L, T=L/2, r)
Output: Re s = dw/rho and -2 Im s = G/rho per k, as in w2d_single.py.
"""
import sys
import numpy as np
L = int(sys.argv[1]); T = int(sys.argv[2]); r = complex(sys.argv[3])
s2 = 1/np.sqrt(2)
P = {0: (np.array([1, 1])*s2, np.array([1, -1])*s2),          # sigma_x eigenvectors (+,-)
     1: (np.array([1, 1j])*s2, np.array([1, -1j])*s2),        # sigma_y
     2: (np.array([1, 0]), np.array([0, 1]))}                 # sigma_z
Wm = np.zeros((L, L, L)); Wm[L//2, L//2, L//2] = 1; F = 1 - Wm
def sub(psi, a):
    vp, vm = P[a]
    ap = np.conj(vp[0])*psi[:, 0] + np.conj(vp[1])*psi[:, 1]
    am = np.conj(vm[0])*psi[:, 0] + np.conj(vm[1])*psi[:, 1]
    Wb = np.roll(Wm, 1, axis=a); Wf = np.roll(Wm, -1, axis=a)
    nap = F*(np.roll(ap, 1, axis=a+1) + r*Wb*am)
    nam = F*(np.roll(am, -1, axis=a+1) + r*Wf*ap)
    out = np.empty_like(psi)
    out[:, 0] = vp[0]*nap + vm[0]*nam; out[:, 1] = vp[1]*nap + vm[1]*nam
    return out
def Uk(k):
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    e = lambda q, s: np.cos(q)*np.eye(2) - 1j*np.sin(q)*s
    return e(k[2], sz) @ e(k[1], sy) @ e(k[0], sx)
ns = [(4, 0, 0), (8, 0, 0), (12, 0, 0), (16, 0, 0), (5, 5, 5)]
x = np.arange(L)
for n in ns:
    k = 2*np.pi*np.array(n)/L
    w, V = np.linalg.eig(Uk(k)); om = -np.angle(w); i = int(np.argmax(om)); om0, v = om[i], V[:, i]
    ph = np.exp(1j*(k[0]*x[:, None, None] + k[1]*x[None, :, None] + k[2]*x[None, None, :]))
    psi = np.zeros((1, 2, L, L, L), complex); psi[0, 0] = v[0]*ph*F; psi[0, 1] = v[1]*ph*F
    psi /= np.linalg.norm(psi); chi = psi.copy(); sig = []
    for t in range(1, T + 1):
        psi = sub(sub(sub(psi, 0), 1), 2)
        sig.append((np.vdot(chi, psi)*np.exp(1j*om0*t) - 1)*L**3)
    sig = np.array(sig); tt = np.arange(1, T + 1); sel = tt >= T//2
    s = 1j*np.polyfit(tt[sel], sig[sel], 1)[0]
    print(n, f"|k|={np.linalg.norm(k):.4f} w0={om0:.4f} dw/rho={s.real:+.3f} G/rho={-2*s.imag:.3f}")
