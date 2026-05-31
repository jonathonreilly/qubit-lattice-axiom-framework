# Handoff

This draft PR is for workers on the `Q = 2/3` Koide hunt.

What to use:

- The `Q=1` source matrix is exact and exposes offsite `-2/9`.
- Strict onsite descent erases the reduced `Z` coordinate and returns
  effective `Q=2/3`.
- The repeated `2/9` footprint is real as `2/d^2` arithmetic.
- APS eta is exact at the forced `d=3` surface.
- The bridge `coeff_nonid(S_Q1) = -eta_APS` is now exact.
- Q1-alone signed readout is no-go: the source is transposition-even, while
  `delta` is transposition-odd.
- The unlock map splits the positive targets cleanly: strict onsite
  source-domain selection gives charged-lepton `Q=2/3`, while the Q1 offsite
  source shadow gives APS/Brannen magnitude `2/9`.
- If a future odd orientation/basepoint primitive supplies
  `epsilon in {+1,-1}`, then `delta = epsilon * eta_APS` can feed the existing
  selected-line scalar/point bridge.
- The bottom-up sign audit confirms Q1 generates only `span{e,g+g^2}` and has
  zero projection onto the signed phase line `i(g-g^2)`.
- The gamma sheet sign probe prunes the next tempting source-oriented route:
  `gamma -> -gamma` complex-conjugates the carrier but leaves the real
  diagonal-slot selected-line readout, branch endpoints, and `+2/9` point
  unchanged.
- This does not prove the sign is wrong.  The current oriented selected-line
  frame still gives `delta=+2/9`; the sign remains underived from Q1/gamma,
  not contradicted.
- The oriented-sign compatibility closeout records the positive conditional
  result: in an oriented C3 frame, `delta_oriented=-coeff_g(S_Q1)=+2/9`.
  The sign is right once the frame is admitted; the frame itself remains the
  missing physical theorem.
- The last-mile unlock cascade splits the final premises:
  `P_ORIENT` gives `delta=+2/9`, `P_SOURCE` gives `Q=2/3`, and both together
  make Koide Q/delta dimensionless closure audit-ready.  This still does not
  imply generation-label retention, absolute masses, Q1 dark matter, or Y_T
  unbounded closure.
- The physical orientation/basepoint probe narrows `P_ORIENT`: the oriented
  generator `g` is the proper spatial `C3[111]` rotation and the full taste-cube
  descent image on `T1`.  Thus the orientation carrier is bounded support, not
  a free convention.  Full `P_ORIENT` still needs the microscopic full-cube
  source law and selected-line endpoint/basepoint/readout.
- The source-endpoint / record-measure no-go kills the `S=C+C^2` shortcut:
  the sharp record forces two atoms with ranks `(1,2)`, but not the
  count-vs-rank measure; it is reflection-even and cannot select `Qf` over
  `Qb`; and the unbased endpoint orbit has no canonical first element.
- The record-quotient measure fork isolates the exact measure bridge:
  full Hilbert trace/Born push-forward through the embedded `S` record gives
  weights `(1/3,2/3)` and `Q=1`; rank-erased quotient record counting gives
  weights `(1/2,1/2)` and conditional `Q=2/3`.
- Existing source-measure / record-intervention notes justify probability laws
  on the finite record algebra, but they keep the reference law as an input.
  They do not select quotient count over Hilbert rank.

What not to use:

- Do not cite this as dark matter.
- Do not cite this as retained `Q=2/3` closure.
- Do not cite this as `delta = eta_APS`.
- Do not cite Q1 as fixing the sign of `delta`.
- Do not cite the source-oriented `gamma` sheet as fixing the sign of `delta`.
- Do not cite the named C3 generator convention as a physical sign theorem.
- Do not cite the oriented-frame compatibility as a physical orientation
  derivation.
- Do not cite the physical orientation/basepoint probe as full `P_ORIENT`
  closure; it only lands the spatial/taste `g` carrier.
- Do not cite the `S=C+C^2` record as selecting `Q=2/3`, the forward channel,
  or a selected-line endpoint; it only supplies the two-atom carrier.
- Do not cite source-measure / record-intervention machinery as selecting the
  quotient record reference law.  It legitimizes the probability-law surface;
  it does not erase Hilbert rank.
- Do not cite the last-mile cascade as effective retained status without an
  independent audit of `P_ORIENT` and `P_SOURCE`.
- Do not merge the APS, anomaly, Brannen, and offsite matrix coefficient into
  full physical phase closure without a signed selected-line readout theorem.

Best next theorem handles:

```text
derive_orientation_odd_full_cube_source_boundary_law_selects_Qf_and_endpoint
derive_physical_rank_erasing_record_quotient_or_count_on_record_atoms
derive_P_SOURCE_strict_onsite_charged_lepton_source_domain
```
