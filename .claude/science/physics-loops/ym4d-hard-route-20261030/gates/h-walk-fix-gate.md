# Gate of h-walk-fix (queue row 132)
Provenance: OpenAI Codex (GPT-6 family; exact serving variant not exposed); effort xhigh requested, runtime setting not independently exposed; checkout 6a1fad49bafa6f2b67a5324fce02024d08f0152e; Sussman–Alpoge commit 31a47c543775; research-text check, not an audit, granting no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's statements, operator conventions and consumer contracts discussed below; Tadeusz Balaban for the cut-down/walk method as used in the supplied notes. Claude wrote the text under review. The outline was fetched once to `/tmp/sa_ym4.tex`; SA references below are line numbers in that file. No computation discharges a mathematical step. No subagents.

Scope: every section of `library/h-walk-fix.md`, against `library/h-walk.md`, the requested portions of its gate, queue rows 115/120/123/126/129/132, and bounded source excerpts. Inputs (I4-tr), (I4a), (I4b) are assumptions whose uses, not truth, are checked. The checkout lacks the referenced `docs/ai_methodology/SCIENCE_WORKFLOW.md` and repository skill files; no workflow or audit was started.

## 0. Result — WRONG as the full disposition

First failure: the assertion that the consumer list establishes a need for single-walk isometry covariance; covariance of pointed totals does not imply covariance of their summands (§1). Independently, Lemma M's metric displacement argument is false (§4), and the stage-2 consumer needs its full field read set, not just the fourth enlargements of its listed walk cubes (§5). These do not refute Lemma N.

The geometric repair advances: N0, N1, N(a)–(d), N2 and the region/translation arguments W', T', H' have valid conditional proofs, with the conventions and field identifications made explicit below. Midpoint multiplication fixes the scalar reflection defect, and IC's factorwise covariance follows under its stated operator premises. The printed proof of quantitative stability under this change needs the repair in §4. The axial subgroup is a sufficient scope under (I4b), not an established necessity for the soft-gauge A of this note.

## 1. Consumer inventory — WRONG in its IC inference; RT consumers confirmed

First failure: the B2 table row infers single-walk covariance from covariance of an activity/pointed total. For a reflection fixing two summand labels, choose a local F with rF≠F and assign F and −F to those labels. Their zero total is invariant, but the labelled summands are not covariant. More generally, adding F to one summand and subtracting it from another preserves a given total and can destroy termwise covariance. Thus single-term covariance is a sufficient construction strategy, not the condition B2 states.

The bounded source check gives this corrected inventory:

| Cited consumer | What the source actually requires |
|---|---|
| Collared A2 / `h-walk-gate.md` §9 | Fixed-region field carrier, support and estimates. No comparison between region sequences and no single-term reflection claim. |
| `o1-decoupled.md` B, C1/C, (H-field); `wf-room-2.md` WF7 | B uses fixed-region field locality; C1 uses the region identity for specified j=0 terms; C and the proposed H-field extension need matched families and quantitative comparisons in addition. Row 129's defects remain. |
| SA 17548–17556, Package C | Label independence of constructed activities and locally selected chains of the conditional quadratic form, including chains containing C^(j)(Λ). Thus A's RT repair is one input, not the entire consumer. The kept-chain rule and carried forms/factors at 17550–17556 should be listed explicitly. |
| SA 19523 | A carried activity keeps its defining function/domain/length; its later background argument may change (17556). This is not an independent proof that newly recomputed walk terms agree. |
| SA 7837; 5878–5890; 32649–32657 | Nonwrapping cross-torus/cutoff compatibility of local families and a specified infinite companion. The last citation is a glossary, not the companion construction or its proof. |
| SA 26879–26932, ET8–ET10 | Besides equal local values: a **bijection of rooted domains** below a nonwrapping threshold, common auxiliary choices and normalizers, and uniform decay beating domain entropy. ET9–ET10 alone, the cited later range, do not state the required bijection; it is before ET9. |
| SA 10400–10404, 10562–10567, R9 | Transport conditional on covariance of the **assigned operator data**; uniqueness does not supply that covariance. |
| SA 3937–3950, 5893–5915, 7477, 7581 | Covariance of each member's unrestricted pointed totals, including unit translations and the full hypercubic group, on the declared background class. Not covariance of every walk or every localization-domain summand. |

A scoped search of the lane's library and parts finds the direct `h-walk.md` references stated in the note: `o1-decoupled.md`, `wf-room-2.md`, and `sa-2.13-2.md`; the latter two add no separate direct RT proof. This establishes a nonempty consumer set and justifies doing the repair. It is not a claim of exhaustive semantic dependency discovery across the repository. The table is incomplete as a consumer **contract** until the conditional-chain and ET8 requirements above are included.

Mechanism (i), SA 10560, lists a gauge mean and translation/covering/normal-family operations; it does not list a coordinate-isometry average. That observation is correct. The further inference that the only possible route to B2 is single-term IC is not. Repair: describe IC as an available sufficient symmetry input, keep the pointed-total obligation separate, and retain the expressly open C^(k)(Y), companion-formation and R14 obligations.

## 2. Cutoff read sets — ADVANCE

First failing step in N0/N1/N/N2: **none**, with θ defined only where its denominator is positive and extended by zero elsewhere when a function on the whole torus is desired. Read `supp φκ = κ^(1/4)` as containment: the profile assumptions do not force equality. Cand is a common **overlist**; boundary-touching candidates may contribute zero. Neither convention changes the proof.

Write s=M_1 ξ_i. The following redoes each geometric step.

**N0.** Interior disjointness of grid cubes and refinement imply that a level-j cube is either contained in Ω_j or has interior disjoint from it, and similarly for Ω_(j+1). Consequently λ lies in closure(Ω_j\Ω_(j+1)) exactly when λ⊂Ω_j and λ⊄Ω_(j+1). If it were contained in both, an interior point could not be a limit of their difference. These are tests on the entire candidate λ, not on its intersection with a smaller set.

**N1.** For i'≥i+2, int κ⊂Ω_(i+1)^c⊂Ω_(i'−1)^c and κ'⊂Ω_(i'). Separation therefore gives distance >R_1 M_1 ξ_(i'−1) from every interior point of κ to κ'. Taking closure gives the asserted non-strict lower bound. Interchanging the cubes proves the other case. The argument uses the larger cube's scale, so a very coarse cube with a long cutoff cannot evade it.

**N(a),(b).** κ⊂κ^♭ gives common membership by N0. If φλ can contribute at a point of κ^(1/4), then

    dist∞(κ,λ) ≤ (M_1/4)(ξ_i+ξ_j) ≤ (M_1/2)ξ_max.

For |i−j|≥2, N1 instead gives ≥(R_1/L)M_1ξ_max, which is at least 8L²M_1ξ_max. Hence only i−1,i,i+1 occur in either sequence. For the largest candidate,

    |cλ−cκ|∞ ≤ (3/4)(L+1)s,
    sup(x∈λ)|x−cκ|∞ ≤ ((5L+3)/4)s ≤ 2Ls  (L≥1).

The equal/finer cases are smaller. Thus **every whole candidate cube** is in κ^♭, of half-side 2Ls. Agreement there decides its Ω_j and Ω_(j+1) tests even if it is absent from one sequence. Apply N1 anew in the other sequence using the now-common κ. Both sums over this fixed candidate list then agree pointwise on the numerator's support. Outside it both θκ vanish. This proves equality without presuming either sequence's list of present cubes.

**N(c).** κ^(4) has half-side 9s/2<2Ls for L≥3. Trace agreement on the larger open neighbourhood identifies the closed layers and both extremal indices in Lemma C. The grid-rounded boxes are then identical. Every Ω_j^κ is their intersection with a common trace; all artificial faces are identical too. For the listed carriers near κ^(7/2), the old 4L carrier bound costs at most 4L²ξ_i in physical units. The inherited M_C bound makes this smaller than s/2, the remaining margin to κ^(4). This identifies the local combinatorial objects, without identifying any global inverse.

**N(d).** κ^♯ has half-side 4L²s. For i≥1 its extension beyond κ is <4L²s, while Ω_(i−1)^c is farther than (R_1/L)s≥8L²s from κ. At the other end Ω_(i+2) is farther than R_1Ls≥8L⁴s. Thus only levels i−1,i,i+1 can meet it; at i=0 the exterior has bare density 1/ξ_0. Assign interface points consistently to layers, or approximate paths avoiding interfaces. The density relevant to path length is ≤L/ξ_i. A straight segment in the four-dimensional cube has length at most 2·8L²s, giving diameter ≤16L³M_1. Missing end levels simply omit a boundary test. Projection of such paths also proves the bound on a torus; cross-torus use later requires an injective lift.

**Old counterexample, rebuilt.** Use a sufficiently large torus, Ω_0,…,Ω_j equal to the torus, Ω_(j+1) an aligned slab on the x_1≥0 side in S and empty in S', and all later regions empty. The slab's other face is far away. Separation holds because the preceding complement is empty. Take κ with first interval [−7s,−6s] and tangential centre at the centre of a coarse cube λ with first interval [0,Ls]. Its fourth enlargement ends at −2s, so S and S' agree there. At cκ the coarse factor is p(−1/2−6.5/L), with tangential factors one. With the new (2.0), any odd L≥53 makes it ≥1/2. All newly introduced fine cubes in x_1≥0 have support starting at ≥−s/4 and contribute nothing there; the old fine contributors are unchanged. Thus D_S(cκ)>D_S'(cκ), while φκ(cκ)=1, and θκ differs. All fields may be flat and J=0.

The candidate test is −Ls/4≤−5.75s, i.e. L≥23. In particular our λ is in Cand(κ) and wholly in κ^♭. The sequences differ on λ, so the new lemma correctly excludes this counterexample. The note's reference to “the gate's L>26” is not what the gate states and does not ensure positivity for every permitted p. Replace it by “sufficiently large odd L,” or the explicit L≥53 above. This repairs the numerical aside without weakening N.

**N2.** A row location c∈κ^(7/2) has |c−cκ|∞≤4s. If θλ(c)≠0, then |c−cλ|∞≤3M_1ξλ/4. The resulting distance between the unexpanded cubes is ≤5M_1ξ_max; N1's lower bound 8L²M_1ξ_max excludes all but adjacent levels. Consequently

    sup(x∈λ^♭)|x−cκ|∞
      ≤ (4+3L/4+2L²)s ≤ 3L²s < 4L²s.

The middle inequality holds at L=3 (6.25≤9) and its right-minus-left difference increases thereafter. Thus λ^♭⊂κ^♯, including candidates present only in one system. Their actual occurrence and θ values agree by N0/N. Also λ^(4)⊂λ^♭. This last inclusion is essential for stage 2, not just the normalization denominator.

## 3. W', T', H' and the hull — ADVANCE as conditional locality statements

First failing step: **none**, provided a comparison holds the fields/current fixed on the **full field hull**, and transport has the separately declared input (I4-tr). For a general prescribed coefficient j, its field read set must also be supplied. Region agreement alone never asserts equality for different field values.

**Hull and stage-2 coefficient.** For a row c used by the local model at κ, define its zero-length coefficient read set as the union of λ^(4) over the λ with θλ(c)≠0; add the actual finite stencils if necessary. The coefficient is

    j⁰(c) = ξ_c^(−4) Σλ ⟨[h̃λ S^G_λ θλ]_(Aν) e_c, J⟩_f.

N2 puts every λ^♭ inside κ^♯. N0/N identify the same candidates, including absent ones, in both systems; N(c) identifies their cut-down matrices. Their inverse reads P only in λ^(4), and the displayed pairing reads J only on its output support, inside λ^(4). Thus the **same local function of these fields** defines j⁰ in both systems. The common row and ξ_c are fixed by N(c). There are only a bounded, L-dependent number of nearby candidate boxes at a given row, and all the coefficient read sets for c∈κ^(7/2) fit in κ^♯. This proves the claimed ♭-local property in the intended, fixed-field sense. No iterative enlargement or global H is hidden in j⁰.

**W'(c').** In each factor the cut-down sequence and its row set are common by N(c); h̃ is fixed; θ is common by N(b). The rule for j^κ keeps the prescribed j on common rows in κ^(7/2) and assigns zero to the other local rows, so it too corresponds. The finite matrix Kκ, its inverse and the commutator factor are therefore identical functions of the identified data. In replacing [K,h̃κ] by [Kκ,h̃κ], only entries with unequal cutoff values occur; their stencil neighbourhood is in the common interior, away from the artificial face. Thus a product of these factors has precisely the asserted trace dependence. Field analyticity/reality still use the admitted local inverse theorem and its prior gate repairs, not this geometric argument.

**W'(d').** The declared translation preserves all needed grids and takes candidate cubes, rounded boxes, supports and common row indices to their counterparts. The open injectively lifted U contains the entire read sets, so it identifies finite local matrices, not merely small portions of a global matrix. (I4-tr) supplies the equality of their entry formulas, including on distinct tori. Matrix inversion and multiplication preserve this equality. Intersections of neighbouring cells survive the injective map. This proves a transported term for each specified walk. It does not by itself construct an infinite companion, a bijection of all small rooted activity domains, or a rule for wrapping hulls without room.

**T'.** Trunk inverses are W' at j⁰, with the coefficient reads just proved. Each branch is W' at j=0. Pairing its Aν block against J produces jβ with its support on the last branch cutoff and its region reads on that branch's enlarged hull. The vertex Vβ is affine-linear in jβ and has only a finite stencil there; that stencil fits inside the same last cube's sharp enlargement. Products of trunk, vertex and branch factors therefore read the union of their sharp cubes. The terminal pairing for j¹_ω reads J on the root output support and preserves the same locality. Under a translation it also preserves the physical weights ξ_c⁴ and η⁴. This proves the stated blocks and the transposed multiplier as well as the full tree term. The quantitative convergence/tree bounds remain the **repaired** ones in the previous gate, including the branch constants.

**H'.** For the local term, θ reads κ^♭ and C_V, G_V^(2), a read the finite level-k stencil around its output. For the G term, T' handles the νν block and the two C stencils; for the E term, T' handles j¹_ω and the E/C stencils around its supporting rows. The active-row and Y masks are determined locally by Ω_(k+1) and Y, which the comparison must carry. (I3) supplies finite analyticity and (I4-tr) the common translated formulas. Rerooting the E term changes neither these reads nor the union of cells.

For each cube, N(d) joins every point of its sharp enlargement to its own cell at cost ≤16L³M_1; adding the finitely many operator stencils costs C_L. Hence the **radius from the union of cells** is O_L(M_1), as claimed. This is not a bound independent of walk length on the diameter of the whole hull. All zero-length stage-2 field boxes fit inside the sharp hull by N2; the old field-hull notation must include them. Passing from the short-sequence metric to the longer one only lowers lengths. Gauge covariance remains conditional on (I2); midpoint scalar multiplication still commutes with gauge action at a bond's base point.

Premise use: (I4-tr) is used for entrywise translation comparisons, with no inference of isometry covariance. (I4a)/(I4b) later supply translation equivariance on their admitted subgroup on one torus; they alone do **not** imply the whole cross-torus common-formula premise (I4-tr), or its finer translation group for W'. The note is valid here because it separately declares that premise.

## 4. Convention (M), Lemma M and IC — WRONG as printed; repairs visible

**Convention (M) and M(m1): ADVANCE; first failure: none.** Midpoints are unchanged by choosing the opposite orientation. A fine bond midpoint is within η/2 of an endpoint in Ω_0; a row midpoint within ξ_j/2 of its endpoint in L_j; an active level-k coordinate within 1/2 of an endpoint in Ω_k; sites/tops require no displacement. Choose the tiling cube κ' at that endpoint with the indicated scale. Each normalized coordinate of the midpoint has modulus ≤1/2+1/(2M_1)≤5/8 for M_1≥4. The four factors are ≥1/2, so D≥1/16 and the partition sums to one at every required unknown. This also covers outward rows and bonds whose midpoint lies outside Ω_0. The cited SA 13191–13210 makes the same orientation correction for the tensor; it does not prove this separate cutoff lemma.

**M(m2)–(m3): WRONG. First decisive false step:** the proof says a location is at d_B-distance at most 1/2 from its base point, then adds only 1 to the range and the support margins.

Here is a hand counterexample. Let j≥1, all preceding regions be the whole large torus, Ω_j be an aligned slab with face x_1=0 and interior x_1>0, and all later regions empty. Take the outward level-j row stored positively from −ξ_j e_1 to 0. Its base and midpoint are in L_(j−1), whose density is L/ξ_j. Their direct distance is L/2. Any path entering Ω_j must first cross the exterior distance ξ_j and later return ξ_j/2 to the midpoint, costing at least 3L/2 there; a path staying outside costs at least L/2. Thus d_B(base,midpoint)=L/2>1/2. Separation and the flat regular pair hold as in §2. This disproves the asserted displacement, not the viability of midpoint cutoffs.

**Written metric repair.** Every level-j outward row segment stays in Ω_(j−1): separation gives room R_1 M_1 ξ_(j−1)≫ξ_j. Its density is at most 1/ξ_(j−1), so either endpoint-to-midpoint displacement is ≤L/2. The fine-bond displacement is ≤1/2 since the maximal density is 1/η. Sites/tops do not move. An old stencil of range ≤8L consequently has midpoint range ≤8L+L=9L by the triangle inequality. Use, for example,

    r₀,new = 16L,
    M_C,new = 16L(ρ' + 4M' + 16L r₀,new),

and replace every “distance 1” support allowance by an O(L) allowance (L suffices for two location shifts). These are L-dependent choices made before M_1. The physical margin M_1ξκ/2 still contains all needed carriers. The precise printed 8L+1 is not established by the printed reasoning; this larger sufficient range is.

The second-difference assertion also needs an actual quotient estimate rather than an unexplained reuse of the first-difference constant. A sufficient replacement is explicit. On a small fine-stencil collar of a required location, the same endpoint cube gives D≥d=1/16: its distance is at most 3ξκ'/2, and M_1≥12, already implied by M_C,new, keeps it in the 5/8 plateau. Separation bounds contributing scales by an adjacent-level factor there. Let B₁(L), B₂(L) bound respectively the first derivatives times M_1ξκ and the second derivatives times (M_1ξκ)² of both φκ and D on this collar. Such bounds follow by summing the fixed profile derivatives over the bounded-overlap cubes. Since 0≤φκ≤1,

    |∂θκ| ≤ (d⁻¹+d⁻²)B₁/(M_1ξκ),
    |∂²θκ| ≤ [(d⁻¹+d⁻²)B₂
                 +(2d⁻²+2d⁻³)B₁²]/(M_1ξκ)².

These follow by differentiating φκ/D twice; integration gives the finite-difference estimates. For longer averaging stencils the first difference can instead be bounded from the two endpoint quotients and the bounded profile slopes. Take C_p,new to dominate these constants and the q-profile bounds. This supplies an L-dependent constant without claiming that the particular printed C_p' controls its uncomputed second differences.

With these repairs, supports and overlap remain unchanged as geometric point sets. The exact identity K h̃=h̃ K+[K,h̃] holds for the new diagonal multipliers. For a derivative block the mismatch between site and bond-midpoint values is O(η/(M_1ξκ)); after its η⁻¹ coefficient this is O(1/(M_1ξκ)), controlled by the mass-weighted norm. For A_s use the usual first- and second-difference product terms. For D A_s, split into the mismatch for D acting on A_sλ and the term pairing DᵀA against [A_s,h̃]λ; the graph norm controls A_sλ, ξ⁻¹Dλ and ξ⁻²λ. Thus no third derivative is demanded. Averaging blocks cost the oscillation over their O_L(ξκ) carriers, hence O_L(M_1⁻¹). This recovers the commutator estimate; the unchanged local inverse bounds and chaining recover W/T and the H kernel bounds, with L-dependent constants. Carry forward the previous gate's graph-norm/branch repairs and count C₀C₁^m at length m, rather than the false literal H1 count C_h^m at m=0. No new norm theorem is supplied for an unadmitted input.

**Theorem IC: ADVANCE as covariance algebra under (I4a),(I4b), with quantitative claims subject to the preceding repair. First failing step in the factorwise covariance proof: none.** A signed permutation plus an admitted translation preserves the nested cube grids and their membership tests. Even coordinate-product profiles are transported exactly. At a reversed bond, g sends its midpoint to the midpoint of the stored image bond; multiplication by the scalar cutoff commutes with the fibre twist −Ad(U⁻¹). Thus g_U M_f g_U⁻¹=M_(f∘g⁻¹), which is precisely the failed base-point identity now repaired. Symmetric face enlargement and outward grid rounding commute with g, so the cut-downs and the coefficient restriction masks correspond. (I4a), including its stated cut-down scope, then transports the local matrices, their inverses and commutators. Products give W's assertion.

For T, the twists preserve the bilinear trace form, even for complex U: tr((UXU⁻¹)(UYU⁻¹))=tr(XY). Opposite-orientation signs occur twice and cancel in the pairing; ξ_c and the physical weights are unchanged. Applying this to arbitrary colour vectors in e_c proves j_(gβ)=g_U jβ, hence transports j⁰, the affine vertex and the entire tree. It proves the Corollary T multiplier as well. (I4b) is used only for the C/G^(2)/a/E factors in A; masks are carried with Ω_(k+1),Y. Transposes transform because the actions preserve the bilinear pairings. Finally g carries the sharp hull and parameter partition, so P(gω)=gP(ω); replacing s by s∘g⁻¹ proves IC(d).

**Axial scope: CORRECT-NO-ADVANCE for the restricted implication; WRONG for the stated reason it is necessary.** The note expressly leaves possible larger symmetry unsettled, which is appropriate. But its description of C_V and G_V^(2) as necessarily tree-dependent tower-axial objects does not match the cited soft construction. SA 10343 reserves the tree-preserving qualification for **strict** axial gauge. SA 7180–7184 and 8437–8453 use the soft gauge built from means of internal coordinate-order transports; SA 7416 distinguishes these means from a chosen comb. C_V is pivot elimination (SA 8167–8176, 8220–8239), and middle pivots are carried by the admitted isometries (10340–10343). A pivot map is not by itself a choice of axial tree.

Under (I4b) exactly as stated, IC proves only the subgroup claim; that is sufficient and honest. There is no counterexample here showing that A needs the restriction. Repair the rationale to “this is the subgroup supplied by our premise.” If full-group covariance of these soft-gauge building blocks is separately supplied, the same proof of IC(b) immediately works on that full group. This report neither assumes nor discharges that stronger premise.

## 5. Consumer applications — WRONG at the stage-2 comparison inference

First unsupported step: item 3 treats the condition that every listed κ^(4) lies in G as sufficient to transfer the H_1 tree comparison into the (H-field) argument. T' identifies a function on the **enlarged field hull**; (H-pair) controls fields only on G. Those are different sets.

The missing inclusion is visible even at one layer. In one coordinate put cκ=0 and s=M_1ξ_i. Take G with half-width just greater than 4.5s, a neighbouring cube λ centred at 4s, and a row location c near 4s on the inside of κ^(7/2). Then θλ(c)>0. Its local inverse reads λ^(4), extending to 8.5s, and its output cutoff can read J out to 6.5s. Thus κ^(4)⊂G does not put these j⁰ reads in G. This is an explicit failure of the required geometric inclusion; no assertion of a numerically observed nonzero Green-function entry is being used. At J=0 the current derivative of j⁰ is the displayed pairing against the zero-current local inverse; no locality statement proved here kills its exterior part. The cited comparison proof has no bound for varying those exterior arguments.

**Visible consumer repair, conditional on its other inputs:** let F_ω be the actual full field carrier, including all λ^(4) supplying j⁰ to each trunk local model. Call a tree inner only if F_ω⊂G. Require common grids and region agreement on

    G ∪ ⋃{κ^♯ : κ∈K(S)∪K(S'), κ^(4)⊂G},

as in row 129's symmetric repair. Both directions of N identify the inner index families and their coefficient carriers. The Cauchy comparison now uses δ_ω=d_B(F_ω,G^c), on which (H-pair) actually applies. A tree with F_ω not contained in G comes within R_h=16L³M_1+C_L of G^c; assign it to the exterior tail and use this larger R_h in the boundary subtraction. Bound the two exterior tails in their respective native metrics/norms, as required by row 129. This gives a concrete route to the correct comparison; it does not discharge the actual box-map assumptions, sup-norm upgrades, or the R9 contraction inputs.

Item-by-item disposition:

1. **Definition D / Theorem B: ADVANCE conditionally.** Its sharp hull agrees exactly with this one. N(d) supplies its radius and N supplies the region read set. Keep hypothesis (P) on the parameter cubes. The midpoint construction requires the corrected L-dependent margins/constants in §4; it does not change the type of estimate or prove its input bounds. It does change the specified walk coefficients: agreement of the total at s=1 does not identify the old and new decoupled operators at general s. Consumers must adopt convention (M) consistently as part of their assigned data.
2. **C1: ADVANCE as a one-way j=0 identity.** Its field carrier is the union of fourth enlargements, and its trace hypothesis covers each sharp enlargement. W' specializes to it. This does not repair C's converse family identification, mixed exterior norms, or D's anchor bookkeeping; row 129's findings persist.
3. **H-field: WRONG as a completed transfer.** The full-carrier repair above is required. T' does supply the conditional region identity. The expansion/regularity needed for 𝔊 and the quantitative field comparison remain separate obligations.
4. **Collared A2 recommendation: ADVANCE conditionally.** Include every varied parameter cube meeting the sharp hull and full carrier, including zero-length terms and the first sixteen cubes. Any nonconstant monomial then forces t≥w−R_h. The argument in the old gate §9 gives #P≤16+C_Lt/ℓ_P once ℓ_P≥8C_geom R_h, and the bound C exp(16κ̄)exp[−δ_h(w−R_h)/4] follows with its stated reserve/count repair. Taking M_1 after the corrected L-dependent cutoff constants and ℓ_P,w afterwards is noncircular. No new starting gap or inverse-root expansion is obtained.
5. **Package C: ADVANCE for the A-term locality input only.** Enlarging the localization domain to contain the full geometric/field read sets makes corresponding A-terms the same function. Choose the consumer's M-cell collar larger than R_h, which is compatible with the order at SA 10582. C^(k)(Y), the local conditional-chain selection and activity formation still require their own constructions. Merely appending an A hull does not prove them.
6. **Cross-torus use: ADVANCE for each transported walk; CORRECT-NO-ADVANCE on the full companion obligation.** W'/H' work on a common injective lift with the admitted grid offset and all fields identified. ET8 also needs a compatible domain-index bijection, common normalizers and decay/entropy hypotheses. The glossary at 32651 does not discharge them.
7. **R9 transport: ADVANCE for supplied walk data.** W', IC and IC(d) transport those data in their respective scopes, with the parameter partition carried along. Only then can an already proved uniqueness theorem transport the nonlinear solution.
8. **B2 / R14: CORRECT-NO-ADVANCE.** The note correctly leaves full pointed-total covariance open. Replace the claim that two particular obstructions are necessarily intrinsic by the precise limitations: this fixed-grid term construction proves only its admitted grid translations, and the stated (I4b) supplies only its subgroup. No implication from symmetry of a sum to symmetry of every term is available. The soft/strict distinction of §4 prevents treating a strict-tree proviso as a proved obstruction for the soft A.

The order of constants survives the repairs: L, profiles/ranges/local bounds and their ceilings first; then the sufficiently large powers R_1,M_1; then parameter and consumer scales. The new geometric radius and the corrected cutoff constants must be carried into those later choices. The phrase that no bound acquires any new constant should not be read literally: R_h and the midpoint estimates have just been enlarged.

## 6. Final disposition — WRONG as the unqualified closure table

First failure: declaring the full midpoint repair and the consumer transfer completed without the corrections above. The region-locality theorem itself is a valid advance. No original source was edited; the repairs in this report must not be attributed silently to Claude's text.

| Source section | Verdict | First failure, or none |
|---|---|---|
| 0 | WRONG | Unqualified consumer/symmetry disposition; see §§1,4,5. |
| 1 | WRONG | Pointed-total symmetry is promoted to a requirement on every walk; the consumer contracts omit the chain/ET8 qualifications. |
| 2 | ADVANCE | None in N0, N1, N, N2; use the support/zero-extension conventions and the corrected counterexample threshold above. |
| 3 | ADVANCE | None with the full field hull and the separately stated (I4-tr); no downstream comparison is implied for a smaller field agreement set. |
| 4 | WRONG | M(m2)'s d_B displacement ≤1/2; the corrected range/quotient argument repairs the construction. IC's conditional algebra advances. |
| 5 | WRONG | Item 3 applies the tree comparison with only κ^(4)⊂G; j⁰ can read outside G. |
| 6 | WRONG | The closure table inherits the quantitative and consumer omissions. |

Four defect groups, ranked by what they affect:

1. **Stage-2 consumer admission:** full coefficient carriers and symmetric family matching are required; row 129's native exterior norms remain indispensable. Repair specified in §5; actual consumer hypotheses remain open.
2. **Midpoint quantitative proof:** outward rows cost O(L), not 1/2, in d_B. The explicit range and quotient repairs in §4 preserve an L-dependent construction and its M_1-independent rate, conditional on the old inverse/norm inputs.
3. **Consumer symmetry contract and completeness:** B2/R14 concern pointed totals; Package C includes conditional chains and ET8 adds domain bijections/normalizers. The repaired walk input alone closes none of these larger contracts.
4. **Axial attribution:** (I4b)'s subgroup is sufficient as assumed; necessity for the soft-gauge A is not shown, and the outline's strict-axial proviso does not establish it. Retain the restricted conditional conclusion or supply a stronger operator premise separately.

The small support/positivity wording corrections in §2 are not additional obstructions. The successful result is the common candidate list and the stage-2 sharp-hull bound, including cubes absent in either sequence. No region-locality counterexample survives those hypotheses. The independent operator assumptions, C^(k)(Y), the actual removed-map comparison and full pointed-total symmetry remain open at exactly the scopes stated above.

Verification checkpoint: the reviewed `h-walk-fix.md` blob is `2a410416ea7c640c482fd6349ba18ead5a11d534`; `h-walk.md` is `c4477d14685f67c1786b5ed0ff326a4de738caaf`; its gate is `2e770acae07f2283336822f4c713e9b1c9bec8ac`; FINISH is `474634539126d25fffa73cbf21671e50b06d5e57`. All matched the pinned HEAD when checked after the substantive reads. Outline SHA-256: `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The only repository file written by this check is this report. An unrelated untracked `library/dec-field.md` appeared concurrently and was not read or changed. No audit, commit, push, PR, posting, subagent or scientific computation was performed. This checkpoint completes the requested text check and grants no status.
