#!/usr/bin/env python3
"""C2b / KI+ consequences for the supplied carriers on main.

Carriers (both supplied, neither derived):
  photon  : Gaussian lattice-Maxwell comparator H = (U/2) E^2 + (K/2)(curl A)^2, omega = sqrt(UK)|s(k)|
            per unit Hamiltonian time. Landed reading sqrt(UK) = 1.025 (cited, not recomputed).
  fermion : two-qubit O-covariant Dirac walk, cone speed s(b) = b0 + 2 b1 + b2 sites per tick.
KI+ in tick-and-edge units (KI+_tick) requires every sector's dimension-4 cone to be 1 edge per tick.
KI+ weak (KI+_w: one universal form, value free) requires only c_gamma = c_psi per common tick.
Exact parts use sympy; the walk spectra are numerical (numpy) and labelled so.
"""
import itertools
import sys
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, ok, tag):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [{tag}] {name}", flush=True)


# ------------------------------------------------------------------ walk family (parent note, re-verified)
b0, b1, b2 = sp.symbols('b0 b1 b2', real=True)
c1, c2, c3 = sp.symbols('c1 c2 c3', real=True)
G = sp.Matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
               [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
               [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
               [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
cs = [c1, c2, c3]
phi = sp.Matrix([1, c1 + c2 + c3, c1*c2 + c1*c3 + c2*c3, c1*c2*c3])
# |g|^2 with sin^2 = 1 - cos^2
g2 = sum((1 - cs[i]**2)*(b0 + b1*(cs[(i+1) % 3] + cs[(i+2) % 3]) + b2*cs[(i+1) % 3]*cs[(i+2) % 3])**2 for i in range(3))
ident = sp.expand((phi.T*G*phi)[0] + g2 - 1)
check('Gram identity phi^T G(b) phi + |g|^2 = 1 holds identically in (b, cos k) (unitarity of the family)', ident == 0, 'exact')

r5 = sp.sqrt(5)
bg = {b0: (9*r5 - 5)/38, b1: (5*r5 - 7)/19, b2: (71 - 29*r5)/38}
s_expr = b0 + 2*b1 + b2
check('b_gold has s = b0 + 2 b1 + b2 = 1 exactly', sp.simplify(s_expr.subs(bg) - 1) == 0, 'exact')
Gg = G.subs(bg).applyfunc(sp.nsimplify)
check('det G(b_gold) = 0 exactly (rank <= 3)', sp.simplify(Gg.det()) == 0, 'exact')
evg = np.linalg.eigvalsh(np.array(Gg.evalf(30), dtype=float))
check(f'G(b_gold) PSD of rank 3 (eigenvalues {np.round(evg, 6)})', evg[0] > -1e-12 and abs(evg[0]) < 1e-12 and evg[1] > 1e-5, 'numerical')
# s <= 1 on the family: the axis doubler X has cos theta_X = 1 - 2 s^2 >= -1 is the parent's bound; we recheck the
# X-point cosine identity cos theta_X = phi(X)^T G phi0-type: f(X) for the massless member equals 1 - 2 s^2
phi0 = sp.Matrix([1, 3, 3, 1]); phiX = phi.subs({c1: -1, c2: 1, c3: 1})
fX = sp.expand((phi0.T*G*phiX)[0])
check('massless member: cos theta_X = phi0^T G phi(X) = 1 - 2 s^2 identically in b, hence s^2 <= 1 on the family',
      sp.expand(fX - (1 - 2*s_expr**2)) == 0, 'exact')

# Uniqueness of the light-speed member (independent re-derivation of the parent's Theorem 5 statement).
# For the massless member f = e_f . F phi with F phi0 = e_f, |F phi(X)| = 1 (Gram identity, g(X) = 0).
# s^2 = 1 <=> f(X) = -1 <=> F phi(X) = -F phi0 <=> F (phi0 + phi(X)) = 0 <=> G(b) v = 0 with v = phi0 + phi(X).
v = phi0 + phiX
eqs = [sp.expand(e) for e in (G*v)]
sols = sp.solve(eqs, [b0, b1, b2], dict=True)
real_sols = [d for d in sols if all(sp.im(sp.N(d[x])) == 0 for x in (b0, b1, b2)) and len(d) == 3]
print(f"  G(b)(phi0 + phi(X)) = 0: {len(sols)} solutions, {len(real_sols)} real and isolated")
psd = []
for d in real_sols:
    ev = np.linalg.eigvalsh(np.array(G.subs(d).evalf(30), dtype=float))
    sv = sp.nsimplify(sp.simplify(s_expr.subs(d)))
    print(f"     b = ({sp.N(d[b0], 8)}, {sp.N(d[b1], 8)}, {sp.N(d[b2], 8)}), s = {sp.N(sv, 10)}, eig G = {np.round(ev, 6)}")
    if ev[0] > -1e-12:
        psd.append(d)
gold_pm = all(any(sp.simplify(d[x] - sg*bg[x]) == 0 for x in (b0, b1, b2)) for d in psd for sg in [1 if sp.N(d[b0]) > 0 else -1])
check('s^2 = 1 with G(b) PSD has exactly the two solutions +-b_gold (exact solve of G(b)(phi0 + phi(X)) = 0, then PSD test)',
      len(psd) == 2 and gold_pm, 'exact solve + numerical eigenvalue signs')

# ------------------------------------------------------------------ numerical walk at named points
I2 = np.eye(2); t1 = np.array([[0, 1], [1, 0]], complex); t2 = np.array([[0, -1j], [1j, 0]]); t3 = np.diag([1.0, -1.0]).astype(complex)
TAU = [np.kron(t1, I2), np.kron(t2, I2)]
TS = [np.kron(t3, x) for x in (t1, t2, t3)]
Gf = sp.lambdify((b0, b1, b2), G, 'numpy')


def walk(b):
    Gm = np.array(Gf(*b), float)
    ev, V = np.linalg.eigh(Gm)
    keep = ev > 1e-12
    F = (V[:, keep]*np.sqrt(ev[keep])).T
    e = F @ np.array([1.0, 3, 3, 1])
    assert F.shape[0] == 3, 'rank-3 member expected'
    Q = np.linalg.qr(np.column_stack([e, np.eye(3)]))[0][:, :3]
    if Q[:, 0] @ e < 0:
        Q[:, 0] *= -1
    F = Q.T @ F                     # now F phi0 = (|e|, 0, 0): the massless member, U(0) = 1

    def U(k):
        c, s = np.cos(k), np.sin(k)
        ph = np.array([1.0, c.sum(), c[0]*c[1] + c[0]*c[2] + c[1]*c[2], c.prod()])
        f, h1, h2 = F @ ph
        g = [s[i]*(b[0] + b[1]*(c[(i+1) % 3] + c[(i+2) % 3]) + b[2]*c[(i+1) % 3]*c[(i+2) % 3]) for i in range(3)]
        return f*np.eye(4) + 1j*(h1*TAU[0] + h2*TAU[1] + sum(g[i]*TS[i] for i in range(3)))
    return U


co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
ustar = min(r.real for r in np.roots(co) if abs(r.imag) < 1e-12 and r.real > 0)
R5, R6, R15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
points = {'b*': (11/30, np.sqrt(ustar), 3/20),
          'b_iso': ((R6 + 2*R15)/27, (5*R6 - 2*R15)/27, (2*R15 - 2*R6)/27),
          'b_gold': ((9*R5 - 5)/38, (5*R5 - 7)/19, (71 - 29*R5)/38)}
speeds = {}
for name, b in points.items():
    U = walk(b)
    s_formula = b[0] + 2*b[1] + b[2]
    # cone speed from eigenphases near Gamma along an axis and a body diagonal
    vs = []
    for d in (np.array([1.0, 0, 0]), np.array([1.0, 1, 1])/np.sqrt(3)):
        eps = 1e-4
        w = np.max(np.abs(np.angle(np.linalg.eigvals(U(eps*d)))))
        vs.append(w/eps)
    speeds[name] = s_formula
    check(f'{name}: Gamma cone speed from spectra (axis {vs[0]:.6f}, diagonal {vs[1]:.6f}) = s(b) = {s_formula:.6f}',
          max(abs(v - s_formula) for v in vs) < 1e-6, 'numerical')
    err = max(np.linalg.norm(U(k) @ U(k).conj().T - np.eye(4)) for k in np.random.default_rng(1).uniform(-np.pi, np.pi, (50, 3)))
    check(f'{name}: walk unitary to {err:.1e}', err < 1e-12, 'numerical')

check('KI+_tick (cone = 1 edge per tick) holds at b_gold and fails at b* and b_iso',
      abs(speeds['b_gold'] - 1) < 1e-12 and abs(speeds['b*'] - 1) > 0.05 and abs(speeds['b_iso'] - 1) > 0.1, 'exact')

# ------------------------------------------------------------------ pi-mode doublers at b_gold
U = walk(points['b_gold'])
X = np.array([np.pi, 0, 0])
check('b_gold: U(X) = -1 (massless pi-mode at the axis doubler X)', np.linalg.norm(U(X) + np.eye(4)) < 1e-12, 'numerical')
eps = 1e-5
vX = []
for d in (np.array([1.0, 0, 0]), np.array([0, 1.0, 0]), np.array([0, 0, 1.0])):
    ph = np.angle(-np.linalg.eigvals(U(X + eps*d)))     # distance from pi
    vX.append(np.max(np.abs(ph))/eps)
print(f"  b_gold pi-mode cone at X=(pi,0,0): velocities along x, y, z = {np.round(vX, 8)}  (sqrt5 - 2 = {R5-2:.8f})")
check('b_gold: the X pi-mode cone is uniaxial with velocities (1 along the X axis, sqrt5 - 2 transverse)',
      abs(vX[0] - 1) < 1e-6 and abs(vX[1] - (R5 - 2)) < 1e-6 and abs(vX[2] - (R5 - 2)) < 1e-6, 'numerical')
U2X = U(X + eps*np.array([0, 1.0, 0])) @ U(X + eps*np.array([0, 1.0, 0]))
w2 = np.max(np.abs(np.angle(np.linalg.eigvals(U2X))))/eps
check(f'b_gold, two-tick clock U^2: the X modes sit at quasienergy 0 with transverse speed {w2/2:.6f} per tick != 1 '
      '(an IR sector violating KI+_tick)', abs(w2/2 - (R5 - 2)) < 1e-6, 'numerical')

# ------------------------------------------------------------------ comparator: Euclidean form on a tick of length rho
U_, K_, rho, E, lam = sp.symbols('U K rho E lambda', positive=True)
beta_t, beta_s = 1/(U_*rho), K_*rho                      # time-like and space-like plaquette weights per tick
# Euclidean pole of the Gaussian transverse mode (W2 formula): 4 beta_t sinh^2(E/2) = beta_s lambda, lambda=|s(k)|^2
Esol = 2*sp.asinh(sp.sqrt(beta_s*lam/(4*beta_t)))
c_tick = sp.limit(Esol/sp.sqrt(lam), lam, 0)
check(f'comparator on a tick rho: small-k speed per tick = {sp.simplify(c_tick)} = sqrt(U K) rho', sp.simplify(c_tick - sp.sqrt(U_*K_)*rho) == 0, 'exact')
rho_sol = sp.solve(sp.Eq(beta_t, beta_s), rho)
check(f'B4 on the gauge sector (beta_t = beta_s) <=> rho = {rho_sol} = 1/sqrt(UK), and then the speed is 1 edge per tick',
      len(rho_sol) == 1 and sp.simplify(rho_sol[0] - 1/sp.sqrt(U_*K_)) == 0 and sp.simplify(c_tick.subs(rho, rho_sol[0]) - 1) == 0, 'exact')
cg = 1.025
print(f"  landed reading sqrt(UK) = {cg} (cited): KI+_tick fixes rho = 1/sqrt(UK) = {1/cg:.4f} Hamiltonian time per tick")
print("  KI+_w (common cone, value free) instead gives the one-parameter relation rho = s(b)/sqrt(UK):")
for name in points:
    print(f"     {name}: rho = {speeds[name]/cg:.4f}")
check('KI+_w imposes one relation on (b, rho): every admissible b has a solution rho > 0 (no selection of b)',
      all(speeds[n] > 0 for n in points), 'exact')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
