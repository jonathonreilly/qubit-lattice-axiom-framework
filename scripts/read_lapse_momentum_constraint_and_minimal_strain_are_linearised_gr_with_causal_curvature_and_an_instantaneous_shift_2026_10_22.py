AUDIT_INPUT_PATHS = ('docs/READ_LAPSE_MOMENTUM_CONSTRAINT_AND_MINIMAL_STRAIN_ARE_LINEARISED_GR_WITH_CAUSAL_CURVATURE_AND_AN_INSTANTANEOUS_SHIFT_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""min-strain probe: CL-3 momentum constraint (matter included) + minimal-strain shift + read lapse.

Linearised ADM on flat slices, every lattice k through the consistent lattice derivative
(d_j -> i kt_j, kt_j = 2 sin(k_j/2), K = |kt|^2), units 16 pi G = 1, sources T^{mu nu} conserved.
(A) mode count with the read lapse dN = tr h/6 (f = 1/3), shift varied (momentum constraint kept),
    minimal-strain gauge d_j(d_t gamma_ij) = 0; (B) causality of gauge-invariant observables vs the
    elliptic shift; (C) local hyperbolic drivers; (D) the variational vs Euler-Lagrange form on open
    and periodic lattices; (E) gauge = no signal, finite toy; (F) estimates.
"""
AUDIT_TIMEOUT_SEC = 120
import time, itertools
import numpy as np
import sympy as sp
t0 = time.time()
NP = [0, 0]
SHORT = {  # printed labels; the full statement of each check is the first argument in the source
 'A0': '[T] control: quadratic ADM form diffeo invariant (4 gauge dirs), tensors omega^2 = K',
 'A1': '[T] read lapse + momentum constraint + minimal strain: scalar and vector sectors have no mode at omega != 0, any K; tensors 2x omega^2 = K',
 'A2': '[T] control: shift held at 0, its equation dropped -> ghost-normal double root omega^2 = K/3',
 'A3': '[T] omega = 0: static kernel = slice tilt (static beta_L) + static transverse relabelling (initial-data gauge)',
 'A4': '[T] robustness: 4 independent lattice multipliers (hop, curvature, lapse, gauge): still no scalar mode',
 'B1': '[T] conserved sources: unique solution; it obeys the dropped Hamiltonian constraint and all of GR',
 'B2': '[T] control: de Donder hbar = c T/(omega^2 - K), one c: covariant, retarded',
 'B3': '[T] Riemann(minimal strain) = Riemann(de Donder) for all sources, all K: observables retarded',
 'B4': '[T] minimal strain = elliptic (K delta + k k) beta = i k tr(kappa) - J; inverse non-polynomial (instantaneous Kelvin kernel)',
 'B5': '[D] 32^3 lattice: one tick after a current appears, beta is nonzero 8 cubes away (~1/r); light moved <= 0.022 cube',
 'B6': '[T] minimal-strain edges transverse, scalar part = Bardeen Psi = rho/(4K): frame-read edges respond instantaneously',
 'C1': '[T] Gamma-driver + read lapse: longitudinal omega^2 = K(1+4mu)/3, transverse mu K; mu = 3/4 -> 2/sqrt3 c; causal iff mu <= 1/2',
 'C2': '[T] strain driver: longitudinal omega^2 = K(1+6mu)/3, transverse mu K; causal iff mu <= 1/3',
 'C3': '[T] eta > 0: all gauge roots damped; eta -> inf slow root -> lapse speed 1/sqrt3',
 'C4': '[T] driver modes pure gauge (Riemann = 0)',
 'D1': '[T] uniform expansion: EL form gives beta = 0; least-squares on an open block gives beta = -Hx (edges frozen); torus: agree',
 'D2': '[T] EL operator positive off k = 0; kernel = affine shifts; cap |beta| <= 1 cube/tick -> unique (Liouville)',
 'E1': '[T] toy: constraint-generated far-controlled shift leaks 0; O(k^2)-mismatched transport leaks ~ b x momentum spread',
 'F1': '[E] cap binds only at r < (sin^2 eps0/3) r_s (inside horizons); not in cosmology (EL form)',
 'F2': '[E] instantaneous frame-read edge change from a lab rearrangement ~ G m/(c^2 r)',
}
def check(name, ok, detail=''):
    NP[0 if ok else 1] += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name[:2]} {SHORT.get(name[:2], name)} | {detail}")

I = sp.I
w, kap, mu, eta = sp.symbols('omega kappa mu eta', positive=True)
PAIRS = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
def hidx(i, j): return PAIRS.index((min(i, j), max(i, j)))
NQ = 10                       # q = (h11,h12,h13,h22,h23,h33, b1,b2,b3, phi)
def e(n):
    v = sp.zeros(NQ, 1); v[n] = 1; return v
def H(i, j): return e(hidx(i, j))
def Bv(i): return e(6 + i)
TR = H(0, 0) + H(1, 1) + H(2, 2)

def build(kv, lapse='read'):
    """Hermitian forms of L = (1/4)(|kap_ij|^2 - |tr kap|^2) + L_V + Re(phi* R1); returns M(omega) (q -> EOM)."""
    PHI = TR / 6 if lapse == 'read' else e(9)
    K = sum(x ** 2 for x in kv)
    WT = sp.zeros(2 * NQ, 2 * NQ)
    def sq(l, c=1):            # c |l.x|^2, x = (qdot, q)
        nonlocal WT; WT += c * l.conjugate() * l.T
    def re(l1, l2, c=1):       # c Re((l1.x)^* (l2.x))
        nonlocal WT; WT += c * (l1.conjugate() * l2.T + l2.conjugate() * l1.T) / 2
    Z = sp.zeros(NQ, 1)
    def dot(lq): return sp.Matrix.vstack(lq, Z)       # form on qdot
    def pos(lq): return sp.Matrix.vstack(Z, lq)       # form on q
    for i in range(3):
        for j in range(3):
            sq(dot(H(i, j)) + pos(-I * (kv[i] * Bv(j) + kv[j] * Bv(i))), sp.Rational(1, 4))
    trk = dot(TR) + pos(-2 * I * sum((kv[i] * Bv(i) for i in range(3)), Z))
    sq(trk, -sp.Rational(1, 4))
    for i in range(3):
        for j in range(3):
            sq(pos(H(i, j)), -K / 4)                  # -(1/4) d_k h_ij d_k h_ij
    for j in range(3):
        sq(pos(sum((kv[i] * H(i, j) for i in range(3)), Z)), sp.Rational(1, 2))
    X = sum((kv[i] * kv[j] * H(i, j) for i in range(3) for j in range(3)), Z)
    re(pos(X), pos(TR), -sp.Rational(1, 2))
    sq(pos(TR), K / 4)
    re(pos(PHI), pos(-X + K * TR), 1)                 # dN * 3R^(1)
    T = WT[:NQ, :NQ]; G = WT[:NQ, NQ:]; Wqq = WT[NQ:, NQ:]
    M = w ** 2 * T + I * w * (G - G.H) + Wqq
    return M.applyfunc(sp.expand), PHI

def source(kv, S, PHI):
    """j = dL_int/dq*, L_int = -Re(phi* rho) + Re(b*.J) + (1/2)Re(h*:S); conserved T from free stresses S."""
    K = sum(x ** 2 for x in kv)
    J = [sum(kv[i] * S[i][j] for i in range(3)) / w for j in range(3)]
    rho = sum(kv[j] * J[j] for j in range(3)) / w
    jv = -PHI * rho / 2
    for i in range(3):
        jv += Bv(i) * J[i] / 2
        for j in range(3):
            jv += H(i, j) * S[i][j] / 4
    return jv, rho, J

def metric4(x, PHI):
    phi = (PHI.T * x)[0]
    h = sp.zeros(4, 4); h[0, 0] = -2 * phi
    for i in range(3):
        h[0, i + 1] = h[i + 1, 0] = x[6 + i]
        for j in range(3):
            h[i + 1, j + 1] = x[hidx(i, j)]
    return h

def riemann(h, kv):
    k = [-w] + list(kv)        # d_mu -> i k_mu
    R = {}
    for a, b, c, d in [(0, 1, 0, 1), (0, 3, 0, 3), (0, 1, 0, 3), (0, 1, 1, 3), (0, 3, 1, 3), (1, 3, 1, 3),
                       (1, 2, 1, 2), (0, 1, 1, 2), (1, 2, 1, 3), (0, 1, 0, 2), (0, 2, 2, 3), (2, 3, 2, 3)]:
        R[(a, b, c, d)] = -sp.Rational(1, 2) * (k[b] * k[c] * h[a, d] + k[a] * k[d] * h[b, c]
                                               - k[a] * k[c] * h[b, d] - k[b] * k[d] * h[a, c])
    return R

kz = [0, 0, kap]
MG, PHIG = build(kz, 'free'); MC, PHIC = build(kz, 'read')
MC9 = MC[:9, :9]

print('== A. mode count: read lapse, momentum constraint with matter, minimal-strain shift (k along z, any K = kappa^2)')
# A0 control: GR is diffeomorphism invariant (4 gauge directions at every omega) and tensors move at omega^2 = K
num = {w: sp.Rational(7, 5), kap: sp.Rational(3, 4)}
nG = len(MG.subs(num).nullspace())
ten = sp.factor(sp.Matrix([[MG[0, 0] - MG[0, 3], 0], [0, MG[1, 1]]]).det())
check('A0 [T] control: the quadratic ADM form is diffeomorphism invariant (4 gauge directions at generic omega, k) and the '
      'tensor modes obey omega^2 = K', nG == 4 and sp.simplify(ten.subs(w, kap)) == 0, f'gauge directions {nG}; tensor det {ten}')
# helicity sectors about z
U = {'S': [H(0, 0) + H(1, 1), H(2, 2), Bv(2)], 'V': [H(0, 2), Bv(0)], 'Vy': [H(1, 2), Bv(1)], 'T': [H(0, 0) - H(1, 1), H(0, 1)]}
U9 = {s: [u[:9, :] for u in U[s]] for s in U}
blocks_ok = all(sp.simplify((a.T * MC9 * b)[0]) == 0 for s1 in U9 for s2 in U9 if s1 != s2 for a in U9[s1] for b in U9[s2])
def sector(Mm, s): return sp.Matrix([[sp.expand((a.T * Mm * b)[0]) for b in U9[s]] for a in U9[s]])
MS_S, MS_V, MS_T = sector(MC9, 'S'), sector(MC9, 'V'), sector(MC9, 'T')
# minimal strain for omega != 0: kt_j h_ij = 0 -> h13 = h23 = h33 = 0
redS = MS_S[:, [0, 2]]; redV = MS_V[:, [1]]
minS = [sp.factor(redS.extract(list(r), [0, 1]).det()) for r in itertools.combinations(range(3), 2)]
gS = sp.factor(sp.gcd_list(minS)); gV = sp.factor(sp.gcd_list(list(redV)))
check('A1 [T] with the read lapse, the shift varied (momentum constraint) and minimal strain, the scalar and vector sectors '
      'have NO mode at any omega != 0 and any K > 0: the gcd of all maximal minors is a monomial in omega and kappa; the tensor '
      'sector keeps omega^2 = K twice. No propagating scalar, no ghost, no vector',
      blocks_ok and sp.Poly(gS, w).is_monomial and sp.Poly(gV, w).is_monomial and sp.simplify(MS_T.det() * 4 - (w ** 2 - kap ** 2) ** 2) == 0,
      f'sectors decouple {blocks_ok}; scalar gcd {gS}; vector gcd {gV}; tensor det {sp.factor(MS_T.det())}')
# A2 control: shift not varied (beta = 0, momentum constraint dropped) -> the ghost pair returns
cB = sp.factor(MS_S[:2, :2].det())
check('A2 [T] control: the same lapse with the shift held at zero and its equation dropped gives the double root '
      'omega^2 = K/3 (ghost-normal pair, inhomog-volume B3); the method sees ghosts when they exist', sp.simplify(cB + (kap ** 2 - 3 * w ** 2) ** 2 / 36) == 0, f'det {cB}')
# A3 static residual (omega = 0): minimal strain is vacuous; residual = time-independent relabellings
nS0 = len(MS_S.subs(w, 0).nullspace()); nV0 = len(MS_V.subs(w, 0).nullspace())
kS0 = list(MS_S.subs(w, 0).nullspace()[0]); kV0 = list(MS_V.subs(w, 0).nullspace()[0])
check('A3 [T] at omega = 0 minimal strain is empty; the static kernel is a slice tilt t -> t + f(x) (pure static beta_L, allowed '
      'because it leaves the read lapse unchanged) and a static transverse relabelling: initial-data gauge, not modes. A static '
      'longitudinal relabelling is not in it (it changes the read lapse, so it needs a growing time shift)',
      nS0 == 1 and nV0 == 1 and kS0 == [0, 0, 1] and kV0 == [1, 0], f'scalar kernel (h11+h22, h33, b3) = {kS0}; vector (h13, b1) = {kV0}')
# A4 robustness: independent lattice multipliers (hops K, curvature K_R, lapse K_N, gauge K_g)
K, KR, KN, Kg = sp.symbols('K K_R K_N K_g', positive=True); tt = sp.symbols('t')
z, E_, B_ = [sp.Function(n)(tt) for n in ('z', 'E', 'B')]
ph = z - KN * E_ / 3
Ls = -6 * z.diff(tt) ** 2 + 4 * K * z.diff(tt) * (E_.diff(tt) - B_) + 2 * KR * z ** 2 + 4 * KR * ph * z
cs = sp.symbols('c0:3'); sb = {q: c * sp.exp(-I * w * tt) for q, c in zip((z, E_, B_), cs)}
rows = [sp.expand(sp.simplify(sp.euler_equations(Ls, [q], tt)[0].lhs.subs(sb).doit() * sp.exp(I * w * tt))) for q in (z, E_, B_)]
Mr = sp.Matrix([[r.coeff(c) for c in cs] for r in rows] + [[1, -Kg, 0]])
gr = sp.factor(sp.gcd_list([Mr.extract(list(r), [0, 1, 2]).det() for r in itertools.combinations(range(4), 3)]))
check('A4 [T] robustness: with four independent positive lattice multipliers (hops, curvature, lapse, gauge) the scalar '
      'sector still has no mode at omega != 0', sp.Poly(gr, w).is_monomial, f'gcd of 3x3 minors {gr}')

print('== B. matter, the dropped Hamiltonian constraint, and causality')
Ssym = sp.symbols('S11 S12 S13 S22 S23 S33')
S = [[Ssym[hidx(i, j)] for j in range(3)] for i in range(3)]
jC, rho, J = source(kz, S, PHIC)
xs = sp.symbols('x0:9')
xv = sp.Matrix(list(xs) + [0])
eqs = list(MC9 * sp.Matrix(xs) + jC[:9, :]) + [xs[2], xs[4], xs[5]]
solC = sp.solve(eqs, xs, dict=True)
xC = xv.subs(solC[0]) if solC else None
# Hamiltonian-constraint residual: GR's lapse row on the CL solution (phi = tr h / 6 inserted)
jG, _, _ = source(kz, S, PHIG)
xG = sp.Matrix(list(xC[:9]) + [(TR.T * xC)[0] / 6]) if xC is not None else None
hc = sp.simplify((MG * xG + jG)[9]) if xG is not None else None
allG = sp.simplify(MG * xG + jG) if xG is not None else None
check('B1 [T] for every conserved source the CL system (9 equations incl. the momentum constraint with matter) plus minimal '
      'strain has a unique solution, and it satisfies the dropped Hamiltonian constraint and all of GR: it IS the GR '
      'solution in the minimal-strain + fixed-step slicing (the E equation carries dN/dE x the Hamiltonian constraint, so '
      'it holds at every k != 0)', xC is not None and len(solC) == 1 and hc == 0 and allG == sp.zeros(10, 1),
      f'solutions {len(solC)}; Hamiltonian residual {hc}')
# de Donder solution: manifestly retarded hbar = c T / (omega^2 - K)
ys = sp.symbols('y0:10'); yv = sp.Matrix(ys)
hd = metric4(yv, PHIG); eta4 = sp.diag(-1, 1, 1, 1); tr4 = sum(eta4[m, m] * hd[m, m] for m in range(4))
hb = hd - eta4 * tr4 / 2; kup = [w, 0, 0, kap]
gauge = [sum(kup[m] * hb[m, n] for m in range(4)) for n in range(4)]
solD = sp.solve(list(MG * yv + jG) + gauge, ys, dict=True)
yD = yv.subs(solD[0])
Tmn = sp.zeros(4, 4); Tmn[0, 0] = rho
for i in range(3):
    Tmn[0, i + 1] = Tmn[i + 1, 0] = J[i]
    for j in range(3): Tmn[i + 1, j + 1] = S[i][j]
hbD = (metric4(yD, PHIG) - eta4 * sum(eta4[m, m] * metric4(yD, PHIG)[m, m] for m in range(4)) / 2)
Tlow = eta4 * Tmn * eta4
ratio = [sp.simplify(hbD[a, b] * (w ** 2 - kap ** 2) / Tlow[a, b]) for a in range(4) for b in range(a, 4) if Tlow[a, b] != 0]
check('B2 [T] control: de Donder gauge gives hbar_mu nu = c T_mu nu/(omega^2 - K) with one constant c for all components, '
      'a covariant, manifestly retarded response', len(set(ratio)) == 1, f'c = {ratio[0]}')
RC = riemann(metric4(xC, PHIC), kz); RD = riemann(metric4(yD, PHIG), kz)
dR = [sp.simplify(RC[key] - RD[key]) for key in RC]
check('B3 [T] the linearised Riemann tensor of the minimal-strain solution equals the de Donder one for every source and every '
      'K: tidal fields, frame dragging and waves are retarded (support in the edge light cone); by rotation covariance of the '
      'construction this holds for every lattice k direction. Gauge-invariant observables do not see the elliptic shift',
      all(d == 0 for d in dR), f'{len(dR)} Riemann components, max residual 0: {all(d == 0 for d in dR)}')
# B4 the shift itself: elliptic symbol P = K delta + kt kt^T, inverse non-polynomial -> instantaneous Kelvin kernel
k1, k2, k3 = sp.symbols('k1:4', real=True); kk = sp.Matrix([k1, k2, k3]); Kk = k1 ** 2 + k2 ** 2 + k3 ** 2
P = Kk * sp.eye(3) + kk * kk.T; Pinv = sp.simplify(P.inv())
target = (sp.eye(3) - kk * kk.T / (2 * Kk)) / Kk
# check the solved shift obeys -P beta = 2 (i k Ktr + j-part) along z: beta3 from solution vs momentum constraint
trk_ = -I * w * (xC[0] + xC[3] + xC[5]) - 2 * I * kap * xC[8]       # tr of kappa_ij = hdot - d beta - d beta = -2 K_ij
rel = sp.simplify(2 * kap ** 2 * xC[8] - (I * kap * trk_ - J[2]))
check('B4 [T] minimal strain is the elliptic equation (K delta + kt kt^T) beta = source, whose inverse '
      '(delta - kt kt^T/2K)/K is not polynomial in kt: beta at x depends instantaneously on the whole slice (Kelvin kernel ~ '
      '(delta + r r/r^2)/8 pi r), sourced by the matter current through the momentum constraint',
      sp.simplify(Pinv - target) == sp.zeros(3, 3) and rel == 0, f'P^-1 = (delta - k k/2K)/K exact; solved shift obeys P beta = i kt tr(kappa) - J (residual {rel})')
# B5 time domain on a 32^3 periodic lattice: current switched on at the origin in one tick
Nl = 32; ks = 2 * np.pi * np.fft.fftfreq(Nl); KX = np.array(np.meshgrid(ks, ks, ks, indexing='ij'))
kt = 2 * np.sin(KX / 2); Kn = (kt ** 2).sum(0); Kn[0, 0, 0] = 1.0
jx = np.zeros((Nl, Nl, Nl)); jx[0, 0, 0] = 1.0; jk = np.fft.fftn(jx)
bx = np.real(np.fft.ifftn(jk / Kn - kt[0] * (kt[0] * jk) / (2 * Kn ** 2))); bx -= bx.mean()
far = [abs(bx[r, 0, 0]) for r in (2, 4, 8)]; lc = np.sin(0.0375) / np.sqrt(3)
check('B5 [D] one tick after a unit current appears at the origin, the minimal-strain shift is already nonzero 8 cubes away '
      '(~1/r), while the edge light cone has advanced sin(eps0)/sqrt3 <= 0.022 cube: the shift (and every edge value read '
      'in its frame) jumps outside the cone; Riemann does not (B3)', far[2] > 1e-3 and far[0] / far[2] > 2,
      f'|beta_x| at r = 2, 4, 8: {far[0]:.4f}, {far[1]:.4f}, {far[2]:.4f}; light per tick {lc:.4f} cube')
# B6 the frame-read edges: zeta (edge trace) in minimal strain carries the Bardeen potential, instantaneous
zC = sp.simplify((xC[0] + xC[3]) / 4)
check('B6 [T] the minimal-strain edges are transverse (kt_j h_ij = 0) and their scalar part is the gauge-invariant Bardeen '
      'Psi = rho/(4K) (Hamiltonian constraint, 16 pi G = 1), a Poisson functional of the energy density: instantaneous in rho, '
      'and in local stresses Psi = kt_i kt_j S_ij/(4 omega^2 K), non-polynomial off the axis. So the floor and the split trigger, '
      'read in this frame, respond at once to distant rearrangements (quadrupole order, monopole and dipole being conserved)',
      sp.simplify(zC - rho / (4 * kap ** 2)) == 0 and xC[2] == 0 and xC[4] == 0 and xC[5] == 0, f'Psi = {sp.factor(zC)}, rho = {sp.factor(rho)}')

print('== C. local hyperbolic alternatives (driver equations; sectors along z, every K)')
def driver(kind, muv, etav):
    """rows: d_t beta = mu Bt, d_t Bt = d_t Gamma - eta Bt; Gamma = d_j(h_ij - delta tr h/3) (Gamma-driver) or d_j h_ij (strain driver)"""
    out = {}
    for s, comp in (('S', 2), ('V', 0)):
        base = sector(MC9, s)                     # unknowns: sector basis
        Ub = [u[:9, :] for u in U[s]]
        n = len(Ub); Bt = sp.Symbol('Bt')
        a = sp.symbols('a0:%d' % n); hq = sum((a[i] * Ub[i] for i in range(n)), sp.zeros(9, 1))
        hcomp = lambda i, j: hq[hidx(i, j)]
        tr = hcomp(0, 0) + hcomp(1, 1) + hcomp(2, 2)
        Gam = I * kap * (hcomp(comp, 2) - (tr / 3 if (kind == 'gamma' and comp == 2) else 0))
        r1 = -I * w * hq[6 + comp] - muv * Bt
        r2 = -I * w * Bt + I * w * Gam + etav * Bt
        rows_ = [list(base.row(i)) + [0] for i in range(n)]
        rows_ += [[sp.expand(r1).coeff(v) for v in list(a) + [Bt]], [sp.expand(r2).coeff(v) for v in list(a) + [Bt]]]
        Mx = sp.Matrix(rows_); m = Mx.shape[1]
        out[s] = sp.factor(sp.gcd_list([Mx.extract(list(r), list(range(m))).det() for r in itertools.combinations(range(Mx.shape[0]), m)]))
    return out
dg = driver('gamma', mu, 0); ds = driver('strain', mu, 0)
def speeds(poly):
    rts = [r for r in sp.solve(sp.Poly(poly, w).as_expr(), w) if r != 0]
    return sorted({sp.simplify(r / kap) for r in rts}, key=lambda x: str(x))
check('C1 [T] Gamma-driver with the read lapse: one longitudinal gauge pair at omega^2 = K(1 + 4 mu)/3 (the lapse adds f = 1/3 '
      'to the standard 4 mu/3) and a transverse pair at omega^2 = mu K; the standard mu = 3/4 moves gauge at 2/sqrt3 > c, '
      'causal only for mu <= 1/2', sp.simplify(dg['S'].subs(w, kap * sp.sqrt((1 + 4 * mu) / 3))) == 0 and
      sp.simplify(dg['V'].subs(w, kap * sp.sqrt(mu))) == 0, f"scalar {dg['S']}; vector {dg['V']}")
check('C2 [T] strain driver (relaxes to minimal strain): longitudinal omega^2 = K(1 + 6 mu)/3, transverse omega^2 = mu K; '
      'every gauge speed <= c iff mu <= 1/3 (mu = 1/3: longitudinal exactly c)', sp.simplify(ds['S'].subs(w, kap * sp.sqrt((1 + 6 * mu) / 3))) == 0
      and sp.simplify(ds['V'].subs(w, kap * sp.sqrt(mu))) == 0, f"scalar {ds['S']}; vector {ds['V']}")
dge = driver('strain', sp.Rational(1, 3), eta)
wc = sp.Symbol('wc'); rts = []
for ev_ in (sp.Rational(1, 2), 5, 50):
    rts.append([complex(r) for r in sp.Poly(dge['S'].subs({kap: 1, eta: ev_}).subs(w, wc), wc).nroots() if abs(complex(r)) > 1e-12])
imag_ok = all(r.imag < 0 for rr in rts for r in rr) and abs(abs(max(rts[2], key=lambda r: r.imag).real) - 1 / np.sqrt(3)) < 0.02
check('C3 [T] with damping eta > 0 every gauge root has Im omega < 0: the driver is stable; as eta grows the slow root tends to '
      'the lapse speed 1/sqrt3 (the frozen-shift limit, still pure gauge because the momentum constraint is kept); the tensor '
      'sector is untouched (the drivers vanish on TT edges)', imag_ok,
      'roots at K = 1, mu = 1/3, eta = 1/2, 5, 50: ' + '; '.join(', '.join(f'{r.real:+.2f}{r.imag:+.2f}i' for r in rr) for rr in rts))
# C4 gauge modes are pure gauge: Riemann of the driver kernel vector vanishes
def driver_kernel_riemann():
    s = 'S'; Ub = [u[:9, :] for u in U[s]]; base = sector(MC9, s); m13 = sp.Rational(1, 3)
    om = kap * sp.sqrt((1 + 6 * m13) / 3)
    a = sp.symbols('a0:3'); Bt = sp.Symbol('Bt')
    hq = sum((a[i] * Ub[i] for i in range(3)), sp.zeros(9, 1))
    r1 = -I * om * hq[8] - m13 * Bt; r2 = -I * om * Bt + I * om * (I * kap * hq[5])
    rws = [list(base.subs(w, om).row(i)) + [0] for i in range(3)]
    rws += [[sp.expand(r1).coeff(v) for v in list(a) + [Bt]], [sp.expand(r2).coeff(v) for v in list(a) + [Bt]]]
    ns = sp.Matrix(rws).nullspace()
    vec = sum((ns[0][i] * Ub[i] for i in range(3)), sp.zeros(9, 1))
    R = riemann(metric4(sp.Matrix(list(vec) + [0]), PHIC), kz)
    return len(ns), all(sp.simplify(R[key].subs(w, om)) == 0 for key in R)
nk, flat = driver_kernel_riemann()
check('C4 [T] the driver modes are pure gauge: their linearised Riemann tensor vanishes, so they carry no energy and no '
      'signal; a hyperbolic shift with gauge speeds <= c keeps every frame-read edge value inside the light cone', nk == 1 and flat,
      f'kernel dim {nk}, Riemann zero {flat}')

print('== D. least squared edge rate vs no component along any site displacement (uniform expansion)')
def lattice(P, periodic):
    sites = list(itertools.product(range(P), repeat=3)); ix = {s: n for n, s in enumerate(sites)}
    dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    rows_, lens = [], []
    for s in sites:
        cand = [(s, d) for d in dirs]
        for a, b in ((0, 1), (0, 2), (1, 2)):           # face diagonal joining even-sum corners
            d = [0, 0, 0]; d[a] = 1; d[b] = 1
            if sum(s) % 2 == 0: cand.append((s, tuple(d)))
            d2 = [0, 0, 0]; d2[a] = 1; d2[b] = -1
            if sum(s) % 2 == 1: cand.append((s, tuple(d2)))
        for s0, d in cand:
            t_ = tuple(s0[i] + d[i] for i in range(3))
            if periodic: t_ = tuple(x % P for x in t_)
            elif not all(0 <= x < P for x in t_): continue
            ev = np.array(d, float); L0 = np.linalg.norm(ev); ev /= L0
            r = np.zeros(3 * len(sites))
            r[3 * ix[t_]:3 * ix[t_] + 3] += ev; r[3 * ix[s0]:3 * ix[s0] + 3] -= ev
            rows_.append(r); lens.append(L0)
    return np.array(rows_), np.array(lens), sites
res = {}
for per in (False, True):
    Jm, Lm, sites = lattice(6, per); rate = 1e-3 * Lm
    u, *_ = np.linalg.lstsq(Jm, rate, rcond=None)
    resid = np.linalg.norm(rate - Jm @ u) / np.linalg.norm(rate)
    interior = [n for n, s in enumerate(sites) if all(0 < x < 5 for x in s)]
    el = np.abs((Jm.T @ rate).reshape(-1, 3)[interior]).max()
    res[per] = (resid, el, np.ptp(u.reshape(-1, 3)[:, 0]))
check('D1 [T] uniform expansion has no component along any interior site displacement (EL form satisfied by zero shift), '
      'but on an open block the least summed squared edge rate removes it completely with beta = -H x (a dilation is a '
      'displacement gradient): read variationally on Z^3 the clause would freeze every edge in an expanding universe and stop '
      'the split cascade. On the torus the two readings agree (beta = 0)', res[False][0] < 1e-9 and res[True][0] > 0.99 and res[False][1] < 1e-12,
      f'open: residual {res[False][0]:.1e}, interior J^T rate {res[False][1]:.0e}, beta spread {res[False][2]:.4f}; periodic: residual {res[True][0]:.3f}')
check('D2 [T] the EL operator (K delta + k k^T) is positive at every k != 0; its kernel on Z^3 is the affine shifts (uniform '
      'translation, rotation, dilation, shear); boundedness (CL-1: at most one cube per tick) leaves only uniform translations '
      '(discrete Liouville): the cap is what makes the elliptic shift unique on the infinite lattice',
      float(np.linalg.eigvalsh(np.einsum('ij,...->...ij', np.eye(3), Kn) + np.einsum('i...,j...->...ij', kt, kt)).min()) > 0.03, 'min eigenvalue K_min = 4 sin^2(pi/32) = 0.038 on the 32^3 grid')

print('== E. gauge = no signal (finite toy, ring of 256 cells)')
Lr = 256; p = 2 * np.pi * np.fft.fftfreq(Lr)
def leak(width, b, gen):
    x = np.arange(Lr); psi = np.exp(-(x - Lr / 2) ** 2 / (4 * width ** 2)) * np.exp(1j * 0.3 * x); psi /= np.linalg.norm(psi)
    ph_ = np.exp(-1j * b * (gen(p) - p))           # matter moved by gen, edges by the exact displacement p
    out = np.fft.ifft(ph_ * np.fft.fft(psi))
    return np.sqrt(max(0.0, 1 - abs(np.vdot(psi, out)) ** 2))
ex = leak(8, 0.5, lambda q: q); d1 = leak(8, 0.5, np.sin); d2 = leak(8, 0.25, np.sin); d3 = leak(16, 0.5, np.sin)
check('E1 [T] a far-controlled displacement generated by the constraint itself leaves the relational state (matter relative to '
      'edges) unchanged to machine precision; a matter transport whose dispersion differs from the edge displacement at '
      'O(k^2) (lattice momentum sin p vs p) leaks a distance linear in the shift and set by the packet momentum spread',
      ex < 1e-12 and 1.8 < d1 / d2 < 2.2, f'exact {ex:.0e}; mismatched b = 0.5: {d1:.2e}, b = 0.25: {d2:.2e}, width x2: {d3:.2e}')

print('== F. estimates against measurement')
for e0 in (0.0075, 0.0375):
    cc = np.sin(e0) / np.sqrt(3)
    print(f'  eps0 {e0}: light {cc:.4f} cube/tick; the cap is {1 / cc:.0f} c; PG shift sqrt(r_s/r) c binds at r < {cc ** 2:.1e} r_s')
GM_c2 = 6.674e-11 * 1.0 / 9e16
rb = [np.sin(e0) ** 2 / 3 for e0 in (0.0075, 0.0375)]
check('F1 [E] the one-cube-per-tick cap never binds outside horizons (minimal strain = Painleve-Gullstrand, zero strain, for '
      'Schwarzschild; |beta| <= c at the horizon; Kerr frame dragging and binaries < c) nor in cosmology (EL form: beta = 0); it '
      'binds only at r < (sin^2 eps0/3) r_s, matching collapse-shift C3 (1.9e-5, 4.7e-4)', abs(rb[0] / 1.9e-5 - 1) < 0.03 and abs(rb[1] / 4.7e-4 - 1) < 0.03,
      f'r_bind/r_s {rb[0]:.2e} to {rb[1]:.2e}')
check('F2 [E] instantaneous frame-read edge change from a lab rearrangement (1 kg moved 1 m, read 1 m away, quadrupole) ~ '
      'G m/(c^2 r) ~ 7e-28 per edge; signal through a split timing needs a register at the trigger within that margin: '
      'acausal in principle, far below any test', GM_c2 < 1e-27, f'G m/c^2 r = {GM_c2:.1e}')
print('supplied: continuum-form ADM quadratic action with the consistent lattice derivative (A4 relaxes it); test sources;')
print('  the 1D dispersion toy (E); drivers of Gamma and strain type with mu, eta. not built: register-level CL-1 insertion,')
print('  nonlinear minimal strain, the lattice momentum-constraint algebra off flat cells.')
print(f'elapsed {time.time() - t0:.1f} s')
print(f'TOTAL: PASS={NP[0]} FAIL={NP[1]}')
