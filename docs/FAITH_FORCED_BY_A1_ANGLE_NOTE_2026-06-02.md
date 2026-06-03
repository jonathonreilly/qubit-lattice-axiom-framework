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
