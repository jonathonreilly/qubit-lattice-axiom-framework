# The Orbit-Converse: the Local-Frame Orbit of the Free Hopping Is Exactly the Flat Sector — Holonomy Is Frame-Unreachable, and ADM-1's Selection Residual Persists

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; panel-rescoped — the attempted root dissolution does NOT go through)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_local_frame_orbit_flat_sector_converse_holonomy_residual_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=18 FAIL=0`, exact, no MC.
A maximum-tier 5-lens adversarial panel returned `land_with_edits` on a draft titled as an
ADM-1 dissolution; **all eleven required edits are applied**, the decisive one being the
re-scoping recorded in the next section.

## What this note is, after the panel

The draft attempted to wipe ADM-1 — the pointer-frame root `{P_r}` — from the board. **The
panel refuted the wipe** and the refutation is adopted here as the note's own scope: what
is derived is ADM-1's **kinematic** content (the absolute local frame field as a *joint*
gauge redundancy); the campaign's `{P_r}` root in its **binding** sense — *which pointer
frame the einselection dynamics selects* (the #3436 S-primitivity fork; the
`retained_bounded` content of #3450/#3453, live-ledger verified) — is **orthogonal to the
joint co-rotation symmetry and persists**. Part 4 of the runner *exhibits* that
persistence (with the driver fixed, the frame choice changes which basis dephases, at
order 1) rather than asserting around it. What survives as **new** is the orbit-converse.

## The results (exact — runner `PASS=18 FAIL=0`)

**(R1) Local fusion** *(corollary-with-citation of #3332)*. Record content of (state,
per-site frame-naming instruments, link-field hopping) — including interleaved dynamics —
is exactly invariant under the simultaneous local action (`10⁻¹⁶`). The underlying
operator law `Γ({g}) H[U] Γ† = H[g_x U_xy g_y†]` is **#3332's central identity**, verified
here at the Fock level for general links and at `U=I`; the link co-transform is #3332's
transporter step. The fusion adds only instrument-side covariance plus cyclicity.
**#3332's forcing argument stays non-vacuous**: without the compensator, the free hopping
breaks under local frames (breaking norm `O(1)`, verified). Teeth: frames-only rotation
changes content at order 1 — only the absolute field is *jointly* vacuous (the kinematic
statement; "theorem, not premise" applies to the in-derivation proposition on this
surface only — **no grade is authored or implied for #3332**, whose live status is the
audit lane's alone).

**(R2) The orbit-converse — the new load-bearing result.** Every trivial-holonomy link
field is comparator (pure-gauge) form — explicit construction, all links reproduced
exactly — so **the local-rotation orbit of the derived free hopping is exactly the entire
flat sector**: `H[flat W] = Γ H_free Γ†`. This closes #3332's one-directional "flat
connection ⟹ trivial holonomy" into a **two-directional orbit characterization**: frame
fields reach the flat sector, the whole flat sector, and nothing else. (Flag-level frames
are torus-blind — `u` and `u·t` give identical instruments while their comparators differ:
the stratification's arrow-1 `T²` gap object, instantiated in-runner; unitary frames are
used for the converse. #3453 stands.)

**(R3) A genuine frame-unreachable residual: holonomy** *(sharpening-with-citation of
#3332's gauge-invariant spectrum/plaquette facts)*. The holonomy conjugacy class is
invariant under the local action — so no frame field reaches a nontrivial class — and a
generic-flux field (`det=+1`, genuine SU(3)) is **record-separated** from the *entire*
flat sector by a color-blind Pauli-singlet probe (order 10×), while every flat field gives
exactly the free value (`10⁻¹²`). This earns the **existence** of the residual; **no
completeness claim** ("holonomy is *the* gauge content") is made — that would be imported
framing. **Caution, corrected per panel:** the draft's accident representative
`diag(−1,1,1)` had `det=−1` (U(3), not SU(3)) — replaced by the genuine SU(3)
representative `diag(−1,−1,1)`, and the wording fixed: at the accident flux the field is
**record-indistinguishable from free on these probes** (Fock spectra coincide *and* all
single-particle return records coincide — particle-hole conjugacy; only the eigenvalue
lists differ). **Genericity of the separating flux is load-bearing.**

**(R4) The persisting root, exhibited.** With the einselection driver fixed, varying the
frame alone changes the physical outcome (`O(1)`) — the pointer-frame **selection**
question is real and dynamics-level; the joint co-rotation is exactly covariant
(`10⁻¹⁶`) — only the kinematic absolute-frame content is vacuous. **ADM-1's selection
content persists.**

## The honest board after this note

- **Derived:** ADM-1's kinematic content (absolute-frame joint redundancy — at the record
  level, a corollary of #3332's identity); the orbit-converse (R2, new); the
  frame-unreachability and record-registrability of holonomy (R3, sharpening).
- **Persisting, exhibited:** the `{P_r}` **selection** root (#3450/#3453's binding
  content; the #3436 fork) — the einselection-dynamics walls of blocks 05–07 untouched.
- **Distinct, not merged:** the instrument-relative remainder is an **instrument-side**
  residual, different in *type* from the #3486 state-realization clause (state-side;
  branch-only source proposal) — no type-identification is claimed.
- **hat-4 / ADM-2:** they share the `{P_r}` root (#3450, #3449), so their frame-shaped
  *kinematic* part re-types as in R1–R2; their isometry-existence / depolarization /
  global-singlet contents are **not addressed here and stand**.
- **Open derivation target (not an admission, not claimed complete):** the holonomy
  field's dynamics — the ST2 action question, on which R2/R3 sharpen the input: whatever
  supplies gauge dynamics must supply *holonomy classes*, which no frame choice can.
- No new axiom, primitive, measure, or weight; `r` untouched; the
  `record_formation_not_unconditionally_forced` family (retained_no_go) untouched;
  conditional on the supplied `C³` carrier, the named hopping, and the named instrument
  classes. No closing language: the selection root and the holonomy dynamics are open
  frontiers, not locks.

## Cross-references

- The central identity and forcing argument this builds on: PR #3332
  (`MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08`,
  on main; live status is the audit lane's).
- The binding root definition this respects: the four-hats stratification (#3453) and the
  blocking-isometry reduction (#3450) — both `retained_bounded` on the live ledger — and
  the unistochastic fork (#3436).
- The global-level fusion machinery localized here: PR #3478 (branch-only source
  proposal); the state-orientation retirement on main:
  [`COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md).
- The state-realization clause kept distinct: PR #3486 (branch-only source proposal).
- Standard math (method only): trace cyclicity; lattice gauge fields, parallel transport,
  holonomy, Peierls flux; particle-hole symmetry; Jordan–Wigner Fock lifts.
