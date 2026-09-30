"""KILL CHECK 5: (a) R1 sensitivity to the scale at which the two Planck conditions are imposed (convention absent from attack's 'route-specific spread');
(b) R1 pole mass on scale-consistent shared corners (alpha_s(v) in {0.0907,0.1033}, kEW in {0,1}); (c) m_H implied by R1;
(d) Test D prior sensitivity."""
import numpy as np, math
from scipy.optimize import brentq
import common as C
from common import *
g0=gauge_at_v(0)

# (a) scale dependence of the criticality condition
def crit_at(mu_uv, g, loop=3):
    t=np.log(mu_uv)
    def f(yt):
        sol=H.run_rge([g[0],g[1],g[2],yt,0.13],t_v,t,n_f=6,loop_order=loop); ypl=sol.y[:,-1]
        return H.beta_full(t,[ypl[0],ypl[1],ypl[2],ypl[3],0.0],n_f=6,loop_order=loop)[4]
    return brentq(f,0.8,1.05,xtol=1e-10)
print("(a) scale at which lambda=beta_lambda=0 is imposed (units of M_Pl=1.221e19):")
base=crit_at(MPL,g0)
for c,lab in ((1.0,"M_Pl"),(0.5,"M_Pl/2"),(2.0,"2 M_Pl"),(0.1995,"reduced Planck mass 2.435e18"),(1/(2*PI),"M_Pl/(2 pi)"),(2*PI,"2 pi M_Pl"),(0.01,"M_Pl/100")):
    z=crit_at(MPL*c,g0); print(f"   mu_UV={lab:28s} y_t(v)_crit={z:.5f}  ({(z/base-1)*100:+.2f}%)")

# (b) pole masses on scale-consistent corners
print("(b) R1 pole mass (3-loop) on shared corners:")
for kEW in (0,1):
    for a_s in (ALPHA_LM,ALPHA_S_V):
        g=gauge_at_v(kEW,a_s); z=crit_yt_v(g,loop=3); pole,m,mu=pole_from_yt_v(z,g,kappaY0=False)
        print(f"   kEW={kEW} alpha_s(v)={a_s:.4f}: y_t(v)={z:.4f} pole={pole:.1f}")

# (c) Higgs mass implied by R1 : run down from M_Pl with lambda=0
z=crit_yt_v(g0,loop=3); ypl=up(z,g0,loop=3)
sol=H.run_rge([ypl[0],ypl[1],ypl[2],ypl[3],0.0],t_pl,t_v,n_f=6,loop_order=3); lam_v=sol.y[4,-1]
print(f"(c) R1: lambda(v)={lam_v:.5f}  m_H(tree, sqrt(2 lam) v)={math.sqrt(2*lam_v)*V:.1f} GeV   [lane's own y_t=0.9176 chain: 125.1 with its CW/matching]")
sol2=H.run_rge([ypl[0],ypl[1],ypl[2],0.9176*0+ypl[3],0.0],t_pl,t_v,n_f=6,loop_order=3)

# (d) prior sensitivity of the '3 bits'
import repo_compression_copy as R
gM=R.run_gauge_up(); mt=lambda y:R.mt_from_yt_MPl(gM,y)
y0=(math.sqrt(4*math.pi*0.09067))/math.sqrt(6); m0=mt(y0)
print("(d) bits for a hit within +-tol in m_t, under different log-uniform priors on y_t(M_Pl):")
for (lo,hi) in ((0.22,0.65),(0.1,1.0),(0.05,1.5)):
    row=[]
    for tol in (0.03,0.01,0.0007):
        ylo=brentq(lambda y: mt(y)-m0*(1-tol),0.01,y0); yhi=brentq(lambda y: mt(y)-m0*(1+tol),y0,3.0)
        p=math.log(min(yhi,hi)/max(ylo,lo))/math.log(hi/lo); row.append(f"+-{tol*100:g}%: {-math.log2(p):.1f} b")
    print(f"   prior [{lo},{hi}]: "+"; ".join(row))
