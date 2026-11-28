Provenance: Codex (gpt-6-astra), xhigh effort, checkout `cf66777798bb8a5e2d731a66bbd9569cf0fe03f0`; one research-text check of FINISH row 393, not an audit. No status is granted.

# Check of B99 Lemma W

## 1. Scope and prior work

`library/prior/b99w-gate.md` is absent. I read `library/prior/b99-w.md` first, then the source notes. The registry assigns B99-W to `b99-w`. CO belongs to `ol` and asks for the account's successive assignment. This check does not attack CO or rebuild the cited flat machinery.

Credit Tadeusz Balaban for the comb averages, nests and propagator construction. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`. Credit Claude (Mini worker, FINISH row 377) for `b99-w.md`, and Claude for the repaired `h-walk` construction. Source locations below use the pinned checkout and the account's original line numbers. The source lookup used `library/sa-index/` (README, neighbouring chunk rows and obligations), including its CA 4.12–4.19 index, followed by bounded source excerpts.

The target is `b99.md:2216–2267`, (84)–(85), clauses 1–4. It concerns the true-current precision, bilinear transposes, complete local reads, and constants fixed before the later expansion size M. A real inverse bound alone is not this statement. No numerical or computer-assisted proof is used.

## 2. The four input checks in §0.5

These verdicts concern the portions used by W, with their stated supplier premises retained.

| Input | Verdict | Checked step |
|---|---|---|
| B13 (47), `b99.md:1344–1484` | ADVANCE | The two longitudinal responses of (49) are respectively (1,0) and (0,1). The small-n determinant is −n⁻⁹. The seeds have bounded overlap and the stated energy cost. H10's carrier convention leaves only the same and adjacent level blocks. Their normalized Schur bounds give L⁻¹ plus the curved error. Thus E=E⁰(QE⁰)⁻¹ has (47). No use of (48) is needed. |
| B11 (41), (44), `b99.md:1224–1310` | ADVANCE | The fixed-leg column bound and summed-leg row bound in (43) give mᵣ⁻³nᵣ⁻². The geometric sum, multiplied by η²/s, gives s(η/s)⁴. Physical row weights and adjacent carrier overlap give (44). The factor two in the quadratic coefficient is accounted for. |
| B15 (63), `b99.md:1651–1682` | ADVANCE | Opposite plaquettes cancel the constant-link quadratic term. The stencil variation and cubic remainder give the displayed first inequality. The actual curl-divergence bound in (3.36) supplies the linear term. The restriction to complete interior stencils is essential; boundary values require the separate boundary premise. |
| H16, `b102.md:2153–2249` | ADVANCE from (H16.1) | Cauchy differentiation of a density-bounded kernel entry yields (H16.2), including its difference estimate. The physical/counting conversion in (H16.3) and bounded carrier overlap yield (H16.4). The final lift statement keeps its named lift bounds. This does not replace (H16.1) by a value-only estimate. |

The outline's PX151–PX156 (SA 11612–11656) contains the second-jet and nonflat-lift argument. Its mechanisms (f)–(h), SA 10533–10550, sketch unfolding and tree assembly. CA-I 47295–47324 imports elementary Balaban sheets. Those citations are not independent proofs of W for the matched comb system. `b102-gate-a.md` covers H9–H12 as implications from their suppliers; it does not check H16.

## 3. Operator and unfolded system: §§1–3

| Step in `b99-w.md` | Verdict | Reason |
|---|---|---|
| (1.1), lines 73–91 | ADVANCE | CA-II 8424–8430, 9086–9101, 9776–9810 and 10050–10088 give the stated precision and pivot map. The two averaging constraints are distinct; the note uses C_flat for Q_flat and the comb Q inside QG₁Q*. Both current corrections remain present. |
| N5, N6, lines 158–159 | ADVANCE as inputs | CA-II 9104–9290 supplies the relative exponential-gauge identities and real finite-range bounds. Its (HD), 9756–9782, remains a hypothesis. Complex coefficient and pivot bounds require the named analytic version: CA-I 46952–47063, with its radius and admission premises in 47187–47231. Covariance remains cited. |
| Lemma 3.1, lines 179–201 | ADVANCE | The BCH mixed term has the printed sign. Differentiating gauge invariance gives ΔᴾD=𝒞[J] (Δᴾ denotes the Wilson Hessian here). Symmetry supplies the stated operator identity. There is no missing η in the mixed bracket. |
| (3.2), (3.3), lines 203–215 | ADVANCE | Polarization gives the Ward correction with both cross terms and the quadratic gauge term. The m³ current norm pairs m⁻¹B with m⁻²λ. No derivative of J is used. For independent J this defines the continuation; it is not a Ward identity at that pair. |
| Lemma 3.2, lines 217–234 | ADVANCE on complete current stencils | B15 (63) handles interior real stencils. The retained boundary-plaquette bound handles bare boundary stencils, where m=η. For the complex increment, (3.38) controls the linear curl-divergence term; H12.3 controls the curvature remainder. The quadratic plaquette remainder has the stated α₁²m⁻³ scale. No bound on every individual second difference is substituted. |
| (3.5), lines 236–254 | ADVANCE | The mixed term is polarized with one half in each off-diagonal block. Every coefficient is local in the layer metric. The λ norm includes its scalar graph term; the h norm is L², as in the referenced definition. |
| Lemma 3.3, lines 256–279 | ADVANCE | Scalar elimination gives L=G′RD*. Substitution yields the displayed T. The multiplier block is −W⁻¹; the field–multiplier block is +T⁻¹Q*W⁻¹. Stage 1 uses H*J, and the final precision uses H₁*J. Neither is silently substituted for the other. |

The normalization reconstruction at `b99.md:1790–1797` is retained. A wrong factor would change the identified operator, not merely an estimate's constant. The claim at `b99-w.md:693–696` that such a factor could only change constants should therefore be deleted. No such factor error was found in the formulas checked here.

## 4. Local inverses: §4

### 4.1 Geometry and local class

**ADVANCE:** lines 283–308 and Lemma 4.0. The divisibility M′ | M_w | M₁ preserves the layer tiling. The repaired midpoint range is 16L. Subtracting the same constant from the partition sum proves both difference bounds for ψ_z. This fixes the nonsmooth exponential problem in the earlier graph-norm argument.

**REVISE:** the local class at lines 101–108, as used in Lemma 4.1. State its spatial domain relative to Ω₀. A footprint includes geometric collars outside Ω₀. The global hypotheses do not impose small gauges on every exterior cube in those collars. CA-I 45439–45481 likewise defines real backgrounds on Ω₀ and uses the intersection with Ω₀ for the enlarged read sets. Reading “every cube Q⊂F” literally beyond Ω₀ would make Lemma 4.1(a) false: alter an exterior plaquette away from all touching boundary stencils while leaving the admitted interior datum fixed.

**Written repair.** The field data on F consist of the original datum on its complete reads in Ω₀, together with every link of each touching boundary plaquette actually read. Apply the gauge and (3.37)–(3.38) tests on the regular-region cubes and complete stencils prescribed by the original class, restricted to F. Retain O's boundary-plaquette test on the original face. Impose no gauge test on unused exterior cubes. All required links and geometry are part of F; no exterior extension is chosen.

With this relative-domain convention, **ADVANCE** for Lemma 4.1(a)–(c), lines 310–335. A small cube meets at most adjacent layers. Its enclosing original class cube supplies the gauge, with a fixed L loss. The cut-down class cubes fit because 10M′≤c_gM_w, and lowering their scale weakens all three bounds. At an artificial face the plaquette is an interior read of the original datum; at an original face retain O's boundary assumption. Lemmas N and N2 identify the cutoff denominator and stage-2 coefficient reads. They do not assert a globally chosen gauge.

### 4.2 Global bound and complex perturbation

| Step of Lemma 4.2 | Verdict | Check |
|---|---|---|
| Step 1, lines 349–365 | ADVANCE with the physical scalar normalization | Scalar coercivity and scale conjugation control G′ into the graph space. Use the normalized scalar Gram: its raw lower bound is ‖G′Q′*μ‖₂≥c_L‖m²μ‖_top, not an unweighted mesh-independent bound on raw N. Thus N maps the m⁻² source norm to the m² target norm. H11's scalar model and its H12 assembly supply this on the admitted nests. The constrained minimum tested on Eb gives the W₀⁻¹ bound. |
| Step 2, lines 367–374 | ADVANCE | (3.3) and B11 (44) bound V_π and V₂ in E→E*. Two Neumann perturbations give T⁻¹ and W⁻¹. The estimates use arbitrary small J and j, which the local models need. |
| Step 3, lines 376–390 | REVISE the transport explanation; the bound survives | The hierarchical Q′ transport must be estimated at each averaging level. It cannot be justified by assigning the same fine-link increment to all its coarse factors. The replacement below gives the required C_Lα₁ bound. The difference, Wilson-form, Q and second-jet estimates use N1, N3 and N4 as stated. |
| Step 4, lines 392–395 | ADVANCE | The elimination formulas are finite compositions between the specified spaces. Invertibility throughout the fixed class gives holomorphy there. This is stronger than a separate, uncontrolled finite-volume neighbourhood. |

**Written transport repair.** On a row carrier of length s, put t_r=Lʳη/s. N4's complex averaging estimate bounds the change of a level-r link angle by C_Lα₁t_r. Each level contributes at most C_L contour factors. Telescope their ordered product against the real product. The norms of the unchanged real transports are one, and the perturbed partial products are bounded by exp(C_Lα₁Σ_rt_r). Since Σ_rt_r≤(1−L⁻¹)⁻¹, the whole transport changes by at most C_Lα₁. Multiply by the normalized pillar coefficients and use their row and column sums. This proves the Q′ and transpose estimates required in Step 3 without a depth factor.

### 4.3 Smooth-weight decay

**ADVANCE:** Lemma 4.3, lines 397–440, from the repaired Lemma 4.2. The four block types exhaust K_b. The third-order-looking mixed block is paired as [D,e^θ]A_sλ plus D[A_s,e^θ]λ; only the graph term and two differences of θ are needed. The averaging blocks use absolute coefficient sums, including B11's two-leg bound. The conjugation error is C_Kτ, so the inverse perturbation is at most one half. Smooth local multiplication then gives (4.2). No elliptic estimate at a re-entrant corner is being inferred.

This proves decay of the unfolded inverse. It does not prove accretivity of the mass-subtracted, pivot-compressed precision or of B17's local near matrices.

## 5. Port of the repaired walk argument: §5

The port is of the repaired construction, including `h-walk-fix.md` and its gate, not the original Lipschitz-weight argument. The following checks cover each row of §5's port table.

| Imported step | Verdict | Identification in this setting |
|---|---|---|
| C, C1–C4, N and N2 | ADVANCE after §4.1's repair | The tiling, overlap, cutoff-denominator reads and complete stage-2 supplier reads are geometric. Restrict the datum on those reads; do not select an extension or a global gauge. |
| D, P and S | ADVANCE using Lemmas 4.0 and 4.3 | The required inverse decay is now the smooth-weight graph-space estimate. Bounded overlap and the summation constant K_τ are uniform on these nests. The old claim that an arbitrary Lipschitz exponential preserves the graph estimate is unnecessary. |
| K | ADVANCE | Its commutators are precisely the four block types checked in §4.3. The comb rows use H10/H12; the second-jet block uses B11's absolute two-leg sums. |
| L | ADVANCE | Lemma 4.3 supplies the local inverse bound, on the full cut-down local class. |
| W(a), W(b) | ADVANCE | On the cutoff neighbourhood the local and original matrices agree. The artificial face is outside the retained stencil. The local coefficient current is the copied coefficient, not a current recomputed from a different truncated action. The local distance dominates the original distance where the proof needs that inequality. |
| W′, T′ and H′ | ADVANCE | Each factor carries its complete read, including the zero-length stage-1 supplier used in the second matrix. A parent box without that supplier would be insufficient; N2 provides the enlarged box used here. |
| J and T | ADVANCE with the repaired branch constants | Keep C_* raised to n+Σᵢmᵢ, rather than only n. For p=n−v+Σᵢmᵢ and q=n+Σᵢ(mᵢ+1), 3p−q=2(n−v)+2Σᵢ(mᵢ−1)≥0. The resulting factor is (C_T M_w⁻¹ᐟ³)^q, with at most C₀C₁^q labels per root. |
| H | ADVANCE from N5 and cited covariance | The level-k contour and pivot maps read finitely many neighbouring level-k bonds. Their complete fine-data suppliers must accompany those bonds. Conjugation covariance is preserved by the scalar cutoffs, contractions and local inverses. |

**ADVANCE** for §5's three subsequent points. The stage-1 transpose estimate has exactly the compensating factors s³ (current norm), s⁻⁴ (physical row pairing), and s (dual norm of the unnormalised row source). Their product is one. Thus the local zero-length coefficient is bounded by C₀γ_V. Choosing the current ceiling below the local inverse ceiling admits both matrices. Their block outputs are respectively H, H₁ and −(QG₁Q*)⁻¹; the final vertex uses H₁*J. This is the two-stage system of Lemma 3.3, not a single resummed propagator.

All branch reads remain in the labelled enlarged boxes. The proof of (5.1) therefore provides an intrinsic analytic family with exponential tree decay, not merely an estimate on its total. Datum-independent constants require the uniform ceiling specified below. No new flat-model proof is needed.

## 6. Assembly of (84)–(85): §6

### 6.1 The three families and exact sum

**ADVANCE:** (6.1), with the geometric read convention below. The local term is C_flatᵀ(G−a)C_flat, partitioned by the cutoffs. The Gram term is the negative active multiplier block of the second inverse, compressed by C_flat. The final family is −C_flatᵀD[j₁,ω]C_flat. Linearity of D in its current permits termwise substitution of the absolutely summable j₁ family. Re-root this last family at its coefficient row. These three sums give (84) exactly, including its signs and both multiplier currents.

**ADVANCE:** the complete-read and connectedness argument. Every path vertex carries its cut-down inverse, all normalised-cutoff reads and the stage-1 suppliers in its coefficient. Consecutive enlarged boxes overlap; the branches meet their parent boxes. Adding the fixed contour/pivot reads preserves connected interior. These are the domains of the terms, rather than supports of a numerically evaluated coefficient.

For literal constants, let R_loc≥4L be a fixed upper bound for every N5 stencil radius, including the final D vertex and C_flat, plus one unit. Use Dom_κ=κ^sharp+R_loc if the printed +4L does not already contain this radius. A conservative diameter bound is ρ_W=40L²M_w+8R_loc in the current-unit ℓ¹ metric. This harmless enlargement is chosen before M and preserves every overlap and read assertion. It avoids inferring a numerical stencil radius from an unspecified C_{L,N}.

### 6.2 Datum-independent majorants and endpoint counting

**REVISE the constant assignment:** make the uniform current ceiling in (6.3)–(6.7) explicit. This does not change the expansion.

First choose a fixed Γ within the admitted coefficient-current ball, and impose γ_V≤Γ when choosing a_W. Replace every γ_V in the majorant constant by Γ. In particular use

\[
 \overline C_A=C_L(B_1+C_D C_J\Gamma+1).
\]

This is independent of the datum and remains affine in C_D. The printed γ_V=C_L(ε+α₁) is already a uniform bound for a fixed regularity class, not the measured current of one datum. The point of replacing it by Γ is to make B_W uniform over the later choices of regularity radii, as the theorem requires.

**ADVANCE the endpoint count:** (6.4)'s reference to the support condition of clause 2 must retain the detailed endpoint supports at lines 519–526, not merely the margin condition in W's statement. That paragraph already supplies the stronger supports. Explicitly, the indicator can be written using the following sets.

* For a Gram term, let L_ω be the fixed stencil enlargement of the root output cutoff support and R_ω the corresponding enlargement of the terminal source cutoff support.
* For a final-current term, both sets are the fixed stencil enlargement of its coefficient-row cutoff support, after the stated re-rooting.
* For a local term, use the root cutoff support and its fixed G/C_flat stencil enlargement; a common fixed enlargement of the root box is also sufficient.

These are geometric sets of free level-k bonds, independent of field values. At a fixed b there are at most ν_L possible root boxes with b∈L_ω. Each R_ω contains at most C_LM_w⁴ bonds. For the column bound use terminal rooting for the Gram terms and the same coefficient rooting for the current terms. The reversed rooted tree count has the same C₀C₁^q bound. Mere support in the union of all visited boxes would not justify these assertions.

Let D_ω(b,b′) be the shortest current-unit ℓ¹ tree meeting the endpoints and every labelled enlarged domain. The metric conversion used in §6 gives

\[
 D_\omega(b,b')\le 2d_B(\omega;b,b')+C_L(q+2).
\]

Consequently the following is a fixed replacement for (6.4), after enlarging its geometric constants:

\[
 a_\omega(b,b')=\overline C_A e^{C_L\tau}
   \bigl(C_Te^{C_L\tau}M_w^{-1/3}\bigr)^q
   e^{-\tau D_\omega(b,b')/16}
   {\bf1}_{b\in L_\omega,\ b'\in R_\omega}.
\]

This is (6.4) with its detailed support indicator made explicit and its constant uniformised. It uses the current-unit footprint metric required by W. With δ_W=τ/32, the weighted row and column sums are bounded by

\[
 C_LM_w^4\overline C_Ae^{C_L\tau}C_0
 \sum_{q\ge0}
 \bigl(C_1C_Te^{C_L\tau}M_w^{-1/3}\bigr)^q.
\]

Choose M_w so the ratio is at most one half. Absorb the finitely many family types into C₀ and take twice the displayed prefactor as B_W. The count is correct with these endpoint supports; it does not infer absolute summability from a bound on the resummed operator.

### 6.3 Verdict on each clause

| Lemma W clause | Verdict | What has been checked |
|---|---|---|
| 1: domains, size and order of constants | ADVANCE with the explicit stencil enlargement | The complete domains have connected interior and the early bound ρ_W above. M_w is an auxiliary size fixed before the later M. |
| 2: endpoint support | ADVANCE | The actual cutoff/pivot/vertex supports lie inside their recorded domains with the required margin. The stronger endpoint sets above are retained for clause 4. |
| 3: intrinsic analytic local dependence | ADVANCE after the relative-domain repair | Every inverse is admitted by §4 on the local datum alone; the analytic map bounds retain their supplier premises. All factors and their normalisation denominators use complete recorded reads. Equal admitted local data and geometry give equal terms and equal majorants, with no global extension. |
| 4: fixed exponential majorants, both sums | ADVANCE after the written majorant repair | The uniform ceiling, endpoint rooting, tree metric conversion and geometric series prove (85) with fixed B_W and δ_W. Covariance follows from the cited covariance of the factors. |

## 7. Constants and claimed scope: §§7–8 and Result

**ADVANCE** for the floor, divisibility and smooth-weight choices in §7. Fix the N1–N6 supplier floors and local inverse bounds first. Obtain C_K and τ from that admitted class. Raising ρ′ to meet the scale-conjugation/decay condition subsequently restricts the class, so the old constants remain valid; they need not be recomputed in a circular order. The M_w floor then handles the repaired branch count, the cut-down gauge cubes and the fixed stencil enlargement. M_w divides the later M₁. None of this fixes the later expansion parameter M.

**REVISE** the explicit assignment of B_W before a_W as follows. Choose an early positive Γ with C₀Γ≤γ_g and Γ≤a_T. Use Γ in the majorants of §6. Fix M_w, ρ_W, δ_W and B_W. Last choose a_W small enough that

\[
 C_L(M_1\alpha_0+\alpha_1)\le a_g,\qquad
 C_L\{C_L(M_1\alpha_0+\alpha_1)+\alpha_1\}\le\Gamma,
\]

and that O's boundary and N4's analytic-radius ceilings hold. This is possible uniformly because the theorem bounds both M₁α₀ and α₁ by a_W. The later choice of the primed radius can enforce it. This completes the promised constant order and preserves the asserted affine dependence of B_W on C_D. No finer-mesh absolute sum enters this choice.

**ADVANCE** for §8's distinction from the earlier failed arguments. The inverse estimate uses the graph norm and smooth weights. Only walk labels, not all fine sites of a kernel, are counted absolutely. Complete supplier reads are retained. These are the specific reasons the old graph-norm, omitted-read and mesh-counting objections do not reappear.

**ADVANCE, with its stated scope,** for the free-current algebraic observation. `ol.md` §11.2, especially (11.3a), identifies the signed quadratic forms for independent J and distinguishes H*J from H₁*J. Its §11.3 also identifies the relative contour gauge term, which must not be replaced by an absolute soft-gauge Hessian. That existing unfolded version is not a proof of the present statement on every admitted curved nest or a transfer to the account's successive sheets. No work on that separately owned transfer is undertaken here.

**REVISE** the self-check at lines 693–696: delete the claim that a normalisation error could only change constants, as explained in §3 above. Keep the supplier qualifications in the Result. “N1–N6” includes the cited covariance, the account's analytic map admission, H16.1 and (HD); this check has not proved those assumptions from a smaller premise set.

**BLOCK the further inference** at lines 675–676 if read as saying that W plus B17's local accretivity already supplies all the conditioned and switched families in `5.2:lem-random-walk-bounds`. B17 is an inverse/root construction from a suitable local precision family. It does not, just by being applied to (84), identify the account's assigned families on its independent-current spaces, their switches or their reference restrictions. The missing implication is identified below; no counterexample to W is asserted.

The conditioned inverse/root operation itself is already covered by B17 for every allowed Y, conditional on its displayed global and local accretivity hypotheses. It is not a new proof obligation to rebuild that operation. The unresolved work is to supply those hypotheses and the larger account domain and switch structure.

## 8. What remains open, and what CM actually needs

The account distinguishes the family from its sum. CA-II 2181–2277, item (b3), specifies analytic operators A, C_Λ, C_Λ^{1/2} and C_I on its local independent-(U,J) data spaces and for switches |s_Δ|≤e^{κ₁}. It also specifies their reference restrictions and component locality. `5.2:lem-random-walk-bounds`, CA-II 8922–8988, concerns those assigned families, with its domain/separation and M floors. Its proof imports the Balaban propagator estimate; it is not a proof there of the missing supplier construction. The subsequent use at CA-II 10104–10124 and 10178–10188 returns to those switches.

| Open item | Needed for CM via `5.2:lem-random-walk-bounds`? | Exact boundary of this check |
|---|---|---|
| B17's uniform local accretivity | Yes for the proposed W→B17 supplier route. It is not a separately named premise when the account's full (b3) is taken as an input. | Each local near precision must have the required lower bound throughout its admitted complex class. Bounds on the unfolded saddle inverse do not imply this for the final mass-subtracted precision. Global positivity also does not supply it on local data that need not extend globally. W does not discharge this input. |
| The account's successive sheet assignment | Verbatim equality of sheet labels is not intrinsically needed for the numerical CM tail bound. Identification with the assigned family, or a complete replacement satisfying the same consumer hypotheses, is needed to invoke that bound for a chosen family. | Equality of the resummed precision at s=1 does not identify the switched families. The specific assignment-transfer problem is owned by CO/`ol`; it remains untouched. W establishes an existential unfolded family only. |
| Conditioned covariance and root families, independent currents, and switches | Yes. These are part of the family and analytic-domain requirements of (b3) and hence of this route to CM. | W's theorem is on the true-current graph. B17 supplies conditioning and inverse/root families there once its accretivity hypotheses hold. The additional work is the independent-current domain, the switch polydisc, the prescribed component/reference restrictions and the identification with the consumer's family. In particular, W alone does not license a Cauchy derivative in J at fixed U. |
| CM's old-term determining-set/domain identification | Yes for the full CM consumer statement, beyond a conditional estimate on admitted (b3) data. | `gates/cm-gate.md` already records this as O3. CA-II 59540–59610 invokes membership of the new determining spaces and the companion local bounds. This is existing, separately owned work; W alone does not repair it. |

In particular, replacing an assigned family by any family with the same total is invalid: a cancelling pair of contributions can have zero sum at s=1 and nonzero sum after different switches are applied. This is the precise reason a total-operator identity does not discharge the switch obligation.

For an actually admitted conditioned/root family with an early exponential rate r>0, the elementary tail estimate used by CM can spend decay at a smaller rate, for example min(μ₀,r). The later M must meet the corresponding rM≥2κ₁ floor as well as the other printed floors. W's early constants are compatible with such an order. They do not prove that this family exists, that its rate is the account's printed rate, or that its data lie in the required spaces.

## 9. Overall verdict

**REVISE the note; ADVANCE the repaired conditional Lemma W, clauses 1–4.** The four specifically requested input checks pass under their retained supplier premises. The Ward normalisation, two Schur stages, smooth graph-space inverse estimate, branch count and endpoint count are correct. The written changes specify the relative local class, justify the hierarchical transport estimate, make the stencil diameter and early uniform constants explicit, and narrow the downstream claim. There is no identified counterexample to the resulting W implication.

This is a research-text conclusion only. B17's local accretivity, assignment compatibility and the conditioned/switch-family obligations remain open; CM is not closed by this check. No source note, registry row, audit record or scientific status is changed.

Checked line by line by Codex (gpt-6-astra).
