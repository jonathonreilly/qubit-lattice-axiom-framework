# GEOH-O6: complete carriers and geometric Lift

Codex, 2026-11-08. Checkout `80d70474cd39fe476ac1b11aa86be01953967036`.
FINISH row 487. Research text, not an audit. This note grants no status.
No computation supplies a proof step.

**Result: stopping outcome (c).** LIFT-ONE in §6 remains open after three distinct routes.
The unrestricted indexed-carrier contract fails by §5.
That is not promoted to a physical-history counterexample.
Section 4 supplies a local member bootstrap, and §7 checks a proposed contract change.

## 1. Target and prior work

The target is GEOH-O6 in `open-registry.md:231`.
It concerns the complete constructed carriers and reads in CLS.
The two consumers are `cls.md:22` and `cls.md:462`.
The first requires embedding with read margins.
The second extends this requirement to constructed carriers.

Use the literal geometric definition in `geoh.md:261`.
A complete read must fit inside one filled coordinate box on the covering lattice.
Each side must be strictly less than half the corresponding torus period.
Collections compared in one chart need a common such box.
This is stronger than lifting a path, or choosing representatives of its vertices.

`prior/geoh-o6.md` is absent. The prior record is `prior/geoh.md`, especially O6 and verdict item 1.
Its bounded-box Lift criterion is already available in `geoh.md:263–278`.
It does not supply the spans of CLS's complete family.
The registry assigns this question to GEOH-O6.
CLS-READ, CLS-HISTORY and O-live-geometry retain their separate matching questions.
This note does not take over those rows.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the source constructions below.
Credit Tadeusz Bałaban for the large-field method.
Source keys are:

- **SA:** [YM4_sketch_500.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), commit `31a47c543775`.
- **I:** [theorem_0_complete_account_raw_I.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), the same commit.
- **N:** [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex), commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.

The full-read index and its neighbouring entries were consulted before the source excerpts.
SA and I were fetched once from the specified pinned URLs.
N was already present at the supplied `/tmp/ym4_1400.tex` path and was reused.
The workflow file is absent at the pinned checkout; its copy on `origin/main` was read without checkout.

## 2. What the proposed ports supply

These are source classifications, not new scientific status.

| Source | Statement and source standing | Use here |
|---|---|---|
| N 61908–61914 | The induction assumes the torus floor `ell L^(K-j) >= 2 L^11 M check-R_j`. Its theorem is conditional on the actual-history inputs. | Input floor for bounded operation boxes. |
| N 63684–63692; SA 17575–17583 | The small, quiet, quarantined class has bounded operation boxes. The nonwrapping conclusion follows conditionally from the floor. | Ported bounded-class geometry only. |
| N 2320–2332 | C2 requires constructive histories and preserved margins. Other carriers retain their winding in torus estimates. | Input contract. It does not assert universal nonwrapping. |
| N 70104–70112 | The short-carrier argument supposes a complete carrier inside a filled nonwrapping box. | Input to that argument, not a span proof. |
| N 82915–82923; SA 5883–5889 | Companion compatibility is required on common nonwrapping lifts with collars. | Separate function-identity input. Geometric embedding does not prove it. |
| I 85575–85644 | Live-region geometry is headed “Proof outstanding”; the listed clauses are hypotheses. | No supplier of complete CLS Lift. |

The relevant SA index entries are in chunks 04, 05 and 16.
They distinguish C2, pointed domains, retained slots, the test recursion and the small operation class.
The CA index for 4.12–4.19 ends before I's live-geometry package.
That later package was read at its supplied lines.

## 3. The actual CLS set constructors

Work at level `j`, in units of its `M`-cubes.
Use `p_j` for the number of those cubes in one torus period.
The torus metric and the metric inside a nonwrapping chart are distinct until a chart is supplied.

| Constructor | Complete geometric content | Source |
|---|---|---|
| Island birth, continuation or swallowing | `U_j=N_2 H_j`; `R_j=N_c U_j` united with every projected predecessor `pi M_(j-1)`. | CLS 19–40 |
| Recursive collars | `rho_j=ceil(eta s(R_j))`; `Rhat_j=N_(rho_j+2)R_j`; `M_j=N_(rho_j+3)R_j`. | CLS 29–40 |
| Old slot and projection | Its formation-time family, domain and length remain recorded. Later projection carries its tree and excused members. | CLS 42, 143–147 |
| Complete presentation reads | `X(f)` lies in `X_f`; the required coverage includes stencils, endpoints, pins and stored reads. | CLS 44–59, 147 |
| Filing base | `N_f=X_f` united with `Rhat_j(alpha)` for every core met by `T_f`. | CLS 229 |
| Boolean carrier | `Y_(f,V)=N_1(N_f union V)`, for `V` contained in the torus cube set outside `N_f`. | CLS 229–234 |
| Connecting graph | `T_f`, radius-`c+1` balls, root-MST geodesics, core connectors and neighbour stars at `V`. | CLS 237–246 |
| Filled carrier | `Y*_(f,V)=Y_(f,V) union vertices(U_(f,V))`. Here “filled” means adding this graph. It need not be a coordinate box. | CLS 276 |
| Cluster carrier | Further incompatibility joins and Gaussian-read stars, with their complete read radii. | CLS 278 |

The Boolean carrier is defined before any choice of its connecting tree.
Adding paths or complete margins can only enlarge it.
The parameter `V` has no cardinality, tree-length or span cutoff in CLS's definition.
Whether a label carries a nonzero emitted term is a separate question.
An arbitrary index in a majorant is not, by itself, a nonzero-term counterexample.

## 4. Span bounds before the CLS side estimates

Here is a bootstrap for the recursive members alone.
It does not invoke CLS's conditional side estimates or assume Lift for their output.
Its inputs are supplied hub boxes, G, Drop and Mon.
Their realization on every physical history remains their stated supplier's obligation.
Take CLS D2–D3's constants: odd `L>=27`, `C>=1`, integer `c>=0` and `0<eta<=eta_sharp`.
In particular `eta<=1/8`.
The scalar contraction mechanism is already in CLS Lemma 3.
The additional step here constructs each chart before using the core's coordinate span.

Write `r_j=check-R_j` and
\[
 a_j=CLr_j+6+2c.
\]
Supply a lifted box for each hub `U_j`, of side at most `CLr_j+6`.
Let the nonnegative integer `b` bound the additional margin in these cube units.
This statement concerns a specified fixed margin.
It does not identify all physical reads with such a margin.
The early-order conclusion requires `b` fixed before `kappa`, independently of `M` and `bar-kappa`.
Suppose
\[
                 p_j>2(2a_j+16+2b).                 \tag{1}
\]

**Local bootstrap.** Every recursively constructed `M_j`, together with its `b`-neighbourhood, fits in a filled box of side at most `2a_j+16+2b`.
This is uniform in the finite age and number of predecessors.

*Proof.* Let `e_j` be the least integer with `R_j subset N_(e_j)(N_c U_j)` on the torus.
The core uses only previously constructed members, so this definition precedes its new collar.
At a predecessor-free birth set `e_j=0`.
For a continuation, or a swallowing birth, the required upper recursion is
\[
 e_j\le\max_{\alpha\mapsto\beta}
 \left\{{3\over2L}e_{j-1}(\alpha)+{\eta a_{j-1}\over L}+2\right\}.
                                                        \tag{2}
\]
This upper sequence is a bound, not a change to the set constructor.

To justify (2), suppose the parent core lies in `N_e(N_c U)`.
Its span is at most `a+2e` in its already constructed chart.
Thus its actual collar radius obeys `rho<=eta(a+2e)+1`.
Its member lies in `N_(e+rho+c+5)H`.
Coarsening and Mon place its image within
\[
 \max\{0,\lceil(e+\rho+c+5)/L\rceil-c\}
 \le (e+\rho)/L+32/27
\]
layers of the new `N_c U`.
Here `L>=27` and `c>=0`.
Since `eta<=1/8`, this is at most the right side of (2).
Coarsening this distance uses the periodic graph only.
Indeed, lift a shortest coordinate displacement; rounding divides its size by `L`, with a ceiling.
No chart for the whole carrier is used.

Follow a maximizing predecessor back to its birth.
Drop gives `a_(j-k)<=L^ceil(k/2) a_j`.
Consequently
\[
\begin{split}
e_j
&\le \eta a_j\sum_{k\ge1}(3/2)^{k-1}L^{-\lfloor k/2\rfloor}
       +2\sum_{k\ge0}(3/(2L))^k\\
&\le {38\over33}\eta a_j+{36\over17}
 <2\eta a_j+3.                                      \tag{3}
\end{split}
\]
For the first sum, pair consecutive terms after its initial term `1`.
It is at most `1+(5/3) sum_(m>=1)(1/12)^m=38/33`.
The second uses `3/(2L)<=1/18`.
These bounds follow from finite geometric sums and their limits.

Now construct the current chart before defining `rho_j`.
The union defining `R_j` lies in `N_(e_j)(N_c U_j)` on the torus.
Condition (1) lifts that entire neighbourhood into the hub's enlarged box.
All predecessors meet this common box through their projected hulls, by Mon.
This supplies the common lift for their union.
Its span is at most `a_j+2e_j`.
Therefore
\[
 \rho_j\le\eta(a_j+2e_j)+1\le2\eta a_j+2,
\]
and the complete member box has side at most
\[
 a_j+2e_j+2\rho_j+6+2b
 \le (1+8\eta)a_j+16+2b
 \le 2a_j+16+2b.                                    \tag{4}
\]
Condition (1) makes this box smaller than half the period.
This completes the finite induction, including every swallowing.
Compatible deck translations preserve aligned coarsening. ∎

The proof uses supplied hub charts. It does not derive them from CLS's output bounds.
With `r_j>=1`, (4) is at most
\[
        (2CL+28+4c+2b)r_j.                          \tag{5}
\]
The already proved GEOH torus-floor criterion applies to this constant.
This repairs the local induction's circular use of Lift, under its explicit hub inputs.

**Trees and complete carriers.** Let a connected graph have `n` edges.
Lift a spanning tree from a root by nearest coordinate increments.
Its coordinate span is at most `n` in each direction.
Attach any met member through its own chart at a meeting vertex.
If each member has side at most `S`, their union fits in a box of side at most `n+1+2S`.
The extra `1` includes the cubes themselves, not just their indices.
An additional margin `b` raises this to `n+1+2S+2b`.
If this is less than `p_j/2`, every attachment agrees in that common box.
Otherwise this argument supplies no local chart.
It does not erase a periodic cycle in the projected carrier.

For CLS's connecting graph, `n` includes the old tree, all root-MST paths, connectors and neighbour stars.
Its actual constructor has no bound on `d_f`, `m_(X(f))(W union V)` or `|V|`.
CLS (14) bounds its cost in those quantities. It does not bound them by `r_j`.
Cluster unions add their constituent lengths and joining paths, with no bound on the number of constituents.
Thus (4) controls recursive members, but supplies no uniform span for the complete family.

The margin accounting is literal:

- Recursive core margins are `rho+2` and `rho+3`, already included in (4).
- A presentation must include every connected read stencil, endpoint, pin and stored read. TD2 20–23 supplies the stencil convention; actual coverage remains CLS (4).
- Boolean filing adds one whole cube layer. DRL 397–399 attributes it to the completed source rows.
- Graph filling adds all its paths, not a bounded collar of the original disconnected carrier.
- Clusters add Gaussian stars of radius `c_G^pair` and incompatibility paths. These are CLS 278 and DRL 482–484.

No unspecified read is absorbed into the symbol `b`.
The obstruction below is already present before any missing margin is added.

## 5. A winding label generated by the printed filing rule

Fix a level with even period `p`, and any actual filing input `f`.
Its nonempty complete read set contains a cube `x`.
Translate coordinates so `x=0`.
Let
\[
 C_p=\{(t,0,0,0):t\in\mathbb Z/p\mathbb Z\},\qquad
 V=C_p\setminus N_f.                                \tag{6}
\]
This is an allowed Boolean index in CLS 229–233 and DRL 272–280.
The constructor gives
\[
 C_p\subset N_f\cup V\subset Y_{f,V}\subset Y^*_{f,V}.
                                                               \tag{7}
\]
Each vertex of `V` connects to `x` inside `N_f union V`.
Thus DRL Theorem 2's component support rule does not remove this index.
This is the printed constructor, not a freely selected upper tree.
Its genealogy in the filing operation is explicit:
start with `N_f`, visit `x+e_1,...,x+(p-1)e_1`, and add each cube not already present.
The resulting index is exactly (6).

**Span obstruction.** No filled box of side less than `p/2` contains the image of `C_p`.
The two cubes with indices `0` and `(p/2)e_1` have periodic coordinate distance `p/2`.
Any representatives differ in that coordinate by at least `p/2`.
A smaller box cannot contain both.
Using closed cubes only increases the necessary side.
Every complete margin and every further filling preserves this obstruction. ∎

The simpler index `V=all cubes minus N_f` gives `Y_(f,V)=the whole torus`.
Increasing the torus floor does not help either example.
The construction forms the corresponding long index on the larger torus too.

Here is the associated geometric history pattern.
It makes explicit where an actual-history counterexample would need more than an index.
Create one isolated failure cell at level `1`.
Take no later creation, joining or failure during a quiet window.
The region update is exactly
\[
 Z_1=\mathsf{bx}(N_4\{0\}),\qquad
 Z_t=\mathsf{bx}(N_{10}\widehat Z_{t-1})\quad(t>1).
                                                               \tag{8}
\]
This follows from GEOH Input R and SA's test rule, indexed at SA 17317–17332.
For this labelled pattern take a constant rounded radius `N_t=R` through `k=R+1`.
Then `N_k=k-1`, and no earlier operation is eligible.
The bounded quiet component is then in the operation class.
This is N 63684–63692's isolated-cell example; its geometry is ported, not reproved.
Select the island outcome at level `k`.
SA 17415–17419 retains its operation, variables, measure and factors.
At the next step its old island term is a TD2 exempt input.
Its first recursive core is `N_c U_k`; later cores use every projected predecessor as in CLS (1).
Choose the period large enough that the isolated component leaves distant gas cubes.
At that filing step use (6), or the full complement index.

This specifies a permitted labelled history and its exact constructed carrier.
It does **not** certify a nonempty physical fibre for all chosen test outcomes.
It also does not prove that the selected Boolean coefficient is nonzero.
The old operation and actual-response identifications are inputs in the cited construction.
An assumed realization of this pattern cannot serve as a counterexample under the question's stronger actual-history test.

The conclusion proved so far is exact but narrower:
**the literal requirement on every indexed constructed carrier fails whenever a filing input exists.**
It does not prove failure for a nonzero term on an exhibited physical history.

## 6. One supplier, attacked by three routes

**Stopping outcome: (c).** The supplier below remains open after the three routes written here.
The labelled obstruction in §5 is not promoted to outcome (b).
No physical history and nonzero long coefficient have both been exhibited.

**LIFT-ONE (actual one-piece span).** There is an early finite constant `A` with the following property.
For every actual finite history, every level and every admissible volume, take an actual old exempt input `f`.
For every nonempty gas set `W` and Boolean index `V`, suppose `f_(W,V)` is not identically zero.
Then the assigned carrier `Y_(f,V)`, including its complete declared reads, lies in one filled covering-lattice box.
Its side is at most `A check-R_i` and strictly less than half the torus period.
Use common boxes whenever the piece's coordinates are compared.
The constant is independent of scale, volume and history.

This is a necessary sublemma of the requested full Lift.
It is still GEOH-O6, not a proposed new registry row.
Even a proof would leave later graph fillings and clusters to check.
A counterexample must specify an actual history and a nonzero piece, or another actual mandatory read.

### Route 1: close the geometric induction

The mechanism is contraction under coarsening, with a maximum over predecessors.
Equations (2)–(4) complete that argument for members without using CLS's conditional side bounds.
For the filing carrier, however, the next operation is union with `V`, at the same scale.
No factor `L^-1` acts on this union.

Take successive initial arcs of (6).
Before reaching half a period, their coordinate span grows by one at each new cube.
At the full cycle, (7) violates every half-period chart.
The history length and member excess have stayed fixed during these additions.
Thus no recurrence of form (2) bounds these spans.
The torus floor controls `r_i/p_i`; it cannot bound a freely growing arc in units of `r_i`.

**First failed step:** inferring a span bound for `N_f union V` from the bound for its recursive members.
To prove LIFT-ONE this route needs exact exclusion of the offending active indices.
G, Drop and Mon provide no such exclusion.

### Route 2: use Boolean cancellation and exponential response decay

DRL 272–280 defines the actual finite alternating sum.
Theorem 2, at DRL 348–364, supplies two zero rules:
`W` must lie in `N_f union V`, and every added cube must connect to a read stencil there.
The cycle (6) meets both rules whenever its selected gas cubes exist.

Here is a hand test of the proposed stronger cancellation argument.
Take `p` divisible by four and put
\[
 a=(p/4)e_1,\qquad b=(3p/4)e_1,\qquad W=\{a,b\}.
\]
For a local base near `0`, both can lie in the distant gas.
Consider the scalar polynomial
\[
 F(s,\zeta)=\epsilon\Bigl(\prod_{c\in C_p}s_c\Bigr)
                         \zeta_a\zeta_b.             \tag{9}
\]
At the corner `s=1_(N_f union A)`, with `A subset V`, its switch product is nonzero exactly when `A=V`.
The gas difference `D_W` keeps the product `zeta_a zeta_b`.
Therefore its Boolean coefficient is exactly
\[
                   F_{W,V}=\epsilon\zeta_a\zeta_b\ne0.
                                                               \tag{10}
\]
No numerical calculation is involved.
The polynomial is holomorphic and obeys the stated connected-support test.
On a prescribed finite polydisc, a positive sufficiently small `epsilon` meets any prescribed positive amplitude bound.
It can in particular carry an arbitrarily strong exponential penalty in `p`.
Such a penalty never makes (10) zero.

This tests only the cancellation, holomorphy and decay mechanisms being used.
It is not identified with the Yang–Mills response or an actual retained function.
Thus it is not a counterexample to LIFT-ONE.
It proves that these interface consequences cannot supply LIFT-ONE by themselves.

**First failed step:** replacing exponential smallness, or connected support, by exact vanishing beyond the local-chart span.
An evaluation of the actual response coefficients would be needed to settle that vanishing.
Neither the bounded-box port nor I's outstanding geometry evaluates them.

### Route 3: recover one chart by cutting, filling or exact refiling

First lift the cycle edge by edge.
Following its `p` positive unit steps changes the lifted coordinate by `p`.
The start and end represent the same torus cube.
A single-valued lift preserving all those adjacencies cannot identify them.
Deleting an edge produces a lifted path, but its vertex span is `p-1`.
It still cannot fit in a half-period box.
Graph filling and complete margins only enlarge its projection.
Changing the tree, root or torus seam therefore does not repair (7).

Next try an exact sum of terms on small charts.
Every half-period chart omits at least one of the antipodal cubes `a,b`.
Any function with all source and pair reads in such a chart has `D_a D_b=0`.
The same holds for a finite sum, or for a sum absolutely convergent at the four difference evaluations.
But (10) has `D_a D_b F=epsilon zeta_a zeta_b`.
Thus even exact refiling is not a consequence of locality terminology alone.
For the actual coefficients this method must first prove the corresponding mixed differences vanish.
Equation (9) again supplies a test of the method, not a physical counterexample.

Common-lift companions do not alter this conclusion.
N 82915–82923 imposes their identity when a common lift exists.
It does not produce a chart for a cycle or replace its coefficient.
N 70104–70112 assumes a filled box before its gluing argument starts.

**First failed step:** replacing a periodic carrier, with all its reads retained, by a single small chart.
A patch cover can retain the periodic carrier, but that changes the Lift contract.
It does not prove LIFT-ONE.

These are different mechanisms: geometric contraction, analytic cancellation, and exact localization by refiling.
Their failure is not a proof that LIFT-ONE is false for the physical construction.
It is the named stopping point allowed by the task.

## 7. Smallest proposed contract change and consumer checks

N's C2 already makes the relevant distinction, at 2320–2332.
Port its bounded-box requirement and its retention of winding carriers.
Do not import a new claim that every carrier has a chart.

The following changes concern the geometric interface only.
They are proposals in this file; no frozen consumer was edited.

**Replacement for CLS 22:**

> **Lift-local.** Supply compatible filled nonwrapping charts for hubs, recursive members and operation boxes, with every complete margin used in their local box arguments. Constructed tree, Boolean and cluster carriers are periodic cube sets. Keep their winding and use periodic graph distances and lengths. Require a common filled chart only when applying a local box argument or a companion comparison to the complete read region. Preserve D4 and every actual-domain, read and filing hypothesis on general periodic carriers.

**Replacement for CLS 462:**

> Choose the admissible torus/grid to embed the specified bounded local boxes with their complete margins, using independently proved spans. Keep all constructed carriers as periodic sets, including winding carriers. Invoke local box arguments and companion identities only on complete regions for which the required common chart exists.

This changes one quantifier: which sets must fit in a single chart.
It neither discards long coefficients nor changes their assigned carrier.
It preserves the complete-read requirement.
In particular it does not turn locality on restrictions of global pairs into full local-domain admission.

**Consumer at CLS 22.** Its geometric proofs can use this replacement as follows.

| CLS use | Check under the replacement |
|---|---|
| D3 and Lemmas 3–4: spans of cores and members | The local charts are still required. Section 4 constructs them from independent hub charts, G, Drop and Mon. Full local margins must be supplied. |
| Lemma 2: coarsening and family lengths | Lift a shortest displacement to prove the periodic coarsening inequality. An image tree is connected; remove cycles. Adding excused members weakens the same graph minimization. None of these steps needs a chart for the full tree. |
| Lemma 5: later projection | Project the old tree on the torus. Its vertices remain covered by that tree or by successor cores. The recursive inclusion supplies the latter. Additional physical reads remain the stated import. |
| Lemma 6: entropy | A periodic cube graph still has degree at most 80. Depth-first tree codes give the same count. Only individual member volumes use local side bounds. |
| Lemma 7: ordinary-distance estimates | Realize root-MST edges by periodic geodesics. Connect across an encountered core inside its supplied box. The gas gap is periodic. The proof sums path costs; it does not require one lift for their union. Its diameter is the periodic diameter. AG1 starts with a periodic lattice and the same sup-distance convention, at AG1 14–32. |
| Lemma 8: shell sum | For a fixed core point, choose one shortest representative of each periodic displacement. This injects each shell into the corresponding lattice shell. Hence the same upper shell count applies. The local core-volume bound is unchanged. |
| Lemma 8: filling | Keep `Y* = Y union vertices(U)` on the torus. Its spanning tree lies in `Y*`. No coordinate-box filling is inferred from this graph filling. |
| Cluster joins, CLS 278 | Incompatibility edges use periodic geodesics. Gaussian stars are periodic neighbourhoods of their specified radii. Their costs add as before. In-domain filing includes those paths. Analytic G-P and complete domains remain inputs. |

For the shell assertion, a shortest representative has each coordinate in a fixed interval of length `p`.
If its sup-distance is `n`, it lies on a face of `[-n,n]^4`.
Eight faces, each with at most `(2n+1)^3` integer points, give the original bound.
Boundary ties are assigned once. They cannot increase the count.
This proves the periodic version of the shell step directly.

These checks preserve CLS's conditional geometric estimates.
They do not prove its response, coefficients or full class transfer.
In particular, a local gauge construction on a filled box cannot be invoked on a winding carrier.
Such a carrier needs the torus version of the actual analytic supplier already demanded by D4.

**Consumer at CLS 462.** Row 10 chooses the final torus after the early constants.
For the specified local member margins, (5) gives an early constant
\[
                    A_{\rm loc}=2CL+28+4c+2b.
\]
Take the maximum with the independently supplied operation-box constants.
GEOH Theorem 4 then gives the uniform scale floor for those boxes.
No history-dependent tree length enters that choice.
N 61908–61914's floor remains a lower bound; increase it if these local constants require more space.
There is no finite floor that forces every new instance of (6) into a half-period box.
The replacement removes precisely that failed demand.

N 82915–82923's companion requirement stays conditional on a common complete lift.
The modification supplies no new companion identity.
CLS 373–376's Match-SF/O, Match-read/file, Match-heal/LD and Match-history also remain unchanged inputs.
They are assigned to other registry rows and are not attacked here.
Adopting this proposal would therefore remove the all-carrier span demand, not establish (Cls+).

## 8. Scope and claim record

The local bootstrap is a conditional geometric theorem with all inputs displayed.
The cycle argument is a theorem about the printed carrier constructor.
The polynomial is only a test of two proposed proof mechanisms.
It is not claimed to solve the Yang–Mills equations or realize any physical history.
No failure of these routes proves a general impossibility theorem.

The strongest remaining route for the unchanged contract is exact cancellation in the actual formation map.
It must establish LIFT-ONE, including complete assigned reads.
Neither a smaller amplitude nor a different spanning tree establishes that statement.
The proposed periodic contract avoids it, while retaining the existing analytic suppliers.

The prior digest's bounded-box results and frozen gate conclusions are preserved.
No source status, registry row or audit result was changed.
This is an author proof check only; no independent reader has checked this new note.

| Claim | Status and dependencies |
|---|---|
| Source classification of C2 and winding | **Ported from N 2320–2332:** input contract there, not an established full-history theorem. |
| Bounded quiet operation-box geometry | **Ported from N 63684–63692; SA 17575–17583:** conditional on the stated class and torus floor. |
| Torus admissibility floor | **Input**, N 61908–61914. GEOH 263–278 already proves the local floor criterion. |
| Short-carrier filled-box premise | **Input**, N 70104–70112. It is not a proof of that premise. |
| Companion agreement on complete common lifts | **Input**, N 82915–82923 and SA 5883–5889. |
| Live-region geometry | **Input**, I 85575–85644; explicitly proof outstanding there. |
| Recursive member chart bootstrap, (1)–(5) | **Proved here**, from supplied hub charts, G, Drop, Mon and the displayed floor. No CLS output-side estimate is used. |
| Complete fixed local margin bound | **Proved here** for the specified integer `b`; identification of every physical margin with such a bound is **input**. |
| Exact Boolean carrier and filled-carrier rules | **Input definitions**, CLS 229–246, 276; DRL 272–280, 397–399. |
| Winding indexed carrier, (6)–(7), has no local Lift | **Proved here**, for every nonempty filing input. No coefficient nonvanishing is asserted. |
| Isolated-cell geometric history pattern | **Ported from N 63684–63692**, with the island retention rule at SA 17415–17419. Physical realization and a nonzero selected coefficient are **input**, not proved here. |
| Failure of contraction to bound arbitrary attachments | **Proved here**, route 1, at the printed set-constructor level. |
| Boolean polynomial calculation and exact-refiling obstruction | **Proved here**, routes 2–3; neither is a physical counterexample. |
| Local/periodic replacement preserves the listed geometric arguments | **Proved here**, §7, retaining all their named analytic and matching inputs. |
| LIFT-ONE for actual nonzero pieces | **Input still open.** Three distinct routes fail at the steps specified in §6. This is stopping outcome (c). |
| First open input for the requested unchanged contract | **LIFT-ONE, §6.** No complete proof or actual physical-history counterexample is claimed. |
