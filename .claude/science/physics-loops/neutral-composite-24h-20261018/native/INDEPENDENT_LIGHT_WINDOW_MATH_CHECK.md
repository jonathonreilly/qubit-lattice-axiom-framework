# Fixed-box light-window original-source weight: independent check

Disposition: PASS for the fixed finite geometry and real native word-preserving reduction specified in the task, with all asymptotic constants allowed to depend on R,L. This is a positive-window weight statement, not a pole theorem. No canonical/shared edits.

## Hierarchical reductions and source subtraction

The first exact analytic reduction isolates the full N=0 block from the O(Jz) wall gap. In the native gauge, all terms below order L are diagonal in aligned-column configurations. The first nonconstant diagonal term is D4=-Jz L lambda^4 sum P/128; lower diagonal terms are scalar. The first off-diagonal term is K=-gamma_L T, with T=sum_edges Xbar_i Xbar_j, under the previously checked minimal-winding hypothesis. The uniform original source has corresponding nonconstant diagonal aD4 and first off-diagonal bK, with

 a=3/(Jz sqrt(V)), b=A_L/(2Jz sqrt(V)).

Scalar source terms, even if appearing at lower orders, cannot create transitions. Higher diagonal/source coefficients are relatively O(lambda) after the lambda^4 scale is divided out, at this fixed geometry.

Now reduce the P0 ground-plaquette space against its complement in the N=0 block. The gap to the four-bad-plaquette space is Delta4=Jz L lambda^4/16. To leading order, an off-diagonal k=<e|K|g> mixes the ground vector by -k/Delta4 and the excited vector by +conjugate(k)/Delta4. The source diagonal difference is aDelta4. Hence its transition is

 bk-a k=(b-a)k,

not bk. This calculation is equally valid as a degenerate block calculation: the leading D4 energies are scalar separately on P0 and P4. The first source connection from the initial real native reduction was already excluded at order L by the winding gauge argument. The second block rotation is exactly the mixing accounted for here; it must not be omitted or counted twice.

Consequently the leading source operator from the continued ground subspace to the continued four-plaquette subspace is

 -gamma_L (A_L/2-3)/(Jz sqrt(V)) T P0,

up to a relative O(lambda) operator error, provided the coefficient A_L/2-3 is nonzero. Repeated ground/excited mixing contributes relative O(lambda^(L-4)) or smaller; since even L>=6, this is within the claimed conservative O(lambda) error. Higher diagonal energy corrections likewise only perturb the denominators relatively O(lambda).

## Counting and ground degeneracy

Each adjacent column-pair flip produces exactly four bad plaquettes on the transverse torus, so T maps P0 into P4. There are 2R^2 distinct undirected nearest-neighbor transverse edges. The same edge applied twice is the identity. Two distinct edges differ on at most four columns. A nontrivial row/column-pattern change in P0 needs at least R columns, so for R>4 no cross-edge product maps one P0 configuration to another. Therefore

 P0 T^dagger T P0=2R^2 P0.

This is an operator identity on the entire degenerate ground-reference space, not just on a polarized state. Any exact ground vector, including a coherent superposition selected by much higher-order splittings, is carried into P0 by the analytic spectral-subspace identification. The norm of its leading source image is therefore the same, with no dimension factor. No assertion that all P0 states remain exact ground states is needed.

Using V=R^2 L gives the proposed total window weight

 [2gamma_L^2/(Jz^2 L)](A_L/2-3)^2[1+O(lambda)].

It scales as lambda^(2L), with the fixed-L coefficient supplied by the exact winding recurrence. It is dimensionless, as required for a squared matrix element of the normalized diagnostic.

## Nonzero coefficient without the conjectured closed form

For even L>=6 the recurrence average already implies A_L>6. At intermediate subset sizes 1 and L-1, d2/c=2. At sizes 2 and L-2, d2/c>=1 (two sites either adjacent, at distance two, or farther; the minimum is one). All other terms are nonnegative. Thus every path statistic is at least six. Paths whose first two rungs are adjacent have the size-two contribution four rather than one, and have positive weight; hence the weighted mean is strictly greater than six. Therefore A_L/2-3>0. No unproved all-L closed form is needed for the leading weight's nonvanishing.

## Meaning of the actual spectral window

At fixed finite R,L, higher N=0 diagonal coefficients split P4 only by a relative O(lambda) correction to Delta4. Off-diagonal mixing is even smaller relative to that scale. Other plaquette counts have different leading lambda^4 energies; the next allowed nonzero count above four is separated by a fixed fraction of Delta4. The N>0 block remains at O(Jz). Therefore for sufficiently small lambda the window [0.9,1.1]Delta4 above actual Eg contains the entire continued P4 cluster and excludes the other leading sectors. Replacing Evac by actual Eg changes the leading center only by higher-order scalar/common and ground-shift terms already included in this hierarchy.

The measured statement is the full positive spectral weight of the original source in that window from any actual ground vector, and by averaging from any ground density. The cluster may contain many split eigenvalues. The argument is not a uniform theorem when R or L grows with lambda, does not resum the winding series, and gives neither a single isolated pole nor a lifetime or propagation law. In particular it does not contradict the growing-box superalgebraic darkness result, which uses a different limit.
