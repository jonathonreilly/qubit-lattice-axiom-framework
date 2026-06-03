# The C^2<->C^3 Carrier "Bridge" Is Self-Imposed: Two Independent Residuals, Not One Object

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded localization / necessity audit. This note shows the
charged-lepton carrier decomposes into two Z_2 selection bits living on *disjoint,
mutually commuting tensor factors* -- a VALUE bit on the generation factor `C^3`
and a CARRIER bit on the site factor `C^2` -- each with its own retained-backed
residual, and that the two posited links which would weld them into one
"reality-respecting" object are POSITED, not proven. It does not derive either
bit, close either residual, approve an import, force matter attachment, or set an
audit verdict. It reclassifies the "single terminal bridge import" as a
self-imposed coupling of two separable residuals.
**Primary runner:**
`scripts/frontier_koide_carrier_bridge_necessity_attack.py`
with cache
`logs/runner-cache/frontier_koide_carrier_bridge_necessity_attack.txt`
(15/15 checks).

## The assumption under audit (A3)

The session's `C^2<->C^3 bridge` program assumes that closing the carrier requires
**unifying** the two terminal bits -- a VALUE bit (the 2-sector / Frobenius
partition on generation `C^3`, identified with `sign(beta)` and a `Hodge`-orientation
bit) and a CARRIER bit (the records / CAR Hermitian-Kraus sign on site `C^2`) --
into ONE object via a reality-respecting bridge. Both bridge routes (on-site
Bloch/Hopf quotients; cross-site graph-braid `P(t)=0`) being closed then reads as
"the bridge is the single terminal import."

The audit question: is the bridge **necessary** (the two bits provably one object),
or **self-imposed** (the bits close independently, leaving two separate residuals)?

## Result: the bits are INDEPENDENT; the bridge is self-imposed

The carrier factorizes as `(value bit on C^3) (x) (carrier bit on C^2)` over two
disjoint commuting tensor factors, each closing by its own argument with no
reference to the other. The "single bridge" welds them only through two **posited,
unproven** links.

### The two factors are disjoint and commuting (runner F1, F5)

The VALUE structure lives in the **site-indexed** first-order operator `D`
(`H = iD`), whose generation readout is the `C^3` circulant data. The CARRIER
structure lives in the **on-site spinor** `sigma_i` on `C^2`. The merger fact
`[H (x) I_2, I (x) sigma_i/2] = 0` (verified for a generic real-antisymmetric `D`)
makes `D` **spin-blind on `C^2`**: the two carry orthogonal information on
commuting factors. A value-axis operator on `C^3` and a carrier-axis (site
exchange / SWAP) operator on `C^2 (x) C^2` commute on the joint space and can be
set independently -- so **no single operator is forced to be simultaneously both
bits**. (The CPT authority below is the retained source for `H = iD` real
anti-Hermitian; the merger / per-site spin-1/2 are the operator-frame sources.)

### The VALUE residual closes on `C^3` alone (runner F2)

`sign(beta)` / `Jcs`-orientation is a **generation-factor** datum. Every circulant
generation mass `H = aI + bC + conj(b)C^2` commutes with the finite Kahler
structure `Jcs = (C - C^2)/sqrt(3)` for **all** moduli `r = |b|^2/a^2` (verified,
200 random `(a,b)`), so orienting the value `Z_2` is decoupled from the `r=1/2`
vs `r=1` modulus -- the value side is itself internally two-axis, all on `C^3`.
The remaining value question is **chiral vs non-chiral generation mass**: the
native circulant commutes with `Gamma_chi = 2P_singlet - I` and never
anticommutes, so the `Q=2/3` branch needs a `Gamma_chi`-anticommuting coupling,
blocked **on the generation `R^3`** by the retained-bounded
`koide_z3_equivariant_anticommuting_no_go` (`comm(C) cap anticomm(Gamma_chi) = {0}`),
with the off-generation-factor route explicitly **not foreclosed**
(`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31`). This is an
`O_h` / Frobenius / representation-theory residual, attackable on `C^3` with no
mention of the site `C^2`.

### The CARRIER residual closes on `C^2` alone (runner F3)

The records / CAR sign is fermion-vs-hard-core-boson on the **site** factor. On
one site, `sigma_+` is the **same** `2x2` matrix for both (`(sigma_+)^2 = 0`), so
single-site invariants are blind to it; the discriminator is the **cross-site**
exchange sign -- native ladders commute (`[O_0,O_1]=0`, hard-core boson) while the
Jordan-Wigner relabel anticommutes (`{c_0,c_1}=0`, fermion). This is a graded-
locality / graph-braid-framing question entirely on the site factor, sitting on the
retained_no_go statistics gate
(`staggered_dirac_substep1_statistics_agnostic_no_forcing`) and the retained_no_go
discrete FS-insufficiency (`fs_rotation_exchange_discrete_insufficiency`). The
generation `C^3` index never appears.

### The two welding links are POSITED, not proven (runner F4)

The "two bits are one object" claim rests on a chain
`records-Z_2 = sign(beta) = Hodge-orientation bit = value-Z_2`. Both links are
unproven on `origin/main`:

- **Link (a) `records-Z_2 = sign(beta)`.** The string
  `{records-pointer Z_2 = sign(beta)}` occurs in exactly ONE place -- the
  carrier-locus note itself -- where it is labelled **"open, not a theorem"** and
  listed as front (iii) "close the bridge." Link (a) *is* the bridge. It is not a
  theorem; it is the thing being assumed.
- **Link (b) `sign(beta) = Hodge-orientation / value bit`.** The carrier-locus
  note asserts "the lone residual is a `Z_2` Hodge bit `= sign(Pfaffian of the
  doublet block) = sign(beta)`, left free by CPT-exactness." But the cited retained
  authority `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`
  (retained_bounded) proves **only** C1 (`Theta D Theta^{-1} = D`) and C2
  (`[Theta_H, H] = 0`) -- a generic discrete-symmetry commutation. It contains no
  `beta`, no `Pfaffian`, no `Hodge`, and asserts no "Pfaffian-sign = Hodge-bit"
  identity (C3 was demoted by audit in 2026-05-17). So link (b) is asserted in the
  **unaudited** carrier-locus note and is not carried by the retained source it
  cites.

Independently, the **unaudited** `KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01`
states the opposite of unification on the load-bearing tier: the value/faithfulness
residual (G1) and the carrier/statistics residual (L1) collapse to one **only**
conditionally, riding unaudited spin-statistics / OS-reconstruction rows, and "on
the retained-only tier, two posits remain."

## Verified tiers (origin/main audit ledger)

| claim_id | effective status | role |
|---|---|---|
| `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | retained_bounded | source of `H=iD`; proves only C1/C2, NOT the Hodge=sign(beta) link |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | retained_bounded | VALUE residual wall on `C^3` (`comm(C) cap anticomm(Gamma_chi)={0}`) |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | retained_no_go | CARRIER residual gate on `C^2` (statistics) |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | retained_no_go | CARRIER residual: discrete rotation->exchange decoupling |
| `koide_carrier_locus_decomposition_note_2026-06-01` | unaudited | asserts link (b); labels link (a) "open, not a theorem" |
| `koide_p1_collapses_frame_residuals_note_2026-06-01` | unaudited | "on the retained-only tier, two posits remain" |
| `koide_matter_attachment_graded_statistics_gate_narrow_theorem_note_2026-06-02` | unaudited | localizes CARRIER residual to a single cross-site gate |
| `koide_berry_monopole_bridge_reduction_note_2026-05-31` | unaudited | VALUE residual = chiral/nonzero-Berry, off-generation route open |

## Disposition

The "single terminal `C^2<->C^3` bridge import" **over-couples two separable
residuals**. The honest picture is **two independent residuals**, each attackable
on its own factor with no bridge:

- **VALUE residual (generation `C^3`):** supply a `Gamma_chi`-anticommuting
  (chiral) generation mass -- the `O_h` / Frobenius / nonzero-Berry question --
  via the off-generation-factor route the Berry-monopole reduction leaves open.
- **CARRIER residual (site `C^2`):** select the cross-site graded (CAR) statistics
  over the native hard-core boson -- the graded-locality / graph-braid-framing
  question on the site factor.

There is **no proven coupling** forcing them to be one object: the welding chain's
two links are posited (one is literally the open bridge; the other is asserted past
its cited retained authority). The bridge is therefore **a self-imposed
requirement**, not a derived necessity. Closing it is *sufficient* to weld the two
bits but not *necessary* to close the carrier; the carrier closes when both
factor-local residuals close, which can proceed in parallel.

## Non-circularity

`Q=2/3` never appears; no faithful representation and no fermionic frame are
assumed. Every check is a direct tensor-factor / linear-algebra fact about `C^3`
and `C^2` (spin-blindness, `[H,Jcs]=0`, hard-core-vs-JW exchange, joint-space
commutation) plus tier and prose verification that the welding links are posited,
not proven. The conclusion is a localization (two separable residuals), not a
forcing of either.

## Next paths this opens

- Attack the VALUE residual and the CARRIER residual **as two parallel lanes**,
  dropping the bridge as a prerequisite: the off-generation chiral-factor route
  for `Q=2/3`, and the discrete graph-braid framing / energy-positivity statistics
  route for CAR. Neither needs the other.
- If a future source theorem *does* derive link (a) or link (b) from retained
  rows, the welding becomes real and the two lanes merge; until then the
  single-bridge framing should not be load-bearing.
- Audit the unaudited capstone notes that assert the unification; the present note
  predicts they cannot promote the `Hodge = sign(beta)` and `records = sign(beta)`
  links to retained without a fresh source theorem.

## Load-bearing authorities

[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md),
[STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md),
and
[FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md](FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md).

Non-load-bearing context (the unaudited notes whose unification framing this audit
corrects) remains plain text:
`koide_carrier_locus_decomposition_note_2026-06-01`,
`koide_p1_collapses_frame_residuals_note_2026-06-01`,
`koide_matter_attachment_graded_statistics_gate_narrow_theorem_note_2026-06-02`,
and
`koide_berry_monopole_bridge_reduction_note_2026-05-31`.

## No-Go Discipline Gate

- **N1 - Alternative routes.** Three weldings were tested: (a) `records = sign(beta)`
  (open bridge), (b) `sign(beta) = Hodge bit` (asserted past CPT's C1/C2), and a
  forced shared operator on the joint space (commutes / independent). All fail to
  force one object.
- **N2 - Wall independence.** The VALUE wall (`koide_z3_equivariant_anticommuting_no_go`)
  and the CARRIER wall (`staggered_dirac_substep1` / `fs_rotation_exchange`) are
  distinct retained rows on distinct factors; closing one does not close the other.
- **N3 - Hidden-wall scan.** "value bit," "carrier bit," "`C^3`," "`C^2`,"
  "`sign(beta)`," "Hodge," "records" are explicit finite objects; the welding links
  are named as posited, not smuggled.
- **N4 - Residual matching.** The two residuals match the two factor-local gates
  exactly (generation chirality on `C^3`; cross-site statistics on `C^2`); the
  bridge residual matches neither -- it is their (open) product.
- **N5 - Rhetoric audit.** The verdict is "self-imposed / two independent
  residuals," scoped to the retained tier; no "only/last/closes" framing is used,
  and both factor-local lanes are left open.
- **N6 - Partial-closure path.** Either factor-local residual can close
  independently; a later source theorem deriving link (a) or (b) would re-merge the
  lanes without an axiom change.
- **N7 - Steelman.** The strongest case for necessity is that one reality
  structure (CPT / `Theta`) governs both factors. Granted at the level of generic
  commutation (C1/C2), but `Theta` acting on the site factor does not fix the
  generation `sign(beta)` nor the cross-site exchange sign -- the specific
  identities remain unproven, so the steelman does not force one object.
- **N8 - Cross-cycle echo.** The same two-residual shape appears in the
  P1-collapses, matter-attachment-graded-statistics, and Berry-monopole notes; this
  note names the welding as the assumption rather than inheriting it.
