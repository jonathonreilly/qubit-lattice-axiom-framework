"""Kill check: R2 (Pati-Salam pair (1/4, 3/14)) needs g_4^2 = 1 at the lattice scale, but t33_C runs the pair down with the SM-extrapolated g_3^2(M_Pl)=0.2375.
Re-run the R2 pair with g_3^2(M_Pl) = 1 (the value R2's own premise sets) and with intermediate values; also the R2 relation with g_4^2 = SM g_3^2."""
import sys, numpy as np
sys.path.insert(0,'/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/walls/attacks/T33_scratch')
from rge import *
up = up_from_mz(MPL,2)
print("SM-extrapolated y0 at MPl (g1,g2,g3,yt):", up)
def run_pair(g22,gp2,g32,loops=2):
    y0=np.array([np.sqrt(5/3*gp2),np.sqrt(g22),np.sqrt(g32),up[3]])
    try:
        y=run(y0,MPL,MZ,loops)
    except Exception as e:
        return None
    if not np.all(np.isfinite(y)): return None
    o=observables(y); return o
for g32 in (0.2375, 0.5, 1.0):
    for loops in (1,2):
        o=run_pair(0.25,3/14,g32,loops)
        if o is None: print(f"R2 pair, g3^2(MPl)={g32}, {loops}-loop: no finite result"); continue
        print(f"R2 pair (1/4,3/14), g3^2(MPl)={g32}, {loops}-loop: sin2={o['s2']:.4f} ({(o['s2']/S2W_MZ-1)*100:+.1f}%) 1/aem={o['aem_inv']:.2f} ({(o['aem_inv']/AEM_INV_MZ-1)*100:+.1f}%)  [g3^2(MZ)={o['g32']:.3f}]")
# what does g3^2=1 at MPl do to g3 itself (Landau pole scale)?
import scipy.integrate as si
def rhs1(t,g): return -7*g**3/(16*np.pi**2)
sol=si.solve_ivp(lambda t,g: [-7*g[0]**3/(16*np.pi**2)*(-1)], [0,-30],[1.0]) # placeholder no use
# analytic 1-loop: 1/alpha3(mu)=1/alpha3(MPl)-(7/2pi) ln(MPl/mu) -> pole where zero
a3inv=4*np.pi/1.0
Lpole=a3inv*2*np.pi/7
print("1-loop Landau pole of g3^2=1 at M_Pl: mu = M_Pl*exp(-%.2f) = %.2e GeV"%(Lpole, MPL*np.exp(-Lpole)))
# PS relation needs g4^2:  data pair (gL^2=gR^2=SM g2^2) requires
o=observables(up)
need=(2/3)/(1/o['gp2']-1/o['g22']); print("g4^2 needed by PS relation with gL^2=gR^2=SM g2^2(MPl): %.3f  vs SM g3^2(MPl)=%.4f  (ratio %.1f)"%(need,o['g32'],need/o['g32']))
for g4 in (o['g32'],):
    gy=1/(1/0.25+(2/3)/g4)
    print("PS relation with g4^2=SM g3^2=%.4f, gL^2=gR^2=1/4: gY^2=%.4f"%(g4,gy))
