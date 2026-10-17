"""Item 1 (O-only invariant operators, no translation symmetry), item 4 (symmetries of the massive model,
cube-centre rotations and their projective class), spin content of the massive doublets.  L = 4 real space."""
import itertools
import numpy as np
from core import *
from bases import get

L = 4; SITES = list(itertools.product(range(L), repeat=3)); SI = {n: i for i, n in enumerate(SITES)}
NV = 12 * len(SITES)
def vid(n, c): return SI[tuple(x % L for x in n)] * 12 + c
def realspace(m, P=0):
    """blocks m[sh][c2,c1], phase e^{i P.n} at the source; P = 0 or 1 (Q)."""
    A = np.zeros((NV, NV), complex)
    for n in SITES:
        ph = (-1) ** (sum(n) * P)
        for sh, Mx in m.items():
            t = tuple(a + b for a, b in zip(n, sh))
            A[vid(t, 0):vid(t, 0) + 12, vid(n, 0):vid(n, 0) + 12] += ph * Mx
    return A
def op_rot(R, eta, s, origin_shift=(0, 0, 0)):
    """signed permutation: c_{n,c} -> sigma c_{R n + a, R c}; returned as matrix U (U[gi, i] = sigma_i)."""
    Um = np.zeros((NV, NV))
    for n in SITES:
        Rn = tuple(int(x) for x in R @ np.array(n) + np.array(origin_shift))
        sg = (-1) ** int(s @ np.array(n))
        for c in range(12):
            Um[vid(Rn, rc(R, c)), vid(n, c)] = sg * eta[c]
    return Um
def op_tr(a):
    Um = np.zeros((NV, NV))
    for n in SITES:
        for c in range(12): Um[vid(tuple(x + y for x, y in zip(n, a)), c), vid(n, c)] = 1
    return Um
def sym_ok(A, Um): return np.allclose(Um @ A @ Um.T, A, atol=1e-10)

rng = np.random.default_rng(7)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
Xb = get('X_r1'); Mb = get('Q_onsite_im_A2')
def rnd(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
X = rnd(Xb); M = rnd(Mb)
Hb = realspace(addm(hop(-1.0, 0.2), X, coeffs=[1, 0.05])); Mr = realspace(M, P=1)
print("Hb, M Hermitian:", np.allclose(Hb, Hb.conj().T), np.allclose(Mr, Mr.conj().T), "; M odd under K:", np.allclose(Mr.conj(), -Mr))
UR = [op_rot(R, e, s) for R, (e, s) in zip(ROTS, PSG)]
UI = op_rot(INV, *PSGI)
TR = {a: op_tr(a) for a in SITES}
print("Hb invariant under 24 site rotations, inversion, all translations:",
      all(sym_ok(Hb, Um) for Um in UR), sym_ok(Hb, UI), all(sym_ok(Hb, T) for T in TR.values()))
ev, V = np.linalg.eigh(Hb); EN = ev[0]; nodeV = V[:, np.abs(ev - EN) < 1e-8]
print("node space dim (lowest level of Hb on L=4):", nodeV.shape[1], " E_N =", EN)
# split node space by momentum (eigenvectors of T_x + 2 T_y + 3 T_z restricted)
Tm = sum((j + 1) * nodeV.conj().T @ TR[a] @ nodeV for j, a in enumerate(((1,0,0),(0,1,0),(0,0,1))))
w, Z = np.linalg.eig(Tm); nodeV = nodeV @ Z
order = np.argsort(np.angle(w)); nodeV = nodeV[:, order]; w = w[order]
nodeV, _ = np.linalg.qr(nodeV)
print("  momentum labels of node states (T_x+2T_y+3T_z eigenvalues):", np.round(w, 6))

print("\n== O-only invariant operators WITHOUT translation symmetry (random, site range <= 2, complex), symmetrized over the 24 rotations about site 0")
def rnd_local(rmax=2):
    A = np.zeros((NV, NV), complex)
    for n in SITES:
        for t in SITES:
            d = [min((a - b) % L, (b - a) % L) for a, b in zip(n, t)]
            if sum(d) <= rmax and rng.random() < 0.3:
                A[SI[t]*12:SI[t]*12+12, SI[n]*12:SI[n]*12+12] = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    A = A + A.conj().T
    return sum(Um @ A @ Um.T for Um in UR) / 24
for trial in range(3):
    A = rnd_local(); Pn = nodeV.conj().T @ A @ nodeV
    off = np.abs(Pn[:2, 2:]).max(); d1 = np.abs(Pn[:2, :2] - np.trace(Pn[:2, :2]) / 2 * np.eye(2)).max()
    d2 = np.abs(Pn[2:, 2:] - np.trace(Pn[2:, 2:]) / 2 * np.eye(2)).max()
    print(f"  trial {trial}: |A| = {np.abs(A).max():.2f}; node-space off-diagonal (k* <-> -k*) max {off:.1e}; diagonal blocks non-scalar part {d1:.1e}, {d2:.1e};"
          f" diagonal scalars {np.real(np.trace(Pn[:2,:2]))/2:+.4f}, {np.real(np.trace(Pn[2:,2:]))/2:+.4f}")
# the same operator with A2 character
A = rnd_local(); A2 = sum(((-1) ** W1[k]) * UR[k] @ A @ UR[k].T for k in range(24)) / 24
Pn = nodeV.conj().T @ A2 @ nodeV
print(f"  A2-symmetrized (no translation symmetry): off-diagonal {np.abs(Pn[:2,2:]).max():.2e}, diagonal {np.abs(Pn[:2,:2]).max():.1e}, {np.abs(Pn[2:,2:]).max():.1e}")

print("\n== massive model symmetries (m = 0.05)")
m = 0.05; Hr = Hb + m * Mr
evr, Vr = np.linalg.eigh(Hr)
Tok = all(sym_ok(Hr, UR[k]) for k in range(24) if W1[k] == 0)
oddbroken = [not sym_ok(Hr, UR[k]) for k in range(24) if W1[k] == 1]
evenT = all(sym_ok(Hr, TR[a]) for a in SITES if sum(a) % 2 == 0); oddT = [sym_ok(Hr, TR[a]) for a in SITES if sum(a) % 2]
print(f"  T about site: {Tok}; w1-odd site rotations broken: {sum(oddbroken)}/12; even translations kept: {evenT}; odd translations kept: {sum(oddT)}/{len(oddT)}")
print(f"  site inversion kept: {sym_ok(Hr, UI)};  inversion x odd translation kept: {sym_ok(Hr, TR[(1,0,0)] @ UI)}")
# cube-centre rotations: n -> R(n - p) + p = R n + (p - R p), p = (1/2,1/2,1/2)
p = np.array([0.5, 0.5, 0.5])
GC = []
for R, (e, s), w in zip(ROTS, PSG, W1):
    a = np.rint(p - R @ p).astype(int)
    assert (sum(a) % 2) == w, "odd translation exactly for w1-odd"
    GC.append(op_rot(R, e, s, origin_shift=a))
print(f"  p - R p is an odd translation exactly for the 12 w1-odd R (asserted); all 24 cube-centre rotations n -> R(n-p)+p commute with H_massive:",
      all(sym_ok(Hr, G) for G in GC))
# maps a cube centre to itself: check geometrically on vertices: the corner positions n + (d+e)/2 rotate about p
ok = True
for R, G in zip(ROTS, GC):
    for n in SITES[:5]:
        for c in range(12):
            i, j = CORN[c]; x = np.array(n) + (DV[i] + DV[j]) / 2
            y = R @ (x - p) + p
            img = np.argmax(np.abs(G[:, vid(n, c)])); n2, c2 = SITES[img // 12], img % 12
            i2, j2 = CORN[c2]; x2 = np.array(n2) + (DV[i2] + DV[j2]) / 2
            ok &= np.allclose(np.exp(2j * np.pi * (x2 - y) / L), 1)
print("  geometric check: each cube-centre operator moves corner points by the rotation about p (mod L):", ok)

print("\n== projective class of the fermion under the cube-centre O (full one-fermion space and massive doublets)")
def mult_table(Ops):
    bad = 0; om = {}
    for a in range(24):
        for b in range(24):
            ab = rid(ROTS[a] @ ROTS[b]); X_ = Ops[a] @ Ops[b]
            r = np.vdot(Ops[ab].ravel(), X_.ravel()) / NV
            if not np.allclose(X_, r * Ops[ab]): bad += 1
            om[(a, b)] = r
    return bad, om
ix = rid(np.diag([1, -1, -1])); iy = rid(np.diag([-1, 1, -1]))
for nm, Ops in (('site O', UR), ('cube-centre O', GC)):
    bad, om = mult_table(Ops)
    comm = Ops[ix] @ Ops[iy] @ Ops[ix].T @ Ops[iy].T
    cs = np.vdot(np.eye(NV).ravel(), comm.ravel()) / NV
    print(f"  {nm}: products proportional to the product element: {bad == 0}; multipliers in {sorted(set(np.round(np.real(list(om.values())), 6)))};"
          f" C2x C2y C2x^-1 C2y^-1 = {np.real(cs):+.3f} * 1  (-1 = spin-1/2 class w2, +1 = linear up to phases)")
    for tw, tl in ((1, 'no twist'), (1j, 'twist i^w1')):
        D_ = [(tw ** w) * Op for w, Op in zip(W1, Ops)]
        print(f"     {tl}: lifts to a linear rep of 2O (central -1 acting as -1): {len(lift(D_)) > 0}")
# C4 conjugation of a translation (the C17 caveat)
c4 = rid(np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
cc = UR[c4] @ TR[(1, 0, 0)] @ UR[c4].T @ TR[(0, 1, 0)].T
print("  site C4z T_x C4z^-1 T_y^-1 =", np.round(np.real(np.trace(cc)) / NV, 6), "* 1")

# massive doublets
mD_levels = []
e4 = evr[:8]; print("  lowest massive levels:", np.round(e4 - EN, 6))
for E, lab in ((evr[0], 'lower'), (evr[2], 'upper')):
    Vs = Vr[:, np.abs(evr - E) < 1e-8]
    for nm, Ops in (('site T', UR), ('cube-centre O', GC)):
        if nm == 'site T':
            comm = (Vs.conj().T @ UR[ix] @ Vs) @ (Vs.conj().T @ UR[iy] @ Vs)
            comm = comm @ np.linalg.inv(Vs.conj().T @ UR[ix] @ Vs) @ np.linalg.inv(Vs.conj().T @ UR[iy] @ Vs)
            print(f"  {lab} doublet (dim {Vs.shape[1]}, E - E_N = {E-EN:+.5f}): site-T D2 commutator {np.round(np.real(comm[0,0]), 6):+}")
        else:
            inv = all(np.allclose(Op @ Vs, Vs @ (Vs.conj().T @ Op @ Vs)) for Op in GC)
            Dd = [(Vs.conj().T @ Op @ Vs) for Op in GC]
            comm = Dd[ix] @ Dd[iy] @ np.linalg.inv(Dd[ix]) @ np.linalg.inv(Dd[iy])
            res = {}
            for tw, tl in ((1, 'none'), (1j, 'i^w1')):
                Ls = lift([(tw ** w) * d for w, d in zip(W1, Dd)])
                res[tl] = [decomp(np.array([np.trace(Lq[g]) for g in range(48)])) for Lq in Ls]
            print(f"     invariant under cube-centre O: {inv}; cube-centre D2 commutator {np.round(np.real(comm[0,0]), 6):+}; 2O lifts/labels: {res}")
