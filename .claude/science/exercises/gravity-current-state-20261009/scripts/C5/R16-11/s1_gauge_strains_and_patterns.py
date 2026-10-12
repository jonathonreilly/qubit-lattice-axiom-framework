"""R16-11 s1 (written before running).  Exact integer stencil of N0914:95-97 (vector law G) on Z^3.
Slots: E_jj(x) at position x; face slot E_ij(x) (i<j) at x+(e_i+e_j)/2.  Gauss site G_j(x) at x+e_j/2.
Pre-registered expectations:
 (A) Every constant and every linear symmetric strain field l(pos) on slots (6+18=24 fields) equals
     G^T alpha on the interior for some alpha (constant -> linear alpha, linear -> quadratic alpha).
     => sum_s l(s) E_s is a (cut-off) combination of Gauss operators, so EVERY local operator commuting
     with all G_j commutes with it (support-moment lemma, operator form).  Residual ~1e-12 expected.
     U(1) control (links, div): constants (3) in image; linear vector fields: only the 6 symmetric ones;
     the 3 rotations l = w x pos are NOT in the image (residual O(1)) -> photon vertex is O(k).
 (B) Qubit-compatible invariant hops exist: planar 'Airy rectangle' patterns (L1 x L2, L>=2) have entries
     in {-1,0,1}, satisfy G m = 0 exactly (integers), zero 0th and 1st moments, |eps.mhat(k)|^2 slope 4,
     and obey the support-moment bound |c.mhat(k)| <= k^2 sum_s |c_s||m_s||pos_s-x0|^2/2.
     L=1 (single-site Airy) needs |m_s|=2 (spin>=1).
 (C) No nonzero invariant pattern with <=2 nonzero slots (entries +-1) exists -> first-order projection
     (P V P) of any one- or two-slot law-violating hop term (e.g. R13-2's D0 sin.B.sin) is zero.
 (D) Law-violating single flips: |eps.mhat|^2 slope 0 (O(1)).
"""
import numpy as np, itertools
np.set_printoptions(precision=4, suppress=True)
E3 = np.eye(3, dtype=int)
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
def slot_pos(x, t):
    i, j = TYPES[t]
    p = np.array(x, float)
    if i != j: p = p + 0.5*(E3[i] + E3[j])
    return p
def tidx(i, j):
    return TYPES.index((min(i,j), max(i,j)))

def G_rows(m):
    """m: dict {(x tuple, t): int}.  returns dict {(x, j): (Gm)_j(x)} nonzero entries (integer)."""
    out = {}
    def add(key, v):
        out[key] = out.get(key, 0) + v
    for (x, t), v in m.items():
        if v == 0: continue
        i, j = TYPES[t]
        x = np.array(x)
        if i == j:
            # p_jj(x) appears in G_j(x - e_j) with +1 and in G_j(x) with -1
            add((tuple(x - E3[j]), j), +v); add((tuple(x), j), -v)
        else:
            # p_ij(x) appears in G_j(x) (+1), G_j(x+e_i) (-1), G_i(x) (+1), G_i(x+e_j) (-1)
            add((tuple(x), j), +v); add((tuple(x + E3[i]), j), -v)
            add((tuple(x), i), +v); add((tuple(x + E3[j]), i), -v)
    return {k: v for k, v in out.items() if v != 0}

print("== (A) gauge-generated strains: tensor (N0914 stencil) vs U(1) ==")
L = 7
sites = list(itertools.product(range(L), repeat=3))
# unknowns alpha_j(x) on Gauss sites in a box [-1, L] (so every interior slot's rows exist)
gsites = [(x, j) for x in itertools.product(range(-1, L+1), repeat=3) for j in range(3)]
gidx = {g: n for n, g in enumerate(gsites)}
inner = [x for x in sites if all(1 <= c <= L-2 for c in x)]
slots = [(x, t) for x in inner for t in range(6)]
# matrix GT: rows = slots, cols = gauss sites, entry = coefficient of p_slot in G_gauss
GT = np.zeros((len(slots), len(gsites)))
for r, (x, t) in enumerate(slots):
    for (gx, j), v in G_rows({(x, t): 1}).items():
        GT[r, gidx[(gx, j)]] += v
center = np.array([L/2 - 0.5]*3)
def strain_fields():
    F = []
    names = []
    for t in range(6):  # constants: coefficient of slot type t
        F.append(np.array([1.0 if tt == t else 0.0 for (x, tt) in slots])); names.append('const %s' % (TYPES[t],))
    for t in range(6):
        for a in range(3):
            F.append(np.array([(slot_pos(x, tt) - center)[a] if tt == t else 0.0 for (x, tt) in slots]))
            names.append('lin %s*pos_%d' % (TYPES[t], a))
    return np.array(F), names
F, names = strain_fields()
res_t = []
for f, nm in zip(F, names):
    a, *_ = np.linalg.lstsq(GT, f, rcond=None)
    res_t.append(np.abs(GT @ a - f).max())
res_t = np.array(res_t)
print("tensor: 24 strain fields (6 const + 18 linear); max residual of G^T alpha = l on interior: %.2e" % res_t.max())
print("        rank of image restricted to span of the 24 fields: %d / 24" %
      np.linalg.matrix_rank(np.column_stack([GT @ np.linalg.lstsq(GT, f, rcond=None)[0] for f in F]), tol=1e-8))

# U(1): links E_i(x) at x + e_i/2; G(x) = sum_i [E_i(x) - E_i(x - e_i)]
gs1 = list(itertools.product(range(-1, L+1), repeat=3)); g1 = {g: n for n, g in enumerate(gs1)}
lslots = [(x, i) for x in inner for i in range(3)]
GT1 = np.zeros((len(lslots), len(gs1)))
for r, (x, i) in enumerate(lslots):
    GT1[r, g1[x]] += 1; GT1[r, g1[tuple(np.array(x) + E3[i])]] -= 1
def lpos(x, i): return np.array(x, float) + 0.5*E3[i]
res_u = {}
for i in range(3):
    f = np.array([1.0 if ii == i else 0.0 for (x, ii) in lslots])
    a, *_ = np.linalg.lstsq(GT1, f, rcond=None); res_u['const_%d' % i] = np.abs(GT1 @ a - f).max()
for i in range(3):
    for b in range(3):
        f = np.array([(lpos(x, ii) - center)[b] if ii == i else 0.0 for (x, ii) in lslots])
        a, *_ = np.linalg.lstsq(GT1, f, rcond=None); res_u['lin E_%d*pos_%d' % (i, b)] = np.abs(GT1 @ a - f).max()
# symmetric / antisymmetric combinations
for (i, b) in [(0, 1), (1, 2), (0, 2)]:
    for sgn, lab in [(+1, 'sym'), (-1, 'rot')]:
        f = np.array([((lpos(x, ii) - center)[b] if ii == i else 0.0) + sgn*((lpos(x, ii) - center)[i] if ii == b else 0.0)
                      for (x, ii) in lslots])
        a, *_ = np.linalg.lstsq(GT1, f, rcond=None); res_u['%s(%d,%d)' % (lab, i, b)] = np.abs(GT1 @ a - f).max()
print("U(1): constants residual: %s" % [('%.1e' % res_u['const_%d' % i]) for i in range(3)])
print("      linear diagonal (E_i*pos_i) residual: %s" % [('%.1e' % res_u['lin E_%d*pos_%d' % (i, i)]) for i in range(3)])
print("      symmetric off-diagonal residual: %s" % [('%.1e' % res_u['sym%s' % s]) for s in ['(0,1)', '(1,2)', '(0,2)']])
print("      ROTATIONS (w x pos) residual:     %s   <- not pure gauge: photon vertex O(k)" % [('%.2f' % res_u['rot%s' % s]) for s in ['(0,1)', '(1,2)', '(0,2)']])
print("counting: tensor linear strains 18 = sym-grad of quadratic alpha (3x6=18, Killing kernel 0 at degree 2);"
      " U(1) linear vector fields 9 > grad of quadratic scalar (6)")

print("\n== (B) qubit-compatible invariant hops: planar Airy rectangles ==")
def airy(L1, L2, plane=(0, 1), z0=0):
    a, b = plane; c = 3 - a - b
    phi = {}
    for u in range(L1):
        for v in range(L2):
            x = np.zeros(3, int); x[a] = u; x[b] = v; x[c] = z0; phi[tuple(x)] = 1
    def ph(x): return phi.get(tuple(x), 0)
    m = {}
    def add(x, t, v):
        if v: m[(tuple(x), t)] = m.get((tuple(x), t), 0) + v
    rng_ = [np.array(x) for x in itertools.product(range(-2, max(L1, L2) + 2), repeat=3)]
    for x in rng_:
        if x[c] != z0: continue
        add(x, tidx(a, a), ph(x + E3[b]) - 2*ph(x) + ph(x - E3[b]))        # m_aa = Delta_bb phi
        add(x, tidx(b, b), ph(x + E3[a]) - 2*ph(x) + ph(x - E3[a]))        # m_bb = Delta_aa phi
        add(x, tidx(a, b), -(ph(x + E3[a] + E3[b]) - ph(x + E3[a]) - ph(x + E3[b]) + ph(x)))  # m_ab
    return {k: v for k, v in m.items() if v}
def qhat(k): return 2*np.sin(np.asarray(k, float)/2)
def tt_pols(k):
    q = qhat(k); n = q/np.linalg.norm(q)
    # two TT unit tensors (Frobenius) orthogonal to n
    t1 = np.cross(n, [1.0, 0.3, 0.17]); t1 /= np.linalg.norm(t1); t2 = np.cross(n, t1)
    e1 = (np.outer(t1, t1) - np.outer(t2, t2))/np.sqrt(2); e2 = (np.outer(t1, t2) + np.outer(t2, t1))/np.sqrt(2)
    return [e1, e2]
def coef(eps, t):
    i, j = TYPES[t]
    return eps[i, j] if i == j else 2*eps[i, j]     # eps:E = sum_diag + 2 sum_{i<j} on the single face slot
def symb(m, k, eps, x0):
    return sum(coef(eps, t)*v*np.exp(1j*np.dot(k, slot_pos(x, t) - x0)) for (x, t), v in m.items())
def moments(m):
    m0 = np.zeros(6); m1 = np.zeros((6, 3))
    for (x, t), v in m.items():
        m0[t] += v; m1[t] += v*slot_pos(x, t)
    return np.abs(m0).max(), np.abs(m1).max()
dirs = {'axis': [0, 0, 1], 'face': [1, 1, 0], 'body': [1, 1, 1], 'gen125': [1, 2, 5], 'gen213': [2, 1, 3]}
ks = np.array([1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3])
for (L1, L2, pl) in [(1, 1, (0, 1)), (2, 2, (0, 1)), (2, 3, (1, 2)), (3, 5, (0, 2)), (6, 6, (0, 1))]:
    m = airy(L1, L2, pl)
    Gm = G_rows(m)
    ent = sorted(set(m.values()))
    x0 = np.mean([slot_pos(x, t) for (x, t) in m], axis=0)
    mu2 = lambda eps: sum(abs(coef(eps, t))*abs(v)*np.sum((slot_pos(x, t) - x0)**2) for (x, t), v in m.items())
    slopes, worst = [], 0.0
    for nm, d in dirs.items():
        d = np.array(d, float); d /= np.linalg.norm(d)
        ys = []
        for kk in ks:
            k = kk*d
            vals = [abs(symb(m, k, e, x0)) for e in tt_pols(k)]
            ys.append(sum(v**2 for v in vals))
            for e, v in zip(tt_pols(k), vals):
                worst = max(worst, v/(kk**2*mu2(e)/2))
        ys = np.array(ys)
        if ys.max() > 1e-30: slopes.append(np.polyfit(np.log(ks), np.log(ys), 1)[0])
        else: slopes.append(np.nan)
    m0, m1 = moments(m)
    print("Airy %dx%d plane%s: slots=%d entries=%s  |Gm|=%d  max|0th mom|=%g max|1st mom|=%.1e  TT slopes=%s  max ratio to support-moment bound=%.3f"
          % (L1, L2, pl, len(m), ent, len(Gm), m0, m1, np.round(slopes, 3), worst))

print("\n== (C) no invariant pattern with <=2 nonzero +-1 slots (box 3^3 around origin) ==")
box = list(itertools.product(range(-1, 2), repeat=3))
allslots = [(x, t) for x in box for t in range(6)]
count = 0; found = 0
for s1 in allslots:
    for v1 in (1, -1):
        if not G_rows({s1: v1}) == {}: pass
        else: found += 1
        count += 1
for a_, b_ in itertools.combinations(allslots, 2):
    for v1, v2 in [(1, 1), (1, -1)]:
        count += 1
        if G_rows({a_: v1, b_: v2}) == {}: found += 1
print("patterns tested: %d ; exactly invariant: %d  -> P0 (one/two-slot hop) P0 = 0 at first order" % (count, found))

print("\n== (D) law-violating single flip: TT symbol slope ==")
m = {((0, 0, 0), tidx(0, 1)): 1}
for nm, d in list(dirs.items())[:3]:
    d = np.array(d, float); d /= np.linalg.norm(d)
    ys = np.array([sum(abs(symb(m, kk*d, e, np.zeros(3)))**2 for e in tt_pols(kk*d)) for kk in ks])
    print("  %-6s slope=%.3f value@1e-3=%.3f  |Gm| entries=%d" % (nm, np.polyfit(np.log(ks), np.log(ys), 1)[0], ys[0], len(G_rows(m))))
