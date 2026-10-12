# C5 R13-5 report: the graviton–matter split with a Ward-completed pair-creating stress

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Not refereed. 2026-10-12, 20:13Z to about 20:45Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R13-5/`. Scripts and outputs are in `S/scripts/`. Each runs in under 3 s at `OMP_NUM_THREADS=2`.
- `r135_w1_pair.{py,out}`: part (a). The W1 completion of the pair channel, with checks (residuals, Hermiticity, box agreement with the continuum, the q → 0 limit, the TT components left untouched, locality).
- `r135_moments.{py,out}`: Lemma B2. The pair channel drops out of H, P and K.
- `r135_xi_split.{py,out}`: parts (b) and (c). The Ξ split into box-transverse and edge-transverse parts, the class bound, the birefringence knob, and the split table.
- `r99_profiles_copy.py`: R9-9's band profiles, unmodified.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - the C5 method (`:2302-2320`);
  - lane RV4 results (`:2204-2236`) and lane RFW (`:2237-2300`);
  - Round 13 in full (`:4560-4694`); R13-5 is `:4668-4678`.
- `agents/C5_S14_synthesis.md`, in full.
- Reports and verdicts:
  - `C5_R9-9_report.md` and `C5_R9-9_referee_verdict.md` (`vR9-9`);
  - `C5_R11-1_report.md` and `C5_R11-1_referee_verdict.md` (`vR11-1`);
  - `C5_R8-2_report.md`;
  - `C5_R11-3_report.md:30-80` and `C5_R11-3_referee_verdict.md:1-60` (`vR11-3`);
  - `C5_R10-5_referee_verdict.md` (`vR10-5`);
  - `C5_R12-1_referee_verdict.md:15` (`vR12-1`).
- `C4_F1_report.md:96,140` and `C4_F3_referee.md:13`, for the khronometric and aether comparator.
- Scripts `scripts/C5/R9-9/r99_tt_selfenergy.{py,out}` and `scripts/C5/R11-1/r111_split_numbers.out`.

**What I did not read.** `SUMMARY.md` §§21–25 was not read in full; I used S14 §1 instead. C5 results from round 6 to round 9 were read only through S14, the cited verdicts and the R9-9/R11-1 reports.

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature, RECALLED unless verified.

---

## 0. In plain words

1. **Completing the pair-creating stress to first order is easy, and it fixes nothing that matters.**
   - The creation of a particle pair always costs at least 2m of energy. So the conservation law (W1) can always be met by *defining* the time components of the stress from its space components.
   - Every smooth choice of the spatial pair stress therefore has an exactly conserved completion. Inside the box it stays the continuum stress (checked to 1e-15).
   - The TT (graviton-polarization) part of the stress is not touched by this completion. W1 does not see it at all.
   - So R9-9's "completion assumed, not built" (`vR9-9:5`) is now built at first order, for every TT vertex. R9-9's numbers are numbers for conserved stresses.
2. **No Ward identity of any order can fix the graviton's speed.**
   - For q along a cube axis, cubic symmetry splits the self-energy into blocks. The two TT channels are 1×1 blocks that no Ward identity reaches.
   - Gauge invariance pins the graviton's *mass* (its q → 0 value), never its *speed*. This is why aether/khronometric gravity can be fully gauge-invariant and still have c_T ≠ 1 (comparator).
3. **The second-order (gauge-invariance) identity cannot hold for any member.**
   - Its moments are the Poincaré relations. The pair channel drops out of H, P and the boost K exactly, because its time components vanish like q and q².
   - So R8-2's Theorem E applies unchanged: [K_i, P_j] = i·dΓ(ε(δ_ij + A_ij)), with zone mean A = −I. Poincaré fails on edge states whatever the pair stress is.
   - Hence the matter pole is not Ward-protected in this class. The registered phrase "pole positions (which is gauge-invariant)" cannot be delivered for the matter side.
4. **The graviton-cone shift has a floor that the free part of the vertex cannot remove.**
   - Box-exactness fixes the TT vertex on box-transverse momenta. On the gapped edge, every allowed vertex gives a slower graviton by at least |Ξ_box⊥|, at every mass (proved).
   - On the literal edge every allowed vertex gives a faster graviton, but only for loop masses m ≥ 0.1 (checked).
   - For lighter L species the floor fails. L's doubler corners make the weight I(B) negative for B < 7e-4, so a free edge vertex can push Ξ either way.
   - For physical, light matter in the de Donder prescription, with G-type loop species, the split is at least 2.8e-3 (E_g) to 5.3e-3 (T_2g) per species at a = ℓ_P. That is about 3e12 to 5e12 times the GW170817 band. The free edge part of the vertex can only *add* to it.
5. **Birefringence is not forced in this class (a correction).** One smooth edge knob equalizes the two polarizations at one mass. Equality at all masses holds exactly when an isotropy (pushforward) condition holds, and the same condition removes the CC-independent TT mass split. So "matter can sit on at most one TT cone" (`vR11-1:19`) is true for the M and U vertices, not for the whole class.
6. **With the pairing unit:**
   - the TT shift vanishes identically, for both polarizations (Theorems PT and S);
   - the scalar matter's own shift is unpaired, so c_m − c_T = 2κJ = 4κm²J₂. That is nonzero, but about 2e-39 for a proton in de Donder;
   - so the split is not identically zero, but it is negligible in that prescription.

**Against the FIXED readings (worker reading; referee required).**
- **Without pairing: SPLIT-PRESENT, scoped.**
  - Graviton side: class-wide over 𝒲_V (§1).
  - Matter side: in the Lemma-M (de Donder) prescription, for light external matter.
  - At lattice masses (m = 1, 0.3) it is not class-wide: two edge tunings per mass (one per polarization) can zero it.
- **With pairing: OPEN by the letter.**
  - Not SPLIT-ABSENT, because c_m − c_T = 4κm²J₂ ≠ 0.
  - The TT part is exactly zero.
- **(a): a no-go for the second-order Ward-complete stress (Lemma B2)**, in the class of §1, to the referee. If the referee reads "Ward-complete" as second order, the class in the FIXED readings is empty, and the overall reading is OPEN with this no-go recorded.

---

## 1. Hypotheses and classes (stated before any title)

- **H-mat.**
  - A free real scalar field on Z³ × ℝ, with ε² = m² + Σ_i u(k_i).
  - Profiles G (gapped) and L (literal) of R8-2/R9-9, box |k_i| ≤ B = 2 (`C5_R9-9_report.md:42`). m = 1, 0.3, with 0.1 and 0.01 added for loop species.
  - The paired variant is Theorem S's unit: 4 complex scalars per 8-component Clifford-flat fermion, a common curve, w = S², matched masses (`vR11-1:9`).
- **H-grav.**
  - R9-9's N-type box graviton, with symbol d(q) (c₁ = 1, c₂ = 2.5) and divergence symbol D = d·e^{iq/2} (`C5_R9-9_report.md:35-39`).
  - GR normalization, with c_T² − 1 = 2κ_lat Ξ and κ_lat = 8π(ℓ_P/a)².
- **W1 (first-order Ward identity).**
  - In each channel, ω_ch F^{0ν} = Σ_j D_j F^{jν}, where ω_ch = (created energy) − (destroyed energy).
  - Channels: scattering (R8-2's Construction A, `C5_R8-2_report.md:73-90`); pair creation, ω = ε₁ + ε₂; pair annihilation, ω = −(ε₁ + ε₂).
  - The stress is Hermitian, symmetric and quasi-local (C^∞ kernels). Its forward values are universal: F^{00}(k,k) = ε and F^{0i}(k,k) = p_i = ∂_i(ε²/2).
- **Second-order identity (W2).**
  - The O(κ) closure of the linearized constraint algebra with matter: the Dirac–Schwinger algebra of the stress at flat background, with the seagull.
  - I test only its moment form. With H = ∫T^{00}, P_j = ∫T^{0j} and K_i = ∫x_i T^{00}, the Poincaré relations must hold. In particular [K_i, P_j] = iδ_ij H.
  - That degree-2 closure needs exact Poincaré is refereed for free number-conserving box fermions (`vR12-1:15`). For scalars I use it as the moment form of W2 (Schwinger, RECALLED).
- **Class 𝒲_V (for part (b)).** W1-complete pair stresses whose TT pair vertex at q ∥ z:
  - (i) depends only on the transverse pair momenta (R9-9's class 𝒱, `C5_R9-9_report.md:44`);
  - (ii) equals the continuum minimal vertex on box-transverse momenta |k_x|, |k_y| ≤ B. That is |V|² = 4k_x²k_y² (T_2g) and (k_x² − k_y²)² (E_g). This is box-exactness, carried to every k_z by (i);
  - is otherwise free: nonnegative, smooth, and with the right C_4v parity.
  - The members **U** (w = p = u′/2) and **M** (w = s, s² = u) are in 𝒲_V. M is smooth only on L. On G, s = sign(k)√u jumps at the zone face (`vR11-1:17`); see §3.1(6).
- **Matter-side prescription (Lemma-M class, R11-1).**
  - A de Donder-type box propagator, an ultralocal seagull, and a vertex of covariant tensor form in the external leg. The internal functions are arbitrary (`C5_R11-1_report.md:222-232`).
  - J values are R11-1's, as refereed and reproduced (`vR11-1:15-17`).
- **Subtractions, named before the runs (R9-3 rule).**
  - Ξ: none. It is an identity of one-loop integrals, and ultralocal seagulls drop out by construction.
  - J: R11-1's λ → 0 extrapolation, with no channel subtracted.
  - The locality decay (§3.1(6)) uses raw Fourier coefficients of the kernel, with nothing subtracted.
- **Perturbative order of exactness (new rule).**
  - W1 is required exactly at O(√κ), i.e. linear in h.
  - W2 is examined at O(κ), the moment form only.
  - Pole shifts are one loop, O(κ).
- **Excluded (outside realizations):**
  - fermion external matter (the electron's graviton-loop shift);
  - non-axis q;
  - TT vertices that depend on k_z or q, such as R9-9's INV vertex (Ξ_para = 0 there, `C5_R9-9_report.md:171-178`);
  - non-separable bands;
  - graviton loops on the graviton line;
  - two loops;
  - interacting matter;
  - compact link variables.

## 2. Prior art (each counted once)

- **R8-2 Construction A and Theorem E** (`C5_R8-2_report.md:73-124`). The scattering-channel W1 stress, and [K, P_grav] = i(H + 𝒜) with zone mean A = −I.
- **R9-9 and its verdict.**
  - Theorem T: Ξ = (1/32)⟨|V|²A_zz/ε⁵⟩ (`vR9-9:7`).
  - G-edge sign (`vR9-9:12`).
  - Lemma N needs vertex richness (`vR9-9:14`).
  - The pair-stress completion was assumed (`vR9-9:5`).
  - Matter shift omitted (`vR9-9:23`).
- **R11-1 and its verdict.**
  - Lemma M and the dD-M split table (`vR11-1:11-19`).
  - Theorem N\* and Theorem S (`vR11-1:3-9`).
  - Birefringence, existential (`vR11-1:19`).
- **R10-5 Theorem PT.** Algebra confirmed; the scalar vertex was stipulated and not Ward-completed (`vR10-5:5`).
- **R11-3's U/M vertices.** Forward values (`C5_R11-3_report.md:54-58`). The U pair completion was assumed (`vR11-3:31`).
- **R12-1.** Degree-2 closure needs exact Poincaré on the core (`vR12-1:15`).
- **RV4 S1.** "Compact Ward covariance would enforce μ_E = μ_T2, but it is incompatible with the field-independent e^{−iP[ξ]} bulk response" (`TESTS:2219`).
- **RFW.** F2: no O(κ²) completion for K2's nearest-neighbour scalar, C¹ at q = 0. F1: narrow fixed-field FAIL (`TESTS:2263-2300`).
- **C4 lane RF.** Khronometric c_T² = 1/(1 − β) with full diffeomorphism redundancy in Stückelberg form (`agents/C4_F1_report.md:96`; `agents/C4_F3_referee.md:13`). Comparator for "gauge invariance does not fix c_T".
- **GW170817.** −3e-15 ≤ c_T − 1 ≤ 7e-16 (`C4_F1_report.md:103`; GWTC/LVK values as recorded there; not re-verified).
- **Repo search.** grep for "Ward-complete", "pair-creating stress" and "pair stress" over `docs/` and `.claude/science`. The only hits are the C5 packet's own open items (`TESTS:3948`, `vR9-9:5`, `vR11-3:31`, R11-1 §4.4) and one unrelated staggered TT-projected-stress ledger row. No prior pair-channel W1 completion exists.

## 3. Results

### 3.1 (a) Lemma P1: first-order completion of the pair channel. Proved; checked (`r135_w1_pair.out`)

**Statement.**
- Let m > 0, and let F^{ij}(k₁, k₂) be any smooth symmetric spatial pair-creation kernel on T³ × T³.
- Define F^{0j} := Σ_i D_i(q)F^{ij}/ω and F^{00} := Σ_j D_j F^{0j}/ω, with q = k₁ + k₂ and ω = ε₁ + ε₂ ≥ 2m.
- Take the annihilation channel of T(−q) to be the complex conjugate.
- Then:
  - W1 holds exactly in both pair channels;
  - T is Hermitian, because D(−q) = −D(q)*;
  - the kernel is C^∞, so quasi-local;
  - F^{0j} = O(|q|) and F^{00} = O(|q|²) as q → 0.

**Proof.**
- ν = i: ωF^{0i} = Σ_j D_j F^{ji} by definition.
- ν = 0: ωF^{00} = Σ_j D_j F^{j0}.
- For the conjugate channel, conjugate W1 and use D(−q) = −D(q)*.
- Smoothness holds because ω ≥ 2m > 0.
- The orders in q follow from one or two factors of D, with D(0) = 0. ∎

**Checks** (d = 3; 20 000 random pairs per set; G and L; U and M; m = 1, 0.3):
1. W1 residual ≤ 3.6e-15 (creation) and ≤ 8.2e-15 (annihilation). |D(−q) + D(q)*| ≤ 1.1e-15. μν symmetry ≤ 1.8e-15.
2. **Box-exactness is kept.** On box pairs (|k_i| ≤ 1.9, |q_i| ≤ 0.9) the completed F^{0ν} equals the continuum π∇φ kernels to ≤ 7.2e-16 (G, and L M). For L U it is 1.8e-11, from L's finite-difference u′.
   - Reason: the continuum minimal kernel satisfies pair-W1 with D = q. I checked the algebra by hand: Σ_j q_j F^{jν} = −(ε₁ + ε₂)(ε₁k₂ + ε₂k₁)^ν/(2√(ε₁ε₂)).
3. **The q → 0 limit.** max |F^{0ν}| = 1.5e-4 to 9.9e-4 at |q| = 1e-4, scaling as q. max |F^{00}|/|q|² stays at 0.5–2.3 (`r135_moments.out`).
4. **TT is untouched.** At q ∥ z, |V_T2g|² = 4w_x²w_y² and |V_Eg|² = (w_x² − w_y²)² to 1e-13, and to 2.5e-7 for L U (finite-difference p).
5. **Locality** (d = 1, raw Fourier coefficients of F^{00}_pair, N = 512, nothing subtracted). Max |c| at sup-distance r = 200:

| member | max \|c\| at r = 200 | decay |
|---|---|---|
| G U | 1.3e-12 | super-polynomial |
| L U | 1.0e-9 | super-polynomial |
| L M | 6.3e-11 | super-polynomial |
| G M | 1.5e-4, 2.4e-4 at r = 100 | power-law |

   - The G M decay is power-law: M on G is **not** local, because s_G jumps at the face. Use U on G.

**Corollaries.**
- **(C1) Completion is now built (proved).** R9-9's TT numbers for M and U (`C5_R9-9_report.md:136-142`, reproduced in `r135_xi_split.out` to every printed digit) are numbers for W1-exact pair stresses. The "completion assumed" caveat (`vR9-9:5`, `vR11-3:31`) is discharged at first order. M on G stays non-local.
- **(C2) Richness holds (proved).** Every smooth nonnegative TT vertex in 𝒱 is W1-completable. So Lemma N's richness hypothesis (`vR9-9:14`) holds in the W1-complete class: no band nulls Ξ for every W1-complete stress. The same goes for R10-5's stipulated scalar TT vertex: PT's "not Ward-completed" (`vR10-5:5`) is discharged at first order, for the boson side. The fermion pair channel has ω ≥ 2m as well and completes the same way. That is argued, not run.
- **(C3) W1 is no constraint here (proved).** In the pair channel W1 constrains nothing: every spatial pair kernel is admissible. The pair stress is therefore a law datum, not fixed by conservation (reading).

### 3.2 Lemma W0: no Ward identity fixes a TT pole position at axial q. Proved

**Statement.** Take q = qẑ, a cubic-invariant vacuum, and any stress and seagull. Under the little group C_4v the components of h split as:
- A₁: 00, 0z, zz, xx+yy;
- E: (0x, 0y);
- E: (xz, yz);
- B₁: xx−yy (E_g);
- B₂: xy (T_2g).

Then:
1. The one-loop Π^{μν,ρσ}(ω, qẑ) is block-diagonal, so B₁ and B₂ do not mix with anything.
2. Any Ward identity q_μΠ^{μν,ρσ} = C^{ν,ρσ} with q_μ = (ω, 0, 0, D_z) and covariant tadpole contact terms is empty for ρσ ∈ B₁ or B₂.
   - Its left side involves only (0ν) and (zν), which lie in A₁ ⊕ E. These do not couple to B_i, by part 1.
   - C^{ν,ρσ} transforms in (A₁ ⊕ E) ⊗ B_i, which contains no invariant.
3. So for q ≠ 0, Π_TT(ω, qẑ) is unconstrained by Ward identities of any order.

**What can be fixed.** Only the q → 0 values are tied to constrained components. Continuity of the gapped loop at q = 0 links them to the Ward identity at non-axial q: the cubic constants c₄₄ and c₁₁ − c₁₂ of Π^{ijkl}(0, 0), i.e. the two TT masses. Beyond cubic symmetry, the continuum spin projectors also leave the spin-2 function Π₂(ω², q²) free under transversality. Only boosts fix its (ω² − q²) dependence.

**Comparator.** Khronometric/aether gravity: exact diffeomorphism redundancy with c_T free (`C4_F1_report.md:96`).

**Consequence.**
- The TT pole at axial q is fixed by the law's TT vertex and by the q-dependence of the TT seagull. A q-dependent TT seagull is a speed counterterm (`C5_R9-9_report.md:55`).
- Ultralocal seagulls drop out of Ξ (Theorem T).
- At one loop the TT self-energy contains no graviton propagator, so it has no gauge parameter. It depends on the stress, not on a gauge.

### 3.3 Lemma B2: no member is second-order Ward-complete. Proved (moment form); checked (`r135_moments.out`)

**Statement.**
- For every stress that is W1-complete in all channels (pair kernel arbitrary) and has universal forward values F^{00}(k,k) = ε and F^{0i}(k,k) = p_i on a C² periodic band:
  - H = dΓ(ε);
  - P_j = dΓ(p_j);
  - K_i = dΓ(½{X_i, ε}).
- All three are number-conserving, and **[K_i, P_j] = i·dΓ(ε(δ_ij + A_ij))**, with A = Hess(ε²/2) − I.
- The zone mean of A is −I, so A ≠ 0 on a set of positive measure. The Poincaré relation [K_i, P_j] = iδ_ij H, the moment form of W2, therefore fails on edge one-particle states for every member, whatever the pair kernel.

**Proof.**
- By Lemma P1, F^{0ν}_pair = O(q) and F^{00}_pair = O(q²). So the pair parts of ∫T^{0ν} (q = 0) and of ∫xT^{00} (i∂_q at q = 0) vanish.
- The scattering parts are R8-2's: Y = 0 for real symmetric F^{00}, and Theorem E's operator identity (`C5_R8-2_report.md:115-124`).
- The vacuum normal-ordering constant does not enter commutators. ∎

**Meaning.**
- R12-1's "degree-2 closure ⇒ exact Poincaré" (`vR12-1:15`) plus Theorem E is extended here to pair-creating scalars. The new piece is that the pair channel cannot repair it.
- So a Ward-complete stress in the registered (second-order) sense **does not exist** in this class. That is answer (a)'s "prove none exists in a stated class". It is a no-go, to the referee.
- The scalar case relies on W2's moment form, i.e. the Schwinger moments (RECALLED). It is not an independent proof of R12-1's implication for scalars.
- **Consequence for the registered premise (proved for the protection; suggested for the size).** The Nielsen-type argument that makes the matter pole gauge-independent needs W2's one-particle matrix elements. These fail on edge states, and loop momenta reach the edge. So the matter pole is **not Ward-protected** in any member.
- Its gauge dependence at O(κ) is suggested to be an edge integral. It is not computed. R11-1's ζ-gauge diagnostic was withdrawn for lack of the seagull's gauge part (`C5_R11-1_report.md:266`).

### 3.4 (b) TT pole shifts over 𝒲_V: the box-transverse floor. Proved (G), checked (L) (`r135_xi_split.out`)

**The split.**
- Write Ξ = Ξ_box⊥ + Ξ_edge⊥, where Ξ_edge⊥ = (1/32)∫_{edge⊥}|V|²(k_⊥) I(m² + u_x + u_y) and I(B) = ∫A_zz(B + u_z)^{−5/2} dk_z.
- In 𝒲_V the vertex on box⊥ is fixed (continuum), and the edge⊥ vertex is free and ≥ 0.
- **G** (I < 0 for every B, because A_zz ≤ 0, proved; `C5_R9-9_report.md:147-150`, `vR9-9:12`): **every member has Ξ ≤ Ξ_box⊥ < 0**, for both polarizations and every mass.
- **L, m ≥ 0.1** (checked, fine quadrature, `r135_L_small_m.out`): every member has Ξ ≥ Ξ_box⊥ > 0. The minimum of I over the edge⊥ B values is +7.3e-3 (m = 0.3) and +7.6e-3 (m = 0.1).
- **L, small m: the floor fails** (checked; asymptotics proved).
  - L has doublers at k = π, where u = 0 and A_zz ≈ −2δk². So I(B) ≈ −4/(3B) as B → 0, and I changes sign at B ≈ 7e-4 (I(1e-4) = −1.13e4).
  - For loop masses m ≲ 0.026, edge⊥ points near the doubler corners carry I < 0, and their vertex weight is free. So 𝒲_V has L members with Ξ of either sign.
  - The E_g vertex need not vanish at the corner (π, 0), so it can even diverge like ln(1/m).
  - This is R8-2's Finding D, the literal edge's light doublers (`C5_R8-2_report.md:64-71`), seen in the TT channel.
  - The N = 128 grid values for L at m = 0.1 and 0.01 agree with the fine quadrature to ≤ 0.8%: Ξ_box⊥ = +3.00e-3 and +3.05e-3 for T_2g. The M and U vertices vanish at the corners, so their totals are unaffected.

**Ξ per scalar species** (N = 128; lattice units):

| edge, m | pol. | Ξ_box⊥ (class floor) | U total | M total |
|---|---|---|---|---|
| G, 1.0 | T_2g | −1.694e-4 | −4.840e-4 | −9.602e-4 |
| G, 1.0 | E_g | −8.80e-5 | −2.521e-4 | −5.292e-4 |
| G, 0.3 | T_2g | −2.075e-4 | −5.723e-4 | −1.112e-3 |
| G, 0.3 | E_g | −1.099e-4 | −3.042e-4 | −6.279e-4 |
| G, 0.01 | T_2g | −2.119e-4 | −5.823e-4 | −1.129e-3 |
| G, 0.01 | E_g | −1.125e-4 | −3.101e-4 | −6.390e-4 |
| L, 1.0 | T_2g | +1.138e-3 | +2.688e-2 | +2.409e-3 |
| L, 1.0 | E_g | +8.56e-4 | +9.056e-2 | +2.319e-3 |
| L, 0.3 | T_2g | +2.660e-3 | +6.071e-2 | +5.276e-3 |
| L, 0.3 | E_g | +2.192e-3 | +2.477e-1 | +5.519e-3 |
| L, 0.01 | T_2g | +3.05e-3 (box part only; **not a floor**) | +6.803e-2 | +5.984e-3 |
| L, 0.01 | E_g | +2.56e-3 (box part only; **not a floor**) | +2.876e-1 | +6.336e-3 |

**How the floor depends on hypothesis (ii)'s region (checked, `r135_floor_bprime.out`).** The floor depends on b′, the half-width of the region where the TT vertex is fixed to the continuum. On G:

| b′ | what it is | Ξ_floor, T_2g / E_g (m = 0.3) | at a = ℓ_P |
|---|---|---|---|
| 2.0 | full box | −2.13e-4 / −1.13e-4 | 5.4e-3 / 2.8e-3 |
| 1.6 | R8-2's χ₁ gluing region (`C5_R8-2_report.md:80-81`) | −8.2e-5 / −4.1e-5 | 2.1e-3 / 1.0e-3 |
| 1.0 | | −7.7e-6 / −3.4e-6 | 1.9e-4 / 8.6e-5 |

- Any b′ > 0 gives a strictly negative floor on G, because I < 0 everywhere.
- At b′ = 1.0 the floor is still about 1e11 times the GW band.
- The b′ = 2 values differ by about 3% between N = 128 and N = 256, from discretizing the sharp mask. The floors carry that uncertainty.

**Size at a = ℓ_P (κ_lat = 8π; reading on `AX:189-190`).**
- Every member: |c_T − 1| ≥ 2.2e-3 to 5.3e-3 (G, all m), per species.
- For L with m ≥ 0.1: ≥ 2.2e-2 to 7.5e-2.
- A single G species needs a ≳ 1.5–2.3 × 10⁶ ℓ_P to fit the GW170817 band, for every member. That is the class floor (R9-9 quoted 2–9 × 10⁶ for M and U).

**Mass interval.**
- Theorem N\* (`vR11-1:3`) applies in all of 𝒲_V, since the weights are k_∥-independent.
- So no purely bosonic loop content in 𝒲_V has Ξ = 0 on a mass interval. A mix of G and L scalars could cancel at one mass, by one tuning.

### 3.5 Birefringence in 𝒲_V. Checked (single mass); proved (all masses ⇔ isotropy)

**One knob, one mass (checked).**
- Scale E_g's edge weight by a smooth knob 1 + (c − 1)η, with η = 1 − ρ(k_x)ρ(k_y), which is 0 on box⊥.
- On G (U), c\* = 6.14 gives Ξ_Eg = Ξ_T2g at m = 1. The difference drifts to −1.1e-6 at m = 0.3 (0.2%).
- On L the E_g knob would need c < 0. Raising T_2g's edge weight instead works, because Ξ_T is linear in the knob with a positive edge part (proved, one line).

**All masses (proved).**
- Ξ_T2g(m) = Ξ_Eg(m) on a mass interval ⇔ the pushforward of |V_T|² − |V_E|² under k_⊥ ↦ u_x + u_y vanishes.
- Proof: Laplace/Lerch, as in N\*. F_A(t) = ∫A_zz e^{−tu}dk_z is analytic with F_A(0) = −2π ≠ 0.
- The same isotropy condition makes the CC-independent mass split vanish, because Δμ = −(1/8)⟨(|V_E|² − |V_T|²)/ε³⟩ is the same pushforward with a different kernel.
- A smooth nonnegative member that meets it is suggested, not constructed.

**Correction.** `vR11-1:19` ("a scalar matter cone can coincide with at most one graviton polarization") holds for the M and U vertices. It is **not** class-wide in the W1-complete class: one mass-dependent tuning, or an isotropy rule, removes it. The speed floor of §3.4 stays.

### 3.6 The split c_m − c_T = κ_lat(2J − Ξ)

J is R11-1's dD-M value, with the external species equal to the loop species. The M rows reproduce `vR11-1:16`. Values are in κ_lat/16π² units:

| edge, m | pol. | M | U (new) | paired (Ξ ≡ 0) | at a = ℓ_P: M / U / paired |
|---|---|---|---|---|---|
| G, 1.0 | T_2g | −1.589 | −1.665 | −1.741 | −0.253 / −0.265 / −0.277 |
| G, 1.0 | E_g | −1.657 | −1.701 | −1.741 | −0.264 / −0.271 / −0.277 |
| G, 0.3 | T_2g | +0.014 | −0.071 | −0.162 | +2.3e-3 / −1.1e-2 / −2.6e-2 |
| G, 0.3 | E_g | −0.062 | −0.113 | −0.162 | −9.9e-3 / −1.8e-2 / −2.6e-2 |
| L, 1.0 | T_2g | −2.555 | −6.420 | −2.175 | −0.407 / −1.02 / −0.346 |
| L, 1.0 | E_g | −2.541 | −16.48 | −2.175 | −0.405 / −2.62 / −0.346 |
| L, 0.3 | T_2g | −1.040 | −9.793 | −0.206 | −0.166 / −1.56 / −0.033 |
| L, 0.3 | E_g | −1.078 | −39.32 | −0.206 | −0.172 / −6.26 / −0.033 |

**Light external matter (physical case; checked).**
- By Lemma M, J = m²J₂ → 0 (`vR11-1:11`). Lemma M needs only the external leg on shell inside the box, so it holds for any internal vertex functions.
- So c_m − c_T → −κΣ_sΞ_s, summed over the loop species. Per scalar loop species at m = 0.01:

| edge | pol. | U | M | class floor | floor at a = ℓ_P | × GW band |
|---|---|---|---|---|---|---|
| G | T_2g | +0.092 | +0.178 | ≥ 0.0335 | 5.3e-3 | ≥ 5.3e12 |
| G | E_g | +0.049 | +0.101 | ≥ 0.0178 | 2.8e-3 | ≥ 2.8e12 |
| L | T_2g | −10.7 | −0.945 | **no floor** (doubler corners, §3.4) | n/a | n/a |
| L | E_g | −45.4 | −1.001 | **no floor** | n/a | n/a |

- Floors are in κ_lat/16π² units. For G-type scalar content the floors add with one sign.
- For light L species, members with Ξ = 0 exist in 𝒲_V, by one tuning per polarization. These are members, not natural choices.

**At lattice masses (proved).** On G, 2J < Ξ_box⊥ < 0 (for example −1.10e-2 against −1.69e-4 at m = 1). The free edge weight can lower Ξ to 2J, separately for each polarization. So two tunings per mass remove the split there. SPLIT-PRESENT is class-wide only for light external matter.

### 3.7 (c) The paired unit

- With Theorem S's unit (common Clifford-flat curve, w = 2√(N_F/N_B)S² = S², matched masses), the TT coefficient cancels identically for both polarizations (Theorem PT, algebra confirmed, `vR10-5:5`; Theorem S, `vR11-1:9`).
- Pairing removes 𝒲_V's freedom: w is forced pointwise, edge included.
- The boson TT vertex is W1-completable by Lemma P1, so PT's "not Ward-completed" is discharged at first order.
- What is left is the unpaired scalar matter shift: c_m − c_T = 2κJ = 4κm²J₂.
  - At lattice masses: −1.741 (G, 1), −0.162 (G, 0.3), −2.175 (L, 1), −0.206 (L, 0.3), in κ/16π² units.
  - For a proton at a = ℓ_P: −1.7e-39 (G) and −2.2e-39 (L), in dD-M.
- The fermion partner's own (electron) graviton-loop shift is not computed.
- The pairing residual under a mass split, O(Δm²), is not computed for TT.

### 3.8 (d) Which seagull terms a Ward identity fixes

| identity | what it fixes |
|---|---|
| W1 | Fixes no seagull. Ultralocal seagulls drop out of Ξ (Theorem T) |
| W2, if it held | Only the q → 0 TT constants: c₄₄ and c₁₁ − c₁₂, i.e. μ_T2 and μ_E, both at the tadpole (CC) value (Lemma W0's continuity step; RV4 S1, `TESTS:2219`). No q-dependent TT term, and so no speed term |
| W2 in this class | Fails for every member (Lemma B2). So no TT seagull is Ward-fixed |

- The two TT masses are independent ultralocal constants per polarization (cubic symmetry; `vR9-9:16`).
- A q²-dependent TT seagull is a per-polarization speed counterterm.

## 4. Against the FIXED readings (`TESTS:4675-4677`)

**Worker reading: SPLIT-PRESENT (without pairing), scoped. Referee required, because the claim is class-wide in the TT vertex.**

What the reading covers:
- every first-order Ward-complete pair stress in 𝒲_V;
- scalar loop content on gapped (A_zz ≤ 0) edges, for any loop mass (proved);
- light external scalar matter, with its pole in the Lemma-M (de Donder) prescription.

What it rests on:
- |c_m − c_T| ≥ κ_lat|Ξ_box⊥| per species, with the numbers in §3.6.

What it does not cover:
- On the literal L edge the floor holds only for loop masses m ≥ 0.1 (checked). For light L species, L's doublers allow tuned members with Ξ = 0, so L is not covered.
- At lattice-scale external masses, two edge tunings per mass remove the split.
- The matter pole is not Ward-protected (Lemma B2), so the matter side is prescription-scoped. A prescription-independent split number does not exist in this class by the standard argument.

**With pairing: OPEN by the letter.**
- The TT shift is identically zero. The scalar matter shift 4κm²J₂ is nonzero (dD-M), so the split does not "vanish identically".
- It is about 1e-39 for physical matter.

**(a): no-go.** No second-order Ward-complete stress exists in the class of §1 (Lemma B2; to the referee). If "Ward-complete" in the FIXED readings means second order, the class is empty, and the reading is **OPEN**, with this no-go and the first-order results recorded.

**Against the expectation.**
- "SPLIT-PRESENT without pairing (birefringence alone forces one polarization off the matter cone)": SPLIT-PRESENT holds, but **not** because of birefringence, which is removable in 𝒲_V (§3.5). It comes from the box-transverse floor of the speed shift (§3.4).
- "With pairing, SPLIT-ABSENT for TT at matched unit-speed curves, with the scalar matter self-energy unpaired": as expected. TT is exactly on the bare cone, and the matter side is O(κm²).
- Not expected:
  - W1 constrains nothing in the pair channel;
  - no Ward identity reaches the TT channels at axial q;
  - the pair channel drops out of the Poincaré moments, so second-order completion is impossible whatever the pair stress.

## 5. Prices (named, not adopted)

- **P-TTV: the TT pair vertex is a law datum.** Its edge-transverse values are fixed by neither W1 nor any Ward identity (P1, W0). Against the source/action gate (`AX:187`). Dynamics are not supplied by Admissibility (`AX:116-130`).
- **Keeping light matter and the graviton on one cone without pairing.** One of:
  - a per-polarization TT speed counterterm (a q-dependent seagull);
  - a ≳ 1.5–8.7 × 10⁶ ℓ_P per species (the class floor), against the scale reference `AX:189-190`;
  - mixed L/G edge content tuned per mass. Interval cancellation is excluded for bosons alone (N\*).
- **Matter-pole gauge protection.** It needs W2, which needs exact Poincaré on the whole zone (Lemma B2 + Theorem E). Two ways to get it:
  - I1's complete tower, which makes the Qubit fibre `AX:47` infinite-dimensional (R8-2 option (c));
  - non-universal edge coupling (R7-1's χ-cut), so that edge energy does not gravitate.
- **The pairing unit P46** (`C5_S14_synthesis.md:177`). It buys c_T = 1 at one loop for both polarizations, with matched masses. It leaves 4κm²J₂, negligible, and the electron.

## 6. Strong-word check

- **"Proved":**
  - Lemma P1 (algebra);
  - Lemma W0 (representation theory);
  - Lemma B2 (in its moment form, given Theorem E);
  - the G floor (from A_zz ≤ 0);
  - the all-mass isotropy equivalence (Lerch);
  - "two tunings remove the split at lattice masses" (monotone, linear knob).
- **"Checked":**
  - every number in §§3.1, 3.4–3.6;
  - the L floor's sign for m ≥ 0.1 (fine quadrature of I over the edge⊥ B values);
  - the floor's failure on L at m = 0.01, with I(B) < 0 for B < 7e-4;
  - the b′ dependence of the G floor, with about 3% mask-discretization uncertainty.
- **"Exact":** W1 for the completion, and TT ≡ 0 for the paired unit at matched masses (PT, worker R10-5, algebra refereed).
- **"Not Ward-protected":** proved in the sense that W2 fails. The *size* of the matter pole's gauge dependence is not computed (suggested nonzero).
- **"Does not exist":** only for second-order Ward-complete stresses with universal forward T^{00} and T^{0i} on C² periodic bands, in moment form.
- **RECALLED:** Schwinger's moment conditions; Nielsen identities; the GW170817 band (as recorded in `C4_F1_report.md:103`).
- **Not claimed:**
  - fermion external matter;
  - k_z- or q-dependent TT vertices (the INV route escapes §3.4);
  - non-axis q;
  - a constructed isotropic member;
  - the matter pole in any gauge other than de Donder.

## 7. For the referee

1. **Lemma P1.** The conjugate-channel W1 with D(−q) = −D(q)*. Is "any smooth spatial pair kernel" a fair reading of "Ward-complete at first order"?
2. **Lemma W0.** The C_4v block structure, and the claim that contact terms with one TT index vanish in a cubic vacuum.
3. **Lemma B2.**
   - The pair channel drops out of K (F^{00}_pair = O(q²)).
   - Is the Poincaré moment form a legitimate necessary condition for W2 for scalars, as `vR12-1:15` has it for fermions?
4. **Class 𝒲_V's hypothesis (ii).** Box-exactness carried to edge k_z by k_z-independence. Is this fair, given that the INV vertex escapes it?
5. **The scope of SPLIT-PRESENT.** It is light external matter only, and the matter side is Lemma-M scoped. Should the reading instead be OPEN because Lemma B2 empties the second-order class?

## 8. Files

All in `S/scripts/`:
- `r135_w1_pair.py` and `.out`;
- `r135_moments.py` and `.out` (filtered to its own lines; it re-imports `r135_w1_pair`, which reprints that script's output);
- `r135_xi_split.py` and `.out`. Its L rows at m = 0.01 in block (b2), and the L "W_V bound" lines in block (b4), are superseded by `r135_L_small_m.out`: they are not floors;
- `r135_L_small_m.py` and `.out`;
- `r135_floor_bprime.py` and `.out`;
- `r99_profiles_copy.py`.

No downloads.
