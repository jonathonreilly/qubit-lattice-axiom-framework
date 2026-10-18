# Structured exact-loader coefficients: distinct check

Disposition: SUPPORT for the stated sufficient correlated coefficient family, exact event identities, and separately scoped finite-horizon perturbation bound. No required correction found. Neither an arbitrary independent coefficient box preserving exact gates nor a generic native precision guarantee is proved.

## Evidence and exposure

Completely read and hash-verified `exact_loader_structured_coefficients/PROPOSAL.md`, SHA256 `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2`, under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The global premise is `exact_two_body_direct_loader_composition/PROPOSAL.md`, `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946`, and my complete review `41a080068c63261491aeaa04b9c4b397fb31de03f160724be0024b81020e73f6`. ROOT has accepted that review at its stated scope; the target's pending label is historical. The immediately preceding complete diamond7fa888/reviewda5cbc and corrected matchinga1157/review36a1 reads are reused at their exact local scopes. No finite success-time result is imported.

ROOT suggested the structured-family and local-error routes, and the author wrote the global composition. I checked those ancestors and read the new candidate before independently reconstructing the changed algebra and support bounds below. This is same-model source-exposed checking, not blind replication or a formal retained audit.

## 1. Nonuniform local reductions

For a physical diamond, each arm receives a_L+a_R from its two head bonds. Its contacts are gI+gX and gI-gX; the common p_A occupation adds equally. The endpoint occupations are 2a_L+c_L+p_L and 2a_R+c_R+p_R. Thus the physical arm diagonals are d_A I plus/minus gX with d_A=a_L+a_R+g+p_A.

The unchanged B/C rotation sums the two left hoppings into -sqrt(2)a_L at L-B and cancels L-C. At the right it cancels R-B and gives -sqrt(2)a_R at R-C. The contact difference becomes gX between B and C; their diagonals both become d_A. Applying W_pre on L,B and -X W_pre on C,R converts that central link to -g I and leaves the outer scalar links unchanged. This uses X*=X and X^2=I, not commutation of X with the earlier prefix. Therefore different a_L and a_R are allowed; equal coefficients on the two arms at each fixed end and paired contacts remain essential sufficient correlations.

For an identity lane the u contact is 2g n_u and the v contact is absent. The same arm rotation gives the identical scalar d_A and central g, so the identity lane matches the gated lane's scalar operator even with independent endpoint/arm potentials. The comparator is positive because it is a unitary image of the positive physical one-head operator. The source does not assert that arbitrary independently prescribed Jacobi diagonals can be realized by this family.

At a Hadamard mixer, two incident weights t/sqrt(2) give diagonal sqrt(2)t, and the signed cross matrix is -t H. Adding the one physical cable and p yields the two displayed scalar endpoint diagonals. Common t and potentials in both parallel mixers make these scalar on the full four-rail fiber. At the permutation layer, one t bond plus cable and p gives t+c+p and the cross matrix -t X_b. No mu repair is required unless uniform matching is being recovered. Ordinary scalar cable sites similarly have c_-+c_++p. A cable contributes its occupation at both incident module endpoints once, while remaining one installed block.

## 2. Global gauge, extensions and exact record event

After the44 independent arm rotations, every forward link is -w_x V_x with a strictly positive scalar w_x and exactly the old unitary V_x. Define W_(x+1)=V_x W_x. Then W_(x+1)*(-w_x V_x)W_x=-w_x I, while W_x*d_x I W_x=d_x I. The prefix products are ordered and no shared Q/P operators are exchanged. The same W therefore gives the claimed h_str, with all physical heads and data retained.

The complete scalar matrix generally has neither a uniform shift convention nor reflectionless scattering. Its full phase belongs in exp(-it h_str). The old minus in W_out=-U_f remains; it does not imply the old exp(73ik) transmission phase for a nonuniform scalar scatterer. Extracting a common mu only when actually present, and only once, is correct. Uniform boundedness of d_x,w_x is sufficient for the infinite one-head version; finite installations need no uniform-in-volume operator norm assumption.

Identical scalar extensions on all four rails are required for the literal global tensor product. The permitted unequal a=0/a=1 left terminations instead give a direct sum. Since W=I there, those boundary coefficients stay scalar and rail diagonal. The two selected a=1,b chains remain identical, so the supplied input subspace has a common profile. Arbitrary b-dependent source detuning would destroy that common-profile inference. Equal right terminations are also retained. This is the necessary qualification at mixed prefixes, not a general allowance for rail-dependent internal potentials.

The final gauge values are unchanged: W_70=W_71=G_pre and W_72=W_73=-U_f. Earlier prefixes leave initially blank R untouched. In physical final arms, the B contribution has R0 and the C contribution has R1, with opposite arm signs. Projecting on R1 therefore eliminates the unfinished B term exactly and yields the stated -J_rec profile tensored with U_f. New scalar coefficients only change f_71,f_72 and later amplitudes; they do not change the projection identity. Passive references tensor through it. Nonzero event probability is input independent and exact normalization acts on the common apparatus profile alone.

This record event still includes the internal antisymmetric arm coordinate and the final origin. External-only occupancy begins at74, and returns can undo the record. No high-success probability, window or permanent completion claim follows from the gauge.

## 3. Full-support loads and inventory

Each Q bond has full norm twice its weight, each nontrivial contact has norm2g, and each positive occupation has norm its coefficient. Summing them gives exactly the proposed endpoint loads 4a_L+2c_L+p_L and 4a_R+2c_R+p_R, gated arm loads 2a_L+2a_R+2g+p_A, and data load4g per gated diamond. Identity v omits its zero contact; identity u retains norm2g. Mixer and scalar-site load formulas follow by the same block counting, without a one-head expectation shortcut.

Each of the five Q-target layers has two gated diamonds, yielding load(Q)=8 sum g_d; the five P-target layers give the same expression. Four final diamonds give load(R)=16g_final. Consequently the scale box with all relevant positive hopping/contact weights and onsite coefficients at most s gives data loads at most40s,16s and head loads at most7s. For a compensated source of ordinary weight c and gamma<=c, its full combined norm is3c; near-site ordinary bond and onsite give at most2c+3c+s<=6s. Thus s<=Lambda/40 is sufficient with the explicitly stated endpoint inventory. These are sufficient inequalities, not a scalar cancellation of physical load.

The fixed graph has392 head-head blocks,48 nontrivial head-data contacts and20 identity-diamond occupations, total460 before optional potentials. Adding at most one separately listed potential at each of296 heads gives460+N_p. The correlated parameter choices restrict which values of N_p occur, but the ceiling0<=N_p<=296 is correct. Uniform matching has the eight permutation repairs and hence468 blocks. An identity-u contact and an optional potential are intentionally counted separately. This convention matters for the perturbation block-degree bound below.

No support changes, so the range18 placement and299 internal-qubit count remain valid. Equal numbers at different sites are supplied correlations rather than a consequence of their placement. Added exterior heads, potentials and terminations have their own inventory; no fixed finite count is claimed for arbitrary extensions.

## 4. Symmetry-breaking examples and the exact-family boundary

An extra delta n_u gives delta/2 on both B/C diagonals and delta/2 I on their cross link. After the data gauge that cross term carries X rather than becoming scalar. Direct physical path multiplication gives (H^3)_(R,L)=2a_L a_R g X+a_L a_R delta I, as stated. The perturbation can even be positive for delta>0; positivity alone does not preserve the exact gate.

With unequal arm hoppings the two order-two paths give a_(L,u)a_(u,R)-a_(L,v)a_(v,R), which need not vanish. With contacts g_u and g_v, the transformed diagonal contains (g_u-g_v)X/2 and the cross link contains (g_u-g_v)I/2, besides their intended terms. These calculations demonstrate failures of an unqualified exact-robustness statement, not a maximal classification or a no-go for compensating designs. The actual claim remains a sufficient family with explicit coefficient equalities.

## 5. Restricted unstructured perturbations

Consider a finite installation and the source's perturbation domain: E_b self-adjoint on the same listed support, local head-number conserving, and zero on local head vacuum for every data state. Positivity of each changed installed block is a separate assumption. A small norm perturbation does not ensure it because nominal blocks have zero eigenvalues. No data-only error is admitted.

On the global one-head sector, a one-head/data or onsite E_b is zero whenever the head is elsewhere and contributes only its head-diagonal operator block, of norm at most ||E_b||. A two-head E_b has a2-by-2 local one-head block, each entry bounded by ||E_b||, and contributes nothing on a remote head coordinate. Hence every head-coordinate block row of the total error has sum of norms at most2kappa, with kappa=max_i sum_(b containing head i)||E_b||. Self-adjointness gives the same column bound.

For clarity, writing a_i=||psi_i|| and M_ij=||E_ij|| gives |<psi,E psi>|<=sum_ij M_ij a_i a_j. The symmetric nonnegative matrix M has row sum at most2kappa, so its scalar operator norm is at most2kappa. Therefore ||E||<=2kappa. Shared data axes need not commute: their entries were bounded in full operator norm. The proof is volume independent precisely because local vacuum annihilation excludes a data action at every remote head coordinate.

Under the fixed counting convention every head belongs to at most four listed blocks. A diamond arm has two bonds, one contact and at most one potential; an endpoint/Hadamard port has two internal bonds, one cable and at most one potential. Identity/permutation, ordinary and compensated-source cases have no larger count. Thus ||E_b||<=delta implies kappa<=4delta and ||E_one||<=8delta. This ceiling does not authorize arbitrary additional decompositions or multiple newly listed onsite blocks without recounting kappa.

Both evolutions preserve the one-head sector by the perturbation hypotheses. Duhamel on that sector gives the complete induced norm bound8delta*t, and hence8delta*T uniformly on the stated finite horizon, with arbitrary passive references. For normalized purified inputs, the corresponding unhalved channel bound is16delta*T. Fixed output projections contract the vector bound; their unnormalized pure-state operators obey the same factor-two trace bound because each projected vector has norm at most one. Purification supplies the subnormalized CP-map statement. No normalized conditional channel estimate is obtained at this stage.

Full-support load increases follow separately from ||h_b+E_b||<=||h_b||+delta. Heads add at most4delta, Q/P at most20delta and R at most8delta. A nominal margin20delta therefore covers every vertex. The need to supply positive perturbed blocks remains. The norm conversion2|Delta a|,2|Delta g|,|Delta p| is valid for the indicated fixed operator forms; it is not an entrywise-error or changed-axis conversion.

## 6. Rare-event normalization and interpretation

Let b be the ideal event vector with ||b||=sqrt(p), a the actual event vector and ||a-b||<=eta=8delta*t. If eta<sqrt(p), then ||a||>0. Adding and subtracting a/sqrt(p) gives

    ||a/||a||-b/sqrt(p)||
       <= |sqrt(p)-||a|||/sqrt(p)+eta/sqrt(p)
       <=2eta/sqrt(p).

The unhalved pure-state trace bound is at most twice this vector bound, giving4eta/sqrt(p). Also | ||a||^2-||b||^2 |<=eta(||a||+||b||)<=2eta. These are valid statewise bounds; the perturbed probability may depend on input, and normalized postselection need not be a linear channel. At p=0 the ideal conditional state is undefined, and as p decreases the bound loses uniform accuracy. The exact structured-family identity has no such approximation term, but changing to an unstructured perturbation does not retain that exact rare-event guarantee.

Errors that remain inside the correlated family should instead be compared to their new exact scalar h_str. This changes propagation and can change its success probabilities; it is not zero complete-state error relative to the old scalar profile. The source correctly separates these two comparisons. The energy-valued sufficient tolerance delta<=epsilon_abs/(8T) is a finite-horizon bound under the stated support class, not a native fabrication specification or optimal precision requirement.

Only this REVIEW.md was written. Work consisted of analytical reconstruction, complete source reading and deterministic hash/directory bookkeeping. No scientific executable, solver, simulation, sweep, delegation, Git/publication/W/checkpoint/axiom/editable-prompt change or model override occurred. No editable prompt file changed. The verdict is scoped analytical support, not a finite performance theorem or formal retained audit status.
