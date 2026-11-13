# CL1 Lemma 4: line-by-line read of the 2026-11-13 edit

Dispatch note, written by the session that made the edit (Claude, Fable 5.2), not by the reader. Everything below the rule is the reader's file, unchanged.

- Reader: Codex, `gpt-6-astra`, reasoning effort high, thread `01a1d4cd-00f8-7153-be95-c05bd9545fb1`, 2026-11-13, 12:06 to 12:12 UTC. The reader could not see its own model name, so its last line says "undisclosed"; the model and effort here are from the launch command and the session file.
- It read [cl1.md](../library/cl1.md) with SHA-256 `2704a8d685a9355584b758c2998a457c108cb5809b42e3a0a7d98d6f33b2cdaa` and [sr1.md](../library/sr1.md) with SHA-256 `b95906583787c65d5cbdded79f438bcd242b4f796a4b0829bd045ce97a9bbf4d`.
- The committed `cl1.md` has SHA-256 `bfcfbb52b262f33eb9ef975e2738da76012c3f78814087a34c69b3cd7ce54119`. It differs from the text that was read in one sentence of the 2026-11-13 change log, outside Lemma 4: the reader's step 6 found that sentence too wide if read literally, and it was tightened after the read. Lemma 4 itself, from its heading to the heading of Lemma 5, is byte for byte the text that was read.
- The brief asked for steps 1 to 5 before the change logs were opened. The reader reports that a search showed it two change-log entries early. This is one reading by one model. It is not an audit and grants no status.

---

# Lemma 4 independent read

The SHA-256 of `cl1.md` is `2704a8d685a9355584b758c2998a457c108cb5809b42e3a0a7d98d6f33b2cdaa`, matching the required value.

Procedure deviation: the initial heading/anchor search also matched and displayed `cl1.md:533–534` (two entries in the first change log) before steps 1–5. This was an error; the requested blind read order was not preserved. The analysis below checks source statements directly. The complete change logs will be read only at step 6. The search also incidentally displayed `sr1.md:566`.

## Step 1 — Claim with quantifiers

The statement is `cl1.md:203–208`. Fix the upstream data and constants in I1–I3 and the original subsequence of Lemma 2. For every integer $n\ge1$, take either $\sigma_n$ or $(\sigma_S)_n$; for every integer $n\ge2$, one may instead take the cumulant $S_n$.

1. Each such form has exactly one distribution on $\mathbb E^n_{\ne}$ agreeing with its values on every smooth compact separated tensor. Locally finite order means that on each compact subset of this open set some finite derivative order and finite constant control its test evaluations; these may depend on the compact set and $n$.
2. Each has exactly one continuous linear extension to $\mathcal S_{\Delta,n}$, the diagonal-flat Schwartz space with the inherited Schwartz topology (`cl1.md:50–54`). Agreement is with the off-diagonal distribution, hence in particular its smooth separated-tensor values.
3. For each permitted $n$, there is a finite $A'_n$ such that for every $\Phi\in\mathcal S_{\Delta,n}$ and every lattice index $j$, both $|\Sigma_{j,n}(\Phi)|$ and $|\Sigma_n(\Phi)|$ are at most $A'_n p_{20n}(\Phi)$. The corresponding lattice families are moments centered at $\nu_j$, moments centered at $\rho_j$, and integrating-state cumulants, respectively. These use the same construction and a common bound; taking a maximum over the finitely many families at a given order is harmless. The constant is independent of $j$, states, positions and the test, but may depend on $n$, the fixed source data and fixed smooth cutoffs (`cl1.md:93,212–217`). There is no asserted growth rate for $A'_n$.
4. For each such family and each fixed flat test, $\Sigma_{j_r,n}(\Phi)\to\Sigma_n(\Phi)$ on the original subsequence. More generally, whenever $\Phi_{j_r},\Phi\in\mathcal S_{\Delta,n}$ and $\Phi_{j_r}\to\Phi$ in Schwartz topology, $\Sigma_{j_r,n}(\Phi_{j_r})\to\Sigma_n(\Phi)$.
5. For both moment-limit families only, for all $n\ge1$ and all flat tests, the bound strengthens to $C_E^n(n!)^{k+32}p_{20n}(\Phi)$. Here $k=\lceil p\rceil+5$ and $C_E$ are fixed source/extension constants, chosen before $n$ and tests; the same imported constant works for the two families. The last sentence of line 208 explicitly excludes a claim of this flat-space factorial bound for cumulant limits or lattice forms. This exclusion does not withdraw their separated-tuple factorial estimates (4).

Degree zero is not an assertion of this lemma. The proof also establishes density of finite sums of smooth separated tensors, and its strictly positive-time version, although these are not separately listed in the statement.

## Step 2 — Line-by-line proof read

| Lines in `cl1.md` | Inference and check |
|---|---|
| 210 | Provenance only; not used as mathematical evidence. |
| 212–217 | Establish (13) for each family and uniformly for its lattice versions from (4). On unit-radius supports, $B(1)$ is fixed; $\|f\|_\sharp\le\max(1,c_M)\|f\|_1$. Complexification costs a fixed factor per slot. Cumulants use the third line of (4); canonical moments use $(\rho_j,\rho_j)$. Lemmas 2–3 give the corresponding limits. No growth control of the resulting $A_n$ is needed here. |
| 219 | The inner/expanded cubes, period $8\ell$ and $\ell=h/64$ permit independent smooth slot cutoffs without intersecting another periodic copy. The separation hypothesis permits applying (13) to every cut-off tensor mode. Small product boxes of this kind cover the off-diagonal open set. |
| 221–226 | Four Laplacian integrations per four-dimensional slot use at most $8n$ derivatives and produce the product Fourier decay shown. Rescaling only changes constants depending on $n$. |
| 228–230 | Each tensor mode costs $\ell^{-n}\prod_i(1+|v_i|)$; (13) costs at most a constant times $h^{-5n}$. The four-dimensional shell sum is summable, since its summand is $O(r^{3-7})$. Thus (14) follows with $h^{-6n}$. Absolute convergence defines a linear local functional. |
| 232–236 | Extra integrations give derivative convergence. The displayed Fejér kernel has integral one with normalized period-two measure and concentrates at zero; hence it identifies the series with the original test. Applying slotwise $C^1$ convergence to smooth separated tensors and (13) gives their prescribed values. |
| 238, first two sentences | Finite-dimensional evaluation maps are injective, as are their tensor products, so a tensor-function relation is respected by the multilinear functional. This justifies passing from formal sums to functions. |
| 238, overlap sentences | A compact overlap admits smaller product boxes with expanded boxes inside it. On each such box the two local functionals agree on the cut-off separated Fourier tensors; derivative convergence and their local bounds give equality on the test. Refining two finite partitions by their products therefore gives cover independence. |
| 238, final sentences | The local functionals glue. Splitting each factor of a larger separated tensor recovers its value by admissible multilinearity. A finite cover of a compact set and (14) give finite order there. Any other distribution with those tensor values agrees on the Fourier approximations and hence on all local tests. This delivers the off-diagonal existence and uniqueness in line 203. |
| 240–245 | $\sum_{r=0}^R D_r=P_{h_R}\to1$ off the diagonals. If $D_r\ne0$ for $r\ge1$, the minimum pair sup-distance is greater than $h_r$ and less than $4h_r$: below the former both products vanish, above the latter both equal one. For $n=1$ there are only coarse terms. |
| 247 | Normalizing bump translates gives a smooth grid partition. If a product box meets the layer, its witness point has every pair distance at least $h_r$ in sup norm. Moving from that witness to expanded cubes changes the pair distance by at most $6\ell_r$ in that norm. Their sup-distance, hence Euclidean distance, exceeds $h_r/2$. The local bound is therefore available on each piece. |
| 249–256 | Every derivative of a flat test vanishes on a pair diagonal. Taylor expansion at the nearby diagonal gives the power $h_r^{10n+2}$ for derivatives through order $8n$; at most $18n+2\le20n$ derivatives are used. The displacement is bounded by $8h_r$, so the Schwartz weights are comparable. Scaled derivative factors cancel the cutoff costs, and the finite product/Leibniz constants may depend on $n$. At derivative-support boundary points the same bounds hold by closure. The coarse layer needs no small factor. This delivers (15). |
| 258–262 | The displayed weight inequality follows from $\prod_i(1+|x_i|^2)\le(1+\sum_i|x_i|^2)^n$. The supremum on each small box is comparable to the weight at its grid center. Each four-dimensional grid sum is $O(\ell_r^{-4})$ since the one-slot weight decays as $|x_i|^{-20}$, with radial tail $r^{-17}$. Thus the full position sum is $O(h_r^{-4n})$. |
| 262–267 | Combining (14), (15) and the position count leaves $h_r^{10n+2-6n-4n}=h_r^2$. Its dyadic sum converges. The coarse sum is finite as well. Summation defines a continuous functional bounded by $A'_np_{20n}$, agrees with the off-diagonal distribution by the partition identity, and works with the same constants at every $j$. This proves existence of the flat extension and (12). |
| 269 | Cutting off infinity converges in each Schwartz seminorm. Flatness of all jets makes removal of a shrinking diagonal neighborhood converge in each seminorm by Taylor expansion of arbitrary order. The remainder has compact off-diagonal support and finite product-box Fourier approximations convergent with every derivative and fixed compact support. A diagonal sequence gives Schwartz density. Two continuous extensions agreeing on this dense subspace agree everywhere. This proves flat-space uniqueness. |
| 271 | A smooth function supported in nonnegative times has all jets zero at a zero-time boundary. The same Taylor argument removes a thin boundary neighborhood; the expanded boxes can then remain strictly in positive time. This proves the extra positive-time density assertion used later. |
| 273, first three sentences | Approximate a fixed flat test by a finite separated tensor sum. The common (12) bounds the two approximation errors uniformly in $j$. Convergence on the tensor sum follows from Lemma 2 for moments, the self-centered moment identity for canonical moments, and the finite cumulant formula of Lemma 3 for cumulants. For moving tests add $A'_np_{20n}(\Phi_{j_r}-\Phi)\to0$. This delivers all convergence in line 208 on the same subsequence. The reference to Lemma 2 here is sufficient through the already-given Lemma 3 finite identities; no further extraction is required. |
| 273, last sentence | The two moment families are precisely all-state moment limits to which H1 applies. Their imported and constructed extensions have the same space, dense tensor values and Schwartz continuity. The detailed scope/uniqueness check is in step 3. This supplies exactly the factorial assertion in line 208. |

Assertion-to-proof map: off-diagonal distribution and local order, 219–238; flat extension and uniform per-order bound, 240–267; uniqueness, 269; fixed and moving-test convergence, 273; moment-limit factorial bound, 273 with I3/H1. First failing step: none found.

## Step 3 — The two factorial sentences and uniqueness

The statement sentence (`cl1.md:208`) is:

> For the limit forms of the moments $\sigma_n$ and $(\sigma_S)_n$, I3 improves $A'_n$ to $C_E^n(n!)^{k+32}$.

It gives the flat-space factorial estimate to $\sigma_n$ and $(\sigma_S)_n$, for every $n\ge1$, and to no other forms. The immediately following sentence expressly excludes cumulant limits $S_n$ and lattice forms $\Sigma_{j,n}$ from this claim.

The proof sentence (`cl1.md:273`) is:

> For $\sigma_n$ and $(\sigma_S)_n$, I3's quantitative extension agrees by uniqueness, so its factorial bound applies to these two limit forms.

This sentence refers to the factorial bound rather than printing its formula. Its scope is exactly the same two moment-limit families and orders as the statement. It does not assign this bound to the generic $\Sigma_n$ when that symbol denotes the cumulant extension, or to $\Sigma_{j,n}$.

### What the sources actually supply

I3 introduces its separated-tuple estimates at `cl1.md:63`:

> At all chosen data, for any two periodic states and every separated real tuple of type $(d,R)$, import the one-point comparison, higher cumulant bounds, and

The relevant inequalities at `cl1.md:67–71` are

$$
|m_{j,n}(\mathbf f)|\le B(R)^n(n!)^k\max\{1,d^{-5n}\}\prod_i\|f_i\|_\sharp,
$$

$$
|\kappa_n^{\rho_j}(\mathcal O(f_1),\ldots,\mathcal O(f_n))|
\le[2B(R)]^n(n!)^k\max\{1,d^{-5n}\}\prod_i\|f_i\|_\sharp\quad(n\ge2).
$$

These are separated-tuple estimates, not assertions of the $p_{20n}$ bound for flat-space lattice or cumulant extensions. The extension passage at `cl1.md:74` reads:

> Here $B(R)=C(R+1)^4$, $k=\lceil p\rceil+5$ for SR1's cell-loss exponent $p$, and all constants are independent of cutoff, states and positions. For $n=1$, take $d=1$. Complexification enlarges $B$ by at most two. SR1's H1 implication gives the unique diagonal-flat extension with bound $C_E^n(n!)^{k+32}p_{20n}$ and constrained smooth-tensor density. The per-order extension needed to identify the Hilbert spaces is proved again in Lemma 4; factorial accounting is imported from SR1. SR1 itself retains UV1's full D1 with rooted geometry and LG1.

The words “SR1's H1 implication” retain H1's domain of applicability. They do not make H1 a theorem about every multilinear form satisfying the preceding separated estimate.

H1, `sr1.md:121–127`, says:

> **H1.** Every existing limit (7) extends uniquely from smooth separated tensors to $\mathcal S_{\ne,n}$, with
>
> $$|S_n(\varphi)|\le C_{\rm E}^n(n!)^{k+32}\sup_{|\alpha|\le20n,x}(1+|x|^2)^{10n}|\partial^\alpha\varphi(x)|.$$
>
> Finite sums of separated tensors are dense in this space. The positive-time version has strictly positive-time factors. Compact RP transfers to finite sequences in $\mathcal S_{\ne,+,n}$. The same constants apply to any component *realized by limits of the all-state moments (7)*; no component realization is proved here.

Its defining limit (7), `sr1.md:67–73`, is:

> **Limit and test spaces.** A separated limit is a family
>
> $$S_n(f_1,\ldots,f_n)=\lim_{j\to\infty}\rho_j\!\left(\prod_i\Phi_{K_j}^{\nu_j}(f_i)\right),\qquad K_j\to\infty,$$
>
> on every separated compact tuple, with $a^{(j)}=L^{-K_j}$, $\rho_j,\nu_j\in\mathcal G_{a^{(j)},\beta_j}$, and common source constants. Its existence is not asserted here. Set $S_0(1)=1$. Multilinearity is required only when all supports occurring in the identity remain separated; (7) has this property.

Here $\Phi_K^\nu(f)=\mathcal O_K(f)-\nu(\mathcal O_K(f))$ (`sr1.md:24`). Thus SR1's $S_n$ in H1 is a moment limit, not CL1's higher cumulant. H1 applies to CL1's $\sigma_n$ via its defining limit and Lemma 2. It applies to $(\sigma_S)_n$ by choosing $\nu_j=\rho_j$: `cl1.md:193–199` identifies those self-centered moment limits on the same subsequence. This identification follows also from Lemma 3 as given: the higher cumulants converge, self-centering makes singleton cumulants zero, and the finite partition formula gives (3). Both choices obey the same all-state hypotheses and use common source constants. Neither a single finite-$j$ form nor CL1's cumulant-limit family is asserted to be a limit of the moment form (7).

**Comparison for each sentence:** the statement sentence and the proof sentence each claim the **same** factorial bound as H1 on the two moment-limit families present in CL1. Viewed against H1's full universal quantification over all possible existing moment-limit families and realized components, each is a specialization, hence has less scope; neither claims more. Neither claims a stronger seminorm, exponent, constant uniformity or set of tests than H1.

### “Agrees by uniqueness”

For each fixed $n$ and each of these two families:

- The spaces are identical: CL1's $\mathcal S_{\Delta,n}$ consists of all Schwartz functions with all jets zero on the pair diagonals (`cl1.md:50`); SR1's $\mathcal S_{\ne,n}$ has exactly that definition (`sr1.md:75–80`). At $n=1$ the diagonal is empty in both, so this is the entire one-slot Schwartz space.
- The common subspace is the finite span of tensors of smooth compact factors with pairwise separated supports. Both extensions agree there with the same moment limit. CL1 proves its density at line 269; H1 also expressly supplies it at `sr1.md:127`.
- Both extensions are continuous for the inherited Schwartz topology. CL1 bounds its extension by $A'_np_{20n}$; H1 bounds its extension by $C_E^n(n!)^{k+32}p_{20n}$. The two seminorms are literally the same because $(20n)/2=10n$. Different numerical bounding constants do not prevent common continuity.

Consequently their difference is continuous and zero on a dense subspace, so it is zero everywhere. H1's factorial estimate transfers to the constructed moment-limit extensions. The positive-time spaces also agree: smoothness plus support in nonnegative times forces all boundary jets to vanish, matching SR1's condition at nonpositive times. No comparable uniqueness argument can import H1 for cumulants or fixed-cutoff lattice forms without first supplying an H1 extension for those forms; Lemma 4 does not claim to do that.

## Step 4 — Other factorial uses and the consumer

Before opening the complete change logs, I searched every line preceding the first change-log heading for `k+32`, `C_E`, `n!`, and then more broadly for factorial/growth wording and exclamation marks. I also read all later lemmas and Theorem 9, rather than relying on the absence of literal matches. The change-log matches are deferred to step 6.

| Location in `cl1.md` | Forms and role; whether Lemma 4 supplies it |
|---|---|
| 67–68 | $(n!)^k$ bounds the lattice centered moments $m_{j,n}$ on separated tuples, for all evaluating/centering state pairs. This is an I3 premise, not supplied by Lemma 4. Its self-centered case covers the canonical lattice moments. |
| 69–71 | $(n!)^k$ bounds the raw lattice cumulants on separated tuples for $n\ge2$. Again an I3 premise, not a Lemma 4 consequence. |
| 74 | The $C_E^n(n!)^{k+32}p_{20n}$ bound is the H1 implication for existing all-state moment limits. Lemma 4 supplies its application to $\sigma$ and $\sigma_S$ and identifies the imported extension with its construction. It does not supply this conclusion for lattice or cumulant forms. |
| 93 | $C_E$ is listed among fixed SR1 constants; no new bound or application is made. This is compatible with Lemma 4's fixed moment-growth constant. |
| 117, 127, 138, 144, 191, 199 | These references preserve or apply (4) to separated moment/cumulant limits, and to self-centered moments. They inherit the separated factorial estimates from the premises and finite limit identities, not from Lemma 4. At 127 the additional word “factorial” concerns the exponential/partition identity, not an extension estimate. |
| 187, 191 | $(|\pi|-1)!$ and $r!$ are exact combinatorial factors in the inverse moment–cumulant formula. They are not factorial-growth assertions for extended forms. |
| 208, 210, 273 | The moment-limit flat bound and its attribution already checked in steps 1–3. The scope exclusion in line 208 is explicit. |
| 212–217 | (4) is used to obtain the per-order (13) for all three lattice/limit families. The proof needs polynomial dependence on separation, uniformity in $j$ and positions, and a finite constant at each $n$. It does not use a bound on the growth of that constant with $n$. |
| 302 | Lemma 5 applies (4) to translated separated moment correlations for $\varphi=\sigma$ or $\sigma_S$, in a fixed finite vector $F$. It needs uniformity in translation, not a factorial growth rate. No cumulant or flat lattice factorial estimate is used. |
| 392 | $N!$ occurs in the Gamma-function product limit, with $N$ a scalar approximation parameter. This is not a bound for any moment, cumulant or lattice form and does not use Lemma 4. |
| 495 | The source-check table attributes the graded factorial implication to SR1. Lemma 4 realizes precisely its moment-limit use; the table makes no further form-specific claim. |
| 500 | A negative source statement: CA-II does not supply the factorial bound. It asserts no bound and is consistent with Lemma 4's import attribution. |
| 526 | The result notes retain factorial growth as an SR1 import and identify the compact and flat spaces only for the same scalar moment functional. Lemma 4 supplies that restricted moment extension; no cumulant/lattice growth claim is made. |

The full downstream dependency check is:

- **Lemma 5, 275–324:** moment positivity, separated-tuple fixed-order estimates, continuity and the compact-tuple construction. No extended cumulant/lattice factorial bound.
- **Lemma 6, 326–360:** finite positive-time flat sequences of moment forms. Line 343 expressly uses (12) with the tensor seminorm estimate (20); a finite sum of fixed-order constants suffices. Density and agreement of forms provide the unitary identification. No summation over arbitrarily high orders calls for factorial control.
- **Lemma 7, 362–414:** a measure/functional-calculus argument with no such form-growth hypothesis.
- **Lemma 8, 416–453:** the compact moment Hilbert space, Lemmas 5 and 7, then Lemma 6 to transfer the result. No such factorial hypothesis.
- **Theorem 9(1), 459 and 468–485:** compactness and fixed-order moving-test limits use Lemmas 1–3 and the separated bounds. The finite-torus recognition chooses finitely many cumulants at each $j$ and uses the explicitly chosen error in (29). It needs neither factorial growth in cumulant order nor a factorial bound on flat lattice forms.
- **Theorem 9(2), 460 and 468:** cumulant regularity is the off-diagonal, locally finite-order assertion of Lemma 4. The symmetry/positivity assertions come from Lemma 3. No cumulant flat-space factorial estimate occurs.
- **Theorem 9(3), 461–463:** Lemmas 5–6 supply the Hilbert spaces and identification using finite sequences and the per-order bound (12).
- **Theorem 9(4), 464:** the cone uses Lemma 8 and that identification.

Thus **no clause of Theorem 9 and no lemma after Lemma 4 needs $C_E^n(n!)^{k+32}p_{20n}$ for CL1's cumulant limits $S_n$ or lattice forms $\Sigma_{j,n}$**. There are inherited separated-tuple inequalities containing factorials, notably (4); their occurrence must not be confused with a need for factorial growth control of the flat extensions. The later arguments consume only their fixed-order consequences. Lemma 4 supplies every extension/continuity/density property those consumers use.

## Step 5 — Symbols with different meanings

1. **$S_n$ is the decisive collision.** In `cl1.md:41,43–48,186–191`, $S_n$ denotes higher connected cumulants ($n\ge2$). In `sr1.md:69–73,121–127`, it denotes centered *moments* in the all-state limit (7), also admitting $n=0,1$. SR1's H1 $S_n$ becomes CL1's $\sigma_n$ for the original state pair, or $(\sigma_S)_n$ for the self-centered pair. Reading the same glyph as a cumulant in H1 would falsely add precisely the factorial claim excluded by `cl1.md:208`.
2. **$\Phi$ changes role.** SR1's $\Phi_K^\nu(f)$ (`sr1.md:24,70`) is a centered lattice observable. CL1's $\Phi$ in (12) (`cl1.md:205`) is a diagonal-flat Schwartz test; its centered observable is $Z_j(f)$ (`cl1.md:37`). H1's $\varphi$ is the Schwartz test. The limit (7) must be read with this translation of notation.
3. **$c$ is not one common constant.** CL1's $c$ in Lemma 3 is the real one-point density (`cl1.md:144,179–182`); its constant-order table separately uses $c=C_vc_r$ (`cl1.md:88`). SR1 also uses unspecified positive decay/constants $c$ (`sr1.md:61,105`). In the self-centering identity needed for step 3, $c$ means only the one-point density, which can vanish and need not be a positive reserve/decay parameter. No equality of these constants is used.
4. **$C_E$ in the two factorial displays has the same meaning.** CL1's $C_E$ and SR1's $C_{\rm E}$ are the H1 growth constant, chosen after the source package and before $n$ and tests (`cl1.md:74,93`; `sr1.md:105,123`). The excerpts read do not independently identify an IN1 row-7 constant named $C_E$: the local tables abbreviate that row. Therefore an alleged collision with that external constant cannot be independently checked from these tables alone. It has no role in the estimates read here.

There is also a change of names without a change of space: $\mathcal S_{\Delta,n}$ in CL1 is $\mathcal S_{\ne,n}$ in SR1. The glyph $\Sigma_n$ in Lemma 4 is generic for the selected family, not an assertion that moments and cumulants coincide. These distinctions prevent an erroneous transfer of H1 to all the families in (12).

Steps 1–5 are complete. Their mathematical finding is that the lemma's written assertions close under the stated premises. The earlier accidental exposure of two change-log items remains the procedural limitation recorded at the start.

## Step 6 — Change logs, item by item

I now read both complete change logs, `cl1.md:530–542`. Their factorial search matches are lines 533, 534 and 538; these add historical/scope commentary, not a new bound used by a consumer. To check the first log's specific statement about SR1's proof machinery, I additionally read `sr1.md:333–480` (Lemmas 7–9), after completing steps 1–5. I did not re-prove the assumed Theorem 1.

### Pass 3 log, 2026-11-05

- **Introductory claim, line 532:** the assertion that a gate's findings were applied, and the attribution “first failing step none,” are historical/procedural reports. I did not read that gate and do not use its verdict as evidence. The next log expressly says its item 1 was only now applied in the text, so the older “Applied” cannot by itself establish when the two sentences were corrected.
- **Item 1, line 533, scope criticism:** this correctly describes why an unrestricted upgrade of all the forms in (12) would overstate the imported H1 statement. It does **not** describe a present failure in the hash-verified Lemma 4: lines 208 and 273 now expressly restrict the upgrade to the two moment-limit forms. The first log must be read as the old finding, not as a literal quotation of the current sentence's full scope. Its identification of H1's coverage agrees with step 3.
- **Item 1, line 533, Theorem 9:** “No clause of Theorem 9 uses that bound” agrees with the consumer analysis in step 4. Fixed-order estimates suffice throughout; in particular, no factorial estimate on cumulant/lattice flat extensions is needed.
- **Item 1, line 533, SR1 Lemmas 7–9:** the supplementary read confirms that (28), `sr1.md:337–343`, is the separated unit-radius estimate with $b_0^n(n!)^k\max(1,d^{-5n})$, and the analytic construction in Lemmas 8–9 consumes that estimate and the multilinear/tensor structure. Saying “only the bound (28)” is accurate as to the quantitative input, not a replacement for that structure. CL1's cumulants meet this quantitative input by (4), after absorbing the factor two into $b_0$; lattice moments and cumulants meet it uniformly at their data as well. This supports applicability of the analytic method, but H1 as **stated** still quantifies over limits (7). Nor does it identify an enlarged cumulant growth constant with the very same numerical moment constant. The current Lemma 4 does not need or claim such an additional quantitative conclusion. The cited SA passage was not read; its historical/source attribution is unverified here.
- **Item 2, line 534:** the proposed names $C_{H1}$ and $c_\sigma$ agree with the roles found in step 5. The distinction between the one-point $c$ and the reserve product $C_vc_r$ is directly visible in CL1. The further claim that IN1's row 7 has its own $C_E$ is not independently verified, because IN1 was not read and the local abbreviated table does not display it. No argument in Lemma 4 equates the H1 constant with an IN1 reserve constant, so that unverified nomenclature claim creates no missing premise for this read.

### Log of 2026-11-13

- **“Item 1 ... is now applied,” line 538:** agrees with the current text in the specific, checkable sense that both formerly criticized locations restrict the factorial bound to moment limits.
- **Earlier wording and PR #10141 hold, line 538:** neither the earlier snapshot nor the PR/review history was consulted. The claim that those earlier sentences covered every form of (12), and the reported 2026-11-11 hold, therefore remain unverified historical claims. They are not evidence against the current lemma and were not needed to decide it.
- **“Both sentences now give the bound ... only,” line 538:** agrees exactly with steps 1–3.
- **“No factorial bound is stated for ... $S_n$ or ... $\Sigma_{j,n}$,” line 538:** agrees when read in its immediate context as the flat-space $C_E^n(n!)^{k+32}p_{20n}$ bound in Lemma 4. Read literally as a denial of *every* factorial-containing bound anywhere in the file, it would be false: (4) expressly supplies separated-tuple factorial estimates for lattice moments and cumulants, inherited by their limits. Step 4 distinguishes those estimates.
- **“No other line ... is changed,” line 538:** not verifiable from one snapshot; no historical diff was inspected.
- **Edit credit and linked reader record, line 540:** authorship and the linked record outside the current folder were not verified. This report is the requested current-folder `./cl1-l4-read.md`, not the linked `../gates/cl1-l4-read.md`.
- **Frozen status and reopening rule, line 542:** these are project status/procedure statements, not mathematical deductions. My finding is compatible with the stated conditional implication and supplies no `wrong` signal for Lemma 4. I do not independently certify the whole file, its imports' actual construction, or landing/frozen status.

## Verdict and scope of this read

**Right.** Taking exactly the stipulated premises, the off-diagonal construction, common per-order flat extension, density/uniqueness and convergence close for all the stated families. The stronger flat-space factorial bound closes for the two moment-limit families through H1 and the checked uniqueness argument. No stronger bound for cumulant or lattice extensions is asserted or required by the identified consumers.

This mathematical verdict does not erase the procedural error: two entries of the first change log were accidentally exposed by the initial search before steps 1–5, so this run is not a fully blind read in the requested order. The report preserves that limitation rather than claiming compliance. No network access or git commands were used. Only `cl1-l4-read.md` was written; neither source file was edited. The exact runtime model identifier and reasoning-effort setting were not exposed, so the reader field records them as undisclosed rather than guessing.

verdict: right
first failing step: none
read: cl1.md:1–542; sr1.md:1–129,333–480; heading/anchor search hits in sr1.md through line 566
not read: remaining sr1.md text except those search hits; cited external files, prior revisions, PR and gate records
reader: openai/undisclosed/undisclosed
