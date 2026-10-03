"""A25 check 3: unstaggered (collocated) alternatives.
U1 central differences, all six components at every site: exact gauge invariance, constraint rows,
   all 48 site-centred rotations; spectrum: gapless at all 8 zone corners (7 doublers)
U2 'tastes': the central-difference theory on Z^3 (side 2L) equals EXACTLY the direct sum of the
   staggered theory over the 8 role translates (V scaled by 1/4)
U3 Wilson-type lift: doublers lifted but exact gauge invariance lost; constraint drift; mode count
U4 one-sided differences at sites: gauge invariance lost; S1 'ownership' storage of the staggered theory:
   exact gauge invariance but site-centred rotation covariance only for the 3 rotations fixing an octant
U5 representation theory at the zone corners (characters): collocated vs staggered ('twisted')
U6 limiting gauge directions at the corners for several covariant collocated generators (symbols)
U7 all covariant, local (range<=2), exactly gauge-invariant potentials for those generators:
   common kernel at each zone corner
Supplied toy only."""
import sys, time, itertools
import numpy as np
import scipy.sparse as sp
from stag2 import *

t0 = time.time()
tau = 0.5
rng = np.random.default_rng(11)
Oh = signed_perms(); O = signed_perms(proper=True)

# ---------------------------------------------------------------- U1
N = 6
opc = build(N, 'central'); latc = opc['lat']; nc = latc.n
Dc, Vc, Mc, Rc, Divc = (opc[k] for k in ('D', 'Vp', 'Mp', 'R', 'Div'))
print(f'U1 central differences, N={N}:  |Vc Dc| = {maxabs(Vc @ Dc)}, |Rc Dc| = {maxabs(Rc @ Dc)}, '
      f'|Rc Mc + Divc Dc^T| = {maxabs(Rc @ Mc + Divc @ Dc.T)}  (exact)')
ok = all(maxabs(O_ @ Vc @ O_.T - Vc) == 0 and maxabs(O_ @ Mc @ O_.T - Mc) == 0
         for O_ in (rot_matrix(latc, H_OFF, 'sym2', Rm, (0, 0, 0), mode='central') for Rm in Oh))
print(f'   all 48 rotations about a site commute exactly with both layers: {ok}')
ks = kgrid(N)
Vk = bloch(latc, Vc, H_OFF, H_OFF, ks, mode='central')
zero_V = [tuple(np.round(k / np.pi, 3)) for ik, k in enumerate(ks) if np.abs(Vk[ik]).max() < 1e-12]
dev = max(np.abs(np.linalg.inv(S_ORTH) @ Vk[ik] @ np.linalg.inv(S_ORTH) - V_EH_orth(np.sin(k))).max()
          for ik, k in enumerate(ks))
print(f'   symbol = V_EH(sin k): max dev {dev:.1e};  momenta where the potential vanishes identically: {len(zero_V)} -> {zero_V}')
# near-corner TT dispersion (from the real-space stencil)
K1c, P1c, K2c = layers_hp(opc, tau)
Uc = (K2c @ P1c @ K1c).tocsr()
Z12 = H_OFF + H_OFF
T = np.block([[S_ORTH, np.zeros((6, 6))], [np.zeros((6, 6)), np.linalg.inv(S_ORTH)]])
for Kc in ([np.pi, 0, 0], [np.pi, np.pi, 0], [np.pi, np.pi, np.pi]):
    q = 1e-3 * np.array([0.3, -0.5, 0.8])
    kk = np.array([np.array(Kc) + q])
    Uq = T @ bloch(latc, Uc, Z12, Z12, kk, mode='central')[0] @ np.linalg.inv(T)
    ev = np.linalg.eigvals(Uq); ph = np.sort(np.abs(np.angle(ev)))[::-1][:4]
    print(f'   near corner {np.round(np.array(Kc)/np.pi).astype(int)}*pi: 4 largest |phase|/(tau|q|) = {np.round(ph/(tau*np.linalg.norm(q)), 5)}  (a full second massless graviton)')

# ---------------------------------------------------------------- U2
Ls = N // 2
ops = build(Ls, 'stag'); lat = ops['lat']; n = lat.n
site = lambda y: ((y[..., 0] % N) * N + (y[..., 1] % N)) * N + (y[..., 2] % N)


def emb(offs, s):
    rows, cols = [], []
    for c, o in enumerate(offs):
        y = 2 * lat.coords + np.array(o) + np.array(s)
        rows += list(c * nc + site(y)); cols += list(c * n + np.arange(n))
    return sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(offs) * nc, len(offs) * n))


pats = list(itertools.product((0, 1), repeat=3))
EH = {s: emb(H_OFF, s) for s in pats}; EX = {s: emb(XI_OFF, s) for s in pats}
part = maxabs(sum(EH[s] @ EH[s].T for s in pats) - sp.identity(6 * nc))
sumV = sum(EH[s] @ ops['Vp'] @ EH[s].T for s in pats)
sumM = sum(EH[s] @ ops['Mp'] @ EH[s].T for s in pats)
sumD = sum(EH[s] @ ops['D'] @ EX[s].T for s in pats)
print(f'U2 tastes (side {N} = 2x{Ls}): the 8 role translates partition the collocated components: |sum E E^T - I| = {part}')
print(f'   |Vc - (1/4) sum_s E_s Vstag E_s^T| = {maxabs(Vc - 0.25 * sumV)};  |Mc - sum_s E_s Mstag E_s^T| = {maxabs(Mc - sumM)};  '
      f'|Dc - (1/2) sum_s E_s Dstag E_s^T| = {maxabs(Dc - 0.5 * sumD)}  (exact)')

# ---------------------------------------------------------------- U3
r = 0.25
Lap = [latc.Sp[a] - 2 * latc.I + latc.Sm[a] for a in range(3)]
W1 = sum(Lp.T @ Lp for Lp in Lap)
W = sp.kron(sp.diags([1, 1, 1, 2, 2, 2]), W1, format='csr') * r
VW = (Vc + W).tocsr()
print(f'U3 Wilson-type term r*sum_a |Delta_a h|^2 (r={r}): gauge invariance |(Vc+W) Dc| = {maxabs(VW @ Dc):.3f} (lost); '
      f'rotations still exact: {all(maxabs(O_ @ VW @ O_.T - VW) == 0 for O_ in (rot_matrix(latc, H_OFF, "sym2", Rm, (0,0,0), mode="central") for Rm in Oh))}')
opW = dict(opc); opW['Vp'] = VW
KW1, PW, KW2 = layers_hp(opW, tau)
UW = (KW2 @ PW @ KW1).tocsr()
UWk = bloch(latc, UW, Z12, Z12, ks, mode='central')
nprop = []; maxmod = 0.0; corner_info = []
for ik, k in enumerate(ks):
    ev = np.linalg.eigvals(UWk[ik])
    maxmod = max(maxmod, np.abs(ev).max())
    nprop.append(int(np.sum(np.abs(ev - 1) > 1e-6)))
    if np.all(np.isclose(np.abs(k), np.pi) | np.isclose(k, 0)) and not np.allclose(k, 0):
        corner_info.append((tuple(np.round(k / np.pi).astype(int)), round(float(np.abs(ev).max()), 3)))
print(f'   with W: non-unit eigenvalues per k range {min(nprop)}..{max(nprop)} of 12 (gauge directions now move); max |eig| over zone {maxmod:.3f}')
print(f'   corners (k/pi, max|eig|): {corner_info}  (|eig|>1: the indefinite DeWitt trace mode is driven unstable)')
# traceless-only Wilson term (no potential on the conformal trace): stability vs extra modes
Ptl = np.eye(3) - np.ones((3, 3)) / 3
Wtl = sp.kron(sp.csr_matrix(np.block([[Ptl, np.zeros((3, 3))], [np.zeros((3, 3)), 2 * np.eye(3)]])), W1, format='csr') * r
optl = dict(opc); optl['Vp'] = (Vc + Wtl).tocsr()
A1_, A2_, A3_ = layers_hp(optl, tau)
Utl = (A3_ @ A2_ @ A1_).tocsr()
Utlk = bloch(latc, Utl, Z12, Z12, ks, mode='central')
npr2 = [int(np.sum(np.abs(np.linalg.eigvals(Utlk[ik]) - 1) > 1e-6)) for ik in range(len(ks))]
mm2 = max(np.abs(np.linalg.eigvals(Utlk[ik])).max() for ik in range(len(ks)))
print(f'   traceless-only Wilson term: |(Vc+Wtl) Dc| = {maxabs(optl["Vp"] @ Dc):.3f}; non-unit eigenvalues per k {min(npr2)}..{max(npr2)} of 12 '
      f'(vs 4 for the gauge-invariant tick); max |eig| {mm2:.3f}')
Dd = Dc.toarray(); Rd = Rc.toarray()
p0 = rng.normal(size=6 * nc); h0 = rng.normal(size=6 * nc)
p0 -= Dd @ np.linalg.lstsq(Dd, p0, rcond=None)[0]; h0 -= Rd.T @ np.linalg.lstsq(Rd.T, h0, rcond=None)[0]
for name, (A1, A2, A3) in (('without W', (K1c, P1c, K2c)), ('with W   ', (KW1, PW, KW2))):
    z = np.concatenate([h0, p0]); mx = 0.0
    for _ in range(20):
        z = A3 @ A2 @ A1 @ z
        mx = max(mx, np.abs(Dc.T @ z[6 * nc:]).max())
    print(f'   momentum row |Dc^T p| over 20 ticks from constraint-surface data, {name}: {mx:.1e}')

# ---------------------------------------------------------------- U4
opf = build(N, 'forward')
fgood = [Rm for Rm in Oh if maxabs((lambda O_: O_ @ opf["Vp"] @ O_.T - opf["Vp"])(rot_matrix(opf["lat"], H_OFF, "sym2", Rm, (0,0,0), mode="forward"))) == 0]
print(f'U4 one-sided (forward) differences at sites: gauge invariance |Vf Df| = {maxabs(opf["Vp"] @ opf["D"]):.3f} (lost); '
      f'site rotations commuting with Vf: {len(fgood)}/48 ({sum(round(np.linalg.det(g)) > 0 for g in fgood)}/24 proper); '
      f'sign patterns of those: {sorted(set(tuple(perm_sign(g)[1]) for g in fgood))}')
# S1 ownership: staggered theory, each site stores its vertex and its three 'up' faces; a site-centred rotation
# that only relabels components on the site (no re-ownership) is a symmetry only if it fixes the up-octant
opS = build(N, 'stag')
good = [Rm for Rm in Oh if maxabs((lambda O_: O_ @ opS['Vp'] @ O_.T - opS['Vp'])(
    rot_matrix(opS['lat'], H_OFF, 'sym2', Rm, (0, 0, 0), mode='central'))) == 0]
print(f'   S1 ownership storage (exactly gauge-invariant): on-site-relabelling rotations about a site that commute with Vp: '
      f'{len(good)}/48 ({sum(round(np.linalg.det(g)) > 0 for g in good)}/24 proper) = the rotations fixing the (+,+,+) octant')

# ---------------------------------------------------------------- U5 representation theory at the corners
def rho_sym(Rm):
    P, sg = perm_sign(Rm)
    M = np.zeros((6, 6))
    for a, (i, j) in enumerate(H_PAIR):
        M[hidx(P[i], P[j]), a] = sg[i] * sg[j]
    return M


def twist(Rm, K, offs):
    n_ = np.round((Rm @ K - K) / (2 * np.pi)).astype(int)
    return np.diag([(-1) ** int(n_ @ np.array(o)) for o in offs])


def little(G, K):
    return [Rm for Rm in G if np.allclose(((Rm @ K - K) / (2 * np.pi)) % 1, 0)]


def hom_dim(G, repA, repB):
    return round(sum(np.trace(repA(g)) * np.trace(repB(g)) for g in G) / len(G), 6)


print('U5 dim Hom_G(gauge vector -> symmetric tensor) at the zone corners (G = little group of K):')
for Kn in ([1, 0, 0], [1, 1, 0], [1, 1, 1]):
    K = np.pi * np.array(Kn, float)
    for gname, G in (('O ', O), ('Oh', Oh)):
        Gk = little(G, K)
        hc = hom_dim(Gk, lambda g: g.astype(float), rho_sym)
        hs = hom_dim(Gk, lambda g: twist(g, K, XI_OFF) @ np.abs(g) * 0 + (twist(g, K, XI_OFF) @ g),
                     lambda g: twist(g, K, H_OFF) @ rho_sym(g))
        print(f'   K={Kn} pi, {gname} (|G_K|={len(Gk):2d}): collocated {hc:.0f};  staggered (twisted) {hs:.0f}')


def irreps_O(g):
    P, sg = perm_sign(g)
    sgnP = round(np.linalg.det(np.abs(g)))
    tr = np.trace(g)
    # E character: 2 on identity-perm classes(E, C2axes), -1 on C3, 0 on C4/C2'
    if list(P) == [0, 1, 2]:
        chiE = 2
    elif sgnP > 0:
        chiE = -1
    else:
        chiE = 0
    return {'A1': 1, 'A2': sgnP, 'E': chiE, 'T1': tr, 'T2': sgnP * tr}


K = np.pi * np.ones(3)
for lbl, block in (('diagonal', slice(0, 3)), ('off-diagonal', slice(3, 6))):
    for name, rep in (('collocated', lambda g: rho_sym(g)), ('staggered', lambda g: twist(g, K, H_OFF) @ rho_sym(g))):
        mult = {ir: round(sum(np.trace(rep(g)[block, block]) * irreps_O(g)[ir] for g in O) / 24, 6) for ir in ('A1', 'A2', 'E', 'T1', 'T2')}
        print(f'   K=(pi,pi,pi), {lbl:12s} components, {name:10s}: ' + ', '.join(f'{k}:{v:.0f}' for k, v in mult.items() if abs(v) > 1e-9))
xi_tw = {ir: round(sum(np.trace(twist(g, K, XI_OFF) @ g) * irreps_O(g)[ir] for g in O) / 24, 6) for ir in ('A1', 'A2', 'E', 'T1', 'T2')}
print('   K=(pi,pi,pi), gauge vector, staggered: ' + ', '.join(f'{k}:{v:.0f}' for k, v in xi_tw.items() if abs(v) > 1e-9))


# ---------------------------------------------------------------- U6 generator symbols
def c2(x):
    return (1 + np.cos(x)) / 2


def gen(kind, lam=0.5):
    def D(k):
        M = np.zeros((6, 3), complex)
        for i in range(3):
            M[hidx(i, i), i] = 2j * np.sin(k[i])
        for (i, j) in ((0, 1), (0, 2), (1, 2)):
            m = 3 - i - j
            if kind in ('central', 'chiral'):
                fj, fi = 1.0, 1.0
            elif kind in ('smear1', 'smear1+chiral'):
                fj, fi = c2(k[j]), c2(k[i])
            elif kind == 'smear2':
                fj, fi = c2(k[j]) * c2(k[m]), c2(k[i]) * c2(k[m])
            M[hidx(i, j), j] += 1j * np.sin(k[i]) * fj
            M[hidx(i, j), i] += 1j * np.sin(k[j]) * fi
        if 'chiral' in kind:
            M[hidx(0, 1), 2] += lam * (np.cos(k[0]) - np.cos(k[1]))
            M[hidx(1, 2), 0] += lam * (np.cos(k[1]) - np.cos(k[2]))
            M[hidx(0, 2), 1] += lam * (np.cos(k[2]) - np.cos(k[0]))
        return M
    return D


def covariant(D, G):
    err = 0.0
    for _ in range(5):
        k = rng.uniform(-np.pi, np.pi, 3)
        for g in G:
            err = max(err, np.abs(D(g @ k) - rho_sym(g) @ D(k) @ g.T).max())
    return err


def limit_span_dim(D, K, eps=1e-3, ndir=300):
    dirs = list(rng.normal(size=(ndir, 3))) + [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]
    bases = []
    for q in dirs:
        q = q / np.linalg.norm(q)
        u, s, vh = np.linalg.svd(D(K + eps * q))
        rnk = int(np.sum(s > 1e-9 * max(s[0], 1e-300)))
        bases.append(u[:, :rnk])
    Bst = np.hstack(bases)
    sv = np.linalg.svd(Bst, compute_uv=False)
    return int(np.sum(sv > 0.1 * sv[0]))


corners = {'(pi,0,0)': np.pi * np.array([1., 0, 0]), '(pi,pi,0)': np.pi * np.array([1., 1, 0]),
           '(pi,pi,pi)': np.pi * np.ones(3)}
print('U6 covariant collocated gauge generators: covariance error (O, Oh) and dim of limiting gauge span S_K at corners')
print('   (dim S_K >= 5 forces a zero-frequency transverse mode at K; see report)')
for kind in ('central', 'smear1', 'smear2', 'chiral', 'smear1+chiral'):
    D = gen(kind)
    cO, cOh = covariant(D, O), covariant(D, Oh)
    k0 = 1e-4 * np.array([0.3, 0.5, -0.2])
    clim = np.abs(D(k0) / 1e-4 - gen('central')(k0) / 1e-4).max()
    dims = {nm: limit_span_dim(D, K) for nm, K in corners.items()}
    print(f'   {kind:14s}: cov err O {cO:.0e}, Oh {cOh:.0e}; IR = central to {clim:.0e}; dim S_K: {dims}')


# ---------------------------------------------------------------- U7 gauge-invariant potentials, range <= 2
R2 = 2
offs_n = [np.array(v) for v in itertools.product(range(-R2, R2 + 1), repeat=3)]
nidx = {tuple(v): i for i, v in enumerate(offs_n)}
nO = len(offs_n)


def V_of_k(vec, k):
    Vn = vec.reshape(nO, 6, 6)
    ph = np.exp(1j * np.array(offs_n) @ k)
    return np.einsum('n,nab->ab', ph, Vn)


def invariant_basis(G):
    cols = []
    seen = set()
    for v in offs_n:
        orb = frozenset(tuple(g @ v) for g in G)
        if orb in seen:
            continue
        seen.add(orb)
        for a in range(6):
            for b in range(6):
                X = np.zeros((nO, 6, 6))
                for g in G:
                    rg = rho_sym(g)
                    E = np.zeros((6, 6)); E[a, b] = 1
                    X[nidx[tuple(g @ v)]] += rg @ E @ rg.T
                    X[nidx[tuple(-(g @ v))]] += (rg @ E @ rg.T).T
                cols.append(X.ravel())
    A = np.array(cols).T
    u, s, vh = np.linalg.svd(A, full_matrices=False)
    return u[:, s > 1e-8 * s[0]]


print('U7 covariant local potentials (range<=2 in each direction), exactly gauge-invariant under each generator:')
for gname, G in (('O', O),):
    Bv = invariant_basis(G)
    print(f'   group {gname}: {Bv.shape[1]} covariant Hermitian range-2 forms')
    kt = [rng.uniform(-np.pi, np.pi, 3) for _ in range(40)]
    for kind in ('central', 'smear1', 'chiral', 'smear1+chiral'):
        D = gen(kind)
        rows = []
        for k in kt:
            Dk = D(k)
            blk = np.array([(V_of_k(Bv[:, a], k) @ Dk).ravel() for a in range(Bv.shape[1])]).T
            rows += [blk.real, blk.imag]
        Asys = np.vstack(rows)
        u, s, vh = np.linalg.svd(Asys, full_matrices=True)
        null = vh[np.sum(s > 1e-9 * s[0]):].T
        coef = Bv @ null
        # check EH-type member exists for 'central'
        info = f'{null.shape[1]:3d} gauge-invariant forms'
        ck = []
        for nm, K in corners.items():
            Ms = [V_of_k(coef[:, a], K) for a in range(coef.shape[1])]
            if Ms:
                st = np.vstack(Ms)
                sv = np.linalg.svd(st, compute_uv=False)
                kerdim = 6 - int(np.sum(sv > 1e-8 * max(1.0, sv[0])))
            else:
                kerdim = 6
            ck.append(f'{nm}: common kernel {kerdim}')
        # generic member: nonzero eigenvalues of V(k) at random k (should be 3 = rank of physical quotient)
        cgen = coef @ rng.normal(size=coef.shape[1]) if coef.shape[1] else None
        rk = []
        if cgen is not None:
            for k in kt[:5]:
                ev = np.linalg.eigvalsh(V_of_k(cgen, k))
                rk.append(int(np.sum(np.abs(ev) > 1e-8 * np.abs(ev).max())))
        print(f'   {kind:14s}: {info}; ' + '; '.join(ck) + f'; generic member rank at random k: {rk}')
print(f'done in {time.time() - t0:.1f}s')
