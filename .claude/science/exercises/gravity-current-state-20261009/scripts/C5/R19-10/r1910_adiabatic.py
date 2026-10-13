"""R19-10 probes (b)-(c): ramped ("adiabatic") insertion of a plane of sites into a 3D NN scalar lattice.
Lattice units a = c = hbar = 1.  Exact Gaussian dynamics.
Setting: torus, plane insertion Lx -> Lx+1 at x0.  Transverse momentum k_perp is conserved; with
s = cos ky + cos kz each sector is a 1D ring (antiperiodic in x, twist placed far from the insertion) with
  K(g) = (1-g) K_A + g K_B,
  K_A: old ring (bond (x0-1, x0) present) + new site decoupled with K_nn = m^2 + 6 (its site-local ground state:
       the best product state P-loc, so the ramp starts from exactly the P-loc state of r1910_insert_product),
  K_B: new ring of Lx+1 sites (the final perfect lattice), K_nn = m^2 + 6 - 2s.
The in-plane bonds of the new plane and its x-bonds ramp together with g; the old bond fades as 1-g.
Ramp g(t) = smoothstep (C-infinity) over duration T.  Initial state = ground state of K_A.
Per inserted site = integral over s with the square-lattice density of states rho(s) = K(m = 1 - s^2/4)/pi^2
(RECALLED formula, checked here: normalisation and second moment).
Measured per inserted site:
  eps_inf(T) = <H_B> - E0(K_B) after the ramp (net excitation left behind);
  A_fix(T)   = int_0^T [<H_B>_psi(t) - E0(K_B)] dt   (energy above the final ground state, final law H_B);
  A_law(T)   = int_0^T [<H(g(t))>_psi(t) - E0(K_B)] dt (energy of the time-dependent law above the final ground
               state, the new site counted from t = 0);  delta(g) = E0(K(g)) - E0(K_B) is its static part.
Propagation: exact for piecewise-constant K at step midpoints (dt = 0.05).
"""
import numpy as np, time
from scipy.special import ellipk
T0 = time.time()
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

def sstep(x):
    x = np.clip(x, 0, 1)
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    e1 = np.exp(-1/x); e2 = np.exp(-1/(1-x)); return e1/(e1+e2)

def rho2d(s): return ellipk(1 - s*s/4)/np.pi**2

# s-quadrature: [0,2] with s = 2 - 2 v^2 (dense near the gapless edge s = 2), [-2,0] plain Gauss-Legendre
xv, wv = np.polynomial.legendre.leggauss(20); v = 0.5*(xv+1); wv = 0.5*wv
s_hi = 2 - 2*v**2; w_hi = wv*4*v*rho2d(s_hi)
xs, ws = np.polynomial.legendre.leggauss(10); s_lo = -1 + xs; w_lo = ws*rho2d(s_lo)
S_nodes = np.concatenate([s_hi, s_lo]); S_w = np.concatenate([w_hi, w_lo])
pr('s-quadrature check: sum w = %.5f (1), sum w s^2 = %.5f (1), sum w s^4 = %.5f (exact 9/4 = 2.25)'
   % (S_w.sum(), (S_w*S_nodes**2).sum(), (S_w*S_nodes**4).sum()))

def build(N, m, s):
    """K_A, K_B on N+1 indices: old ring sites 0..N-1, new site index N between N-1 and 0. AP twist at N/2."""
    n = N + 1
    diag_old = m*m + 6 - 2*s
    KA = np.zeros((n, n)); KB = np.zeros((n, n))
    for i in range(N):
        KA[i, i] = diag_old; KB[i, i] = diag_old
    KA[N, N] = m*m + 6; KB[N, N] = m*m + 6 - 2*s
    tw = N//2
    for i in range(N-1):            # old bonds i,i+1 (twist on bond tw-1,tw)
        sg = -1.0 if i == tw-1 else 1.0
        KA[i, i+1] = KA[i+1, i] = -sg; KB[i, i+1] = KB[i+1, i] = -sg
    KA[N-1, 0] = KA[0, N-1] = -1.0                       # old closing bond (faded out)
    KB[N-1, N] = KB[N, N-1] = -1.0; KB[N, 0] = KB[0, N] = -1.0
    return KA, KB

def run(N, m, s, T, dt=0.05, nsamp=40):
    KA, KB = build(N, m, s)
    wA, OA = np.linalg.eigh(KA); omA = np.sqrt(wA)
    U = OA/np.sqrt(2*omA); Ud = -1j*OA*np.sqrt(omA/2)
    wB = np.linalg.eigvalsh(KB); E0B = 0.5*np.sqrt(wB).sum()
    def energies(U, Ud, K, E0K):
        Phi = np.real(U @ U.conj().T); Pi = np.real(Ud @ Ud.conj().T)
        EK = 0.5*np.trace(Pi) + 0.5*np.trace(K @ Phi)
        EB = 0.5*np.trace(Pi) + 0.5*np.trace(KB @ Phi)
        return EK - E0B, EB - E0B, E0K - E0B
    nst = max(1, int(round(T/dt))); h = T/nst
    A_law = 0.0; A_fix = 0.0; delta_int = 0.0
    e_law_prev, e_fix_prev, d_prev = energies(U, Ud, KA, 0.5*omA.sum())
    for j in range(nst):
        g = sstep((j + 0.5)/nst)
        K = (1-g)*KA + g*KB
        w, V = np.linalg.eigh(K); om = np.sqrt(w)
        a = V.T @ U; b = V.T @ Ud
        c = np.cos(om*h)[:, None]; sn = np.sin(om*h)[:, None]
        a2 = c*a + (sn/om[:, None])*b; b2 = -(om[:, None]*sn)*a + c*b
        U = V @ a2; Ud = V @ b2
        # trapezoid on the energy integrals (evaluate with the step's K as the law at this time)
        e_law, e_fix, d = energies(U, Ud, K, 0.5*om.sum())
        A_law += 0.5*h*(e_law + e_law_prev); A_fix += 0.5*h*(e_fix + e_fix_prev); delta_int += 0.5*h*(d + d_prev)
        e_law_prev, e_fix_prev, d_prev = e_law, e_fix, d
    _, eps_inf, _ = energies(U, Ud, KB, E0B)
    return eps_inf, A_fix, A_law, delta_int

def static_curve(N, m, s, gs):
    KA, KB = build(N, m, s); E0B = 0.5*np.sqrt(np.linalg.eigvalsh(KB)).sum()
    return [0.5*np.sqrt(np.linalg.eigvalsh((1-g)*KA + g*KB)).sum() - E0B for g in gs]

# static delta(g) per inserted site (sector-integrated)
gs = [0.0, 0.25, 0.5, 0.75, 1.0]
for m in (0.0, 1.0):
    N = 64
    dg = np.zeros(len(gs))
    for s, w in zip(S_nodes, S_w):
        dg += w*np.array(static_curve(N, m, s, gs))
    pr('static delta(g) = E0(K(g)) - E0(K_B) per inserted site, m=%.1f: ' % m +
       ', '.join('g=%.2f: %+.5f' % (g, d) for g, d in zip(gs, dg)))
    pr('   (delta(0) = E0(old) + site-local zero point - E0(new); for comparison e0 = %.5f per site)' % (1.193801 if m == 0 else 1.300034))

Ts = [1, 2, 4, 8, 16, 32]
Ts_extra = {0.0: [64]}
for m in (0.0, 0.3, 1.0):
    pr('=== m = %.1f: ramped plane insertion, per inserted site ===' % m)
    for T in Ts + Ts_extra.get(m, []):
        N = int(2*T + 48); N += N % 2
        tot = np.zeros(4)
        for s, w in zip(S_nodes, S_w):
            tot += w*np.array(run(N, m, s, T))
        pr('  T=%3d N=%3d: eps_inf = %.4e ; A_fix = %.4e ; A_law = %+.4e ; int delta dt = %+.4e ; [%.0fs]'
           % (T, N, tot[0], tot[1], tot[2], tot[3], time.time()-T0))
pr('elapsed %.1f s' % (time.time() - T0))
