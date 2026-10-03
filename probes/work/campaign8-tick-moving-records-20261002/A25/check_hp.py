"""A25 check 1: staggered real-space (h,p) leapfrog for the linear spin-2 toy.
P1 exact operator identities (gauge invariance, Bianchi, Hamiltonian-row propagation)
P2 Bloch symbols of the real-space operators vs A23's symbols (V_EH(s), DeWitt M, leapfrog U)
P3 spectrum on the L^3 torus: TT phases, polarization count, doublers, pi-phases, power traces
P4 constraint preservation layer by layer on a random constraint-surface trajectory
P5 cubic covariance: all 48 signed permutations about a vertex and a cube centre; face/edge centres
P6 reach of each layer in three encodings (staggered geometry; S1 cell ownership; S2 parity roles)
P7 exactly conserved local quadratic form; exact inverse
P8 infrared z=1 from the real-space stencil; real-space plane-wave phase
Supplied toy only.  tau = 1/2 (dyadic) so P1/P5/P7 identities are exact in floating point."""
import sys, time
import numpy as np
import scipy.sparse as sp
from stag2 import *

t0 = time.time()
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
tau = 0.5
rng = np.random.default_rng(20261003)
ops = build(L, 'stag')
lat = ops['lat']; n = lat.n
D, Vp, Mp, R, Div, Curl, J = (ops[k] for k in ('D', 'Vp', 'Mp', 'R', 'Div', 'Curl', 'J'))
print(f'L={L}  cells={n}  dim(h)={6*n}  dim(C)={9*n}  tau={tau}')

# ---------------------------------------------------------------- P1
print('P1 exact identities (max |entry|; 0.0 means exactly zero):')
print(f'   gauge invariance  |Vp D|            = {maxabs(Vp @ D)}')
print(f'   Ham. row gauge inv |R D|            = {maxabs(R @ D)}')
print(f'   Ham. row propagation |R Mp + Div D^T| = {maxabs(R @ Mp + Div @ D.T)}')
print(f'   Bianchi |div1C Curl|, |trC Curl|     = {maxabs(ops["div1C"] @ Curl)}, {maxabs(ops["trC"] @ Curl)}')
print(f'   R written on C: |RC Curl - R|        = {maxabs(ops["RC"] @ Curl - R)}')
print(f'   symmetry |Vp - Vp^T|                = {maxabs(Vp - Vp.T)}')
print(f'   Vp rank deficiency check: nnz per row max {np.diff(Vp.indptr).max()}')

# ---------------------------------------------------------------- P2
ks = kgrid(L)
Vk = bloch(lat, Vp, H_OFF, H_OFF, ks)
Mk = bloch(lat, Mp, H_OFF, H_OFF, ks)
Vk2 = bloch(lat, Vp, H_OFF, H_OFF, ks, ref_cell=n // 2 + 1)
errV = errM = 0.0
Mgr = M_orth_GR()
for ik, k in enumerate(ks):
    s = 2 * np.sin(k / 2)
    Vor = np.linalg.inv(S_ORTH) @ Vk[ik] @ np.linalg.inv(S_ORTH)
    Mor = S_ORTH @ Mk[ik] @ S_ORTH
    errV = max(errV, np.abs(Vor - V_EH_orth(s)).max())
    errM = max(errM, np.abs(Mor - Mgr).max())
print(f'P2 Bloch symbol of real-space Vp vs A23 V_EH(s), s=2sin(k/2): max dev {errV:.1e} over {len(ks)} k')
print(f'   Bloch symbol of Mp vs A23 DeWitt weights 2(-1/2 A1 + E + T2): max dev {errM:.1e}')
print(f'   translation invariance (two reference cells): {np.abs(Vk - Vk2).max():.1e}')

# full one-step map
K1, P1_, K2 = layers_hp(ops, tau)
U = (K2 @ P1_ @ K1).tocsr()
Z12 = H_OFF + H_OFF
Uk = bloch(lat, U, Z12, Z12, ks)
T = np.block([[S_ORTH, np.zeros((6, 6))], [np.zeros((6, 6)), np.linalg.inv(S_ORTH)]])
errU = 0.0
for ik, k in enumerate(ks):
    s = 2 * np.sin(k / 2)
    V = V_EH_orth(s)
    I6, Z6 = np.eye(6), np.zeros((6, 6))
    Ka = np.block([[I6, tau / 2 * Mgr], [Z6, I6]]); Pb = np.block([[I6, Z6], [-tau * V, I6]])
    UA23 = Ka @ Pb @ Ka
    errU = max(errU, np.abs(T @ Uk[ik] @ np.linalg.inv(T) - UA23).max())
print(f'   Bloch block of the real-space tick vs A23 leapfrog symbol: max dev {errU:.1e}')

# ---------------------------------------------------------------- P3
nprop, minth, maxth, ferr, trerr, leak = [], np.inf, 0.0, 0.0, 0.0, 0.0
zero_k = []
for ik, k in enumerate(ks):
    Ukk = T @ Uk[ik] @ np.linalg.inv(T)
    s = 2 * np.sin(k / 2)
    if np.allclose(k, 0):
        # k=0: tick must be unipotent (all eigenvalues 1)
        ev = np.linalg.eigvals(Ukk)
        zero_k.append(('k=0', np.abs(ev - 1).max()))
        continue
    Tt = tt_basis_orth(s)
    Pp = np.zeros((12, 4)); Pp[:6, :2] = Tt; Pp[6:, 2:] = Tt
    blk = Pp.T @ Ukk @ Pp
    leak = max(leak, np.linalg.norm(Ukk @ Pp - Pp @ blk))
    ev = np.linalg.eigvals(blk)
    th = np.abs(np.angle(ev))
    minth = min(minth, th.min()); maxth = max(maxth, th.max())
    ferr = max(ferr, np.abs(np.cos(th) - (1 - tau ** 2 * (s @ s) / 2)).max())
    Uj = np.eye(12)
    for j in range(1, 13):
        Uj = Uj @ Ukk
        trerr = max(trerr, abs(np.trace(Uj) - (8 + np.sum(ev ** j).real)))
    nprop.append(int(np.sum(th > 1e-9)))
print(f'P3 k=0: max |eig-1| = {zero_k[0][1]:.1e} (no propagating mode at k=0)')
print(f'   k!=0 ({len(ks)-1} momenta): TT-block leak {leak:.1e}; spectrum = 1 x8 + TT (power traces j=1..12) max dev {trerr:.1e}')
print(f'   propagating eigenvalues per k (TT block): min {min(nprop)}, max {max(nprop)}  (=4: two polarizations, +-theta)')
print(f'   TT phase range over k!=0: min {minth:.4f} rad, max {maxth/np.pi:.4f} pi;  |cos th-(1-tau^2 s^2/2)| max {ferr:.1e}')
smin = min(np.linalg.norm(2 * np.sin(k / 2)) for k in ks if not np.allclose(k, 0))
print(f'   smallest nonzero |s| on grid {smin:.4f}; expected min phase 2asin(tau|s|/2) = {2*np.arcsin(tau*smin/2):.4f}  (no extra zero-phase momentum = no doubler)')

# ---------------------------------------------------------------- P4
# random data on the constraint surface: p in ker D^T, h in ker R
Dd = D.toarray(); Rd = R.toarray()
p0 = rng.normal(size=6 * n); h0 = rng.normal(size=6 * n)
p0 -= Dd @ np.linalg.lstsq(Dd, p0, rcond=None)[0]          # project out range(D) -> D^T p = 0
h0 -= Rd.T @ np.linalg.lstsq(Rd.T, h0, rcond=None)[0]      # project out range(R^T) -> R h = 0
z = np.concatenate([h0, p0])
c0 = (np.abs(D.T @ p0).max(), np.abs(R @ h0).max())
worst_m = worst_H = 0.0
nD, nR = abs(D).max(), abs(R).max()
for step in range(200):
    for Lyr in (K1, P1_, K2):
        z = Lyr @ z
        worst_m = max(worst_m, np.abs(D.T @ z[6 * n:]).max() / (nD * np.abs(z[6 * n:]).max()))
        worst_H = max(worst_H, np.abs(R @ z[:6 * n]).max() / (nR * np.abs(z[:6 * n]).max()))
scale = np.abs(z).max()
force = np.abs(Vp @ z[:6 * n]).max()          # gauge-invariant (Vp D = 0): stays bounded
print(f'P4 constraint-surface trajectory, 200 ticks x 3 layers: initial rows ({c0[0]:.1e},{c0[1]:.1e}); '
      f'max over every layer, relative to field size: |D^T p| {worst_m:.1e}, |R h| {worst_H:.1e}')
print(f'   field size {scale:.1f} (grows linearly along pure-gauge directions only); gauge-invariant force |Vp h| = {force:.2f} stays O(1)')
# off-surface: D^T p exactly conserved by every layer, R h changes only through Div D^T p
p1 = rng.normal(size=6 * n); h1 = rng.normal(size=6 * n); z = np.concatenate([h1, p1])
g0 = D.T @ p1; r0 = R @ h1
for Lyr in (K1, P1_, K2):
    z = Lyr @ z
print(f'   generic data, one tick: |D^T p - D^T p0| = {np.abs(D.T @ z[6*n:] - g0).max():.1e}; '
      f'|R h - (R h0 - tau Div D^T p0)| = {np.abs(R @ z[:6*n] - (r0 - tau * (Div @ g0))).max():.1e}')

# ---------------------------------------------------------------- P5
Oh = signed_perms()
res = {}
for cname, cb in (('vertex', (0, 0, 0)), ('cube', (1, 1, 1)), ('face12', (1, 1, 0)), ('edge1', (1, 0, 0))):
    ok_all, nsym, nprop_ok = True, 0, 0
    for Rm in Oh:
        OH = rot_matrix(lat, H_OFF, 'sym2', Rm, cb)
        if OH is None:
            continue
        nsym += 1
        OX = rot_matrix(lat, XI_OFF, 'vec', Rm, cb)
        OS = rot_matrix(lat, VERT_OFF, 'scalar', Rm, cb)
        if OX is None or OS is None:
            ok_all = False
            continue
        e1 = maxabs(OH @ Vp @ OH.T - Vp); e2 = maxabs(OH @ Mp @ OH.T - Mp)
        e3 = maxabs(OH @ D @ OX.T - D)
        e4 = maxabs(OS @ R @ OH.T - R)
        if max(e1, e2, e3, e4) != 0.0:
            ok_all = False
        if round(np.linalg.det(Rm)) > 0:
            nprop_ok += 1
    res[cname] = (nsym, nprop_ok, ok_all)
for cname, (nsym, npr, ok) in res.items():
    print(f'P5 rotations about a {cname:6s} centre that map every role to its relabelled role: {nsym}/48 '
          f'({npr}/24 proper); all layers (Vp, Mp) and D, R commute EXACTLY: {ok}')

# ---------------------------------------------------------------- P6
def reach(Mat, offs, frame):
    Mat = Mat.tocoo()
    nn = n
    r_c, r_x = np.divmod(Mat.row, nn); c_c, c_x = np.divmod(Mat.col, nn)
    keep = (Mat.row != Mat.col) & (Mat.data != 0)
    oR = np.array([offs[c] for c in r_c[keep]]); oC = np.array([offs[c] for c in c_c[keep]])
    xr = lat.coords[r_x[keep]]; xc = lat.coords[c_x[keep]]
    if frame == 'geom':        # staggered geometric positions, units of the vertex spacing
        d = (xc - xr + L // 2) % L - L // 2 + (oC - oR) / 2.0
        return np.sqrt((d ** 2).sum(1)).max()
    if frame == 'S1':          # site = cell (vertex owns its 3 up-faces)
        d = (xc - xr + L // 2) % L - L // 2
    if frame == 'S2':          # Z^3 sites 2x+o on the 2L torus (parity-role encoding)
        N = 2 * L
        d = ((2 * xc + oC) - (2 * xr + oR) + N // 2) % N - N // 2
    return np.abs(d).sum(1).max(), np.abs(d).max(1).max()

for name, Lyr in (('h-layer K(tau/2)', K1), ('p-layer P(tau)', P1_)):
    g = reach(Lyr, Z12, 'geom'); s1 = reach(Lyr, Z12, 'S1'); s2 = reach(Lyr, Z12, 'S2')
    print(f'P6 {name}: max Euclidean reach (staggered units) {g:.4f}; S1 cell reach Manhattan/Chebyshev {s1}; '
          f'S2 Z^3 reach Manhattan/Chebyshev {s2}')
Pc = (Vp != 0).astype(int)
inputs_per_row = np.diff(Pc.tocsr().indptr)
print(f'   p-layer inputs per output component: {sorted(set(inputs_per_row.tolist()))}')

# ---------------------------------------------------------------- P7
E = sp.bmat([[Vp, None], [None, Mp - (tau ** 2 / 4) * (Mp @ Vp @ Mp)]], format='csr')
print(f'P7 conserved local quadratic form  |U^T E U - E| = {maxabs(U.T @ E @ U - E)}  (exact)')
Ki, Pi, Ki2 = layers_hp(ops, -tau)
print(f'   exact inverse |U(-tau) U(tau) - I| = {maxabs(Ki2 @ Pi @ Ki @ U - sp.identity(12 * n))}')
# positivity on TT for tau<1/sqrt3: TT weight of the p-block = 2 - tau^2 |s|^2 /2 >= 2 - 6 tau^2
print(f'   TT kinetic weight of E at the zone corner: 2 - 6 tau^2 = {2 - 6 * tau ** 2:+.3f} (>0 iff tau<1/sqrt3)')

# ---------------------------------------------------------------- P8
kir = 1e-3 * np.array([0.37, -0.81, 0.45]); kir2 = np.array([[*kir]])
Uir = T @ bloch(lat, U, Z12, Z12, kir2)[0] @ np.linalg.inv(T)
s = 2 * np.sin(kir / 2); Tt = tt_basis_orth(s)
Pp = np.zeros((12, 4)); Pp[:6, :2] = Tt; Pp[6:, 2:] = Tt
th = np.abs(np.angle(np.linalg.eigvals(Pp.T @ Uir @ Pp))).max()
print(f'P8 infrared from the real-space stencil: theta/(tau|k|) = {th / (tau * np.linalg.norm(kir)):.8f} at |k|={np.linalg.norm(kir):.1e}  (z=1, speed 1)')
# real-space TT plane wave (cosine standing wave) phase check
kk = 2 * np.pi * np.array([1, 0, 0]) / L
s = 2 * np.sin(kk / 2)
Tt = tt_basis_orth(s)[:, 0]                       # orthonormal TT polarization
hpol = np.linalg.inv(S_ORTH) @ Tt                 # independent-component amplitudes
h = np.zeros(6 * n)
for c in range(6):
    pos = lat.coords + np.array(H_OFF[c]) / 2.0
    h[c * n:(c + 1) * n] = hpol[c].real * np.cos(pos @ kk)
z = np.concatenate([h, np.zeros(6 * n)])
nt = 40
zz = z.copy()
for _ in range(nt):
    zz = U @ zz
th_exp = 2 * np.arcsin(tau * np.linalg.norm(s) / 2)
pred = np.cos(nt * th_exp) * h
print(f'   real-space TT standing wave, {nt} ticks: |h(t) - cos(n theta) h(0)| max {np.abs(zz[:6*n] - pred).max():.1e}; '
      f'R h = {np.abs(R @ zz[:6*n]).max():.1e}; D^T p = {np.abs(D.T @ zz[6*n:]).max():.1e}')
print(f'done in {time.time() - t0:.1f}s')
