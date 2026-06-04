# Does A1 force the faithful Weyl boost action? (FAITH-from-A1 angle)

**Date:** 2026-06-02
**Status:** review-only angle note (deliverable to /tmp; NOT for repo, NOT audited)
**Runner:** `/tmp/faith_forced_by_a1_check.py` (SCORECARD: PASS=18 FAIL=0,
verified with `/private/tmp/cl3-review-venv/bin/python3`)
**Angle:** Does A1 ("each site = one qubit = C^2 = the spinor of Cl(3,0)")
DIRECTLY FORCE the faithful Weyl (1/2,0) **boost/mass** rep, collapsing FAITH
from a residual to an axiom-consequence?

---

## VERDICT: **NO** — A1 does not force FAITH by itself. **Confidence: HIGH (~0.9).**

A1 forces the **state-space** carrier to be the 2-dim faithful Cl(3,0) spinor
(the j=1/2 module, not the 1-dim j=0 scalar). It does **not**, by itself, force
the reconstructed **boost / mass operator** to act on that C^2 as the faithful
(1/2,0) Weyl intertwiner rather than as a scalar multiple of the identity. The
faithful-vs-scalar selection of the *dynamical action* needs an **extra
ingredient** beyond A1 — the relativistic spin-1/2 kinetic kernel /
little-group content (equivalently, the matter-attachment pin). This matches
the live retained surface; it does not overturn it.

This is a **POSIT, not a DERIVATION**, *at the A1-alone level*: A1 *permits*
the faithful boost action and (once the boost is assumed to act through the
operator-frame Pauli triple) *uniquely identifies* it, but A1 alone does not
*force* the boost operator to be that action rather than a scalar.

---

## The decisive distinction (state space vs dynamical action)

The prompt's subtlety is the whole answer. Two logically independent things both
live on C^2:

- **STATE SPACE.** "The site is a qubit C^2" fixes the *Hilbert space* and the
  *operator algebra* M_2(C) = Cl(3,0). A1 forces this to be the **faithful j=1/2
  spinor** (the unique 2-dim faithful complex irrep of Cl(3,0)); the j=0 trivial
  rep is a **different, 1-dimensional** module — it is *not a qubit*. So at the
  level of "what space does matter live in", A1 *does* exclude the scalar
  **by dimension**. (Runner block A: faithful injective algebra map, rank 8;
  Schur-irreducible, commutant = scalars; J^2 = (3/4) I; j=0 carrier is 1-dim.)

- **DYNAMICAL (BOOST / MASS) ACTION.** FAITH is *not* about which space matter
  lives in. It is about **how the reconstructed boost (and hence the mass term)
  acts on that fixed C^2**: is it the faithful (1/2,0) Weyl generator
  K_i = i sigma_i / 2, or could it be a scalar K_i = c_i * I on the **same** C^2?
  A1 fixes the space; it does **not** dictate which operator on that space plays
  the role of the boost generator.

A1 collapses the *state-space* question. It leaves the *dynamical-action*
question open. FAITH is the dynamical-action question.

---

## What A1 DOES force (the part that is genuinely an axiom-consequence)

**(A) State space = faithful j=1/2 spinor, scalar excluded by dimension.**
The faithful complex irrep of Cl(3,0) has dim_C = 2 (retained:
`cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10`, via
`cl3_complexification_split_..._2026-05-10`). The trivial j=0 rep is 1-dimensional
and so is *not* a qubit. **A1 forces the carrier state space to be the spinor,
not the scalar.** (Runner A.1–A.4.)

**(B) IF the boost acts through the operator-frame Pauli triple, faithfulness is
forced (no scalar boost).** Using the *same* Pauli operators as J_i = sigma_i/2
(rotations) and K_i = bivector = i sigma_i/2 (boosts):

- {J,K} close so(3,1) with the Lorentzian minus sign [K,K] = -i eps J (runner B.1);
- **K = 0** (inert scalar boost) *fails* the bracket once J = sigma/2 != 0, in
  **both** so(3,1) and so(4) — **signature-free** (runner B.2);
- a **nonzero scalar** boost K_i = c_i * I also fails [J_i, K_j] = i eps K_k for
  J = sigma/2 unless c = 0 (runner B.3 — this is the sharper test the bivector
  notes state but do not isolate this cleanly);
- the only 2-dim so(3,1) completions of J = sigma/2 are the two faithful Weyl
  chiralities K = ± i sigma/2, *both* faithful, **no K=0 / scalar branch**
  (runner B.4).

This (B) is exactly the **retained-bounded** content of
`koide_faithfulness_rotation_scalar_excluded_note_2026-06-01`: *the
spatial-rotation scalar is excluded once J != 0.* It is real and it is forced —
**but it is conditional on the antecedent "the boost acts via the operator-frame
spatial-rotation triple."** That antecedent is precisely the open pin.

---

## What A1 does NOT force (the gap = where FAITH actually lives)

**(C) A1 + native dynamics do not force the boost to BE the operator-frame action
rather than a scalar on the same C^2.** Three independent facts (runner C):

1. **The native dynamics is spin-blind.** The single-component H = iD satisfies
   [H ⊗ I_2, I ⊗ B_i] = 0 (runner C.1; matches
   `koide_onsite_weyl_boost_from_bivectors_note_2026-06-01` §E, ledger
   `audited_conditional`). So the dynamics does **not** single out B_i as "the"
   boost generator. The dynamical lever *provably fails* to force faithfulness —
   this is on the live ledger, not my invention.

2. **A scalar boost is a legitimate rep on the qubit vector space.**
   S(eta) = exp(eta·c) I_2 is a perfectly good representation of the boost
   1-parameter subgroup on C^2 *as a vector space* (runner C.2, S(a)S(b)=S(a+b));
   it is simply non-faithful (its generator is the B.3-excluded scalar). Nothing
   in "C^2 is the qubit *state space*" forbids the boost *generator* from being
   c*I. The qubit being 2-dimensional forces the **state** space to be the
   spinor; it does **not** force the **dynamical** boost action to be faithful.
   This is the exact answer to the prompt's subtlety: **the 2-dimensionality of
   the qubit constrains the state space, not the boost generator.**

3. **The actual selector is an EXTRA ingredient (not "C^2 = spinor").** The thing
   that *does* exclude the scalar boost is the **relativistic spin-1/2 kinetic
   kernel**: the propagator numerator m I − i sigma·p has a **nonzero traceless
   part** (runner C.3a), so its Lorentz covariance *requires* the faithful
   intertwiner S = exp(eta·sigma/2) (runner C.3b), and the scalar S = I **fails**
   covariance (runner C.3c). This is the Weinberg covariant-field / little-group
   selector carried by the **retained-bounded**
   `koide_onsite_boost_reconstruction_weyl_faithful_vs_scalar_selection_note_2026-06-02`.
   It is a real forcing — but it is **NOT** a consequence of A1 ("the site is a
   qubit"); it is the **mass + Poincaré covariance of the reconstructed
   field**. That is precisely the matter-attachment / reconstruction (R)
   ingredient, which the `koide_faithfulness_rotation_scalar_excluded` note flags
   as the *dominant, upstream, signature-independent open pin*: its input
   `per_site_su2_spin_half` **explicitly disclaims** identifying the operator-frame
   C^2 action with "the physical spin generator of every matter excitation."

So the honest decomposition is:

```
  FAITH (boost/mass acts faithfully on C^2)
      <== A1 gives the STATE SPACE = faithful spinor (forced, by dimension)
      AND  IF boost = operator-frame triple  => scalar excluded (forced, B)
      BUT  "boost = operator-frame triple, not a scalar c*I"
           = matter-attachment pin  (NOT from A1; needs the relativistic
             spin-1/2 kernel + Poincare covariance, i.e. the reconstruction R)
```

A1 supplies the first two; it does **not** supply the bridge. FAITH therefore
**reduces to STAT-only only if** the matter-attachment/relativistic-kernel
selector is itself derived from A1+A2+retained — which it currently is not (the
selector that works rides the `retained_bounded`/`audited_conditional`/`unaudited`
reconstruction siblings, not A1 directly).

---

## Direct answer to "does the carrier reduce to STAT-only?"

**Not from A1 alone.** If the question is "can we drop FAITH and keep only the
cross-site CAR sign (STAT)?", the answer is **no at the A1 level**: A1 fixes the
spinor *state space* but not the faithful *boost/mass action*, so FAITH does not
collapse into A1.

There is, however, a genuinely **narrower** true statement, already retained on
main:

- **A1 forces FAITH at the level of the STATE SPACE** (scalar excluded by
  dimension — A1.4, the qubit is 2-dim, j=0 is 1-dim). This is an
  axiom-consequence.
- **The boost-action FAITH is reduced (not closed)** to the matter-attachment
  pin: "the matter field index transforms as the C^2 spinor under the
  reconstructed Lorentz action" — equivalently "the boost acts via the
  operator-frame Pauli triple, not as a scalar." This pin, **once granted**,
  forces faithfulness (B + the relativistic kernel). It is **not** granted by A1.

So the carrier residual is **STAT + (boost-action FAITH = the matter-attachment
pin)**, with the matter-attachment pin being the live open piece. The reduction
"FAITH → 0, carrier = STAT-only" is **not** available from A1; the reduction
that *is* available is "boost-action FAITH → the single matter-attachment pin"
(state-space FAITH being already an A1-consequence).

---

## Import flags

**None required for this angle.** The verdict uses only A1 (qubit = Cl(3,0)
spinor), the Lorentzian so(3,1) bracket, rotation/Casimir representation theory,
and the structure of the spin-1/2 kinetic kernel — all already on the retained /
retained-bounded surface. No new axiom, transcendental, PDG/fitted input, or
literature comparator is introduced.

The selector that *would* close the boost-action FAITH (the relativistic
spin-1/2 kernel + Poincaré covariance of the reconstructed massive field) is the
reconstruction (R) content, currently carried by
`koide_onsite_boost_reconstruction_..._2026-06-02` (`retained_bounded`,
massless-chiral level) with the **massive-doubling delivery as the named
residual**. If a future step claimed that this kernel-level selector follows
*from A1+A2+retained without the reconstruction siblings*, that would be the step
to flag — but no such claim is made here, and none is needed.

> IMPORT FLAG (latent, for the *closing* step, not this angle): asserting "the
> matter field index = the C^2 spinor under spatial rotations" as more than a
> posit — i.e. lifting `per_site_su2_spin_half`'s explicitly-disclaimed
> operator-frame action to the physical matter rep — currently has no
> A1+A2+retained derivation. Closing it without one would be an import requiring
> user approval.

---

## Ledger cross-check (verified on origin/main, 2026-06-02)

| Row | effective_status | Bearing on this angle |
|---|---|---|
| `cl3_faithful_irrep_dim_two_narrow_theorem_note_2026-05-10` | `decoration` (under `cl3_complexification_split`, `retained`) | State-space spinor (A) |
| `cl3_complexification_split_narrow_theorem_note_2026-05-10` | `retained` | State-space spinor (A) |
| `per_site_su2_spin_half_theorem_note_2026-05-02` | `retained` | Carries the **disclaimer** (matter pin) |
| `internal_external_su2_merger_..._2026-05-27` | `retained_bounded` | Operator-frame Spin(3) action (B antecedent) |
| `cl3_to_cl31_spinor_extension_..._2026-05-27` | `retained` | (3,1) signature / doubling algebra |
| `cpt_exact_real_anti_hermitian_d_..._2026-05-10` | `retained_bounded` | Native H=iD (spin-blind, C.1) |
| `koide_faithfulness_rotation_scalar_excluded_note_2026-06-01` | `retained_bounded` | (B) spatial-rotation scalar excluded; names matter pin as dominant |
| `koide_onsite_boost_reconstruction_..._2026-06-02` | `retained_bounded` | (C.3) kernel/little-group selector; massive doubling residual |
| `koide_onsite_weyl_boost_from_bivectors_note_2026-06-01` | `audited_conditional` | (C.1) dynamics spin-blind; faithful = residual posit |
| `no_per_site_chirality_theorem_note_2026-05-02` | `retained_no_go` | No on-site gamma^0 / boost-spin part |
| `anomaly_forces_time_theorem` | **`unaudited`** (INVALID as load-bearing) | (3,1) signature delegate — not used here |

My verdict is **consistent with** every retained / retained-bounded / retained-no-go
row above and does not lean on any `unaudited` row.

---

## No-go discipline gate (N1–N8)

**Status:** PASS for the narrow scoped claim only. The negative core being
gated is *not* "FAITH is false" and *not* "boost-action faithfulness can never
be derived." It is the single scoped statement: **A1 alone does not force the
reconstructed boost/mass operator to act faithfully on C^2** — because the
scalar boost `S(eta) = exp(eta·c) I_2` is a legitimate (non-faithful) rep on the
*same* qubit C^2, and the operator that excludes it (the relativistic spin-1/2
kinetic kernel) is matter-attachment content, not A1. The positive companion —
*state-space* FAITH (j=0 is 1-dim, excluded by dimension) — IS an A1-consequence
and is NOT being negated here.

### N1 — Alternative route enumeration

Routes by which A1 (or A1 + native dynamics) might be claimed to *force*
boost-action FAITH directly, each evaluated against the scoped claim.

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Dimension-collapse transfer | Reuse the state-space argument ("qubit is 2-dim, j=0 is 1-dim") to also fix the *boost operator* on that C^2. | A category slip: dimension fixes which *module* matter lives in (the spinor), not which *operator* on that fixed C^2 plays the boost generator. Both `K = i sigma/2` and `K = c·I` act on the same 2-dim space (runner C.2). | ATTEMPTED |
| Native-dynamics lever | Let `H = iD` single out `B_i` as "the" boost generator, forcing faithfulness. | `H = iD` is provably spin-blind: `[H ⊗ I_2, I ⊗ B_i] = 0` (runner C.1; `koide_onsite_weyl_boost_from_bivectors` §E, `audited_conditional`). The dynamical lever cannot select the boost operator. | ATTEMPTED |
| Operator-frame triple as forced | Assert the boost *must* act via the same Pauli triple as the rotations `J = sigma/2`, whence scalar excluded (B). | (B) is real and forced *conditional on that antecedent*, but the antecedent "boost = operator-frame triple, not c·I" is exactly the open matter-attachment pin; it is not delivered by A1. | ATTEMPTED |
| Bracket-closure squeeze | Use `[K,K] = -i eps J` so(3,1) closure to forbid `K = 0`. | Excludes only the *inert* `K = 0` and the *nonzero scalar* `c·I` once `J = sigma/2 != 0` (runner B.2–B.3) — but this is again conditional on `J` being the operator-frame triple, the same open antecedent, and it lives on `koide_faithfulness_rotation_scalar_excluded` (`retained_bounded`), not on A1. | ATTEMPTED |
| Kinetic-kernel route | Use `m I − i sigma·p` (nonzero traceless part) to force the faithful intertwiner. | This genuinely forces faithfulness (runner C.3a–c) — but it is the **relativistic spin-1/2 kernel + Poincaré covariance of the reconstructed massive field**, i.e. matter-attachment (R) content carried by `koide_onsite_boost_reconstruction_..._2026-06-02`, NOT a consequence of "the site is a qubit." | ATTEMPTED |
| Signature-import route | Have the (3,1) signature / `anomaly_forces_time` supply the boost rep faithfully. | `anomaly_forces_time` is **`unaudited`** (INVALID as load-bearing); not used. Signature fixes the algebra `cl3_to_cl31` enters, not the faithful-vs-scalar *action* on C^2. | NOT INVOKED |

### N2 — Wall-independence audit

The negative core collapses to **one** wall: *A1 fixes the qubit state space but
underdetermines which operator on that fixed C^2 is the boost generator.* The
apparently distinct routes in N1 (dimension-transfer, native dynamics, bracket
closure, operator-frame triple) are not independent walls — each one, when
pushed, reduces to the *same* missing antecedent "boost acts via the
operator-frame Pauli triple rather than a scalar `c·I`." Crucially, the gate does
*not* lean on any forcing-failure of (B) or the kernel route: (B) and the kernel
route both genuinely *succeed* at excluding the scalar — the wall is solely that
their **antecedent** (the matter-attachment identification) is not A1-derived.
Granting that single antecedent collapses the wall; nothing else in the cluster
needs to move.

### N3 — Hidden-wall scan (explicit load-bearing inputs)

The load-bearing inputs for the negative core are stated explicitly and none is
smuggled in as an unstated retained wall:

- **A1** = "site = qubit = C^2 = Cl(3,0) spinor" — used only to deliver the
  *state-space* spinor (positive side), `cl3_complexification_split` (`retained`)
  + `cl3_faithful_irrep_dim_two` (`decoration`).
- **Spin-blindness of `H = iD`** — `[H ⊗ I_2, I ⊗ B_i] = 0`, from
  `cpt_exact_real_anti_hermitian_d` (`retained_bounded`) /
  `koide_onsite_weyl_boost_from_bivectors` (`audited_conditional`). Load-bearing
  for "the dynamical lever cannot force faithfulness."
- **Legitimacy of the scalar boost rep** `S(eta) = exp(eta·c) I_2` —
  `S(a)S(b) = S(a+b)` is an elementary 1-parameter-group fact (runner C.2), not a
  retained import; it is the positive existence witness that A1 *permits* a
  non-faithful action.
- **The relativistic spin-1/2 kernel** is named as the *actual* selector and
  explicitly attributed to the reconstruction (R) sibling
  `koide_onsite_boost_reconstruction_..._2026-06-02` (`retained_bounded`), NOT to
  A1. The note does not let "covariance" or "Lorentz" act as a hidden A1-level
  wall.

The words "spinor", "Lorentz", "covariance", "boost" are not used as
load-bearing axiomatic content for the negative claim; their only forcing role is
explicitly routed to the matter-attachment pin, not to A1.

### N4 — Residual matching table

The gated negative claim must attack the *same* residual the cited cluster rows
leave open, not a softer or harder one.

| cited witness | residual it leaves open | residual attacked here | match? |
|---|---|---|---|
| `koide_onsite_boost_reconstruction_..._2026-06-02` (`retained_bounded`) | The faithful boost holds at the massless-chiral level; the **massive-doubling delivery** is its named residual, and the selector that works is the relativistic kernel (R content), not A1. | Whether *A1 itself* (not R) forces the boost-action FAITH. Verdict: it does not; the kernel selector is R, not A1. | yes |
| `koide_faithfulness_rotation_scalar_excluded_note_2026-06-01` (`retained_bounded`) | Excludes the *spatial-rotation* scalar once `J != 0`, and flags the **matter-attachment pin** as the dominant, upstream, signature-independent open piece. | Same matter-attachment pin, now isolated for the *boost/mass* action: it is what "boost = operator-frame triple" needs and what A1 does not supply. | yes |
| `koide_onsite_weyl_boost_from_bivectors_note_2026-06-01` (`audited_conditional`) | The native dynamics is spin-blind, so faithful boost = residual **posit** at the dynamical level. | The exact same spin-blindness (`[H ⊗ I_2, I ⊗ B_i] = 0`) is used to show the dynamical lever cannot upgrade the posit to A1-forced. | yes |
| `per_site_su2_spin_half_theorem_note_2026-05-02` (`retained`) | Carries the **disclaimer**: the operator-frame C^2 action is *not* identified with "the physical spin generator of every matter excitation." | This disclaimer is precisely the gap: lifting it is the matter-attachment pin, which A1 does not close. | yes |
| `anomaly_forces_time_theorem` (**`unaudited`**) | (Would-be (3,1)-signature delegate.) | Not attacked / not load-bearing — explicitly excluded as INVALID. | no (intentionally unused) |

Non-matching / invalid-status rows are not used as load-bearing support for the
negative claim.

### N5 — Rhetoric audit

Scope-controlling phrases used in this note and their guards:

- **"A1 does not force [FAITH]"** — scoped to the *boost/mass dynamical action*
  on C^2. It explicitly does NOT deny that A1 forces *state-space* FAITH (j=0
  excluded by dimension); the note states the positive half in the same breath
  ("What A1 DOES force"). The negative is about the operator, not the module.
- **"reduces to the matter-attachment pin"** — a *reduction*, not a closure. The
  note is explicit that the pin, *once granted*, forces faithfulness via (B) + the
  kernel; the claim is that A1 does not grant it, not that it is unreachable.
  "Reduces" never tightens to "refutes" or "closes."
- **"spin-blind"** — scoped to the *single-component* `H = iD` and stated as the
  precise commutator `[H ⊗ I_2, I ⊗ B_i] = 0`; it is not a global claim that the
  framework can never see spin, only that *this* dynamical lever does not select
  the boost generator.
- **"VERDICT: NO" / "permitted, not forced"** — both carry the qualifier "*at the
  A1-alone level*" / "*by itself*" throughout; no sentence claims faithfulness is
  false, un-derivable, or that the carrier is "STAT-only."

No phrase in the note silently widens the negative core beyond "A1 alone does not
force the boost-action FAITH."

### N6 — Partial-closure path scan

Three partial-closure paths remain open and are *not* re-labeled as axioms or
imports by this note:

1. **State-space FAITH is already closed** (A1-consequence by dimension) — a
   genuine partial win, not a residual.
2. **Boost-action FAITH conditional on (B)'s antecedent is closed** — granting
   "boost = operator-frame Pauli triple" forces faithfulness; the only open piece
   is the antecedent itself.
3. **The reflection-positivity / KMS / records route** (named in the bottom line)
   is the open positive path to *derive* "matter field index = C^2 spinor under
   the reconstructed Lorentz action" from A1+A2+retained — which would then
   collapse the boost-action FAITH via (B)+(C). The note flags closing it *without*
   such a derivation as an import requiring user approval (the latent IMPORT FLAG),
   and does not itself take that step.

### N7 — Steelman

The strongest objection: *"Once you accept that matter lives in the qubit C^2,
relativistic invariance of a massive field leaves no choice — the boost MUST be
the faithful Weyl intertwiner, so calling boost-action FAITH 'not forced by A1' is
pedantry; the spinor state space already entails it."* This is the best case for
collapsing FAITH into A1, and it is partly right: the relativistic spin-1/2 kernel
**does** force faithfulness (runner C.3). The steelman fails to break the *scoped*
claim because the forcing rides on the **massive relativistic field + Poincaré
covariance** (the kernel `m I − i sigma·p` and its nonzero traceless part), which
is *matter-attachment content* — it presupposes that the qubit index transforms
as the physical spin of a covariant massive excitation. That presupposition is
exactly what `per_site_su2_spin_half` *disclaims* and what A1 ("the site is a
qubit") does not state. So the steelman concedes the very pin the note isolates:
faithfulness is forced *by the reconstruction (R)*, not *by A1*. It correctly
blocks any claim that boost-action FAITH is *unreachable* — and the note makes no
such claim.

### N8 — Cross-cycle echo

Prior carrier-residual cycles in this lane repeatedly failed by conflating the two
things that both live on C^2 — the *state space* and the *dynamical action* — and
then declaring the residual closed (or, conversely, declaring the whole carrier an
unforced posit). Two specific echoes this note avoids: (i) the **over-collapse
echo** — using the by-dimension exclusion of j=0 to claim the *boost operator* is
also fixed (it is not; runner C.2 exhibits the scalar boost on the same C^2); and
(ii) the **over-pessimism echo** — declaring the carrier "STAT-only" or
boost-action FAITH unreachable, when in fact (B) + the kernel *do* force it once
the single matter-attachment antecedent is granted. The note keeps the claim
boundary exactly at "A1 alone does not bridge state-space FAITH to boost-action
FAITH," leaving the reflection-positivity / KMS / records derivation of that bridge
as live positive work rather than a closed wall.

## One-line bottom line

A1 forces the **spinor state space** (scalar excluded by dimension) and uniquely
identifies the faithful boost **if** the boost acts via the operator-frame Pauli
triple — but A1 alone does **not** force the boost/mass *operator* to be that
faithful action rather than a scalar on the same C^2. **FAITH is permitted, not
forced, by A1; it remains a posit pending the matter-attachment / relativistic-
kernel selector.** The carrier does **not** reduce to STAT-only at the A1 level.
The next path is exactly the one the three 2026-06-01/02 notes already point at:
derive "matter field index = C^2 spinor under the reconstructed Lorentz action"
from A1+A2+retained (reflection-positivity / KMS / records on the emergent-time
field), which would *then* collapse the boost-action FAITH via (B)+(C).
