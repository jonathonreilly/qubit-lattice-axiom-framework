import numpy as np, sys, itertools
sys.path.insert(0, '.')
from rge import *
rng = np.random.default_rng(20260929)
up = up_from_mz(MPL, 2)
def ir(g22, gp2, loops=2):
    y = down_from_mpl(gp2, g22, up, MZ, loops)
    o = observables(y)
    return o['s2'], o['aem_inv']
def errs(g22, gp2, loops=2):
    s2, ai = ir(g22, gp2, loops)
    return (s2/S2W_MZ-1)*100, (ai/AEM_INV_MZ-1)*100, s2, ai
# sanity: SM-extrapolated pair returns the input
o = observables(up)
print("sanity (SM-extrapolated pair run back down):", ["%.5f" % x for x in ir(o['g22'], o['gp2'])], "vs", S2W_MZ, AEM_INV_MZ)

cands = {
 'c1 counting (1/4, 1/5)': (0.25, 0.2),
 'c2 Pati-Salam relation (g4^2=1, gL^2=gR^2=1/4) -> gY^2=3/14': (0.25, 1/(1/0.25 + (2/3)/1.0)),
 'c2b PS with g4^2 = g_L^2 = g_R^2 = 1/4 (unified) -> gY^2 = 3/20 (sin^2=3/8)': (0.25, 1/(1/0.25 + (2/3)/0.25)),
 'c3 SU(5)-type unified g^2=1/4: gY^2 = 3/5 g^2': (0.25, 0.15),
 'c4 universal 1/4 (both)': (0.25, 0.25),
 'c5 unit tick (SU(2) beta=4: g2^2=1; gY^2=1)': (1.0, 1.0),
 'c6 PS with g4^2=1, gL^2=gR^2=1 (unit tick on all): gY^2 = 3/5': (1.0, 1/(1/1.0 + (2/3)/1.0)),
}
# c7: single parent coupling g0 with kinetic (1/g0^2) Tr_8 F^2 on the lane's 8-state left-handed surface
T3 = np.array([0.5]*8)                          # |T3| = 1/2 on all 8 states (4 doublets)
Y = np.array([1/3]*6 + [-1.0]*2)
tr_T3 = (T3**2).sum(); tr_Yh = ((Y/2)**2).sum()
print(f"\n8-state left-handed surface: Tr T3^2 = {tr_T3:.4f}, Tr (Y/2)^2 = {tr_Yh:.4f}; Tr-normalised ratio g'^2/g2^2 = {tr_T3/tr_Yh:.3f} -> sin^2 = {(tr_T3/tr_Yh)/(1+tr_T3/tr_Yh):.4f}  (needs right-handed states for 3/8)")
cands['c7 8-state trace normalisation, g2^2=1/4'] = (0.25, 0.25*tr_T3/tr_Yh)

print("\nTEST C: IR predictions (2-loop SM running down from M_Pl)")
print(f"{'candidate':78s} g2^2   gY^2   sin2(MZ)  err%    1/aem(MZ) err%   verdict(<=3%,<=5%)")
res = {}
for k, v in cands.items():
    e_s, e_a, s2, ai = errs(*v)
    ok = abs(e_s) <= 3 and abs(e_a) <= 5
    res[k] = dict(g22=v[0], gp2=v[1], s2=s2, aem_inv=ai, err_s2_pct=e_s, err_aem_pct=e_a, PASS=bool(ok))
    print(f"{k:78s} {v[0]:.4f} {v[1]:.4f}  {s2:.4f}  {e_s:+6.1f}  {ai:8.2f}  {e_a:+6.1f}   {'PASS' if ok else 'FAIL'}")
# PS with SU(2)_R coupling exponent check: dependence on g4^2 / g_R^2
print("\nPS relation: gY^2 as function of (g4^2, gR^2 = gL^2 = 1/4):")
for g4 in (0.25, 0.5, 1.0, 2.0, 4.0, 1e9):
    gy = 1/(1/0.25 + (2/3)/g4)
    e = errs(0.25, gy)
    print(f"   g4^2={g4:9.2f}: gY^2={gy:.4f}  sin2={e[2]:.4f} ({e[0]:+.1f}%)  1/aem={e[3]:.2f} ({e[1]:+.1f}%)")

# ---------- trial factor ----------
print("\nTRIAL FACTOR")
e1_s, e1_a = abs(res['c1 counting (1/4, 1/5)']['err_s2_pct']), abs(res['c1 counting (1/4, 1/5)']['err_aem_pct'])
print(f"box of the counting pair: |err sin2| <= {e1_s:.2f}%, |err 1/aem| <= {e1_a:.2f}%")
grid = list(itertools.product(range(1, 13), range(1, 13)))
hits = []
allres = []
for n, m in grid:
    es, ea, s2, ai = errs(1/n, 1/m)
    allres.append((n, m, es, ea))
    if abs(es) <= e1_s and abs(ea) <= e1_a: hits.append((n, m, es, ea))
print("family F = {(1/n, 1/m): n,m=1..12}: pairs at least as good as (4,5) in BOTH errors:", [(n, m, round(es,2), round(ea,2)) for n, m, es, ea in hits])
# pairs meeting the PASS bar (3%,5%)
ok = [(n, m, round(es,2), round(ea,2)) for n, m, es, ea in allres if abs(es) <= 3 and abs(ea) <= 5]
print("family pairs meeting (3%, 5%):", ok)
# base rate: random log-uniform pair in [0.1,0.5]^2 lands in the counting pair's box.
# Vectorised analytic 1-loop with g3 and y_t irrelevant at 1 loop; box for both pairs recomputed at 1 loop for consistency.
LT = np.log(MPL/MZ)
def ir1(g22, gp2):
    ginv2 = 1/g22 + (B1[1]/(8*PI**2))*LT          # g2^-2(MZ)
    g1inv2 = 1/(5/3*gp2) + (B1[0]/(8*PI**2))*LT      # g1^-2(MZ), GUT norm
    g2sq = 1/ginv2; gp2z = 3/5/g1inv2
    e2 = g2sq*gp2z/(g2sq+gp2z)
    return gp2z/(g2sq+gp2z), 4*PI/e2
def box1(pair):
    s2, ai = ir1(*pair)
    return abs(s2/S2W_MZ-1)*100, abs(ai/AEM_INV_MZ-1)*100
b1 = box1((0.25, 0.2)); b2 = box1((0.25, 3/14))
print(f"1-loop boxes: counting pair |err|=({b1[0]:.2f}%, {b1[1]:.2f}%); PS pair ({b2[0]:.2f}%, {b2[1]:.2f}%)")
N = 400000
lo, hi = np.log(0.1), np.log(0.5)
g22 = np.exp(rng.uniform(lo, hi, N)); gp2 = np.exp(rng.uniform(lo, hi, N))
s2, ai = ir1(g22, gp2)
es = np.abs(s2/S2W_MZ-1)*100; ea = np.abs(ai/AEM_INV_MZ-1)*100
p1 = np.mean((es <= b1[0]) & (ea <= b1[1])); p2 = np.mean((es <= b2[0]) & (ea <= b2[1]))
pPASS = np.mean((es <= 3) & (ea <= 5))
print(f"base rate (random log-uniform pair in [0.1,0.5]^2): in counting-pair box {p1:.4f}; in PS-pair box {p2:.4f}; in (3%,5%) PASS box {pPASS:.4f}")
print(f"expected chance hits among 144 family pairs: counting box {144*p1:.2f}; PS box {144*p2:.2f}; PASS box {144*pPASS:.2f}")
# family under 1-loop for consistency
hits1 = [(n, m) for n, m in grid if (lambda r: abs(r[0]/S2W_MZ-1)*100 <= b1[0] and abs(r[1]/AEM_INV_MZ-1)*100 <= b1[1])(ir1(1/n, 1/m))]
print("family pairs (1-loop) at least as good as (4,5):", hits1)
okf = [(n, m) for n, m in grid if (lambda r: abs(r[0]/S2W_MZ-1)*100 <= 3 and abs(r[1]/AEM_INV_MZ-1)*100 <= 5)(ir1(1/n, 1/m))]
print("family pairs (1-loop) meeting the (3%,5%) PASS bar:", okf)
# finer family: g^2 = p/q, p in 1..3, q in 1..20  (both couplings)
fam = sorted({(p, q) for p in (1, 2, 3) for q in range(1, 21) if 0.08 <= p/q <= 0.6})
cnt = 0; hh = []
for (p, q) in fam:
    for (p2_, q2) in fam:
        r = ir1(p/q, p2_/q2)
        if abs(r[0]/S2W_MZ-1)*100 <= 3 and abs(r[1]/AEM_INV_MZ-1)*100 <= 5:
            cnt += 1; hh.append(((p, q), (p2_, q2)))
print(f"finer family (p/q, p<=3, q<=20, value in [0.08,0.6]; {len(fam)} values, {len(fam)**2} pairs): pairs meeting (3%,5%): {cnt}; sample {hh[:12]}")
import json
json.dump(dict(cands=res, box_counting_1loop=b1, box_ps_1loop=b2, p_counting_box=p1, p_ps_box=p2, p_pass_box=pPASS, family_hits_leq_counting=hits1, family_meeting_pass=okf, finer_family_pairs=len(fam)**2, finer_family_meeting_pass=cnt), open('t33_C_results.json', 'w'), indent=1)
