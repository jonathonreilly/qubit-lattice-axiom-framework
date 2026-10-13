"""R19-31 Wilson-fermion channel: strain dependence of the one-loop ADDITIVE mass of a Wilson-Dirac fermion (r = 1, bare m = 0)
on Z^3 x R with a U(1) photon (Feynman gauge), H-cov E_g strain l = (e^h, e^-h, 1). Per e^2. Lattice units.
Free inverse propagator S^-1(P) = i g0 p0 + i sum_j g_j sbar_j + M(p), sbar_j = sin p_j / l_j, M = sum_j (r/l_j)(1 - cos p_j) (law datum: Wilson
term metric-scaled per direction). Minimal coupling p_i -> p_i + l_i a_i gives V_i(p,p') = i g_i cos((p+p')_i/2) + r sin((p+p')_i/2),
tadpole T_i = (1/2) l_i^2 d^2 S^-1/dp_i^2, V_0 = -i g0. Sigma = tadpole - sum_Q V S V D. Mass part (1/4) tr Sigma(P=0):
  dm/e^2 = G_gam sum_i (r l_i/2) + sum_q [ M_q + sum_i (c_i^2 M_q - r^2 s_i^2 M_q - r sin^2 q_i / l_i) ] / (2 E_q Om_q (E_q + Om_q)),
  c_i = cos(q_i/2), s_i = sin(q_i/2), E_q^2 = sbar^2 + M_q^2.   Checks: r -> 0 gives 0 (chiral symmetry).
The thermal cross term of soft fermions is <psibar psi>_th x d2(dm)/dh2 (fixed per-site counterterm at h = 0; R19-27-type per-site
counterterms are invariant under traceless strain, so they cannot absorb it)."""
import numpy as np, time
t0 = time.time()
br = np.array([0, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.2, np.pi])
xg, wg = np.polynomial.legendre.leggauss(6)
nodes, wts = [], []
for a, b in zip(br[:-1], br[1:]):
    nodes += list(0.5*(b - a)*xg + 0.5*(b + a)); wts += list(0.5*(b - a)*wg)
nodes = np.array(nodes); wts = np.array(wts)
k1 = np.concatenate([-nodes[::-1], nodes]); w1 = np.concatenate([wts[::-1], wts])/(2*np.pi)
Q = np.meshgrid(k1, k1, k1, indexing='ij', sparse=True)
W = w1[:, None, None]*w1[None, :, None]*w1[None, None, :]
def avg(x): return float((W*x).sum())
def dm(h, r=1.0):
    l = (np.exp(h), np.exp(-h), 1.0)
    Om = np.sqrt(sum(4*np.sin(q/2)**2/l[i]**2 for i, q in enumerate(Q)))
    M = sum((r/l[i])*(1 - np.cos(q)) for i, q in enumerate(Q))
    E = np.sqrt(sum(np.sin(q)**2/l[i]**2 for i, q in enumerate(Q)) + M*M)
    Gg = avg(0.5/Om)
    num = M + sum(np.cos(q/2)**2*M - r*r*np.sin(q/2)**2*M - r*np.sin(q)**2/l[i] for i, q in enumerate(Q))
    return Gg*sum(r*li/2 for li in l) + avg(num/(2*E*Om*(E + Om))), Gg
d = 0.02
print('r=0 check (chiral): dm = %+.2e' % dm(0.0, 0.0)[0])
vals = {h: dm(h)[0] for h in (-2*d, -d, 0.0, d, 2*d)}
for h, v in vals.items(): print('  h=%+.3f  dm/e^2 = %+.9f' % (h, v))
h2 = (vals[d] - 2*vals[0.0] + vals[-d])/d**2; h2b = (vals[2*d] - 2*vals[0.0] + vals[-2*d])/(2*d)**2
print('d2(dm)/dh2 per e^2 (H-cov): %+.5e (step d), %+.5e (step 2d)' % (h2, h2b))
# thermal <psibar psi> per Dirac field (4 states): 4 <nF M/E>; soft massive (m_f) and massless-Wilson cases
def nF(e, T): return 1/(np.exp(e/T) + 1)
print('soft-fermion scalar density <psibar psi>_th = 4<nF M_p/E_p> (lattice units), and the cross term per e^2 = <psibar psi>_th * d2(dm)/dh2:')
for mf in (0.0, 0.01, 0.03):
    for T in (0.1, 0.05, 0.025):
        M = mf + sum((1 - np.cos(q)) for q in Q); E = np.sqrt(sum(np.sin(q)**2 for q in Q) + M*M)
        pp = 4*avg(nF(E, T)*M/E)
        print('  m_f=%.3f T=%.3f: <psibar psi>_th %.4e  (m_f T^2/6 = %.4e; massless-Wilson ~ T^4 scale %.3e)  cross %+.4e  cross/T^2 %+.4e  cross/T^4 %+.4e'
              % (mf, T, pp, mf*T*T/6, T**4, pp*h2, pp*h2/T**2, pp*h2/T**4), flush=True)
print('time %.0f s' % (time.time() - t0))
