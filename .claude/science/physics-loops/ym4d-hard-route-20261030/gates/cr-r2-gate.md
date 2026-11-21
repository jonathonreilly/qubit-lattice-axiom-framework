Codex (gpt-6-astra); effort not specified in the task; checkout `5160385d105de58f661891bf7264e690b03c8964`; research-text check, not an audit, granting no status.

# CR, second round: line-by-line check

## 1. Sources and scope

This checks FINISH row 398, `library/cr-r2.md`, after reading `gates/cr-gate.md`. “Note” means the second-round note's lines. Its Git blob is `e70aea6ac016af0bc483232513100c776945e2d6`; the previous gate's is `3d253dccaa548ab7180c5c46c56950cc8aad60b6`. CA-I and SA refer to the supplied account and outline at revision `31a47c543775`. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban.

`library/prior/cr-r2-gate.md` does not exist. The registry assigns CR to `cr-claude`, still OPEN; this is its requested second-round check. No competing owner's lemma is attacked. The generic `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent from this checkout. The task's specific instructions govern. The full-read index, neighbouring rows and relevant obligations were used for source navigation. Previously accepted calculations are confirmed with their premises, not re-proved.

Balaban's papers are unavailable within the permitted source scope. Their quotations here are checked against the account and repository notes where available; no claim of independent PDF verification is made. No computation discharges a mathematical step.

The target is CA-I 45085–45106: conclusions **(a) and (b)**, including both cases of (b), for each actual outside pair. Clause (c) and the real-factor corollary are separate. The note's conditional theorem deliberately adds readings and source properties to the target's printed hypotheses.

## 2. First check: the uniform circuit bound

**Note 16–26, source identification: REVISE to an open identification.** CA-I 42980–42984 defines an elementary closed circuit but does not identify its cells. CA-I 43013–43016 composes averages at interfaces; 43113–43127 imports the data test in that graph's terms. Four-factor squares on Balaban's homogeneous lattices do not by themselves identify the graph circuits after interface composition. Retain (EC) as an additional, unverified reading of those exact plaquettes. The quoted homogeneous-square examples support that reading but do not prove it.

**Lemma 2.1, note 28–32: ADVANCE.** The flat cut configuration on a chordless block ring has trivial fine plaquettes and nontrivial coarse holonomy. Locality, normalization and covariance give the stated factors in their stated order. Thus AV(e) cannot hold on every simple graph cycle. This excludes the indiscriminate simple-cycle reading; it does not prove (EC), or exclude every contractible circuit without a common point. The claim about collars' topology is not needed for this example.

**(EC) and Lemma 2.2, note 36–46: ADVANCE conditionally.** The open-orthant injection is valid for axis-aligned cubes with disjoint interiors. It bounds the number of distinct blocks through one point by `2^d`, without a level, volume or tower dependence. Hence `n_P=16` for four dimensions under (EC). This is a written finite argument, not machine enumeration.

**Lemma 6′, note 50–56: ADVANCE under (EC), SRC, Lemma 5 and COMP.** Gauge factors telescope on the circuit; the unitary product difference costs at most the sum of the row defects. AV(e), `ell(P)<=ell_q`, and `F=C_F alpha_k` give exactly

\[
\varepsilon'_1=(2+2^d C_{\rm RD}C_F L^2)\alpha_k\ell_q^2.
\]

The two stated ceilings give T1 admission. The previous gate's constraint inclusion, restricted criticality and uniqueness argument then applies on the same action domain. No new flaw occurs in that argument. Replace “closed” by “the uniform bound is proved under (EC); identification of the source's plaquettes remains open.” Calling (EC) a reading rather than a consumer hypothesis does not discharge it.

## 3. R: geometry, coverage and radius

**Lemma 3.1 and Corollary 3.2, note 60–75: ADVANCE.** The sublevel union, superlevel intersection and distance inequality are correct. Extending the tower by `-1` includes the exterior in the lower set. The intersection of unions from the same big-block grid is again such a union. Truncation at `q` causes no problem for `j<q`; the top region retains cubicality.

**(G-c), note 68–71: REVISE the source claim.** The quoted width sentence is at **CA-I 43520–43524**, not 43454–43458. It supports widths of the named shells and collars. CA-I 37559–37565 also supplies the thin-shell width and the healed region. Neither passage proves that every restricted consumer superlevel set has the particular global big-block extension required by (G-c). CA-I 55632–55636 is a hypothesis about specified label members; it is not a universal cubicality assertion about these consumers. Retain the width and aligned-cubicality clauses of (G-c), separately, as source properties to be matched on every read domain. The outline's separated-sequence and localisation assertions (SA 9593–9599, 9776–9789) are indexed as definitions/sketches, not a completed proof of this matching.

**(G-t), note 69, 87, 220: REVISE to one explicit premise.** State that the actual tower has the advertised aligned superlevel cubes and widths, **and that `LM_1>w_adm` in the admissibility distance**. The floor `M>w_adm` cannot establish that second inequality. CA-I 43060–43064 only says that the determining-set hypothesis abstracts several constructions. It does not identify every actual tower with the particular CMP 119 tower. The note correctly lists that identification as open at 220.

**Proposition 4.1, note 79–93: ADVANCE as an implication after those qualifications.** Its antecedent must also retain SRC, AV(e), T1 and the smallness conditions, as its proof and Theorem 8′ do. Corollary 3.2 gives

\[
\operatorname{dist}((\Omega_j^{(q)})^c,\Omega_{j+1}^{(q)})
\ge\min(M,LM_1)\ell_j>w_{\rm adm}\ell_j.
\]

Use the same distance on both sides. The note defines widths in Euclidean distance, whereas SA 9596 and 10116 state separation in sup-distance. If that is the admissibility convention being imported, use `dist_infinity >= dist_2/sqrt(d)` and require **both** `M>sqrt(d) w_adm` and `LM_1>sqrt(d) w_adm`. Alternatively formulate (G-c) and (G-t) in the required distance from the outset. This norm choice must be included in the open tower/source matching; it cannot be changed silently.

**(R-form), note 85: REVISE the explanatory sentence, retain the identification as open.** Where `c_E<q`, the ladder level is `min(c_E,t)`, not necessarily `c_E`. Write: “The shell regions are truncated by the actual tower; assume that the resulting set, including its rows, interfaces and base conventions, is the stated `B_q(X'') union {Gamma_i}_{i<q}` system of R.” CA-I 43060–43064 does not prove this identification. With it, admissibility, and the regular real base supplied by T1, CA-I 10175–10204 supplies R uniformly. This checks the implication; it does not independently verify Balaban's five-member response formula.

**Fixed radius and derivatives, note 89–91: ADVANCE with the preceding coverage.** The fixed real-data class and closed half polydisc implement the previous gate's repair. CA-I 16567–16586 supplies the logarithmic radius and Landau representation; 14842–14866 supports the covariant derivative convention and distinguishes the independent-current replacement. The proof uses the real-base second-order member, not that replacement. The stencil scale is the one at CA-I 44271–44303. Keep the uniform reference-point/stencil constant among the constants of this identified response system.

## 4. ROW and the interface anchor

**Lemma 5.1, note 99–101: ADVANCE under Corollary 3.2 and `M_1>=2`.** The neighbouring coarse cube lies in a different big block across the face. One tangential coarse neighbour remains in the original big block. Its parallel small cubes stay outside the top region and within `ell_q` of it. The strict width bound excludes both lower levels and the exterior. This supplies the claimed chain, including either tangential sign and the endpoint `gamma_L`. It excludes the isolated-top-block counterexample from the previous gate by an explicit additional geometric premise.

**Lemma 5.2, note 103–107: ADVANCE.** The zero rows are rows of the actual set, their carriers avoid the support of the truncated one-form, and AV(d) uses one simultaneous gauge. P6 controls the two equal-level connecting rows. The previous factor calculation therefore gives the unchanged `C_b`. No ambient-partition ROW assertion is used here.

**Shared rows, note 109–111: ADVANCE under COMP(=) and (BP).** CA-I 44949–44953 expressly grants trivial composition where the sets coincide. On rows with both blocks unchanged, that is the equality needed for `B(c)=0`. The base points must agree. The notation `z_B` at CA-I 42968 alone does not prove this consistency across partitions; (BP) remains a reading. Thus broad ROW is removed, but its required common-row instance is retained explicitly within the account's COMP grant. Nothing here proves COMP.

## 5. SRC and the outside consumer classes

**Lemma 7.1, note 139–143: ADVANCE under (S).** CA-I 43225 and 43295–43299 give the claimed curvature bound on `Y_4 intersect (Z union Omega_k^old)`. All source plaquettes used in AV(e), the local carriers and `N` lie in `X''`; the one-step enlargement used for the *minimiser* bound is not an additional source read. The source condition is sufficient, as the corrected wording says.

**Note 145–155 and the coverage assertion at 191: REVISE.** A level function's listed values do not prove that every consumer domain is contained in the listed regions. Retain (S) for each actual pair, rather than infer it from the absence of another formula. Similarly, the table's shell names do not discharge either clause of (G-c).

| Class and step | Verdict | Exact coverage |
|---|---|---|
| K1, note 149 | ADVANCE | `c_E=j` and `p<=j` exclude the target's below-slot pair (CA-I 43350, 43361–43363). |
| K2, note 150 | ADVANCE conditionally | CA-I 43243–43245 puts `B_5` in `Z` and gives `o=k_0` there. If the entire read domain lies in this band, the ladder for `q>=k_0` is constant and `B=0`. For an entire cleaned-collar domain, retain its inclusion in the source-controlled region and its (G-c) properties. Localisation “on” a collar does not by itself locate every read carrier. |
| K3, note 151 | REVISE | `c_E=o` is specified at CA-I 43365. The required full-domain inclusion (S) and old-collar geometry remain source properties. |
| K4, note 152 | REVISE | `c_E=mathsf b` is specified at CA-I 43366. Meeting `Z''_k` and `Omega_k^old` does not imply containment in their union, or in `Y_4`. Retain (S), both clauses of (G-c), and the actual tower matching. |
| K5, note 153 | ADVANCE conditionally | It inherits the obligations of each constituent read, by CA-I 43367; it supplies no independent shortcut. |

The examples at CA-I 44995–45003 do not assert these inclusions for all classes. Therefore (S) proves SRC once supplied; the claimed all-consumer supply of (S) is still open. This is consistent with the note's own final open list, but not with dropping (G-c) from the premises at line 191.

## 6. SEP in the response metric

**Metric formula, note 115–117: ADVANCE as the quoted contour metric.** CA-I 152251–152265 prints precisely this weighted length, with the infimum over admissible contours. CA-I 147850 says that each layer's contour uses that layer's lattice bonds. This is distinct from identifying it with CMP 122a's `M_1`-cube distance. SA 9602–9605 and 10119–10127 also distinguish the more permissive ambient path distance from CMP 96 (2.46).

**Lemma 6.1, note 119–125: ADVANCE for contours contained in `X''`, under (G-c).** The first-high/last-low intervals are well chosen. The counted steps have weights at least `eta/ell_i`; different levels have disjoint counted steps. The total omitted-step cost is at most `1/(L-1)`. The argument that `c_E` is constant on a determining block follows from the compatible superlevel grids. It permits using the source's block reference points. These parts need no box or separate comparison with CMP 122a.

**The exterior extension at note 127: REVISE; its stated proof fails.** Extending `c_E=-1` outside `X''` changes its widths. An exterior site next to a high-level consumer site can make the extended `W_i` at most `eta`, even when the original low-level set is far away. For example, take two distant cubical components, one at consumer level `n` and one at level `m>=n+2`. Their original intermediate widths are their separation; the extended widths are small at the boundary of the high component. The tower can be fine there; it does not change this fact about `c_E`. Thus the last-low site outside the domain need not be separated from the first-high site by the original `W_i`. This refutes the extension's inference, not CR or the asserted SEP inequality itself.

Here is a sufficient repair that also covers paths leaving the domain. It uses the existing (G-t), and weakens the separation constant by the fixed factor `L+1`. It avoids adding a contour-confinement assumption to R.

For `n<i<m`, put

\[
A_i=\{x\in X'':c_E(x)\le i-1\},\qquad
v_i(x)=\min\{W_i(c_E),\operatorname{dist}_2(x,A_i)\},\qquad
V(x)=\sum_{i=n+1}^{m-1}\ell_i^{-1}v_i(x).
\]

Define these functions on the whole fine lattice. Both sets defining each width are nonempty because of the endpoints. At the low endpoint `V(y)=0`; at the high endpoint

\[
V(y')=\sum_{i=n+1}^{m-1}W_i(c_E)/\ell_i.
\]

Each `v_i` changes by at most `eta` on a fine step. At an interior site of consumer level `j`, it equals its cap for `i<j` and zero for `i>j`. Interior neighbouring sites have consumer levels differing by at most one: a jump of two would contradict `W_i>=M ell_i>eta` at the intervening index. Thus on a step with equal endpoint levels `j`, only `v_j` can change. On a step between levels `j` and `j+1`, only `v_j,v_(j+1)` can change, and

\[
|\Delta V|\le\eta(\ell_j^{-1}+\ell_{j+1}^{-1})
=(L+1)\eta/\ell_{j+1}.
\]

Terms outside the displayed index range are simply absent. Since `b_q<=c_E`, the weighted step length is at least `eta/ell_j` in the first case and `eta/ell_(j+1)` in the second. These are the same fine-step lower bounds used at note 123.

For a step touching the exterior, its inside endpoint, if any, has tower level zero. Otherwise (G-t) at level zero would give distance at least `LM_1 eta>eta` from that endpoint to the exterior. Such a step therefore has weight one, as do wholly exterior steps under the proposed finest-scale exterior convention. On it,

\[
|\Delta V|\le\sum_{i=n+1}^{m-1}\eta/\ell_i
\le 1/(L-1)\le1.
\]

Summing these inequalities over a subdivided admissible contour and taking the infimum proves the sufficient replacement

\[
d(y,y')\ge\frac1{L+1}\sum_{i=n+1}^{m-1}\frac{W_i(c_E)}{\ell_i}
\ge\frac{M}{L+1}(m-n-1).
\tag{SEP*}
\]

It also holds when only contours inside `X''` are allowed. Passing to block reference points uses the already checked blockwise constancy of `c_E`. No run or finite enumeration is used.

**Use in Lemma 7, note 129–135: REVISE with this explicit repair.** Set

\[
w_*:=M/(L+1),\qquad
N_q=C_{\rm RD}F\ell_{q+1}^2e^{-\delta_Hw_*(q-n-1)_+}.
\]

The note's `C_H'=C_H exp(delta_H(c_st+1))` is still sufficient; the extra `1` is now harmless slack. Keep the supremum over the support of `B`, with value zero for empty support. Replace the floors by

\[
M\ge\frac{L+1}{\delta_H}\log(2L),
\quad\text{or}\quad
M\ge\frac{L+1}{\delta_H}\log(2L^2)
\text{ for Corollary 9}.
\tag{Phi-H*}
\]

Then the previous gate's response estimate and all subsequent sums apply unchanged. If R's actual contours are proved confined to `X''`, the original stronger SEP bound and smaller floor can instead be retained. The unrestricted reading does not follow from the proof at note 127; (SEP*) supplies the needed implication without that claim.

## 7. Every remaining step and the previous gate's repairs

The current `cr-claude.md` blob is `1a3364d1d5831f50fd663220eac92aef86e1a47e`, exactly the revision identified by the previous gate. Its accepted calculations can therefore be reused with their original premises and the explicit substitutions above.

| Step | Verdict | Check or written repair |
|---|---|---|
| Note 6–16, provenance and target | ADVANCE with §1's source limit | This is a second-round research implication, not retained status. The account still labels the target “Proof outstanding.” The quotations from unavailable PDFs are not independently checked here. |
| Inherited Lemmas 1–3 and 4(a) | ADVANCE | The previous gate's path, perturbative-curvature, two-block gauge and equal-level anchoring checks remain valid. Retain SU(2), P6 and their stated ceilings. |
| Inherited Lemma 5, after new Lemma 5.2 | ADVANCE | The relative-datum identity, three path comparisons and constants remain unchanged. Replace its common-row invocation of ROW by COMP(=) and (BP), exactly as §4 states. |
| Note 161, lower scale at `q=0` | ADVANCE | `max(eta,ell_(q-1))` implements the previous gate's repair. |
| Note 162, gauge sentence | ADVANCE | It now asserts invariance of the norms. CA-I 42767–42768 and 42793–42795 support precisely that statement. |
| Note 163–165, step-size sum | ADVANCE with (Phi-H*) | The indicator removes the nonexistent `L^4` term when `p=n+1`. The three endpoint cases and the final `5L^2 C_RD F ell_n ell_p` bound are correct. The repaired SEP supplies the same geometric factor under (Phi-H*). |
| Note 166, current at `n=0` | ADVANCE | Taking `ell=eta` respects `xi<=ell` in CUR (CA-I 10350–10373). The displayed curvature parameter, response norm and current increment implement the earlier repair. For `n>=1` retain the checked full incident-plaquette stencil and `ell=ell_n/L`. |
| Note 167, Corollary 9 | ADVANCE with (Phi-H*) | Use its `2L^2` version. The bound `S<=3L^4 C_RD F ell_n^2` and the explicit ceiling `108L^10(C_H')^2 C_RD^2 C_F^2 alpha_k<=1` are correct. This gives the stated unit-scale estimates; it does not verify all consumer-radius comparisons. |
| Note 168–172, replacements | ADVANCE with §§2–6 | The avoiding-path remark is withdrawn. Lemmas 6′ and 5.2 replace the indicated lemmas. Proposition 4.1 needs its explicit source and tower qualifications; use (SEP*) for the unrestricted metric convention. The half-polydisc and support-supremum repairs are correct. |
| Note 173, intermediate levels | ADVANCE conditionally | CA-I 43055–43059 supplies a determining set at every level. No consumer slot at each intermediate `q` is needed if (R-form), the geometric hypotheses and R/T1 admission hold for each such set. This last quantifier must remain explicit. |
| Note 177, ceilings (8.1′) | ADVANCE | Substitution of `2^d`, a fixed half radius and `alpha_k<=c_av` closes the stated admission requirements. The other ceilings remain those checked previously. |
| Theorem 8′: existence and `n>=p` | ADVANCE under (S) | AV(e), T1 and the two-layer scale give the exact existence parameter and both above-slot estimates, by CA-I 44226–44303. No global box is needed once SRC is available. |
| Theorem 8′: `n<p` | REVISE, then ADVANCE | Use the clarified R coverage and (SEP*) with (Phi-H*). The checked curvature/current iteration, ceilings and absorption by `Phi_K` then give exactly the two below-slot constants in CA-I 44179–44185. |
| Note 191, all outside pairs | BLOCK as a source-discharge claim | Retain (S), (G-c), (G-t) and (R-form) for **every** actual read pair and every intermediate level. The table does not establish them for all consumers. |
| Note 204–224, Result and suggested record | REVISE | Record the repaired conditional implication and all its open readings, source properties and grants. Do not record the original proposition as proved from its printed hypotheses. Include the revised SEP floor and the admissibility-distance/tower qualification. |

## 8. Order of constants: answer (2)

**REVISE the order at note 195–200; the new late floors and ceilings are compatible once the early source properties are supplied.** CA-I 1498–1514 and 2063–2070 place `M_1`, the determined variational constants, the gap parameter and the kernel constants before `M`. The note lists all variational constants before `M_1`; there is no need for that stronger ordering. CA-I 1614–1629 allows subsequent downward choices of radii. CA-I 43573–43627 supplies the local floors-then-couplings order.

Use this order:

1. Fix `L` and the earlier construction parameters. Choose `M_1>=2` and the required gap parameters in their prescribed order. Then fix T1, AV, AX, P6, R and CUR constants, the admissibility threshold, and the response stencil/reference constant. Establish the tower part of admissibility here: `LM_1>w_adm`, or the norm-converted version in §3. This is an open part of (G-t), not something a later choice of `M` can fix.
2. Fix `C_F,C_RD,C_H',C_star,K_0` and `n_P=2^d`. Choose the next permitted `M` above the old floors, the admissibility floor, (Phi-H*) and `C_star/(3L^2 B_H K_0)`. These are finite one-sided lower bounds with earlier coefficients. For the stronger corollary use the `log(2L^2)` floor. If the admissibility distance is sup-distance and the width premises remain Euclidean, use `M>sqrt(d) w_adm` as well.
3. Fix a positive uniform `bar epsilon_1` in the admitted real-base class, with `bar epsilon_1<=a_1` and `B_3 bar epsilon_1<=epsilon_0`; set `r_P=2C_1 bar epsilon_1`. It must be fixed before the couplings and uniform over the pairs, not reselected at each rung. Independence from `M` is unnecessary; dependence on already chosen size parameters is allowed. Respect any further radius restrictions of the identified R source.
4. Choose `N_*` and the coupling ceiling for the account's Gamma conditions and (8.1′), including `2 alpha_k<=bar epsilon_1` and `C_RD C_F alpha_k<=r_P/2`. Add the Corollary 9 ceiling only when using that corollary. All coefficients are now fixed. CA-I 43618–43627 gives the stated uniform small-coupling choice.

Thus the additional `M` floors and coupling ceilings create no backward dependency, upper bound on `M`, or depth-dependent constant. This does **not** verify that the actual tower has sufficient width for the response theorem. In particular, if `w_adm` depends on `M_1`, increasing `M_1` cannot simply be assumed to make `LM_1>w_adm`; that relation needs its source identification.

## 9. Final implication and open clauses: answers (1) and (3)

**As printed: REVISE. After the repairs written here: ADVANCE the conditional SU(2) implication. BLOCK unconditional identification with CA-I 45085.** The implication gives (a) and both cases of (b), with the account's `K_b`, uniformly in depth and read domain. It assumes the account's determining-set hypothesis and inputs T1, AV (including the interface hypothesis), R at real minimiser bases, CUR and AX. Those are cited inputs, not results discharged by this check.

The additional open premises are exactly these, with their scope made explicit:

| Premise | Remaining obligation |
|---|---|
| **(EC)** | Identify every plaquette used by AV(e) and T1 with the common-point, distinct-block class. Under it, the new proof supplies `n_P=16`. |
| **(R-form)** | Identify every intermediate ladder, with its tower, rows, averaging maps, reference conventions and regular real base, with R's source system. The false untruncated-shell explanation is removed. |
| **(BP)** | Common blocks have the same base points in the two ladders. |
| **(S)** | Every actual read domain lies wholly in `Y_4 intersect (Z union Omega_k^old)`. Under it, Lemma 7.1 supplies SRC. |
| **(G-c)** | All required consumer superlevel sets have the aligned big-block extensions and widths. Shell names and inside-box separation alone do not supply this for all outside pairs. |
| **(G-t)** | The actual tower has the aligned superlevel cubes and widths, with enough width in the response theorem's admissibility norm. Keep the early inequality specified in §§3 and 8. |
| **P6** | The anchored equal-level bound applies to the account's chosen averages and base points. SA 7265–7283 supports its form but is indexed as sketched; this check does not discharge the source identification. |
| **COMP, including COMP(=)** | The account's refinement-composition grant applies to these actual ladders and gives equality on common rows. It remains a grant. |

There is no separate ROW assumption after §4. There is no separate SEP assumption after the written repair (SEP*), which follows from (G-c), (G-t), the compatible block geometry and the specified contour weights. Its stronger floor is compatible with the account's order. This advances the conditional argument by supplying `n_P`, anchoring and SEP; it does not prove that every outside consumer satisfies the antecedent.

**Clause (c) and the real-factor corollary remain open.** Neither the original outside proposition nor Theorem 8′ exports (c). CA-I 44803–44843 requires the consumer-radius conclusion and identification of the real factors of all four composites on the relevant domains. The level-`k` restriction at CA-I 43437–43440 belongs to inside boxes and cannot be transferred to arbitrary outside domains. No repaired estimate here establishes those remaining comparisons or identifications.

For recovery, the checked source file hashes are: CA-I SHA-256 `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`; SA SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`. The supplied upstream revision is an attribution, not a locally verified source Git HEAD. The next decision is source matching of the listed open premises, not another proof of the accepted finite calculations. No counterexample to CR has been established.

Only `gates/cr-r2-gate.md` was written. No prompt file, library note, registry, tree, status record, system instruction or developer instruction was changed. This report grants no scientific status.

Checked line by line by Codex (gpt-6-astra).
