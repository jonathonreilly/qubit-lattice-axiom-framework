# DM Full Closure — 64:1 Same-Surface Channel-Weight Bridge (Narrow Companion Theorem)

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py`](../scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py)

**Authority role:** narrow companion to the audited_conditional parent
[`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md).
Supplies an **inline-proved derivation of the 64:1 same-surface
channel-weight bridge** — item (i) of the parent's three open
`missing_bridge_theorem` audit items. Does **NOT** modify the parent
note text.

## Honest scope (read this first)

- **One of three audit items only.** Parent's 2026-05-31 verdict
  (`audited_conditional`, auditor
  `codex-cli-gpt-5.5-20260531-131147`) names three open
  `missing_bridge_theorem` items: **(i)** the 64:1 same-surface
  channel-weight bridge, **(ii)** the live-DM plaquette / eta-omega
  observational constants, **(iii)** the packet-completeness /
  selector premise. This companion supplies item (i) only; items
  (ii) and (iii) are explicitly out of scope (§4) and remain open.
- **Does not modify the parent.** Parent's text and ledger row stay
  in place. Lifting `audited_conditional` requires all three items
  closed and re-audited; this companion is item (i) only.
- **Prove-textbook-inline discipline.** The Casimir
  `C_F = (N_c² − 1)/(2N_c) = 4/3`, the octet repulsion coefficient
  `1/(2N_c) = 1/6`, and the decomposition `3 ⊗ 3̄ = 1 ⊕ 8` are
  standard SU(3) representation theory, but they are load-bearing
  here, so they are proved inline as class-A algebraic identities
  (§3, Lemmas B.1–B.4), with the runner constructing explicit
  Gell-Mann generators and singlet/octet projectors and verifying
  the Casimir trace identities and `(C_F)² / (1/(2N_c))² = 64` to
  machine precision (and exactly on rationals).
- **Naming clarified.** "64:1" refers to the **squared-coupling
  weight ratio**: `(C_F)² : (1/(2N_c))² = (4/3)² : (1/6)² = 64 : 1`.
  After multiplicity folding with `(1, 8)` from `3 ⊗ 3̄ = 1 ⊕ 8`,
  the visible-channel formula is `s_vis = (8 s_1 + s_8)/9`
  (multiplicity-folded weights `w_1 : w_8 = 16/81 : 2/81 = 8 : 1`,
  not 64 : 1; the raw 64 : 1 is the pre-fold squared-coupling ratio).
- **No new admissions.** The `R_conn = (N_c² − 1)/N_c² = 8/9`
  multiplicity fraction is cited from retained
  [`CL3_COLOR_AUTOMORPHISM_THEOREM`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  (`cl3_color_automorphism_theorem`, `retained`). The Sommerfeld
  thermal-average algebra underlying `s_1`, `s_8` is cited from
  retained_bounded
  [`DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17`](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md).
  Both pre-exist on `origin/main`; this companion adds no new
  axiom, convention, or import. The cited retained theorem
  **defers** the identification of the 3D symmetric base carrier
  with physical SM color SU(3)_c; this companion carries that
  deferral through verbatim.

---

## §1. Setting (parent objects re-used)

`N_c = 3`. From the parent helper
`scripts/dm_full_closure_same_surface_thermal_support_common.py`
lines 73–81, the load-bearing visible-channel formula is

```text
    s_vis(α_s)  :=  (8 · s_1(α_s) + s_8(α_s)) / 9                     (1)

    α_1  :=  C_F · α_s,             C_F  :=  (N_c² − 1)/(2 N_c)        (2)
    α_8  :=  (1/(2 N_c)) · α_s,     1/(2 N_c)  =  1/6 at N_c = 3       (3)

    s_1  :=  <S_+(α_1; v)>_T,       s_8  :=  <S_-(α_8; v)>_T           (4)
```

with `S_±` the standard attractive/repulsive Sommerfeld factors and
`<·>_T` the Maxwell-Boltzmann thermal average (algebra retained at
`dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17`).
At `N_c = 3`: `C_F = 4/3`. The 3 ⊗ 3̄ = 1 ⊕ 8 multiplicity fraction
`R_conn = (N_c² − 1)/N_c² = 8/9` is the load-bearing content of
retained `cl3_color_automorphism_theorem` on the 3D symmetric base
carrier.

---

## §2. Statement of the narrow bridge theorem

**Theorem (64:1 same-surface channel-weight bridge).**

**(B.1) Casimir-square ratio (raw 64:1).**
At `N_c = 3`,
`(C_F)² / (1/(2N_c))² = ((N_c² − 1)/(2N_c))² · (2N_c)² = (N_c² − 1)² = 64.`

**(B.2) Multiplicity-folded weights.**
`w_1 := (1/9) · C_F² = 16/81`,
`w_8 := (8/9) · (1/(2N_c))² = 8/(9·36) = 2/81`,
`w_1 / w_8 = 8`.

**(B.3) Two equivalent forms of s_vis.**
`(w_1 s_1 + w_8 s_8)/(w_1 + w_8) = (16 s_1 + 2 s_8)/18 = (8 s_1 + s_8)/9 = s_vis`,
matching (1) exactly.

**(B.4) The bridge.** Formula (1) is exactly the multiplicity-folded
squared-coupling-weight average over the SU(3) 1 ⊕ 8 channels, with
multiplicity fractions `(1/9, 8/9)` from retained
`cl3_color_automorphism_theorem` and squared couplings
`C_F²`, `(1/(2N_c))²` carried by attractive-singlet / repulsive-octet
Coulomb coefficients of the t-channel one-gluon exchange.

---

## §3. Proof (class-A inline)

### §3.1 Casimir C_F and octet coefficient (Lemma B.1)

In the SU(N_c) normalization `Tr(T^a T^b) = (1/2)δ^{ab}`,
`Σ_a T^a T^a = C_F · I_{N_c}` with `C_F = (N_c² − 1)/(2N_c)`. The
runner constructs explicit Gell-Mann generators `T^a = λ^a/2`, verifies
`Tr(T^a T^b) = (1/2)δ^{ab}` to machine precision, and verifies
`Σ_a T^a T^a = (4/3) I_3` to machine precision (Part A).

For the quark-antiquark t-channel one-gluon exchange, the color operator
is `T_q · T_q̄ = −Σ_a T^a ⊗ (T^a)^T` (antiquark in conjugate rep). On
total-color subspaces, the identity
`<T_q · T_q̄> = (1/2)(C_2(pair) − 2 C_F)` gives
`= −C_F = −4/3` on the singlet (`C_2 = 0`, attractive) and
`= (N_c − 2 C_F)/2 = (3 − 8/3)/2 = 1/6 = 1/(2N_c)` on the octet
(`C_2 = C_A = N_c`, repulsive). The runner constructs explicit
`3 ⊗ 3̄` singlet/octet projectors
`P_singlet = (1/N_c) Σ_{i,k} |ii⟩⟨kk|`, `P_octet = I − P_singlet`,
verifies completeness, idempotency, and traces
`Tr(P_singlet)=1`, `Tr(P_octet)=N_c² − 1 = 8`, and the
channel-projected scalars to machine precision (Part B).

### §3.2 Squared-coupling ratio = 64 (Lemma B.2)

By direct rational computation,
`(C_F)² / (1/(2N_c))² = ((N_c²−1)/(2N_c))² · (2N_c)² = (N_c²−1)² = 64`
at `N_c = 3`. The runner verifies this exactly on
`fractions.Fraction` (Part C).

### §3.3 Multiplicity decomposition (Lemma B.3)

`3 ⊗ 3̄ = 1 ⊕ 8` gives `dim(1) = 1`, `dim(8) = N_c² − 1 = 8`,
`dim(1) + dim(8) = N_c² = 9`, hence multiplicity fractions
`f_1 = 1/9`, `f_8 = 8/9`. The retained
`cl3_color_automorphism_theorem` audited
`R_conn = (N_c² − 1)/N_c² = 8/9` on the 3D symmetric base carrier; we
cite that retained authority here. The runner verifies (B.3) via the
projector traces of §3.1 (Part D).

The retained theorem **explicitly defers** identification of the 3D
symmetric base with physical SM color SU(3)_c. This companion carries
that deferral through verbatim: the algebraic channel-weight bridge
is proved here; physical-color identification is the same separate
open bridge already named by the retained authority.

### §3.4 Visible-channel folding (Lemma B.4)

Combining (B.2.a) and (B.3.b):
`w_1 := f_1 · C_F² = (1/9)(4/3)² = 16/81`,
`w_8 := f_8 · (1/(2N_c))² = (8/9)(1/6)² = 2/81`,
`w_1 + w_8 = 18/81 = 2/9`, `w_1 / w_8 = 8`.

Therefore
`s_avg := (w_1 s_1 + w_8 s_8)/(w_1 + w_8) = (16 s_1 + 2 s_8)/18 = (8 s_1 + s_8)/9`
which matches formula (1) **exactly** on rationals. The runner
verifies this symbolically with arbitrary distinct rational
`s_1, s_8`, and numerically against the parent helper at
`α_s = (ALPHA_LO + ALPHA_HI)/2` (zero relative error; Part E). ∎

---

## §4. What this companion closes, and what stays open

**Closed by this companion (load-bearing, runner-verified):**

- Casimir identity `C_F = (N_c²−1)/(2N_c) = 4/3` (Lemma B.1, runner Part A).
- Octet repulsion coefficient `1/(2N_c) = 1/6` (Lemma B.1.b, runner Part B).
- Squared-coupling ratio `C_F² / (1/(2N_c))² = 64` ("the 64:1")
  (Lemma B.2, runner Part C).
- Multiplicity decomposition `1 ⊕ 8` with fractions `(1/9, 8/9)`
  (Lemma B.3, runner Part D, citing retained
  `cl3_color_automorphism_theorem`).
- Bridge identity `s_vis = (8 s_1 + s_8)/9` is the multiplicity-folded
  squared-coupling weighting (Lemma B.4, runner Part E, exact on
  rationals and zero relative error vs parent helper).

**Explicitly out of scope (still open after this companion):**

- **Item (ii) — live-DM plaquette / eta-omega observational
  constants.** `OMEGA_DM_OBS = 0.268` (Planck CMB) and
  `ETA_OBS = 6.12e-10` (BBN) and the conversion coefficients
  `omega_b_h2 = 3.6515e-3 · η_10`, `H_PARAM = 0.674` are
  **empirical observational data** not derivable from A1+A2
  retained primitives. Promoting them to retained authorities
  requires either user-approved Tier-A admission or a separate
  derivation lane; not attempted here.
- **Item (iii) — packet-completeness / selector premise.** Whether
  the helper-defined endpoints `α_LM` and `α_short` exhaust the
  same-surface admitted family is a structural definition-space
  enumeration outside this companion's scope; requires a separate
  selector-law authority.
- **Physical-color identification.** Retained
  `cl3_color_automorphism_theorem` defers identifying the 3D
  symmetric base carrier with physical SM SU(3)_c; this companion
  preserves that deferral.

This companion closes one of three named `missing_bridge_theorem`
items as a real inline-proved bridge theorem. It does **not** lift
the parent's `audited_conditional` status.

---

## §5. Audit cite chain (one-hop)

**Retained authorities cited (one-hop):**

- [`CL3_COLOR_AUTOMORPHISM_THEOREM`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  — `cl3_color_automorphism_theorem`, `retained`. Supplies
  `R_conn = 8/9` (used in Lemma B.3).
- [`DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17`](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
  — `dm_thermal_average_sommerfeld_textbook_import_note_2026-05-17`,
  `retained_bounded`. Supplies Maxwell-Boltzmann / Sommerfeld
  normalization algebra for `s_1`, `s_8`.

**Parent (not modified):**

- [`DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17`](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_BOUNDING_THEOREM_NOTE_2026-04-17.md)
  — `dm_full_closure_same_surface_thermal_bounding_theorem_note_2026-04-17`,
  `audited_conditional` (verdict 2026-05-31T13:14:33). Items (ii)
  and (iii) remain open.

## §6. Command

```bash
python3 scripts/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.py
```

Expected: 30 PASS, 0 FAIL. See cache
`logs/runner-cache/frontier_dm_full_closure_64_to_1_channel_weight_bridge_narrow_verifier.txt`.

## §7. Honest auditor read

The Tier-3 audit panel verdict named three `missing_bridge_theorem`
items. This companion supplies item (i) — the 64:1 channel-weight
bridge — as a real inline-proved bounded theorem with an explicit
Casimir computation, a rational-exact squared-coupling ratio, and a
runner that verifies all four lemmas (B.1–B.4) on explicit SU(3)
Gell-Mann generators, singlet/octet projectors, and the parent's
own helper function at the endpoint median. Items (ii) and (iii) are
not in scope here and remain open for separate authority; the
parent's `audited_conditional` verdict is preserved until all three
items close and the parent is re-audited.

The physical-color identification deferral carried by the retained
`cl3_color_automorphism_theorem` is preserved verbatim: the
algebraic 1 ⊕ 8 decomposition + Casimir computation closes the
bridge **on the algebraic carrier**, not on physical SM color
SU(3)_c. Reading the bridge as a physical channel-weight result for
the same-surface DM process requires that same retained-bridge
authority to land.
