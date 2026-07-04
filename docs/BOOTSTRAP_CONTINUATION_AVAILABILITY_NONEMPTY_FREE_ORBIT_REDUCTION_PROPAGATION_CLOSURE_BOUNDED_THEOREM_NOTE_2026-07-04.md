# The Bootstrap Continued: "Records Form" Makes the First Availability Set Nonempty, Every Orbit With Proper Symmetry Is Automatically Achiral (Chirality Requires a Free Off-Mirror Orbit), and Achirality Propagates — an Achiral Rule Keeps the Reachable Class Flip-Closed Inductively, While a Chiral Rule Breaks One-Step Closure at a Reachable Configuration (Bounded Theorem)

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact orbit/stabilizer classification,
universal one-step closure statements, and explicit toy-model witnesses;
the toy rules are named toys; not a determination of the framework's fixed
rule).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire
or re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/bootstrap_continuation_nonempty_free_orbit_propagation_closure_2026_07_04.py`](../scripts/bootstrap_continuation_nonempty_free_orbit_propagation_closure_2026_07_04.py)
**Runner cache:**
[`logs/runner-cache/bootstrap_continuation_nonempty_free_orbit_propagation_closure_2026_07_04.txt`](../logs/runner-cache/bootstrap_continuation_nonempty_free_orbit_propagation_closure_2026_07_04.txt)

## Question

The empty-state bootstrap left two named targets: the locus class of the
first availability set `A0`, and whether achirality — if the rule has it —
propagates past the first step. The premises are the Record axiom's
sentences "Records form." and "When present, a record locks exactly one
admissible local possibility"; the state definition ("A state is a
configuration of records", `I(empty) = 0`); and the Admissibility
covariance sentence
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)).

## Answer

1. **Nonemptiness (Theorem 1 — the first derivation consuming "Records
   form.").** Records occur; each locks an available possibility; the
   first record's availability set is `A0`. Hence `A0` is **nonempty**,
   and with proper-cubic invariance it **contains a full proper orbit**.
   The bootstrap is not vacuous: the realized alphabet has at least one
   orbit's worth of contents.

2. **Free-orbit reduction (Theorem 2).** Every content orbit with a
   nontrivial proper stabilizer lies on a rotation axis of the cubic
   group (all 23 nontrivial proper elements' axes computed), every such
   axis is improper-stabilized, and every such orbit is therefore
   inversion-invariant — **automatically achiral**. Orbit size below 24
   is equivalent to nontrivial proper stabilizer. So set-level chirality
   of `A0` requires a **free (trivial-stabilizer) orbit off the mirror
   loci**, unpaired with its twin: everything with any symmetry at all is
   derivably safe, and the locus-class question reduces to the free
   off-mirror part of `A0`.

3. **Propagation closure (Theorem 3).** If the rule is achiral — its
   availability function even under the improper flip — then **one-step
   closure holds universally**: for every configuration `C` and site
   `s`, `avail(flip C, s) = flip(avail(C, s))`. Since the empty state is
   flip-fixed, induction gives: **the reachable configuration class is
   closed under the flip at every record count** (endpoint witness: full
   breadth-first enumeration to depth three on the `L = 2` quotient,
   every layer flip-closed). Conversely, a chiral rule breaks one-step
   closure **at a reachable configuration**: in the toy model, the odd
   channel `J2 = sum det(d, e, c(e))` over recorded slot pairs drives a
   threshold shift, and the explicit two-record witness has
   `J2(C) = +2`, `J2(flip C) = -2`, with `avail(C)` equal to **all six**
   candidates and `avail(flip C)` **empty** — the flipped configuration
   is a dead end while the original is fully open, and the witness is
   reachable in two verified formation steps. Chirality is not a
   first-step artifact: it propagates as a class asymmetry exactly when
   the rule spends the bit, and never otherwise.

4. **Parity protection on the `L = 2` quotient, and spontaneous
   registration (Theorem 4).** On the `L = 2` torus the two slots of
   each axis read the same neighbor, so every slot pattern is
   antipodally duplicated — and the `J2` channel **vanishes identically**
   (direction-sensitive rule chirality needs `L >= 3`). Meanwhile, under
   the achiral rule a single history can register a nonzero `J2`
   (orientation registered in the configuration) while its flipped
   history is equally reachable, step by verified step: class-level
   symmetry with configuration-level breaking — the state-versus-law
   separation, witnessed dynamically.

**Continuation summary.** The realized alphabet starts nonempty by axiom;
everything in it with any proper symmetry is derivably orientation-free;
and the one bit, if the rule ever spends it, shows up as a reachability
asymmetry that no achiral rule can produce and every chiral rule must.
The remaining question is unchanged in kind but smaller in size: the free
off-mirror part of the availability structure.

## Authorities and premises

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — quoted:
  "Records form."; "When present, a record locks exactly one admissible
  local possibility"; "A state is a configuration of records";
  `I(empty) = 0`; the Admissibility sentences ("one fixed
  nearest-neighbor admissibility rule, covariant under lattice
  translations and proper cubic rotations"; "the available possibilities
  are determined by, and vary with, the nearest-neighbor conditions");
  the open-gates item placing formation rules downstream.
- [`READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md`](READING_NOTE_FINAL_DERIVATIONS_MOTION_CLOSURE_BOUNDED_NOTE_2026-07-02.md)
  — condition typing (record absence included).
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
  — the realized-state reading (contents as polar vectors; the toy's
  axis-vector contents are its simplest instance).
- The empty-state bootstrap (first availability set proper-invariant,
  orbit dichotomy, degree-nine wall) and the coupled cubic action are
  carried from in-review companions (prose references only, not
  dependency edges); the pieces needed here are re-earned by the runner.

## Theorem statements and proofs

### Theorem 1 (nonemptiness from "Records form.")

*Proof.* "Records form." puts occurrence at axiom strength: records are
not merely possible but occur. Each record "locks exactly one admissible
local possibility" — an element of the availability set at its formation
step. The first record forms at the empty state, whose availability set
at every site is `A0` (all-open conditions, translation covariance). A
lock requires an element: `A0 != empty`. Proper-cubic invariance (the
bootstrap constraint) then puts the full proper orbit of any member
inside `A0` (A1, model-checked closure). No claim is made about which
element the first record locks — formation selection is explicitly
downstream.

### Theorem 2 (free-orbit reduction)

*Proof.* A point with nontrivial proper stabilizer is fixed by some
nontrivial proper rotation, hence lies on its rotation axis; the 23
nontrivial proper elements' axes are computed and each is
improper-stabilized (A2); improper-stabilized points have
inversion-invariant orbits (the bootstrap dichotomy, re-earned at A3
together with the equivalence orbit-size `< 24` iff nontrivial
stabilizer). Model unions witness the reduction: symmetric orbits plus
mirror-plane orbits in any combination remain inversion-invariant;
adding a single free off-mirror orbit breaks it; adding its twin
restores it (A4). Hence chirality of any proper-invariant availability
set is carried exclusively by unpaired free off-mirror orbits.

### Theorem 3 (propagation closure and its converse witness)

*Proof.* Let `Phi` be the improper flip on configurations. If the rule
is achiral, `avail(Phi C, s) = Phi(avail(C, s))` for all `C, s` — in the
toy, verified exactly on 200 random partial configurations (B3); the
general statement is the definition of rule achirality applied
configuration-wise. `Phi(empty) = empty`, so by induction every
formation sequence maps to a valid formation sequence under `Phi`, and
each reachable layer is `Phi`-closed — witnessed end-to-end by the full
depth-three enumeration on the `L = 2` quotient (B4, layer sizes
reported). For the converse, the chiral toy rule shifts its threshold on
the sign of the proper-covariant, flip-odd channel `J2` (B1); the
explicit witness configuration is reachable in two verified steps and
has `avail(C)` all-six versus `avail(flip C)` empty (B5) — one-step
closure fails at a reachable configuration, so the reachable class is
flip-asymmetric from the third record onward. The chiral rule remains
proper-covariant (B6): the asymmetry is precisely improper, the one bit.

### Theorem 4 (parity protection at L = 2; spontaneous registration)

*Proof.* On the `L = 2` torus, `+d` and `-d` neighbors coincide, so
every readable slot pattern carries the same content at antipodal slots;
`J2` then cancels pairwise in its `d`-sum — identically zero on 50
random duplicated patterns (B2). So the quotient itself protects parity:
no direction-sensitive odd channel can fire below `L = 3`. Separately, a
three-record history under the achiral rule reaches a configuration with
nonzero `J2` at a site — an orientation registered in the state — while
the flipped history is verified reachable step-by-step (C1): the class
is symmetric, the individual configuration is not, and nothing lawful
distinguishes the pair.

## What this note does and does not claim

- **The toy rules are toys.** They witness the closure/violation
  structure exactly; no claim is made that the framework's fixed rule is
  either of them, or that it is achiral or chiral.
- **Theorem 1 uses only occurrence.** "Records form." supplies that
  records occur; which record, where, and with what weight remain
  downstream, and nothing here constrains them.
- **Theorem 3's converse is a witness, not a universal converse**: it
  shows a chiral rule CAN break closure at a reachable configuration
  (and the toy does, maximally); whether every chiral rule's
  distinguishing condition is reachable depends on the rule and is not
  claimed.
- No fermion-sector claims; no measured quantities; no imports.

## Residuals and next paths

1. **The free off-mirror part of `A0`**: the locus-class question is now
   exactly this — any derivation showing the all-open availability set
   avoids unpaired free off-mirror orbits (or must contain them) settles
   the realized-alphabet bootstrap. The safe/dangerous split is fully
   classified; what remains is which side the fixed rule's `A0` sits on.
2. **Quotient-size thresholds**: the `L = 2` parity protection suggests a
   graded family — which odd channels first fire at which lattice
   quotients — a possible tool for bounding rule chirality by locality
   range.
3. **Reachability-asymmetry as an audit target**: any proposal of a
   chiral rule now predicts a concrete signature — a flip-asymmetric
   reachable class from some finite record count onward — giving future
   accounts a named, checkable consequence.
