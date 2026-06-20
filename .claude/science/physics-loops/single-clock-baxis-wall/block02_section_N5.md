# Block02 Section — N5 (no independent commuting transfer factor / no second clock)

**Decomposition slot:** B-AXIS.3 = N5 — "no independent commuting transfer factor
is admitted as a second physical clock," the third undischarged premise of
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`
(audited_conditional, bounded_theorem, downstream fanout 959 / Class A).

**Type:** branch-local source obstruction section (no-go-supporting / negative
boundary). **Claim type (intended audit classification):** negative_route_pruning
with an exact source-surface countermodel; relocates the residual to an open gate.

**Status (branch-local vocabulary):** N5 is a LIVE wall, sharpened — NOT closed,
NOT cracked, NOT a derivation of B-AXIS, NO new axiom or primitive. Independent
audit lane is the sole status authority.

- **proposal_allowed:** false
- **bare_retained_allowed:** false
- **audit_required_before_effective_retained:** true
- **B_AXIS_DERIVED:** false · **SECOND_PHYSICAL_CLOCK_EXCLUDED:** false ·
  **AUDIT_LEDGER_WRITTEN:** false

---

## 1. Headline result (source-surface, not proxy)

N5 cannot be derived from A_min (Lattice + Quantum + Record) plus the supplied
two-step transfer. The decisive correction this section carries over all prior
N5 work is that the obstruction is now anchored on the framework's **own**
supplied object rather than on an arbitrary tensor-product proxy:

> The supplied two-step transfer is **maximally factorized**:
> `T̂² = ⊗_p diag(1, e^{-2E(p)}) = exp(-2 a_τ Ĥ)`, with `Ĥ = Σ_p E(p) n_p`,
> `E(p) = arcsinh(√(m² + sin²p))`, `n_p = a_p† a_p`. It is a tensor product of
> `L_s` independent commuting positive per-mode factor clocks (generator tangent
> span `{n_p}` has dimension `L_s`, not 1).

Two consequences follow, each a closed route rather than an open hope:

1. **The naive irreducibility / commutant-center route is CLOSED-as-FALSE.** No
   commutant or center argument can force a single one-parameter clock orbit,
   because the supplied transfer is maximally *reducible* — it already exhibits
   the `L_s`-factor split a second-clock comparator would need. ("`T̂²` is
   irreducible" is therefore false on the source surface itself, not merely
   unproven.)

2. **The gauge-redundancy route is FALSIFIED.** The factor flows are not gauge:
   their generators escape `span{I, Ĥ}` (best-fit residual of the single-mode
   clock `n_0` against `c·Ĥ + b·I` ≈ 0.65 > 0), and they produce **distinct
   durable occupation records** that no single `Ĥ`-orbit reproduces — a swept
   single-clock time `t` never matches the alternate factor clock's durable
   record pair `(⟨n_0⟩, ⟨n_1⟩)` (min-distance ≈ 0.40 over the sweep; normalized
   record profiles differ by L1 ≈ 2.0). This is a relabeling-invariant,
   Record-visible discriminator — not a phase Record cannot see.

Therefore the missing supplier is a **physical-clock-admission datum**: a chosen
positive clock-ray in `span_{≥0}{n_p}`, equivalently a record-order bridge tying
durable outcomes to one supplied clock. That choice carries `(L_s − 1)`
undetermined parameters and is NOT supplied by Lattice, Quantum, or Record. N5
relocates to the **record-production / emergent-dynamics OPEN GATE** of
`MINIMAL_AXIOMS_2026-06-05` (Record supplies no occupancy rule, no time metric,
no dynamics).

---

## 2. Absorbed runner (in-tree, recomputed, NOT rebuilt here)

This section ABSORBS the block01 fresh-attempt runner R-N5-IRR. The runner builds
the actual supplied `T̂²` from action-derived data and checks the irreducibility
and gauge-redundancy closures leg-by-leg with explicit numpy residuals. It was
re-run in-tree on this branch to confirm the load-bearing facts; it reproduces
deterministically (< 1s, surfaces `L_s=3/m=0.5` and `L_s=4/m=0.3`).

- Runner: `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py`
- Cache: `logs/runner-cache/single_clock_n5_irreducibility_factor_clock_2026_06_20.txt`
- Result: **TOTAL: PASS=36 FAIL=0** (verified in-tree on
  `physics-loop/single-clock-baxis-wall-block02-20260620`).

Block map (load-bearing residuals, recomputed not cited blind):

- **[SURF]** `T̂² = exp(-2 a_τ Ĥ)` (resid ≤ 5.6e-17); `T̂² = ∏_p` lifted per-mode
  factor (resid 0); every factor positive-definite; factors commute pairwise
  (resid 0); generator span dim = `L_s`. Maximal reducibility established.
- **[GAUGE]** all `L_s` mode generators lie OUTSIDE `span{I, Ĥ}` (rank grows on
  adding each `n_q`, base_rank{I,Ĥ}=2); single-mode `n_0 ≠ c·Ĥ + b·I`
  (resid ≈ 0.65). Gauge-collapse closure FALSIFIED.
- **[CONTENT]** factor clock freezes durable `⟨n_1⟩` while `Ĥ` moves it; no
  swept `t` reproduces the alt clock's `(⟨n_0⟩, ⟨n_1⟩)` (min-dist ≈ 0.40);
  record profiles differ (L1 ≈ 2.0); alt-clock projectors commute / additive
  (Record-legitimate flow).
- **[BRIDGE]** physical-clock admission is a free ray choice in `span_{≥0}{n_p}`
  (two admissible rays differ by ≈ 1.5) carrying `(L_s − 1)` free parameters.

Per source discipline, this section does NOT take load-bearing edges to the
conditional parent keystone (2026-05-03), the unaudited finite-speed cone note,
or the downstream ANOMALY_FORCES_TIME consumer; the facts above are the runner's
own in-tree recomputation.

---

## 3. Supersession of the precursor N5 branches

Two prior in-flight branches owned N5 and both left an **unexplained** boundary
flag because they built only a *foreign* arbitrary two-qubit tensor product as
the countermodel and never built the framework's own `T̂²`:

| precursor branch | runner (path) | PASS | left-open flag |
|---|---|---|---|
| `origin/physics-loop/single-clock-n5-factor-boundary-20260617` | `scripts/single_clock_independent_commuting_transfer_factor_n5_no_go_2026_06_17.py` | 34 | `SECOND_PHYSICAL_CLOCK_PROVED=FALSE`, escape named but unresolved |
| `origin/physics-loop/single-clock-physical-clock-inventory-20260617` | `scripts/single_clock_physical_clock_admission_inventory_n5_support_2026_06_17.py` | 35 | `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE`, explicitly *source-inventory, not algebraic exclusion* |

R-N5-IRR **supersedes** both: the prior `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED
= FALSE` and `SECOND_PHYSICAL_CLOCK_PROVED = FALSE` are no longer *unexplained*
flags — they now have a **source-surface reason**. The factor split is not a
weaker proxy a future irreducibility theorem might dismiss; it is the real
object's own maximal `⊗_p` structure, so the irreducibility route is closed as
false and the gauge route is falsified by Record-visible content. These branches
are CITED as the precursors (by path + PASS above); they are NOT rebuilt here.

---

## 4. The physical-clock-admission definition (the missing supplier shape)

N5 closure requires admitting exactly one transfer as "the physical clock" and
declaring all other commuting factor flows non-physical. The
physical-clock-inventory precursor specified the admission as a four-part
firewall; a transfer counts as an admitted physical-clock transfer only if **all
four** checks are met (carried forward verbatim from
`SINGLE_CLOCK_PHYSICAL_CLOCK_ADMISSION_INVENTORY_N5_SUPPORT_NOTE_2026-06-17`):

1. A named source authority supplies the transfer as a physical evolution or
   clock object, not merely as a finite-matrix comparator.
2. The authority supplies positivity / trivial-kernel data sufficient for the
   finite Stone/log construction.
3. The authority supplies the clock denominator or block spacing used by the
   reconstructed generator.
4. The source packet consumes that transfer as the framework evolution clock,
   or explicitly admits it as a second physical-clock transfer.

This definition is not a new axiom or primitive; it is a source-scope firewall
separating admitted physical-clock authorities from arbitrary positive operators
writable on a local tensor factor. Under it, the **only** currently admitted
physical-clock transfer is `{ (T̂², 2 a_τ) }`; the per-mode factor clocks `n_p`
(p ≠ the admitted ray) satisfy checks (1)–(3) on the source surface but FAIL
check (4) — no source packet admits them. R-N5-IRR shows that *which* ray gets
admitted is exactly the `(L_s − 1)`-parameter choice A_min does not fix: the
admission datum is the supplier N5 needs, and it is undischarged.

---

## 5. Named load-bearing wall + authorities

**Wall:** N5 / B-AXIS.3 requires a physical-clock-admission datum — a chosen
positive clock-ray in `span_{≥0}{n_p}` (equivalently a record-order bridge tying
durable outcomes to a unique supplied clock), carrying `(L_s − 1)` undetermined
parameters — that is NOT derivable from Lattice/Quantum/Record. The supplied
`T̂²` is maximally factorized, so no commutant/center argument forces a single
orbit; the factors are not gauge (they escape `span{I, Ĥ}` and produce distinct
durable occupation records `Ĥ` cannot reproduce). A_min + the (R-RP2)/(R-SC2)
surface does not supply this admission ray.

**Authorities cited (recompute-or-retained-no-go only; no load-bearing edge to
the conditional parent keystone / unaudited cone / downstream consumer):**

- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (**retained_no_go**, N5
  checklist) — finite-Stone uniqueness is transfer- and τ-relative; the transfer
  alone cannot exclude an independent commuting second factor.
- `MINIMAL_AXIOMS_2026-06-05` — Record supplies no occupancy rule, no time
  metric, no dynamics; Lattice/Quantum supply no dynamics; record-production
  dynamics is an EXPLICIT OPEN GATE outside axiom content. This is the gate the
  residual relocates to.
- Precursor branches (CITED as precursors only, by path + PASS in §3; NOT
  authorities and NOT rebuilt): `single-clock-n5-factor-boundary-20260617`
  (PASS=34) and `single-clock-physical-clock-inventory-20260617` (PASS=35),
  whose unexplained `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE` /
  `SECOND_PHYSICAL_CLOCK_PROVED=FALSE` are superseded with a source-surface
  reason.

---

## 6. Scope caveats this section must carry

- **Even-extent / finite-block scope.** The `T̂² = ⊗_p diag(1, e^{-2E(p)})`
  factorization is computed on the finite staggered surfaces `L_s=3/m=0.5` and
  `L_s=4/m=0.3`. The `(L_s − 1)`-parameter admission-ray statement is stated for
  the finite spatial-mode count `L_s`; it scales with the surface and is not a
  continuum claim.
- **Surface-specific.** The maximal-`⊗_p` factorization is a property of the free
  diagonal staggered transfer recomputed here; the section claims N5
  non-derivability on this supplied surface, not over all positive operators
  (the prior inventory branch's same scope-honesty caveat).
- **Conditional parent.** The parent theorem 2026-05-03 stays audited_conditional
  with B-AXIS.3 live; this section supplies a sharpened obstruction reason, not a
  status change. Independent audit lane is the sole status authority.

**One line:** the supplied two-step transfer `T̂² = ⊗_p diag(1,e^{-2E(p)})` is
maximally factorized into `L_s` commuting per-mode clocks that are neither
irreducible-excludable nor gauge (they escape `span{I,Ĥ}` and produce distinct
durable occupation records `Ĥ` cannot reproduce, min-dist ≈ 0.40), so N5 stays a
live wall whose closure needs an `(L_s−1)`-parameter physical-clock-admission ray
A_min does not supply — superseding the precursor branches' unexplained
`MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE` with a source-surface reason
(in-tree runner PASS=36 FAIL=0).
