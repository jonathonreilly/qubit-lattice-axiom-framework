## Repo search

The lead's search found no outside-lane proof of HC-WEIGHT.
See `prior/repo-search-2026-11-08.md`, lines 362–378.
It searched main and PRs #10114, #10133, #10134 and #10141.
`prior/leaf-hc.md` is absent at this checkout.

I fetched main and the two cited PR heads, without changing this checkout.
Main was `43a1fcc374711ca50626eca667441d3ca575c7d1`.
The cited heads still matched the digest.

| Hit checked | What it supplies | Distance from this leaf |
|---|---|---|
| PR #10114, `MEAN_READER_RETURN_ASTRA.md`, 117–143; head `f76f6c649cff7dffbab664d8976e680e8f287fe9` | Codex/Astra's complete-reader substitution proposition assumes a rooted weighted sum, with individual suprema inside it. | Useful norm discipline. Its hypothesis ME4 does not construct the actual collar readers or their copy weights. |
| Same PR, `ROUGH.md`, 406–414 | The original complete readers must remain in the weighted sum Q24. | Same warning; different family. It supplies no HC-MARGIN estimate. |
| PR #10141, `research/ym4d/library/in1.md`, 86–90, 197–203, 568–573; head `c73ad7b177d94f89ff37b77386936e3d52b48b05` | The exact two-pair consumer H-O and its use in class induction. | Same open conclusion, not a supplier. |
| This branch, `lfi-ho.md` §4A and Claude's `gates/ho-collar-check.md` | Anchored two-pair Schwarz–Cauchy reduction; the distinction between total and per-carrier bounds. | Reused without re-proving (C1)–(C2) or the kept-change sum. |

The registry's H-O row has owner `none`; FINISH row 540 assigns this leaf.
No separate HC-MARGIN owner or completed proof appeared in the registry, `open-core.md`, or `l17c.md`.
The composition and later-admission inputs retain their existing owners.

# HC-MARGIN and the Wilson carrier checks

Codex, 2026-11-08. Source pin `5e09ceb63dee6bb25006f5c51006f8552f6a481f`.
Research text, not an audit. Grants no status. No independent check of this note has occurred.
No computation supplies a proof step.
The checkout advanced concurrently; the consulted local science inputs were compared against the pin and remained unchanged.
This session wrote only `library/leaf-hc.md`.

**Result: stop (c), at HC-MARGIN-0 after three distinct routes.**
The Wilson carrier checks close on the supplied complex domain.
The swallowed-hull test does not refute the leaf.
The empty-switch complete-reader comparison below remains unproved.
Consequently this note supplies no complete HC-WEIGHT or H-O bound.

Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Bałaban supplies the large-field method.

- **SA:** `YM4_sketch_500.tex`, commit `31a47c543775`.
- **Y:** `YM4_1400.tex`, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **I:** `theorem_0_complete_account_raw_I.tex`, commit `31a47c543775`.

All three source files were already present at the requested `/tmp` paths.
SA locators came first from `sa-index/README.md`, chunks 05, 16, 17, and `obligations.md`.
CA locators came from `sa-index/ca-full/index.tsv`; the source's status overrides that index.
In particular, I 88187–88189 explicitly calls its proof incomplete, despite the index's `PROVED` field.
Only bounded source ranges were read.

## 1. Kill test, before the estimates

**Outcome: the swallowed-hull test does not kill the leaf. The mask test remains uninstantiated.**
The argument below is by hand. No numerical search was used.

SA 6191–6198 minimizes over exempt hulls **contained in the carrier**.
The tree must meet every other cube and every selected hull.
Being inside an exempt hull does not exempt a smaller carrier.
Write \(\mathsf H^-\) and \(\mathsf H^+\) for the standing hulls before and after birth.
Nested stored-variable labels in SA 6281–6286 do not themselves add members to \(\mathsf H^+\).

Take a long swallowed hull \(H\subsetneq X^\sim\).
For \(R=H\), the old distance is zero by selecting \(H\).
For \(R\subsetneq H\), that selection is unavailable even before birth.
After birth the new hull \(X^\sim\) cannot be selected for the smaller carrier \(H\).
This is the dangerous case if an old nonconstant factor remains filed on \(H\).

The source does not do that for the retained inner changes.
Y 73373–73404 places their original reads inside the prepared core and gives a stored-only anchor.
Y 73761–73768 moves that anchor to \(\Phi_\omega^\circ\).
Y 73887–73892 files each retained full-reader change on \(X^\sim\), whose output length is zero.
Thus the proposed swallowed **kept-factor** counterexample is excluded by the actual assignment.
This uses the existing kept-change construction; it does not re-prove its estimate.

There is also a geometric reason the proposed long hull cannot stay long at the birth scale.
Put \(h=t-\mathsf N_t\).
The single-box, quiet and quarantine conditions are SA 17575–17585.
No swallowed island was created in \([h,t)\); its old hull belongs to the inner lineage.
Y 73375–73384 includes these hull enlargements within one extra level-\(h\) cell.
That passage also supplies \(\check R_h\le L\check R_t\).
The single-box bound therefore puts their union in a box of side at most
\[
 C_g M\check R_h L^{h-t}
 \le C_g ML\check R_t L^{-\mathsf N_t}
 \le C_g ML
 \tag{K1}
\]
in level-\(t\) units. Here \(\mathsf N_t=\check R_t\), as in SA 17630.
For integers \(n\ge1\) and \(L\ge2\), \(n\le2^{n-1}\le L^n\).
The first inequality follows by induction: \(n+1\le2n\) for \(n\ge1\).
This proves the last inequality in (K1), without a computation.

Its coarse image meets at most \(q_*=(\lceil C_gL\rceil+2)^4\) output cubes.
A box of that size has a cube-edge covering tree of length at most \(4q_*\).
Thus even an absorbed hull that is no longer exempt costs a fixed constant at level \(t\).
This constant uses the class's fixed single-box constant and \(L\), before \(\bar\kappa\).
The test cannot hold that hull long at level \(t\) while retaining the actual birth conditions.
This statement concerns the swallowed hull, not a carrier extending far outside the inner core.

After birth, unabsorbed standing hulls remain available as exemptions.
Absorbed marks cease to stand; the newborn \(X^\sim\) replaces them in the output family.
SA 17415–17433 makes the new island a component without inner regions.
For retained changes the whole-reader filing uses the new exemption.
For a smaller read containing an absorbed hull, (K1) supplies its bounded filling cost.
No exemption for a proper subcarrier is invented.

Boundary slots have another rule.
Y 105931–105953 consumes a member containing an absorbed hull in the localized interaction.
It fills the exterior slot from a reduced-history donor and subtracts that donor in the interaction.
The donor uses the surviving hulls and has the required exterior length.
That statement does not bound the consumed interaction on its smaller collar carrier.
It is not a second proof of HC-MARGIN.

For the mask test, use unit coordinates on the output cube grid.
Let a one-cube primitive have a read mask reaching a cube at coordinate distance \(n\).
Assume neither end belongs to a selected complete exempt hull.
Every admissible tree then has length at least \(n-1\).
With \(K=\varnothing\), the proposed right side is constant if only the primitive cube is charged.
This refutes that shortened-reader inference by a hand calculation.
It does not exhibit an actual mask of the collar construction.
Y 63044–63059 requires full datum and read masks; Y 63115–63124 assumes a bounded enlargement.
A mask included in the complete class carrier is already charged on the right.
A connecting switch chain is charged through \(|K|\).
The unresolved case is an additional, uncharged mask in the actual action-difference roster.

## 2. The two Wilson carrier checks

These checks use the full common complex domain retained in `lfi-ho.md` (11a)–(11b).
They prove implications from the source's Wilson bounds on that domain.
They do not establish domain admission.

**Small Wilson sum.** Y 73655–73658 names the collected term \(\mathfrak v(X^\sim)\).
Keep that carrier and that grouping.
Its complete read includes the comparison backgrounds and the analytic normalizer.
Do not give those comparisons artificial one-plaquette readers.
Y 73707–73743 bounds this term by \(C_v(1+\bar c)\ell_t^{5r}\).
The weight is its net Wilson weight, not a fresh copy of \(\theta_t\).
Since \(X^\sim\) is exempt in the output label,
\[
 e^{\kappa d_t^\natural(\mathcal S^+;X^\sim)}
 \sup|\mathfrak v(X^\sim)|
 \le C_v(1+\bar c)\ell_t^{5r}.
 \tag{W1}
\]
Treat this prescribed collected term as one primitive, with \(K=\varnothing\).
No additional split or copy is introduced.
For \(\ell_t\ge1\), \(5r<2p_0\) gives its part of (C3).
The oscillation of this factor is at most twice its displayed complex supremum.

**Weight correction.** Y 74011–74023 identifies it as
\[
 \mathsf W_X=A(w'-w_{\rm fr},\bar W).
 \tag{W2}
\]
It is the outgoing Wilson density with the difference of weights, supported in \(X\).
Here \(\bar W\) is the configuration coordinate of the outgoing pair.
At birth this is a function of that pair, not a new substitution of its defining boundary data.
Its plaquette summands read four links and the fixed label weight.
They read no stored inner field and no response switch.
Thus their native differenced set is empty.

Y 73744–73756 explicitly permits the split into local plaquette carriers.
Use its carriers, including the endpoint convention for boundary plaquettes.
Each lies in a bounded star of output cubes; let its cube count be at most \(q_W\).
Let \(D_W\) bound its ordinary tree length.
Both constants are fixed and independent of \(t\), the cutoff and the coupling.
There is one summand per plaquette. A frame average preserves the total absolute weight.
For any fixed carrier \(R\), the source's two counts give
\[
 \begin{aligned}
 \sum_{p:R_p=R}\sup|w_p|
 &\le C q_W M^4\eta_t^{-4}
       \eta_t^4\alpha_{0,t}^2
       (|x_{t-1}-\theta_t|+\bar c)\\
 &\le C_W(1+\bar c).
 \end{aligned}
 \tag{W3}
\]
The last inequality is exactly the net-weight estimate at Y 73749–73754.
The fine plaquette count cancels the fourth power of the fine mesh.
Since \(d_t^\natural\le d_t\le D_W\),
\[
 e^{\kappa d_t^\natural(\mathcal S^+;R)}
 \sum_{p:R_p=R}\sup|w_p|
 \le e^{\kappa D_W}C_W(1+\bar c).
 \tag{W4}
\]
This supplies the second Wilson part of (C3), and twice it bounds the two-pair oscillation.
The constant precedes the coupling ceiling and does not use \(B_\Phi\).

The same local Wilson filing is explicit in Sussman and Alpoge's I 55088–55119.
There each fine plaquette is assigned once by its base point.
The cube term is an entire function of its own plaquette variables.
I 55121–55156 proves its per-cube estimate before inserting it into the weighted norm.
This is supporting source agreement, not a port of the whole preparatory-stage theorem to this birth.

## 3. The one remaining lemma

**HC-MARGIN, for the actual action-difference roster.**
Cancel carried trunks first, as prescribed at Y 73660–73673.
For each remaining entry \(e\), retain its complete class carrier \(R_e\), its coefficient, and every prescribed copy.
Let \(B_e=\widehat R_e\) be its level-\(t\) image without an added layer.
Let \(K\) be the differenced switch cubes.
Let \(R(e,K)\) include every field, current, datum, gauge and stored-variable read of the actual bracket.
Prove, with the actual output family \(\mathsf H^+\),
\[
 d_t^\natural(\mathcal S^+;R(e,K))
 \le (1+2\beta_s)d_t(B_e)+c|K|+C,
 \tag{HC}
\]
where \(c,C\) precede \(\bar\kappa\).
Match the length on the right to the entry's available decay majorant.
Then give the rooted count, with every original copy weight, below the remaining decay rate.
These are the clauses of the requested leaf, not new independent suppliers.

The failed substep is the treatment of fixed read masks outside \(B_e\).
Call their union \(N_e\); this notation does not change their filing or their switch status.
The source's analytic admission inputs do not themselves put a length bound on \(N_e\).

The precise remaining lemma is **HC-MARGIN-0**:
there exists \(C\), fixed before \(\bar\kappa\), such that every nonzero empty-switch action-difference bracket satisfies
\[
 d_t^\natural(\mathcal S^+;R(e,\varnothing))
 \le(1+2\beta_s)d_t(\widehat R_e)+C.
 \tag{HC0}
\]
The quantifiers range over all admitted histories, levels, tori and cutoffs of this construction.
The carrier includes all actual fixed masks; \(R_e\) is the complete carrier paid by the source class bound.
The constant is independent of the history, coupling ceiling and inherited island constant.
An assertion about an arbitrarily enlarged kernel support is not (HC0).
This is one sublemma of HC-MARGIN within the assigned H-O task, not a new owner or a new route.

The available source room must be stated accurately.
SA 19445 **sketches** the new \(\mathbf T\) rate \((1+4\beta_s)\kappa\).
For older ordinary entries it sketches
\[
 e^{-\kappa d_j(R_e)}
 \le e^{-c_0\kappa d_j(R_e)}
       e^{-(1+3\beta_s)\kappa d_t(B_e)}.
 \tag{S1}
\]
Neither length in (S1) includes an added collar.
SA 17999–18009 states the successive rate budget; it does not prove the missing mask comparison.
For an old boundary entry the class bound is instead R23, with its own exempt-family length.
One cannot replace that length by \(d_j(R_e)\) in (S1).
The swallowed-hull check above pays the local loss at this birth.
Surviving exemptions must still be retained when matching a boundary source majorant.

## 4. Three routes to HC-MARGIN-0

### Route 1: transfer a covering tree directly

Start with a shortest tree for the full base \(B_e\).
If every new read cube belongs to a connected switch extension of that base, attach those cubes in forest order.
For each attached cube, connect its entry and exit corners inside that cube.
The cube graph has four coordinate directions, so this costs at most a fixed number of edges per cube.
Join each forest root to the old tree within the base cube it touches.
There are at most \(|K|\) nonempty forest components.
Deleting cycles leaves a covering tree.
This proves
\[
 d_t(R(e,K))\le d_t(B_e)+c_1|K|+C_1
 \tag{T1}
\]
when the remaining fixed masks cost at most \(C_1\).
Taking a natural length can only decrease the left side.
The bounded swallowed hull from (K1) can be paid in \(C_1\).

For general fixed masks, the same construction charges each additional read star.
It then gives a cost proportional to the number of base cubes, not a fixed \(C_1\).
A tree of \(m\) cube edges has \(m+1\) vertices.
At most sixteen four-dimensional cubes meet one vertex.
Thus the ordinary base has at most \(16(m+1)\) cubes.
Charging a fixed cost \(a\) at each base cube gives only
\[
 d_t(R(e,K))\le (1+16a)d_t(B_e)+c_1|K|+C_2.
 \tag{T2}
\]
It gives no reason for \(16a\le2\beta_s\).

Y 63115–63124 proves the fixed-bond version with a bounded read star.
Its bound is \(c_h(|K|+n_b)\), where \(n_b\) counts that star.
It does not identify every collar entry's fixed mask with the complete source base \(B_e\).
In particular, a current or remade-row read is not determined just by naming its kernel support.
**Failure:** the direct tree construction stops at the uncharged part of the fixed masks.
It proves (T1) for entries with the stated containment, not for the whole actual roster.

### Route 2: force those masks into the differenced switch set

Try to use component cancellation to make every additional read pay a Cauchy factor.
The exact rule is SA 5840–5848.
A component containing a differenced cube and missing the base cancels.
A component made only of fixed cubes need not cancel.
The excess also vanishes when the base component has no response datum.
None of these rules charges a fixed mask connected to the base and carrying datum.

For \(K=\varnothing\), the bracket is the value with the remaining varied switches set to zero.
Its fixed switches remain one.
The anchored estimate is still \(a_eM_e\); it contains no factor depending on \(|N_e|\).
This follows directly from SA 5849–5861 and Y 63078–63111.
Differencing a formerly fixed cube would change this bracket and the prescribed decomposition.
Restoring the exact decomposition would restore its undifferenced term too.

An empty-bracket term could still acquire spatial decay from an actual response estimate.
That requires its full datum path, including the mask, to be charged in that estimate.
Neither the cancellation identity nor complex-domain admission supplies that path comparison.
**Failure:** the nonzero empty bracket is the first case this route cannot charge.
This is a failure of the proposed deduction, not an actual long-mask counterexample.

### Route 3: spend the source's rate reserve on a bounded enlargement

Try (T2), or the fixed-bond bound, with a larger but fixed carrier multiplier \(C_{\rm mask}\).
For an entry with rate \((1+3\beta_s)\kappa\), the weighted majorant would contain
\[
 \exp\{-[(1+3\beta_s)-C_{\rm mask}]\kappa d_t(B_e)\}.
 \tag{T3}
\]
There is no entropy reserve if \(C_{\rm mask}\ge1+3\beta_s\).
Even \(C_{\rm mask}<1+3\beta_s\) needs a quantitative gap above the actual entropy.
Increasing \(\bar\kappa\) affects nonempty switch sets only.
Coarsening can help older entries, but cannot help a new entry at level \(t\).

Here is an explicit reason bounded enlargement alone cannot give the required small fractional loss.
This tests that inference, not the actual masks.
Use the cube-edge convention stated in Y 105817–105821.
Let
\[
 P_n=[0,n]\times[0,1]^3,
 \qquad P_n^{+}=[-1,n+1]\times[-1,2]^3,
 \qquad n\ge3,
\]
viewed as unions of unit cubes with no exemptions.
A straight grid segment from first coordinate \(1\) to \(n-1\) meets every cube of \(P_n\).
Its length is \(n-2\), which is minimal by the separation of the two end cubes.
The enlargement contains \(27(n+2)\) cubes.
If a covering grid tree has \(m\) edges, its \(m+1\) vertices meet at most \(16(m+1)\) cubes.
Every cube met along a grid edge also meets an endpoint of that edge.
Consequently
\[
 d(P_n)=n-2,\qquad
 d(P_n^+)\ge\frac{27(n+2)}{16}-1.
 \tag{T4}
\]
For \(\beta_s<11/32\), (T4) rules out
\(d(P_n^+)\le(1+2\beta_s)d(P_n)+C\) for every fixed \(C\).
The coefficient difference is \(11/16-2\beta_s>0\).
For any other fixed fraction, a larger fixed collar gives the same test.
Choose its width \(h\) so that \((2h+1)^3>16(1+2\beta_s)\).
The proof is unchanged with \(27\) replaced by \((2h+1)^3\).

This example is not an instance with the required complete source carrier.
If the source already pays \(P_n^+\), its cost belongs in \(R_e\) and no contradiction follows.
That distinction is precisely why actual source-to-mask matching is needed.
**Failure:** a fixed collar bound cannot replace the coefficient in (HC).
A lower output rate would change the consumer; it is the separate HC-RATE fallback, not this leaf.

## 5. Supplier handoff

The missing comparison is needed before the rooted sum.
To see the exact reserve, suppose an entry has the matched majorant
\(M_e\le A_e e^{-(1+3\beta_s)\kappa D_e}\).
Here \(D_e\) must be the length actually paid, with surviving exemptions retained where required.
If its analogue of (HC) holds, its contribution to (C3) is at most
\[
 e^{\kappa C}w_eA_e\,
 e^{-\beta_s\kappa D_e}
 \left(\frac{e^{\kappa c}}{e^{\bar\kappa}-1}\right)^{|K|}.
 \tag{R1}
\]
This is the rate budget, with the individual supremum and copy weight still inside the sum.
It is not obtained from the unweighted action-difference total at Y 73675–73704.

Sussman and Alpoge already give the fixed-family rooted hull count at Y 105823–105864.
Its entropy is \(c_E=2\log8+(16+m_H)\log2\), with bounded hull multiplicity \(m_H\).
Its root is either outside the exempt hulls or a specified vertex of the minimizing tree.
Use that proof when the actual source roots and masks have been matched; do not re-prove it.
For the full collar roster, source levels and original copy weights must also be assigned to those roots.
The soft-route proposition checked in the Repo search likewise requires that weighted input before substitution.

In such an assignment, let the total root amplitude at lengths \((m,n)=(D_e,|K|)\)
be bounded by \(C_{\rm rt}\ell_t^{2p_0}e^{h_0m+h_1n}\).
Then (R1) sums to two geometric series when
\[
 \beta_s\kappa>h_0,
 \qquad \log(e^{\bar\kappa}-1)>\kappa c+h_1.
 \tag{R2}
\]
The entropy constants and \(c,C\) must be available before these choices.
No full-roster assignment or values for \(h_0,h_1\) are asserted here.
The first unsupported case precedes that count: (HC0).

The alternative source results do not bypass it.
I 84503–84586 treats two whole kept members and assumes the potential bound in KH1.
I 88187–88221 retains that input and explicitly calls its proof incomplete.
I 55194–55225 qualifies the lower-level stage rate by its condition \((F_m)\).
It cannot be read as an unconditional version of (S1) for these collar entries.
The donor refiling at Y 105931–105953 fixes the exterior slot.
It leaves the old-minus-donor interaction to be estimated with its actual reader.

**Stopping reason.** The direct tree route, cancellation route and rate-reserve route each stop at (HC0).
The displayed tests refute weaker deductions, not an actual admissible birth.
There is no claimed counterexample to Sussman and Alpoge's construction.
This is a research checkpoint after three failed routes to one specified lemma.

## 6. Status table

| Item | Result in this note |
|---|---|
| Existing kept-change sum and two-pair reduction | Reused from `lfi-ho.md`; not re-derived. |
| Output exempt family | Standing unabsorbed hulls and the newborn hull; nested stored labels alone confer no exemption. |
| Swallowed-hull kill test | Does not kill the actual birth. Kept changes use the whole reader; absorbed old hulls have bounded output size by (K1). |
| One-cube primitive with a long uncharged mask | Refutes a shortened-reader inference. No actual collar entry with that mask was established. |
| Small Wilson sum | Carrier check and weighted bound (W1), conditional on the source's supplied complex-domain estimate. |
| Wilson weight correction | Literal plaquette readers, no response switches; weighted bound (W4) from the net weights. |
| **HC-MARGIN-0** | **Open after three distinct routes.** Exact missing assertion: (HC0) for the actual empty-switch brackets. |
| HC-MARGIN and the actual rooted sum | Not supplied; the complete-reader comparison fails first in the attempted proof. |
| HC-WEIGHT for the action difference; full H-O | Open. No value of the complete collar constant \(b_V\) is returned. |
| (11a), (11b) and independent checking | Retained inputs. No domain result, audit result or independent check is claimed. |

**First open input:** HC-MARGIN-0, equation (HC0).
Supply the actual empty-switch masks and their charge to the source's complete class carrier.
Keep the prescribed carriers and copy weights. An enlarged substitute carrier or an unweighted total does not supply this input.
