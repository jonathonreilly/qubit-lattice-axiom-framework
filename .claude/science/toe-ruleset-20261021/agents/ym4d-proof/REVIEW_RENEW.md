**Independent hostile review of RENEW.md — 30 October 2026**

**LAND as partial research. The requested matched renewal theorem remains
OPEN.** The explicit flux family, finite-horizon persistence estimate,
localized linear dilution and conditional integration/window bounds survive
re-derivation. They do not establish LF-JMBR clauses 2–5 on the actual
all-cut reference. The note states that limitation rather than hiding a
renewal estimate among its assumptions. No binding correction remains.

Reviewed source: RENEW.md, 623 lines, SHA-256
`42b4d2a16625d4af4f6443a38ff92d63a483485816c4533292b44f867fc978a7`.
All candidate line numbers below refer to this revision. “None” in the fix
column means no correction at the stated scope, not that an actual-model
antecedent has been proved.

This is the user-assigned fresh-context review, separate from authorship,
and **same-family Codex review**, not cross-family validation. I reconstructed
the candidate's mathematics before reading the prior RENEW review and its
findings. I subsequently checked both predecessor reviews and the prior
RENEW correction record. Their verdicts supply no proof step here. No
additional reviewer, numerical physics experiment or formal audit was run.

| Item and RENEW lines | Verdict | Fix or condition for stronger use |
|---|---|---|
| Supplied model, reference and full norm, 31–75 | CONFIRMED | None. Keep the inherited density distinct from the bare comparison, with all normalizers, predicates and original readers. |
| R-LIN: curvature map, action bound and sharpness, 79–117 | CONFIRMED | None. This is the noncompact abelian linearization; the sharp constant one is a supremum over volumes. |
| Localized iteration R7, 119–145 | CONFIRMED | None. Return depends on the inherited curvature l1 size and the actual cut; nonlinear dynamics and noise are not covered. |
| R-FLUX, 149–205 | CONFIRMED for every N>=2 and odd L>=3 on the specified even tori | None. The positive polar factor is computed for actual arithmetic means; no general SU(N) polar-projection formula is imported. |
| R-TUBE and fresh-gap exclusion, 207–268 | CONFIRMED at fixed finite horizon and lattice | None. The conclusion excludes coupling-uniform return on all real inputs, not fixed-coupling return or weighted renewal. |
| Measure, original charge and local embedding, 270–300 | CONFIRMED | None. Positive tube mass is not a normalized matched-reference estimate or a bounded-size singleton witness. |
| R-CAP and adapted gap prices, 304–336 | CONFIRMED | None. The cap bound deteriorates with coupling, volume and cut; full chart/completion return requires more. |
| R19 replacement identity, 340–364 | CONFIRMED finite algebra | None. The inherited insertion stays inside the joint replacement integral. |
| Complete-reader elimination, 365–396 | CONFIRMED under the explicit normalized-law hypotheses | None. Noncreator factors must remain selected or be fully expanded; the interacting all-cut law is not asserted to factor. |
| R-WINDOW and R20–R22, 398–452 | CONFIRMED conditional theorem | Construct and bound the actual matched operators before applying it to LF-JMBR. No such estimate is supplied here. |
| R-GROUP and R23, 454–490 | CONFIRMED conditional theorem | Instantiate complete factorization, mixed absolute-integral bounds and analytic hypotheses on D_*. Separate event probabilities do not suffice. |
| Weighted readers R24, 492–512 | CONFIRMED conditional theorem | None. Roots on reader tails are included. Actual reader/core budgets remain unproved. |
| Clause table, RENEW-MATCH and nonlinear recurrence, 514–559 | CONFIRMED OPEN/ARGUED classification | Prove the stated matched window, mixed-support and invariant-domain estimates, including initial membership and relevant/marginal recursions. |
| Negative scope and evidence claims, 561–623 | CONFIRMED as partial narrowing | None. No complete negative packet, retained status, continuum result or numerical PASS is established or claimed. |

The following calculations record the load-bearing checks.

1. **Linear averaging and localization.** The two axial legs contribute
   `h(X)-h(X+e_mu)`, so root and straight averaging differ by an exact
   coarse gradient. Pairing the four straight edges at a common offset
   and applying discrete Stokes gives R4. For each curvature orientation,
   its nonnegative matrix has row sum L² and column sum L⁻²: a fixed fine
   plaquette and a chosen pair of in-plane offsets determine one block
   and one base point. Weighted Cauchy–Schwarz therefore gives R5, with
   general-dimensional constant `L² L^(2-d)=L^(4-d)`.

   A direct Fourier calculation checks the sharpness on admissible exact
   periodic curvature. With `z=exp(2pi i/(LT))`, the potential
   `A_2(x)=z^x1/(z-1)` gives `F_12=z^x1`. The output multiplier is
   `(1+z+...+z^(L-1))²`; the coarse lattice has L⁻⁴ as many sites.
   The squared norm ratio is precisely R6 and tends to one. For T>2,
   real and imaginary parts have half the complex squared norm at each
   level, so real examples have the same ratio. Scaling the amplitude
   removes any potential-size objection. No nonzero constant exact
   periodic curvature is needed.

   In two successive straight averages the offsets `La+r` and `Ls+t`
   run bijectively through the side-L² block and path offsets. Induction
   gives the side-n formula for n=L^r. Gradient corrections remain exact
   under further averaging. Each matrix entry then receives at most n²
   contributions of weight n⁻⁴. This proves the l1-to-sup bound R7.
   The return assertion requires `s b L^(-2r)<epsilon_r`; it supplies no
   bound independent of inherited size, original readers or kernel noise.

2. **The nonlinear flux construction.** Independently of the author's
   translated-path cancellation, calculate in the additive Z_2 cochain
   of the powers of g. Its only nonzero curvature is `da_12=1`.
   Relative to the root straight leg, the paired contour encloses a
   ribbon of parity `L(r_2-o)` in direction 1 and `L(r_1-o)` in direction
   2. The straight-leg exponents are respectively `X_2+o+a` and b.
   Odd L therefore gives contour exponents `X_2+r_2+a` and `b+r_1-o`.
   Directions 3 and 4 give identity. This uses the specified root offset,
   works for every coordinate order, and remains valid after projection
   from the periodic lift because the torus sides are even.

   Among L offsets there is one more even than odd. Averaging thus gives
   exactly R9 with `P=diag(1/L,1/L,1,...,1)`. Also `det g=1`, `g²=I`,
   `||I-g||op=2`, and `s(g)=4/N`; centrality in SU(N) is unnecessary.
   For `M=WH`, the factor W in this example belongs to SU(N) and H>0.
   In an eigenbasis of H, with `A=W*V`,

       tr H-Re tr(A*H)
         =sum_i h_i(1-Re A_ii)
         >=lambda_min(H) sum_i(1-Re A_ii)
         =lambda_min(H)||I-A||HS²/2.

   Each summand is nonnegative. Vanishing of the difference forces A=I
   by unitarity.
   Expanding the corresponding quadratic trace gives the exact identity
   R10 as well. Here `lambda_min(H)>=1/L`, so the unique maximum is the
   claimed `U^(a,b+o mod 2)`. Every 12 plaquette remains g. This establishes
   a true rough orbit of the actual normalized kernel's maxima, without
   mistaking density at a point for an event probability.

3. **Normalization, perturbation and the probability quantifiers.** A
   matrix-entry cell of side r/(2N) has Hilbert–Schmidt diameter at most
   r/sqrt(2). Representatives of occupied cells cover SU(N) by at most
   `(1+4N/r)^(2N²)` equal-Haar-mass operator balls. Trace duality gives
   Lipschitz constant one for h_M. Integrating `exp(-t psi_M)` over a
   1/t ball about a maximum, for t>=1, yields the lower denominator
   `e^(-1)(1+4Nt)^(-D)` and hence R12. This retains the full normalizer.

   Each paired contour contains at most `L+4(L-1)=5L-4` links. Telescoping
   unitary factors, including inverse links, bounds its perturbation by
   `p_L delta_j`. Comparing h at V and at the template W costs at most
   twice that amount. Substitution of R13 leaves exactly
   `delta_(j+1)²/(4NL)` in R14. Union over output links followed by
   conditioning successively on the past proves R15; temporal
   independence is not assumed. The recursively chosen radii are all
   at most delta_R. Four-link telescoping gives plaquette distance at
   least `2-4delta_j>epsilon_max` throughout the tubes.

   At fixed R and finite lattices every positive exponential rate beats
   the polynomial C_N(t_j). The probability of leaving the tubes tends
   to zero as their couplings grow. A second union bound for fresh gaps
   has terms `|E_(j+1)| C_N(t_j) exp(-t_j A_j)`; the displayed threshold
   condition makes this sum tend to zero too. Thus a rough continuation
   without fresh priced gaps has probability tending to one. This rules
   out a coupling-independent finite R and positive return probability
   valid for every real input. For an expected maximum-curvature
   contraction, the output expectation is at least
   `(2-4delta_R)(1-o(1))`, while the input maximum is at most two.
   Taking delta_R small also excludes any uniform factor below one.

   These arguments do not exchange the finite-horizon limit with infinite
   depth or volume. The initial tube can become extremely small with R.
   Each finite tube nonetheless has positive Haar measure and positive
   finite original-chain mass. Expanding `(I-W)*(I-W)` gives
   `2N s(W)=||I-W||HS²`; applying this to the distinct initial 12 plaquettes
   proves R16. Future normalized kernels preserve this creation charge
   once. They do not pay it anew. A local embedding preserves the tower
   only when its entire finite backward reader set is filled; no uniform
   collar-size assertion follows.

4. **The nonuniform return bound.** From `|h_M|<=1`, one has
   `exp(-2t)<=k_t`. The product identity cap has Haar measure at least
   `(1+4N/delta)^(-Dm)` and every plaquette on it is within 4delta of I.
   This proves R17. On the event of no earlier return the next conditional
   success probability is still at least p_l; iterating proves R18.
   The small p_l and the extra placement cost explain why this does not
   prove the required RG bound. The fresh-gap multiplication is likewise
   valid only for distinct output links and past-adapted choices under
   the forward law. A future or all-cut tilt must remain in the estimate.

5. **Replacement and complete readers.** RD's cut uses only plaquettes
   wholly inside individual blocks; crossing links stay frozen. Distinct
   G_2 components have sup-distance at least three, so their radius-one
   collars and allocated reading factors are disjoint. An identity cap
   on each replaced interior satisfies its cuts for every fixed exterior,
   and positivity gives C_Y>0. In a fixed B summand of R19, integrating
   the old good interiors first produces exactly `product_Y C_Y`.
   It cancels the denominator of T_B. The replacement interiors carry
   zeta_B, the other interiors retain their good cuts, and
   `b_j J_h=rho_(j,h)`. Summing B applies `product_Q(chi_Q+zeta_Q)=1`.
   There is no division by a hard predicate or history mass, and no
   factorization of J_h is required.

   The general incident-factor Fubini rule holds regardless of product
   structure in an effective density. The sharper deletion has stronger,
   now explicit hypotheses: a finite directed acyclic law of normalized
   creators, with every other factor retained or completely expanded.
   A latest vertex outside a selected ancestral closure has neither a
   selected factor nor a child in that closure and integrates to one.
   Reverse induction removes the complement. A kernel edge joining two
   remaining components would put its parent in both closures, contradicting
   disjointness. This proves conditional factorization. Integrating a
   shared outside variable later requires joining its law and all readers
   first. In particular this proof cannot declare the interacting nu_A
   independent merely by renaming it.

6. **Windows, returns and nonlinear invariance.** For `r=qm+s`, split an
   ordered continuation product into q adjacent m-windows and a remaining
   product of length s<m. Uniformity in the starting index and
   submultiplicativity give `B theta^q`. Summing q and s gives both R21
   bounds, with D_ret for the return operator. The same estimate applies
   to insertions arriving at different times before a fixed output.
   No stationarity, commutation or unproved scalar-to-operator conversion
   enters this arithmetic. The exact first-return representation and
   the operator estimates are stated assumptions of the construction.

   Disjoint splitting by the first newly priced gap proves R22 by the
   triangle inequality in the same norm. Substituting the forward R12
   price without its reference, support and tilt costs would be invalid;
   lines 447–452 prohibit that substitution. Finally, on 0<=x<=M,
   `Cx²<=CMx`, so the conditions at 540–543 give x'<=M. Iteration still
   needs initial membership, the actual norm estimates and the separate
   relevant/marginal recursions. None is produced by this scalar inequality.

7. **Grouping, logarithms and long readers.** Every selected atom set
   has a unique partition into complete overlap components. The stated
   factorization of the measure and coefficients gives an exact gas of
   their joint integrals. Nonempty supports prevent compatible components
   from reusing an atom. The mixed absolute-integral assumption bounds
   each component by the product of its alpha_i.

   With v_i and b_i as in the note,

       sum_(j:H_j meets H_i) b_j <=Q |H_i|,
       v_i exp(sum_j b_j)<=v_i exp(|H_i|)=b_i.

   Thus monotone tree iteration is bounded by b_i. Each distinct connected
   selection has a spanning tree; allowing repetitions in this positive
   majorant can only enlarge it. Marking an atom through the output root
   bounds the integrated gas at rate mu+1 by Q. The nonnegative rate is
   needed when replacing a union's support exponent by the product of
   constituent exponents.

   For each polymer tuple, a graph has a specified Kruskal tree precisely
   when its extra edges are later than every edge on their tree paths.
   Summing signs over this interval has modulus zero or one. The tree
   bound therefore applies to the logarithm, including repeated polymer
   labels. Marking the spatial root supplies the factor changing 1/n!
   to 1/(n-1)!; a second tree bound spends the remaining support exponent
   and gives log norm <=Q. Scaling atoms by z replaces Q by |z|Q<=1/2
   for |z|<=2. Both majorants converge, their exponential agrees with
   the finite gas near zero, and analytic continuation proves equality
   and nonvanishing at z=1. Parameter holomorphy additionally needs the
   explicitly stated fixed selectors, holomorphic factors and integration
   envelopes; the auxiliary z alone would not supply it.

   For R24, first absorb the extra eta weight into reader weights.
   Multiplying core weights by `R=(1/2-q)/d>=1` makes the total positive
   tree budget 1/2. Every core-containing group gains at least R, so its
   original full-root norm is at most `(1/2)/R=d/(1-2q)`. For d=0 these
   groups vanish. A connected path reaching distance r outside all cores
   uses reader supports of total size at least r, yielding exp(-eta r).
   The root is unrestricted and may lie on a tail. This estimate cannot
   manufacture the mixed hypothesis from separate one-core probabilities
   or justify charging readers a second time.

**Source and scope checks.** R1 matches the paired contours and arithmetic
mean in PROOF.md:1414–1427,2466–2472. The earlier group-valued logarithmic
averaging map has a small-field domain; the Decision-4 arithmetic mean and
normalized kernel are the actual objects used for the rough witness.
RD.md:72–99 supplies the interior-cut and frozen-link convention crucial
to C_Y>0. RD3.md:98–168,332–423 distinguishes inherited density, history
mass, the all-cut denominator and the missing uniform comparison.
RD4.md:25–75 specifies the full original-reader norm and D_*.
LFPRICE.md:654–708 is exactly the five-clause target.

JMBRA.md:24–382 supports the exact replacement and conditional
reader/grouping interfaces. JMBRB.md:126–377,595–686 distinguishes conserved
old mass, fresh gaps, per-step arithmetic and the missing extracted
operator. Its review's energy/action and cut-index cautions are respected:
RENEW retains u_0 in R16, uses actual level cuts and does not identify a
forward gap exponent with a matched one.

The cited LINEAR_PACKAGE §2.2–2.3 is at lines 124–135; its straight-iterate
identity is at 137–138. BFT_A §3.4–3.6, lines 129–174, gains from small-field
oscillations and derivative control. BFT_B §22.3–22.8, lines 3012–3102,
uses small-curvature refinement and cancellation of the averaging defect
on constant curvature. It does not remove that curvature. SOFTHARD G1–G2,
lines 285–295, concerns density analyticity and a finite seam response;
neither is a return probability. LARGE55:578–598,725–737 retains the limits
of impulse evidence and withdraws zero boundary cost. RENEW does not
promote these different statements into an inherited-roughness estimate.

The primary abstracts confirm the attribution and scalar three-dimensional
scope of Dimock's [Large fields](https://arxiv.org/abs/1212.5562) and
[Convergence](https://arxiv.org/abs/1304.0705), expositions of Balaban's
method. No external theorem or unread full-paper proof carries a step in
this review. No comprehensive novelty or open-PR search is certified.

**Binding fixes: none at the stated partial-results scope.** One optional
wording clarification is to add “coupling-uniform” to the opening return
claim at line 9. Lines 261–268 already give the correct quantifiers, and
R17 explicitly preserves finite-coupling return; this is not a mathematical
blocker. No author file was changed.

The five-clause disposition is supported: clause 1 has finite algebra,
clause 2 still lacks the joint charged/reference estimate, clause 3 lacks
the common complex reference and local TV control, clause 4 lacks actual
small mixed type/support sums, and clause 5 still needs control of every
failed completion and the extracted next-step bound. RENEW-MATCH(m), lines 524–549, is a useful
explicit construction target overlapping those obligations, not a solved
or demonstrably weaker substitute for them. Acceptance of this research
record is not completion of the author's requested renewal theorem.

The no-go-discipline check supports only this narrow disposition. The
tested averaging, restoring-force/gap and minorization mechanisms do not
exhaust routes. No independence of the remaining conditions is claimed.
The premises, resolutions and residuals are explicit, and no physical
primitive is declared missing. The strongest live alternative remains a
matched background/residual construction or a joint original-weight charge
followed by extraction. The flux example cannot exclude it. Comparison
with the existing linear dilution and boundary corrections reveals no
retired obstruction being reinstated. The note correctly withholds a
five-route packet PASS and an all-route NO-GO; this review grants neither.

**Source identities, recovery and verification limits.** Observed HEAD is
`ecd35b1be990b779de0f3af74c299c7cf1855513`; local origin/main is
`01589af3faf806b736c42dc2f3bd625e9edead9f`. The planning fetch returned
success and its ref remains
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
The attempted main fetch was denied when opening FETCH_HEAD, so remote
main freshness is unverified. The workflow, reviewer, no-go, freshness and
proof-governance sources used match the identified local main. I inspected
the installed reviewer skill's wording differences and used the repository
source; no model downgrade or delegation was introduced.

All 21 entries of checks/renew_sources.json and all ten recorded artifact
hashes in checks/renew_validation.json match. The additional RD identity
also matches. The source manifest has SHA-256
`c1dc9bb854825bb7c416e9e54995c53d50293fabd7c299c6cc57663df90b9f05`;
the validation file has SHA-256
`5dbca1a00bceaa536cc8f8810495fbb8ea8b8dc088919663ad17eded3b7a463f`.
The exact unified diff from the saved submitted note to the current note
equals checks/renew_review_fixes.patch. Both earlier binding findings are
resolved in the current text: normalized ancestral law/complete noncreator
factors at 365–396, and mu>=0 at 61. Their historical counterexamples no
longer satisfy the stated hypotheses. Hash agreement establishes identity
and recovery, not correctness.

Coverage is all 623 candidate lines, both briefs, the log, predecessor
reviews, correction record and the necessary source arguments identified
above. Needed passages from truncated broad reads were read again in
bounded slices. Historical BFT theorems not consumed here, coordinator
outputs, numerical suites, continuum reconstruction and empirical
identifications were not independently certified. The reported author
priority failure was not re-executed; no numerical physics computation or
resource-guard bypass was used. The evidence here is written mathematical
checking plus deterministic source bookkeeping.

Only REVIEW_RENEW.md is created by this task. No editable prompt, author
source, check, audit, ledger or axiom file is changed, and no commit is made.
The current recovery decision is to preserve these scoped results and
pursue RENEW-MATCH with every failed completion and original reader intact.
A change to the reviewed source or its load-bearing premises requires
refreshing the affected review.

VERDICT: LAND
