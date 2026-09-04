"""T43 - THE REFINEMENT GATE WITH MATTER, plus the analytic reason it passes.
T42 showed the cell-complex operator gives the same continuum spectrum for
uniform, wave, and two-mode choppings of the same interval, at O(1/L^2).  The
rigid-lattice construction failed the analogous test by 54% (Results 19-22), and
it failed WITH MATTER, so the cell version has to be tested with matter too.

Same physical system, two different choppings.  The matter is a function of
PROPER POSITION, m(s), sampled at the cell centres of each chopping -- that is
the honest 'same physics, different coordinates'.

Three routes, so nothing rests on one:
  (1) spectra vs the same chopping-independent limit, refined;
  (2) MODE-BY-MODE agreement between two choppings at the SAME L, out to high n
      -- a far stronger statement than the lowest mode matching the continuum;
  (3) the ANALYTIC reason, checked symbolically: with s_(x+1) - s_(x-1) =
      (1/2) l_(x-1) + l_x + (1/2) l_(x+1), the operator (1/l_x)(1/2)(psi_(x+1) -
      psi_(x-1)) reproduces d/ds with the FIRST-order l' error cancelling
      exactly, leaving O(l'')."""
import numpy as np, sympy as sp
NF=2
EPSm=np.array([[0.,0.],[1.,0.]]); IOTm=np.array([[0.,1.],[0.,0.]]); GAM=EPSm+IOTm
def centres(l):
    e=np.concatenate([[0.0],np.cumsum(l)]); return e[:-1]+l/2
def Q_of(l,mvals):
    L=len(l); Q=np.zeros((L*NF,L*NF))
    for x in range(L):
        i=x*NF; Q[i:i+NF,i:i+NF]+=mvals[x]*np.eye(NF)
        for sgn in (+1,-1):
            y=(x+sgn)%L; Q[i:i+NF,y*NF:y*NF+NF]+=sgn*0.5*(1.0/l[x])*GAM
    return Q
def chop(L,T,kind,amp=0.6):
    if kind=="uniform": l=np.ones(L)
    elif kind=="wave":  l=1.0+amp*np.cos(2*np.pi*np.arange(L)/L)
    elif kind=="wave3": l=1.0+amp*np.cos(2*np.pi*3*np.arange(L)/L)
    elif kind=="ramp":  l=1.0+amp*(np.arange(L)/L-0.5)*2
    return np.abs(l)*(T/np.abs(l).sum())
T=2*np.pi
def mfun(s,m0=0.7,mu=0.45): return m0+mu*np.cos(s)      # matter as a function of PROPER position
def modes(l,k=8):
    ev=np.linalg.eigvals(Q_of(l,[mfun(c) for c in centres(l)]))
    return np.array(sorted(ev,key=lambda z:(abs(z.imag),z.real)))[:2*k]
print("T43 (1)+(2)  INHOMOGENEOUS matter m(s) = 0.7 + 0.45 cos(s), T = 2 pi")
print("     same physics, four different choppings; modes sorted by |Im|")
print()
ref=None
for L in (32,64,128,256):
    row=[]
    specs={}
    for kind in ("uniform","wave","wave3","ramp"):
        specs[kind]=modes(chop(L,T,kind))
    base=specs["uniform"]
    print(f"   L={L:4d}   max |lambda(chopping) - lambda(uniform)| over the lowest 8 modes:")
    for kind in ("wave","wave3","ramp"):
        d=np.max(np.abs(np.sort_complex(specs[kind])-np.sort_complex(base)))
        print(f"      {kind:8s} : {d:.4e}", flush=True)
    print(f"      (lowest four |Im| of uniform: {[f'{abs(z.imag):.6f}' for z in base[:8:2]]})", flush=True)
    print(flush=True)
print("T43 (3)  ANALYTIC: expand the operator on a smooth chopping")
x=sp.symbols('x'); h=sp.Symbol('h',positive=True)
lf=sp.Function('l'); pf=sp.Function('p')
# cell centres: s(x); s(x+1)-s(x) = (l(x)+l(x+1))/2
lx=lf(x); lxp=lf(x)+h*sp.diff(lf(x),x)+h**2/2*sp.diff(lf(x),x,2)
lxm=lf(x)-h*sp.diff(lf(x),x)+h**2/2*sp.diff(lf(x),x,2)
span=sp.simplify(lxm/2+lx+lxp/2)          # s(x+1) - s(x-1)
print(f"   s(x+1) - s(x-1) = {sp.simplify(sp.expand(span))}")
print(f"   divided by 2 l(x):  {sp.simplify(sp.expand(span/(2*lx)))}")
print(f"   -> the l' term CANCELS; the leading error is the l'' term:")
print(f"      {sp.simplify(sp.expand(span/(2*lx)) - 1)}")
print()
print("   So (1/l_x)(1/2)(psi_(x+1) - psi_(x-1)) = d psi/ds * (1 + O(l'')),")
print("   second-order accurate for ANY smooth cell-length profile -- which is")
print("   exactly the measured O(1/L^2) in T42 and above.")
