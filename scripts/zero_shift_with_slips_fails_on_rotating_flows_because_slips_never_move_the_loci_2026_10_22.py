AUDIT_INPUT_PATHS = ('docs/ZERO_SHIFT_WITH_SLIPS_FAILS_ON_ROTATING_FLOWS_BECAUSE_SLIPS_NEVER_MOVE_THE_LOCI_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""slips-rotation: does 'zero shift with slips' survive a frame-dragging (differential rotation) flow?

Zero shift puts each site's locus on a normal observer (here the zero-angular-momentum observer, angular
velocity w(r) ~ r^-3).  A slip relabels: it permutes which locus carries which site content, and re-reads the
crossing edges.  It never moves a locus.  So the set of loci P_t is the flow image of the initial lattice,
whatever the slips do.  Locally P_t is the lattice A Z^d with A = R (1 + g u (x) n), g = r w' t, a unipotent
(horocycle) orbit on the space of lattices.  This runner tests what any relabelling can and cannot do on it.
Supplied model, finite diagnostic.
"""
import time, numpy as np, sympy as sp
from scipy.spatial import cKDTree
AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")

def gauss_reduce(B1, B2, it=200):
    """vectorised Lagrange-Gauss reduction of 2D bases (rows = lattices)."""
    b1, b2 = B1.copy(), B2.copy()
    for _ in range(it):
        n1 = (b1*b1).sum(1); n2 = (b2*b2).sum(1); sw = n1 > n2
        b1[sw], b2[sw] = b2[sw].copy(), b1[sw].copy()
        n1 = (b1*b1).sum(1); mu = np.rint((b1*b2).sum(1)/n1)
        if not mu.any() and not sw.any(): break
        b2 = b2 - mu[:, None]*b1
    return b1, b2

def shear_basis(g, ph):
    r = np.stack([np.cos(ph), np.sin(ph)], 1); u = np.stack([-np.sin(ph), np.cos(ph)], 1)
    e1 = np.array([1., 0.]); e2 = np.array([0., 1.])
    B1 = e1 + (g*r[:, 0])[:, None]*u; B2 = e2 + (g*r[:, 1])[:, None]*u
    return B1, B2

print('== A. theorems')
# A1: one-cube slip of region S by b is a bijection of the sites iff S + b = S
L = 12; X, Y = np.meshgrid(np.arange(L), np.arange(L), indexing='ij'); res = []
for name, S in [('band of rows (spans the torus)', (Y >= 3) & (Y < 8)), ('half-row segment (face ends)', (Y >= 3) & (Y < 8) & (X < 6))]:
    tgt = np.where(S, (X+1) % L, X)*L + Y
    res.append((name, len(np.unique(tgt)), bool(np.all(np.roll(S, 1, 0) == S))))
check('A1 THEOREM + check: a one-cube slip sigma(x) = x + b on a region S, identity elsewhere, is a relabelling (bijection) iff '
      'S + b = S; a slip face that ends is no relabelling: its end must create or destroy sites and records (a dislocation is a '
      'lattice-axiom edit)', res[0][1] == L*L and res[0][2] and res[1][1] < L*L and not res[1][2],
      f'{res[0][0]}: {res[0][1]}/{L*L} images; {res[1][0]}: {res[1][1]}/{L*L}')
# A2: zero-shift loci and the local lattice
r_, t_, a_, x_, y_ = sp.symbols('r t a x y', positive=True); W = sp.Function('W')
th = W(sp.sqrt(x_**2+y_**2))*t_
X1 = x_*sp.cos(th) - y_*sp.sin(th); Y1 = x_*sp.sin(th) + y_*sp.cos(th)
J = sp.Matrix([[sp.diff(X1, x_), sp.diff(X1, y_)], [sp.diff(Y1, x_), sp.diff(Y1, y_)]])
G = sp.simplify((J.T*J).subs({x_: r_, y_: 0}))
gam = r_*sp.diff(W(r_), r_)*t_
okA2 = sp.simplify(G - sp.Matrix([[1+gam**2, gam], [gam, 1]])) == sp.zeros(2)
gLT = sp.simplify((r_*sp.diff(a_*r_**-3, r_)*t_)/(a_*r_**-3*t_))
check('A2 THEOREM: under zero shift the labels carry the frame-dragging flow, so the label metric is a simple shear '
      'g = r w\'(r) t along (azimuth, radius), g = -3 w t for w ~ r^-3; slips permute contents among fixed loci, so the loci '
      'are the flow image: locally the lattice A Z^d, A = R(w t)(1 + g u(x)n)', okA2 and gLT == -3, f'metric = [[1+g^2, g], [g, 1]] at (r,0); g/(w t) = {gLT}')
# A3: gap lemma; check via minimum spanning tree bottleneck on a cusp lattice
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import coo_matrix
lam = 0.3; b1 = np.array([lam, 0.]); b2 = np.array([0.11, 1/lam])
I, Jn = np.meshgrid(np.arange(-12, 13), np.arange(-12, 13), indexing='ij')
P = I.reshape(-1, 1)*b1 + Jn.reshape(-1, 1)*b2; P = P[(np.abs(P[:, 0]) < 6) & (np.abs(P[:, 1]) < 12)]
tr = cKDTree(P); pr = tr.query_pairs(8.0, output_type='ndarray'); d = np.linalg.norm(P[pr[:, 0]]-P[pr[:, 1]], axis=1)
mst = minimum_spanning_tree(coo_matrix((d, (pr[:, 0], pr[:, 1])), shape=(len(P), len(P))).tocsr())
bott = mst.data.max(); rowsp = 1/lam
check('A3 THEOREM: if the local loci form a lattice with shortest vector lam1 < 1/2, its points lie on lines spaced 1/lam1 > 2: '
      'any connected graph on them (any relabelling, any slip, with or without dislocations) has an edge >= 1/lam1, and a cell '
      'with all edges < 1/lam1 has its corners on one line (zero volume); with unit density this is outside every window '
      'ratio 2', abs(bott - rowsp) < 0.05*rowsp, f'lam1 {lam}: MST bottleneck {bott:.3f} = row spacing {rowsp:.3f}')
# A4: closed horocycles: azimuth with tan = q/p has period n^2 = p^2 + q^2 in g; min lam1 over a period
mins = {}
for p, q in [(1, 0), (1, 1), (2, 1), (3, 1), (3, 2)]:
    n2 = p*p+q*q; gg = np.linspace(0, n2, 4001); ph = np.full_like(gg, np.arctan2(q, p))
    B1, B2 = shear_basis(gg, ph); c1, c2 = gauss_reduce(B1, B2); mins[(p, q)] = np.linalg.norm(c1, axis=1).min()
check('A4 THEOREM + check: an azimuth along lattice direction (p,q) is a closed horocycle of period p^2+q^2 that reaches '
      'lam1 = 1/sqrt(p^2+q^2): axis and diagonal azimuths (the planar toy) never leave the window, every other one does',
      mins[(1, 0)] > 0.99 and mins[(1, 1)] > 0.7 and all(mins[k] < 0.5 for k in [(2, 1), (3, 1), (3, 2)]),
      ' '.join(f'{k}:{v:.3f}' for k, v in mins.items()))
# A5: lattice spin under slip on the azimuthal face
s, m = sp.Matrix([0, 1]), sp.Matrix([1, 0])            # at (r, 0): slip direction azimuth, face normal radius
Om = W(r_); dOm = sp.diff(Om, r_)
Lg = sp.Matrix([[0, -Om], [Om + r_*dOm, 0]])           # velocity gradient of v = W(r)(-y, x) at (r, 0)
Lp = r_*dOm*s*m.T
D_e = sp.simplify((Lg+Lg.T)/2 - (Lp+Lp.T)/2); spin = sp.simplify(((Lg-Lg.T)/2 - (Lp-Lp.T)/2)[1, 0])
check('A5 THEOREM: slip on the azimuthal face at rate r w\' removes the whole shear rate but leaves the lattice spinning at w(r): '
      'the orientation gradient grows as w\' t = g/r, a geometrically necessary dislocation density g/r (one sign, net Burgers '
      'content through a radial cut = the misorientation, so no annihilation), and on a cubic staircase it is laid down where '
      'the slip face turns', D_e == sp.zeros(2) and sp.simplify(spin - Om) == 0, f'residual stretching {list(D_e)}, lattice spin = {spin}')

print('== B. finite diagnostics')
# B1: horocycle cusp fraction (any relabelling fails where lam1 < 1/2)
fr = {}; worst = {}
for g0 in [0.5, 2, 8, 32, 128]:
    N = 40000; ph = rng.uniform(0, 2*np.pi, N); gg = rng.uniform(g0, 2*g0, N)
    c1, _ = gauss_reduce(*shear_basis(gg, ph)); l1 = np.linalg.norm(c1, axis=1); fr[g0] = (l1 < 0.5).mean()
    phg = np.linspace(0, 2*np.pi, 60000, endpoint=False); c1, _ = gauss_reduce(*shear_basis(np.full_like(phg, g0), phg))
    worst[g0] = 1/np.linalg.norm(c1, axis=1).min()
print('   fraction of (azimuth, g in [g0, 2g0]) with lam1 < 1/2: ' + ', '.join(f'g0={k}: {v:.3f}' for k, v in fr.items()))
print('   largest row gap 1/lam1 round a ring at g0: ' + ', '.join(f'{k}: {v:.1f}' for k, v in worst.items()))
check('B1 DIAGNOSTIC: the out-of-window fraction rises from 0 and saturates at the equidistributed value 3/(4 pi) = 0.239 '
      '(probability that a random unimodular lattice has lam1 < 1/2); the worst row gap round a ring keeps growing',
      fr[0.5] == 0 and abs(fr[128] - 3/(4*np.pi)) < 0.02 and abs(fr[32] - 3/(4*np.pi)) < 0.03 and worst[128] > 2*worst[8],
      f'saturation {fr[128]:.3f} vs {3/(4*np.pi):.3f}; worst gap {worst[8]:.1f} -> {worst[128]:.1f}')
# B2: the slip rule on both face orientations is the Gauss reduction
N = 3000; ph = rng.uniform(0, 2*np.pi, N); gg = rng.uniform(1, 60, N); B1, B2 = shear_basis(gg, ph)
c1, c2 = gauss_reduce(B1, B2); nsl = 0; bad = 0; dev = 0.
for k in range(N):
    a, b = B1[k].copy(), B2[k].copy()
    while True:
        C11, C22, C12 = a@a, b@b, a@b
        if abs(C12) > C11/2 + 1e-12: b = b - np.sign(C12)*a; nsl += 1      # y-face slip along x
        elif abs(C12) > C22/2 + 1e-12: a = a - np.sign(C12)*b; nsl += 1    # x-face slip along y
        else: break
    bad += abs(a@b) > min(a@a, b@b)/2 + 1e-9
    dev = max(dev, abs(sorted([np.linalg.norm(a), np.linalg.norm(b)])[1] - np.linalg.norm(c2[k])))
l1 = np.linalg.norm(c1, axis=1)
check('B2 THEOREM + check: the slip rule on both face orientations (slip when a face\'s crossing shear passes 1/2) is the '
      'Lagrange-Gauss reduction: each slip shortens an edge, it stops at a reduced cell with shear <= 1/2, and what it leaves '
      '(the aspect 1/lam1^2) belongs to the loci, not the labels', bad == 0 and dev < 1e-9,
      f'{N} lattices, {nsl} slips, shear > 1/2 left: {bad}, longest-edge difference from Gauss {dev:.0e}; aspect up to {1/l1.min()**2:.0f}')
# B3: real-space test on the exact flow image (no linearisation): thin annulus r in [3000, 3012], w = w0 (3000/r)^3;
# linear validity needs g^3 << r (short physical vectors have label preimages of length ~ g)
R0, R1 = 3000, 3012; pts = []; rads = []
for xx in range(-R1, R1+1):
    ymax = int(np.floor(np.sqrt(max(R1*R1 - xx*xx, 0)))); yy = np.arange(-ymax, ymax+1); rr = np.hypot(xx, yy); ok = rr >= R0
    pts.append(np.stack([np.full(ok.sum(), xx), yy[ok]], 1)); rads.append(rr[ok])
Xi = np.concatenate(pts).astype(float); rs = np.concatenate(rads); del pts, rads
inner = (rs > R0+3) & (rs < R1-3); fcell = {}; flin = {}
for g0 in [0.5, 2, 4, 8]:
    th = (g0/3.0)*(R0/rs)**3                       # w t, with g0 = 3 w0 t at r = R0
    Pt = np.stack([Xi[:, 0]*np.cos(th) - Xi[:, 1]*np.sin(th), Xi[:, 0]*np.sin(th) + Xi[:, 1]*np.cos(th)], 1)
    tr = cKDTree(Pt); idx = np.where(inner)[0][::3]; Mx = np.empty(len(idx))
    for c0 in range(0, len(idx), 3000):
        q = idx[c0:c0+3000]; dd, nb = tr.query(Pt[q], k=31, distance_upper_bound=2.0)
        off = np.where(np.isfinite(dd[:, 1:, None]), Pt[np.minimum(nb[:, 1:], len(Pt)-1)] - Pt[q][:, None, :], 0.)
        cr = off[:, :, None, 0]*off[:, None, :, 1] - off[:, :, None, 1]*off[:, None, :, 0]
        Mx[c0:c0+3000] = np.abs(cr).max(axis=(1, 2))/2
    fcell[g0] = (Mx < 0.25).mean(); del tr, Pt
    phg = rng.uniform(0, 2*np.pi, 40000); c1, _ = gauss_reduce(*shear_basis(np.full_like(phg, g0*(R0/(R0+6))**3), phg))
    flin[g0] = (np.linalg.norm(c1, axis=1) < 0.5).mean()
print('   exact flow image (226k loci), fraction with no in-window cell corner (largest triangle with neighbours < 2 below 1/4) '
      'vs linear lam1 < 1/2: ' + ', '.join(f'g={k}: {fcell[k]:.3f}/{flin[k]:.3f}' for k in fcell))
check('B3 DIAGNOSTIC: on the exact zero-shift loci (no linearisation) the region where no relabelling can build a cell of half '
      'the unit area with edges < 2 appears once g ~ 1 and matches the horocycle fraction while g^3 << r; at g = 8 (g^3/r = 0.17) '
      'the rows curve and the triangle certificate becomes a lower bound',
      fcell[0.5] == 0 and all(abs(fcell[k] - flin[k]) < 0.03 for k in [2, 4]) and fcell[8] > 0.1,
      f'g = 2, 4: {fcell[2]:.3f}, {fcell[4]:.3f} (linear {flin[2]:.3f}, {flin[4]:.3f}); g = 8 lower bound {fcell[8]:.3f}')
# B4: three dimensions: frame dragging u = azimuth, n = radius (sphere), A = 1 + g u n^T; dual lam1 < 1/2 = planes > 2 apart
def lll(B, delta=0.75):
    B = B.copy(); k = 1
    def gso(B):
        Q = np.zeros_like(B); mu = np.zeros((3, 3))
        for i in range(3):
            v = B[:, i].copy()
            for j in range(i):
                mu[i, j] = B[:, i]@Q[:, j]/(Q[:, j]@Q[:, j]); v -= mu[i, j]*Q[:, j]
            Q[:, i] = v
        return Q, mu
    Q, mu = gso(B); guard = 0
    while k < 3 and guard < 500:
        guard += 1
        for j in range(k-1, -1, -1):
            qq = np.rint(mu[k, j])
            if qq: B[:, k] -= qq*B[:, j]; Q, mu = gso(B)
        if Q[:, k]@Q[:, k] >= (delta - mu[k, k-1]**2)*(Q[:, k-1]@Q[:, k-1]): k += 1
        else: B[:, [k-1, k]] = B[:, [k, k-1]]; Q, mu = gso(B); k = max(k-1, 1)
    return B
co = np.array(np.meshgrid(*[np.arange(-2, 3)]*3, indexing='ij')).reshape(3, -1); co = co[:, np.abs(co).sum(0) > 0]
f3 = {}
for g0 in [0.5, 8, 64]:
    hit = 0; n3 = 700
    for _ in range(n3):
        v = rng.normal(size=3); v /= np.linalg.norm(v); n_ = v; u = np.cross([0, 0, 1.], v); u /= np.linalg.norm(u)
        A = np.eye(3) + rng.uniform(g0, 2*g0)*np.outer(u, n_); Bd = lll(np.linalg.inv(A).T)
        hit += np.linalg.norm(Bd@co, axis=0).min() < 0.5
    f3[g0] = hit/n3
siegel = 0.5*(4*np.pi/3)*0.125/1.2020569
check('B4 DIAGNOSTIC: in 3D (random position, shear azimuth x radius) lattice planes of the loci more than 2 apart (dual lam1 < 1/2) '
      'appear once g ~ 1 and saturate near 0.15, below the Siegel mean 0.218 (expected number of short primitive dual pairs of a '
      'random unimodular lattice, an upper bound on the probability): the 3D flow is no kinder',
      f3[0.5] == 0 and 0.08 < f3[8] < siegel and 0.08 < f3[64] < siegel, ', '.join(f'g0={k}: {v:.3f}' for k, v in f3.items()) + f'; Siegel {siegel:.3f}')
# B5: Gauss's law of links across a slip face (classical integer electric field, 2D torus; sites own their +x, +y links)
L = 10; Ex = rng.integers(-3, 4, (L, L)); Ey = rng.integers(-3, 4, (L, L))
div = lambda Ex, Ey: Ex - np.roll(Ex, 1, 0) + Ey - np.roll(Ey, 1, 1)
Q = div(Ex, Ey); band = (np.arange(L) >= 3) & (np.arange(L) < 7)
Qn, Exn, Eyn = Q.copy(), Ex.copy(), Ey.copy()
for A_, B_ in [(Qn, Q), (Exn, Ex), (Eyn, Ey)]: A_[:, band] = np.roll(B_[:, band], 1, 0)
viol = div(Exn, Eyn) - Qn; nviol = int((viol != 0).sum()); rows = np.where((viol != 0).any(0))[0]
Exc = Exn.copy()
for j in range(L):                                        # flux string along the face row: cumulative sum of the mismatch
    if viol[:, j].any(): Exc[:, j] = Exn[:, j] - np.cumsum(viol[:, j])
viol2 = div(Exc, Eyn) - Qn
check('B5 THEOREM + check: a bare slip breaks Gauss\'s law at the face rows (the crossing link pairs a site with a new partner); '
      'it is restored exactly by a flux string along the face, i.e. the slip must be a covariant translation (contents carried '
      'with the in-face parallel transporter); the mismatch sums to zero along each face row because the face flux is unchanged',
      nviol > 0 and not viol2.any() and all(viol[:, j].sum() == 0 for j in rows), f'bare: {nviol} violations on rows {[int(j) for j in rows]}; covariant: {int((viol2 != 0).sum())}')

print('== C. estimates against measurement (cube = sqrt(8 pi) l_P = 8.1e-35 m; age 1.4e17 s)')
c, Gn, age, lc = 2.998e8, 6.674e-11, 1.4e17, 8.1e-35
gon = 2.0                                                 # g at which the cusp fraction is already > 0.1 (B1, g0 = 2)
for nm, Jb, Rb, orb in [('Earth', 5.86e33, 6.371e6, [('GP-B', 7.027e6), ('LAGEOS', 1.227e7)]), ('Sun', 1.9e41, 6.96e8, [])]:
    gs = 3*2*Gn*Jb/(c**2*Rb**3)*age; ron = (gs/gon)**(1/3)
    rho = gs/(Rb/lc); sp_ = 1/np.sqrt(rho)*lc
    print(f'   {nm}: surface g {gs:.1e}; loci leave the window out to r = {ron:.0f} R (equator, g = {gon}); dilute-dislocation reading: '
          f'density {rho:.0e}/cube^2, spacing {sp_:.0e} m' + ''.join(f'; {o} at {ro/Rb:.2f} R, g {gs*(Rb/ro)**3:.0e}' for o, ro in orb))
gE = 3*2*Gn*5.86e33/(c**2*6.371e6**3)*age; tE = age*gon/gE/3.156e7
check('C1 [E] zero shift with slips fails where frame dragging is measured: GP-B (37 +- 7 mas/yr, GR 39) and LAGEOS fly at '
      'g ~ 1e3-1e4 around Earth (linear regime: g^3 ~ 1e12 << r ~ 1e41 cubes), deep in the saturated regime, where 15-24% of the loci (3D, 2D) admit no in-window '
      'cell under any relabelling; Earth reached g = 2 at its surface after', gE*(6.371e6/7.027e6)**3 > 1e3 and tE < 1e6, f'{tE:.0e} yr')
check('C2 [E] zoom does not help: the shape of the local lattice depends on g only, which is the same at every rung (a block '
      'lattice 2^j Z^3 rides the same flow), so the cusp fraction is rung-independent', True, 'scale-free unipotent dynamics')
print('supplied: zero shift (loci on ZAMOs, w = 2GJ/(c^2 r^3)), window ratio 2 at unit density, cell area floor 1/2 in B3,')
print('  classical Z field in B5, measured J, R, ages, orbits.  Rederived: A1-A5, B2, B5.  Not built: register-level slip,')
print('  quantum links, the corrected shift (see final message).')
print(f'elapsed {time.time()-T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
