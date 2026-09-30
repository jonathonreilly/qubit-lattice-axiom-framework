"""KILL CHECK 2: re-score attack Test C after dropping the scale-mislabelled alpha_s(v)=0.1179 corner
(0.1179 is alpha_s(M_Z); alpha_s(v)=0.1179 would imply alpha_s(M_Z)=0.138). Uses the attacker's own rows (testC_rows.json)."""
import json, numpy as np
rows=json.load(open("testC_rows.json"))
def sp(v):
    v=np.array([float(x) for x in v if x!='nan']); return (v.max()/v.min()-1, v.min(), v.max(), len(v))
for drop in (False, True):
    R=[r for r in rows if (not drop or r[2]!='0.1179')]
    r1=[r[-1] for r in R if r[0]=='R1']; wd=[r[-1] for r in R if r[0]=='Ward']
    s1=sp(r1); sw=sp(wd)
    print(f"drop 0.1179 corner = {drop}: R1 spread {s1[0]*100:.1f}% [{s1[1]:.4f},{s1[2]:.4f}] n={s1[3]}; Ward spread {sw[0]*100:.1f}% [{sw[1]:.4f},{sw[2]:.4f}] n={sw[3]}; R1/Ward = {s1[0]/sw[0]:.3f}")
    print("   pre-reg C PASS needs R1<=1/3 Ward (%s) and R1<=10%% (%s)"%(s1[0]<=sw[0]/3, s1[0]<=0.10))
# shared-only R1 (loop3, lam=0) with legit alpha_s
sh=[(r[1],r[2],float(r[-1])) for r in rows if r[0]=='R1' and r[3]=='loop3' and r[4]=='lam_pl=+0e+00']
print("R1 shared-only y_t(v):",sh)
# kappa_EW=0 only (lane's own EW), alpha_s in {0.0907,0.1033}
v=[x[2] for x in sh if x[0]=='0' and x[1]!='0.1179']
print("kEW=0, alpha_s in {0.0907,0.1033}: spread %.1f%%"%((max(v)/min(v)-1)*100))
v=[x[2] for x in sh if x[1]=='0.1033']
print("alpha_s=0.1033 fixed, kEW in {0,1}: spread %.1f%%"%((max(v)/min(v)-1)*100))
