"""R15-5 s2: what the N-type constraint algebra demands of a matter source (pre-registered before running).

With sources, the constraints read  G E = j  (vector)  and  S h = rho  (scalar).
Preservation under H_N + H_matter(h):
  d/dt(S h) = S dH/dE = J S K E.
Claim A (to check): S K = lambda(k) G exactly, with lambda(k) proportional to qhat (a lattice divergence),
  so d/dt(S h) = J lambda . (G E) = J lambda . j : the scalar source rho must obey rho_dot = J lambda.j,
  i.e. the vector-constraint source j must be (up to normalization) the CURRENT of the scalar source.
  If rho is matter energy density, j must be its energy current;  if j is matter momentum density,
  energy current = momentum density (T^{0i} = T^{i0}).
Claim B (to check): G R = 0 exactly, so d/dt(G E) = -g G R h - G dH_matter/dh = -(G T-coupling);
  the vector source must obey j_dot = -G T (a local stress current), i.e. j is locally conserved.
Claim C (free band, 1D illustration): for a band eps(k), the per-mode condition
  'momentum symbol p(k) = energy-current symbol eps*eps'(k)' and additivity of p in 2->2 scattering
  (p(k1)+p(k2) = p(k3)+p(k4) whenever k1+k2=k3+k4 mod 2pi and eps sums agree) is tested numerically
  for a cosine band and for a box-type band (exact sqrt(m^2+k^2) inside |k|<b).
"""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('s1', __file__.replace('s2_source_consistency.py', 's1_ntype_reduced.py'))
# import only ops() from s1 without re-running its prints: exec the top part
src = open(__file__.replace('s2_source_consistency.py', 's1_ntype_reduced.py')).read().split('J, g = 1.0, 1.0')[0]
ns = {}; exec(src, ns)
ops = ns['ops']; qhat = ns['qhat']

print("== Claims A, B on random momenta ==")
rng = np.random.default_rng(1)
worstA = worstB = worstL = 0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3)
    q, G, S, R, C, K = ops(k)
    # solve S K = lam G for lam (1x3) by least squares
    lam, res, rk, sv = np.linalg.lstsq(G.T, (S@K).T, rcond=None)
    worstA = max(worstA, np.abs(lam.T@G - S@K).max())
    worstB = max(worstB, np.abs(G@R).max())
    # compare lam with -q (or c*q)
    c = (lam.ravel()@q)/(q@q)
    worstL = max(worstL, np.abs(lam.ravel() - c*q).max())
print("max |S K - lam G| = %.2e ; max |lam - c qhat| = %.2e ; last c = %.6f ; max |G R| = %.2e" % (worstA, worstL, c, worstB))

print("\n== Claim C: per-mode momentum = energy current, and additivity in 2->2 scattering (1D) ==")
def bands(name, k, m=0.5, b=2.0):
    if name == 'cos':
        e = np.sqrt(m**2 + 2*(1 - np.cos(k)))
    elif name == 'box':   # exact relativistic inside |k|<b, smooth periodic outside (illustrative profile)
        kk = (k + np.pi) % (2*np.pi) - np.pi
        p = np.where(np.abs(kk) < b, kk, np.sign(kk)*(b + (np.pi - b)*np.sin(np.pi/2*(np.abs(kk)-b)/(np.pi-b))*0 ) )
        # smooth periodic odd p(k): equal to k on |k|<b, bends back to 0 at +-pi
        t = (np.abs(kk) - b)/(np.pi - b)
        p = np.where(np.abs(kk) < b, kk, np.sign(kk)*b*(1 - t**2*(3 - 2*t)))
        e = np.sqrt(m**2 + p**2)
    return e
for name in ['cos', 'box']:
    ks = np.linspace(-np.pi, np.pi, 4001)[:-1]
    e = bands(name, ks); de = np.gradient(e, ks)
    pE = e*de                       # energy-current symbol per particle (= d(eps^2/2)/dk)
    # additivity test: sample pairs (k1,k2) with total K, find (k3,k4) with same total energy
    rng = np.random.default_rng(2); viol = []; inbox = []
    f = lambda k: np.interp((k + np.pi) % (2*np.pi) - np.pi, ks, pE, period=2*np.pi)
    E = lambda k: bands(name, k)
    for _ in range(3000):
        k1, k2 = rng.uniform(-np.pi, np.pi, 2); Kt = k1 + k2; Et = E(k1) + E(k2)
        # solve E(x)+E(Kt-x)=Et for x != k1,k2 by scanning
        xs = np.linspace(-np.pi, np.pi, 2001); F = E(xs) + E(Kt - xs) - Et
        idx = np.where(np.sign(F[:-1]) != np.sign(F[1:]))[0]
        for i in idx:
            x = xs[i] - F[i]*(xs[i+1]-xs[i])/(F[i+1]-F[i])
            if min(abs(((x-k1+np.pi)%(2*np.pi))-np.pi), abs(((x-k2+np.pi)%(2*np.pi))-np.pi)) < 1e-2: continue
            v = abs(f(k1) + f(k2) - f(x) - f(Kt - x))
            viol.append(v)
            w = lambda y: abs((y + np.pi) % (2*np.pi) - np.pi)
            inbox.append(max(w(k1), w(k2), w(x), w(Kt-x)) < 2.0 and abs((Kt+np.pi)%(2*np.pi)-np.pi) < 2.0 and name=='box')
    viol = np.array(viol); inbox = np.array(inbox, bool)
    msg = "%-4s band: %d nontrivial 2->2 events; max |Delta p_E| = %.3e; median = %.3e" % (name, len(viol), viol.max(), np.median(viol))
    if name == 'box' and inbox.any():
        msg += "; events with all momenta and total inside the box: %d, max |Delta p_E| there = %.2e" % (inbox.sum(), viol[inbox].max())
    print(msg)
