"""R9-6, script 3b (integrator-floor check, ball packet only, dt halved):
R9-6, script 3: finite ROTATIONS on the lattice box law (cube vs inscribed ball), and the boost budgets.

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
    dt = dt or 0.75/(JMAX*L/2)
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
thetas = [np.pi/2, np.pi]
for lab, c0, s0 in [('ball (inscribed disc): k0 = (1.5, 0.8), |k0| = 1.70', (1.5, 0.8), 0.10),
                    ][:1]:
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
           % (th, leak, bnd, 'OK' if leak <= bnd + 1e-9 else 'VIOLATED', Elat, E0, Econt))

with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
