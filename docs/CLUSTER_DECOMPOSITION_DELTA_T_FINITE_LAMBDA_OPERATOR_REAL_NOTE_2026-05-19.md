# Finite-volume spectral gap for a specified SU(3) heat-kernel operator

**Date:** 2026-05-19; source correction 2026-10-21.
**Claim type:** bounded_theorem (conditional operator theorem).
**Status authority:** independent audit lane only; no ledger verdict is changed.
**Runner:** `scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py`.

## Scope and missing physical identification

On a finite link set E, the configuration space X=SU(3)^E is continuous and compact, and H=L²(X,dU) is infinite dimensional. The result below concerns the explicitly supplied integral kernel. It does not derive the canonical lattice gauge/fermion transfer operator. In particular, integrating spacetime fermions generally produces a determinant depending on links across time slices. Such a determinant is not established to be a single-slice multiplication operator merely because it is positive.

The old source's symmetrization already corrected self-adjointness of a multiplication sandwich, but it did not establish physical transfer equivalence. We retain the conditional mathematics and withdraw that identification. The original text and counts are recoverable at f24d17d97d372df977476e4a69674577f31af575. No thermodynamic, continuum, uniform-volume, spatial-clustering or Yang-Mills mass-gap result follows.

## 1. Supplied kernel and hypotheses

Fix tau>0 and normalized Haar measure. Choose the Laplacian normalization with Casimir C2(1,0)=4/3, C2(1,1)=3 (not an unspecified Killing-form normalization). Define

```text
d(p,q)=(p+1)(q+1)(p+q+2)/2,
C2(p,q)=(p²+q²+pq)/3+p+q,
K_tau(g)=sum_(p,q) d(p,q) chi_(p,q)(g) exp[-tau C2(p,q)/6].
T_W(U,V)=a(U,V) product_l K_tau(U_l V_l^dagger).
```

Here a is a supplied smooth, strictly positive, real symmetric function on X×X. The example a=exp(-beta S(U,V)) requires S smooth, real and symmetric. Calling S a Wilson increment is not a derivation of these properties or of an action-to-transfer correspondence. The runner tests a=1, not an interacting Wilson action.

## 2. Heat-kernel facts

Since |chi_R(g)|<=d_R and dimensions grow polynomially whereas C2 grows quadratically, the series converges uniformly absolutely for tau bounded away from zero; differentiated series also converge. It is the kernel of exp(tau Delta/6). Constants are preserved and Haar integral K_tau is one. The heat semigroup preserves nonnegative functions by the parabolic maximum principle on the compact manifold: starting from f>=0, a negative interior minimum contradicts the heat equation after the usual small positive time barrier. Approximate a delta mass by nonnegative smooth densities to obtain K_tau>=0. The strong maximum principle on connected SU(3), together with integral one, gives K_tau(g)>0 for tau>0.

Individual SU(3) characters need not be real or positive. Positivity is a property of the complete heat kernel, not of each character term. The conjugate representations (p,q) and (q,p) make the full series real. A finite torus mesh only checks a finite truncated sample, even though every group element is conjugate to some torus point.

Characters chi_R are orthonormal in the central-function subspace of L²(SU(3)); the complete Peter-Weyl basis is sqrt(d_R) D^R_ab. Thus single-link convolution has eigenvalue exp(-tau C2(R)/6) with multiplicity d_R², and

```text
Tr K_tau = sum_R d_R² exp(-tau C2(R)/6),
||K_tau||_HS² = sum_R d_R² exp(-tau C2(R)/3).
```

Both converge by polynomial growth versus Gaussian decay. The unweighted single-link top eigenvalue is 1, simple; the second is exp(-2 tau/9). These explicit eigenvalues do not apply to an arbitrary nonconstant factor a.

## 3. Compactness, trace class and the top gap

The smooth real symmetric T_W kernel is self-adjoint. It is Hilbert-Schmidt on compact X, hence compact. It is also trace class because a smooth kernel on a compact manifold is smoothing: factoring through sufficiently high Sobolev regularity makes the two factors Hilbert-Schmidt and their product trace class. This is the compact smooth-kernel theorem, not the false implication “positive Hilbert-Schmidt implies trace class.” The diagonal operator diag(1/n) on l² is a counterexample to that implication (sum 1/n² finite, sum 1/n infinite). The trace of this smooth kernel equals its diagonal integral, bounded by ||a||_infinity K_tau(e)^|E|.

By strict positivity of each kernel factor, T_W is positivity improving. Apply the standard Perron-Jentzsch theorem for a compact integral operator with strictly positive kernel: its spectral radius r>0 is a simple eigenvalue with positive eigenfunction, and every other spectral value has modulus <r. Compactness makes the off-top supremum s<r, so delta=r-s>0. These are operator hypotheses, not a new physical axiom.

Pointwise kernel positivity does not mean positive semidefinite as an operator. The real symmetric matrix [[1,2],[2,1]] has positive entries but eigenvalues 3 and -1. Thus -log(s/r)>0 (or infinity if s=0) is a normalized spectral decay rate. Identifying it with a Hamiltonian excitation energy additionally requires a suitable positive transfer operator and reconstruction; no such identification is made here.

## 4. Conditional determinant-weighted construction

If f:X→(0,infinity) is continuous, compactness gives 0<c<=f<=C. Define a constructed operator, using the historical symbol T_full only as notation,

```text
T_full=M_sqrt(f) T_W M_sqrt(f).
```

Bounded multiplication preserves trace class, symmetry gives self-adjointness, and strictly positive factors preserve the positivity-improving kernel. The same simple-top/modulus-gap conclusion follows. This theorem is true for any such f; naming f(U)=det(D[U]+mI) requires proving its positivity, continuity and actual single-slice domain. Anti-Hermiticity alone is insufficient for real-positive determinant; the paired spectrum or equivalent bipartite structure is also needed.

The historical [Leg A salvage source](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) and [parent context](STRONG_CP_THETA_ZERO_NOTE.md) supply proposed physical premises, not a proof here of transfer equivalence. No audit status of either is promoted. A positive determinant from an entire spacetime action does not establish the factorization above.

The runner's two-site one-bond fixture is much narrower: D=[[0,U/2],[-U^dagger/2,0]] with U unitary. Exactly det(mI+D)=(m²+1/4)^3, independent of U. Sampling this fixture tests its algebra, not an interacting fermion theory or a general conditional Leg A claim.

## 5. Reproduction and limitations

Run `python3 scripts/frontier_cluster_decomp_delta_t_su3_operator_real_2026_05_19.py`.

- V1–V3: finite character truncations and torus quadrature; no universal positivity or certified tail bound from mesh agreement.
- V4: enumeration of the supplied exact single-link heat spectrum.
- V5: finite differences against the derivative of the same series, a consistency check.
- V6: two independent heat links, a tensor-product spectrum, not a two-site interacting transfer construction.
- V7–V8: the one-bond determinant fixture (including its exact determinant formula) and its artificial scalar sandwich, with a=1.
- V9: complex fundamental/antifundamental characters, repeated-eigenvalue and center controls.

The character implementation uses Schur polynomials so a repeated torus eigenvalue is not incorrectly replaced by the identity character. Full operator conclusions rest on the explicit analytical hypotheses above, not a PASS count. No physical full-fermion transfer operator, gauge-restricted reconstruction or infinite-volume gap has been supplied. The [temporal clustering bridge](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md) remains downstream context, not evidence for the missing identification.
