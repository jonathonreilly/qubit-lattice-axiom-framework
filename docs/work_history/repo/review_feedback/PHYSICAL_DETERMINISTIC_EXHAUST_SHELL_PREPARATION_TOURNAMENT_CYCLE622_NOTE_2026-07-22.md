# Physical deterministic exhaust-shell preparation tournament — Cycle 622

Date: 2026-07-22. Authority: none. Audit: unset. Constitutional effect: none.

Runner:
`scripts/physical_deterministic_exhaust_shell_preparation_tournament_cycle622_2026_07_22.py`
Frozen contract SHA
`46f9cbe09fd60cddde1f69005f87a8173d0cfbf0e5e24098c90f414ace258a55` (hashed
before any output). Cold: **6 PASS / 6 FAIL, exit 1 expected** — this cycle is
an honest double-falsification with a diagnosed mechanism.

Work-history line: the two active lanes have collided on cycle numbers (the
campaign branch reaches Cycle 621 and carries unrelated Cycle 610/611/612
notes); this lane claims Cycle 622 per owner directive. Execution: workhorse
split, supervisor Fable 5, Opus 4.8 workers bounded only, no codex.

## Result up front — both frozen routes falsified; the mechanism is new physics

The mission target was deterministic, non-postselected bound-branch
preparation: raw source in, certified clock out, all weight accounted.

1. **Route D-1 (exhaust-shell absorber) is falsified — by a discovery.**  The
   fully unitary shell absorber (per-step SWAP of the Chebyshev-shell
   amplitude into fresh blank exhaust registers; exact matter+exhaust ledger,
   defect < 4e-14; no conditioning anywhere) fails to purify: survivor purity
   plateaus at 0.40-0.47 on every frozen row and *declines* with longer
   preparation, and no row certifies on either channel.  The decisive control
   inverted its prediction: with the contact deleted (g = 0), the absorber was
   predicted to drain everything (survivor < 0.02); it retained **0.19** after
   128 absorbing steps.  Diagnosis: **the free two-CAR walk retains slow,
   near-origin content that geometric escape cannot drain** — the six
   zero-displacement direction pairs (d, d) are stationary each step and the
   coin continually remixes amplitude through them, so a substantial free
   component lingers near the origin indefinitely.  A spatial absorber
   therefore cannot separate bound-by-contact content from slow free content;
   the survivor is a roughly half/half mixture and winds at neither line.
   This retention effect is a real, previously uncharacterized property of
   the accepted walk (it is consistent with Cycle 578's algebraic partial: no
   exact flat band exists, but near-stationary content does).
2. **Route D-3 (dephasing-pointer cascade) is falsified as predicted.**  The
   frozen negative-leaning prior held exactly: full onsite-pair dephasing
   destroys the bound state's onsite/offsite coherence; the ensemble
   bound-branch weight decays monotonically 0.263 -> 0.031 over eight rounds
   (initial decay consistent with the 2 x 0.263 x 0.737 estimate).
   Decoherence-driven schemes in the contact basis cool away from, not
   toward, the clock state.
3. **Passing rows**: byte-pins; all-24 shell invariance (exact); the norm
   ledger (the deterministic accounting itself works perfectly); absorber-off
   control; lawful-domain refusal; the D-3 prior.
4. **Failed prediction rows shipped unrepaired**: P1 (certification), the
   survivor-norm band, the purity band, P2 (contact-off inversion — the
   discovery row), P4/P5 (nothing to transfer), and P8 (the masked-operator
   power iteration did not converge to a bound-adjacent phase; with a
   clustered non-normal slow spectrum the Rayleigh estimate is unreliable —
   reported as a method limitation; the independent worker computation is
   pinned in the work log for comparison).

## No-wall disposition (full N1 applied)

Attempted-and-failed autonomous-preparation families across Cycles 611-622:
window-conditioning certification (611), adiabatic contact ramp (611),
exhaust-shell absorber (622), dephasing cascade (622) — four.  Attempted and
positive but postselected: the minus-port echo filter (611/612).  Live and
unattempted: **coherent contact-echo filtering with retained ancilla exhaust**
(the deterministic descendant of the successful postselected route: the g-echo
discriminates by contact response, which the slow free modes — unlike a
spatial shell — cannot mimic), engineered two-shell interferometric drains,
and driven/Floquet contact modulation.  `4 < 5` and live routes exist:
**no wall, minimum-content, or shared-obstruction claim ships.**  The
constructive map, however, is now sharp: geometric filtering and contact-basis
decoherence are both excluded mechanisms; contact-response discrimination is
the surviving mechanism class, and its postselected form is already proven to
purify (0.263 -> 0.909).

## Supplied / derived / open

Supplied: shell geometry and schedule (frozen; no spectral data); fresh blank
exhaust registers (54 sites x N_prep at R=3; ledger reported); the D-3 pointer
resources; certification machinery (spectral data on the certification side
only).  Derived: the exact deterministic ledger; the slow-free-retention
discovery and its consequence for geometric filtering; the D-3 decay curve;
both falsifications.  Open: the deterministic contact-echo route (named next
campaign); everything inherited (occurrence middle, pulse/readout,
calibration, deterministic preparation itself).

## Interpretation firewall

A preparation schedule is not time.  Exhaust registers are not Records.  The
survivor/exhaust split is a coherent norm ledger, not Born probability.  The
slow-free retention is a finite-box statement at L9 (held sizes untested for
it beyond the frozen rows); it is not an infinite-volume localization theorem.
No proper time, lapse, energy, or actuality claim.

## Cold verification

```text
RESULT 6 PASS / 6 FAIL (exit 1 expected; falsification tournament)
external wall ~14.3 s; ledger defect < 4e-14; receipts and cold transcript:
outputs/physical_deterministic_exhaust_shell_preparation_tournament_cycle622_receipt_2026_07_22.json
outputs/physical_deterministic_exhaust_shell_preparation_tournament_cycle622_cold_2026_07_22.txt
frozen contract SHA 46f9cbe09fd60cddde1f69005f87a8173d0cfbf0e5e24098c90f414ace258a55
```

## Optimal next campaign

Deterministic contact-echo filtering: the Cycle-611 minus-port map
(G_g^m - G_0^m)/2 executed with the path ancilla RETAINED as decoupled exhaust
each round (never recombined, never conditioned), plus the exhaust-locality
argument of this cycle's D-1 for the word semantics.  Frozen questions for
that contract: does the all-minus-history amplitude dominate the certification
word (the echo analog of shell decoupling), and does the slow-free content —
which is g-INsensitive by construction — exit through the plus-port exhaust at
first order?  If that also fails, the attempted-family count reaches five and
a bounded negative claim becomes N1-admissible for the first time.

## Appendix — independent worker cross-check ADJUDICATES AND CORRECTS the
## mechanism diagnosis (added after the worker's masked-operator computation)

The independent Opus worker computation (own position-rep build of G from the
c219/c210 modules only; symmetry-block Arnoldi, ARPACK-confirmed, residuals
<= 9e-15) supersedes two mechanism claims in the body of this note:

1. **The contact-off retention was a frozen-geometry artifact, not
   near-origin free content.**  The literal frozen operator
   (1 - Pi_{|r|inf==3}) G has dominant eigenvalue |lambda| = 1.0000000 with
   its eigenvector living ENTIRELY at Chebyshev radius 4: the surface-only
   shell at radius 3 does not enclose the periodic minimal-image radius-4
   ring, which is a near-lossless invariant subspace.  The body's sentence
   attributing the retention to "stationary (d,d) direction pairs remixed by
   the coin" is **withdrawn** as the mechanism of the observed retention.
   (The jump-over risk was flagged in the supervisor's design analysis and
   the surface geometry was frozen anyway — recorded as a contract-design
   error.)
2. **The purification plateau is caused by a second long-lived interior A2
   resonance, not by generic slow dust.**  For the corrected absorbing-ball
   operators (removing radius >= 3, and the clean R4 ball), the dominant
   eigenpair is an antisymmetric proper-cubic A2 interior quasi-bound mode
   at (|lambda|, arg lambda) = (0.99910937, +0.30655) [ball r<=2] and
   (0.99981521, +0.31182) [ball r<=3], radius profile concentrated at
   r <= 2 with ZERO weight at r >= 3, survival^256 = 0.796 / 0.954.  Its
   phase coincides numerically with the dust-lock winding rate of Cycles
   610-622 (+0.3136 rad = +0.0499 rev): the "dust lock" is evidently a
   coherent second A2 line, not featureless dust, and it outlives the
   Birman-Schwinger bound state under spatial absorption — which is the
   correct explanation of the D-1 purity plateau at ~0.45.
3. Consequences, stated with N-discipline: the D-1 falsification stands AS
   RUN (the frozen rows failed), but its mechanism attribution is corrected,
   and "geometric filtering is excluded" is **narrowed** to "surface-shell
   filtering is excluded and ball filtering is compromised by the second A2
   resonance."  Whether the +0.31 mode is contact-dependent (a second
   contact-bound internal A2 state — the object whose held absence was the
   Cycle-578/583/599 open item, which would make a two-line vernier clock
   physical) or a contact-independent lattice/cavity resonance is NOT
   determined here: the worker ran only g = 0.37.  That single discriminator
   (g = 0 versus g = 0.37 ball-absorber spectra, then a two-line beat word)
   is the decisive question of the next campaign, replacing the note body's
   earlier next-campaign paragraph.

Worker artifacts (session scratchpad), SHA-256:
masked_eigen.json  eda675d3d4e96ae995f20e23345f42e93b13b58564bca363a338837cf8ef90dc
masked_eigen.py    cc1563ce6ef28b0c2fda5f86c97b3a67f728ed46afa62c6b10c062ff44057add
This appendix changes only the human-readable note; the runner, receipt, and
cold transcript remain byte-frozen as run.
