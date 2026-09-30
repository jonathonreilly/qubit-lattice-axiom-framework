"""TEST A: validate the lane's 3-loop RGE runner against SM literature values
(Buttazzo et al., JHEP 12 (2013) 089, arXiv:1307.3536, Table: couplings at mu = M_t).
Also cross-check the 1-loop pieces of beta_lambda against my own analytic formula."""
import numpy as np, sys
import lane_rge_copy as H
PI=np.pi
t_top=np.log(173.34); t_pl=np.log(H.M_PL)
# Buttazzo Table 1 (from memory of the paper; g' is SM-normalised): 
g2=0.64779; gp=0.35830; g3=1.1666; yt=0.93690; lam=0.12604
g1=np.sqrt(5/3)*gp
y0=[g1,g2,g3,yt,lam]
for L in (1,2,3):
    sol=H.run_rge(y0,t_top,t_pl,n_f=6,loop_order=L)
    y=sol.y[:,-1]
    print(f"loop {L}: at M_Pl g1={y[0]:.4f} g2={y[1]:.4f} g3={y[2]:.4f} yt={y[3]:.4f} lam={y[4]:+.5f}")
# analytic 1-loop beta_lambda at lambda = 0 (SM, lambda|H|^4 normalisation), GUT-normalised g1
def bl1(g1,g2,yt):
    gp2=3/5*g1**2
    return (-6*yt**4 + 3/8*(2*g2**4+(g2**2+gp2)**2))/(16*PI**2)
for yt_ in (0.35,0.38,0.42):
    for (g1_,g2_) in ((0.6144,0.5041),(0.5774,0.5)):
        y=[g1_,g2_,0.49,yt_,0.0]
        b=H.beta_full(t_pl,y,n_f=6,loop_order=1)[4]
        print(f"yt={yt_} g1={g1_} g2={g2_}: lane 1-loop beta_lam={b:+.6e}  mine={bl1(g1_,g2_,yt_):+.6e}")
