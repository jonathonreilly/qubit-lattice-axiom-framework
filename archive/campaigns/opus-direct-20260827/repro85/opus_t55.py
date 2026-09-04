"""T55 - why is the circumcentric l=1 level 1.999998 and not 2 +- O(h^2)?
T54b: with the dual that Result 1's uniform-weight condition selects, the l=1
level came out 1.999982 (sub=2) and 1.999998 (sub=3) -- errors 1.8e-5 and 2e-6,
where ordinary O(h^2) mesh error should be ~1e-2 and ~1e-3.  That is a thousand
times too accurate to be an accident, and the l=2, l=3 levels are NOT that
accurate, so it is specific to l=1.

Hypothesis: on a mesh whose vertices lie exactly on a sphere, the l=1
eigenfunctions are the RESTRICTIONS OF LINEAR FUNCTIONS x, y, z -- and the
circumcentric (cotan) Laplacian may reproduce those EXACTLY, because the cotan
Laplacian is built from the same circumcentric geometry that the sphere's
symmetry respects.  Test it directly: measure the residual

     || L0 X - lambda X ||  /  || X ||       for X = x, y, z

for the circumcentric dual and for the barycentric one.  If it is at machine
precision for circumcentric and not for barycentric, the near-exactness is a real
structural property of the selected dual, not luck."""
import numpy as np
exec(open("/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/opus_t54b.py").read().split('print("T54  cross-check')[0])
def L0_of(V,F,kind):
    if kind=="barycentric":
        s0b=bary_star0(V,F); _,s1,s2,_,_,_,E=build_dual(V,F,"barycentric"); s0=s0b
    else:
        s0,s1,s2,_,_,_,E=build_dual(V,F,"circumcentric")
    d0,d1=incidence(V,F,E)
    # unweighted (non-symmetrised) Laplacian: L = star0^-1 d0^T star1 d0
    return np.diag(1.0/s0)@d0.T@np.diag(s1)@d0, s0
print("T55  is L0 X = lambda X EXACT for the linear functions X = x,y,z ?")
print(f"   {'mesh':>16} {'dual':>16} {'lambda(x)':>13} {'residual/|X|':>15} {'l=1 level err':>15}")
for k in (1,2,3,4):
    V,F=icosphere(k)
    for kind in ("circumcentric","barycentric"):
        try: L,s0=L0_of(V,F,kind)
        except Exception as ex: print(f"   sub={k} {kind}: {ex}"); continue
        res=[]; lam=[]
        for a in range(3):
            X=np.array([p[a] for p in V])
            LX=L@X
            l=float(np.dot(s0*X,LX)/np.dot(s0*X,X))
            lam.append(l); res.append(float(np.linalg.norm(LX-l*X)/np.linalg.norm(X)))
        # the l=1 level from the actual spectrum, for comparison
        s0f,s1f,s2f,_,_,_,E=build_dual(V,F,kind if kind=="circumcentric" else "barycentric")
        if kind=="barycentric": s0f=bary_star0(V,F)
        d0,d1=incidence(V,F,E)
        A0=np.diag(np.sqrt(s1f))@d0@np.diag(1.0/np.sqrt(s0f))
        e=np.sort(np.clip(np.linalg.eigvalsh(A0.T@A0),0,None)); nz=e[e>1e-9]
        print(f"   {'icosphere '+str(k):>16} {kind:>16} {np.mean(lam):13.9f} "
              f"{max(res):15.3e} {abs(float(np.mean(nz[:3]))-2.0):15.3e}", flush=True)
print()
print("   residual at machine precision => the linear functions are EXACT")
print("   eigenfunctions of the selected (circumcentric) Laplacian on an inscribed")
print("   mesh, so the l=1 level is exact up to how well lambda itself is resolved.")
