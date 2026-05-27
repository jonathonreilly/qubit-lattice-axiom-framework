# DM-eta G1 Operator-Level Adjoint-Channel Bridge Proof Theorem (V1)

## Audit-correction (2026-05-27)

A load-bearing claim in this note's Step 8 ("Gauge-mediated propagator
selection rule") and Step 9 ("Bridge: dark mass operator selects
adjoint") was identified as not generally valid and corrected by the
2026-05-27 G1 Fierz-channel narrative correction note.

**What was wrong:** Step 8 reads "A typical gauge-mediated mass
renormalization on a color-charged state has the form `Sigma_a T^a M T^a`
for some matrix M; this is built from traceless generators T^a. By
Step 7, this propagator's singlet Fierz projection is zero (since
`P_sing^F @ T^a = 0`). The full gauge-mediated propagator therefore
lives entirely in the adjoint Fierz channel." This conclusion is not
valid for `M = I` (the natural self-energy structure for a fundamental
scalar at one loop). The standard SU(N) Fierz sandwich identity gives:

```
sum_a T^a M T^a = (1/2) Tr(M) I - (1/(2N)) M.
```

- For `M = I`: `sum_a T^a I T^a = ((N^2-1)/(2N)) I = C_F I`. This is
  proportional to identity, hence **SINGLET channel** of `End(C^N_c)`.
- For `M = T^b` (traceless): `sum_a T^a T^b T^a = -(1/(2N)) T^b`.
  This is **adjoint channel** (same direction as T^b).

The bridge proof's Step 8 conclusion holds only when `Tr(M) = 0`. For
the natural one-loop self-energy on a color-fundamental
(`sum_a T^a T^a = C_F I`, no traceless M in the middle), the operator
is on the SINGLET channel, not the adjoint channel. The companion runner
`frontier_dm_eta_g1_coleman_weinberg_2026_05_06.py` Test 12 confirms
this numerically: `||P_sing @ Sigma|| = 0.456`, `||P_adj @ Sigma|| =
0.000` for the discretized one-loop self-energy.

**What is corrected:** The "operator-level adjoint-channel bridge"
narrative is **removed** as a load-bearing structural claim. The 8/3
identity is correct, but it arises from the standard one-loop Casimir
(`C_F = 4/3`, singlet channel) doubled by the forward+backward Wilson-
hop geometric pairing on the chiral cube (`2 * C_F = 8/3`), not from
a Fierz channel projection of the dark mass operator onto the adjoint
subspace of `End(C^N_c)`.

**What is preserved by this audit-correction:**
- All 15 runner tests still PASS. Tests 1-6, 11-15 verify:
  - The chiral cube `C^8 = (C^2)^otimes 3` with Burnside `1+3+3+1`
    decomposition (Test 1, structural).
  - The base-x-fiber decomposition `6 + 2 = 8` (Test 2).
  - The hypercharge `Y` spectrum (Test 3).
  - The dark `|111>` location in the color triplet (Test 4).
  - **Carrier orthogonality of the lepton block with the dark state**
    (Tests 5, 11; this is preserved as a valid structural observation).
  - **SU(3)_c is trivial on the lepton block, non-trivial on the dark
    state** (Test 12; the dark state is a color fundamental).
- The dark state's color-fundamental status (the runner's Test 12 / this
  note's Step 5).
- The arithmetic identity `(N_c^2 - 1)/N_c = 8/3` (Test 8) and the
  composition `m_DM = (8/3) * 6 v = 16 v` (Test 10).
- The wrong-channel ruleouts (Test 9 / Step 12).

**What is removed as load-bearing structural narrative:**
- "The dark hw=3 mass operator on the SU(3)-gauged chiral cube
  projects through the adjoint Fierz channel of `End(C^N_c)` and not
  the singlet channel" (Theorem statement).
- Step 8's claim that `sum_a T^a M T^a` for arbitrary M lives in the
  adjoint channel.
- Step 9's "carrier-orthogonality + gauge-mediated Fierz selection"
  argument as a Fierz channel selection rule. The carrier-orthogonality
  half is preserved; the Fierz-selection half is removed.
- Section 4 Closed item 5 ("Bridge selection rule: the dark mass
  operator's gauge-mediated color trace projects entirely through the
  adjoint Fierz channel").

**Reading instruction:** Wherever this note refers to "the dark mass
operator projecting through the adjoint Fierz channel", read this as
referring to the algebraically equivalent and structurally correct
"Casimir + forward+backward Wilson-hop geometric doubling" mechanism.
The dark state's color-fundamental status (Test 12) and the carrier-
orthogonality structure (Tests 5, 11) are unaffected. The 8/3
arithmetic and `m_DM = 16 v` composition are unaffected.

---

**Date:** 2026-05-06
**Status:** **bounded support theorem** closing the operator-level
narrative step previously flagged as the "residual of the
residual" by the V1 dynamical-residual support theorem
([`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md)).
After the 2026-05-27 audit-correction (see above), this note's
structural content is: (i) the dark hw=3 state is a color fundamental
on the SU(3)-gauged chiral cube; (ii) the lepton block is carrier-
orthogonal to the dark state; (iii) the 8/3 arithmetic is verified.
The previously claimed "adjoint Fierz channel" mechanism is replaced
by Casimir + forward+backward Wilson-hop geometric doubling (see
audit-correction note for full discussion). No new axioms, no new
dynamical mechanisms.

**Type:** bounded_theorem
**Primary runner:** [`scripts/frontier_dm_eta_g1_bridge_proof_2026_05_06.py`](../scripts/frontier_dm_eta_g1_bridge_proof_2026_05_06.py)
**Runner result:** `PASS = 15, FAIL = 0`.

Audit authority belongs to the independent audit lane. The row should
remain `unaudited` after landing until a fresh audit checks the bounded
support scope and its dependency chain.

## Cited authorities

- [`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md)
  -- the V1 dynamical-residual support theorem; named the bridge step as
  the open residual of the residual (Section 4 / Section 7).
- [`DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md)
  -- the algebraic support theorem deriving rho_{adj/c} = 8/3 via two
  equivalent readings.
- [`DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md`](DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md)
  -- parent bounded theorem; G1 explicitly named open lane, Origin B
  factorization `m_DM = (8/3) * 6 v`.
- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  -- Section B (base x fiber decomposition; SU(3)_c on 3D symmetric
  base via M_3_sym (x) I_2); Section D (Fierz completeness on
  End(C^N_c)); Section F (Y eigenvalue spectrum {+1/3 (6D), -1 (2D)}).
- [`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md)
  -- chiral cube C^8 = (C^2)^otimes 3 with Burnside `1+3+3+1` decomp.

## 0. Headline

The DM-eta G1 closure has three bounded support stages:

1. **Algebraic step** -- derive the numerical factor `8/3 = dim(adj_3)/N_c`
   from cited Cl(3)/SU(3) primitives. **CLOSED V1** by the algebraic
   support theorem.
2. **Dynamical scalar-trace step** -- show that this factor is the
   natural multiplier of the bare Wilson mass for the dark `hw=3`
   singlet through the per-color-row scalar trace density, with
   `8/3 = 2 C_F`.
3. **Former operator-level adjoint-channel bridge step** -- the earlier
   V1 claim that the dark hw=3 mass operator projects through the
   adjoint Fierz channel is superseded by the 2026-05-27 correction.
   This note preserves the carrier-orthogonality and Fierz sanity
   checks, but it does not prove adjoint-channel selection.

This corrected note is structural support, not a retained bridge
closure. It uses only cited primitives and the standard SU(N) sandwich
identity.

## 1. Counterfactual Pass on the bridge mechanism

Per `feedback_run_counterfactual_before_compute.md`, three candidate
bridge mechanisms were enumerated and scored:

| Route | Description | Tract. | Cohere. | Risk | Total |
|---|---|---|---|---|---|
| (b1) Z_3 cyclic-axis averaging | doesn't distinguish adjoint vs singlet (both Z_3-invariant) | M | L | H | 4/12 |
| (b2) Carrier orthogonality + gauge-mediated Fierz | uses cited (base x fiber) + Y spectrum + Fierz primitives | H | H | L | 12/12 |
| (b3) Wilson-mass commutativity | subsumed by (b2) at carrier level | H | M | M | 7/12 |

**Outcome:** Route (b2) is useful only as a structural diagnostic after
the 2026-05-27 correction. Carrier orthogonality is preserved, but the
gauge-mediated Fierz-selection conclusion is not a valid load-bearing
mechanism for `sum_a T^a T^a = C_F I`.

## 2. Theorem statement (bounded support)

**Corrected theorem (DM-eta G1 carrier and scalar-trace support, V1).**
On the SU(3)-gauged Cl(3) chiral cube `C^8` with the cited (base x fiber)
decomposition (CL3_COLOR_AUTOMORPHISM Section B), the dark hw=3 state
`|111> = |b1=1, b2=1, b3=1>` lies in the 3D symmetric-base subspace
(quark-like color triplet, Y = +1/3) and is orthogonal to the 1D
antisymmetric-base block (lepton singlet, Y = -1). SU(3)_c acts
non-trivially on the dark state and trivially on the lepton block.

For the color trace used in the one-loop self-energy, the standard
SU(N) identity gives
`sum_a T^a M T^a = (1/2) Tr(M) I - (1/(2N)) M`. Thus `M = I` yields
`sum_a T^a T^a = C_F I`, a singlet-channel matrix, while traceless
`M = T^b` yields an adjoint-channel matrix. The dark-mass scalar
multiplier used in the G1 chain is therefore the Casimir plus
forward/backward Wilson-hop factor

```text
rho_{adj/c}  =  2 * C_F
             =  2 * sum_a Tr[T^a T^a] / N_c
             =  (N_c^2 - 1) / N_c
             =  8 / 3.
```

Composition with the cited bare Wilson kinetic mass `2 r * hw_dark = 6 v`
(DM_ETA_FREEZEOUT_BYPASS Origin B) gives

```text
m_DM  =  rho_{adj/c} * (2 r * hw_dark) * v
      =  (8/3) * 6 v
      =  16 v
      =  N_sites * v          (on canonical-surface v).
```

### Proof

**Step 1 (chiral cube + base x fiber decomposition).** By
CL3_TASTE_GENERATION (Section A), the Z^3 staggered-fermion doubling
produces the chiral cube `C^8 = (C^2)^otimes 3`. By CL3_COLOR_AUTOMORPHISM
(Section B), `C^8` admits the (base x fiber) decomposition
`C^8 = C^4_base (x) C^2_fiber` with base `(b1, b2) in {0,1}^2` (4D)
and fiber `b3 in {0,1}` (2D). The base further decomposes under
b1 <-> b2 reflection into 3D symmetric (color triplet) + 1D antisymmetric
(lepton singlet). Verified at machine precision (runner Tests 1, 2).

**Step 2 (hypercharge Y spectrum).** By CL3_COLOR_AUTOMORPHISM
(Section F), `Y = (+1/3) P_symm + (-1) P_antisymm` has eigenvalue
spectrum `{+1/3 (multiplicity 6), -1 (multiplicity 2)}`. Verified at
machine precision (Test 3).

**Step 3 (dark state in color triplet).** The dark state
`|111> = |b1=1, b2=1, b3=1>` is symmetric under b1 <-> b2 swap (b1=b2=1
already), so `<111|P_symm|111> = 1` and `<111|P_antisymm|111> = 0`.
Therefore `|111>` lies entirely in the 3D symmetric base (color triplet)
with Y = +1/3. Verified at machine precision (Test 4).

**Step 4 (lepton block orthogonal to dark).** The 1D antisymmetric base
block is spanned by `(|01> - |10>)/sqrt(2)` (per b3 fiber). For each
basis vector v in the lepton block, `<v|111> = 0` and `Y(v) = -1`.
Therefore the lepton singlet block is carrier-level orthogonal to the
dark state. Verified at machine precision (Test 5, 11).

**Step 5 (SU(3)_c trivial on lepton, non-trivial on dark).** By
CL3_COLOR_AUTOMORPHISM (Section B and H), SU(3)_c is embedded as
`T^a_8d = (M_3_sym (x) I_2)` where `M_3_sym` acts on the 3D symmetric
base block and is zero on the 1D antisymmetric block. Numerically:
`max |T^a_8d @ lepton_vec| = 0` (machine precision); `max |T^a_8d @ |111>|
= 0.5774` (non-trivial). Therefore SU(3)_c acts trivially on the lepton
block (singlet representation) and non-trivially on the dark state
(fundamental representation). Verified at machine precision (Test 11b).

**Step 6 (Fierz completeness on End(C^N_c)).** By CL3_COLOR_AUTOMORPHISM
(Section D), `End(C^N_c) = singlet (1D) + adjoint (N_c^2-1 = 8D)` with
weights `F_sing = 1/N_c^2 = 1/9` and `F_adj = (N_c^2-1)/N_c^2 = 8/9`.
The projectors satisfy `P_sing^F + P_adj^F = I` on `End(C^N_c)` and
`Tr[P_sing^F] = 1`, `Tr[P_adj^F] = 8`. Verified at machine precision
(Test 6).

**Step 7 (Singlet Fierz annihilates gauge-mediated propagators).**
The singlet Fierz projector maps `M -> (Tr M / N_c) I`. For any traceless
matrix `T^a` (Gell-Mann generator), `Tr T^a = 0`, so
`P_sing^F @ T^a = 0`. The adjoint Fierz projector preserves traceless
matrices: `P_adj^F @ T^a = T^a`. Verified at machine precision
(Test 11c).

**Step 8 (Gauge-mediated sandwich identity).** A gauge-mediated mass
renormalization on a color-charged state has the schematic color
sandwich `sum_a T^a M T^a`. The standard SU(N) Fierz identity gives

```text
sum_a T^a M T^a = (1/2) Tr(M) I - (1/(2N)) M.
```

For a traceless matrix `M = T^b`, this remains in the adjoint channel.
For the one-loop fundamental self-energy `M = I`, it becomes
`C_F I`, which is singlet-channel. The earlier claim that every
gauge-mediated mass propagator lives entirely in the adjoint Fierz
channel is therefore too broad and is not retained here.

**Step 9 (Corrected bridge boundary).** By Step 5, the dark state
`|111>` is color-charged (SU(3)_c-fundamental), and by Step 4 it is
orthogonal to the lepton block. Those carrier facts are preserved.
They do not by themselves prove that the scalar one-loop self-energy
projects through the adjoint Fierz channel. For the G1 scalar
multiplier, the load-bearing bridge is instead the CW note's
Casimir-plus-hop calculation: `sum_a T^a T^a = C_F I` per link and
forward/backward Wilson-hop pairing gives `2 C_F = 8/3`.

**Step 10 (Per-color-row scalar trace density).** By the cited
Gell-Mann normalization `Tr[T^a T^b] = (1/2) delta^{ab}`, the
per-color-row scalar trace density is

```text
rho_{adj/c}  =  2 * sum_a Tr[T^a T^a] / N_c  =  (N_c^2 - 1)/N_c  =  8/3.
```

Verified at machine precision (Test 8).

**Step 11 (Composition with Wilson kinetic mass).** Substituting into
the cited Origin B factorization (DM_ETA_FREEZEOUT_BYPASS, § Origin B,
eq. `m_DM = (dim(adj_3)/N_c) * 2 * hw_dark * v`):

```text
m_DM  =  (8/3) * 2 * 3 * v  =  (8/3) * 6 v  =  16 v.
```

The integer identity `dim(adj_3) * 2 * hw_dark / N_c = 16 = N_sites`
anchors Origin A (spacetime APBC, 2^d = 16) to Origin B (chiral cube +
adjoint density). Verified at machine precision (Test 10).

**Step 12 (Wrong-channel sanity).** Six alternate scalar candidates are
explicitly distinct from 8/3: F_singlet = 1/9, no enhancement = 1,
1/N_c = 1/3, C_F = 4/3, C_A = 3, C_A/C_F = 9/4 (Test 9). Only the
forward/backward Wilson-hop doubled Casimir, equivalently the per-row
scalar trace density, gives 8/3.

**QED on the carrier support and corrected scalar-trace bridge
boundary.**

## 3. Claim Boundary

This bounded support theorem supplies carrier support and a corrected
claim boundary for the DM-eta G1 dynamical residual. The dark `hw=3` state
`|111>` on the Cl(3) chiral cube `C^8` lies in the 3D symmetric-base
subspace and is orthogonal to the 1D antisymmetric-base lepton singlet.
The singlet Fierz projector annihilates traceless matrices `T^a`, but
the one-loop scalar self-energy `sum_a T^a T^a = C_F I` is
singlet-channel. The retained load-bearing content is the carrier
orthogonality plus the per-row scalar trace density
`rho_{adj/c} = 8/3`; the prior adjoint-channel bridge claim is
superseded.

No new axioms or repo-wide dynamical premises are introduced.

## 4. What is closed, bounded, and open

### Closed by V1 (operator-level bridge)

1. **Carrier-level dark-state location**: |111> in 3D symmetric base
   (color triplet, Y=+1/3) verified at machine precision.
2. **Lepton-block orthogonality**: lepton singlet (Y=-1, antisym base)
   has zero overlap with the dark state, verified at machine precision.
3. **SU(3)_c representation identification**: trivial on lepton block,
   fundamental on dark state, verified at machine precision via the
   cited M_3_sym (x) I_2 embedding.
4. **Singlet Fierz channel annihilation of traceless generators**:
   `P_sing^F @ T^a = 0` for all 8 Gell-Mann generators, verified at
   machine precision.
5. **Corrected bridge boundary**: the scalar one-loop self-energy is
   `C_F I`, hence singlet-channel; no adjoint-channel projection is
   asserted.
6. **Per-color-row scalar trace density** = (N_c^2-1)/N_c = 8/3 exactly.
7. **Composition** m_DM = (8/3)*6v = 16v on canonical surface.

### Inherited bounded inputs (NOT closed by V1)

1. **A0 hierarchy compression** -- inherited assumption from the parent
   bounded theorem.
2. **Sommerfeld band** S_vis/S_dark in [1.4, 1.7] -- inherited bounded.
3. **Freeze-out coefficient** x_F in [22, 28] -- inherited bounded.
4. **alpha_X = alpha_LM** -- inherited bounded candidate-route choice.

### Honest residual on the bridge mechanism

The bridge proof relies on the structural identification
"gauge-mediated propagator" = "constructed from T^a generators". This
identification is cited from CL3_COLOR_AUTOMORPHISM Section H (the
Gell-Mann embedding), not derived in this note. A reviewer might
challenge whether the dark hw=3 mass renormalization on the
SU(3)-gauged staggered chiral cube is *necessarily* of the
gauge-mediated form `Sigma_a T^a (x) T^a` rather than admitting some
gauge-singlet self-energy contribution. This residual sub-claim is the
last-mile structural input -- it is not derived from a deeper Wilson
action calculation in this note. A future explicit Coleman-Weinberg
derivation on the SU(3)-gauged chiral cube would close this residual
to retained-grade.

For now, the bridge sub-claim "the dark mass operator on the
SU(3)-gauged chiral cube is gauge-mediated, not self-energy" is the
remaining structural input. It is consistent with the cited Wilson
action structure (the bare hopping kernel includes link insertions
`U_mu`, which are SU(3) elements built from T^a), and the
counterfactual sanity (Test 9) rules out the alternative C_F, C_A,
C_A/C_F Casimir-self-energy options as wrong-channel.

## 5. What this theorem does NOT claim

- That the parent DM-eta freezeout-bypass lane is now retained-grade.
  This V1 closes the G1 dynamical step's bridge; the parent lane still
  carries A0, x_F, Sommerfeld, alpha_X bounded inputs.
- That a Coleman-Weinberg-on-chiral-cube derivation has been supplied.
  The bridge mechanism is structural (carrier orthogonality + Fierz
  selection), not a perturbative loop calculation.
- That a new axiom is introduced. The note uses cited authorities:
  (base x fiber) decomposition (CL3_COLOR_AUTOMORPHISM B), Y spectrum
  (CL3_COLOR_AUTOMORPHISM F), SU(3)_c on sym base (CL3_COLOR_AUTOMORPHISM
  B+H), Fierz completeness (CL3_COLOR_AUTOMORPHISM D), chiral cube
  (CL3_TASTE_GENERATION), bare Wilson kinetic mass (DM_ETA_FREEZEOUT_BYPASS
  Origin B). No new axioms, no new dynamical mechanisms.

## 6. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_eta_g1_bridge_proof_2026_05_06.py
```

Expected: `PASS = 15, FAIL = 0`.

**Object-level matrix tests run:**

1. Chiral cube `C^8 = (C^2)^otimes 3` Burnside `1+3+3+1` (exact).
2. (base x fiber) decomposition `6+2 = 8` (exact).
3. Hypercharge Y spectrum `{+1/3 (6D), -1 (2D)}` (exact).
4. Dark `|111>` in color triplet (`<111|P_symm|111> = 1`, exact).
5. Lepton block `(|01>-|10>)/sqrt(2)` orthogonal to dark (exact).
6. Fierz completeness `P_sing^F + P_adj^F = I` on End(C^3) (max err < 1e-12).
7. **BOUNDARY**: carrier orthogonality preserved; gauge-mediated
   adjoint Fierz selection rejected for the scalar self-energy.
8. Per-color-row scalar trace density `(N_c^2-1)/N_c = 8/3` (exact).
9. Six wrong-channel candidates all distinct from 8/3 (exact ruleouts).
10. Composition `m_DM = (8/3)*6v = 16v` on canonical surface (exact).
11. Carrier-orthogonality numerical check (exact).
12. SU(3)_c trivial on lepton block, non-trivial on dark (exact).
13. Singlet Fierz annihilates Gell-Mann T^a (exact).
14. Counterfactual Pass scoring (informational; b2 wins).
15. Parent-scope unchanged after correction (informational).

## 7. Honest residual

- **Coleman-Weinberg-on-chiral-cube explicit calculation**: supplied by
  the companion CW note as the corrected Casimir-plus-hop mechanism.
  This bridge note does not independently promote parent status; the
  corrected chain still requires independent audit.
- **A0 hierarchy compression**: inherited assumption; not lifted.
- **Sommerfeld + freeze-out band**: inherited bounded.
- **alpha_X = alpha_LM**: inherited bounded candidate-route choice.
- **Numerical consequence on inherited inputs**: `m_DM = 3.94 TeV`
  unchanged from the parent bounded theorem.

## 8. Position on the publication surface

This V1 bounded support theorem corrects the former operator-level
adjoint-channel bridge step:

- **The G1 algebraic step** is closed (V1 algebraic note).
- **The G1 dynamical operator-trace arithmetic step** is closed (V1
  dynamical-residual note).
- **The G1 operator-level adjoint-channel bridge step** is removed as
  a load-bearing claim; carrier orthogonality remains bounded support.
- **The DM-eta G1 lane** is therefore reduced to audit of the corrected
  Casimir-plus-hop scalar-trace chain and its inherited bounded inputs.

The flagship paper line should remain `eta` IMPORTED with this theorem
listed only as bounded carrier/scalar-trace support for the DM-eta G1
dynamical-step correction. The parent DM-eta freezeout-bypass lane
status does not change here; any parent promotion requires independent
audit of the corrected dependency chain.

## 9. Cross-references

- DM-eta G1 dynamical residual V1 (corrected scalar-trace support):
  [`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md)
- DM-eta G1 algebraic support V1:
  [`DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md)
- DM-eta freezeout-bypass quantitative theorem (parent bounded theorem):
  [`DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md`](DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md)
- Cl(3) color automorphism (load-bearing one-hop authority):
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- Cl(3) taste generation (chiral cube structure):
  [`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md)

## 10. Hypothesis set used (formal)

```yaml
claim_type: bounded_theorem
claim_scope: |
  Carrier and scalar-trace support for the DM-eta G1 dynamical
  residual: the dark hw=3 state on the SU(3)-gauged chiral cube C^8
  lies in the 3D symmetric-base color triplet (Y=+1/3) and is
  orthogonal to the 1D antisymmetric-base lepton singlet (Y=-1). The
  standard SU(N) sandwich identity shows that a traceless test matrix
  remains adjoint-channel, but the scalar one-loop self-energy
  sum_a T^a T^a = C_F I is singlet-channel. The load-bearing
  multiplier is the per-color-row scalar trace density
  rho_{adj/c} = 2 C_F = (N_c^2-1)/N_c = 8/3, with composition
  m_DM = 16v on the canonical surface when the cited bare Wilson
  kinetic mass is used. Six alternate scalar candidates are explicitly
  ruled out.
upstream_dependencies:
  - dm_eta_g1_dynamical_residual_operator_trace_support_theorem_note
  - dm_eta_g1_cl3_adj3_embedding_algebraic_support_theorem_note
  - dm_eta_freezeout_bypass_quantitative_theorem
  - cl3_color_automorphism_theorem
  - cl3_taste_generation_theorem
admitted_context_inputs:
  - SU(N) Fierz identity (already in CL3_COLOR_AUTOMORPHISM)
  - Standard Lie-algebra Casimir values (already in SU3_ADJOINT_CASIMIR)
  - Standard Wilson lattice action (cited in DM_ETA_FREEZEOUT_BYPASS)
no_new_axioms: true
no_new_combinatorial_inputs: true
no_new_dynamical_mechanisms: true
counterfactual_pass_done: true
runner_passes: 15
runner_fails: 0
```

---

## Reading rule

This note is the corrected claim boundary for the former
operator-level adjoint-channel bridge step on the DM-eta G1 dynamical
residual. It sharpens the DM-eta G1 lane by preserving carrier support
and removing the unsupported adjoint-channel selection rule. Any
downstream parent-status change requires independent audit of the
corrected dependency chain.
