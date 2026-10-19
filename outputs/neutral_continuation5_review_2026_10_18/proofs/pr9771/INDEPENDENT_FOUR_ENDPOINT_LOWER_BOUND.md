<!-- Original PR9771 source SHA256 40cd30dd23899f0b8cd7b180431e5b43f8ff3f1ab1a0d8f6ddc69514be37203c. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Four-column uniform lower bound: focused check

Disposition: PASS for the graph/Schur/Lipschitz reduction in the all-even height-multiplicity sector; final rigorous numerical certificate conditional on the stated interval LDL artifact. The supplied /private/tmp/neutral_four_lower_bound.py contains ordinary numpy eigvalsh, not an interval certificate. Its JSON minimum is approximately .46887112585. No canonical files edited.

Equal-height pair moves remove two occurrences of one height and add two of the neighboring height; swap moves preserve the height multiset. Thus parity of the multiplicity of each absolute height is invariant. Four heights with every multiplicity even are either all equal or split 2+2. Modulo common shift, the latter are exactly six choices of the high pair at each separation n>=1. This proves exhaustive coverage of that parity sector, including components disconnected from flat.

At separation n>=2, no low-high pair can move: their heights differ by at least two. Only an edge joining the two low columns or the two high columns contributes. Each changes separation by one, with center displacement +/-1/2. Their summed hopping has the form t(k)=a exp(ik/2)+b exp(-ik/2), with a,b each 0,+1,-1 according to the induced edges and XX/YY signs. Hence |t|<=2 and |t'|<=1. The high-pair label is unchanged, so the six tails are independent. If t=0 a tail consists of isolated sites; the same Schur formula covers it. At separation one the extra swaps remain in the six-state core and have no center phase. Flat-to-core links have the same two-term form. This matches the script's physical-center phase exp[-ik(sa+sb)/4]. Common-shift orbits are free and equally normalized.

Each tail has zero diagonal and spectrum [-2|t|,2|t|] subset [-4,4]. At energy E=-5 the negative tail self-energy is

 s=|t|^2 g_tail(-5)=(-5+sqrt(25-4|t|^2))/2.

The Schur complement of H+5 is therefore M=H_core+5I+diag(0,s1,...,s6), exactly as implemented. The tail block H_tail+5 is uniformly positive. Positivity of M implies positivity of the full H+5 by block congruence, so H>=-5. No truncation of the infinite tails is involved.

Only the flat-core star depends on k in H_core. Its derivative norm equals the Euclidean norm of its six derivative entries and is at most sqrt(6). Further,

 |s'|=2|Re(conjugate(t)t')|/sqrt(25-4|t|^2)<=4/3.

Thus ||M'||<=sqrt(6)+4/3<4, and the proposed conservative constant 8 is safe. This calculation remains valid when t=0. The formulas are smooth in the chosen physical-center gauge throughout [-pi,pi]; possible endpoint gauge equivalence does not affect covering this closed interval.

For 257 equally spaced grid points including both endpoints, every k lies at distance at most pi/256 from one grid point. If interval LDL proves M(k_j)-(1/4)I positive at every grid point for all 15 induced subsets, then

 lambda_min M(k) > 1/4-8pi/256 > .1518.

This is a valid strict uniform certificate. The smaller proven derivative constant gives an even larger margin. The present numpy output is ample numerical evidence for that certificate, but is not itself a directed-rounding or exact-arithmetic certificate; retain the interval input/output or reproducible certifying code before calling the computation rigorous.

Scope: the 15 subsets exhaust four-column induced nearest-neighbor graphs inside the specified nonperiodically-identified 2x3 footprint. This does not certify arbitrary four-column graphs or sectors with odd height multiplicities. For an application to the essential spectrum of an all-even six-column sector, explain why each separated height cluster has even multiplicities independently: at large separation, distinct clusters occupy disjoint absolute-height sets, so global even parity enforces even parity in each cluster. If instead a proposed decomposition groups columns whose height supports overlap, that inference is unavailable. Physical boundary edges or a different transverse torus can change the induced graph and require their own check.

## Completed interval-certificate confirmation

Final disposition: PASS, with the parity and footprint scope above. Subsequently inspected /private/tmp/neutral_four_interval.py and its completed JSON, then independently replayed all 15 x 257 interval checks into /private/tmp/neutral_four_interval_reviewer.json. All passed. The script uses interval pi and exact integer/rational grid construction, interval exponential and square root, and complex LDL* with explicit interval conjugation. It asserts strict positivity of each pivot's lower endpoint before division. The real diagonal and Hermiticity are guaranteed by the previously checked symbolic graph; only the lower triangle is needed by the LDL recurrence. Float conversion occurs solely in displayed pivot summaries after the interval assertions and does not enter certification. The minimum displayed pivot lower bound across all checks is approximately 1.0994751754781376; it is a pivot bound, not an eigenvalue bound.

This supplies the missing certifying computational step. Combined with the analytic Lipschitz estimate it proves H4>=-5 for all common-shift momenta in the stated even-height sector of every induced four-column subset of the 2x3 footprint. Root confirms the intended six-column breakup uses separated height clusters; global even multiplicity then enforces the required parity independently in each cluster. There is no remaining issue in this scoped bound.
