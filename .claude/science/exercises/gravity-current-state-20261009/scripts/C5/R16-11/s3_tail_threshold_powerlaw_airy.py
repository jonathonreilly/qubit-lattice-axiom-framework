"""R16-11 s3 (written before running).  Is the tail hypothesis needed?  A family of EXACTLY vector-invariant,
qubit-compatible hops with power-law range: planar Airy L x L squares (s1 (B)) in all three planes, weight
w_L = L^{-p} per site per plane, L = 2..Lmax.  Per-site energy norm sum_L L^{-p} is finite for p > 1.
f-sum per site (unit <T+T^dag>):  m1(k) = sum_planes sum_L L^{-p} |phihat_L|^2 |t^T eps t|^2,
 c.mhat = -phihat_L(k_a,k_b) (t^T eps t),  t = (-qhat_b, qhat_a) in the plane, phihat = D_L(k_a) D_L(k_b),
 |D_L(kappa)|^2 = sin^2(kappa L/2)/sin^2(kappa/2)   (formula checked against s1's explicit patterns first).
Pre-registered expectations:
 (T1) slope of m1(k) = min(4, p-1) for 1 < p < 5 (log at p = 5) -> p = 3 gives m1 ~ k^2 (an EH-like f-sum
      power from an exactly law-conserving, compact, qubit-compatible, but power-law-ranged H).
 (T2) p >= 6: slope 4 (Theorem B regime).  Support-moment sum K2 converges only for p > 11 (L^2 multiplicity x L^8);
      the pattern bound (B2) for p > 7; actual k^4 already for p > 5.  Sufficient conditions are not sharp.
 (T3) Gaussian comparator: harmonic TT stiffness K_TT = m1 -> with electric energy (J/2)E^2,
      omega^2 = J m1 ~ k^{p-1}: z = (p-1)/2 = 1 at p = 3.  The transverse-trace (scalar) channel gets a
      POSITIVE stiffness of the same order (no conformal-sign attraction).
"""
import numpy as np, itertools, importlib.util, sys, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('s1', os.path.join(here, 's1_gauge_strains_and_patterns.py'))
# --- formula check against explicit patterns (re-implement minimal pieces instead of importing s1's prints)
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
E3 = np.eye(3, dtype=int)
def tidx(i, j): return TYPES.index((min(i,j), max(i,j)))
def slot_pos(x, t):
    i, j = TYPES[t]; p = np.array(x, float)
    if i != j: p = p + 0.5*(E3[i] + E3[j])
    return p
def airy(L, plane):
    a, b = plane; c = 3 - a - b
    phi = {}
    for u in range(L):
        for v in range(L):
            x = np.zeros(3, int); x[a] = u; x[b] = v; phi[tuple(x)] = 1
    ph = lambda x: phi.get(tuple(x), 0)
    m = {}
    for x in itertools.product(range(-2, L + 2), repeat=3):
        x = np.array(x)
        if x[c] != 0: continue
        for t, val in [(tidx(a, a), ph(x + E3[b]) - 2*ph(x) + ph(x - E3[b])),
                       (tidx(b, b), ph(x + E3[a]) - 2*ph(x) + ph(x - E3[a])),
                       (tidx(a, b), -(ph(x + E3[a] + E3[b]) - ph(x + E3[a]) - ph(x + E3[b]) + ph(x)))]:
            if val: m[(tuple(x), t)] = val
    return m
def coef(eps, t):
    i, j = TYPES[t]; return eps[i, j] if i == j else 2*eps[i, j]
def qhat(k): return 2*np.sin(np.asarray(k, float)/2)
def tt_pols(k):
    q = qhat(k); n = q/np.linalg.norm(q)
    t1 = np.cross(n, [1.0, 0.3, 0.17]); t1 /= np.linalg.norm(t1); t2 = np.cross(n, t1)
    return [(np.outer(t1, t1) - np.outer(t2, t2))/np.sqrt(2), (np.outer(t1, t2) + np.outer(t2, t1))/np.sqrt(2)], (np.outer(t1, t1) + np.outer(t2, t2))/np.sqrt(2)
def D2(kap, L):
    s = np.sin(kap/2)
    return np.where(np.abs(s) < 1e-14, L**2*1.0, np.sin(kap*L/2)**2/np.where(np.abs(s) < 1e-14, 1, s)**2)
PLANES = [(0, 1), (1, 2), (0, 2)]
def cm_formula(k, eps, L, plane):
    a, b = plane; q = qhat(k); t = np.zeros(3); t[a] = -q[b]; t[b] = q[a]
    return np.sqrt(D2(k[a], L)*D2(k[b], L))*abs(t @ eps @ t)
print("== formula check |c.mhat| explicit vs analytic ==")
worst = 0
for L in [2, 3, 5]:
    for pl in PLANES:
        m = airy(L, pl)
        for k in [np.array([0.3, 0.7, 0.2]), np.array([1.1, -0.4, 0.9])]:
            for e in tt_pols(k)[0]:
                ex = abs(sum(coef(e, t)*v*np.exp(1j*np.dot(k, slot_pos(x, t))) for (x, t), v in m.items()))
                worst = max(worst, abs(ex - cm_formula(k, e, L, pl)))
print("max |explicit - formula| = %.2e" % worst)

Lmax = 20000; Ls = np.arange(2, Lmax + 1, dtype=float)
ks = np.array([3e-3, 1e-2, 3e-2, 1e-1, 3e-1])
dirs = {'face': [1, 1, 0], 'body': [1, 1, 1], 'gen125': [1, 2, 5], 'gen213': [2, 1, 3]}
print("\n== (T1,T2) f-sum slope vs tail exponent p (unit <cos>), Lmax=%d ==" % Lmax)
for p in [2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 12.0]:
    w = Ls**(-p)
    row = []; anis = []
    for nm, d in dirs.items():
        d = np.array(d, float); d /= np.linalg.norm(d)
        ys, ys_s = [], []
        for kk in ks:
            k = kk*d; pols, scal = tt_pols(k)
            tot = 0.0; tots = 0.0
            for pl in PLANES:
                a, b = pl; q = qhat(k); t = np.zeros(3); t[a] = -q[b]; t[b] = q[a]
                g = np.sum(w*D2(k[a], Ls)*D2(k[b], Ls))
                tot += g*sum(abs(t @ e @ t)**2 for e in pols)
                tots += g*abs(t @ scal @ t)**2
            ys.append(tot); ys_s.append(tots)
        ys = np.array(ys); ys_s = np.array(ys_s)
        row.append(np.polyfit(np.log(ks[:3]), np.log(ys[:3]), 1)[0]); anis.append(ys[0]/ks[0]**min(4, p - 1) if p < 5 else ys[0]/ks[0]**4)
        if nm == 'body': sc = (np.polyfit(np.log(ks[:3]), np.log(ys_s[:3]), 1)[0], ys_s[0] > 0)
    print("p=%-4s m1_TT slopes (face,body,gen125,gen213; k=3e-3..3e-2) = %s ; m1/k^min(4,p-1) at 3e-3: %s ; scalar-trace slope(body)=%.3f positive=%s"
          % (p, np.round(row, 3), np.round(anis, 3), sc[0], sc[1]))
print("\nsummability: per-site norm sum L^-p finite for p>1; pattern 2nd-moment sum (B2; mu2(m_L)~L^3, one class per L)"
      " finite iff p>7; support form K2 (L^2 squares contain a site, mu2(support)~L^4) ~ sum L^(10-p) finite iff p>11."
      " Observed k^4 already for p>5: the sufficient conditions are not sharp; p<=5 lowers the power.")
print("Gaussian comparator (T3): omega_TT^2 = J m1 -> z = slope/2 ; p=3 gives z=1 (harmonic, unit <cos>), with a positive k^2 scalar-trace stiffness")
