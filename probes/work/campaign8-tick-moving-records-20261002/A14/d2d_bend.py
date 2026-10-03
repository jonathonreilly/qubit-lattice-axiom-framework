"""A14 check N5: ray bending of a Dirac-type ripple under a paced change (averaged generator).
Continuous-time lattice Dirac H = sum_bonds r_b (1/2i)(|x+e_a><x| - h.c.) sigma_a  (cone at E=0).
Activity field N(y) = 1 - g (y - y0) (clock rate).  Bond rates:
  OR  : r_b = (N_x + N_y)/2      (one event at either end steps the bond)
  AND : r_b = N_x N_y            (each end needs its own event)
  OBST: r_b = 1 for all bonds (no pacing) -- control, no bending.
Eikonal prediction: transverse drift dy = (1/2) * p * g * t^2 toward smaller N, p = 1 (OR), 2 (AND).
"""
import sys, signal, time
import numpy as np
signal.alarm(58)
L = 160; g = float(sys.argv[1]); T = float(sys.argv[2]); dt = 0.1
x = np.arange(L); X, Y = np.meshgrid(x, x, indexing='ij')
y0 = L//2; x0 = 30; sig = float(sys.argv[3]); k0 = 0.45
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]])
# upper-branch spinor for k = (k0, 0): eigenvector of sin(k0) sigma_x with + sign
v = np.array([1, -1], complex)/np.sqrt(2)   # sigma_x=-1: upper branch of -sin(k) sigma_x, moves +x
env = np.exp(-((X-x0)**2 + (Y-y0)**2)/(4*sig**2) + 1j*k0*X)
psi0 = np.stack([v[0]*env, v[1]*env]); psi0 /= np.linalg.norm(psi0)
N = 1 - g*(Y - y0)
def rates(mode):
    Nx1 = np.roll(N, -1, axis=0); Ny1 = np.roll(N, -1, axis=1)
    if mode == 'OR':  return (N + Nx1)/2, (N + Ny1)/2
    if mode == 'AND': return N*Nx1, N*Ny1
    return np.ones_like(N), np.ones_like(N)
def Hpsi(psi, rx, ry):
    out = np.zeros_like(psi)
    for (r, ax, s) in ((rx, 1, sx), (ry, 2, sy)):
        # bond (x, x+e): rate r[x]; term (1/2i)(|x+e><x| - |x><x+e|) sigma_a
        sp = np.einsum('ij,jab->iab', s, psi)
        fwd = np.roll(r*sp, 1, axis=ax)            # (|x+e><x|) psi : value at x+e from x
        bwd = r*np.roll(sp, -1, axis=ax)           # (|x><x+e|) psi : value at x from x+e
        out += (fwd - bwd)/(2j)
    return out
def evolve(mode):
    rx, ry = rates(mode); psi = psi0.copy(); nsteps = int(round(T/dt))
    for _ in range(nsteps):
        k1 = -1j*Hpsi(psi, rx, ry); k2 = -1j*Hpsi(psi + 0.5*dt*k1, rx, ry)
        k3 = -1j*Hpsi(psi + 0.5*dt*k2, rx, ry); k4 = -1j*Hpsi(psi + dt*k3, rx, ry)
        psi = psi + dt*(k1 + 2*k2 + 2*k3 + k4)/6
    p = np.sum(np.abs(psi)**2, axis=0)
    return np.sum(X*p)/p.sum(), np.sum(Y*p)/p.sum(), p.sum()
t0 = time.time()
res = {m: evolve(m) for m in ('NONE', 'OR', 'AND')}
xc0 = np.sum(X*np.abs(psi0).sum(0)**0)  # unused
base = res['NONE']
print(f"g={g} T={T} dt={dt} L={L} k0={k0}")
for m in ('NONE', 'OR', 'AND'):
    xc, yc, nrm = res[m]
    print(f"  {m:4s}: x-advance {xc-x0:7.3f}  y-drift {yc-y0:+8.4f}  (rel. to no-pacing {yc-base[1]:+8.4f})  norm {nrm:.6f}")
pred = 0.5*g*T**2
d_or = res['OR'][1]-base[1]; d_and = res['AND'][1]-base[1]
print(f"  eikonal: OR {-pred:+.4f}?  sign convention: N smaller at larger y -> drift toward +y; magnitude OR {pred:.4f}, AND {2*pred:.4f}")
print(f"  measured |drift| OR {abs(d_or):.4f} (ratio to eikonal {abs(d_or)/pred:.3f}), AND {abs(d_and):.4f} (ratio {abs(d_and)/(2*pred):.3f}); AND/OR = {d_and/d_or:.4f}")
print(f"elapsed {time.time()-t0:.1f}s")
