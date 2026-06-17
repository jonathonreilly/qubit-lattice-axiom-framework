# 't Hooft 1981 Dual-Superconductor / Center-Vortex Confinement — External Narrow Gate

**Date:** 2026-05-16
**Type:** open_gate
**Claim type:** open_gate
**Scope:** external 4D SU(N) Yang-Mills confinement-mechanism context:
abelian projection with residual U(1)^(N-1), magnetic monopole
condensate / dual-superconductor picture, center-vortex disorder
picture, and symbolic vortex / monopole action forms. These are
recorded as published mechanism targets and diagnostics, not as a
standalone proof of confinement in 4D Yang-Mills and not as a
framework theorem. Cited only as published gauge-theory context
('t Hooft 1978, 1981; Mandelstam 1976; Greensite 2011;
Del Debbio-Faber-Greensite-Olejnik 1996). No framework substrate
identification, hierarchy closure, scale ratio derivation, or
`α_LM^16` substitution is claimed.
**Runner:** [`scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py`](../scripts/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.txt`](../logs/runner-cache/frontier_thooft_1981_dual_superconductor_center_vortex_confinement_external_narrow.txt)

## Source boundary (2026-06-12)

**Boundary:** external notation / published-context registration. Effective
status is audit-derived; this source records only the claim boundary.

The runner checks text presence and tautological symbolic forms; it does not
verify the external confinement mechanisms or derive a framework confinement
theorem.

This note may be cited for vocabulary, bibliography, and future bridge targets.
It may not be cited as retained framework support for monopole condensation,
center-vortex condensation/percolation, Wilson-loop area law, hierarchy
closure, or any `alpha_LM^16` substitution.

## 2026-06-07 Pure-Notation Source Boundary

The load-bearing packet for this row is only the syntactic registration
packet

```text
P_THOOFT_REG = (
  abelian-projection vocabulary,
  residual U(1)^(N-1) group notation,
  monopole / dual-superconductor labels,
  center-vortex disorder labels,
  symbolic action-form templates,
  Wilson-loop area-law target notation
).
```

The runner checks text presence and tautological symbolic identities for this
registration packet. It does not check the truth of the external confinement
mechanisms, does not verify the cited papers in full, and does not treat the
external references as retained authorities or one-hop framework dependencies.
The references below are bibliographic labels for the notation being
catalogued, not a retained authority packet.

This row has no published-context support claim. It is a pure syntactic
vocabulary registration and open-gate boundary for future bridge work. It does
not prove monopole condensation, center-vortex condensation/percolation,
positive string tension, a Wilson-loop area law, or any framework observable
identification. Any later use as a theorem input must first supply a separate
retained bridge theorem or retained/effective-bounded authority packet.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The restricted packet closes only the syntactic and symbolic recording of the open gate. It does not derive monopole condensation, center-vortex percolation, the Wilson-loop area law, σ > 0, or a framework substrate/readout bridge."*

with repair: *"missing_bridge_theorem: Add retained-grade bridge theorems or one-hop retained authorities for monopole/vortex condensation, the Wilson-loop area law/string tension, and any framework substrate observable identification before upgrading bey"*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The runner-verified symbolic recording of the published open gate — abelian-projection residual group structure, vortex and monopole action symbolic forms, area-law observable target, and center/order-disorder diagnostic vocabulary — verified across checks T1–T10 (PASS=N, FAIL=0); this closes as a faithful syntactic registration of the external 't Hooft 1981 / Mandelstam 1976 / Greensite 2011 confinement-mechanism context.
- **NON-load-bearing (split off / admitted):** Any framework substrate identification with the dual-superconductor or center-vortex mechanism, and any derivation of monopole condensation, center-vortex percolation, the Wilson-loop area law `σ > 0`, or framework-observable readout from framework primitives; these require retained-grade bridge theorems or one-hop retained authorities that are not supplied and remain admitted, not-derived targets.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Claim

Let `A_μ(x)` be a smooth Euclidean SU(N) gauge connection on `R^4` (or
on a 4-torus compactification), with field strength

```text
F_μν = ∂_μ A_ν - ∂_ν A_μ + i [A_μ, A_ν].
```

The Euclidean Yang-Mills action is

```text
S[A] = (1 / (4 g²)) ∫ d^4x  Tr( F_μν F^μν ).
```

**Statement (external open gate; 't Hooft 1981; Mandelstam 1976):**

1. *Abelian projection.* For SU(N) gauge theory, fix a gauge by
   diagonalizing a chosen adjoint composite field `X(x)` ('t Hooft 1981).
   In a generic configuration `X(x)` is non-degenerate almost everywhere,
   and the residual gauge symmetry after diagonalization is the maximal
   abelian subgroup `U(1)^(N-1) ⊂ SU(N)`. Defects where two eigenvalues
   of `X(x)` coincide form codimension-3 loci in 4D Euclidean spacetime;
   these are the worldlines of **magnetic monopoles** carrying U(1)^(N-1)
   magnetic charge dual to the electric Wilson-line charge.

2. *Dual-superconductor / monopole condensate mechanism.* (Mandelstam
   1976; 't Hooft 1981.) If the magnetic monopoles **condense** — i.e., a
   gauge-invariant monopole creation operator `φ_mono(x)` acquires a
   non-zero vacuum expectation value `⟨φ_mono⟩ ≠ 0` — then by the
   electric-magnetic dual to the Meissner effect, **electric flux is
   confined into thin flux tubes** between colored charges, producing a
   **Wilson-loop area law**:

   ```text
   ⟨ W(C) ⟩  ~  exp(- σ × Area(C) ),     for large loops C,
   ```

   where `σ > 0` is the string tension. The vacuum free-energy density
   contributed by a dilute monopole gas carries a structural factor

   ```text
   f_mono ~ - exp( - S_mono ) × ( zero-mode determinant ),
   ```

   with `S_mono` the classical monopole action; the corresponding
   monopole-condensation phase is the dual superconductor.

   This note does not prove that this condensate exists in the
   framework, compute `σ`, or prove 4D confinement from first
   principles.

3. *Center-vortex disorder picture.* (Mandelstam 1976; 't Hooft 1978;
   Greensite 2011 review arXiv:0810.4392; lattice realization
   Del Debbio-Faber-Greensite-Olejnik arXiv:hep-lat/9609025.) In the
   center-vortex picture, magnetic disorder is carried by closed
   codimension-2 worldsheets (`Z_N` vortices) on which Wilson loops in
   the fundamental representation pick up a center phase
   `z = exp(2π i k / N)`, `k ∈ {1, ..., N-1}`. A condensate/percolating
   ensemble of `Z_N` center vortices can disorder Wilson loops and is
   used as a confinement diagnostic in the cited center-vortex
   literature: a
   Wilson loop linking `n` vortices on average picks up a center phase,
   and a random distribution of vortices over the minimal surface
   spanning the loop yields

   ```text
   ⟨ W(C) ⟩  ~  exp(- σ_vortex × Area(C) ),
   ```

   with `σ_vortex` set by the planar vortex density.

   This note does not assert theorem-grade equivalence between all
   monopole-condensate and center-vortex formulations, nor does it
   assert ordinary electric center-symmetry breaking in the confining
   phase.

4. *Symbolic vortex action and condensation criterion.* The vortex
   classical action per unit transverse area scales as

   ```text
   S_vortex ~ (1 / g²) × (string-tension factor σ a²),
   ```

   in lattice units `a`, where `σ a²` is the standard lattice
   string-tension factor. A schematic disorder/condensation criterion is
   that the exponential vortex weight is not parametrically suppressed
   relative to entropy and measure factors:

   ```text
   exp( - S_vortex )  ~  O(1)   at confinement,
   ```

   This is an open mechanism criterion, not a proof that the disorder
   field acquires a VEV in the framework. The monopole
   classical action carries an order-of-magnitude structural form

   ```text
   S_mono  ~  (8 π / g) × ( O(1) profile factor ),
   ```

   characteristic of a 't Hooft-Polyakov monopole in the U(1)^(N-1)
   subgroup ('t Hooft 1974; Polyakov 1974, cited for completeness as
   published context; the precise prefactor and profile depend on the
   Higgs sector chosen in the abelian projection).

5. *Center/order-disorder diagnostics.* On a 4-torus with one compact
   thermal-like direction or in pure Yang-Mills with `Z_N` center
   structure, Wilson loops, Polyakov loops, and vortex creation
   operators diagnose order/disorder phases. In the confining phase,
   magnetic disorder variables can have a nonzero disorder expectation
   while the Wilson-loop area law characterizes the electric order
   variable. This note records the order/disorder diagnostic vocabulary;
   it does not prove the phase structure or assert the wrong electric
   center-symmetry-breaking statement for the confining phase.

6. *Area law as physical observable target.* The defining physical observable
   of confinement is the area-law decay

   ```text
   - lim_{R, T → ∞}  (1 / (R T)) log ⟨ W(R × T) ⟩  =  σ  >  0,
   ```

   for the rectangular `R × T` Wilson loop in the fundamental
   representation, with `σ` the string tension. This note records that
   target observable; it does not derive `σ > 0` from framework
   primitives or prove area-law confinement.

## Boundary

This note records external 4D Yang-Mills confinement-mechanism context.
It does **not** claim:

- that the framework's substrate is identified with the dual-
  superconductor / monopole-condensate / center-vortex mechanism (no
  identification of any framework substrate, lattice cell, taste,
  blocking, plaquette family, or project-specific structure with the
  't Hooft 1981 abelian-projection vacuum);
- that the 4D SU(N) Wilson lattice is identified with any
  framework-specific lattice;
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- theorem-grade proof of 4D Yang-Mills confinement, monopole
  condensation, center-vortex condensation/percolation, or equivalence
  between mechanism pictures;
- ordinary electric `Z_N` center-symmetry breaking in the confining
  phase;
- closure of the `α_LM^16` substitution or any framework `α^N`
  hierarchy at integer `N`;
- closure of `v/M_Pl` or any other dimensional scale ratio (the
  electroweak hierarchy is **not** claimed; the note records only an
  external mechanism target);
- derivation of the string tension `σ` from framework primitives — the
  external string-tension factor `σ a²` is named symbolically, and
  numerical values of `σ` from lattice or experiment together with any
  derivation of `σ` from framework primitives are not asserted here;
- any numerical prediction or comparison with observation beyond the
  published gauge-theory context;
- any new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework
substrate with the 4D SU(N) gauge background, identify a framework
observable with the Wilson loop or vortex condensate, derive the
monopole/vortex measure and string tension, and verify the
substrate-specific bridge.

## Scope Repair Checker

The source-side scope checker for this row is:

```bash
PYTHONPATH=scripts python3 scripts/frontier_thooft_center_vortex_scope_repair.py
```

This checker is a source-boundary guard. It does not apply an audit result or
promote the row beyond `open_gate`; promotion would require retained one-hop
authorities or new retained bridge theorems for condensation/percolation,
string tension, Wilson-loop area law, and framework observable identification.
This row is a permanent `open_gate` external-context catalogue. The source
repair must not treat the row as a confinement theorem, and does not ask audit
to close monopole condensation, center-vortex condensation/percolation, or a
Wilson-loop area law. A future retained bridge theorem would be needed before
any framework observable identification could use this context as a theorem
input.

## External References

- G. 't Hooft, "Topology of the gauge condition and new confinement
  phases in non-abelian gauge theories", Nucl. Phys. B **190** [FS3]
  (1981) 455 (abelian projection; magnetic monopole condensate).
- G. 't Hooft, "On the phase transition towards permanent quark
  confinement", Nucl. Phys. B **138** (1978) 1 (center symmetry
  breaking; disorder operator).
- S. Mandelstam, "Vortices and quark confinement in non-abelian gauge
  theories", Phys. Rep. **23** (1976) 245 (original dual
  superconductor mechanism).
- J. Greensite, "An introduction to the confinement problem", Lect.
  Notes Phys. **821** (2011); review arXiv:0810.4392 (modern
  center-vortex review).
- L. Del Debbio, M. Faber, J. Greensite, Š. Olejnik, "Center dominance
  and Z₂ vortices in SU(2) lattice gauge theory", arXiv:hep-lat/9609025
  (lattice center-vortex observable; center dominance).
- G. 't Hooft, "Magnetic monopoles in unified gauge theories",
  Nucl. Phys. B **79** (1974) 276 (monopole action structure).
- A. M. Polyakov, "Particle spectrum in quantum field theory",
  JETP Lett. **20** (1974) 194 (independent monopole solution; cited
  for completeness).

## Verification

The paired runner checks (in exact Fraction arithmetic with SymPy `pi`
symbolic where appropriate):

1. **T1**: abelian-projection structure — residual gauge group after
   diagonalization of the adjoint composite is `U(1)^(N-1) ⊂ SU(N)`;
   stated symbolically for general `N` and verified for `N = 2, 3`.
2. **T2**: vortex action symbolic form
   `S_vortex = (1 / g²) × (σ a²)` reproduced from the published center-
   vortex parameterization.
3. **T3**: at SU(3) with `g² = 1` and lattice `σ a² = 1`, the
   symbolic vortex action `S_vortex = 1` (named symbolically; no
   numerical confinement claim).
4. **T4**: monopole action order-of-magnitude form
   `S_mono ~ (8 π / g) × O(1)` recorded as published symbolic shape
   (no precise prefactor asserted; runner verifies the structural form
   only).
5. **T5**: condensation criterion `exp(-S_vortex) ~ O(1)` recorded as
   an open symbolic / qualitative threshold, with entropy/measure gaps
   left open.
6. **T6**: Z_N center/order-disorder diagnostic — note records the
   center-vortex disorder vocabulary while explicitly avoiding an
   electric-center-breaking overclaim for the confining phase.
7. **T7**: area-law observable
   `- lim (1 / (R T)) log ⟨ W(R × T) ⟩ = σ > 0`
   stated as the canonical Wilson-loop confinement diagnostic; runner
   verifies the formula is present in the note.
8. **T8**: source-note boundary — note declares `claim_type: open_gate`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure, hierarchy closure, or scale ratio derivation.

Expected primary runner result: `PASS=33`, `FAIL=0`.
Expected scope-repair checker result: `PASS=16`, `FAIL=0`.
