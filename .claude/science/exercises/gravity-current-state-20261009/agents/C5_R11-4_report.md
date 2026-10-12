# C5 R11-4 report: box bodies in a curved field (γ, von Laue, geodetic precession, spin–curvature force; d = 3)

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 18:36Z to about 19:00Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R11-4/`. Scripts and outputs in `S/scripts/` (`OMP_NUM_THREADS=2`, each under 10 s):
- `r114_bsector.py` → `r114_bsector.out`: Lemma KB3; the d = 3 box-sector stress on the bound triplet; Ward identities; moments; von Laue; uniqueness rank; spin–orbit coefficient c(v); frame dragging; a random Riemann-type improvement;
- `r114_dixon.py` → `r114_dixon.out`: every first moment against the flat Dixon pole–dipole stress (Newton–Wigner condition);
- `r114_twobody_P0.py` → `r114_twobody_P0.out`: the actual two-body triplet at P = 0. Kinetic pressure against interaction stress (von Laue with real constituents), the constituent-only comparator, and the constituent-dust quadrupole;
- `r114_shell.py` → `r114_shell.out`: the transition shell for moving bound triplets, as a function of binding.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: C5 method `:2302-2320`; round 6 onward results (`:3285-3345`, `:3396-3445`, `:3483-3575`, `:3793-3960`, `:4014-4077`); Round 11 `:4078-4282`, R11-4 at `:4192-4214`.
- `agents/C5_S11_synthesis.md:1-120,280-330`; `SUMMARY.md:534-635` (§§21–24).
- `C5_R9-10_report.md` in full; `C5_R9-10_referee_verdict.md` (`vR9-10`); `C5_R9-2_report.md:1-200`; `C5_R9-2_referee_verdict.md` (`vR9-2`); `C5_R9-6_report.md:1-140`; `C5_R9-6_referee_verdict.md` (`vR9-6`); `C5_R8-2_report.md:60-175`; `scripts/C5/R9-6/r81_common.py`.

**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED.

---

## 0. In plain words

- **On the box domain, a bound spinning body couples to curved space exactly as GR's spinning test body does, to dipole order.** For the d = 3 bound triplet of R9-6's law, the total stress, the energy dipole, the momentum-density moments and the first moments of the spatial stress are all fixed by four things: H, P, the boost K and the angular momentum J. Any symmetric stress that conserves momentum box-to-box and has those first moments gives the same values. They equal the flat-space Dixon pole–dipole stress of a free spin-1 particle of mass M_b, with the Newton–Wigner spin condition (proved, Theorem PD; checked to 1e-14).
- **Von Laue holds exactly.** For a bound body at rest, ∫T^{ij} = 0 for every binding and every spin state. In motion ∫T^{ij} = P^iP^j/H. The kinetic pressure of the constituents is not small: tr Π_kin/M_b = 0.49, 0.62 and 0.80 at binding fractions 0.05, 0.15 and 0.30. The interaction stress cancels it to 2e-11 (checked).
- **The effective γ is binding-independent and equals the field's γ** at linear order. In field (ii) every bound body follows a = −∇Φ(1 + γv²) + 2(1 + γ)(v·∇Φ)v (proved).
  - Comparator: if h_ij coupled only to the constituents, the passive weights would differ by η = 0.08–0.19 between binding fractions.
- **Geodetic precession is 3/2.** The spin–orbit Hamiltonian is H_SO = c(v) S·(∇Φ × v), with c(v) = Γ/(Γ+1) + γ, exact in v at linear order in Φ.
  - At v → 0 this gives c = 1/2 + γ = 3/2, the Gravity Probe B value. Checked: c = 1.500000138504 at |P| = 0.001.
  - At γ = 1, c(v) = (2Γ+1)/(Γ+1) at every v; that is the GR formula as recalled.
  - The ½ comes from the boost's spin term, whose coefficient α = 1 is forced by the Poincaré algebra (R9-6). The γ comes from the spin carried by the spatial stress's first moment, which is fixed by J_T = J and the Ward identity.
- **Spin–curvature (MPD) force and frame dragging, to dipole order.** The bound body's dipole-order stress is the Dixon stress, so it obeys the linearized MPD dynamics. In canonical variables the force is −∇[c(v) S·(∇Φ × v)]. A gyroscope at rest in a gravitomagnetic field has H = −½(∇×w)·S (ratio 1.000000000000), i.e. Schiff's frame-dragging rate.
- **What the box law does not fix: the body's quadrupole.** The second moment of T⁰⁰ (where the interaction energy sits inside the body) can be changed by exact improvement terms. These keep every property of (a) and every dipole-order number above. So the tidal quadrupole coupling and the spin-induced quadrupole (GR's body-dependent C_ES² coefficient) are not determined by the box law's Poincaré data. Two natural realizations differ by Q_xx − Q_yy ≈ 5 lattice units (checked). This is beyond the registered clauses (MPD is dipole order); it is reported as a finding and a named price.
- **The shell.** Everything above holds for |P| < Π₁ = 0.6 (lattice units). Bodies at rest are never in the shell, so the shell source contributes exactly zero to von Laue at rest, for every binding (proved).
  - Moving bound triplets entering the shell lose Lorentz form (E_b − √(M_b²+P²) = 2e-3 to 9e-2). Their gravitating momentum departs from P by 0.16 to 1.5, and the shell source norm is 2e-2 to 0.20, growing with binding.
  - The triplet unbinds inside the shell, by |P| ≈ 0.8–0.9 (checked).

**Against the FIXED readings (`TESTS.md:4211-4213`): worker reading PASS WITH SCOPE** (d = 3; two-body bound triplet sector ℬ inside the box domain; linear order in h; dipole order; prescribed static fields). The four clauses:
- (a) met at the same level as R9-10's refereed d = 2 construction: explicit T⁰⁰, and a constructive existence proof of the fluxes;
- von Laue exact;
- γ binding-independent and equal to 1;
- geodetic 3/2 and the MPD force reproduced.

**The caveat the referee must rule on.** The R9-10 referee counted "global quasi-local flux proved constructively rather than numerically checked" against PASS (`vR9-10:24-25`). If that standard is kept, the reading is **INCONCLUSIVE**. What is new here partly answers it: Theorem PD makes every registered observable independent of the realization on ℬ. So the box-sector numbers are provably the global stress's numbers there, not those of a different object. The global flux itself is still not evaluated on the lattice.

**FAIL is not available.** No binding-dependent γ and no precession ≠ 3/2 exists in the stated class (Theorem PD).

---

## 1. Hypotheses and class (stated before any title)

- **H-law** (R9-6, refereed PASS WITH SCOPE, `TESTS.md:4016-4024`, `vR9-6:40`).
  - One CAR mode per site of Z³, graded composition, continuous time, two-particle sector.
  - Box band ε = √(m² + |k|²) on |k_a| ≤ B = 2.6, with m = 0.5.
  - p-wave triplet M = M₀ + λΣ_a|g_a⟩⟨g_a|, g_a = q_a b(|q|²), κ = 0.8.
  - Plateau c = 1 for |P| ≤ Π₁ = 0.6 and c = 0 for |P| ≥ Π₂ = 1.2.
  - H = H₀ + cW. J = J₀. K = K₀ + ½{cW, X_NW} + ½{(P×S), cF} (`C5_R9-6_report.md:95-97`). On the box domain: H = √(M² + P²), J = X_NW × P + S, K = ½{H, X_NW} + (P×S)/(M+H), with α = 1 forced.
  - M is internal: it commutes with P, X_NW and S (`C5_R9-6_report.md:115`).
  - Bound masses M_b = 0.95, 0.85, 0.70, i.e. binding fractions f_B = 0.05, 0.15, 0.30.
- **H-stress (the class).** T^{μν}(Q) raises the total momentum by Q. It is Hermitian (T(Q)† = T(−Q)), symmetric and translation covariant, and:
  - (W) [H, T^{0ν}(Q)] = Σ_j D_j(Q_j) T^{jν}(Q) + s^ν(Q), with D = Q on |Q_j| ≤ 1 (R8-2's D) and P_B s P_B = 0 box-to-box;
  - (M) ∫T⁰⁰ = H, the energy dipole is K, and J_T := ε(−i∂_Q)T^{0·}|₀ = J box-to-box.

  This is (a)'s registered list (`TESTS.md:4206`).
- **H-sector.** ℬ := {f(P) ⊗ φ_{b,σ} : f ∈ C_c^∞(|P| < Π₁), σ = 1..3}. Here φ_{b,σ}(q) is the bound triplet in the canonical chart. It is P-independent, because M is P-independent at fixed q, and it is q-compact (|q| < κ). So ℬ ⊂ 𝒟₂³ (R9-6's domain), and X_NW, P, S, H, K, J preserve it.
- **H-grav.** H_tot = H − ½∫h_μν T^{μν}, i.e. H + ∫Φ(T⁰⁰ + γT^{kk}) − ∫w_i T^{0i}, in the fields:
  - (i) uniform lapse;
  - (ii) h₀₀ = −2Φ, h_ij = −2γΦδ_ij (γ = 1 registered; kept general);
  - (iii) tidal Φ = ½ x·T·x;
  - (iv) h₀ᵢ = w_i.

  The sign convention reproduces R9-2/R9-10's H + g·K for Φ = g·x. "Linear order" = O(h). "Dipole order" = Φ, w expanded to first derivatives at the body; tidal force at dipole level via one more gradient.
- **Excluded, not addressed:**
  - N ≥ 3;
  - pair creation and loops;
  - gauge fields;
  - nonlinear gravity;
  - graviton dynamics;
  - the edge sector (Theorem E stands for edge quanta, `C5_R8-2_report.md` §3.3);
  - ungraded ⊗M₂.
- **Outside realizations not excluded.** Any T in H-stress. Theorem PD below shows that all of them agree on ℬ to first moments. They differ at second moments (§8).
- **Subtractions (new rule, named before the runs).**
  - The shell measures in §5.3 subtract the exact plateau value at the same P: E → √(M_b² + P²), J′ → P, [H, J′] → 0.
  - The only decay clause is the Gevrey-2 decay of the constructed kernels themselves. No channel limit is subtracted, because none exists.

## 2. Prior art (each counted once)

- **R9-10** (`vR9-10:27`): the d = 2 Weyl-midpoint T⁰⁰, Lemma KB, Belinfante fix, J_T = J box-to-box, Ẍ_E = −g + 2(g·V)V; GR curved-field spin coupling unmet (`vR9-10:21-22`). This report is its d = 3 continuation plus the curved-field part.
- **R9-2** (`vR9-2:21`): d = 1 stress, box-to-box momentum Ward identity with a shell source, the R7-4 escape.
- **R9-6** (`vR9-6:40`): the d = 3 law and α = 1.
- **R8-2**: Construction A (the universal free stress, dust kernel, D), Theorem E (`C5_R8-2_report.md:73-124`).
- **R7-4's conditional exclusion**: as `vR9-2:17`, the missing hypothesis is global source-free momentum conservation. Unchanged here.
- **C4 V2** (`agents/C4_V2_report.md:196`): "Von Laue (PROVED): under Principle M … a composite at rest carries ∫T_ij = 0." This is a different law (V1/V2's R and Principle M), with the same mechanism.
- **Blocks 144/145** (`docs/ADMISSIBILITY_RULE_THE_MEMBERS_PULL_CARRIES_THE_VELOCITY_TERMS…_2026-09-25.md`, `…BINDING_ENERGY_FALLS_WITH_ITS_WEIGHT…_2026-09-25.md`): a tensor-virial argument giving pull-bound pairs weight 1, in block 60's supplied continuum member action. Same virial mechanism, different setting.
- **Block 138** (lattice Belinfante identity, counted in R9-10).
- **Comparators.**
  - Gravity Probe B geodetic 3/2 and Schiff frame dragging: RECALLED.
  - Barker–O'Connell canonical test-spin Hamiltonian (3/2)(GM/r³)L·S/m: RECALLED.
  - Dixon/MPD pole–dipole stress and the Newton–Wigner spin condition: RECALLED.
  - Kobzarev–Okun (no anomalous gravitomagnetic moment): RECALLED, as in R9-10.
  - The exact-in-v GR weak-field rate (2Γ+1)/(Γ+1): RECALLED. A web search found Silenko–Teryaev gr-qc/0407015 (PRD 71, 064016) and Obukhov–Silenko–Teryaev 0907.4367 as the likely sources, but the formula was **not** confirmed from their text.
  - Spin-induced quadrupole coefficient C_ES² (= 1 for Kerr, body-dependent in general): RECALLED.

---

## 3. Probe (a): the d = 3 stress (proved at R9-10's level; d = 3-specific steps checked)

The construction is R9-10 §3.1–3.3 (`C5_R9-10_report.md:139-190`) with d = 3 inputs. Only the dimension-specific steps are new.

1. **T⁰⁰ (explicit).** T⁰⁰ := T⁰⁰_A + T⁰⁰_I, with
   T⁰⁰_I(Q) = e^{iQ·X_NW/2} χ(Q)[cW + iQ_aB_a](P̄) e^{iQ·X_NW/2} and B_a = ½{(P×S)_a, cF}.
   - ∫T⁰⁰ = H₀ + cW = H.
   - The dipole is K₀ + ½{X_NW, cW} + B = K, using R9-6's lattice-native form (`C5_R9-6_report.md:97`).
   - It is Hermitian, because B_a is Hermitian ([P, S] = 0).
   - Quasi-local: Gevrey-2 in Q through χ; relative-local through the compact q-support of every interaction kernel. Kernel support is |k| < 1.548 < B (`vR9-6:16-26`).
2. **Energy current** (scalar division of N(Q) = [H, T⁰⁰(Q)] − [H₀, T⁰⁰_A(Q)], with N(0) = 0).
   - In d = 3 the transverse Belinfante freedom is −iε^{jkl}D_k σ_l. It is divergence-free identically. Its angular moment is 2σ(0) (checked: `r114_bsector.out:4`, J_T change/σ = [2, 2, 2]).
   - J_T,A = Σ_legs ½{X, × ε∇ε} equals J₀ on box legs and commutes with H₀ globally, because [H₀, J_T,A] ∝ Σ ∇ε × ε∇ε = 0.
   - J_T,A commutes with cW, because W is a rotational scalar supported on box legs inside the ball, where J_T,A acts as J₀ (`vR9-6:28`).
   - C⁽⁰⁾(0) = J′ − J_E = P − P = 0 on 𝒟₂³. So σ can be chosen with **J_T = J box-to-box** (proved, as R9-10 §3.2).
3. **Momentum flux: Lemma KB3** (the d = 3 Koszul–Belinfante division).
   - **Statement.** Let R^i(Q) be smooth (Gevrey-s) with R(0) = 0, ε_{mab}∂_aR^b(0) = 0 (three torque conditions) and R^i(Q)† = −R^i(−Q). Then there is a symmetric Hermitian smooth (Gevrey-max(s, 2)) T^{ij} with Σ_j D_j T^{ji} = R^i. The two conditions are also necessary, since ∂_aR^b(0) = T^{ab}(0) is symmetric.
   - **Near zero.** R^i = Q_jA^{ji}. Split A = A_s + ε^{jim}α_m. Then α(0) = 0 by the torque conditions, so α_m = Q_kβ_{km}, and
     **Y^{ji} = −(ε^{jlm}Q_lβ_{im} + ε^{ilm}Q_lβ_{jm})** is symmetric with Q_jY^{ji} = Q_jε^{jim}α_m. T_near = A_s + Y.
   - **Far.** T_far = R aᵀ + a Rᵀ − (R·D) a aᵀ, with a = D̄/|D|².
   - **Glue, Hermitize, box-to-box inheritance** by convexity, as R9-10.
   - Checked on 200 random draws: the near step to 3.8e-15, the far formula to 9.9e-16 (`r114_bsector.out:2-3`).
   - Applied to R^i = [H, T^{0i}] − s^i, with s = s₁ + s₂: s₁ = the Weyl density of [H, J′_i] (shell and interaction region off 𝒟₂³), s₂ = a pure torque source with zero integral. Both vanish box-to-box, since [H, J′] = [H, J] = 0 on 𝒟₂³.

**Result (proved; construction plus KB3).** T^{μν} is symmetric, Hermitian, translation covariant and Gevrey-quasi-local, with:
- ν = 0 exact on all two-particle states;
- ν = i exact box-to-box, with sources only in the transition shell and in the interaction region off 𝒟₂³;
- ∫T⁰⁰ = H and dipole K (global);
- J_T = J (box-to-box).

**Scope (as R9-10).** The fluxes are constructed, not evaluated on the lattice.

**The explicit box-sector form** (used for the numbers; not relative-quasi-local on scattering states, as `C5_R9-10_report.md:208`). On ℬ:
- T⁰⁰ = e^{iQX/2}𝒯e^{iQX/2}, with 𝒯 = H(P̄) + iQ·(P̄×S)f(P̄) and f = 1/(M+H);
- T^{b0} = e^{iQX/2}[𝒯Δ_b − iε_{bkl}Q_kΣ_l]e^{iQX/2};
- T^{ij} = e^{iQX/2}[𝒯Δ_iΔ_j − i(Δ_iε_{jkl} + Δ_jε_{ikl})Q_kΣ_l]e^{iQX/2}.

Here Δ is averaged over the 6 staircase orderings, with Σ_jQ_jΔ_j = ω, and the d = 3 Belinfante curl is
**Σ = ½[S − (SP² − P(P·S)) f/H] = ½[S M/H + P(P·S)/(H(M+H))]**. In d = 2 (P·S = 0) this reduces to R9-10's SM/(2H).

Checked (`r114_bsector.out`, each M_b), at 60 random (P, Q):
- the ν = 0..3 Ward identities to ≤ 2.4e-16;
- symmetry to 1.4e-17;
- Hermiticity to 5.4e-15;
- moments at P = 0 and P = (0.21, −0.13, 0.30) to ≤ 3e-14.

## 4. Theorem PD (dipole-order data on ℬ are fixed by H, P, K, J). Proved; checked

**Statement.** Let T satisfy H-stress. On ℬ write T(Q) = e^{iQ·X_NW/2} τ(P̄, Q) e^{iQ·X_NW/2}. Every translation-covariant operator has this form in the chart, and τ_b := Π_bτΠ_b acts on the 3-dimensional spin space. With h = √(M_b² + P²), v = P/h and d := (P×S)/(M_b + h), the following hold for all |P| < Π₁ and every M_b:

| moment | value on ℬ |
|---|---|
| τ⁰⁰(P,0), τ^{0i}(P,0) | h, P_i |
| **τ^{ij}(P,0) = ∫T^{ij}** | **P_iP_j/h** |
| −i∂_aτ⁰⁰ (energy dipole about X_NW) | d_a |
| m^{a,i} := −i∂_aτ^{0i} | ½(v_id_a + v_ad_i) + ½ε_{aic}S_c |
| n^{a,ij} := −i∂_aτ^{ij} | ½(S^{ai}v_j + S^{aj}v_i) + ½v_a(d_iv_j + d_jv_i), with S^{ab} = ε_{abc}S_c |

These are exactly the moments of the flat Dixon pole–dipole stress T = p^{(μ}u^{ν)}δ/u⁰ − ∂_ρ(S^{ρ(μ}u^{ν)}δ/u⁰), with the Newton–Wigner condition S^{a0} = d_a.

**Proof.**
1. **The fibre Ward identity.** For φ, ψ ∈ ℬ, Hψ = hψ, because ψ lies on plateau fibres in the M = M_b eigenspace. With P_B s P_B = 0 and D = Q this gives, pointwise for P̄ ± Q/2 in the plateau:
   ω(P̄,Q) τ_b^{0ν}(P̄,Q) = Σ_j Q_j τ_b^{jν}(P̄,Q), with ω = h(P̄+Q/2) − h(P̄−Q/2) a scalar.
2. **Expand in Q** (ω = Q·v + O(Q³)).
   - O(Q) of ν = 0: τ₀^{j0} = v_jh = P_j.
   - O(Q) of ν = i: Q_jτ₀^{ji} = (Q·v)P_i for all Q, so τ₀^{ji} = v_jP_i. This is symmetric by itself.
   - O(Q²) of ν = 0: the symmetric part m^{(a,j)} = ½(v_jd_a + v_ad_j), where d is K's spin term restricted to ℬ.
   - The antisymmetric part of m is fixed by J_T = J = X_NW × P + S, so ε_{baj}m^{a,j} = S_b.
   - O(Q²) of ν = i: τ₁^{a,ji} + τ₁^{j,ai} = v_jτ₁^{a,0i} + v_aτ₁^{j,0i}. With τ₁ symmetric in (j, i), the Christoffel step τ₁^{a,ji} = ½(B_{aji} + B_{aij} − B_{jia}) solves it uniquely. The homogeneous system has rank 18 of 18 (checked, `r114_bsector.out`, "(3)").
3. **Compare with Dixon.** Substituting gives the table, and the Dixon moments are an elementary integration (shown in `r114_dixon.py`'s docstring). ∎

**Checks.**
- The closed form matches the table and the Dixon moments to ≤ 5.7e-14 at P = 0, (0.21, −0.13, 0.30) and (0, 0.5, 0.1), for all three M_b (`r114_dixon.out`).
- A random Riemann-symmetric (Kulkarni–Nomizu) improvement, internal-operator-valued with Y(−Q) = Y(Q)†:
  - keeps Ward to 9.9e-16, symmetry to 2e-15 and Hermiticity to 2.2e-14;
  - changes no zeroth or first moment (≤ 1.1e-14);
  - changes the T⁰⁰ second-moment coefficient by 48.6 (`r114_bsector.out`, "(6)").

**Why this matters (reading).** It answers the R9-10 referee's caveat on its own scope. The numerically checked closed form and the constructed quasi-local stress cannot differ on any registered observable on ℬ.

## 5. Probe (b): von Laue

### 5.1 Exact on the box domain (proved)
By Theorem PD, ∫T^{ij} = P_iP_j/h on ℬ. At rest it is the zero 3×3 matrix on the spin space, for every binding fraction and every spin state, including off-diagonal spin elements.

**Mechanism.** The forward Ward identity at second order is T^{ki}(0) = i[H, M^{ki}] − ∂_ks^i(0). On ℬ the source term vanishes, and i[h, fibre-operator] vanishes in the degenerate bound eigenspace. Checked at the zero floor (`r114_bsector.out`, "(2)").

### 5.2 With real constituents (checked)
`r114_twobody_P0.out`: the actual triplet at P = 0 (q = k₁ = −k₂, all legs in the box), 400 radial nodes.
- **Kinetic forward stress** of the constituent stress (R8-2 dust forward value): Π_kin^{ij} = ⟨2q_iq_j/ε⟩, anisotropic for a polarized triplet.

| f_B | diag Π_kin (pol. x) | tr Π_kin/M_b |
|---|---|---|
| 0.05 | (0.2782, 0.0927, 0.0927) | 0.488 |
| 0.15 | (0.3138, 0.1046, 0.1046) | 0.615 |
| 0.30 | (0.3360, 0.1120, 0.1120) | 0.800 |

- **Interaction forward stress** from the Ward identity, i[W, ½{r_i, q_j}]: the exact negative of the kinetic stress. The residual is 7.1e-12, 1.1e-11 and 1.8e-11 (relative 2.5e-11 to 5.2e-11; the floor of the finite-difference u′).
- **Comparator** (h_ij couples to the constituents only): passive weight 1 + γ tr Π_kin/M_b. Between binding fractions, η = 0.082 (0.05 vs 0.15), 0.190 (0.05 vs 0.30) and 0.108 (0.15 vs 0.30). With the interaction stress it is 0 (proved).

### 5.3 Shell-source contribution as a function of binding
- **At rest it is exactly zero for every binding** (proved): P = 0 lies in the plateau, so P_B s P_B = 0 applies.
- **Moving bound bodies.** ℬ covers |P| < Π₁ = 0.6, i.e. v < 0.534, 0.577 and 0.651 for M_b = 0.95, 0.85 and 0.70 (rapidity asinh(Π₁/M_b) = 0.60, 0.66, 0.77; lattice units).
- **In the shell** (`r114_shell.out`; fibre l = 1 radial problem; N = 400 radial nodes, with N = 200 agreeing on the source norm to the digits shown). Measured against the plateau values (subtraction named in §1):

| f_B | \|P\| | c | E_b − √(M_b²+P²) | ⟨J′_∥⟩ − \|P\| | ‖[h, J′_∥]b‖/E_b |
|---|---|---|---|---|---|
| 0.05 | 0.70 | 0.992 | +2.17e-3 | +0.159 | 2.24e-2 |
| 0.15 | 0.70 | 0.992 | +3.08e-3 | +0.211 | 3.03e-2 |
| 0.15 | 0.80 | 0.818 | +6.39e-2 | +1.163 | 0.148 |
| 0.30 | 0.70 | 0.992 | +4.15e-3 | +0.256 | 4.17e-2 |
| 0.30 | 0.80 | 0.818 | +8.72e-2 | +1.525 | 0.200 |

  - At |P| ≤ 0.6 every entry is ≤ 2.4e-15 (E) or ≤ 2e-9 (J′, the finite-difference floor with dp = 1e-4).
  - ⟨J′_∥⟩ agrees with the Hellmann–Feynman value E_b dE_b/d|P| to all digits shown.
  - The bound triplet unbinds inside the shell: above the pair threshold at |P| = 0.8 for f_B = 0.05, and at 0.9 for f_B = 0.15 and 0.30. The rows beyond are continuum states and are not bound-body data.
- **Scope.** ⟨J′⟩ is the longitudinal fibre part. The spin term i[h, (P×S)g] has zero expectation in an h-eigenstate and is not in the source norm. The forward ∫T^{ij} in the shell depends on the realization through s and is not given.

## 6. Probe (c): passive coupling to (ii) and the effective γ (proved; checked)

- **Monopole.** On ℬ, H_tot = Weyl[(1+Φ)h + γΦP²/h] + H_SO + O(∂²Φ, h²), by Theorem PD (τ^{kk}(P,0) = P²/h).
- **Every bound body is a free particle of mass M_b in this Hamiltonian.** M_b scales out of the trajectory (P = M_b Γv). So the centre's acceleration is binding-independent (proved):
  **a = −∇Φ(1 + γv²) + 2(1 + γ)(v·∇Φ)v**, the linearized PPN geodesic. At γ = 1, light-like limit: deflection factor 1 + γ = 2 (comparator: Cassini, RECALLED).
- **Control (i)** (uniform lapse, h_ij = 0): a = −g + 2(g·v)v, R9-10's refereed result.
- **Effective γ = the field's γ**, for every binding, at rest and moving within |P| < Π₁. Checked: τ₀^{ij} = P_iP_j/h to ≤ 2.8e-17 for all three M_b (`r114_bsector.out`).

## 7. Probe (d): geodetic precession, MPD, frame dragging (proved; checked)

- **Geodetic (field (ii)).** The dipole term is ∂_aΦ(d_a + γ n^{a,kk}), with n^{a,kk} = (v×S)_a (Theorem PD). So
  **H_SO = [Γ/(Γ+1) + γ] S·(∇Φ × v)**, and dS/dt = i[H, S] = Ω × S with Ω = c(v)∇Φ × v.
  - At v → 0: Ω = (½ + γ)∇Φ × v = (3/2)(GM/r³) r × v for Φ = −GM/r, the GP-B value (comparator RECALLED).
  - Checked, c(v) at |P| = 0.001, 0.1, 0.3 and 0.55 for γ = 1, 0 and 0.5, all three M_b: agreement with Γ/(Γ+1) + γ to every printed digit (12). For example, M_b = 0.85, |P| = 0.001, γ = 1: c = 1.500000173010. The structure residual (part not ∝ S·(∇Φ×v)) is ≤ 2.2e-19.
  - At γ = 1 the formula equals (2Γ+1)/(Γ+1) identically (proved algebra), which is the GR weak-field value as RECALLED, not verified this run.
  - **Origin of the two parts (reading, from the proof).** ½ (more generally Γ/(Γ+1)) is K's spin term with α = 1, forced by [K_a, K_b] = −iε_{abc}J_c (`vR9-6:5-11`). γ is the spin carried by the first moment of T^{kk}, forced by J_T = J plus the momentum Ward identity.
  - Comparator: J_T = J + βS (still symmetric and conserved) would give c = Γ/(Γ+1) + γ(1+β) and gravitomagnetic ratio 1 + β. GR's values need β = 0: no anomalous gravitomagnetic moment, which (a) requires.
- **MPD (iii).** On ℬ the dipole-order stress is the Dixon stress (Theorem PD), so the bound body obeys the linearized MPD dynamics of a pole–dipole particle (proved, given Dixon's RECALLED result that MPD follows from that stress's coupling).
  - In canonical variables, with Φ = ½x·T·x at the body: Ṗ = −c(v)T·(v×S) + monopole terms.
  - Not done: I attempted a direct comparison with the covariant-SSC form of the MPD force. The SSC change of variables was not completed (the canonical ↔ covariant centre and momentum map), so that form is not independently checked here.
- **Frame dragging (iv).** −∫w_iT^{0i} at dipole order gives −½(∇×w)·S at rest. Checked for a random linear w: residual 0, ratio 1.000000000000. For the linearized Lense–Thirring field this is Schiff's Ω = G[3(J·r̂)r̂ − J]/r³ (comparator RECALLED). The rigid-rotation case reproduces R9-10's unit gravitomagnetic ratio.

## 8. Beyond dipole order: the quadrupole is not fixed (proved; checked). A finding

- **Improvements.** For any quasi-local, symmetric, Hermitian internal-operator density Y^{ab}(Q), the improvement δT^{μν} = ∂_ρ∂_σY^{ρμσν} keeps all of (a)'s properties exactly, on all states. Take only Y^{a0b0}-type components and their Riemann partners, with ∂₀ = i[H, ·]. The improvement:
  - changes no zeroth or first moment;
  - is conserved and symmetric identically;
  - changes ∫x_ax_bT⁰⁰ on ℬ by an arbitrary symmetric internal operator, e.g. a spin quadrupole S_aS_b + S_bS_a − (4/3)δ_ab.

  A quasi-local example uses Π_b, which is relative-quasi-local because φ_b is C^∞ and q-compact. Checked: the random improvement in §4 moves the second-moment coefficient by 48.6 with all lower moments fixed.
- **Two natural realizations differ.**
  - Constituent-dust T⁰⁰ (free energy at the legs, interaction at the centre; R9-10 §3.1 type): Q_xx − Q_yy = 5.26, 4.95 and 5.02 (f_B = 0.05, 0.15, 0.30; polarization x; lattice units; nonrelativistic leg placement ±r/2 and the stated ordering, an estimate).
  - Closed form: 0.
  - Compare the Kerr-like scale S²/M_b = 2.1–2.9. So the difference is O(1) in natural units.
- **Consequence (reading).** The tidal quadrupole force, F = −½∇(Q^{ab}∂_a∂_bΦ), and the spin-induced quadrupole coefficient (GR's C_ES², body-dependent) are not determined by the box law's Poincaré data. In GR they are fixed by the matter's own field theory, i.e. where the binding field's energy sits. The BT direct interaction has no binding field, so the location of interaction energy inside a body is a free choice.
- This does not touch the registered clauses (MPD is dipole order), and it is not a FAIL. It is a named open item:
  - **P-Q (named, not adopted):** a localization rule for interaction energy, i.e. a field carrier for the binding, or a minimal-coupling principle for the box law.
  - Observable size: suppressed by (body size/distance)² relative to the monopole; not estimated here.

## 9. Prices (named, not adopted)

- **Inherited from R9-2/R9-10 (P-W2):** the linearized gauge invariance (momentum Ward identity) is exact only box-to-box. Sources sit in the transition shell, at lattice-scale total momentum, plus a torque source. The bound body's relativity, von Laue and γ-coupling hold for |P| < Π₁ only. The triplet unbinds inside the shell (§5.3).
- **Inherited:**
  - non-quasi-analytic band and kernels;
  - the frame-fixed box;
  - invariant-mass (BT) interactions;
  - graded fermions;
  - R8-2's edge (Theorem E for edge quanta);
  - BT's N ≥ 3 problem (R9-3/R11-6).
- **New: P-Q** (§8).
- **No axiom text change.** Admissibility supplies no dynamics or stress (`AX:116-123`). Source/action and observable identification are outside the axioms (`AX:187`). The fields are prescribed, not produced (R11-2's question).

## 10. Scope and strong words

- **"Exact"** is used only for:
  - the operator identities on ℬ (Theorem PD, von Laue);
  - ν = 0 on all two-particle states;
  - ν = i box-to-box;
  - the algebra of c(v).
- **"Proved"** for §3 is the construction plus KB3, at R9-10's level: Hadamard and Gevrey steps at sketch level; the fluxes not evaluated on the lattice.
- **"Proved"** for Theorem PD uses only H-stress and H-sector. It is elementary (an order-by-order fibre expansion), not a sketch.
- **"Checked"** numbers:
  - the d = 3 closed form on ℬ, by finite differences: 8th order; tiny-step divided differences replaced by centred derivatives, error O(Q²);
  - the actual two-body triplet at P = 0 and in the shell fibre (radial l = 1 channel, Gauss–Legendre).
- **Not done:**
  - no lattice-native d = 3 evaluation of the global T^{0i}, T^{ij};
  - no real-time evolution in field (ii);
  - no covariant-SSC MPD force comparison (§7);
  - no N ≥ 3, loops or edge populations.
- **Linear in h; dipole order; prescribed static fields; two-body bound triplet; d = 3.**

## 11. For the referee

1. Theorem PD: the fibre Ward identity on ℬ (H commutes with Π_b on plateau fibres; P_B s P_B = 0); the O(Q) and O(Q²) expansion; the Christoffel uniqueness (rank 18/18); the match with the Dixon NW moments.
2. KB3's near-zero Y^{ji} = −(ε^{jlm}Q_lβ_{im} + ε^{ilm}Q_lβ_{jm}), and the factor 2σ(0) of the transverse fix.
3. [cW, J_T,A] = 0 in d = 3 (W rotationally scalar, supported in the ball).
4. Whether (a) at R9-10's construction level plus Theorem PD meets "(a) met" for PASS, given `vR9-10:24-25`.
5. c(v) = Γ/(Γ+1) + γ and its identity with (2Γ+1)/(Γ+1) at γ = 1. The GR comparator is RECALLED.
6. The MPD claim rests on Theorem PD plus Dixon (RECALLED). The covariant-SSC force form was not derived (§7).
7. §8: whether quadrupole underdetermination should be recorded against (iii) or only as a finding.

**Sources (web search this run; the formula itself not confirmed from them):**
- [Silenko & Teryaev, gr-qc/0407015](https://arxiv.org/abs/gr-qc/0407015)
- [Obukhov, Silenko & Teryaev, 0907.4367](https://ar5iv.arxiv.org/html/0907.4367)
