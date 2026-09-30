import math, itertools
from fractions import Fraction as F
import numpy as np

# ---- K1: eta step = product of two comparisons (algebra check with attack's numbers) ----
Oc_pred=0.1275; Oc=0.1200; Ob=0.02237
R_pred=float(F(31,9))*1.59; R_obs=Oc/Ob
print("K1 Omega_DM pred/obs =%.4f ; R_obs/R_pred = %.4f ; product = eta_pred/eta_obs = %.4f"%(Oc_pred/Oc,R_obs/R_pred,(Oc_pred/Oc)*(R_obs/R_pred)))
print("   with R replaced by R_obs the eta ratio would be %.4f (Omega_DM comparison alone)"%(Oc_pred/Oc))
print("   with R=3.444 (S=1) the eta ratio would be %.4f -> R value DOES enter the eta test"%((Oc_pred/Oc)*(R_obs/float(F(31,9)))))

# ---- K2: sphaleron-decoupling T_d is not free in the SM: T_sph ~ 130-160 GeV ----
m=16*246.282818290129
def ratio_x(x,gr=1.0): return 12*gr*(x/(2*math.pi))**1.5*math.exp(-x)
for Tsph in (131.7,150,160):
    x=m/Tsph
    print("K2 T_sph=%.1f GeV -> x=m/T=%.1f -> n_DM/n_b (attacker's suppression formula, g-ratio 1) = %.2e ; needed 1.30e-3 ; R would be %.2e"%(Tsph,x,ratio_x(x),ratio_x(x)*m/0.938272))

# ---- K3: chance rate of the look-elsewhere windows, duplicates and spread ----
C3,C2,d3,d2=F(4,3),F(3,4),8,3
T3,T2=F(1,2),F(1,2)
styles={"C*dA":(C3*d3,C2*d2),"T*dA":(T3*d3,T2*d2),"dA":(F(d3),F(d2)),"C":(C3,C2),"C^2":(C3**2,C2**2),"C^2*dA":(C3**2*d3,C2**2*d2)}
prefs=[F(1),F(3,5),F(5,3),F(1,2),F(2),F(3),F(1,3)]
sig=5.364*math.sqrt((0.0012/0.12)**2+(0.00015/0.02237)**2)
lo,hi=(5.364-2*sig)/1.7,(5.364+2*sig)/1.4
vals=[]
for sn,(w3,w2) in styles.items():
    W_={"3":w3,"2":w2,"3+2":w3+w2}
    for a,b in itertools.permutations(W_,2):
        for p in prefs:
            vals.append(p*W_[a]/W_[b])
print("K3 family A size",len(vals),"distinct values",len(set(vals)))
d=set(vals); hits=[v for v in d if lo<=float(v)<=hi]
print("   distinct hits",len(hits),"of",len(d),"= %.1f%%"%(100*len(hits)/len(d)),"; hits:",sorted(map(str,hits)))
lv=np.log10([float(v) for v in vals]); print("   log10 spread: min %.2f max %.2f ; width of S-free window = %.3f decades"%(lv.min(),lv.max(),math.log10(hi/lo)))
# chance rate if values were log-uniform over the family's own span
print("   chance rate for a log-uniform value over the family span: %.1f%%"%(100*math.log10(hi/lo)/(lv.max()-lv.min())))
# empirical central-90% span
q5,q95=np.percentile(lv,[5,95]); print("   5-95%% span %.2f decades -> chance-ish %.1f%%"%(q95-q5,100*math.log10(hi/lo)/(q95-q5)))
