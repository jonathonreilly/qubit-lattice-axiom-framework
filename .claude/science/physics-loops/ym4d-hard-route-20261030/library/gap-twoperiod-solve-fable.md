lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T17:37Z

# Row 1520, gap-twoperiod-solve-fable: the two-period transport input (*) of check 1516

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned at commit 48951d201. Proved-by-Claude items
below are not yet checked by another model. Nothing here is a status claim.

## Status log (times from date -u)

- 2026-11-25T05:37Z start. File created. Plan below.
- 2026-11-25T05:38Z read: row 1520, FINISH rule sections, GOAL.md, check 1516 in full (section (v) = statement (*), consumer, separation example), row 1517 in full (CONJ, VOL, TR2, COLD, FLOOR, 6.1).
- 2026-11-25T05:45Z Sections 1-2 written: Theorem EQ (the existence form of (*) contains kappa = 0 at period u, which is the target in integrated form; (*) forces the purity bound at every bare coupling on the way). Registry: TWO-PER at open-registry L1020; R11 L1018.

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
   tori; guide: true in the scaling picture; no Griffiths inequality is on file for SU(2)). The row's rule
   "equivalent is not progress" applies either way: a proof of E(u) is a proof of the target with B/2, and
   under (MON_u) the converse holds too.
4. **(*) is stronger than (PUR-io) in one respect that matters.** By (a), E(v_e) at the cutoff K gives the
   purity bound J(u, t) <= J(v_e, t_0) + B/2 < B for the fixed lattice n^3 x u at **every bare coupling** t in
   [1/25600, beta_K], not only at the calibrated root. (PUR-io) asks it at beta_K only. Letting K run through
   the infinite set (beta_K is unbounded; row 1511's calibration, read), E gives: at every bare coupling
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
