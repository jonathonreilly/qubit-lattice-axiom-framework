# A24 report: can a record form without disturbing the energy?

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A24/`
- Each script `X.py` writes `out_X_<args>.txt` and `time_X_<args>.txt` through `run.sh`. The wrapper runs at nice 10, with the four thread caps at 1 and a 58 s alarm.
- S3 and S8 import A19's `core1d.py` from `../A19/`.

**Grades.**
- **EXACT**: proof or exact arithmetic.
- **CHECKED**: numeric check with a stated tolerance.
- **ARGUED**: reasoning without proof.
- **COMPARATOR**: literature or data quoted from memory, unverified, never adopted.

**Scope.** All models are supplied toys. I1–I6 and the Q-readings appear only as "if … then …". I did no git, repo, audit or review operations.

**Notation.**
- H = Σ_j h_j is the change's conserved energy, a sum of local terms.
- A record at site x with menu basis {|k⟩} acts through the one-site projectors P_k = |k⟩⟨k|_x ⊗ 1.
- The branches are ψ_k = P_k ψ.
- The "ghost source" is A23(f)'s mismatch at the level of expectation values: −δ⟨h_j⟩ on each energy term. A23 D13 keeps it static.

---

## 1. Question

Can a record form, compatibly with Record (one admissible local possibility locked, one record per site), while injecting energy far below the bandwidth, ideally zero on average? Two routes were posed:
- **(i)** locks that commute with the energy density;
- **(ii)** mediated locks (A19 R2), where a probe bumps the mover and the probe's site is then locked sharply.

How small can the injected energy be, and what controls it?

## 2. Answer

**Conditional yes.** The bookkeeping, conditions and no-gos are EXACT. The toy behaviour is CHECKED in continuous-time and ticked toys. The physical scales are ARGUED.

**What sets the cost.** A lock injects exactly the shared "interference" energy that its rival possibilities still carry through the energy terms touching the recording site: ΔE = −Σ_{k≠l} Re⟨ψ_k|H|ψ_l⟩. Nothing else contributes.

**Route (i).**
- Taken literally (the lock commutes with the energy as an operator), it is sterile. The site's odds are then constants of the change, so the record registers nothing the change carried to it.
- The state-wise version works. If the rivals no longer overlap through any local term at the site (call the possibility *settled*), the record leaves every local energy and momentum density unchanged on average. That means a zero ghost source at every point.

**Route (ii) as posed** (a sharp record of the probe) does not lower the injection; it moves it onto the probe.
- The total is exactly the probe's depth below its band centre. The mover's mean energy is untouched.
- Softer probes cost more. Continuous-time toy: 1.96 out of a maximum 2 at q = −0.15. A19's ticked toy: 1.42 out of 1.47 per registration.

**What works: catch first, record later.**
- The probe is caught at a trap site, and its spare energy leaves as an emitted excitation. The one-site trap record is then settled.
- A single lock after settling injects zero up to packet tails (CHECKED: about 5e-8 of the band scale in the ticked toy).
- A constant-chance formation weight injects ≈ κħΓ_f per record, where Γ_f is the formation chance per unit time. CHECKED: κ = ½cot k_e to 0.4% in continuous time (k_e is the emitted excitation's momentum); κ ≈ 0.4–0.5 in the ticked toy.
- The mover still feels only A19's coarse recoil cut.

**Floors for unsettled records** (EXACT):
- ħ²/(8mσ²) per axis at resolution σ (Cramér–Rao);
- about ħc/σ below the Compton length;
- the depth below the band centre at one-site sharpness, ≈ (π/2)ħ/τ, which is Planck-scale under the identification.

**Summary of control.** The injection is controlled first by whether the locked possibility has been caught and settled, and then by how quickly the record forms after the catch.

## 3. Derivation

### 3.1 Bookkeeping (Task 1)

**E1 [EXACT; CHECKED 5e-15 on 200 random instances].** For Hermitian Kraus operators A_k with Σ A_k² = 1, the outcome-averaged change is

ΔE = Σ_k⟨A_k H A_k⟩ − ⟨H⟩ = −½ Σ_k ⟨[A_k,[A_k,H]]⟩.

- Proof: [A,[A,H]] = A²H + HA² − 2AHA; sum over k.
- For projectors, ΔE = −Σ_{k≠l} Re⟨ψ_k|H|ψ_l⟩, because H = Σ_{k,l} P_k H P_l.

**E2 [EXACT] Locality.**
- A term not containing x commutes with every P_k, so its cross terms vanish.
- Only terms containing x change: δ⟨h_j⟩ = −Σ_{k≠l} Re⟨ψ_k|h_j|ψ_l⟩. The ghost on those terms is −δ⟨h_j⟩.
- For a one-site lock, ΔE = −⟨H^⊥_x⟩, where H^⊥_x is the part of the terms at x that flips x in the menu basis.
- Current (momentum) densities obey the same formula with their own terms.

**E3 [EXACT; CHECKED] Sign.** A lock drives the shared energy at x toward zero.
- Bonding, sub-centre states (the low-energy case) are heated.
- Inverted states are cooled: at k0 = 2.5, ΔE = −1.602.

**E4 [EXACT] A9's formation instrument.** The Kraus operators are P_k√F (record with content k) and √(1−F) (no record). Then

ΔE_tick = −½⟨[√F,[√F,H]]⟩ − ½⟨[√(1−F),[√(1−F),H]]⟩ − ½Σ_k⟨√F[P_k,[P_k,H]]√F⟩.

For F = f·P with a projector P:
- ΔE_tick = c·ΔE_bin(P) + (f/2)·(dephasing inside the formed branch);
- c = 1 − √(1−f) ≈ f/2 (using c² + f = 2c);
- ΔE_bin(P) = −⟨[P,[P,H]]⟩ is the cost of one binary lock {P, 1−P}.

**E5 [EXACT; CHECKED] Sharp records of one excitation.**
- **Record wherever the excitation is.** ΔE = Σ_y p_y H_yy − ⟨H⟩ = ε_c − ⟨H⟩, the depth below the band centre ε_c (the diagonal average). On the tight-binding ring (J = 1): 1.99957 at k0 = 0, 1.91026 at 0.3, 0 at π/2.
- **One binary site.** ΔE = −(energies of the bonds at x), agreeing to all printed digits.
- **Per record under A9's instrument.** About the depth for every chance f: 1.908–1.915 for f = 1 down to 0.003, against a depth of 1.911.
- **Ticked toy (A19 core).** The conserved one-excitation energy is W(K) on both velocity branches, with cos W = cos m cos K. In the cell basis E = W(K) ⊗ 1, so ⟨y|E|y⟩ = mean W = π/2 at every site. This is exact by W(K+π) = π − W(K), and CHECKED to 1e-15.
- So a sharp record injects π/2 − ⟨W⟩, about (π/2 − m)ħ/τ for a slow excitation. Under τ = t_P that is about 3e9 J (ARGUED identification).

**E6 [EXACT; CHECKED] Unsharp position records.** The Kraus operators are √w_y(x), with Σ_y w_y = 1.

*Lattice.*
- ΔE = Σ_bonds (1 − B_b)(−⟨h_b⟩).
- B_b = Σ_y √(w_y(x) w_y(x+1)) is the overlap of the record laws for the two ends of the bond.
- So the cost is how well the record tells the bond's ends apart, times that bond's shared energy. This agrees with direct Kraus sums to 7 digits.

*Continuum* (H = p²/2m + V; Kraus f_y = √w_y e^{iθ_y}; A = Σ_y w_y θ_y′):

2m ΔE = ħ²⟨I_F⟩/4 + ħ²⟨Var_y θ′⟩ + [⟨(p + ħA)²⟩ − ⟨p²⟩].

- I_F is the Fisher information of the record law.
- The bracket is a reversible mean kick. In a conserving setting a partner pays it.
- The first two terms are the irreducible back-action. By Cramér–Rao they are at least ħ²/(8mσ²) per axis, with equality for a Gaussian.
- CHECKED: 8σ²(1 − B) tends to 1.000 (Gaussian), 1.999 (Laplace, where I_Fσ² = 2) and ≈ 2s/3 (sliding window of s sites).

*Pixel records.*
- Fixed blocks of s sites cost (1/s)(−⟨H⟩) exactly.
- At s = 64 that is 43× a Gaussian of equal variance: sharp edges heat (matches A19).

*Ticked toy, resolution law.*
- The averaged Gaussian cut is a Gaussian kick of cell momentum with variance 1/σ_s², so ΔE(σ) = E[W(K+δ)] − W(K) (EXACT).
- σ ≫ 1/m: ΔE → ½cot m/σ_s², i.e. ħ²/(8mσ²). At m = 0.01, σ_s = 1000: 4.963e-5 against 5.000e-5.
- 1 ≪ σ ≪ 1/m: ΔE ≈ √(2/π) cos m/σ_s, i.e. order ħc/σ. At σ_s = 2: 0.390 against 0.399.
- σ → 0: ΔE → π/2 − m. At σ_s = 0.25: 1.5604 against 1.5608.

### 3.2 When it vanishes, and the no-gos (Task 1)

**V1 [EXACT] Operator-commuting one-site records are sterile.**
- Suppose [P_k, H] = 0, i.e. every term at x is diagonal there in the menu basis. Then tr(P_k ρ) is a constant of the change.
- Lüders locks at other sites leave x's marginal unchanged on average.
- So the odds are fixed by the initial snapshot, apart from neighbouring formation instruments that act on x. Such a record registers nothing the change carried to x.
- One-site locks of conserved local quantities are this same case. Global conserved quantities have no one-site projectors.

**Why U(1) is fine and gravity is not.** U(1)'s source n_y is diagonal in the occupation basis, so every occupation lock commutes with it and leaves no ghost charge, settled or not. Gravity's source contains the off-diagonal hopping energy.

**V2 [EXACT] Settled possibilities cost nothing.**
- *Definition.* Call x's possibility settled if every local term containing x (energy and current) has zero matrix elements between the record's branches.
- *Consequence.* By E2 the record then leaves every local energy and momentum density unchanged on average. That is a zero ghost, with no monopole and no higher multipoles.
- *Sufficient condition.* The branches' states outside each such term's support are orthogonal, because then tr_{S^c}|ψ_l⟩⟨ψ_k| = 0. In words: the change has already copied the distinction beyond the reach of every term at x.
- Settled does not mean static. The branches keep evolving; they just no longer interfere through the recording site.

**V3 [EXACT] A slow lone excitation is never settled.**
- With nearest-neighbour hopping, the cross term on bond (x,y) is H_xy ψ_x* ψ_y.
- Settledness needs ψ_y = 0 on all neighbours wherever ψ_x ≠ 0. That is sparse support: a sublattice-polarized band-centre state, or a flat-band cage.
- A smooth (slow) excitation never has it. So the first record that resolves a lone, freely spreading excitation always pays its shared energy.

**V4 [EXACT; CHECKED] The band-centre probe is a formal escape only.**
- A sharp probe record is free on average if and only if the probe sits at its band centre (|q| = π/2 in 1D).
- Its kick is then lattice-scale. At q = −π/2 the record costs 0.059, but the mover's momentum shifts by −3.06 and its energy rises by 0.171, which is 1.7× its half band.

**V5 [EXACT] Formation weights cannot tell coherent from decohered.**
- Take ψ_θ = a|k,e⟩ + b e^{iθ}|l,e′⟩. If F ≥ 0 vanishes on ψ_θ for all θ, it annihilates both components, and so also the decohered mixture.
- So no linear local F fires only on settled possibilities. The formation rule must rely on support (caught, stationary configurations) plus slowness (C3).

### 3.3 Mediated records (Task 2)

**M1 [EXACT].**
- After the collision, the probe record's projectors commute with the mover's energy and with on-site contact terms.
- So ΔE_lock = Σ_y⟨P_y H_B P_y⟩ − ⟨H_B⟩ = ε_c,B − ⟨H_B⟩: exactly the probe's depth.
- The mover's mean energy is unchanged by the record. Its energy changed only in the collision, by exchange with the probe.
- The ghost sits at the probe's record site.

**M2 [CHECKED] Continuous-time ladder** (`mediated_ct.py`).
- Mover: J_A = 0.05 (m_A = 10), K_A = 0.5. Probe: J_B = 1. Contact U = 1.5.
- Energy is conserved to 1e-8.
- "Record cost, all outcomes" equals −⟨H_B⟩ to all digits.

| q | P(reflected) | Record cost, all outcomes | Per reflected-probe record | Mover energy change per registration | Mover momentum shift (−2\|q\|) |
|---|---|---|---|---|---|
| −0.15 | 0.916 | 1.966 | 1.963 | −0.011 | −0.335 (−0.30) |
| −0.30 | 0.839 | 1.899 | 1.898 | −0.011 | −0.617 (−0.60) |
| −0.60 | 0.618 | 1.656 | 1.661 | +0.011 | −1.187 (−1.20) |
| −1.00 | 0.428 | 1.112 | 1.157 | +0.076 | −1.952 (−2.00) |
| −1.30 | 0.365 | 0.582 | 0.667 | +0.132 | −2.530 (−2.60) |
| −π/2 | 0.349 | 0.059 | 0.170 | +0.171 | −3.056 (−3.14) |

For comparison, direct records on this mover cost 0.088 (sharp; its own half band is 0.1) and 7.6e-5 (Gaussian with σ = 12).

**M3 [CHECKED] A19's ticked ladder** (`floquet_energy.py`). Probe m_p = 0.1, mover K_A = 0.8, probe half band 1.471.

| Mover m_A | q | Record cost, all outcomes (π/2 − ⟨W_B⟩) | Per registration, ordinary channel | Mover change per registration | Doubled-channel weight | Collision jump in doubled channel |
|---|---|---|---|---|---|---|
| 1.2 | −0.05 | 1.035 | 1.422 | −0.038 | 0.145 | +3.43 |
| 1.2 | −0.2 | 1.243 | 1.252 | −0.098 | 0.039 | +3.21 |
| 1.2 | −0.8 | 0.727 | 0.767 | −0.000 | 0.026 | +2.04 |
| 0.6 | −0.05 | 1.369 | 1.223 | −0.238 | 0.031 | +4.14 |
| 0.6 | −0.4 | 1.154 | 0.866 | −0.296 | 0.002 | +3.55 |
| 0.3 | −0.05 | 1.434 | 0.973 | −0.488 | 0.008 | +4.38 |

- In the ordinary channel the pair's energy is conserved to ≤ 0.003 (finite packets).
- Reflected registrations split about 50/50 between the ordinary channel and A19 R3's doubled (time-umklapp) channel.
- In the doubled channel the collision itself, with no record involved, moves W_A + W_B to 2π − W_in (to ≤ 0.004).
- A record there lowers the probe by exactly the ordinary channel's amount, since W → π − W. So the out files print about 0 per reflected record. This is a doubled-channel artifact, not an escape.

**M4 [ARGUED].** Mediation moves the ghost; it does not shrink it unless the probe's possibility is settled.

### 3.4 Settled records: catch first, record later (Tasks 2–3)

**C1 [EXACT construction] The trap toy** (`capture_trap.py`).
- States: |B_x⟩ is the probe on its chain; |C_z⟩ is the probe held at the trap site *and* an emitted excitation at z on chain C.
- H = −J_B Σ(B hops) − J_C Σ(C hops) − V Σ_z |C_z⟩⟨C_z| + g(|C_0⟩⟨B_j0| + h.c.).
- The trap is one site, with occupation projector P_t = Σ_z |C_z⟩⟨C_z|.
- In qubit language the capture term is a three-site term (B_j0, trap, C_0) inside the trap's star.
- It is the only term that flips the trap, so the record costs ΔE(t) = −2 Re[g c_0* b_j0].
- This vanishes once the probe has left j0 and the emitted excitation has left C_0: settled.

**C2 [CHECKED] Single record versus time.**
- The trap record peaks at 3.4e-3 during the capture and falls to 9.2e-6 at t = 240. The formula matches the direct computation to all digits.
- At the same times, a sharp record of the probe costs 1.08–1.91.
- A sharp record of the emitted excitation costs 0.395, which is P(capture) × its depth 0.909.

**C3 [EXACT in the stationary limit; CHECKED] Constant-chance formation on the trap.**
- An outgoing wave forces g b_j0 = −J_C e^{−ik_e} c_0.
- So the shared energy per unit captured flux is cot k_e, and the cost per record is (f/2)cot k_e. In words: half the formation chance during the emitted excitation's passage across the capture link, times its depth.
- CHECKED with f = 0.003:

| k_e | Measured (cost per record)/f | ½cot k_e |
|---|---|---|
| 0.55 | 0.8225 | 0.8225 |
| 0.86 | 0.4330 | 0.4328 |
| 1.10 | 0.2552 | 0.2551 |
| 1.36 | 0.1043 | 0.1045 |
| 1.57 | 0.0020 | 0.0023 |

- On unsettled sites the same instrument costs the full depth at every f: 1.908–1.915 on a probe site, 0.908–0.910 on an emitted-excitation site.

**C4 [CHECKED] Full chain: mover, probe and trap** (`capture_mover.py`, dimension 70,000).
- Energy is conserved to 1e-8.
- The trap record peaks at 1.85e-3 and ends at 4.3e-5. A sharp probe record costs 1.19–1.91 at the same times.
- Given a trap record (weight 0.373), the mover shows:
  - momentum shift −0.619 (the recoil −2|q| is −0.60);
  - momentum spread 0.097 (from 0.0625);
  - position spread 8.17 (from 8.0);
  - energy −0.011, handed to the probe by Doppler shift.
- So the registration is A19's coarse recoil cut, at near-zero record cost.

**C5 [CHECKED] Ticked version** (`ticked_capture.py`).
- Setup: A19's round on both chains, a partial-swap capture gate, and energy E = arccos(−(U+U†)/2) as a function of the whole tick U.
- [E,U] ≤ 1e-14, and E is conserved to 1e-8.
- The trap record peaks at 5.2e-3, then falls to 6.9e-8 (m_C = 0.05) and 2.6e-8 (m_C = 0.3) by t = 400. A sharp probe record costs 0.73–1.15.
- Under constant-chance formation, (cost per record)/f is 0.49–0.50 (m_C = 0.05) and 0.37–0.39 (m_C = 0.3). It is linear in f within 5% over f = 0.003–0.03.

**C6 [ARGUED; kernel CHECKED] Reach.**
- In the ticked toy the energy is quasi-local. Its kernel decays as r^{−3/2} e^{−κr} with κ = arccosh(1/cos m) ≈ m (CHECKED to ≤ 2.1%).
- So "settled" means the distinction has moved beyond about one Compton length 1/m.
- For a massless one-excitation energy |K| the tails are power-law.

**C7 [ARGUED] Physical scale.**
- For an emitted excitation crossing one link at light speed, the cost is κħΓ_f with κ of order 1.
- A record forming about 1 ns after its catch costs about 7e-7 eV.
- A record forming on the very next tick costs about ħ/τ. In the toy, f = 1 gives 0.78 against a depth of 1.91.

### 3.5 Energy-eigenstate records (Task 3)

- **T1 [EXACT].** A one-site projector commutes with a subsystem's energy if and only if the site is diagonal in every subsystem term at it. If the outside coupling is diagonal too, V1 applies: the record is sterile.
- **T2 [EXACT].** A projector onto an entangled multi-site eigenstate has the wrong form to be P_k ⊗ 1, so it is not a Record lock. A one-site lock on such a pattern costs its shared binding energy: J/2 for a Heisenberg singlet, J for a two-site bonding state.
- **T3 [EXACT; CHECKED] Static trap.** The one-site record of a probe bound in an on-site well −V costs 2|c_0|²(H_00 − E_b) = 2V(√(V²+4J²) − V)/√(V²+4J²), which tends to 4J²/V (at V = 64: 0.06245 against 0.0625).
- **T3, flat band.** A flat-band caged state costs exactly 0, because the cage is sparse support.
- **T3, entry.** A free single excitation cannot enter either kind of state, since energy is conserved. Entry needs energy released into something else, which is exactly C1.
- **T4 [EXACT at expectation level].** Settled records give zero ghost on every term.
- **T4, operator level [ARGUED].** The operator-level constraint is beyond linear order: the lattice's local energy terms do not commute with one another.
- **Conclusion.** Strict energy-eigenstate records are either not one-site or sterile. The workable version is a one-site record on a caught, settled configuration.

### 3.6 Bounds and the field route (Task 4)

**B1 [EXACT].** Zero is possible (V2, C2–C5), so there is no universal floor.
- Unsettled records have the floors in E5–E6.
- Settled records cost about κħΓ_f.

**B2 [EXACT in linear bookkeeping; ARGUED physically] What the ghost does.**
- After a record injects ΔE, the field keeps the pre-record energy, and A23 D13 holds the mismatch static at the formation site.
- The injected heat gravitates wherever it goes, while −ΔE stays put.
- In total, the ghost is heat that never gravitates. Heating bounds therefore bound it.

**B3 [ARGUED; data COMPARATOR] Bounds from heating.**

| Record type | Cost per record | Bound on the rate |
|---|---|---|
| Unsettled sharp | ~3e9 J | ≤ 4e-48 per nucleon per second (≈ 2e-91 per Planck tick; agrees with A19's ~1e-90) |
| Direct at 1 Å, nucleon | 2.5e-22 J (1.6 meV) | ≤ 5e-17 per second, about once per 6e8 years |
| Direct at 1 Å, electron | 4.6e-19 J (2.9 eV) | ≤ 6e-20 per second |
| Settled (κħΓ_f) | ~7e-7 eV per 1 ns record | negligible |

- The bounds come from Earth's heat flow of about 47 TW, i.e. ≤ 7.9e-12 W/kg or 1.3e-38 W per nucleon.
- GRW-like parameters would give 3e-17 W/kg, far inside the bound.
- The accumulated ghost, if all of Earth's heat flow were record heat for 4.5 Gyr, would be 7e13 kg ≈ 1e-11 M_⊕. That is below the GM_⊕ uncertainty, so the heating bounds dominate.

**B4 [EXACT in the toy] A separate defect.** The doubled channel of contact collisions (M3) changes the lifted energy without any record. A field sourced by that energy also needs the A19 R3 / A23(d) fix.

### 3.7 The owner's ideas (if … then)

- **Ticks (I1).** If records form at set ticks and a caught possibility records on the very next tick, then it costs about ħ/(tick). If it records with a small chance per tick, it costs about κħ × (chance per unit time).
- **Moving records (I2–I3, A13 option A).** If records move by re-forming one site away as localized hopping excitations, then each re-lock keeps the mean energy (EXACT: ⟨y|E|y⟩ = π/2) but resets the record's currents. Its standing energy is the band-centre value, Planck-scale under the identification (ARGUED).
- **Jams (I5).** If a jammed region's change keeps locked possibilities, then a caged site's value is a constant of the change. A record there costs nothing and registers nothing (V1).
- **Empty sites.** If an empty site forms a record on its own with the emptiness-aligned menu, then it costs nothing (EXACT). Other menus create excitations and cost energy.

## 4. Checks

All runs used `nice -n 10`, the four thread caps at 1 and the alarm. The longest took 16 s; peak memory was 263 MB.

| Script | What it checks | Key numbers | Tolerance |
|---|---|---|---|
| `lock_energy_1d.py` | E1, E3, E5, E6, T3, flat band | Identity 5.3e-15; pixel 43× Gaussian; trap closed form; flat-band cage 0 | 1e-12 |
| `mediated_ct.py` (3 runs) | M1–M2 | Record cost = −⟨H_B⟩ exactly; energy to 1e-8 | 1e-8 |
| `floquet_energy.py` (4 runs) | E5, M3, time-umklapp | Mean W = π/2 to 1e-15; doubled channel 2π − W_in to ≤ 0.004 | as stated |
| `capture_trap.py`, `capture_rate_vs_k.py` | C1–C3 | ½cot k_e law to ≤ 0.4% (f = 0.01), ≤ 0.2% (f = 0.003) | as stated |
| `capture_mover.py` | C4 | Recoil −0.619 against −0.60; energy to 1e-8 | — |
| `ticked_capture.py` (m_C = 0.05, 0.3) | C5 | Residual 2.6–6.9e-8; κ = 0.37–0.50, linear in f within 5% | — |
| `floquet_kernel.py`, `resolution_law.py` | C6, E6 regimes | Decay rate within ≤ 2.1%; regimes within 0.03–4.5% | as stated |

- No run exceeded the budget, and no outputs were discarded.
- The first `floquet_energy` batch was rerun to get its per-channel lines.

**Should be run next (tiny, not run).** Three excitations on a ~60-site ring in A13's model, with a contact phase. Look for a bound pair forming while a third excitation leaves, then compute the one-site record cost on the pair.

## 5. Real-physics match

**Comparators** (from memory, unverified, none adopted):
- Gaussian position back-action of ħ²/(8mσ²) per event (Caves–Milburn; Diósi).
- GRW's 3λħ²/(4m r_C²), which is E6 with σ² = r_C²/2. CSL heating bounds from cold atoms, neutron stars, the intergalactic medium and LISA Pathfinder.
- Wigner–Araki–Yanase / Ozawa: observables that do not commute with a conserved quantity can be registered only approximately, better with a larger apparatus. V2 and C1 are the record-level analogue.
- Zurek's redundant records: after decoherence, selecting a branch changes no local expectation value.
- Glauber photodetection: absorption plus amplification, with energy resolution ~ħ/Δt (C7).
- Semiclassical gravity with collapse breaks ∇·T = 0 (Bianchi). Tilloy–Diósi gave a Newtonian version.

**Implications.**
- Known detection is "catch first, record later", and no anomalous heating of isolated cold matter is seen. That fits a world where every record is settled.
- Under the field route, A13's lone-excitation weight c·P_singlet (star-sharp per A19 R1), and any energy-tracking F acting on lone excitations, must form records at ≲ 4e-48 per nucleon per second.

**Falsifiers.**
- Spontaneous heating of isolated matter with a ħ²/(mσ²) mass scaling.
- A change with no catch-with-emission or amplification process, which triggers A23's kill condition.
- Prompt next-tick records after catches, which cost about ħ/τ.
- Static negative-mass ghosts.

## 6. Open edges and next steps

1. **A catch-with-emission process in A13's model.** Its change conserves the excitation number, so the spare energy must go to another excitation (Auger-like) or to a field sector (A23 F1). This is the tiny toy above.
2. **A lower bound on κ** (a WAY-type inequality), and whether a formation weight supported on caught configurations can make κ small.
3. **Ticked residual and the doubled channel.** The residual reaches about 1/m; the doubled channel needs suppressing (B4).
4. **Momentum and centre-of-energy ghosts** of unsettled records in 3D.
5. **A 3D illuminated mover with traps near its path.** This tests A19's straight trail with settled records (medium size, not run).
6. **Moving records** that are caught static configurations rather than hopping excitations.
7. **Owner decision** (in the axioms' register): does a record form only on a caught, settled possibility, slowly compared with the beat? This is not implied by Record or by the formation weight.

## 7. Plain-language summary

A record can form without changing the total energy, but only when what it locks has already been settled: the change has already passed the difference on to other places, so the rival possibilities no longer overlap through any of that spot's links to its neighbours. Locking something that is still freely spreading, whether the moving thing itself or a small thing that just bounced off it, always jolts it by about half of its whole energy range, which on the finest grid is enormous; and if gravity is a field fed by energy, that jolt would leave a phantom weight behind for ever. What works is "catch first, record later": the small thing is caught at one place, its spare energy flies off as a new ripple, and the record forms at the catching place. Once the ripple has left, that record costs nothing, and the moving thing still feels only a soft nudge. If such a record forms with a steady chance, its cost is set by how quickly it forms after the catch, the quicker the bigger, so the gravity-as-field idea needs records that form only on caught, settled possibilities, slowly, and never directly on something still spreading.