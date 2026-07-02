# Fourth Axiom (Dynamics): the Minimal Non-Triviality + Realized-Branch Posit (PROPOSAL)

**Date:** 2026-06-29
**Type:** axiom proposal / scoping
**Claim type:** proposal
**Status:** **PROPOSAL.** Sets **NO** audit status, claims no theorem, grants no
promotion. **Owner + audit lane hold sole authority** over disposition, tier, and
any landing. Pre-validation draft: not yet panel/Codex-checked.
**Touches NO canonical / audit / publication file.** Does not edit
`docs/MINIMAL_AXIOMS_*.md`, `docs/audit/**`, `MISSING_DERIVATION_PROMPTS.md`, any
`*_EFFECTIVE_STATUS.md`, and runs no tracked-output rewriter.

```yaml
hypothetical_axiom_status: proposed_fourth_axiom
proposal_allowed: false
proposal_allowed_reason: "Pre-validation draft for owner/panel review; not a status-promotion request."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Why a fourth axiom is small, not large

The A1/A2/A3 baseline (Lattice, Quantum, Record) has no dynamics. But most of
what "dynamics" would supply is **already a theorem off Record**, and the rest is
**walled by two no-gos**. The fourth axiom must live in the narrow gap between:

- **Forced (not axiom content).**
  `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_..._BOUNDED_THEOREM_NOTE_2026-06-05`:
  record-preservation + locality + Hermiticity forces the evolution **form** into
  the gauge-invariant-local (Wilson) class — Wilson plaquette + covariant hopping
  + on-site mass as leading terms (bounded, given the two-endpoint Gauss and
  quantum-Darwinism record bridges).
- **Walled (must NOT be axiom content).**
  - `DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06`: the form-class still
    contains `H=0` and all couplings; class membership selects neither.
  - `FOURTH_AXIOM_RELOCATION_NOGO_OR_LOOPHOLE_2026-06-05`: any fourth axiom that
    selects **flavor moduli** by extremum/fixed-point dynamics lands on a
    distinguished dial point `r in {0, 1/2, 1}`; the observed **quark** moduli are
    generic (`r_up ~ 0.77`, `r_down ~ 0.60`, `r_nu ~ 0.24`), so extremum-dynamics
    is quark-falsified, and any generic-valued dynamics relocates a free coupling.

So the only residual a fourth axiom can honestly supply is the firewall's named
gap: **non-triviality** plus the **realized matter branch** — and explicitly
**not** the form (already forced), the couplings, the truncation, or the flavor
moduli (walled).

## The posit (Dynamics)

> **Dynamics.** The realized time evolution of the qubit lattice is a **nonzero**
> member of the gauge-invariant-local Hermitian class that Record-preservation
> forces, and its **matter kinetic kernel resolves the full one-site Clifford
> algebra** — equivalently, the realized readout context is the one in which all
> three grade-1 generators are active, so the matter kernel's zero set is the
> finite, point-like (codim-3, Dirac) branch rather than the scalar surface
> branch.

Two minimal clauses, each independent and each the smallest thing that defeats a
named ambiguity:

- **D1 — Non-triviality.** `H != 0`. (Defeats the firewall's `H=0` member; the
  "nontriviality/production premise" the firewall names as the missing selector.)
- **D2 — Realized branch (B-Z2 / full Clifford).** The realized matter kernel
  lies in the codim-3 (all-three-sigma-active, Dirac) sector. This is the
  contingent realized-state (P3) selection: laws do not pick the branch, the
  realized recording context does. It is hosted at the A3 <-> P3 seam (the
  central-sector decomposition resolving the full one-site Clifford algebra), not
  forced kinematically in A1.

## Supplied-vs-derived discipline (what D1/D2 do NOT add)

Mirroring the A2-correction hygiene, the posit supplies **only** D1+D2. It does
**not** supply, and must not be read as supplying:

- the dynamics **form** (forced upstream by Record-preservation, not here);
- **couplings** (`beta`, `g_bare`, matter coupling, mass, relative weights) — free;
- the **specific action functional** (Wilson vs heat-kernel vs Manton — the
  action-form no-go's residual) or the **minimality/truncation** choice;
- the **generic flavor moduli** (quark/neutrino `r`) — the relocation no-go's
  kinematic floor: one continuous modulus per sector. A fourth axiom that fixed
  these would be quark-falsified or a relocation; D1/D2 deliberately do not touch
  them;
- **Born weights / probabilities / occupancy** — a separate measurement question
  (Record disclaims it; Dynamics does not supply it either);
- the **clock rate / absolute scale / lattice spacing** (the "scale is the clock
  rate" no-gos; `scale_reference_primitive` is separate);
- the **gauge group**, particle masses, EWSB, strong-CP `theta`, or any
  boundary/initial data.

## Why D2 is legitimate where a moduli-selector is not

The relocation no-go falsifies fourth axioms that select moduli by landing on a
**distinguished dial point**. D2 does not select a modulus — it selects a
**branch** (scalar surface vs Dirac point-node), a binary realized-state fact, not
a continuous `r`. Its one quantitative consequence is **structural, not extremal**:
the same full-Clifford operator on the hw=1 orbit is an anticommutant of the
chiral grading `Gamma_chi`, so any eigenvector lies on the chiral-null cone
`<v|Gamma_chi|v> = 0`, i.e. the charged-lepton special point `r = 1/2` (`Q = 2/3`).
This is exactly **opening (1)** flagged by the relocation no-go ("a distinguished
parameter-free *spectral* invariant of a C3-native flavor operator on the hw=1
orbit"). It pins the **lepton** point and **leaves the generic quark/neutrino
moduli free** — consistent with both horns of the no-go, which is why D2 escapes
it where a moduli-selector cannot. (Scratchpad demonstration 2026-06-29: a Koide
`H` built from qubit-Pauli words on the hw=1 triplet, `{H, Gamma_chi}=0`,
all-positive eigenvector gives `Q = 0.666661`.)

## What the four-axiom combination unlocks (and what it does NOT)

Adding D1+D2 on top of {Lattice, Quantum, Record + the Record dynamics-form
theorem}:

**UNLOCKED / upgraded (candidate — each needs its own audit):**

- **U1 — Dynamics exists.** "There is a nonzero gauge-invariant-local
  Hamiltonian." (Form from Record-theorem; non-triviality from D1.) Removes the
  `H=0` ambiguity the firewall isolates.
- **U2 — d=3 as a derivation, not a posit (the original goal).** D2 supplies the
  `phi=-1` / B-Z2 carrier bit (finite point-like matter zero set). With B-Z2 in
  hand the d<=3 upper leg (the `M_2(C)` anticommutant cap <= 3 self-adjoint
  anticommuting unitaries) and the d>=3 lower leg (`Z^d` Polya transience) close
  to **d = 3**. The standing blocker on "weaken A1's `Z^3` to a derived `Z^d`
  cap" was exactly this un-supplied bit (`D3_NATIVE_UNBLOCK` /
  `PHI_MINUS_ONE_SELECTOR_ATTACK`). This is the headline unlock.
- **U3 — P-DECAY + P-FIELD downgrade.** With the kernel form (isotropic Dirac) +
  d=3, the static lattice Green function normalizability (P-DECAY) and
  static-response-governed-by-`L^-1` (P-FIELD) become **consequences** of
  transience rather than separate posits — candidate posit->theorem downgrades.
- **U4 — Matter chirality.** Forced once the realized branch is the
  full-Clifford/Dirac one ({eps, D} = 0 is automatic in-branch).
- **U5 — Charged-lepton Koide `r = 1/2`, structurally.** Per D2's chiral-null
  consequence above (relocation-no-go opening 1). PARTIAL: lepton only.

**NOT unlocked (honest residual — the frontier that remains):**

- **R1 — Generic flavor moduli** (quark/neutrino `r`): free continuous inputs
  (relocation no-go, both horns). The kinematic floor stands.
- **R2 — Couplings / `beta` / the specific action** (Wilson vs heat-kernel vs
  Manton): action-form no-go; free.
- **R3 — Born rule / probabilities / occupancy:** a **measurement** question, not
  a dynamics one. This is the next keystone after Dynamics, not part of it.
- **R4 — Clock rate / absolute scale / lattice spacing:** the "scale is the clock
  rate" no-gos; separate `scale_reference_primitive`.
- **R5 — Gauge group, masses, EWSB, `theta`:** downstream of the form-class.

**Reading.** The fourth axiom closes the d=3 derivation (U2) and tidies the
propagation posits (U3), at the cost of only a two-clause non-triviality+branch
premise — because Record already did the heavy lifting on the form. It pointedly
does **not** crack the flavor moduli or the couplings (walled), and it makes
explicit that the **next** frontier is a **measurement / Born** posit (R3), not
more dynamics.

## Validation gate (before any PR / status change)

Per standing practice: a 10-physicist BEFORE/AFTER blind panel (Opus 4.8 MAX) +
Codex cross-check on (a) the two-clause minimality, (b) the no-smuggling of form/
couplings/moduli, (c) the U/R unlock ledger's honesty, before this is offered as
anything beyond a source-note proposal. Audit status remains the audit lane's.

## Load-bearing inputs

- `MINIMAL_AXIOMS_2026-06-05.md` (Lattice/Quantum/Record baseline).
- `DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md` (the form is forced).
- `DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md` (the residual = non-triviality + couplings + truncation).
- `FOURTH_AXIOM_RELOCATION_NOGO_OR_LOOPHOLE_2026-06-05.md` (moduli-selection walled; opening 1 = hw=1 spectral invariant).
- `D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md` / `PHI_MINUS_ONE_SELECTOR_ATTACK_PROPOSAL_2026-06-23.md` (d=3 legs; `phi=-1` is the un-supplied bit D2 supplies).
- Scratchpad `p213_coexistence.py` (2026-06-29): the hw=1 Clifford Koide operator and the B-Z2<->Koide common-parent demonstration.
```

## PANEL OUTCOME (2026-06-29) + REVISION

Blind 10-physicist panel (Opus 4.8, max rigor), given ONLY the four axiom
statements as context. **Tally: 10/10 needs-revision** (0 unsound, 0 clean).
Verdict direction: the **core survives**; the **wrapper smuggles**. Convergent
findings:

1. **Split by TYPE, not just clauses (≈all seats; sharpest: philosopher,
   axiomatic-QFT).** D1 is a *law* (a nonzero local self-adjoint generator
   exists); D2 is a *contingent realized-state* fact (which branch actualized). A
   law-axiom cannot carry a contingency without a type error. Re-file D2 as an
   **approved primitive** (the framework's existing axiom-vs-primitive seam; this
   is P3 `realized_state`), not an axiom clause.
2. **Redundancy ambiguity, resolved by the split (operator-alg, Occam).** D2
   implies D1 (a kernel resolving the full algebra is nonzero), so D1 is redundant
   under a present-tense reading but non-redundant under the contingent reading —
   the axiom never disambiguates. Splitting fixes it: D1 stays the law; the
   counterfactual scalar realization satisfies D1, fails the D2-primitive.
3. **The codim-3 geometry smuggles a 3<->3 bridge (skeptic [headline], QI, band,
   philosopher, Occam).** "Resolves the full one-site Cl(3,0)" is an *internal/
   algebraic* fact (Axiom 2); "codim-3 point node on Z^3" is a *geometric* fact
   (Axiom 1). The inference needs a bijection between the three grade-1 generators
   and the three lattice axes — the observable bridge Axiom 2 disclaims, and the
   *same* grade-3<->spatial-3 coupling already flagged open in the A2 correction.
   Fix: state the algebraic core only; make "codim-3 => point node" a downstream
   consequence conditional on the separately-named bridge.
4. **"matter / Dirac / kinetic / massless" contradict the disclaimer (all
   seats).** They import species/particle-content + a kinetic/mass split that
   Axioms 2-3 disclaim. Drop them; use "full-grade-1 / grade-0 (scalar)".
5. **The branch is a 4-rung ladder, not a binary (band [headline], SM, lattice).**
   #active grade-1 generators = 0/1/2/3 -> extended / surface / nodal-LINE /
   point. The "scalar-surface vs Dirac-point" binary deletes the codim-2 line, the
   bare "=>" overclaims (full resolution *permits*, not *forces*, a nonempty
   point), and "scalar = surface" is codim-1 not codim-0.
6. **Basis-dependence (operator-alg).** "The three grade-1 generators" presupposes
   a chosen triple; the invariant statement is "acts irreducibly on the one-site
   M_2(C) (trivial commutant)".
7. **Missing time-ordering companion + record compatibility (GR [headline],
   skeptic, axiomatic-QFT).** "Nonzero time evolution" presupposes an *ordered*
   parameter and a single global clock; nothing posits even the bare existence of
   the ordering (rate/arrow stay rightly deferred — self-adjoint => t->-t
   symmetric, so no arrow smuggle). Also: self-adjoint => reversible vs durable
   (irreversible) record is consistent only if the generator preserves the
   Axiom-3 central sector — an unstated requirement.

### REVISED (post-panel)

**Axiom 4 — Dynamics (LAW only).** Time evolution is nonzero: there is a
one-parameter evolution ordered by a primitive evolution parameter (its existence
posited; rate, scale, metric, and arrow/orientation deferred), generated by a
local self-adjoint operator that acts compatibly with the Axiom-3 central (record)
decomposition. Supplies the existence of a nonzero, local, self-adjoint generator
and the bare time-ordering, compatible with records. Does NOT supply: the
generator's specific form / couplings / truncation, the clock rate / scale /
spacing, the arrow / orientation, Born weights / probability / occupancy, species
/ particle content, or any gauge group.

**Realized-branch primitive (contingent; P3 `realized_state`) — re-homed from old
D2.** The realized generator acts irreducibly on the one-site algebra `M_2(C)`
(trivial commutant; equivalently it saturates the grade-1 sector) — the maximal
(codim-3) rung of the resolution ladder {grade-0 scalar -> ... -> full grade-1}.
This is contingent realized-state data (Axiom 3's realized outcome), not a law.
The geometric reading "codim-3 => isolated point node on `Z^3`" is a downstream
consequence **conditional on a separately-posited bijection between the one-site
grade-1 directions and the three `Z^3` axes** — the grade-1<->spatial-3 bridge
(the same coupling flagged open in the A2 correction).

### Consequence for the unlock ledger

U2 (d=3 derived) is **not free**: it rests on the grade-1<->spatial-3 bridge,
which the panel isolated as the true load-bearing residual. The four-axiom set
derives "the carrier supports a codim-3 / point-node branch" and "`Z^3` is
spatially 3D" *separately*; identifying them is the bridge. So the sharpened
keystone after Dynamics is **that bridge**, not more dynamics and not Born.

## RE-PANEL (confirmation) + BRIDGE ATTACK (2026-06-29, second pass)

**Re-panel of the revised draft (7 concern-raising seats, each handed the revision +
their prior objection): 1 closed, 6 partially-closed, 0 not-closed.** The structural
objections from round 1 are CLOSED — altitude/type (law vs contingent primitive),
modal ambiguity, the "matter/Dirac/kinetic" smuggle, the false binary (4-rung ladder
restored), basis-dependence (→ trivial commutant), and the D1 redundancy. The
remaining residuals are a tight, convergent set of **wording sharpenings**, no
structural reopening:

- **R-a (record-compat, 3 seats).** "acts compatibly with the central decomposition"
  is too loose; pin it to `[H, central record projectors] = 0` (H block-diagonal,
  preserves each record sector).
- **R-b (operator-alg, sharp).** "irreducible" must mean the **Bloch family `{H(k)}`
  has trivial JOINT commutant**, NOT a single generator — a lone self-adjoint
  generator on `M_2(C)` always has a >=2-dim commutant (its spectral projections).
- **R-c (band + operator-alg, independently).** Grade-1 saturation pins codim-3 only
  GENERICALLY; a symmetry-locked `d(k)=(f,f,g)` keeps all three Paulis active yet
  gives a codim-2 LINE. The top rung needs a **transversality / full-Jacobian-rank /
  nonzero-monopole-charge** clause.
- **R-d (GR).** "one-parameter" still hides the **single global clock** (one shared
  parameter synchronizing all `Z^3` sites with no posited foliation) — make it
  explicit.
- **R-e (skeptic + GR).** "ordered" imports **orientability**; only the **arrow** is
  deferred. And the arrow is **unowned** across the whole set — flag it explicitly.

**Bridge attack (`scratchpad/bridge_attack.py`, reproducing ADJACENCY_RANK_QUBIT_
CLIFFORD_BOUND T1-T3 by hand): the grade-1<->spatial-3 bridge is NOT a free posit —
it is DISCHARGED by the Dynamics kinetic kernel.**

- **T2 (verified):** the kernel's Dirac-square / no-spin-lattice-cross-term condition
  (`D^2 = Laplacian*I`) holds **iff** the per-direction coefficients are mutually
  anticommuting self-adjoint unitaries = grade-1 generators. The kernel IS the glue,
  and the gluing is forced, not arbitrary (hostile witness `(sx+sy)/sqrt2` fails).
- **T1 (verified):** `M_2(C)` admits at most 3 such generators (4th-element nullspace
  = 0). So codim <= 3.
- **T3 + codim (verified):** a point node (codim = d) needs `#active = d`; the cap
  gives `d <= 3`, and `d = 3` SATURATES. The `Z^3` symbol `sum sigma_mu sin(k_mu)`
  has exactly the 8 TRIM corners as isolated nodes, and its Jacobian is full-rank
  there (cos = +-1) — so **R-c's transversality holds automatically for the realized
  Dirac-square carrier** (the nodes carry nonzero monopole charge).

So the skeptic's "d=3 posited twice and glued" is answered: the identification is a
**theorem** of the Dirac-square kinetic kernel + the qubit capacity. The residual
narrows from "a bijection" to: **(a) carrier-class** — that the realized kernel is
first-order Dirac-square (this IS the realized-branch primitive); **(b) saturation**
— `d=3` over `d<3`, closed by the lower leg (`d>=3` from propagator normalizability /
transience). **Honest status: `d <= 3` FORCED (qubit Dirac-square capacity) AND
`d >= 3` FORCED (transience) => `d = 3`, modulo the single realized-branch primitive
+ the lower-leg P-DECAY posit.** The bridge retires as a separate residual.

### FINAL revised draft (post re-panel + bridge)

**Axiom 4 — Dynamics (LAW).** Time evolution is nonzero: a single global one-parameter
group (one shared, orientable evolution parameter synchronizing all `Z^3` sites; its
rate, scale, metric, and arrow deferred), generated by a local self-adjoint operator
`H` that commutes with the Axiom-3 central record projectors (`[H, P_c] = 0` —
preserves each record sector). Supplies: a nonzero, local, self-adjoint generator; the
bare orientable un-arrowed global time-ordering; record-sector preservation. Does NOT
supply: the generator's form/couplings/truncation, the clock rate/scale/spacing, the
time **arrow** (unowned across the whole set — flagged open), Born/probability/
occupancy, species/particle content, or any gauge group.

**Realized-branch primitive (contingent; P3 `realized_state`).** The realized Bloch
family `{H(k)}` over the Brillouin torus has **trivial joint commutant** — equivalently
the realized kernel is in the first-order Dirac-square (no spin-lattice cross-term)
class, saturating the qubit's grade-1 capacity. By T1+T2 this **forces** one
anticommuting grade-1 generator per lattice direction (the grade-1<->axis
identification is a consequence, not a posit) and caps the adjacency rank at 3; on
`Z^3` the gap-closing locus is the codim-3 set of isolated point nodes, each
transversal (full-rank symbol Jacobian => nonzero monopole charge). The one-site
carrier saturation (this primitive) and the global record-sector preservation (the
LAW) are at **different levels** — the record central projectors are sector/global,
not the one-site `M_2(C)` center — so they coexist without tension. Residual:
(a) carrier-class (this primitive); (b) saturation `d=3` vs `d<3` (closed by the
lower-leg `d>=3`).
