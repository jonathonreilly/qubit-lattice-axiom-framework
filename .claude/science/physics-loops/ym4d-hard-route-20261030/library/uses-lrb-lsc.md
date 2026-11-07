# Uses of the local real base and last-scale constants

Reading inventory of `/tmp/sa_ca_I.tex`, `/tmp/sa_ca_II.tex`, and `/tmp/sa_ca_III.tex`. All three files were already present. Locations below are **TeX source lines**, not printed page numbers. Only grep searches and short, targeted ranges of the source files were read. No proofs were attempted.

“Use” includes an explicit hypothesis, an invocation in a proof, and an identifiable reuse of the distinguished conclusion without its label. Repeated invocations in one statement are recorded separately where they do different work; nearby repetitions doing the same work are grouped with multiple locations. Internal uses of earlier parts in the item's own partial proofs are separated from downstream uses. An ordinary invocation of a later theorem is not automatically counted as a direct use of every earlier input to that theorem.

## A. `4.4:prop-local-real-base`

Source: `sa_ca_I.tex:8110`. The relevant content is the real symmetric base and its bounds (`4.4:eq-local-real-base-1`, `-2`), displacement bounds (parts (2σ), (2U), (2s), (2Γ)), positivity on the entire interpolation polydisc (`4.4:eq-local-real-base-4`, part (3)), and the applications to Gaussian perturbation/cancellation and the local vertex functional (parts (4a)–(4c)). The proposition is headed “Proof outstanding”; the following partial proofs do not change the scope of this reading inventory.

### Clear downstream uses

| Location | Statement using A | What is used |
|---|---|---|
| `sa_ca_I.tex:8770`, `sa_ca_I.tex:8774`, `sa_ca_I.tex:8780` | `4.4:rem-cluster-lemmas-base` | Replaces Bałaban's original base by `(Γ₀ᴿ,C₀ᶜᵛ)` and reads the listed cluster-expansion lemmas/propositions with perturbation size `C_P` times the local small parameter. |
| `sa_ca_I.tex:8809` | `4.4:rem-cluster-lemmas-base` (proof) | Uses the reality of both base members and symmetry of the covariance to justify that replacement. |
| `sa_ca_I.tex:8814` | `4.4:rem-cluster-lemmas-base` (proof) | Applies the replacement and changed small parameter to the two cluster-expansion lemmas, their proposition, and the further proposition. |
| `sa_ca_I.tex:8824` | `4.4:rem-cluster-lemmas-base` (proof) | Uses the constructed local vertex functional, citing `4.4:prf-polydisc-positivity` as a “Proposition”; that label actually belongs to A's partial proof. |
| `sa_ca_I.tex:9215`, `sa_ca_I.tex:9216` | `4.4:rem-cluster-lemmas-local` | Assumes A's hypotheses, including the parameter floors and (k2), (k3), and uses its positivity polydisc as the local interpolation domain. |
| `sa_ca_I.tex:9237`, `sa_ca_I.tex:9240` | `4.4:rem-cluster-lemmas-local` | Identifies the symmetrised inverse base covariance as an input to the perturbation estimate; item (C) explicitly assumes A itself. |
| `sa_ca_I.tex:9255`, `sa_ca_I.tex:9260` | `4.4:rem-cluster-lemmas-local` | Transfers the base-covariance lemma's items (i)–(iv) with A's changed perturbation size, lower bounds, inverse-kernel decay, symmetrisation error, and parameter floors. |
| `sa_ca_I.tex:9278` | `4.4:rem-cluster-lemmas-local` (proof) | Uses the standing lower bound on `M`, described as A's hypothesis “(R9),” with the enlarged pair of kernel constants. This is the source's wording; A is currently enumerated (a)–(d). |
| `sa_ca_I.tex:9287`, `sa_ca_I.tex:9292`, `sa_ca_I.tex:9298` | `4.4:rem-cluster-lemmas-local` (proof) | Constructs the local real base explicitly as `(Re Γ(0;U|Z,0),G₀⁻¹)`, where `G₀=sym Re T_{Z₀′}(U|Z₀′,0)`, following A. |
| `sa_ca_I.tex:9299`, `sa_ca_I.tex:9304` | `4.4:rem-cluster-lemmas-local` (proof) | Uses the content of A(1): `5γ*/8 ≤ G₀ ≤ B` and exponential decay of `G₀`; the text also names A's precursor coercivity and symmetric-form results. |
| `sa_ca_I.tex:9313`, `sa_ca_I.tex:9325`, `sa_ca_I.tex:9329` | `4.4:rem-cluster-lemmas-local` (proof) | Reuses A(4a)'s substitutions in the perturbation lemma and the three additional smallness/floor conditions, including the symmetrisation contribution. |
| `sa_ca_I.tex:9333`, `sa_ca_I.tex:9340` | `4.4:rem-cluster-lemmas-local` (proof) | Explicitly invokes A(3), reproducing `Re C(Z₀,σ;u)⁻¹ ≥ 3γ*/8` on the whole σ-polydisc. |
| `sa_ca_I.tex:9342` | `4.4:rem-cluster-lemmas-local` (proof) | Invokes A(4c)'s equal-level restriction of Σ-representatives to every admissible `Y′ ⊂ Z`. |
| `sa_ca_I.tex:9348` | `4.4:rem-cluster-lemmas-local` (proof) | Uses the local-base bounds and σ-polydisc positivity at every restricted local datum to conclude persistence of Bałaban's Lemma 3 and the account's analogue for the CMP119 expansions. |
| `sa_ca_I.tex:9665`, `sa_ca_I.tex:9668` | `4.4:cor-localised-independence` | Uses A to ensure that the vertex functionals for the second and third parts are defined on the indicated one-power hereditary local class. |
| `sa_ca_I.tex:9774`, `sa_ca_I.tex:9777` | `4.4:cor-localised-independence` (proof) | Uses A's property on `P_{1+β,X}`, with the chapter's standing hypothesis, to make the vertex functionals admissible before comparing the second and third parts. |

These clear downstream invocations are all in Part I. Searches found no explicit invocation of A, its equation labels, or its distinctive symmetrised local-base pair in Parts II–III.

### Clear internal uses within A

These are uses of earlier clauses while formulating or partially proving later clauses, not additional downstream statements.

| Location | Statement / proof label | What is used |
|---|---|---|
| `sa_ca_I.tex:8313` | `4.4:prop-local-real-base`, (4a) | Uses (2σ) and (2U) to supply the interpolated-family and product bounds. |
| `sa_ca_I.tex:8323`, `sa_ca_I.tex:8333`, `sa_ca_I.tex:8335` | `4.4:prop-local-real-base`, (4a) | Uses equation `4.4:eq-local-real-base-2` for covariance lower/reciprocal-norm bounds and inverse-kernel decay, and (2σ), (2U), (2s) for the perturbation. |
| `sa_ca_I.tex:8340`, `sa_ca_I.tex:8345` | `4.4:prop-local-real-base`, (4b) | Uses (1)'s positive real symmetric base to obtain exact zeroth-order Gaussian cancellation and convergence of the remaining integral. |
| `sa_ca_I.tex:8419`, `sa_ca_I.tex:8423` | `4.4:prop-local-real-base`; partial proof `4.4:prf-imaginary-part` | Uses the symmetrisation-tail bound and the already established real symmetric, coercive, decaying `A₀` to bound the difference of the base covariances; these properties also come from the named precursor corollary. |
| `sa_ca_I.tex:8578`, `sa_ca_I.tex:8585` | `4.4:prop-local-real-base`; partial proof `4.4:prf-polydisc-positivity`, (3) | Imports earlier parts (1), (2σ), (2U), (2s), (2Γ), and specifically applies (2σ)'s Schur bound to the covariance displacement. |
| `sa_ca_I.tex:8634`, `sa_ca_I.tex:8637` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4a) | Uses (2σ)'s walk count and (2U)'s Cauchy estimate for the kernel and product lemmas. |
| `sa_ca_I.tex:8646`, `sa_ca_I.tex:8650`, `sa_ca_I.tex:8654`, `sa_ca_I.tex:8672` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4a), perturbation item (i) | Uses (1)'s covariance bounds and inverse decay, (2σ)/(2U)/(2s)'s displacement, and (3)'s already available positivity. |
| `sa_ca_I.tex:8674`, `sa_ca_I.tex:8680` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4a), item (ii) | Uses (2Γ)'s small imaginary part of `Γ₀`, together with the interpolated-kernel displacement, to perturb from `Γ₀ᴿ`. |
| `sa_ca_I.tex:8684` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4a), item (iii) | Uses the just-bounded covariance and vertex-kernel differences in the telescoping quadratic prefactor. |
| `sa_ca_I.tex:8687`, `sa_ca_I.tex:8692` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4a), item (iv) | Uses (1)'s real inverse covariance and norm bound, plus the small displacement, for the real-part determinant perturbation. |
| `sa_ca_I.tex:8695`, `sa_ca_I.tex:8700`, `sa_ca_I.tex:8711` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4b) | Uses (1), (2σ), (2U), (2s) and the smallness floors for the positivity lemma, exact cancellation, and the `α₅‖C₀ᶜᵛ‖ < 1/2` condition. |
| `sa_ca_I.tex:8733`, `sa_ca_I.tex:8738` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4b) | Uses (1)'s norms of `C₀ᶜᵛ` and `Γ₀ᴿ` to control the remaining exponent and make the outer Gaussian integral convergent. |
| `sa_ca_I.tex:8748`, `sa_ca_I.tex:8750` | `4.4:prop-local-real-base`; `4.4:prf-polydisc-positivity`, (4c) | Uses (4b) at interpolation vertices, then (2σ), (3), and (4b) on the full polydisc to obtain the analytic vertex functional needed by the vertex formula. |

### Ambiguous mentions and related content

| Location | Statement / context | Why it is not a confirmed additional use of A |
|---|---|---|
| `sa_ca_I.tex:6950` | `4.4:lem-cell-resolvent`, (v) (proof labelled `4.4:prf-local-resolvent`) | Says that a later “local symmetry lemma and its companion proposition” supply the real symmetric Gaussian base. This plausibly points forward to A, but is a description of a later application, not an input to the resolvent argument here. |
| `sa_ca_I.tex:7337`, `sa_ca_I.tex:7341`, `sa_ca_I.tex:7347` | `4.4:rem-symmetric-base-need` | Describes the reality/symmetry inputs needed by the vertex analysis. It motivates A; it does not invoke A's symmetrised replacement, and its assertion of a real unmodified `Γ₀` is not A's small-imaginary-part conclusion. |
| `sa_ca_I.tex:9603` | Unlabelled remark beginning at line 9580, following `4.4:lem-interior-sufficiency` | Calls on the “vertex-functional theorem at equal levels” for the second and third parts of the ensuing corollary. This matches A(4c)/its proof and the local-base remarks, but identifies no unique theorem label. |
| `sa_ca_II.tex:3647`, `sa_ca_II.tex:3651`, `sa_ca_II.tex:3727`, `sa_ca_II.tex:3735` | `5.2:lem-complex-fluctuation` | Uses real reference operators, small covariance/kernel perturbations, and zeroth-order cancellation in the same CMP116 Gaussian analysis. It attributes them to Bałaban's original operators and estimates, without identifying A's local symmetrised base. Shared content, but attribution to A is uncertain. |
| `sa_ca_II.tex:10501` | `5.2:rem-positivity-scope`, (n1) | Assumes a real symmetric positive reference covariance at zero interpolation, justified by the takeover of Bałaban's cluster-expansion bounds and a quotation. It does not identify the replacement covariance of A. |

Reference-only occurrences: `sa_ca_I.tex:8764` identifies the parameter; `sa_ca_I.tex:8391` and `sa_ca_I.tex:8564` are partial-proof titles. The route at `sa_ca_I.tex:8376`–`8389` describes how A is to be established, not a separate downstream invocation. The earlier symmetric-base corollary and floor definition are inputs **to** A, not uses of A.

## B. `6.3:lem-last-scale-constants`

Source: `sa_ca_II.tex:63365`–`63367` is a **remark saying that the lemma's statement is unwritten**. The inventory does not supply a missing statement. Its printed partial proofs and later invocations identify the content in use: a finite cutoff offset `a=K_J-K`; a fixed block exponent and bounded unit rescaling `b`; the bound `E₊^♯+C_low ≤ E_*` independent of the physical torus exponent `m₁`; the rescaled per-ball constant `C_n^*`; the short-run local-plaquette bound `C_n^B`; and the bare-coupling subsequence/limit argument.

In particular, the correlation theorem's omitted-step/block exponent `m` and the physical torus exponent `m₁` are distinct. The printed bound `x_{K′} ≤ X+b₊+3λm+2c₂` alone is an antecedent of B, not yet B's torus-uniform conclusion; the latter uses the choice `m=m_𝕋^J(g)`.

### Clear downstream uses by label or uniquely identifying description

| Location | Statement using B | What is used |
|---|---|---|
| `sa_ca_II.tex:60354`, `sa_ca_II.tex:60356`, `sa_ca_II.tex:60358` | `6.1:not-units-sources`, (a) | Uses B's identification of the last lattice and `0 ≤ b ≤ b_*(g)`, independent of cutoff and physical torus exponent, to fix length conversion and a finite collection of unit rescalings. |
| `sa_ca_II.tex:63839`, `sa_ca_II.tex:63844`, `sa_ca_II.tex:63848` | `6.3:cor-volume-free-constant` | Explicitly assumes B(c), B(d), their hypotheses, and the extra per-ball torus floor to state the bound in unit-lattice units. |
| `sa_ca_II.tex:63870` | `6.3:cor-volume-free-constant` (proof, Case A) | Applies B(c)'s transported bound with constant `C_n^*(d;R)`. |
| `sa_ca_II.tex:63880`, `sa_ca_II.tex:63888` | `6.3:cor-volume-free-constant` (proof, Case B) | Applies B(d)'s local-plaquette/cumulant bound `C_n^B`, then bounds the sup norm by the sharp norm. |
| `sa_ca_II.tex:63897`, `sa_ca_II.tex:63899` | `6.3:cor-volume-free-constant` (proof) | Uses the parameter dependence and monotonicity from (c), and uniformity from (d), to make `max{C_n^*,C_n^B}` independent of `K,g₀,m₁,a,N` and position. |
| `sa_ca_II.tex:63917`, `sa_ca_II.tex:63919` | `6.3:rem-per-ball-reading` | Reuses B(b)'s fixed-block-exponent evaluation and uniform `E_*` bound, displayed as `6.3:eq-per-ball-reading-2`. |
| `sa_ca_II.tex:63923`, `sa_ca_II.tex:63924` | `6.3:rem-per-ball-reading` | Reads the per-ball constant as B(c)'s finite maximum `C_n^*` from `6.3:eq-unit-rescalings-b`, with B(d)'s local count for the remaining short runs. |
| `sa_ca_II.tex:63938`, `sa_ca_II.tex:63940` | `6.3:rem-per-ball-reading` (proof) | Invokes “the result on admissible data and the last-scale coupling,” i.e. B(b)'s printed proof, to bound both per-site constants independently of `K,g₀,m₁,a`. |
| `sa_ca_II.tex:63943`, `sa_ca_II.tex:63945`, `sa_ca_II.tex:63946` | `6.3:rem-per-ball-reading` (proof) | Uses “the result on the per-ball bound across unit rescalings” and the “local plaquette count and cumulant bound,” i.e. B(c), B(d). |
| `sa_ca_II.tex:64271`, `sa_ca_II.tex:64273` | `6.4:thm-per-ball-bound` (proof labelled `6.4:prf-recentred-quotient`) | Explicitly invokes uniformity of the last-scale constants to replace `C_low` at the torus index by an index-free bound; this is used to establish the constant's claimed volume independence at `sa_ca_II.tex:64000`. |
| `sa_ca_II.tex:64504`, `sa_ca_II.tex:64505` | `6.4:rem-unit-conversion`, (2) | Uses “the first case of the lemma fixing the torus index of the correlation theorem”: a bounded nonnegative integer `b`, independent of `K,m`, eventually constant on the limit subsequence. This is B's Case A/finite-offset content, without its label. |
| `sa_ca_II.tex:64512`, `sa_ca_II.tex:64543`, `sa_ca_II.tex:64547`, `sa_ca_II.tex:64565` | `6.4:rem-unit-conversion` and proof | Uses that finite range of rescalings to take `max_b C_n^∞(dL^b;RL^b)` and a common torus floor, preserving independence from `K,g₀,m` and positions. |

### Clear reuse of B's uniformity content, without an attribution to B

The following passages concretely need the same torus-free per-site constants or bounded rescaling data. The **content-use is clear**; the source does not establish a labelled dependency on B at these locations, and sometimes calls the input simply the correlation theorem.

| Location | Statement / context | What is used |
|---|---|---|
| `sa_ca_II.tex:62804`, `sa_ca_II.tex:62820` | Unlabelled paragraph after `6.2:prop-cell-covariance` | Calls the displayed averaged-orbit bound independent of `m`, while its right side contains `(E₊^♯+C_low)ℓ⁴`; this needs uniformity of those per-site constants. |
| `sa_ca_II.tex:64299`, `sa_ca_II.tex:64340`, `sa_ca_II.tex:64341` | `6.4:rem-complex-sources` and proof | Deduces an `m`-independent zero-free radius from `Q_∞`, explicitly listing `E₊^♯` and `C_low` among its ingredients. |
| `sa_ca_II.tex:140927`, `sa_ca_II.tex:140931` | `8.22:not-partition-sources-cells` | Declares `E₊^♯`, `C_low`, and their sum `B` independent of `K,g₀,m`, making the torus-uniform last-scale content a standing input for volume transfer. |
| `sa_ca_II.tex:141546`, `sa_ca_II.tex:141836` | `8.22:thm-volume-transfer` and proof | Uses that same `B=E₊^♯+C_low` and explicitly its freedom from both torus exponents `m,m′` to obtain a volume-independent transfer constant. |
| `sa_ca_III.tex:71674`, `sa_ca_III.tex:71677` | `9.98:def-prolongation-depths` | Evaluates `B(g)=E₊^♯+C_low` at the fixed reference coupling and treats the resulting transfer constants as independent of `m`, cutoff, bare coupling, and tuned depth. |
| `sa_ca_III.tex:72738`, `sa_ca_III.tex:72759` | `9.98:prop-transfer-three-sources`, hypotheses (a), (d) | Explicitly assumes upper and lower per-site stability constants independent of `K,g₀,m,m′`; this is the torus-uniform content needed for the three-source transfer. |
| `sa_ca_III.tex:72972`, `sa_ca_III.tex:72980`, `sa_ca_III.tex:72984` | `9.98:prop-transfer-three-sources` (proof) | Uses those constant-dependence hypotheses to remove cutoff and torus dependence from `Q_{*,3}` and `C_{VT,3}`. |

### Clear internal uses in the printed partial proofs of B

| Location | Statement / proof label | What is used |
|---|---|---|
| `sa_ca_II.tex:63371`, `sa_ca_II.tex:63372`, `sa_ca_II.tex:63425` | `6.3:lem-last-scale-constants`, (b); `6.3:prf-last-scale-coupling` | Uses (a)'s finite-offset assertion `a∈A` to obtain nonnegative admissible exponents and an integer `N_T`. |
| `sa_ca_II.tex:63414`, `sa_ca_II.tex:63485` | `6.3:lem-last-scale-constants`, (b); `6.3:prf-last-scale-coupling` | Uses the lemma's bare-lattice/partition-function setup to identify the dilated correlation-theorem lattice and the same connected derivatives. |
| `sa_ca_II.tex:63585`, `sa_ca_II.tex:63587`, `sa_ca_II.tex:63590` | `6.3:lem-last-scale-constants`, (c); `6.3:prf-unit-rescalings` | Uses earlier admissible-data identifications, the bound `6.3:eq-last-scale-coupling-c`, and the finite range `b=m_𝕋^J(g)-a`. |
| `sa_ca_II.tex:63625` | `6.3:lem-last-scale-constants`, (c); `6.3:prf-unit-rescalings` | Uses the identifications of (a)/(b) to read the per-ball theorem's torus floor in the rescaled units. |
| `sa_ca_II.tex:63656`, `sa_ca_II.tex:63658`, `sa_ca_II.tex:63668` | `6.3:lem-last-scale-constants`, (c); `6.3:prf-unit-rescalings` | Substitutes the earlier `E_*` bound into the monotone function `Φ` and maximises over the finite set of rescalings to define `C_n^*`. |
| `sa_ca_II.tex:63700` | `6.3:lem-last-scale-constants`, (d); `6.3:prf-plaquette-count` | Uses the earlier conclusion `K≤K_J` from (I1)–(I3), hence a uniform upper bound on the cutoffs in Case B, for the local count. |
| `sa_ca_II.tex:63802`, `sa_ca_II.tex:63807`, `sa_ca_II.tex:63809` | `6.3:lem-last-scale-constants`, (e); `6.3:prf-bare-coupling-limit` | Uses the first-passage divergence input and (a)'s finite offsets to get `K_J→∞` and eventually Case A. |
| `sa_ca_II.tex:63817`, `sa_ca_II.tex:63824` | `6.3:lem-last-scale-constants`, (e); `6.3:prf-bare-coupling-limit` | Uses finiteness of `A` to choose a subsequence with fixed `a`, hence fixed `N_T,m_J,b,N`, as required by the correlation-theorem limit clauses. |
| `sa_ca_II.tex:63828`, `sa_ca_II.tex:63831` | `6.3:lem-last-scale-constants`, (e); `6.3:prf-bare-coupling-limit` | Uses the last-scale coupling input and the displayed bounds `6.3:eq-last-scale-coupling-c`, `6.3:eq-unit-rescalings-b`, and (d)'s bound; their constants apply along the whole sequence without fixing its offsets. |

### Dependency summaries, ambiguous mentions, and explicit non-uses

| Location | Statement / context | Reading |
|---|---|---|
| `sa_ca_I.tex:3173`, `sa_ca_I.tex:3175` | Discussion following `3.1:thm-main`, OS0 item | **Explicit dependency summary:** the per-ball bound uses last-scale uniformity in the torus exponent, described as “stated; proof incomplete.” This is a clear named dependency, not a new proof application. |
| `sa_ca_II.tex:63275`, `sa_ca_II.tex:63277` | `6.3:def-one-sided-floors` | **Explicit scope mention:** specifies the extra torus floor for B(c) and its corollary; it supplies a hypothesis to B rather than using a conclusion of B. |
| `sa_ca_II.tex:63531`, `sa_ca_II.tex:63550`, `sa_ca_II.tex:63558` | `6.3:rem-exponent-statements` and proof | **Explanation of B's antecedents:** identifies the three correlation-theorem assertions on which B(b) rests and refers to `6.3:eq-last-scale-coupling-a`. It explains how B's claim is obtained, rather than assuming B downstream. |
| `sa_ca_II.tex:64442` | `6.4:rem-small-cutoffs` | **Explicit non-use:** says a separate small-cutoff treatment “as in the second case” of B is not needed, then describes an optional local-plaquette alternative. |
| `sa_ca_II.tex:64467`, `sa_ca_II.tex:64468`, `sa_ca_II.tex:64469` | `6.4:rem-small-cutoffs` (proof) | **Explicit but inconsistent description:** claims B's second case counts all torus plaquettes. The printed B(d) instead makes a local count at `sa_ca_II.tex:63712`–`63738` and explicitly rejects the global count at `sa_ca_II.tex:63795`–`63798`; do not infer a valid dependency on the alleged global-count bound. |
| `sa_ca_II.tex:64598`, `sa_ca_II.tex:64599` | `ch:6`, unlabelled “Inputs used by statement” list | **Bibliographic dependency mention:** lists CMP122b p. 355 among block-exponent assertions assumed in B. The more precise `6.3:rem-exponent-statements` says the particular independence clause on that page is not used (`sa_ca_II.tex:63552`). |
| `sa_ca_II.tex:68362`, `sa_ca_II.tex:68364` | `ch:7`, unlabelled “Inputs used by statement” closing discussion | **Explicit dependency summary:** says the clause-(ii) proofs appeal by statement to last-scale uniformity, together with the correlation theorem, per-ball bound, and reflection positivity. No particular clause-(ii) lemma is identified here as its direct user. |
| `sa_ca_III.tex:21101`, `sa_ca_III.tex:21104` | `9.1:not-stop-depth` | **Ambiguous identity:** invokes a lemma on dependence of last-lattice constants on `m₀`, saying the dependence of `Q_w`, window radius, `C_*(N_w)`, and threshold length passes through `N_w` only. This resembles B's content but does not identify B, and concerns a stopped uniqueness run with different constants. |
| `sa_ca_III.tex:73462`, `sa_ca_III.tex:73465`, `sa_ca_III.tex:73524` | `9.98:lem-reference-torus-limit`, (c), and proof | **Ambiguous attribution / inherited content:** uses the displayed last-lattice factor `exp[(E₊^♯+C_low)N_w⁴]` to describe torus dependence of convergence moduli. The proof attributes this to clause (v), not B; it evaluates on one torus fixed by `g`, so it need not invoke B separately. |
| `sa_ca_III.tex:73535`, `sa_ca_III.tex:73537` | Unlabelled remark after `9.98:lem-reference-torus-limit` | **Inherited-content explanation:** says the same factor is incurred once on a reference torus and disappears with the cutoff limit; it explicitly attributes the input to clause (v). |
| `sa_ca_III.tex:73926`, `sa_ca_III.tex:73937` | `9.98:thm-short-distance-uniqueness`, proof of (g), labelled `9.98:prf-proof-rectangular-tori` | **Possible content use:** uses the per-cell mismatch `B=E₊^♯+C_low` in a rectangular-torus stability estimate. The named inputs are the correlation theorem and the last-level lower bound of (i-b), rather than B. |
| `sa_ca_III.tex:75692`, `sa_ca_III.tex:75696`, `sa_ca_III.tex:75703` | `9.98:rem-five-counter-states` | **Explanatory mention:** lists the same global, per-cell, and clause-(v) volume factors while discussing limitations of later conclusions; it does not apply B. |
| `sa_ca_III.tex:110895`, `sa_ca_III.tex:110898` | `ch:11`, unlabelled “The standing of the clauses,” (iii) | **Explicit dependency summary:** again names last-scale uniformity as an input to the per-ball bound, with status “stated; proof incomplete.” |

Proof-title references at `sa_ca_II.tex:63369`, `sa_ca_II.tex:63568`, `sa_ca_II.tex:63694`, and `sa_ca_II.tex:63800` identify the item being partially proved; they are not extra downstream applications.

The ordinary correlation-theorem last-scale estimates in `6.3:not-data-families`, `6.3:rem-constant-dependence`, and `5.12:eq-torus-bound-proof-6` are antecedents of B. Likewise the hatted-run floor comparison at `sa_ca_III.tex:60586`–`60598` uses the correlation theorem's `x_{K′}` bound, without fixing the block exponent as B does. These were checked, but are not counted as uses of B's torus-uniform conclusion. Generic later uses of the per-ball theorem alone are transitive dependencies, not additional identified direct uses of B.

## Search terms and completeness confidence

Searches were run across **all three** files, then hits were checked in short `sed` ranges. Exact terms and stems included:

- A: `prop-local-real-base`, `local-real-base`, `4.4:eq-local-real-base`, `4.4:prf-polydisc-positivity`, `4.4:prf-imaginary-part`, `4.4:rem-cluster-lemmas-base`, `4.4:rem-cluster-lemmas-local`; `local real base`, `real local base`, `real base`, `local base`, `symmetric base`, `symmetrised base`, `symmetrized base`, `local symmetry lemma`, `companion proposition`, `base covariance`, `base-covariance`, `polydisc positivity`, positivity/polydisc in both orders, `vertex functional`, `vertex-functional theorem`, `Gaussian vertex`, `perturbation lemma`; `C_0^{\mathrm{cv}}`, `Gamma_0^{\mathbb{R}}`, `\Gamma_0`, `\mathsf{G}_0`, `hat\varepsilon`, `\hat{\varepsilon}`, `eta_{\mathrm{sym}}`, `varepsilon_0^{P`, `C(Z_0`, `C^{(k)}(Z_0`, `f(\sigma)`; CMP116 equation descriptions `(2.16)--(2.17)` and `(2.23)--(2.26)`; `4.4:lem-vertex-formula` and its downstream uses.
- B: `lem-last-scale-constants`, `last-scale-constants`, `last-scale-coupling`, `6.3:eq-last-scale`, `6.3:prf-`, `6.3:eq-unit-rescalings`, `6.3:eq-plaquette-count`, `6.3:eq-per-ball-reading`, `6.3:cor-volume-free-constant`, `6.3:rem-per-ball-reading`, `6.3:rem-exponent-statements`; last-scale/last-lattice with `constant`, `uniform`, `uniformity`, `coupling`, and `torus exponent`; `unit rescalings`, `unit conversion`, `local plaquette count`, `block-exponent dependence`, `admissible data and the last-scale`, `fixing the torus index`, `bare couplings tending`; `E_{*}`, `E_*`, `x^{*}(g)`, `C^{*}_{n}`, `C^*_{n}`, `C^{B}`, `C^B`, `\mathcal{B}(g)`, `b_*(g)`, `K_J`, `m_J`, `m^{J}`, `E_{+}^{\sharp}`, `E_+^{\sharp}`, `C_{\mathrm{low}}`; statements that constants are free of, independent of, or depend on the torus/exponent, and the volume-transfer and stopped-run displays found through those searches.
- Environment/label searches (`\begin{lemma}`, `proposition`, `corollary`, `theorem`, `definition`, `remark`, `proof`, and `\label{...}`) identified the enclosing statement of each retained hit. Case-insensitive and bounded-distance phrase searches were used as well as literal searches.

**Confidence:** high for completeness of explicit labels, equation-label references, named mentions, and the distinctive local formulas; moderately high for direct descriptive/content uses. The principal residual uncertainty is attribution of generic Gaussian-base assumptions to A and of later torus-free stability constants to B, especially because B's statement is absent. Those candidates are retained above rather than silently treated as confirmed dependencies. This is a direct-use inventory, with named dependency summaries and salient inherited-content candidates included; it is not the full transitive dependency closure of either item.
