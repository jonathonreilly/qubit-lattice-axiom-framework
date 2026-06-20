# Block 02 — B-AXIS.2 / N4 CORE obstruction (axis-label selection)

**Section id:** block02_section_N4_core
**B-AXIS clause:** B-AXIS.2 = N4 (axis-label / evolution-axis selection): which of
the four Euclidean directions carries the RP/transfer construction — can it be
*derived* rather than *declared*?
**Type:** branch-local obstruction section (no-go-grade, negative_route_pruning).
**Claim type:** no_go (axis-label not A_min-derivable; the only axis-selecting
datum is a per-axis Z₂ BC-asymmetry that is itself S₄-transportable and outside
A_min).
**proposal_allowed:** false  •  **bare_retained_allowed:** false  •
**audit_required_before_effective_retained:** true
**Status authority:** independent audit lane only. This branch-local source
artifact sets no audit/publication/effective status and derives nothing into
A_min (no new axiom, no new primitive). A_min = Lattice + Quantum + Record only.

---

## 0. One-line core claim

On the even cubic-symmetric staggered-Dirac surface the four Euclidean axes lie in
a **single transitive S₄ orbit** of an exact lattice-automorphism group
`|G_bare| = 384`; **every** A_min-available enrichment's joint stabilizer with the
staggered hop is either full S₄ (isotropic) or trivial (a symmetric, non-axis-
selecting break of W), so **no** A_min structure singles out an axis; the only
one-axis-selecting datum is a per-axis Z₂ boundary-condition asymmetry, which is
itself S₄-transportable and is withheld by the Lattice axiom (an explicit open
gate). Therefore B-AXIS.2 (N4) is a **declared premise, not derived**.

---

## 1. The signed exchange unitary W, upgraded to S₄-transitivity

The staggered-Dirac surface carries the signed time↔space exchange unitary

```
W = W_{τ,1} = P_{τ↔1} · diag( (-1)^{x_τ x_1} )
```

— the bare permutation `P_{τ↔1}` dressed by the diagonal Z₂ sign field
`(-1)^{x_τ x_1}` needed to absorb the staggered η-phase. The plain unsigned swap
is **not** a symmetry (it fails by residual `> 1`); only the *signed* W conjugates
the staggered hop `M_KS` to itself, `W M_KS Wᵀ = M_KS` (residual `0`).

**Upgrade to the full group (recomputed in-tree).** W is not an isolated
coincidence: it is one element of the entire bare-surface automorphism group. The
in-tree block01 runner
`scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` enumerates the
signed hyperoctahedral group B₄ (24 axis-permutations × 16 per-axis reflections =
384 candidate site relabelings), solves per element for the diagonal Z₂ sign field
by BFS over the hop graph, and admits `g` iff `‖U_g M U_gᵀ − M‖ < 1e-9`. Result
(re-run here, deterministic, no RNG):

- **`|G_bare| = 384`** (the full hyperoctahedral group is realized),
- axis-permutation image = **all of S₄ (24 elements), acting transitively** (the
  orbit of axis 0 is `{0,1,2,3}`).

This is strictly stronger than the single-W certificate: the *entire* automorphism
group — not one exchange — projects onto a transitive S₄ over the four axes.
Transitive ⇒ any axis-selector built from W-invariant structure is transportable
onto any other axis ⇒ the time axis cannot be derived from the surface, only
declared.

**Authority for the S₄ upgrade:** the s4-transportable retained no-go
`docs/SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17.md`
(retained_no_go; resides on `origin/science/single-clock-axis-datum-s4-transportable-2026-06-17`,
runner `scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py`):
adjacent transpositions `(0,1),(1,2),(2,3)` generate S₄ acting transitively on the
four axes; the per-axis Z₂ BC datum is itself S₄-transportable (block [T]). The
S₄ fact is **recomputed in-tree** above (not taken as a citation edge).

---

## 2. The CORRECTED block01 R-N4-AUT result (the steelman, falsified)

The standing wall ("S₄ is transitive") is only fatal if the surface is *too poor*.
The block01 steelman R-N4-AUT genuinely attempted the strongest pro-derivation
move: search for **any** A_min-available surface enrichment whose automorphism
stabilizer drops below S₄ and **fixes exactly one axis** (a non-transportable
axis-selector), *without presupposing the Hamiltonian H*. Eight enrichments
E1–E8 were enumerated and each joint stabilizer (with the staggered hop, inside
`G_bare`) computed.

**Corrected selector criterion.** An enrichment SELECTS an axis iff its stabilizer
**fixes exactly one axis as a common fixed point AND acts transitively on the
other three** (the S₃-fixing-one signature). The subtle false positive that the
correction rejects: a *trivial* (identity-only) stabilizer fixes **all four** axes
and therefore selects **none**; the full S₄ likewise fixes none. Only the middle
class — S₃-fixing-one — is a genuine selector.

**Precise corrected structural result (recomputed in-tree, 17/17 PASS):**

| id | enrichment | A_min source | joint-stab class | selects axis? | A_min? |
|----|-----------|--------------|------------------|---------------|--------|
| E1 | reality/CPT parity grading ε=(−1)^{Σx} | Quantum (internal C² reality) | S₄-isotropic (\|img\|=24) | None | yes |
| E2 | cubic adjacency Laplacian | Lattice (nn cubic graph) | **trivial-joint (symmetric W-break, \|img\|=1)** | None | yes |
| E3 | staggered η hop-sector family {D₀…D₃} | the staggered structure itself | S₄-isotropic (\|img\|=24) | None | yes |
| E4 | STW crossing-link RP invariant P_a | crossing-link surface | S₄-isotropic (P_a=+1 all axes) | None | yes |
| E5 | η-curvature 2-cocycle on plaquettes | staggered phase curvature | S₄-isotropic (cocycle=−1 all planes) | None | yes |
| E6 | Record additive scalar readout | Record (additivity, I(∅)=0) | S₄-isotropic (scalar identity) | None | yes |
| **E7** | **per-axis Z₂ BC datum (A,P,P,P)** | **boundary datum (NOT A_min)** | **one-axis-selecting S₃ (\|img\|=6, fixes axis 0)** | **axis 0** | **NO** |
| E8 | face-diagonal-enriched cubic graph | richer isotropic Lattice graph | **trivial-joint (symmetric W-break, \|img\|=1)** | None | yes |

**The corrected headline:** *every A_min enrichment's joint stabilizer with the
staggered hop is either all of S₄ (isotropic) or trivial (a symmetric, non-axis-
selecting break of W); **NO A_min enrichment has a one-axis-selecting (S₃)
stabilizer.*** The only one-axis-selecting enrichment is the per-axis Z₂ BC datum
(E7), which is S₄-transportable and outside A_min.

This is **stronger** than the naive "every A_min enrichment is S₄-isotropic":
some A_min enrichments **do break W** — E2 (cubic Laplacian) and E8 (face-diagonal
graph) have a **trivial** joint stabilizer (identity-only). Concretely for E2: the
plain swap keeps the Laplacian but breaks the staggered hop (resid ≈ 22.63); the
dressed W keeps the hop but breaks the Laplacian (resid ≈ 45.25); no non-identity
B₄ element keeps both. So W is genuinely broken — **but the break is axis-
SYMMETRIC** (a trivial joint stabilizer fixes all four axes / acts freely), so it
singles out no axis. The wall is therefore not "W happens to be a symmetry"; it is
"the full hyperoctahedral group acts transitively, and no A_min enrichment's joint
stabilizer fixes exactly one axis."

**Recomputed in-tree:** `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`
→ TOTAL **PASS=17 FAIL=0**; `|G_bare|=384`, axis image = full transitive S₄;
A_min classes `{E1:S₄-iso, E2:trivial-joint, E3:S₄-iso, E4:S₄-iso, E5:S₄-iso,
E6:S₄-iso, E8:trivial-joint}`, E7 one-axis-selecting=True; crackers found = `[]`.

---

## 3. The four transport witnesses (no W-invariant anchor selects the axis)

Beyond the automorphism enumeration, every previously proposed *axis-anchor* is
exactly transported across W-equivalent axes (or is circular). These are NOT
rebuilt here; they are CITED from the retained no-go
`docs/SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
(retained_no_go; **Type: no_go**) and from the in-flight branch runners:

1. **OS/GNS reconstruction.** W transports the OS reflection, covariance, the
   one-particle Euclidean kernel (`W M⁻¹ Wᵀ = M⁻¹`, residual ~`2.7e-15`), the
   half-space OS kernels, spectra, and positivity status to the `x_1` axis. The OS
   construction is built *after* the axis is chosen and anchors nothing.
   *Cited authority:* 2026-06-11 retained_no_go (route A1); in-flight branch runner
   `origin/physics-loop/single-clock-axis-nogo-self-contained-20260617`:
   `scripts/single_clock_axis_selection_check_2026_06_11.py` block [RT-RP] (PASS;
   transport residual 0).

2. **Record durability.** Durability = operator-order monotonicity of the
   registered-record counter, which unitary transport preserves (max increment-
   spec diff `8.9e-16`); the Record axiom supplies no time metric, and a fixed
   finite record word admits many inequivalent strictly increasing clock maps.
   *Cited:* 2026-06-11 retained_no_go (route A2); branch runner block [RT-REC]
   (PASS); `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` (retained_no_go).

3. **Finite-speed registration cone (circularity).** Any cone whose evolution
   generator and clock window are already supplied is downstream of B-AXIS, so
   citing it to select the axis consumes B-AXIS to derive B-AXIS. The slice package
   transports exactly: `W_sl D^(1) W_slᵀ = D^(τ)` (slice dim 16, transport resid 0,
   identical spectra). *Cited:* 2026-06-11 retained_no_go (route A2 / CAP-K leg);
   branch runner block [RT-REC]; the block01 R-N4-REGDIR fresh attempt
   (`scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`,
   PASS=20 FAIL=0) confirms the A_min record-accumulation monotone is a W-invariant
   reflection-symmetric **ball, not a cone**, and a real LR cone needs a supplied
   generator whose W-conjugate yields an identical cone (Δ `7e-16`, circular).

4. **Anomaly / chirality (count-not-label firewall).** The staggered chirality
   grading `ε(x) = (-1)^{x_τ+x_1+x_2+x_3}` is exactly W-invariant (`W ε Wᵀ = ε`,
   residual 0) and the chiral anticommutation `{D_hop, ε} = 0` is W-preserved
   (residual 0); a count-only anomaly rule can constrain the *number* of temporal
   directions but cannot choose a *label* among two W-equivalent axis
   presentations. *Cited:* 2026-06-11 retained_no_go (route B); branch runner
   block [RT-ANOM] (PASS).

**Reality / CPT grading ε is W-inert.** The same ε=(−1)^{Σx_μ} grading is the
N4-AUT enrichment E1: its stabilizer image is full S₄ (recomputed in-tree, §2), so
the reality/CPT grading carries no axis label. This reproduces the s4-transportable
and s3-axis-identity-convention branches' W-inertness fact inside the full-group
computation.

---

## 4. Pruned-supplier enumeration (every proposed axis-supplier closed)

| candidate axis-supplier | outcome | mechanism | authority |
|---|---|---|---|
| OS/GNS reconstruction privileges τ | PRUNED | W transports reflection/covariance/half-space kernel/spectra/positivity to x₁ (resid 0; M⁻¹ resid ~2.7e-15) | 2026-06-11 retained_no_go + branch [RT-RP] |
| Record durability as physical axis | PRUNED | durability = unitary-invariant operator-order monotonicity (Δ 8.9e-16); Record supplies no time metric | 2026-06-11 retained_no_go + branch [RT-REC] |
| Finite-speed registration cone / CAP-K | PRUNED (circular) | cone consuming a supplied generator+window is downstream of B-AXIS; slice transports D^(1)→D^(τ) resid 0; A_min monotone is a ball | 2026-06-11 retained_no_go + R-N4-REGDIR |
| Anomaly/chirality identifies the axis | PRUNED | ε W-invariant, {D_hop,ε}=0 preserved (resid 0); count-not-label firewall | 2026-06-11 retained_no_go (route B) |
| KMS/APBC thermal antiperiodicity | PRUNED | exchange-covariant: W maps APBC-τ → APBC-x₁ exactly; KMS is covariant with a *supplied* time circle | **retained_no_go** `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md` (on `origin/physics-loop/single-clock-apbc-axis-bridge-20260616` + n5-factor branch; runner `scripts/single_clock_kms_apbc_axis_supplier_no_go_2026_06_16.py`) |
| Wilson temporal-gauge / plaquette | PRUNED (labeled choice) | singles an axis only via the *labeled* choice U₀=1 (transportable); plaquette / Bessel coeffs are axis-blind | s4-transportable retained_no_go |
| Quantum tensor factor as a time slot | PRUNED (reduces to OS) | the equal-time tensor factorization carries no axis; reconstructing a slice reduces to the OS package, already W-transported | 2026-06-11 retained_no_go (OS) + Lieb-Robinson equal-time tensor locality note (M1 generator-free) |
| reality/CPT grading ε=(−1)^{Σx_μ} as selector | PRUNED (W-inert) | W ε Wᵀ = ε (resid 0); stabilizer image = full S₄ | N4-AUT E1 (in-tree) + s4/s3 branches |
| crossing-link RP invariant P_a + η-curvature 2-cocycle | PRUNED (isotropic) | P_a=+1 uniformly on all axes; cocycle=−1 in all planes incl temporal; S_d-isotropic | N4-AUT E4/E5 (in-tree) |
| cubic Laplacian / richer (face-diagonal) graph | PRUNED (symmetric W-break) | trivial joint stabilizer: W IS broken but axis-symmetrically (fixes all four axes), selects none | N4-AUT E2/E8 (in-tree) |
| record-production direction (Lieb-Robinson causal cone) | PRUNED (relocated) | production CPTP + POVM are W-/swap-covariant (resid 0); breaks W only with a supplied asymmetric pointer datum (break 3.44) → record-production-dynamics open gate | R-N4-REGDIR (in-tree, PASS=20) |
| **per-axis Z₂ BC-asymmetry datum** | **the sole selector** | breaks W exactly; S₃ stabilizer fixing one axis — **but S₄-transportable + outside A_min** | 2026-06-11 retained_no_go (sharpened pin) + s4 retained_no_go + N4-AUT E7 |

Every Euclidean-surface candidate is either W-transported (resid 0), axis-symmetric
(trivial joint stabilizer), circular (consumes B-AXIS), a labeled convention, or
relocated to an open gate. The only datum that genuinely selects one axis is the
per-axis Z₂ BC-asymmetry — which §5 shows is both transportable and unsupplied.

---

## 5. The N4 sharpened pin (the minimal axis-selecting input)

The exact negative boundary of N4: the **minimal** axis-selecting input is
**precisely one per-axis Z₂ boundary-condition asymmetry datum** (e.g. antiperiodic
on τ, periodic on the spatial axes: `bc=(A,P,P,P)`). Four computed legs pin it
exactly (from the 2026-06-11 retained_no_go sharpened pin and the apbc-axis-bridge
companion):

- **(A) all-PBC surface is W-invariant** (resid `<1e-13`); the two hop sectors have
  equal kernel dim (32 = 32). The kinetic/RP surface cannot select the axis.
- **(B) the relabeling-invariant kernel-dimension discriminator 0 vs 32.** With
  `bc=(A,P,P,P)`, W is broken exactly (resid `2.828`) and the temporal APBC hop
  sector has trivial kernel **0** vs the spatial PBC kernel **32** — a basis-free,
  relabeling-invariant discriminator proving no signed exchange map can identify
  the two sectors once the asymmetric datum is present.
- **(C) symmetric-BC restoration falsifier.** APBC on **both** τ and x₁ RESTORES W
  exactly (resid 0) and re-matches kernel dims (0 = 0). This proves the selector is
  **BC-ASYMMETRY, not APBC alone** — APBC per se carries no axis content.
- **(D) S₃ residual automorphism.** The boundary vector `(A,P,P,P)` has
  automorphism group exactly **S₃**, fixing the APBC axis and permuting only the
  three spatial axes. So even the positive bridge selects one axis *label* but no
  spatial orientation/frame.

**The datum is NOT derived.** Two independent facts keep it outside A_min:

1. **S₄-transportability:** a `G_bare` element maps `(A,P,P,P)` onto `(P,A,P,P)`
   exactly (`‖W₀₁ M_appp W₀₁ᵀ − M_pappp‖ = 0`; recomputed in-tree, N4-AUT E7), so
   the datum selects an axis only *relative to an already-privileged axis*.
2. **A_min withholds it:** the Lattice axiom explicitly supplies no boundary
   condition (and no dynamics/orientation); the boundary condition is an EXPLICIT
   OPEN GATE in `MINIMAL_AXIOMS_2026-06-05.md`.

So the residual is relocated, not dissolved: B-AXIS.2 (N4 axis-label) remains a
declared premise; the only supplier shape is a per-axis Z₂ BC-asymmetry datum (or
an equivalent registration-direction bridge) that lands on the boundary-condition /
record-production-dynamics OPEN GATE of the minimal axioms. The sole form in which
the single-clock theorem may cite axis selection is the conditional contract: *if*
a per-axis Z₂ BC-asymmetry datum is supplied, *then* the axis label is fixed.

---

## 6. EVEN-extent scope boundary (explicit)

All S₄-transitivity exact-zeros, the `|G_bare|=384` certificate, and the entire
E1–E8 enrichment table are computed on the **EVEN-extent** cubic-symmetric staggered
block (the periodic staggered η-phase closes consistently across the boundary wrap
iff each extent is even — the standard staggered-fermion requirement). The
**odd-L falsifier** is recorded: on `L=(3,3,3,3)` the signed exchange does **not**
preserve the hop, `‖W M Wᵀ − M‖ = 6.000` (recomputed in-tree, matches the
s4-branch odd-L falsifier exactly); on `L=(4,4,4,4)` the residual is 0. The
exhaustive-S₄-orbit conclusion and the enrichment table are therefore **scoped to
even extent**; odd extent is a separate surface (a declared regulator choice, not
an A_min datum) on which W is not even a symmetry and this section's certificate
does not apply.

---

## 7. Absorbed runners + cited authorities

**Recomputed in-tree (block01 runners, PASS):**
- `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` — PASS=17
  FAIL=0; `|G_bare|=384`, transitive S₄, corrected joint-stabilizer table,
  odd-L resid 6.
- `scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` —
  PASS=20 FAIL=0; record-accumulation is a W-invariant ball, cone transports with
  H (circular), production CPTP+POVM W-covariant.

**Cited (not rebuilt) — retained no-gos:**
- `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
  (retained_no_go) — four transport witnesses + sharpened pin.
- `SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17.md`
  (retained_no_go; on `origin/science/single-clock-axis-datum-s4-transportable-2026-06-17`)
  — S₄ transitivity + BC datum transportability.
- `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md` (retained_no_go;
  on `origin/physics-loop/single-clock-apbc-axis-bridge-20260616`) — KMS/APBC
  exchange-covariant.
- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (retained_no_go) — N4
  clause / Stone τ-relativity.
- `MINIMAL_AXIOMS_2026-06-05.md` — Lattice withholds boundary condition / dynamics
  / metric / orientation (explicit open gates).

**Cited (not rebuilt) — in-flight branch runners:**
- `origin/physics-loop/single-clock-axis-nogo-self-contained-20260617`:
  `scripts/single_clock_axis_selection_check_2026_06_11.py` blocks
  [RT-RP]/[RT-REC]/[RT-ANOM]/[PIN] (PASS) — OS/GNS, durability, cone, anomaly
  transport + the kernel-dim discriminator.
- `origin/physics-loop/single-clock-apbc-axis-bridge-20260616`:
  `scripts/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py` (PASS=21
  FAIL=0) — the conditional axis-label bridge (W-break, kernel discriminator,
  symmetric-BC falsifier, S₃ automorphism).

---

## 8. Status discipline

Branch-local source artifact for
`physics-loop/single-clock-baxis-wall-block02-20260620`. Sets no audit /
publication / effective-status surface; asserts no bare "retained"/"promoted"
status; derives nothing into A_min and adds no axiom/primitive. B-AXIS.2 (N4)
remains a **live declared premise**. The independent audit lane is the sole status
authority.
