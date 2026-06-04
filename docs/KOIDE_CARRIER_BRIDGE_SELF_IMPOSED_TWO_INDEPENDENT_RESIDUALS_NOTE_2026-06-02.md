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

## No-go discipline gate (N1-N8)

**Status:** PASS for the narrow necessity/localization claim only. The claim being
made is NOT "the carrier can never be closed," NOT "the two bits are unrelated in
all physics," and NOT "either factor-local residual is itself closed." It is the
single structural statement that the `C^2<->C^3` bridge is **sufficient but not
necessary** to close the carrier, because the VALUE bit (generation `C^3`) and the
CARRIER bit (site `C^2`) live on disjoint commuting tensor factors and each closes
by its own factor-local argument, while the two welding links that would fuse them
into one object are posited rather than proven on `origin/main`.

### N1 - Alternative route enumeration

Each route below is an independent way one might try to force the two terminal
bits to be **one object** (and so make the bridge necessary). Each was checked
against the runner and the cited tiers; none forces unification for this scoped
claim.

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Single joint-space operator carries both bits | Exhibit one operator on `C^3 (x) C^2 (x) C^2` that is simultaneously the value-`Z_2` and the carrier-`Z_2`, so the two cannot be set independently. | `[H (x) I_2, I (x) sigma_i/2] = 0` for generic real-antisymmetric `D` (runner F1/F5): `D` is spin-blind on `C^2`, so a value-axis operator on `C^3` and a carrier/SWAP operator on `C^2 (x) C^2` commute and are independently choosable. No operator is forced to be both. | ATTEMPTED |
| Welding link (a): `records-Z_2 = sign(beta)` | Promote the records/CAR pointer sign on the site factor to equal the generation Frobenius `sign(beta)`, fusing carrier into value. | The string occurs in exactly one place -- the carrier-locus note -- where it is self-labelled "open, not a theorem" and listed as front (iii) "close the bridge" (runner F4). Link (a) *is* the bridge; assuming it begs the question. | ATTEMPTED |
| Welding link (b): `sign(beta) = Hodge/value bit` | Use CPT-exactness to identify `sign(beta)` with a `Z_2` Hodge/Pfaffian-orientation bit, anchoring the value side to a retained authority. | The cited retained `cpt_exact_real_anti_hermitian_d_narrow_theorem` proves only C1 (`Theta D Theta^{-1}=D`) and C2 (`[Theta_H,H]=0`); it contains no `beta`, `Pfaffian`, or `Hodge`, and C3 was audit-demoted 2026-05-17. Link (b) is asserted in the unaudited carrier-locus note past its cited source (runner F4). | ATTEMPTED |
| Modulus-coupling route | Tie orienting the value `Z_2` to the `r=1/2` vs `r=1` modulus, so the value bit is not separable even within `C^3`. | Every circulant `H = aI + bC + conj(b)C^2` commutes with `Jcs = (C - C^2)/sqrt(3)` for ALL moduli `r` (runner F2, 200 random `(a,b)`): orienting the value `Z_2` is decoupled from `r`, so the value side stays a pure `C^3` datum. | ATTEMPTED |
| Single-site carrier discriminator | Distinguish fermion from hard-core boson by an on-site invariant, making the carrier bit a property of one site that the generation factor could touch. | `(sigma_+)^2 = 0` makes `sigma_+` the same `2x2` matrix for both statistics (runner F3); single-site invariants are blind. The discriminator is the cross-site exchange sign (`[O_0,O_1]=0` vs `{c_0,c_1}=0`), a graded-locality fact entirely on the site factor, where the generation `C^3` index never appears. | ATTEMPTED |
| Conditional collapse via spin-statistics / OS | Cite a route that collapses the value (G1) and carrier (L1) residuals into one. | The unaudited `KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01` collapses them only conditionally, riding unaudited spin-statistics / OS-reconstruction rows, and states "on the retained-only tier, two posits remain" -- i.e. it confirms separability on the retained tier rather than forcing unification. | ATTEMPTED |

### N2 - Wall-independence audit

The collapsed wall set for this localization has **two independent walls on two
disjoint tensor factors**, not one wall doing double duty:

- VALUE wall on `C^3`: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded),
  `comm(C) cap anticomm(Gamma_chi) = {0}` -- a representation-theory fact about the
  generation circulant algebra.
- CARRIER wall on `C^2`: `staggered_dirac_substep1_statistics_agnostic_no_forcing`
  (retained_no_go) and `fs_rotation_exchange_discrete_insufficiency` (retained_no_go)
  -- graded-locality / discrete-rotation facts about the site factor.

These are distinct ledger rows whose statements share no symbols (`Gamma_chi` and
the generation index never enter the statistics gates; the cross-site exchange sign
never enters the `C^3` anticommutation no-go). Closing one leaves the other
untouched -- exactly the independence the localization asserts. What could change the
picture is a *future* source theorem deriving welding link (a) or (b) from retained
rows; that would couple the two walls and make the bridge necessary. No such
derivation exists on `origin/main` today, so the two walls stand independent.

### N3 - Hidden-wall scan

The phrases "self-imposed," "independent," "bridge," "reality-respecting,"
"terminal," and "single object" are **not** used as hidden retained inputs for the
localization. The explicit load-bearing inputs are finite and named:

- the tensor factorization `C^3 (x) C^2 (x) C^2` and the commutation
  `[H (x) I_2, I (x) sigma_i/2] = 0` (linear algebra, runner F1/F5);
- the circulant--Kahler commutation `[H, Jcs] = 0` for all `r` (linear algebra,
  runner F2);
- the nilpotency `(sigma_+)^2 = 0` and the exchange relations
  `[O_0,O_1]=0` vs `{c_0,c_1}=0` (linear algebra, runner F3);
- the retained tiers of the four authorities in the table above;
- the **prose status** of the two welding links, read directly out of the cited
  notes ("open, not a theorem" for (a); C1/C2-only for the CPT source under (b)).

No rhetorical phrase ("welds," "single terminal import") is doing proof work; each
is annotated as posited and traced to where it is asserted.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` (retained_bounded) | Chiral (`Gamma_chi`-anticommuting) generation mass on the generation `R^3`. | The VALUE residual: supply a `Gamma_chi`-anticommuting generation mass on `C^3`. | yes |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` (retained_no_go) | No dynamical forcing of CAR over hard-core-boson statistics on the site factor. | The CARRIER residual: select cross-site graded (CAR) statistics on `C^2`. | yes |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` (retained_no_go) | Discrete rotation does not fix the discrete exchange sign. | The CARRIER residual's cross-site exchange-sign question on `C^2`. | yes |
| `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` (retained_bounded) | C1/C2 generic discrete-symmetry commutation of a real anti-Hermitian `D`. | Source of `H=iD` only; it does **not** attack `sign(beta)`, Pfaffian, or Hodge. | no -- not load-bearing for either residual's *content*; cited only as the `H=iD` frame and as the authority link (b) over-reaches past |
| `koide_carrier_locus_decomposition_note_2026-06-01` (unaudited) | Asserts welding link (b); labels link (a) "open." | The bridge residual = the (open) product of the two factor-local residuals. | no -- context for the over-coupling, not a proof input |

The two factor-local residuals match the two retained gates **exactly**. The
**bridge residual** matches neither single gate -- it is the open *product* of the
two -- which is precisely why closing it is sufficient but not necessary. The CPT
and carrier-locus rows are explicitly marked non-matching and are not used as
load-bearing proof of the localization.

### N5 - Rhetoric audit

Broad phrases are scoped to the exact claim and disclaimed against over-broad
readings:

- "**self-imposed**" is scoped to: the welding of the two bits into one object is an
  assumption of the bridge program, because its two links are posited on
  `origin/main`. It does **not** mean the welding is false or that no future source
  theorem could establish it -- N6 leaves that path open.
- "**not necessary**" is scoped to: closing the bridge is not required to close the
  *carrier*, which closes when both factor-local residuals close. It does **not**
  mean the bridge is impossible or that the carrier is already closed.
- "**independent**" is scoped to: the two bits live on disjoint commuting tensor
  factors and each residual is attackable with no reference to the other. It does
  **not** assert the two are physically unrelated in the final theory; a derived
  link (a)/(b) would couple them.
- "**posited**" is scoped to the two named links having no retained derivation
  today; it is not a claim that they are wrong.

No "only," "last route," "closes the route," "exhausted," or finite-enumeration
framing is used. Both factor-local lanes are explicitly left open.

### N6 - Partial-closure path scan

Three non-axiom partial-closure paths remain open, none of them a new axiom or
import:

- **VALUE lane (`C^3`):** supply a `Gamma_chi`-anticommuting (chiral) generation
  mass via the off-generation-factor route the unaudited
  `koide_berry_monopole_bridge_reduction_note_2026-05-31` leaves explicitly
  **not** foreclosed (the `C^3` no-go blocks only the on-generation-factor route).
- **CARRIER lane (`C^2`):** select the cross-site graded (CAR) statistics over the
  native hard-core boson via the discrete graph-braid-framing / energy-positivity
  route on the site factor.
- **Re-merge path:** a future source theorem that derives welding link (a)
  (`records-Z_2 = sign(beta)`) or link (b) (`sign(beta) = Hodge bit`) from retained
  rows would couple the lanes and make the bridge necessary after all. This note
  predicts the unaudited capstones cannot promote those links without such a fresh
  source theorem; it does not call any of these three paths a new axiom.

### N7 - Steelman

The strongest objection to the localization is that a **single reality structure**
(CPT / the antiunitary `Theta`) governs both tensor factors, so the value and
carrier bits ought to be two faces of one `Theta`-orientation datum and the bridge
is forced. This is granted at the level of generic commutation: the retained CPT
source does give C1 (`Theta D Theta^{-1} = D`) and C2 (`[Theta_H, H] = 0`), which
constrain both factors. But the specific welding identities are strictly stronger
than C1/C2: `Theta` acting on the site factor does **not** fix the generation-factor
`sign(beta)` (the orientation of the value `Z_2`), and it does **not** fix the
cross-site exchange sign (hard-core boson vs fermion) -- both are left **free** by
`Theta`-commutation, and the cited source contains no `beta`/Pfaffian/Hodge content
(C3 demoted). So the steelman establishes a shared *constraint*, not a shared
*value*; it does not force the two free bits to be one object, and the scoped
localization survives.

### N8 - Cross-cycle echo

A recurring overclaim failure mode in this repo is to test **one representative
witness** (here: one welding identity, or one factor) and then declare the whole
lane -- "the carrier is closed" or "the bridge is the single terminal import" --
settled. The unaudited `koide_p1_collapses_frame_residuals`,
`koide_matter_attachment_graded_statistics_gate`, and
`koide_berry_monopole_bridge_reduction` notes each exhibit the same two-residual
shape, and the single-bridge framing risks inheriting the echo by treating the
posited weld as a closed object. This note avoids the echo by (i) keeping the claim
boundary at *localization* (two separable residuals) rather than closure of either,
(ii) naming both welding links as posited and tracing each to where it is asserted,
and (iii) leaving both factor-local lanes and the re-merge path open in N6. It
closes nothing it has not separately exhibited on disjoint tensor factors.
