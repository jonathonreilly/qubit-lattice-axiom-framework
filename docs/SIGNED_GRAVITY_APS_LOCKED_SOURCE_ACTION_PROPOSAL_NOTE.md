# Signed Gravity APS-Locked Source Action Proposal

**Date:** 2026-04-25 (2026-05-28: Origin obligation sharpened to a single
derivation target — the generation-chirality grading — see panel section).
**Type:** open_gate
**Claim type:** open_gate
**Status:** **open gate, sharpened** — the proposed `χ_η M_phys ⟨ρ,Φ⟩`
source-action cross term is not supplied by the current retained inventory. The
7-angle panel localizes the known route to a generation/orientation-factor
**chiral grading** `Γ` anticommuting with `D_Y` (the same gate type appearing in
the Koide-Q=2/3 / generation-ID chirality lanes). Deriving such a grading is the
frontier target; sufficiency still has to be checked by the resulting
construction rather than asserted here. Under no-admissions the grading must be
**derived**, not admitted. The local source/response harness passes but is not a
derivation.
**Script:** [`../scripts/signed_gravity_aps_locked_source_action_proposal.py`](../scripts/signed_gravity_aps_locked_source_action_proposal.py)
**Cached log:** [`../logs/runner-cache/signed_gravity_aps_locked_source_action_proposal.txt`](../logs/runner-cache/signed_gravity_aps_locked_source_action_proposal.txt)

## 2026-06-07 Exact-Source Boundary Manifest

This note is the exact source-action proposal row for the inserted term

```text
S_int = - chi_eta M_phys <rho, Phi>.
```

Its direct runner claim is conditional: once this term is inserted, finite
variation, source/response locking, source-unit conversion, and fixed-sector
Born/unitarity controls pass. The runner does not derive the term.

The strongest current retained-route statement is negative and already lives
on the signed-gravity lane: retained separable APS/Wald/Gauss ingredients span
only the orientation-even positive source vector `[+1,+1]` plus source-neutral
spectator vectors `[0,0]`. They do not span the required orientation-odd source
vector `[+1,-1]`; the latter appears only after the explicit cross term is
added. This is the scope of
`SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE.md`.

The strongest current positive host statement is also narrower than source
closure: the finite `Cl(3)`/`Z^3` determinant-line package derives a
source-character grammar and naturally hosts a real orientation line, but the
host is a `Z2` torsor/local system and does not canonically choose the section
or force the active `chi_eta rho Phi` source action. This is the scope of
`SIGNED_GRAVITY_CL3Z3_SOURCE_CHARACTER_DERIVATION_NOTE.md` and
`SIGNED_GRAVITY_NATURALLY_HOSTED_ORIENTATION_LINE_NOTE.md`.

Therefore the current exact-source status is:

```text
retained APS/Wald/Gauss source-action derivation: blocked
determinant orientation-line host: present but not canonically selected
source-action term: open_gate conditional ansatz, not retained
```

To move this row beyond open-gate status, a later retained theorem must derive
a canonical orientation-section/source principle and protected eta sector from
the current axiom surface, then rerun the variation/table checks here. This
note does not introduce a new axiom and does not mark that source principle as
admitted.

## 2026-06-12 Source-Action Hard Residual

The local variation/table harness is not the missing science: it closes
only after `S_int = - chi_eta M_phys <rho,Phi>` is inserted. The live
frontier is the origin of that cross term.

Current retained signed-gravity ingredients still split into the same
two honest facts:

- separable APS/Wald/Gauss source terms and positive mass/area carriers
  span orientation-even sources plus spectators, not the required
  orientation-odd `[+1,-1]` source vector;
- determinant-line/orientation-line structure hosts a `Z2` label but
  does not canonically select a section or force an active local
  `chi_eta rho Phi` variation.

The best positive route remains the generation/cochain/taste grading
program described below: derive a non-transportable chiral grading,
then prove that it selects the APS-locked scalar source term and a
protected eta sector. This note does not add that grading as a premise,
does not introduce a new axiom, and does not promote the proposal while
the source-action origin is open.

Source-surface summary: this remains an open-gate source-action target. The
live blocker is a derivation of the APS-locked `chi_eta rho Phi` source action.
No retained-grade proposal or status promotion is made here; the independent
audit lane remains the only authority for effective status.

## 2026-06-15 Bridge-Audit Source Bundle

This source packet now binds its open-gate boundary to the executable
APS/Wald/Gauss bridge audit instead of relying only on prose lineage:

- [`SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md`](SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md)
  states the current retained-route result:
  `FINAL_TAG: APS_WALD_GAUSS_BRIDGE_NOT_DERIVED`.
- [`scripts/signed_gravity_aps_wald_gauss_bridge_audit.py`](../scripts/signed_gravity_aps_wald_gauss_bridge_audit.py)
  checks that the APS eta sign is a stable boundary label, retained
  Wald/Gauss/source-unit terms produce only a positive unsigned active source,
  eta is source-neutral under gap-preserving variations, and the locked
  four-pair table appears only after inserting `chi_eta` into the source action
  by hand.
- [`logs/runner-cache/signed_gravity_aps_wald_gauss_bridge_audit.txt`](../logs/runner-cache/signed_gravity_aps_wald_gauss_bridge_audit.txt)
  records `SUMMARY: PASS=14 FAIL=0` and the same not-derived final tag.

The row runner now verifies these three surfaces before checking the inserted
action ansatz. This does not prove the desired source action and does not add a
new axiom. It makes the conditional row audit-ready as a source-boundary/no-go
packet: the proposed action passes its local variation and sign-table controls
only after the missing `chi_eta M_phys <rho,Phi>` source term is supplied, while
the current retained APS/Wald/Gauss stack is explicitly certified not to derive
that term.

## 2026-05-28 Panel Convergence — Origin Obligation Sharpened to the Generation-Chirality Grading

Proof obligation #1 ("Origin": derive `S_int = −χ_η M_phys ⟨ρ,Φ⟩` from retained
structure rather than adding it as an axiom) was attacked by a 7-angle panel
framed to **find the escape** (APS-index coupling, anomaly inflow,
eta-variation/spectral-flow, Wald/Gauss source-unit accounting, adversarial
refutation, literature scout, first-principles + math). The panel did **not**
find an impossibility — it found that the examined routes all reduce to the
same missing structure: a chiral grading on the generation/orientation factor.
This **sharpens** the open gate to a precise derivation target rather than
closing it. The two structural facts below are the *localization* of that gate
(they show that, absent the grading, the current retained inventory does not
supply the χ-odd source) — they are **not** a no-go verdict on the physics. "No
admissions" means the grading must be derived; it does **not** mean the gate is a
wall.

**Two independent structural reasons the χ-odd source cannot come from retained structure:**

1. **Positivity forces the active source orientation-even.** Every retained
   object that can source `Φ` by variation is non-negative and orientation-even:
   the Born density `ρ = |ψ|² ≥ 0`, the inertial mass / Gauss-flux magnitude
   `M_phys = C_abs > 0` (an absolute exterior-monopole coefficient `φ → C/r`,
   sign-blind, NOT spectral-index data), `q_bare = 4π M_phys`, `c_cell = 1/4`,
   `λ = 1`, and the positive Wald area carrier `(1/4)A/a² ≥ 0`. The active source
   `ρ_active = −δS_int/δΦ` is a variation of a sum of these, hence orientation-even:
   it spans only `[+1,+1]` over the two `χ` sectors and **structurally cannot
   realize the required orientation-odd `[+1,−1]`**. The lane's own factorization
   `C_signed = Q_χ · C_abs` concedes the sign must come from a separate `Q_χ`
   factor the retained stack does not contain. (Verified independently: the
   Stieltjes / M-matrix positivity of the screened-Poisson source forces
   `ρ ≥ 0 ⇒ Φ ≥ 0`; a sign flip needs a mixed-sign source, which positivity
   forbids.)
2. **`sign(η)` is variationally inert.** The action carries `χ_η = sign η_δ(D_Y)`,
   an integer-valued spectral-asymmetry label that is **locally constant** on the
   gapped admissible domain (`h_δ = 0`). Hence `δ sign(η)/δΦ ≡ 0` there (verified:
   2000 random gap-preserving deformations give `max|δη/δΦ| = 0` exactly; the
   smooth APS local term vanishes on the closed flat lattice by `Γ₅` ±-pairing,
   `η ≡ 0`; standard APS theory — Farber–Levine, Fukaya et al. — confirms `η`
   varies only by integer jumps at zero-crossings, which `h_δ=0` excludes). A
   label with vanishing functional derivative **cannot be an active variational
   source** — it can only multiply an independently-varied positive source by
   hand, which is exactly the new axiom. "Source sign = boundary η sign" is an
   aesthetic ansatz, not a dynamical derivation.

**Examined escape routes reduce to the same missing grading (on the current retained substrate):**

- **APS index:** `M_phys = C_abs` is a Gauss-flux magnitude, not index data; the
  matter index is locally constant (`dIndex/dΦ = 0`); `δη/δΦ = 0` by gap rigidity.
- **Anomaly inflow:** retained boundary `η = 0` (flat `Z³`, no Pontryagin density,
  torsion-free — both new-axiom additions); and even a hypothetical bulk term
  would land `χ_η` in the **area coefficient** — the channel the proposal
  explicitly rejects — not the interior `ρΦ` source (anomaly invariants are
  orbit-functorial global labels, the wrong shape for a local `ρ(x)` source).
- **Literature:** `sign(η)` is a genuine active coupling for **gauge/EM** fields
  in 2+1D (parity anomaly) and the Witten-effect monopole charge, but there is
  **no established mechanism** where `sign(η)` of a boundary Dirac operator sources
  a 3+1D **scalar-gravity** `ρΦ` coupling; in the canonical APS/QFT framework
  (Witten; Witten–Yonekura) `η` is a partition-function **spectator phase**.
- **Separability:** retained structure factorizes (disjoint regions sew by direct
  sum ⇒ `det` factorizes, `log|det|` additive, block-local derivatives), so it
  produces no boundary-label × bulk-source × field **product** term; the
  determinant orientation line is a section-less `Z₂` **torsor** (hosts the
  label, selects no canonical section).

**The frontier target (a shared gate TYPE, not one shared operator).** The route
identified here is for `Φ`/the mass operator to couple to a **chiral grading that
anticommutes with `D_Y`** and breaks the native symmetry of the relevant factor.
A 5-agent follow-up panel established the precise relation to the Koide lane,
**correcting an earlier overstatement** that it was literally the same grading:
the three lanes need gradings on **three distinct tensor factors** —
Koide `Γ_χ` on the **generation R³**, signed-gravity's grading on the
**cochain/taste** factor of `D_Y`, and the Connes–Lott chirality `γ_CL = I⊗σ₃` on
an **L/R factor**. They are **not one operator**; they share a **gate type**:
*derive a non-transportable, symmetry-breaking chiral grading on a factor whose
native structure (C₃-equivariance / cochain pairing) forbids it.* Two sub-results
sharpen this:

- **The Connes–Lott separate-factor route genuinely evades the retained
  `koide_z3_equivariant_anticommuting_no_go`** (its §4 leaves this open): with
  `D = [[0,M],[M†,0]]`, `{D, γ_CL=I⊗σ₃} = 0` is automatic for any `M`, and the
  no-go provably does not reach `γ_CL` (which is generation-trivial). But `γ_CL`
  is **generation-blind**, so it yields the L/R-balance invariant, *not* the
  Z₃-character Koide invariant — `Q=2/3 ⟺ r=|b|²/a²=1/2` stays **unforced**
  (consistent with the team's prior `KOIDE_U_BAE_NCG_SPECTRAL_TRIPLE` Probe U and
  the KO-dimension real-structure narrowing: the spectral action is symmetric in
  the three eigenvalues and never selects `r=1/2`). And the L/R factor itself is
  **not native** — it is the framework's existing `Z³→Z⁴`/`e₄` Wick-rotation
  admission (Cl(3) is odd, so no native `γ₅`).
- **The concrete, unforeclosed unification target** is therefore a *single
  product-grading spectral triple* `H = R³_gen ⊗ (taste) ⊗ (H_L⊕H_R)` carrying one
  Dirac whose off-diagonal blocks simultaneously (i) restrict to an `{H,Γ_χ}=0`
  operator on the generation R³ (→ Koide) and (ii) induce a nonzero orientation-odd
  `η_δ(D_Y)` on the cochain factor (→ signed source), via the **product** grading
  `Γ_χ⊗ε` — not the (foreclosed) identification `γ_CL=Γ_χ`. No retained no-go
  forecloses this product-grading triple; the decisive open computation is whether
  its order-one / `J`-reality condition pins `b/a = 1/√2`.

This is the no-admissions path being targeted: construct the grading, never
axiomatize it. If the sufficiency checks close, it could unlock signed-gravity,
Koide `Q=2/3`, and generation-ID — but the two honest open sub-gates remain the
`e₄`/P2 L/R-factor origin and the `r=1/2` forcing, neither yet supplied.

This convergence reproduces and sharpens the existing lane infrastructure
(`signed_gravity_response_lane_status_note`;
`SIGNED_GRAVITY_RETAINED_BOUNDARY_SOURCE_PRINCIPLE_NO_GO_NOTE` orientation-even
`[+1,+1]` cannot span `[+1,−1]`; the native-complex containment and
host-vs-selector results) by supplying the positivity + variational-inertness
**reasons** the gate sits exactly at the chiral grading. No new axiom, import, or retained
bridge is introduced by this repair.

This note proposes the smallest action that would close the remaining
APS/source-locking gap identified in
`SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md` (see-also
cross-reference; backticked to break newborn cycle-XXXX through
aps_locked_source_action_proposal -> aps_wald_gauss_bridge_audit ->
response_backlog -> aps_locked_source_action_proposal — the audit note is
the upstream gap-identifying lineage doc, not a load-bearing dep, and the
load-bearing direction is preserved downstream).

The boundary remains strict. This is not a negative-mass, shielding,
propulsion, reactionless-force, or physical signed-gravity claim. It is a
conditional action ansatz: if accepted or later derived, it supplies the
missing `chi_eta` variation by construction. Until then it is a proposal and a
test harness, not a retained theorem.

## Permanent Boundary Repair (2026-05-27)

The audit blocker offered two repair routes:

1. derive the `chi_eta M_phys rho Phi` source-action cross term from retained
   APS/Wald/Gauss structure; or
2. mark the row as an unadmitted proposed-extension boundary.

This repair takes route (2). The source-action term is classified as an
`open_gate` proposed-extension boundary, not as an admitted axiom and not as a
retained theorem. A future, separately reviewed theorem could derive it from
retained structure; until then the interaction is not available as a
load-bearing premise over the current APS/Wald/Gauss stack.

The related lane-status context is
[`SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md`](SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md),
which keeps the signed-response lane in no-go/open status rather than a
physical signed-gravity closure. The downstream extension follow-up remains a
controlled candidate only; it is not an admitted axiom, not a retained theorem,
and not a physical signed-gravity claim.

## Proposed Action

For each compact source region `Omega_a` with gapped APS boundary
`Y_a = partial Omega_a`, define:

```text
chi_a = chi_eta(Y_a) = sign eta_delta(D_Ya)
```

only when:

```text
h_delta(D_Ya) = 0
eta_delta(D_Ya) != 0.
```

The `eta = 0` or zero-window sector is a null/control sector, not a third
active sign.

Let `rho_a(x) = |psi_a(x)|^2` be normalized:

```text
sum_x rho_a(x) = 1,
M_a > 0.
```

The proposed weak-field source action is:

```text
S_APS-lock[Phi, psi, Y]
  = (1/(8 pi)) sum_<xy> (Phi_x - Phi_y)^2
    - sum_a chi_a M_a sum_x rho_a(x) Phi_x
    + sum_a S_matter,0[psi_a; M_a]
    + sum_a S_APS-gap[D_Ya]
    + S_Wald^+[Y_a].
```

The positive boundary carrier remains:

```text
S_Wald^+[Y] / k_B = (1/4) A(Y)/a^2.
```

The sign is not placed in the Wald/area coefficient. Putting `chi/4` there
would make the `chi=-1` branch a negative-area-coefficient branch, which is
rejected.

For the staggered parity-correct response implementation, the same branch
label would enter the scalar channel as:

```text
H_diag,a = (m_a + chi_a Phi) epsilon(x),
```

or, in the point-particle weak-field readout:

```text
U_a = - chi_a M_a Phi.
```

The source and response signs are therefore locked by the same APS boundary
label.

## Variation

The active source is defined as:

```text
rho_active(x) = - delta S_int / delta Phi_x.
```

For the proposed interaction term,

```text
S_int = - sum_a chi_a M_a sum_x rho_a(x) Phi_x,
```

the variation gives:

```text
rho_active(x) = sum_a chi_a M_a rho_a(x).
```

Stationarity of `Phi` gives the physical-source Poisson equation:

```text
(-Delta) Phi = 4 pi sum_a chi_a M_a rho_a.
```

The source-unit theorem then consumes the already supplied signed active
source:

```text
q_bare,a = 4 pi chi_a M_a.
```

This is exactly what the earlier bridge audit could not derive from the
existing retained APS/Wald/Gauss stack.

## What Is New

Existing retained ingredients:

- the APS eta sign as a basis-invariant, gap-stable boundary label
- the positive Wald/Gauss/source-unit scale:
  `c_cell = 1/4`, `lambda = 1`, `M_phys = C_abs`,
  `q_bare = 4 pi M_phys`
- positive inertial mass from the ordinary norm and kinetic term

New premise:

```text
S_int = - chi_eta M_phys <rho, Phi>.
```

That premise is the whole proposal. It should not be hidden. It is not derived
by source-unit normalization, and it is not obtained by multiplying the
positive Wald coefficient by `chi_eta`.

## Harness Result

Command:

```bash
python3 scripts/signed_gravity_aps_locked_source_action_proposal.py
```

Summary:

```text
[PASS] source variation gives +M rho in chi=+ sector
       residual=1.628e-12, active=+2.750000
[PASS] source variation gives -M rho in chi=- sector
       residual=1.628e-12, active=-2.750000
[PASS] positive Wald/area carrier is not multiplied by chi
[PASS] positive inertial mass is branch independent
       M_+=M_-=2.750
[PASS] same-point +/- active source cancels with positive inertia
       C_signed_sum=+0.000e+00, M_sum=5.500
[PASS] source-unit conversion consumes the proposed signed source
       q_bare=4*pi*chi_eta*M_phys
FINAL_TAG: APS_LOCKED_SOURCE_ACTION_CONDITIONAL_CANDIDATE
```

The proposed action passes the local algebraic gates because it was built to
do so. That is useful as a target, but it is not a derivation.

## Four-Pair Table

The harness compares the proposed action with controls:

| law | max balance residual | table | derived without new action | reads |
|---|---:|---|---|---|
| retained positive | `0.000e+00` | fail | yes | all pairs attract |
| APS eta spectator | `0.000e+00` | fail | yes | zero active source |
| APS source-only inserted | `2.000e+00` | fail | no | mixed pairs unbalanced |
| APS response-only inserted | `2.000e+00` | fail | no | mixed pairs unbalanced |
| APS locked action ansatz | `0.000e+00` | pass | no | same-sector attract, opposite-sector repel |

The proposed action is the first APS route that gives the desired locked table,
but only because the new action term puts `chi_eta` into both source and
response.

## Controls

The proposal keeps the basic controls clean in the finite harness:

```text
Born I3, chi=+ sector: +1.794e-43
Born I3, chi=- sector: +1.794e-43
max norm drift: 2.887e-15
same-point +/- q_bare sum: 0
same-point +/- inertial mass sum: positive
```

The 2026-06-03 boundary repair runner checks these displayed control numbers
against the current harness. It does not change the open-gate status or derive
the missing `S_int = - chi_eta M_phys <rho, Phi>` source term.

The branch sign does not alter Born linearity, unitary norm preservation, or
positive inertial mass in the fixed-sector harness.

## Proof Obligations

To promote this from action proposal to retained theorem, the lane must still
prove:

1. **Origin.** Derive `S_int = -chi_eta M_phys <rho,Phi>` from retained
   APS/Wald/Gauss boundary structure, rather than adding it as a new axiom.
2. **Superselection.** Prove the eta sector is protected under admissible
   boundary dynamics. Zero crossings must remain classified defects.
3. **Energy stability.** Supply a bounded Hamiltonian/constraint argument that
   prevents runaway production of positive-inertial-mass opposite active
   signs.
4. **Scalar/tensor discipline.** Keep this as a scalar active-monopole action
   unless a separate tensor-valued gravity theorem is supplied.
5. **Continuum and family portability.** Only after the first four gates pass,
   test refinement, graph families, and two-packet dynamics.

## Boundary Verdict

The proposed action is:

```text
APS_LOCKED_SOURCE_ACTION_CONDITIONAL_CANDIDATE
```

It is the cleanest concrete action target found so far. It also makes the
remaining scientific burden sharper:

> The signed-response lane now needs a derivation of this APS-locked source
> term, or a no-go showing that no retained APS/Wald/Gauss source action can
> produce it without adding a new sign axiom.

Until that derivation exists, the action remains a conditional candidate and
the signed-gravity claim surface remains blocked.

## Follow-Up Audit

The origin, superselection, and stability gates are audited in
`SIGNED_GRAVITY_APS_ACTION_ORIGIN_SUPERSELECTION_STABILITY_NOTE.md`
(downstream consumer in same lane; cross-reference only — not a one-hop dep of this note)
with runner
[`../scripts/signed_gravity_aps_action_origin_superselection_stability_audit.py`](../scripts/signed_gravity_aps_action_origin_superselection_stability_audit.py).

Result:

```text
FINAL_TAG: APS_LOCKED_ACTION_CONDITIONAL_NOT_RETAINED
```

The proposal remains the cleanest target action, but it is not retained:
separable APS/Wald/Gauss terms cannot produce the signed source without the
new `chi_eta rho Phi` cross term, eta superselection is conditional on a
protected boundary gap, and full boundedness still needs an ordinary
short-distance gravity UV/core or constraint argument.

## Axiomatic Extension Follow-Up

The retained route is blocked, so the next honest move is to name the new
structure directly. That pass is recorded in
`SIGNED_GRAVITY_APS_LOCKED_AXIOM_EXTENSION_NOTE.md` (downstream follow-up
artifact; cross-reference only — that note cites the retained-boundary
no-go as its predecessor, not this proposal)
with runner
[`../scripts/signed_gravity_aps_locked_axiom_extension_audit.py`](../scripts/signed_gravity_aps_locked_axiom_extension_audit.py).

Result:

```text
FINAL_TAG: APS_LOCKED_AXIOM_EXTENSION_CONTROLLED_CANDIDATE
```

The axiom extension treats `chi_eta M_phys rho` as an eta-polarized source
line on gapped APS boundary sectors and imposes hard gap admissibility. It is
coherent as a controlled candidate, but it is not a retained theorem or a
physical signed-gravity claim.

## 2026-06-15 audit-unlock residual certificate

The local finite variation and sign-table harness is useful only after the
cross term `S_int = - chi_eta M_phys <rho, Phi>` is inserted. This packet
does not derive that term.

The exact frontier target is a framework-native derivation of the canonical
orientation section/source principle that forces the APS-locked
`chi_eta rho Phi` source action and protects the eta sector. Until that is
proved, this row should be re-audited as an open-gate source-action proposal
with a passing conditional harness, not as a source-action theorem. No new
axiom or admitted source principle is added here.
