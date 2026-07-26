# Cycle 710 — V1–V5 Promotion Value Gate and N1–N8 No-Go Discipline Gate

Block: `physics-loop/poisson-response-kernel-diagnostic-20260726`
Deliverable: `docs/POISSON_SELF_CONSISTENCY_BOTH_OPERATOR_DISCRIMINATORS_ARE_ARTIFACTS_ON_THE_TESTED_CONSTRUCTION_DEMOTION_NOTE_2026-07-26.md`
Runner: `scripts/physical_poisson_response_kernel_sign_indefinite_cycle710_2026_07_26.py` (13 PASS / 0 FAIL)

## V1–V5 Promotion Value Gate

**V1 — What specific verdict-identified obstruction does this PR close?**
Verbatim from the parent row's `notes_for_re_audit_if_any`:

> "missing_bridge_theorem: compare susceptibility with the matched
> point-to-point inverse-Laplacian kernel, normalize alternative-operator
> source signs consistently, and revise the note to the resulting finite
> numerical scope before re-audit."

and from `chain_closure_explanation`:

> "it does not establish that the transfer propagator's response kernel is the
> inverse graph Laplacian. Its susceptibility scalar is correlated with the
> domain-integrated Green-function norm for sources moved toward the boundary,
> rather than with a matched point-to-point Poisson profile."

Both named computations are performed (Part A = matched point-to-point kernel;
Part C = per-operator source-sign normalization) and the resulting scope is
stated. This is a derivation-gap obstruction on the parent row itself, not a
dependency-chain complaint about an unratified upstream. **PASS.**

**V2 — What new derivation does this PR contain that the audit lane doesn't
already have?**
The audit lane named two computations and did not run them; it recorded the
`r^(-2.805)` exponent as an inconsistency but did not identify the mechanism or
test the consequence. New content:

1. The obstruction is a **sign structure**, not a normalization or a
   boundary-proximity effect. The inverse Dirichlet graph Laplacian is
   single-signed (max principle, verified R2); the propagator's density response
   kernel is sign-indefinite with 70–78% of interior sites negative (R3). No
   scalar multiple can connect them, and R4 confirms this by least squares
   (residual 0.9987–0.9996) rather than by argument.
2. The matched comparison the audit lane asked for yields `corr = -0.06` where
   the parent note reports `0.93`.
3. The mismatch is not a regime artifact: it survives four decades of coupling
   `k` in `[0.05, 10]` (R5), which is the steelman for the parent note.
4. The obvious repair is **falsified**: removing the per-layer renormalization
   does not restore the match (R6). The cause is that the field enters only as a
   phase, so the response is an interference kernel either way.
5. Quantified discriminating power of the parent statistic: on the parent note's
   own radii a 0.93 Pearson threshold admits every exponent up to `4.57`,
   including the `2.805` in the verdict rationale and (within 0.013) the `8.637`
   of the operator the parent note calls unphysical (R9).
6. **The operator ranking inverts.** Under the sign normalization the audit lane
   asked for, Poisson ranks third of four by `abs(beta-1)` at both N=20 and
   N=24, behind biharmonic and the `1/r^2` kernel, with all four attractive and
   monotone throughout the interior (R11, R12). The audit lane flagged the sign
   comparison as "convention-dependent"; it did not establish that correcting
   the convention reverses the note's conclusion. **PASS.**

**V3 — Could the audit lane already complete this from existing primitives plus
standard math machinery?**
No. The single-signedness of the inverse Dirichlet Laplacian is standard (max
principle) and is not the new part. The new part requires actually running the
repo's propagator: the sign structure of `d rho / d phi`, its behaviour across
`k`, its behaviour with the renormalization removed, and the sign-normalized
`beta` ranking are all outputs of this specific construction and are not
derivable from general machinery. Nothing in the framework's axioms is
load-bearing here either — this is a diagnostic-correctness result about a
runner, which is why the deliverable is a demotion packet and not a theorem.
**PASS.**

**V4 — Is the marginal content non-trivial?**
Yes. The strongest single item is that correcting the convention the audit lane
had already flagged as suspect does not merely weaken the parent note's
conclusion, it **reverses** it: the operator the parent note lists as
unphysical-by-attractiveness (biharmonic) is attractive, monotone, and closer to
the Newtonian exponent than Poisson at both tested lattice sizes. That is not a
restatement of the flag. **PASS.**

**V5 — Is this a one-step variant of an already-landed cycle in this campaign?**
No. Closest prior cycles are 707b (erratum on the P4 weak-field action formula,
PR #5651) and 709 (A2 bridge identification, backlogged). Both are analytic
statements about supplied operator families. This cycle is a numerical
diagnostic-correctness result on a different parent row, obtained by running the
repo's own propagator, and its load-bearing content (sign structure of a
response kernel; ranking inversion under sign normalization) appears in neither.
Structural distinction: prior cycles asked "can `L^{-1} = G_0` be derived?"; this
cycle asks "does the numerical evidence the repo already banked for that
identification support it?" and answers no, with the parent row's own asks as
the method. **PASS.**

**Gate result: PASS on all five.**

## N1–N8 No-Go Discipline Gate

Applies because the deliverable asserts negative results (`no_go` for the two
named discriminators). The negative claims are exactly: the response kernel is
not a scalar multiple of the inverse Laplacian on this construction (L3); the
0.93 statistic does not discriminate (L7); the attractiveness column has no
content beyond the source-sign convention (L8, L12); Poisson is not the
best-ranked operator under normalization (L9).

**N1 — Alternative route enumeration (≥5 distinct attacks on the no-go).**

| # | Route | What it would attempt | Outcome |
|---|---|---|---|
| 1 | Weak-coupling regime | The mismatch is a strong-`k` interference artifact; at small `k` the response linearises to the resolvent | **ATTEMPTED (R5).** `corr` stays in `[-0.13, +0.01]` across `k` in `[0.05, 10]`. Fails. |
| 2 | Per-layer renormalization | The renormalization projects out the monopole component that carries the `1/r` tail; remove it and the kernel matches | **ATTEMPTED (R6).** Residual stays `1.0000`. Fails. This was my own preferred repair. |
| 3 | Normalization/scale mismatch | `K` and `G` differ only by a scale, so compare after best-fit scaling | **ATTEMPTED (R4).** Least-squares `c` leaves residual 0.9987–0.9996. Fails. |
| 4 | Boundary-proximity artifact | The Dirichlet boundary corrupts the comparison at large `r`; restrict to the interior | **ATTEMPTED.** All comparisons are already interior-masked (`interior_mask`), and R3's sign indefiniteness is an interior statement. Fails to rescue. |
| 5 | Smearing | The parent note perturbs a 3×3×3 block, not a site; the smeared kernel might match while the site kernel does not | **ATTEMPTED.** R8 runs the parent note's own smeared statistic and reproduces `corr = 0.920`, then shows the slopes differ (`-2.24` vs `-1.57`) and the ratio spreads 10.7×. The smeared comparison is the one that looks good and it does not survive a matched test. |
| 6 | Wrong Green's function sign convention | `G` should be `+Laplacian^{-1}` not `-Laplacian^{-1}`, flipping the correlation sign | **RULED OUT.** A global sign flip changes `corr` by a sign and leaves `abs(corr) ≤ 0.13` and the residual unchanged; R3's sign-indefiniteness of `K` is convention-free. |
| 7 | Different beta diagnostic | The ranking inversion is an artifact of `check_field_physics`'s power-law fit | **PARTIALLY UNTESTED — declared.** R11 deliberately uses the parent note's own diagnostic so the comparison is apples-to-apples. A different decay measure could reorder the operators. This is recorded as an open route below, not as a closed one. |

**N2 — Wall-independence audit.**
Named walls: (a) sign-indefiniteness of `K`; (b) non-discrimination of the 0.93
statistic; (c) emptiness of the attractiveness column; (d) ranking inversion.
Pairwise: (c) and (d) are **not independent** — both follow from R10's
definiteness fact. They are reported as two consequences of one cause, and the
note says so ("which is the entire content of the parent note's 'Attractive?'
column"). (a) and (b) are independent of each other and of (c)/(d): (a) is a
sign-structure fact about the kernel, (b) is a property of the Pearson statistic
on seven radii, and neither uses the source-sign convention. No wall is
presented as independent when it follows from another.

**N3 — Hidden-wall scan.**
Grepped the runner and note for "we assume", "by construction", "naturally",
"standard", "registered", "canonical". Hits and classification:
- "by construction" (R12 detail, note §C): explicit, and it is the *point* of
  that row — the source-point sign is fixed by the normalization, which is why
  R12 tests the whole interior instead. Non-hidden.
- "standard math machinery" (V3 above): non-load-bearing context.
- Load-bearing conditions promoted to explicit `[supplied]` tags in the ledger:
  the parent note's parameters, the parent note's `beta` diagnostic, the seven-
  point `k` grid, `delta_phi = 1e-3`, least squares as the matching criterion,
  Pearson correlation as the statistic. No further hidden condition found.

**N4 — Residual matching.**
The only prior witness cited is the parent row's own `notes_for_re_audit_if_any`
and `chain_closure_explanation`, quoted verbatim, and both match exactly — the
cycle performs the two computations they name. No prior no-go or campaign is
cited as a witness, so nothing is dropped and no witness count is at risk.

**N5 — Rhetoric audit.**
Phrases of the form "X is not a Y-fact" were checked at the resolutions actually
tested:
- "the response kernel is sign-indefinite" — verified per-site over the interior
  at three perturbation sites, N=10 (R3). Narrowed in the ledger to "at the
  three tested perturbation sites, N=10".
- "no scalar `c` makes `K = c*G`" — verified per-site, three sites (R4).
  Narrowed to "at the tested sites"; the note explicitly does not claim that no
  operator-valued relation exists.
- "the mismatch is not a weak-coupling artifact" — verified at seven sampled
  `k`, not all `k`. L4's ledger row says so in the Hypotheses and the Shown-vs-
  claimed cells.
- "Poisson is not the best operator in the tested family" — verified at N=20 and
  N=24 only, with the parent note's own diagnostic. Explicitly **not** a
  continuum-limit claim; the note states that the parent note's continuum
  extrapolation was run for Poisson alone.
- "both operator discriminators are artifacts" (title) — qualified in the title
  itself to the parent note's own parameters and decay diagnostic.

**N6 — Partial-closure path scan.**
The parent note's Bounded Claim 1 can be **partially rescued by convention**
rather than abandoned: restricted to the screened family, R13 shows every member
shares Poisson's definiteness, so one fixed source sign treats them all
consistently and Test 4's conclusion is untouched. The note records this as the
proposed narrowing rather than calling for the claim to be dropped, and lists
Tests 1 and 4 under "what survives". No "new axiom required" language appears
anywhere in this cycle; no axiom or primitive is involved.

**N7 — Steelman.**
Hostile-reviewer voice: *"You measured `d rho / d phi` for a propagator whose
field coupling is a pure phase, and found an oscillatory kernel. Of course you
did. The parent note's step 4 is a statement about the amplitude propagator's
resolvent — the object that satisfies a lattice Helmholtz equation — and its
Green's function genuinely is Laplacian-related. You compared the wrong object,
then used the mismatch to demote a row. The density response of an interfering
amplitude was never the thing anyone claimed was the inverse Laplacian."*

Response, and why the cycle survives it: this steelman is largely **correct as
physics**, and the note says so — the last bullet of the proposed revision is
exactly that step 4 conflates the amplitude resolvent with the density response
kernel. But it does not rescue the parent note, because the parent note's own
Test 3 measures the **density** response (`rho_p - rho_0`) and reports the
resulting correlation as "confirm[ing] that the propagator's own structure
selects the inverse Laplacian as its natural response kernel". The object this
cycle tests is the object the parent note tested; the demotion is of the
evidence the parent note actually offers. The steelman strengthens the cycle's
conclusion — that the parent note's step 4 is a conflation — rather than
defeating it. It also names the correct next target, which is recorded in the
trace gate: what the density response kernel of a phase-only coupling actually
is.

Consequently the cycle is **not** demoted for N7, but the steelman's substance
is carried into the note rather than left in this checklist.

**N8 — Cross-cycle echo.**
Structurally similar prior wall: cycle 707b's erratum (PR #5651) found that a
probe's measured quantity (`valley_sqrt`, `p = 1/2`) did not match the action
formula the note claimed for it (`p = 1`). Same failure class as here — a runner
measuring a different object from the one its note names — and it was resolved
by an erratum that corrected the note, not by retiring the physics. This cycle
follows that precedent: correct the note's scope, keep the tests that stand
(Tests 1 and 4). No structurally similar wall was found that has since been
retired by a mechanism not considered here.

**Gate result: no failure condition hit. Route 7 (alternative decay diagnostic)
is declared as untested and recorded as an open route rather than closed.**

## Open routes this cycle does not close

1. **Alternative decay diagnostic (N1 route 7).** R11 uses the parent note's own
   `check_field_physics` power-law fit so the comparison is apples-to-apples. A
   different decay measure could reorder the operators. Untested.
2. **Continuum limit.** The parent note extrapolates `beta -> 1` for Poisson
   from lattices up to 96³ but never ran that extrapolation for the rivals.
   Whether the N=20/24 ranking survives extrapolation is open, and is the single
   most valuable follow-up: if biharmonic's `beta` does not converge to 1 while
   Poisson's does, the parent note's Bounded Claim 1 is recoverable at the cost
   of resting entirely on the continuum extrapolation.
3. **What the density response kernel of a phase-only coupling actually is.**
   R3/R5 show it is sign-indefinite at every sampled coupling strength. Its
   actual form is not identified here.
