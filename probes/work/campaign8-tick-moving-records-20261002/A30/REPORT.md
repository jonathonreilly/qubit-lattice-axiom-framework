*(Saved by the coordinator from the agent's final message; the agent's sandbox blocked it from writing REPORT.md.)*

# A30 report: the owner's black-hole instinct (I5) under Option R

**Scratch directory.** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A30/`
- Scripts: `q1_*.py`, `q2_*.py`, `q4_horizon.py`, `q6_heat.py`, `diag_flat.py`.
- Outputs `out_*.txt`, timings `time_*.txt`.
- `run.sh`: nice 10, four thread caps at 1, 55 s alarm. It refuses to start when the 1-minute load is 6 or more.

**Grades.**
- **EXACT**: proof or exact arithmetic.
- **CHECKED**: numeric check in a stated toy, with tolerance.
- **ARGUED**: reasoning without proof.
- **SUPPLIED**: a premise put in by hand.
- **COMPARATOR**: literature from memory, unverified, never adopted.

**Scope.**
- Every model is a supplied toy. I5 and the other instincts appear only as "if … then …".
- Option R's parts (ticks, SW, CL, compression) are A27's named conditionals.
- No git, no repo edits, no PRs, no review or audit lanes.
- A28 had no report when I read it. I used its partial outputs and did not redo its growth runs.

**Provenance.**
- While grepping `LOG.md` for "jam" and "black", I saw the coordinator's 1D pre-derivation (LOG lines 1222 and 1225). It gives the reflection formula with surface rate Γ and says "black only at k = π/2, Γ = 2t".
- So Step 1.2 was not derived blind to it. It agrees in the ε = 0 case.
- Nothing else was derived after seeing any pre-derivation.

---

## 1. Question

**The package (Option R, A27).**
- Records step on ticks by SW and settle clashes by CL.
- Unrecorded possibilities change smoothly under a covariant generator that holds recorded sites fixed ("compression"), so records act as walls and fixed weights.
- Records form on caught, settled things (A24), gated or not (A28).

**The instinct under test (I5).** "A fully recorded (jammed) region may behave like a black hole. Nothing can form or move inside it, so time stops there."

**Six questions.**
1. **Wall or absorber?**
   - Exact capture and reflection fractions in 1D.
   - Zeno effect, critical coupling, graded or porous surfaces.
   - A 2D disk's capture cross-section against the geometric one.
2. **Leak or seal?**
   - Can the odds of stepping into quiet emptiness be exactly zero?
   - Is that consistent with covariance, no signalling and Q7, and what does it cost?
   - If the jam leaks, how do rate and lifetime scale?
3. **What can "time stops" mean?** Does a record lock the field part of a site's possibilities?
4. **Horizon estimate (COMPARATOR).** When is a jam inside its own horizon, and what can the linear field route say?
5. **Information.**
6. **Evaporation.**

## 2. Answer (short, graded)

**Bottom line (conditional).** Under Option R a full jam is exactly a region where nothing can ever happen again, and it can be sealed. It is not black:
- it absorbs fast waves and reflects slow ones;
- it cannot be black at all energies;
- it absorbs only what its surface can record;
- it emits nothing thermal.

Its "stopped time" is the absence of record events. That matches gravitational clock-stopping only under readings the linear field route cannot reach.

**Q1. A grey absorber, never black at all energies.**
- **1D law [EXACT].** Semi-infinite recorded wall, capture rate Γ at the surface site, which also feels a field ε from the records.
  - Captured fraction: A(k) = 2tΓ sin k / (t² + ε² + Γ²/4 + 2tε cos k + tΓ sin k).
  - Reflected fraction 1 − A. Nothing passes through.
- **Critical coupling [EXACT].** Γ_c = 2|t + εe^{ik}|, which is Γ_c = 2t at every k when ε = 0.
- **At Γ_c, capture depends only on speed.**
  - A = 2u/(1+u) and reflected fraction (1−u)/(1+u), with u = v/(2t), where 2t is the lattice light speed.
  - EXACT for the uniform chain. CHECKED to 5.6e-15 for a staggered-mass (massive Dirac) chain, with a proof sketch.
  - So light-speed waves are swallowed (1 − A ≈ (E/4t)² for massless waves), and slow matter mostly bounces (A ≈ 2v/v_max).
- **Never black at all energies [EXACT].**
  - For any finite-range capture rule with energy-independent rates, |R| → 1 at both band edges (threshold theorem).
  - Black happens only at isolated energies.
  - A catch-first channel is black at all energies only if it is an exact copy of the incoming medium with no energy released, which is no catch.
- **Zeno [EXACT; CHECKED].**
  - Fast capture reflects: A ≈ 8t sin k/Γ.
  - Sure capture on every tick gives A(π/2) = x/(1+x/4)², which → 0 as the dose x = 2tτ → 0.
  - The per-tick black chance at the band centre is f_c = x/(1+x/4)², about the dose.
- **Records' own field [EXACT].** Blackness at any energy needs |ε| < t. In the J·SWAP toy, a jam of caught matter has ε = 2J, which caps capture at exactly 2/3.
- **Graded or porous surfaces [CHECKED].**
  - A capture layer L sites deep is near-black (A > 0.99) for k_min < k < π − k_min, with k_min·L ≈ 4–8.
  - That covers 13% of the band with one capture site and 93% at L = 64.
  - A 2D porous shell captures about 10% more than a smooth disk of the same outer radius at low k, with 35% fewer records.
- **2D disk [CHECKED].**
  - At critical capture, σ_abs/(2a) is 0.46–0.62 at k = 0.39, 0.91–1.05 at k = π/2, and 0.70–0.95 at k = 2.75 (a = 16 down to 4).
  - It always stays below the lattice width.
  - Wave packets reproduce the stationary capture to ≤ 2e-3 (1e-4 at Γ = 2) under both the smooth-rate and per-tick Option R dynamics.
- **What can be captured at all [EXACT under compression + F1].**
  - Only content that the surface's formation or step weights act on.
  - Never-recorded content meets a mirror or passes through; it is never absorbed. Examples: an F1 field, or light under a light-blind rule.

**Q2. Sealing is possible as a named choice; otherwise jams dissolve diffusively.**
- **The seal [EXACT; CHECKED ≤ 3e-32].**
  - With A27's content weight, step odds into a quiet neighbour are (c/z)[β + (α−β)|⟨r|n⟩|²].
  - They vanish iff β = 0 and the record content r is opposite to the quiet axis n.
  - With a quiet formation weight, jam plus emptiness is then a fixed point of all of Option R.
- **Other weights [EXACT].**
  - Fixed (blind) odds always leak.
  - The activity weight seals flat faces but leaks at concave notches (weight 1/6 in 2D) unless r = n.
- **Consistency [EXACT/ARGUED].**
  - Covariance: the seal is a relation between state contents, not a privileged possibility.
  - No signalling: the odds stay linear.
  - Q7: holds per A16 C4/C20.
- **Costs [EXACT; CHECKED].**
  - No record can ever cross quiet empty space; lone void records are frozen.
  - A6-type move clocks cannot run in the void.
  - The seal fails as soon as any jam content is off the quiet axis.
- **If it leaks [EXACT reduction; CHECKED].**
  - The record sector is exactly a classical exclusion process with claim chance p = cβ/z.
  - t_half ≈ 0.11R²/p in 3D and 0.24R²/p in 2D, so lifetime ∝ N^{2/3} ∝ M^{2/3} in 3D.

**Q3. "Time stops": four exact meanings, one open.**
- **EXACT under Option R.** Inside a full jam:
  - no record forms or moves;
  - matter possibilities never change;
  - nothing outside can ever change the interior;
  - the region's record-time budget is used up.
- **Does a record lock the field part? Under the axioms as written, yes [EXACT reading].**
  - The full one-site domain is M₂(C), and a locked site is pure, so nothing unlocked is left.
  - F1 can then only mean the field lives on unrecorded sites. A jam is then a hole in the field too.
  - Time stops in every sense. But the jam's content does not feed gravity, and field waves bounce off it.
- **If the owner enlarges the site domain** so a field sector is never locked, record-time stops but the lapse keeps running: N = 1 − U > 0 at linear order [ARGUED; linear part EXACT].
- **Not jam-specific [EXACT].** Under the sealing rules, a lone record in quiet void never changes either. What is specific to a full jam is interior isolation.

**Q4 (COMPARATOR arithmetic).**
- A grid-density ball (ρ = m/a³) is inside its horizon when R ≥ R_h = √(3c²/(8πGρ)). On a Planck grid, R_h = ℓ_P√(3m_P/(8πm)).
- One nucleon per site: R_h ≈ 1.2e9 ℓ_P ≈ 2.0e-26 m, M_h ≈ 14 kg. Any bigger jam is inside.
- One electron per site: M_h ≈ 580 kg.
- Planck-energy records: one site is already past the line.
- **The linear route can give:** the weak exterior field, γ = 1 bending, N = 1 − U (centre 1 − 3C/4), and where it fails (C ~ 1).
- **It cannot give:** horizons, β, or the strong interior.
- **ARGUED tension:** a rigid, stress-free jam is not a consistent source at second order.

**Q5. Captured things become permanent surface records in plain view [EXACT under Option R + Record].**
- Recorded: which sites, which locked contents, and, through layering, in what order.
- Not recorded: reflected waves, coherence, the field, tick times.
- **Contrast (COMPARATOR).** A GR horizon hides the interior, and no-hair leaves only M, J and Q.
- The jam is a library, not a vault. Its volume-law record count would clash with GR entropy bounds if it were inside its horizon.

**Q6. No evaporation by any thermal-like channel.**
- A sealed jam in quiet surroundings emits nothing [EXACT].
- No Option R channel gives emission with T ∝ 1/M [ARGUED].
- In an entangled vacuum, each surface lock releases about 0.21 J of non-thermal, power-law heat, and the jam grows [CHECKED; reproduces A28 c2 exactly].
- A leaking jam lives ∝ M^{2/3}, not ∝ M³ [CHECKED; COMPARATOR].

---

## 3. Derivation

### Step 0. Setup and named conditionals [SUPPLIED]

- **S0.1 Option R (A27).**
  - Records: a site plus a pure content |r⟩.
  - Between ticks: ρ → e^{−iH_R s}ρe^{iH_R s} with H_R = Q_R H Q_R.
  - On ticks, local linear instruments act:
    - formation: A9 Kraus operators P_k√F and √(1−F);
    - SW steps: K_y = √(c/z)·SWAP_{xy}√W_y, plus a stay outcome;
    - the CL claim rule.
- **S0.2 Jam.**
  - A set J of recorded sites; "full" means every site of a region is recorded.
  - The gate-open surface S is the set of unrecorded sites next to J.
  - Gated formation (A28) puts capture weights only on S.
- **S0.3 Capture channel.**
  - At s ∈ S the formation weight is F_s = f·P_s, where P_s projects on the matter-like possibility ("occupied" = −n).
  - No-record Kraus: 1 − κP_s, with κ = 1 − √(1−f).
  - Rate limit f = Γτ (A27 Step 8): H_eff = H − i(Γ/2)P_s.
  - Captured probability = norm lost.
- **S0.4 1D toy (one-excitation sector).**
  - H = −t Σ(|j⟩⟨j+1| + h.c.) + ε|1⟩⟨1| on sites j ≥ 1, with the jam starting at site 0.
  - J·SWAP toy over |0⟩^⊗ [EXACT bookkeeping]: r = n gives ε = 0; r = −n ("occupied", caught matter) gives ε = +2J relative to the bulk.
  - An XX-type toy gives ε = 0.
- **S0.5 Two readings of the axioms.**
  - **RA (as written):** the full one-site domain is M₂(C); a record locks one possibility; with Q1, shared possibilities live only on unrecorded sites.
  - **RB (enlarged; an owner decision):** a site also hosts a field sector that Record never locks (A23 F1, A25 payload).

### Step 1. Q1: wall or absorber

**1.1 Nothing passes through [EXACT].** The compressed generator never puts content into a recorded site (A27 Step 1a). The jam is a wall.

**1.2 Rate law [EXACT; CHECKED 3.4e-12].**
- Write ψ_j = e^{−ikj} + Re^{ikj} for j ≥ 1, with E = −2t cos k.
- The bulk equation extended to site 1 needs ψ₀ = 1 + R. The true equation at site 1 has no ψ₀ and carries V = ε − iΓ/2.
- Subtracting the two: t(1+R) + V(e^{−ik} + Re^{ik}) = 0. Hence:

  **R = −(t + Ve^{−ik})/(t + Ve^{ik})**, A = 1 − |R|² = 2tΓ sin k/(t² + ε² + Γ²/4 + 2tε cos k + tΓ sin k).
- Check: six packets evolved in real time under H_eff, compared with the packet-averaged formula.

**1.3 Critical coupling and black points [EXACT; CHECKED].**
- With X = |t + εe^{ik}|², dA/dΓ ∝ X − Γ²/4. So Γ_opt = 2√X and A_max = 2t sin k/(√X + t sin k).
- For ε = 0: Γ_c = 2t at every k, with A_max = 2 sin k/(1 + sin k). CHECKED: argmax within ±0.0005 at 200 values of k; A_max to 1e-6.
- |R| = 0 iff V = −te^{ik}. For fixed V this holds at most at one k. For ε = 0 that is k = π/2 with Γ = 2t (A = 1.0).

**1.4 At Γ = 2t, capture depends only on speed.**
- **Uniform chain [EXACT].** v = 2t sin k, so A = 2u/(1+u) with u = v/(2t).
- **Staggered-mass chain [CHECKED to 5.6e-15].**
  - On-site m(−1)^j; capture on the surface site with on-site −m; upper band; m = 0.05, 0.2, 0.6.
  - The same law holds exactly at Γ = 2t (`q1_dirac_b.py`). It fails at other Γ, with deviations of 0.12–0.47.
- **Proof sketch.**
  - y = t·g₁₁ obeys ty² − (E−m)y + t(E−m)/(E+m) = 0.
  - So |y|² = (E−m)/(E+m), and −Im y = sin k·√((E−m)/(E+m)) = u·E/(E+m), using E² − m² = 4t²cos²k.
  - Insert into the one-site-absorber formula A = −4 Im y/|1 + iy|² to get 2u/(1+u).
- **Massless waves near the band centre.** With sin δ = E/2t: 1 − A = tan²(δ/2) ≈ (E/4t)². At E/2t = 1e-3, 1 − A = 2.50e-7.
- **Slow massive waves.** A ≈ 2v/v_max: 0.0060 at v/2t = 0.003 and 0.18 at 0.1.
- **Packet check (m = 0.2):** 0.94834 = 0.94834.

**1.5 Threshold theorem: never black at all energies [EXACT].**
- Take capture rates on sites 1..L, energy-independent.
- Solving from ψ₀ = 0, ψ₁ = 1 gives ψ_j = P_j(E), polynomials in E = −t(z + 1/z) with z = e^{ik}.
- Matching to the bulk gives R = −z^{−2L} g(1/z)/g(z), with g(z) = ψ_{L+1} − zψ_L a Laurent polynomial.
- As z → ±1, |R| → 1 whatever the order of a zero of g there.
- CHECKED: A/k → 2tΓ/(t² + Γ²/4) for one site (0.9407 vs 0.9412 at Γ = 0.5). It stays finite (3.1–27) for every graded layer, so A ∝ k.
- The per-tick law below has the same limit: R → −1 as sin k → 0.

**1.6 Zeno, rate version [EXACT; CHECKED].**
- For Γ ≫ t: A ≈ 8t sin k/Γ.
- At Γ = 1000: 0.00797 vs 0.00800 (k = π/2) and 0.002361 vs 0.002364 (k = 0.3).

**1.7 Per-tick law [EXACT; CHECKED ≤ 2.5e-5].**
- One tick: ψ ← (1 − κ|1⟩⟨1|)e^{−iH₀τ}ψ. Below the aliasing bound 2tτ < π:

  **R = −1 + 2κ sin k/[tτ(1 − κ + κS(k))]**, S(k) = ½ + sin k/(tτ) + (i/π)PV∫₀^π sin²q·cot[tτ(cos q − cos k)]dq.
- **Proof sketch.**
  - The stationary solution with λ = e^{−iE_kτ} solves (λ − U₀)ψ = −κ⟨1|U₀ψ⟩|1⟩.
  - So ψ = sin(kj) − κa·G(λ)|1⟩, with the outgoing resolvent G and a = λ sin k/(1 − κ + κλG₁₁).
  - The only pole of G_{j1} in the upper half q-plane is q = k. Its residue gives the outgoing tail −ie^{ikj}/(tτλ).
  - λG₁₁ = S(k), using 1/(1 − e^{iθ}) = ½ + (i/2)cot(θ/2) plus the pole term.
  - As τ → 0 the law reduces to the rate law.
- **Band centre (the PV term vanishes).**
  - Sure capture, f = 1: R = (1 − tτ/2)/(1 + tτ/2), so A = x/(1 + x/4)².
  - As x → 0 this is Zeno: R → −e^{−2ik}, a hard wall one site out. CHECKED: A = 0.640, 0.331, 0.181, 0.0952, 0.0392, 0.0198 for τ = 0.5 down to 0.01.
  - Black iff κ = tτ/(1 + tτ/2), i.e. **f_c = x/(1 + x/4)²**. CHECKED: best f = 0.095, 0.180, 0.395, 0.640 at x = 0.1, 0.2, 0.5, 1.0, each with A_max = 1.0000.

**1.8 The records' own field limits blackness [EXACT; CHECKED].**
- From 1.3, a black point exists iff |ε| < t.
- Best capture over all k and Γ: 0.80 at |ε| = 1.5t, and exactly 2/3 at |ε| = 2t (k = 2π/3, Γ = 2√3 t).
- So a J·SWAP-toy jam of caught matter (ε = 2J) is at most two-thirds dark.

**1.9 Catch-first capture (A24 C1 structure) [EXACT; CHECKED].**
- Model: the surface couples (g) to an emission chain with hopping t_C and on-site −V (energy V released).
- This gives Σ(E) = g²g_C(E+V), and R = −(t + Σe^{−ik})/(t + Σe^{ik}).
- **Black at every energy** requires Σ(E) = −te^{ik(E)} across the band. Matching the branch points and the modulus forces V = 0, t_C = t and g = t. That is plain transmission into a copy of the medium: no catch.
- **Otherwise:** with (g, t_C, V) = (1, 1, 0.5), A = 0.052 / 0.78 / 0.98 / 0 at k = 0.01 / 0.3 / π/2 / 3.0, and A/k → 5.3. With (1, 1, 1): A = 0.034 / 0.64 / 0.93 / 0.

**1.10 Graded layers (effective-medium stand-in for a porous surface) [CHECKED].**

| Layer depth L (p = 2, best G_max) | Window where A > 0.99 | Share of the band (in k) |
|---|---|---|
| 1 | [1.37, 1.77] | 0.13 |
| 4 | [0.71, 2.43] | 0.55 |
| 16 | [0.30, 2.85] | 0.81 |
| 64 | [0.11, 3.04] | 0.93 |

- k_min·L = 3.95, 4.72, 5.69, 6.83, 8.29 for L = 8, 16, 32, 64, 128.
- Near-black needs a capture layer deeper than a few wavelengths. Slow waves still reflect.

**1.11 2D recorded disk [CHECKED].**
- **Model** (`q1_2d.py`).
  - 128² periodic lattice; recorded sites removed (walls).
  - Capture rate Γ on unrecorded sites touching records (gated).
  - Stationary plane-wave scattering at k = 2πm/128; a 36-site absorbing frame takes up the scattered wave (a numerical device).
  - σ_abs = ΣΓ|ψ|²/(2t sin k).
- **Validation.** A full-height recorded column reproduces the exact 1D law to ≤ 0.001 for k ∈ [0.39, 2.75], oblique incidence included.

**σ_abs/(2a) at Γ = 2t**

| a (lattice width) | k = 0.39 | 0.59 | 0.79 | 1.18 | 1.57 | 1.96 | 2.36 | 2.75 |
|---|---|---|---|---|---|---|---|---|
| 4 (9) | 0.622 | 0.730 | 0.823 | 0.967 | 1.053 | 1.111 | 1.112 | 0.950 |
| 8 (17) | 0.532 | 0.659 | 0.761 | 0.894 | 0.969 | 0.995 | 0.955 | 0.777 |
| 16 (33) | 0.459 | 0.588 | 0.690 | 0.836 | 0.914 | 0.943 | 0.899 | 0.705 |

- **Other capture rates.** Γ = 0.5t peaks at 0.60–0.73. Γ = 8t (Zeno side) peaks at 0.68–0.85.
- **Against the lattice width.** The best is 0.99 (a = 4), 0.94 (a = 8) and 0.91 (a = 16).
- **Extinction.** Absorbed plus scattered is 2.1–2.7 × 2a. The largest disk at mid-band gives 2.15, close to the large-body value 2 (COMPARATOR).
- **Wave packets** (`q1_2d_packet.py`; uniform in y, Gaussian in x):

| k, Γ | Captured, rate dynamics | Captured, per-tick Option R (τ = 0.05) | Stationary prediction |
|---|---|---|---|
| π/2, 2 | 0.121085 | 0.121093 | 0.121103 |
| 0.589, 2 | 0.082296 | 0.082321 | 0.082316 |
| 2.356, 8 | 0.078748 | 0.078910 | 0.078749 |

  The 0.2% per-tick deviation at Γ = 8 is the expected Trotter size.
- **Porous shell.** Core radius 8 plus a shell to radius 16 with density falling outward: 515 records, against 797 for the full radius-16 disk.
  - Porous σ_abs/32: 0.503, 0.652, 0.841, 0.934, 0.902, 0.707 at k = 0.39–2.75 (3 seeds).
  - Smooth radius-16 disk: 0.459, 0.588, 0.773, 0.914, 0.934, 0.705.

**1.12 What can be captured at all [EXACT under compression + F1].**
- Only content that the surface's formation or step weights act on.
- Never-locked content is never captured. Under RA it lives on unrecorded sites and meets a mirror (|R| = 1). Under RB it crosses the jam.
- This covers an F1 field, and light under a light-blind rule (C15).
- If gated formation can lock light-like content next to records, the jam can be dark to light. A jam is dark only to what it can record.

**1.13 Energy cost of capture [EXACT via A24 E5].**
- A direct lock at the surface injects the depth below the band centre: 2t cos k per capture (ε = 0).
- That is zero exactly at the black point k = π/2.
- Elsewhere it is a ghost source in the field route (A23 f). Catch-first moves the cost into emission.

### Step 2. Q2: leak or seal

**2.1 Inside a full jam nothing can happen [EXACT].**
- SW and CL need an empty neighbour; formation needs an unrecorded site.
- Q_R H Q_R on the interior is a number: covariant terms a + bσ·σ compress to a + b·n_r·σ.

**2.2 Step odds [EXACT].** The odds of stepping into y are (c/z)tr(W_yρ_y).
- Blind weight: c/z > 0, so it always leaks.
- Content weight: (c/z)[β + (α−β)⟨r|ρ_y|r⟩].

**2.3 Seal theorem [EXACT; CHECKED].**
- **Hypotheses:**
  - (i) β = 0;
  - (ii) every jam record has r = −n;
  - (iii) the unrecorded region is |n⟩^⊗;
  - (iv) the formation weight annihilates the quiet star marginal (A9).
- **Conclusion:** the snapshot is a fixed point of all of Option R.
- **Proof.**
  - Covariant bulk terms fix |nn⟩.
  - Boundary terms compress to a + b(−n)·σ_y, which is diagonal in the n basis.
  - Step odds (c/z)α|⟨−n|n⟩|² = 0; formation odds 0; the stay and no-record operators act as the identity. ∎
- **Check** (`q2_seal.py`; 10-qubit compressed J·SWAP chain, t ∈ [0, 12], 49 sampled times):

| Jam content r | Content-weight odds | Activity odds | Formation odds | How far the emptiness moved |
|---|---|---|---|---|
| −n | ≤ 2.7e-32 | ≤ 2.7e-32 | ≤ 2.7e-32 | 1.3e-15 |
| +n | 1.000 | 0 | 0 | — |
| off-axis, θ = π/2 | 0.853 | 0.063 | 0.511 | 0.955 |
| off-axis, θ = 0.99π | 7.5e-4 | 1.2e-4 | 1.8e-3 | — |

- This agrees with A28 c5: zero formation for r = ±n, 6.6e-2 off axis.

**2.4 Activity weight [EXACT].**
- A recorded neighbour compresses P_singlet(y,z) to ½|r⊥⟩⟨r⊥|_y.
- Flat faces are sealed for any r.
- At a 2D notch, the weight on |n⟩ is 1/6 for r = −n and 0 for r = +n.
- A box has no outside site touching two box sites, so a box is sealed. Lattice balls have notches and leak there [ARGUED: holes then wander inside, A4-like].

**2.5 A record-set alternative [EXACT].**
- Rule: "step only into a site touching ≥ 2 records".
- It seals flat faces, is covariant, and does not depend on the possibilities at all.
- Cost: isolated records never move.

**2.6 Consistency.**
- **Covariance [EXACT].** SW is covariant for any α, β (A27 Step 3). The seal is a relation between state contents.
- **No signalling [EXACT].** Odds are linear (A9 Th.1; A5 T1.2; A27's c4 checked CL to ≤ 2e-16).
- **Q7 [ARGUED].** Holds per A16 C4/C20: records cut to their sites set the offer; unrecorded possibilities enter only linearly.

**2.7 Costs [EXACT, plus ARGUED readings].**
- **No record ever enters quiet emptiness.** Lone void records are frozen. A6's move clock cannot run in the void.
- **The seal is fragile.** It needs every jam content antipodal to n (2.3).
- **The β = 0 stay branch weakly measures matter-like neighbours.** The coherence factor is 1 − cα/12 per tick (A27 Step 4). That measurement is exactly the capture channel of Step 1.
- **Capture by swap.** A step into an excitation swaps the record outward and the excitation inward. On a flat face the excitation is caged, and gated formation then locks it. A sealed jam is a pure accretor: it never loses a record.

**2.8 Leak rate and lifetime [EXACT reduction; CHECKED].**
- **Reduction.** For β > 0 in quiet surroundings, √W_y|n⟩ = √β|n⟩. Vacated sites hold |n⟩ again. The record pattern is then exactly a classical CL exclusion process with claim chance p = cβ/z.
- **Gross leak [EXACT].** Per surface record per tick: p times the number of quiet empty neighbours, less clashes.
- **Lifetime (8 seeds, `q2_dissolve.py`).**
  - 2D: t_half·p/R² = 0.231, 0.222, 0.249, 0.247, 0.235, 0.249 for R = 3–16.
  - 3D: 0.136, 0.131, 0.115, 0.115, 0.112 for R = 2–8.
  - So t_half ≈ 0.11R²/p in 3D (∝ N^{2/3}) and ∝ N in 2D.
- A28's dissolved V3 disc is consistent with this.

### Step 3. Q3: what "time stops" can mean

**3.1 Four exact senses [EXACT under Option R].**
- **T1.** No record events inside a full jam.
- **T2.** Matter possibilities never change there.
- **T3.** The interior is isolated: no influence crosses into it in the record or matter sectors.
- **T4.** Under "time = accumulation of records" plus permanence plus one record per site, the region's record-time is at its maximum (A4 3.1).

**3.2 Reading RA: a record locks the field part too [EXACT reading; ARGUED physics].**
- The texts:
  - Qubit: "The full one-site possibility domain has algebraic presentation M₂(C)".
  - Record: a record "locks exactly one admissible local possibility".
- So a recorded site is pure, with nothing unlocked, and by Q1 it shares nothing.
- A23's F1 ("records never lock them") can then only mean that the field lives on unrecorded sites.
- **Consequences:**
  - no field inside a full jam;
  - field waves meet compression walls and reflect;
  - the jam's content enters the field at most through surface terms, so it does not gravitate as ordinary mass-energy (compare A6/A8's radius-scaled absorber strength).

**3.3 Reading RB: the field part stays unlocked [ARGUED; linear part EXACT].**
- This needs a site domain larger than one qubit (A25's payload; A21 C22 escape 3, which touches the Qubit axiom).
- The field then crosses the jam. If F3 counts locked contents, the jam sources the lapse: N = 1 − U, with U at the centre 3/2 of U at the surface.
- So N > 0 at linear order.

**3.4 Which answer needs which reading**

| Claim | Needs | Grade |
|---|---|---|
| No record forms or moves inside | Option R + Record (one per site) | EXACT |
| Matter possibilities frozen inside | A27's compression reading of "kept" | EXACT |
| Interior never influenced (record and matter sectors) | Compression + SW/CL locality | EXACT |
| Record-time budget exhausted | Owner's "time = accumulation of records" + permanence | EXACT |
| Field absent inside; jam reflects field waves; content does not gravitate locally | RA + Q1 + F1 | EXACT reading, ARGUED physics |
| Lapse runs inside, N = 1 − U > 0 | RB + A23 F1–F4 + F3 counting locked contents | ARGUED (linear EXACT) |
| Lapse → 0 somewhere | RB + strong-field dynamics (A23 D20 open) | OPEN |

**3.5 Not jam-specific under sealing rules [EXACT].**
- A lone record in quiet void also never changes. What is jam-specific is T3.
- So A27 Step 10's "time stops there (EXACT)" is exact for the record and matter sectors only; under RB it does not cover the field.

**3.6 Comparator.** This matches GR's external "frozen star" picture (Zel'dovich–Novikov), not the infaller's continuing proper time [COMPARATOR].

### Step 4. Q4: horizon estimate (COMPARATOR, flagged)

**4.1 Compactness [EXACT arithmetic; constants COMPARATOR].**
- C = 2GM/(Rc²) = (8π/3)(Gρ/c²)R², with ρ = m/a³.
- C ≥ 1 for R ≥ R_h = √(3c²/(8πGρ)). On a Planck grid, R_h = ℓ_P√(3m_P/(8πm)) and M_h = 0.1727·m_P^{3/2}m^{−1/2}.
- Since C ∝ R², every larger jam is inside.

**4.2 Numbers (`q4_horizon.py`)**

| Mass per site | R_h | Number of sites | M_h | GR comparator: Hawking T, lifetime |
|---|---|---|---|---|
| electron | 5.34e10 ℓ_P = 8.6e-25 m | 6.4e32 | 581 kg | 2.1e20 K, 1.7e-8 s |
| nucleon | 1.25e9 ℓ_P = 2.0e-26 m | 8.1e27 | 13.6 kg | 9.0e21 K, 2.1e-13 s |
| m_P | 0.35 ℓ_P | < 1 | — | — |
| (π/2)E_P (A24's unsettled sharp-record depth) | 0.28 ℓ_P | < 1 | — | — |

- An Earth-mass jam at one nucleon per site: R = 1.5e-18 m, against r_s = 8.9 mm (C ≈ 6e15).
- At nuclear density the same formula gives R_h ≈ 6 km.

**4.3 What the linear route can say.** Under A23/A26 with F1–F4, G1, F6 and K1, and reading RB:
- the weak exterior field n = −U, h_ij = 2Uδ_ij;
- γ = 1 bending;
- universal fall of one-site masses;
- N = 1 − U (1 − C/2 at the surface, 1 − 3C/4 at the centre);
- where it breaks: U ~ 1, i.e. R ~ R_h.

**4.4 What it cannot say.**
- Horizons and trapped surfaces. Even extrapolated, N = 1 − U vanishes at GM/c², not at GR's isotropic horizon GM/(2c²) (COMPARATOR).
- β and second order (A23 D20).
- The strong interior.
- Hawking emission.

**4.5 Rigid-jam tension [ARGUED].**
- At second order a static self-gravitating body needs stresses with ∂_jT^{ij} = −ρ∂_iU.
- Records carry no momentum or stress (A7/A13); the lattice simply holds them.
- So source conservation (A23 D13/D17, A26 Laue) fails unless the lattice's holding force enters the source.
- In GR no static fluid ball exists below (9/8)r_s (Buchdahl, COMPARATOR).
- Under RA the premise fails altogether, since the content does not source the field (3.2).

### Step 5. Q5: information

**5.1 What is recorded [EXACT under Option R + Record].**
- For each capture: a surface site and its locked content (one menu outcome; at most 1 bit for a two-outcome menu).
- Layering also records the accretion order: later captures sit further out.
- These are permanent, readable records. An outside reader of records can in principle learn the jam's shape and growth history, where each capture happened, and what each lock selected.

**5.2 What is not recorded [EXACT].**
- The reflected fraction 1 − A.
- Coherence and alternative outcomes (removed by the Lüders cut).
- Momentum or internal state, unless the menu offers them.
- The field.
- Tick numbers: timing survives only as order.

**5.3 Contrast with a GR horizon [COMPARATOR].**
- **GR:**
  - nothing escapes classically;
  - no-hair leaves M, J and Q;
  - the quantum fate of information is debated (Page curve);
  - S = A/(4ℓ_P²).
- **The jam:**
  - shows its captures in plain view;
  - has no information puzzle of its own (coherence is cut at every record formation, not specially at jams);
  - its surface layer holds about A/a² records (area scaling up to O(1));
  - its total is about V/a³ (volume law).
- If a jam were inside its horizon, the volume-law count would exceed the Bekenstein bound [ARGUED; COMPARATOR].

### Step 6. Q6: evaporation

**6.1 A sealed jam in quiet surroundings emits nothing [EXACT].** The snapshot is a fixed point (2.3). The time-independent compressed generator has the quiet state as an eigenstate.

**6.2 No channel tracks M [ARGUED].**
- Every surface process is star-local, so nothing can produce emission with T ∝ 1/M.
- Capture is irreversible, so Kirchhoff balance between absorption and emission does not apply. A sealed jam is a perfect sink at "zero temperature".
- GR needs T_H > 0 for the generalized second law (COMPARATOR). Option R's arrow is record permanence itself.

**6.3 Formation heat in an entangled vacuum [CHECKED].**
- **Toy** (`q6_heat.py`): free fermions, half-filled chain; one sharp two-outcome lock of the surface site; the wall then moves out by one site.
- **Injected energy.** 0.848852 J under the old generator and 0.208312 J above the new walled ground state (M = 200); 0.211227 J at M = 800.
- **Independent check of A28.** These match A28 `out_c2_edge_rank` to every printed digit, from independent code.
- **Spectrum not thermal.**
  - Define T_loc = |ε − ε_F|/ln(1/n − 1). For a thermal spectrum it would be constant.
  - Instead it rises from 0.0048 to 0.12 for particles and from 0.0043 to 0.18 for holes.
  - 0.47 of the 0.74 created particles lie within 0.01 of the Fermi level: a soft, power-law, quench-type spectrum (COMPARATOR: Anderson orthogonality).
- **Growth.** A Dirac-type sea has no quiet surface weight (A9 n4), so gated formation keeps firing and the jam grows. A28's V0/V1 box fills are consistent with this.

**6.4 Other candidate channels [ARGUED].**
- **Moving-mirror production** (COMPARATOR: Fulling–Davies) needs exponential recession. A jam surface moves only by discrete record events, and outward when growing.
- **No-record back-action** heats a non-quiet neighbourhood at a rate set by the measurement strength, not by M.
- **Leaking records** leave as classical dust.

**6.5 Scaling against Hawking [CHECKED; COMPARATOR].**
- Sealed jam: infinite lifetime.
- Leaking jam: t ≈ 0.11R²/p ∝ M^{2/3}/(cβ). This is a lattice process with no G in it.
- Hawking: t ∝ M³ (COMPARATOR).
- For the 14 kg nucleon jam, GR predicts evaporation in 2e-13 s.
- A16 C9's older crowd-tilt jams (lifetime ∝ N) follow a different rule.

---

## 4. Checks

**How runs were made.**
- Every run went through `run.sh`: nice 10, OMP/OPENBLAS/MKL/VECLIB = 1, a 55 s alarm, and a 1-minute load guard below 6.
- The guard refused one attempt at load 6.75; it was rerun later.
- Longest run 5.8 s; largest peak RSS 251 MB.
- `diag_flat.py` (frame tuning; three runs of a few seconds) was started directly with nice 10 and the thread caps. Loads measured just before and after were 2.3 and 4.4; the scripted guard was not used for those three.

| Script | What it checks | Key numbers | Tolerance | Time, RSS |
|---|---|---|---|---|
| `q1_1d.py` | Rate and per-tick laws vs packets; critical Γ; Zeno; threshold; f_c | Packet vs formula ≤ 3.4e-12 (rate), ≤ 2.5e-5 (per tick); Γ_opt = 2 ± 0.0005 | 1e-10; 1e-4 | 4.6 s, 77 MB |
| `q1_graded.py` | Graded layers; transfer matrix self-checked against the closed form to 1e-12 | Step 1.10 | exact | 0.3 s, 27 MB |
| `q1_eps.py` | Surface-field cap; catch-first Σ(E) | max A* = 0.666667 at \|ε\| = 2t; degenerate match black; threshold law returns for V > 0 | 1e-12 | 0.1 s, 27 MB |
| `q1_dirac.py`, `q1_dirac_b.py` | Massless vs massive capture; speed-only law | tan²(δ/2) to all digits; \|A − 2u/(1+u)\| ≤ 5.6e-15 for m = 0.05–0.6 | 1e-10 | 0.7 s, 251 MB |
| `q1_2d.py flat` | Solver validation on a flat face | ≤ 0.001 vs the 1D law | 0.002 | 0.8 s, 119 MB |
| `q1_2d.py disk 4/8/16` | σ_abs/(2a) at three Γ | Table in Step 1.11 | ~0.2% (frame) | ≤ 3.0 s, ≤ 131 MB |
| `q1_2d.py porous 2.0` | Porous shell vs smooth disks | Step 1.11 | seed spread ±1 | 3.9 s, 245 MB |
| `q1_2d_packet.py` | Packets vs stationary | Ratios 0.9997–1.0020 | 0.5% | ≤ 5.8 s, ≤ 126 MB |
| `q2_seal.py` | Seal conditions; notch | ≤ 2.7e-32 / 1.000 / off-axis nonzero / 1/6 | 1e-14 | 0.4 s, 60 MB |
| `q2_dissolve.py 2`, `q2_dissolve.py 3` | Leak lifetime | t_half·p/R² ≈ 0.24 (2D), 0.112 (3D) | 8-seed standard error | ~3 s each |
| `q4_horizon.py` | Horizon arithmetic | Step 4.2 | exact arithmetic | 0.2 s |
| `q6_heat.py` | Formation heat; thermality | Matches A28 c2; T_loc rises 25× | 1e-12 | 2.0 s, 112 MB |

**First-run problems (fixed).**
1. **Absorbing frame.**
   - A 24-site frame let the shadow wave leak around the periodic box: the flat face read 0.99638 against 1.
   - Strong frames instead reflect slow waves.
   - I chose a 36-site frame, validated to ≤ 0.2% for k ∈ [0.39, 2.75], and restricted the 2D scans to that range.
2. **Packet envelope.** The first packet was cut at x = 0, giving a 1.7% mismatch. A periodic envelope fixed it (1e-4).
3. **Dissolution seeds.** Moved from 1 seed to 8.

**Not run.**
- 3D cross-sections: needs an iterative solver at 48³–64³.
- A28's grown record patterns as 2D targets: cheap, but A28 has not saved its patterns.

## 5. Real-physics match

**Comparators (from memory, unverified, none adopted).**
- **Threshold law and quantum reflection.** Slow ultracold atoms reflect from surfaces (Shimizu 2001).
- **Impedance matching and coherent perfect absorption** (Chong–Ge–Cao–Stone 2010). The black-hole membrane paradigm treats the horizon as a 377 Ω resistive surface matched to vacuum. Γ_c = 2t is the lattice match, exact only as u → 1.
- **Graded absorbers.** Complex absorbing potentials and perfectly matched layers (Bérenger) are reflectionless only for wavelengths shorter than the layer.
- **Black-hole absorption.**
  - Geometric cross-section 27π(GM/c²)².
  - Low-frequency massless cross-section → horizon area 16π(GM/c²)² (Das–Gibbons–Mathur).
  - Slow massive capture σ ≈ 16π(GM)²/(c²v²).
  - **Opposite low-energy behaviour:** without gravity, a jam's capture vanishes for slow waves.
- **Extinction ≈ 2 × geometric** for large absorbers.
- **Black-hole structure and thermodynamics.**
  - No-hair; S = A/4ℓ_P²; the Bekenstein bound.
  - Hawking T and lifetime ∝ M³.
  - Buchdahl's (9/8)r_s.
  - The frozen-star picture.
- **Emission mechanisms.**
  - The moving mirror (Fulling–Davies).
  - Local-quench spectra.
  - The symmetric-exclusion hydrodynamic limit.

**If jams are to stand for astrophysical black holes.**
- **Matches:**
  - absorption is best when impedance-matched and near-geometric at mid-band;
  - the external frozen look;
  - a surface record count that scales like area.
- **Mismatches:**
  - slow matter bounces;
  - field waves are never absorbed;
  - no Hawking emission;
  - records grow with volume;
  - "time stops" refers to record events, not the lapse.

**Falsifiers.**
1. **Echoes.** A partly reflecting surface (A < 1) near horizon scale gives gravitational-wave echoes. None are confirmed (COMPARATOR: Cardoso–Pani; LIGO/Virgo searches).
2. **Surface emission.** Catch-first accretion must re-emit the infall binding energy at the surface. Sgr A* and M87* limits disfavour that (COMPARATOR: Broderick–Narayan), unless the jam is inside its own horizon, which the linear route cannot show.
3. **Slow-matter capture.** A ≈ 2v/v_max, against black holes' efficient capture of slow matter.
4. **Gravitational waves** cross a jam (RB) or bounce off it (RA). Black holes absorb them (tidal heating, COMPARATOR).
5. **Small jams.** A sealed 14 kg jam is stable; a GR 14 kg hole evaporates in 2e-13 s.
6. **Entropy.** Volume-law records against the Bekenstein bound.
7. **Leaking jams** last ∝ M^{2/3}. Leaked records become void dust and inherit A14's bound (u∞ ≲ 1e-47 per Planck site, if records are walls for light).

## 6. Open edges

1. **Many-body capture in an entangled vacuum.**
   - A Dirac-type sea has no quiet surface weight (A9 n4), so the jam keeps recording its own vacuum.
   - The single-particle black window (Γ = 2t, 1 − A ≈ (E/4t)²) competes with that.
   - Needs a fermionic Gaussian instrument toy with a moving wall.
2. **Realistic porous surfaces.** Run A28's grown patterns, or DLA-like clusters (A8), through `q1_2d.py`. Do grown surfaces become broadband-dark?
3. **3D cross-sections** with an iterative solver.
4. **Joint per-site instrument** (A27 open edge 1): formation, a β = 0 claim, or nothing. Check that the combined damping obeys Steps 1.2–1.7 with f_total.
5. **Owner decisions** (axioms' register; none adopted):
   - (i) One qubit's possibilities per site (a full region then has nothing left for gravity, so everything stops there), or an added never-recorded part (gravity's clocks keep running inside)?
   - (ii) May a record step only into a neighbour that already holds something like its own content? This seals jams, but lone void records never move.
   - (iii) May light-like possibilities be recorded next to existing records? A jam is dark to light only if so.
6. **Second order.** β, constraint closure, and the stresses a static rigid jam needs (A23 test 5).
7. **Accretion energy.** A direct capture costs 2t cos k (zero at the black point). Catch-first sends the binding energy out. Quantify the surface luminosity per accreted mass under the field route and compare with Broderick–Narayan-type limits.
8. **Is A = 2u/(1+u) at Γ = 2t a general matched-lead theorem** for one-site absorbers? Tested on two leads so far.

## 7. Plain-language summary

If the "Option R" rules hold, a region where every spot holds a record is a place where nothing can ever happen again: no new record can appear inside, none can move, and nothing from outside can reach in. With one particular choice of how records step (a record may only step into a neighbouring spot that already holds something like itself), the region also never loses records into empty surroundings and lasts forever. The price is that a lone record in empty space can never move either. But the region is not black the way a black hole is. Things that hit its edge are caught only part of the time: things moving near the grid's top speed are caught almost always, slow things mostly bounce off, and no setting of the edge catches everything at every speed. A rough, spongy edge helps a little, but not for the slowest things, and anything that records never lock, such as a never-recorded "stretch" field for gravity, is never caught at all. Whatever is caught becomes a permanent record on the edge in plain view, so the region keeps a readable log of what fell in, where a black hole hides it. A sealed region gives off nothing and never wears away, while a region whose records can wander off falls apart in a time that grows with its size far more slowly than a black hole's would. Whether its stopped time also means that clocks stop in the gravity sense depends on a choice for you. If each spot holds only one set of possibilities, a full region has nothing left to carry gravity, so everything stops there. If each spot can also hold a never-recorded part for gravity, clocks there keep running, only slower.

---

## ERRATA from the fourth hostile review (A34/REVIEW.md), added by the coordinator

- Line ~108: the seal fails for any content 'not opposite to the quiet axis' (+n leaks too), not just 'off axis' (C68).
- Line ~422: R_h at nuclear density ≈ 25 km, not 6 km (C69).
- The 'speed-only' law holds at Γ = 2t for both terminations and both bands. But Γ = 2t is optimal only for massless waves; massive waves are best caught at Γ = 0.67–6.0 (C65).
- 'Lapse keeps running, N = 1 − U > 0' is linear-order only. The centre lapse 1 − 3C/4 < 0 for C > 4/3, so it is open in the black-hole regime (C66).
