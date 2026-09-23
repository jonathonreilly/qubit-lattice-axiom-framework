#!/usr/bin/env python3
"""next-order-force-between-capturing-bodies a3 (w-jonathonsmac4f50-jb2c0).

Linearized hydrodynamics of the sphere-menu inertial gas (block 44/45 closure): d(drho)/dt + div J = 0 with
J = (1 - rho) g/sqrt3, dg/dt + grad p = nu lap g + (bulk term) + f, p = drho/(3 sqrt3). Steady state: div g = 0, so a
point momentum sink -F delta gives the Stokes problem nu lap g - grad p = F delta, g = -F.(I + rr)/(8 pi nu r).
  E1 (exact, sympy) sound speed (1 - rho)/9 from the two equations; the Oseen pair (u, p) solves the Stokes equations
     away from the origin and is divergence-free; the axial and transverse values 1/(4 pi r), 1/(8 pi r)
  E2 (exact, sympy) the lattice Stokes symbol: g = (I - d d^dagger/|d|^2) F/(nu |d|^2), p = conj(d).F/|d|^2 solves
     -nu |d|^2 g - d p + F = 0, conj(d).g = 0 (d_a = e^{ik_a} - 1)
  N1 the FFT lattice Green function equals a direct solve of the real-space discrete Stokes system on a periodic 6^3 box
  N2 the lattice Stokeslet approaches the continuum Oseen tensor; the periodic box of side 96 keeps 0.70 of it at r = 16
  N3 the second-order pull at the executed parameters (Q ~ 7.8, r = 16, rho = 0.3) against block 49's 0.10 +- 0.07
"""
import sys
import numpy as np
import sympy as sp

FAILS = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok: FAILS.append(name)

# ------------------------------------------------------------------ E1
rho, t, kk = sp.symbols('rho t k', positive=True)
# plane wave drho = A e^{i(kx - wt)}, g = B e^{i(kx - wt)} (longitudinal), no viscosity:
w, A, B = sp.symbols('omega A B')
eqs = [-sp.I*w*A + sp.I*kk*(1 - rho)*B/sp.sqrt(3), -sp.I*w*B + sp.I*kk*A/(3*sp.sqrt(3))]
Msys = sp.Matrix([[sp.diff(e, A), sp.diff(e, B)] for e in eqs])
check("E1.1 the linearized equations give sound speed squared (1 - rho)/9 (block 44's value)",
      sp.simplify(sp.solve(Msys.det(), w)[1]**2/kk**2 - (1 - rho)/9) == 0 or sp.simplify(sp.solve(Msys.det(), w)[0]**2/kk**2 - (1 - rho)/9) == 0)
x, y, z = sp.symbols('x y z', real=True)
r = sp.sqrt(x**2 + y**2 + z**2); X = [x, y, z]
u = [(sp.KroneckerDelta(i, 0)/r + X[i]*X[0]/r**3)/(8*sp.pi) for i in range(3)]      # force e_x, nu = 1
p = X[0]/(4*sp.pi*r**3)
lap = lambda f: sum(sp.diff(f, v, 2) for v in X)
ok_st = all(sp.simplify(lap(u[i]) - sp.diff(p, X[i])) == 0 for i in range(3))
ok_div = sp.simplify(sum(sp.diff(u[i], X[i]) for i in range(3))) == 0
check("E1.2 the Oseen pair u = (I + rr)e_x/(8 pi r), p = x/(4 pi r^3) solves lap u = grad p and div u = 0 for r > 0", ok_st and ok_div)
check("E1.3 on the force axis u_x = 1/(4 pi r); transverse to it u_x = 1/(8 pi r)",
      sp.simplify(u[0].subs({y: 0, z: 0}).subs(x, t) - 1/(4*sp.pi*t)) == 0 and sp.simplify(u[0].subs({x: 0, z: 0}).subs(y, t) - 1/(8*sp.pi*t)) == 0)

# ------------------------------------------------------------------ E2 the lattice symbol
k1, k2_, k3 = sp.symbols('k1 k2 k3', real=True); nu = sp.symbols('nu', positive=True)
d = sp.Matrix([sp.exp(sp.I*k1) - 1, sp.exp(sp.I*k2_) - 1, sp.exp(sp.I*k3) - 1])
dc = d.applyfunc(sp.conjugate)
D2 = sum(sp.expand(d[i]*dc[i]) for i in range(3))
F = sp.Matrix(sp.symbols('F1 F2 F3'))
pk = (dc.T*F)[0]/D2
gk = (F - d*pk)/(nu*D2)
res1 = (-nu*D2*gk - d*pk + F).applyfunc(sp.simplify)
res2 = sp.simplify((dc.T*gk)[0])
check("E2 lattice Stokes symbol: -nu|d|^2 g - d p + F = 0 and conj(d).g = 0 with g = (I - d d^+/|d|^2)F/(nu|d|^2)",
      all(v == 0 for v in res1) and res2 == 0)

# ------------------------------------------------------------------ N1 FFT Green function against a direct solve
def fft_green(L, Fvec=(1.0, 0.0, 0.0)):
    kq = 2*np.pi*np.fft.fftfreq(L)
    KX, KY, KZ = np.meshgrid(kq, kq, kq, indexing='ij')
    dd = [np.exp(1j*KX) - 1, np.exp(1j*KY) - 1, np.exp(1j*KZ) - 1]
    k2 = sum(np.abs(v)**2 for v in dd); k2[0, 0, 0] = 1
    Fh = np.array(Fvec)
    pdot = sum(np.conj(dd[b])*Fh[b] for b in range(3))/k2
    g = [(Fh[a] - dd[a]*pdot)/k2 for a in range(3)]
    for a in range(3): g[a][0, 0, 0] = 0
    return [np.real(np.fft.ifftn(g[a])) for a in range(3)]
def direct_solve(L, Fvec=(1.0, 0.0, 0.0)):
    N = L**3
    ix = lambda a, b, c: ((a % L)*L + (b % L))*L + (c % L)
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    M = np.zeros((4*N, 4*N)); rhs = np.zeros(4*N)
    for a0 in range(L):
        for b0 in range(L):
            for c0 in range(L):
                s = ix(a0, b0, c0)
                for comp in range(3):
                    row = comp*N + s
                    for e in E:                          # nu lap g_comp (nu = 1)
                        M[row, comp*N + ix(a0 + e[0], b0 + e[1], c0 + e[2])] += 1
                        M[row, comp*N + ix(a0 - e[0], b0 - e[1], c0 - e[2])] += 1
                        M[row, comp*N + s] -= 2
                    e = E[comp]                          # - (p(x + e_comp) - p(x))
                    M[row, 3*N + ix(a0 + e[0], b0 + e[1], c0 + e[2])] -= 1
                    M[row, 3*N + s] += 1
                    rhs[row] = -(Fvec[comp]*(1.0 if s == 0 else 0.0) - Fvec[comp]/N)
                row = 3*N + s                             # divergence sum_a (g_a(x) - g_a(x - e_a)) = 0
                for comp in range(3):
                    e = E[comp]
                    M[row, comp*N + s] += 1
                    M[row, comp*N + ix(a0 - e[0], b0 - e[1], c0 - e[2])] -= 1
    sol = np.linalg.lstsq(M, rhs, rcond=None)[0]
    g = [sol[comp*N:(comp + 1)*N].reshape(L, L, L) for comp in range(3)]
    return [gc - gc.mean() for gc in g]
L = 6
gf = fft_green(L); gd = direct_solve(L)
err = max(np.max(np.abs(gf[a] - gd[a])) for a in range(3))
check("N1 FFT lattice Green function = direct solve of the real-space discrete Stokes system (periodic 6^3, unit force)", err < 1e-10, "max diff %.1e" % err)

# ------------------------------------------------------------------ N2 against the continuum and the box
rows = {}
for Lb in (64, 96, 128, 192):
    g = fft_green(Lb)
    rows[Lb] = [(rr, g[0][rr, 0, 0]*4*np.pi*rr, g[0][0, rr, 0]*8*np.pi*rr) for rr in (4, 8, 16)]
for Lb in rows: print("   L=%3d " % Lb + "  ".join("r=%2d axial %.3f transverse %.3f" % v for v in rows[Lb]))
check("N2 NUMERICAL: the lattice Stokeslet tends to the Oseen tensor (axial ratio -> 1 with L, e.g. 0.98 at r=4, L=192), and a periodic "
      "box of side 96 keeps %.2f of the axial value at r = 16" % rows[96][2][1],
      rows[192][0][1] > 0.98 and 0.65 < rows[96][2][1] < 0.75)
box96 = rows[96][2][1]

# ------------------------------------------------------------------ N3 the second-order pull at the executed parameters
Q, rsep, rh = 7.8, 16, 0.3
DL = 0.62                                  # executed longitudinal diffusivity (task statement): D_L = (4/3) nu + nu_bulk
nu_max = 0.75*DL
base = Q/(4*np.pi*rh*rsep)                 # pull / (F1 / nu) in reference units: Q2 / (4 pi nu rho r) x (F1/F_ref)
for push in (1.0, 0.75):
    lo = base/nu_max*push; lob = lo*box96
    print("   first-order push %.2f of reference: second-order pull >= %.3f (infinite space), %.3f (periodic side-96 comparator), nu <= %.3f" % (push, lo, lob, nu_max))
pred = base/nu_max*0.75*box96
check("N3 NUMERICAL: with nu <= (3/4) D_L = 0.465 and block 49's push 0.75, the Stokeslet pull on body 2 is >= %.2f of the "
      "reference (%.2f in the periodic side-96 comparator), within 1 sigma of the executed 0.10 +- 0.07 and of 0.92 - 0.75 = 0.17 +- 0.08"
      % (base/nu_max*0.75, pred), abs(pred - 0.10) < 0.07 and abs(pred - 0.17) < 0.08)

print()
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + FAILS[0]); sys.exit(1)
print("SUMMARY: PROVED within the linearized hydrodynamics (viscosity nu a parameter): a body taking up momentum F1 from a wind "
      "is a point momentum sink whose steady disturbance is the Oseen tensor g = -F1.(I + rr)/(8 pi nu r) (div g = 0 exactly from "
      "number conservation); a capturing body 2 at distance r is pushed towards body 1 by Q2 F1 (I + rr)/(8 pi nu rho r): with "
      "F1 = K0 Q1 Q2/r^2 the second-order force is attractive, K0 Q1 Q2^2/(4 pi nu rho r^3) on the axis, i.e. Q2/(4 pi nu rho r) of "
      "the reference; at the executed parameters >= %.2f (%.2f with the periodic box), matching block 49's pull of a body in "
      "balance 0.10 +- 0.07 and the capturing pair's 0.92 against the balanced push 0.75" % (base/nu_max*0.75, pred))
print("HIT: the force of second order in the capture rates is the Stokeslet push: body 1's momentum uptake F1 = K0 Q1 Q2/r^2 "
      "leaves the Oseen flow -F1.(I + rr)/(8 pi nu r) (div g = 0 exactly), so a capturing body 2 is pulled towards body 1 with "
      "K0 Q1 Q2^2/(4 pi nu rho r^3) on the axis (Q2/(4 pi nu rho r) of the first-order force, attractive, one power of r faster); "
      "with nu <= (3/4)(0.62) it is >= 0.21 of the reference at Q = 7.8, r = 16, rho = 0.3 (0.15 in a periodic side-96 box), "
      "accounting for block 49's pull of a body in balance (0.10 +- 0.07) and for 0.92 - 0.75 between capturing and balanced pushes")
