---
claim_id: mobile_records_rare_formation_event_law_and_six_site_witness_bounded_theorem_note_2026-09-20
claim_type: bounded_theorem
claim_scope: "For a finite graph, a nonempty finite content menu, strictly positive symmetric pair weights, content-preserving pair-weight hops, and permanent births at rate epsilon times the local product weight: the rare-formation limit on slow time tau=epsilon t is a Markov process on motion communication classes, with off-diagonal rates equal to the class-stationary averages of the insertion rates; the pre-birth law is pi_C B / E_pi_C B. Where entire content-count sectors are connected, insertion rates are (n_a+1) Z_(n+e_a)/Z_n. Starting empty on the specified 2x3 graph with the six-axis weights (3/2,1/2,1), the probability all three contents agree immediately after the third birth tends to 2701/53880; the fixed-three-record static law gives 73/1440. The difference is -73/129312. These are conditional finite-model statements, not a physical law selected by the framework or a thermodynamic result."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mobile_records_rare_formation_event_law_2026_09_20.py
---

# The rare-formation law of mobile permanent records and an exact six-site witness

**Date:** 2026-09-20
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support. Independent audit has not ratified this proposal.

## Result and physical question

When records move without changing their content and empty sites can form new records, motion and formation must be analyzed together. Motion equilibrates arrangements within each accessible class. Formation samples those arrangements in proportion to their total birth rate, then changes the class. The following theorem constructs the resulting slow process; it does not replace it by an equilibrium ensemble.

**Target proved here.** On the finite model specified below, derive the limiting next-birth time, pre-birth configuration and post-birth motion class as formation becomes slow, and compute an exact same-menu example of its content law.

The example uses the six-axis menu and the neutral weights of the moving-record proposal: equal, opposite and orthogonal contents weigh `3/2`, `1/2` and `1`. Starting empty on a `2 x 3` window, let `E` mean that all three records have the same content immediately after the third formation event. Then

\[
\lim_{\epsilon\downarrow0}\Pr(E)=\frac{2701}{53880},\qquad
\mu_{N=3}(E)=\frac{73}{1440},\qquad
\lim\Pr(E)-\mu_{N=3}(E)=-\frac{73}{129312}.
\]

Here `mu_(N=3)` is the product-weight static law over all configurations with three records, including all content compositions. The event probability is evaluated at the third birth, not at a fixed observation time. This existence witness survives arbitrarily fast motion relative to birth; it is not a claim about every graph, weight or formation rule.

The useful positive output is the effective formation law. It specifies which ensemble a downstream calculation of ordering, correlations or field response would have to use for this candidate dynamics. The magnitude of a six-site discrepancy does not establish its large-volume behavior.

## Status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Which law is realized when content-preserving record motion and permanent new-record formation act together?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Determine the correlation and response of the derived growing process, with a quantitative finite-rate and volume-dependent mixing estimate."
conditional_surface_status: "Finite positive-rate candidate model; rare-formation limit at each fixed finite graph."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A self-contained finite Markov-process theorem and an exact content-law witness under explicit dynamics."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and model

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the lattice, local possibility domain, admissibility distribution and permanent records. The owner's moving-record reading permits a site to be reused after its record leaves. The following stochastic law, its menu restriction, rates and time parameter are **supplied model conditions**, not consequences of those axioms. No primitive or axiom is adopted here.

Let `G=(V,E)` be a finite simple graph, `M` a nonempty finite menu of size `q`, and `W(a,b)=W(b,a)>0`. A configuration `s` assigns either vacancy or one content to every site. Define

\[
 w(s)=\prod_{\{x,y\}\in E:\,x,y\text{ occupied}}W(s_x,s_y),\qquad
 u_{x,a}(s)=\prod_{y\sim x:\,y\text{ occupied}}W(a,s_y).
\]

Empty products are one. A neighboring occupied-vacant pair exchanges at rate `rho_xy w(s')/[w(s)+w(s')]`, with fixed `rho_xy=rho_yx>0`. This equals the local pair-weight acceptance because all unchanged factors cancel. The content travels unchanged. Let `Q` be this motion generator with row-sum convention `Q 1=0`. At an empty site `x`, content `a` is inserted at rate `epsilon u_(x,a)(s)`. Thus formation at `x` has total rate `epsilon Z_x`, with conditional content law `u_(x,a)/Z_x`. There is no removal, replacement or export from the finite graph.

Write `A(s,t)=u_(x,a)(s)` if `t=s^(x,a)` is one insertion, and zero otherwise; `B(s)=sum_t A(s,t)>0` in every non-full configuration. Hops preserve each content count. Let `C` index a **communication class of motion**, not merely an occupied-site set or a total number of records. Its partition function is `Z_C=sum_(s in C) w(s)` and `pi_C(s)=w(s)/Z_C`.

## Proof obligations

| Obligation | Disposition |
|---|---|
| Motion invariant law on each accessible class | Proved below by detailed balance. |
| Exact next-birth resolvent and its rare-formation limit | Proved below for arbitrary initial law on a finite class. |
| Class transition process and content-sector partition identity | Proved below, with connectivity hypotheses retained. |
| Six-site connectivity and numerical witness | Finite enumeration in the runner; the witness also has a separate combinatorial derivation below. |
| Uniform mixing estimate as the graph grows | Open; no exchange of volume and slow-birth limits is used. |
| Physical selection of these rates and a gravity/matter observable map | Open; not a leaf of the finite-model theorem. |

## Motion and the next-formation theorem

**Motion.** For a hop `s -> t`, `w(s) Q(s,t)=rho_xy w(s)w(t)/(w(s)+w(t))=w(t)Q(t,s)`. All allowed hops have positive rate. Therefore `pi_C Q_C=0`, and irreducibility on the finite class gives its unique invariant probability. Different classes can have the same content counts; neither content counts nor their relative probabilities are changed by motion.

**Next formation.** Fix a non-full class `C`, an arbitrary initial row probability `alpha` on it, and let `T_epsilon` be the next birth time. Put `D=diag(B)`, restricted to `C`. Before the birth, the killed generator is `Q_C-epsilon D`. Its occupation integral gives exactly

\[
 \Pr(s_{T_\epsilon-}=s,\ s_{T_\epsilon}=t)
 =\big[\epsilon\alpha(\epsilon D-Q_C)^{-1}\big]_s A(s,t). \tag{1}
\]

Indeed, the row at time `t` before any birth is `alpha exp[(Q_C-epsilon D)t]`; multiply its `s` entry by the insertion rate and integrate. Since `b_min=min_C B>0`, survival is at most `exp(-epsilon b_min t)`, so the integral exists.

For `h>=0`, define `v_epsilon(h)=epsilon alpha[epsilon(D+hI)-Q_C]^-1`. This is a nonnegative row and

\[
 v_\epsilon(h)(B+h\mathbf1)=1,\qquad
 v_\epsilon(h)Q_C=\epsilon[v_\epsilon(h)(D+hI)-\alpha]. \tag{2}
\]

The first identity bounds its total mass by `1/(b_min+h)`. Every convergent subsequence therefore has a nonnegative limit `v` with `vQ_C=0`. Irreducibility implies `v=c pi_C`, and the first identity fixes `c=1/(bar B_C+h)`, where `bar B_C=E_(pi_C) B`. The limit is unique, so

\[
 v_\epsilon(h)\longrightarrow\frac{\pi_C}{\bar B_C+h}. \tag{3}
\]

Taking `h=0` in (1) gives the pre-birth law and marked transition probabilities:

\[
 \nu_C(s)=\frac{\pi_C(s)B(s)}{\bar B_C},\qquad
 K_{CD}=\frac{1}{\bar B_C}\sum_{s\in C}\pi_C(s)\sum_{t\in D}A(s,t). \tag{4}
\]

Here `D` in `K_CD` denotes a target motion class, distinct from the diagonal matrix in (1). For a particular insertion mark `(s,t)`, its discounted probability `E[exp(-h epsilon T_epsilon) 1_(s,t)]` is `[v_epsilon(h)]_s A(s,t)`. Equation (3) is the transform of an exponential waiting time of rate `bar B_C` and a mark with probability `pi_C(s)A(s,t)/bar B_C`, independent in the limit. Thus on slow time `tau=epsilon t`, successive classes have rates

\[
 \bar Q(C,D)=\sum_{s\in C}\pi_C(s)\sum_{t\in D}A(s,t),\quad D\ne C;\qquad
 \bar Q(C,C)=-\bar B_C. \tag{5}
\]

The strong Markov property iterates the next-event result. There are finitely many states and at most `|V|` births, so convergence is uniform over the possible entry states and suffices for each finite sequence of births and its slow waiting times. Full configurations are absorbing, with `bar B_C=0` and a zero generator row. No uniform-in-volume theorem is inferred.

For any function `f` on a class, (4) also gives

\[
 E_{\nu_C}f-E_{\pi_C}f=\frac{\operatorname{Cov}_{\pi_C}(f,B)}{\bar B_C},\qquad
 \|\nu_C-\pi_C\|_{\rm TV}=\frac{E_{\pi_C}|B-\bar B_C|}{2\bar B_C}. \tag{6}
\]

This is ordinary rate-biased event sampling. Multiplying all birth rates by a small common factor changes the waiting times; it cancels from (4).

## The content-count process when its sectors are connected

For a count vector `n=(n_a)`, let `Omega_n` contain every configuration with these counts and `Z_n=sum_(Omega_n)w`. **Assume each source sector used is one motion class.** Then its average rate for adding content `a` is

\[
 r_{n,a}=\frac{1}{Z_n}\sum_{s\in\Omega_n}w(s)\sum_{x\text{ empty}}u_{x,a}(s)
 =\frac{(n_a+1)Z_{n+e_a}}{Z_n}. \tag{7}
\]

To prove the second equality, pair each summand with its child `t=s^(x,a)`. Its weight is `w(t)`. Every child is counted exactly `n_a+1` times, once for deleting each occurrence of `a`. This identity sums over the complete source sector; replacing a smaller class by that sector without checking accessibility is unjustified.

Let `R_n=sum_a r_(n,a)`. Starting empty, define `p_N` as the limiting law of content counts after the `N`th birth as `epsilon -> 0`, at fixed graph and motion rates. It obeys

\[
 p_0(0)=1,\qquad
 p_{N+1}(m)=\sum_{a:m_a>0}p_N(m-e_a)\frac{r_{m-e_a,a}}{R_{m-e_a}}. \tag{8}
\]

This is a constructive law, including the composition carried forward from every earlier birth. The static fixed-number comparator instead assigns `Z_n / sum_(|m|=N) Z_m`. Equation (8) includes the source-sector denominators `R_n`. It is not a claim about counts conditional on a fixed physical time, where residence times also matter.

## Six-site witness: hand derivation and exact computation

Use sites `0,...,5` and edges `(0,1),(1,2),(3,4),(4,5),(0,3),(1,4),(2,5)`. Let `M={0,...,5}`, antipodes `a xor 1`, and weights as stated up front. Set all edge proposal rates to one. All 28 count sectors with at most two records are connected: the runner traverses all their configurations, 577 in total, with the declared vacancy hops. This checks exactly the accessibility needed by (8) through the third birth.

Each row of `W` sums to six. The graph has seven edges and eight non-edge pairs. For two identical records of a specified content,

`Z_(2e_a)=8+7(3/2)=37/2`.

For one record of each of two opposite contents `Z_(e_a+e_b)=2[8+7(1/2)]=23`; for two orthogonal contents it is `30`. The total two-record partition function is `540`. The content law after two births is its static law: all single-record content sectors are symmetry-related, have the same exit rate, and insertion counting in (7) supplies the factor two. Thus the probability that the two records agree is `37/180`.

For a pair of identical records, a prospective empty site reads zero, one or two of them. Its total insertion weight is respectively `6`, `6` or `13/2`. If `c(s)` counts their common neighbors, `B(s)=24+c(s)/2`. Common-neighbor pairs are nonadjacent, so their existing pair weight is one. The sum of common-neighbor counts over all unordered pairs is

`sum_x binom(deg(x),2)=4 binom(2,2)+2 binom(3,2)=10`.

Consequently `R_(2e_a)=24+5/(37/2)=898/37`. The same count gives `R_(e_a+e_opposite)=542/23`, while `R_(e_a+e_orthogonal)=24`.

Among the twenty three-site subsets, two have no internal edge, eight have one and ten have two. For three identical contents,

`Z_(3e_a)=2+8(3/2)+10(3/2)^2=73/2`.

Every induced three-site graph is a forest. Summing the content at a leaf multiplies its partition function by six, so its total content-summed weight is `6^3`. Hence `Z_(N=3)=20*6^3=4320`, and the static all-identical probability is `6(73/2)/4320=73/1440`.

Equation (7) gives the rate for a third copy of `a` from two copies as `219/37`. Therefore the formation-event probability is

\[
 \frac{37}{180}\frac{219/37}{898/37}=\frac{2701}{53880}.
\]

Subtracting the static value gives the quoted `-73/129312`. The runner separately enumerates every configuration through three records, directly sums every insertion rate, and checks (7). It also obtains the complete content-count distance `811/387936`. This is a finite rational witness, not a fitted phase boundary.

Within the two-identical-record class, (6) gives `||nu-pi||_TV=125/16613`. A second computation forms its full 15-state killed motion generator and solves (1) at nonzero formation rates. At `epsilon=1/1000`, the all-identical probability is `2851401694918427/56880888215238000`; the absolute distance to the proved limit is below `6*10^-7`. This finite-rate value concerns this particular generator, not a general error bound. The initial law after the second birth is exactly the static two-record law for every positive epsilon here: with one record all empty-site normalizers are six, so the total birth rate is constant at thirty, and insertion flux into a two-record configuration is proportional to twice its static weight.

## Scope checks and remaining work

Constant weights `W=1` give spatially uniform births, constant `B=q(|V|-N)` and independent uniform new contents; the event and static content laws agree. A three-site path with two distinct contents and one vacancy has two motion classes, distinguished by the order of those contents. The general class theorem covers that example; the complete-sector version is used only with its connectivity hypothesis checked.

For the finite closed graph, a useful separate bound is also immediate. If `d` is its maximum degree and `w_min=min W`, each empty site has total birth rate at least `epsilon b_*`, where `b_*=q min(1,w_min^d)>0`. For the vacancy count `V_t`, motion contributes zero and `L V=-epsilon B`, so

`E V_t <= V_0 exp(-epsilon b_* t)` and `Pr(T_full>t) <= V_0 exp(-epsilon b_* t)`.

The runner checks the generator identity against explicit transitions. Boundaries allowing export, time-dependent rates, zero weights and growing windows require separate treatment. This bound is not an argument against ongoing formation on the infinite lattice.

The finite rare-formation theorem has no missing mathematical lemma within its stated domain. The next stronger target is a quantitative comparison at increasing volume and finite formation rate, followed by correlations and sourced response of that process. Uniform control of motion relaxation and of formation-event sampling is an unresolved bridge to that target; merely restating an equilibrium correlation formula would not supply it. No assertion about clumping thresholds, a Newtonian field, quantum dynamics or TOE closure follows here.

## Prior work, imports and review record

The immediate comparison is the rare-formation remark in PR `#8530`, frozen at `1c1a56df6c979401f94ff7191a5b18a1236f1b74`, in `ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md`. It describes configurations immediately before formation by the static motion law. Equations (4) and (6) provide the rate-weighted version for the continuous-time birth process specified here. The parent's detailed-balance identity for motion remains valid. All model definitions and proofs used here are restated and derived locally; that open PR is provenance, not an uncarried theorem dependency.

The finite-generator resolvent, invariant-class decomposition and rate-biased event sampling are standard probability machinery. Related primary literature is Melamed and Whitt, *On arrivals that see time averages: a martingale approach*, Journal of Applied Probability 27 (1990), 376–384, DOI `10.2307/3214656`. Its abstract distinguishes event-observed and time-observed distributions through stochastic intensity. It is background attribution; the finite result needed here is proved in (1)–(3), with no imported numerical constant or theorem hypothesis left unchecked.

The scientific addition is the effective law for this moving-and-forming candidate and its exact six-site comparison. A statement search of main `5d784d8ccda5268f2b7c056fcdf0d81fdb703319` and the 66 open PRs inspected on 2026-09-20 located the moving-record parent as the matching model. The older `RECORD_PRESERVATION_CONSERVES_THE_WITHIN_SECTOR_MEASURE_BOUNDED_THEOREM_NOTE_2026-06-15.md` concerns a supplied quantum-generation block; its conserved quantities and dynamics differ.

Primary author calculations and the separate finite-generator implementation are recorded in the branch checkpoint. Independent scientific checking and final-source confirmation are recorded there as they complete; no author check is an audit verdict. The primary runner contains every computation on which the numerical claims above rely.

## Reproduction

`python3 scripts/mobile_records_rare_formation_event_law_2026_09_20.py`

`python3 scripts/mobile_records_rare_formation_event_law_2026_09_20.py --list-mutations`

The canonical cache is `logs/runner-cache/mobile_records_rare_formation_event_law_2026_09_20.txt`, generated by `scripts/runner_cache.py` after freezing the note and runner inputs.
