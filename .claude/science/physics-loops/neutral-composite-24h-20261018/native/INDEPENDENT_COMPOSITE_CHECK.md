# Native compass local-energy-square check

Reviewed the current `native/compass_scalar.py` and JSON. This is the separately supplied compass candidate H=K sum_(x,a) sigma_x^a sigma_(x+e_a)^a, not a derived interacting completion of the previous quadratic corner model. No extra interaction is introduced by choosing a composite observable.

## Exact local identity

Write B_a=sigma_(x−e_a)^a+sigma_(x+e_a)^a and T_a=(K/2)sigma_x^a B_a, so e_x=sum_a T_a. Assume neighbors are not the central site and neighbor supports for distinct axes are disjoint. Then B_a commutes with the central Pauli matrices and with B_b for a!=b. The central Pauli anticommutator gives

    {T_a,T_b}=0 for a!=b.

For each axis, including coincident left/right neighbors,

    T_a²=(K²/4) B_a²
         =(K²/2)[I+sigma_(x−e_a)^a sigma_(x+e_a)^a].

Consequently

    e_x²=(3K²/2)I+(K²/2)sum_a sigma_(x−e_a)^a sigma_(x+e_a)^a,
    sum_x e_x²=(3NK²/2)I+(K²/2)C.

The local definition sums to H with the stated periodic oriented-bond convention. A length-two periodic axis has left=right and contributes K² I to e_x²; the identity still holds because the neighbor pair is I. Length-one axes, or graph identifications making different-axis neighbors coincide, do not meet the derivation's support assumptions and require recomputation. K=0 trivially satisfies the identity, but solving it for C by division assumes K!=0.

## Symmetry and physical identification

Under the declared physical transformation of Pauli components as an axial vector together with cubic spatial rotations, the equal-axis sum C is a cubic scalar: signed axis permutations transform both spins, whose signs cancel, and permute the bonds. The same holds under cubic improper transformations with the axial-vector determinant factor. Under the usual spin time reversal sigma->−sigma, each pair and hence C is T-even.

Those transformation rules are assumptions about how the qubit is identified physically. A generic encoded pseudospin need not carry that microscopic axial-vector/time-reversal representation. A cubic scalar is not automatically a Lorentz scalar, an electromagnetic-neutral observable, or a universally conformally coupled field. No electromagnetic charge or corresponding symmetry has been supplied here.

The (3,2,2) and (4,2,2) finite tori do not possess full cubic axis-permutation symmetry. C is the restriction of the infinite-cubic scalar formula, but those cluster spectra alone cannot establish a cubic scalar irrep in a three-dimensionally symmetric thermodynamic limit.

## Conserved energy versus the composite

Total H at q=0 commutes with H, so its retarded dynamical commutator spectrum has no finite-frequency weight. It can have thermal elastic variance; in a fixed-energy ground eigenspace its connected inelastic response vanishes. The composite sum_x e_x² is not H², and its C term is not generally conserved.

For generic sufficiently large lattice sizes, a C bond of length2 along axis a and an H bond of length1 along distinct axis b overlapping at one endpoint have a nonzero commutator proportional to a three-site Pauli string. For a nonwrapping triple {0,2e_a,e_b}, this string is not canceled by another geometrically identical pair, so [H,C]!=0. This permits finite-frequency weight in some states; it does not guarantee weight in a selected ground state or an isolated mode.

## Finite-size cautions and checks

On the 2x2x2 torus every neighbor pair in C has equal endpoints, hence exactly

    C=3N I=24 I.

Its zero inelastic weight is a geometric identity, not evidence against the generic composite route. An independent direct Kronecker-Pauli calculation verifies all eight local-square identities exactly (zero entrywise residual), C=24I, ground energy −13.856406460551025 and a unique ground vector. Its ground-projected C inelastic norm is approximately 7.4e−15. Files: `/private/tmp/native-compass-check/check.py` and `result.json`.

On a length-three periodic x direction, the next-neighbor pair in C becomes a nearest-neighbor x bond after periodic relabeling. With the other two directions of length2,

    C=H_x/K+2N I  (K!=0),

where H_x is the x-axis part of H. Thus the (3,2,2) result is also subject to a strong short-direction aliasing effect. The (4,2,2) direction has diametrical x pairs counted twice. Neither is a generic cubic finite-size sample.

The script correctly removes the full **computed** ground-ground elastic block and evaluates first/second inelastic moments through full H matrix-vector action, not through only the24 computed excited Ritz values. Its stated caveat is necessary: small Ritz residuals alone do not certify that the sparse solver found the entire ground eigenspace. The reported weights are total-C weights averaged over ground vectors, not divided by number of sites; use a declared per-site normalization before comparing volume scaling.

Conclusion: the energy-square composite is algebraically derived within the supplied native compass Hamiltonian and is a legitimate alternate observable route. Current controls do not establish a thermodynamic pole, electromagnetic neutrality, universal coupling or the environmental/cosmological bridge.
