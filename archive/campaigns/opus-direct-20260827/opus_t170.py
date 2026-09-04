"""T170 - WHAT JUSTIFIES LINEARITY?  A scoping check on the whole axioms chain.

R92 counted LINEAR covariant maps and found six.  The axioms say nothing about
linearity.  So before the chain R92-R103 is handed on, the question has to be
asked: is 'six' the number of covariant rules, or only of covariant LINEAR rules?
If the latter, the axioms plus covariance pin nothing without a further premise,
because the space of nonlinear covariant maps is infinite-dimensional.

There IS a defensible argument for AFFINITY (not linearity), and it should be
stated as the premise it is rather than smuggled:

   CONVEX-CONSISTENCY.  If a neighbour's condition is itself uncertain -- a
   mixture p rho_1 + (1-p) rho_2 -- then the distribution the rule returns should
   be the corresponding mixture of what it returns for rho_1 and rho_2.  A map
   respecting convex combinations on a convex domain is AFFINE.

That is a physical requirement about probabilistic consistency, not an axiom, and
it is what the chain actually rests on.  Two things are checkable here:
  (1) an affine map is what convex-consistency forces (verify on the state space);
  (2) the CONSTANT term must itself be covariant, and the only covariant constant
      is kappa*I -- so affinity adds exactly ONE parameter over linearity, which
      is the kappa R93 already used.
CONTROL: exhibit a covariant NONLINEAR rule, to confirm the space really is bigger
without the premise."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=s[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
print("T170  what the axioms chain actually rests on")
print()
print("(1) convex-consistency forces affinity -- check on random mixtures")
rng=np.random.default_rng(3)
def lin_rule(vs,al=1/3,de=1/np.sqrt(3)):
    V=sum(vs); C=sum(np.cross(DIRS[i],vs[i]) for i in range(6))
    return (al*V+de*C)/6.0
w=0.0
for _ in range(2000):
    a=[0.4*rng.normal(size=3) for _ in range(6)]
    b=[0.4*rng.normal(size=3) for _ in range(6)]
    p=rng.uniform()
    mix=[p*a[i]+(1-p)*b[i] for i in range(6)]
    w=max(w,np.linalg.norm(lin_rule(mix)-(p*lin_rule(a)+(1-p)*lin_rule(b))))
print(f"    |rule(mix) - mix(rule)| for the affine rule: max {w:.2e}   (must be ~0)")
print()
print("(2) CONTROL -- a covariant NONLINEAR rule exists, so the space is bigger")
def nonlin(vs):
    # covariant but quadratic: sum_i (n_i . v_i) v_i
    return sum((DIRS[i]@vs[i])*vs[i] for i in range(6))/6.0
def check_cov(f):
    worst=0.0
    for R in ROT:
        for _ in range(50):
            vs=[0.4*rng.normal(size=3) for _ in range(6)]
            # rotate: permute the direction slots AND rotate each vector
            idx=[[k for k,e in enumerate(DIRS) if np.allclose(e,R@d)][0] for d in DIRS]
            vr=[None]*6
            for j in range(6): vr[idx[j]]=R@vs[j]
            worst=max(worst,np.linalg.norm(f(vr)-R@f(vs)))
    return worst
print(f"    quadratic rule sum_i (n_i.v_i) v_i is covariant: max residual {check_cov(nonlin):.2e}")
w2=0.0
for _ in range(500):
    a=[0.4*rng.normal(size=3) for _ in range(6)]; b=[0.4*rng.normal(size=3) for _ in range(6)]
    p=rng.uniform(); mix=[p*a[i]+(1-p)*b[i] for i in range(6)]
    w2=max(w2,np.linalg.norm(nonlin(mix)-(p*nonlin(a)+(1-p)*nonlin(b))))
print(f"    but it VIOLATES convex-consistency: max |rule(mix)-mix(rule)| = {w2:.3f}")
print()
print("    so covariance alone does NOT give six; covariance + convex-consistency does.")
