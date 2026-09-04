"""T25 - continuum extrapolation of the induced a_1 tensor structure.

The two lattice errors are a^2/s and a^2 k^2; the physical combination is s k^2.
Comparing (L=32, s) with (L=64, 4s) holds s k^2 FIXED and halves the effective
lattice spacing, so the residual error scales like 1/L^2 and
       b_inf = (4 b_64 - b_32)/3
is a Richardson extrapolation to the continuum at fixed physics."""
import numpy as np, sys; sys.path.insert(0,".")
CH8=[(0,1,1,0),(0,1,-1,0),(1,1,1,1),(1,0,0,0),(0,1,0,0),(0,1,1,1),(0,2,1,0),(2,1,1,1)]
def inv(c):
    a0=c[0]; Sp=c[1]+c[2]+c[3]; Qp=c[1]**2+c[2]**2+c[3]**2
    return np.array([Sp**2,Qp,a0*Sp,a0**2],dtype=float)
X=np.array([inv(c) for c in CH8])
def bvec(fn,L,AMP,NKW,s,imp=True):
    z=np.load(fn); lf=z['flatlam']; Vf,Rf=z['flatVR']
    muf=lf+lf*lf/24.0 if imp else lf
    k2=(2*np.pi*NKW/L)**2; NORM=float(L)**4*AMP**2*k2
    u=[]
    for c in CH8:
        lp=z[str(c)+'lam']; Vp,Rp=z[str(c)+'VR']; mu=lp+lp*lp/24.0 if imp else lp
        P=(float(np.exp(-s*mu).sum())-float(np.exp(-s*muf).sum()))*(4*np.pi*s)**2
        u.append((P-(Vp-Vf))/s/NORM)
    b,*_=np.linalg.lstsq(X,np.array(u),rcond=None)
    r=np.linalg.norm(np.array(u)-X@b)/np.linalg.norm(u)
    return 48*b, r
f32="struct_L32_a0.06_nk1_14.npz"; f64="struct_L64_a0.06_nk1_8.npz"
print("T25  matched s k^2, Richardson (4 b64 - b32)/3.   continuum = (+1, -1, 0, 0)")
print(f"{'s(32)':>6} {'s(64)':>6} {'s k^2':>7} | "
      +" ".join(f"{n:>26}" for n in ("b(S^2)","b(Q)","b(a0S)","b(a0^2)")))
print(f"{'':>6} {'':>6} {'':>7} | "+" ".join(f"{'L32':>8}{'L64':>9}{'Rich':>9}" for _ in range(4)))
for s32 in (4,5,6,8,10,12,15,16,20,25):
    s64=4*s32
    if s64*(2*np.pi/64)**2 > 1.1: break
    b32,r32=bvec(f32,32,0.06,1,s32); b64,r64=bvec(f64,64,0.06,1,s64)
    br=(4*b64-b32)/3
    row=f"{s32:6.1f} {s64:6.1f} {s32*(2*np.pi/32)**2:7.3f} | "
    row+=" ".join(f"{b32[i]:8.4f}{b64[i]:9.4f}{br[i]:9.4f}" for i in range(4))
    print(row)
print()
print("Same-s comparison (NOT matched physics; shows the raw L dependence):")
for s in (8,12,16,20,25,32,40,50,60):
    if s*(2*np.pi/64)**2>1.1: break
    out=f"  s={s:5.1f}  L64: "
    b64,r64=bvec(f64,64,0.06,1,s); out+=" ".join(f"{v:8.4f}" for v in b64)+f"   resid {r64:.1e}"
    if s<=25:
        b32,_=bvec(f32,32,0.06,1,s); out+="   | L32: "+" ".join(f"{v:8.4f}" for v in b32)
    print(out)
