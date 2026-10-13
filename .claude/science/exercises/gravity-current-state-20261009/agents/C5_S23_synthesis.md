# C5 S23: synthesis after rounds 16–17 (refereed: R16-10 … R16-14, R17-1 … R17-8; worker readings R17-9, R17-10, R17-11; R17-12, R17-13 running)

**Author and provenance.** Claude Opus 5.5 (S23). This is the same model family as every C5 worker, the supervisor, and S5–S20. **This synthesis is not refereed and gives no verdicts.**
- Every verdict quoted is from codex gpt-5.6-sol at xhigh, as recorded in `TESTS` or in the cited `agents/` verdict file.
  - R17-6, R17-7 and R17-8 were first read from the referee runs in `SP/`. Each run's `codex_run.log` header reads `model: gpt-5.6-sol` and `reasoning effort: xhigh`.
  - Those verdicts were recorded at 01:38Z (`TESTS:6283-6318`). The `agents/` copies are byte-identical to the `SP/` files (checked with `cmp`), so the line cites hold.
- Written 2026-10-13, 01:19Z to about 01:48Z. Updated at about 01:40Z–01:47Z for the records added at `TESTS:6267-6390`. No repository file was edited.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`).
- `agents/C5_S20_synthesis.md` (`S20`), the base. Its structure is followed here.
- `TESTS:5449-5684`: the R16-10 … R16-14 pre-registrations, worker readings and the R16-9 verdict record.
- `TESTS:5685-6390`: everything from "C5 Round 17" on, including the 01:38Z records, the R17-12/R17-13 pre-registrations and R17-10's worker reading.
- Referee verdicts:
  - `C5_R16-10` … `C5_R16-14` and `C5_R17-1` … `C5_R17-7` (`_referee_verdict.md`, in `agents/`);
  - R17-8's full verdict, `agents/C5_R17-8_referee.md` (`vR17-8`; identical to `SP/ref_R17-8/R17-8_referee_verdict.md`). Its 18-line summary, `agents/C5_R17-8_referee_verdict.md`, gives the same reading, OPEN.

**Read in part.**
- Price sections:
  - `rR16-10:255-262`, `rR16-11:296-305`, `rR16-12:292-299`, `rR16-13:269-281`, `rR16-14:221-233`;
  - `rR17-1:251-259`, `rR17-2:186-194`, `rR17-3:319-329`, `rR17-4:271-278`, `rR17-5:256-260`, `rR17-6:268-276`, `rR17-7:292-306`, `rR17-8:284-298`;
  - the worker reports with referees still running: `rR17-9:279-300` and `rR17-11:263-285`.
- Plain-words sections and heads: `rR17-4:1-60`, `rR17-6:1-70`, `rR17-7:1-80`, `rR17-8:1-75`. Line checks in `rR16-13` (`:53-64,176,200,225`), `rR16-3` (`:18,23,212-213,263`) and `vR16-3:13`.
- The P15–P73 rows of S5–S17's price tables, extracted mechanically for the v7 delta (§8.2).
- `SUMMARY` and `PRICE_NOTE` section headings, and `PRICE_NOTE:251,354-370`.

**Not read.** Worker scratch for R17-12 and R17-13, which are still running, and R17-10's report (its reading is taken from `TESTS:6384-6390`). `SP/R17-10/METHOD.md` was read only to confirm that its method was fixed before the run.

**Pending at about 01:47Z.**

| Item | State | Where |
|---|---|---|
| R17-9 (SM content on one cone; vector loops) | **worker reading OPEN; referee running** | `TESTS:6108-6128` (registration), `:6267-6281` (worker); `rR17-9` |
| R17-10 (certify K₆ / μ_E conflicts, U vertex) | **worker reading: K₆ OPEN on the superset, CERTIFIED-CONFLICT on the fast-only slice 𝓕; μ_E OPEN; referee running** | `TESTS:6206-6228` (registration), `:6384-6390` (worker); `agents/C5_R17-10_method.md` |
| R17-11 (the E₀ principle's pressure residual, bridge (d-i)) | **worker reading CONSISTENT in 𝒟; referee running** | `TESTS:6230-6250` (registration), `:6319-6335` (worker); `rR17-11` |
| R17-12 (VU or VM: does consistency force the vector placement?) | pre-registered 01:39Z; running | `TESTS:6337-6363` |
| R17-13 (the Wilson-Dirac μ_T2: zeroable or sign-definite?) | pre-registered 01:39Z; running | `TESTS:6365-6383` |

**Paths and abbreviations.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. Bare `TESTS`, `SUMMARY` and `PRICE_NOTE` are in `P/`.
- `rX` = `P/agents/C5_X_report.md`. `vX` = `P/agents/C5_X_referee_verdict.md`, except vR17-8 = `P/agents/C5_R17-8_referee.md` (the full verdict).
- `SP/` = the session scratchpad's `C5/`. `AX` = the axioms memo. `S20` = `C5_S20_synthesis.md`. `S17` and the earlier syntheses likewise.

**Labels.**
- **[ref]**: referee-confirmed, within the referee's scope.
- **[ref, bounded: class]**: a refereed FAIL, EXCLUDED, OBSTRUCTED or no-go, with its class.
- **[worker]**: a worker claim the referee did not confirm or has not ruled on.
- **[pending]**: R17-12, R17-13 (no reading yet). R17-9, R17-10 and R17-11 have worker readings, labelled [worker].
- **[S23 reading]**: an interpretation made here. Same model family; unrefereed.

**Sets** (as S8–S20). A = continuum base, discreteness only in records. B = Euclidean Z⁴. C = the axioms' Z³ with continuous time, tuned. C-box = Z³ × ℝ with a box-exact law. C-box-S = C-box with boson–fermion pairing per cell.

**Record-keeping notes.**
- `TESTS` now runs to 6390. vR17-6, vR17-7 and vR17-8 are recorded at `:6283-6318` (01:38Z). The R17-9, R17-10 and R17-11 worker readings are at `:6267-6281`, `:6384-6390` and `:6319-6335`.
- `SUMMARY` ends at §26 (`SUMMARY:677-714`, rounds 13–15). Rounds 16–17 are in `TESTS` only. §26 still labels R15-4 and R15-6 as worker results (`S20:47`), which is uncorrected.
- The R17-5 runner's import fix is recorded at `TESTS:6264` and `rR17-8:8`.

---

## 1. What changed since S20, in plain words

### 1.0 The short version

S20 left two things that nobody could price: a produced graviton, and a Λ that is neither tuned nor faster than light. It also left a candidate cone bill of 9 + CC (conditional). Since then:

1. **Λ now has a number-free option, but only as an added principle.**
   - "The law's lowest state weighs nothing" (C = E₀[H], P92) is consistent and number-free, and it tracks radiative corrections by definition. It is not "an independent exact number". It is also not forced by the four texts [ref, R17-3 OPEN; `vR17-3:7,17`].
   - If it is added, it survives under named conditions [ref, R17-7 OPEN; `vR17-7:69-70,74`]:
     - our vacuum must be the true lowest state. Standard-Model-only running would otherwise leave 1e112–3e120 ρ_Λ;
     - the grid zero-point's leftover pressure, 1.2–1.8e123 ρ_Λ per real scalar, must be absorbed by an exchange bridge (d-i), or paid by pairing or by tunings;
     - records must be inert labels, or pay the heating already priced as P4.
   - It does **not** imply that today's acceleration is temporary (`vR17-7:12`).
   - [worker, R17-11 CONSISTENT in 𝒟; referee running] Bridge (d-i) absorbs the grid enthalpy through a unique exchange current Q_ν = ∇^μ(W h_μν), with no instantaneous channel at linear order (`TESTS:6319-6335`).
     - It needs a receiver where the spatial trace equation is not imposed: √h fixed per site, plus site creation.
     - It also needs a hypersurface-orthogonal site congruence, and a non-Lagrangian partner (`rR17-11:267-270`).
2. **For the graviton, the qubit opens a window in the f-sum, and a dynamical obstruction appears behind it.**
   - Reading the metric slot as a Z₂ clock escapes the k⁴ f-sum bound: explicit qubit models have k⁰ and k² TT f-sums. Neither is a graviton [ref, R17-1 WINDOW].
   - There is no general representation obstruction. But Goldstone-type gravitons force at least 4 gapless branches. A soft TT f-sum with a finite, direction-independent response forces gapless vector/scalar weight unless the response has a **pinch point** [ref, bounded: two stated Z₂ classes, R17-6 OPEN overall].
   - Dressed integer-law phases stay capped at k⁴ [ref, R16-11 TRANSFERS].
3. **The cone bill lost the M vertex and gained a fermion row.**
   - R9-9's M vertex has no summable local realization on doubler-free laws (Lemma M). So every M-vertex number in R16-3, R16-9 and R16-13 belongs to a non-local vertex. R16-3's refutation stands, through the U vertex [ref, R17-4].
   - The off-axis rows cost one new condition (a sixth cumulant, K₆), not two. The vacuum tadpole is a separate condition that no shape can meet. Bill: 8 + CC per class / 12 + CC per species (U + E1) [ref, arithmetic conditional].
   - Fermion loops have the opposite sign to scalar loops. But the only joint zero found uses M, and Wilson-Dirac seas add a T₂g shear row (μ_T2 ≠ 0) [ref, R16-13 OPEN].
   - [worker, R17-9 OPEN; referee running] The Maxwell vector pushes the cone the same way Dirac fields do, not the way scalars do (`TESTS:6269`). Which SM content works then depends on where the photon's magnetic stress sits relative to h_xy:
     - at R9-9's placement (VU), there is no SM-count zero;
     - at a half-shifted placement (VM), there is an explicit SM-count zero with 3 tunings, leaving μ_T2 = +0.106 (`TESTS:6270-6278`).
   - R17-12 (does consistency force the placement?) and R17-13 (can μ_T2 be zeroed?) are running.
   - [worker] R17-11: in class 𝒟, the bill's tadpole row is paid by (d-i) with no number (`TESTS:6332`).
   - [worker, R17-10; referee running] The K₆ conflict is certified only on the sharp-turn slice 𝓕, which lies outside 𝒮. On 𝒮 it stays OPEN. Any shape solution of the K₆ row needs a finite fraction of slow-slope structure. μ_E: OPEN (`TESTS:6384-6390`).
4. **W15 (GW170817 as a gauge-invariant grid test) is nearly closed for free, finite-band, local matter.**
   - The multi-band class with multiplier-generated shifts is EXCLUDED [ref, bounded, R17-5].
   - These are each excluded in their analytic or isolated-band forms [ref, R17-8 OPEN with scoped no-gos]:
     - altered canonical generators (locked by Noether);
     - finite component mixing;
     - regular linear field-dependent generators.
   - What is left: merely continuous multi-shift mixing, crossing bands, joint mixing with field dependence, and anything outside the free/symmetric/projectable class.
5. **Set A's β needs a nonlinear source.**
   - A metric linear in matter records gives β = 0 or ½. Mercury excludes both, by 3.4–3.7 decades [ref, bounded, R16-14].
   - "Completion N" (the record is sourced by total stress, gravity's own included) restores β = 1 formally. It is a new nonlinear source/action bridge [ref].
6. **W7's bulk is GR's own dressing.**
   - At leading bulk order, the forced translation term is canonically equivalent to the inverse of a linearized-GR Coulomb/comoving dressing. No instantaneous physical bulk interaction is demonstrated [ref, R17-2 OPEN].
   - Degree 3 remains unclosed.
7. **W1.**
   - The λ → 0 limit is finite, with no divergent log [ref, R16-10 Theorem L].
   - Under the literal registered class, a lattice-superluminal photon (v_max 7.35) gives a Dirac zero. With subluminal photons the question is OPEN [ref].
   - n_t ≤ 2 is an upper bound, not a minimum [ref].

**[S23 reading], the one-sentence picture.** Every remaining unpriced item has turned into a question about the source/observable bridge that the axioms leave open (`AX:85-90,187`):
- what weighs ((S), Λ);
- what sources the metric (N, β);
- what "the metric" is on a qubit (the readout, W2);
- which observables are physical (W7).

The graviton is still the one thing with no construction at any price except supplying it (P-N1).

### 1.1 The electron–photon split (W1)

- **R16-10: CONFIRMED WITH CORRECTIONS [ref; `TESTS:5890-5893`; `vR16-10:27`].**
  - **Theorem L.** For the named box-exact D1/literal/G families with integrable valleys, IR excision gives a finite, path-independent (m, λ) → (0, 0) limit F_s = K_s + Λ_s. Here K_0 = −1/3 and K_½ = +2/3, and there is no divergent IR log.
    - λ = 0 is a boundary value.
    - Corrections such as m² log m are not excluded.
    - Uniformity over all C² deformations is not proved (`vR16-10:3`).
  - **The Dirac zero.** The stiffened R8-5 photon gives a zero by continuity near G* = 3.1264: F_½(G* ∓ 0.1) ≈ −0.0546 / +0.0532 (`vR16-10:7-12`). That photon's whole-zone v_max is 7.35299 (`:16`).
  - **Two readings of class membership** (`vR16-10:14-17`):
    - under the literal registered text, Dirac is **REFUTED-ZERO**;
    - under a subluminal-photon reading, the witness is excluded and Dirac is **OPEN**.
  - **Minimality not confirmed.** n_t ≤ 2 is a checked upper bound. "A tuning is any real equation" is not convention-independent, since F² + Σ² = 0 packs two equations into one. COUNTED is not met (`vR16-10:19`).
  - **Subluminal-photon bounds.** ⟨w(π)⟩⊥ ≥ 0.0255870490, so the Dirac tadpole is ≤ −2.02027 and the scalar seagull ≤ −1.01014. These bound only the leading tadpole/seagull, not F_s (`vR16-10:21-25`).
- **[S23 reading]**
  - The round-17 rule "gauge fields too" (`TESTS:5699`) makes the subluminal reading the operative one for every later item. On it, the charge rows stay at R16-2's conditional 3 (per class) or 7 (per species).
  - P101 survives only as a named price that gives up that rule.

### 1.2 Producing the graviton (W2)

- **R16-11: CONFIRMED WITH CORRECTIONS, TRANSFERS [ref; `TESTS:5894-5899`; `vR16-11:37`].**
  - **The statement.** Take a volume-uniform quasi-local unitary that maps the chosen ground state into an exact Gauss sector, with a uniformly finite K₂ (Σr¹³Φ < ∞ suffices for finite-range, bounded-density H). Then the dressed, V^{−1/2}-normalized TT-electric m₁ ≤ 2S²K₂k⁴.
  - **Corrections:**
    - Corollary B-inv does **not** close R16-7's gap 1. A constant contribution from gapped weight is compatible with an Einstein–Hilbert IR pole (`vR16-11:23`);
    - the approximate floor is not small in the thermodynamic limit (`:13`);
    - the 20-slot minimum is shown only in finite boxes (4³, 6³, 8³) (`:31`);
    - spin ice is a comparator, not a control (`:27`).
- **R17-1: CONFIRMED WITH CORRECTIONS, WINDOW; EXTENDS refuted at the f-sum level [ref; `TESTS:6157-6166`; `vR17-1:24-28`].**
  - **Why the bound fails.** Modular Gauss invariance gives Gδ = Nγ and M₀ = −N·D(γ).
  - **The explicit models:**
    - an N = 2 cube + μ₈ stabilizer model has an exact, positive, k-independent TT-label f-sum;
    - a moving-cube model has m₁ ≥ c(k̂, ε)k² for generic directions and polarizations, with a rank-one TT form;
    - integer lifts recover O(k⁴).
  - **Not a graviton.** The face-only k⁰ model is the even sector of a scalar 3D transverse-field Ising model; the k² model supplies only a scalar-density signal (`vR17-1:27`).
  - **Corrections:**
    - the k⁰/k²/k⁴ split gives the generic leading orders, not an exhaustive trichotomy (`:10`);
    - "no Z₂-invariant hop of weight < 20" holds only in the tested boxes, and the big-M MILP is not a reliable certificate (`:13`);
    - A₁+E holds only under the pure-permutation action (`:22`);
    - "every stoquastic ground state" is too strong (`:22`);
    - no slot model has been compiled into one M₂(C) per site (`:25`).
- **R17-6: CONFIRMED WITH CORRECTIONS. OPEN; OBSTRUCTED for two bounded classes [ref, bounded; worker `TESTS:6192-6204`; `vR17-6:17,19`].**
  - **No general representation obstruction.**
    - For N0914's slots at Γ, the six slots carry 2A₁+2E; at R they carry A₁+E+T₂.
    - Pair labels can carry T₂ at Γ.
    - Proposition S needs F_all to be a Hamiltonian symmetry (`vR17-6:5`).
  - **Theorem G (sharp):** in the internal-Goldstone class there are at least 4 gapless branches. It needs the extra hypothesis that the Goldstone representation is continuously identified with the broken-generator representation (`:11`).
  - **Theorem Z:** take a unique symmetric ground state, vanishing axial TT f-sums, both TT responses nonzero, and a finite, direction-independent full response. Then strict V/S spectral gaps are impossible without a pinch point. "Gapped" here means a uniform gap, including multiparticle continua (`:13`).
  - **Z′ is overstated:** it forces a partner only in an irrep whose leading coefficient is nonzero (`:13`).
  - **Lemma R narrowed:** exact only for states uniform over the full coset n₀ + ker G. Equal-weight CSS on span{1} is a counterexample (`:15`).
  - **Unresolved domain:** pinch-point phases; finite-response k⁰ f-sums; non-strict V/S continua; degenerate or symmetry-broken grounds; readouts outside E⊕T₂ (`:19`).
- **[S23 reading] Where W2 stands.**
  - Six bounded exclusions: X1, X-G, G-mix, auxiliary irreps, the integer-law f-sum, and the dressed integer-law f-sum. Two bounded Z₂ obstructions: G and Z.
  - The axioms' own Qubit text (`AX:47`) matters exactly here. The Z₂ reading (P110) opens the f-sum, and R17-6 moves the obstruction into dynamics.
  - The live window is a pinch-point Z₂ phase whose emergent constraint is not dressing-connected to an integer law. That is P96 restated with a measurable signature.
  - P-N1 is still the only known source of a light-like TT pair (`rR17-6:276`).

### 1.3 The graviton cone, the shear and the bill (W3, W4, W11)

- **R17-4: CONFIRMED WITH CORRECTIONS, COUNTED-ROWS for U + E1 [ref; `TESTS:6171-6178`; `vR17-4:15`].**
  - **Off-axis formula** Ξ(n, e) = (1/32)⟨W_e A_nn/ε⁵⟩ − (1/192)⟨(n·∇)²W_e/ε³⟩. Confirmed to 6.7e-16. The D²W form needs W ∈ C² or a weak derivative (`vR17-4:3`).
  - **U identities (exact):** Ξ_face2 ≡ Ξ_T2g, and Ξ_face1 = (3Ξ_Eg + Ξ_T2g)/4 − ⟨K₆/ε⁷⟩/128. So the off-axis rows add **one** condition (`:5`).
    - [worker] On R16-3's U zeros, Ξ_face1 ≈ −8.94e-4. The largest value found at points with both axis rows ≥ 0 is −1.12e-4 (`rR17-4:23,25`).
    - [ref] The referee calls this strong but non-certified evidence of conflict.
  - **The LV tadpole** is strictly positive and no edge shape zeroes it (`:11`).
  - **The vertex extension matters.** E2 moves the NN face1 value from −1.24545e-4 to +4.42800e-4 (`:9`).
  - **Lemma M.** A single periodic, C₂ᵧ-covariant scalar T₂g amplitude must vanish at k_x = π. M does not, so M has no absolutely summable doubler-free realization (`:7`).
  - **Dated consequence (`TESTS:6178`).** The M-vertex numbers in R16-3, R16-9 and R16-13 come from a non-local vertex.
  - **Bill.** The literal reading is COUNTED-ROWS, not "in part". Conditional arithmetic: 8 + CC per class / 12 + CC per species (U + E1), and 9 + CC / 13 + CC (E2) (`:13`).
- **R17-10: worker reading K₆ OPEN on the relaxation superset, CERTIFIED-CONFLICT on the fast-only slice 𝓕; μ_E OPEN; referee running [worker; `TESTS:6384-6390`].**
  - **Theorem F.** On 𝓕 (the sharp-turn limit, disjoint from 𝒮), an exact rational certificate shows that the axis zeros force ⟨K₆/ε⁷⟩ > 0 for every m.
  - **On the general relaxation**, local searches keep the sign (best −6.3e-5), but there is no certificate: the bin slack is 70–80× the margin, and no SDP solver is installed.
  - **μ_E:** no constant-multiplier pointwise certificate can exist.
  - **P-K6′:** any shape solution of the K₆ row needs a finite fraction of slow-slope structure.
  - [S23 reading] This is the first certified statement on a cone row. It covers only the limit P87's zigzags approach (sharp turns), so it rules out the cheapest P87-type shapes for the K₆ row, not shape in general.
- **R16-13: NOT CONFIRMED (the LIFTED). Reading OPEN [ref; `TESTS:6146-6156`; `vR16-13:29`].**
  - **Confirmed conditionally** (ultralocal seagull, stipulated V0 Dirac TT vertex and SF strain response):
    - Theorem DT, to 2.7e-9;
    - opposite signs, D1 versus G;
    - Lemma V1;
    - the Wilson T₂g shear mechanism (H_xy = W′_xW′_y), with μ_T2 = −3.53e-5 at the root;
    - a subluminal codimension-3 axial zero: (b₂, b_f, r) = (1.740668966789, 1.313474886012, 0.572783392213) at m = 0.01, with Jacobian determinant 6.75e-8 (`vR16-13:5-23`).
  - **Not lifted:**
    - the only root uses the non-local M amplitude;
    - μ_T2 ≠ 0;
    - neither one-Higgs-edge nor SM-count content is reached (`:25`).
  - **Corrections:** μ_E is about 1% underconverged; the width fraction (not w₂) is frozen; the mass drift is linear, not O(m²) (`:15,23`).
  - **This invalidates R16-9's "μ_T2 = 0" row** (`:17`).
- **[worker] SM counts without vectors.** With 4 scalars + 22.5 Dirac fields the solve stalls. Dirac birefringence, Ξ_T2g − Ξ_Eg ≥ +2.6e-3 per field on every Dirac law tested, dominates (`rR16-13:59,200,225`).
- **R17-9: worker reading OPEN; referee running [worker; `TESTS:6267-6281`; `rR17-9:279-300`].**
  - **The vertex (VU).** The vector TT vertex is the Maxwell stress of site-averaged fields at R9-9's placement. It is local, and it reduces to the continuum helicity-2 amplitude.
  - **The sign.** The Maxwell vector pushes the cone outward, like Dirac, through E–B interference. So the registered premise "boson-like" fails.
  - **Under VU, no SM-count zero.** The T₂g row needs Ξ_γ,T2g ≤ 6e-4, while offsetting the Dirac birefringence needs Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3. The two are incompatible on every sampled law.
  - **Under VM, an SM-count zero.** VM moves the magnetic product to z + ½. The content is 4 scalars + 22.5 Dirac + 12 vectors, one Higgs edge, every edge subluminal. It needs 3 tunings for Ξ_T2g = Ξ_Eg = μ_E = 0 at m = 0.01 and 0.001.
    - μ_T2 = +0.106 is left over, from the Wilson-Dirac fields.
    - The photon box is 0.25/a, with a lattice-modified photon beyond it whose shape re-enters the charge cones, which were not re-solved. The Dirac r is 3.1% below the cap (`rR17-9:284-287`).
  - **The placement decides.** It is a law datum (P127). By the precedent of `vR16-13:25`, the worker does not read VM as in-setting (`rR17-9:299`).
  - **The block split ends.** The photon edge now enters the gravity rows (`TESTS:6279`).
  - **Running on its two open questions:** R17-12 (is the placement forced?) and R17-13 (is μ_T2 zeroable or sign-definite?).
- **[S23 reading] Which zeros are local.**
  - The referee-confirmed common E_g/T₂g zero is on **M** (`vR16-3:13`), which is now non-local.
  - The U common zeros were found by the worker (`rR16-3:23,263`) and reused by R17-4 (`rR17-4:23`). No referee re-solved one.
  - So P87 on a local vertex rests on worker-checked U zeros together with the refereed U witness Z1. R17-10 presupposes those zeros; its referee should re-solve one.
  - The shear joint-zero question on a local vertex reverts to R16-9's U branch: OPEN, with a margin of about 1.3e-4.
  - R17-9's SM-count zero [worker] uses the local **U** scalar vertex (`rR17-9:40,67`). So its only locality question is the vector placement (R17-12).
  - Its off-axis rows for vectors and Dirac fields were not computed. The off-axis count could be 2 if face2 ≡ T₂g fails for them (`rR17-9:273`).

### 1.4 GW170817 as a gauge-invariant test (W15)

- **R17-5: CONFIRMED WITH CORRECTIONS, EXCLUDED-MB [ref, bounded; `TESTS:6179-6191`; `vR17-5:17`].**
  - **The class:** finite-N free quadratic matter on the BZ torus, with continuous quasi-local kernels, W1 regularity, symmetric stress, a projectable lapse and multiplier-generated shifts.
  - **What fails:** W2_pf forces k-independent momentum spectra, so standard W2_pf is impossible for nonzero momentum density. Nonzero-label sectors are 1D axis movers.
  - **Corrections:**
    - Lemma RB is conditional on H-RB (`:9`);
    - Lemma R needs a continuous SO(3); proper cubic rotations alone do not suffice (`:11`);
    - "only remaining route" holds only while the free/symmetric/projectable assumptions are kept (`:15`).
- **R17-8: CONFIRMED WITH CORRECTIONS. Reading OPEN, with scoped no-gos [ref; worker `TESTS:6251-6266`; `vR17-8:3,39`].**
  - **Confirmed:**
    - **Lemma N:** in the canonical, local-in-time class with no ∂ₜξ acting on matter, any altered leading generator is locked to ∫T^{0j} (`:7`);
    - **MIX-1** (single band) (`:11`);
    - **MIX-2:** for one small mixing eigenvalue with any Jordan blocks, and for several when the symbols are real-analytic (`:13-15`).
  - **Lemma FD corrected.** On an equal-energy surface the identity holds to first order with an O(q²) remainder. Off-shell absorbability is not proved (`:19`).
  - **Theorem W (iii) repaired** in the analytic tame class, by analytic continuation plus the tame Reeb theorem. It gives rank C ≤ 1 against the rank 3 that H-RB needs (`:21-29`).
  - **Correction:** the Jordan-block sentence is false as written (`:13`).
  - **Still open:**
    - continuous non-analytic multi-shift mixing;
    - crossing bands;
    - joint mixing with field dependence (`:31,35`).
- **[S23 reading]**
  - In the free, finite-band, continuous, symmetric-stress, projectable class, every generator kind tested is excluded in its analytic or isolated-band form.
  - GW170817 on a grid still has no gauge-invariant formulation unless the grid pays one of:
    - P64 (tower);
    - P90 (discontinuous symbol);
    - P124 (a non-canonical shift action);
    - a merely continuous or crossing-band construction;
    - interactions, non-symmetric couplings, or a non-projectable lapse.

### 1.5 Set A and the post-Newtonian β (W8, new W17)

- **R16-14: CONFIRMED WITH CORRECTIONS. E1 and E2 OPEN and observationally tied; L0 and L½ EXCLUDED [ref, bounded; `TESTS:6000-6006`; `vR16-14:23`].**
  - **Linear order.** E1 has α₁ = α₂ = 0 and γ = 1, with corrections from 6(ωτ)² and 1/r³ terms. E2 has the same near-zone projection plus tiny non-PPN friction; calling E2 "exactly PPN" globally is too strong (`vR16-14:5`).
  - **The spheroid factor.** 45(cτ/R)² = 6.9378e-13, a margin of 3.4598 decades, for a weak-field spheroid. It is not a neutron-star coefficient (`:11`).
  - **Lemma L.**
    - A source-linear geodesic metric gives β = 0; the literal ½hT coupling gives β_eff = ½.
    - The corrected Mercury values are 57.3067″/cy and 50.1433″/cy, failing by 3.679 and 3.378 decades (`:13`).
  - **Completion N.** It formally restores β = 1, but it is a new nonlinear source/action completion. The metric is no longer linear in independent matter records, E2 lacks a sink action, and premise (iii) is not established (`:15`).
- **[S23 reading]**
  - New wall **W17**: a metric that is linear in matter records cannot give β = 1. Option A pays P107 (completion N) on either route.
  - **P107 and P88 interlock.** Under N the metric solves the Einstein equations with recorded sources. It is then fixed by records only together with the free TT data that R16-4 showed are remembered. So "a readout value is determined by record content alone" (`AX:82-83`) needs either P88's zero datum or recorded initial TT data.

### 1.6 Λ (W9, W10)

- **R17-3: NOT CONFIRMED (the TUNING). Reading OPEN [ref; `TESTS:6007-6016`; `vR17-3:19`].**
  - **The sound bounded obstruction:**
    - g ≡ 0 forces GR with one constant, C = ρ_v,late, and a fixed independent value of it is radiatively unstable;
    - without an informative pre-branch label, no causal common rule cancels histories that end in unequal vacua;
    - fixed nonnegative record weights cannot source radiation;
    - the causal average signals, and gives only 1.27 accelerating e-folds (`:13`);
    - vacuum-shift symmetry does not select C.
  - **The ruling.** (S), C = E₀[H], is number-free and radiatively tracking. It is an added source/action principle, not forced, and not an independent exact number (`:17`).
  - **Corrections:**
    - Theorem T is not proved, because H-an makes V analytic but not Γ (`:5`);
    - Lemma U is not uniqueness among all number-free references, and `AX:82-83` supplies no Hamiltonian (`:7`);
    - Lemma M (records) holds only for fixed nonnegative additive weights. An unrecorded plateau gives 60+ e-folds, but only through g ≠ 0 (`:9`);
    - the record-map shifts, 3.516e77–4.016e88 ρ_Λ, are cutoff- and a-conditional (`:11`);
    - the list of symmetries is not exhaustive; frustration-free positivity is omitted (`:15`).
- **R17-7: CONFIRMED WITH CORRECTIONS. Reading OPEN [ref; `TESTS:6129-6142`; `vR17-7:74`].**
  - **(a) Late universe.**
    - Λ̃_late = κ(V_late − e₀) ≥ 0, and it is zero with P93.
    - Acceleration need **not** be temporary: the λ = 0.639 attractor has w = −0.864 and a ∝ t^4.90 (`vR17-7:12`).
    - The 54.4% and 62.2% BAO-proxy recoveries are arithmetic on a proxy, not a likelihood.
    - "Phantom not reproducible" holds for canonical scalars only (`:14`).
  - **(b) Grid zero-point.**
    - The residual is (ρ, p) = (0, ρ₀+p₀), 1.2–1.8e123 ρ_Λ per real scalar at a = ℓ_P (`:21`).
    - It is invisible under (d-i), a bridge-specific result. Under (d-ii), ρ_v + p_v = 0 is needed locally (`:23`).
    - c₄ = +0.0388 (with t* = 0.00117), so one c₂ tuning is insufficient. "One tuning per order" is shown only through m⁴ (`:30`).
  - **(c) Metastability.**
    - The SM-only numbers are 1.49e112 and 2.87e120 ρ_Λ, conditional on extrapolation and cutoff (`:37-40`).
    - (S′-start) is causal, but adds a basin structure, a first reading, a loss of positivity, and P94′ (`:42`).
    - (S′-current): a varying algebraic C with separately conserved T violates Bianchi, but a local carrier can escape this (`:44-50`).
  - **(d) Covariant form.**
    - G + Λ_*g = κT with Λ_* = −κe₀ is local, covariant and non-signalling once e₀ is stipulated.
    - The selection map H ↦ e₀ is not local or manifestly covariant (`:58`).
  - **Lemma X.**
    - Dense projection records cost 1.1938/a⁴; the first isolated record costs 2.38/a. This is about 1.05e123 ρ_Λ per staggered field, conditional.
    - R-proj records give P4 heating; R-label records cost nothing (`:60-67`).
- **R17-11: worker reading CONSISTENT in 𝒟; referee running [worker; `TESTS:6319-6335`; `rR17-11:263-285`].** The expectation was SIGNALS.
  - **Class 𝒟:** R14-5's E-sector, with √h fixed per site (so the spatial trace equation is not imposed), sites riding the slice normals, and C = E₀.
  - **The exchange.** The grid enthalpy W is absorbed by the unique exchange current Q_ν = ∇^μ(W h_μν).
    - W never enters λ̇ (generalized Lemma V).
    - Under (S), g′ ≡ 0 and the site frame drops out of the field equations.
  - **Linear order.** The dust equation has no W terms, and there is no instantaneous channel.
  - **Other receivers excluded:**
    - unimodular Λ(x), which would drift by about 1e123 ρ_Λ;
    - matter;
    - an ultralocal khronon;
    - (d-ii) still needs W = 0.
  - **Prices.**
    - P-vac′ (= P70's (d-i), sharpened; no number).
    - P-r1711a: a receiver that exists only with √h fixed per site plus site creation. The worker counts it once with P52/P53.
    - P-r1711b: a hypersurface-orthogonal site congruence with θ_s ≥ 0 through collapse. Its existence is P68's hypothesis.
    - P-r1711c: a non-Lagrangian partner (`rR17-11:267-270`).
  - **Bill.** R17-4's LV-tadpole row and P70's uniform part are one quantity. In 𝒟 it is paid by (d-i) with no number, so the bill drops by one (`rR17-11:271-273`). This is the identification S23 made independently in §3.1.
- **[S23 reading] Where Λ stands.**
  - Refereed:
    1. the four texts force no Λ removal;
    2. without an added principle, every non-signalling route is one constant subtraction whose value is stipulated;
    3. a number-free principle (S) exists. It is consistent, non-signalling in its fixed-e₀ form, and carries three named conditions.
  - This supersedes S20's "W10 collapses onto P51" (§5). The price moves from "a tuned number" to "an added sentence plus conditions".
  - (S)'s sharpest observational lever is P93, the stability of the electroweak vacuum. R18-2 drafts that test.
  - The grid-enthalpy condition is the same physical object as W9's p-tadpole and the bill's "LV tadpole" row (count once; §3.1).
  - If vR17-11 confirms CONSISTENT, condition 2 costs no number, but its receiver needs site creation with √h fixed per site. That is a Lattice price (`AX:37`, P52) that (S) alone did not need. Then (S) + (d-i) is a two-sentence package: "the lowest state weighs nothing" and "the vacuum's enthalpy is exchanged with site creation".

### 1.7 W7, the off-box tail

- **R16-12: CONFIRMED WITH CORRECTIONS, OPEN [ref; `TESTS:5900-5906`; `vR16-12:21`].**
  - T3/J3 are confirmed at leading order, in the weak Killing sector, with weak/deformed closure.
  - **B3** is forced only under the standard HDA, inside the linear-bilinear bounded-angular ansatz: X_T = −(q·Δ_b)/(|q|²(q·v)). It is a presentation-dependent obstruction. The kernel is homogeneous of degree −2; only its angular factor is unbounded (`vR16-12:11`).
  - **Lemma C corrected.** Strict |v| < 1 is sufficient, not necessary. At |v| = 1 the limit is bounded, 0.49497475 (`:15`).
  - **Population.** The infimum is 1.431782/a = 1.748e19 GeV (m = 0.3). Occupation is negligible only for a low-temperature thermal ensemble; number-conserving matter may keep any initial edge population (`:19`).
- **R17-2: CONFIRMED WITH CORRECTIONS, OPEN [ref; `TESTS:6167-6170`; `vR17-2:17`].**
  - **Lemma D** is confirmed (ratios −1 to within 1.1e-14). W is the inverse of *one particular* linearized-GR Coulomb/comoving dressing, not a unique one (`vR17-2:5`).
  - **Lemma H** is confirmed weakly. H′ ≈ H₀; H′ is non-local off shell, but that non-locality is constraint-proportional, so conditionally gauge (`:7`).
  - O_F is invariant only under the dressed *linear* constraints; a TT counterexample gives a variation of −1/2. R13-4's operational test is not invalidated (`:13`).
  - **Degree 3 is unclosed:** the global boundary algebra, the zero-frequency shell, the remaining boost brackets, exact lower-order closure and a completed Dirac observable are all missing.
- **[S23 reading]**
  - At leading bulk order, W7's tail reads as GR's own Coulomb-type dressing of edge quanta, written in lattice variables.
  - What is lattice-specific has moved to the global boundary algebra and the q·v = 0 shell.
  - Whether anything physical remains depends on which observables are admitted (P118). That is the same kind of bridge as W2's readout.

### 1.8 The count (W11)

The rows are R13-8's P,T-even rows, with each source's status. The [S23 reading] totals add R16-13's μ_T2 row to R17-4's refereed arithmetic.

| Row | U + E1 (local vertex) | Status |
|---|---|---|
| Charged-matter cones | 3 per (spin, \|q\|) class / 7 per species | [ref, conditional; R16-2]. ≤ 2 only with P101, an upper bound [ref, R16-10] |
| Graviton axis cone (E_g, T₂g) | 2 edge shapes | Z1 [ref] for U; common zero [ref] only for M (non-local); U zeros [worker] |
| Off-axis TT (face2 ≡ T₂g; face1 = K₆) | 1 for scalars; possibly 2 with vector/Dirac rows (not computed, `rR17-9:273`) | [ref] one condition for U scalars. Shape-compatible with the axis zeros: OPEN on 𝒮; certified conflict on the sharp-turn slice 𝓕; shape needs slow-slope structure ([worker, R17-10]) |
| E_g shear μ_E | 1 | OPEN whether shape can pay it jointly (R16-9). No constant-multiplier certificate exists ([worker, R17-10]). [worker, R17-9] Under VM, SM content zeroes Ξ_Eg, Ξ_T2g and μ_E together with 3 tunings |
| T₂g shear μ_T2 | 0 with scalars only; ≥ 1 per Wilson-Dirac edge | [ref, mechanism; `vR16-13:17`]. [worker] +0.106 at R17-9's VM root. R17-13 [pending]: zeroable or sign-definite |
| LV tadpole (vacuum ρ + p) | 1 non-shape; **0 numbers under (d-i) in 𝒟** | [ref, `vR17-4:11`] for the 1. [worker, R17-11] for the 0 (`rR17-11:271`). Same object as P51/P70 [S23 reading; R17-11 worker agrees] |
| CC | 1 tuned, or 0 numbers under (S) with its conditions | [ref, `vR17-3:17`; `vR17-7:69`] |
| **Total, scalars only** | **8 + CC / 12 + CC** | [ref, arithmetic, `vR17-4:13`] |
| **Total, with Wilson-Dirac content** | **9 + CC / 13 + CC** | [S23 reading]; R17-9's worker bill agrees (`TESTS:6279`) |
| **Total, with Wilson-Dirac, (S) and (d-i)** | **8 / 12 numbers, plus the two added rules** | [S23 reading] on [worker, R17-11] |
| E2 extension | +1: 9/13 (scalars), 10/14 (with Wilson-Dirac) | [ref] / [S23 reading] |

**[S23 reading]**
- Precisions are unchanged: about 1e-16 for the charge rows, about 1e-13 for the shapes.
- R17-10 [worker] certifies the K₆ conflict only in the sharp-turn limit. If its referee confirms, the K₆ row stays a count of 1 but cannot be paid by sharp zigzags; it needs slow-slope shape structure or a non-shape knob (P122).
- SM counts on one cone:
  - not reached under the local vertex at R9-9's placement (VU) [worker, R17-9];
  - reached under VM, with μ_T2 left over [worker].
- The bill's next movers are R17-12 (placement) and R17-13 (μ_T2). If both go the favourable way (VM allowed, μ_T2 zeroable by shape), the total does not fall: those rows are already counted. What changes is that the cone would then be paid entirely by edge shapes and counterterms, with no pairing.

---

## 2. Updated wall map

"DERIVED" means a refereed no-go or confirmed lemma in a stated class, including bounded EXCLUDED, FAIL and OBSTRUCTED. "OPEN" means no refereed no-go covers the route's class and there is no PASS. "Cheapest named price" is the least expensive price on record that passes the wall. Nothing is adopted.

| # | Wall | Refereed statement (scope) | DERIVED or OPEN | Cheapest named price | Axiom lines touched by that price |
|---|---|---|---|---|---|
| W1 | **Electron–photon split** (C, C-box, C-box-S) | No interval zero in 𝒬_lit⁻ (R13-7) or 𝒬_W⁺ ⊃ D1 (R16-1). Theorem L: finite λ → 0 limit, integrable valleys (R16-10). Literal class: Dirac zero with a v_max 7.35 photon (R16-10) | **DERIVED on D1** (λ > 0). Class-wide nonvanishing **REFUTED-ZERO** on the literal class; **OPEN** with subluminal photons. Count OPEN | P73: 3 per class / 7 per species, conditional. P101: ≤ 2 (an upper bound) with a lattice-superluminal photon | None (`AX:114-130`); sizes `AX:189-190`. P101 gives up the gauge-field subluminality rule (`TESTS:5699`), which is no axiom line |
| W2 | **Graviton production** | X1; X-G; G-mix; auxiliary irreps (R15-3); integer-law f-sum O(k⁴) (R16-7); **dressed integer law O(k⁴) (R16-11)**; **Z₂ clocks escape the f-sum bound (R17-1)**; **Z₂ Goldstone ≥ 4 branches; soft-TT finite response ⇒ V/S zero-energy weight unless a pinch point (R17-6, bounded)** | **DERIVED** (six exclusions + two bounded Z₂ obstructions). **Production OPEN.** Z₂ pinch-point window OPEN | P-N1 (= P41/P49/P71), a supplied CCR graviton. The Z₂ route (no production shown): P110 + P113 + P96 | P-N1: Qubit `AX:45-53` (`:47`). P110: none directly (`AX:47` presentation; `AX:57-61` conserved structure). P113: `AX:82-90`. P96: none (dynamical) |
| W3 | **Graviton–matter cone** (bare cone, prescription-scoped) | Ξ < 0 on 𝒰₀ (R14-3) and B″ (R16-3). Universal negativity REFUTED (Z1, U and M). **M non-local (Lemma M).** Common E_g/T₂g zero refereed only on M. **Off-axis: U + E1 adds one K₆ condition (R17-4)** | DERIVED in 𝒰₀ ∪ B″; REFUTED as universal. **K₆ jointly with the axis zeros: OPEN** on 𝒮 (search suggests conflict); [worker, R17-10] certified conflict on the sharp-turn slice 𝓕. Physical: OPEN (W15) | P87 on U (2 shapes; zeros worker-checked) + **P122** (K₆: a shape, or a q²-dependent TT seagull) + P63(iii) refined (vertex and extension datum; for vectors, the placement P127 [worker]). M excluded (**P123**) | Shapes: none (`AX:116-123`). Vertex data: `AX:187` |
| W4 | **Shear** (supplied zero-point vacuum) | μ_E zero per mass on G_w (R14-3). Joint zero with P87: uncertified tension, U margin about 1.3e-4 (R16-9). Fermion loops opposite in sign (D1 vs G), joint zero only via M. **μ_T2 ≠ 0 for Wilson-Dirac (R16-13)** | Not a wall in the empty vacuum. Otherwise μ_E: one condition, shape-compatibility OPEN (R17-10 [worker]: no constant-multiplier certificate); μ_T2: one per Wilson-Dirac edge. [worker, R17-9] SM content: joint Ξ/μ_E zero under VM, none under VU; R17-12/R17-13 [pending] | P100 (a non-shape knob) + **P109** (μ_T2). Or pairing (P46). [worker] VM placement (**P127**) with 3 edge tunings | P100: none, `AX:47` or `AX:184-187` per option. P109: none (tuning) or `AX:47` (Clifford-flat 8-component) |
| W5 | **Lattice-scale superluminality** | Lemma V; R14-1 repair; D1 v_max ≤ 1. **Lemma V1: s′² + 3W′² ≤ 1 ⇒ v_max ≤ 1 for Wilson-Dirac (R16-13, conditional)**. Round-17 rule extended to gauge fields | DERIVED (cause) and repaired for matter. The photon rule is now load-bearing (R16-10's 7.35) | P61 | `AX:57` |
| W6 | **BF photon multiplet** | Physically non-local in 𝓔 (R13-4(i)) | DERIVED in 𝓔 (unchanged) | P60 | Dynamics downstream; `AX:57` only under a range reading |
| W7 | **Off-box gravity tail** | 1/r² kernel, 1/r⁴ curvature, box-inert (R16-8). T3/J3: weak/deformed translation closure at leading order (R16-12). B3: a presentation-dependent bounded-angular obstruction (R16-12). **Forced translation term ≅ inverse of a linearized-GR Coulomb dressing; coupling movable into non-local multipliers; no instantaneous physical bulk interaction (R17-2)** | **OPEN.** Degree 3 unclosed: boundary algebra, q·v = 0 shell, boost brackets, Dirac observable | **P116** (non-local multipliers; gauge only with a relational readout) + **P117** (boundary charges) + **P118** (an observable-algebra readout bridge). Alternative: P104 | P116: `AX:116-130`. P117: `AX:82-83`. P118: `AX:82-83`, `AX:187`. P104: `AX:57-61` |
| W8 | **Set A, covariant** | 𝒰 no-go (R12-4); literal E1 gain (R13-6); E2 drag (R14-2); spin-2 assembly (R15-2); TT memory (R16-4). **α₁ = α₂ = 0, γ = 1 at linear order; β unfixed by the bare routes (R16-14)** | DERIVED walls; **E1 and E2 OPEN and tied** | E1: P65 + P76 + P88 + **P107**. E2: P66 + **P107** + an unbuilt sink action | `AX:185-186`; `AX:94` (P88); `AX:82-83` and `AX:187` (P107) |
| W9 | **Λ, fixed grid** | V1 tadpoles, w ≥ 0 (R11-3). **The tadpole is strictly positive on 𝒮 (R17-4).** **Under (S), the energy cancels and the enthalpy ρ₀+p₀ remains (R17-7)** | DERIVED (unchanged) | P51. Or, under (S), the energy part is number-free and the enthalpy part is paid by (d-i) ([worker, R17-11]: CONSISTENT in 𝒟, no number; the receiver needs √h fixed per site plus site creation, P52) or by P70 (d-ii): pairing, or ≥ 2 tunings per species (shown through m⁴) | `AX:187`; `AX:47` (pairing); `AX:37` (P52, for the (d-i) receiver); `AX:189-190` (sizes) |
| W10 | **Λ, site creation + P-T** | As S20, plus: **bounded obstruction (R17-3): g ≡ 0 ⇒ GR + one stipulated constant; fixed values radiatively unstable; no causal rule for unequal late vacua; record weights cannot source radiation.** **(S) is a consistent, number-free added principle (R17-3), conditionally viable (R17-7)** | **DERIVED:** without an added principle, no non-signalling route avoids a stipulated constant. **OPEN:** (S) with its conditions | **P92 = (S)** (no number) + P93 + ((d-i) [worker: consistent in 𝒟, with P52 and P128] or P70) + R-label records (P4). Alternative P125 (S′-start) | `AX:187`; `AX:116-130` (no H supplied); `AX:94` (reading, owner); `AX:79-83` (records); `AX:37` (P52) |
| W11 | **Set C count** | R13-8; R16-2; R16-3; **R17-4: 8/12 + CC (U + E1), 9/13 (E2)**; **μ_T2 row (R16-13)** | **OPEN.** K₆ and μ_E rows uncertified. SM counts: no zero under VU, a zero under VM with μ_T2 left over ([worker, R17-9]). R17-12/R17-13 [pending] | P72 refined by P73, P87, P122, P100, P109, P51 (0 numbers under (d-i) [worker]); P127 for VM | None (tunings); P127: `AX:187` |
| W12 | **Matter on the box** (linear gravity) | R11-4 PASS WITH SCOPE; survives subluminal (R14-1) | No wall at linear order (unchanged) | P56 | Unchanged |
| W13 | **Set B** | R10-2 | DERIVED (unchanged) | Give up RP, or whole-zone SLAC | Unchanged |
| W14 | **Λ, set A q-charge** | μ fixed to 2.1e-55 (R10-4) | Minimal realization excluded; OPEN beyond (unchanged) | P54 | Unchanged |
| W15 | **Translation Ward wall** (GW170817 as a gauge-invariant test) | T_pf, single band (R16-5). **EXCLUDED-MB: multiplier class, multi-band (R17-5).** **Lemma N, MIX-1/2, FD, Theorem W (R17-8, scoped)** | **DERIVED** for free finite-band local matter: the multiplier class, canonical altered generators, finite mixing (analytic for several eigenvalues), and regular linear field-dependent generators (isolated analytic bands, given H-RB). **OPEN:** continuous non-analytic multi-shift mixing, crossing bands, joint mixing + FD, interacting, non-symmetric, non-projectable | P90; P64; **P124** | P90: `AX:57-61`, `AX:187`. P64: `AX:47`. P124: `AX:187`, `AX:116-123` |
| W16 | **Newtonian attraction, sign-free finite slots** | Theorem D (R16-7). The scalar channel is not covered by the dressing transfer (R16-11) | DERIVED in the stoquastic conserving class (unchanged) | P97 | None; a source bridge is `AX:187` |
| **W17 (new)** | **Post-Newtonian β from records** | A metric linear in matter records: β = 0 (geodesic) or β_eff = ½ (literal coupling). Mercury excludes both, by 3.679 and 3.378 decades (R16-14, L0/L½) | **DERIVED** for the literal linear completions | **P107** (completion N) | `AX:82-83` (the metric becomes a nonlinear functional of records); `AX:187` |

**[S23 reading] The shape of the map.**
- **Changed since S20:**
  - W10 is no longer "a counterterm only": it has a number-free added-principle option.
  - W15 is DERIVED across nearly the whole free finite-band class.
  - W2 gained a window and a bounded obstruction at once.
  - W7's bulk part reads as gauge.
  - One new wall, W17.
- **Still OPEN because a construction is unbuilt:**
  - W2's pinch-point phase;
  - W7's degree-3 boundary algebra;
  - W8's N completion and sink;
  - W11's K₆/μ_E certificates and SM counts;
  - W15's non-analytic and crossing-band routes.
- **Where the axiom texts bear directly.**
  - Qubit (`AX:47`): W2, through the Z₂ reading.
  - Record readout (`AX:82-90`): W2, W7, W17.
  - "A law privileges no states" (`AX:94`): W10, through (S) and E₀; W8, through P88.
  - Every other open wall ends at the source/action gate (`AX:187`).

---

## 3. Price ledger delta since S20 (P107 onward; named only, none adopted)

S20 ended at P106 (`S20:401`).

### 3.1 Label collisions, resolved; count-once notes

| Worker label | Item | Meaning | S-number |
|---|---|---|---|
| P-r16-14a | R16-14 | completion N (the record is sourced by total stress) | **P107** (not P88 = "P-r16a", P92 = "P-r166a", or P101 = "P-r16-10a") |
| P-R16-13a | R16-13 | the V0 Dirac TT vertex and SF strain stipulations | **P108** |
| P-R16-13b | R16-13 | the Wilson-Dirac μ_T2 row | **P109** |
| P-R16-13c | R16-13 | the bill of the mixed-species lift | **withdrawn as a local price**: it uses M (`vR16-13:25`). No number |
| P-r17-1a | R17-1 | the Z₂-clock reading of the metric slot (mod-2 law) | **P110** |
| P-r17-1b | R17-1 | dynamics that conserves the uniform strain | **P111** |
| P-r17-1c = P-r17-6a | R17-1, R17-6 | the shift action of rotations = the R-point readout (Proposition S) | **P112** (count once). Equivalent only if F_all is a symmetry (`vR17-6:5`) |
| P-r17-1d | R17-1 | the N = 2 metric readout (coarse-grained Z₂ flux) | **P113** |
| P-r17-6b | R17-6 | composite two-slot T₂ labels | **P114** |
| P-r17-6c | R17-6 | low-symmetry slots plus a block encoding | **P115** |
| P-r17-6d = P-r16-7a = P-r16-11a | R17-6 | emergent constraints that are not dressing-connected | **P96** (no new number) |
| P-W7mult / P-W7bdy / P-W7ro | R17-2 | non-local multipliers / boundary charges / observable-algebra readout | **P116 / P117 / P118** |
| P-r173a | R17-3 | (S) | **= P92** (status change, §3.2) |
| P-r173b | R17-3 | final-state datum + consistency-selection rule | datum = R5-3's Λ6 (counted once); the selection rule is **P119** |
| P-r173c | R17-3 | record sourcing re-adds I, additivity and I(∅) = 0 | **P120** (named, not payable as stated) |
| P-r173d | R17-3 | matter-side relaxation (a late H-sensitive vacuum pick) | **P121** |
| P-K6 | R17-4 | the sixth-cumulant off-axis condition | **P122** |
| P-TTV₂ | R17-4 | the off-axis vertex-extension datum (E1 vs E2) | **P63(iii) refined** (no new number) |
| P-LocM | R17-4 | the non-summable M vertex | **P123** (named, not payable under a local law) |
| P-Tad | R17-4 | the trace-tadpole counterterm | **= P51** (count once; see below) |
| P-r175a → P-r178a | R17-5, R17-8 | altered shift generators → the non-canonical or ξ̇-dependent shift action left after Lemma N | **P124** |
| P-r178b | R17-8 | one-axis matter | an exclusion, not a price (as R17-5's axis movers) |
| P-r177a | R17-7 | (S′-start) with P94′ | **P125** |
| P-r177b | R17-7 | R-label records | **= P4** (`PRICE_NOTE:166`; count once) |
| P-R17-9a | R17-9 [worker] | the stipulated vector TT vertex (site-averaged Maxwell stress at VU, ultralocal seagull, W1 assumed, SF shear) | **P126** |
| P-R17-9b | R17-9 [worker] | the vector placement datum (VM: the B-part off R9-9's h_xy) | **P127** (refines P63(iii) for vectors) |
| P-R17-9c | R17-9 [worker] | the VM root's bill | a bill, not a price; no number (§1.3) |
| P-R17-9d | R17-9 [worker] | the in-setting route under VU: a non-shape knob, pairing, or the Fock vacuum | **= P100** (count once) |
| P-vac′ (sharpened) | R17-11 [worker] | (d-i) as a number-free exchange rule | **= P70 (d-i)**, refined (no new number) |
| P-r1711a | R17-11 [worker] | a receiver: √h fixed per site plus site creation | **= P52/P53** (counted once, as the worker does) |
| P-r1711b | R17-11 [worker] | a hypersurface-orthogonal site congruence with θ_s ≥ 0 through collapse | **= P68's existence hypothesis** (P-r15c; no new number) |
| P-r1711c | R17-11 [worker] | a non-Lagrangian partner (no ultralocal action gives −W h) | **P128** |

**Spelling hazard.**
- Round 17 uses several styles: P-r17-1a / P-r17-6a, then P-r173a / P-r175a / P-r177a / P-r178a, then P-r1711a and P-R17-9a.
- "P-r1711a" (R17-11) reads like a variant of "P-r17-1a" (R17-1, = P110).
- Round 16 uses P-R16-13a beside P-r16-14a.
- The wrap-up should use only S-numbers.

**Count once: the grid zero-point's enthalpy [S23 reading].** Four entries name one physical quantity, the zero-point vacuum's ρ₀ + p₀ > 0 (R11-3):
- P51's p-tadpole (`S14:182`);
- P70's (d-ii) branch;
- R17-4's "LV tadpole" row (P-Tad);
- R17-7's enthalpy residual.

In the graviton self-energy it appears as the u^μu^ν tadpole. In the Friedmann source it appears as the residual pressure. In the bill it is one row, not two. R17-11's worker reaches the same identification independently (`rR17-11:271`).

**Theorem-name collisions (for the wrap-up's theorem list; cite as "item + name").** New since S20:
- "Lemma M": R16-4 (product vacuum), R17-3 (record weights), R17-4 (M non-local).
- "Theorem Z": R16-6 (g ≡ 0 ⇔ GR + C), R17-6 (f-sum).
- "Theorem W": R16-1, R17-8 (winding).
- "Lemma R": R16-9 (relaxation), R17-5 (rotations), R17-6 (CSS/RK).
- "Lemma D": R13-6, R16-8, R17-2 (dressing).
- "Lemma N": R15-3, R17-8 (Noether lock). R15-4's Lemma N+ is distinct.
- "Theorem T": R9-9, R17-3 (not proved).
- "Theorem L": R15-6, R16-10. "Lemma L": R16-14 (β).
- "Lemma F": R13-3, R16-2, R16-8, R17-5.
- Unique names: Lemma H (R17-2), Theorem G (R17-6), Lemma U (R17-3), Lemma X (R17-7), Lemma V1 and Theorem DT (R16-13), MB-A, MB-B, Corollary S and Lemma RB (R17-5), MIX-1, MIX-2 and Lemma FD (R17-8), Identity V and Propositions F and S (R17-6), Theorem B′ (R16-11).

### 3.2 Status changes to earlier prices

- **P51** (fixed-grid vacuum).
  - R17-4: the tadpole is strictly positive for every law in 𝒮, and no shape pays it (`vR17-4:11`). P-Tad is P51.
  - Under (S), the ρ-tadpole is paid with no number. The (ρ+p) part remains (§3.1).
- **P62 / P100** (shear).
  - R16-13's mixed-species alternative is not lifted in the local setting (`vR16-13:25`).
  - Shape-compatibility on U is OPEN (R16-9's U branch). R17-10 [worker] finds that no constant-multiplier certificate can exist for μ_E.
- **P63(iii)** (the TT vertex as a law datum). Now also its O(q²) off-axis extension: E1 and E2 differ by O(1) on P-Z edges (`vR17-4:9`). M is excluded as a local choice (P123).
- **P70** (vacuum bridge), sharpened by R17-7:
  - (d-i) makes the residual enthalpy invisible, a bridge-specific result;
  - under (d-ii), (ρ+p)_v must vanish along the history. That takes pairing, or at least 2 tunings per species (m² and m⁴ shown, `vR17-7:30`).
  - [worker, R17-11] (d-i) is consistent and non-signalling in class 𝒟, through the unique exchange current Q_ν = ∇^μ(W h_μν). It is number-free and tracks radiative changes of W by construction. It needs P52 (receiver), P68's existence hypothesis (site congruence) and P128 (`rR17-11:267-270`).
- **P52** (site creation). [worker, R17-11] Now also the receiver for (d-i). This links W9/W10's (S) route to a Lattice price (`AX:37`).
- **P73** (e–γ). R16-10: 3 or 7 survives on the subluminal-photon subclass. On the literal class, ≤ 2 via P101, as an upper bound only (`vR16-10:19`).
- **P87** (P-Z).
  - The referee-confirmed common zero is on M (`vR16-3:13`), which is now non-local.
  - The local (U) version rests on worker-checked zeros (`rR16-3:23,263`) and the refereed U witness Z1 (`vR16-3:3`).
  - Off-axis, it now needs P122 too.
- **P88** (initial TT datum). Interlocks with P107 (§1.5) [S23 reading].
- **P92** (the law-fixed gravitating zero, = (S), C = E₀[H]).
  - **The refereed status changed.** It is a consistent, number-free added source/action principle, not "an independent exact number" (`vR17-3:17`). This narrows `vR16-6:18-28`.
  - It is conditionally viable (`vR17-7:69-70`).
  - S20's "same price as P51" is withdrawn (§5).
- **P93** (late-vacuum stability), sharpened. With SM-only extrapolation the residual would be 1.49e112–2.87e120 ρ_Λ (`vR17-7:37-40`). So (S) with P93 predicts a stabilized electroweak vacuum.
- **P94** (no branching among unequal late vacua). Unchanged under (S). (S′-start) replaces it with P94′, part of P125.
- **P96** (emergent constraint, not dressing-connected).
  - R16-11 is refereed TRANSFERS, so the dressed integer-law route is closed and P96 is what remains.
  - R17-6 identifies its signature: a pinch point in the readout.
  - It equals P-r17-6d.
- **P101** (superluminal photon). Refereed: in the literal registered class, v_max = 7.35299. n_t ≤ 2 is an upper bound (`vR16-10:16,19`).
- **P102 / P103** [worker, R16-11]. P103's escape is moot as a closure of gap 1, which `vR16-11:23` says B-inv never closed.
- **P104** (world-line boost kernel).
  - Narrowed to a presentation-dependent, bounded-angular obstruction; the kernel is homogeneous of degree −2 (`vR16-12:11`).
  - It is now one of two options; P116 is the other (`rR17-2:193`).
- **P105** (weak closure). Confirmed at leading order as weak/deformed closure (`vR16-12:5`).
- **P106** (subluminal defect modes).
  - Corrected: strict |v| < 1 is sufficient, not necessary. The condition is the absence of an active Cherenkov zero (`vR16-12:15`).
  - R17-2 restates it as "the comoving field exists".
- **P64, P90** (tower; discontinuous symbol). Unchanged. With P124 they are now the named W15 payments for free finite-band local matter (`rR17-8:286-287`).
- **P65 / P66** (E1 / E2). Both add P107. E2 also needs a sink action (`vR16-14:15`).
- **P-N1.** Unchanged: still the only known source of a light-like TT pair.

### 3.3 New prices

| # | Price (named only) | Axiom text touched | Set | What the record says it buys or costs |
|---|---|---|---|---|
| P107 | **Completion N** (R16-14 P-r16-14a). The classical metric record is sourced by the Landau–Lifshitz total stress (matter + gravitational), i.e. obeys the full Einstein equations with recorded matter. It is not a linear functional of matter records | Record readout `AX:82-83` (the metric becomes a nonlinear functional of records); source/action `AX:187` | A (E1, E2) | Formally restores β = 1. A new, uncompleted nonlinear source/action bridge: for E2 the sink action is missing, and premise (iii) is not established (`vR16-14:15`). Alternative N̄ (mean-field stress) is in tension with `AX:82-83` [worker, `rR16-14:247`]. `rR16-14:223-225` |
| P108 | **V0 + SF stipulations** (R16-13 P-R16-13a). A Wilson-Dirac TT vertex with the Wilson mass uncoupled, and a strain flow for the Dirac sea | `AX:187`; dynamics `AX:114-130` | C-box | Usable stipulations, not derived from one Belinfante lattice action; they need an ultralocal seagull (`vR16-13:5`). `rR16-13:271` |
| P109 | **The Wilson-Dirac μ_T2 row** (P-R16-13b). One more tuning per Wilson-fermion edge, or a Clifford-flat 8-component realization | None (tuning); `AX:47` for the 8-component option (as P42) | C-box | The mechanism is confirmed (H_xy = W′_xW′_y; μ_T2 = −3.53e-5 at the root). It is not a universal nonvanishing proof (`vR16-13:17`). `rR16-13:272` |
| P110 | **The Z₂-clock reading of the metric slot** (P-r17-1a): a mod-2 tensor law in place of a spin-½ link with an integer law | None directly: both present M₂(C) (`AX:47`). It is a choice of the admissibility rule's conserved structure (`AX:57-61`) and of the readout | All grid | Escapes Theorems B and B′ at the f-sum level (k⁰, k²) [ref, `vR17-1:27`]. Buys no graviton (R17-6). `rR17-1:255` |
| P111 | **Dynamics conserving the uniform strain** (P-r17-1b): hopping of invariant patterns | Admissibility, a dynamical hypothesis | All grid | k² instead of k⁰, with conserved scalar densities. The TT form is rank one (`vR17-1:16`). `rR17-1:256` |
| P112 | **Shift action of rotations at N = 2 = the R-point readout** (P-r17-1c = P-r17-6a) | Lattice `AX:37-41` (how rotations and translations act on the possibility domain; not fixed by the axioms) | All grid | On-site T₂ labels (at R: A₁+E+T₂). Equivalent to the natural action only if F_all is a Hamiltonian symmetry (`vR17-6:5`). `rR17-1:257`; `rR17-6:272` |
| P113 | **A metric readout at N = 2** (P-r17-1d): coarse-grained Z₂-flux density | Record readout `AX:82-90` | All grid | Unbuilt; nonlinear; zero linear vertex for the stated pure-character probe in a real ground state (`vR17-1:22`). `rR17-1:258` |
| P114 | **Composite (two-slot) T₂ labels at Γ** (P-r17-6b) | Record readout `AX:82-90` | All grid | Confirmed existentially (`vR17-6:5`). The readout is nonlinear in records. `rR17-6:273` |
| P115 | **Low-symmetry slot positions plus a block encoding into site qubits** (P-r17-6c) | Lattice and Qubit `AX:37-47` | All grid | Linear T₂ at Γ. Costs a superlattice for the readout. `rR17-6:274` |
| P116 | **Non-local, matter-dependent lapse/shift multipliers** (R17-2 P-W7mult) in place of B3's world-line kernel | Dynamics downstream `AX:116-130`. Gauge only if the readout is relational | C-box | [worker, suggested]. Referee: the B3 gap is real but unclosed (`vR17-2:9`). `rR17-2:190` |
| P117 | **Boundary Poincaré charges** (P-W7bdy): asymptotic charges with gravitational boundary cross terms, or edge-quantum Lorentz violation in the global algebra | Readout bridge for global charges `AX:82-83` | C-box | The global boundary algebra is unbuilt (`vR17-2:17`). `rR17-2:191` |
| P118 | **An observable-algebra readout bridge** (P-W7ro): which observables are physical, bare-local or GR-dressed | `AX:82-83`; `AX:187` | C-box (also W2) | Decides whether W7 is gauge. Referee: R13-4's operational test still stands (`vR17-2:13`). `rR17-2:192` |
| P119 | **Consistency-selection rule for final-state Λ laws** (P-r173b, b2): which history is real when a final-state rule has zero or several self-consistent ones | `AX:94` (tension); `AX:185-186` | C, C-box | Toy-demonstrated only; it does not prove every H-sensitive rule ill-posed (`vR17-3:13`). The final-state datum itself = R5-3's Λ6. `rR17-3:324` |
| P120 | **Record sourcing with re-added I** (P-r173c): fixed nonnegative additive record weights as the gravitational source | `AX:148-151,220-223` (the removed I, additivity, I(∅) = 0); `AX:79-83` | A, C | **Named, not payable as stated.** Fixed nonnegative weights cannot source radiation (`vR17-3:9`); the extra premises are not Record content. `rR17-3:325` |
| P121 | **Matter-side relaxation** (P-r173d): an H-sensitive selection of the final vacuum that finishes after the QCD step | `AX:60-61` if carried by Admissibility; `AX:185` | C, C-box | Outside 𝒦; necessary condition only; not built [worker]. `rR17-3:326` |
| P122 | **The K₆ off-axis condition** (R17-4 P-K6): ⟨K₆(f)/ε⁷⟩ = 0 on the scalar edge (U + E1), one tuning to ~1e-13. If shape cannot meet it with the axis zeros, a q²-dependent TT seagull or a vertex datum | None (dynamics, `AX:114-123`); a vertex datum is `AX:187` | C-box | One condition, not two (`vR17-4:5`). Conflict with the axis zeros strongly suggested, not certified on 𝒮. [worker, R17-10] certified on the sharp-turn slice 𝓕. P-K6′ (any shape solution needs slow-slope structure) refines it; no new number. `rR17-4:273`; `TESTS:6384-6390` |
| P123 | **Keeping R9-9's M vertex** (P-LocM): a non-summable stress kernel | `AX:57-61` (range) | C-box | Named so the cost is visible. **Not payable under a local law** (Lemma M, `vR17-4:7`; `vR16-13:27`). `rR17-4:275` |
| P124 | **Non-canonical or ξ̇-dependent shift action on matter** (R17-8 P-r178a, the residue of R17-5's P-r175a after Lemma N) | `AX:187`; `AX:116-123` (no Hamiltonian/Noether structure supplied) | C-box | Escapes Lemma N, which covers only the canonical, local-in-time, no-∂ₜξ-on-matter class (`vR17-8:7`). Unbuilt. `rR17-8:288-290` |
| P125 | **(S′-start)** (R17-7 P-r177a): C = the minimum of the starting basin, plus **P94′** (no basin change since the start) | `AX:116-130`; `AX:94` reading; `AX:185-186` | C, C-box | Causal (g ≡ 0). Adds a basin structure and a first reading, and loses positivity. Not a rescue of (S) itself (`vR17-7:42`). `rR17-7:298` |
| P126 | **The stipulated vector TT vertex** (R17-9 P-R17-9a): site-averaged Maxwell stress (c = d′) at R9-9's placement (VU), an ultralocal seagull, W1 for vectors assumed and not built, SF for the vector shear | `AX:187`; dynamics `AX:114-130` | C-box | [worker; referee running]. Local; reduces to the continuum helicity-2 amplitude; the sign is Dirac-like (`TESTS:6268-6269`). `rR17-9:281` |
| P127 | **The vector placement datum** (R17-9 P-R17-9b): VM puts the B-part of T_ij at z + ½ relative to h_ij. That means a graviton whose h_xy is not at R9-9's plaquette centres, or a non-local half-shift of h | `AX:187` (vertex datum); `AX:57-61` if it needs a non-local half-shift | C-box | [worker]. It decides "no SM zero" (VU) against "SM zero with 3 tunings" (VM). R17-12 [pending] tests whether consistency fixes it. `rR17-9:282` |
| P128 | **A non-Lagrangian partner for (d-i)** (R17-11 P-r1711c): no ultralocal action yields the lapse-independent pure pressure −W h; consistency rests on the imposed equations plus Bianchi | `AX:187` | C, C-box | [worker; referee running]. Named; not a no-go. `vR14-5:84` already notes that no action exists for the E-sector. `rR17-11:270` |

**Named gaps, not prices.**
- No vector TT vertex existed. R17-9 [worker] built one for the Maxwell field (P126). Non-abelian gluon vertices are counted as 12 Maxwell-type vectors in the free-field limit (`TESTS:6114`).
- No completed Dirac observable for W7 (`vR17-2:17`).
- No Z₂ model has been compiled into one M₂(C) per site (`vR17-1:25`).

**[S23 reading] How the price structure shifted since S20.**
- **Λ: from a number to a sentence.** P92 is no longer a counterterm in the refereed sense; it is an added principle with three conditions (P93, P70 or (d-i), and R-label records = P4).
- **The graviton: a window with a named signature.** P110 opens the f-sum; P96 (pinch points) is the dynamical price, and it is unbuilt. P-N1 is unchanged.
- **The cone: the bill grew by one row and lost one vertex.** P109 and P122 are new; P123 removes M; P87's local form rests on worker-checked zeros.
- **[worker] Vectors made the vertex placement decisive.** P127 is an O(q²) vertex datum that decides whether SM content fits on one cone. It is the third vertex-datum price, after P63(iii) and P123.
- **[worker] (d-i) moved the enthalpy price from a number to a Lattice price.** P52 and P128 replace the trace counterterm.
- **W15: almost every free finite-band generator kind is excluded.** P124 is the only unbuilt canonical-structure price.
- **The source/observable bridge is now where most prices live.** P107, P113, P114, P116–P118 and P92 all touch `AX:82-90` or `AX:187`.

---

## 4. Owner decision memo (for Jon; supersedes S20 §4; options with prices; nothing adopted)

### 4.1 The question in one line [S23 reading]

On a slower-than-light grid, what has been computed can be made to agree with relativity at a count of tuned numbers: 9 + CC on the local vertex with fermions, each held to 1e-13–1e-16. The referee calls that count bookkeeping, not proven minimal. The cosmological constant can now be removed without a number and without signalling, but only by **adding** a sentence about what weighs. The graviton still cannot be produced from the axioms' qubits by any construction on record. It has a window with a named signature and nothing built in it.

### 4.2 Options (updated)

**Option A: continuum base, discreteness only in records.**
- *Buys:* exact Poincaré, one cone, no LV tunings. Newtonian records-as-metric VIABLE (R6-4).
- *Pays:*
  - a supplied graviton;
  - to go covariant, E1 (P65 + P76 + P88) or E2 (P66), **each plus P107 (completion N)** for β (R16-14);
  - Λ by a q-charge (P54), or by (S).
- *New since S20:*
  - a metric linear in matter records fails Mercury (W17, refereed);
  - E1 and E2 tie observationally;
  - E2 additionally lacks a sink action.

**Option C: keep the four texts and tune.**
- *Buys:* no text changes.
- *Pays:*
  - the bill of §1.8: 8 + CC (scalars) to 9 + CC (with Wilson-Dirac) per class on U + E1, conditional bookkeeping;
  - P51;
  - a supplied graviton.
- *Open:* K₆ and μ_E certificates on 𝒮 (R17-10 [worker]: certified only on the sharp-turn slice); SM counts, decided by the vector placement (R17-9 [worker]; R17-12 [pending]) and μ_T2 (R17-13 [pending]).

**Option C-box: Z³, a box-exact law, qubits in a sector.**
- *Buys:* as S17/S20.
- *Pays:* S20's list, with these changes:
  - M is excluded (P123);
  - P87 on U, plus P122 off-axis;
  - P109 for Wilson-Dirac content.
- *Open:*
  - W15 (now nearly closed against free finite-band matter);
  - W7 (bulk reads as gauge; boundary algebra open).

**Option C-box-S: C-box with boson–fermion pairing per cell.**
- *Buys:* as S20, plus the pairing route to P70 (d-ii) under (S).
- *Pays:* P46 plus one of P58–P60, and still P73.

**Cosmology overlay (any option). Changed.**
- Active CMC compensation: FAIL (R15-1).
- g ≡ 0 with a stipulated constant: a counterterm (R16-6).
- **New:** g ≡ 0 with the number-free rule (S), C = E₀[H] (Q1 below).

### 4.3 Questions only Jon can answer

**Q1 (replaces S20 Q1). Λ: will you add "the law's lowest state weighs nothing"?**
- **What it is.**
  - The source of gravity is T − e₀g, where e₀ is the energy density of the law's lowest state. It costs no number: if the law's ground-state energy shifts, the subtraction shifts with it.
  - The referee rules that it is consistent, number-free and **not** a disguised tuning, but that nothing in the four texts forces it (`vR17-3:17`).
  - Written as Einstein's equation with Λ_* = −κe₀, it is local and non-signalling (`vR17-7:58`).
- **What it predicts** [ref, `vR17-7`]:
  - the leftover cosmological constant can never be negative, and is zero if our vacuum is the lowest state;
  - today's acceleration must come from something above the lowest state. It need not be temporary (`:12`);
  - DESI's phantom-like phase cannot come from an ordinary rolling field (canonical scalars only; `:14`).
- **What it needs (each named, none adopted):**
  1. **Our vacuum is the true lowest state (P93).** With Standard-Model running alone, a deeper Higgs state exists, and the rule would make our vacuum weigh 1e112–3e120 times the observed dark energy (`vR17-7:37-40`). So the rule predicts physics that stabilizes the Higgs potential. R18-2 drafts that test.
  2. **The grid zero-point's pressure is absorbed.** The rule cancels the zero-point energy, but on a grid with its own time the zero-point also has a pressure, 1.2–1.8e123 ρ_Λ per field, which one number cannot cancel (`vR17-7:21`). Three ways to pay:
     - The vacuum exchanges energy and momentum with the expansion sector (bridge (d-i)). [worker, R17-11; referee running] This is consistent and non-signalling, with no number. But it needs a "receiver": sites created as space expands, with a fixed volume per site (P52, against `AX:37`'s fixed Z³), plus a partner that no simple action produces (P128) (`TESTS:6319-6335`; `rR17-11:267-270`).
     - Pairing.
     - At least 2 tunings per species (P70).
  3. **Records do not pin sites as physical projections** (R-label, = P4). Otherwise each record costs about 2.4 Planck energies (`vR17-7:65-67`).
- **Variant (S′-start), P125.** "The bottom of the valley we started in weighs nothing" avoids condition 1 without looking ahead. It adds a basin structure and requires that the universe never changed valleys (`vR17-7:42`).
- **Your questions:**
  - (i) Would you state (S) as a principle?
  - (ii) Is "the law's lowest state" a *privileged state* under "A law privileges no states" (`AX:94`), or structure the law supplies? R17-3's worker reads it as supplied structure, like `AX:52` (`rR17-3:323`); the referee did not rule on `AX:94`.
  - (iii) For condition 2, which do you prefer?
    - site creation as the receiver (P52, `AX:37`), if vR17-11 confirms;
    - pairing (`AX:47`);
    - tunings.
  - [S23 reading] Site creation was already the grid options' Λ route (P52, `S14:183`; W10). With (S) and (d-i), it would carry the vacuum's pressure without the active compensation that R15-1 failed.

**Q2 (new). β and completion N (P107).**
- Mercury rules out every set-A route in which the metric is linear in the records of matter (W17, refereed).
- The fix is "the metric record is sourced by the total stress, gravity's own included". It works formally, but it makes the metric a *nonlinear* function of the records, and for E2 the needed sink action is not built (`vR16-14:15`).
- The worker's alternative N̄ (mean-field stress) is in tension with "only records are readable" (`rR16-14:247`).
- **Your question:** is a metric that is a nonlinear functional of records still "determined by record content alone" (`AX:82-83`) in the sense you intend?
- [S23 reading] Under N it is, only together with an initial gravitational-wave datum (Q6, P88). So Q2 and Q6 are one decision for any option with a start.

**Q3 (new). The qubit window for the graviton.**
- **What is now known.**
  - If the metric slot's qubit is read as a two-state clock with a mod-2 law (P110), R16-7/R16-11's obstruction no longer applies at the f-sum level (R17-1, refereed).
  - But no qubit model on record has exactly two gapless graviton modes.
  - A graviton made as a Goldstone mode comes with at least two extra gapless modes (`vR17-6:7-11`).
  - Any other construction in the stated regular class needs a pinch point, i.e. a static response that jumps with direction, like a Coulomb phase (`vR17-6:13,19`).
  - The one way to get that is an emergent constraint that is not a smooth deformation of an exact integer law (P96). Nobody has built one.
- **The options:**
  - (a) Keep looking in that window (R18-1 drafts a test).
  - (b) Supply the graviton (P-N1). This is against the one-site M₂(C) (`AX:47`), as before.
- **Your questions:**
  - (i) Is reading the qubit as a Z₂ clock with a mod-2 conserved structure (P110) within what you mean by Qubit plus Admissibility?
  - (ii) Is a metric readout that is nonlinear in records (P113/P114) acceptable?
  - Also note: no slot model has yet been compiled into one M₂(C) per site (`vR17-1:25`).

**Q4 (new). GW170817 on a grid (W15).**
- For free matter with finitely many bands, smooth local kernels, symmetric stress and a projectable lapse, every way of making constant shifts gauge while keeping physical, redshifting momentum has failed (R16-5, R17-5, R17-8, refereed in their scoped classes).
- A gauge-invariant graviton–matter speed comparison on a grid therefore needs one of:
  - P64 (an infinite tower per cell, `AX:47`);
  - P90 (a discontinuous momentum symbol, `AX:57-61`);
  - P124 (a non-canonical shift action, `AX:187`);
  - non-analytic or crossing-band matter, interactions, non-symmetric couplings or a non-projectable lapse (untested);
  - or accepting that the grid's GW170817 statement is a bare-cone (prescription-scoped) comparison, not a gauge-invariant one.
- **Your question:** which of these, or the last?

**Q5 (replaces S20 Q3). The cone bill after R17-4 and R16-13 (§1.8).**

| Item | Tunings (U + E1, local vertex) |
|---|---|
| Charged-matter cones (per (spin, \|q\|) class) | 3 |
| Graviton axis cone (two edge shapes) | 2 |
| Off-axis TT (one sixth-cumulant condition) | 1 |
| E_g shear | 1 |
| T₂g shear (Wilson-Dirac content) | 1 |
| Vacuum tadpole (ρ + p; non-shape) | 1, or 0 numbers under (d-i) [worker, R17-11] |
| Cosmological constant | 1, or 0 numbers under (S) |
| **Total** | **9 + CC** (13 + CC per species); 8 + CC with scalars only (refereed arithmetic). With (S) and (d-i): 8 (12) numbers plus two added rules [S23 reading on worker results] |

- **Lemma M** removes R9-9's M vertex as a local law. Every M-vertex number in R16-3, R16-9 and R16-13 belongs to a non-local vertex, including the only refereed common zero of the axis cone and the only joint zero with fermion loops.
- **[worker, R17-9] Where the photon's magnetic stress sits relative to the graviton's h_xy decides whether SM content fits on one cone.**
  - At R9-9's placement: no.
  - Half a cell over (P127): yes, with 3 edge tunings, except the T₂g shear of the Wilson fermions (+0.106).
  - R17-12 tests whether consistency forces one placement; R17-13 tests whether the leftover can be zeroed.
  - If the placement is free, it becomes your choice of law datum.
- **Your questions:**
  1. Is a bill of about nine numbers at this precision acceptable for keeping all four texts? (carried)
  2. Per class (3) or per species (7)? (carried)
  3. Is choosing the local U-type vertex and its E1 extension a structural choice you would make (P63(iii))? E2 adds one row. If R17-12 returns FREE, the same question applies to the vector placement (P127).
  4. For Wilson-Dirac fermions, one μ_T2 tuning per edge, or 8-component fermions per site (P109, `AX:47`)?
  5. Is lattice-scale superluminality excluded for the photon too (P101; carried)? The refereed literal class allows it.

**Q6 (carried; S20 Q2). The initial gravitational-wave datum (P88).** Unchanged, but now tied to Q2 [S23 reading].

**Q7 (carried). E1 or E2.** Observationally tied (R16-14). Both need P107. E2 also needs a sink action.

**Q8 (carried). Edge-shape tuning; pairing per cell (`AX:47`); site creation (`AX:37`); a law that reads only changes in stress (`AX:94`); range (box tails, W7's 1/r², P90's 1/n tails); sector selection (P45).**

### 4.4 Open in every option

- **Producing the graviton.**
  - Window: Z₂ pinch-point phases not dressing-connected (P96).
  - Also open: finite-response k⁰ f-sums, non-strict V/S continua, degenerate grounds (`vR17-6:19`).
- **Λ without an added principle.** The bounded obstruction is refereed (`vR17-3:19`).
- **GW170817 as a gauge-invariant test on any grid** (W15).
- **W7's degree-3 boundary algebra and Dirac observables.**
- **The full tuning count:** K₆ and μ_E certificates, SM counts, vector vertices.
- **N ≥ 3 tails** (R11-6) and **the body quadrupole** (P56).

---

## 5. Dated corrections (this period; dated 2026-10-13)

| Correction | What it was | What it is now | Source |
|---|---|---|---|
| **M-vertex numbers** in R16-3, R16-9, R16-13 | Local bare-cone numbers for R9-9's M vertex; R16-3's referee-confirmed common zero is M at m = 0.1 | M has no absolutely summable doubler-free realization, so these numbers belong to a non-local vertex. R16-3's REFUTED stands via U; R16-9 stays OPEN via U; R16-13's only root is non-local | `TESTS:6178`; `vR17-4:7`; `vR16-13:25,27` |
| **R16-12's "non-local H′"** | The undressed H′ is non-local (`rR16-12:226`: "non-local H′ = H + {W, H₀}"; quoted at `TESTS:5989`) | H′ ≈ H₀. Its off-shell non-locality is constraint-proportional (gauge multipliers), so conditionally gauge. The literal off-shell statement is not overturned | `TESTS:5989`; `vR17-2:7` |
| **R16-9's μ_T2 = 0** | "T₂g shear 0 at one loop" (`S20:260`; `TESTS:5682`) | Wilson-Dirac seas give μ_T2 ≠ 0 (−3.53e-5 at R16-13's root). The zero was coupling- and content-specific | `vR16-13:17` |
| **R17-3 TUNING** | Worker reading TUNING; Theorem T as a trichotomy (`TESTS:5907-5920`) | OPEN. Theorem T is not proved (H-an makes V analytic, not Γ). (S) is number-free, not "an independent exact number" | `TESTS:6007-6016`; `vR17-3:5,17` |
| **R17-5 runner import** | The committed runner imported `r99_profiles_copy` from a non-archived path (ModuleNotFoundError) | Profile file copied beside it, path corrected; the rerun matches the stored output | `TESTS:6264`; `rR17-8:8` |
| **S20: "W10 collapses onto P51"** | P92 = Lemma PT's counterterm, "the same price as P51"; the overlay offers nothing beyond P51/P54 (`S20:89,230,287,407,460`) | (S) is a consistent, number-free added principle, conditionally viable. `vR16-6`'s "counterterm" stands only in the sense "unforced" | `vR17-3:17`; `vR17-7:69-70` |
| **S20's Theorem NA reading** | "The final vacuum's energy must be a law constant; making gravity ignore it is the tuning" (`S20:230`) | The law constant can be fixed with no number, as E₀[H]. NA still excludes causal cancellation across unequal late vacua without a pre-branch label | `vR17-3:17,19` |
| **S20 W3: the common zero** (a status change, not an error; `S20:156` named M correctly) | "Two shape tunings zero E_g and T₂g together [ref]" (`S20:69,280`) | The refereed zero is on M, which is now non-local. U zeros are worker-checked (`rR16-3:23,263`) | `vR16-3:13`; `vR17-4:7` |
| R16-10 minimality | "n_t = 2 (convention-independent minimum)" (`TESTS:5569`; `S20:117`) | A checked upper bound n_t ≤ 2. "Any real equation" is not convention-independent. COUNTED not met | `vR16-10:19` |
| R16-10 Theorem L scope | "No log, class-wide" | Named families with integrable valleys; λ = 0 as a boundary value; m² log m not excluded | `vR16-10:3` |
| R16-11 B-inv | "Excludes EH for any local invariant readout with a nonzero vertex" (`TESTS:5616`) | An O(1) lower bound on total susceptibility only. It does not exclude an EH IR pole without a readout and spectral-isolation bridge. Gap 1 is not closed | `vR16-11:23` |
| R16-11 floor and 20 slots | An approximate floor; "the smallest invariant qubit hop flips 20 slots" | The floor is not small thermodynamically; 20 is shown in 4³–8³ boxes only | `vR16-11:13,31` |
| R16-12 B3 and population | "Unbounded" world-line kernel; Lemma C "every defect mode must be subluminal"; ≥ 1.7e19 GeV | Kernel homogeneous of degree −2, only its angular factor unbounded; presentation-dependent. Strict \|v\| < 1 sufficient, not necessary. Infimum 1.431782/a = 1.748e19 GeV; negligible only for thermal ensembles | `vR16-12:11,15,19` |
| R16-13 LIFTED and numbers | LIFTED with 3 tunings; μ_E values | OPEN (M non-local; μ_T2 ≠ 0; no SM counts). μ_E about 1% underconverged; width fraction frozen; linear mass drift | `vR16-13:15,23,25` |
| R16-14 PASS and numbers | "PASS for both with completion N"; Mercury 57.5 / 50.3″/cy; "exactly PPN"; 3.5-decade margin universal (`TESTS:5875-5884`) | OPEN and tied; N is a new nonlinear bridge. 57.3067 / 50.1433″/cy (fail by 3.679 / 3.378 decades). E2 "exactly PPN" too strong. The margin holds for a weak-field spheroid only | `vR16-14:5,11,13,15,21` |
| R17-1 quantifiers | "Every Z₂-invariant hop of weight < 20 has no integer lift"; "every stoquastic ground state"; k² bound | Tested boxes only (big-M MILP unreliable as a certificate). Real/Perron ground state only. Generic directions and polarizations, rank one | `vR17-1:13,16,22` |
| R17-2 O_F and R13-4 | "O_F is bulk-invariant"; "R13-4's criterion is not a valid gravity control" (`TESTS:5992`) | O_F is invariant only under the dressed linear constraints (TT counterexample −1/2). R13-4's operational test is not invalidated | `vR17-2:13` |
| R17-4 reading | "COUNTED-ROWS in part" (`TESTS:5940`) | COUNTED-ROWS for U + E1 (the literal second clause) | `vR17-4:13` |
| R17-5 scope | Lemma R from proper rotations; "the only route left" | Needs a continuous SO(3). "Only" holds only while free/symmetric/projectable are kept | `vR17-5:11,15` |
| R17-6 representation and Lemma R | Expectation "a representation obstruction for the natural action" (`TESTS:5986`); Lemma R for "every equal-weight CSS/RK state"; Z′ forces both partners | No general obstruction (T₂ at R, in pair labels, in low-symmetry orbits). Lemma R exact only for full-coset-uniform states. Z′ forces partners only in the nonzero irrep | `vR17-6:5,13,15` |
| R17-7 claims | "Acceleration temporary"; "phantom not reproducible"; "one tuning per order per species"; "(S′-current) breaks Bianchi in every local form" (`TESTS:6130-6138`) | Need not be temporary (w = −0.864 attractor); canonical scalars only; shown through m⁴ only; only without a local carrier | `vR17-7:12,14,30,50` |
| R17-8 Jordan and FD | "Φ annihilates the Jordan-chain parts"; FD "exactly on shell"; Theorem W (iii) | False as written (the generalized vector may survive); first order with an O(q²) remainder; (iii) repaired by analytic continuation plus the tame Reeb theorem | `vR17-8:13,19,23-29` |
| SUMMARY §26 labels (carried from S20) | R15-4, R15-6 listed as worker results | Both refereed | `TESTS:5301-5324` |

Carried, still in force: S20 §5 and S17 §1.8.

---

## 6. Calibration [S23 reading]

### 6.1 S20's round-17 expectations (`S20:659,696,726,756-759,782`)

| Item | S20 expectation | Refereed outcome | Calibration |
|---|---|---|---|
| R17-1 | WINDOW at the f-sum level; the obstruction moves to "whether any gapless Z₂ tensor phase exists" | WINDOW; EXTENDS refuted. R17-6 then found the obstruction in dynamics | **Right**, including the moved question |
| R17-2 | PHYSICALLY NON-LOCAL in principle and unobservable, or OPEN; "invariant content likely real" | OPEN. The bulk term is canonically a GR dressing; no physical bulk interaction is shown | **Reading right, physics lean wrong.** The Coulomb-gauge analogy pointed to gauge, not to physical non-locality |
| R17-3 | TUNING; "a refereed 'tuning or acausal' theorem" | OPEN. (S) is a number-free third option | **Wrong.** The registered disjunction had no slot for a number-free rule. S20's own Theorem NA reading made the same omission |
| R17-4 | COUNTED-ROWS with two further shape conditions; CONFLICT the alternative; (f) CERTIFIED-CONFLICT for M | COUNTED-ROWS with **one** further condition (K₆); tadpole non-shape; M non-local (Lemma M); (f) OPEN | **Reading right, count wrong, M moot.** Lemma M was unanticipated |
| R17-5 | EXCLUDED-MB or OPEN; "labels bands rather than carrying kinetic momentum" | EXCLUDED-MB, for exactly that reason | **Right** |

**Score.** Three of five right in reading (R17-1, R17-4, R17-5), one right in reading only (R17-2), one wrong (R17-3). S17's round-16 score was one in five (`S20:577`).

### 6.2 Supervisor-registered items, for the wrap-up record

| Item | Expected | Outcome |
|---|---|---|
| R16-10 | COUNTED for scalars, OPEN for Dirac (`TESTS:5476`) | Dirac REFUTED-ZERO (literal) / OPEN (subluminal); scalar OPEN. **Reversed** |
| R16-11 | TRANSFERS (`TESTS:5513`) | TRANSFERS [ref]. **Right** |
| R16-12 | NON-LOCAL in the class, population-suppressed (`TESTS:5549`) | OPEN; B3 presentation-dependent. **Wrong** on the reading |
| R16-13 | LIFTED with one more tuning (`TESTS:5613`) | OPEN; the sign is right (D1 vs G), the lift is non-local. **Wrong** on the reading |
| R16-14 | Both PASS; likeliest failure α₂ for E2 (`TESTS:5651-5653`) | OPEN and tied; the failure was β (nonlinear source), not α₂. **Wrong** on the location |
| R17-6 | OPEN; representation obstruction plus an unresolved shift class (`TESTS:5986`) | OPEN; no representation obstruction; dynamical OBSTRUCTED in two bounded classes. **Reading right, mechanism wrong** |
| R17-7 | OPEN with three conditions: (b) E₀ includes the zero-point; (c) needs SM stabilized; (d) needs a global constant (`TESTS:6044-6047`) | OPEN. (b) was the wrong condition (the live one is the enthalpy); (c), (d) right. **Two of three** |
| R17-8 | EXCLUDED-MIX by a winding argument (`TESTS:6087`) | OPEN. The winding argument holds for isolated analytic bands after repair. **Mechanism right, reading wrong** |
| R17-9 | OPEN; vector sign "boson-like", adding to the scalar side (`TESTS:6128`) | [worker] OPEN, but the vector sign is Dirac-like (E–B interference). **Reading right, sign premise wrong** (referee running) |
| R17-11 | SIGNALS (`TESTS:6250`) | [worker] CONSISTENT in 𝒟. **Wrong**, if the referee confirms. The removed hypothesis (separate vacuum conservation) mattered less than the receiver (√h fixed per site), which the expectation did not consider |
| R17-10 | CERTIFIED-CONFLICT for K₆ at m = 0.01, if the margins beat the relaxation gap; OPEN for μ_E (`TESTS:6226-6228`) | [worker] K₆: certified only on the sharp-turn slice; the relaxation gap (70–80× the margin) did not close. μ_E OPEN. **The conditional came out the other way for K₆; right for μ_E** |
| R17-12, R17-13 | FREE at O(q); SIGN-DEFINITE | [pending] |

**Pattern.**
- Four of the five round-16 misses expected the obstruction where the previous no-go had put it: R16-12 in boost non-locality, R16-14 in preferred-frame α₂, R16-13 in the shear sign, R16-10 in the scalar sector.
- In fact it moved to a presentation, a bridge or a vertex choice: B3 is presentation-dependent; β needs a nonlinear source; M is non-local; the Dirac zero needs a superluminal photon.
- Round 17 repeated the pattern twice:
  - R17-9's answer turned on an O(q²) vertex placement;
  - R17-11's on which equation is left unimposed.
- **Lesson for round 18:** when the governing no-go's hypotheses include a presentation, a bridge or a vertex datum, expect OPEN plus a new owner question, not a cleaner no-go. Each expectation below says which kind of hypothesis it removes.

---

## 7. Draft round-18 pre-registrations (readings fixed before any run)

**Rules (as rounds 2–17, `TESTS:5688-5706`).**
- Probes on Opus 5.5 at xhigh. Every FAIL, EXCLUDED, OBSTRUCTED or no-go goes to codex gpt-5.6-sol (xhigh) before it is recorded.
- Prices are named, never adopted. Prior art is grepped first and counted once. Hypotheses come before titles. Numbers from memory are labelled RECALLED.
- Every law states its whole-zone v_max, gauge fields included.
- Every count states its counterterm basis.
- Every Λ mechanism says what is enforced and what is stipulated.
- Controls must measure the same observable. Every finite-slot claim names its readout bridge. Forks list their exclusions. Memory claims say generic-GR or model-specific. Expectations name the removed hypothesis.
- **New (from round-17 verdicts):**
  - **Locality of vertices.** Every TT or stress vertex states whether it satisfies the C₂-covariance zero of Lemma M (`vR17-4:7`), or is labelled non-local.
  - **Number-free ≠ forced.** A Λ result distinguishes "no number" from "forced by the four texts" (`vR17-3:17`).
  - **Bounded classes for spectra.** "Gapped" means a uniform spectral gap, multiparticle continua included (`vR17-6:13`).
  - **Certificates.** Any CONFLICT claimed from a relaxation states its enclosure method in advance, as R17-10 did (`SP/R17-10/METHOD.md`).

**Timing.** Each item is sized for about 75 minutes of worker time. The campaign starts no new probes after 09:57Z and ends at 10:57Z.

**Overlap check.**
- R17-9 covers the vector TT vertex and the SM-count solve.
- R17-12 covers the vector placement (VU vs VM), including vector Lemma-M covariance.
- R17-13 covers the Wilson-Dirac μ_T2 row.
- **No R18 item drafts R17-12's or R17-13's questions.**
- R18-3 covers only two things those items leave out: the Dirac TT vertex's own locality (a Lemma-M test for V0), and a certificate for R17-9's VU conflict. It launches only if R17-12 does not return FORCED-VM.
- R17-10 covers the K₆ and μ_E certificates for scalars on U; no R18 item repeats them.
- R17-11 covers bridge (d-i). R18-2 covers P93 (vacuum stability), a different condition of (S).
- R17-6 covers representation theory and Theorems G/Z. R18-1 covers the static pinch-point test and Theorem Z's k⁰ gap, both left open by `vR17-6:19`.

**Priority.**
1. R18-1 (graviton) and R18-2 (Λ), in parallel.
2. R18-3 (SM content on one cone), after R17-12's worker reading.
3. R18-4 (W15) only if time allows, after nothing else is pending.

---

**R18-1. The Z₂ window's signature: does any local Z₂ tensor ensemble with suppressed γ-charges show a pinch point, and does Theorem Z's k⁰ gap close?**

- **Plain question.**
  - R17-1 (refereed WINDOW): reading the qubit as a Z₂ clock escapes the k⁴ f-sum bound.
  - R17-6 (refereed OPEN; OBSTRUCTED in two bounded classes): two gapless helicity-±2 branches with strict V/S gaps need a pinch point in the readout's static response, unless the f-sum is in the k⁰ finite-response gap.
  - Identity V says the pinch point needs the mod-2 law's even γ-charges (Gn = 2γ) suppressed at long wavelength faster than k². Lemma R says states uniform over the full coset have white-noise labels (`vR17-6:15`).
  - Two questions:
    1. Does any local, cubic-covariant Z₂ ensemble that penalizes γ-charges have a pinch point at nonzero γ-density, or only in the exact integer-law limit (which R16-7/R16-11 already cap)?
    2. Can Theorem Z be extended to a k⁰ f-sum with a finite TT response?
- **Setting.**
  - N0914's slots, mod-2 law.
  - Rokhsar–Kivelson-type states with amplitude ∝ exp(−βU Σ_x |γ(x)|²/2). Their equal-time correlations equal a classical ensemble. This is an RK identity, stated as the readout bridge for "static response" here, not a general one.
  - Moves: R17-1's minimal Z₂-invariant cube patterns, which preserve Gn mod 2. Metropolis on L = 6–12 periodic, plus L = 16 if time allows.
  - Observables: the E⊕T₂ structure factors S_TT, S_V, S_S, and the γ structure factor, along the axis, face and body directions.
  - βU ∈ {0, 0.5, 1, 2, 4} plus the βU = ∞ sector (Gn = 0, 0/1 occupations).
  - Excluded: spectra and dynamics; integer-law lifts; non-local moves; degenerate or symmetry-broken grounds (`vR17-6:19`).
- **Prior art (count once):**
  - R17-6 and vR17-6 (Theorems G, Z, Z′ corrected; Identity V; Lemma R narrowed);
  - R17-1 and vR17-1;
  - R16-11 and vR16-11 (the dressing cap);
  - R16-7; N0914's stencil;
  - classical Coulomb-phase pinch points with charge fugacity (Henley; Castelnovo–Moessner–Sondhi; comparators, RECALLED);
  - rank-2 U(1) four-fold pinch points (Prem–Vijay–Chamon; Pretko; comparators, RECALLED).
- **Removed hypothesis.** Lemma R's uniform (full-coset) weight. Kept: locality, finite fugacity, the mod-2 law.
- **Probes.**
  - (a) Build the cube-flip MC. Check detailed balance, and ergodicity within the mod-2 sector, by exact enumeration at L = 2–3 where feasible.
  - (b) At each βU, measure the three readout structure factors and S_γ.
    - A pinch point means the k → 0 limit depends on direction, with the width set by finite size.
    - Report the fitted width ξ⁻¹(βU) and its scaling with L.
  - (c) Is ξ(βU) finite at every finite βU (screening by γ-charges), or is there a βU_c beyond which ξ = ∞ at nonzero γ-density?
  - (d) Analytic. Extend Theorem Z to the k⁰ f-sum class with a finite TT response (e.g. through m₃ or the Goldstone counting), or exhibit the obstruction to extension.
  - (e) Prices.
- **FIXED readings.**
  - For (a)–(c):
    - **PINCH-PRESENT:** a finite-βU ensemble with nonzero γ-density whose readout has a pinch point, consistent with ξ = ∞ under finite-size scaling to the largest L run. Checked. This is evidence for the window at the static level, not production.
    - **SCREENED:** at every finite βU tested, ξ(βU) is finite and fitted; only βU = ∞ is sharp. Checked. This is evidence that the static window needs exact emergence, which is P96 at a phase boundary.
    - **OPEN:** otherwise.
  - For (d):
    - **GAP-CLOSED:** a refereed extension of Theorem Z to the stated k⁰ finite-response class;
    - **OPEN:** otherwise.
- **Expectation.** SCREENED, and (d) OPEN.
  - Classical charge fugacity screens Coulomb-phase pinch points into Lorentzians of width ~ (γ-density)^{1/2} (comparator, RECALLED).
  - The removed hypothesis is uniform weighting, but finite fugacity keeps charges at nonzero density.
  - If SCREENED holds, the Z₂ window narrows to an exact-emergence critical point or a first-order boundary.
  - The likeliest failure is an MC ergodicity problem in the βU = ∞ sector.

---

**R18-2. (S)'s sharpest prediction: must the electroweak vacuum be the true minimum, and is that consistent with the measured inputs?**

- **Plain question.**
  - vR17-3 rules that (S), "the law's lowest state weighs nothing", is a consistent number-free principle.
  - vR17-7 finds it conditionally viable, but only with P93: our vacuum must be the global minimum. SM-only extrapolation would leave 1e112–3e120 ρ_Λ (`vR17-7:37-40`). That turns (S) into a test of particle physics.
  - Within the SM, with measured m_t, m_h and α_s (RECALLED, labelled), is the electroweak vacuum absolutely stable within stated uncertainties?
  - If not, can the lattice at a = ℓ_P stabilize it?
  - If not, what minimal content stabilizes it, and is that a tuning under rule `TESTS:5700` or a content choice?
- **Setting.**
  - Two-loop SM RGEs for λ, y_t and g₁₋₃ (three-loop results as RECALLED comparators). MS-bar matching at m_t with stated threshold corrections (RECALLED, labelled).
  - Effective potential at the stated loop order; instability scale and λ_min.
  - Lattice terms: Planck-suppressed φ⁶/Λ² with Λ = 1/a = M_P, and the box law's dispersion near k ~ 1/a.
  - One stabilizer family: a real singlet with a Higgs portal (tree-level threshold mechanism; RECALLED).
  - (S′-start) as the comparison.
  - Excluded: anthropic selection; landscape branching (P94); active compensation.
- **Prior art (count once):**
  - R17-7 and vR17-7; R17-3 and vR17-3; P93 and P125;
  - Buttazzo et al. 2013 and Degrassi et al. 2012 (comparators, RECALLED; cited in `vR17-7:40`);
  - the singlet-threshold stabilization literature (comparator, RECALLED).
- **Removed hypothesis.** R17-7's SM-only content.
- **Probes.**
  - (a) Reproduce λ(μ), the instability scale and the absolute-stability bound on m_t at the stated order. Compare with the RECALLED published bounds.
  - (b) With the RECALLED m_t average and uncertainty, including a labelled pole-mass ambiguity, state the tension in σ.
  - (c) Can φ⁶/M_P² or the lattice's own dispersion make the electroweak vacuum the global minimum? State the field values involved, against the instability scale.
  - (d) The minimal singlet window (m_S, λ_HS, λ_S) that gives absolute stability up to 1/a, while keeping (S)'s Λ̃ ≥ 0 and no deeper minimum. Say whether any parameter must be held to better than O(1) (a tuning) or not (a content choice).
  - (e) Prices and counting convention.
- **FIXED readings.**
  - **SM-STABLE:** SM-only absolute stability within 2σ of the stated inputs. Checked. (S) then adds no particle-physics price.
  - **NEEDS-STABILIZER:** SM-only metastability beyond 2σ, plus an explicit stabilizer, content stated, that makes the electroweak vacuum the global minimum below 1/a. Checked.
  - **LATTICE-STABILIZES:** a lattice-scale term at a = ℓ_P alone suffices. Checked.
  - **OPEN:** otherwise. An EXCLUDED-for-(S) reading would need a refereed proof that no stabilizer in a stated class works.
- **Expectation.** NEEDS-STABILIZER.
  - SM-only metastability is a 2–3σ tension (RECALLED).
  - Lattice-scale operators cannot act at the 1e10–1e11 GeV instability scale.
  - A singlet threshold stabilizes over an O(1) window, so it is content, not a tuning.
  - The likeliest failure is that RECALLED inputs make (b) inconclusive at 2σ, which gives OPEN.

---

**R18-3. SM content on one cone under the local placement: is the Dirac TT vertex local, and can R17-9's VU conflict be certified?** *(Launch after R17-12's worker reading, and only if it is not FORCED-VM. The readings are fixed now.)*

- **Plain question.**
  - R17-9 [worker] finds the outcome turns on the vector placement. At R9-9's placement (VU), two conditions are incompatible on every sampled law:
    - the T₂g row needs Ξ_γ,T2g ≤ 6e-4 per vector;
    - offsetting the Dirac birefringence (≥ +2.6e-3 per field, `rR16-13:200`) needs Ξ_γ,Eg − Ξ_γ,T2g ≥ 4.46e-3 (`TESTS:6270-6272`).
  - R17-12 asks whether consistency forces VU. If it does, or if the placement is free, the in-setting answer at VU rests on samples. Two questions are left that neither R17-12 nor R17-13 asks:
    1. Is R16-13's V0 Dirac TT amplitude itself local in Lemma M's sense? Every Dirac number since R16-13 uses it.
    2. Can the VU conflict be certified by class bounds — a lower bound B_min on the Dirac birefringence over subluminal Wilson-Dirac edges, and an upper bound on the VU vector's Ξ_γ,Eg − Ξ_γ,T2g over subluminal photon edges — so that 22.5·B_min exceeds what 12 vectors and one Higgs edge can supply?
- **Setting.**
  - Dirac: separable Wilson-Dirac edges with Lemma V1 subluminality, the V0 vertex, SF strain and an ultralocal seagull.
  - Vectors: R17-9's VU vertex (P126) on subluminal photon edges in R17-9's family, with stated regularity.
  - Scalars: one Higgs edge on the U vertex (R17-4's class).
  - Axial q, m ≤ 0.01, one loop, the supplied zero-point vacuum. SM counts: 4 + 22.5 + 12.
  - Excluded: VM (R17-12's subject); μ_T2 (R17-13's subject); the M vertex; pairing; superluminal edges.
- **Prior art (count once):**
  - R17-9 (worker; its referee, when back);
  - R16-13 and vR16-13 (Theorem DT, Lemma V1, V0 as a stipulation);
  - R17-4's Lemma M and `vR17-4:7`;
  - R16-3's IBP identity;
  - R17-10's certification method (`SP/R17-10/METHOD.md`), as the template for any enclosure.
- **Removed hypothesis.** Sampling: class bounds replace sampled laws. Kept: the VU placement, V0, SF.
- **Probes.**
  - (a) The Lemma-M test for V0. Does the Dirac T₂g pair amplitude vanish where proper C₂ᵧ covariance and periodicity require it on doubler-free Wilson edges? A proof either way.
  - (b) A closed form for the Dirac birefringence B through Theorem DT's IBP, and a lower bound B_min on the class, or a law with B ≤ B_crit (the value that would let VU close).
  - (c) An upper bound on the VU vector's Ξ_γ,Eg − Ξ_γ,T2g over the stated photon class, with the T₂g row's constraint imposed.
  - (d) The certified inequality at SM counts, or an explicit point that breaks it.
  - (e) Prices.
- **FIXED readings.**
  - **V0-NONLOCAL:** a proof that V0 violates the covariance zero, so the local Dirac class needs a different vertex. Checked, then refereed.
  - **VU-CERTIFIED-CONFLICT:** a refereed certificate, with the method stated in advance, that no content in the stated class meets Ξ_Eg = Ξ_T2g = μ_E = 0 at SM counts under VU.
  - **VU-ZERO:** an explicit SM-count law under VU, all edges subluminal and local, with Ξ_Eg = Ξ_T2g = μ_E = 0 at a common light mass. Checked.
  - **OPEN:** otherwise.
- **Expectation.**
  - (a) Undecided, with a lean to V0-NONLOCAL.
    - The Wilson part enters through W′, which vanishes at k = π for (1 − cos k)-type terms.
    - The kinetic part's derivative s′ need not vanish there: for sin-type edges s′(π) = −1.
    - Whether V0's T₂g amplitude obeys the covariance zero depends on how V0 combines them. A second Lemma M is a live outcome.
  - (b)–(d) OPEN or VU-CERTIFIED-CONFLICT for the birefringence row. The sign mechanism (H_xy = W′_xW′_y, `vR16-13:17`) is fixed, but a certified vector bound over a continuous photon family may not fit in 75 minutes.
  - Removed hypothesis: sampling only. Kept: the vertex stipulations, which (a) tests.

---

**R18-4. W15's last free finite-band holes: crossing bands and merely continuous multi-shift mixing.** *(Launch only if time allows.)*

- **Plain question.** vR17-8 confirms scoped no-gos for finite mixing (analytic symbols), canonical altered generators, and regular linear field-dependent generators on isolated analytic bands. It names its steelman as "an analytic crossing-band or joint mixing/field-dependent completion" (`vR17-8:35`). Does a symmetry-protected band crossing let a field-dependent generator carry rank-3 C, so that the Reeb rank bound ≤ 1 fails?
- **Setting.**
  - Two-band analytic Bloch Hamiltonians on T³ with a symmetry-protected crossing surface or line.
  - Free quadratic matter, symmetric stress, projectable lapse, R9-9's N-type graviton.
  - Field-dependent canonical generators as in R17-8, with H-RB as the redshift bridge.
  - Excluded: interactions; non-symmetric couplings; non-projectable lapse; P64; P90.
- **Prior art (count once):** R17-8 and vR17-8 (Lemma N, MIX-1/2, FD, Theorem W repaired); R17-5 and vR17-5; R16-5; the tame Reeb-graph facts as cited in `vR17-8:29`.
- **Removed hypothesis.** Isolated bands.
- **Probes.**
  - (a) The equal-energy identity across a crossing: does the analytic-continuation step of `vR17-8:25-29` survive along the crossing branches?
  - (b) Construct the best crossing-band candidate and test rank C, then the redshift test.
  - (c) Prices.
- **FIXED readings.**
  - **ESCAPE:** an explicit crossing-band law with W2_pf, nonzero physical momentum and correct redshift. Checked.
  - **EXCLUDED-CROSS:** a refereed no-go for the stated crossing-band class.
  - **OPEN:** otherwise.
- **Expectation.** EXCLUDED-CROSS for symmetry-protected crossings. The union of analytic branches still lives on T³, and the winding obstruction is topological. The main alternative is OPEN, if the branch continuation fails at the crossing set.

---

## 8. Draft of the 10:20Z wrap-up (as complete as possible at about 01:48Z)

### 8.1 Plain-words section for SUMMARY (proposed §27)

> ## 27. Campaign C5, rounds 16–17: a number-free Λ rule, a qubit window for the graviton, and a bill with one vertex removed (2026-10-12/13)
>
> **What these rounds did.** Rounds 16–17 asked whether the remaining walls could be closed by proof or by counting. There were 27 probes: 14 in round 16 and 13 in round 17. By 01:40Z, 22 had verdicts from a codex gpt-5.6-sol referee. The probes and every synthesis are Claude Opus 5.5, the same model family.
>
> **The cosmological constant.**
> - Making gravity ignore a fixed number is a tuning, and the four axiom texts do not force any rule that removes Λ (refereed, R16-6, R17-3).
> - But one rule needs no number: "the law's lowest state weighs nothing". The referee rules it consistent and not a disguised tuning. It would have to be **added**; it does not follow from the axioms (R17-3).
> - If added, it predicts:
>   - that our vacuum is the true lowest state, so the Higgs potential must be stabilized by physics beyond the Standard Model;
>   - that dark energy is something above the lowest state, never a negative constant (R17-7, refereed OPEN).
> - It also needs:
>   - the grid vacuum's pressure to be absorbed by an exchange with the expansion, or cancelled by pairing. The exchange worked without signalling in the worker's check, but it needs sites to be created as space expands; its referee is still running (R17-11);
>   - records that do not act as physical projections.
>
> **The graviton.**
> - Reading each qubit as a two-state clock escapes the earlier proof that finite slots cannot give Einstein's stiffness (refereed, R17-1). The explicit models found are not gravitons.
> - Theorems in two bounded classes show the price (R17-6, refereed OPEN):
>   - a graviton built as a Goldstone mode brings extra gapless modes;
>   - any other construction in the stated class needs a "pinch point" in its static response.
> - No such qubit model exists on record. A supplied graviton is still the only known source.
>
> **One light cone for everything.**
> - One of the two graviton–matter vertices used since round 9 (M) turned out to be non-local (Lemma M, refereed). The other (U) keeps the earlier refutation.
> - The off-axis graviton speeds cost one more condition, and the vacuum's pressure term cannot be shaped away (R17-4, refereed).
> - Fermion loops pull the shear the opposite way, but the only joint zero used the non-local vertex, and Wilson fermions add a new shear row (R16-13, refereed OPEN).
> - Photon loops push the cone the same way fermions do. Whether the Standard Model's particle content then fits on one cone depends on a half-cell choice of where the photon's magnetic stress sits: no at the original placement, yes at the shifted one, apart from one shear row (R17-9, worker; referee running). Two follow-ups are running.
> - The conditional bill is about 9 tuned numbers plus the cosmological constant, each to 1e-13 to 1e-16. It drops by one if the vacuum-exchange rule holds.
>
> **Comparing graviton and light speeds on a grid (GW170817).** For free matter with finitely many bands, every way tried of making that comparison gauge-invariant fails (R16-5, R17-5, R17-8, refereed in their classes). What is left: an infinite tower per cell, a discontinuous momentum, a non-canonical shift action, or untested interacting or crossing-band matter.
>
> **Set A.** A metric that depends linearly on the records of matter fails Mercury's perihelion by more than three decades (R16-14, refereed). Fixing it needs gravity's own energy in the source, a new nonlinear bridge.
>
> **The off-box tail (W7).** Its bulk part is, at leading order, gravity's own Coulomb-type field written in lattice variables (R17-2, refereed OPEN). Whether anything physical is left depends on which observables count.
>
> **Status.**
> - Nothing was adopted.
> - Four new owner questions:
>   - the Λ principle;
>   - the nonlinear source;
>   - the qubit reading of the metric slot;
>   - how to treat GW170817 on a grid.
> - Pending at close (as of 01:47Z): the referees of R17-9, R17-10 and R17-11; the workers R17-12 and R17-13; any round-18 item.

### 8.2 PRICE_NOTE v7 delta (proposed): campaign C5's prices, P15–P128 (named; none adopted)

**Status line (replace `PRICE_NOTE:3`).** "DRAFT v7: v6 plus campaign C5's ledger P15–P128 (syntheses S5–S23). Every price is named, none adopted. Prices refereed as FAIL or non-local (P74, P120, P123) are listed so the owner can see them; they are not payable under the registered readings."

**Rows.** Format: price — axiom text touched — source. "None" means a dynamical or tuning choice that the axioms leave downstream (`AX:114-130`).

*Rounds 1–14 (from S5–S17 tables).*
- P15 Exact Z⁴ Ward identity needs an infinite one-particle fibre — Qubit `AX:47` (one-particle reading) — `S5:253`
- P16 Lorentz-random lattice (Haar-random Poincaré frame of L₇) — Lattice `AX:37-41`; Admissibility `AX:57-58` — `S5:254`
- P17 Retarded, infinite-orbit law in place of one nearest-neighbour rule — Admissibility `AX:57` — `S5:255`
- P18 LRL particles off the qubit fibre (multi-site or dissipative matter) — Qubit `AX:47` — `S5:256`
- P19 LRL graviton tunings (5, plus b = −2a) — none — `S5:257`
- P20 Non-positive or non-local sourced weight in set B — Admissibility `AX:60-61` — `S5:258`
- P21 Set B records: boundary-only formation, or non-RP / probabilistic permanence — Record `AX:77-80` — `S5:259`
- P22 Set A gravity–record coupling (compensator, foliation, …) — none directly — `S5:260`
- P23 Everpresent-Λ premises — Lattice `AX:37`; Record `AX:79-80` — `S5:261`
- P24 Discontinuous covariant event rule on LRL (Theorem Q) — Admissibility `AX:60-61`, via a bridge — `S8:227`
- P25 Frame superselection — a new primitive; arguably `AX:82` — `S8:228`
- P26 Box-confined Poincaré matter law (non-analytic hopping, local boost covariance, graded composition) — `AX:116-130`; `AX:47` for (c) — `S8:229`
- P27 Edge sector (unpopulated gravitating edge, gapped edge, …) — none; (c) `AX:47`, `AX:37-41` — `S8:230`
- P28 Loop protection (custodial vertices) — none (a named conditional, `AX:89-90`) — `S8:231`
- P29 Many-body closure plus the H-P bridge — Lattice `AX:37-41` — `S8:232`
- P30 Exact additive momentum on a grid — Qubit `AX:47` — `S8:233`
- P31 N-type universality by imposition — none — `S8:234`
- P32 Records as a smeared classical metric (ℓ_s ∈ [1e-10, 5e-6] m) — all four, plus a bridge — `S8:235`
- P33 Covariant CQ leaves the R8-3 subclass — none beyond P32 — `S8:236`
- P34 Holographic substrate — Lattice `AX:37-41`; Qubit; Admissibility — `S8:237`
- P35 Rotation multiplets and the ball (continuous SO(3) on the box) — Lattice `AX:37-38` — `S11:222`
- P36 Box-to-box gravitational conservation — `AX:187` — `S11:223`
- P37 Gauge-charge rigidity — `AX:47`; `AX:37-41`; `AX:57-58` — `S11:224`
- P38 Gapped edge for charged species (temperature cap) — none — `S11:225`
- P39 Loop protection revised (16-dim site block) — `AX:47` — `S11:226`
- P40 The empty vacuum (scope price) — none — `S11:227`
- P41 Supplied box graviton (N-type) — Qubit `AX:45-53`; `AX:187` — `S11:228`
- P42 Edge supertrace (Clifford-flat fermions plus scalars) — `AX:47` — `S11:229`
- P43 Set B box symbols (give up RP, or whole-zone SLAC) — `AX:60-61` — `S11:230`
- P44 Covariant CQ narrowed (non-Markovian noise or preferred frame) — `AX:60-61` — `S11:231`
- P45 Sector selection for qubits (flux-free sector) — `AX:47`; `AX:94` — `S11:232`
- P46 Pairing unit, refined — `AX:47` — `S14:177`
- P47 Photon multiplet outside 𝒮 — `AX:47`; `AX:57` — `S14:178`
- P48 No momentum in the superalgebra — `AX:116-130` — `S14:179`
- P49 Graviton production menu (P-N1, P-N2, P-N4) — `AX:45-53`; `AX:57`; `AX:187` — `S14:180`
- P50 Nonlinear closure tails (1/r^{d−1} off the box) — `AX:57` — `S14:181`
- P51 Fixed-grid vacuum (two tadpoles or signed pairing); = P-Tad — `AX:37-41`; `AX:189-190` — `S14:182`; `vR17-4:11`
- P52 Site creation (rate 3H) — `AX:37,40`; `AX:182-184` — `S14:183`
- P53 P-T, temporal vacuum reference — `AX:187`; `AX:94` — `S14:184`
- P54 q-charge for set A — `AX:187`; `AX:182-184`; `AX:94` — `S14:185`
- P55 Set A past 𝒰 (start time, …) — `AX:185-186` — `S14:186`
- P56 P-Q, quadrupole localization — `AX:187` — `S14:187`
- P57 dD-M graviton coupling — `AX:187` — `S14:188`
- P58 N = 4 KD content — `AX:47`; `AX:116-130` — `S17:212`
- P59 Spinor SUSY with momentum — `AX:47`; `AX:116-130`; `AX:57` — `S17:213`
- P60 BF non-local term — `AX:116-130`; `AX:57` (range reading) — `S17:214`
- P61 Subluminal edge — `AX:57` — `S17:215`
- P62 Edge-shape tuning for the shear (P-W*) — none; vacuum `AX:184-187` — `S17:216`
- P63 Graviton-cone edge prices; (iii) the vertex and its off-axis extension as law data — (iii) `AX:187` — `S17:217`; `vR17-4:9`
- P64 W2 protection by a tower or χ-cut — `AX:47`; `AX:187` — `S17:218`
- P65 Set A E1 (start time) — `AX:40`; `AX:185-186` — `S17:219`
- P66 Set A E2 (leaky waves) — `AX:57-61`; `AX:82-83` — `S17:220`
- P67 P-T readers — `AX:57`; `AX:187`; `AX:94` — `S17:221`
- P68 CMC lattice time — `AX:57` — `S17:222`
- P69 P-arrow — `AX:80`; `AX:185-186` — `S17:223`
- P70 Vacuum bridge (d-i)/(d-ii); under (S), the enthalpy condition — `AX:187`; `AX:47` (pairing) — `S17:224`; `vR17-7:21-30`
- P71 Graviton production, sharpened menu — `AX:45-53`; `AX:57` — `S17:225`
- P72 Set C bookkeeping — none — `S17:226`
- P73 e–γ tuning: 3 per class / 7 per species (conditional); ≤ 2 with P101 — none; sizes `AX:189-190` — `S17:227`; `vR16-10:19`

*Rounds 15–16 (S20 §3.3, `S20:369-401`).*
- P74 Instantaneous g-influence. **Refereed FAIL (signalling); not payable** — `AX:57`; `AX:185-186`
- P75 Reader stability below the 6H² ghost line — `AX:185-187`
- P76 Initial-value record B — open gate `AX:185`
- P77 Gauge-fixed metric record — `AX:82-83`
- P78 Under-recorded constraint channels — Admissibility/Record (as R6-4 (iii))
- P79 Tolerated dark gapless partners — none (observational)
- P80 Register reader. **Bounded FAIL for DESI in 𝓡⁺** — `AX:57`; `AX:116-123`; `AX:94-95`
- P81 Slow-content degravitation — `AX:185-187`; `AX:57`
- P82 Dual rotor — Qubit `AX:47`
- P83 Exact first-class constraint pair as a redundancy — none (`AX:57` supplies none)
- P84 Symmetric, locally conserved matter stress — `AX:187`
- P85 Running-minimum reader — `AX:57`; `AX:184-187`
- P86 Fast-transition exclusion or large |g| — `AX:186`
- P87 P-Z: zigzag edge plus 2 shape tunings (local form on U: zeros worker-checked) — none (`AX:116-123`); vertex `AX:184-187`
- P88 Law-supplied initial TT datum — `AX:185-186`; `AX:92-94`
- P89 Product initial states for meters — none
- P90 P-pf1, discontinuous momentum symbol — `AX:57-61`; `AX:187`
- P91 Sharp edge decoupling — `AX:57`; `AX:187`
- P92 **(S): the law's lowest state weighs nothing. Number-free; consistent; unforced; conditionally viable** — `AX:187`; `AX:116-130`; `AX:94` (reading)
- P93 Late-vacuum stability (the EW vacuum is the global minimum) — `AX:187`
- P94 No later pick among indistinguishable branches with unequal late vacua — `AX:57-66`
- P95 Exact first reading (IE) — `AX:94`; `AX:185-186`
- P96 Emergent constraint not dressing-connected (= P-r17-6d; signature: pinch points) — none (dynamical)
- P97 Sign problem, scalar-law violation, or another source bridge — none; `AX:187`
- P98 Non-local Hamiltonian-constraint completion (W7α) — `AX:57-58`
- P99 Dynamical auxiliary tensor field (W7aux) — `AX:47`
- P100 Shear by a non-shape knob — none / `AX:47` / `AX:184-187`
- P101 Lattice-superluminal photon (v_max 7.35299); n_t ≤ 2 (upper bound) — none; gives up the gauge-field subluminality rule
- P102 Power-law-ranged invariant hops — `AX:57`
- P103 Non-local or zero-vertex curvature readout — `AX:82-90`
- P104 World-line boost kernel (presentation-dependent) — `AX:57-61`
- P105 Weak/deformed translation closure — none (it deforms the HDA)
- P106 No active Cherenkov zero for defect modes (met by P61) — `AX:57-61`

*Rounds 16–17 (§3.3 here).*
- P107 Completion N — `AX:82-83`; `AX:187`
- P108 V0 + SF Dirac stipulations — `AX:187`
- P109 Wilson-Dirac μ_T2 row — none / `AX:47`
- P110 Z₂-clock reading of the metric slot — (`AX:47`); `AX:57-61`
- P111 Uniform-strain-conserving dynamics — `AX:57-61`
- P112 Shift action = R-point readout — `AX:37-41`
- P113 N = 2 metric readout — `AX:82-90`
- P114 Composite T₂ labels — `AX:82-90`
- P115 Low-symmetry slots plus block encoding — `AX:37-47`
- P116 Non-local multipliers (W7) — `AX:116-130`
- P117 Boundary Poincaré charges — `AX:82-83`
- P118 Observable-algebra readout bridge — `AX:82-83`; `AX:187`
- P119 Consistency-selection rule for final-state Λ laws — `AX:94`; `AX:185-186`
- P120 Record sourcing with re-added I. **Not payable as stated** — `AX:148-151,220-223`; `AX:79-83`
- P121 Matter-side relaxation — `AX:60-61`; `AX:185`
- P122 K₆ off-axis condition — none; `AX:187` for a vertex datum
- P123 M vertex (non-summable). **Not payable under a local law** — `AX:57-61`
- P124 Non-canonical or ξ̇-dependent shift action — `AX:187`; `AX:116-123`
- P125 (S′-start) with P94′ — `AX:116-130`; `AX:94`; `AX:185-186`
- P126 Stipulated vector TT vertex (VU) [worker] — `AX:187`
- P127 Vector placement datum (VM) [worker] — `AX:187`; `AX:57-61` if it needs a non-local half-shift
- P128 Non-Lagrangian partner for (d-i) [worker] — `AX:187`

**Count-once notes for the note.**
- P51 = P-Tad = P70's uniform part (paid by P-vac′ = P70 (d-i) with no number in 𝒟 [worker, R17-11]) = R17-7's enthalpy residual.
- P96 = P-r16-7a = P-r16-11a = P-r17-6d.
- P112 = P-r17-1c = P-r17-6a.
- P92 = P-r166a = P-r173a.
- P-r177b = P4.
- P-r1711a = P52/P53.
- P-r1711b = P68's existence hypothesis.
- P-R17-9d = P100.

**"In plain words" addition (proposed for §1).** "On a slower-than-light grid, every relativity test computed so far can be met at a count of about nine tuned numbers plus the cosmological constant. That constant can be removed without a number only by adding the rule 'the law's lowest state weighs nothing', which predicts a stabilized Higgs vacuum. The graviton cannot yet be made from the axioms' qubits at any named price except supplying it."

### 8.3 Pending at close (as of 01:47Z; the wrap-up should update it)

- **Referees running:**
  - R17-9 (worker OPEN; VU no zero, VM zero with μ_T2 = +0.106);
  - R17-10 (worker: K₆ OPEN on 𝒮, CERTIFIED-CONFLICT on 𝓕; μ_E OPEN);
  - R17-11 (worker CONSISTENT in 𝒟).
- **Workers running:**
  - R17-12 (VU or VM);
  - R17-13 (μ_T2 zeroable or sign-definite).
- **Recorded since S20:** vR17-6, vR17-7 and vR17-8, at `TESTS:6283-6318`; the `agents/` copies are identical.
- **Round-18 drafts:** R18-1 … R18-4, none launched.
- **Never refereed (worker findings to list in provenance):**
  - R16-1's Z-width transfer to D1;
  - R16-4's E2 memory figure;
  - R16-3's U common zeros (P87's local form);
  - R16-13's SM-count stall numbers;
  - R17-1's N0914 full-J k⁰ phase;
  - R17-6's best candidate;
  - R17-7's DESI proxy beyond arithmetic;
  - R17-2's escape-3 and escape-5 sketches;
  - R17-8's joint-class sketch.
- **`SUMMARY` §26 label fix** (R15-4, R15-6), and §27 (from §8.1).

### 8.4 Theorem-list additions for the wrap-up (rounds 16–17; cite as "item + name")

| Item | Result | Verdict |
|---|---|---|
| R16-10 | Theorem L (integrable valleys); Dirac zero (literal class) | `vR16-10:27` |
| R16-11 | Theorem B′ (dressed f-sum) | `vR16-11:37` |
| R16-12 | T3/J3 (leading, weak); B3 (bounded-angular, presentation-dependent) | `vR16-12:21` |
| R16-13 | Theorem DT, Lemma V1, Wilson T₂g shear (conditional on V0/SF/seagull) | `vR16-13:29` |
| R16-14 | Lemma L (L0/L½ EXCLUDED) | `vR16-14:23` |
| R17-1 | Modular moment identity; k⁰ and k² Z₂ models | `vR17-1:28` |
| R17-2 | Lemma D; Lemma H (weak) | `vR17-2:17` |
| R17-3 | The bounded Λ obstruction; (S) number-free | `vR17-3:19` |
| R17-4 | Off-axis formula; U identities; Lemma M; tadpole positivity | `vR17-4:15` |
| R17-5 | MB-A, MB-B, Corollary S, Lemma RB (H-RB) | `vR17-5:17` |
| R17-6 | Theorem G; Theorem Z; Z′ (corrected); Propositions F, S | `vR17-6:19` |
| R17-7 | Λ̃ ≥ 0 under (S); c₄; Lemma X; fixed-e₀ covariant form | `vR17-7:74` |
| R17-8 | Lemma N; MIX-1; MIX-2; Lemma FD (first order); Theorem W (repaired, analytic tame) | `vR17-8:39` |

---

## 9. Caveats

- **Same family, unrefereed.** Everything this synthesis adds is unrefereed and from the same model family as the workers:
  - the DERIVED/OPEN and "cheapest price" columns;
  - W17 as a wall;
  - the P107–P128 numbering and the count-once identifications (notably P51 = P-Tad = P70's uniform part = R17-7's enthalpy, which R17-11's worker also makes);
  - every [S23 reading], including the P107/P88 interlock and the "9 + CC with Wilson-Dirac" total;
  - the owner questions and the round-18 drafts.
- **Worker readings used with referees running.**
  - R17-9: VU/VM, the Dirac-like vector sign, P126 and P127.
  - R17-11: (d-i) consistent; the tadpole row at 0 numbers; P128; P52 as the receiver.
  - R17-10: Theorem F on 𝓕; P-K6′.
  - If any of these referees narrows them, these change: §1.0 items 1 and 3, §1.3, §1.6, §1.8's last total row, W4, W9, W10, W11, Q1 condition 2, Q5, and R18-3's premise.
- **Pending.**
  - R17-10's referee rules on Theorem F (sharp-turn slice only).
  - R17-12 decides whether the vector placement is a law datum or forced.
  - R17-13 decides whether μ_T2 is a shape tuning or a separate knob.
- **Bounded, not class-wide.**
  - R16-11: volume-uniform dressings with finite K₂.
  - R17-1: the staggered-slot Z_N class, not compiled into M₂(C) per site.
  - R17-6: the internal-Goldstone and regular soft-TT classes.
  - R17-4: separable 𝒮, supplied zero-point vacuum, E1.
  - R17-5 and R17-8: free, symmetric-stress, projectable, finite-band matter.
  - R17-3: the homogeneous conserved setting.
  - R16-14: weak-field linear order.

  **No refereed result says the graviton, Λ or the split is impossible in general.**
- **Prescription scope.** Every Ξ and μ statement uses an R9-9-type vertex (now U for locality), an assumed standard W1, an ultralocal seagull and a supplied zero-point vacuum. They are bare-cone shifts, not dressed poles. W15 still supplies no gauge-invariant replacement.
- **Scale bridge.** Every Planck-unit number uses a = ℓ_P (`AX:189-190`): the 1e123 enthalpy, 1.748e19 GeV, the record costs, and the 1e-13 to 1e-16 precisions.
- **RECALLED inputs.** SM metastability sizes, DESI and the m_t tension are recalled or proxy values, as their sources label them.
- **Drafts are proposals for the driver.** Readings are fixed here so they cannot be adjusted after a run. The driver may reorder or drop items. R18-3 waits on R17-12's worker reading and is dropped if it returns FORCED-VM. R18-4 is optional. No draft repeats R17-12 or R17-13.
