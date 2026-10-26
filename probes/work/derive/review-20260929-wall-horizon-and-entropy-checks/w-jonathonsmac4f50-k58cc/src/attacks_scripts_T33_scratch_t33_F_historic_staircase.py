"""Replicate the HISTORIC (branch-only, never mainlined) alpha_EM staircase route and test how much of it is one tuned number.
Spec from archive_unlanded/historic_intake_originals/branch01/45_ALPHA_EM_DERIVATION_NOTE.md sec 2.1-2.5:
 lattice 1/a2=16pi, 1/aY=20pi at M_Pl; three staircase segments (n_extra = 14, 10, 4) of 0.52 decades each with n_eff = n_extra*tw;
 b_2_eff = 19/6 - (4/3) n_eff ; b_Y_eff = -41/6 - (20/9) n_eff ; SM 1-loop for the remaining ln; colour projection g^2 -> g^2*9/8;
 then 2-loop SM v -> M_Z.  (Sonnet 5.5 replication; not the original runner, which is not in the repo.)"""
import numpy as np, sys, itertools
sys.path.insert(0, '.')
from rge import *
ALPHA_LM = 0.0907
Lseg = 0.52*np.log(10)
L = np.log(MPL/V)
def chain(tw, K=9/8, ns=(14, 10, 4)):
    i2, iY = 16*PI, 20*PI
    for n in ns:
        neff = n*tw
        b2 = 19/6 - (4/3)*neff; bY = -41/6 - (20/9)*neff
        i2 -= b2/(2*PI)*Lseg; iY -= bY/(2*PI)*Lseg
    Lr = L - len(ns)*Lseg
    i2 -= 19/6/(2*PI)*Lr; iY -= (-41/6)/(2*PI)*Lr
    g22, gY2 = K*4*PI/i2, K*4*PI/iY
    return g22, gY2
def to_mz(g22, gY2):
    y0 = np.array([np.sqrt(5/3*gY2), np.sqrt(g22), np.sqrt(4*PI*0.1033), 0.95])
    o = observables(run(y0, V, MZ, 2))
    return o['s2'], o['aem_inv']
tw0 = 7/18
g22, gY2 = chain(tw0)
print(f"tw=7/18: g_2(v)={np.sqrt(g22):.5f} (note 0.64803)  g_1GUT(v)={np.sqrt(5/3*gY2*5/3):.5f}? -> g'(v)={np.sqrt(gY2):.5f} => g1_GUT={np.sqrt(5/3)*np.sqrt(gY2):.5f} (note 0.46438)")
s2, ai = to_mz(g22, gY2); print(f"   sin2(MZ)={s2:.5f} (note 0.23064)  1/aem(MZ)={ai:.3f} (note 127.682)")
print("\nno staircase (tw=0), no projection:", ["%.4f" % x for x in to_mz(*chain(0.0, K=1.0))])
print("no staircase (tw=0), K=9/8       :", ["%.4f" % x for x in to_mz(*chain(0.0))])
print("staircase tw=7/18, no projection K=1:", ["%.4f" % x for x in to_mz(*chain(tw0, K=1.0))])
# scan
tws = np.linspace(0, 1.0, 201)
rows = []
for tw in tws:
    s, a = to_mz(*chain(tw)); rows.append((tw, s, a, (s/S2W_MZ-1)*100, (a/AEM_INV_MZ-1)*100))
rows = np.array(rows)
best = rows[np.argmin(np.abs(rows[:, 3]))]
print(f"\nscan: tw minimising |sin2 err|: tw={best[0]:.3f}, sin2 err {best[3]:+.2f}%, 1/aem err {best[4]:+.2f}%")
for tol in (0.5, 1.0, 2.0):
    m = (np.abs(rows[:, 3]) <= tol) & (np.abs(rows[:, 4]) <= 2*tol)
    if m.any(): print(f"   tw window with |sin2|<={tol}% and |1/aem|<={2*tol}%: [{rows[m,0].min():.3f}, {rows[m,0].max():.3f}]")
    else: print(f"   no tw with |sin2|<={tol}% and |1/aem|<={2*tol}%")
# is the 1/aem residual independent of tw? show tw = 0.2,0.3,0.39,0.5,0.7
for tw in (0.2, 0.3, 0.3889, 0.5, 0.7, 1.0):
    s, a = to_mz(*chain(tw)); print(f"   tw={tw:.4f}: sin2 {s:.4f} ({(s/S2W_MZ-1)*100:+.2f}%), 1/aem {a:.2f} ({(a/AEM_INV_MZ-1)*100:+.2f}%)")
# forking count: products a*b*c of natural factors landing in the 1% window
S1 = [1, 7/8, 15/16, 3/4, 1/2]; S2 = [1, 1/2, 1/4, 1/3, 2/3, 3/4]; S3 = [1, 8/9, 9/8, 2/3, 3/4, 1/3]
prods = sorted({round(a*b*c, 6) for a in S1 for b in S2 for c in S3})
ok = []
for p in prods:
    s, a = to_mz(*chain(p))
    if abs(s/S2W_MZ-1)*100 <= 1.0 and abs(a/AEM_INV_MZ-1)*100 <= 2.0: ok.append(p)
print(f"\nforking ledger: {len(prods)} distinct products of one factor from each of three small sets; those within (1%, 2%): {len(ok)} -> {ok}")
lo = rows[(np.abs(rows[:,3]) <= 1.0) & (np.abs(rows[:,4]) <= 2.0), 0]
print("fraction of tw in [0,1] that lands in the (1%,2%) window:", (lo.max()-lo.min())/1.0 if lo.size else 0)
