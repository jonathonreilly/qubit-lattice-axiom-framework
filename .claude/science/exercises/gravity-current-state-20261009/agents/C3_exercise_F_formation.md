# Exercise on the wall: records cannot grow the event set (lane F) (campaign C3; 2026-10-10)

Compressed exercise (scratchpad/c3/exercise_wall.js): 3 route lenses (Opus 5.5 max), a kill round on every route (Opus 5.5 xhigh), then a next test pre-registered and run by an Opus 5.5 max worker. Same model family throughout; no codex referee on the exercise itself.

## Routes (9)

### 0. R-CM1: The qubit already carries the round light cone, so read the causal order from record content (the Löwner order on Herm(2) inside M2(C))

- **Premise dropped:** H-order, the premise that event relations are bare data, which a growth law must build from the order alone or which must be supplied as a sprinkling. It also drops the reading that a record's locked possibility carries no spacetime content. A36 survives in its exact form ('formation order cannot be recovered from a snapshot', prior_art_event_history.md), because under this route the causal order is readable but the formation order is not.
- **Mechanism:** The facts this rests on:
- PROVED, standard. The Hermitian part of the Qubit domain M2(C) is Herm(2) = {tI + x·σ}, and det X = t² − |x|² is the Minkowski form. X ⪰ 0 (both eigenvalues ≥ 0) holds iff t ≥ |x|. So the Löwner order Y − X ⪰ 0 is the 3+1 causal order.
- CHECKED in T-CM1: 0 mismatches in 2e5 random Hermitian differences.
- The null rays are rank-one c|ψ⟩⟨ψ|, so the celestial sphere is the qubit's Bloch sphere. CHECKED: 2000/2000 rays have Bloch vector equal to the spatial direction. COMPARATOR: Penrose–Rindler vol. 1.
- The causal automorphisms are Poincaré × dilations (COMPARATOR: Alexandrov–Zeeman, J. Math. Phys. 5 (1964) 490).

Why this matters for Lane F (SUGGESTED, condensed-matter lens):
- The round cone needs a whole S² of null directions.
- In 1+1 two linear orders suffice; that is why a random 2-order is a 2D sprinkling (COMPARATOR).
- In 3+1, insertion into k linear orders gives a box-shaped cone with only polylog link valency (maxima of random points; COMPARATOR from memory).
- The Bloch sphere supplies exactly the missing S². This is the 'order parameter fixes the cone' pattern: Volovik's ³He-A vierbein and analog gravity (COMPARATOR, reading).
- A record set whose locked Herm(2) values form a Lebesgue-intensity Poisson process is a 4D sprinkling, with no separately supplied order. CHECKED as control G in R-CM2.
- Records then lock 'where', not matter. That is the referee-backed resolution in SUMMARY §8: an event locks only its own occurrence and relations (READING).
- **Must believe:** (i) Reading of Qubit: a locked possibility is a point of M2(C) whose Hermitian part is the event's place. The axioms' continuous-domain note allows points; it does not say this.
(ii) The formation law uses only the cone (Jordan) structure. It must not use the algebra's unit or trace. PROVED, standard: the *-automorphisms of M2(C) are X ↦ UXU†; they fix I and act on Herm(2) only as SO(3). So any law that uses M2(C)'s full algebraic structure singles out a rest frame, and the Collins speed split returns. That is in tension with 'possibilities are distinguished by the supplied algebraic structure alone'.
(iii) The value law is translation- and SL(2,C)-invariant (Lebesgue). That is an Admissibility price: it is not a probability distribution on the whole domain, it does not vary with neighbour conditions, and it needs a finite region or an improper law.
(iv) Matter's qubit content lives somewhere else, e.g. a second slot or the anti-Hermitian part. M2(C) = Herm(2) ⊕ i·Herm(2) is complexified Minkowski space (READING).
(v) PROVED, sketch, same-family: one parent is never enough. There is no SO+(1,3)-invariant probability measure on J+∖{0}, because each orbit (hyperboloid or null cone) carries only an infinite invariant measure. So no Lorentz-invariant law can draw a child's value relative to a single parent. Equivariant finite kernels need a timelike parent pair, whose stabiliser SO(3) is compact. This is the growth analogue of BHS.
- **First test:** (a) Done here (CHECKED): T-CM1, the Löwner order against the causal order, and the null rays as pure states. Pre-registered at 01:59:36Z; PASS.
(b) Next (hours): write the one-parent lemma and the 'only cone structure' lemma, and send both to the codex referee.
(c) The decisive step is an owner decision, not a computation: may a record lock its place as a Herm(2) value read only through the cone?
- PASS: accepted, and the formation law is stated without I or the trace.
- FAIL: rejected, or the law needs M2(C)'s unit, which brings back a frame.
- **Cost:** Hours for the two lemmas plus a referee, then one owner decision. No new 4D statistics are needed: Lebesgue Herm(2) values under the Löwner order are a sprinkling by construction (control G below reproduces Lane F's numbers).

### 1. R-CM2: Bulk nucleation, not surface growth: let records form in the causal past of existing records (drop internal temporality)

- **Premise dropped:** H-seq, i.e. Rideout–Sorkin internal temporality: each new record is maximal at birth. Theorem L uses it in Step 1 (the up-set U_j and the new element's past = ↓D), and so do the frontier lemma and BG. B2's candidate wording 'forms with its relations to earlier records' builds it in. The axioms do not state it.
- **Mechanism:** - PROVED, elementary. A fixed-N Poisson sprinkling, enumerated in its i.i.d. insertion order, is a Markov growth process on labelled orders in which every labelling of an order is equally likely, by exchangeability. Its new elements are often not maximal, so Lane F's no-gos do not apply. The order-only kernel exists (a Bayes posterior), but it is non-local.
- PROVED and CHECKED, using R-CM1's values. The rule G, 'each new record uniform in the Alexandrov interval of the first and last records', is label-free and Lorentz-equivariant, and gives exactly a uniform sprinkling.
  - N = 1000 (8 runs): L/N = 17.59 ± 0.23, r = 0.1003, H = 10.25, n1/n0 = 0.350, Fano64 = 0.93.
  - N = 2000: L/N = 27.67 ± 0.42.
  - Lane F's values are 17.75 and 27.48.
- Condensed-matter analogue: JMAK bulk nucleation against Eden/MBE surface growth.
- **Must believe:** (i) A record's past may gain members after it forms; 'permanent' then means the lock, not the relations. Under H-seq only its future relations grow. This is in tension with the owner thought 'time = record creation' (a thought, not a rule).
(ii) The formation law is non-local. Every local insertion rule tried clusters, and the clustering grows with N. All CHECKED at N = 1000 against readings pre-registered at 01:59:36Z, 02:01:18Z and 02:08:09Z; all FAIL:
- U, uniform comparable pair: r = 0.387 ± 0.009 against 0.100, Fano64 = 110 ± 32.
- V, pair weighted by τ⁴: r = 0.236 ± 0.004, L/N = 26.5, central fraction 0.29 against 0.0625. Fano64 is 4.3, 18.7 and 47 at N = 300, 1000 and 2000.
- D, V plus one global chemical potential (insert only into under-populated intervals): r = 0.209, Fano64 = 8.8 ± 0.3, up from 3.3 at N = 400.
- W, an empty interval (a link) weighted by τ⁴: from a two-tip seed the order stays a chain forever. PROVED by induction: inserting inside a link of a chain keeps a chain. CHECKED: r = 1.
READING: insertion density is proportional to the number of bracketing pairs, a rich-get-richer feedback. The non-locality BHS forces on links reappears as non-locality of formation.
- **First test:** Already run here: U, V, D and W FAIL; G passes.

Next decisive test (hours): one local rule whose insertion rate per unit 4-volume is held constant by construction. For example, weight each candidate pair (a,b) by V(a,b)/B(a,b), where B counts the existing pairs bracketing the proposed point, measured inside a bounded interval.
- PASS: Fano64 in [0.5, 2], and r, L/N, H and n1/n0 within 5 SE of G, at both N = 1000 and 2000.
- FAIL: clustering grows with N.
A FAIL fixes the price as 'a whole-region formation law', i.e. Admissibility's nearest-neighbour locality given up for event formation.
- **Cost:** Hours. The scripts exist and take about 10 s per run at N = 1000 with OMP_NUM_THREADS=2.

### 2. R-CM3: Spacetime as a condensed coherent phase: select whole orders by an action (free energy) instead of locking relations one at a time

- **Premise dropped:** Sequential classical locking of the micro-relations (H-seq plus H-Markov read as a record process). The relations stay unrecorded (B2's candidate C, SUMMARY §8). A weight exp(−βS) or exp(iS) over whole orders, with S the smeared BD action, selects the phase. Records then lock matter only.
- **Mechanism:** This is energy against entropy, as in crystallisation. The BD action is a sum of local interval counts, and it competes with the roughly N²/4·ln 2 entropy of Kleitman–Rothschild layered orders.

COMPARATOR, from memory and unverified, no web search run:
- Loomis–Carlip, CQG 35 (2018) 024002, and Carlip–Carlip–Surya (2023) find KR and multilayer orders suppressed by the quantum weight.
- Surya, CQG 29 (2012) 132001, and Glaser–O'Connor–Surya, CQG 35 (2018) 045006, find a continuum phase, but only for 2D orders.

Nothing is grown sequentially, so Theorem L, the frontier lemma and BG do not apply.
- **Must believe:** (i) A 4D manifold-like phase exists and wins in the full space of orders. So far it is shown only in dimension-restricted spaces: 2D orders, and d-orders, whose cones are box-shaped for d ≥ 3.
(ii) The micro-geometry is coherent, i.e. the owner's C/B choice is made for C.
(iii) Its fluctuations stay off long waves; E1's noise question is unchanged.
- **First test:** Pre-register, then run MCMC over all labelled orders of N = 30–80 with the ε-smeared 4D BD action under the Wick-rotated weight, scanning β and ε.
- PASS: some (β, ε) region whose typical orders match same-N 4D sprinklings, with d_MM ≈ 4 and L/N, n1/n0, height and the 2+2/3+1 densities all within 5 SE, and with the region not shrinking from N = 30 to 80.
- FAIL: only KR, layered or crystalline phases at every (β, ε).
- **Cost:** 1–3 days for the MCMC and its validation, plus a referee. This is the highest-risk of the three routes.

### 3. R1 (rank 1). The order stays quantum: a sum over orders weighted by the smeared Benincasa-Dowker (BD) action, with records locking matter only

- **Premise dropped:** That the event set and its causal order are classical, permanent records produced by a positive probability law. Theorem L's proof is probabilistic throughout (P(join), concave J, the compensator identity), and lane F scoped quantum and action-weighted sums out, so they are not excluded. This is B2's fallback candidate C ("which events neighbour which is itself a possibility, not a record"). Named only as a price: Record is narrowed to matter, and an action plus a nonlocality scale eps become law data.
- **Mechanism:** Amplitude exp(i S_BD,eps(C)) over orders C. Phase cancellation suppresses non-manifold classes [comparator, verified on arXiv listings]: bilayers (Loomis-Carlip arXiv:1709.00064), Kleitman-Rothschild (KR) orders (Carlip-Carlip-Surya, CQG 40 (2023) 095004, arXiv:2209.00327), and layered families via the link action (Mathur-Singh-Surya arXiv:2009.07623). A growth form exists as quantum sequential growth (Surya-Zalel arXiv:2003.11311, covariance criterion; Srivastava-Surya arXiv:2603.25503, quantum Bell causality). In framework terms the relations stay part of the wave and only sparse matter records lock values. That also removes B1/B2's Planck-density heating tension ("an event happening is not a value being locked") [reading].
- **Must believe:** (a) Phase cancellation removes every super-exponentially numerous non-manifold class, not just KR orders and bilayers. Carlip-Carlip-Surya arXiv:2311.18238 report entropically dominant layered sets that can outweigh the action, and Carlip's review arXiv:2405.14059 says the survivors are poorly understood [comparator]. (b) What survives is 4D and manifold-like. In dimension-restricted samples (Cunningham-Surya arXiv:1908.11647) the manifold-like phase is the ENTROPY phase and the action phase is layered, so there the sample space, not the action, supplied the dimension [comparator]. (c) The action's per-realization noise is controllable. CHECKED here from lane F's stored interval counts (qg_lens/xf2_bd_action_classes.out, eps = 1 column only):
  - 4D sprinkled diamonds: the local 4D BD action (with 4/sqrt6) has mean S/N of +0.08 to +0.53 and per-realization sd of about 2.0-2.5 N at N = 500-4000, i.e. the noise grows proportional to N.
  - Lane F's r-tuned TP/OP/FACT orders: S/N of about -3.5 to -17, 2 to 7 sd away.
  - At hbar = 1 the 4D class's own phase spread is about 2N radians, so the LOCAL action cannot favour 4D by phase coherence [checked arithmetic plus reading]. Everything rests on the smeared action, whose noise E1 found large (row gain proportional to eps(T/l_k)^2).
(d) The owner accepts that micro-geometry is not recorded.
- **First test:** X-F2. Pre-register before running. Compute the exact smeared action S_eps (Benincasa-Dowker f(n,eps) summed over ALL interval sizes) per realization for:
  - 4D diamonds;
  - lane F's r-tuned TP/OP/FACT orders;
  - Varadarajan-Rideout (VR) towers;
  - X-F1's action-chasing orders.
Use N = 500-4000 and eps in {0.5, 0.2, 0.1, 0.05}. My quick pass truncated at n = 12, and the truncation error dominates for eps < 1, so it is not usable.
  - PASS-signal: for some eps, sd_4D(S_eps) grows more slowly with N than every competitor class's separation |<S_eps>_class - <S_eps>_4D|. That is a necessary condition for any coupling to keep 4D coherent while cancelling the growth attractors.
  - FAIL: for every eps, some class lies within sd_4D(S_eps) at N >= 2000.
Necessary, not sufficient: the entropy question stays open either way.
- **Cost:** X-F2: 2-4 hours, reusing lane F's samplers with bitset interval sizes. A real Lorentzian path-integral test is the open literature problem: weeks to months. The price if pursued: Record narrowed to matter (relations are possibilities, not records), plus an action (BD, eps) as law data.

### 4. R2 (rank 2). Records carry their own light cone: formation reads relations from the qubit content

- **Premise dropped:** That formation decides relations from the order alone (content-blind), and A36 ('records carry no time') for the relational part of content. Theorem L needs the ancestor choice to be exchangeable given the history. A choice that depends on record content breaks that, and lane F leaves 'rules that use the qubit or admissibility data' open.
- **Mechanism:** The Qubit axiom's algebra already contains the 3+1 light cone.
  - The self-adjoint part of M_2(C) is R^{1,3}, with det as the Minkowski form.
  - Positive semidefinite means future-causal.
  - X -> A X A^dag with A in SL(2,C) preserves both.
CHECKED on 20000 random samples to 2e-11, with zero cone mismatches (qg_lens/xf3_qubit_cone_check.out). This is standard algebra; that the Bloch ball is the Klein model of H^3 is standard and not checked here.
The rule: each record locks a positive Hermitian step, and e < f is read from det(transported dX) >= 0 with tr > 0. New links then sit on det = 0 shells, which is the near-null structure that gives the 4D link valency proportional to sqrt(N). The qubit would then also explain why 3+1 [suggested; von Weizsaecker ur-theory and Mueller-Masanes 2013 are comparators from memory, unverified].
- **Must believe:** (a) No probability law on H^3, or on the celestial sphere, is invariant under the non-compact SL(2,C) (standard measure theory; suggested here, not checked). So each step must be drawn in some frame, and a frame-covariance condition must replace discrete general covariance (DGC): the law of the final order must not depend on the frames used.
(b) Contents at different events must be compared through a transport, an SL(2,C) connection (tetrad-like data). That is a new field. With one global identification of all site algebras instead, the background is flat and supplied, and records hold absolute positions (labels). That re-opens the stiffness wall (Lemma R) and removes dynamical geometry (B2's S3).
(c) The content law yields uniform density (number = volume) without being told to.
- **First test:** (a) A proof obligation, which is decisive either way: is every content-aware sequential rule that has frame-drawn steps and a frame-independent final-order law a time-ordered Poisson sprinkling?
  - If yes, the route collapses to 'supply the sprinkling'. That is an exact price, and a useful result.
  - If no, the counterexample is a new rule.
(b) Run any counterexample through lane F's statistics (L/N, n1/n0, H, nmin/N, 3+1 density) at N = 1000-4000, with lane F's tolerances fixed in advance.
- **Cost:** (a) 1-2 days of proof work; (b) hours. Price if it works: records lock causal content (A36 narrowed), plus a transport field.

### 5. R3 (rank 3, wounded). The gravitational action steers classical growth: structure-aware, records stay classical. First test RUN: FAIL in its first form

- **Premise dropped:** Exchangeability of the ancestor choice (H-exch). Classical permanent records and sequential growth are kept. The new event's past P is weighted by the exact local 4D BD increment dS = 1 - N0 + 9N1 - 16N2 + 8N3, so the rule prefers existing events by their place in the order. DGC and Bell causality are not imposed.
- **Mechanism:** The BD action is the discrete Einstein-Hilbert action. Weighting by exp(-beta dS) rewards links (N0), so it could in principle lift link valency past the exchangeable ceiling H_(N-1).
- **Must believe:** That a local action increment steers growth toward 4D rather than toward action-chasing non-manifold orders. That a new coupling beta is acceptable, which is a price. That DGC (the dynamical form of A36) may be dropped.
- **First test:** RUN. Pre-registered in qg_lens/PREREG_XF1.md (01:57:31Z); script qg_lens/xf1_bd_tilted_growth.py; output qg_lens/xf1_N500.out. Incremental counts were validated against brute force at N = 150 (n_k, L, R and transitivity all exact).
Rule: a TP prior plus 60 Metropolis toggles weighted by exp(-beta dS), with beta in {0, 0.5, 1, 2, 4}, p tuned to r = 0.1, N = 500, 4 realizations.
Result at every beta:
  - L/N = 1.9-2.6, against the exchangeable ceiling of 6.79 and 4D's 11.28.
  - The tilt chases N2 (coefficient -16): n2/n0 is about 2.1 against 4D's 0.18, and S_BD/N is about -20. H = 11-17 against 8.1.
FAIL under the fixed reading, bounded to this family. Same-family; the rules require the codex sol referee before it is recorded.
Two dated controls also stayed at L/N <= 2.9: X-F1b (pure link reward under the TP prior) and X-F1c (flat prior plus a past-size penalty, with link reward or BD). My written prediction that X-F1c would go layered was wrong. Those controls are mechanism-INCONCLUSIVE, because the random-toggle sampler may be what limits them [checked].
Also CHECKED from lane F's data: Euclidean weighting exp(-beta S) with beta > 0 favours CSG-like orders (S/N -3.5 to -17) over 4D (+0.1 to +0.5). PROVED (one line): the local action is unbounded below over orders; a complete bilayer has S = (4/sqrt6)(N - N^2/4).
- **Cost:** Done, in minutes of compute. Reopen only if X-F2 finds a smeared action that separates 4D from the growth attractors. The next version would be eps-smeared dS with geometry-blind proposals, about 1 day. Do not pursue the local Euclidean form.

### 6. R1. Write the arena price exactly: one sentence forces the sprinkling

- **Premise dropped:** That records forming must produce the event set, which is lane F's target. Records were never asked to grow Z^3, and the axioms supply no formation rule for anything (MINIMAL_AXIOMS lines 63-73 and 181-186). The route replaces that target with an arena premise of the same kind as Lattice.
- **Mechanism:** Lemma V (proved here, elementary; Renyi plus Bernstein; referee pending). Take a simple, locally finite point process whose void probabilities depend only on volume: P(no event in B) = phi(|B|) for every finite union of boxes B. Then it is a mixed Poisson process. Proof: take A of volume a and disjoint B_1..B_k of volume h each. P(A empty and every B_i occupied) = sum_j C(k,j)(-1)^j phi(a+jh) = (-1)^k Delta_h^k phi(a) >= 0. So phi is completely monotone, with phi(0+) = 1 because there are no fixed atoms. Bernstein then gives phi(v) = E exp(-alpha v). Voids on a dissecting ring determine a simple process (Renyi-Monch), so the law is Poisson with a random density alpha. Fixing the density with the scale reference gives the Poisson sprinkling. The event arena therefore costs exactly three things: (P1) flat light cones, i.e. which events can influence which; (P2) 'no region of spacetime is preferred over another of the same volume'; (P3) one density, which is the existing scale reference. The realized arena is world-supplied data, as with realized_state. Checked (X2): symmetry under linear maps in law is not enough. A Haar-random unimodular 2D lattice is SL(2,R)-invariant and stationary in law. For three sets of equal area 0.5 its void probabilities are 0.5805 (disc), 0.5781 (1:20 rectangle) and 0.5951 (two half-discs), each +-0.0020, a 6.0 sigma dependence on shape. Poisson gives exp(-0.5) = 0.6065 for every shape. Prior art: the archived Cycle 46 note (causal order plus a known uniform record density fixes the metric, via HKM/Malament). B2's wording 'one per unit of spacetime volume' (B2_report.md:190) becomes exact under Lemma V.
- **Must believe:** That a supplied random arena is acceptable as a premise in the same way Z^3 is, with the realized arena as world-supplied data. That flat light cones may be supplied for the flat-background lanes (E1', G, M, D). It gives no dynamical geometry. For gravity proper, P1 would have to become dynamical, and the formation question would come back as the mediator and GR-dynamics wall (B2's G3 and G6), which lane F's flat-4D target does not test.
- **First test:** An other-vendor referee of Lemma V with its hypotheses: simple, locally finite, voids depend only on volume on box unions, any d >= 1. The referee should also check the one step that is only suggested: in d >= 2, invariance in law under compactly supported volume-preserving diffeomorphisms implies volume-only voids. That step needs volume-preserving maps to be weakly dense among measure-preserving rearrangements, plus finite intensity for voids to vary continuously. PASS: confirmed with its hypotheses, and the owner-level price is the three-item sentence. FAIL: a process with volume-only voids that is not mixed Poisson.
- **Cost:** About 1 hour of writing plus one referee round. No compute; the X2 illustration has already run (3 s).

### 7. R2. A short label-invariant growth rule without Bell causality

- **Premise dropped:** Bell causality, i.e. choosing ancestors without looking at the existing order (exchangeable choice, lane F's H-exch). Kept: label invariance (discrete general covariance), one event at a time, no coordinates.
- **Mechanism:** Lemma G (proved here, elementary; checked). Take any law mu_N on unlabeled N-element orders. Draw an order from it, then a uniformly random natural labeling. The result is a sequential growth law that is label-invariant at every stage, because P(labeled stem B) = sum_C mu(C)/e(C) * sum over down-sets D of C isomorphic to B of |Aut B| e(C minus D), which does not depend on the labeling. Checked exactly in Fraction arithmetic with the empirical 4D-diamond law (K = 20000 each): no class with unequal labelings among 69 stem classes at N = 5 and 217 at N = 6. So the 4D sprinkling is itself a label-free growth law at every N. Lane F's 4D link density (L/N = 7.72 > H_299 = 6.28 at N = 300) and Theorem L's contrapositive show that this law breaks H-exch. Checked directly: after the stem 'two-element chain plus a lone element', the new event's past is {chain bottom} with probability 0.21 at N = 6 (0.217 at N = 5) and {lone element} with probability 0.028 (0.027), from about 1100 samples each. H-exch forces these to be equal; the gap is about 15 sigma. The rule favours events by their place in the order, which is what lane F said a working rule must do. N-dependence is small at tiny N (X3): the total-variation distance between the N = 5 law and the stage-5 stems of the N = 6 growth is 0.033, against a sampling floor of 0.018. What is still open is how short the rule can be: is there a short rule, independent of N, that looks only at the order near the candidate past?
- **Must believe:** That a rule using only local order data near the new event's past (counts of small intervals, as in the Benincasa-Dowker action) can aim at a light-cone layer and give link valency growing like sqrt(N). It must also stay label-invariant, which structure-aware rules break easily (lane F's FRONT0 did).
- **First test:** Two rules with fixed parameters. (a) Benincasa-Dowker-tilted CSG: the CSG subset weight times exp(-beta * Delta S_BD^(4)) for the new event. (b) A cone-layer rule: the past is the down-closure of a random maximal antichain, weighted by its size. Gate 1: exact enumeration of label invariance at N <= 6 (x1 here, or lane F's F7). Gate 2: lane F's battery (L/N, n1/n0, nmin/N, height, 2+2 and 3+1 densities) at N = 1000-4000, with parameters fixed at N = 1000. PASS: Gate 1 exact, and Gate 2 within 3 sigma of 4D at every N. FAIL: Gate 1 fails, or L/N does not grow like sqrt(N). Pre-register before running. Prediction (suggested): the naive tilt (a) fails Gate 1.
- **Cost:** About one day. Lane F's code (scratch c3/F/scripts) and x1 here can be reused.

### 8. R3. Unrecorded geometry: an action-weighted sum over orders

- **Premise dropped:** That the event set is one classical realized history, i.e. a record. The fine-grained relations become possibilities weighted by a local rule, and records lock matter only (B2's fallback candidate C, B2_report.md:205).
- **Mechanism:** Weight each N-element order by exp(i S_BD^(4)) or by its rotated form exp(-beta S_BD^(4)); on sprinklings the action's mean is Einstein-Hilbert. Comparators, cited from memory and not re-fetched: the BD action suppresses Kleitman-Rothschild and bilayer orders (Loomis-Carlip 2018); 2D orders show a continuum phase (Surya 2012; Glaser-O'Connor-Surya 2018); restricted 3D samples have been studied (Cunningham-Surya 2020). All of these restrict the sample space to d-orders, which supplies the dimension. 4D over all orders is open. Admissibility's 'distribution determined by the nearest-neighbour conditions' becomes the local weight. Nothing is grown classically, so neither Theorem L nor Brightwell-Georgiou applies.
- **Must believe:** That dimension 4 comes out of the weight, not out of a restricted sample space. That the rotated weight means something physically. That geometry may stay unrecorded (a change in how Record is read, named as a price). That coherent rather than recorded fine-grained relations keep the noise off long waves (B2 section 3a).
- **First test:** Metropolis sampling over all N-element orders, N = 30-80 (moves: add or remove a relation while keeping transitivity), with weight exp(-beta * eps * S_BD^(4)). Measure d_MM, L/N, n1/n0 and height against 4D sprinklings as functions of beta. PASS: a beta window with 4D-like statistics at every N tested, with no restriction on the sample space. FAIL: only Kleitman-Rothschild, layered or chain-like phases at every beta.
- **Cost:** Several days. Small-N runs take hours, but mixing over all orders is slow.

## Kill round

| # | Route | Killed | Reason / survives as |
|---|---|---|---|
| 0 | R-CM1: The qubit already carries the round light cone, so read the causal order  | True | Kill check by Claude Opus 5.5, the same model family as the route's author, so it does not count as an independent referee. Files read: the axioms in full, the exercise skill, the packet SUMMARY, TESTS, the C3_F report and referee, prior_art_event_history, the B2 report and the C3_D/G-C excerpts. Prior art: campaign 8 A36/REPORT.md D1 on origin/ai/probes, docs/RECORD_FAITHFUL_CUBIC_NEIGHBOR_RESPONSE_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-11.md, the candidate-pack FR3 referee, and the sibling T-CM1/T-CM2 outputs. Scratch files: .../scratchpad/c3/exercise_F_formation/kill_RCM1/{PREREG.md, kill_rcm1_checks.py, kill_rcm1_checks.out}. PREREG.md was stamped 02:19:38Z, before the run.  VERDICT: blocked-equivalent for this wall, with a gravity lock-in on top. The route does not supply a formation rule. It renames the supplied sprinkling and adds new supplied structure.  1. The terminal obli |
| 1 | R-CM2: Bulk nucleation, not surface growth. Records form in the causal past of e | True | KILLED. The route's passing rule G is the supplied sprinkling under another name. Its proposed decisive test either passes by construction, using a global count, or fails. Bulk nucleation cannot grow the region it fills. Details, each labelled:  (1) PROVED (elementary): interval insertion cannot enlarge the region. - Take any rule that places a new record x inside I(a,b) for an existing pair a<b. That rule leaves the causal hull H(C) = union of I[a,b] unchanged: c<x gives I(c,x) inside I(c,b), and x<d gives I(x,d) inside I(a,d). - So bulk nucleation never enlarges the universe. The 4-volume is fixed by the seed, and two of the seed records are privileged: G's tips. - The density n/V grows without bound with the stage. Holding a fixed discreteness scale would need a global stopping count.  (2) PROVED: G is target-equivalent. - G is "uniform Lebesgue measure on a seed-supplied region, with |
| 2 | R-CM3: spacetime as a condensed coherent phase. Select whole orders by an action | True | KILLED as a testable route. The proposed first test (Wick-rotated MCMC at N = 30-80) has two problems. Its large-N answer is already a FAIL, proved below. And at N = 30-80 the test cannot decide anything. The quantum branch does survive, but only as a blocked-equivalent price (see survives_as).  PRIOR ART (step 0). - C3_F_report §7 and C3_G-C_report lines 264-269. Both list as comparators, from memory: the BD-action sums over 2D orders (Surya 2012; Glaser-O'Connor-Surya 2018), the partial suppression of Kleitman-Rothschild (KR) orders (Loomis-Carlip 2018), and "no 4D sum is known to have a manifold-like phase". - B2_report lines 205, 270-273 and 311. Candidate C (coherent micro-relations) is a change to the Record axiom, and B2 calls it an owner decision. - The QG lens of this exercise (scratch exercise_F_formation/qg_lens) gives two checked results:   - X-F1/b/c: tilting growth by the B |
| 3 | R1 (rank 1): a quantum sum over orders weighted by the smeared Benincasa-Dowker  | True | The route needs a coupling at which the 4D class keeps its phase while layered orders cancel. No such coupling exists at any eps or N tested. Its own first test, X-F2, measures the wrong thing.  Prior art (step 0): - The packet has only lane F, X-F1 (BD-tilted classical growth: L/N stays at 1.9 to 2.9, below the exchangeable ceiling) and the truncated quick pass xf2_bd_action_classes.out. - E1 already found that the BD row noise grows like eps(T/l_k)^2. - No repo surface computes BD path-sum class amplitudes.  1) X-F2 run as specified (checked): - The exact smeared action A_eps = N - eps * sum_n N_n f4(n,eps) was computed over all interval sizes. S/hbar = (4/sqrt6) sqrt(eps) (l/l_p)^2 A_eps. - The local limit reproduces the stored eps = 1 column: 4D sd/N = 1.44, i.e. 2.37/1.633; TP mean -8.2. - Classes: 4D diamonds (10 to 30 realizations), TP tuned to r = 0.1, and VR towers dust(m)+TP tu |
| 4 | R2 (rank 2). Records carry their own light cone: formation reads relations from  | True | Kill-check agent: Claude Opus 5.5, the same model family as the route's authors, so this is not an independent referee. Work ran 02:10Z to 02:20Z. Read in full: docs/MINIMAL_AXIOMS_2026-06-29.md, the exercise SKILL.md, packet SUMMARY.md, C3_F_report.md and C3_F_referee.md, prior_art_event_history.md, the TESTS.md lane F readings, and B2 §3. No repository file was edited.  STEP 0, PRIOR ART: this route was already partly tested inside this exercise. - The condensed-matter lens ran T-CM2 (scratch exercise_F_formation/PREREG.md, out/cm2_N1000.log, out/cm2_D_N1000.log). Records carry Herm(2) values and the order is the Loewner cone, i.e. the route's own relation. - Rules that place new records using the content of existing records all fail (checked):   - U: r 0.387, L/N 26.4, slab Fano 110;   - V: r 0.236, L/N 26.5, Fano 18.7;   - D (density feedback): r 0.209, L/N 22.3, Fano 8.8;   - W: sta |
| 5 | R3: the gravitational (Benincasa-Dowker, BD) action steers classical sequential  | True | KILLED as a classical, real-beta action tilt. The kill is bounded to the tested family (Markov, one-step kernels whose log-weight depends only on the new past's interval profile) and to accessible sizes (history N up to 700). The codex referee has not seen this; Opus 5.5 same-family work only.  Prior art (step 0): - Main docs mention causal-set growth only as literature positioning (docs/LITERATURE_POSITIONING_NOTE.md:159). - The archived audits treat CSG as a law-data family. - The candidate-law pack has no growth or BD objects; its only formation reading is CANDIDATE_1.md:93. - Packet: lane F (C3_F_report.md and referee), X-F1/X-F1b/X-F1c (FAIL or mechanism-INCONCLUSIVE), and X-F2 (qg_lens/xf2_bd_action_classes.out). X-F2 shows that at eps = 1 and 0.5, the growth classes already have lower S/N than 4D, and the gap grows with N. At eps = 0.3, 4D has the lower S/N up to N = 2000, but the |
| 6 | R1. Write the arena price exactly: one sentence forces the sprinkling (Lemma V:  | True | The route is killed. The kill rests on argument and citations; I ran no new computation. Lemma V's mathematics is correct, but the route neither passes the wall nor prices it, and its central claim that the arena costs "exactly three things" is an undercount.  Refresher read: docs/MINIMAL_AXIOMS_2026-06-29.md in full; the packet SUMMARY.md; C3_F_report.md and C3_F_referee.md; TESTS.md (rules and the C3 lanes); prior_art_event_history.md; B2_report.md sections 3–3b; REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md; SCALE_REFERENCE_PRIMITIVE_NOTE.md; the archived Cycle 46 note.  (1) The lemma is classical, not new. - Labels: proof checked here; the theorem itself is a comparator. - I checked the proof step by step and it is correct:   - the inclusion-exclusion identity P(A empty, all B_i occupied) = (-1)^k Delta_h^k phi(a);   - phi(0+) = 1, because a locally finite process has only countably ma |
| 7 | R2. A short label-invariant growth rule without Bell causality | True | The route is killed as an escape from the price; it is blocked-equivalent. It was pre-registered before any run in kill_R2/PREREG_KR2.md. Scratch folder: /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/exercise_F_formation/kill_R2/. Note: another agent wrote unrelated files (PREREG_R2kill.md, r2_step_rule.*) into the same folder, for a different "R2". My files are PREREG_KR2.md, kr2_enum.py, kr2_k3.py, kr2_n7.py and *.out.  (1) The route's own first test fails Gate 1 (checked; exact enumeration of every labelled growth path to stage 5; kr2_N5.out). - Control, TP(0.3): label-invariant, with 0 unequal classes through n = 5. - (a) BD-tilted TP (p = 0.3, beta = 0.25 or 1): not label-invariant from n = 3 on. Spread within the chain-plus-lone class is 0.32 at beta = 0.2 |
| 8 | R3. Unrecorded geometry: an action-weighted sum over orders | True | KILLED as specified: a rotated, real weight exp(-beta*S_BD^(4)) over all N-element orders, tested by Metropolis.  PRIOR ART (step 0). Three places already cover the ground: - C3_G-C_report.md:269 (R8) records that Kleitman-Rothschild (KR) entropy dominates 4D, that the BD action suppresses only part of it (Loomis-Carlip, comparator), and that no 4D sum is known to have a manifold-like phase. - C3_G-C_report.md R9 names the unrecorded-geometry price (B2_report.md:205, candidate C). - C3_F_report.md section 7 lists the same comparators, and prior_art_event_history.md records the event era's 'no growth rule forces d=3'. Nothing in the packet, the candidate pack or main docs tests a sum over all orders. Scripts and outputs are in scratchpad/c3/exercise_F_formation/R3kill/; PREREG.md was written and stamped before any run.  (1) PROVED (elementary; same-family; not refereed). Take any real wei |

## Next test (pre-registered and run by the worker)

**Next-test stage, exercise F_formation.** Claude Opus 5.5 (max), 02:24–02:39Z. No repository files were edited. Nothing here has been refereed.

## Plain summary

No route survived the kill round, so there was nothing to rank as a survivor. I ranked what the kills left open instead. The top item is writing down the exact price.

The one rule known to reproduce 4D statistics is Lemma G: read the sprinkling's own law, in uniformly random birth order, as a growth rule. I tested whether that rule can run open-ended, without knowing in advance how many events will form. It cannot. The early stages it produces are measurably less ordered than small diamonds, so it can only aim at one final size it is told in advance. The pre-registered TELEOLOGICAL reading was met at 10–19 SE.

## 1. Kill round: survivors = none

The kill verdict objects were not passed to me. I took the reasons from the kill folders under `.../scratchpad/c3/exercise_F_formation/`.

- **R-CM1 (Löwner order on Herm(2)):** checked, killed.
  - Boosts do not preserve the Jordan product (median relative error 1.05; under SU(2) it is 4e-15).
  - If each record's domain is identified only up to an automorphism, 40–42% of related pairs lose their relation.
  - So a single global identification, a supplied flat arena, is needed (`kill_RCM1`).
- **R-CM2 (bulk nucleation):** checked, killed. Rule B_I clusters: Fano64 is 6.6, 14.9 and 34.6 at N = 500, 1000 and 2000, and r ≈ 0.19 against 0.10 (`kill_RCM2`).
- **R-CM3 and price-R3 (real-weight action sums):** checked, killed.
  - An entropy bound gives sup over β of (ub − lb) ≤ −8000 for N ≥ 600, at every ε tested. The N = 30–80 window does not decide (`kill_RCM3`).
  - On flat sprinklings the action changes sign across d = 4, so no real β can select d = 4 (`R3kill` K1).
- **QG-R1 (Lorentzian sum):** killed.
  - X-F2's necessary separation passed at ε ≤ 0.2.
  - But suppressing bilayers needs a phase per link in (2π/3, 4π/3). That gives the 4D class itself a phase spread of 386–12032 rad, so there is no coupling window (`kill_R1`).
- **QG-R2 (records lock Hermitian steps):** checked, killed. Mode G gives r = 0.50 (z = +31). In Mode I the frame rapidity grows 0.60 per generation.
- **QG-R3 (BD-tilted growth):** checked, killed. In KR3b, started at the true 4D past, the kill reading was met in 74/75 settings and the survive reading in 0/75 (`kill_R3`).
- **Price-R1 (Lemma V):** no kill file, so the reason is not visible to me. It is a price statement, not a route past the wall.
- **Price-R2 (Lemma G plus a short rule):** checked, killed.
  - BD-type interval-histogram rules that keep label invariance (DGC) reduce to CSG at N ≤ 7, so Theorem L applies.
  - **Residue:** rules that also look at events outside the new past do have interior non-CSG DGC solutions (deviation ≈ 0.9 at N = 5 and 6; 5 extra free parameters at N = 7). This is the only freedom the kill round found (`kill_R2/k3_*.out`).

## 2. Ranking of the residues by (change)/(cost)

1. **Write the price exactly once.** Assemble Theorem L, the frontier lemma, BG, Lemma V, Lemma G, the kills, and T-F1 and Lemma S below. It gives the owner one statement of what formation costs. Cost: hours plus one referee.
2. **Spectator-aware order-invariant short rules (the K3 freedom).** If one worked, it would remove the supplied-sprinkling price. Cost: days. The first need is a family of rules that stays label-invariant at every stage. Prior chance of success is low.
3. **Lorentzian sum over orders.** Largest payoff, cost of months. It must first beat kill_R1's phase-spread bound.

**Prior art.**
- The repo already asks history laws to be "prefix-consistent" (`docs/RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md`, claim scope).
- The 09-07 formation note supplies the formation order through iid clocks (`docs/NATIVE_RECORD_SUPPORT_PRESERVING_PRIORITY_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`).
- No repo surface mentions linear-extension or order-invariant growth.
- Comparator, from memory and unverified: Brightwell–Łuczak, order-invariant growth.

## 3. T-F1 pre-registration

Stamped 02:33:43Z, in `next_test/PREREG_T-F1.md`.

**Question.** Is Lemma G's family projective (open-ended)? That is, is the law of the first n events of the N-growth equal to μ_n, the law of an n-point diamond sprinkling, for every N > n?

**Setting.**
- A 4D diamond with N uniform points; only the causal order is kept.
- Exact counts of natural labellings by dynamic programming over down-sets, so the uniform random natural labelling is exact.
- N ∈ {2, 3, 4, 5, 6, 8, 10, 12}, with K = 3000 orders for N ≤ 6 and 2000 for N ≥ 8.

**Observables.**
- **O1:** p2, the probability that the first two events are related. Target 0.1.
- **O2:** m3, the expected number of related pairs among the first three events. Target 0.3.
- **O3:** a3, the probability that the first three events are mutually unrelated. Target μ_3, measured directly.

**Readings.**
- **TELEOLOGICAL:** some observable is more than 5 SE from its target at some N ≤ 12, with one sign for every N ≥ 6.
- **OPEN-ENDED-CONSISTENT:** every observable within 3 SE at every N.
- **INCONCLUSIVE:** otherwise.

**Prediction:** p2 falls below 0.1 as N grows.

## 4. Result (checked): the TELEOLOGICAL reading is met

**Code checks.** Dynamic-programming counts against brute force: 0 mismatches in 50 orders at N = 6 and 7. The probabilities for the first two events sum to 1 within 1e-15. Direct samples give μ_2 = 0.10049 ± 0.00039 and μ_3 antichain probability = 0.75597 ± 0.00096.

| N | p2 (target 0.1) | z | m3 (target 0.3) | a3 (target 0.756) |
|---|---|---|---|---|
| 2 | 0.0997 ± 0.0055 | — | — | — |
| 3 | 0.0902 ± 0.0037 | −2.6 | 0.291 ± 0.010 | 0.765 ± 0.008 |
| 4 | 0.0855 ± 0.0029 | −5.0 | 0.272 ± 0.008 | 0.773 ± 0.006 |
| 6 | 0.0759 ± 0.0023 | −10.6 | 0.240 ± 0.006 | 0.799 ± 0.004 |
| 8 | 0.0706 ± 0.0024 | −12.5 | 0.219 ± 0.006 | 0.813 ± 0.005 |
| 12 | 0.0622 ± 0.0020 | −19.2 | 0.192 ± 0.005 | 0.835 ± 0.004 |
| 16* | 0.0612 ± 0.0027 | −14.2 | 0.186 ± 0.007 | 0.840 ± 0.005 |
| 20* | 0.0543 ± 0.0031 | −14.6 | 0.165 ± 0.008 | 0.857 ± 0.006 |

\* Addendum A1, dated before it ran; reported as a trend only.

- At N = 3 the first three events are the whole order, so they must match the targets, and they do: m3 and a3 are within 0.9 and 1.2 SE.
- The prediction was confirmed.

## 5. What it means

**No label-invariant growth law gives the diamond law at every stage (checked).** Under DGC (the dynamical reading of A36), every birth order of the order grown so far is equally likely. So the law of the first two events is fixed by the N-point law. Because p2(12) differs from μ_2 by 19 SE, no DGC growth law can give the diamond-sprinkling law at both stage 2 and stage 12. This holds whether or not the law is Markov, Bell-causal or exchangeable. Stages 6 and 12 also differ, by 4.6 SE through p2.

**Consequence.** Lemma G's rule reproduces a 4D diamond only if it knows the final size in advance. It is not an open-ended formation law, and it fails the repo's own prefix-consistency standard.

**Scope.**
- Only diamond-shaped regions were tested.
- A rule that is only asymptotically diamond-like is not excluded.
- Rules that are not label-invariant escape. For example, label events by advanced time t + r along the diamond's axis. This is a natural labelling (if x < y then t_x + r_x ≤ t_y + r_y), and each stage up to time T is exactly the sub-diamond I(bottom tip, T). It needs a frame (the axis). This is proved and elementary.

**Lemma S (proved as an elementary sketch, same-family, unrefereed; it assumes the sprinkled order almost surely has no symmetries).**
- **Claim:** no process that adds events one at a time and sees only the order can produce an infinite event set whose law is invariant under a non-compact group. Examples: boosts about a point (a sprinkling of J+(0)), or spatial translations (a half-space).
- **Proof:** the process's conditional labelling law is equivariant. So the first event's position would need an invariant probability law on hyperboloids or on R³, and none exists.
- **What it means:** one-at-a-time formation needs a beginning that has a preferred frame or centre, or a compact spatial section.
- **Comparators:** BHS, and R-CM1's one-parent lemma.

**Updated price (suggested; assembled from the pieces above).** Classical one-at-a-time formation of the event set costs one of:
- (a) a supplied event set, Lemma V's three-part sentence;
- (b) a law that knows its final size or region in advance (Lemma G plus T-F1);
- (c) a physical birth order that carries a frame (axis growth; Lemma S makes a frame or centre unavoidable for infinite growth);
- (d) a short rule that does not obey Bell causality, not yet found (the K3 residue).

## 6. Needs

- T-F1 is a no-go-type result, so it needs the codex sol referee before it is recorded (TESTS.md rule).
- Lemma S needs the same referee.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/c3/exercise_F_formation/next_test/`:
- PREREG_T-F1.md
- tf1_projectivity.py
- tf1_main.out
- tf1_A1_N16.out
- tf1_A1_N20.out
