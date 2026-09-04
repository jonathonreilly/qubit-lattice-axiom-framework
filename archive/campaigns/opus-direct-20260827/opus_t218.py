"""
T218 - AUDIT of R137's coincidence: is "the consistent family's endpoint IS the
Born weight" a real convergence, or is it one condition stated twice?

Four earlier coincidences in this packet (alpha = 1/3, the algebra fit, 16 = 16,
48 Weyl = 3 generations) all dissolved when the chain was written out.  This
applies the same check.

The question to answer: WHAT WOULD HAVE TO BE TRUE FOR THE AGREEMENT TO FAIL?
"""
import numpy as np

S = [np.array([[0,1],[1,0]],dtype=complex),
     np.array([[0,-1j],[1j,0]],dtype=complex),
     np.array([[1,0],[0,-1]],dtype=complex)]
rho = lambda v: (np.eye(2) + sum(v[i]*S[i] for i in range(3)))/2
rng = np.random.default_rng(7)
sph = lambda n: (lambda x: x/np.linalg.norm(x,axis=-1,keepdims=True))(rng.normal(size=(n,3)))

print("=== step 1: how big is the space R136's derivation lands in? ===")
# symmetric + isotropic + affine-in-each-argument functions of two Bloch vectors
A = sph(4000); B = sph(4000)
cand = {"1": np.ones(len(A)), "v.v'": np.sum(A*B,axis=1),
        "(v.v')^2": np.sum(A*B,axis=1)**2, "|v+v'|": np.linalg.norm(A+B,axis=1)}
Mx = np.array([cand["1"], cand["v.v'"]]).T
print(f"  affine+symmetric+isotropic basis: {{1, v.v'}} -> dimension 2 (1 after scale)")
for nm in ("(v.v')^2", "|v+v'|"):
    r = np.linalg.lstsq(Mx, cand[nm], rcond=None)
    res = np.max(np.abs(Mx@r[0]-cand[nm]))
    print(f"  is {nm:9s} inside it?  max residual {res:.3f}  -> {'yes' if res<1e-9 else 'NO (so the space really is 2-dim)'}")

print("\n=== step 2: is the Born weight automatically in that space? ===")
born = np.array([np.trace(rho(a)@rho(b)).real for a,b in zip(A[:800],B[:800])])
Mx2 = np.array([np.ones(800), np.sum(A[:800]*B[:800],axis=1)]).T
c,*_ = np.linalg.lstsq(Mx2, born, rcond=None)
print(f"  Tr(rho rho') = {c[0]:.6f} + {c[1]:.6f} (v.v'),  residual "
      f"{np.max(np.abs(Mx2@c-born)):.2e}")
print(f"  Tr(rho rho') is BILINEAR in the two density matrices by construction,")
print(f"  hence automatically affine in each -> it could not have landed outside.")

print("\n=== step 3: what picks the endpoint? ===")
print("  family (scale fixed): phi = 1 + lam (v.v'),  positivity phi >= 0 <=> |lam| <= 1.")
print("  at lam = 1: phi vanishes exactly when v.v' = -1, i.e. on ORTHOGONAL states.")
print("  Born weight Tr(rho rho') >= 0, vanishing exactly on ORTHOGONAL states.")
print("  => 'positivity boundary' and 'Born weight' are the SAME condition:")
print("     the unique member of the family that vanishes anywhere.")

print("\n=== step 4: what would have to be true for the agreement to FAIL? ===")
print("  (a) the Born weight not affine in each state -> impossible, it is bilinear;")
print("  (b) the consistent family not the 2-space {1, v.v'} -> would need covariance")
print("      or affineness of the potential to fail (R136 step 5/6);")
print("  (c) the family's positivity boundary not to vanish on orthogonal pairs")
print("      -> would need a different inner product on the Bloch sphere.")
print("  Given (a) is automatic, the agreement is forced ONCE the family is the")
print("  2-space.  So this is ONE condition stated twice, not two computations")
print("  that happened to agree.")

print("\n=== verdict, with the residual content stated ===")
print("  DEFLATED but NOT empty.  What survives is genuinely nontrivial:")
print("   * R136's chain (permanence -> Markov -> triangle-free -> Hammersley-")
print("     Clifford -> covariance -> affine potential) never mentions qubits,")
print("     Born weights, or Tr(rho rho'); it could have produced a family that")
print("     EXCLUDES the Born weight (e.g. if the potential had to be quadratic,")
print("     or if the cliques had not been edges).  It does not.")
print("   * The information content is small: the family is a 1-parameter")
print("     interval lam in [0,1] and the Born weight sits at its endpoint.")
print("     That is a 1-in-few statement, not a numerical coincidence.")
print("  R137's phrase 'two lanes that never touched each other meet at the same")
print("  function' OVERSTATES it and is corrected here.")
