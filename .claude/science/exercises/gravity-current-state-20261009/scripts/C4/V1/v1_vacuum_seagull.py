"""V1: O(lambda^2) vacuum energy of the dressed-flow coupling, split into its two pieces.

Coupling (exact):  H(h) = U_h(lam) H U_h(lam)^dag,  U_h(lam) = W U0_h W^dag,  W = exp(lam S),
  S = -(V40/sum w) + h.c.  (S|0> = |Omega_1>; [S,P] = P1^{40} = V40 sum f/sum w, the forced 0<->4 momentum correction).
Local coupling (rule R: drop only the explicit-position part of the >=2-in/>=2-out sectors of U0 Y U0^dag):
  H_loc(h) = W [E0 + H2(h) + Y_loc(h)] W^dag.
O(lam^2) vacuum energy around the strained free vacuum |0_h>:
  (i)  second order from the O(lam) vertex [S,H2(h)]:   -sum_n |<n|[S,H2(h)]|0_h>|^2/E_n = -sum_n E_n |S_n0|^2
  (ii) first order from the O(lam^2) seagull 1/2[S,[S,H2(h)]]:  +sum_n E_n |S_n0|^2   (f-sum identity)
  (iii) constant E2 (h-independent);  Y_loc annihilates |0_h> on both sides -> no contribution.
4-particle part (the 2-particle part of S|0_h> is O(eps) * int s(p) (cubic invariant) = 0 by the E/T2 symmetry, so O(eps^4)):
  sum_n E_n|S_n0|^2 = (1/24) int_{K=0} sum_l Omega(q_l) prod_l [alpha_l^2 c_l^2] / (sum_l w(q_l))^2
  alpha^2 = 1/(2w), beta^2 = J/(2 Omega), c = (alpha/beta + beta/alpha)/2  (Bogoliubov unstrained a -> strained b at fixed lab q).
Control: L2 design  E2 = -(1/24) int prod (J/2Omega)/sum Omega  ->  mu_E = -1.00931e-6, mu_T2 = +1.61082e-8 (m=1).
"""
import numpy as np, sys, time
sys.path.insert(0, '/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/W1')
from w1_core import strained, wdisp, onsite_I, tquad
m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
Ls = [int(a) for a in sys.argv[2].split(',')] if len(sys.argv) > 2 else [16, 24]
u, wu = np.polynomial.laguerre.laggauss(40)
def quad(smin, smax, power):
    best = None
    for beta in np.linspace(0.3*smin, 4*smin, 80):
        tn, wn = u/beta, wu*np.exp(u)/beta
        wq = wn*tn**(power-1)   # int t^{p-1} e^{-ts} dt = (p-1)!/s^p ; p=1,2
        s = np.linspace(smin, smax, 3001)
        err = np.max(np.abs((wq[None, :]*np.exp(-np.outer(s, tn))).sum(1)*s**power - 1))
        if best is None or err < best[0]: best = (err, tn, wq)
    return best
wmax = np.sqrt(m**2 + 12)
e1, tn1, wq1 = quad(3.9*m, 4.1*wmax, 1)
e2, tn2, wq2 = quad(3.9*m, 4.1*wmax, 2)
print(f'm={m}: t-quadrature max rel err 1/s: {e1:.1e}, 1/s^2: {e2:.1e}')
def pieces(L, eps, ch):
    k1 = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
    w = wdisp(KX, KY, KZ, m)
    J, Om = strained(L, m, eps, ch)
    a2 = 1/(2*w); b2 = J/(2*Om); c = 0.5*(np.sqrt(a2/b2) + np.sqrt(b2/a2))
    A = a2*c**2
    tot_ii = 0.0
    for t, wq in zip(tn2, wq2):
        e = np.exp(-t*w)
        g = np.fft.ifftn(A*e).real; hh = np.fft.ifftn(Om*A*e).real
        tot_ii += wq*4*np.sum(g**3*hh)
    # ifft carries 1/N per leg and sum_x gives N, so sum_x g^3 h = (1/N^3) sum_{K=0}: per-cell, as in W1 onsite_I
    return tot_ii/24.0
def l2_design(L, eps, ch):
    tn, wn = tquad(24, 9.0)
    return -onsite_I(L, m, eps, ch, tn, wn)/24.0
def hess(fun, d=0.04):
    I = {e: fun(e) for e in [-d, -d/2, 0, d/2, d]}
    D = lambda e: (I[e] + I[-e] - 2*I[0])/e**2
    return (4*D(d/2) - D(d))/3, I[0]
t0 = time.time()
for L in Ls:
    for ch in ['E', 'T2']:
        mu_l2, E0l2 = hess(lambda e: l2_design(L, e, ch))
        mu_ii, Eii = hess(lambda e: pieces(L, e, ch))
        print(f'L={L:2d} ch={ch:2s}: control L2-design E2={E0l2:.6e} mu={mu_l2:+.5e} | '
              f'piece(ii) seagull sum E_n|S_n0|^2 = {Eii:.6e} (=-E2 at eps=0), its Hessian mu_ii = {mu_ii:+.5e}; '
              f'piece(i) = -piece(ii): mu_i = {-mu_ii:+.5e}; total mu = mu_i + mu_ii + 0 = 0 (identity) [{time.time()-t0:.0f}s]')
        sys.stdout.flush()
# first-order (in eps) relative change of the 0->4 lab vertex vs the L2 design's (phi^4 in lab: prod beta):
# u_eff = [sum Om/sum w] prod_l (alpha_l c_l/beta_l) = [sum Om/sum w] prod_l (1 + Om_l/(J_l w_l))/2
