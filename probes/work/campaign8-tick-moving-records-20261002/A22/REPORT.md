# A22 report: does stepping on ticks fill the time-doubled partner states, can a local interaction stop it, and is the doubled content harmless?

All files are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A22/`. Each script `X.py` writes `out_X_<args>.txt` and `time_X_<args>.txt`. The wrapper `run.sh` and the helper `core1d.py` are copied from A19.

**Grades.** EXACT means proved or exact arithmetic. CHECKED means a numeric check with a stated tolerance. ARGUED means reasoning without proof. COMPARATOR means literature, cited and not adopted. Everything below is a supplied toy. I1 (records form on ticks) is a named conditional.

---

## 1. Question

Suppose the change steps on ticks (I1). Then interacting content populates the time-doubled partner states: content staggered at the tick frequency.
- Can a strictly local, reversible interaction suppress this?
- If not, is the doubled content invisible to records, and so harmless?

Along the way:
- Pin down the symmetry behind A19's 50/50 split, and classify which interactions keep or break it, including the covariant ones.
- Measure the doubled weight against interaction type, mass and relative momentum.
- Test whether a small change per beat suppresses doubler production exponentially in many-body settings.
- Test visibility to records, and say what the doubled content does with energy and gravity.

## 2. Answer

**Conditional. The premise holds only for maximal steps.**

**(i) When the partner exists [EXACT].** An exact time-doubled partner exists if and only if one partner set is fully swapped every beat. In formula terms, cos θ_e cos θ_o = 0 for the two-layer round. This is the step that lets light run at the lattice cone (A5's Dirac step, A19's round).

**(ii) Interactions cannot remove it in that step [EXACT, CHECKED].**
- The joint staggering Λ = ∏ σ_s^{n_s} survives every record-basis-diagonal interaction and every spin-½-covariant gate. Here σ = (+,−,−,+) repeats with period 4 along the conveyor axis.
- So no such local, reversible interaction removes the doubled channel.
- Covariant interactions act in one Λ-lane only, which makes slow collisions maximally doubling:
  - distinguishable contact pairs: 41–50% of the outcome is doubled;
  - identical excitations under the purely covariant round: 92–99.9% for slow pairs.
- Non-covariant phases that act alike on both lanes do suppress it:
  - in 1D, D → 0 roughly as k² at low momentum (CHECKED trend);
  - in 3D, only by tuning two scattering lengths equal (ARGUED).

**(iii) In that step the doubled content is not reliably harmless.**
- *Hidden from:* single-tick record-basis-diagonal formation and energy-selective windows (EXACT).
- *Behaves like ordinary content:* it moves, collides and keeps comoving clocks exactly as ordinary content does.
- *Leaves traces:* tick-alternating lattice-scale fringes, partly incoherent collisions, and changed odds under non-diagonal formation weights. Under any lapse in the change per beat it would carry a Planck-scale mass shift (ARGUED).

**(iv) Small steps remove it [EXACT, COMPARATOR, CHECKED trend].** Suppose every local term changes by a small angle θ0 per beat; A18 needs θ0 ≲ 6×10⁻³ anyway.
- The doubler's mass becomes π − θ_e − θ_o ≈ π, so the region of the quasi-energy circle at π is empty.
- No collision of fewer than about 90–200 excitations can populate any π-shifted state (EXACT).
- Many-body production (heating at the tick frequency) falls like e^{−c/θ0}. This rests on comparator theorems; the toy gives c ≈ 10–16 (CHECKED trend).

**Verdict:** the doubling is a suppressible nuisance. A small change per beat suppresses it, not interactions. It is fatal only for maximal-step rounds.

## 3. Derivation

**Conventions.**
- Site x = 2j + α, with cell j and sublattice α ∈ {a, b}. The sign pattern is σ_x = (−1)^{⌊(x+1)/2⌋}, which equals (−1)^j·σ_z per cell.
- A *flipped* pair has σσ = −1: the in-cell bonds (2j, 2j+1) and pairs two sites apart.
- An *equal-sign* pair has σσ = +1: the between-cell bonds, the same site, and pairs four sites apart.
- A19's round is a full swap on in-cell bonds and an angle π/2 − m between cells.
- Gates are exp(−iθ SWAP) (A10 S1), optionally with a |11⟩ phase φ.

**D1. Conjugation rule [EXACT; CHECKED 1.7e-16, `sym_check.py`].**
- For a number-conserving gate g on (s,t), conjugating by Λ multiplies g's hop amplitudes by σ_sσ_t and leaves every diagonal entry unchanged (|00⟩ and |11⟩ phases, on-site parts).
- Hence g is Λ-invariant if and only if it has no hop or σ_sσ_t = +1.
- And ΛgΛ⁻¹ = (−1)^{n_s+n_t} g if and only if σ_sσ_t = −1 and g is a pure hop, i.e. a full swap with any |00⟩/|11⟩ phases.
- So a round with one pure-hop layer on flipped bonds covering all sites, all other hopping on equal-sign bonds, and any diagonal layers satisfies **ΛUΛ⁻¹ = (−1)^N U**.

Checked on an 8-site ring in the full Fock space:

| Round | Doubler residual ‖ΛUΛ⁻¹ − (−1)^N U‖/‖U‖ |
|---|---|
| A19 round | 1.7e-16 |
| A19 round + |11⟩ phase on odd bonds | 1.7e-16 |
| A19 round + |11⟩ phase on even bonds | 1.7e-16 |
| A19 round + diagonal NNN phase | 1.7e-16 |
| A19 round + staggered on-site phase | 1.7e-16 |
| In-cell layer detuned to π/2 − 0.1 | 0.28 (broken) |
| Added NNN partial swaps | 1.0 (broken) |
| Two full-swap layers on flipped pairs | doubler broken (1.4); plain symmetry exact (2.7e-16) |

**D2. Spectral criterion and the doubler's mass [EXACT; CHECKED].**
- For one excitation: cos ω = cos θ_e cos θ_o − sin θ_e sin θ_o cos K.
- The spectrum is invariant under a half-turn of the quasi-energy circle if and only if cos θ_e cos θ_o = 0.
- There are always two gaps, with centres exactly π apart. Their half-widths ("masses") are:
  - ordinary cone: M_ord = |θ_e − θ_o|;
  - doubler: M_dbl = π − θ_e − θ_o.
- For the massless walk, the light speed is **v = sin θ = cos(M_dbl/2)** cells per tick:
  - light at the lattice cone ⟺ a massless doubler degenerate with the ordinary cone;
  - light at ≲ 1% of the cone (A18) ⟺ M_dbl ≈ π.
- CHECKED: v matches cos(M/2) to 1e-6. The half-turn distance of the spectrum is 0.003 (grid resolution) when θ_e = π/2, and equals the mass difference otherwise (e.g. 0.100 for masses 0.30/0.40).

**D3. Lanes and the 50/50 split [EXACT; CHECKED].**
- In the two-excitation sector, Λ = σ_{x_A}σ_{x_B} commutes with the two-body step. The lanes are Λ = ±1.
- The ordinary in-state is orthogonal to its image Λ|in⟩, so it splits into the two lanes with weight ½ each.
- Define S_±^ord = 2 Q_ord S P_±|in⟩. The doubled outgoing amplitude is then **Λ(S_+^ord − S_−^ord)/2**.
- If the interaction lives in one lane, the other lane is exactly free. Then **D = ½‖(S − 1)|in⟩‖²** in any dimension: half of whatever the interaction does goes into the doubled channel. The doubled share of reflected weight is exactly ½.
- The contact x_A = x_B lies in the equal-sign lane (σ² = 1). That is A19's 50/50.
- CHECKED:
  - the share is 0.5000 in every one-lane run;
  - in the flipped lane, the two-excitation dynamics of the covariant round equals free bosons to 3e-15 (double occupancy 2.5e-31);
  - in the equal-sign lane it differs by 0.94.
- Also EXACT: for distinguishable partners with diagonal interactions, each partner's own Λ already anticommutes with the interacting step (Λ_A U₂ Λ_A⁻¹ = −U₂). "Ordinary vs doubled" is therefore a hidden two-valued label per particle (a temporal "taste"), and collisions flip it jointly for both partners.

**D4. Classification [EXACT, from D1/D3].**

| Term | Placement | Keeps Λ? | Lane it acts in | Spin-½ covariant? |
|---|---|---|---|---|
| exp(−iθ SWAP) | equal-sign bonds | yes | equal-sign (hard-core rule) | yes |
| full swap (θ = π/2) | flipped bonds | yes (flips) | none (a permutation, free) | yes |
| exp(−iθ SWAP), θ ≠ π/2 | flipped bonds | no; the doubler gets mass π − θ_e − θ_o | — | yes |
| |11⟩ / contact phase | equal-sign pairs (r ≡ 0 mod 4, odd bonds) | yes | equal-sign | no (splits the triplet; U(1) only) |
| |11⟩ / diagonal phase | flipped pairs (even bonds, r = ±2, NNN) | yes | flipped | no |
| NN phase on both bond types | — | yes | both | no |
| On-site phases (incl. staggered mass) | any | yes | one-body | no |
| Hop with diagonal part, or partial NNN swap, across flipped pairs | — | no | — | the SWAP_{s,s+2} form is covariant |
| Pair creation on flipped pairs | — | no | — | no |

**D5. Covariance [EXACT for nearest-neighbour gates; ARGUED for 3D stars].**
- Under spin-½ soldering, only the full swap keeps Λ on a flipped bond, and it is interaction-free. Every covariant gate on an equal-sign bond keeps Λ, and its only two-body effect lies in the equal-sign lane.
- A19's |11⟩ contact phase is not spin-½ covariant.
- For three consecutive sites, the SU(2)-invariant gates that commute with Λ are generated by the equal-sign SWAP (EXACT). The one-excitation block fixes the gate, and the site of the other sign must be an eigenvector.
- In 3D with σ varying along one axis, every star contains exactly one site of the minority sign. So no covariant correlated hop across both lanes fits inside a star (ARGUED).
- Consequence: with covariant gates and an exact doubler, the flipped lane is always free, which gives maximal doubling.
- The covariant way out found here is to detune the conveyor (θ_e ≠ π/2). That is a change of the one-body step, which splits the doubler's mass from the ordinary mass. It is not a two-body interaction.

**D6. Low-energy laws [1D threshold law ARGUED (textbook); CHECKED].**
- An interacting lane reflects totally at threshold. Therefore, as k → 0:
  - one-lane, distinguishable: D → ½;
  - covariant, identical: the equal-sign lane acts like an impenetrable gas (S = −1) and the flipped lane is free (S = +1), so the pair comes out as its own doubled image and D → 1;
  - two-lane: D → 0, as |ℓ_+ − ℓ_−|² k², i.e. linear in the kinetic quasi-energy (Eτ), not (Eτ)².
- Massless content: a nearest-neighbour phase on one bond type gives D = sin²(φ/2) exactly at every momentum. The same phase on both bond types gives D = 0 exactly. The contact never acts, because chiral movers sit on opposite sublattices at the end of each tick.
- In 3D (ARGUED): S_± ≈ 1 − 2ika_±, so D/σ_scatt → ((a_+ − a_−)/(a_+ + a_−))². This is half for one-lane interactions, and vanishes only when the two scattering lengths are tuned equal.

**D7. Kinematic closure by the one-body step [EXACT; CHECKED].**
- If M_dbl − M_ord = 2ε, doubled pairs cannot be reached when the kinetic quasi-energy per particle is below 2ε.
- CHECKED with θ_e = π/2 − 0.05, θ_o = π/2 − 0.3 (masses 0.25/0.35; threshold k ≈ 0.25): D stays at the method floor below threshold and jumps above it (table in §4).

**D8. Small steps, few bodies: the arc lemma [EXACT; CHECKED `arc_check.py`].**
- Relative to emptiness, each covariant layer contributes the generator 2θ Σ_b P_singlet,b. In the n-excitation sector this is bounded by 2nθ. Diagonal phases J add at most nJ.
- Monotone-path lemma (unitary Hellmann–Feynman): every n-body quasi-energy lies in [0, n(2θ_e + 2θ_o + J)].
- If that arc is shorter than 2π, there is no time-umklapp and no π-shifted partner in that sector, and quasi-energy is conserved exactly as a real number.
- For θ0 = 6e-3 this holds for n ≲ 200 (1D) or ≈ 90 (A10's 3D cycle, 6 layers per beat). For the 3D cycle the π-region is empty whenever θ < π/12. That is consistent with A10's census (π-gap open up to θ ≈ 0.7).

**D9. Small steps, many bodies [COMPARATOR; CHECKED trend; ARGUED extrapolation].**
- Umklapp needs about 2π/(4θ) coordinated elementary moves.
- Floquet-prethermal theorems bound the heating time below by exp(c·Ω/J), with Ω/J ~ 2π/θ.
- Toy estimate: c ≈ 10–16 (§4).
- Extrapolated to θ0 = 6e-3, the heating time is about e^{10/0.006} ≈ 10^724 ticks.
- Requirement (ARGUED): no vacuum heating beyond the observed vacuum energy, at Planck-scale spacing, needs c/θ0 ≳ 435–570. The toy gives about 1700.

**D10. Visibility [EXACT; CHECKED `task4.py`].**
- Λ commutes with every record-basis cut and every diagonal formation weight. So ψ and Λψ give identical record statistics, and site densities are identical at every tick (difference 0.0).
- Coherent ordinary + doubled content produces fringes that flip every tick and repeat every 4 sites (ratio 1.623/0.377, alternating).
- An A12 energy window's response to Λψ equals the π-shifted window's response to ψ. With DPSS windows of T = 8–64 ticks, the doubled/ordinary ratio is 1.5e-13 to 2.9e-10.
- A13's c·P_singlet weight maps to P_triplet0 on flipped bonds, so it is not Λ-invariant.
- **Correction to the premise:** the doubled content made in collisions runs its comoving clocks *forward*, at the ordinary rate (+0.6294 vs +0.6294; dW/dm = 0.6292). A5's "backward clock" (−0.6294) belongs to the other branch at K + π, which is the image of the antiparticle branch.

**D11. Energy and gravity [ARGUED].**
- The doubled content has the same density, velocity, kinetic energy and collisions as ordinary content. Each doubled particle's quasi-energy is offset by π (a pair's by 2π, i.e. zero).
- Under A18's angle lapse (θ → Nθ), the full swap becomes partial. The doubler's mass becomes π(1 − N) + Nm while the ordinary mass is Nm.
  - So doubled content feels a potential of about πU per tick: a Planck-scale violation of the equivalence principle.
- If records source gravity with diagonal formation, doubled content sources like ordinary content. With windowed formation it is dark, but it converts back in collisions.

## 4. Checks

All runs used `nice -n 10`, the four thread caps at 1 and a 60 s alarm. The longest took 55 s; peak memory was ≤ 134 MB. One combined run that included k = 0.0125 hit the alarm; it was discarded and rerun in batches without that point.

| Script | What it tests | Key result |
|---|---|---|
| `sym_check.py` | D1, D2, flipped-lane freedom | As in D1/D2/D3 |
| `arc_check.py` (12-site ring, n = 1, 2, 3) | D8 arc bound | Small steps (0.1, 0.1, J = 0.1): arcs 0.40/0.78/1.13 within bounds 0.5/1.0/1.5. Moderate steps (0.25, 0.2, 0.2): 0.90/1.75/2.54 within 1.1/2.2/3.3. A19 round: 5.29/5.87/6.05 (wraps) |
| `tb.py` + `two_body.py` | Exact relative-coordinate collisions, narrow packets (σ_k = 0.15k), φ = 0.8 | Tables below |
| `xcheck_chain.py` | Independent exact-qubit site simulation (256 sites) | D = 0.3326 vs relative code 0.3374 (m = 0.3, k = 0.3) |
| `heat.py`, `heat2.py` | Many-body heating vs θ | Table below |
| `eth_check.py` (L = 12) | Spread over Floquet eigenstates | sd of ⟨H0⟩/L: 0.25 (θ = 0.2) → 0.057 (θ = π/2); sd of ⟨O⟩: 0.047 → 0.019 |
| `task4.py` | D10 | As stated |

The method floor for D is 1.0e-7 (a free control with no interaction).

**Doubled weight D(k), A19 round, m = 0.3.** Rows marked "1 lane" have a doubled share of reflection of exactly 0.5000.

| Interaction | Lane | k = .025 | .05 | .1 | .2 | .4 | .8 |
|---|---|---|---|---|---|---|---|
| contact | 1 (equal) | 0.414 | 0.276 | 0.118 | 0.034 | 7.4e-3 | 1.5e-3 |
| r = ±2 | 1 (flipped) | 0.470 | 0.398 | 0.246 | 0.090 | 0.019 | 3.2e-3 |
| NN, odd bonds | 1 | 0.478 | 0.426 | 0.313 | 0.200 | 0.159 | 0.153 |
| NN, even bonds | 1 | 0.483 | 0.439 | 0.337 | 0.218 | 0.164 | 0.153 |
| NN, both bond types | 2 | 3.3e-4 | 1.06e-3 | 2.3e-3 | 3.1e-3 | 2.9e-3 | 2.0e-3 |
| contact + r=±2 at half strength | 2 | 3.5e-3 | 6.5e-3 | 5.0e-3 | 1.3e-3 | 3.0e-4 | 7.8e-4 |
| contact + r=±2 at full strength | 2 | 0.016 | 0.035 | 0.036 | 0.015 | 3.2e-3 | 1.7e-3 |
| Identical: S1 covariant | 1 | 0.980 | 0.924 | 0.762 | 0.482 | 0.249 | 0.136 |
| Identical: + |11⟩ on odd bonds | 1 | 0.994 | 0.977 | 0.919 | 0.776 | 0.590 | 0.463 |
| Identical: + |11⟩ on even bonds | 2 | 2.2e-3 | 7.0e-3 | 0.014 | 9.5e-3 | 8.4e-4 | 3.4e-3 |

- Local exponents of the two-lane cases at k = 0.025–0.035 are 1.2–1.8, rising toward 2.
- NN, both bond types: the doubled share of reflection ranges from 1e-4 to 0.78 depending on k.

**Mass dependence at k = 0.05**

| m | contact | S1 (identical) | NN both types |
|---|---|---|---|
| 0.15 | 0.053 | 0.463 | 4.9e-4 |
| 0.3 | 0.276 | 0.924 | 1.06e-3 |
| 0.6 | 0.463 | 0.994 | 1.7e-3 |
| 1.0 | 0.495 | 0.9987 | 8.7e-3 |

**Massless (m = 0), at k = 0.3 and 0.8**
- One bond type (ladder or chain): 0.15165, vs sin²(0.4) = 0.151647.
- Both bond types: ≤ 1.1e-8.
- Contact and covariant round: ≤ 8e-11.

**Doubler gapped**
- Detuned conveyor θ_e = π/2 − 0.05, θ_o = π/2 − 0.3 (threshold k ≈ 0.25):

| k | 0.05 | 0.1 | 0.2 | 0.25 | 0.3 | 0.4 |
|---|---|---|---|---|---|---|
| contact | 1.8e-7 | 1.8e-7 | 2.4e-3 | 0.019 | 0.021 | 0.010 |
| S1 | 7e-7 | 7e-7 | 0.013 | 0.151 | 0.251 | 0.216 |

  The k = 0.2 value comes from the packet's momentum tail above threshold.
- Small steps (θ_e = 0.35, θ_o = 0.25): D ≤ 4.8e-7 for contact, S1 and NN at all k, i.e. at the method floor.

**Many-body heating** (`heat2.py`). Ring, half filling. H0 = SWAPs + 0.5 n n + 0.7 n n(NNN). The step scales all angles by θ; at θ = π/2 it is A19's round plus diagonal interactions.
- Heating time t* (first log-window where the heating fraction exceeds 0.5):

| θ | 1/θ | t* (L = 14–18) |
|---|---|---|
| π/2, 1.2, 1.0, 0.85 | 0.64–1.18 | ≤ 20 |
| 0.75 | 1.33 | 160 |
| 0.7 | 1.43 | 320 (L = 18), 1280 (L = 16) |
| 0.65 | 1.54 | 640–1280 |
| 0.6 | 1.67 | > 10⁴ (L = 16, 18), > 2×10⁴ (L = 14) |

- At θ ≤ 0.5 the heating fraction stays at the dressing plateau 0.64θ² over 2×10⁴ ticks.
- Small systems also show resonant episodes: for example θ = 0.55 reaches 0.31 at L = 16.

**Should be run (bigger, not run)**
- `heat2.py 20 10240 0.6,0.65,0.7`: about 3–4 min per θ, about 150 MB. Pins the exponent c.
- `two_body.py nn,phie 0.0125 m=0.3`: about 70 s. Confirms the k² asymptote.
- A 2D/3D two-body lane test on A10's signed cycle near full swap, to test D/σ → ((a_+ − a_−)/(a_+ + a_−))².

## 5. Real-physics match

**Maximal steps (light at the lattice cone) with interactions.** These predict:
- a hidden per-particle "taste", flipped jointly in collisions with O(1) probability:
  - 1D slow collisions: 50–100%;
  - lattice-contact scattering: half of everything scattered;
- an incoherent elastic-looking channel;
- fringes that flip every tick at the lattice scale;
- a gross equivalence-principle violation under any lapse.

Tensions (ARGUED):
- coherent forward scattering of matter waves (comparator: Schmiedmayer et al., PRL 74, 1043, 1995);
- equivalence-principle tests;
- no Planck-frequency staggered matter is seen.

Comparators, not adopted:
- Nielsen–Ninomiya doubling, and Wilson's mass for doublers (here: a detuned conveyor);
- exact π-pairing as in discrete time crystals (Khemani et al. 2016; Else–Bauer–Nayak 2016).

**Small steps.** Consistent with known physics: no doubler, and exponentially slow heating.
- Comparators: Abanin–De Roeck–Huveneers PRL 115, 256803 (2015); Mori–Kuwahara–Saito PRL 116, 120401 (2016); Abanin–De Roeck–Ho–Huveneers PRB 95, 014112 (2017); Else–Bauer–Nayak PRX 7, 011026 (2017); Heyl–Hauke–Zoller Sci. Adv. 5, eaau8342 (2019); generic heating to infinite temperature without a small step: D'Alessio–Rigol 2014, Lazarides–Das–Moessner 2014.
- Falsifier: a concrete package with heating exponent c/θ0 below about 435–570 would conflict with the observed vacuum energy, or with the absence of Planck-scale events.
- All citations are from memory; verify before citing.

## 6. Open edges and next steps

1. Pin c for an A18-type package with lapse-scaled angles and the time-symmetric word, at L ≥ 20.
2. Run the 3D lane formula on A10's cycle.
3. In maximal-step worlds, do mediators' own doublers feed matter doubling at low energy? (ARGUED yes.)
4. Small steps make A12's windows easier: the π edge of the occupied arc disappears (EXACT).
5. Owner choice: is light meant to run at the lattice cone? If so, the doubler must be gapped, which in effect means a small step. If small steps are adopted (A18), the lattice cone is about 1/θ0 times faster than light; check that this carries no readable consequence beyond A5 T1.5.
6. A19's mediated registration (R3) is free of doubling under small steps (D7/D8).

## 7. Plain-language summary

If every beat moves the unrecorded possibilities a whole step along the grid, everything that moves gets a hidden twin. The twin flips sign from one beat to the next and from one spot to the next, but moves and collides exactly like the original. When two slow things meet in that setup, half or more of what comes out is the twin version, and no rule acting only between neighbours can stop it. The twins leave the same marks in single records, so they hide, but they still show up in finer ways: patterns that flip every beat, collisions that lose their sharpness, and very different behaviour wherever the change per beat varies, as in the gravity idea. If each beat changes things only a little, which that gravity idea already needs, the twin does not exist: no collision of a few things can make one, and a crowd makes them only at a rate that falls off extremely fast as the change per beat shrinks. So the doubling is not a flaw of beats as such; it is the price of making each beat a full jump.