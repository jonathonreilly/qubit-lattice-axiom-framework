"""T43c - is the ramp's O(1/L) a defect of the construction or of my test?
T43b: 'wave' and 'wave3' choppings converge at O(1/L^2); 'ramp' only at O(1/L)
and it splits the degenerate +-n pair.  PREDICTION from the analytic error term
h^2 l''/(4 l): the ramp is  l = 1 + a(x/L - 1/2)*2  on a PERIODIC chain, so it
jumps at the wrap-around and l'' carries a delta there.  If that is the cause,
then a chopping that is just as lopsided but SMOOTH and periodic must return to
O(1/L^2), and a deliberately re-introduced discontinuity must go back to O(1/L).
Both directions are tested -- a prediction, not a rationalisation."""
import numpy as np
NF=2
EPSm=np.array([[0.,0.],[1.,0.]]); IOTm=np.array([[0.,1.],[0.,0.]]); GAM=EPSm+IOTm
def centres(l):
    e=np.concatenate([[0.0],np.cumsum(l)]); return e[:-1]+l/2
def Q_of(l,mv):
    L=len(l); Q=np.zeros((L*NF,L*NF))
    for x in range(L):
        i=x*NF; Q[i:i+NF,i:i+NF]+=mv[x]*np.eye(NF)
        for sgn in (+1,-1):
            y=(x+sgn)%L; Q[i:i+NF,y*NF:y*NF+NF]+=sgn*0.5*(1.0/l[x])*GAM
    return Q
T=2*np.pi
def mk(L,kind):
    u=np.arange(L)/L; th=2*np.pi*u
    if   kind=="uniform":            l=np.ones(L)
    elif kind=="ramp (DISCONT)":     l=1.0+0.6*(u-0.5)*2
    elif kind=="sawtooth (DISCONT)": l=1.0+0.6*(2*(u%0.5)/0.5-1)
    elif kind=="skew-smooth":        l=np.exp(0.6*np.cos(th)+0.35*np.sin(2*th))   # lopsided, C-infinity
    elif kind=="peaked-smooth":      l=np.exp(1.1*np.cos(th))                     # 3:1 length ratio, smooth
    l=np.abs(l); return l*(T/l.sum())
def energies(l,k=6):
    mv=[0.7+0.45*np.cos(c) for c in centres(l)]
    return np.sort(np.abs(np.linalg.eigvals(Q_of(l,mv)).imag))[:2*k]
print("T43c  gap vs the uniform chopping, same interval, inhomogeneous matter")
print("      PREDICTION: smooth -> O(1/L^2) (gap falls x4 per doubling)")
print("                  discontinuous -> O(1/L) (gap falls x2 per doubling)")
print()
kinds=["ramp (DISCONT)","sawtooth (DISCONT)","skew-smooth","peaked-smooth"]
prev={k:None for k in kinds}
print(f"   {'L':>5} " + "".join(f"{k:>26}" for k in kinds))
for L in (32,64,128,256,512):
    base=energies(mk(L,"uniform")); row=f"   {L:5d} "
    for k in kinds:
        g=float(np.max(np.abs(energies(mk(L,k))-base)))
        r=(prev[k]/g) if prev[k] else float('nan')
        row+=f"{g:>14.4e} (x{r:4.1f})" if prev[k] else f"{g:>14.4e}  (--) "
        prev[k]=g
    print(row, flush=True)
print()
print(f"   length ratio max/min: skew-smooth {mk(256,'skew-smooth').max()/mk(256,'skew-smooth').min():.2f}, "
      f"peaked-smooth {mk(256,'peaked-smooth').max()/mk(256,'peaked-smooth').min():.2f}, "
      f"ramp {mk(256,'ramp (DISCONT)').max()/mk(256,'ramp (DISCONT)').min():.2f}")
print("   (the smooth choppings are at least as lopsided as the ramp, so a")
print("    smoothness explanation is not an amplitude explanation in disguise)")
