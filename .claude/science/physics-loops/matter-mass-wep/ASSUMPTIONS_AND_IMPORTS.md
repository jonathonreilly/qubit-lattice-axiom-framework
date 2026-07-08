# Assumptions and Imports — matter-mass-wep

Registry check performed 2026-07-08 against
`docs/audit/data/axiom_premise_nodes.json` + `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`.
Approved primitives consumed: `realized_state_primitive` (pointwise evaluation
at the supplied realized kinetic branch), `kinetic_isotropy_primitive`
(structural c_t = c_s where I-TIME needs the tick/edge footing). Everything
below the line is an explicit bounded import, NOT a primitive, NOT an axiom.

## Import ledger

| ID | Object | Role | Wired authorities | Retirement path |
|---|---|---|---|---|
| I-DYN | Real-time one-particle dynamics `H_eff = -log(T_2)/(2 a_tau)` from the free staggered two-step transfer | non-derivation premise; supplies evolution the axioms do not | `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`; dispersion note 2026-06-12; same premise shape as microcausality M2b | Dynamics existence is realized-sector data per owner ruling 2026-07-03; narrows no-go residual R1 to this chain; full retirement needs the realized kinetic-branch family to land |
| I-MASS | On-site mass sector with free coefficient m > 0 per species | supplies the on-site term the kinetic parent's licensed surface excluded | `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md` (forced leading-term class includes on-site mass) | value freedom is conceded permanently (no-go lambda-freedom); sector licensing retires when dynamics-form chain retains |
| I-TIME | Blocked-time normalization | units only; all identity/ratio claims are normalization-free | `kinetic_isotropy_primitive` (approved) + registered convention | approved primitive covers the structural part; residue is convention, not physics |
| I-EXT (block02) | Weak linear probe coupled to the conserved on-site Q-density, species-independent coefficient g | inertial probe; form to be classified on the licensed surface (classification lemma in block02), coefficient free | licensed-surface Q-conserving structure | explicitly NOT EP-S3a's mass-weighted `-m phi` coupling — using that would beg WEP; the I-EXT/EP-S3a relation IS block04's gamma question |
| I-INT (block03) | Supplied short-range two-body interaction | comparator/non-derivation role only; produces the binding defect `M = m1 + m2 - E_B` | none (declared comparator) | if not honestly declarable, drop bound-pair leg and record block04 weakening |
| EP-S3a (block04) | Normalized psi-squared source-readout + weak-field coupling form | bounded-support interface | `EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md` | already bounded-support; EP-S3b (coefficient identity) is the WALL, never imported silently |

Cascade note: the staggered realization (`AC_phi_lambda`) is itself an open
gate; expected downstream verdict `audited_conditional /
dependency_not_retained` — normal dependency bookkeeping per the skill.

## Counterfactual pass (hidden-choice audit)

| Implicit choice | What if wrong | Direction the alternative opens |
|---|---|---|
| Two-step transfer surface (not naive first-order kernel) | naive kernel gives exact `E^2 = m^2 + K(p)` and ratio 1 | naive kernel is a bigger un-wired dynamics import with O(g/m^2) adiabatic-leakage errors; transfer surface is the framework-native choice; keep naive-kernel comparison as a block01 lemma |
| Momentum centering p-bar = 0 | packets centered off-zero probe `E''(p-bar)` not `1/M_I` | generalization is free (theorem (b) is exact at any center); scaling-window claims quoted at p-bar = 0 only |
| Torus + vector-potential gauge for linear probe | position-gauge linear potential inconsistent with periodic BC | open-boundary position-space cross-check leg in the block02 runner |
| Q-density probe form (I-EXT) | if lawful on-site probes are NOT exactly the Q-density rays, coefficient-form freedom re-enters | block02 classification lemma must close this; failure = new named wall, surfaced not silently absorbed |
| Taste degeneracy treated as exact | taste-split masses would break the one-observable claim | runner symbol-scalarity check is exact-zero gated; nonzero = block01 kill criterion, pivot to per-taste observables |
| Free (bilinear) surface throughout | no bound states exist on it | binding defect only via declared I-INT comparator; persistence honestly rescoped (see block03 scope sentence) |
