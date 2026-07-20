# Cycle 513 — Route-C Q6 generic factor-growth attempt-1 failure

Date: 2026-07-20

Authority: **none**

Audit: **unset**

Status: **dry local certificate positive; one authorized factor-growth attempt
failed closed at an under-instrumented axis-1 compound fixture gate; no
update-3 science result**

## Result up front

Cycle 513 produced a meaningful local algebra certificate and then exposed an
under-instrumented compound contract mismatch before an all-axis update-3
result existed.

The clean dry contract passed `9/9`.  On the complete lawful local domain it
reconstructed all `2,794` matter-`N<=2`, mediator-`Q<=6` states, including all
`24` size-four components.  The full local unitary has `64` nonzero matter
matrix blocks and `3,850` nonzero entries; `K=U-I` has `60` blocks and `1,920`
entries.  The exact 61-term structural product reconstructs the component
exponentials with maximum residual `6.938893903907228e-18`, and its forward /
inverse residual is `2.220446049250313e-16`.  Numerical operator-Schmidt ranks
are `1/12/49/61` in the `N=0`, `N=1`, `N=2`, and combined sectors at each of
the relative cutoffs `1e-10`, `1e-12`, and `1e-14`.  This local certificate
uses no global amplitude, response, held, deletion, selector, or refit path.

The one hash-bound factor-growth invocation then exited `1` with

```text
RuntimeError: axis1 frozen prefix or geometry equivalence failed
```

after `63.70 s`, with `159,645,696` bytes maximum RSS and zero swaps.  The
runner failed before axis-1 generic factor growth.  Its top-level exception
handler discarded the completed axis-0 component row and the individual
axis-1 predicate values, so no all-axis `461`-descriptor result, update-3
word, response, or other physics result is retained.

The attempt establishes only an under-instrumented compound-gate failure.  It
does not establish a proper-cubic covariance failure, compiler no-go,
resource obstruction, substrate obstruction, minimum-content result, or
source of axiom pressure.  The consumed runner is not rerun.

## Frozen evidence

| artifact | SHA-256 |
|---|---|
| Cycle-513 runner | `84ccd28c0ef428a851d0f9328ba7988c13a59ac1627d218e1ca9b9ee0b01a297` |
| clean dry transcript | `e6c92ffb2158230afcb755bc7ad987c25f0eefa83aa444eb4bcbd5c3566fb762` |
| authorized attempt-1 transcript | `e4ac928931cdd77445a690e767b64e56b70118f12a467e667c8c3e5fc35d5cd7` |
| typed attempt-1 receipt | `fbae7dfced0ace45d490651dc4a36c5018743be91ac0792df8651d2f03a68fd3` |

The typed receipt binds the Cycle-512 runner, raw transcript, typed receipt,
and note at their packaged hashes.  The attempt transcript contains no
authorization token.  One authorized invocation was consumed; retry under
the old Cycle-513 integrity contract is false.

## Exact local certificate and representation boundary

The lawful local component census is:

| component size | components | source states |
|---:|---:|---:|
| `1` | `1,930` | `1,930` |
| `2` | `384` | `768` |
| `4` | `24` | `96` |

The three commuting axis exponentials give an exact structural ceiling

```text
1 + 3*4 + C(3,2)*4^2 = 61
```

because every term nonidentity on all three axes annihilates the global
`N<=2` sector.  This is an algebraic product-term construction, not numerical
truncation and not a propagated-state Schmidt rank.

The separate `581` count is the compact D/X matter-support-only upper
`sum_j(1+2 C_j+4 P_j)` before mediator two-cell compatibility and exact-zero
filtering.  It is not an upper on arbitrary decompositions.  The runner's
`461` count is only the frozen unmerged descriptor forecast for its chosen
generic `K=U-I` matrix-unit representation.  It is neither minimal nor
canonical and was not established on all axes.  The earlier `453` helper was
unpreserved and unreconciled and is not evidence.

No additional global parity service is used by the even local numerical
update.  This does **not** close the physical parity/superselection compiler,
the complete physical-M2 compiler, or the framework locality wall.

## Proven attempt-1 facts

The transcript and typed receipt establish only:

1. process exit `1` and status `fail-closed-exception`;
2. the axis-1 combined frozen-prefix-or-geometry error above;
3. `63.70 s` real, `62.13 s` user, `0.46 s` system;
4. maximum RSS `159,645,696` bytes and zero swaps;
5. zero science, response, held, and deletion rows;
6. zero response values, occupation/bond fields, and state hashes;
7. selector and refit false;
8. no packed joint state or dense X/Y construction; and
9. no post-collision update-3 mediator stream or joint Schmidt core/rank.

Because the axes execute sequentially, reaching the axis-1 compound gate
implies that axis 0 returned past its prefix, geometry, factor-growth, and
sparse-Gram checks.  That is only a control-flow implication.  The component
row and residuals were discarded by the exception path and are not retained
quantitative science evidence.  Axis-1 factor growth never ran.

## Strongest diagnosis — explicitly unproven

The strongest current cause is an axis-0-derived machine-exact floating
support fixture applied as if it were a proper-cubic invariant.  In
particular, the frozen update-3 row includes
`sum(value != 0j)` after another coin/stream/contact word.  Canonical-mode
permutations change dictionary insertion and floating accumulation order, so
algebraically cancelling coefficients can be exactly `0j` on one axis and a
tiny nonzero residue on another while the represented states agree within
roundoff.

This cause is not proved because the runner collapsed roughly ten prefix and
geometry predicates into one exception and emitted neither the observed
axis-1 row nor a touched-set witness.  A genuine stored-support, omitted-shell,
per-label ordering, or CAR-frame defect remains live until a witness-level
diagnostic separates those predicates.

Cycle 512's all-axis update-2 factor-versus-packed residuals
`4.154678936338152e-20`, `4.41011352369794e-20`, and
`4.6515383332589104e-20` and its rank-nine spectra favor the
fixture/representation diagnosis.  An independent all-axis `C_j/P_j`
geometry helper agreed during working analysis, but it was not preserved or
hash-bound and is not evidence.  Neither surface substitutes for the missing
Cycle-513 axis-1 witness.

The same issue means that `461`, the factor-entry totals, and the Gram-work
ceilings derived from them cannot be frozen as all-axis gates.  They are
axis-0 representation forecasts until independently observed.  A revision
must compute descriptor counts, sparse entries, and row-multiplicity work
dynamically against conservative resource caps.

## Supplied, derived, and open

Supplied:

1. the complete packaged Cycle-512 prefix and its frozen Route-C Q6 apparatus;
2. the Cycle-219 coin, Cycle-230 contact, Cycle-501 collision, emitter angle,
   open L15 geometry, Q6 preparation, and update order;
3. the local matrix-unit representation, numeric cutoffs, and resource caps;
4. the compact D/X support ledger and fixed 18-cell compiler optimization; and
5. the inherited single resource-scout authorization and exact Cycle-513
   runner integrity hash.

Derived in the clean dry contract:

1. the complete local component, branch, full-U, and `K=U-I` censuses;
2. the exact 61-term structural reconstruction and local inverse;
3. stable numerical local operator-Schmidt ranks at three cutoffs;
4. local collision-generator and shell-set proper-cubic covariance; and
5. strict authorization, quarantine, and resource contracts.

Open after attempt 1:

1. the exact failing axis-1 subpredicate;
2. an exact symbolic update-3 support oracle for all nine branches;
3. frame-transported sparse amplitude comparison with CAR signs;
4. all-axis generic descriptor, sparse-entry, and Gram-work ledgers;
5. the post-collision update-3 mediator stream;
6. forward/reverse cell-order equality and full update-3 inverse;
7. the 72 state-orbit cases, joint Schmidt core/rank, depth five, and response;
8. Route-C train/deletions, atomic held evaluation, and source-law selection;
9. the physical parity/superselection and arbitrary-volume M2 compiler; and
10. time, conserved energy/stress/source, gravity calibration, Born law, and
    realized-history selection.

## Six-wall and TOE-lane effect

| wall | Cycle-513 movement | residual |
|---|---|---|
| `C_ref` | none | preparation and law selection remain supplied |
| `C_num` | local rank sensitivity and full matrix-block census sharpen the numerical representation | machine-exact zero counts are not physical covariance invariants; number/probability meaning is unchanged |
| `C_wrap` | none | update order is not time, rate, synchronization, or proper time |
| `C_int` | the generic local collision is constructive on the complete lawful local domain | no all-axis third update, interaction selection, rate, or protection result |
| `C_local` | the local algebra and bounded shell optimization are sharper | the attempted global factor-growth continuation failed before axis-1 growth; the physical compiler remains open |
| `C_source` | none | no conserved source/stress or gravity coupling follows |

Cycle 513 itself makes no TOE maturity-score change.  The last score triples
printed in a packaged repo note were Cycle 511's
`90/49/99, 65/40/99, 80/42/99, 59/30/94, 76/44/99`.  After the packaged
Cycle-512 update-2 result, the campaign-level planning update—not a retained
or audited claim—revised those estimates to `91/50/99, 65/40/99, 81/43/99,
61/32/94, 76/44/99`.  This failed Cycle-513 attempt changes neither ledger.
Each triple is integrated / strict / conditional planning maturity, not
probability or audit status.

## N1–N8 no-go discipline

### N1 — normalized alternatives

Live routes include per-axis structural fixtures, extension of the exact
cyclotomic/contact-tag support oracle, frame-transported sparse-state
comparison, retain-all-stored-key evolution, grouped analytic D/X factors,
generic matrix-unit factors, coherent DAG/tensor-network evolution, and
out-of-core sparse aggregation.  One compound failure does not exhaust them.

### N2 — wall independence

The failed gate merges machine-zero representation, stored support, prefix
replay, shell geometry, and carried-frame obligations.  It neither isolates
one wall nor connects failures across direct, gauge/auxiliary, and staggered
compiler families.

### N3 — hidden-condition scan

The hidden conditions are the axis-0-only exact-zero fixtures, floating
accumulation order, discarded partial telemetry, CAR relabel signs, per-label
ordering, and the distinction among structural support, stored keys, and
machine nonzeros.

### N4 — residual matching

No individual predicate residual or symmetric difference survived the
exception.  Therefore neither a geometry residual nor a covariance residual
is matched by the transcript.

### N5 — rhetoric and resolution

The licensed statement is: **axis 1 failed a combined frozen-prefix-or-geometry
fixture before factor growth**.  “Proper-cubic covariance failed,” “the
compiler failed,” “depth five is impossible,” and any broader negative are
forbidden.

### N6 — partial closure paths

The local 2,794-state certificate and all Cycle-512 update-2 evidence remain
intact.  A predicate-level diagnostic can retire the instrumentation wall
without changing the physical law or axioms.

### N7 — hostile steelman

A genuine omitted-shell or CAR-frame-sign defect remains possible.  It must
be tested by actual/expected touched-set differences, first omitted-cell
witnesses, exact frame maps, and transported-amplitude residuals rather than
assumed away from the likely floating explanation.

### N8 — cross-cycle echo

Cycle 512 passed all three axes and the local Cycle-513 certificate is
proper-cubic.  The new failure has no route-independent cross-cycle echo.  It
adds a diagnostics-quality obligation, not constitutional evidence.

Broad no-go: **FAIL**.  Minimum-content claim: **FAIL**.  Shared substrate
obstruction: **FAIL**.  Axiom pressure: **FAIL**.

## Exact next contract

The next runner must be newly hash-bound and must not reuse or retry the
Cycle-513 invocation.  Before any growth it must:

1. persist every prefix and geometry predicate separately for all three axes;
2. report stored keys, exact symbolic support, machine-exact zeros, and
   below-cutoff norm only as distinct quantities;
3. extend the Cycle-512 exact `Q(zeta_9)[z]` contact-tag support oracle through
   update 3 for every structural branch, explicitly representing the
   emitter/collision sine and cosine factors and distinguishing global
   nonzero prefactors from cancellations across a branch sum;
4. emit actual/expected touched sets, symmetric differences, first omitted
   witness, and per-label `C_j/P_j` rows;
5. compare frame-transported sparse amplitudes with the correct exterior-CAR
   signs and a declared residual;
6. preserve typed partial-axis evidence before any failure;
7. derive descriptor, nonzero-entry, and `sum_row k_row^2` work dynamically
   and compare them only with independently reviewed conservative caps; and
8. keep final mediator stream, joint rank, inverse/order/orbit, depth five,
   response, deletion, train, and held paths closed.

Only after that diagnostic contract passes may a separately reviewed bounded
growth invocation be considered.  A failure of that representation remains
route-local unless the full three-route and N1–N8 obligations are satisfied.

Cycle 513 consumed one bounded authorization and failed safely at an
under-instrumented axis-1 contract gate; it changes neither physics maturity
nor axioms and licenses only a better diagnostics contract.
