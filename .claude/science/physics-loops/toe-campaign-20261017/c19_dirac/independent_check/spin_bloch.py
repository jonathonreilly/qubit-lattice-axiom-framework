"""Spin content at the folded k* (Bloch level): massless node states under the twisted site O (both lifts),
massive doublets under 2T about a site and under the cube-centre O; the action of w1-odd site rotations
and odd translations on the node space (chirality); finite-strength O-invariant staggered terms."""
import numpy as np
from core import *
from bases import get

rng = np.random.default_rng(21)
fm = fixed_momenta(); KS = np.array(fm[0]) * np.pi / 4
def rnd(bs):
    c = rng.normal(size=len(bs)); m = addm(*bs, coeffs=list(c))
    nrm = max(np.abs(M).max() for M in m.values()); return {k: v / nrm for k, v in m.items()}
Hb = addm(hop(-1.0, 0.2), rnd(get('X_r1')), coeffs=[1, 0.05]); M = rnd(get('Q_onsite_im_A2'))
p = np.array([0.5] * 3)
def site_op(r, twist=True):
    return ((1j ** W1[r]) if twist else 1) * np.kron(np.eye(2), WR[r])
def trans_op(a):   # T_a on (k*, k*+Q) components: e^{-i k.a}
    return np.diag(np.concatenate([np.full(12, np.exp(-1j * KS @ a)), np.full(12, np.exp(-1j * (KS + Q) @ a))]))
def cube_op(r, twist=False):
    a = np.rint(p - ROTS[r] @ p).astype(int); return trans_op(a) @ site_op(r, twist)
H0 = fold(Hb, {k: 0 * v for k, v in M.items()}, KS)
for r in range(24): assert np.allclose(site_op(r) @ H0, H0 @ site_op(r))
e, V = np.linalg.eigh(H0); EN = e[0]; Vn = V[:, np.abs(e - EN) < 1e-9]; print("node space dim at folded k*:", Vn.shape[1])
# split by momentum component
Pk = np.diag([1.0] * 12 + [0.0] * 12); w_, Z = np.linalg.eigh(Vn.conj().T @ Pk @ Vn); Vn = Vn @ Z  # first two: -k* (k*+Q) part, last two: k*
gam5 = None
for lift_i in (0, 1):
    Ls = lift([Vn.conj().T @ site_op(r) @ Vn for r in range(24)])
    Lb = Ls[lift_i]
    labs = []
    for blk in (slice(0, 2), slice(2, 4)):
        labs.append(decomp(np.array([np.trace(Lb[g][blk, blk]) for g in range(48)])))
    print(f"  twisted site O, lift {lift_i}: (k*+Q doublet, k* doublet) = {labs}")
# chirality operator on node space: Berry flux sign of each doublet; w1-odd rotation vs w1-even, relative sign between the doublets
Rn = [Vn.conj().T @ site_op(r) @ Vn for r in range(24)]
rel = []
for r in range(24):
    A, B = Rn[r][:2, :2], Rn[r][2:, 2:]
    # compare characters relative: chi_B / chi_A when nonzero
    ca, cb = np.trace(A), np.trace(B)
    if abs(ca) > 1e-6: rel.append((W1[r], np.round(cb / ca, 6)))
print("  ratio of characters (k* doublet / k*+Q doublet) by w1:", sorted(set(rel), key=lambda x: (x[0], np.real(x[1]))))
T1 = Vn.conj().T @ trans_op(np.array([1, 0, 0])) @ Vn
print("  odd translation T_x on the node space: diag phases", np.round(np.diag(T1), 6), "(relative sign -1 between the doublets = chirality operator up to a phase)")

mval = 0.01
Hm = fold(Hb, {k: mval * v for k, v in M.items()}, KS); em, Vm = np.linalg.eigh(Hm)
mD = None
for lab, E in (('lower', EN - 0), ('upper', EN)):
    pass
idx_lo = np.where(np.abs(em - em[np.argmin(np.abs(em - EN + 0.03))]) < 1e-9)[0]
# find the two doublets nearest E_N
lv = sorted(set(np.round(em, 9)), key=lambda x: abs(x - EN))[:2]
for E in sorted(lv):
    Vs = Vm[:, np.abs(em - E) < 1e-8]
    D2 = []
    ix = rid(np.diag([1, -1, -1])); iy = rid(np.diag([-1, 1, -1]))
    Tel = [r for r in range(24) if W1[r] == 0]
    DT = {r: Vs.conj().T @ site_op(r) @ Vs for r in Tel}
    c = DT[ix] @ DT[iy] @ np.linalg.inv(DT[ix]) @ np.linalg.inv(DT[iy])
    LT = lift([DT.get(r, np.eye(2)) for r in range(24)], elems=Tel)
    chiT = [np.trace(LT[0][g]) for g in LT[0]] if LT else None
    sh = np.real(sum(np.conj(CH12[g]) * np.trace(LT[0][g]) for g in LT[0])) / 24 if LT else None
    nrm = np.real(sum(abs(np.trace(LT[0][g]))**2 for g in LT[0])) / 24 if LT else None
    DC = [Vs.conj().T @ cube_op(r) @ Vs for r in range(24)]
    inv = all(np.allclose(cube_op(r) @ Vs, Vs @ DC[r]) for r in range(24))
    cc = DC[ix] @ DC[iy] @ np.linalg.inv(DC[ix]) @ np.linalg.inv(DC[iy])
    LC = lift(DC)
    labC = [decomp(np.array([np.trace(Lq[g]) for g in range(48)])) for Lq in LC]
    print(f"  m={mval}: doublet at E-E_N = {E-EN:+.6f} (dim {Vs.shape[1]}): 2T lift exists {bool(LT)}, |chi|^2 norm {nrm:.4f}, overlap with SU(2) spin-1/2 {sh:.4f};"
          f" site-T D2 commutator {np.real(c[0,0]):+.3f}; cube-centre O invariant {inv}, D2 commutator {np.real(cc[0,0]):+.3f}, 2O labels (both lifts) {labC}")

print("\n== finite-strength O-invariant staggered term (A1, on-site real and imag, range 1): node levels stay 2-fold, no gap at the doublets")
for nm in ('Q_onsite_re_A1', 'Q_r1_im_A1'):
    S = rnd(get(nm))
    for s in (0.1, 0.3, 1.0):
        Hs = fold(Hb, {k: s * v for k, v in S.items()}, KS); es = np.linalg.eigvalsh(Hs)
        # the E1/2-sector and E5/2-sector levels: degeneracies of the lowest levels
        degs = []; i = 0
        while i < 24:
            j = i
            while j + 1 < 24 and abs(es[j+1] - es[i]) < 1e-8: j += 1
            degs.append(j - i + 1); i = j + 1
        print(f"  {nm} strength {s}: degeneracy pattern of the 24 folded levels at k*: {degs}")
