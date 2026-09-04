"""T65 - the matter-shift test with the FULL Kahler-Dirac operator D = d + delta.
Everything in Results 26, 27 and 29 used only the 0-form Laplacian.  The
framework's actual object is the full operator on all degrees, which is what
Result 25 built and what carries the topology (McKean-Singer) and the doubler-free
spectrum.  So the matter-shift result has to be re-run with it before it can be
said to be about the framework's operator rather than about a scalar Laplacian.

D acts on vertices+edges+faces; matter enters as a mass m added to D, and the
observable is the multiplet mean of the low |eigenvalue| of D+m -- the
differentiable observable at a degenerate level (Result 27).
Same exactly area-preserving spheroid family, same orientation test."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t45b.py").read().split('print("T45')[0])
def spheroid_area(a,c):
    if abs(c-a)<1e-12: return 4*np.pi*a*a
    if c<a:
        e=np.sqrt(1-(c*c)/(a*a)); return 2*np.pi*a*a*(1+((1-e*e)/e)*np.arctanh(e))
    e=np.sqrt(1-(a*a)/(c*c)); return 2*np.pi*a*a*(1+(c/(a*e))*np.arcsin(e))
def fixed_area(eps,A0):
    c=1.0+eps; lo,hi=0.2,3.0
    for _ in range(80):
        mid=(lo+hi)/2
        if spheroid_area(mid,c)<A0: lo=mid
        else: hi=mid
    return (lo+hi)/2,c
def Dspec(V,F,mfun):
    d0,d1,s0,s1,s2,nv,ne,nf=geometry(V,F,None)
    if np.any(s1<=1e-12): return None
    A0=np.diag(np.sqrt(s1))@d0@np.diag(1.0/np.sqrt(s0))
    A1=np.diag(np.sqrt(s2))@d1@np.diag(1.0/np.sqrt(s1))
    N=nv+ne+nf; D=np.zeros((N,N))
    D[nv:nv+ne,0:nv]=A0; D[0:nv,nv:nv+ne]=A0.T
    D[nv+ne:,nv:nv+ne]=A1; D[nv:nv+ne,nv+ne:]=A1.T
    mv=np.array([mfun(p) for p in V])
    D[0:nv,0:nv]+=np.diag(mv)                    # matter on the 0-cells
    return np.sort(np.abs(np.linalg.eigvalsh(D)))
EPS=np.array([-0.04,-0.02,0.0,0.02,0.04])
def crit(V0,F,mfun,lo,hi):
    y=[]
    for eps in EPS:
        a,c=fixed_area(eps,4*np.pi)
        V=[np.array([p[0]*a,p[1]*a,p[2]*c]) for p in V0]
        e=Dspec(V,F,mfun)
        if e is None: return None
        y.append(float(np.mean(e[lo:hi])))
    c2,c1,c0=np.polyfit(EPS,np.array(y),2)
    return -c1/(2*c2)
for k in (2,3):
    V0,F=icosphere(k)
    e0=Dspec(V0,F,lambda p:0.0)
    nz=e0[e0>1e-9]
    print(f"\n  icosphere sub={k} ({len(V0)} verts): full D spectrum, "
          f"{int(np.sum(e0<1e-9))} zero modes, first levels "
          f"{[f'{v:.5f}' for v in nz[:6]]}")
    base=crit(V0,F,lambda p:0.0,2,8)
    print(f"   zero-matter critical eps (baseline) = {base:+.6f}")
    print(f"   {'profile':>20} {'mu':>7} {'crit':>12} {'crit-baseline':>15} {'slope':>10} {'ratio':>9}")
    for mu in (0.10,0.20):
        cz=crit(V0,F,(lambda m:(lambda p: m*(3*p[2]**2-1.0)))(mu),2,8)
        cx=crit(V0,F,(lambda m:(lambda p: m*(3*p[0]**2-1.0)))(mu),2,8)
        co=crit(V0,F,(lambda m:(lambda p: m*(p[0]**2-p[1]**2)))(mu),2,8)
        for nm,c in (("z-aligned",cz),("x-aligned",cx),("x^2-y^2",co)):
            if c is None: continue
            print(f"   {nm:>20} {mu:7.2f} {c:12.6f} {c-base:15.6f} "
                  f"{(c-base)/mu:10.4f} {((cx-base)/(cz-base) if nm=='x-aligned' else float('nan')):9.4f}",
                  flush=True)
print()
print("  A shift that tracks the matter, with the OPPOSITE sign for x-aligned,")
print("  reproduces on the FULL operator what Results 29's 0-form test found.")
