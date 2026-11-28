lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T17:23Z

# Check of row 1509 (Lean Stage 1e, Periodic.lean) by reading: queue row 1518

Started 2026-11-25T05:23Z (date -u) on Mac mini worker 2, Claude Opus 5.5 high, at commit 514eb85cd.
Author of the checked work: gpt-6.2-astra max (row 1509, lane commit e4b1f4b9a). This is a
cross-provider check by reading only; the lead replays the build and prints axioms.

## Plan

1. Read `lean/gapchain/RECEIPT-1e.md`, `lean/gapchain/GapChain/Periodic.lean` in full, and the parts
   of `Wilson.lean`, `Transfer.lean`, `TheoremS.lean` that Periodic.lean uses or that consume TorusData.
2. Find the definition of `cyclic` fixed for rows 1508-1509 (FINISH rows 1506-1508, check 1507) and compare (Q1).
3. Check the reindexing (site, linkIndex, layers, measurePreserving_layers) (Q2).
4. Check action_eq_layers, density_eq_layerProduct, integral_layerWeight against check 1507 Q3 steps 2 and 4 (Q3).
5. Z_eq_cyclic hypotheses and the case a = 0 / small a (Q4).
6. torusData_of_trace faithfulness (Q5) and vacuity of TorusData fields (Q6).
7. Verdict.

## Steps

### Sources read (step 1)

`lean/gapchain/RECEIPT-1e.md` and `lean/gapchain/GapChain/Periodic.lean` (299 lines) in full;
`Wilson.lean` (575 lines) in full; the Wilson section of `Transfer.lean` (lines 492-768:
spatialSides, Vertex, Edge, Slice, Gauges, sliceHaar, gaugeHaar, spatialStep, spatialAction,
gaugeAction, temporalAction, temporal, transferKernel, transferKernel_apply, transfer,
transfer_boxSpectrum); FINISH rows 1503-1509; check 1507 (`library/lean-gap-chain-stage1c-check-opus.md`)
Q3-Q4 and verdict. `Trace.lean` (row 1508) is not in this checkout at 514eb85cd
(`git ls-files | grep Trace.lean` empty), so its exact interface could not be compared here.

## Q1. Is `cyclic` the fixed definition?

Periodic.lean lines 21-23:

    def cyclic (β : ℝ) (R : Box) (a : ℕ) : ℝ :=
      ∫ u : Fin a → Slice R, ∏ t : Fin a, transferKernel β R (u t, u (finRotate a t))
        ∂(Measure.pi fun _ => sliceHaar R)

Check 1507 Q3 fixed it as: "∫ over u : Fin a → Slice R, under `Measure.pi (fun _ => sliceHaar R)`, of
prod_{t : Fin a} transferKernel β R (u t, u (finRotate a t))". Symbol for symbol the same: same
argument order (β, R, a), same measure, same kernel, same argument order K(u t, u (t+1)) inside the
kernel (the order check 1507 showed is forced by the temporal plaquette orientation without using
pointwise symmetry of K), finRotate a in the same place. **Yes.** Caveat: the row 1508 `Trace.cyclic`
body is not on disk here; RECEIPT-1e says its consumer re-typed "the exact row 1508 interface" in a
separate namespace and proved equality by `rfl`. That consumer is in the author's /tmp, not in the
repository, so the rfl join with the real Trace.lean is still to be done (RECEIPT-1e next row 1 says so).

## Q2. The reindexing

- `site a R := Fin.consEquiv (fun i => Fin (sides a R i))`, so `site a R (t, x) = Fin.cons t x`:
  coordinate 0 is t, coordinate j.succ is x j. Time is coordinate 0, matching `sides a R = ![a, R.x, R.y, R.z]`
  (Wilson.lean 287). The fibre types `Fin (sides a R 0)` = `Fin a` and `Fin (sides a R j.succ)` =
  `Fin (spatialSides R j)` are definitionally equal (vecCons reduces on 0 and succ), so no `Fin.cast`
  was needed; check 1507 note (a) is resolved this way.
- `linkIndex`: `inl (t, (x, i)) ↦ (site (t,x), i.succ)` (spatial edge (x,i) of slice t is the link in
  direction i+1 at (t,x)); `inr (t, x) ↦ (site (t,x), 0)` (the temporal link at (t,x)). Inverse by
  `Fin.cases` on the direction. Both inverse laws are proved, so it is a bijection, and each link occurs
  exactly once.
- `layers` = (precomposition with linkIndex, `piCongrLeft.symm`) then `sumPiEquivProdPi` then `curry`
  on each factor. Hence `(layers a R U).1 t (x,i) = U (site (t,x), i.succ)` and
  `(layers a R U).2 t x = U (site (t,x), 0)`. These two equalities are stated inside
  `action_eq_layers` as `spaceLink` and `timeLink` and closed by `rfl` (lines 95-97), so given the
  lead's replay they are kernel-confirmed, not only read. **The temporal link of (t,x) is the gauge
  at x for layer t**, as asked.
- `measurePreserving_layers`: `haar (sides a R)` (product linkHaar over all links) goes to
  `(pi sliceHaar).prod (pi gaugeHaar)`; `sliceHaar R` and `gaugeHaar R` are themselves products of
  `linkHaar` (Transfer.lean 504-505). Proof is the composition of three Mathlib measure-preserving
  facts (`measurePreserving_piCongrLeft`, `measurePreserving_sumPiEquivProdPi`,
  `infinitePi_map_curry` with `infinitePi_eq_pi`). The statement is the right one.
- Direction of finRotate: `timeStep` proves `step (site (t,x)) 0 = site (finRotate a t, x)`;
  `step` (Wilson.lean 105-106) rotates coordinate k by `finRotate (n k)`, and `n 0 = a`. `cyclic` uses
  the same `finRotate a t`. `spaceStep` proves `step (site (t,x)) i.succ = site (t, spatialStep x i)`
  with `spatialStep` rotating by `finRotate (spatialSides R j)`. **Same direction on both sides. Yes.**


## Q3. The action split and the gauge integration

**action_eq_layers** (lines 87-153) states, for every a, R and U,

    action U = ∑ t : Fin a, (spatialAction (u t) + temporalAction (u t, gaugeAction R (u (finRotate a t), g t)))

with u = (layers a R U).1, g = (layers a R U).2. Check 1507 Q3 step 2 is: the planes (j+1,k+1), j<k,
at (t,v) sum to spatialAction (U t); the planes (0,j+1) give
g_t(v) U(t+1)_(v,j) g_t(v+e_j)^-1 U(t)_(v,j)^-1 = (gaugeAction R (U(t+1), g_t))_(v,j) (U(t)_(v,j))^-1,
summing to temporalAction (U t, gaugeAction R (U(t+1), g_t)). The Lean statement is exactly that sum.
Read through the proof:

- `planes : Fin 3 ⊕ SpatialPlane ≃ Plane`, `inl i ↦ (0, i.succ)`, `inr (j,k) ↦ (j.succ, k.succ)`,
  both inverse laws proved: the six geometric planes split as 3 temporal + 3 spatial, each once.
- Spatial terms: `transport U (site (t,x)) j.succ k.succ` rewritten with `spaceStep`, `spaceLink` to
  u t (x,j) · u t (x+e_j, k) · (u t (x+e_k, j))^-1 · (u t (x,k))^-1, the summand of `spatialAction`
  (Transfer.lean 512-515) with (p.1.1, p.1.2) = (j,k), same order.
- Temporal terms: `transport U (site (t,x)) 0 i.succ` = U(x,0) U(step x 0, i+1) U(step x (i+1), 0)^-1 U(x,i+1)^-1
  = g t x · u (t+1) (x,i) · (g t (x+e_i))^-1 · (u t (x,i))^-1 (by `timeStep`, `spaceStep`, `timeLink`,
  `spaceLink`); and `temporalAction (u t, gaugeAction R (v, g t))` has summand
  1 - halfTrace ((g t x · v (x,i) · (g t (x+e_i))^-1) · (u t (x,i))^-1) (Transfer.lean 531-540). Same word,
  same order of factors; no use of trace cyclicity or inversion.
- Before the split, `action_eq_geometric` (Wilson.lean 145) has already turned the ordered-plane sum
  with weight 1/2 into one term per (site, canonical plane); row 1505 checked that.

**density_eq_layerProduct** (172-187): density β U = ∏_t layerWeight β (u t) (u (t+1)) (g t), where
layerWeight β u v g = exp(-β (S u + S v)/2) · temporal β R (u, gaugeAction R (v, g)). This is check 1507
step 3 (half the spatial action on each endpoint; rotation permutes Fin a, `Equiv.sum_comp (finRotate a)`):
exp(-β Σ_t (S_t + V_t)) = exp(Σ_t (-β(S_t + S_{t+1})/2 - β V_t)) because Σ_t S_{t+1} = Σ_t S_t. Correct
for every a, including a = 1 (both halves on u 0) and a = 0 (empty sums and products).

**integral_layerWeight** (160-169): ∫ g, layerWeight β u v g ∂gaugeHaar R = transferKernel β R (u, v).
It pulls out the constant exp(-β(S u + S v)/2) and matches the integrand of `transferKernel_apply`
(Transfer.lean 552-555), ∏_e exp(-β (1 - halfTrace (g e.1 · v e · (g (spatialStep e.1 e.2))^-1 · (u e)^-1))),
by exp of a sum = product of exps. Gauge on the second argument v, as in `transferKernel`. This is
check 1507 step 4 for one time slice.

**Z_eq_cyclic** (191-214) does step 4 for all slices: change of variables by
`measurePreserving_layers` (symm); integrability from `integrable_density` carried through the
measure-preserving map; Fubini (`integral_prod`) with slices outer and gauges inner; pointwise the
density is the product over t of functions of g t alone (`density_eq_layerProduct` at e.symm (u,g),
`apply_symm_apply`); `integral_fintype_prod_eq_prod` over `Measure.pi` of gaugeHaar; then
`integral_layerWeight` per factor. The outer integral is over `Measure.pi fun _ => sliceHaar R`, the
measure of `cyclic`.

**Q3: yes. The three statements are exactly steps 2, 3 and 4 of check 1507 Q3.**

## Q4. Hidden hypotheses; a = 0 and small a

`theorem Z_eq_cyclic (β : ℝ) (a : ℕ) (R : Box) : Z β a R = cyclic β R a`. No hypothesis: no sign of β,
no validity of R, no lower bound on a. The only instance arguments are those Mathlib derives for finite
products (Fintype, measurable spaces, probability and sigma-finiteness for Fubini), all unconditional
since each factor is the Haar probability `linkHaar`. Nothing in the proof needs a ≥ 1 (no `NeZero a`):
`finRotate a` and `Fin.consEquiv` are defined for every a.

- a = 0: `Site (sides 0 R)` is empty (time fibre `Fin 0`), so `Config` is one point, `haar` is the
  empty product (mass 1), action = 0, Z = 1. On the right, `Fin 0 → Slice R` is one point,
  `Measure.pi` over `Fin 0` has mass 1, the empty product is 1, so cyclic = 1. RECEIPT-1e's consumer
  proves `Z β 0 R = 1`. Correct as Lean objects.
- a = 1: `finRotate 1 = id`; the temporal word is g_0(x) u_0(x,i) g_0(x+e_i)^-1 u_0(x,i)^-1, the factor
  K(u_0, u_0). Both sides are the same Lean expression after reindexing. Correct.
- a = 2: `finRotate 2` swaps; the temporal plaquettes at t = 0 and t = 1 are distinct (site, plane)
  terms; factors K(u_0,u_1) K(u_1,u_0). Correct.
- Spatial sides 0, 1, 2: same remarks (`spatialStep` and `step` use the same `finRotate`); with a zero
  side both sides are 1. Consumers use only valid boxes and a ≥ 3 anyway.

**Q4: no hidden hypothesis; a = 0 and small a are correct; the theorem is stronger than the row asked
(row 1509 asked for a ≥ 3).**

## Q5. Faithfulness of torusData_of_trace

- *Hypothesis.* `trace : ∀ R, R.Valid → ∀ a, 3 ≤ a → cyclic β R a = ∑' i : PositiveSlot (transfer β R), i.1.val ^ a`,
  at the fixed β with `hβ : 0 < β`. Row 1508 is to prove this for β positive, valid R and a ≥ 3: the
  same statement. A row 1508 theorem `∀ β, 0 < β → ∀ R, R.Valid → ∀ a, 3 ≤ a → Trace.cyclic β R a = …`
  instantiates it at (β, hβ), provided `Trace.cyclic` and `Periodic.cyclic` are definitionally equal
  (Q1 caveat). A stronger row 1508 (a ≥ 2, or all R) also instantiates. The right side is literally the
  weight clause of `transfer_boxSpectrum` (Transfer.lean 757-761), the same ∑' over the same index type.
  It is not a junk-value equation: for a ≥ 3 the ∑' is summable (λ_i^a ≤ ‖T‖^(a-2) λ_i² with Σ λ_i²
  finite, inside `boxSpectrum_of_operator`), and cyclic > 0. Check 1507 Q4 proved it by hand.
- *Spectrum on valid boxes.* `spectrum β hβ R = (transfer_boxSpectrum β hβ R hR).choose` when R.Valid
  (`dif_pos`); `torusData_of_trace_spectrum` states this for the constructed TorusData. With
  `choose_spec` a consumer gets top = ‖transfer β R‖, an enumeration of the non-top positive slots with
  full multiplicity (`EnumeratesRatios`), and weight a = Σ λ^a for a ≥ 3.
- *bridge.* (spectrum R).weight a = ∑' λ^a (choose_spec) = cyclic β R a (trace) = Z β a R
  (`Z_eq_cyclic`): exactly the bridge hypothesis of `fields_of_bridge` (Wilson.lean 336-337), which
  row 1505 checked yields `cross` and `lower` with the TorusData types.
- *logConvex.* `weight_logConvex` (Periodic.lean 217-256) is byte-identical to the theorem in appendix A
  of row 1503 (`library/lean-gap-chain-stage1-check-opus.md`; `diff` of the two 40-line blocks is
  empty): for every BoxSpectrum B and a ≥ 3, B.weight (a+1)^2 ≤ B.weight a · B.weight (a+2). It is applied
  with the validity argument ignored, which is fine since it holds for every BoxSpectrum.
- *Invalid-box default.* On invalid R the spectrum is the cube-3 transfer spectrum at the same β. I read
  every use of `T.spectrum` in TheoremS.lean (`pair`, `pair_thermal`, `enlarge_side`, `cube_enlarge`,
  `seed`, `theoremS_step`, `dyadic_thermal`, `intermediate_thermal`, `seedRate`, `corollaryS3'`,
  `theoremS`, `log_space_double`, `phi`, `log_seed_le_phi`, `seed_of_phi`). The TorusData fields
  quantify only over valid R and `R.replace i b` with b ≥ 3, which is valid. Every theorem evaluates
  the spectrum at `R.replace i b` (R valid, b ≥ 3), at `cube m` with m ≥ 3 (cube n, cube (2n),
  cube (4n), cube L with L ≥ 2N ≥ 6, cube (2·2^k N)), or at the intermediate boxes ⟨L,b,b⟩, ⟨L,L,b⟩
  with L, b ≥ 6. All valid. The total definitions `seed n`, `seedRate n`, `phi n` would read the
  default at n < 3 only for `phi` and at n ≤ 1 for `seed`, but every theorem carries 3 ≤ n. So the
  default never enters a hypothesis or conclusion of a theorem in TheoremS.lean. Harmless; and being
  a genuine Wilson spectrum, it would give real data to a future consumer that forgot validity.

**Q5: faithful.**

## Q6. Vacuity

- The TorusData from `torusData_of_trace` has the transfer operator's own spectrum on valid boxes;
  `cross` and `lower` follow from Z; `logConvex` is automatic. `spectrum` is not a free parameter that
  could be chosen to make the seed small.
- `T.seed N = (T.spectrum (cube 2N)).thermal N` is then Σ over the non-top positive slots of
  (λ_i/‖T‖)^N = Z β N (cube 2N)/‖T‖^N - 1, a Wilson quantity; `gap` is inf over the non-top positive
  slots of log(‖T‖/λ_i), the gap of -log(T/‖T‖) above the chosen top slot (0 if the top eigenvalue is
  degenerate, in which case seed ≥ 1 and Theorem S does not apply). Both are independent of `.choose`:
  the multiset of ratios is fixed by T once one top slot is removed, and all top slots carry the same
  value. So the choice of witness cannot weaken Theorem S's conclusion.
- The only conditional input is `trace`. If it were false the construction would be vacuous; it is the
  content of row 1508 and true by hand (check 1507 Q4). Applied to this TorusData, Theorem S says: if
  the Wilson seed at (β, N) is below 1/5041, the transfer gap on every cube of side ≥ 2N is at least
  log(1/(5041 seed))/N. That is the intended statement. The link from the 4D torus to the transfer
  spectrum is now a Lean theorem (`Z_eq_cyclic` plus `trace`), not an assumption on a free family.
- In the other direction, check 1503's toy already showed TorusData consistent.

**Q6: nothing vacuous or trivially satisfiable.**

## Verdict

**FAITHFUL.** No change to row 1509's Lean statements or definitions is needed.

1. `cyclic` is symbol for symbol the definition fixed in check 1507 Q3 for rows 1508-1509.
2. site, linkIndex, layers and measurePreserving_layers put time in coordinate 0, make the temporal link
   of (t,x) the gauge at x for layer t, and use finRotate in the same direction as `cyclic`
   (`timeStep`; the link correspondence is closed by `rfl` inside `action_eq_layers`).
3. action_eq_layers, density_eq_layerProduct and integral_layerWeight state check 1507 Q3 steps 2, 3 and
   4 exactly: gauge on the later slice, kernel order K(u t, u (t+1)).
4. Z_eq_cyclic has no hypothesis; a = 0 (both sides 1), a = 1, 2 and degenerate spatial sides are correct
   as Lean objects. Stronger than asked.
5. torusData_of_trace: its hypothesis is row 1508's statement at fixed positive β; the valid-box spectrum
   is the `transfer_boxSpectrum` witness (`torusData_of_trace_spectrum`); the invalid-box default never
   reaches a theorem of TheoremS.lean; `weight_logConvex` is byte-identical to row 1503's.
6. Nothing vacuous; seed and gap are the transfer quantities and do not depend on `.choose`.

Remarks, not changes:

- (R1) The join with the real row 1508 module is not in the repository. RECEIPT-1e's consumer (re-typed
  interface, `rfl`) is in the author's /tmp, and `Trace.lean` is not in this checkout, so I could not
  compare its `cyclic` body. The join row (RECEIPT-1e next row 1) should import both modules and prove
  `Trace.cyclic = Periodic.cyclic` by `rfl`, or better, keep one `cyclic` in a module both import.
- (R2) I did not build. The lead's replay supplies the kernel check and the axiom print. I read the
  proofs for what they prove and for the soundness of each step, not tactic by tactic.

Prior work: `grep -i "Z_eq_cyclic|torusData_of_trace|periodic haar"` in library/open-core.md has no
match; the identity is FINISH rows 1507 (by hand) and 1509 (Lean). Nothing here is claimed new.

Credit: Lean Stage 1e by gpt-6.2-astra (row 1509), on Stages 1-1c (rows 1459, 1504, 1506, same author);
hand construction rows 667 and 698 and check 1507 (Claude Opus 5.5); weight_logConvex from row 1503
(Claude Opus 5.5); Wilson and transfer conventions from Ethan Sussman and Levent Alpoge, with Claude
and Codex (outline GL8 and CA-I §1.1 at 31a47c543775, as cited by RECEIPT-1e; not re-read here).

No numeric job and no build were run, so the numeric lock and memory floor did not apply.

Done 2026-11-25T05:27Z (date -u).
