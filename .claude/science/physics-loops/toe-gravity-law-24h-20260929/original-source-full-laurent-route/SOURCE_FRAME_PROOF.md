# Exact physical source frame on a full six-B star

This is a separate analytical component under SOURCE_FRAME_CONTRACT.md. It uses the actual supplied rotor words, not the winding theorem or a numerical rank. The carrier, Gauss law, compensation, initial preparation and original resolved/coherent instrument remain supplied premises. This theorem is about a formal operator range. It does not replace the actual Omega source state by a maximally mixed input or prove its faithfulness.

## 1. Operators and statement

Use an even cubic torus of side L>=8, oriented locally from A to B, with integer electric fields and div E=q-1_A. Site charges are 0,+1,-1. In global W=0 all A sites are occupied. F_h is the unsigned sum of legal outward hops from h. A hop of charge sigma from h to b changes E_hb by -sigma. The original birth j_(hb,nu) creates charges nu at h and -nu at b and changes E_hb by nu. The coherent edge instrument is the unnormalized sum j_(hb,+)+j_(hb,-); the resolved instrument keeps those labels separate. These are the original observed event labels. The moving q occupations are not those event-history records.

Let P_(h,3) project onto global W=0 and exactly three occupied B neighbors of h. The positive-grade normal-form source is

    B_(h,mu) = -F_h j_mu F_h P_0.                           (1)

Let D_h project onto global W=1, with the hole at h and all six B neighbors occupied. Let D_(h,mix) remove from D_h the two configurations whose six star charges are all + or all -. All projectors include the physical Gauss sector. At fixed global B number k in the output, the input has k-3 B occupations. Define the formal frame

    Q_h = sum_(mu at h) B_(h,mu) P_(h,3) B_(h,mu)^*.         (2)

The exact bounds are

    56 D_(h,mix) <= Q_h^resolved <= 144 D_(h,mix),
    40 D_(h,mix) <= Q_h^coherent <= 288 D_(h,mix).            (3)

The inequalities are positive operator inequalities on the full physical rotor Hilbert space. In particular Q_h vanishes outside D_(h,mix), and the closed row range of the original source operators with all formal P_(h,3) inputs is exactly Ran D_(h,mix). The two different lower constants matter: summing resolved gains and using the original coherent gain are different operations.

## 2. Literal three-word block, with fields and marks

Fix the three initially empty neighbors T={1,2,3}, the initial A charge sigma, the charges on the other three occupied B neighbors, and all initial fields. The source fills T and leaves h empty. For each i in T let e_i denote the actual output word whose unique charge -sigma on T lies at i. The other two new charges equal sigma. Relative to the common input, its electric changes on T are +sigma at i and -sigma at the other two sites. Thus the output field is independent of which source path creates e_i. The three e_i are orthogonal physical charge/field words.

For a marked site l in T, the complete resolved columns of (1) are

    j sign nu=sigma:    -2 e_l,
    j sign nu=-sigma:   -sum_(i != l) e_i.                  (4)

For the first column the first and last outward hops place sigma on the two unmarked empty sites. Their two orders give the same full charge/field word and add. For the second column the first outward hop places sigma on one unmarked site and the last places -sigma on the other. Each possible minority position occurs once. No column with marked site outside T survives: that B site was occupied and remains so after the first outward hop. The overall minus in (1) is retained; no destructive relative phase has been discarded.

Writing J_3 for the all-ones matrix, the sum of resolved column outer products is

    4I+(J_3-I)^2 = 5I+J_3.                                 (5)

With the original coherent edge mark the two columns for a fixed l must first be added. They become -(I+J_3)e_l. Their frame is

    (I+J_3)^2 = I+5J_3.                                    (6)

The eigenvalues of (5) are 8,5,5, and those of (6) are 16,1,1. Neither calculation merges distinct edge labels. In particular equal primitive losses do not imply equal source frames.

## 3. Gluing the blocks in the physical Gauss Hilbert space

Fix all charges outside the six star B sites and all fields outside the six star links. Fix h to be empty. At each B neighbor let s_b be the divergence contribution from its exterior links, in the convention div_B E=-E_hb+s_b. Gauss fixes

    E_hb=s_b-q_b.                                          (7)

Gauss at h then fixes sum_b q_b=sum_b s_b+1. Thus it fixes the number m of minus signs among its six occupied neighbors. For each m the physical star block has the basis of m-subsets of the six neighbors; (7) uniquely assigns its six electric fields. There is no unpriced circulation variable within this tree. Exterior fields can be arbitrarily large, but do not change the following matrices.

For any nonmonochromatic triple T in an output, remove its three charges and restore at h the majority sign sigma on T. The common input fields on T are E_hb=s_b, so all three outputs in section 2 arise from exactly the same physical input. At h their output charge sum on T is sigma, which verifies the input Gauss equation sum E=q_h-1 as well. Exterior charges, fields and every original global sector are preserved. Distinct missing triples give orthogonal input occupation words; distinct remaining input data are also orthogonal. Therefore the block frames (5)-(6) add without hypothetical cross terms between different input words.

For a fixed output with m minus signs, the number of nonmonochromatic triples is

    m binom(6-m,2)+(6-m) binom(m,2)=2m(6-m).                (8)

It is zero for m=0,6 and positive for all other m. Summing just the lower and upper bounds from (5)-(6) already yields valid uniform constants 50,144 for the resolved frame and 10,288 for the coherent frame. The sharper exact lower constants in (3) follow below.

## 4. Exact full-star matrices and elementary spectra

Let A_(6,m) be the adjacency matrix of m-subsets of a six-element set, adjacent when one minus position is exchanged with one plus position. It represents the actual physical exchanges including their field change in (7), not a substitute charge-only dynamics. For a chosen exchanged pair x,y, the third member of T can be any of the remaining four sites. If its sign is plus the majority is plus; if minus the majority is minus. Each such triple contributes the same off-diagonal coefficient, respectively 1 or 5 in (5) or (6), with the same full-field output. Both frames have diagonal contribution 6 per containing triple. Consequently, exactly,

    Q_h^resolved |_m = 12m(6-m) I + 4 A_(6,m),
    Q_h^coherent |_m = 12m(6-m) I +20 A_(6,m).              (9)

All coefficients were obtained from actual original source words. No independent edge phases have been introduced.

Here is a direct spectrum calculation, requiring no spin representation assumption. For m=1, A_(6,1)=J_6-I, with eigenvalues 5,-1 of multiplicities 1,5. For m=2 let R have rows indexed by pairs and columns by singletons, R_(p,x)=1_(x in p). Then

    RR*=2I+A_(6,2),       R*R=4I+J_6.

The positive eigenvalues of RR* equal those of R*R. Hence A_(6,2) has eigenvalues 8,2,-2 of multiplicities 1,5,9. For m=3 let T have rows indexed by triples and columns by pairs with the analogous containment entries. Then

    TT*=3I+A_(6,3),       T*T=4I+A_(6,2).

The latter is positive definite, giving eigenvalues 9,3,-1,-3 for A_(6,3), of multiplicities 1,5,9,5. Complementation gives m=4,5 from m=2,1. Substitution into (9) gives:

|m|resolved frame eigenvalues|coherent frame eigenvalues|
|---|---|---|
|1 or 5|80,56|160,40|
|2 or 4|128,104,88|256,136,56|
|3|144,120,104,96|288,168,88,48|

This proves (3) on every exterior-data block and therefore on their orthogonal sum. Global constraints may omit some blocks; restriction cannot weaken these bounds. Large fields and physical cycle phases do not alter the proof. Fourier decomposition in the actual Gauss cycle coordinates carries these same operator inequalities to almost every phase fiber by decomposability; it is not an independent-phase genericity argument.

## 5. Local right inverse and its limited meaning

Let Bbold_h be the row operator from the orthogonal direct sum of the original input-label spaces P_(h,3)H_0, with Bbold_h(xi_mu)=sum_mu B_(h,mu)xi_mu. Equation (2) is Q_h=Bbold_h Bbold_h*. On D_(h,mix), Q_h has bounded inverse. Therefore

    R_h=Bbold_h* Q_h^(-1) D_(h,mix),
    Bbold_h R_h=D_(h,mix),
    ||R_h|| <= 1/sqrt(c),                                  (10)

where c=56 or 40 for the resolved or coherent instrument respectively. This is a direct-sum operator right inverse. It does not authorize combining distinct observed labels into one physical instrument, nor does it prepare a particular input from Omega.

The inverse in (10) is local to the star: its finite charge-block matrix is (9)^(-1), and (7) provides the corresponding field changes. For each output word and any input word in its right-inverse support, three B charges are removed, costing one unit of field displacement each; the remaining three B charges can at most reverse sign, costing two each. Hence total field l1 displacement is at most nine and each link changes by at most two. This is a support statement, not a claim of a finite-spin inverse: rotor shifts have unit amplitude and the spin-boundary zeros would require a new argument. The inverse entries can be expressed as finite local charge-controlled translations; no unbounded electric inverse or domain restriction occurs here.

## 6. Exact consumer for the actual source, and unresolved steps

Let C_(k-3) denote the closed span in W=0, NB=k-3 of COMPLETE actual original history vectors from Omega, with the required (k-3)/2 ordinary births and all actual no-event waiting evolution. Include the original coherent or resolved marks consistently. This is not assumed to equal the full physical sector. For a vector psi in ker G, its hole-h component has the full six-B star. Thus

    (B_(h,mu))* psi = P_(h,3) (B_(h,mu))* D_h psi.           (11)

Indeed the source creates exactly three B occupations, all on this star, and its only A hole is h. A full-star output forces the corresponding input to have exactly three star occupations. This also verifies that possible other hole locations in psi do not contribute to this adjoint.

Suppose psi is orthogonal to B_(h,mu)C_(k-3) for every original mu. This only implies that the vectors in (11) lie in the annihilator of P_(h,3)C_(k-3). A sufficient additional hypothesis is

    closure(P_(h,3) C_(k-3)) = Ran P_(h,3),                 (12)

in the declared physical sector, for each h. Under (12), every vector (11) vanishes. Then (3) yields

    ||D_(h,mix) psi||^2 <= c^(-1)
                          sum_mu ||(B_(h,mu))*psi||^2 = 0. (13)

The weaker exact hypothesis only needs the annihilator of the projected actual history span to intersect the relevant source-adjoint range trivially; full (12) is stronger than necessary. If this reasoning is applied to a fast invariant dark submodule, it reduces a source-invisible submodule to aligned full stars, conditionally on that actual input-span hypothesis.

Neither (12) nor the absence of an invariant module confined to the aligned-star subspace is proved here. Infinite global winding span does not imply (12), including after phase decomposition. Formal source range, positive diagonal source weight and bounded right inverses do not remove this distinction. No actual late-survival bound, spin-transfer estimate, continuously forced residence bound or physical microscopic energy conclusion follows from (3) alone.
