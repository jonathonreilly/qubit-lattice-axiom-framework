"""T23 - IS THE LATTICE a_1 THE RICCI SCALAR?

For g_mumu = 1 + alpha_mu A sin(k x0), sympy (T22) gives EXACTLY
      < sqrt(g) R >  =  A^2 k^2 (a1 a2 + a1 a3 + a2 a3) / 4  =  A^2 k^2 (S'^2 - Q')/8
with S' = a1+a2+a3, Q' = a1^2+a2^2+a3^2  --  note NO dependence on alpha_0
(a g_00 modulation is pure gauge).  Hence the continuum
      Delta int sqrt(g) a_1 = (1/6) int sqrt(g) R = Vol A^2 k^2 (S'^2 - Q')/48.

The lattice, having only hypercubic symmetry, may instead produce any combination
of the FOUR quadratic invariants available with a preferred derivative direction:
      S'^2 ,  Q' ,  alpha_0 S' ,  alpha_0^2 .
Measuring many channels and fitting all four coefficients decides whether the
induced a_1 IS the Einstein term (b = (1/48, -1/48, 0, 0)) or something else."""
import numpy as np, sys, os, time; sys.path.insert(0,".")
from bridge_fit import *
from bridge_spec import local_Hmatrix
L=int(sys.argv[1]); AMP=float(sys.argv[2]); NKW=int(sys.argv[3])
IMP=(len(sys.argv)<5) or sys.argv[4]!='plain'
CH=[(0,1,1,0),(0,1,-1,0),(1,1,1,1),(1,0,0,0),(0,1,0,0),(1,1,0,0),(0,1,1,1),
    (0,2,1,0),(1,0,1,-1),(2,1,1,1),(0,1,-1,1),(1,1,-1,0),(0,3,1,0),(1,2,0,0)]
if len(sys.argv)>5 and sys.argv[5]=='short':
    CH=[(0,1,1,0),(0,1,-1,0),(1,1,1,1),(1,0,0,0),(0,1,0,0),(0,1,1,1),(0,2,1,0),(2,1,1,1)]
fn=f"struct_L{L}_a{AMP}_nk{NKW}_{len(CH)}.npz"
if os.path.exists(fn):
    z=np.load(fn); lam={k:z[k] for k in z.files if k.endswith('lam')}; VR={k:z[k] for k in z.files if k.endswith('VR')}
else:
    lam={}; VR={}
    for tag,al in [('flat',(0,0,0,0))]+[(str(c),c) for c in CH]:
        t0=time.time(); S=edge_s(L,0.0 if tag=='flat' else AMP,NKW,list(al)); g=geometry(S,L)
        _,lm=local_Hmatrix(S,L,{'z':lambda w:w*0},ret_spec=True,geom=g)
        lam[tag+'lam']=np.sort(lm); VR[tag+'VR']=np.array([g['Vol'],g['Reg']])
        print(f"  {tag}: {time.time()-t0:.0f}s",flush=True)
    np.savez_compressed(fn,**lam,**VR)
lf=lam['flatlam']; Vf,Rf=VR['flatVR']; muf=lf+lf*lf/24.0 if IMP else lf
k2=(2*np.pi*NKW/L)**2; Vol=float(L)**4; NORM=Vol*AMP**2*k2
print(f"\nT23 L={L} amp={AMP} nk={NKW} {'improved' if IMP else 'plain'} k^2={k2:.5f}  "
      f"norm=Vol*A^2*k^2={NORM:.4f}")
def uval(c,s):
    lp=lam[str(c)+'lam']; Vp,Rp=VR[str(c)+'VR']; mu=lp+lp*lp/24.0 if IMP else lp
    P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
    return (P-(Vp-Vf))/s/NORM
def inv(c):
    a0=c[0]; Sp=c[1]+c[2]+c[3]; Qp=c[1]**2+c[2]**2+c[3]**2
    return np.array([Sp**2,Qp,a0*Sp,a0**2],dtype=float)
X=np.array([inv(c) for c in CH]); cont=np.array([(inv(c)[0]-inv(c)[1])/48.0 for c in CH])
print(f"\n{'s':>5} {'b(S^2)*48':>10} {'b(Q)*48':>10} {'b(a0 S)*48':>11} {'b(a0^2)*48':>11} "
      f"{'|resid|/|u|':>11}   continuum: (+1, -1, 0, 0)")
for s in (4,5,6,8,10,12,16,20,25,32,40,50,60):
    if s*k2>1.1: break
    u=np.array([uval(c,s) for c in CH])
    b,*_=np.linalg.lstsq(X,u,rcond=None); r=np.linalg.norm(u-X@b)/np.linalg.norm(u)
    print(f"{s:5.1f} {48*b[0]:10.4f} {48*b[1]:10.4f} {48*b[2]:11.4f} {48*b[3]:11.4f} {r:11.3e}")
print(f"\nper-channel u/u_continuum:")
SLIST=[x for x in (4,6,8,12,16,20,32,50) if x*k2<=1.1]
print(f"{'alpha':>16} {'S^2-Q':>7}"+"".join(f"{'s=%g'%s:>9} " for s in SLIST))
for c in CH:
    d=inv(c)[0]-inv(c)[1]
    row=f"{str(c):>16} {d:7.0f}"
    for s in SLIST:
        if s*k2>1.1: continue
        u=uval(c,s); row+=f"{u/(d/48.0) if d!=0 else np.nan:9.4f} " if d!=0 else f"{'(null)':>9} "
    print(row)
