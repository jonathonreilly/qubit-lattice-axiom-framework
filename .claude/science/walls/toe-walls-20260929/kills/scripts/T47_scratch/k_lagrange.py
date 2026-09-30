"""KILL check: is the attack's N->inf 'limit' a property of the field or of the repo's global cubic-spline interpolation of the lattice field?
Replace the global cubic spline by a LOCAL 6-point Lagrange tensor interpolation (no ringing from the source peak) and rerun the same functional."""
import sys, math, time
sys.dont_write_bytecode=True
import numpy as np
import ladder_infvol as L
rh=L.rh; tcomp=rh.tcomp
def lagr_weights(t, npts=6):
    # t = position within stencil; nodes at 0..npts-1
    nodes=np.arange(npts,dtype=float); w=np.ones(npts)
    for i in range(npts):
        for j in range(npts):
            if i!=j: w[i]*=(t-nodes[j])/(nodes[i]-nodes[j])
    return w
CACHE={}
def interp_local(phi_grid, xyz):
    N=phi_grid.shape[0]; c=(N-1)//2
    idx=[]; ws=[]
    for a in range(3):
        u=c+xyz[a]; fl=math.floor(u); base=fl-2
        idx.append(np.arange(base,base+6)); ws.append(lagr_weights(u-base))
    sub=phi_grid[np.ix_(idx[0],idx[1],idx[2])]
    return float(np.einsum('i,j,k,ijk->',ws[0],ws[1],ws[2],sub))
def run(N, radius=4.25, variant='xx'):
    tcomp.interpolated_phi=interp_local
    rh.ETA_CACHE.clear(); rh.ANCHOR_CACHE.clear()
    rh.base_eta_floor=L.make(variant,radius)
    r=rh.compute_row(N)
    return dict(N=N,qT=r.gamma_t_center/r.gamma_t_shell,sTE=r.gamma_t_shell/r.gamma_e_shell,rhoE=r.rho_e,qE=r.q_e,gTc=r.gamma_t_center,gTs=r.gamma_t_shell,gEc=r.gamma_e_center,gEs=r.gamma_e_shell)
if __name__=='__main__':
    variant=sys.argv[1]; sizes=[int(x) for x in sys.argv[2].split(',')]; radius=float(sys.argv[3]) if len(sys.argv)>3 else 4.25
    for N in sizes:
        t=time.time(); d=run(N,radius,variant)
        print(f"LOCAL-LAGRANGE {variant} R={radius} N={N:3d} qT={d['qT']:+.4f} sTE={d['sTE']:+.4f} rhoE={d['rhoE']:+.4f} qE={d['qE']:+.4f} gTc={d['gTc']:+.3e} gTs={d['gTs']:+.3e} gEc={d['gEc']:+.3e} gEs={d['gEs']:+.3e} [{time.time()-t:.0f}s]",flush=True)
