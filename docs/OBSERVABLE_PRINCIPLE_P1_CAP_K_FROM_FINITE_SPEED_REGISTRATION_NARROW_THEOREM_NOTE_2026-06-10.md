# Observable-Principle P1 — (CAP-K) From Finite-Speed Registration: the Lieb-Robinson Sensitivity Cone Caps Registrations Per E-Fold (Narrow Theorem, Conditional on a Declared Registration Realization Class)

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem with four declared realization
clauses (none asserted as framework-forced), plus two computed
falsification legs and one named open refinement.
**Claim scope (narrow):** the single rate clause left open by the
(BR)-license no-go note
`OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md`
(wave 2 of this campaign; in-flight on branch
`claude/science-fix/p1-br-license-record-capacity-20260610`, commit
`c116993cf`, not yet merged into this branch's tree — every consumed fact
is therefore **recomputed in this note's runner**, none cited blind) —
the premise

```text
(CAP-K)  a record register registers boundedly per e-fold of source
         change: every e-fold's registered disjoint record collection
         has at most K sectors, with K uniform over e-folds,
```

which, with the declared realization clause (CAP-real) and the retained
unit-record normalization ((CAP-M) at `M = 1`), completes the P1 exponent
selection through that note's Lemma C:

```text
(CAP-real) + (CAP-M, M = 1) + (CAP-K)
    => sup_z |W(ez) - W(z)| <= K      (BR-int)
    => pass set on {s.g_p} is exactly {p = 0}   (W = c log z selected).
```

That note proved (CAP-K) has **zero retained static suppliers**: the
finite-sector algebra is cap-free by its own freedom identity; the
retained unbounded-additivity schema affirmatively licenses `4^k` unit
records per e-fold; the Busch/Gleason effect rows are magnitude-shaped,
probability-conditional, and readout-blind; and bare register-size growth
`(2n+1)^3` defeats static rate inference. **Every one of those kills is
static** — an algebraic capacity statement about the register *inventory*.
None consumed dynamics. This note consumes the dynamics:

> **Theorem (conditional, the dynamical route).** Registering a record is
> a physical process on the lattice: a correlation must be established
> between the source region and the register sites, and the retained
> finite-range Lieb-Robinson surface bounds how fast. Within the
> **finite-speed registration realization class** — four declared clauses
> (REG-dyn), (REG-tau), (REG-thr), (REG-site) of Section 2, none claimed
> as framework-forced — every e-fold's δ-sensitive register set is
> contained in the Lieb-Robinson sensitivity cone of radius
>
> ```text
> D* = v_LR·tau + R·ln( (e/(e-1)) · ||V|| · R / (v_LR · δ) ),
> ```
>
> with `v_LR = 2·e·q·W·R = 4e(|m| + 2d)` the retained (F4) velocity of
> the microcausality bridge note (q = 2, R = 1, W = |m| + 2d), so the
> per-e-fold disjoint-record count is capped:
>
> ```text
> (CAP-K)  K <= (s_X + 2·ceil(D*))^3 · log2(d_site)/log2(2)
>             = (s_X + 2·ceil(D*))^3        (site-register reading), or
>          K <= d_site^{(s_X + 2·ceil(D*))^3}  (weakest joint-sector
>                                               reading; still finite),
> ```
>
> with `d_site = 2` from the Quantum axiom, **uniformly in the e-fold
> index k** (the bound contains no k — verified by symbol inspection, not
> extrapolation). Lemma C then yields (BR-int) with constant `K` and the
> exponent selection `p = 0` completes, conditionally on the class.
> Canonical computed instance (`Z^3`, `m -> 0`, `tau = 1`, `||V|| = 1`,
> `δ = 1/10`, single-site source): `D* ~ 63.82`, `K = 129^3 = 2146689`.
>
> **The schema's `4^k` witness is disarmed, not contradicted:** assigning
> `4^k` unit records to e-fold `k` stays licensed as additive bookkeeping
> (the retained schema is untouched), but it is **not realizable by any
> finite-speed registration process at a uniformly bounded window**: the
> required window grows without bound (`tau_11 >= 1.25 > 1`,
> `tau_30 >= 8036` on the canonical instance; under the weakest joint
> reading, failure at `k = 1073345` for `tau = 1`) — computed, both
> readings. And an unbounded-speed comparator (one long-range bond)
> breaks the sensitivity bound by a factor `> 100`: the finite `v_LR` is
> load-bearing, not decorative.

**Result.** (CAP-K) is **derived inside the declared finite-speed
registration realization class** — the first dynamical carrier for the
rate clause after the static kills, and exactly the structural/schema-row
shape (a per-e-fold capacity *principle*, not a finite certificate) that
the BR-license note's Section 4.2 specified a (CAP-K) supplier must take.
This note does NOT retire P1: (CAP-real) remains DECLARED (it is a
quantitative slice of the record-scalar-map no-go's middle arrow and is
never asserted here), and the four (REG) clauses are declared realization
boundaries — no retained row forces records to be established by the
lattice dynamics (the record-formation no-go stands), and the clock
window is supplied, never derived from counts (the clock/rate interface
no-go stands). What changes, monotonically, is the open premise's shape:
the bare rate cap with zero suppliers becomes a **physical realization
statement** — "records of an e-fold are established by the retained
finite-range dynamics within a bounded supplied clock window" — from
which the cap *follows* with a computed constant.

**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; later status is generated by the
audit pipeline after independent review.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent audit
lane.
**Primary runner:**
[`scripts/observable_principle_p1_cap_k_check_2026_06_10.py`](../scripts/observable_principle_p1_cap_k_check_2026_06_10.py)
(expected `TOTAL: PASS=31 FAIL=0`, exact SymPy plus deterministic
finite-dimensional dynamics, < 5 min).

## 0. Honest framing: what is derived, what is declared

Wave 3 of the P1 exponent campaign (barrier selector → (NU) license hunt
→ (BR)/capacity license hunt → this note). The campaign meta-move is
unchanged: split the open premise into finite mechanically checkable
clauses; hunt for an adjacent already-retained structure covering one
clause; ship the residual strictly smaller. The wave-2 hunt was static
and failed with witnesses; the opening it left was named in its own
text: the retained surface lacks *capacity* rows, but the repo's
**dynamics** rows were never consumed. The adjacent already-retained
surface that the static kills never touched is the Lieb-Robinson surface:
the microcausality bridge note's unconditional (F4) leg (`retained_bounded`,
grade A) supplies a *proved* finite-range Lieb-Robinson lemma with every
constant derived (`v_LR = 2·e·q·W·R`), applied unconditionally to the
framework hopping Hamiltonian on `Z^3`.

The honest split:

- **Derived (the theorem, Section 3):** within the declared realization
  class, the sensitivity-cone bound, the cap `K`, its k-uniformity, and
  the completion of the Lemma C chain — every step recomputed or
  measured-against-bound in the runner.
- **Declared (the class, Section 2):** that records are established by
  the lattice dynamics at all (REG-dyn); that each e-fold's registration
  occupies at most a supplied clock window (REG-tau); the operator-norm
  sensitivity threshold (REG-thr); the disjoint-records-on-disjoint-sites
  reading (REG-site). Plus the inherited (CAP-real), which remains
  DECLARED exactly as the BR-license note left it.
- **Open refinement (named, Section 4.2):** a volume-uniform quasilocal
  Lieb-Robinson constant for the *exact* reconstructed `H` (the retained
  quasilocality row supplies the kernel data on the free bilinear sector;
  the volume-uniform tail constant is standard mathematics but not
  retained in-repo and is not imported).

This note explicitly does NOT:

- retire P1 or claim P1 closure; (CAP-real) remains declared — never
  asserted as supplied, never derived here;
- assert that records form, or that registration *must* proceed by the
  lattice dynamics ((REG-dyn) is a class definition; the record-formation
  no-go is untouched);
- derive a clock, a clock rate, or the window value tau ((REG-tau) is a
  supplied-clock clause; the clock/rate interface no-go is untouched);
- construct a probability law for records or assert a branch-to-scalar
  map (Section 6); no readout is constructed, identified, or selected;
- promote, demote, or predict the status of any cited row;
- add a framework axiom or repo vocabulary tag ("(REG-dyn)", "(REG-tau)",
  "(REG-thr)", "(REG-site)" are local labels for clauses of this note's
  theorem, not registry entries).

## 1. Inputs and licenses (one-hop)

| Input | Where used | License / status (ledger grades read 2026-06-10) |
|---|---|---|
| (CAP-K)/(CAP-real)/(CAP-M) clause split; Lemma C (`sup-increment <= K·M => (BR-int) => p = 0`); the `4^k` witness; the unit normalization `M = 1`; the supplier-shape constraint ("structural/schema row, not a finite certificate") | the target clause and the completion chain | `OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md` — unaudited, in-flight (commit `c116993cf`); **every consumed fact recomputed in the runner** (T1, T6, T7). |
| (BR-int) point-selection and class escape; demand ladder | completion chain context | `OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md` — unaudited, in-flight (commit `f3a94a9bc`); selection and escape facts recomputed (T1). |
| Proved finite-range Lieb-Robinson lemma (F3-L1/L2) with derived constants; unconditional (F4) leg: hopping family on `Z^d` has `q = 2`, `R = 1`, `W = \|m\| + 2d`, `v_LR <= 4·e·(\|m\| + 2d)` (on `Z^3`: `~ 65.24` at `m -> 0`) | the registration cone (T3, T4); the velocity in `D*` (T5) | [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md) — `retained_bounded` (grade A). The series and exponential bounds are **verified against exactly computed dynamics** on explicit blocks (T3, T4), not cited blind. Its hopping-operator input is `hopping_bilinear_hermiticity_theorem_note_2026-05-02`, graded decoration under the retained `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`; the same commuting per-site mode convention is used here. |
| Exact-H quasilocality on the free bilinear sector: `W_H = \|\|h\|\|_l1 = 1.757278` at `m = 0.3`, `W_tail(10) = 3.526e-03`, sharp rate `arcsinh(m)`; exact `H` is NOT finite-range | the quasilocal extension remark (T9) | [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md) — `retained_bounded` (grade A); numbers read from its cached runner log at that grade, free (`U = 1`) bilinear sector only. |
| One qubit per site; `A_x ~= M_2(C)`; `Z^3` adjacency | `d_site = 2`; the per-site sector bound; the box counts | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — approved axiom memo (Lattice, Quantum). |
| Finite-sector readout identity `I(A) = chi_A · v`, finite additivity | Lemma C recomputation (T1) | [`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md) — `retained`. |
| Unit-record schema `I(R_n) = n`, no intrinsic cap | `M = 1`; the `4^k` witness is schema-licensed (T7 disarms its realization, not its license) | [`RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md`](RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md) — `retained`. |
| "Evolve for clock time t given (T, tau)" is well-defined and unique | the meaning of (REG-tau)'s window, NOT its value | [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) — `retained`; scope boundary per `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (`retained_no_go`): tau-relative, transfer-relative — the window value stays supplied. |
| The clock map is supplied, never derived from counts | why (REG-tau) is declared | [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — `retained_no_go` (T11). |
| Record formation is not unconditionally forced | why (REG-dyn) is declared | [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) — `retained_no_go`. |
| The pruned certificate class and the named reopening inputs | the family-lift escape (Section 5, T10) | [`POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md`](POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md) — `retained_no_go`; class definition quoted verbatim and escaped by input type. |
| Firewalls: no probability law from counts; no branch-to-scalar map | Section 6 compliance | [`POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md`](POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md), [`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md) — both `retained_no_go`. |

No PDG values, no fitted constants, no numerical comparators, no
same-surface family arguments.

## 2. The finite-speed registration realization class (four declared clauses)

Fix a source region `X ⊂ Z^3` occupying an axis-aligned box of `s_X`
sites per axis, and parameters `tau > 0` (window), `δ in (0, 2]`
(sensitivity threshold), `J_V > 0` (source-coupling budget). A T1-d
readout realization belongs to the class iff:

- **(REG-dyn)** — *declared.* The records registered for e-fold `k` are
  established by a physical process on the lattice: unitary evolution
  generated by `H + V_k`, where `H` is the retained finite-range hopping
  family of the microcausality bridge note's (F4) leg (support family
  `q = 2`, `R = 1`, per-site overlap weight `W = |m| + 2d`, commuting
  per-site mode convention) and `V_k` — the e-fold's source change — is
  supported in `X` with `||V_k||_op <= J_V`. No retained row forces this:
  the record-formation no-go exhibits baseline-consistent no-record
  witnesses, so membership is a realization choice, not a theorem. (The
  operator-norm budget side does have a retained_bounded carrier: the
  bridge note's (F2) per-site action-density budgets bound any
  carrier-surface-supported source term by `|X|·J_max`; what stays
  declared is the *association* of one amplitude e-fold with one such
  `V_k` — an instance of (CAP-real)'s middle-arrow slice.)
- **(REG-tau)** — *declared.* Each e-fold's registration process runs for
  at most clock time `tau` in the supplied clock. The retained
  single-clock Stone row makes "evolve for time `t` given `(T, tau)`"
  well-defined and unique; the clock map itself and the window value are
  **supplied**, consistent with the clock/rate interface
  `retained_no_go` ("Without the supplied `tau`, the same record history
  supports many inequivalent rates").
- **(REG-thr)** — *declared (class definition).* A register site `y`
  carries a record of e-fold `k`'s realized outcome only if the process
  is δ-sensitive at `y` to the e-fold's source change:
  `||alpha^{H+V_k}_t(B_y) - alpha^H_t(B_y)||_op >= δ` for some unit-norm
  observable `B_y` at `y` and some `t <= tau`. This is pure operator-norm
  distinguishability — **no probability law, no Born weights, no outcome
  statistics**: a register whose every observable evolves identically
  whether or not the source changed has registered nothing about the
  change. That is the durability semantics of "registration", stated as
  a norm inequality.
- **(REG-site)** — *declared (class definition).* Pairwise-disjoint
  records of one e-fold occupy pairwise-disjoint nonempty register-site
  sets (the records-on-registers reading). The theorem also covers the
  weakest alternative reading (records as pairwise-orthogonal sectors of
  the joint reachable algebra) with a larger but still finite cap.

Inherited and untouched: **(CAP-real)** — the association of the T1-d
readout's e-fold increments with registered collections — remains
DECLARED exactly as in the BR-license note. Asserting it would be the
record-scalar-map no-go's forbidden middle arrow; this note does not.

The class may, for all the axioms care, be empty: the theorem is "every
member satisfies (CAP-K) with a computed K", not "the framework is a
member".

## 3. The theorem and proof

**Theorem.** Let a T1-d readout realization belong to the class of
Section 2. Then for every e-fold `k`:

**(i) Duhamel reduction.** For any observable `B` and `t <= tau`,
with `F(s) = alpha^{H+V_k}_s(alpha^H_{t-s}(B))`,
`F'(s) = i·alpha^{H+V_k}_s([V_k, alpha^H_{t-s}(B)])` (product rule;
unitary conjugation is norm-preserving), so

```text
||alpha^{H+V_k}_t(B_y) - alpha^H_t(B_y)||  <=  int_0^t ||[V_k, alpha^H_u(B_y)]|| du.    (1)
```

**(ii) Lieb-Robinson tail.** The bridge note's proved series lemma
(F3-L1), applied with `A = B_y` (single site, prefactor `|X_A|/q = 1/2`)
and `B = V_k` (distance `D = d(y, X)`), gives
`||[V_k, alpha^H_u(B_y)]|| <= ||V_k|| · sum_{n >= D} (4Wu)^n/n!` (since
`2qW = 4W`, `R = 1`); integrating term-by-term over `u in [0, t]`,

```text
int_0^t ... du  <=  (||V_k||/(4W)) · sum_{n >= D+1} (4Wt)^n / n!                        (2)
            <=  (e/(e-1)) · (||V_k||/v_LR) · exp(v_LR·t - D),     v_LR = 4eW,           (3)
```

the closed form by the bridge note's Step-5 tail estimate
(`sum_{n>=n0} a^n/n! <= e^{ea - n0}/(1 - 1/e)` with `n0 = D + 1` and
`e·a = v_LR·t`). Both (2) and (3) are verified against exactly computed
dynamics on an explicit 10-site chain and an explicit `Z^3` block in the
runner (worst measured/bound ratios `0.030` and `0.027`; the bound is
rigorous, not tuned).

**(iii) Sensitivity cone.** If `y` is δ-sensitive ((REG-thr)) then
combining (1), (3) with `t <= tau`, `||V_k|| <= J_V`:

```text
δ  <=  (e/(e-1)) · (J_V/v_LR) · e^{v_LR·tau - D}
   <=>   D  <=  D* := v_LR·tau + ln( (e/(e-1)) · J_V / (v_LR·δ) ).                      (4)
```

So the δ-sensitive register set of e-fold `k` is contained in the
`l1`-ball of radius `ceil(D*)` around `X`, hence in an axis-aligned box
of `(s_X + 2·ceil(D*))^3 =: N_reach` sites — **independent of k** (the
expression (4) contains no `k`; runner symbol check).

**(iv) The cap.** By (REG-site), pairwise-disjoint records occupy
pairwise-disjoint nonempty subsets of the sensitive register set:
`K <= N_reach`. Per site, the Quantum axiom's `d_site = 2` bounds any
central-sector decomposition at 2 sectors (rank/trace argument:
pairwise-orthogonal nonzero projections in `M_2(C)` number at most 2),
i.e. `log2(d_site) = 1` record-bit per register site. Under the weakest
joint-sector reading (records as pairwise-orthogonal nonzero projections
of the joint algebra on `N_reach` qubits) the same rank argument gives
`K <= d_site^{N_reach} = 2^{N_reach}` — astronomically larger but still
a finite, k-uniform cap. Either way **(CAP-K) holds**:

```text
K  <=  (s_X + 2·ceil(D*))^3        (site-register reading)
K  <=  2^{(s_X + 2·ceil(D*))^3}    (weakest joint-sector reading).        (5)
```

**(v) Completion.** With the retained unit-record normalization
((CAP-M) at `M = 1`) and the inherited declared (CAP-real), Lemma C of
the BR-license note (recomputed: the finite-sector identity on all 81
ordered disjoint pairs of a 4-sector model; the triangle inequality)
gives `sup_z |W(ez) - W(z)| <= K·1` — (BR-int) — and the (BR-int)
point-selection (recomputed: e-fold increment `s·e^{pu}(e^p - 1)/p`,
unbounded for every `p != 0`, constant for `p = 0`) selects exactly
`{p = 0}`: `W = c·log z` on the FORM-stage family. The class-escape
screen is inherited and spot-checked (the cos witness passes (BR-int)
and violates the additive identity at `(e, e)`): no additive-identity
instance is smuggled. ∎

**Canonical computed instance** (`Z^3`, `m -> 0`, `tau = 1`, `J_V = 1`,
`δ = 1/10`, `s_X = 1`): `v_LR = 24e ~ 65.2388`,
`D* = 24e + ln(10/(24(e-1))) ~ 63.8219`, `ceil(D*) = 64`,
`K = 129^3 = 2146689` (site-register reading). The `p = 1` member's
e-fold increment exceeds this `K` at `u = ln(K/(e-1)) + 1` (`z ~ 3.4e6`)
— the cap has teeth against the wrong exponents at explicit points.

### 3.1 Where each kill of the static hunt is respected

- *Finite-sector algebra cap-free:* untouched — the algebra is consumed
  only as the realization identity inside Lemma C; the cap comes from
  dynamics, not from the algebra.
- *Unbounded-additivity schema licenses `4^k`:* untouched — the schema's
  license is bookkeeping over arbitrary finite collections; the theorem
  bounds what a bounded-window finite-speed *process* can realize
  (Section 4.3), which is exactly the distinction the schema's own
  "production of those records: still outside the Record axiom" boundary
  draws.
- *Busch/Gleason magnitude-shaped, probability-conditional,
  readout-blind:* not consumed at all — (REG-thr) is operator-norm
  distinguishability, no measure hypotheses, no effects.
- *`(2n+1)^3` register growth defeats static rate inference:* inverted —
  the same cubic count, intersected with the dynamical cone, is what
  *supplies* the cap: growth of the inventory is irrelevant because only
  the cone is reachable per window.

## 4. Corollaries and the named open refinement

### 4.1 The prompt-shaped information form

Registered information per e-fold is at most
`N_reach · log2(d_site) = (s_X + 2·ceil(D*))^3 · log2(2)` record-bits —
"bits" here is the logarithm of a sector-count dimension (rank), not a
probabilistic entropy; no probability law is constructed. With
`D* = v_LR·tau + O(ln(1/δ))` this is the
`K <= c·(v_LR·tau)^3·log2(d_site)` shape: **a record register registers
boundedly per e-fold of source change** because correlation
establishment is finite-speed and the local dimension is finite.

### 4.2 Quasilocal extension (at the quasilocality row's grade; named open refinement)

The exact reconstructed `H = -log(T_hat^2)/(2 a_tau)` on the free
bilinear sector is **not** finite-range (the retained quasilocality row
exhibits range-4 hops), so the strict (F4) form does not apply to it.
The same row supplies the quasilocal data: finite kernel weight
`W_H = 1.757278` at `m = 0.3` with tails `W_tail(R)` decaying at the
sharp rate `arcsinh(m)` (`W_tail(10) = 3.526e-03`). The truncation `H_R`
is a finite-range family with `q = 2`, range `R`, per-site overlap weight
`<= 2·W_H`, hence `v(R) <= 2e·q·(2W_H)·R` (`~ 382.2` at `R = 10`,
`m = 0.3`), and the cone argument goes through verbatim for `H_R`
(`D* ~ 379.0`, `N_reach ~ 759^3 ~ 4.4e8` on the canonical parameters) —
the cap form survives quasilocally with the same `(v·tau)^3` scaling.
What is **not** imported: the volume-uniform control of the exact-H tail
`H - H_R` inside the Duhamel integral (a standard quasilocal
Lieb-Robinson refinement in the literature, but not retained in-repo).
This is recorded as the named open refinement; the theorem's
unconditional dynamical carrier is the retained (F4) finite-range leg.

### 4.3 The `4^k` family demands unbounded windows (computed)

Realizing `4^k` pairwise-disjoint unit records at e-fold `k` requires,
under the site-register reading, `(s_X + 2·ceil(D*(tau_k)))^3 >= 4^k`,
i.e. `tau_k >= ((4^{k/3} - 1)/2 - c)/v_LR` with
`c = ln((e/(e-1))·J_V/(v_LR·δ))`. On the canonical instance: at
`tau = 1` the cap admits `4^10 = 1048576 <= 2146689` but not
`4^11 = 4194304` (first violation `k = 11`); `tau_11 >= 1.25 > 1`;
`tau_30 >= 8036`. Under the weakest joint reading the requirement is
`N_reach >= 2k`: first failure at `k = 1073345` for `tau = 1`, and
`tau(k = 10^9) >= 9.67`. Under **every** reading, every fixed window
fails at finite `k`: the family remains licensed as schema bookkeeping
and **cannot be realized by any finite-speed registration process at a
uniformly bounded clock window per e-fold**. This is the precise
dynamical disarming of the count-side kill.

### 4.4 Unbounded-speed comparator (the finite speed is load-bearing)

Adding one long-range bond (`0 <-> 5`, `l1`-diameter 5) to the chain
makes the measured sensitivity at `D = 5` violate the finite-range bound
by factors `> 100` (computed: `x3313` at `t = 0.05`); symbolically,
`lim_{v_LR -> oo} D* = oo` — an unbounded-speed process reaches every
register in any window and no finite `K` exists. The retained
`v_LR < oo` is the physics that carries the cap.

## 5. Family-lift escape (the supplier-shape check)

The retained no-go `POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md`
prunes the class

> ```text
> finite post-record certificate alone => unbounded retained law
> ```

and names the only legitimate reopening: "The route can be reopened only
by adding a family-lift input, such as a **supplied law**, projective
consistency, monotone exhaustion, direct-limit compatibility, or
tightness/compactness-style preservation principle."

This route escapes **by input type**, not by strengthened certificates:

1. its load-bearing input is the declared registration-dynamics law
   (REG-dyn)+(REG-tau) — a supplied law quantified uniformly over every
   e-fold, exactly the first named reopening input;
2. **no post-record certificate is consumed anywhere**: the derivation
   reads no finite record prefix, no realized counts, no post-record
   data at all — the bound is computed from the pre-record dynamics
   premise alone;
3. the cap's k-uniformity is proved by symbol inspection of (4) (no `k`
   occurs), i.e. one uniform lemma applied to every e-fold — not an
   extrapolation from finitely many checked e-folds.

It is also exactly the supplier shape the BR-license note's Section 4.2
demanded: "a structural/schema row (a per-e-fold capacity *principle*),
not a finite certificate."

## 6. Firewall compliance (explicit)

- **Count-probability firewall (`retained_no_go`) — respected:** no
  probability law is constructed for records anywhere in this note or
  runner. (REG-thr) is operator-norm distinguishability of Heisenberg
  evolutions; no frequencies, no measures, no Born weights, no outcome
  statistics appear. Realized counts occur only inside the `4^k`
  *witness arithmetic* (exact finite sums), never as laws.
- **Record-scalar-map no-go (`retained_no_go`) — respected:** no
  branch-to-scalar map is asserted. (CAP-real) remains declared — the
  association `z -> A_z` of amplitude e-folds with registered
  collections is part of the open premise, exactly as the BR-license
  note left it; this note caps the collection's size *given* the class,
  it does not build the association.
- **Record-formation no-go (`retained_no_go`) — respected:** (REG-dyn)
  is a class membership clause. Nothing here claims record formation is
  forced by the minimal axioms.
- **Clock/rate interface no-go (`retained_no_go`) — respected:**
  (REG-tau)'s window lives in a supplied clock; no rate is derived from
  counts.

## 7. What T1-d / P1 becomes

P1 is **not** retired; T1-d is **not** edited; this note does NOT retire
P1. The conditional chain now reads:

```text
T1-d (readout W of Z alone on R_{>0})
  + (CAP-real)                          [declared; middle-arrow slice]
  + finite-speed registration class     [four declared (REG) clauses]
      => (CAP-K) with K = (s_X + 2·ceil(D*))^3      [THIS NOTE, computed]
      => with (CAP-M) at M = 1 (retained schema), (BR-int) with constant K
      => pass set {p = 0}: W = c·log z              [Lemma C chain, recomputed].
```

Supplier-side shape change: wave 2 ended with "(CAP-K) has zero retained
suppliers — the retained schema licenses its violation." After this
note, (CAP-K) has a **dynamical carrier with a computed constant**,
conditional on a physically named realization class; the open premise is
no longer a bare rate cap but the class membership statement — records
established by retained finite-range dynamics within a bounded supplied
clock window. The admitted-premise count is unchanged (clauses are
exchanged, not erased); the exchange replaces an unsupplied *cap* by a
declared *process*, with the cap derived. Whether class membership is
ratified, admitted, or eventually derived from a record-production
dynamics row is an owner/audit decision, not this note's claim.

## 8. Route discipline gate

**N1 — Route enumeration.**

| Candidate dynamical route | Marker | Outcome |
|---|---|---|
| Lieb-Robinson / finite-speed registration (this note) | **THEOREM (conditional)** | (CAP-K) derived inside the declared class; constants computed; falsification legs pass |
| Action/Noether budget route (source-magnitude change -> bounded process budget) | PARTIAL, FOLDED IN | the bridge note's (F2) per-site budgets bound `\|\|V_k\|\|` at retained_bounded grade (the `J_V` clause); no retained row converts amplitude e-folds into action budgets — that association is (CAP-real)'s slice and stays declared; no separate route survives |
| Exact-H quasilocal route | OPEN REFINEMENT (named) | cap form survives on truncations with computed `v(R)`; volume-uniform exact-H tail constant not retained, not imported (Section 4.2) |
| Static record/effect routes | KILLED UPSTREAM | wave-2 witnesses; not retried (Section 3.1 shows each kill is respected, not contradicted) |

**N2 — Wall-independence.** The two walls that killed wave 2 (cap-free
record algebra; schema-licensed `4^k`) are both *respected*: the theorem
adds a dynamics premise rather than re-deriving a static cap; the `4^k`
witness keeps its license and loses only bounded-window realizability —
a computed, falsifiable distinction.

**N3 — Hidden-wall scan.** "(REG-*)" labels are local; the Duhamel
identity and tail estimates are standard mathematics with every consumed
instance verified on explicit finite-dimensional dynamics in the runner;
the LR constants are the bridge note's derived constants, re-verified
against measured commutator dynamics, not imported from literature.

**N4 — Residual matching.** The residual attacked is exactly the wave-2
note's Section 4.4 open clause: "(CAP-K license, open): retained-grade
structure forcing a uniform finite cap on record registrations per
e-fold of amplitude, together with the realization clause (CAP-real)".
This note supplies the cap-forcing structure conditionally on a declared
realization class and leaves (CAP-real) declared — the residual shrinks
from "cap + realization, both unsupplied" to "realization clauses only".

**N5 — Rhetoric audit.** No claim that P1 closes, that the class is
forced, that records must form, or that the clock is derived. The
theorem is conditional and presented as such.

**N6 — Partial-closure path scan.** Named paths: (a) owner/audit
ratification of the (REG) class as the declared registration realization
(governance); (b) a future record-production dynamics row deriving class
membership (would have to pass the record-formation no-go's named
escape); (c) the quasilocal refinement of Section 4.2; (d) governance
ratification of (BR-int)/(CAP) directly (wave-2 spec).

**N7 — Steelman.** *"The cap depends on (δ, tau, J_V, s_X) — isn't K a
dial?"* Response: K's *value* is class-parameter-dependent (and stated
so), but (BR-int) needs only *finiteness and k-uniformity* of K, which
hold for every parameter choice in the class; the selection of `p = 0`
is parameter-independent. *"(REG-thr) smuggles measurement."* Response:
it is an operator-norm inequality on Heisenberg evolutions — weaker than
any measurement postulate; a register violating it is unchanged by the
source change in every observable, which no reading of "durable
registration of the realized outcome" can call a record of that change.
*"The joint-sector reading makes K astronomically large."* Conceded and
computed (`2^{N_reach}`); the chain needs finiteness, not smallness, and
the `4^k` witness still fails at finite k under that reading (T7).

**N8 — Cross-cycle echo.** This is the same dynamical move that
discharged the GL(F) discriminator this morning (static no-gos,
dynamical derivation): the static kills documented the supplier shape;
the adjacent retained surface the kills never consumed was the
Lieb-Robinson dynamics; the derivation lands one hop from it.

## 9. Reproduction

```bash
python3 scripts/observable_principle_p1_cap_k_check_2026_06_10.py
```

Expected output (matches stdout):

```text
== T1: Lemma C and the selection chain (BR-note facts recomputed, not cited blind) ==
  [PASS][A] retained finite-sector identity recomputed: I(A u B) = I(A) + I(B) on all 81 ordered disjoint pairs of a 4-sector model  -- pairs=81
  [PASS][A] Lemma C capacity bound: |sum_{i in A} v_i| <= K*M by finite additivity + triangle inequality; retained unit-record schema has M = 1 by normalization (I(R_7) = 7 recomputed)  -- I(R_7)=7
  [PASS][A] e-fold increment identity: g_p(e^{u+1}) - g_p(e^u) = e^{pu}(e^p - 1)/p exactly; p -> 0 member has constant increment 1
  [PASS][A] (BR-int) point-selection recomputed: increments unbounded for p in {1, 2, 1/2, -1/2, -1} (limits = oo), constant for p = 0 — pass set on {s*g_p} exactly {p = 0}
  [PASS][A] class-escape spot check: W = log z + (1/10) cos(log z) has e-fold increments <= 1 + 2/10 ((BR-int) holds) yet additive residual at (e, e) is (1/10)(cos 2 - 2 cos 1) != 0 — no additive-identity instance is entailed (Lemma-R screen)  -- res(e,e)=-0.149675
== T2: the Duhamel identity (the bridge from generator difference to commutators) ==
  [PASS][A] Duhamel identity verified on an explicit 4-site instance: alpha^{H+V}_t(B) - alpha^H_t(B) = i int_0^t alpha^{H+V}_s([V, alpha^H_{t-s}(B)]) ds (Simpson quadrature residual < 1e-8)  -- residual=5.08e-14
  [PASS][A] integrated-commutator bound: ||alpha^{H+V}_t(B) - alpha^H_t(B)|| <= int_0^t ||[V, alpha^H_u(B)]|| du on the same instance  -- lhs=1.7565e-02 <= int=1.7650e-02
== T3: the registration cone on the chain — retained (F4) LR data, measured vs bound ==
  [PASS][C] chain (d=1, m=0, q=2, R=1, W=2, v_LR=8e): measured sensitivity ||alpha^{H+V}_t(B_y) - alpha^H_t(B_y)|| <= series bound (||V||/(4W)) sum_{n>=D+1} (4Wt)^n/n! on the full (D, t) grid (D in 2..5, t in 0.02..0.15)  -- worst measured/bound = 0.0300
  [PASS][A] closed exponential form dominates the series form on the grid: (e/(e-1))(||V||/v_LR) e^{v_LR t - D} >= series bound — the D* formula below is licensed by the proved chain
== T4: the registration cone on an explicit Z^3 block ==
  [PASS][C] Z^3 2x2x2 block (d=3, m=0, W=6, v_LR=24e): measured sensitivity <= series bound at l1-distances 2 and 3, t in {0.005, 0.01, 0.02}  -- worst measured/bound = 0.0269
  [PASS][A] explicit Z^3 l1-ball enumeration: |B_1(3)| = 63, |B_1(5)| = 231, each <= the (2D+1)^3 box bound used by the cap (343, 1331)  -- counts={3: 63, 5: 231}
== T5: the sensitivity radius D* and the per-e-fold cap K (exact arithmetic) ==
  [PASS][A] D* formula derived (sympy solve): delta-sensitivity at distance D forces D <= D* = v_LR*tau + ln((e/(e-1)) ||V|| / (v_LR delta)) (R = 1)
  [PASS][C] canonical instance (Z^3, m -> 0, tau = 1, ||V|| = 1, delta = 1/10, s_X = 1): D* = 24e + ln(10/(24(e-1))) ~ 63.82, ceil = 64, N_reach = (1 + 2*64)^3 = 129^3 = 2146689 — a finite computed cap  -- D*=63.8220, N_reach=2146689
  [PASS][A] per-site sector bound (Quantum axiom, d_site = 2): at most 2 pairwise-orthogonal nonzero projections per M_2 site (rank sum <= 2); joint reading over N sites: at most 2^N — so K <= N_reach (site-register reading, log2(d_site) = 1 record-bit per site) or K <= 2^{N_reach} (weakest joint reading), both finite
  [PASS][A] k-uniformity (the cap is one lemma, not an extrapolation): the D* expression's free symbols are exactly {tau, delta, J_V, v} — the e-fold index k does NOT occur, so (CAP-K) holds with the SAME K for every e-fold
== T6: chain completion — (CAP-K computed) + (CAP-M = 1) + (CAP-real declared) => (BR-int) => p = 0 ==
  [PASS][A] completion: increments <= K*M = 2146689 forces (BR-int); on {s*g_p} the pass set is exactly {p = 0}: W = c log z is selected (Lemma C chain recomputed with the computed K; (CAP-real) remains DECLARED, not supplied)
  [PASS][D] wrong-exponent rejection at the computed cap: the p = 1 member's e-fold increment e^u (e-1) exceeds K = 2146689 at u = ln(K/(e-1)) + 1 (z = e^u ~ 3.4e6) — explicit witness, exact inequality  -- increment/K = e at u = 15.038
== T7: the 4^k family demands unbounded windows (the schema-licensed witness cannot be realized) ==
  [PASS][D] site-register reading: at tau = 1 the cap K = 2146689 admits 4^10 = 1048576 but NOT 4^11 = 4194304 (first violation k = 11); required windows grow without bound: tau_11 >= 1.25 > 1, tau_30 >= 8036 — the 4^k family needs unbounded processing time per e-fold  -- tau_11>=1.2501, tau_30>=8036.5
  [PASS][D] weakest joint-sector reading: at tau = 1 the cap 2^{N_reach} fails first at k = 1073345; at k = 10^9 the required window is tau >= 9.67 > 1 — under EVERY reading each fixed window tau fails at finite k, so no uniformly bounded-window finite-speed process realizes the family (it stays licensed as schema bookkeeping only)  -- k_b*=1073345, tau(k=1e9)>=9.67
== T8: unbounded-speed comparator — the finite LR speed is load-bearing ==
  [PASS][D] one long-range bond (0 <-> 5) breaks the finite-range sensitivity bound at D = 5 by a factor > 100 (t = 0.05 and 0.1): without finite-range dynamics the registration cone (and hence the cap) does not exist  -- violations x3313, x194
  [PASS][A] symbolic comparator: lim_{v_LR -> oo} D* = oo (sympy limit) — an unbounded-speed process reaches every register in any window and (CAP-K) has no finite value; the retained v_LR < oo is the load-bearing physics
== T9: quasilocal extension — landed exact-H numbers reused at their grade ==
  [PASS][B] landed quasilocality numbers read from the cached retained_bounded runner log: W_H = 1.757278 (m = 0.3) and W_tail(10) = 3.526e-03 — finite per-site weight, exponentially small tails (free bilinear sector, at that row's grade)  -- W_H=1.757278, W_tail(10)=0.003526
  [PASS][C] exact-H truncation H_R (R = 10, m = 0.3): v(R) <= 2e*q*(2 W_H)*R ~ 382.2, D* ~ 379.0, N_reach ~ 759^3 ~ 4.4e8 — the cap form survives quasilocally with the same (v tau)^3 scaling; the volume-uniform exact-H tail constant is a NAMED open refinement, not imported  -- v(10)=382.1, D*=379.0, N=437245479
== T10: family-lift class escape (textual, against the retained no-go itself) ==
  [PASS][B] the pruned class quoted from the retained no-go: 'finite post-record certificate alone => unbounded retained law' is present verbatim
  [PASS][B] the reopening clause quoted from the retained no-go: a family-lift input such as 'a supplied law, ...' is the named legitimate route
  [PASS][B] this route's escape is by input type: the note declares its load-bearing input as a supplied dynamics law ((REG-dyn)+(REG-tau), uniform over every e-fold) and consumes no post-record certificate; the cap's k-uniformity is the T5 symbol check, not a finite-prefix extrapolation
== T11: clock-window boundary honesty ==
  [PASS][B] the clock is supplied, never derived from counts: the retained_no_go clock/rate interface states 'Without the supplied `tau`, the same record history supports many inequivalent rates' — present verbatim
  [PASS][B] the note declares (REG-tau) as a supplied clock-window clause of the realization class (not derived); the retained single-clock Stone row licenses only that 'evolve for t given (T, tau)' is well-defined — the window value stays declared
== T12: ledger grades, firewall strings, honest scope ==
  [PASS][B] cited rows present in the audit ledger at the cited effective statuses (one-hop presence check, 10 rows)  -- mismatches=[]
  [PASS][B] note honest-scope and firewall-compliance strings present  -- missing=[]
  [PASS][B] forbidden closure/promotion strings absent  -- found=[]

TOTAL: PASS=31 FAIL=0
```

A passing run supports only: (i) the Lemma C chain and (BR-int)
selection facts, recomputed; (ii) the Duhamel identity and the
sensitivity-cone bounds, verified against exactly computed dynamics on
explicit chain and `Z^3` blocks with the retained (F4) constants; (iii)
the cap arithmetic, its k-uniformity, and the completion with the
computed K; (iv) the two falsification legs (`4^k` windows; long-range
comparator); (v) the quasilocal numbers at their grade; (vi) the
family-lift, clock, ledger, and firewall textual facts. It does **NOT**
establish class membership for the framework, does NOT retire P1, and
does NOT promote any row.

## 10. Cross-references

- `OBSERVABLE_PRINCIPLE_P1_BR_LICENSE_FROM_RECORD_CAPACITY_NARROW_NO_GO_NOTE_2026-06-10.md`
  (commit `c116993cf`, in-flight) — wave 2: the (CAP) clause split,
  Lemma C, the static kills, the supplier-shape spec this note meets.
- `OBSERVABLE_PRINCIPLE_P1_NU_LICENSE_FROM_RETAINED_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`
  (commit `f3a94a9bc`, in-flight) — wave 1.5: the demand ladder this
  chain plugs into.
- [`OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md`](OBSERVABLE_PRINCIPLE_P1_EXPONENT_BARRIER_PARAMETER_SELECTOR_NARROW_THEOREM_NOTE_2026-06-10.md)
  — wave 1: the conditional selector; its physical reading ("the readout
  resolves the amplitude domain with finitely many distinguishable
  units") is what (CAP-K)-from-dynamics makes precise.
- [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  — the retained_bounded LR surface: proved lemma, derived constants,
  unconditional (F4) leg consumed here.
- [`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the retained_bounded exact-H quasilocal data (Section 4.2).
- [`POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md`](POST_RECORD_FINITE_TO_UNBOUNDED_FAMILY_LIFT_NO_GO_2026-06-06.md)
  — the pruned certificate class; escape in Section 5.
- [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md),
  [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md),
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
  — the clock boundary: window well-defined given `(T, tau)`, value
  supplied.
- [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
  — why (REG-dyn) is declared.
- [`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md),
  [`RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md`](RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md)
  — the retained record surface consumed inside Lemma C and the `M = 1`
  normalization; their cap-freedom is respected (Section 3.1).
- [`POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md`](POST_RECORD_COUNT_PROBABILITY_FIREWALL_2026-06-06.md),
  [`OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md`](OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md)
  — the firewalls (Section 6).
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — Lattice,
  Quantum (`d_site = 2`), Record.

### Source-note boundary

**Hypothesis set used:** (1) the four declared (REG) clauses of Section 2
(class definition; not asserted as framework-forced); (2) the inherited
declared (CAP-real) (untouched); (3) the retained (F4) Lieb-Robinson
data and proved lemma, re-verified against exactly computed
finite-dimensional dynamics; (4) the Duhamel identity (standard, verified
on an explicit instance); (5) the Quantum axiom's `d_site = 2` and the
Lattice axiom's `Z^3` adjacency (box/ball counting, exact); (6) the
retained record rows inside Lemma C and the `M = 1` normalization
(recomputed); (7) ledger reads (presence/status checks only). Throughout:
no probability law is constructed; no branch-to-scalar map is asserted;
no readout is constructed, identified, or selected; no post-record
certificate is read.

**Forbidden-imports check:** no new framework axiom; no new repo
vocabulary tag; no PDG/fitted/observed values; no literature constant
imported (the LR constants are the bridge note's derived constants); no
status promotion or prediction for any row.

**No-promotion statement:** this note does not promote, demote, or set
the audit status of any cited row. The independent audit lane is the only
status authority.

## Changelog

- **2026-06-10** — initial note. Wave 3 of the P1 exponent campaign:
  (CAP-K) derived inside a declared finite-speed registration realization
  class ((REG-dyn), (REG-tau), (REG-thr), (REG-site)) from the retained
  (F4) Lieb-Robinson surface via a Duhamel sensitivity-cone argument;
  cap `K <= (s_X + 2·ceil(D*))^3` (canonical instance `129^3 = 2146689`),
  k-uniform by symbol inspection; completion through Lemma C / (BR-int)
  recomputed (`p = 0` selected, conditionally); `4^k` schema witness
  disarmed dynamically (unbounded windows required, both readings,
  computed); unbounded-speed comparator violates the cone bound `x3313`;
  quasilocal extension computed at the quasilocality row's grade with the
  volume-uniform exact-H tail named as the open refinement; family-lift
  no-go escaped by input type (supplied law; no post-record certificate;
  k-uniformity by symbol inspection). Runner `TOTAL: PASS=31 FAIL=0`.
  P1 not retired; (CAP-real) and the (REG) clauses declared, not derived.
