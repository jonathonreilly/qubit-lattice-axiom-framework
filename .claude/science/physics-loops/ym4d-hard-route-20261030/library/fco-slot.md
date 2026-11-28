# FCO-slot: ownership of stored coordinates and record slots

Checked line by line by Claude (Opus 5.5), gates/fco-slot-check.md: FIX, repairs applied.

Codex, 2026-11-08. Source checkout `f70c307da5fd5d6eb0c0baf5db784cd340396a53`.
FINISH row 519. Research text, not an audit. This text grants no status.
No computation, enumeration or numerical bound supplies a proof step.
**Result: stopping condition (a).** FCO-slot holds for the specified revised rules.
Here “the specified revised rules” use N's two-range nest (Y 63773–63825), with SA 17421's \(X\setminus Z''_l\) labels.
The proof gives UO2-geo at slot scope, the code count and the original reserve comparison.
FCO-read remains a named input for history products.

## 1. Scope and prior work

`prior/fco-slot.md` is absent at this revision.
The assigned target is the slot part of GEOH-O2, `open-registry.md:227`.
The existing proofs in `uo2-geo.md` and `geoh-o2.md` are inputs, not new targets.
Their check, `../gates/uo2-geo-check.md`, confirms the chain, owner rules and conditional counts.
Its findings 7, 8, 10, 13 and 14 specify the remaining case check.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the large-field method and preparation geometry.
Every source port below is theirs.

- **Y:** [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), revision `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **SA:** [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), revision `31a47c543775`.
- **I:** [complete account, Part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), at the same revision as SA.

The outline index was consulted before its source passages.
The relevant entries are chunks 05, 16 and 17, with their neighbouring rows and `obligations.md`.
The complete-account index is `sa-index/ca-4.12-4.19/`.
The source files were read in bounded ranges.
SA 18450–18460 proves a site budget once the collars have owners.
Y 78917–78923 states the remaining geometric assertion; it does not perform this slot case check.
I 85575–85644 explicitly treats live-region geometry as hypotheses.
I 166650–166659 still lists that geometry and volume counts as outstanding.

The proof concerns the specified revised operation and its actual finite records.
Its class, selectors, coordinate masks and stopped branches remain fixed.
H-LF supplies the single-storage convention and coordinate identities.
The finite operation grammar supplies the fixed coordinate types and local test lists.
These are the existing inputs of `uo2-geo.md`, sections 2 and 4.
No analytic density bound is assumed or concluded.

FCO-read is a separate input for history restriction and products, SA 18878–18927.
It concerns complete background boxes, original indicator carriers and class windows.
Locating their stored arguments does not prove locality of the functions that read them.

## 2. The ported geometry and the statement

Put \(a_n=ML^nR_n\), in bare units.
A cell below means a boxing cell of side \(a_n\), not an \(M\)-cube.
Use half-open cells for addresses and closed carriers for distances.
For an integer \(c\), let \(Q^{[c]}\) be the union of cells at cell-index distance at most \(c\) from \(Q\).
This is a collar in owner cells.

The following ports supply the geometry.
They were also checked in `../gates/uo2-geo-check.md`, findings 1–6.

| Port | Exact content used | Source |
|---|---|---|
| Surviving chain | For an attempt at \(t\), with \(h=t-N_t\), \(G_i=X\cap Z_i\) is an as-made node at every \(h\le i\le t\). | Sussman–Alpoge, Y 63713–63771; `uo2-geo.md`, section 3. |
| Prepared containment | \(D_i\subset O_i:=X\cap\Omega_i^{\circ c}\subset G_i\), and \(G_h\subset D_{h+1}\subset\cdots\subset D_t\). | Sussman–Alpoge, Y 63773–63825. |
| Visible containment | \((\Omega_i^{\rm d})^c\subset(\Omega_i^{\rm a})^c\subset Z_i^{\rm a}\). | SA 17415–17447; port in `sa-2.13.md`, (6.1). |
| Owners | Unaltered slots use their action cells. Remade slots use their remaking history. Prepared means keep their level. Nested records use the latest remaker. | Sussman–Alpoge, Y 78906–78916. |
| Unique active window | Overlapping standing marks are nested and their preparation windows are disjoint. | Sussman–Alpoge, SA 17440–17449. |
| Cut multiplicity | A clearing node occurs in two outer trees. Every other node occurs in one. | Sussman–Alpoge, Y 74218–74271. |

The circle in \(\Omega_i^\circ\) means just before the attempt.
The preparation is the explicit two-range preparation in Y 63773–63825.
The class uses ancestral quarantine with its lower endpoint included.
A match to a different operation remains GEOH-O1, owned elsewhere.
We do not replace those rules by CA's weaker quarantine convention.

The slot proof uses only \(D_h=G_h\), nesting (N1), and \(D_i\subset O_i\) (N3) from the nest.
The thin rule (N) in `ti-2.md:43–50` supplies all three: \(a=h\), \(D_a=C=G_h\), and \(D_i\subset A_i=H_i^{[8]}=O_i\).
Sections 3–4 therefore carry over unchanged, with the same constants.
Y's row chart and prefix list (Y 75842–75960) for the thin first member remain an input owned by ti-2 / GEOH-O1.
In particular, its first-stage “five of the eight layers” clause (Y 75863–75865) is not supplied by this slot transfer.

A **slot** is an actual stored coordinate, a visible determining or action address, or an address in the discrete record.
It retains its native level, position, type and creation identity.
A bond slot includes its endpoints.
A stored collar contains its actual added storage addresses, with their coordinate types.
Split that collar into its stored sites before assigning owners.
This retains every site in SA's count; it does not put a whole component collar in one cell.
A test slot is its recorded outcome address; its full input set is a different object.
A function, reconstructed value or repeated evaluation does not create an integration coordinate.
A genuinely new coordinate does receive a new identity.

Write \(a=(n,Q)\) for one cell occurrence in the expanded island recursion.
Its price is \(w(a)=\ell_n(MR_n)^4\), where \(\ell_n=1+\log x_n\).
Summing these prices gives IN1's existing \(v^\natural\).
An inner island is one outer leaf plus its separate inner record.
No descendant is recopied when the island is carried.

**FCO-slot.** For every finite history of these specified rules, each stored slot has one owning occurrence \((n,Q)\).
Its native level is \(n\) or \(n-1\).
Its site or bond address lies in \(Q^{[c]}\), for a fixed integer \(c\).
Every added storage-collar slot obeys the same assertion.
The same assertion holds for visible nonterminal slots and the local discrete record.
At each owner-level lattice site, assigned multiplicity is at most \(\mu L^4\).
Discrete slots have multiplicity at most \(J\mu L^4\).
For each fixed native level and site, the covering multiplicity is bounded uniformly.
The constants are independent of depth, volume, stopping stage and coupling floor.
They depend only on the fixed geometry and coordinate templates.

The terminal unmarked determining field is the existing current-level term \(N_k\).
It is not a stored coordinate of a component operation.
Likewise, forced successful tests away from the recorded component require no independent code letters.
These are the conventions of Y 78867–78903 and `sa-2.13.md`, sections 3 and 6.
They remain explicit in the restated load bound below.

## 3. Filing the actual slots

Fix one history, not arbitrary assignments of test outcomes.
At each new slot choose the first eligible endpoint in a fixed orientation order.
Choose its half-open cell inside the node specified below.
For a collar site outside that node, choose the first nearest cell of the node.
The distance bounds below show that this choice is local.
Keep this owner when carrying the same slot.
For a remade datum use the unique remaking window and the corresponding historical node.
The latest-owner rule changes the datum read; it does not recopy its inner coordinates.

### Ordinary storage and visible slots

At step \(j+1\), the exterior Haar field \(V_j\) is stored on \(\Omega_{j+1}^c\).
The stored fluctuation \(A'_j\) is on \(\Omega_{j+1}\setminus\Lambda_{j+1}\).
Both sets lie in the as-made \(Z_{j+1}\).
This is the actual coordinate split of Sussman–Alpoge, SA 17528–17532.
Assign both types to the containing level-\((j+1)\) action cell.
Store the fine offset; this conversion has exactly \(L^4\) offsets per coarse lattice site.
The first ordinary step treats native level zero in the same way.
It needs no level-zero genealogy node.

The collar, rim and cut-off-zone sets are subsets of this stored stock.
They are three distinct masks, not three new copies of its coordinates.
SA 17354–17358 defines the collar and rim.
SA 17453–17459 records all three masks separately.
SA 17518–17526 makes the cut-off substitution bond by bond on the strip.
Its new variable has the old bond address.
A pivot is solved at its original coarse row; it is not an additional stored Haar coordinate.
Keep the mask and pivot role in the finite type at that address.

A determining bond of level \(j<k\) has neither endpoint in \(\Omega_{j+1}^{\rm d}\).
SA 5612–5629 is its definition.
Visible containment puts its selected endpoint in \(Z_{j+1}^{\rm a}\).
Assign it to that level-\((j+1)\) as-made node, including any recorded inner history.
A visible level-\(j\) action address uses its original level-\(j\) node.
Its collared extension uses the nearest such cell.
These are the already proved assignments in `sa-2.13.md`, (6.2)–(6.3).
An erased healed slot is absent; later reuse of its location does not revive it.

### A preparation and every stopped prefix

Use the current attempt's chain \(G_h,\ldots,G_t\).
At stage \(j+1\), the exterior collar stock lies on
\[
 C_j=(\Omega_{j+1}^{\circ c}\setminus D_{j+1})\cap X
       \subset O_{j+1}\subset G_{j+1}.
 \tag{1}
\]
The old strip stock lies on
\[
 T_j=(Z_{j+1}^{\circ}\cap\Omega_{j+1}^{\circ})\cap X
       \subset G_{j+1}.
 \tag{2}
\]
Here \(Z_{j+1}^{\circ}\cap X=G_{j+1}\).
The coordinate sets are those in Sussman–Alpoge's Y 75845–75862 and I 74309–74320.
Thus the level-\(j\) collar and rim coordinates have level-\((j+1)\) owners.
Under the incident-bond convention, an endpoint lies in (1) or (2).
The other endpoint adds one lattice spacing, not another scale.
I 159058–159075 states that larger bond convention.
Deleting its pivots only reduces the stock.

For the newly solved rows, use the three-way split in Y 75845–75904.
An inner row has its full double block in \(D_{j+1}\).
A collar row has its double block outside the old \(\Omega_{j+1}\), inside the same component.
Its endpoint is in \(O_{j+1}\); its fixed block reach remains within one owner-cell collar.
An ordinary row retains its old reconstruction.
Its pivot never becomes a second collar coordinate.
These statements are Sussman–Alpoge's row-ownership port, not a new chart theorem.

The coarse target of a collar row is native level \(j+1\).
File it at that row's level-\((j+1)\) cell.
The fine nonpivots are native level \(j\), with the one-step offset.
A shell datum of native level \(i<t\) lies outside the next determining member.
In the remade portion it therefore lies in \(D_{i+1}\subset G_{i+1}\).
In an unremade portion it lies in \(O_{i+1}\subset G_{i+1}\).
A datum on \(D_i\) itself can use \(G_i\).
These statements locate the actual datum, including a prepared mean, at its own or next level.
They never replace it by a field that has already been integrated.
This is the distinction required by Y 73160–73179 and 78909–78916.

The bottom core is \(C_h=G_h\).
Its native level-\(h\) field uses that node.
Its older integral operation keeps its existing lower-level owners.
The main box is \(D_t\) plus one level-\(t\) \(M\)-layer, inside \(X=G_t\).
Main-step free fields and reference-law coordinates use their native addresses there.
The shell fields retain the addresses just assigned, even when their common expansion parameter is \(g_t\).
Sussman–Alpoge describes this stock at Y 63828–63842.
SA 17604–17608 puts the reference draw on this same box, with its external tree bond.
That incident tree bond requires only the endpoint allowance below.
Changing the normalization of a coordinate does not change its native lattice.

A stop before the collar pivot change retains the old stock.
A sharp failure after that change retains its nonpivots and translated density.
It adds no free pivot and no integrated collar normalizer.
After a completed stage, the remaining inner rows lie wholly in the next prepared core.
These are all the prefix alternatives in Y 75915–75960.
Their assigned sets are respectively unchanged sets or the subsets in (1)–(2).
A late main-step stop uses the same shell, core and main-box stock.
Thus stopping anywhere does not require a new owner level or a larger collar.

### Islands, inherited fields and live strips

An island retains \(\mathbf T'_t(X)\), with its actual variables, measure and factors.
This is Sussman–Alpoge's rule, SA 17418 and 17642–17654.
Its completed-stage shell and core variables are exactly the preceding cases.
Its inner histories are retained by reference, with their owners and native levels.
A drop-out keeps the unreached ordinary operations and the reached bare graph integrals.
Those are respectively the ordinary case and the prepared-row case.
The failing factor is a test slot, not an additional field.

At an island cut, put interior slots in the inner record.
Put the outer entrance and cut header at the outer leaf.
Use the inner root for the island operation's own coordinates.
This fixes the otherwise harmless tie at the two copies of the boundary node.
Y 74218–74271 supplies those occurrences and proves that there is no third copy.
Carrying the block does not copy its slots.
Healing removes the block from the standing record.
These moves exhaust SA 17415–17440.

There is also an existing check for live-strip storage.
`geoh-live-ab.md`, section 5, assertions 3–4, gives
\[
 S_Y\subset B_Y\subset\Omega_{m+1}^c,
 \qquad B_Y\subset\text{the level-}(m+1)\text{ component containing }Y.
 \tag{3}
\]
Its proof was checked by Claude in `../gates/geoh-live-ab-check.md`.
For a native level-\(m\) stored site, (3) gives an owner at level \(m+1\), once that level exists.
At birth, the strip reaches only \(q_m\le(R_m-1)/2\) birth \(M\)-cubes beyond \(Y\).
It fits a one-cell collar of the level-\(m\) birth node.
For native levels below \(m\), use the coordinate's own ordinary or inner-record owner instead.
Equation (3) does not permit converting those finer sites directly to level \(m+1\).

This check uses CA's strip definition only where it has been matched to the record.
That match is GEOH-O1, not a claim here.
The island proof above uses SA's retained operation directly and does not depend on that match.
In particular, it does not identify all lower-level island variables with the current strip.

### Seams and discrete anchors

A seam records its actual gauge prescription, background recipe and pivot role.
Sussman–Alpoge, Y 73181–73194, requires those tags.
A tag belongs to the row already filed above.
Its background value is a function of existing arguments, not a new free coordinate at each later read.
A stored gauge variable uses its actual vertex or row address and finite gauge type.
The coarea identity in Y 75915–75932 consumes each solved row exactly once.
It neither deletes its density nor creates another Haar variable.

Ordinary failed test cubes and failed collar/rim objects are recorded in the created cells.
The construction puts these cells in the final as-made \(Z_{j+1}\), SA 17317–17334.
Successful local masks use the adjacent stored regions; exterior forced successes are recovered by replay.
A collar/rim round visits each object at most once.
A preparation records its stopping stage and failure locations; completed stages have forced passing outcomes.
These replay rules are ported in `sa-2.13.md:104–118` from SA 17356–17368.
Prepared tests are anchored in the corresponding stage's sets (1)–(2), prepared shells or main box.
An old indicator retains its original address and type.
Its evaluation at reconstructed data adds no new outcome letter for its old test.

Keep all discrete selector outputs that the fixed record requires.
Their site, seam and entrance addresses use the same cases.
The component header is assigned to its first cell in a fixed address order.
Its stage index is counted as a polynomial-size header, not as a fixed-alphabet letter.
This is exactly Sussman–Alpoge's finite coding condition, Y 74649–74669.
It does not cover a different operation with additional unpriced selector choices.

## 4. A fixed cell collar and bounded multiplicity

The case check gives a fixed spatial bound, not just a candidate owner.
Here are all the enlargements used in that check.

- A stored field has an endpoint in its assigned region.
  Its bond adds one native lattice spacing.
- A pivot row uses its full double block.
  Its diameter is at most two owner-level lattice spacings.
- An assigned component/action collar adds one \(M\)-layer at its assigned level.
  SA 17356 defines this collar; Y 78893–78903 charges its cells to the original action cells.
- The ordinary collar has reach \(\varpi_T\) in the preceding level's units.
  The fixed floor \(M\ge\varpi_T\) makes this smaller than one owner cell.
- Rim masks inspect neighbouring cells, with \(\Omega_i^c\) entering at most two layers away, SA 17459.
  Those are mask addresses; they do not enlarge the stock into the full background read region.
- An ordinary test cube and its indicated local test enlargement fit within one owner cell's reach.
  Y 65175–65183 bounds the relevant reach by \(2LM_2R_m+1<LMR_m\).
  Y 64048–64078 keeps the test-cube centre box and specifies its width.

The last estimate uses the source's choice of \(M\), after \(L,M_2\).
It says less than one *cell*, not a fixed number of \(M\)-layers.
For a native level-\((n-1)\) object, use the level-\(n\) cell in this comparison.
For a native level-\(n\) object, use its own cell.
No comparison across more than one level occurs.
The main-box enlargement was already included in section 3.

Use the source floors \(M\ge\max\{3,\varpi_T,L^2M_2\}\) and \(R_n\ge1\).
Take \(c=6\).
The endpoint and double block together cost at most one cell, since \(MR_n\ge3\).
Allow one cell each for the storage collar, ordinary collar and test enlargement, and two for mask layers.
Their sum is at most six cells.
These allowances overcount the cases where only one of these enlargements occurs.
The construction does not successively add these collars when a mark is carried.
Its coordinates and masks retain their original addresses.
New shells receive new stage owners instead of enlarging an earlier owner's collar.
Thus \(c\) is independent of the number of stages or later reads.
The whole test-centre box is not being asserted to satisfy FCO-read.
Only its recorded test address and its genuinely stored coordinates enter this calculation.

We now verify multiplicity in time as well as in space.
Fix an owner level \(n\), an owner site and a fixed literal recursive history.
There is one ordinary step that creates its native level-\((n-1)\) stock.
A preparation that remakes this stock uses window index \(n\).
It performs that stage once and stops at its first failure.
At a fixed place, two overlapping retained attempts cannot both use that index.
Indeed, while the older mark stands, the newer attempt must start strictly above its level.
Their windows are disjoint by SA 17440–17449.
If the newer attempt swallows it as an island, its old record becomes an inner record with the same older window.
The inequality between the two windows is unchanged.
If it heals, that earlier genealogy ends and is not restored by later spatial reuse.
This proves the same uniqueness within the expanded recursion.

A native level-\(n\) target is filed with the stage that creates that target.
If the next stage reads it as input, the read keeps its identity.
If that next stage creates a genuinely different variable, it belongs to the next owner level.
The finite main-step change of shell coordinates uses the same attempt's native row addresses.
Its finite coordinate roles can be included with that stage's types.
No variable is added once per later stage merely because the reconstruction uses it.
H-LF and the coarea port in Y 75915–75960 give exactly this convention.

Let \(\tau\) bound the fixed types at a site for one ordinary or remaking stage.
Include orientations, colour coordinates, gauge roles, shell transformations and seam roles in \(\tau\).
This is the finite template used in Y 74655–74666 and `uo2-geo.md`, section 4.
There are two native levels, at most two origins (ordinary and remade), and five geometry uses (Y 73147–73158).
Consequently the deliberately generous choice
\[
 \mu=20\tau
 \tag{4}
\]
suffices before the one-step offsets.
After projection, the per-owner site bound is \(\mu L^4\).
The fixed record template contributes at most \(J\mu L^4\) discrete slots there.
Here \(J\) is the fixed template constant of `uo2-geo.md:441–442`, independent of analytic factor counts.
Stage headers are treated separately in section 7.
A repeated analytic factor is not removed by this argument.
It remains in the actual density and is outside the asserted multiplicity.

Put
\[
 A_c=(2c+1)^4.
 \tag{5}
\]
An owner collar has at most \(A_c(MR_n)^4\) owner-level sites.
A site belongs to at most \(A_c\) such collars at one owner level.
Both statements follow coordinate by coordinate from the \(2c+1\) possible cell indices.
Half-open addresses avoid duplicated endpoints; the chosen collar already includes physical bond endpoints.
On a torus, coincident cell addresses reduce these counts.

For a fixed native level \(j\), the owner level is \(j\) or \(j+1\).
There are at most two recursive occurrences of a cell, by the ported cut lemma.
Thus one safe covering-and-slot bound is
\[
 C_{\rm d}^{\rm slot}=4A_c\mu L^4.
 \tag{6}
\]
This counts actual slot records, including their finite types.
It makes no bound on the number of analytic factors using one slot.

Induction over the finite history now proves FCO-slot.
The initial stock uses the ordinary case.
Every stage either preserves stock, makes the located coordinate change, or deletes integrated stock.
An island cuts the existing record without copying its interior.
Carrying preserves addresses; healing deletes them.
Sections 3–4 cover every branch of these moves and preserve the same constants.
This is stopping condition **(a)** for the specified-rule FCO-slot theorem. \(\square\)

## 5. Reconstruction reads are filed where they occur

This applies the route suggested by finding 10 of the check.
At a stage, write \(\Psi_W(s,a)\) for its reconstruction, as in Y 75906–75932.
The coordinates \(a\) are the collar nonpivots from (1).
The arguments \(s\) are retained inner or shell coordinates with the owners already specified.
The datum \(W\) uses its actual coarse rows.
Untouched exterior arguments keep their existing visible or stored addresses.

File each primitive reconstruction input at that input's producing stage and native slot.
Stop at an actual stored or determining argument.
If a read uses an earlier reconstruction, follow that earlier recorded recipe.
Do not expand an independent outgoing argument by the forward map of the chart being inverted.
Each such descent removes a later chart from the finite stack, so it terminates.
Y 75890–75904 requires the old centre to be read at reconstructed exterior data.
The same passage retains each old indicator on its complete original carrier.
Nothing here changes those functions or their carriers.
A later evaluation of their composition therefore creates no additional stored coordinate or old outcome letter.
This proves the needed storage assertion through reconstruction.

It proves no spatial bound for the complete composed read region.
Extend \(\Psi\) by the identity on untouched arguments.
For an old indicator \(F\), a sufficient read set is given by
\[
 \operatorname{Read}(F\circ\Psi)
 \subseteq\bigcup_{b\in\operatorname{Read}(F)}\operatorname{Read}(\Psi_b).
 \tag{7}
\]
Knowing where the arguments in (7) are stored does not place this union near the present reader.

**Handoff: FCO-read.** The history-product/restriction consumer at SA 18878–18927 must control complete move read regions.
It must retain the full background boxes, original indicator carriers, gauge and reference factors, and class windows.
The source requires this before commuting independent moves or restricting a history to full clusters.
That named input is not a premise of FCO-slot or of the two counts below.
No history-product theorem is claimed here.

## 6. Restated UO2-geo

Retain the prescribed revised rules, H-LF and the fixed finite record grammar.
For the consumers in this lane, UO2-geo now means:

1. Each stored coordinate has one creation identity and one owning historical cell occurrence.
   Carries and reconstruction reads do not create copies.
2. Its native level is the owner level or one below it.
   Stored slots, added storage-collar slots, visible slots and discrete anchors have the cell-collar inclusion of FCO-slot.
3. The per-owner and per-site multiplicities are (4)–(6).
   They concern slots, not full read stencils or analytic factor incidences.

Sections 3–4 prove these three clauses from the stated rules.
This replaces the stronger target in `uo2-geo.md`, section 5, for its reserve and code consumers.
It does not replace action supports by determining supports.

For the visible-label load, the already proved argument in `sa-2.13.md`, (6.2)–(6.4), gives
\[
 \mathscr L_q(\mathcal S)
 \le 8qN_k+\lambda_q
       \left(V_{\rm outside}+\sum_{X\ {m outer\ mark}}v^\natural(\omega_X)\right),
 \qquad q\ge0,
 \tag{8}
\]
with a fixed coefficient \(\lambda_q\) affine in \(q\).
The constants absorb the cell-collar and finite-type counts above.
Y 78867–78937 gives the corresponding source calculation.
This is a port of the visible-load argument, not a bound on every historical analytic read.

## 7. The code count

Use the original outer active address set \(A\).
The collar addresses are determined by its cells; they are not independently chosen cells.
The replay record keeps all actual selector outputs, seam tags, stopping data and frame slots.
Inner island records remain in their own factors.
This is the record of `geoh-o2.md`, section 8.

Let \(K\ge2\) bound its bundled local alphabet.
Let the header at a component of level \(n\) have at most \(3K_f(R_n+1)^p\) possibilities.
These constants and \(J,\tau\) are fixed before the coupling floor.
By FCO-slot there are at most
\[
 A_cJ\mu L^4(MR_n)^4
 \tag{9}
\]
local discrete slots per owner occurrence.
The existing scale estimate is
\[
 \log(R_n+1)\le c_R\ell_n,
 \qquad c_R=\log(2^{r+1}L)+r.
 \tag{10}
\]
See `geoh-o2.md`, section 8, using GEOH's common scale sequence.

Multiply the local alphabet sizes and the component headers.
Use one creation bit per cell and \(\ell_n\ge1\).
The number of components is at most the number of their cells.
Thus Sussman–Alpoge's multiplication, Y 74649–74669, gives
\[
 \boxed{\#\{\text{non-frame outer codes over }A\}
       \le \exp\{b_{\rm code}V^\circ(A)\},}
 \tag{11}
\]
where the sufficient constant is
\[
 b_{\rm code}
 =\log2+A_cJ\mu L^4\log K+\log(3K_f)+pc_R.
 \tag{12}
\]
The bound is uniform in the frame choices.
Chronological replay recovers every discrete move from this code.
Earlier stages passed; stages after the recorded stop are unread.
A coordinate or background value is an integration argument, not a code letter.
This supplies the spatial slot premise left open in the earlier conditional count.

For the positions of \(A\), port the rooted-address argument of Y 74615–74647, also SA 18673–18690.
The graph degree satisfies \(D\le L^4+3^4+2\).
A canonical depth-first traversal gives at most \(D^{2(N-1)}\) rooted address sets of size \(N\).
Since \(V^\circ\ge N\), (11) implies
\[
 \boxed{
 \sum_{\omega^\circ\ne\varnothing}
 |W_4|^{-1-f(\omega^\circ)}
 e^{-c_{\rm ent}V^\circ(\omega^\circ)}\le1,
 \qquad
 c_{\rm ent}\ge b_{\rm code}+2\log D+\log2.}
 \tag{13}
\]
Indeed, after the frame averages, the sum is bounded by
\(D^{-2}\sum_{N\ge1}2^{-N}\le1\).
Each frame slot is averaged once, including the root.
This is the entropy port in SA 18702–18717.
There is no factor for the height, torus volume or number of later reads.

## 8. SA's original stored-site reserve

Keep Sussman–Alpoge's reserve exactly:
\[
 v(\omega)=\sum_j(\log x_j)s_j(\omega).
 \tag{14}
\]
Here \(s_j\) counts the actual stored sites at native level \(j\).
It includes assigned storage collars and the fixed coordinate multiplicities.
SA 17274 and 18087–18091 specify this convention.
It does not count every later evaluation as a new site.

The weight comparisons have already been proved in `geoh-o2.md`, section 3:
\[
 0<\log x_n\le\ell_n,
 \qquad \log x_{n-1}\le2\ell_n.
 \tag{15}
\]
They use the IN1 tube, bounded adjacent frame drift and a common scale sequence.
Retain the existing floor \(X_0\ge4\overline B\).

An owner occurrence has at most \(A_c(MR_n)^4\) coarse sites.
Each has assigned native multiplicity at most \(\mu L^4\).
By (15), its contribution to (14) is at most
\[
 2A_c\mu L^4\ell_n(MR_n)^4.
\]
Summing over the occurrences in the existing recursive volume proves
\[
 \boxed{v(\omega)\le C_vv^\natural(\omega),
        \qquad C_v=2A_c\mu L^4.}
 \tag{16}
\]
The cut-boundary multiplicity is already in \(v^\natural\).
It supplies no additional factor here.
This is the reserve comparison of `uo2-geo.md`, (15), with a cell collar replacing an \(M\)-layer collar.
It uses the source's actual reserve, not a replacement definition.

For any requested \(c_r\ge0\), choose the natural-volume price \(q=C_vc_r\).
Then
\[
 e^{c_rv(\omega)}\le e^{qv^\natural(\omega)}.
 \tag{17}
\]
This inequality holds before integration or the pair supremum.
It changes neither the stored measure nor its densities.
Thus any supplied bound with the right-hand weight pays SA's requested reserve on the left.
FCO-slot alone supplies no analytic mass estimate.

For clarity, the source's credit reserve also keeps its original premises.
Sussman–Alpoge, SA 18606–18652, proves
\[
 \mathfrak F(x)
 :=\sum_tG_tn_t^{\rm cr}+\sum_tP_tn_t^{\rm mk}
       -\sum_{u\in\mathcal G(x)}c_{n(u)}|C(u)|_{n(u)}
 \ \ge\ 2\sum_tP_tn_t^{\rm cr},
 \tag{18}
\]
provided
\[
 c_t\le r_t=C_3c_1M^4R_t^5,\qquad
 G_t\ge2P_t+C_2T_tr_t,\qquad P_t\ge C_2T_tr_t.
\]
Its waiting bound and creation/mark credits are separate inputs.
The source includes the volume, entropy and coordinate prices in \(c_1\).
Equations (12) and (16) now give their fixed slot contributions explicitly.
With \(\mathfrak p_0\ge6r+1\), its stated logarithmic floor is imposed after that fixed price.
For the outer recursion, the same port is SA 18847–18857:
\[
 \sum_e\Gamma_e-(C_5+C_7+q+c_{\rm ent})V^\circ
       \ge2\sum_tP_tn_t^{\rm cr},
 \tag{19}
\]
with its actual envelope and fresh cut-leaf witness premises retained.
Equations (18)–(19) are conditional ports, not consequences of geometry alone.
FCO-slot supplies the stored-slot price required to use them.

## 9. Result

**Stopping condition (a): FCO-slot is proved for the specified revised rules.**
The new step is the case check in section 3 and its uniform count in section 4.
The chain, coordinate conventions and counting method are credited ports.
The result is a written implication from the stated operation rules, H-LF and finite grammar.
It does not establish those rules for a different operation or discharge analytic admission.

The proof restores UO2-geo at its slot scope, the code bound (11)–(13), and the reserve comparison (16).
The full-read question is assigned to its history-product consumer in section 5.
This lane wrote only this file. It changed no registry row or scientific status.
The shared checkout advanced during writing; the proof's repository inputs remained unchanged from the source revision.
Written and author-checked by Codex; not yet checked by the other model.

| Claim | Standing in this text | Source or limit |
|---|---|---|
| As-made chain and prepared containment | Ported, previously checked by Claude | Y 63713–63825; `uo2-geo-check.md`, findings 1–3. |
| Owner rules, disjoint windows and cut multiplicity | Ported, previously checked by Claude | Y 78906–78916, 74218–74271; SA 17440–17449. |
| Ordinary storage, collar, rim and cut-off slots | Proved by the case check | Section 3; SA 17354–17358, 17453–17459, 17518–17532. |
| Prepared means, stopped prefixes and seam coordinates | Proved from the ported coordinate rules | Section 3; Y 73160–73194, 75845–75960. |
| Island storage, including older native levels | Proved from the retained-record rule | SA 17418, 17642–17654; no CA-to-revised dictionary assumed. |
| Live-strip shortcut at level \(m+1\) | Existing checked result, usable after its dictionary match | `geoh-live-ab.md`, assertions 3–4; GEOH-O1 remains separately owned. |
| FCO-slot and its multiplicities | Proved here from the stated rules | \(c=6\), \(\mu=20\tau\), equations (5)–(6). |
| Stage filing through reconstruction | Proved for stored arguments | Section 5; complete composed read regions are not bounded. |
| Restated UO2-geo | Proved at slot scope | Section 6; visible terminal load retains \(N_k\). |
| Code count and frame-normalized entropy | Ported count with its slot premise supplied | Equations (11)–(13); Y 74615–74669, SA 18702–18717. |
| Original reserve comparison | Proved with the source's \(s_j\) | Equations (14)–(17); weight inputs retained. |
| Source credit reserve | Conditional port | Equations (18)–(19); waiting, witness and envelope inputs remain. |
| FCO-read | Named input for the history-product row | SA 18878–18927; outside this slot theorem. |
| First open input | None within the stated FCO-slot theorem | Beyond it: FCO-read for history products. GEOH-O1 and analytic admission retain their separate owners. |
