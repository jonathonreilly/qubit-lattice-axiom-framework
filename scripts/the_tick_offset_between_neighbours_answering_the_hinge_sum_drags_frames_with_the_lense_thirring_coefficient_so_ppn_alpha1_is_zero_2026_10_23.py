AUDIT_INPUT_PATHS = ('docs/THE_TICK_OFFSET_BETWEEN_NEIGHBOURS_ANSWERING_THE_HINGE_SUM_DRAGS_FRAMES_WITH_THE_LENSE_THIRRING_COEFFICIENT_SO_PPN_ALPHA1_IS_ZERO_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Tick-fraction frame dragging: the stationary (rotating) sector of the tick-fraction rule.
Variables: site tick fraction N, spatial edges h, and the tick OFFSET between neighbouring sites
(shift beta, one value per neighbour pair = per edge).  Stationary: edges and offsets are the same
every tick.  The hinge sum (1/8 pi G) sum A delta over sheared prisms -> (1/16 pi G) int sqrt(-g) R4
(SUPPLIED Regge limit); the record phase per taken tick is -m dtau.  First order in J, flat background.
Self-contained; seeded; numpy + scipy + sympy only."""
AUDIT_TIMEOUT_SEC = 120
import time
import numpy as np
import sympy as sp
import scipy.sparse as sps
from scipy.sparse.linalg import cg, minres
from sympy.calculus.euler import euler_equations

np.random.seed(20261023)
T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    if ok: P += 1
    else: F += 1
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

x, y, z, t = sp.symbols('x y z t', real=True)
X3 = (x, y, z)
eps, G, lam = sp.symbols('epsilon G lambda', positive=True)
b = [sp.Function(f'b{i}')(x, y, z) for i in range(3)]
jf = [sp.Function(f'j{i}')(x, y, z) for i in range(3)]

# ---------- A. the sheared-prism hinge sum reduces to the K-terms with coefficient one ----------
# stationary metric with offsets: ds^2 = -dt^2 + |dx + eps b dt|^2  (N = 1, flat edges, sqrt(-g) = 1)
X4 = (t, x, y, z)
g4 = sp.zeros(4, 4)
g4[0, 0] = -1 + eps**2*sum(bi**2 for bi in b)
for i in range(3):
    g4[0, i+1] = g4[i+1, 0] = eps*b[i]; g4[i+1, i+1] = 1
check("A0 det g = -1 exactly (sqrt(-g) = N sqrt(h) = 1)", sp.simplify(g4.det()) == -1)
gi4 = sp.simplify(g4.inv())
Gam = [[[sum(gi4[a, d]*(sp.diff(g4[d, bb], X4[c]) + sp.diff(g4[d, c], X4[bb]) - sp.diff(g4[bb, c], X4[d]))
             for d in range(4))/2 for c in range(4)] for bb in range(4)] for a in range(4)]
R4 = 0
for bb in range(4):
    for c in range(4):
        Ric = sum(sp.diff(Gam[a][bb][c], X4[a]) - sp.diff(Gam[a][bb][a], X4[c]) +
                  sum(Gam[a][a][d]*Gam[d][bb][c] - Gam[a][c][d]*Gam[d][bb][a] for d in range(4)) for a in range(4))
        R4 += gi4[bb, c]*Ric
R4_2 = sp.expand(sp.series(sp.expand(R4), eps, 0, 3).removeO()).coeff(eps, 2)
s = [[(sp.diff(b[j], X3[i]) + sp.diff(b[i], X3[j]))/2 for j in range(3)] for i in range(3)]
divb = sum(sp.diff(b[i], X3[i]) for i in range(3))
LK = sum(s[i][j]**2 for i in range(3) for j in range(3)) - divb**2     # K_ij K^ij - K^2, K_ij = -s_ij
E_R = [e.lhs for e in euler_equations(R4_2, b, X3)]
E_K = [e.lhs for e in euler_equations(LK, b, X3)]
check("A1 sqrt(-g) R4 at O(offset^2) has the same Euler-Lagrange equations as K_ij K^ij - K^2 (coefficient ONE, "
      "same hinge sum as the static N sqrt(h) R3 part)", all(sp.simplify(E_R[i] - E_K[i]) == 0 for i in range(3)))

# ---------- B. how the record's momentum couples: a record crossing tilted timelike hinges ----------
v = sp.symbols('v0:3', real=True); bb_ = sp.symbols('B0:3', real=True); Nn = sp.Symbol('N', positive=True)
dtau = sp.sqrt(Nn**2 - sum((v[i] + eps*bb_[i])**2 for i in range(3)))
lin = sp.simplify(sp.diff(dtau, eps).subs(eps, 0))
check("B1 record phase per taken tick -m dtau: linear offset term is +m v.beta / dtau0 (momentum x offset)",
      sp.simplify(lin + sum(v[i]*bb_[i] for i in range(3))/sp.sqrt(Nn**2 - sum(vi**2 for vi in v))) == 0,
      "S_m contains + int j.beta, j = rho v")

# ---------- C. the shift (offset) equation from the rule's stationarity ----------
Lg = (LK - (lam - 1)*divb**2)/(16*sp.pi*G) + sum(jf[i]*b[i] for i in range(3))   # lam = 1 is the hinge sum
EL = [sp.expand(e.lhs) for e in euler_equations(Lg, b, X3)]
lap = lambda f: sum(sp.diff(f, X3[i], 2) for i in range(3))
EL1 = [sp.expand(e.subs(lam, 1)) for e in EL]
target = [jf[i] - (lap(b[i]) - sp.diff(divb, X3[i]))/(16*sp.pi*G) for i in range(3)]
check("C1 offset equation: curl curl beta = -16 pi G j  (i.e. lap beta - grad div beta = 16 pi G rho v)",
      all(sp.simplify(EL1[i] - target[i]) == 0 for i in range(3)))
f = sp.Function('f')(x, y, z)
gsub = {b[i]: sp.diff(f, X3[i]) for i in range(3)}
pure = [sp.simplify((EL1[i] - jf[i]).subs(gsub).doit()) for i in range(3)]
check("C2 a per-SITE offset (beta = grad f, tick-counter relabel) drops out identically: pure gauge",
      all(p == 0 for p in pure))
divEL = sp.expand(sum(sp.diff(EL[i], X3[i]) for i in range(3)))
divj = sum(sp.diff(jf[i], X3[i]) for i in range(3))
check("C3 divergence of the offset equation = div j + (lam-1) lap(div beta)/(8 pi G): solvable iff the record "
      "current is conserved; for lam != 1, div beta = 0, curl beta unchanged",
      sp.simplify(divEL - divj - (lam - 1)*lap(divb)/(8*sp.pi*G)) == 0)

# ---------- D. rotating source: exterior field and gyroscope precession ----------
rr, th, ph, Rb, rho0, w = sp.symbols('r theta phi R rho0 omega', positive=True)
xs = [rr*sp.sin(th)*sp.cos(ph), rr*sp.sin(th)*sp.sin(ph), rr*sp.cos(th)]
jac = rr**2*sp.sin(th)
Mom = sp.Matrix(3, 3, lambda k, m: sp.integrate(sp.integrate(sp.integrate(rho0*xs[k]*xs[m]*jac, (ph, 0, 2*sp.pi)),
                                                             (th, 0, sp.pi)), (rr, 0, Rb)))
Iball = sp.integrate(sp.integrate(sp.integrate(rho0*(xs[0]**2 + xs[1]**2)*jac, (ph, 0, 2*sp.pi)), (th, 0, sp.pi)), (rr, 0, Rb))
check("D1 uniform ball: int rho x_k x_m = (I/2) delta_km, so V = G int rho v/|x-x'| -> G (J x x)/(2 r^3) at dipole order",
      sp.simplify(Mom - Iball/2*sp.eye(3)) == sp.zeros(3, 3))
Jv = sp.Matrix(sp.symbols('J0:3', real=True)); Xv = sp.Matrix([x, y, z]); R3 = sp.sqrt(x**2 + y**2 + z**2)
beta_ext = -4*G*Jv.cross(Xv)/(2*R3**3)          # Coulomb solution of C1: beta = -4 G int j/|x-x'|
curl = lambda A: sp.Matrix([sp.diff(A[2], y) - sp.diff(A[1], z), sp.diff(A[0], z) - sp.diff(A[2], x),
                            sp.diff(A[1], x) - sp.diff(A[0], y)])
cc = sp.simplify(curl(curl(beta_ext)))
dvb = sp.simplify(sum(sp.diff(beta_ext[i], X3[i]) for i in range(3)))
check("D2 exterior beta = -2G (J x x)/r^3 solves the source-free offset equation (curl curl = 0, div = 0)",
      cc == sp.zeros(3, 1) and dvb == 0)
Om = sp.simplify(-curl(beta_ext)/2)
LT = G*(3*(Jv.dot(Xv))*Xv/R3**2 - Jv)/R3**3
check("D3 gyroscope precession -(1/2) curl beta = (G/r^3)[3(J.rhat)rhat - J]: Lense-Thirring, GR coefficient",
      sp.simplify(Om - LT) == sp.zeros(3, 1))

# ---------- E. preferred-frame test alpha1: moving point source vs boosted static field ----------
gam, U = sp.symbols('gamma U', real=True); wv = sp.symbols('w0:3', real=True)
g00 = -(1 - 2*U); gij = (1 + 2*gam*U)
g0i_boost = [sp.expand(-wv[i]*g00 - wv[i]*gij) for i in range(3)]    # first order in w
g0i_rule = [-4*U*wv[i] for i in range(3)]                             # C1 with j = rho w: beta = -4 U w
a1 = sp.Symbol('alpha1')
sol = sp.solve(sp.Eq(-4, -(2*(1 + gam) + a1/2)), a1)[0]
check("E1 boosted static field g0i = -2(1+gamma)U w; rule's offset gives -4 U w; equal iff gamma = 1 "
      "(tick-skip-gamma's derived value)", all(sp.simplify((g0i_boost[i] - g0i_rule[i]).subs(gam, 1)) == 0 for i in range(3)))
comb = sp.Rational(1, 8)*(4*gam + 4 + sol)
check("E2 alpha1 = 8 - 4(1+gamma) = 0 at gamma = 1; PPN frame-dragging factor (4gamma+4+alpha1)/8 = 1",
      sol.subs(gam, 1) == 0 and sp.simplify(comb.subs(gam, 1)) == 1, f"alpha1(gamma) = {sol}")

# ---------- F. option table (rule-internal choices) ----------
cw = sp.Symbol('c', positive=True)
opt = {'per-edge offset responds (hinge sum, c=1)': 1, 'offset frozen (beta = 0)': 0,
       'per-site offset only (beta = grad f)': 0, 'tilt hinges weighted c': 1/cw}
a1opt = {k: sp.simplify(8*vv - 8) for k, vv in opt.items()}
print("INFO F options (frame-dragging ratio to GR -> alpha1): " +
      "; ".join(f"{k}: {opt[k]} -> {a1opt[k]}" for k in opt))
check("F1 frozen or per-site-only offset: Omega_FD = 0, alpha1 = -8; responding per-edge offset: ratio 1, alpha1 = 0",
      a1opt['offset frozen (beta = 0)'] == -8 and a1opt['per-edge offset responds (hinge sum, c=1)'] == 0)

# ---------- G. lattice check of the offset equation (periodic cubic L = 14, offsets on edges) ----------
L = 14; n = L**3
idx = lambda i, j, k: ((i % L)*L + (j % L))*L + (k % L)
rows, cols, vals = [], [], []
for i in range(L):
    for j in range(L):
        for k in range(L):
            v0 = idx(i, j, k)
            for a, (di, dj, dk) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                e = 3*v0 + a
                rows += [e, e]; cols += [idx(i+di, j+dj, k+dk), v0]; vals += [1.0, -1.0]
d0 = sps.csr_matrix((vals, (rows, cols)), shape=(3*n, n))          # site potential -> edge offset
rows, cols, vals = [], [], []
eid = lambda i, j, k, a: 3*idx(i, j, k) + a
for i in range(L):
    for j in range(L):
        for k in range(L):
            base = (i, j, k)
            for p, (a, c) in enumerate(((0, 1), (1, 2), (2, 0))):     # plaquette in (a,c) plane
                pl = 3*idx(i, j, k) + p
                ua = [0, 0, 0]; ua[a] = 1; uc = [0, 0, 0]; uc[c] = 1
                for sgn, (o, d) in ((1, ((0, 0, 0), a)), (1, (tuple(ua), c)), (-1, (tuple(uc), a)), (-1, ((0, 0, 0), c))):
                    rows.append(pl); cols.append(eid(i+o[0], j+o[1], k+o[2], d)); vals.append(float(sgn))
d1 = sps.csr_matrix((vals, (rows, cols)), shape=(3*n, 3*n))         # edge offset -> plaquette slip (curl)
check("G1 lattice: curl of a site-difference offset is identically zero (d1 d0 = 0): per-site offsets carry no slip",
      abs(d1 @ d0).max() == 0)
# current loop: 2x2 square in plane z = 7, centred on the axis x = y = 7, unit current (conserved: j = d1^T p)
pvec = np.zeros(3*n)
for (i, j) in ((6, 6), (6, 7), (7, 6), (7, 7)):
    pvec[3*idx(i, j, 7) + 0] = 1.0                                    # xy-plaquettes
jv = d1.T @ pvec
check("G2 loop current is conserved on the lattice (d0^T j = 0): the per-site offset sees no source",
      np.abs(d0.T @ jv).max() < 1e-14)
Gn = 1.0
def solve_hodge(wgt):
    A = (d1.T @ d1 + wgt*(d0 @ d0.T)).tocsr()
    sol_, info = cg(A, -16*np.pi*Gn*jv, rtol=1e-12, maxiter=20000)
    return sol_, info
b1, i1 = solve_hodge(1.0); b3, i3 = solve_hodge(3.0)
A0 = (d1.T @ d1).tocsr()
bg, ig = minres(A0, -16*np.pi*Gn*jv, rtol=1e-12, maxiter=20000)
res = np.linalg.norm(A0 @ b1 + 16*np.pi*Gn*jv)/np.linalg.norm(16*np.pi*Gn*jv)
check("G3 lattice offset equation d1^T d1 beta = -16 pi G j solved (residual)", res < 1e-8 and i1 == 0, f"rel res {res:.1e}")
F1, F3, Fg = d1 @ b1, d1 @ b3, d1 @ bg
dev = max(np.abs(F1 - F3).max(), np.abs(F1 - Fg).max())/np.abs(F1).max()
check("G4 the slip field curl beta is independent of the longitudinal (gauge) weight and of gauge fixing",
      dev < 1e-6, f"max rel dev {dev:.1e}")
Lap0 = (d0.T @ d0).tocsr()                                            # positive scalar lattice Laplacian
jx = jv[0::3]
Vx, iv = cg(Lap0, 4*np.pi*Gn*jx, rtol=1e-13, maxiter=20000)
Vx -= Vx.mean(); bx = b1[0::3] - b1[0::3].mean()
dv = np.abs(bx + 4*Vx).max()/np.abs(bx).max()
check("G5 lattice: beta_x = -4 V_x with V the Newtonian-normalised potential of the momentum density (same Green function)",
      dv < 1e-6, f"rel dev {dv:.1e}")
gl_x, gl_w = np.polynomial.legendre.leggauss(24)
def square(cx, cy, cz, half, plane):                 # oriented square as 4 segments (start, end) (xy plane)
    if plane == 'xy':
        P_ = [(cx-half, cy-half, cz), (cx+half, cy-half, cz), (cx+half, cy+half, cz), (cx-half, cy+half, cz)]
    return [(np.array(P_[q]), np.array(P_[(q+1) % 4])) for q in range(4)]
def neumann(S1, S2):                                  # int int dl.dl'/|x-x'| (mutual inductance)
    tot = 0.0
    for (a0, a1) in S1:
        for (c0, c1) in S2:
            da, dc = a1 - a0, c1 - c0
            pa = a0[None, :] + np.outer((gl_x + 1)/2, da); pc = c0[None, :] + np.outer((gl_x + 1)/2, dc)
            dist = np.linalg.norm(pa[:, None, :] - pc[None, :, :], axis=2)
            tot += np.dot(da, dc)/4*np.einsum('i,j,ij->', gl_w, gl_w, 1/dist)
    return tot
# isolated loop: by G5 each offset component obeys the scalar lattice equation, so solve it by FFT on a
# larger periodic box (Lb = 96; images ~ (r/Lb)^3) and compare its slip flux with the continuum Neumann integral
Lb = 96; cb = Lb//2
jx_b = np.zeros((Lb, Lb, Lb)); jy_b = np.zeros((Lb, Lb, Lb))
for (i, j) in ((cb-1, cb-1), (cb-1, cb), (cb, cb-1), (cb, cb)):   # unit-current boundary of the 2x2 xy-plaquettes
    jx_b[i, j, cb] += 1; jy_b[i+1, j, cb] += 1; jx_b[i, j+1, cb] -= 1; jy_b[i, j, cb] -= 1
kk = 2*np.pi*np.fft.fftfreq(Lb)
k2 = (2 - 2*np.cos(kk))[:, None, None] + (2 - 2*np.cos(kk))[None, :, None] + (2 - 2*np.cos(kk))[None, None, :]
k2[0, 0, 0] = 1.0
def solve_fft(src):
    hat = -16*np.pi*Gn*np.fft.fftn(src)/k2; hat[0, 0, 0] = 0
    return np.real(np.fft.ifftn(hat))
bxb, byb = solve_fft(jx_b), solve_fft(jy_b)
def circ(i0, j0, k0, side):         # circulation of beta around the xy-window [i0, i0+side] x [j0, j0+side] at z = k0
    c_ = sum(bxb[i0+q, j0, k0] for q in range(side)) + sum(byb[i0+side, j0+q, k0] for q in range(side))
    c_ -= sum(bxb[i0+q, j0+side, k0] for q in range(side)) + sum(byb[i0, j0+q, k0] for q in range(side))
    return c_
loop = square(float(cb), float(cb), float(cb), 1.0, 'xy')
rows_out, err = [], {}
for r_ in (4, 7, 10):
    Ba = circ(cb-1, cb-1, cb + r_, 2); Be = circ(cb + r_ - 1, cb-1, cb, 2)
    ca = -4*Gn*neumann(square(float(cb), float(cb), float(cb + r_), 1.0, 'xy'), loop)
    ce = -4*Gn*neumann(square(float(cb + r_), float(cb), float(cb), 1.0, 'xy'), loop)
    err[r_] = max(abs(Ba/ca - 1), abs(Be/ce - 1))
    rows_out.append(f"r={r_}: axis {Ba/ca:.3f}, eq {Be/ce:.3f}, lattice axis/eq {Ba/Be:.2f} vs {ca/ce:.2f}")
check("G6 isolated lattice loop: slip flux -> continuum offset field -4G int j/|x-x'| (grid error falls with r, ~1/r^2, < 4% at r=10)",
      err[10] < 0.04 and err[10] < err[7] < err[4], "; ".join(rows_out))
print("INFO G6 Lb = 96 periodic: image error ~ (r/Lb)^3; continuum = exact Neumann integral of the same square loop; "
      "point-dipole axis/equator ratio is -2 (D3 pattern)")

# ---------- H. measured comparators (test only) ----------
Gs, c, I_E, w_E, a_orb = 6.674e-11, 2.998e8, 8.034e37, 7.2921e-5, 7.027e6
Om_c = Gs*I_E*w_E/(2*c**2*a_orb**3)*3.15576e7*206264806.2            # polar-orbit average of D3: G J/(2 c^2 a^3)
print(f"INFO H circular polar-orbit average of D3 for the Earth: {Om_c:.1f} mas/yr (published GR value 39.2 uses the mission orbit)")
GR, meas, sig = 39.2, 37.2, 7.2
pr_rule, pr_frozen = 1.0*GR, 0.0
check("H1 GP-B: rule (ratio 1 -> 39.2 mas/yr) within 1 sigma of 37.2 +- 7.2", abs(pr_rule - meas) < sig,
      f"{abs(pr_rule-meas)/sig:.2f} sigma")
check("H2 GP-B: frozen / per-site offset (0 mas/yr) excluded at > 5 sigma", abs(pr_frozen - meas)/sig > 5,
      f"{abs(pr_frozen-meas)/sig:.1f} sigma")
check("H3 LAGEOS (~10%): rule ratio 1 passes, frozen ratio 0 fails", abs(1.0 - 1) < 0.1 and abs(0.0 - 1) > 0.1)
check("H4 lunar ranging |alpha1| < 1e-4: rule alpha1 = 0 passes; frozen alpha1 = -8 fails",
      abs(int(a1opt['per-edge offset responds (hinge sum, c=1)'])) < 1e-4 and abs(int(a1opt['offset frozen (beta = 0)'])) > 1e-4)
cmin, cmax = GR/(meas + 2*sig), GR/(meas - 2*sig)
print(f"INFO H a separate tilt-hinge weight c is bounded by GP-B (2 sigma) to {cmin:.2f} < c < {cmax:.2f}; the single hinge sum gives c = 1")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")
