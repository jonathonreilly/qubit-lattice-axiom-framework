# DM-eta G1 Fierz Channel Narrative Correction Note

**Date:** 2026-05-27
**Status:** **bounded source-correction note** clarifying a narrative
contradiction in three landed G1 chain notes from 2026-05-06. This note
corrects how the algebraic identity `(N_c^2 - 1)/N_c = 8/3` is described
in the DM-eta G1 chain. It does NOT change the arithmetic outcome, does
NOT change `m_DM = 16 v` on the canonical surface, and does NOT introduce
any new mechanism. It explicitly removes the load-bearing narrative claim
that the dark mass operator `Sigma_a T^a T^a` projects through the
*adjoint* Fierz channel of `End(C^N_c)`. That claim is incompatible with
the runner's own Test 12 output and with the standard SU(N) Fierz
identity. The corrected narrative attributes `8/3` to a Casimir +
forward+backward Wilson-hop geometric doubling, with the operator
`Sigma_a T^a T^a` correctly identified as living in the SINGLET channel
of `End(C^N_c)`.

**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Affects:** three landed G1 chain notes from 2026-05-06.
**Does not affect:** arithmetic identity `8/3 = (N_c^2-1)/N_c`, the
runner-verified `PASS = 17/17, 15/15, 12/12` test counts, or the
`m_DM = 16 v` canonical-surface composition.

## Cited authorities

- [`DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md)
  -- the explicit Wilson-link CW note. Test 12 of its runner produces
  `||P_sing @ Sigma|| = 0.456`, `||P_adj @ Sigma|| = 0.000` for the
  one-loop self-energy `Sigma = (1/Volume) sum_q sum_a T^a D(q) T^a`,
  numerically demonstrating that `Sigma_a T^a T^a = C_F I` lives in the
  SINGLET Fierz channel of `End(C^N_c)`. This is consistent with the
  textbook SU(N) Fierz identity. The note's Section 2 Step 6 already
  partially acknowledges this ("the per-link self-energy `sum_a T^a T^a
  = C_F I` is proportional to the identity; in the Fierz channel
  decomposition of `End(C^N_c)`, an identity matrix lives on the
  SINGLET channel (Test 12)") but the headline and several earlier
  passages retain the contradictory "adjoint Fierz channel" framing.
- [`DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md)
  -- the operator bridge proof. Steps 7-9 frame the bridge as
  "gauge-mediated propagator therefore lives entirely in the adjoint
  Fierz channel" via a `Sigma_a T^a M T^a` template argument. This is
  not generally true: for `M = I` (the natural self-energy structure
  for a fundamental scalar), `Sigma_a T^a I T^a = ((N^2-1)/(2N)) I =
  C_F I`, which is SINGLET (proportional to identity).
- [`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md)
  -- the operator-trace support note that introduced the "adjoint
  Fierz channel projection" framing. Its arithmetic (Steps 1-3) is
  correct as a *per-color-row trace density* computation; the
  conflation with a Fierz channel projection is the narrative gap
  this note corrects.
- [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
  -- Section D Fierz completeness on `End(C^N_c)`; Section H Gell-Mann
  embedding with `Tr[T^a T^b] = (1/2) delta^{ab}`. The Fierz channel
  decomposition `End(C^N_c) = singlet (1D) + adjoint (N_c^2 - 1)D` is
  used here at the standard textbook level.
- [`SU3_ADJOINT_CASIMIR_THEOREM_NOTE_2026-05-02.md`](SU3_ADJOINT_CASIMIR_THEOREM_NOTE_2026-05-02.md)
  -- standard Casimir values `C_F = (N^2-1)/(2N) = 4/3` and `C_A = N
  = 3`.

## 0. Headline

The 8/3 algebraic identity used in the DM-eta G1 chain is correct:

```
(N_c^2 - 1) / N_c = 2 * C_F = 8/3        (for N_c = 3)
```

The narrative attribution of this identity to "adjoint Fierz channel
projection of the dark mass operator" is **wrong**. The correct
attribution is:

- `C_F = (N_c^2 - 1)/(2N_c) = 4/3` is the standard one-loop Casimir for
  a color-fundamental, arising from `sum_a T^a T^a = C_F I` (textbook
  SU(N) one-loop Coleman-Weinberg).
- The matrix `C_F I` is **proportional to the identity**, hence lives in
  the **SINGLET channel** of the Fierz decomposition `End(C^N_c) =
  singlet (1D) + adjoint (N_c^2 - 1)D`.
- The factor of 2 turning `C_F = 4/3` into `8/3` is **geometric**: the
  chiral-cube Wilson hopping kernel pairs forward and backward links
  per direction `(U_mu + U_mu^dagger)`, doubling the per-link Casimir
  contribution.

The framework's algebraic identity `8/3 = (N_c^2 - 1)/N_c` is also
equal to `Sigma_a Tr[T^a T^a] * 2 / N_c`, which is a **per-color-row
trace density** computation. This is **not** a Fierz channel projection
on `End(C^N_c)`. It is the scalar `(1/N_c) Tr[2 * C_F I] = 2 * C_F`, a
per-row trace of a singlet-channel matrix.

The runner's Test 12 explicitly confirms the singlet attribution:
`||P_sing @ Sigma_loop|| = 0.456`, `||P_adj @ Sigma_loop|| = 0.000`
for the discretized one-loop self-energy `Sigma_loop = sum_q sum_a T^a
D(q) T^a / Volume`.

## 1. The contradiction in the landed notes

The 2026-05-06 G1 chain has three notes that introduce the structural
claim "the dark mass operator projects through the adjoint Fierz
channel":

(i)   `DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`
     -- Section 2 ("operator-trace projection through the adjoint Fierz
     channel"), Theorem statement Step 7 ("Carrier-level necessary
     condition `dim(C^8) = dim(adj_3) = 8`"), and the "operator-level
     adjoint-channel bridge step" named as the open residual.
(ii)  `DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md`
     -- Steps 7-9 of the proof. Step 8 reads: "A typical
     gauge-mediated mass renormalization on a color-charged state has
     the form `Sigma_a T^a M T^a` for some matrix M; this is built
     from traceless generators T^a. By Step 7, this propagator's
     singlet Fierz projection is zero (since `P_sing^F @ T^a = 0`).
     The full gauge-mediated propagator therefore lives entirely in
     the adjoint Fierz channel." This conclusion is not valid for
     `M = I` (the natural self-energy structure for a fundamental
     scalar at one loop), where `Sigma_a T^a I T^a = C_F I` is on
     the SINGLET channel.
(iii) `DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md`
     -- Step 6 (Fierz channel verification) explicitly recognizes
     that `sum_a T^a T^a = C_F I` lives on the singlet channel, but
     the Headline (Section 0), the proof's "carrier-orthogonality +
     gauge-mediated Fierz selection" framing, and Section 4 Closed
     item 5 ("equivalent per-color-row Fierz trace density reading")
     retain the contradictory "adjoint Fierz channel" framing.

The runner output for `frontier_dm_eta_g1_coleman_weinberg_2026_05_06.py`
Test 12 explicitly displays this:

```
TEST 12: Discretized 1-loop self-energy on Z^3 lattice
  Sigma_loop[0,0]  = 0.263368 (proportional to identity)
  Off-diag err     = 5.551e-17
  Sigma is C_F * sum_q D(q) / Vol = (4/3) * <D>
  ||P_sing  @ Sigma|| = 0.456167
  ||P_adj   @ Sigma|| = 0.000000
  NOTE: Point-coupling Sigma = C_F*I lives on Fierz SINGLET channel.
```

This is the runner's own self-consistency check. The "Note" line
correctly states the operator lives on the singlet channel, but the
upstream narrative claims an adjoint-channel projection.

## 2. The math: SU(N) Fierz identity properly applied

The textbook SU(N) Fierz identity in the standard normalization
`Tr[T^a T^b] = (1/2) delta^{ab}` is:

```text
Sigma_a (T^a)_{ij} (T^a)_{kl}
   =  (1/2) delta_{il} delta_{jk}  -  (1/(2N)) delta_{ij} delta_{kl}.
```

This is an identity on the bilinear tensor `T^a otimes T^a`, NOT a
projector on a single matrix in `End(C^N)`. Two consequences:

**(a) Sandwich identity.** Contracting with a matrix M acting in the
middle slot:

```text
Sigma_a (T^a M T^a)_{il}
   =  Sigma_a (T^a)_{ij} M_{jk} (T^a)_{kl}
   =  (1/2) Tr(M) delta_{il}  -  (1/(2N)) M_{il}.
```

Equivalently:

```text
Sigma_a T^a M T^a  =  (1/2) Tr(M) I  -  (1/(2N)) M.
```

- For **M = I**: `Sigma_a T^a I T^a = (N/2) I - (1/(2N)) I = ((N^2-1)/(2N)) I = C_F I`.
  Proportional to identity -> **SINGLET channel** of `End(C^N_c)`.
- For **M = T^b** (traceless): `Sigma_a T^a T^b T^a = -(1/(2N)) T^b`.
  Same direction as T^b -> **ADJOINT channel** of `End(C^N_c)`.

The bridge proof's Step 8 claim "for some matrix M, `Sigma_a T^a M
T^a`... lives entirely in the adjoint Fierz channel" is therefore not
generally true. It is true only when `Tr(M) = 0`. For the natural
self-energy at one loop on a fundamental scalar, the structure is the
direct Casimir `Sigma_a T^a T^a = C_F I` (no traceless M in the
middle), and this is on the SINGLET channel.

**(b) Single-matrix Fierz projection in `End(C^N_c)`.** For any matrix
M in `End(C^N_c)`, the singlet and adjoint Fierz projectors decompose
M as:

```text
P_sing  M  =  (Tr M / N_c) I
P_adj   M  =  M  -  (Tr M / N_c) I.
```

These are orthogonal projectors with `P_sing + P_adj = identity`,
`Tr[P_sing] = 1` (one singlet basis vector, the normalized identity),
`Tr[P_adj] = N_c^2 - 1` (`N_c^2 - 1` adjoint basis vectors, the
traceless N_c x N_c matrices).

For `M = C_F I` (the per-link self-energy on a fundamental):
`Tr M = C_F N_c`, so `P_sing M = (C_F N_c / N_c) I = C_F I = M`.
That is, M is **entirely in the singlet channel**. `P_adj M = 0`.
This is the runner Test 12 result.

For `M = T^b` (any single Gell-Mann generator): `Tr T^b = 0`, so
`P_sing T^b = 0` and `P_adj T^b = T^b`. Each T^b is **entirely in
the adjoint channel**. This is the runner Tests 9-10 result.

The bridge proof's Step 7 ("`P_sing^F @ T^a = 0`") is correct. The
Step 8 extension ("therefore `Sigma_a T^a M T^a` is adjoint") is
**not** correct for M = I, where the entire operator is singlet.

## 3. The correct attribution of 8/3

The identity `8/3` appears in the G1 chain through two distinct
algebraic operations that the landed notes conflate:

**(I) Casimir + forward+backward Wilson-hop doubling.**

```text
2 * C_F  =  2 * (N^2 - 1)/(2N)  =  (N^2 - 1)/N  =  8/3.
```

`C_F` is the single-Wilson-link one-loop Casimir for a color-fundamental
(`sum_a T^a T^a = C_F I`, proportional to identity, singlet channel).
The factor of 2 is **geometric**: the chiral-cube Wilson kernel
`K_W = 2r * sum_mu (U_mu + U_mu^dagger)` pairs forward `U_mu` and
backward `U_mu^dagger` links per direction. Each link contributes the
single-link Casimir independently, doubling the contribution per
direction.

This reading correctly describes the runner's calculation and the
mathematical content of the explicit Wilson-link CW expansion.

**(II) Per-color-row scalar trace density.**

```text
(1/N_c) * 2 * sum_a Tr[T^a T^a]
   =  (1/N_c) * 2 * (N^2 - 1)/2
   =  (N^2 - 1) / N
   =  8/3.
```

`Sum_a Tr[T^a T^a] = (N^2 - 1)/2` follows from `Tr[T^a T^b] =
(1/2) delta^{ab}` summed over a. The factor of 2 again absorbs the
forward+backward Wilson-hop pair. Dividing by `N_c` yields a per-row
scalar (a trace divided by the number of color rows). This is a
**scalar trace density**, not a Fierz channel projection.

Note that Reading (II) is the SCALAR `(1/N_c) Tr[2 C_F I] = 2 C_F`,
because `sum_a Tr[T^a T^a] = Tr[sum_a T^a T^a] = Tr[C_F I] = C_F N_c`,
so `(1/N_c) * 2 * sum_a Tr[T^a T^a] = (1/N_c) * 2 * C_F * N_c = 2 C_F`.
Readings (I) and (II) are algebraically equivalent (this is what the
Coleman-Weinberg note's Test 13 verifies).

**The 8 in `dim(adj) = N^2 - 1 = 8`** appears as the count of Gell-Mann
matrices (the dimension of the SU(3) adjoint rep) entering
`sum_a Tr[T^a T^a]`. The dimension `dim(adj)` is structural group
theory; its appearance in the *scalar* `(N^2-1)/N` is via the standard
identity `sum_a Tr[T^a T^a] = dim(adj) * T_F = 8 * (1/2)`, not via a
Fierz channel projection of the dark mass operator onto the adjoint
subspace of `End(C^N_c)`.

## 4. Resolution: Option C

This audit-correction adopts **Option C** of the three resolutions the
contradiction admits:

- **Option A (downgrade)** -- abandon the Fierz framing entirely;
  treat `8/3 = 2 C_F` as Casimir arithmetic only, with the structural
  `8/3 = dim(adj_3)/N_c` reading explicitly demoted to algebraic
  identity without Fierz-channel structural significance.
- **Option B (different operator)** -- replace `sum_a T^a T^a` with
  some other operator `sum_a T^a M T^a` for traceless M (which would
  genuinely live in the adjoint channel via the sandwich Fierz
  identity), and check whether 8/3 emerges. This option requires
  introducing a new dynamical mechanism not justified by the standard
  one-loop CW machinery on a fundamental scalar, and would constitute
  a new dynamical input.
- **Option C (distinguish operations)** -- recognize that the landed
  notes conflate "Fierz channel projection of a matrix in `End(C^N_c)`"
  with "per-color-row scalar trace density of a singlet-channel
  matrix". These ARE distinct algebraic operations. The 8/3 identity
  is correct as Reading (I) [2 * C_F geometric] and Reading (II) [per-
  color-row scalar trace], with the matrix `sum_a T^a T^a = C_F I`
  correctly identified as singlet-channel. The "adjoint Fierz channel
  projection of the dark mass operator" narrative is removed.

Option B is rejected because the standard one-loop CW Casimir on a
fundamental scalar is `sum_a T^a T^a = C_F I`; introducing a different
operator structure with traceless M is a new dynamical input. The
framework's `feedback_no_new_axioms.md` discipline forbids this.

Option A and Option C reach the same arithmetic endpoint
(`m_DM = 16 v`) and the same Casimir + geometric-doubling mechanism.
Option C preserves more of the existing structure -- it does not
demote `dim(adj_3)/N_c` to numerology; it correctly identifies the
arithmetic identity `dim(adj_3)/N_c = 2 C_F` as a *consequence* of the
SU(N) algebra (the count of Gell-Mann generators and their
normalization), without claiming it arises from a Fierz channel
projection on `End(C^N_c)`.

This note adopts Option C. The correction edits in the three landed
notes are minimal and surgical: each note retains its arithmetic
content, runner test counts, and `m_DM = 16 v` conclusion. The
"adjoint Fierz channel" narrative is replaced with "Casimir +
forward+backward Wilson-hop geometric doubling" wherever it appears
as a load-bearing structural claim.

## 5. Implications for the bounded G1 chain

This correction is **a narrative clarification, not a mechanism
change**. The corrected mechanism is:

1. The dark `|111>` state is a color fundamental (verified in the
   runner Test 3 of all three notes; this is independent of the Fierz
   narrative).
2. The standard one-loop Coleman-Weinberg self-energy on a fundamental
   scalar is `Sigma_a T^a T^a = C_F I` per single Wilson link, with
   `C_F = (N^2-1)/(2N) = 4/3` (textbook SU(N) Casimir).
3. The chiral-cube Wilson kinetic kernel `K_W = 2r * sum_mu (U_mu +
   U_mu^dagger)` pairs forward and backward links per direction,
   independently contributing the single-link Casimir; the
   per-direction enhancement is `2 * C_F = 8/3`.
4. The bare Wilson kinetic mass for the dark hw=3 singlet is `2r *
   hw_dark = 6 v` on the canonical surface (cited Origin B).
5. Composition: `m_DM = (8/3) * 6 v = 16 v = N_sites * v` on canonical
   surface (Origin A <-> Origin B integer identity).

The bounded G1 chain's downstream conclusion `m_DM = 16 v` is
**unchanged**. The runner test counts (`17/17, 15/15, 12/12 PASS`) are
**unchanged**. Downstream bounded eta-prediction work that uses
`m_DM = N_sites * v = 16 v` as a structural product depends on the
product value, not on the rejected adjoint-channel narrative. The
mechanism by which 8/3 emerges from the G1 chain is what this
correction adjusts; the value of m_DM at the end of the chain is
**unchanged**.

What is **honestly downgraded** by this correction:

- The structural significance of `dim(adj_3)/N_c = 8/3` as evidence
  for an adjoint-channel mechanism in the dark mass renormalization
  is **removed**. The algebraic identity `dim(adj_3)/N_c = 2 C_F`
  remains, but it is a consequence of the SU(N) generator count and
  normalization, not a Fierz-channel projection of the dark mass
  operator.
- The "operator-level adjoint-channel bridge step" in the bridge
  proof note's Section 3 (Claim Boundary) and Section 4 (Closed item
  5: "Bridge selection rule: the dark mass operator's gauge-mediated
  color trace projects entirely through the adjoint Fierz channel")
  is **removed** as a structural claim. The remaining content is
  the Casimir + geometric-doubling mechanism, which is standard
  textbook one-loop CW on a fundamental with the chiral-cube Wilson
  kernel structure.

What is **unchanged**:

- The arithmetic identity `8/3 = (N_c^2 - 1)/N_c = 2 C_F` (the runner
  verifies this at exact rational precision).
- The standard one-loop CW Casimir `sum_a T^a T^a = C_F I` for a
  color-fundamental (textbook SU(N), runner Test 4).
- The dark `|111>` color-fundamental status (runner Test 3 of each
  note).
- The forward+backward Wilson hop pair on the chiral-cube kernel
  (cited Origin B factorization).
- The composition `m_DM = (8/3) * 6 v = 16 v` on the canonical
  surface (runner Test 15 of CW note).
- The runner PASS/FAIL counts of all three notes' runners.

## 6. Specific corrections to the three landed notes

This note carries surgical "Audit-correction (2026-05-27)" edits to
the three landed G1 notes. Each edit adds a correction section near the
top of the corresponding note, and this landing also updates surviving
load-bearing wording inline where the old proof text would otherwise
continue to assert the rejected adjoint-channel mechanism.

The specific corrections per note:

**`DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md`:**
- The headline "operator-trace projection through the adjoint Fierz
  channel" framing is corrected. The accurate mechanism is "Casimir
  + forward+backward Wilson-hop doubling on the chiral cube".
- Section 0 Step 2 ("the dynamical operator-trace step ... operator-
  trace projection through the adjoint Fierz channel") is corrected
  to refer to the per-color-row scalar trace density (not a Fierz
  channel projection).
- Section 2 Step 6's Fierz channel verification is correct as
  written (it already identifies `sum_a T^a T^a = C_F I` as singlet);
  the surrounding narrative referring to "Fierz adjoint channel
  selection" is corrected.
- Section 4 Closed item 5 ("Equivalent per-color-row Fierz trace
  density reading") is corrected: the per-color-row trace density is
  a scalar trace, not a Fierz channel projection. The two readings of
  8/3 (2 C_F geometric and per-row trace) are algebraically
  equivalent because both equal `(N^2-1)/N`, but neither is a Fierz
  channel projection.

**`DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md`:**
- The theorem's load-bearing claim "the dark hw=3 mass operator on
  the SU(3)-gauged chiral cube projects through the adjoint Fierz
  channel of `End(C^N_c)` and not the singlet channel" is
  corrected. The operator `sum_a T^a T^a = C_F I` is in the singlet
  channel. The 8/3 arithmetic arises from Casimir + geometric
  doubling, and the original bridge proof is retained only as carrier
  and scalar-trace support.
- Step 8 ("gauge-mediated propagator selection rule") is corrected.
  The conclusion holds when M is traceless; it does NOT hold when
  M = I (the natural self-energy structure).
- Step 9 ("Bridge: dark mass operator selects adjoint") is corrected.
  The carrier-orthogonality argument (Step 4-5) remains valid; the
  Fierz-channel argument does not.

**`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`:**
- The headline "operator-trace projection through the adjoint Fierz
  channel" is corrected to "per-color-row scalar trace density".
- The Counterfactual Pass route (c) ("adjoint Fierz channel
  projection") is relabeled to "per-color-row scalar trace density
  + forward+backward Wilson-hop geometric doubling".
- Section 2 Step 7 ("Carrier-level necessary condition `dim(C^8) =
  dim(adj_3) = 8`") is preserved as a structural observation about
  the SU(3) generator count, but is no longer framed as a necessary
  condition for an adjoint-channel projection.

## 7. What this note does NOT claim

- That the G1 chain is wrong arithmetically. The arithmetic identity
  `8/3 = (N_c^2 - 1)/N_c` and the composition `m_DM = 16 v` are
  unchanged.
- That the runner tests fail. They pass exactly as recorded; the
  runner's Test 12 has correctly displayed the singlet attribution
  since the notes landed, but the narrative in the prose did not
  match.
- That `m_DM = N_sites * v = 16 v` is no longer the candidate dark
  mass. The structural product remains as recorded in
  the DM-eta N_sites-v structural support note and used by PR #2064.
- That the bounded eta prediction in PR #2064 is invalidated. PR
  #2064's premise P2 cites the structural product `m_DM = N_sites *
  v` as a bounded input from
  `DM_ETA_NSITES_V_STRUCTURAL_SUPPORT_LIFT_THEOREM_NOTE_2026-04-29.md`;
  the mechanism through which the 8/3 enters is what this note
  corrects, not the value of m_DM.
- That a new dynamical mechanism is introduced. Option B is
  explicitly rejected. The corrected mechanism is the standard
  one-loop Coleman-Weinberg Casimir on a fundamental scalar, with
  the chiral-cube Wilson kernel's forward+backward hop pair as the
  geometric origin of the factor of 2.
- That a new axiom is introduced. The framework's
  `feedback_no_new_axioms.md` is honored. The standard SU(N) Fierz
  identity used in this correction is the textbook one already cited
  in `CL3_COLOR_AUTOMORPHISM_THEOREM.md` Section D.

## 8. Position on the publication surface

- The G1 chain's `m_DM = 16 v` candidate-statement is preserved.
- The mechanism's narrative is sharpened from "adjoint Fierz channel
  projection" to "Casimir + forward+backward Wilson-hop doubling".
- The structural significance of `8/3 = dim(adj_3)/N_c` as evidence
  for an adjoint-channel mechanism is removed; the identity remains
  as `8/3 = 2 C_F` Casimir arithmetic with `dim(adj) = N^2 - 1 = 8`
  entering as the generator count in `sum_a Tr[T^a T^a] = (N^2-1)/2`.
- The bounded eta prediction in PR #2064 is unaffected at the
  prediction level (`eta_pred in [4.94e-10, 7.24e-10]`); the
  structural input `m_DM = 16 v` is unchanged.

The independent audit lane retains authority over the parent DM-eta
freezeout-bypass row's effective status. This note is an
audit-correction landed on the framework surface to remove the
narrative contradiction; the audit lane's verdict on the corrected
chain remains to be issued.

## 9. Cross-references

- DM-eta G1 Coleman-Weinberg note (correction target 1):
  [`DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_COLEMAN_WEINBERG_BOUNDED_THEOREM_NOTE_2026-05-06.md)
- DM-eta G1 operator bridge proof (correction target 2):
  [`DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_OPERATOR_BRIDGE_PROOF_THEOREM_NOTE_2026-05-06.md)
- DM-eta G1 dynamical residual operator-trace (correction target 3):
  [`DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_DYNAMICAL_RESIDUAL_OPERATOR_TRACE_SUPPORT_THEOREM_NOTE_2026-05-06.md)
- DM-eta G1 algebraic support (algebraic identity, unaffected):
  [`DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md`](DM_ETA_G1_CL3_ADJ3_EMBEDDING_ALGEBRAIC_SUPPORT_THEOREM_NOTE_2026-05-06.md)
- DM-eta freezeout-bypass parent and N_sites-v structural product:
  mentioned only as unaffected downstream context; not direct evidence
  for this correction note.
- Cl(3) color automorphism (Fierz primitive, Section D):
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
- SU(3) adjoint Casimir (`C_F = 4/3`, `C_A = 3`):
  [`SU3_ADJOINT_CASIMIR_THEOREM_NOTE_2026-05-02.md`](SU3_ADJOINT_CASIMIR_THEOREM_NOTE_2026-05-02.md)

## 10. Hypothesis set used (formal)

```yaml
claim_type: bounded_theorem
claim_scope: |
  Narrative clarification of the DM-eta G1 chain (three 2026-05-06
  notes). The arithmetic identity 8/3 = (N_c^2-1)/N_c = 2 C_F is
  unchanged; the runner test counts (17/17, 15/15, 12/12 PASS) are
  unchanged; the composition m_DM = 16 v is unchanged. The
  "operator-trace projection through the adjoint Fierz channel"
  narrative is removed because the dark mass operator sum_a T^a T^a
  = C_F I is on the SINGLET channel of End(C^N_c). The corrected
  mechanism is Casimir + forward+backward Wilson-hop geometric
  doubling: 8/3 = 2 * C_F where C_F = (N^2-1)/(2N) = 4/3 is the
  textbook SU(N) one-loop Casimir for a fundamental scalar and the
  factor of 2 is the chiral-cube Wilson kernel's geometric pairing
  of forward and backward links per direction. The standard SU(N)
  Fierz identity in CL3_COLOR_AUTOMORPHISM Section D is the only
  Fierz machinery used; it gives the sandwich identity
  sum_a T^a M T^a = (1/2) Tr(M) I - (1/(2N)) M, which yields C_F I
  (singlet) for M = I and -(1/(2N)) T^b (adjoint) for M = T^b.
upstream_dependencies:
  - dm_eta_g1_coleman_weinberg_bounded_theorem_note_2026_05_06
  - dm_eta_g1_operator_bridge_proof_theorem_note_2026_05_06
  - dm_eta_g1_dynamical_residual_operator_trace_support_theorem_note_2026_05_06
  - dm_eta_g1_cl3_adj3_embedding_algebraic_support_theorem_note_2026_05_06
  - cl3_color_automorphism_theorem
  - su3_adjoint_casimir_theorem_note_2026_05_02
admitted_context_inputs:
  - SU(N) Fierz identity (already in CL3_COLOR_AUTOMORPHISM Section D)
  - Standard Lie-algebra Casimir values (already in SU3_ADJOINT_CASIMIR)
no_new_axioms: true
no_new_combinatorial_inputs: true
no_new_dynamical_mechanisms: true
correction_type: narrative_clarification
m_DM_value_unchanged: true
runner_pass_counts_unchanged: true
```

---

## Reading rule

This note is a bounded source correction. It does not introduce new
science. The companion runner arithmetic is unchanged, but runner
headings and summaries are updated so PASS output no longer carries the
rejected adjoint-channel interpretation. In the three landed G1 chain
notes of 2026-05-06, the mechanism described as "adjoint Fierz channel
projection of the dark mass operator" is actually "Casimir +
forward+backward Wilson-hop geometric doubling", with the operator
`sum_a T^a T^a = C_F I` correctly identified as singlet-channel. The
arithmetic identity `8/3 = 2 C_F`, the runner test counts, and the
composition `m_DM = 16 v` are unchanged. Any downstream parent-status
change requires independent audit of the corrected chain.
