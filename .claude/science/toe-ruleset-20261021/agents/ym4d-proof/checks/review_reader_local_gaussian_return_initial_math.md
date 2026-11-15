# Source-first independent mathematical findings

This record was written before opening the author's checks, read manifest,
receipt, freezer, or any prior review verdict. It is a mathematical freeze,
not the final packet disposition. The target author did not participate in
this review. This is fresh-context, same-family review. Astra/max was
requested; that request is not independent backend attestation.

## Frozen scope and direct reads

- Target: `READER_LOCAL_GAUSSIAN_RETURN_ASTRA.md`, all 608 lines,
  SHA256 `4f94b5e2102391441233621d99be3e4b14dc46b9be89ea35915b354a4d0a06d6`.
- Actual covariance producer: `POSITIVE_READER_COVARIANCE_ASTRA.md`, all
  543 lines, SHA256
  `68bb7798bfcc0806c65531ab894e3e7f67ef1c155afd6da2f20f1b9dc2bb8da8`.
- Boundary/forest producer: `CHART_BOUNDARY_FOREST_ASTRA.md`, all 564 lines,
  SHA256 `c74260a3984330c9393f66c9e7b43068ae4d411d35f593d3241378a96fe3abd8`.
- `PROCESS_LIGHT.md`, full file, SHA256
  `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab`.
- Methodology authority: observed-main commit
  `01589af3faf806b736c42dc2f3bd625e9edead9f`, read using `git show`.
- HEAD observed after the scientific reads:
  `d55e65eb929ecf5370e025227e7eac07621c9c10`. The scientific hashes above
  still matched. No conclusion is inferred from the unrelated HEAD change.

The direct read order was target lines 1--310, target lines 306--608, PC
lines 1--300, PC lines 300--543, BF lines 1--300, BF lines 298--564.
The overlap at the bounded read boundaries is intentional. No producer
review verdict was read. No source, proof, runner, or checks from the joint
critical-field or nonlinear extension was consumed. The broader CB/PS/IC
upstream proofs were not recursively reviewed; the actual K, its local
analytic domain and real spectral bounds are the explicit PC producer
inputs. The present check reconstructs PC6--PC22 as used here and every new
RG estimate, rather than inferring correctness from PC's review status.

## Exact proposition tested

For fixed N>=2, odd L>=3, positive fixed kappa interval, PC's admitted real
centers and common complex coarse tube, choose one sufficiently large fixed
R, then a sufficiently large u_0. For all u>=u_0 and T>=2, the exactly
normalized, centered Gaussian cutoff with covariance K(V)^-1 on all
D(3L^4+1)T^4 original scalar coordinates has the RG29 connected
complete-original-reader logarithm at rate 1/[3(16R)^4], with the displayed
marked norm and complex nonvanishing. The cutoff is a product of single-link
HS balls. No interacting, shifted-mean, original-cut, history, effective-level
or continuum statement is part of this proposition.

## Independent analytical reconstruction

1. **Actual covariance and the residual algebra (RG1--RG4).** PC2/BF2
   retain kappa(1-c_N)B_V and N^2/(6u)I in K; all free links and colours
   remain. A block contains 4L^4 edges minus L^4-1 pinned tree variables,
   giving 3L^4+1 free links. The T=2 convention in PC/BF excludes the far
   seam only in the lifted coercivity brick, not from the field space.
   PC12 has the correct ordered identity KP=I-Rcal, hence
   C=P(I-Rcal)^-1. For a mark, the product inequality follows by charging
   it to one factor and summing the other via its row or column envelope.
   Therefore sum_{n>=1}p r^n=p r/(1-r), while the marked sum is
   n_R p sum_{n>=1}(n+1)r^n, exactly the two terms in RG3. Symmetrizing
   each matrix product does not enlarge either maximum row/column or
   marked-entry bound. Repeated labelled products are not cancelled.

2. **Entrywise suprema and the R-independent inverse (RG4--RG7).** For
   fixed i,j, sum_A chi_A(i)chi_A(j)<=1. Apply PC6 before this sum:
   sup|P_ij|<=(2/gamma)e^{-m d(i,j)}. Thus the scalar envelope, not merely
   each numerical matrix, has row/column norm <=g. At a real center,
   P>=B^-1 I=2c0 I; PC21--PC22 cost less than c0/8, leaving the claimed
   weaker c0. The Gram compression is an isometry on the full colour
   space, so every link principal matrix and forest mask retains this
   accretivity and operator bound. For a fixed column j, the weighted
   conjugation changes a row/column by at most
   (2n0/gamma) sum_z e^{-m|z|}(e^{theta|z|}-1)<=theta A_1<=c0/2.
   With q_m=e^{-m/2}, the geometric sum in A_1 is
   8q_m(1-q_m)^-2[(1+q_m)/(1-q_m)]^3, as stated. Torus representatives
   embed in Z^4, including even-T distance ties. Undoing the conjugation
   gives (2/c0)e^{-theta d(i,j)}, and summation gives v_0. These constants
   contain no R, no |X|, no connectivity assumption on X, and no loss from
   a mask. Finally Re(P[X,s]^-1)>=c0/g^2 follows from
   Re P>=c0 and ||P||<=g. The upper inverse bound is 1/c0.

3. **The choice of R and all collar costs (RG8--RG10).** Since r<=1/4,
   eps<=2pr. The three relevant RG8 restrictions imply eps<=c0/16,
   v_0 eps<=1/2, and v_0^2 eps/(1-v_0 eps)<=a/16. Increasing R changes
   beta to (16R)^-4; no fixed-rate smallness is claimed. PC's final coarse
   tube contains no R in its radius restriction. Every S_A used in H_e
   contains the owner of e, so H_e is connected, has at most J s_R cells,
   and lies within sup distance 8R of that owner. The safe J_H incidence
   dominates the possible owners. For T<16R the single whole-torus patch
   gives E=0 exactly and |Lambda|<s_R; J_H still dominates all links.
   T=16R uses the large-torus cover without a new estimate. A nonzero
   P_ef requires a common patch, so disjoint collars force its vanishing.

4. **Normalization, determinants and arbitrary residual repetitions
   (RG11--RG14).** Gaussian marginalization selects C[X], not K[X]^-1.
   Continuation from positive symmetric covariances is legitimate on the
   convex accretive domain with local Gaussian domination. The branch
   uses Tr Log throughout. The empty marginal is exactly one, so it has
   no determinant loop or vacuum species. For nonempty X, write G=P[X,s]^-1.
   Independently, the ratio follows from
   -1/2 Tr log(I+GE) and 1/2 y^T[G-(P+E)^-1]y; expanding the resolvent
   gives the two signs and the 1/(2k), 1/2 coefficients of RG12.
   Introduce nonnegative entry envelopes Gbar and Ebar, with row/column
   bounds v_0 and eps. A length-k trace is <=d_X(v_0 eps)^k; a length-k
   quadratic chain has row/column norm <=v_0^{k+1}eps^k. Summing the
   former with 1/(2k) gives d_X ell_0; summing the latter with 1/2 gives
   t_0||y||^2/2. This checks the absolute coefficient sum and all repeated
   indices/labels; it is stronger than a bound on the unexpanded ratio.
   The singular values of P are >=c0, so the normalizer is bounded by
   (b/(2pi))^{d_X/2}. Young's inequality gives the stated c_g (with slack).
   Adding the chain majorant changes -a||x||^2/4 to at most
   -3a||x||^2/16. No inactive-mode determinant remains.

5. **A marked residual and all weak derivatives (RG15--RG20).** Tilting
   the positive residual envelope by one reader mark and differentiating
   the trace resolvent gives v_0/[2(1-tau)] times its total marked entry
   mass. Differentiating the quadratic resolvent puts the marked matrix
   between two geometric resolvents, giving v_0^2/[2(1-tau)^2] times that
   mass and ||y||^2. Restriction to X makes the marked mass <=D_v(X),
   and sum_i d_v(i)<=B_E. This includes i=j atoms reading a remote v.
   The x-polynomial is absorbed with x^2 e^{-a x^2/16}<=16/a; the
   z-polynomial with z^2 e^{-z^2}<=1. This produces precisely K_m and
   c_* in RG17, with remaining x decay a/8. For a scalar order k,
   Cauchy's radius sqrt(k/(2c_*)) gives
   k!(2ec_*/k)^{k/2}<=(2ec_*)^{k/2}sqrt(k!). Cauchy integrals and
   the positive majorant justify summing individual coefficient suprema;
   no interchange of sup and sum is assumed. Since partial_j eta=n_j dS,
   moving the remaining r-|B| derivatives onto the test function yields
   the exact sign (-1)^{r-|B|}. This retains every product of spheres
   and every higher surface distribution. Reserve e^{-a R_c^2/16} on
   each link; the remaining exterior integral is <=(16pi/a)^{D/2} and
   the sphere has exact area omega_D R_c^{D-1}. Scalar factorials are
   bounded by (k_e-1)! at each touched link. Thus RG20 covers all orders,
   including zero, with the active determinant and colour dimensions.

6. **Endpoint forest, heat equation and reader support (RG21--RG23).**
   In an independent off-diagonal link-pair variable, the two symmetric
   covariance entries cancel the 1/2 in the heat equation. The entries
   C_{e alpha,f eta} do not depend on that variable. Thus successive
   distinct pair derivatives give exactly the product of entries and
   the weak field derivatives, including the determinant derivative.
   The maximum-spanning-forest clock proof works monomial by monomial:
   absent edges contribute zero derivatives, and the surviving forests
   span each component of the monomial's edge graph. C^k polynomial
   approximation extends the identity; a smooth extension off the
   accretive forest locus cannot change any used jet. Factorization is
   over endpoint components at this stage. This does not use PC29 or
   differentiate a path minimum; it therefore omits none of PC29's
   higher monomial derivatives. Every inverse and determinant reads H_X
   once. Tree P edges join overlapping collars; tree residual edges join
   their endpoints by a connected complete reader. Additional density
   readers attach at an endpoint in X. Hence the entire support in RG23
   is connected, including remote diagonal readers.

7. **The entire marked species norm (RG24--RG26).** Summing colour
   indices on an endpoint edge gives c_row<=D(g+eps); B_E already sums
   both scalar colours. A tree has 2n-2 field legs. Prüfer occurrence
   counts k_e=deg(e)-1 give the exact factorial sum
   (n-2)! binomial(2n-3,n-1). With one fixed link, the other positions
   cost c_row^{n-1} and their ordering contributes (n-1)!; this is
   bounded by the geometric series with lambda=4L_*^2 c_row Q.
   For a collar mark there are at most J_H roots. For a density mark,
   summing the pinned scalar mass gives B_E. For a distinguished residual
   tree edge, removing it gives two rooted components and positional
   cost B_E c_row^{n-2}; (n-1) choices of the marked edge and division
   by n! leave binomial(2n-3,n-1)/n. The displayed 4B_E L_*^2 Q^2
   numerator safely dominates the resulting sum. For n=1 the empty
   tree is included; for n=2 the single-edge and 1/2 ordering factors
   are correctly bounded. These three mark locations cover the union
   support. Fixed B_E may be enormous, but q is a fixed polynomial in
   R_c times e^{-a R_c^2/16}. Therefore RG26 holds at some finite u_0
   for fixed R, uniformly in volume and admitted coarse data.

8. **Exact regrouping, both margins and the analytic logarithm
   (RG27--RG29).** The initial gas really has field-set exclusion. A
   compatible family has a unique decomposition into connected
   components of its reader-overlap graph. Grouping those components
   gives exactly the b_Gamma gas with reader-set exclusion; merely
   replacing the original exclusion would have been false. All raw
   species have nonempty X, so fixed-volume families have bounded size;
   their countably many decorations are absolutely summable by RG25.
   Rooted overlap trees majorize connected families, even with repeated
   tree labels allowed. At beta_1=2beta/3, p_z exp[(beta/3)|S_z|] is
   a supersolution because its neighbor sum is <=|S_z|epsilon_G.
   This spends the first beta/3 and proves RG28. For the hard-core log,
   the breadth-first interval partition of connected subgraphs gives
   the tree bound: equal-level edges and the permitted previous-level
   edges leave the least parent and levels fixed, and every interval's
   alternating sum is zero or has modulus one. A second rooted-tree
   majorant spends another beta/3, giving output rate mu=beta/3.
   Rooting at a species containing the marked box overcounts every
   anchored cluster, so it introduces no missing volume or cluster-size
   factor. The resulting locally uniformly absolute series is analytic.
   Finite-species identities hold near zero activity multiplier and
   extend through |t|<1; dominated convergence reaches t=1 and the
   countable-species limit. Its exponential equals J_0, which is thus
   nonzero on the stated complex domain. The series fixes the branch
   and its local norm tends to zero as u tends to infinity.

## Scope disposition before author-packet inspection

No consequential mathematical defect or counterexample was found in this
bounded proposition. The exact consumer proof is closed under the explicit
PC producer inputs. No source repair is requested at this stage. The larger
interacting return is not proved: its actual force, source Hessian, nonlinear
remainder, determinant and vacuum in RG30 cannot be replaced by J_0. The
original cut, G/Omega, chart complement, histories, source insertions,
effective-level iteration and multiscale limits remain separate obligations.
Both physical targets remain OPEN. This is a positive bounded mathematical
construction; no no-go or route-exhaustion conclusion is made.

No numerical experiment, numerical runner, audit/ledger operation, lock
change, Git mutation, PR action or target-source edit was performed. Analytic
edge-case checks above are written proofs. The author's package remains
unopened at this freeze. The provisional source disposition is LAND for
this exact Gaussian statement, subject to inspection of the frozen package
and final identity recheck; it is not an integration or audit verdict.
