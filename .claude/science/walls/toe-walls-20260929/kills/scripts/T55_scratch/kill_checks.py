#!/usr/bin/env python3
"""T55 kill checks (Claude Sonnet 5.5, same family as attacker/supervisor; not independent).
Independent re-derivation with exact interval unions (no sampling), plus the T56 factor-2 interplay.
Reads the repo checkout only for canonical constants."""
import sys, math, itertools
sys.path.insert(0, "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts")
from canonical_plaquette_surface import (CANONICAL_ALPHA_BARE as A_BARE, CANONICAL_ALPHA_LM as A_LM,
                                         CANONICAL_ALPHA_S_V as A_SV, CANONICAL_U0 as U0)
PI=math.pi; MPL=1.2209e19; V=MPL*(7/8)**0.25*A_LM**16
GS, XF, ETA, BBN, KT = 106.75, 25.0, 6.12e-10, 3.65e7, 1.07e9
R0 = (31/9)*1.59
def C(a,R=R0,xf=XF): return KT*xf/(math.sqrt(GS)*MPL*PI*a*a*R*BBN)
def mt(a,R=R0,xf=XF): return math.sqrt(ETA/C(a,R,xf))
LAM = mt(A_LM)/A_LM
BLK=[("alpha_LM",A_LM),("u_0",U0),("pi",PI),("2",2.),("3",3.),("N_c",3.),("N_sites",16.),("hw_dark",3.),("R_base",31/9),("alpha_s(v)",A_SV),("dim_adj",8.)]
def fam(ps): return [(f"{n}^{p}",x**p) for n,x in BLK for p in ps]
F22,F44=fam([1,-1]),fam([2,1,-1,-2])
def union_cov(vals,tol,lo,hi):
    """exact fraction (ln-uniform) of targets x in [lo,hi] with some v within relative tol: |v/x-1|<tol."""
    iv=sorted((math.log(v/(1+tol)),math.log(v/(1-tol))) for v in vals)
    a,b=math.log(lo),math.log(hi); tot=0; cur=None
    for s,e in iv:
        s,e=max(s,a),min(e,b)
        if e<=s: continue
        if cur is None: cur=[s,e]
        elif s<=cur[1]: cur[1]=max(cur[1],e)
        else: tot+=cur[1]-cur[0]; cur=[s,e]
    if cur: tot+=cur[1]-cur[0]
    return tot/(b-a)
print(f"v={V:.4f}; m_target={mt(A_LM):.2f} GeV={mt(A_LM)/V:.4f} v; Lambda*={LAM/V:.3f} v; 16v dev={16*V/mt(A_LM)-1:+.4f}")
tm=mt(A_LM)/V; lo,hi=tm/math.sqrt(10),tm*math.sqrt(10)
v22=[v for _,v in F22]; v44=[v for _,v in F44]
print("\n== K1 exact base rates (factor-10 window centred on target) ==")
for nm,vals in (("F22",v22),("F44",v44)):
    print(f"  {nm}: "+"; ".join(f"tol {t:.4f}: {union_cov(vals,t,lo,hi):.4f}" for t in (0.0209,0.05,0.108)))
print("  (tol 0.0209 = the observed closeness of 16 v: P(a random target is at least this close to some family member))")
print("  F22 members inside the window:", [n for n,v in F22 if lo<=v<=hi], " values:", [round(v,3) for n,v in F22 if lo<=v<=hi])
# ---- K2 coupling-list sensitivity
g2=[0.65939,0.6711,0.68283]; a2=[g*g/(4*PI) for g in g2]
LISTS={
 "canonical3 {1/4pi,alpha_LM,alpha_s(v)}":[A_BARE,A_LM,A_SV],
 "canonical3 + alpha_2(v) one point (g=0.6711)":[A_BARE,A_LM,A_SV,a2[1]],
 "canonical3 + alpha_2(v) x3 points":[A_BARE,A_LM,A_SV]+a2,
 "+0.048 (R-pin, cosmology note)":[A_BARE,A_LM,A_SV]+a2+[0.048],
 "+1/(16pi) (lattice-scale SU2 anchor) = attacker's A_FILE":[A_BARE,A_LM,A_SV]+a2+[0.048,1/(16*PI)],
}
print("\n== K2 pair sensitivity: F44 masses x coupling list; pairs within 5% of Lambda* and random-target coverage ==")
for nm,al in LISTS.items():
    pv=sorted({m*V/a for _,m in F44 for a in al})
    P=sorted({(round(m,5),round(a,5)) for _,m in F44 for a in al if abs(m*V/a/LAM-1)<0.05})
    cov=union_cov(pv,0.05,LAM/math.sqrt(10),LAM*math.sqrt(10))
    print(f"  {nm:62s} pairs@5%={len(P)}  coverage={cov:.3f}   {[(round(m,3),round(a,4)) for m,a in P]}")
# ---- K3 how the target moves with the inputs T55 froze
print("\n== K3 Lambda* / target under alternative R and counting (alpha_X = alpha_LM) ==")
R_obs=0.1200/0.02237; R_corr=7.9717; R_june=5.4420
cases=[("base R=(31/9)*1.59=5.477",R0,1.0),("R pinned to Planck 5.364",R_obs,1.0),
       ("June kernel R(alpha_LM)=5.442",R_june,1.0),("T56 corrected kernel R(alpha_LM)=7.972 (one coupling)",R_corr,1.0),
       ("x_F=22",R0,1.0),("x_F=28",R0,1.0),("Dirac counting (sigma v needs x2 -> Lambda/sqrt2)",R0,2.0)]
for nm,R,f in cases:
    xf = 22 if "x_F=22" in nm else 28 if "x_F=28" in nm else XF
    t = mt(A_LM,R,xf)/math.sqrt(f)/V
    h5=[n for n,v in F22 if abs(v/t-1)<0.05]; h11=[n for n,v in F22 if abs(v/t-1)<0.108]
    print(f"  {nm:58s} target={t:7.3f} v  16v dev={16/t-1:+.3f}  F22 hits@5%={h5} @10.8%={h11}")
# ---- 0.048 vs corrected pin
print("\n== K4 the 0.048 coupling under the T56 factor-2 correction ==")
for a in (0.048,0.0438,0.0461):
    print(f"  (8 v, {a}): dev from Lambda* = {(8*V/a)/LAM-1:+.3f}")
# ---- K5 Omega from the note's formula at (16v, alpha_LM) and at Lambda*
def Om(m,a): return KT*XF*m*m/(math.sqrt(GS)*MPL*PI*a*a)
print(f"\n== K5 Omega_DM h^2 = K x_F m^2/(sqrt(g*) Mpl pi alpha^2): at (16v,alpha_LM) = {Om(16*V,A_LM):.4f}; at target = {Om(mt(A_LM),A_LM):.4f}; Omega_b(eta_obs) * R0 = {BBN*ETA*R0:.4f}")
sv=PI/LAM**2*1.1673e-17
print(f"   <sigma v>(Lambda*) = {sv:.3e} cm^3/s; the formula returns it for Omega_DM h^2 = R0 * Omega_b(eta_obs): Test C is the note's own formula read backwards (cannot fail)")
