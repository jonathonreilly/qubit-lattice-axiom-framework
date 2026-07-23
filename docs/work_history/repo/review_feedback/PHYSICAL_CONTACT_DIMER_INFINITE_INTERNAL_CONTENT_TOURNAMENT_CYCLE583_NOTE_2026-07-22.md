# Physical contact-dimer infinite/internal-content tournament — Cycle 583

Date: 2026-07-22

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, PR-control, or audit-status
surface.

Runner:

`scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py`

## Result up front

Cycle 583 gives the Cycle-578 contact-bound dimer its exact finite-rank
spectral equation and locates the precise boundary of the current
infinite-volume argument.

1. **Route A — exact contact reduction.** At fixed total momentum `K=0`, the
   free relative two-CAR fiber is the `36 by 36` matrix
   `F(p)=D(p)(C tensor C)`. The onsite antisymmetric contact space has dimension
   15. The literal Cycle-230 update therefore obeys the exact 15 by 15
   Birman–Schwinger equation

   ```text
   B_L(z) = I_15 - z (exp(-i g)-1)
                    L^-3 sum_p J_2^dagger (F(p)-z I)^-1 J_2.
   ```

   The proper-cubic `A2` contact sector is rank one. Frozen L11/L15/L19/L23/
   L27/L31 roots converge rapidly toward wrapped phase
   `-2.975575990912`, with the exact finite-sum residuals reported by the
   runner. This finite/BIC-like symmetry-channel candidate is the strongest
   constructive result; it is not yet an infinite-volume theorem.
2. **The infinite-volume boundary is explicit.** The candidate wrapped phase
   lies on the full free spectrum: an explicitly retained momentum has an
   on-shell free vector to numerical residual below `1e-12`. That on-shell
   vector is dark to the `A2` contact source. Sampled L9/L13/L17/L21 grids show
   a positive contact-cyclic gap near `0.064`, and the L31 inverse Fourier
   candidate has stable finite localization diagnostics. But the full free
   spectrum touches the pole phase, so an ordinary full-spectrum gap or
   Combes–Thomas argument is unavailable. The exact unfinished lemma is to
   prove a uniform continuous-torus contact-cyclic cancellation/reducing
   structure and prove that it survives exponential spatial weighting. The
   **infinite-volume isolated-pole and exponential-tail theorem remains open**.
3. **Route B — internal irrep search.** The onsite two-CAR decomposition is
   `A2 + E + 3 T1 + T2`. A frozen fixed-window search finds a pure `T2`
   contact-active finite-box candidate and a nonzero component-local `A2-T2`
   transition matrix element. Its proper-cubic observable orbit is covariant.
   The candidate fails the frozen held localization bounds as volume grows;
   therefore this family does not certify a second co-moving localized branch.
   This is a route-specific held certification failure, not a second-mode
   absence theorem.
4. **Route C — three-CAR scout.** The exact translation-quotiented three-CAR
   code and contact-last free update are constructed on L3 train and L5 held
   boxes. The onsite decomposition is `A1 + A2 + 3 T1 + 3 T2`. Forward,
   inverse, antisymmetric-projection, deletion, lawful-domain, and held-size
   controls and the L3 A1/A2 seed-update covariance test under all 24 frames
   pass. Under the global `360 s / 3 GiB maximum-RSS` cap, rank-one `A1/A2`
   Arnoldi scouts do not produce a held isolated Ritz mode. `T1/T2`, deeper
   Krylov, finite-rank three-body resolvents, and larger CAR sectors remain
   open. This scout cannot support a three-CAR absence claim.

There is no route-independent obstruction, no minimum-content conclusion, no
shared-substrate no-go, and no axiom pressure.

## Frozen contract

```text
beta = -0.3
g = 0.37
total momentum K = 0 for the contact resolvent and irrep classification

Route A finite sums: L11/L15/L19/L23/L27/L31
Route A contact-cyclic diagnostic grids: L9/L13/L17/L21
Route A all24 proper-cubic A2 source test

Route B train: L7
Route B held:  L9/L11
fixed eigensolver window: sigma = 0.999 exp(-3.0 i), k=16, ncv=33
selection: maximum contact weight among onsite-T2 weight > 0.999
moving label check: K_x = 2 pi / 127, overlap continuation
localization thresholds: contact > 0.15, r^2 < 8, seam < 0.15

Route C train: L3, Arnoldi m=80, onsite A1/A2 seeds
Route C held:  L5, Arnoldi m=45, onsite A1/A2 seeds
held Ritz certification: residual < 1e-6 and modulus residual < 1e-6
T1/T2 deeper scan: open under cap

tolerance = 5e-9
cold caps = 360 seconds / 3 GiB maximum resident set
external peak-memory-footprint metric = separately disclosed, not conflated with RSS
```

The finite root phases were frozen after reconnaissance and are independently
tested by substituting them into the full finite sums. No held threshold or
root is refit by this definitive run.

## Definitive cold verification

The accepted cold run returned `15/15` checks with no failure.

```text
internal elapsed:                 79.23240337497555 seconds
external wall:                    80.06 seconds
internal/external maximum RSS:    1,850,359,808 bytes
external peak memory footprint:   2,678,671,832 bytes
swaps:                            0
runner SHA-256:                   3f1672ef0d2c0063d5760a6b0885d75cb75b63c64b44951399fd0762d5499f7f
cold transcript SHA-256:          738ecc5e35ad9cecb8db197750834dd3f314b4ded55d6c926e81bc596586e84d
```

Maximum resident set and peak memory footprint are separate metrics; neither
is substituted for the other. Both happen to be below 3 GiB in this accepted
run. Earlier over-cap attempts were rejected and overwritten by the accepted
bounded transcript; they are not evidence rows.

Independent parent verification reran the frozen command after the worker
finished. It returned `RESULT pass=15 fail=0` in `81.81 s` external wall time
with `2,342,502,400` bytes maximum resident set, `3,965,128,160` bytes peak
memory footprint, and `0` swaps. The independent transcript SHA-256 is
`2be2819280de205e14012b00885b1cd4c0b2014f2ac3882da2cd3ce554309b2b`.
The declared cap is on maximum resident set, not the separately reported peak
memory-footprint metric; the independent maximum RSS remains below 3 GiB.

## Exact retained shore

Accepted Cycle-578 commit
`d63ed6fe0d78401c83f52019e217bdd2b5ffb7e8` must be an ancestor of HEAD;
branch-head equality is not a scientific dependency.

| artifact | SHA-256 |
|---|---|
| Cycle219 runner | `ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a` |
| Cycle230 runner | `b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae` |
| Cycle563 runner | `444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b` |
| Cycle569 runner | `c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced` |
| Cycle578 runner | `25806853483a822b86dd55c50ebedb7957395151ef262317110b348c6931b9ab` |
| Cycle578 receipt | `c7af39acc2fe365e317297c7fe0cead00fad125145dec72c61d8d2da151b435c` |
| Cycle578 note | `50cc6d4fc07d5b730d6d9cce5e2fbab6928d5c10caf242109bc07eed2bd0ec5d` |

The Cycle-578 receipt carries the retained physical-M2 one-particle mass,
Cycle-230 contact-factorization, and seam-braid residuals. Cycle 583 reads and
gates them but changes none of their laws.

## Route A derivation and unfinished lemma

Let `P=J_2 J_2^dagger` be the onsite antisymmetric contact projector and

```text
W_g = I + (exp(i g)-1) P,
G = W_g F.
```

For `G psi = z psi`, multiply by `W_g^-1` and rearrange:

```text
(F-z) psi = z (exp(-i g)-1) P psi.
```

With `eta=J_2^dagger psi`, elimination of the free 36-component fiber gives
the displayed 15-dimensional Birman–Schwinger equation. This is an exact
finite-rank reduction of the literal free-plus-contact CAR law, not a fitted
effective Hamiltonian.

The onsite proper-cubic ranks are:

```text
A1: 0, A2: 1, E: 2, T1: 9, T2: 3.
```

The Cycle-578 bound state is the one-dimensional `A2` pole. Its finite-volume
phase convergence is strong evidence that the contact equation has a stable
limit. It is not yet a proof of an isolated infinite-volume eigenvector.

The decisive caveat is constructive rather than rhetorical. At the limiting
phase, the full free matrix has on-shell vectors. The located on-shell vectors
have negligible overlap with the `A2` contact source, and sampled fibers keep
the contact-coupled bands separated. A proof must promote that observation to
a continuous-torus statement and then control exponential spatial weights.
The contact-cyclic subspace can depend on momentum, so spatial weighting may
recouple nominally dark content. Until that is discharged, neither an ordinary
resolvent-gap theorem nor an exponential-tail theorem ships.

## Route B disposition

The `T2` window tests a concrete second internal representation, rather than
relabeling the existing `A2` mode. In each finite box the runner checks:

- the eigen residual and onsite irrep weight;
- contact, radius-squared, and seam weight;
- overlap continuation at the nonzero total-momentum label;
- a component-local observable cross term with the `A2` state;
- the all24 covariant orbit of that component observable.

The fully invariant onsite contact projector cannot connect inequivalent
`A2` and `T2` irreps, and its cross term vanishes as it should. A direction-
resolved onsite component has a nonzero cross term and transforms in a
proper-cubic orbit. Thus the local-observable ingredient exists in finite
boxes. The held localization ingredient does not. A group displacement is not
a rate, and no moving-label phase response is called a transition rate.

## Route C disposition

For three identical CAR excitations, use relative coordinates
`r1=x1-x3`, `r2=x2-x3`. Particle permutations change both the chosen anchor
and the ordered directions. The sparse quotient sums every `S3` orbit with
fermionic sign, rejects stabilizers with zero antisymmetric content, and tests
`Q^dagger Q=I`.

The free stream is literal:

```text
r1 -> r1 + v1-v3,
r2 -> r2 + v2-v3.
```

The local contact-last phase is

```text
exp(i g [1_(r1=0) + 1_(r2=0) + 1_(r1=r2)]).
```

This supplies three pair contacts at triple coincidence. It is the direct
three-particle lift of the supplied pair contact, not a new fitted three-body
law. The A1/A2 Krylov result is only a bounded scout: a large Ritz residual is
unfinished numerical resolution, not evidence that an eigenmode does not
exist.

## Interpretation firewall

- Wrapped phase is not energy.
- Group displacement is not a rate.
- Update schedule is not time.
- Contact weight is not Born probability.
- A CAR-fiber result is not a physical-M2 compiler.
- A finite grid contact-cyclic gap is not an infinite-volume theorem.
- Source coupling is not gravity.
- Candidate occurrence is not a Record.

No Record, realized history, Born law, physical duration, energy calibration,
gravity source, or backreaction is derived here.

## Supplied, derived, and open

Supplied:

- the byte-pinned Cycle-219/230/563/569/578 shore;
- six CAR directions, `beta=-0.3`, and the local even contact `g=0.37`;
- odd periodic boxes, root list, eigensolver window, overlap threshold, Krylov
  depths, and resource caps;
- noiseless arithmetic and exact CAR constraint enforcement.

Derived:

- the exact finite 15 by 15 contact resolvent equation;
- small substituted pole residuals through L31 and rapid phase convergence;
- rank-one proper-cubic `A2` pole content;
- explicit full-spectrum touch and source-dark on-shell content;
- the finite L31 tail diagnostic and sampled contact-cyclic gap;
- a finite pure-`T2` candidate with nonzero component-local cross term;
- exact L3/L5 three-CAR quotients, reversible updates, and controls.

Open:

- the continuous-torus contact-cyclic cancellation/reducing lemma;
- exponential weighting, infinite-volume isolated pole, and tail theorem;
- a second held co-moving localized internal mode;
- three-CAR `T1/T2`, deeper resolvents, and larger contact sectors;
- any bounded physical-M2 compiler for the CAR object;
- unbounded renewal, empirical calibration, gravity/source/backreaction,
Record actuality, and Born probability.

## TOE dependency ledger and maturity

| wall | Cycle-583 movement | residual |
|---|---|---|
| `C_ref` | one finite-volume `A2` contact reference gains an exact finite-rank equation | second held internal reference remains open |
| `C_num` | finite pole residuals, convergence, and contact-cyclic diagnostics sharpen the numerical shore | no empirical scale or physical duration |
| `C_wrap` | unchanged | no renewal or unbounded noisy recurrence result |
| `C_int` | actual contact mechanism and cubic irrep content are substantially sharper | continuous pole/localization lemma remains open |
| `C_local` | exact two-/three-CAR quotient updates | no bounded physical-M2 object compiler |
| `C_source` | `g=0.37` remains an explicit supplied contact strength | no stress, gravity, redshift, or backreaction |

The carried global maturity coordinates remain unchanged; this finite CAR
spectral partial does not regrade lane closure:

| lane | repo-wide evidence | strict-M2 evidence | Cycle-583 delta |
|---|---:|---:|---|
| operational quantum / Records | `96/100 (4.80/5)` | `93/100 (4.65/5)` | exact CAR spectral/quotient controls; actuality unchanged |
| causal time | `79/100 (3.95/5)` | `76/100 (3.80/5)` | no physical time result |
| inertia / matter | `94/100 (4.70/5)` | `97/100 (4.85/5)` | strongest delta: exact contact pole equation; infinite theorem open |
| gravity / source | `82/100 (4.10/5)` | `77/100 (3.85/5)` | unchanged |
| Born / probability | `84/100 (4.20/5)` | `73/100 (3.65/5)` | contact weights remain diagnostics |

These are evidence-planning coordinates, not probabilities, audit grades, or
constitutional status.

## Fresh N1–N8 no-go discipline

The latest `origin/main` no-go-discipline and proof-search-governance texts
were read completely before packaging this result.

### N1 — normalized alternatives

Eight normalized constructive families are recorded: finite two-CAR
resolvent, continuous-torus contact-cyclic proof, T2 branch, three-CAR A1/A2,
three-CAR T1/T2, four-plus CAR, alternate even contacts, and a physical-M2
gauge compiler. Only the held T2 certification and bounded A1/A2 three-CAR
scout qualify as attempted negative families. `2 < 5`, so N1 fails. No absence,
no-go, minimum-content, shared-obstruction, or axiom-pressure claim can ship.

### N2 — wall independence

All 15 unordered pairs among `C_ref`, `C_num`, `C_wrap`, `C_int`, `C_local`,
and `C_source` receive both directional implications in the receipt. A second
localized irrep does not entail calibration; calibration does not entail it.
The continuous contact pole lemma does not entail a physical-M2 compiler; a
compiler does not prove the pole lemma. Renewal and gravity each require
separate mechanisms.

### N3 — hidden-wall scan

The runner exposes the coin, contact strength, periodic boxes, root list,
spectral/Krylov windows, overlap threshold, and noiseless exact arithmetic.
The root list is reconnaissance-supplied and residual-tested, not derived by a
certified interval root proof.

### N4 — residual matching

Cycle-219 mass and Cycle-230 contact/seam fixtures are byte-pinned through the
Cycle-578 receipt. The new two-/three-CAR objects use the literal accepted
coin and contact phase. A CAR-fiber statement is never substituted for the
separate physical-M2 compiler obligation.

### N5 — resolution audit

Route A uses finite sums through L31 plus finite contact-cyclic grids. Route B
uses L7 train and L9/L11 held fixed windows. Route C uses only L3/L5 and
A1/A2 Krylov blocks. Continuous volume, deeper Krylov, T1/T2, and physical-M2
layout remain named.

### N6 — partial-closure paths

The next constructive paths are: prove the contact-cyclic continuous lemma;
prove stability under exponential weighting; create a branch-aware T2 volume
embedding; build three-CAR T1/T2 finite-rank contact resolvents; search larger
CAR clusters; and independently compile any retained object into bounded M2
neighborhoods.

### N7 — hostile steelman

Concrete mechanism: the onsite rank-one `A2` contact source produces an exact
15-dimensional finite-volume Birman–Schwinger equation and rapidly converging
pole phase. Terminal obligation: because the full free spectrum touches that
phase, a hostile reviewer must reject an ordinary spectral-gap or
Combes–Thomas proof until continuous contact-cyclic cancellation stable under
exponential weighting is proved. The finite T2 cross term and exact three-CAR
quotient keep second-mode routes open; the held tests presently do not certify
them.

### N8 — cross-cycle echo

Cycle 219 supplied the massive proper-cubic walk. Cycle 230 supplied intrinsic
CAR and onsite even contact but no physical-site compiler. Cycles 563/569
retained the physical-M2 mass/contact/seam shore. Cycle 578 found the finite
contact-bound dispersive dimer. Cycle 583 exposes its finite-rank resolvent and
the exact full-spectrum-touch boundary while scouting, not excluding,
internal multiplicity.

## Terminal disposition and next campaign

The strongest result is the exact finite-rank contact equation plus L11–L31
pole convergence and proper-cubic `A2` identification. The infinite theorem is
not blocked by evidence of absence; it is blocked by one explicit unfinished
lemma at an embedded/source-dark spectral point.

The optimal next campaign is to prove the continuous-`T3` contact-cyclic
cancellation/reducing lemma with exponential weighting. In parallel, formulate
a branch-aware T2 or three-CAR finite-rank contact resolvent so the internal-
mode search stops depending on boxwise fixed-window eigenvector selection.

There is no axiom pressure.
