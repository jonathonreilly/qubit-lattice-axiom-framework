# Axiom-First Single-Clock Codimension-1 Unitary Evolution on the One-Qubit Cl(3) Pauli Factor over Z^3

**Date:** 2026-05-03 (hostile science-fix re-scope 2026-06-11;
finite-range premise narrowing 2026-06-11 #2; Cl(3) complexification
wording hygiene + B-RANGE supplier wiring 2026-06-11 #3;
free-quasilocal propagation repair 2026-06-12; B-AXIS.1 blocked-time
unit split 2026-06-17; see §0)
**Type:** bounded_theorem
**Claim scope:** **Axis-conditional single-clock codimension-1 unitary
evolution.** Given the declared evolution-axis premise (B-AXIS) below
and the supplied transfer data of the retained_bounded
reflection-positivity and spectrum-condition rows — the positive
Hermitian two-step blocked transfer `T̂²` with blocked time-step
`2 a_τ` on the staggered fixed-background surface — the framework's
lattice dynamics is a single-clock codimension-1 unitary evolution:
(S1′) the generator `H := -(1/(2a_τ)) log(T̂²/M_T)` is the **unique**
self-adjoint generator (retained finite-dim Stone uniqueness,
transfer-relative and τ-relative) of the unique strongly continuous
one-parameter unitary group `U(t) = exp(-itH)` on the finite block
Hilbert space; (S2′) each lattice time slice `Σ_t = {t} × Z^3` is a
codimension-1 Cauchy surface: the equal-time local algebra is the
mutually commuting tensor product of per-site one-qubit `M_2(C)` Pauli
factors selected from the retained complexification split
`Cl(3,0) ⊗ C ≅ M_2(C) ⊕ M_2(C)`, with the physical carrier one
summand, and slice data propagates with the
finite quasilocal Lieb-Robinson envelope of the retained_bounded
free-bilinear exact-log bridge on the free `U = 1` bilinear sector; no
finite-range or interacting/fixed-background exact-log locality is
claimed outside that sector; (S3′) **the axis
is a premise, not a derivation**: the
staggered-Dirac hop operator is *exactly* invariant under the
time-space exchange unitary `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})`
(computed certificate, residual `0`), so RP-admissibility cannot
single out the temporal direction, and the prior revision's S3 claim
("the temporal direction is the unique RP-admissible reflection axis;
hence no second clock") is **withdrawn** as false-as-written. The
"exactly one clock" conclusion holds conditional on (B-AXIS) — one
declared axis/transfer construction (N4), one supplied `τ` (N2), and
no independent commuting clock factor (N5), per the retained
single-clock uniqueness scope boundary. The continuum-limit
identification with a Wightman one-parameter group remains bounded by
the emergent-Lorentz program's `retained_bounded` free-sector scope.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; audit verdict and effective
status are set only by the independent audit lane.
**Loop:** `3plus1d-native-closure-2026-05-02` (original);
science-fix lane 2026-06-11 (re-scope)
**Runner:** [`scripts/axiom_first_single_clock_codimension1_evolution_check.py`](../scripts/axiom_first_single_clock_codimension1_evolution_check.py)
(`TOTAL: PASS=47 FAIL=0`, deterministic, runtime well under one minute)
**Authority role:** source-note proposal. If retained, this row
supplies the *axis-conditional* single-clock codimension-1 clauses
(S1′)+(S2′) cited by `ANOMALY_FORCES_TIME_THEOREM.md` (its SC premise
row), with the axis-selection content explicitly declared as (B-AXIS)
rather than derived.

## 0. Changelog

- **2026-06-11 #3 (supplier wiring + wording repair; historical after
  the 2026-06-12 B-RANGE retirement below).** Two items from the
  2026-06-11 re-audit: (i) the inline claim-scope wording
  `M_2(C) ≅ Cl(3,0) ⊗ C` is corrected to match the cited per-site
  row's complexification split (`Cl(3,0) ⊗ C ≅ M_2(C) ⊕ M_2(C)`,
  physical carrier one summand); (ii) the (B-RANGE) candidate class
  theorem named in the not-in-scope list has landed as a source note
  and is wired as a one-hop edge in the Inputs section, registering the
  supplier route for the audit chain. At that revision, (B-RANGE)
  remained a declared premise; the 2026-06-12 repair below narrows the
  current propagation clause to the retained_bounded free-bilinear
  quasilocal supplier and retires (B-RANGE) from current scope. The
  (B-AXIS) supplier remains future work (Record-direction or
  boundary-condition selection row).
- **2026-05-03.** Original version: (S1) Stone evolution, (S2)
  codimension-1 Cauchy slices, (S3) "the temporal direction is the
  unique RP-admissible reflection axis, hence exactly one clock",
  proposed as positive_theorem on A_min (A1–A4 carrier).
- **2026-05-05 audit (archived).** `audited_conditional`,
  chain_closes=false: every one-hop input was unaudited or
  conditional; the A_min carrier's A3/A4 were recategorised as open
  gates. The S1/S2/S3 algebra was ratified as internally coherent
  *as a conditional step* only.
- **2026-05-09.** Upstream-status bookkeeping note added (now
  superseded by this changelog; the cited statuses have since moved).
- **2026-06-11 (hostile science-fix re-scope; the load-bearing
  change).** Three defects repaired:
  1. **S3 withdrawn (critical defect — false as written).** The old
     Step 4 tested only the *unconjugated* temporal RP template
     against spatial reflections: it fixed the time-first staggered
     phase convention `η_τ = 1, η_1 = (-1)^{x_τ}, …` and observed
     that the temporal-hop phase does not flip under `θ_1`. That
     argument quantified over one factorisation template, not over RP
     constructions. In fact the staggered hop operator is *exactly*
     invariant under the axis-exchange unitary
     `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})` (runner block [C-EX],
     residual `0` on a `4×4×2×2` even periodic block, temporal hop
     sector mapped exactly onto the spatial hop sector), so any RP /
     transfer construction about the `τ` axis conjugates by `W` into
     the identical construction about the `x_1` axis. The conclusion
     "no spatial reflection is RP, hence no second clock" therefore
     does not follow — and the broad no-second-clock inference is
     independently denied by the retained
     `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
     (retained_no_go: Stone uniqueness is transfer-relative and
     τ-relative; N2/N4/N5 are extra premises). The old runner's
     T8/T9 were tautologies over the convention labels (`-1 == -1`,
     `+1 != -1`) and its T10 tested a sign-flip criterion that is
     neither necessary nor sufficient for RP; all three are removed.
     S3 is replaced by (S3′): the computed exchange-symmetry
     certificate plus the declared axis premise (B-AXIS).
  2. **S1/S2 re-based on the current retained-grade suppliers.** The
     inline Stone re-proof is replaced by a citation to the retained
     `SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
     (N1–N4); the transfer supply is the retained_bounded RP row's
     two-step blocked `T̂²` (staggered-only, fixed background,
     factorized `A_+^(2)` observables) with the retained_bounded
     spectrum-condition normalization `H = -(1/(2a_τ)) log(T̂²/M_T)`;
     equal-time tensor locality is re-cited from the audited_conditional
     microcausality note to the retained_bounded
     `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`;
     at this revision the finite-speed clause used the retained_bounded
     cluster row's L1/L3 only. The 2026-06-12 repair below supersedes
     that current-scope supplier with the free-bilinear quasilocal
     bridge. The old S2(b) spatial-clustering clause is demoted to a
     conditional remark (the cluster row's L2 is conditional on a
     transfer-gap bridge and unconditional spatial clustering is
     explicitly excluded there).
  3. **Claim type bounded, premise declared.** positive_theorem was
     an over-claim: the transfer supply is retained_bounded (2-step,
     staggered-only, fixed background), the clustering clause is
     conditional, and the axis selection is a premise. The note is
     now bounded_theorem with (B-AXIS) declared. The runner is
     rebuilt to compute the load-bearing content with falsification
     legs: the exchange intertwiner (exact, with a no-sign-field
     falsifier), a two-clock tensor-factor comparator whose generator
     span is genuinely 2-dimensional (making the single-clock
     constraint non-vacuous), τ-rescaling (N2 is real), a
     non-Hermitian transfer falsifier, and computed Lieb-Robinson
     cone residuals against the cluster row's bound.
- **2026-06-11 #2 (science-fix, finite-range premise narrowing).** The
  2026-06-11 conditional audit identified a missing one-hop bridge in
  S2′(c): the (R-CD) L1/L3 Lieb-Robinson authority applies to
  finite-range Hermitian finite-block Hamiltonians, while
  (R-RP2)/(R-SC2) supply a positive transfer and its logarithmic
  generator `H = -(1/(2a_τ)) log(T̂²/M_T)` with no proof that this
  `H` is finite-range. Finite-range-ness is in fact not automatic:
  the logarithm of a product of strictly local positive factors
  generically carries Baker-Campbell-Hausdorff commutator tails of
  larger support (runner block [C-RANGE] exhibits a strictly local
  3-site transfer whose log-generator has a computed nonzero
  end-to-end Pauli component). Per the audit's offered narrowing
  route, S2′(c) is now stated **conditional on the explicit declared
  premise (B-RANGE)**: the dynamics consumed by the propagation
  clause is generated by a finite-range Hermitian finite-block
  Hamiltonian. At that historical revision, (B-RANGE) joined
  (B-AXIS) in the premise list with a computed non-vacuity witness;
  deriving it (a quasi-locality bridge
  for log-transfer generators, or an exponentially-decaying-
  interaction Lieb-Robinson authority consumed in place of (R-CD)
  L1/L3) is named future work, not claimed here. (S1′), (S2′a,b),
  and (S3′) are unchanged.
- **2026-06-11 #3 (source hygiene, Cl(3) complexification wording).**
  The headline and S2′ summary no longer write the full complexified
  algebra as a single `M_2(C)`. They now match the retained
  classification used below: `Cl(3,0) ⊗ C ≅ M_2(C) ⊕ M_2(C)`, with this
  note consuming one per-site one-qubit `M_2(C)` Pauli factor. This is
  wording synchronization only; it does not discharge the declared
  premise (B-AXIS).
- **2026-06-12 (B-RANGE retired by narrowing the propagation clause to
  a retained supplier).** The current claim no longer declares
  (B-RANGE). Instead, S2′(c) is narrowed to the free `U = 1` bilinear
  exact-log sector and cites the retained_bounded
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md),
  which proves a finite-velocity quasilocal Lieb-Robinson envelope for
  `H = -log(T_hat^2)/(2 a_tau)` when `0 < d mu < eta < arcsinh(m)`.
  The older (B-RANGE) finite-range premise remains only historical
  boundary text: it is still false that a strictly local transfer has a
  finite-range logarithm in general, and this note still makes no
  interacting or fixed-background exact-log locality claim. The only
  current declared premise left in the statement is (B-AXIS).
- **2026-06-15 (source-graph cycle repair, no status change).** The
  remaining-blocker paragraph below now describes the later
  record-durability axis-selection route-pruning result without naming
  its exact source filename. This theorem does not consume that later
  no-go as an input; it leaves B-AXIS open. Avoiding the filename token
  keeps the audit citation graph from treating the forward
  cross-reference as a load-bearing edge back to the follow-up note.
- **2026-06-16 (APBC axis-label bridge wiring, no status change).** The
  companion
  [`SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)
  now packages the sharpened-pin positive theorem: given a supplied
  per-axis boundary-condition datum `APBC` on one axis and `PBC` on the
  other three, the APBC axis is invariantly selected. This source note
  cites that bridge only as a conditional supplier for the axis-label
  component of (B-AXIS.2). It does not derive the APBC/PBC datum, the
  blocked time step, the transfer construction, or the no-second-clock
  clause, and it does not change this row's status authority.
- **2026-06-17 (B-AXIS.1 unit split, no status promotion).** A new
  source-support note separates the N2 blocked-time phrase into two
  parts. The internal denominator of the supplied two-step transfer is
  now source-supported: for the imported `T_hat^2` object the aligned
  reconstruction uses `1/(2a_tau)`, and the `1/a_tau` denominator would
  double the generator. The absolute physical clock unit represented
  by `a_tau` is still not derived from Lattice, Quantum, Record, or
  post-record counts alone. This does not close axis/transfer
  construction uniqueness (B-AXIS.2), does not exclude independent
  commuting transfer factors (B-AXIS.3), and does not make this row a
  retained-grade proposal.

## Scope

`ANOMALY_FORCES_TIME_THEOREM.md` imports its upper bound `d_t ≤ 1`
from this note (its premise row SC). After this re-scope the supplied
content is: **conditional on (B-AXIS), exactly one generator and one
codimension-1 Cauchy slice structure** — i.e. `d_t ≤ 1` holds *given*
that the framework supplies one evolution axis with one transfer
construction and one time step, and admits no independent commuting
clock factor. The free `U = 1` bilinear exact-log sector additionally
has finite quasilocal propagation by the retained_bounded free-bilinear
bridge; propagation beyond that sector is not supplied here. The axis
premise is anomaly-free (it references no anomaly trace, no chirality
content), so the consumer's
non-circularity argument survives in premise-supplied form; what no
longer exists is a derivation of the axis from reflection positivity
alone. The consumer's SC row wording ("the temporal direction is the
unique RP-admissible reflection axis") is stale against this revision
and needs a follow-up edit there.

## Framework objects in use

Current baseline carrier:
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
(Lattice supplies the `Z^3` carrier; Quantum supplies the one-qubit
local algebra per site; Record is not load-bearing here).

- **Per-site algebra.** Each site `x ∈ Z^3` carries the one-qubit
  algebra `M_2(C)`; the retained
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
  identifies `Cl(3,0) ⊗ C ≅ M_2(C) ⊕ M_2(C)` with the two factors
  exchanged by the central element, so the per-site operator content
  is the Pauli realization of the complexified Cl(3).
- **Spatial substrate.** `Z^3` with the cubic graph metric `d(x,y)`,
  used for slices `Σ_t` and for the Lieb-Robinson distance.
- **Euclidean block (supplied surface, not an axiom).** The staggered
  Dirac + Wilson surface `Λ = (Z/L_τ Z) × (Z/L_s Z)^3` enters only
  through the retained_bounded RP/SC supplier rows; its status as a
  gate (not an axiom) is inherited from those rows. No A3/A4 axiom
  status is asserted (the 2026-05-05 audit flagged that carrier as
  superseded; this revision complies).

No fitted parameters. No observed values used as proof inputs.

## Inputs (one hop, with exact licenses)

- **(R-STONE)** — retained positive_theorem
  [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md):
  given finite-dim positive Hermitian `T` with trivial kernel and a
  fixed `τ > 0`, `H_gen = -(1/τ) log(T)` is unique, `U(t) =
  exp(-itH_gen)` is the unique strongly continuous one-parameter
  unitary group with that generator, and `T^n = U(-inτ)` (N1–N4).
- **(R-RP2)** — retained_bounded
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md):
  bounded finite **2-step staggered-only** RP reduction for factorized
  `A_+^(2)` observables on the fixed-background surface; supplies the
  positive Hermitian blocked transfer `T̂²`.
- **(R-SC2)** — retained_bounded
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md):
  with `spec(T̂²) ⊂ (0, M_T]`, functional calculus gives
  `H := -(1/(2a_τ)) log(T̂²/M_T)` self-adjoint with `H ≥ 0`
  (SC1–SC2 after blocked-time normalization; SC3/SC4 conditional
  clauses not consumed here).
- **(S-N2-SPLIT)** — exact-support/no-go source boundary
  [`SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md):
  separates (B-AXIS.1)'s two meanings. The internal blocked-transfer
  denominator for the supplied `T_hat^2` object is fixed by the
  retained-bounded two-step normalization bridge to `2a_tau`; the
  absolute physical clock unit or time metric represented by `a_tau`
  is not derived from the current framework axioms or Record-count
  layer. This source boundary does not close (B-AXIS.2) or (B-AXIS.3)
  and does not set an audit verdict.
- **(R-ET)** — retained_bounded
  [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md):
  raw equal-time commutation and tensor factorization for
  finite-dim tensor factors at distinct sites (dynamics excluded
  there; the free-sector propagation statement below is supplied by
  R-FBQL).
- **(R-FBQL)** — retained_bounded
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md):
  on the free `U = 1` bilinear staggered two-step sector, the exact
  reconstructed Hamiltonian `H = -log(T_hat^2)/(2 a_tau)` has a finite
  weighted overlap and obeys the quasilocal Lieb-Robinson envelope
  `||[alpha_t(A_x), B_y]|| <= 2 ||A_x|| ||B_y||
  exp(-mu d_1(x,y) + 4 W_mu |t|)` whenever
  `0 < d mu < eta < arcsinh(m)`. The row explicitly excludes strict
  finite-range, `m = 0`, gauged/interacting log-transfer locality, and
  full continuum microcausality.
- **(R-CL3)** — retained positive_theorem
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md):
  the per-site complexified Cl(3) algebra classification (2-dim
  irreducible Pauli factors).
- **(G-SCOPE)** — retained_no_go
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md):
  governing boundary. Stone uniqueness is transfer-relative and
  τ-relative; a no-second-clock claim must separately supply N2
  (the time step), N4 (axis/transfer-construction uniqueness), and
  N5 (exclusion of independent commuting transfer factors). This
  note **complies** by declaring those clauses as (B-AXIS) instead
  of deriving them.
- **(B-AXIS)** — **declared premise of this bounded theorem** (not
  derived, not an axiom):
  - (B-AXIS.1) one supplied blocked time step `2a_τ` (= N2), now split
    by (S-N2-SPLIT): the internal denominator `2a_tau` for the supplied
    `T_hat^2` transfer is source-supported, while the absolute
    physical clock unit/time metric represented by `a_tau` remains a
    supplied/open clock-rate boundary;
  - (B-AXIS.2) one declared evolution axis carrying one RP/transfer
    construction, namely the `(T̂², 2a_τ)` supply of (R-RP2)/(R-SC2)
    (= N4);
  - (B-AXIS.3) no independent commuting transfer factor is admitted
    as a second physical clock (= N5).
- **(B-AXIS-APBC)** — conditional supplier for the axis-label part of
  (B-AXIS.2) only:
  [`SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)
  proves that, given a supplied APBC-on-axis/PBC-on-others boundary datum,
  the APBC axis is the selected axis label. This does not supply the
  datum itself, the blocked time step, the transfer construction, or
  (B-AXIS.3). B-AXIS remains live unless the APBC/PBC datum is itself
  supplied by the row consuming this theorem or by a later retained
  supplier.

  Source-side N5 support is now isolated in
  [`SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md`](SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17.md):
  on the current single-clock source packet, the admitted physical-clock
  inventory contains exactly the supplied `(T̂², 2a_τ)` transfer/step pair.
  This supports the admission wording of (B-AXIS.3) only. It does not derive
  (B-AXIS.1), does not select the axis/transfer construction in (B-AXIS.2),
  and does not mathematically exclude arbitrary commuting positive factor
  transfers.

The older declared finite-range generator premise `(B-RANGE)` is no
longer a current premise of this theorem. It was replaced by the
retained_bounded R-FBQL supplier on the narrower free bilinear exact-log
surface; outside that surface, propagation remains open rather than
declared.

The intermediate 2026-06-11 supplier route remains useful context:
`EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11.md`
gives the quasilocal class theorem once a finite weighted norm is
supplied, and
`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`
supplies the free-bilinear exact-log membership. The composed
free-bilinear LR bridge (R-FBQL) is the current one-hop propagation
supplier consumed here; it does not prove gauged/interacting
membership.

## 2026-06-12 Remaining-Blocker Source Firewall

This repair separates the already-retired propagation premise from the
still-live axis-selection premise:

- **B-RANGE is not a current blocker.** The current claim no longer
  asks the auditor to grant finite range for a generic log-transfer
  generator. S2'(c) is sourced only by the retained_bounded free
  bilinear exact-log/quasilocal bridge (R-FBQL) on its own `U = 1`,
  massive-sector surface. Interacting or fixed-background exact-log
  propagation remains open, but it is not part of this row's current
  theorem statement.
- **B-AXIS remains a real declared premise.** The framework has not
  derived the registration direction, the absolute physical clock
  unit/time metric, or the exclusion of independent commuting transfer
  factors from the current retained axiom surface. The internal
  two-step denominator for `T_hat^2` is separately supported by
  (S-N2-SPLIT); this does not make a physical clock/rate unit follow
  from Record or from the transfer spectrum alone. The follow-up source note
  `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
  narrows the route: Record durability, anomaly/chirality labels, and
  the native exchange-symmetric staggered surface transport with the
  axis and therefore do not derive B-AXIS. A future positive supplier
  must provide a non-transportable registration-direction theorem or a
  reviewed boundary-condition asymmetry bridge; this note does not add
  such a premise and does not treat it as an axiom.
- **APBC/PBC narrows the axis-label supplier shape but does not close
  B-AXIS by itself.** The 2026-06-16 APBC bridge proves the axis-label
  consequence if the per-axis boundary-condition datum is supplied. It
  does not derive that datum and does not touch (B-AXIS.1) or
  (B-AXIS.3), so this theorem remains axis-conditional on the live
  premise surface.

Source-surface summary: this is bounded support only. The repair prunes the
old B-RANGE route from the current scope and leaves B-AXIS as the live
declared blocker. No retained-grade proposal or status promotion is made here;
the independent audit lane remains the only authority for effective status.
Equivalently, B-AXIS as the live axis premise remains after the
record-durability axis selection route-pruning context: those routes do not
derive B-AXIS.

## Statement

Let `H_blk` be the finite block Hilbert space of the (R-RP2)
reconstruction and `T̂² : H_blk → H_blk` the supplied positive
Hermitian two-step transfer with `spec(T̂²) ⊂ (0, M_T]`. Fix the
source-supported internal blocked denominator `2a_τ` for this supplied
two-step object (B-AXIS.1a by S-N2-SPLIT), while leaving the absolute
physical clock unit represented by `a_tau` as a supplied/open boundary
(B-AXIS.1b), and define
`H := -(1/(2a_τ)) log(T̂²/M_T)` per (R-SC2). Then, **conditional on
(B-AXIS)**:

**(S1′) Single-clock unitary evolution (transfer- and τ-relative).**
By (R-STONE) applied to `(T̂²/M_T, 2a_τ)`: `H` is the unique
self-adjoint generator determined by the supplied transfer data,
`U(t) := exp(-itH)` is the unique strongly continuous one-parameter
unitary group with generator `H`, and the discrete iteration is
consistent at imaginary argument, `(T̂²/M_T)^n = U(-i n · 2a_τ)`.
`H ≥ 0` by (R-SC2). Uniqueness is exactly the (R-STONE) N1/N3
uniqueness: **relative to the supplied `(T̂², 2a_τ)`**. The same
`T̂²` with a different declared `τ` gives a rescaled generator
(G-SCOPE); that is why the absolute physical clock unit in
(B-AXIS.1b) remains supplied/open even though the internal denominator
of the imported two-step object is fixed to `2a_tau`.

**(S2′) Codimension-1 Cauchy slice structure.** Each lattice slice
`Σ_t = {t} × Z^3` (finite block: `{t} × (Z/L_s Z)^3`) carries:

- (a) the mutually commuting equal-time local algebra
  `A(Σ_t) = ⊗_{x ∈ Σ_t} M_2(C)_x` — raw tensor-factor commutation
  and factorization by (R-ET), per-site factor content by (R-CL3)
  on the Quantum-axiom one-qubit carrier;
- (b) codimension 1: `dim(Σ_t) = 3 = dim(Λ) - 1`;
- (c) free-sector finite-speed propagation: on the free `U = 1`
  bilinear exact-log sector, the same reconstructed Hamiltonian
  `H = -log(T_hat^2)/(2 a_tau)` obeys the R-FBQL quasilocal
  Lieb-Robinson envelope
  `‖[α_t(A_x), B_y]‖ ≤ 2‖A_x‖‖B_y‖
  exp(-μ d_1(x,y) + 4 W_μ |t|)` whenever
  `0 < d μ < η < arcsinh(m)`, hence a finite lattice lightcone speed
  `v_μ = 4 W_μ/μ`. This replaces the older broad finite-range premise:
  strict finite-range of the exact-log generator, gauged/interacting
  exact-log locality, and the `m = 0` gapless boundary are not claimed.

*Conditional remark (not part of the claim):* spatial factorization
of connected expectations on `Σ_t` (the old S2(b)) remains outside
this theorem. The free-sector quasilocal envelope gives a finite
propagation cone, not a general transfer-gap or clustering theorem.

**(S3′) Axis selection is a premise; exchange-symmetry certificate.**
The staggered-Dirac hop operator on an even periodic block, in the
time-first Kogut-Susskind convention
`η_τ = 1, η_1 = (-1)^{x_τ}, η_2 = (-1)^{x_τ+x_1},
η_3 = (-1)^{x_τ+x_1+x_2}`, satisfies **exactly**

```text
    W M_KS W^T = M_KS ,   W := P_{τ↔1} ∘ diag( (-1)^{x_τ x_1} ) ,      (1)
```

with `W` orthogonal, where `P_{τ↔1}` relabels `(t, x_1, x_2, x_3) ↦
(x_1, t, x_2, x_3)`. Moreover `W` maps the temporal hop sector
exactly onto the `x_1` hop sector and vice versa,

```text
    W M_τ-hop W^T = M_1-hop ,   W M_1-hop W^T = M_τ-hop ,              (2)
```

and fixes the transverse sectors. (Runner block [C-EX]: residuals are
exactly `0`; the plain permutation without the sign field fails by a
nonzero margin, so the identity is non-trivial.) Consequently the
staggered phase structure does **not** distinguish the temporal axis:
any reflection/transfer construction about the `τ` axis conjugates by
the unitary `W` into the identical construction about the `x_1` axis
(half-spaces, reflection planes, and hop sectors all map onto each
other under `W`). The framework direction is the same: the approved
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
premise sets `c_t = c_s`, which makes the surface *more*
exchange-symmetric, not less. Therefore the single-clock conclusion
cannot be derived from RP-admissibility of the action; it holds
conditional on (B-AXIS), exactly as the retained (G-SCOPE) boundary
requires. A two-clock comparator exists mathematically (two commuting
tensor-factor transfers with a 2-dimensional generator span; runner
block [C-2CLK]) and is excluded only by (B-AXIS.3) — the premise
excludes something realizable, so it is non-vacuous and load-bearing.

Statements (S1′)–(S3′), conditional on (B-AXIS), constitute the
framework's **axis-conditional single-clock codimension-1 unitary
evolution theorem**.

## Derivation

**Step 1 (S1′).** (R-RP2) supplies `T̂²` positive Hermitian on the
finite-dim `H_blk`; (R-SC2) supplies the normalization
`T := T̂²/M_T` with `spec(T) ⊂ (0, 1]` and trivial kernel. The
hypotheses of (R-STONE) — finite-dim, Hermitian, positive, trivial
kernel, `‖T‖_op ≤ 1`, fixed `τ = 2a_τ` — are met, so its N1–N4 apply
verbatim: unique `H`, unique group `U(t)`, consistency
`T^n = U(-inτ)`. `H ≥ 0` is (R-SC2) SC2. No content beyond the two
cited rows plus functional calculus is used. ∎

**Step 2 (S2′).** (a) is (R-ET)'s raw tensor-factor commutation and
factorization applied to the per-site factors, whose algebra content
is fixed by (R-CL3) on the one-qubit carrier. (b) is arithmetic.
(c) is now R-FBQL, not a declared finite-range premise: on the free
`U = 1` bilinear exact-log sector, R-FBQL has already proved the
finite weighted overlap `W_mu < infinity` and the weighted-path
Lieb-Robinson envelope with speed `v_mu = 4 W_mu/mu`. This theorem
imports that retained_bounded propagation clause only on its stated
sector. The old finite-range step remains false in general: the runner
keeps a boundary witness showing that a strictly local positive
transfer can have a non-range-1 logarithm, so the current statement
does not upgrade R-FBQL to interacting/fixed-background locality. ∎

**Step 3 (S3′).** Equation (1) is verified exactly: for the
transposition `τ↔1`, the sign field `ε(x) = (-1)^{x_τ x_1}`
intertwines the KS phases,

```text
    η_{Pν}(Px) · ε(x) · ε(x + ν̂)  =  η_ν(x)     for all sites x, ν,    (3)
```

(case check: `ν = τ`: `(-1)^{x_1} · (-1)^{x_1} = 1 = η_τ`;
`ν = 1`: `1 · (-1)^{x_τ} = η_1`; `ν = 2, 3`: `ε` cancels and the
relabelled phase reproduces `η_ν`), so the substitution
`χ_x → ε(x) χ_{Px}` maps the staggered action to itself; the mass
term is `ε²`-invariant and the Wilson plaquette is hypercubic
invariant. Hence any RP factorisation `⟨Θ_τ(F) F⟩ ≥ 0` over the
`τ ≥ 0` half-space algebra conjugates to
`⟨Θ_1(W F W^†) (W F W^†)⟩ ≥ 0` over the `x_1 ≥ 0` half-space algebra:
the `x_1` axis admits the identical construction. The old Step 4
tested only whether the *unconjugated* temporal template transfers
verbatim (it does not — `η_τ` does not flip under `θ_1` in the fixed
convention), which shows nothing about conjugated constructions; its
conclusion is withdrawn. What survives is: per declared axis and
supplied `(T̂², 2a_τ)`, the clock is unique (Step 1); selecting the
axis, the `τ`, and excluding commuting factor clocks is (B-AXIS). ∎

## Consistency with retained no-gos (declared, checked)

- **`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
  (retained_no_go).** This revision asserts nothing that row denies:
  uniqueness is stated transfer-relative and τ-relative; N2/N4/N5
  appear verbatim as (B-AXIS.1–3) declared premises. The prior
  revision's S3 violated its N4/N5 discipline and is withdrawn.
- **`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`
  (retained_no_go).** No SO(4)/continuum-isotropy wording is claimed
  from spatial cubic checks; the continuum corollary stays bounded by
  the emergent-Lorentz row. Where that row notes `c_t = c_s` is an
  extra premise now supplied by the kinetic-isotropy primitive, this
  note only *uses* the direction of that premise (exchange symmetry),
  never its converse.
- **`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`
  (retained_no_go).** Nothing here derives a physical boost action
  from the local algebra: (S1′) concerns the single time-translation
  group only; boosts/Lorentz enter only through the bounded continuum
  corollary, which carries that program's own bounded status.

## Continuum-limit corollary (bounded, unchanged in kind)

The identification of `U(t)` with the Wightman one-parameter group of
a relativistic continuum QFT is **not** part of (S1′)–(S3′); it is
bounded by the emergent-Lorentz program
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
retained_bounded free-sector structural dispersion scope only). The
ultrahyperbolic well-posedness obstruction for `d_t > 1`
(Craig-Weinstein 2009; Tegmark 1997) remains an external
classical-PDE result consumed, if at all, by the downstream consumer,
not here.

## Downstream contract (what may be cited)

For `ANOMALY_FORCES_TIME_THEOREM.md` (premise row SC):

- citeable now: **conditional on (B-AXIS), exactly one generator `H`
  of one strongly continuous unitary group, and codimension-1 Cauchy
  slice structure** — i.e. the `d_t ≤ 1` cap in axis-conditional
  form. Free `U = 1` bilinear propagation may also cite the R-FBQL
  finite quasilocal lightcone with speed `v_mu = 4 W_mu/mu`; no
  interacting/fixed-background exact-log propagation clause is supplied
  here. (B-AXIS) references no anomaly content, so the consumer's
  non-circularity separation (time defined upstream of the anomaly
  argument) is preserved in premise-supplied form.
- no longer citeable: "the temporal direction is the unique
  RP-admissible reflection axis of the staggered-Dirac action" and
  any unconditional "no second clock" wording. The consumer's SC row
  text predates this re-scope and needs a follow-up edit.

## Relation to the retained Stone narrow row

`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
is consumed, not duplicated: the old inline Steps 1–2 re-proved its
N1–N4 content and are deleted in favor of the citation. This note
adds, beyond that row: the identification of its abstract `T` with
the (R-RP2)/(R-SC2) supplied `T̂²/M_T` (Step 1), the (S2′) Cauchy
slice structure (Step 2), and the (S3′) exchange-symmetry boundary
with the declared (B-AXIS) premise (Step 3). It contradicts nothing
in that row.

## Honest status

**Bounded theorem.** (S1′) closes from retained/retained_bounded
one-hop inputs given the declared premise; (S2′a,b) closes at the
retained_bounded level of its suppliers and (S2′c) closes only on the
free `U = 1` bilinear exact-log sector by the retained_bounded R-FBQL
supplier; (S3′) is a computed exact certificate plus a declared
premise. Not positive_theorem: the transfer supply is bounded
(2-step, staggered-only, fixed background), spatial clustering is
outside the claim, interacting/fixed-background exact-log propagation
is not supplied, and the axis selection is a premise by the retained
(G-SCOPE) no-go.

The runner computes the load-bearing content: supply-hypothesis
residuals for (R-STONE) on a concrete finite-range block transfer;
Stone reconstruction and group-law residuals; τ-rescaling (N2
load-bearing); a non-Hermitian-transfer falsifier; equal-time tensor
locality and codimension arithmetic; finite-range LR sanity residuals
with inside/outside contrast on the runner's explicit toy block; the
exact exchange intertwiner (1)–(2) with a no-sign-field falsifier; the
two-clock tensor-factor comparator (2-dimensional generator span,
excluded only by B-AXIS.3); and a finite-range boundary block — a
strictly local positive transfer whose log-generator has a computed
nonzero end-to-end Pauli component, with the single-factor contrast
where the log returns the local generator exactly. The retained
free-bilinear quasilocal LR supplier has its own companion runner.

**Honest claim-status summary.** This is a bounded theorem on retained and
retained-bounded one-hop inputs plus the declared B-AXIS premise. Its scope is
axis-conditional single-clock codimension-1 unitary evolution: with the
source-supported internal block denominator `2a_tau` for the
retained-bounded RP/SC two-step transfer supply `T_hat^2`, a still-supplied
absolute physical clock unit/time metric, one declared evolution axis carrying
that transfer construction, and no independent commuting transfer factor
admitted as a second clock, the retained finite-dim Stone row gives the unique
generator
`H = -(1/(2a_tau)) log(T_hat^2/M_T) >= 0` and the unique strongly continuous
one-parameter unitary group `U(t) = exp(-itH)`. Each lattice slice `Sigma_t` is
a codimension-1 Cauchy surface with mutually commuting per-site `M_2(C)`
tensor-product equal-time algebra.

On the free `U = 1` bilinear exact-log sector only, the retained-bounded
free-bilinear quasilocal LR bridge supplies finite propagation with envelope
`||[alpha_t(A_x),B_y]|| <= 2||A_x||||B_y|| exp(-mu d_1(x,y)+4 W_mu |t|)`,
`0 < d mu < eta < arcsinh(m)`. No interacting/fixed-background exact-log
propagation claim is made. The prior S3 claim that the temporal direction is
the unique RP-admissible reflection axis is withdrawn: the staggered hop
operator is exactly invariant under the time-space exchange unitary
`W = P_{tau<->1} diag((-1)^{x_tau x_1})`, so axis selection is a premise,
consistent with the retained single-clock uniqueness scope boundary
(N2/N4/N5). Continuum Wightman identification stays bounded by the
emergent-Lorentz program.

Every load-bearing input is retained or retained-bounded on this source
surface except the surviving declared/open pieces of B-AXIS: absolute
clock-rate/unit content for (B-AXIS.1b), axis/transfer-construction uniqueness
(B-AXIS.2), and no-independent-factor exclusion (B-AXIS.3). The older B-RANGE
finite-range generator premise is no longer part of the current claim;
free-sector propagation is supplied by the retained-bounded R-FBQL bridge.
Because these B-AXIS pieces remain declared/open, this branch is not a
retained-grade proposal. No new axiom, fitted parameter, observed value, or
status promotion is made here; the independent audit lane remains the only
authority for effective status.

**Not in scope.**

- Any unconditional no-second-clock / unique-RP-axis claim (withdrawn;
  see §0 and S3′).
- Spatial clustering on `Σ_t` (conditional L2 of the cluster row; not
  consumed).
- Continuum Osterwalder-Schrader / Wightman reconstruction (bounded
  by the emergent-Lorentz program).
- The ultrahyperbolic `d_t > 1` well-posedness obstruction (external,
  consumer-side).
- Deriving the (B-AXIS) premise itself. Candidate future suppliers:
  a Record-axiom registration-direction theorem, or a
  boundary-condition (antiperiodic temporal BC) selection row; either
  would be a separate note.
- Interacting or fixed-background exact-log locality. The free
  bilinear quasilocal LR bridge does not prove gauged/interacting
  log-transfer locality, the gapless `m = 0` boundary, or continuum
  microcausality.

## Citations

- baseline carrier: [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- Stone core (retained): [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
- transfer supply (retained_bounded):
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- equal-time tensor locality (retained_bounded):
  [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md)
- free exact-log quasilocal propagation (retained_bounded, free
  `U = 1` bilinear sector only):
  [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
- per-site Cl(3) algebra (retained):
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
- governing boundaries (retained_no_go):
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md),
  [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
- kinetic-form premise context (meta, approved premise):
  [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- APBC/PBC axis-label bridge (conditional supplier; no status change):
  [`SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](SINGLE_CLOCK_APBC_AXIS_LABEL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)
- continuum bound (retained_bounded):
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- downstream consumer (cross-reference only, not a dep):
  `ANOMALY_FORCES_TIME_THEOREM.md` (premise row SC)
- standard external references (theorem-grade, no numerical input):
  Stone (1932) *Ann. Math.* 33, 643; Streater-Wightman (1964) ch. 3;
  Osterwalder-Schrader (1973) *Comm. Math. Phys.* 31, 83;
  Sharatchandra-Thun-Weisz (1981) *Nucl. Phys. B* 192, 205;
  Menotti-Pelissetto (1987) *Comm. Math. Phys.* 113, 369;
  Golterman-Smit (1984) staggered lattice rotation symmetry
  (context for the axis-exchange field redefinition);
  Craig-Weinstein (2009) *Proc. Roy. Soc. A* 465, 3023; Tegmark
  (1997) *Class. Quant. Grav.* 14, L69 (both consumer-side only).
