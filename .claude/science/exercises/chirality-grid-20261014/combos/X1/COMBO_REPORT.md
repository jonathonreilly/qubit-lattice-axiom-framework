# X1 "Disentangled inflow": combination report

- **Agent:** Claude Opus 5.5, combination agent, round 2. Same model family as the supervisor and all round-1 route agents, so not independent. Unrefereed.
- **Window:** 2026-10-14, 14:07Z to about 14:45Z.
- **Hygiene:** no repository was edited. Two scripts ran, one at a time, with OMP_NUM_THREADS=2. Peak resident memory was 129 MB, and nothing of mine is still running. Web search and abstract pages were used only for citations; nothing was downloaded.

**Paths used below:**
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full.
- `R` = `/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/chirality-grid-20261014`.
- `P` = `R/.claude/science/exercises/chirality-grid-20261014/`, with `F1` = `P/routes/F1/ROUTE_REPORT.md`, `F3` = `P/routes/F3/ROUTE_REPORT.md`, `F4` = `P/routes/F4/ROUTE_REPORT.md` and `OV` = `P/OUTSIDE_VIEW.md`.
- `X1` = this folder.

**Read in full:** WALL, ASSUMPTIONS, ROUTES, APPROACH_REGISTRY, OUTSIDE_VIEW, F1, F3 and F4. Also read: the governance sections "Independent Search Rounds", "Theorem-Strength Gap Test" and "Candidate-Proof Audit" (`origin/main:docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md:58-114`), and `C5_TW3_report.md:1-80`.

**Labels:** proved / checked / suggested / reading / comparator.

---

## 0. Plain words

1. **The idea.** Put our world on one face of a thicker slab of qubits. The slab's interior is the kind of material whose surface carries one-handed particles. If the interior can be "unknotted" into a plain product state by a sequence of local steps that respect the forces' symmetry (a "symmetric disentangler"), then stopping the unknotting partway gives a far face with no particles on it at all, while the near face keeps our one-handed particles. The force fields can then be ordinary grid links shared by all the layers at a site. That would remove F4's force-side failure.

2. **What it buys, honestly.**
   - **The force side does get fixed, but only by what the far face is made of** (proved skeleton). In the slab the symmetry already acts site by site. F4's failure was never that the symmetry was "not on-site". It was the opposite-handed copy on the far face.
   - **There is no way round a far-face interaction gap** (proved, given F4-L3). The disentangler does not avoid "symmetric mass generation" (SMG, interactions that gap the mirror without breaking the symmetry). It writes that interaction down exactly, as the disentangler sandwiching a trivial term.
   - **Whether such a disentangler exists is exactly as hard as the original wall** (target-equivalent, Lemma E). The physics core is already in the literature: Wang–Wen (PRR 2, 023356 (2020), arXiv:1809.11171) *assume* the needed statement.

3. **What is new, and is it a new mechanism?** Not a new mechanism. It is a sharper map of the obligation:
   - In the slab, every lattice-level obstruction attached to *how the symmetry acts* is automatically zero (proved): Fidkowski–Xu, the Shirley–Zhang–Ji–Levin index, F3-B's κ, and the Tu–Long–Else lattice anomaly. So the qubit-sized-site worry is not an obstruction here.
   - The whole question is one statement about *a state*: the 16-flavour slab interior is trivial in the lattice classification of invertible states with the SM symmetry (S\* below).
   - That statement and Golterman–Shamir's (GS's) conjecture cannot both be true (suggested).
   - No dimensional shortcut exists for the SM gauge group (proved by charge arithmetic). The Smith / decorated-domain-wall shortcut works only when the protection is a bare Z₄.

4. **The test I could run** is in the one dimension where everything is computable: the time-reversal (T) Majorana chain, with 8 chains, i.e. 16 Majoranas per site. It PASSES (checked):
   - the disentangler exists exactly when the far end can be gapped (period 8);
   - it is necessarily interacting;
   - the far end it builds is a symmetric mass generation term with no two-fermion mass, and its propagator vanishes at zero frequency.

   This is an instrument check. It says nothing about 3+1D.

---

## 1. Cores used

| Core | Source | Used as |
|---|---|---|
| (i) F1-R3 | `F1:118-126` (P ⇒ quasi-local U ⇒ exactly gapped mirror), `F1:136-139` (graded "P stronger than T") | the disentangler and its cut |
| (ii) F4 slab, L2, L3, F4-C | `F4:65-90` (L2 forced zero), `F4:92-115` (L3: for every inflow geometry *without symmetric gapping*), `F4:136` (folded slab), `F4:142` (T ⇒ L_A) | geometry, gauge dichotomy, zero |
| (iii) TPF / Gioia–Thorngren / Fidkowski–Xu | `OV:98` (TPF), `OV:56` (FX), `OV:35-39` (qubit obstacles), `OV:99-100` (Seifnashri–Shirley, SZJL) | what the disentangler must and must not do |
| (iv) F3-B κ | `F3:153-176` | the index constraint on preserved U(1)s |

---

## 2. The combined construction (DI) and its lemmas

### Data

- **Slab.** Z³ × {1..L}. The layer index and the 4+1D spinor index are **on-site payload** of each Z³ site (as in F1-R2 `F1:117`, F4-A `F4:134`).
- **Matter.** One generation, 16 left-handed Weyl in the free 4+1D Wilson–Dirac bulk with C₂ = 1 per component.
- **Symmetry.** On-site G, where G = G_SM, or G_SM × Z₄^X, or Spin(10).
- **Bulk state.** ψ₀ is the bulk ground state on Z⁴ with no walls. The near wall carries the 16_L and the far wall the 16_R mirror.

### Terminal statement S\* (the exact mathematical statement needed)

> **S\*(G):** there is a G-symmetric product ancilla state α and a locality-preserving unitary V, generated by a quasi-local, time-dependent, G-invariant fermionic Hamiltonian (so V is in the symmetric connected component, not merely a symmetric QCA), such that V(ψ₀ ⊗ α) is a product state. Sites are finite-dimensional.

S\* is **not** "cobordism-trivial ⇒ the symmetry can be made on-site", which is the TPF / Seifnashri–Shirley / SZJL form. In the slab the symmetry is on-site already. S\* is a statement about an invertible **state**. Concretely it is:

[cobordism invariant of ψ₀ = 0] ∧ [lattice completeness: invertible lattice states with zero cobordism invariant are symmetric-LPU-trivial].

- The first conjunct is known: perturbative cancellation, Witten SU(2) and Z₁₆ all vanish for the 16 (comparator: García-Etxebarria–Montero arXiv:1808.00009; arithmetic re-checked in §5).
- The second is the open conjecture (Kitaev; Kapustin arXiv:1403.1467; Freed–Hopkins arXiv:1604.06527 for the continuum; recalled, not re-verified).

### Lemma E (equivalence ladder; target-equivalence)

| Step | Statement | Label |
|---|---|---|
| **E1: S\* ⇒ H_DI** | Let V_{>w} be V's generator restricted to layers > w. Then H′ = V_{>w} H₀^{semi} V_{>w}† is unitarily equivalent to the semi-infinite slab with only the near wall: same spectrum, near 16_L gapless, everything else gapped. It is G-symmetric (restricted G-invariant generator) and its ground state is a product for layers > w + ξ_V. Freeze that region (error e^{−w/ξ}) to get H_DI on L′ = w + O(ξ_V) layers. H_DI has a gapped symmetric far boundary and the near 16_L. | proved skeleton |
| | Open: (a) the tails (standard quasi-adiabatic estimates); (b) near-wall stability under G-symmetric e^{−w/ξ} perturbations. For Spin(10) or Z₄^X there is no 16_L bilinear. For G_SM alone the only one is ν^cν^c (checked §5), which gives a harmless Majorana mass, a seesaw-type ν_R. | |
| | **Scope:** if V were only a symmetric QCA (not circuit-generated), the cut leaves a 3D interface QCA. FX's chirality pump is such an object, so the circuit-generated clause in S\* is load-bearing. | reading; comparator GNVW/FX |
| **E2: H_DI ⇒ P_bdry** | ψ₀ has a G-symmetric gapped boundary with a unique ground state, i.e. far-wall SMG. | proved (by definition) |
| **E3: P_bdry ⇒ S\*** | The lattice bulk–boundary correspondence for invertible states ("BBC-inv"). | open in general. In 1+1D it holds via fMPS/FK; checked here for BDI, T2. |
| **E4: T ⇒ P_bdry** | Stack the T-model's 16_L on the far wall and pair it with the mirror by a G-invariant bilinear (`F4:142`). | suggested |
| **E5: S\* ⇒ T (gauge side)** | The links live on Z³ and are shared by all layers of a site. Every G-invariant term of V's generator minimally couples with Wilson lines on finitely many links. The far wall is gapped, so L3(a)'s "opposite chirality at the fibre's far end" (`F4:96-99`) is absent. Bulk polarisation only renormalises the local 1/g², because there is no gauge field along the layers, so L3(c)'s nonlocal terms are absent. | proved skeleton |
| | Open: gauge dynamics, and whether the forced zero (F4-L2) is harmless once gauged (GS arXiv:2311.12790 vs Zeng–Xu–Lu–You 2405.05339; `OV:59`). | |

**Conclusion.** S\* ⇔ T modulo BBC-inv (E3) and the gauge-dynamics steps (E5). This **corrects F1's grading "T ⇏ P, P stronger than T" (`F1:136`)**: under BBC-inv, T ⇒ P_bdry ⇒ S\*. If BBC-inv fails on the lattice, F1's grading stands.

### Corollary E6: no cure without far-wall SMG (proved, given L3 and E1)

F4-L3 covers every inflow geometry *without* symmetric far gapping (`F4:92`). So any local cure with on-site links needs the far content gapped G-symmetrically with no bilinear, which is SMG by definition.

The DI far wall is exactly that: H_far = V-conjugated sums of on-site trivial terms. The question's "without far-wall SMG dynamics" can only mean "SMG made kinematic, exactly solvable, by V", and V's existence is S\*, which is target-equivalent.

### Lemma O: on-siteness makes every symmetry-action obstruction vacuous (proved, by definition, plus checked arithmetic)

In the slab and in H_DI, G acts on-site: a tensor product over Z³ sites of unitaries on the payload. Hence:
- (i) Tu–Long–Else lattice anomaly = 0 (PRX 16, 011027 (2026), arXiv:2507.21209; abstract only);
- (ii) the SZJL index ω ∈ H²(G, ℚ₊) is trivial (arXiv:2507.21267; abstract only);
- (iii) every subgroup is depth 0, so FX's shallow-circuit condition is met;
- (iv) any U(1) that H_DI preserves must have Σχq = 0 on the near content (F3-B κ / anomaly matching). For U(1)_Y, U(1)_{B−L} and U(1)_X the sum is 0, but κ_F = 16 (checked, §5). So **V must break U(1)_F**, and that is the only constraint κ adds.

The finite-dimensional (qubit) worry in `OV:35-39` is a worry for **bulk-free** realisations (TPF's rotors). In the slab, finite dimension is automatic, at about 64L fermion modes per site per generation (F4's ~10³ qubits for three generations, `F4:153-156`).

### What Fidkowski–Xu forbids (comparator plus reading)

**Statement** (PRL 131, 196601 (2023), arXiv:2306.10105; abstract checked). With finite-dimensional sites:
- U(1)_A of a single Weyl cannot be a shallow circuit;
- a uniform chiral Z_{2N} on N_f same-helicity Weyl cannot be one when 2N ∤ N_f.

**Here** (bulk-free H_DI after the product region is discarded; G on-site):
- FX forbids keeping U(1)_F;
- it allows Z₄^X at N_f = 16 (4 | 16) and forbids it at 15 (4 ∤ 15). This is the same verdict as the Z₁₆ anomaly (C1, `F1:63-83`).
- FX is weaker than the Z₁₆ anomaly in general (reading). It allows Z₄ at N_f = 4, 8 and 12, where Z₁₆ forbids it.
- **FX forbids nothing that the anomaly does not already forbid** for the SM 16.

### Lemma G: V is necessarily non-Gaussian, and there is no dimensional shortcut for G_SM (proved, given the free classification and Read's theorem)

- **(a) Gaussian part.** The only G_SM-singlet ψψ is ν^cν^c, which is Z₄^X-odd (checked §5). So every G_SM-symmetric Gaussian LPU conserves U(1)_F on the 15 charged components, and with Z₄^X on all 16. It therefore preserves the per-sector second Chern numbers of ψ₀, which are nonzero. **V must be non-Gaussian on every charged sector.**
- **(b) No 1D-style dimer factorisation.** V cannot be "depth-1 non-Gaussian gates on disjoint blocks" ∘ "G-symmetric Gaussian LPU". If it were, the Gaussian intermediate would be a product over finite blocks. Such a product has compactly supported Wannier functions and so carries no strong invariant in d ≥ 2 (Read, PRB 95, 115309 (2017), `OV:61`), contradicting C₂ ≠ 0. In 1D this factorisation *does* exist (T2 below), because 1D windings are compatible with compact Wannier functions. So the 1D mechanism provably does not lift.
- **(c) The Smith / decorated-domain-wall shortcut.**
  - **Bare Z₄ protection.** Ω₅^{Spin×_{Z₂}Z₄} ≅ Ω₄^{Pin+} = Z₁₆ would reduce 4+1D Spin-Z₄ triviality at ν = 16 to 3+1D DIII ν = 16 triviality. That needs a lattice DDW-identification lemma, which is open (suggested).
  - **G_SM protection.** The Z₄-broken ordered phase must still be trivialisable G_SM-symmetrically. At the Gaussian level only ν^c can be trivialised, so the 15 charged components stay free-nontrivial and the reduction returns S\*(G_SM, 15) itself (proved by (a)).

### Lemma Z: S\* needs bulk propagator zeros (proved skeleton; comparator Gurarie PRB 83, 085426, arXiv:1011.2273)

- The 4+1D Green's-function winding N₅[G] is invariant along gapped paths on which G(0, k) has no zeros. It is 16 for ψ₀ (summed; nonzero per Y-sector) and 0 for a product state.
- So any path realising S\* develops **bulk** zeros: the bulk analogue of F4-L2.
- **Reading/suggested.** If GS's "zeros are kinematical" conjecture also holds for gapped 4+1D bulks, where their condition (2) holds a fortiori, then N₅ with complete interpolators would be a path invariant, giving ¬S\*. With Lemma O this sharpens F1-R3's corollary (`F1:126`):
  - GS true ⇒ there is a beyond-cobordism invariant of invertible **states**;
  - it cannot be an invariant of the symmetry action, because those all vanish here;
  - the only candidate in view is N₅ made rigid by kinematical zeros.

### F4-C (folded slab) under X1 (reading)

- Under S\*, the folded slab is dominated: H_DI is local and single-faced, with no world-range gluing.
- Without S\*, F4-C stays the only no-interaction single-face option, at its recorded price (`F4:136`, `:172-177`).
- Combining the disentangler with the fold adds nothing.

---

## 3. Which round-1 obligation changes, and how

| Round-1 item | Before | After X1 |
|---|---|---|
| F4-A, L_A (`F4:134`, `:140-145`) | Far-wall SMG *dynamics* at intermediate coupling (target-equivalent) | Replaced by the kinematic S\* (state classification). Still target-equivalent (Lemma E). |
| F4-B/L3 (`F4:92-115`) | Gauge-side no-go without symmetric gapping | Discharged *conditionally on S\** (E5). L3's premise fails under S\*. Unconditionally, E6: no cure without far-wall SMG. |
| F1-R3 (`F1:118-139`) | P graded "stronger than T" | P ≡ S\*, regraded **target-equivalent modulo BBC-inv**. Circuit-generation clause added (E1 scope). |
| TPF / FX / SZJL / qubit concerns (`OV:35-39`, `:212-223`) | Open obstacles for qubit sites | **Removed for slab constructions** (Lemma O). They bind only bulk-free realisations. |
| F3-B κ (`F3:153-176`) | Index adds nothing for SM gauge charges | Confirmed. Its only use here is "V must break U(1)_F". |

---

## 4. Theorem-strength gap test

- **L = S\*.** S\* ⇒ T via E1 + E5 (modulo gauge dynamics and zero harmlessness). T ⇒ S\* via E4 + E3 (modulo BBC-inv). **L is target-equivalent, so blocked-equivalent.**
- **Genuinely new mechanism? No.**
  - S\* is assumed verbatim by Wang–Wen 2020, whose method is the existence of a symmetric gapped boundary for a trivial symmetric invertible order.
  - X1's additions are a decomposition and bookkeeping: Lemma O removes two leaves, Lemma G closes the Gaussian, dimer and Smith shortcuts for G_SM, and Lemma Z states the bulk-zero hinge. None of these advances the proof of the remaining leaf, lattice completeness in 4+1D.
- **Reopen condition** (any of these):
  - an explicit circuit-generated symmetric V for ψ₀^{16};
  - a proof of lattice completeness (or of BBC-inv plus completeness) for a fermionic class with continuous symmetry in ≥ 3+1D bulk;
  - a beyond-cobordism invertible-state invariant that detects ψ₀^{16}. This would refute S\* and support GS.

---

## 5. Checks run

### DI-Z8 (pre-registered in `X1/PREREG.md` before the script was written)

**Files:** `X1/scripts/di_z8.py` and `di_z8.out`. 29 s, 129 MB peak RSS.

**T1: Z₈ gate (checked).** n T-odd Majoranas alone:

| n | T vs fermion parity | T² | Random-H ground states |
|---|---|---|---|
| 2, 6, 10, 14 | swaps parity | — | every draw ≥ 2-fold |
| 4, 12 | preserves | −1 | every draw ≥ 2-fold |
| 8, 16 | preserves | +1 | 20/20 unique |

- T-symmetrising iγ′₁γ′₂ gives norm 0, so the bilinear is T-forbidden (checked, not assumed).
- **PASS.** P_bdry ⇔ n ≡ 0 mod 8, reproducing Fidkowski–Kitaev (comparator: PRB 81, 134509; PRB 83, 075103).

**T2: explicit disentangler, ν = 8 (checked).** On one Kitaev bond (256-dim), a real Givens rotation sends the Gaussian bond state |B⟩ to |E′(γ′)⟩⊗|E(γ)⟩. Over 5 random T-symmetric end-interaction draws:
- unitarity ≤ 2.7e-15;
- [U, T] ≤ 4.6e-15;
- [U, parity] ≤ 3.8e-15;
- fidelity 1.000000000000;
- one-site covariance max|⟨iγ′_aγ′_b⟩| ≤ 1.1e-15, so |E′⟩ is maximally non-Gaussian and no Gaussian (free) T-symmetric circuit can produce it.

V = ⊗_bonds U_b is depth 1. **PASS** (E3 direction realised explicitly in 1D).

**T3: the cut is an exactly solvable SMG with a forced zero (checked).** Reducing U_b h_B U_b† to the far γ′ factor gives H_far with:
- Hermitian, T-symmetric and parity-even to ≤ 1e-14;
- a unique ground state equal to |E′⟩ (overlap 1.000000000000), gap 8.0000 in every draw;
- bilinear component ≤ 1.7e-15;
- far elementary propagator max|G(iω)| = 3.12e-2·ω at ω = 1e-2, 1e-4 and 1e-6 (a linear zero).

Controls:
- T-breaking (+0.3 iγ′₁γ′₂): |G(i·1e-6)| = 2.1–2.6e-2;
- near free end pole: |G(i·1e-4)| = 2.0e4 = 2/ω.

**PASS.**

**Pre-registered reading: CHAIN-CONSISTENT.** E1–E3 and E6, and the zero, hold in the only dimension where everything is computable.

**Limits, stated before the run:**
- 1+1D bulk is theorem-level, so the PASS carries no weight on 4+1D.
- Row n = 8 of T1 also shows that the toy's *near* end is itself symmetrically gappable. So the toy cannot model the 3+1D near-wall protection, which rests only on four-fermion irrelevance (`F4:123-128`).

### SM-16 arithmetic (`X1/scripts/sm16_arith.py`, `.out`; exact rationals; not pre-registered, no reading involved)

- **κ and anomalies.** Σq = Σq³ = 0 for Y, B−L and X; κ_F = 16.
- **X = 5(B−L) − 4Y** holds on every field. All X ≡ 1 mod 4, giving Z₁₆ index 16 ≡ 0.
- **Pairings.** The only G_SM-singlet ψψ is ν^cν^c, and it is Z₄^X-forbidden.
- **FX.** 4 | 16 but 4 ∤ 15.

---

## 6. Smallest dimension where the claim is nontrivial and testable

| Bulk / boundary | Nontrivial? (free ≠ interacting) | Status of S\*-type statement | Testable here? |
|---|---|---|---|
| 1+1D / 0+1D: BDI, 8 chains = 16 Majoranas per site | yes | theorem (fMPS; FK); explicit V checked (T2) | **yes, run (PASS)**; instrument only |
| 2+1D / 1+1D: Z₂×Z₂^f ν = 8 (16 Majorana movers); 3450 with U(1) | yes | boundary-symmetry form proved for finite G on spin chains (Seifnashri–Shirley, PRL 136, 216603 (2026), abstract: bosonic chains, ancillas needed). Fermionic or U(1) completeness not found. TPF rotors (infinite-dimensional) | no: strips need 2^48 or more |
| 3+1D / 2+1D: DIII (Pin+) ν = 16 = 16 Majorana cones | yes; **first dimension where GS's condition (2) holds** (`F4:123-128`) | open; the surface SMG is QMC-supported in related models (`OV:94`) | no: DQMC, weeks (= F4 test A, `F4:185-195`) |
| 4+1D / 3+1D: target, 16 Weyl, G_SM(×Z₄^X) or Spin(10) | yes | open; assumed by Wang–Wen | no |

**The cheapest test decisive for S\*'s lower-dimensional sibling** is F4 test A as already pre-registered (`F4:185-195`). Reading via X1:
- PASS-SMG there would establish P_bdry, and hence (under BBC-inv) S\*, for 3+1D DIII ν = 16. For bare-Z₄ content this feeds the 4+1D question through the Smith/DDW lemma (suggested).
- For G_SM it is an analogy only (Lemma G(c)).

Not run (weeks).

---

## 7. Price in framework terms

| Axiom / input | Status |
|---|---|
| **Lattice** (AX:37-41) | Z³ is kept. The fourth direction is on-site payload, a reading of what a site is (as F4 states at `F4:46`). No world-range gluing. |
| **Qubit** (AX:47) | Exceeded. A site is about 64L fermion modes per generation, held as Jordan–Wigner qubits (L ≈ 4–6). This is a coarse-graining price; it is not DEFERRED #4 (F6 per `P/ROUTES.md:20`). |
| **Admissibility** (AX:57-61; supplies no dynamics, AX:114-123) | The Hamiltonian is supplied: free Wilson–Dirac plus the V-dressed far term. V is quasi-local, which brings the range question (A3/A4, `P/ASSUMPTIONS.md:9-10`) unless a finite-depth V exists. |
| **Record** (AX:77-83) | Not used. |
| **Supplied, not derived** | Fermion statistics (A7); internal G and the 16 assignment; links (A8); the sign bit for the light wall; the Wilson tuning; and **S\* itself (open)**. |
| **ν_R** | Not forced in the slab unless Z₄^X is imposed. With G_SM only, 15 components suffice, but V must then be G_SM-symmetric on 15 charged sectors. This differs from F1-C1's staggered carrier, where translations force it (`F1:83`). |
| **Not paid** | F4-B's Planck-strength penalty, F4-C's world-range gluing, and the TPF rotors and FX obstructions (Lemma O). |

---

## 8. Strongest objection (kill attempt on myself)

1. **This is Wang–Wen plus F1-R3, renamed.** Largely true. The physics core, "a cobordism-trivial bulk gives a symmetric gapped boundary, hence a lattice Spin(10) chiral theory", is Wang–Wen's proposal (arXiv:1809.11171; `OV:89`, `:173`). X1's content is bookkeeping: Lemmas E, O, G and Z.
   - **Verdict: wounded.** It survives only as an obligation-map sharpening, not as a mechanism.
2. **Target-equivalence rests on BBC-inv.** If the lattice bulk–boundary correspondence for invertible states fails, S\* could be strictly stronger than T, as F1 had it. Either way it is blocked.
3. **E1 needs V circuit-generated.** A merely symmetric QCA V would leave an interface QCA at the cut, possibly an FX-type chirality pump. So S\* must be stated in the connected component. This is stated in S\*, and automorphic equivalence supplies it if a symmetric gapped path exists.
4. **The 1D test is uninformative about 3+1D.** True, and pre-registered as such. Worse, the toy's near end is itself gappable (T1, n = 8), so the toy cannot even represent the near-wall protection.
5. **GS would reject E1's truncation step.** They might argue the e^{−w/ξ} tails restore a light composite at the far wall. Lemma Z/L2 says the success case *must* carry zeros, and GS dispute exactly whether those can be non-kinematical. X1 does not decide this; it only relocates the dispute to the bulk (Lemma Z).
6. **Does it assume the target?** No. It reduces the target to S\* and shows the converse modulo BBC-inv.
7. **Does it contradict a landed result?** No. It refines `F1:136`'s grading and `F4:92`'s scope, as stated in §3.

---

## 9. Proposed registry row

| Field | Entry |
|---|---|
| Family | X1 = F1-R3 × F4-A/L3 × TPF/FX × F3-B |
| Object | Inflow slab with on-site G, plus a circuit-generated symmetric disentangler V of the bulk |
| Mechanism | Cutting V gives an exactly solvable far-wall SMG; links shared across layers |
| Terminal | S\* (lattice completeness for ψ₀^{16}, G_SM(×Z₄^X) or Spin(10), 4+1D) |
| Strength | Target-equivalent modulo BBC-inv |
| Status | **blocked-equivalent** |
| Evidence | DI-Z8 T1–T3 PASS (1D instrument), SM-16 arithmetic |
| Reopen | An explicit V for ψ₀^{16}; or a completeness theorem for a fermionic class with continuous G in ≥ 3+1D bulk; or a beyond-cobordism invariant of invertible states detecting ψ₀^{16} (which would kill S\*) |

---

## 10. Files

All in `X1/`:
- `PREREG.md`, written before any script;
- `scripts/di_z8.py` and `scripts/di_z8.out`, the DI-Z8 run (CHAIN-CONSISTENT);
- `scripts/di_z8.err`, the time and memory record;
- `scripts/sm16_arith.py` and `scripts/sm16_arith.out`;
- this file.

**Sources checked this session (abstract pages only):**
- [FX arXiv:2306.10105](https://arxiv.org/abs/2306.10105)
- [TPF arXiv:2601.04304](https://arxiv.org/abs/2601.04304)
- [SZJL arXiv:2507.21267](https://arxiv.org/abs/2507.21267)
- [Seifnashri–Shirley arXiv:2503.09717](https://arxiv.org/abs/2503.09717)
- [Tu–Long–Else arXiv:2507.21209](https://arxiv.org/abs/2507.21209)
- [Ellison–Fidkowski arXiv:1806.09623](https://arxiv.org/abs/1806.09623): symmetric circuits for 2+1D supercohomology fermionic SPTs; not a completeness result
- [Wang–Wen arXiv:1809.11171](https://arxiv.org/abs/1809.11171)
- [Gurarie arXiv:1011.2273](https://arxiv.org/abs/1011.2273)
- [FK arXiv:0904.2197](https://arxiv.org/abs/0904.2197) and [arXiv:1008.4138](https://arxiv.org/abs/1008.4138), via search snippets

**Recalled, not re-verified:** Kapustin arXiv:1403.1467; Freed–Hopkins arXiv:1604.06527; Read PRB 95, 115309 (via `OV:61`); García-Etxebarria–Montero arXiv:1808.00009.
