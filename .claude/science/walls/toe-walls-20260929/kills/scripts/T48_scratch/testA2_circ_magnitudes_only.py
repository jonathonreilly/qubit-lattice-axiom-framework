"""A2 supplement: circulant universal seed, |V| magnitudes only (drop J) -- is there ANY circulant seed that gets the three magnitudes?"""
import numpy as np, json, time
from scipy.optimize import least_squares
from common import *
from testA_lib import observables
res={}
for sname in ("MZ","LOW"):
    for p in (1.0,0.5):
        tu=np.array(MASSES[sname]["u"])**p; td=np.array(MASSES[sname]["d"])**p
        best=None; nf=0; nt=0
        for rho in np.linspace(0.02,1.4,80):
            for phi in np.linspace(0,np.pi,49):
                nt+=1
                o=observables(circ_seed(rho,phi),tu,td)
                if o is None: continue
                nf+=1
                w=max(abs(o["Vus"]/OBS["Vus"]-1),abs(o["Vcb"]/OBS["Vcb"]-1),abs(o["Vub"]/OBS["Vub"]-1))
                if best is None or w<best[0]: best=(w,rho,phi,o)
        print(f"{sname} p={p}: circulant seed, magnitudes only: best worst-rel-err = {best[0]:.3f} at rho={best[1]:.3f}, phi={np.degrees(best[2]):.0f} deg (feasible {nf}/{nt}); Vus,Vcb,Vub = {best[3]['Vus']:.4f},{best[3]['Vcb']:.4f},{best[3]['Vub']:.4f}",flush=True)
        res[f"{sname}_p{p}"]=dict(worst=float(best[0]),rho=float(best[1]),phi_deg=float(np.degrees(best[2])),obs={k:float(v) for k,v in best[3].items()},feasible=nf/nt)
json.dump(res,open("testA2_results.json","w"),indent=1)
