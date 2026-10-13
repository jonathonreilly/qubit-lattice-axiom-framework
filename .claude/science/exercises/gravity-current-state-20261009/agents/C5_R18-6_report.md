# C5 R18-6 report: one source bridge for everything? Are (S), (d-i) and completion N jointly consistent?

**Worker.** Claude Opus 5.5 (the same model family as the supervisor and every C5 worker). **Unrefereed.** Run 2026-10-13, 02:43Z to about 03:05Z. No repository file was edited. Nothing was downloaded.

**Scratch folder.** `S/` = `.../scratchpad/C5/R18-6/`. Every script ran in under 25 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r186_cbox_bridge.py/.out` (sympy): B1–B6, the C-box arena.
- `S/scripts/r186_vacuum_parts.py/.out` (numpy/sympy): C1–C2 (C-box vacuum parts of N's source), A1–A6 (set A).
- `S/recheck/`: the archived R17-11 (4), R17-7 (5) and R16-14 (1) runners, plus R11-3 (an import dependency), copied and rerun. **All 10 reproduce their stored `.out` byte for byte** (`S/recheck/run_all.log`). R17-7's `r177_enthalpy_orders.py` runs with its archived `../R11-3` import path.
- SHA-256: `r186_cbox_bridge.out` 85edf8c8…fbb; `r186_vacuum_parts.out` 3c6ae1a0…c22 (recompute with `shasum -a 256`).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `S23` = `P/agents/C5_S23_synthesis.md`; `rX` = `P/agents/C5_X_report.md`; `vX` = `P/agents/C5_X_referee_verdict.md`.

**Read.**
- In full: `AX`; the C5 method (`TESTS:2302-2320`); the R18-6 item (`TESTS:6684-6711`); vR16-14, vR17-3, vR17-7, vR17-11, vR15-2, vR14-5; rR17-11; rR16-14.
- In part: `TESTS` entries for R13-6 (`4682-4692, 4728-4733`), R14-5 (`4876-4914`), R15-1/R15-2 (`4924-4951, 5164-5183`), R16-14 (`5630-5653, 5875-5886, 5998-6006`), R17-3 (`5786-5812, 5907-5920, 6007-6016`), R17-7 (`6018-6047, 6129-6141, 6297-6318`), R17-11 (`6230-6250, 6319-6335, 6590-6600`), R18-7 (`6713-6736`); `S23` §§1.0, 1.5, 1.6, 1.7, 4; rR17-7 (`1-110, 178-367`); rR14-5 (`80-180`); rR13-6 (`1-60, 120-175, 430-450`); rR15-2 (grep for premise (iii)).

**Labels.** proved (derived here under stated hypotheses) / checked (a number or identity in a `.out` of this run) / suggested (argued, not proved) / reading (interpretation) / comparator (literature, RECALLED or via an earlier referee).

**Subtraction rule.** Every residual is measured against the source that gravitates under the stated bridge; nothing else is subtracted. ρ_Λ = 5.3e-10 J/m³ (RECALLED).

---

## 0. Reading against the FIXED readings (`TESTS:6707-6710`)

**Worker reading: JOINT-CONSISTENT in the arena "C-box with site creation and the R14-5 E-sector" (class 𝒟 of R17-11, with N stated on the gravitating source). Set A: OPEN.** No JOINT-CONFLICT between the pieces' content was found in either arena.

| Arena | Reading | Why (short) |
|---|---|---|
| **C-box-E** (Z³ × ℝ, site creation P52, R14-5 E-sector, sites on slice normals) | **JOINT-CONSISTENT (checked)** | The combined bridge (§2) is exactly GR + Λ̃ on T_m − (V − e₀)g, at every order: Bianchi exact (B1, B2; R17-11 G1–G3 rerun), β = γ = 1 (B3), Λ̃ = κ(V_late − e₀) = 0 under P93, g ≡ 0 so no Lemma-S channel (B5). 3 stipulated sentences, 0 numbers (§4). Two joint qualifications, J1 and J2 (§3). |
| **Set A** (continuum base, records-as-metric, E1/E2) | **OPEN** | (d-i) cannot be posed (no sites, no unimposed equation) and is not needed for the matter vacuum, whose enthalpy is zero by Poincaré invariance (A1). But N's source contains the **record noise's** field energy, present in the matter vacuum, which (S) cannot subtract (A4) and nothing receives. It is R15-2's premise-(iii) term (A3), so it is budget-conditional. Bianchi at O(G²) with the record gain F ≠ 1 is not exact (A5), and under N the noise injection needs a conserved partner (A6). Those are R18-7's questions (`TESTS:6713-6736`). |

**The one incompatibility found (proved, elementary; B4).** The *literal* wording of N ("sourced by total stress") includes the grid vacuum's enthalpy W h[n]. With W ≠ 0, the literal N and (d-i) cannot both hold in C-box: all ten Einstein equations with T_m + T_v require Q = ∇·(W h) = 0, i.e. W' + WΦ' = 0 in every static well and Wθ = 0 under expansion, hence W = 0 (pairing). This is a correction to N's wording, not a conflict of content. Stated on the gravitating stress (J1), N is consistent with (d-i). It is not offered as a JOINT-CONFLICT. If the referee reads the literal wording as the registered piece, B4 is the demonstration, and it needs the referee.

**Against the expectation (`TESTS:6711`).**
- "JOINT-CONSISTENT in C-box with site creation; N's source is Λ-free once e₀ is subtracted": **confirmed**, with J1 and J2 (§3).
- "(d-i) cannot be posed in set A": **confirmed** (§5.1).
- "so set A needs pairing or a tuning for the enthalpy": **not so for the matter vacuum.** Under set A's exact Poincaré invariance the matter vacuum stress is ∝ η, so W_vac = 0 (A1, proved). The frame-tied stress set A *does* carry is the record noise (A3). Pairing does not remove it, and no scalar tuning can (A4). It is controlled only by R15-2's budget window (P-r15c γ-trade).

---

## 1. In plain words

- **The question.** Three separately refereed pieces say what gravity feels and how the metric is read:
  - (S): the law's lowest state weighs nothing;
  - (d-i): the grid vacuum's leftover pressure is handed to the site-making sector;
  - N: gravity's own energy also gravitates (needed for Mercury's perihelion).

  Do they fit together as one rule?
- **On the grid with site creation they do.** Put together, the equations are exactly Einstein's, sourced by ordinary matter plus "vacuum energy minus the lowest state's". That gives Mercury right (β = 1, γ = 1), zero cosmological constant if our vacuum is the lowest state, and no faster-than-light channel. It needs two clarifications, not new rules:
  - N must say "gravity's own energy plus the *gravitating* stress", not "all stress". Read literally, "all stress" would make the vacuum's pressure gravitate again, and that contradicts (d-i).
  - If gravity itself is quantum, its zero-point energy must be part of "the law's lowest state". Then (S) removes its energy, and (d-i) takes its pressure. Otherwise it would weigh about the Planck density.
- **In the continuum set A, the picture is different.** There are no sites, so (d-i) cannot be stated. It is also not needed for ordinary matter's vacuum, because exact relativity makes that vacuum's pressure equal to minus its energy, which (S) removes completely. But set A's metric record carries its own noise, which exists even in empty space. Under N that noise's energy gravitates. (S) cannot remove it, because it is not the energy of a lowest state and it does not behave like a cosmological constant. So set A's fate rests on the noise budget R15-2 already flagged. Whether set A's N is well posed at second order is R18-7's job.

---

## 2. The combined bridge (probe (a))

### 2.1 Arena C-box-E (hypotheses stated before titles)

- **H-imp** (`rR14-5:94-98`): E := G − κT_tot, with E_ni = 0, E^TL_ij = 0 and E_nn = λ (uniform) imposed in the lattice frame. The spatial trace is not imposed (√h fixed per site; site creation).
- **H-site** (`rR14-5:167`; `rR17-11:109`): sites ride the slice normals n (hypersurface-orthogonal), θ_s ≥ 0.
- **H-m** (`rR17-11:116`): ∇·(T_m − Vg) = 0 (covariant latent-heat exchange of the vacuum *energy*).
- **H-vac**: T_v[current local vacuum] = −V g + W h[n], with V and W C¹ local functions of local fields, masses and phase; one-point (mean) stress (`rR17-11:111-115`).
- **Excluded**: active compensation (R15-1 FAIL), superluminal edges (item), V1/V3 fixed-lapse, vortical site flow, anisotropic or fluctuating vacuum stress (outside 𝒟, `vR17-11:29`), the lattice construction of creation (P52/P53).

**The bridge, as equations (κ = 8πG):**

1. **Source (S):** λ = −κe₀[H], with e₀[H] := lim_V min spec(H_V)/V. **H is the full law Hamiltonian, including any quantum sector whose stress N makes gravitate** (J2).
2. **Exchange (d-i):** ∇^μT^v_μν = −∂_νV + Q_ν, with **Q_ν = ∇^μ(W h_μν) = D_νW + W a_ν + Wθ_n n_ν**, received by E: ∇^μE_μν = −κQ_ν (`vR17-11:5-9`). **W is the current local vacuum's enthalpy only, never matter's or gravity's own classical stress** (J1′).
3. **Readout (N_red):** the metric is the solution of
   G_μν[g] = κ T^eff_μν, with **T^eff := T_m − (V − e₀) g**.
   - Equivalently, in Landau–Lifshitz form, □h̄^μν = −16πG τ^μν with τ = (−g)(T^eff + t_LL[g]) + t_H and ∂_μτ^μν = 0 (comparator RECALLED, as `rR16-14:68,143`).
   - It uses recorded T_m, V of recorded fields, the law constant e₀, and initial TT data (P88; the P107/P88 interlock, `S23:262`).

**Result (proved, all orders; checked).**
- Given H-imp, Bianchi gives N(λ + p_E + κW) = g(t), slice-global, and λ̇ = −gθ_n.
  - B1 checks this for a non-symmetric metric (zero shift, diagonal h_ij, all functions of t, x, y, z): residuals 0 (`r186_cbox_bridge.out:2-4`).
  - The spherical, nonlinear, time-dependent case with arbitrary W(t,r) and V(t,r) is R17-11 G1–G3, rerun identical (`S/recheck/R17-11/r1711_lemmaV_general.rerun`).
- (S) gives λ̇ = 0, so g(t)θ_n(x) = 0 for all x. Since θ_n ≠ 0 somewhere on the slice, **g = 0 on the whole slice, including static regions on it** (B5, `out:24-25`).
  - This answers vR17-11's static-interval caveat (`vR17-11:20`): that caveat bites only if a whole slice is static.
- Then p_E = −λ − κW, and **E + κT_v = −(λ + κV)g in all components**. The ten Einstein equations hold with T^eff (B2: checked for a static star with arbitrary W(r), V(r); W absent from the reduced system, `out:7-9`; the matter Euler equation is exactly the effective-fluid TOV, `out:9`).
- So **N_red is not an extra equation in this arena.** It is what the E-sector's full nonlinear G already is, once (S) and (d-i) fix the source. N's added content is only the readout clause (records + P88) and the requirement that the supplied graviton be GR's self-coupled one (§3, J2(i)).

### 2.2 Arena set A

- **What can be posed.**
  - (S), as C = E₀[H_m] with H_m the continuum matter Hamiltonian (Lorentz-invariant regulator).
  - N, as R16-14's τ-sourced readout: E1: h̄ = G_R·F·τ; E2: (□ − γu·∂)h̄ = −16πG F·(τ + X) (`rR16-14:143-146`).
- **What cannot:** (d-i) (§5.1).
- **The combined bridge:** h̄ = G_R·F·τ, with τ = (−g)(T_m − (V − e₀)g + t_LL[g_realized]) + t_H.
  - By A1, (V − e₀)g removes the whole matter-vacuum stress, enthalpy included.
  - t_LL[g_realized] contains the record noise h_n (`rR16-14:157-160`).

---

## 3. Joint qualifications found (the "one bridge" content)

| # | Statement | Status | Where |
|---|---|---|---|
| **J1** | N must be read on the **gravitating** stress T^eff = T_m − (V − e₀)g (plus t_LL), not on "total stress" T_m + T_v. Literal N with W ≠ 0 needs Q = 0, i.e. W e^Φ = const in a static well and Wθ = 0 under expansion. A fixed-proper-spacing vacuum has W = W₀ const, so Q_r = W₀Φ′ ≠ 0. | proved, elementary | B4 (`out:17-21`); Q from R17-11 G2 (rerun) |
| **J1′** | (d-i)'s W is the current local vacuum's enthalpy. If (d-i) were read as "every isotropic site-frame pressure is exchanged" (the absorbable class is all of s h_μν, `rR17-11:188-190`), it would also absorb matter pressure and the isotropic part of gravity's own stress, and break β = 1 and the radiation era. With W = vacuum only, B3 gives β = 1. | proved (B3) for the stated reading; the alternative's failure is suggested (not computed) | `out:13-15` |
| **J2** | **(i)** N's gravity sector must be GR's nonlinear one: in C-box this is a condition on the supplied graviton (P-N1), whose lattice cubic order is W7's open degree-3 question (`S23:327-343`). **(ii)** If that sector is quantum, it must be inside the H that defines e₀. Then the energy part of ⟨t_LL⟩₀ equals its zero-point energy by the per-mode virial (C2, `r186_vacuum_parts.out:9`), and (S) removes it. Its enthalpy W_g is absorbed by (d-i), since every cubic-covariant one-point stress is ρ nn + p h (C1: anisotropy ≤ 1.2e-12 for cubic dispersions against 0.67 for a tetragonal control, `out:2-4`). If the sector were left out of e₀, its zero-point energy would gravitate at the cutoff scale, the same order as the 1e123 ρ_Λ per field of R17-7 (`vR17-7:21`) (suggested, order of magnitude). | (i) reading; (ii) proved (C1 by O_h, C2) + checked | C1, C2 |
| **J3** | g ≡ 0 is inherited by static regions only because g is slice-global and each slice expands somewhere. That is the arrow/creation-sign condition already carried by R14-5 (`rR14-5:299-302`). If a whole slice were static, g₀ ≠ 0 would be allowed. With |g₀| ≤ H₀² its Solar-System metric effect is ≤ 1.3e-30 (B6, `out:26-27`; suggested scaling). | proved (inheritance); suggested (B6 size) | B5, B6 |

**The question "does N's gravitational-energy source include a vacuum part that (S) must also subtract?" (reading on proved pieces).**
- **C-box: yes, if the metric sector is quantum.** The graviton zero-point stress ⟨t_LL⟩₀, and the O(G) field energy of matter's vacuum fluctuations, are ground-state expectations.
  - Their energy is inside e₀ when J2(ii) holds: (S)'s definition, "every band's zero-point" (`rR17-7:182`), already covers it.
  - Their enthalpy is absorbed by (d-i) (C1).
  - N adds them and (S)+(d-i) remove them, so the net is zero, with no number.
  - Gravity's own *classical* stress (the Sun's U² energy) is content above the ground state. It gravitates, and that is what gives β = 1 (B3).
  - If the metric is classical, the vacuum part is absent.
- **Set A: yes, and (S) cannot subtract it.** The record noise h_n is present in the matter vacuum (CP forces D·P ≥ ¼ per mode, `rR13-6:172-174`). Its field energy enters t_LL[g_realized] under N.
  - It is not a lowest-state energy of any Hamiltonian; it is CQ noise.
  - Its stress has p ≠ −ρ (TT: p = ρ/3; S/V: p = u/3 assumed, `rR16-14:241`).
  - In E1 it grows with age.
  - A scalar C g removes a stress only if p = −ρ and ρ is constant (A4, `out:25-27`).

---

## 4. Probe (b): Bianchi at second order, β, Λ̃, Lemma S

| Check | C-box-E (combined bridge) | Set A (S) + N | Label |
|---|---|---|---|
| Bianchi at O(G²) | **Exact at every order.** The reduced system is GR with conserved T^eff (B1, B2; R17-11 G1–G3; vR17-11:5-20) | **Not exact.** ∂·τ = ∂_μ[(−g)(T − G[g]/κ)] = O(G²(1 − F)) when the readout is the F-filtered metric. Static part outside a body: 6ℓ²/r² ≤ 3.1e-28 at R_☉ for ℓ = 5e-6 m (A5); dynamic part 6(τ_c w/R)² = 4.2e-29 (`rR16-14:149`). Under N the noise injection also needs a conserved partner (A6). | C-box: proved + checked. Set A: magnitudes checked; exact consistency not shown (R18-7) |
| β, γ | β = γ = 1 (B3: isotropic Schwarzschild solves the reduced exterior equations, Ricci = 0; g₀₀ = −1 + 2U − 2U², g_ij = 1 + 2U; `out:13-15`) | β = 1 formally under N (`vR16-14:15`), up to the residuals above | C-box proved/checked; set A carried |
| α₁, α₂ (gravity sector) | 0: n is absent from the field equations (`rR17-11:194`); matter LV is carried | 0 in PPN form (`vR16-14:5`) | carried |
| Λ̃ | κ(V_late − e₀) ≥ 0 (`vR17-7:7-12`). **= 0 under P93.** N adds no constant once J2 holds | κ(V_late − e₀) = 0 under P93 for the matter vacuum (A1). **Plus a non-Λ gravitating noise component** of size \|u₁\| (A3) | proved given P93 (C-box); set A conditional |
| Lemma-S channel | **None at any order:** g ≡ 0 exactly (B5); Δδ̇ = F (`rR17-11:226`) | None from (S) (constant). E1's frame-tied gain is causal (`rR13-6:154-156`); no elliptic lapse | C-box proved; set A reading |

**Set A noise numbers (checked, `r186_vacuum_parts.out:15-22`; reproduces `rR15-2:26` and `vR15-2:17`).**

| ℓ | \|u₁\| strict τ = ℓ/c | \|u₁\| at the τ_c ceiling | Vacuum-fluctuation field energy (ℓ_P/ℓ)²ħc/ℓ⁴ (suggested) |
|---|---|---|---|
| 4e-10 m | 8.6e18 ρ_Λ | 2.3e12 ρ_Λ | 3.8e-30 ρ_Λ |
| 5e-8 m | 3.5e10 | 1.2e6 | 1.0e-42 |
| 5e-6 m | 3.5e2 | 1.2 | 1.0e-54 |

- The matter-vacuum-sourced part is negligible.
- The record-noise part overshoots ρ_Λ at least-decoherence everywhere except near 5e-6 m at the τ_c ceiling, unless R15-2's γ-trade applies (ℓ ≳ 5e-8 m for τ_c, ≳ 2.5e-7 m strict; suggested there, `rR15-2:245`).
- Under N this is premise (iii) made live. That is a worker suggestion (`rR16-14:155-160`); the referee says N does not establish it (`vR16-14:15`).

---

## 5. Probes (a) remainder, (c) and (d)

### 5.1 (d-i) in set A (proved, by inspection of the stated structures)

- (d-i) as registered needs two things:
  - a site frame with fixed proper site density and site creation;
  - an **unimposed equation** to receive Q. In 𝒟 that is the spatial trace (`vR17-11:22-23`).
- Set A has neither:
  - the base is a continuum;
  - E1 and E2 fix all ten components of h̄ from τ (`rR16-14:143-146`).
- A set-A analogue would have to exchange with the record-production (meter) sector. That is the same structure A6 requires anyway, and it is not built (suggested; R18-7).

### 5.2 (c) Count of independent stipulated sentences and numbers

| Arena | Sentences | Numbers |
|---|---|---|
| **C-box-E** | **3:** (S) [P92]; (d-i) [P-vac′]; N_red as the readout clause [P107, with P88]. J1/J1′/J2 are scope fixes inside these three sentences, not new ones. In this arena, N's field equation is the E-sector's own G, so N adds no equation, only the readout clause and J2(i). | **0** |
| C-box-E, arena structure (carried, not bridge sentences) | H-imp + H-site + creation (P52/P53 = P-r1711a; P-r1711b); non-Lagrangian partner (P128 = P-r1711c); P93 (condition) | 0 |
| **Set A** | 2: (S), N. (d-i) is not posable. The noise residual needs P-r15c (γ-trade, a channel-dependent record precision), or ℓ near the window top. | 0 (P-r15c's γ is a law datum per channel, `rR15-2:258`) |

**Independence (reading).** The three C-box sentences are independent:
- (S) without (d-i) leaves the 1.2–1.8e123 ρ_Λ enthalpy (`vR17-7:21`);
- (d-i) without (S) leaves λ a free constant, which is Lemma PT's counterterm (`vR17-3:19`);
- either without N gives β = 0 or ½ (`vR16-14:13`).

Merging them into the single sentence "G = κ(T_m − (V − e₀)g), with the local vacuum's site-frame enthalpy exchanged with creation" does not reduce the stipulated content.

### 5.3 (d) Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P-r186a (J1)** | N is stated on the gravitating stress T_m − (V − e₀)g plus gravity's own stress. Literal "total stress" is incompatible with (d-i) whenever W ≠ 0. A rewording of P107; no number | `AX:187`; `AX:82-83` | proved (B4); needed in C-box |
| **P-r186b (J2)** | (i) the supplied graviton (P-N1) is GR's self-coupled field, whose lattice degree-3 is W7's open item; (ii) a quantum gravity sector is part of the H that defines e₀ | `AX:47` (supplied sector); `AX:187` | (ii) proved consistent; (i) open (W7) |
| **P-r186c (set A)** | Under N, the record-production sector (driven meters, P-r11b) must carry a conserved stress in τ that supplies the noise injection 3H(ρ_n + p_n) (A6). This is the set-A analogue of E2's missing sink action (`vR16-14:15`) | `AX:185` (record production); `AX:187` | suggested; R18-7 |
| Carried | P92 (S); P-vac′ (d-i); P107 (N); P88; P93; P52/P53 (P-r1711a); P-r1711b; P128; P-r15c (set A) | — | carried |

---

## 6. Strong words checked

- **"Exact at every order" (C-box):** an identity given H-imp, H-site, H-m, (S) and expansion somewhere on each slice; one-point, smooth, on shell (the same scope as `vR17-11:44-45`). It is not a lattice derivation or a completed action.
- **"β = γ = 1":** the gravity sector's static exterior with V_out = e₀ (P93). Matter LV in the site frame is carried, not tested.
- **"(S) cannot subtract" (set A):** a scalar times g cannot remove a stress with p ≠ −ρ or with time dependence (A4). An extended (S) that subtracts a time-dependent noise tensor would be N̄-like, an ensemble quantity, in tension with `AX:82-83` (`rR16-14:161`). It is not covered here.
- **"Cannot be posed" ((d-i) in set A):** for (d-i) as registered (site creation + unimposed trace). A meter-sector receiver is not excluded.
- **"Λ-free":** in C-box, under J2 and P93. Without P93, Λ̃ = κ(V_late − e₀) ≥ 0, with the SM-only sizes of `vR17-7:37-40`.
- **"No JOINT-CONFLICT":** none was found between the pieces' content in either arena. B4 is a conflict with N's literal wording only.

## 7. Notes for a referee

1. Is reading N as N_red (J1) within the registered piece "N: the metric record is sourced by total stress, gravity's own included" (`TESTS:6688`)? If not, B4 is a JOINT-CONFLICT demonstration (literal N vs (d-i), W ≠ 0) and needs the referee.
2. B5: does g ≡ 0 on static regions follow from slice-globality? `vR17-11:20` flags only fully static intervals.
3. J2(ii): is the per-mode virial (C2) enough to identify the energy part of ⟨t_LL⟩₀ with the Hamiltonian zero-point for the constraint and gauge parts, or only for TT modes? The enthalpy part is absorbed regardless (C1).
4. Whether set A's OPEN should instead be recorded as "not checked here; deferred to R18-7".

## 8. Files

- Report: `S/R18-6_report.md`.
- Scripts and outputs: `S/scripts/r186_cbox_bridge.{py,out}`, `S/scripts/r186_vacuum_parts.{py,out}`.
- Reruns: `S/recheck/{R17-11,R17-7,R16-14}/*.rerun` (+ `.rerun.err`); `S/recheck/run_all.log` (all 10 IDENTICAL).
