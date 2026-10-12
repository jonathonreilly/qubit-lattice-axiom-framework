"""R9-6, script 3: finite ROTATIONS on the lattice box law (cube vs inscribed ball), and the boost budgets.

Lattice rotation generator (R7-1): J0_a = dGamma( (1/2) eps_abc {X_b, j_c} ), j_c = s(k_c) s'(k_c), X = i d/dk
(= site position).  Since d_b j_c(k_c) = 0 for b != c, J0_n psi = i (n . (j x grad))... i.e.
   d psi/d theta = -i J0_n psi = (u . grad) psi,  u = j(k) x n,
a divergence-free field; u = k x n exactly where |k_c| <= B for the components that enter (the cube).
u is the Hamiltonian field of G = sum_a s(k_a)^2 / 2 = (eps~^2 - m^2)/2, so [J0_n, H0] = 0 on the WHOLE torus.

(A) z-axis, direct lattice operator: 2D (k_x, k_y) slice (k_z is a spectator for z-rotations), L x L torus, X by FFT
    (site positions), RK4 in theta.  Compare with the continuum rotation psi(R(-theta) k).  Packets: inside the
    inscribed disc (ball) and in a corner of the square (cube).  Bound: 2 ||1_E psi||, E = initial points whose
    continuum orbit over [0, theta] leaves the open square.  Also: <eps~> is conserved by the lattice flow.
(B) generic axis in d = 3, by characteristics of the lattice field u (transport is what a symmetric first-order
    operator with smooth real divergence-free coefficients generates): cube corner vs ball packet, same bound.
(C) boost and rotation budgets: cube (axis / face / body diagonal) vs ball.
"""
import numpy as np, time
from r81_common import sstep, wrap, BoxLaw

m, B, B2 = 0.5, 2.6, 3.0
law = BoxLaw(m, B=B, B2=B2)
def jfun(k):                      # j = s s'
    h = 1e-6
    return law.s(k)*(law.s(k + h) - law.s(k - h))/(2*h)
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

# ---------------- (A) z-axis, lattice operator in 2D ----------------
L = 256
g = wrap(2*np.pi*np.arange(L)/L)
KX, KY = np.meshgrid(g, g, indexing='ij')
x = np.fft.fftfreq(L, d=1.0/L)                    # site positions (centred)
jx, jy = jfun(KX), jfun(KY)
pr('(A) max |j - k| on the square |k_a| <= B: %.1e ; max |j| on the torus: %.2f' %
   (np.abs(np.where((np.abs(KX) <= B), jx - KX, 0)).max(), max(np.abs(jx).max(), np.abs(jy).max())))
def dk(f, ax):                                    # d/dk = -i X with X the site position (trig. interpolant)
    sh = (-1, 1) if ax == 0 else (1, -1)
    return np.fft.ifft(1j*x.reshape(sh)*np.fft.fft(f, axis=ax), axis=ax)
JMAX = max(np.abs(jx).max(), np.abs(jy).max())
def rhs(f):                                        # u = j x z = (j_y, -j_x)
    return jy*dk(f, 0) - jx*dk(f, 1)
def evolve(f0, thetas, dt=None):
    dt = dt or 1.5/(JMAX*L/2)
    f = f0.astype(complex); t = 0.0; res = {}
    for th in thetas:
        while t < th - 1e-12:
            h = min(dt, th - t)
            k1 = rhs(f); k2 = rhs(f + 0.5*h*k1); k3 = rhs(f + 0.5*h*k2); k4 = rhs(f + h*k3)
            f = f + (h/6)*(k1 + 2*k2 + 2*k3 + k4); t += h
        res[th] = f.copy()
    return res
def gauss2(kx, ky, c, s):
    return np.exp(-((kx - c[0])**2 + (ky - c[1])**2)/(4*s*s))
def exit_set(theta, nt=721):
    """initial points whose continuum orbit R(t) k, t in [0, theta], leaves the open square |k_a| < B."""
    bad = np.zeros_like(KX, bool)
    for t in np.linspace(0, theta, nt):
        c, s = np.cos(t), np.sin(t)
        bad |= (np.abs(c*KX - s*KY) >= B) | (np.abs(s*KX + c*KY) >= B)
    return bad
eps_t = law.eps(KX, KY)
for lab, c0, s0, thetas in [('ball (inscribed disc): k0 = (1.5, 0.8), |k0| = 1.70', (1.5, 0.8), 0.10, [np.pi/2, np.pi, 2*np.pi]),
                    ('cube corner: k0 = (1.95, 1.95), |k0| = 2.76 > B', (1.95, 1.95), 0.10, [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4])]:
    t0 = time.time()
    f0 = gauss2(KX, KY, c0, s0); nrm = np.linalg.norm(f0); f0 = f0/nrm
    res = evolve(f0, thetas)
    pr('(A) %s, sigma_k = %.2f, L = %d   [%.0fs]' % (lab, s0, L, time.time() - t0))
    E0 = np.sum(eps_t*np.abs(f0)**2)
    for th in thetas:
        c, s = np.cos(th), np.sin(th)
        fc = gauss2(c*KX + s*KY, -s*KX + c*KY, c0, s0)/nrm      # psi(R(-theta) k)
        leak = np.linalg.norm(res[th] - fc)
        bnd = 2*np.linalg.norm(f0[exit_set(th)])
        Elat = np.sum(eps_t*np.abs(res[th])**2); Econt = np.sum(eps_t*np.abs(fc)**2)
        pr('    theta = %6.4f : ||U_lat - U_rot|| psi = %.2e   bound 2||1_E psi|| = %.2e  %s   <eps~>: lattice %.10f (t=0: %.10f), continuum-rotated %.6f'
           % (th, leak, bnd, 'OK' if leak <= bnd + 1e-8 else 'VIOLATED (above 1e-8 floor)', Elat, E0, Econt))

# ---------------- (B) generic axis in d = 3 by characteristics ----------------
def ufield(k, n):                                  # u = j(k) x n
    j = jfun(k)
    return np.cross(j, n)
def flow(k, theta, n, nst=160):
    h = theta/nst
    for _ in range(nst):
        a1 = ufield(k, n); a2 = ufield(k + 0.5*h*a1, n); a3 = ufield(k + 0.5*h*a2, n); a4 = ufield(k + h*a3, n)
        k = k + (h/6)*(a1 + 2*a2 + 2*a3 + a4)
    return k
def rot(k, theta, n):                              # R_n(theta) k (Rodrigues)
    c, s = np.cos(theta), np.sin(theta)
    return k*c + np.cross(n, k)*s + np.outer(k @ n, n)*(1 - c)
NG, H = 40, 0.04
Gfun = lambda k: 0.5*(law.s(k)**2).sum(-1)                  # conserved by the lattice flow (all of T^3)
off = (np.arange(NG) - (NG - 1)/2)*H
G3 = np.stack(np.meshgrid(off, off, off, indexing='ij'), -1).reshape(-1, 3)
for nlab, n, lab, c0, s0, ths in [
        ('z', np.array([0.0, 0.0, 1.0]), 'ball: k0 = (1.5, 0.8, 0.3), |k0| = 1.73', np.array([1.5, 0.8, 0.3]), 0.08, [np.pi/4, np.pi/2, np.pi]),
        ('z', np.array([0.0, 0.0, 1.0]), 'cube corner: k0 = (1.95, 1.95, 0.3), k_xy = 2.76 > B', np.array([1.95, 1.95, 0.3]), 0.08, [0.1, 0.2, 0.3, 0.4]),
        ('(1,2,2)/3', np.array([1.0, 2.0, 2.0])/3.0, 'ball: k0 = (1.2, -0.9, 0.7), |k0| = 1.65', np.array([1.2, -0.9, 0.7]), 0.08, [np.pi/4, np.pi/2, np.pi]),
        ('(1,2,2)/3', np.array([1.0, 2.0, 2.0])/3.0, 'cube corner: k0 = (2.0, 2.0, -1.9), |k0| = 3.42 > B', np.array([2.0, 2.0, -1.9]), 0.08, [0.1, 0.2, 0.3, 0.4])]:
    K = c0[None, :] + G3
    psi = lambda k: np.exp(-((k - c0)**2).sum(-1)/(4*s0*s0))
    w0 = psi(K); nrm = np.sqrt((w0**2).sum())
    pr('(B) axis n = %s, %s, sigma = %.2f (grid %d^3, h = %.2f)' % (nlab, lab, s0, NG, H))
    for th in ths:
        # psi_lat(theta)(k) = psi(Phi_theta(k)) (flow of u for time theta); continuum: psi(R(-theta) k)
        # evaluate both at the rotated grid points k = R(theta) K (where the continuum packet sits)
        Kt = rot(K, th, n)
        FK = flow(Kt.copy(), th, n); lat = psi(FK); cont = psi(rot(Kt, -th, n))
        rel = psi(K) > 1e-6*psi(K).max()        # points carrying the packet (initial grid ~ rotated grid)
        dG = np.abs(Gfun(FK) - Gfun(Kt))[rel].max()
        leak_r2 = ((lat - cont)**2).sum()/nrm**2                       # on the rotated grid (where psi_cont lives)
        # lattice mass that landed OFF the rotated grid: psi_lat lives at Phi_{-theta}(K) (volume-preserving flow)
        Kb = flow(K.copy(), -th, n)
        offg = (np.abs(rot(Kb, -th, n) - c0[None, :]) > (NG/2)*H).any(1)
        extra = (w0[offg]**2).sum()/nrm**2
        leak = np.sqrt(leak_r2 + extra)
        # exit set on initial points: orbit R(t) K, t in [0, th], leaves the open cube
        bad = np.zeros(len(K), bool)
        for t in np.linspace(0, th, 361):
            bad |= (np.abs(rot(K, t, n)) >= B).any(1)
        bnd = 2*np.sqrt((w0[bad]**2).sum())/nrm
        pr('    theta = %6.4f : leakage %.2e (on-grid part %.1e, off-grid lattice mass %.1e)   bound 2||1_E psi|| = %.2e  %s   [max |G(Phi k) - G(k)| = %.1e, integrator check on the packet]'
           % (th, leak, np.sqrt(leak_r2), np.sqrt(extra), bnd, 'OK' if leak <= bnd + 1e-8 else 'VIOLATED (above 1e-8 floor)', dG))

# ---------------- (C) budgets ----------------
pr('(C) boost budget for a particle at rest, eta* = asinh(B_dir/m): B = %.2f, m = %.2f' % (B, m))
for lab, nn in [('cube, axis', [1, 0, 0]), ('cube, face diagonal', [1, 1, 0]), ('cube, body diagonal', [1, 1, 1])]:
    nn = np.array(nn, float)/np.linalg.norm(nn); bd = B/np.abs(nn).max()
    pr('    %-22s eta* = %.4f  (edge distance %.4f)' % (lab, np.arcsinh(bd/m), bd))
pr('    %-22s eta* = %.4f  (every direction)' % ('ball', np.arcsinh(B/m)))
mP, BP = 0.938/1.22e19, 2.0
pr('    Planck reading (R7-1: b = 2.0/l_P), proton at rest: cube axis %.2f, body diagonal %.2f (diff ln sqrt3 = %.3f); ball %.2f'
   % (np.arcsinh(BP/mP), np.arcsinh(np.sqrt(3)*BP/mP), np.log(np.sqrt(3)), np.arcsinh(BP/mP)))
pr('(C) rotation budget about z for a point at (k_x, k_y): unlimited iff k_x^2 + k_y^2 < B^2; corner k0 = (1.95, 1.95): '
   'first exit at theta* = %.4f rad (centre)' % (np.arcsin(B/np.hypot(1.95, 1.95)) - np.pi/4))
with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
