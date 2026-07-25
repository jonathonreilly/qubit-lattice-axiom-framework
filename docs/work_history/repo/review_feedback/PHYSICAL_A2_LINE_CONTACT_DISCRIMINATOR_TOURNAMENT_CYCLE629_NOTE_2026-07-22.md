# Physical A2-line contact discriminator tournament — Cycle 629

Claim type: bounded_theorem

Date: 2026-07-22. Authority: none. Audit: unset. Constitutional effect: none.

Runner:
`scripts/physical_a2_line_contact_discriminator_tournament_cycle629_2026_07_22.py`
Frozen contract SHA
`77a152201d9a2fab6396f087ed11cfb82aee4e76c8bc155b16acc77d5939697a` (both
readings' criteria fixed before output). Cold: **4 PASS / 2 FAIL, exit 1** —
the verdict rows all passed; both FAIL rows are frozen-tolerance/frozen-
prediction artifacts that the discovery itself explains (details below, shipped
unrepaired).

Work-history: joint lane max observed 628; this lane claims 629. The
Cycle-573/575/578/583 substrate is present through the landed, re-frozen
parent surfaces. Execution: workhorse split (supervisor Fable 5; Opus 4.8
workers bounded; no codex).

## Verdict — R1 under the frozen finite discriminator; BS candidate demoted

Under the frozen criteria the reading is **R1 (contact-dependent)**, and the
finite qualified-mode and unmasked-word criteria support a contact-dependent
+0.31 interior antisymmetric A2 line. The full-window Birman-Schwinger scan
records a near-zero candidate but, after the Cycle-662 adjudication, does not
upgrade that reading to a physical-branch identification.

1. **Contact dependence (frozen criterion, decided):** at g = 0.37 the
   ball(r<=2)-absorber interior line sits at
   (|lambda|, arg) = (0.999109, +0.3065475), reproducing the independent W5
   anchor to 2.5e-6 in phase and 4e-10 in magnitude, Ritz residual 2.3e-13.
   At g = 0 the frozen block-subspace criterion finds **no qualifying
   dominant interior mode near +0.31** (the dominant g = 0 interior cavity
   mode sits at -3.0663); `persists_at_g0 = False`. This is a statement about
   the tested qualified modes, not an exhaustive absence theorem for the full
   non-normal spectrum. The unmasked corroborator agrees: the raw-source
   minus-channel word at g = 0 does not lock at the dust line (rate -0.023,
   unlocked).
2. **Full-window BS near-zero diagnostic — not a physical-branch
   identification:** the Cycle-610 A2-branch value has a near-zero at
   **+0.29998** with |b_A2| = 1.12e-10 on the frozen window
   [0.10, 0.50] (coarse floor 2.4e-3 elsewhere).  Cycle 583 established the
   A2 contact channel as rank one with the pole at -2.9756 — but its root
   search was confined to the window around -2.98; the +0.30 root was simply
   never looked for. Cycle 662 later shows that full-window minimization
   latches onto many razor-thin continuum zeros and supersedes +0.29998 as the
   physical second-branch position; the branch-tracked value is near +0.31368.
   That value is not the pi-partner of theta_b
   (wrap(theta_b + pi) = +0.166).
3. **The dust-lock identity:** the two-line beat word on the ball-survivor
   mixture shows exactly two dominant DFT peaks (magnitudes 455 and 60
   against a 0.085 floor): the primary at -2.975413 (within one bin of
   theta_b) and the secondary at **+0.313368 — the historical dust-lock
   rate (+0.3136) to three decimals**.  The "dust lock" of Cycles 610-622
   was never featureless dust: it is this second A2 line.
4. **Position boundary and downstream correction:** this runner records
   +0.29998 (global-min BS zero), +0.30655 (r<=2 absorbing cavity), and
   +0.31337 (unmasked word peak). Cycle 662 shows that the first value is an
   estimator artifact and that the branch-tracked BS line agrees with the word
   near +0.31368; only the absorber cavity carries the displayed shift. The
   rigorous infinite-volume spectral lemma remains open.

## The two FAIL rows (shipped unrepaired, both explained)

- **W5-anchor row:** ball3 agreed to 2.5e-6; ball4 returned no qualifying
  mode because the frozen interior-weight filter (weight at r<=2 above 0.9)
  was written for the r<=2 ball and misapplies to the r<=3 ball whose mode
  legitimately spreads to radius 3 — a contract-design flaw, recorded, not
  repaired post hoc.
- **Beat-word row:** the frozen prediction placed the secondary peak at the
  masked-cavity value (+0.30655); the unmasked word oscillates at the
  undressed/word value (+0.31337), 2.1 bins away.  The FAIL is itself
  confirmatory physics: the frozen prediction used the wrong dressing frame,
  and the discrepancy measures the cavity shift.

## Vernier-clock scoping (scoping only; the build is a separate owner decision)

With two contact-generated A2 lines in one local word:

- **Alias ceiling:** a single line identifies a rate only modulo the
  principal window (the Cycle-610 pi ceiling, |R| <= pi/|theta_b| = 1.0556,
  which made the 5:4 advance word rate-unreachable).  A uniform modulation
  alpha shifts BOTH lines equally, while their wrapped positions fold at
  different alpha values; the pair (wrap(theta_b + alpha),
  wrap(theta_2 + alpha)) is injective in alpha over the full 2*pi window
  provided the two-line set has no nontrivial rotational symmetry (in
  particular, the lines are not antipodal) — so a two-line readout reconstructs the true alpha
  beyond either line's fold, and the advance sector (|R| = 1.25) becomes
  reachable in the reconstructed rate.  Using the corrected physical/word
  second line, the beat phase wrap(theta_2 - theta_b) is approximately
  -2.994 and is alpha-invariant: an internal ruler and a species fingerprint.
- **Preparation:** a two-level internal structure admits Raman-like
  candidates (drive the primary-secondary transition with the modulated
  contact instead of filtering) — a route class entirely distinct from the
  four falsified preparation families, to be enumerated under its own frozen
  contract if the owner opens the build.
- **Prerequisites before any build:** held-size and held-species existence
  of theta_2; its width/isolation; a two-line lock certificate (the
  Cycle-610 certificates assume a single dominant line and must be extended
  to a two-line lawful domain before a vernier word can be certified).

## Supplied / derived / open

Supplied: ball geometries and iteration schedule (frozen); the frozen
windows/tolerances; certification machinery on the corroborator row.
Derived: the R1 verdict under frozen finite criteria; an additional
full-window A2-channel near-zero candidate at +0.29998 (not the downstream
physical-branch position);
the dust-lock identification; the g = 0 dominant cavity spectrum point
(-3.0663); and both FAIL diagnoses. Open at this cycle: held-size and
held-species existence of the physical second branch, width/isolation and the
infinite-volume lemma, the two-line lawful-domain extension, and the vernier
build.

## N1-N8 (abbreviated) and firewall

This cycle ships a positive discriminator outcome and no universal no-go or
wall claim. Its negative limb is restricted to the tested finite-L9 qualified
mode/word criteria; it does not assert exhaustive spectral absence. A spectral
line is not energy; a beat is not a clock law; the DFT of the recorded word is
data analysis, not an instrument; no vernier clock is built here; no proper
time, lapse, redshift, Born, or actuality claim.

## Cold verification

```text
RESULT 4 PASS / 2 FAIL (exit 1; both FAILs explained above, unrepaired)
external wall approximately one minute
receipt:   outputs/physical_a2_line_contact_discriminator_tournament_cycle629_receipt_2026_07_22.json
transcript: outputs/physical_a2_line_contact_discriminator_tournament_cycle629_cold_2026_07_22.txt
contract:  SHA 77a152201d9a2fab6396f087ed11cfb82aee4e76c8bc155b16acc77d5939697a
W5 comparison hashes (session scratchpad, not repository artifacts):
masked_eigen.json eda675d3d4e9...  masked_eigen.py cc1563ce6ef2...
```

## Optimal next campaign

Held verification of theta_2 (L13 and beta = -0.35 BS scans plus ball
spectra), a width/isolation bound, and the two-line lawful-domain extension
of the Cycle-610 certificates — the three prerequisites the vernier build
decision needs.

## Dependency citations

This runner byte-pins
[Cycle 610](PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md),
[Cycle 611](PHYSICAL_AUTONOMOUS_BOUND_BRANCH_PREPARATION_TOURNAMENT_CYCLE611_NOTE_2026-07-22.md),
and
[Cycle 622](PHYSICAL_DETERMINISTIC_EXHAUST_SHELL_PREPARATION_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md).
