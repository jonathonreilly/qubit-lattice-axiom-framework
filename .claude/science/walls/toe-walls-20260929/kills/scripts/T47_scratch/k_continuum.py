"""KILL check: Route-2 functional on an ANALYTIC free-space potential (no box, no lattice Green function, no spline).
phi(x) = sum_i q_i/(4 pi |x-x_i|) for the 7 support sites; same finite-difference Einstein code (imported read-only)."""
import sys, math
sys.dont_write_bytecode=True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
import frontier_quark_route2_honest_gravity_metric_rhoe_characterization as rh
import frontier_same_source_metric_ansatz_scan as same
tcomp=rh.tcomp
SITES=np.array([v for v in same.SUPPORT_COORDS],float)
class Phi:
    def __init__(self,q): self.q=np.asarray(q,float)
def interp(phi,xyz):
    d=np.linalg.norm(SITES-np.asarray(xyz)[None,:],axis=1)
    return float(np.sum(phi.q/(4*math.pi*d)))
tcomp.interpolated_phi=interp
def tf(einstein):
    sp=einstein[1:,1:]; return sp-np.eye(3)*np.trace(sp)/3.0
def floor(q,radius,variant):
    phi=Phi(q); vals=[]
    for p in rh.probe_points(radius):
        _,ein=tcomp.ricci_and_einstein(lambda x: tcomp.adm_metric(phi,x,0.0,0.0,0.0),p,h=rh.RICCI_H)
        t=tf(ein)
        vals.append(t[0,0] if variant=='xx' else np.max(np.abs(t)))
    return vals[0] if variant=='xx' else max(vals)
def g(q,d,radius,variant):
    return (floor(q+rh.EPS*d,radius,variant)-floor(q-rh.EPS*d,radius,variant))/(2*rh.EPS)
def row(radius,variant):
    gTc=g(rh.E0,rh.TX,radius,variant); gTs=g(rh.S_UNIT,rh.TX,radius,variant)
    gEc=g(rh.E0,rh.EX,radius,variant); gEs=g(rh.S_UNIT,rh.EX,radius,variant)
    qT=gTc/gTs; qE=gEc/gEs
    return dict(R=radius,base_E0=floor(rh.E0,radius,variant),base_S=floor(rh.S_UNIT,radius,variant),gTc=gTc,gTs=gTs,gEc=gEc,gEs=gEs,qT=qT,sTE=gTs/gEs,qE=qE,rhoE=6*(qE-1))
if __name__=='__main__':
    for variant in ('xx','max'):
        print('variant',variant)
        for R in (3.5,4.0,4.25,4.5,5.0,6.0,8.0,12.0):
            d=row(R,variant)
            print("  R=%5.2f base(E0)=%+.3e base(S)=%+.3e gTc=%+.3e gTs=%+.3e gEc=%+.3e gEs=%+.3e  qT=%+.4f sTE=%+.4f rhoE=%+.4f"%(d['R'],d['base_E0'],d['base_S'],d['gTc'],d['gTs'],d['gEc'],d['gEs'],d['qT'],d['sTE'],d['rhoE']),flush=True)
