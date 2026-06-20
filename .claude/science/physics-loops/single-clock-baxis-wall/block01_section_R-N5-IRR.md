# Block01 Section — R-N5-IRR (clause N5, no-second-clock)

**Route:** R-N5-IRR
**Clause:** N5 / B-AXIS.3 — "no independent commuting transfer factor is
admitted as a second physical clock."
**Posture:** genuine fresh derivation attempt from A_min (Lattice + Quantum +
Record only), pushing PAST the prior n5-factor-boundary and
physical-clock-inventory branches.
**Runner:** `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py`
**Runner cache:**
`logs/runner-cache/single_clock_n5_irreducibility_factor_clock_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=36 FAIL=0` (deterministic, runtime < 1s,
surfaces L_s=3/m=0.5 and L_s=4/m=0.3).

---

## 1. The exact thing attempted

Prove an irreducibility / nonfactorization theorem for the framework's OWN
supplied two-step transfer: that `T̂²` (the (R-RP2)/(R-SC2) RP/SC two-step
blocked transfer on the staggered surface) admits **no** nontrivial commuting
factor-clock decomposition carrying independent observable clock content — i.e.
that its commutant/center structure FORCES a single one-parameter clock orbit.

If that holds, N5 closes. If the factors are merely **gauge/redundant** (no
independent record-order parameter), N5 also closes. If they carry **independent
observable content**, N5 stays a live wall.

## 2. Why this pushes past the prior branches

Both prior N5 branches built only an **arbitrary** two-qubit tensor product as
a proxy "countermodel" and ended with:

- `single-clock-n5-factor-boundary-20260617`:
  `SECOND_PHYSICAL_CLOCK_PROVED=FALSE`, escape named but unresolved.
- `single-clock-physical-clock-inventory-20260617`:
  `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE`, explicitly *source-inventory,
  not algebraic exclusion*; "not a theorem over all positive operators."

Neither built the **actual supplied `T̂²`**, and neither resolved the
irreducibility / gauge-redundancy question. This route does both.

## 3. The A_min-only method and worked steps

### Block [SURF] — recompute the supplied object from the action-derived data

The supplied transfer, recomputed here from the free staggered dispersion
`E(p) = arcsinh(sqrt(m² + sin²p))` and the second-quantization functor
(both already in-repo, recomputed not cited blind), is

```
    T̂² = Gamma(t1^(2)) = ⊗_p diag(1, e^{-2E(p)}) = exp(-2 a_τ H_hat),
    H_hat = Σ_p E(p) n_p ,   n_p = a_p^† a_p .
```

Verified exactly (resid ≤ 5.6e-17): `T̂² = exp(-2 a_τ H_hat)`; and crucially
`T̂² = ∏_p (lifted per-mode factor)` exactly (resid 0). The per-mode factors
are positive-definite, commute pairwise (resid 0), and their generator tangent
span `{n_p}` has dimension **L_s**, not 1.

**First load-bearing finding:** the SUPPLIED `T̂²` is not merely factorizable —
it is **maximally factorized**, a tensor product of `L_s` independent commuting
per-mode factor clocks. The arbitrary-2-qubit prior countermodel is a strictly
weaker proxy for a structure the real object already exhibits. The naive
irreducibility theorem ("`T̂²` admits no nontrivial commuting factor split") is
therefore **FALSE** on the source surface itself. This is the central
correction this route supplies over the prior branches' framing.

### Block [GAUGE] — closure attempt: are the factor flows gauge/redundant?

A "clock" must be readable by the **Record axiom**: an outcome is the K/CPT
orbit of a realized central sector, and on this diagonal surface the durable
central observables are the simultaneously-diagonal occupations `{n_p}`. The
gauge-collapse hypothesis that would CLOSE N5 is: *the only
record-distinguishable content of any product of factor flows is a function of
the single H_hat-orbit time alone* — equivalently every factor generator
`Σ s_q n_q` lies in `span{ I, H_hat }`.

Computed: for L_s=3 and L_s=4, **all** L_s mode generators lie OUTSIDE
`span{I, H_hat}` (rank grows on adding each `n_q`; `base_rank(I,H_hat)=2`).
Explicitly, the single-mode clock `n_0` is not `c·H_hat + b·I`
(best-fit residual ≈ 0.65–0.67 > 0). The gauge-collapse hypothesis is
**FALSIFIED**: the factor directions are genuinely independent, so N5 cannot be
closed by gauge-redundancy.

### Block [CONTENT] — confirm the independent observable content

Take the framework single clock `H_hat = Σ E(p) n_p` and a second admissible
factor clock `G_alt = n_0` (positive, commutes with `H_hat`, is one of the
supplied tensor factors). Both are legitimate positive transfer generators on
the SAME source surface. Using imaginary-time (positive transfer) propagation
of a fixed diagonal record density:

- The factor clock **freezes** the durable record `<n_1>` (mode 1 untouched)
  while the single H_hat clock **moves** it (init 0.5 → 0.039). A single clock
  cannot freeze `<n_1>` while moving `<n_0>` (both occupations move together at
  ratio E(p_0):E(p_1)).
- **Decisive discriminator:** sweeping the single-clock time `t` over a fine
  grid, NO `t` reproduces the alt clock's durable record pair
  `(<n_0>,<n_1>)` (min distance ≈ 0.40–0.44 > 0). This is relabeling-invariant
  and Record-visible — not a phase Record cannot see.
- The normalized durable **occupation record profile** differs between the two
  clocks (L1 distance ≈ 1.98–2.00).
- Record-compatibility confirmed: the alt-clock record projectors commute, are
  operator-monotone, and scalar readout is additive — so the alt clock is a
  legitimate record-producing flow, not forbidden by Record.

The factor flows carry **independent observable clock content**.

### Block [BRIDGE] — the missing supplier

Collapsing the L_s factor clocks to one requires ADMITTING exactly one positive
ray in `span_{≥0}{n_p}` as "the physical clock" and declaring all others
non-physical. That admission is a **chosen ray in R^{L_s}**, an
`(L_s − 1)`-parameter datum, NOT supplied by A_min:
- Lattice: sites + adjacency, no dynamics, no clock direction.
- Quantum: one-qubit carrier, no dynamics, no clock.
- Record: durable outcomes + finite additivity, **no occupancy rule, no time
  metric, no rule selecting one factor flow as the clock**
  (`MINIMAL_AXIOMS_2026-06-05.md`, Record exclusions).

Two distinct admissible rays (mode-0 clock vs uniform clock) give
non-conjugate, record-distinguishable clocks (generators differ by ≈ 1.15–1.50).

## 4. Honest OUTCOME

**N5 is NOT cracked. It is sharpened into a live wall on its own source
surface.**

- The naive irreducibility theorem is FALSE: the supplied `T̂²` is maximally
  factorized into L_s commuting per-mode clocks.
- The gauge-redundancy closure FAILS: the factor directions escape
  `span{I,H_hat}` and produce distinct durable records.
- Therefore A_min + the supplied (R-RP2)/(R-SC2) surface does **not** exclude an
  independent commuting second clock. Exclusion requires an extra
  **physical-clock-admission** bridge (a chosen positive clock-ray /
  record-order rule) that the minimal axioms do not supply.

This is a NEGATIVE BOUNDARY result anchored on the real object — stronger and
more honest than the prior proxy-only branches, which left
`MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE` unexplained. The residual
relocates to the **record-production / emergent-dynamics OPEN GATE** of the
minimal axioms (explicit open gates per `MINIMAL_AXIOMS_2026-06-05.md`: Record
supplies no occupancy rule, no dynamics, no time metric).

## 5. Named load-bearing wall + authority

**Wall:** N5 / B-AXIS.3 requires a **physical-clock-admission datum** (a chosen
positive clock-ray in `span_{≥0}{n_p}`, equivalently a record-order bridge
tying durable outcomes to a unique supplied clock) that is NOT derivable from
Lattice/Quantum/Record. The supplied `T̂²` is maximally factorized, so no
commutant/center argument forces a single orbit.

**Retained authorities the wall rests on:**
- `MINIMAL_AXIOMS_2026-06-05.md` — Record supplies no occupancy rule, no time
  metric, no dynamics; Lattice/Quantum supply no dynamics; record-production
  dynamics is an EXPLICIT OPEN GATE outside axiom content.
- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (retained_no_go) — N5
  checklist; finite-Stone uniqueness is transfer- and τ-relative.
- `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md` —
  supplies the exact B-AXIS.3 / N5 target wording and the `(T̂², 2a_τ)` supply;
  its block [C-2CLK] already states a two-clock comparator "exists
  mathematically … excluded only by (B-AXIS.3)". This route confirms the
  comparator is realized by `T̂²` ITSELF (per-mode factors), not just an
  abstract tensor product.

**Source discipline:** all load-bearing facts (E(p), the `⊗_p` factorization,
the `exp(-2a_τH_hat)` identity, the record discriminators) recomputed in the
runner; nothing cited blind from the conditional parent keystone.

## 6. What the consolidated no-go should carry (for N1 / N7)

1. **N5 is now anchored on the source surface, not a proxy.** The supplied `T̂²`
   is `⊗_p diag(1, e^{-2E(p)})` — maximally factorized into L_s commuting
   per-mode clocks. Drop any framing that N5's countermodel is a "foreign"
   tensor product; it is the real object's own structure.
2. **The naive irreducibility route is CLOSED-as-FALSE** (cannot supply N5): no
   commutant/center argument forces one orbit, because the supplied transfer is
   maximally reducible.
3. **The gauge-redundancy route is FALSIFIED** (cannot supply N5): factor
   generators escape `span{I,H_hat}`; factor flows produce distinct durable
   occupation records that no single H_hat orbit reproduces (Record-visible,
   relabeling-invariant discriminator, min-distance ≈ 0.40 over a swept t).
4. **The exact missing supplier** is a physical-clock-admission ray
   (`(L_s−1)`-parameter undetermined content), relocating N5 to the
   record-production / emergent-dynamics OPEN GATE — consistent with the N5
   entries in `NO_GO_LEDGER.md` but now backed by the source-surface computation
   rather than the arbitrary 2-qubit proxy.

**One line:** R-N5-IRR built the actual supplied `T̂² = ⊗_p diag(1,e^{-2E(p)})`
and showed it is maximally factorized into L_s commuting per-mode clocks whose
factor flows are neither excludable by irreducibility (the transfer is maximally
reducible) nor dismissible as gauge (they escape span{I,H_hat} and produce
distinct durable occupation records H_hat cannot reproduce) — so N5 stays a live
wall whose closure needs a physical-clock-admission ray that A_min does not
supply; runner PASS=36 FAIL=0.
