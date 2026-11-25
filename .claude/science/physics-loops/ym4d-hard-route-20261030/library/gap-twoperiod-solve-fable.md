lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T17:37Z

# Row 1520, gap-twoperiod-solve-fable: the two-period transport input (*) of check 1516

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned at commit 48951d201. Proved-by-Claude items
below are not yet checked by another model. Nothing here is a status claim.

## Status log (times from date -u)

- 2026-11-25T05:37Z start. File created. Plan below.
- 2026-11-25T05:38Z read: row 1520, FINISH rule sections, GOAL.md, check 1516 in full (section (v) = statement (*), consumer, separation example), row 1517 in full (CONJ, VOL, TR2, COLD, FLOOR, 6.1).
- 2026-11-25T05:45Z Sections 1-2 written: Theorem EQ (the existence form of (*) contains kappa = 0 at period u, which is the target in integrated form; (*) forces the purity bound at every bare coupling on the way). Registry: TWO-PER at open-registry L1020; R11 L1018.
- 2026-11-25T05:49Z Sections 2.3-2.4, 3, 4 written: Proposition H (integral of h is at least J(u, beta_K) - o(1)), Lemma Q, Lemma DY, Proposition F (frame of row 1517 applies; selective form bound reappears), Corollary FLOOR-2. Memory 38 percent free: no numeric job.
- 2026-11-25T05:54Z registry grep and cross-branch search done (Section 7.1). Two wording fixes in 2.2 and 3.2 (exact arithmetic of the three-level example; citation for beta_K unbounded). Sections 5-8 follow.
- 2026-11-25T05:54Z Sections 5-7 written (integer-period forms, verdict EQUIVALENT, registry change, next two rows, search, labels). Re-read of the proved items done: two wording fixes (Lemma Q (d) example with a simple vacuum; 6.1 item 3). Section 8 written. Finished.

## Plan

1. Read check 1516 section (v) in full (the statement (*) and its consumer) and row 1517 (Lemma CONJ, TR2, VOL,
   FLOOR, selective form bound 6.1).
2. Registry grep: is (*) or a sufficient form of it on file (open-core.md, FINISH rows, gap-mid-max.md Section 4)?
3. Decide the frame question: is (*) a form bound for a generator class? Does 6.1 reappear? FLOOR analog for
   Ising and compact U(1): at which step does (*) fail there?
4. Attack (*) or the integer-period sufficient statement; write each step here before the next.
5. Verdict, next two rows with decisive outcomes, RESULT line.

## 1. The statement, in the notation used below (read; nothing new)

Labels: **proved** (a written proof is in this file), **read** (read in a row, not re-derived), **argued**,
**guessed**, **guide** (heuristic size, never a proof step).

Source of (*): check 1516, `library/gap-seed-direction-fable-check-astra62.md` section (v), L60-86 (gpt-6.2-astra).
Registry line TWO-PER, `library/open-registry.md` L1020.

- Box: the spatial torus n^3, n = l b^K, u = n/512 (an even integer). T(t) is the Wilson transfer operator at
  coupling t, P_0 the centre-neutral projection, Z_+(v, t) = Tr(P_0 T(t)^v). Neutral levels E_i(t) >= 0,
  E_0 = 0, ratios r_i = e^(-E_i) in [0, 1] (T >= 0).
- G(v, t) = log(1 + sum_(i>0) r_i^v). **J(v, t) = 2 G(v, t) - G(2v, t) = 2 log Z_+(v, t) - log Z_+(2v, t)**
  (the vacuum terms cancel). J = -log of the neutral purity of the thermal state at time length v.
- Thermal weights p_i(v) = r_i^v / (1 + s(v)), s(v) = sum_(i>0) r_i^v. Mean energy Ebar_v = sum p_i(v) E_i.
  dG/dv = -Ebar_v and **dJ/dv = -2 (Ebar_v - Ebar_2v) <= 0**.
- At integer v, J(v, .) is real-analytic in t > 0 (each Z_+(m, .) is a positive average of eight twisted Wilson
  integrals over a compact space, and Z_+ >= lambda_0^m > 0), and
  dJ/dt = 12 v n^3 (x_v - x_2v), with x_m the neutral mass-weighted mean of (1/2) tr U_p on n^3 x m
  (check 1516 (iii), row 1515 (E2)).
- **(*)** at a point (v, t): D_t^+ J(v, t) <= 2 kappa(t) v (Ebar_v - Ebar_2v) + h(t), that is
  D_t^+ J <= - kappa v dJ/dv + h. Along v(t) = v_0 exp(integral of kappa) this says: the upper right derivative
  of psi(t) := J(v(t), t) is at most h(t).
- **Consumer** (check 1516 (v), L80): (*) on [t_0, t_1) gives psi(t_1) <= psi(t_0) + integral of h, and
  J(u, t_1) <= psi(t_1) when v(t_1) <= u. Entrance: t_0 = 1/25600, v_0 = ceil(log_2 n),
  J(v_0, t_0) <= 2 G_full(v_0, t_0) < 7.4 x 10^(-4) for even n >= 256 (row 708, proof of Corollary TR1).
  Budgets: integral of kappa <= log(u/v_0), integral of h <= B/2, B = log(625/457) = 0.3131 (guide value).
  Then J(u, beta_K) < B, which is (PUR-io) when it holds at infinitely many K for one l and g_0.
- Where the levels are differentiable, with V_i = -dE_i/dt and **w_i := V_i - kappa E_i** (w_0 = 0):
  homogeneous (*) is <w>_v <= <w>_2v, and (VIR_kappa) of row 708 is <w>_v <= 0 (thermal means at v, 2v).

## 2. The existence form of (*) is the target itself (written first because it decides the row)

### 2.1 Theorem EQ (proved; elementary; one author, unchecked)

Fix the box, t_0 < t_1, an integer u >= 4 and an entrance period v_e in [4, u]. Call a pair (kappa, h)
**admissible** when kappa >= 0 and h >= 0 are continuous on [t_0, t_1], integral of kappa <= log(u/v_e), and
integral of h <= B/2. Let E(v_e) be the statement: (*) holds on [t_0, t_1) along v(t) = v_e exp(integral of
kappa) for some admissible pair.

(a) **Every coupling on the way.** E(v_e) implies J(u, t) <= J(v_e, t_0) + B/2 for every t in [t_0, t_1].
(b) **The member kappa = 0 at the period u.** For v_e = u the constant schedule kappa = 0 is admissible, and (*)
    for it reads dJ/dt (u, t) <= h(t). So E(u) holds if and only if

        (PV)   integral over [t_0, t_1] of (dJ/dt (u, t))_+ dt  <=  B/2,
               that is  12 u n^3 * integral of (x_u - x_2u)_+ dt <= B/2.

    (PV) is at least J(u, t_1) - J(u, t_0), with equality if and only if x_u >= x_2u on [t_0, t_1].
(c) **Sandwich.** (PV)  =>  E(u)  =>  sup over t in [t_0, t_1] of J(u, t) <= J(u, t_0) + B/2.
    If (MON_u): x_u(t) >= x_2u(t) on [t_0, t_1], then all three are the one statement
    J(u, t_1) - J(u, t_0) <= B/2.

Proof. (a) Fix t. The consumer argument on [t_0, t] (row 708 Theorem TR's proof applied to psi - integral of
h, as in check 1516 (v)) gives J(v(t), t) <= J(v_e, t_0) + integral of h over [t_0, t]. kappa >= 0 gives
v(t) <= v(t_1) <= u, and J is non-increasing in v. (b) With kappa = 0, v(t) = u, an integer, so J(u, .) is
analytic and D_t^+ J = dJ/dt. A continuous h >= 0 with dJ/dt <= h and integral at most B/2 exists if and only
if the continuous function (dJ/dt)_+ has integral at most B/2. The integral of (dJ/dt)_+ is at least the
integral of dJ/dt. (c) The first arrow is (b), the second is (a) with v_e = u. Under (MON_u), dJ/dt >= 0, so
(PV) is J(u, t_1) - J(u, t_0) <= B/2, and J(u, .) is non-decreasing, so the supremum is J(u, t_1). QED

### 2.2 Reading for the row's statement (proved from 2.1 and the entrance; the last item is argued)

1. **The entrance (u, t_0) is supplied by the same estimate as the row's entrance.** J is non-increasing in v,
   so 0 <= J(u, t_0) <= J(ceil(log_2 n), t_0) < 7.4 x 10^(-4) whenever u >= ceil(log_2 n) (true for n >= 2^13).
   The consumer does not care which entrance period is used. So the class of schedules that the consumer
   accepts contains kappa = 0 at the period u.
2. **For that member, (*) is the coupling integral (E2) of row 1515 with a positive part**: the statement
   "the seam response D = 12 u n^3 (x_u - x_2u) has a majorant h with integral at most B/2". This is the seam
   majorant family of row 1515 2.1 (L111-112), the object of row 1511's bound (4) and of its calibrated
   obstruction. So h is a seam majorant, and (*) with a free pair (kappa, h) is the seam family with a
   relative term subtracted. It is not a new family at kappa = 0.
3. **With a free schedule and the budget B/2, (*) has no content beyond the target.** By (c), under (MON_u)
   the statement E(u) is exactly J(u, beta_K) - J(u, t_0) <= B/2: the purity bound with the constant B/2 in
   place of B (up to 7.4 x 10^(-4)). Without (MON_u) it is at least as strong. I cannot prove (MON_u) for
   Wilson SU(2) (it is "the box n^3 x u heats up when the coupling grows"; a plaquette comparison between two
   tori; no Griffiths inequality is on file for SU(2)). Guide, used in no proof: in the scaling picture
   J(u, t) is about (l x)^3 e^(-c x) up to a constant, with x >= 1 the ratio of the correlation lengths at
   beta_K and at t and c = m l/512; this is monotone in t on the scaling range when c >= 3, that is for
   l >= 1536/m, and it has an interior maximum when c < 3. The target may choose l, so (MON_u) is expected
   for the large l that the target would use. It is false for a weight with a bulk transition (K7). The row's rule
   "equivalent is not progress" applies either way: a proof of E(u) is a proof of the target with B/2, and
   under (MON_u) the converse holds too.
4. **(*) is stronger than (PUR-io) in one respect that matters.** By (a), E(v_e) at the cutoff K gives the
   purity bound J(u, t) <= J(v_e, t_0) + B/2 < B for the fixed lattice n^3 x u at **every bare coupling** t in
   [1/25600, beta_K], not only at the calibrated root. (PUR-io) asks it at beta_K only. Letting K run through
   the infinite set (beta_K = B_K + O(1) with B_K = s K + O(log(1 + K)), s > 0: row 1461,
   `gap-crux-direction-astra62.md`, displays (1)-(2), read), E gives: at every bare coupling
   t >= 1/25600, infinitely many lattices n^3 x n/512 have neutral purity above 457/625. That is a neutral
   seed of the bare Wilson lattice at every coupling, a statement of the kind of (NOCRIT) (row 708 5.1; the
   analogous remark for (R11') is in row 1517 6.1, L288-291). Row 1496 4.1 (as quoted in row 1515 1.5,
   L96-97) lists "integration along beta at a fixed lattice" as equivalent to a closed line; (*) is a member
   of that line for every schedule.
5. **What is left of (*) after this.** Only a version in which the schedule and the error are named in
   advance and h is small against the rise of J(u, .), for example the homogeneous version h = 0 with one
   named kappa. That is a pointwise relative inequality. Section 3 puts it into the frame of row 1517.

Not found on file under the words "front", "kappa = 0", "positive variation", "seam majorant" + "two-period"
(grep in Section 7). Item 2 is implicit in row 1515 (E2); I do not call 2.1 new mathematics. It is the
decision the row asks for.

### 2.3 Proposition H: the error term carries the whole target (proved; elementary)

Let (*) hold on [t_0, t_1) along v(t) = v_e exp(integral of kappa), kappa >= 0 continuous, v(t_1) <= u,
h >= 0 continuous. Then

    integral of h over [t_0, t_1]  >=  J(u, t_1) - J(v_e, t_0).

With the row's entrance (t_0 = 1/25600, v_e = ceil(log_2 n), n >= 256 even):
J(v_e, t_0) <= 0.0202 ceil(log_2 n)/n, which tends to 0 as K grows (n = l b^K).

Proof. The consumer inequality J(u, t_1) <= J(v(t_1), t_1) <= J(v_e, t_0) + integral of h, read as a lower bound
for the integral of h. The entrance value: row 708, proof of Corollary TR1 (`gap-mid-max.md` L156),
g(t_0; b^3; beta_0) <= 0.0101 t_0/b for the full trace, and J <= 2 G <= 2 G_full. QED

Consequences (proved from H and 2.1).

1. **The relative term buys at most J(v_e, t_0).** The schedule kappa = 0 at the period u needs
   integral of h = (PV), which under (MON_u) is J(u, t_1) - J(u, t_0) <= J(u, t_1). Every other schedule from
   the row's entrance needs at least J(u, t_1) - 0.0202 ceil(log_2 n)/n. So under (MON_u) no schedule lowers
   the needed error budget by more than 7.4 x 10^(-4), and by an amount that tends to 0 with K. Without
   (MON_u) a schedule can only help by avoiding oscillations of J(u, .) in t.
2. **Homogeneous (*) from the row's entrance is the wrong statement.** With h = 0 it gives
   J(u, beta_K) <= 0.0202 ceil(log_2 n)/n. So at fixed l it can hold at infinitely many K only if the purity
   of the fixed physical box tends to 1 along them. (Guide: a box of physical side l at physical temperature
   512/l has purity below 1 in the limit when its physical gap stays bounded; row 1511's calibrated
   obstruction (i) bounds a uniform covariance rate in physical units, which is close to this but is not
   the box gap; I do not claim a refutation.) If the purity does tend to 1, (PUR-io) holds outright.
3. So from the row's entrance (*) is an **absolute** statement in substance: a seam majorant h whose
   integral is the target value itself, up to o(1). The word "relative" applies only to the choice of path.
   Row 1515 3.3 ("the forced form is relative") was struck by check 1516; the replacement (*) is relative in
   form and absolute in budget.

### 2.4 The homogeneous form needs a warm entrance, and is then again the target (argued; one gap named)

A homogeneous statement (h = 0) can be true only from an entrance with J(v_e, t_e) =: c_e >= J(u, beta_K).
It then says: there is a non-decreasing path from (v_e, t_e) to a point (v, beta_K), v <= u, along which J
does not increase. If J(v, .) is non-decreasing in t for every v in [v_e, u] (MON), the level curve
v_c(t) of J at the level c_e is non-decreasing, and it is such a path exactly when J(u, beta_K) <= c_e. So
under (MON) the homogeneous existence statement is the target with the constant c_e. Gap: the level curve
gives a continuous kappa only if J is C^1 in both variables; at non-integer v the t-derivative of J is not on
file (row 708 Lemma 4.1 gives joint continuity of G and dG/dv only). I did not close this gap, because the
direction that matters, "(*) implies the target at every coupling on the way" (2.1 (a)), needs nothing.

## 3. Algebra of the two-period weights (written after Section 2)

Setting: one box, one coupling t at which the neutral levels are differentiable (input (RK) of row 710, read
in row 1517 2.1), one real v >= 4. p_i = p_i(v), P = sum_j p_j^2 = e^(-J(v, t)) the purity,
w_i = V_i - kappa E_i.

### 3.1 Lemma Q (proved)

(a) p_i(2v) = p_i(v)^2 / P. So homogeneous (*) at (v, t) is

        sum over i >= 1 of q_i w_i <= 0,   q_i := p_i (1 - p_i/P),

    and (VIR_kappa) at (v, t) is the same with p_i in place of q_i.
(b) If s(v) <= 1 then q_i >= 0 for every i >= 1.
(c) If J(v, t) <= j then (2 - e^j) p_i <= q_i <= p_i for every i >= 1. For j = 0.158 (the value
    J_0 + B/2 of the consumer's path) the factor is above 0.82.
(d) (LEV_kappa), that is w_i <= 0 for every i >= 1, implies homogeneous (*) at every (v, t) with s(v) <= 1.
    Without s(v) <= 1 it does not: two excited levels with r_1^v = 1, r_2^v = 1/2, w_1 = -1, w_2 = 0 give
    p_1(v) = 2/5 < p_1(2v) = 4/9, so <w>_v = -2/5 > <w>_2v = -4/9. (With a simple vacuum take r_1^v
    slightly below 1; the strict inequality persists by continuity.)

Proof. (a) p_i(2v) = r_i^(2v)/(1 + s(2v)) = p_i(v)^2 (1 + s(v))^2/(1 + s(2v)), and
P = (1 + s(2v))/(1 + s(v))^2. <w>_v - <w>_2v = sum_(i>=1) w_i (p_i(v) - p_i(2v)) because w_0 = 0.
(b) s <= 1 means p_0 >= 1/2. For i >= 1, p_i <= 1 - p_0 <= 1/2 <= p_0. x(1 - x) increases on [0, 1/2], so
p_i (1 - p_i) <= (1 - p_0) p_0 <= p_0^2, that is p_i <= p_0^2 + p_i^2 <= P. (c) p_i <= 1 - p_0 = s/(1 + s),
and G <= J (Lemma B of row 1515) gives s <= e^j - 1, so p_i <= 1 - e^(-j). P >= e^(-j). So
p_i/P <= e^j - 1. (d) from (a), (b); the example: weights 1, 1, 1/2 give p_1(v) = 1/(5/2), and squared
weights 1, 1, 1/4 give p_1(2v) = 1/(9/4). QED

### 3.2 Lemma DY (the thermal sum is a dyadic superposition of two-period functions; proved)

For every real v >= 4 and every t:  G(v, t) = sum over k >= 0 of 2^(-k-1) J(2^k v, t).
Consequence: if homogeneous (*) holds on [t_0, t_1) along each of the characteristics 2^k v(t), k >= 0, of one
schedule kappa, then G(v(t), t) <= G(v_0, t_0) on [t_0, t_1]: the conclusion of Theorem TR of row 708 for the
neutral trace. With errors h_k on the k-th characteristic the bound is
G(v(t), t) <= G(v_0, t_0) + sum_k 2^(-k-1) integral of h_k.

Proof. sum over k < m of 2^(-k-1) (2 G(2^k v) - G(2^(k+1) v)) = G(v) - 2^(-m) G(2^m v), and
0 <= G(2^m v) <= G(v). The consumer on the k-th characteristic gives J(2^k v(t), t) <= J(2^k v_0, t_0) +
integral of h_k; multiply by 2^(-k-1) and sum (all terms are non-negative and the series converge). QED

Reading. (i) (*) on the dyadic ladder of one schedule is **stronger** than the transport conclusion of
(VIR_kappa) on its base characteristic. (ii) On one characteristic the two are incomparable for one fixed
kappa (check 1516's three-level example: coefficients 8 w_1 + w_2 against 7 w_1 + w_2; by Lemma Q (a) these
are p = (8, 1)/73 and q = (392, 56)/4161 = (56/4161)(7, 1), with q_1/p_1 = 49/57 = 0.8596 and
q_2/p_2 = 56/57 = 0.9825; hand arithmetic, 4161 = 73 x 57). (iii) The separation lives in the margin of Lemma Q (c): the two tests weigh the same
levels with weights that differ by a factor between 0.82 and 1 on the consumer's path.

### 3.3 Proposition F: (*) in the frame of row 1517 (proved in the setting of Lemma CONJ)

Setting of Lemma CONJ (row 1517 2.1, `gap-r11-tool-design-fable.md` L66-86), on the neutral space:
That = T/lambda_0, Phi(r) = r log(1/r), D_A = That' - [A, That] for bounded A. Put, for real v >= 4,

    rho_v := That^(v-1)/Tr That^v,    sigma_v := rho_v - rho_2v,

and let rho_v^+, sigma_v^+ be their parts on the orthogonal complement of the vacuum vector. Then, at a
coupling where the neutral levels are differentiable:

(a) dJ/dt = 2v Tr(sigma_v D_A) for every bounded A, and -v dJ/dv = 2v Tr(sigma_v Phi(That)). So

        (*) at (v, t)   <=>   Tr( sigma_v^+ (D_A - kappa Phi(That)) ) <= h/(2v),
        (VIR_kappa) at (v, t)   <=>   Tr( rho_v^+ (D_A - kappa Phi(That)) ) <= 0.

(b) sigma_v^+ and rho_v^+ are functions of That. If s(v) <= 1 then sigma_v^+ >= 0, and if J(v, t) <= j then
    (2 - e^j) rho_v^+ <= sigma_v^+ <= rho_v^+.
(c) rho_v = sum over k >= 0 of sigma_(2^k v) (norm convergent on the complement of the vacuum).
(d) If the form inequality Re <phi, D_A phi> <= kappa <phi, Phi(That) phi> holds for one A and all phi
    orthogonal to the vacuum, then homogeneous (*) holds at every (v, t) with s(v) <= 1.

Proof. (a) In the eigenbasis, Tr(rho_v D_A) = sum_i r_i^(v-1) <psi_i, D_A psi_i>/Tr That^v
= sum_i r_i^(v-1) r_i'/Tr That^v (Lemma CONJ (a)) = sum_i p_i(v) V_i, using r_i' = V_i r_i. So
Tr(sigma_v D_A) = <V>_v - <V>_2v = (dJ/dt)/(2v). Tr(rho_v Phi(That)) = sum_i p_i(v) E_i = Ebar_v. The vacuum
contributes 0 to both forms: r_0 = 1 for all t, so <psi_0, D_A psi_0> = r_0' = 0, and Phi(1) = 0.
(b) sigma_v = f(That) with f(r) = r^(v-1)/Tr That^v - r^(2v-1)/Tr That^2v, and f(r_i) = q_i/r_i for i >= 1;
Lemma Q (b), (c). (c) the telescoping of Lemma DY at operator level; rho_(2^m v)^+ tends to 0 in norm.
(d) sigma_v^+ is a non-negative combination of the projections on the excited eigenvectors, by (b). QED

**The row's three questions on the frame.**

1. *Is (*) a form bound for a generator class?* Yes, in exactly the sense in which (VIR_kappa) is one: it is
   the form D_A - kappa Phi(That) evaluated in one positive operator, sigma_v^+ in place of rho_v^+. The
   generator classes of table 2.2 of row 1517 do not depend on the operator in which the form is tested. So
   the table is unchanged: A = 0 (Way 1), norm and locality (Way 2), quasi-adiabatic (needs the gap),
   vacuum transport fields (route B1 with (T), (T-avg)), all A ((LEV_kappa), which implies (*) by (d)).
2. *Does the selective form bound of row 1517 6.1 reappear?* Yes, word for word, with "the cold thermal
   states rho_v^+" replaced by "the cold two-period operators sigma_v^+". It is not a weaker demand: on the
   consumer's path 0.82 rho_v^+ <= sigma_v^+ <= rho_v^+, the two operators commute, and by (c) the cone
   generated by the sigma contains the rho. A method that proved the bound for sigma_v^+ and not for rho_v^+
   would have to resolve single levels inside that margin; that is knowledge of the eigenvectors, the case
   Lemma CONJ (c) calls equivalent.
3. *The floor*: Section 4.

## 4. The floor for (*) (written after Section 3)

### 4.1 Corollary FLOOR-2 (proved; the contrapositive of the consumer, with the cold refinement)

Let a model have a positive transfer operator on a box and a projection P_0 that commutes with it and keeps
the vacuum (P_0 = 1 is allowed), with the regularity of row 708 Lemma 4.1 for the projected trace. Let
s_0 < s_1, an integer u >= v_e >= 4, and eta >= 0 with J(v_e, s_0) <= eta and J(u, s_1) > eta + B/2. Then
for every admissible pair (kappa, h) and every eps > 0 there is s in [s_0, s_1) with

    J(v(s), s) <= eta + B/2 + eps   and   D_t^+ J(v(s), s) > 2 kappa(s) v(s) (Ebar_v - Ebar_2v) + h(s).

In words: on the way the two-period inequality fails at a point where the box n^3 x v(s) is still pure.

Proof. Put Psi(s) = J(v(s), s) - integral of h over [s_0, s], continuous, Psi(s_0) <= eta. If (*) held at
every s with Psi(s) < eta + eps, then Psi <= eta on [s_0, s_1]: otherwise let s' be the infimum of the s
with Psi(s) > eta; Psi(s') = eta, so Psi < eta + eps on a right neighbourhood of s', where (*) makes Psi
non-increasing (the argument in the proof of Theorem TR), against the choice of s'. Psi(s_1) <= eta gives
J(u, s_1) <= J(v(s_1), s_1) <= eta + B/2, against the hypothesis. So (*) fails at some s with
Psi(s) < eta + eps, where J(v(s), s) < eta + eps + B/2. QED

### 4.2 Where it applies (the model facts are recalled or read, as marked)

- **Ising member of row 705 4.1** (four-dimensional Ising, P_0 = 1). Read, proved there for each fixed box:
  as the coupling grows, lambda_1/lambda_0 tends to 1 and all other ratios to 0. So J(u, .) tends to
  2 log 2 - log 2 = log 2 = 0.693 > B/2 + eta for every u and every box. Entrance at small coupling:
  recalled (high-temperature expansion), constants not computed. So FLOOR-2 applies on every box: (*)
  fails for every schedule and every error within the budget, at a pure point, before the purity reaches
  about 0.855. The member kappa = 0 fails in the plain form: the positive variation of J(u, .) exceeds B/2.
- **Ising with the spin-flip-even projection as P_0** (not the class member; added because (*) is a
  neutral statement). In a fixed box at large coupling the odd partner of the vacuum is projected out and
  J tends to 0. So the two-phase region is not a ceiling for the neutral purity. The floor then sits at the
  critical coupling only (guide: there the even gap of the box n^3 is of order 1/n and u = n/512, so the
  box is hot). The same holds for Z_2 gauge theory at large beta with the centre-neutral projection: the
  seven flux partners (row 705 4.1, last line) are projected out.
- **Compact U(1)** (recalled, as in row 708 L58 and row 1517 4.2: a seed at strong coupling; no gap at weak
  coupling, Guth; Frohlich and Spencer). Guide for the size: photon levels 2 pi abs(k)/n at u = n/512 have
  u E = 2 pi abs(k)/512, so the box is hot and J is large. FLOOR-2 then applies across the transition.
- **K7** (the mixed-action weight on its first-order line, row 708 L48; recalled). Two coexisting phases
  that no centre symmetry exchanges: purity near 1/2 on large boxes at coexistence. FLOOR-2 applies. So no
  proof of (*) can use the group, the centre, the twists, reflection positivity or the class lemmas only;
  this is the same test as for (VIR_K).

**At which step.** The consumer has one analytic step, (*) itself. FLOOR-2 says it fails at a pure point of
the path inside the crossing interval. In the frame of Section 3 the failing line is the form bound for D_A
tested in sigma_v^+ (Proposition F (a)); for the member kappa = 0 it is the seam majorant: the positive part
of 12 u n^3 (x_u - x_2u) has integral above B/2. This is Corollary FLOOR of row 1517 with rho replaced by
sigma, and with one difference: the neutral projection removes the symmetry-related two-phase ceiling
(second and third bullets), so for (*) the Ising-type failure is located at the critical window, not in the
whole ordered phase.

## 5. The integer-period forms (the row asks for one; written after Section 4)

### 5.1 The finite-period test of check 1516 (verified by hand; HOLDS)

For integer v >= 2 at one coupling:
0 <= log [ Z_+(v) Z_+(2v) / (Z_+(v+1) Z_+(2v-1)) ] <= Ebar_v - Ebar_2v.
Proof (two lines, as in check 1516 L78). The vacuum cancels (v + 2v = (v+1) + (2v-1)), so the logarithm is
[G(v) - G(v+1)] - [G(2v-1) - G(2v)] = integral of Ebar over [v, v+1] minus integral of Ebar over [2v-1, 2v].
Ebar_w is non-increasing in w and v + 1 <= 2v - 1. QED
It is a pointwise sufficient test for the right side of (*). It does not transport.

### 5.2 Lemma ST (integer staircase; proved; an identity)

Let 4 <= v_0 < v_1 < ... < v_m be integers and t_0 < t_1 < ... < t_m couplings. Then

    J(v_m, t_m) - J(v_0, t_0) = sum over j < m of [ rise_j - drop_j ],
    rise_j := integral over [t_j, t_(j+1)] of 12 v_j n^3 (x_(v_j) - x_(2 v_j)) dt,
    drop_j := J(v_j, t_(j+1)) - J(v_(j+1), t_(j+1)) >= 0.

For unit steps, drop_j = log [ Z_+(v)^2 Z_+(2v+2) / (Z_+(v+1)^2 Z_+(2v)) ] at v = v_j, t = t_(j+1).
Proof. Telescoping; rise_j = J(v_j, t_(j+1)) - J(v_j, t_j) because J(v_j, .) is analytic; the drop is
non-negative because J is non-increasing in v. QED

Reading. (i) The consumer needs no real characteristic and no non-integer period: the integer-period
statement "sum of (rise_j - drop_j)_+ <= B/2 along one staircase from (v_0, t_0) to (u, beta_K)" gives
J(u, beta_K) <= J(v_0, t_0) + B/2. This removes the regularity question that check 1516 leaves ("transport
still requires control along the real characteristic"). (ii) It is no first lemma: by the identity the sum
of all (rise_j - drop_j) is the target quantity itself, whatever the staircase. The staircase with no step
(v = u throughout, entered at (u, t_0)) is the member kappa = 0 of Theorem EQ. (iii) A step-wise form with
content is "rise_j <= drop_j", that is J(v_j + 1, t_(j+1)) <= J(v_j, t_j): the purity does not fall when one
time layer is added and the coupling moves by t_(j+1) - t_j. By Proposition H it can hold on a whole
staircase only from a warm entrance, and then it is the pointwise relative statement of Section 3 in
finite-difference form.

## 6. Verdict, registry change, next two rows

### 6.1 Decisive outcome: EQUIVALENT (an explicit reduction; no proof of (*), no refutation of (*))

(*) with the row's entrance and budgets splits into two parts, and each is a line already on file.

1. **Budget part = the seam majorant of row 1515 (E2) = the target.** Proposition H: the error h must carry
   J(u, beta_K) up to 0.0202 ceil(log_2 n)/n. Theorem EQ: the schedule kappa = 0 at the period u (entered at
   (u, t_0), which the same strong-coupling estimate supplies) turns (*) into "the positive part of
   12 u n^3 (x_u - x_2u) has integral at most B/2 on [1/25600, beta_K]". Under (MON_u) that is exactly
   J(u, beta_K) - J(u, t_0) <= B/2, the target with B/2 for B. Without (MON_u) it is stronger. For every
   schedule, (*) gives the purity bound at every bare coupling on the way, so it is a member of the line
   "integration along beta at a fixed lattice", which row 1496 4.1 (`gap-k2-direction-checkpoint-fable.md`
   L126: "Equivalent to a closed line. The integrand is the target at each coupling.") and row 1380's
   table already close.
2. **Relative part = trigger (R11) in the frame of row 1517, with sigma_v^+ for rho_v^+.** Proposition F:
   (*) at a point is the form D_A - kappa Phi(That) tested in the positive operator sigma_v^+, and
   0.82 rho_v^+ <= sigma_v^+ <= rho_v^+ on the consumer's path. The generator table of row 1517 2.2 is
   unchanged, (LEV_kappa) implies both, the selective form bound of row 1517 6.1 is the missing component of
   both, and the floor is the same (FLOOR-2), with the one difference that the neutral projection removes
   symmetry-related phase coexistence.
3. **The separation of check 1516 stands, and does not change the verdict.** For one fixed kappa and h = 0
   the two pointwise inequalities are incomparable (I re-did the arithmetic of the three-level example,
   3.2). The separation sits inside the factor 0.82 to 1 of Lemma Q (c). In existence form each statement
   is its own endpoint bound (J(u, beta_K) for (*), G(u, beta_K) for the neutral (VIR_kappa)), and the two
   endpoint bounds agree up to the factor 2 of Lemma B; on the dyadic ladder (*) implies the conclusion of
   (VIR_kappa) (Lemma DY).

Not shown: that (*) fails for Wilson SU(2). Nothing here refutes it; it is true along some path if the
target is true with B/2 and J(u, .) does not oscillate. Not shown: (MON_u). Not closed: the t-regularity of
J at non-integer periods (named in 2.4; avoided by Lemma ST).

Equivalence statement, as the lead's rule asks: I cannot show that (*) is weaker than the target, and I
show that it is at least as strong (2.1 (a)), and exactly as strong under (MON_u) with the constant B/2
(2.1 (c)). So TWO-PER is not progress in the sense of the rule, in any of its forms.

### 6.2 Registry change proposed (for the lead; I did not edit the registry)

- TWO-PER (`open-registry.md` L1020): replace "open; no proof for Wilson" by "equivalent (row 1520,
  unchecked): budget part = seam majorant (E2) of row 1515 = the target at every bare coupling; relative
  part = (R11) tested in sigma_v^+; merged under R11". Keep "separated from (VIR_K)" with the addition "for
  one fixed kappa and h = 0 only".
- R11 (L1018): the sentence "one of two candidate relative inputs; the other is TWO-PER" becomes "TWO-PER is
  the same form bound tested in a comparable operator (row 1520 Proposition F)".
- One fact worth a registry note: every input of the kind "a bound along beta on one fixed lattice from
  the strong-coupling entrance" implies the neutral purity bound of that lattice at every bare coupling
  below beta_K (2.1 (a) for (*); row 1517 6.1 for (R11')). So that family cannot be weaker than a bare
  statement in the band, whatever the integrand.

### 6.3 The next two rows and their decisive outcomes

I propose no attack row on (*).

**Row 1, `gap-twoperiod-solve-fable-check-astra62` (cross-provider check of this file; gpt-6.2-astra).**
Order: (i) Theorem EQ (a)-(c), and first of all whether the consumer of check 1516 (v) accepts the entrance
(u, t_0) and the schedule kappa = 0, as 2.2 item 1 claims from that check's own text; (ii) Proposition H;
(iii) Lemma Q with the arithmetic of the three-level example; (iv) Lemma DY; (v) Proposition F (the two
trace formulas, in the setting of Lemma CONJ, and the claim that the generator table is unchanged);
(vi) Corollary FLOOR-2 and the four model bullets (which facts are proved, which recalled); (vii) Lemma ST;
(viii) whether the t-derivative of J at non-integer periods can be bounded (it would make 2.4 exact).
Decisive outcome: HOLDS, and the registry changes as in 6.2 (TWO-PER merged under R11); or FAILS at a named
line, and TWO-PER stays open as written. If (i) fails because the consumer needs v_0 = ceil(log_2 n) for a
reason I did not see, the fallback is Proposition H plus 2.1 (a), which do not use the entrance (u, t_0).

**Row 2, `gap-purity-monotone-decide` (only if the lead wants the equivalence without a hypothesis; Claude
Fable 5.2 medium or gpt-6.2-astra; I rank it low).** Decide (MON_u) for Wilson SU(2): x_u >= x_2u for the
neutral mass-weighted mean plaquette on n^3 x u against n^3 x 2u, on [1/25600, beta_K], for u = n/512 and
large l. Decisive outcome: PROVED, and then (PUR-io) with B/2 at one cutoff is equivalent to the member
kappa = 0 of (*), and (PUR-io) at beta_K implies the neutral purity of the same lattice at every smaller
bare coupling (the target is then at least as strong as a bare statement in the band; this binds trigger
(R12) from the other side); or REFUTED at a named coupling and size by an exact argument (strong-coupling
expansion or a small exact case), and then every fixed-lattice transport is strictly stronger than the
target and the family is retired with that reason; or OPEN with the first failing step (I expect this:
it is a sign statement for SU(2) with no correlation inequality on file). Either decisive outcome changes
a registry line and no outcome supplies a method for the seed. The lead may skip it.

## 7. Repo search, labels, credits, what was not done

### 7.1 Repo search

- Local, before calling anything new: `library/open-core.md` has no hit for "two-period", "TWO-PER",
  "positive variation", "purity ... monotone in the coupling", "plaquette monotone", "dyadic superposition".
  `library/open-registry.md`: TWO-PER L1020, R11 L1018, R12 L1019. `FINISH.md`: "two-period" occurs in 15
  rows (1149, 1151, 1328, 1330, 1333, 1337, 1342, 1349, 1354, 1362, 1370, 1462, 1475, 1511, 1520); I printed
  the context of each: all use the word for the purity Z_+(2u)/Z_+(u)^2 as a target or for a two-period
  defect, none states (*), Theorem EQ, Proposition H, Lemma Q, Lemma DY or Lemma ST. The sentence "the
  integrand is the target at each coupling" is on file (row 1496 4.1, L126); Theorem EQ is its exact form
  for (*). "sigma_v", "rho_v - rho_2v" in `library/gap-*.md`: no file but this one.
- Cross-branch (bare blob-less depth-1 fetch in my own scratch folder /tmp/ym4d-row1520-scratch): pattern
  "TWO-PER, two-period transport / relative / response, purity transport, seam majorant, difference of the
  mean energies, x_u - x_2u, positive variation of J" on the 83 mass-gap `.md` files of main
  (`research/mass-gap/`) and on the 4 files `MASS_GAP*.md`, `RTARGET.md` of PR 10114: no hit. PRs 10133,
  10134, 10141, 10144 were not searched by me; check 1516 searched all five refs for the two-period
  relative bound and reports no hit (its L5).
- Sussman-Alpoge (with Claude and Codex): not searched again in this row. Check 1516 L10 records that the
  outline and CA-I to CA-III at 31a47c543775 hold no statement on purity or transport along the coupling
  (outline 588-599, 4638-4641, 31871-31882; CA-I 2699-2713). No statement of theirs is used in a proof
  here. The calibrated roots beta_K come from their release through rows 1451, 1453, 1461 (read).

### 7.2 Labels

- **Proved here** (one author, checked by no one, all elementary): Theorem EQ; Proposition H; Lemma Q;
  Lemma DY; Proposition F (in the setting of Lemma CONJ of row 1517, at couplings where the neutral levels
  are differentiable); Corollary FLOOR-2 (the model bullets rest on the facts marked there); the test of
  5.1; Lemma ST.
- **Read**, not re-derived: the statement (*), its consumer and the entrance (check 1516 (v)); Theorem TR,
  Lemma 4.1, Lemma 4.2, the start of Corollary TR1 (row 708; checked by Claude Opus 5.5, row 709), in the
  neutral form asserted by check 1516 (iii); Lemma B (row 1515, confirmed by check 1516 (i)); Lemma CONJ
  and table 2.2 (row 1517, unchecked, check 1519 pending); the Ising member (row 705 4.1); the calibration
  (row 1461 (1)-(2)); row 1496 4.1.
- **Argued**: 2.2 item 3 beyond the sandwich; 2.3 consequence 2 (no refutation claimed); 2.4.
- **Guessed**: that (MON_u) holds for Wilson SU(2) at the sizes the target uses.
- **Guide only**: the scaling-picture remark on (MON_u); the sizes in the model bullets of 4.2.
- **Recalled**: high-temperature seed of the Ising member; Guth, Frohlich and Spencer for compact U(1);
  the first-order line of the mixed action (Bhanot and Creutz), all as in rows 705, 708, 1517.

### 7.3 Not done

- (*) is not proved and not refuted for Wilson SU(2). (PUR-io), the seed and the gap are not moved.
- (MON_u) is not decided. The t-derivative of J at non-integer periods is not bounded (gap named in 2.4).
- For the row's entrance v_0 = ceil(log_2 n) I did not construct the steep ramp to the period u (it needs
  that bound); Theorem EQ (b) uses the entrance (u, t_0), Proposition H and EQ (a) use any entrance.
- No numeric run (memory read 38 percent free; nothing here needed one). No Lean. No commit, no push.
- The start constants for the Ising member and for compact U(1) were not computed.

### 7.4 Credit

gpt-6.2-astra (check 1516) for (*), its consumer, the entrance, the integer-period test and the
three-level separation. Row 708 (Claude Fable 5.2 max) for Theorem TR, (VIR_K), (LEV_K), Corollary TR1;
check 709 (Claude Opus 5.5). Rows 1511 (gpt-6.2-astra) and 1515 for (E2), the seam majorant family and
Lemma B; row 1496 for the line "integration along beta at a fixed lattice". Row 1517 for Lemma CONJ, the
generator table and Corollary FLOOR. Row 705 for the Ising member; row 1461 for the calibration. Kato and
Rellich for analytic perturbation theory. Guth; Frohlich and Spencer; Bhanot and Creutz (recalled).
Sussman and Alpoge, with Claude and Codex, for the release and the account; Balaban for the block method;
neither is used in a proof here.

## 8. Result

RESULT: Row 1520 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; no numeric run because memory was at 38 percent free and nothing needed one, no Lean, nothing committed). Decisive outcome: EQUIVALENT. (*) is not proved and not refuted for Wilson SU(2); it reduces to two lines already on file. Proved by hand, all elementary: Theorem EQ (for every schedule, (*) gives the purity bound J(u, t) <= J_entrance + B/2 of the fixed lattice at every bare coupling t in [1/25600, beta_K], not only at the root; the schedule kappa = 0 at the period u, entered at (u, t_0) by the same strong-coupling estimate, turns (*) into "the positive part of 12 u n^3 (x_u - x_2u) has integral at most B/2", the coupling integral (E2) of row 1515; under the monotonicity (MON_u): x_u >= x_2u, that is exactly the target with B/2 for B); Proposition H (in every case the error term must carry the target value: integral of h >= J(u, beta_K) - 0.0202 ceil(log_2 n)/n, so from the cold entrance (*) is an absolute seam-majorant statement and its relative term buys at most 7.4 x 10^(-4); homogeneous (*) from that entrance would force the purity to 1); Lemma Q (homogeneous (*) is sum q_i w_i <= 0 with q_i = p_i (1 - p_i/P), non-negative when s <= 1 and within a factor 0.82 to 1 of the thermal weights on the consumer's path; (LEV_kappa) implies it there); Lemma DY (G(v) = sum 2^(-k-1) J(2^k v), so (*) on the dyadic ladder implies the conclusion of (VIR_kappa)); Proposition F (the frame of row 1517 applies: (*) is the form D_A - kappa Phi(That) tested in the positive operator sigma_v^+ = (rho_v - rho_2v)^+, with 0.82 rho_v^+ <= sigma_v^+ <= rho_v^+; the generator table is unchanged and the selective form bound of row 1517 6.1 reappears word for word); Corollary FLOOR-2 ((*) fails for every schedule and error within budget at a point where the box is still pure, across any coupling interval that ends in an impure box: the Ising member, compact U(1) and the mixed action given recalled facts; the neutral projection removes symmetry-related coexistence, so there the failure sits at the critical window); Lemma ST (an integer staircase identity that removes the real characteristic from the consumer and is the target in sum). Check 1516's separation from (VIR_K) stands for one fixed kappa with h = 0 and does not change the verdict. Open: (PUR-io), the seed, the gap; (MON_u); the t-regularity of J at non-integer periods. Proposed: merge registry line TWO-PER under R11 as equivalent after a check. Next: a cross-provider check of this file (Theorem EQ and the entrance (u, t_0) first); then, optional and low, a row that decides (MON_u).
