"""NT-2 T22 structured pools P4: (plaquette point set) x (Nx x Ny equally spaced holonomy ring in X0, Y0).
The pool matrix is block-circulant in the ring; its spectrum is the union over ring momenta (jx, jy) of the spectra of
M x M Hermitian blocks K_j(a, b) = sum_{s,t} K(p_a, p_b; dX0 = 2 pi s/Nx, dY0 = 2 pi t/Ny) e^{-2 pi i (jx s/Nx + jy t/Ny)}.
Usage: python t22_ring.py GRID H NX NY [DELTA]
  GRID: oct  (admissible margin octahedron |P|+|Q|+|R| <= 2(delta-0.05), spacing H)
        line_P / line_Q / line_R (1D lines through 0 inside the margin octahedron, spacing H)
        unres (power reference R1: cube |P|,|Q|,|R| <= 2.6, spacing H; NOT admissible)
"""
import sys, time, resource, numpy as np
from t22lib import *
grid = sys.argv[1]; h = float(sys.argv[2]); NX = int(sys.argv[3]); NY = int(sys.argv[4])
delta = float(sys.argv[5]) if len(sys.argv) > 5 else 0.6
r = 2 * (delta - 0.05)
if grid == 'oct':
    ax = np.arange(-np.floor(r / h) * h, r + 1e-9, h)
    G = np.array([(p, q, s) for p in ax for q in ax for s in ax if abs(p) + abs(q) + abs(s) <= r + 1e-12])
elif grid.startswith('line'):
    ax = np.arange(-np.floor(r / h) * h, r + 1e-9, h); z = np.zeros_like(ax)
    G = {'line_P': np.c_[ax, z, z], 'line_Q': np.c_[z, ax, z], 'line_R': np.c_[z, z, ax]}[grid]
elif grid.startswith('uline'):
    ax = np.arange(-2.6, 2.6 + 1e-9, h); z = np.zeros_like(ax)
    G = {'uline_P': np.c_[ax, z, z], 'uline_Q': np.c_[z, ax, z], 'uline_R': np.c_[z, z, ax]}[grid]
elif grid.startswith('plane'):
    ax = np.arange(-np.floor(r / h) * h, r + 1e-9, h)
    c = {'plane_PR': (0, 2), 'plane_PQ': (0, 1), 'plane_QR': (1, 2)}[grid]
    G = []
    for x in ax:
        for y in ax:
            if abs(x) + abs(y) <= r + 1e-12:
                g = [0.0, 0.0, 0.0]; g[c[0]] = x; g[c[1]] = y; G.append(g)
    G = np.array(G)
elif grid == 'unres':
    ax = np.arange(-2.6, 2.6 + 1e-9, h)
    G = np.array([(p, q, s) for p in ax for q in ax for s in ax])
P, Q, R = G.T
p00, p10, p01 = (P + Q - R) / 2, (P - Q + R) / 2, (-P + Q + R) / 2
p11 = -(p00 + p10 + p01)
M = len(G)
NSX = sum(1 for s in range(-(NX // 2), NX - NX // 2) if abs(2 * np.pi * s / NX) < 2 * delta) if NX > 1 else 1
NSY = sum(1 for s in range(-(NY // 2), NY - NY // 2) if abs(2 * np.pi * s / NY) < 2 * delta) if NY > 1 else 1
est = M * M * (NSX * NSY * 8 + NSY * 16 * 2 + 40 * 8) / 2**20 + 40  # Kst + complex A,B + temporaries + interpreter
print(f'memory estimate ~{est:.0f} MB (Kst x3)', flush=True)
assert est < 200, 'over memory budget'
maxplaq = np.max(np.abs(np.c_[p00, p10, p01, p11]))
print(f"grid {grid} h={h} M={M} ring {NX}x{NY} delta={delta} | max|plaquette| {maxplaq:.4f} (admissible margin: {maxplaq <= delta-0.05+1e-12})", flush=True)
sx = [s for s in range(-(NX // 2), NX - NX // 2) if abs(2 * np.pi * s / NX) < 2 * delta] if NX > 1 else [0]
sy = [t for t in range(-(NY // 2), NY - NY // 2) if abs(2 * np.pi * t / NY) < 2 * delta] if NY > 1 else [0]
t0 = time.time()
Iu = dict(p00=p00[:, None], p10=p10[:, None], p01=p01[:, None], p11=p11[:, None])
Iv = dict(p00=p00[None, :], p10=p10[None, :], p01=p01[None, :], p11=p11[None, :])
Kst = np.zeros((M, M, len(sx), len(sy)))
for ia, s in enumerate(sx):
    for ib, t in enumerate(sy):
        X0u = 2 * np.pi * s / max(NX, 1); Y0u = 2 * np.pi * t / max(NY, 1)
        Iu2 = dict(Iu, X0=X0u + 0 * Iu['p00'], Y0=Y0u + 0 * Iu['p00'], X1=X0u - Iu['p00'] - Iu['p10'], Y1=Y0u + Iu['p00'] + Iu['p01'])
        Iv2 = dict(Iv, X0=0 * Iv['p00'], Y0=0 * Iv['p00'], X1=-Iv['p00'] - Iv['p10'], Y1=Iv['p00'] + Iv['p01'])
        Kst[:, :, ia, ib] = kernel_closed_inv(Iu2, Iv2, delta)
sx = np.array(sx); sy = np.array(sy)
res = []
for jx in range(NX // 2 + 1):
    A = np.zeros((M, M, len(sy)), complex)  # loop instead of tensordot (tensordot made complex copies of Kst)
    for ia in range(len(sx)):
        A += np.exp(-2j * np.pi * jx * sx[ia] / max(NX, 1)) * Kst[:, :, ia, :]
    for jy in range(NY // 2 + 1):
        B = A @ np.exp(-2j * np.pi * jy * sy / max(NY, 1))
        herm = np.abs(B - B.conj().T).max()
        ev = np.linalg.eigvalsh(0.5 * (B + B.conj().T))
        res.append((ev[0], ev[-1], jx, jy, herm))
res.sort()
lmax = max(z[1] for z in res)
E = M * NX * NY * 1e-15 * lmax * 10  # floating-point floor (kernel exact; closed form == independent builder to 1e-17, V0)
print(f"overall lam_max {lmax:.4e}; most negative blocks (lam_min, jx, jy):")
for z in res[:6]:
    print(f"   lam_min {z[0]:+.4e} (rel {z[0]/lmax:+.3e}) at (jx, jy) = ({z[2]}, {z[3]}), herm defect {z[4]:.1e}")
print(f"RESULT grid={grid} h={h} M={M} ring={NX}x{NY} delta={delta}: lam_min {res[0][0]:+.4e} rel {res[0][0]/lmax:+.3e} "
      f"at j=({res[0][2]},{res[0][3]}) | floor E {E:.1e} | neg-converged {res[0][0] < -10*E and res[0][0]/lmax < -1e-9} | "
      f"admissible {maxplaq <= delta-0.05+1e-12} | {time.time()-t0:.1f}s RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20:.0f}MB")
