# Step 8 — tests run

## T1: a signed compression channel (route F3)

**Script:** `scripts/T1_signed_compression_channel.py`. It reuses probe 18's
model definitions, extracted to `scripts/_p18_defs.py`. The output is in
`scripts/T1_output.txt`.

**Question.** Agent 2 (route 1) argued that the wall's "extra shake" half
rests on a ground-state (positive-weight) premise. By probe 11's identity
4v₁ = v₂ + 3v₀, a light-like spin-2 wave with no helicity ±1 content needs a
negative compression weight v₀ = −v₂/3, the lattice face of Einstein's
conformal-factor sign. A system in its ground state cannot supply that.

**Model.** Probe 18's isotropic metric-stored model:
- the kinetic weight comes from gauge-pattern moves (weight α: helicities 0
  and ±1) and curl moves (weight β: TT and ±1);
- the potential is the landed Einstein–Hilbert symbol plus an on-site
  stiffness m² = 1, optionally of Fierz–Pauli form (fp);
- the scalar rule is exact (reduced to ker s).

Probe 18's identity gives c₁² ∝ α/2 + β/4 (β = 1), so the helicity ±1 speed
vanishes at α = −1/2.

**Pre-registered, before running.**
- **PASS (the route is alive):** at the tuning where the ±1 weight vanishes,
  the spectrum is exactly two linear pure-TT modes; every other mode is
  frozen or has ω² = 0 to the orders checked; and no ω² < 0.
- **FAIL:** the ±1 modes stay gapless at higher order, or some ω² < 0.

**Result.**

| α | fp | TT modes | helicity ±1 modes | helicity 0 |
| --- | --- | --- | --- | --- |
| 1 (control, probe 18) | yes | ω²/q² = 1 | ω²/q² = 0.75 (light-like partners) | frozen |
| −0.51 | yes | ω²/q² = 1 | ω² < 0 at every q: **unstable** | frozen |
| **−0.50** | yes | ω²/q² = 1 | **ω² = 0 to 10⁻¹⁵ at every q up to 1.5, in three directions** | frozen |
| −0.49 | yes | ω²/q² = 1 | ω²/q² ≈ 0.005: slow partners | frozen |
| −0.50 | no | ω²/q² = 1 | ω² = 0 | ω²/q² = −0.5: **unstable** |

**Reading, corrected after the kill round.** The pre-registration was
looser than the target. It counted zero-frequency modes as acceptable, but
the target (step 1) excludes any other gapless mode. A flat zero-frequency
±1 band is gapless physical content: an infinitely degenerate zero-energy
excitation, not a gauge direction. Against the target, **T1 fails.** It
also depends on a knife edge and a frozen negative-kinetic (ghost)
helicity-0 channel. The kill round's verdict on route F3 (dead) stands. What
T1 established is recorded below.

**The raw result.** It passes the pre-registered wording, and only at a
knife edge.
- At α = −½ exactly, with helicity 0 frozen (Fierz–Pauli), the harmonic
  spectrum is Einstein's. There are two light-like pure-TT modes, and the
  three other modes are non-dynamical, with zero frequency at every
  wavelength, not only at long wavelength.
- Below −½ the sideways modes are unstable. Above it they are slow extra
  waves.
- Without the Fierz–Pauli freeze, the negative-weight channel is itself
  unstable.

**What it shows (checked, harmonic, one isotropic model).** The partner half
of the wall is a sign problem. To remove the sideways modes, the kinetic
weight of the compression channel must be negative, at exactly the ratio
α = −β/2, and that channel must be frozen.
- A system expanded around its lowest-energy state cannot have a negative
  weight: the f-sum is positive in a ground state.
- This is the lattice face of Einstein's conformal-factor problem.
  Einstein's own kinetic term (DeWitt, λ = 1) is negative on the trace,
  and his time rule hides that direction.

**What it does not show.**
- It does not show that any finite-record state realises the negative weight
  (population inversion).
- It does not show that the ratio −½ is protected by a symmetry rather than
  tuned. Hojman–Kuchař–Teitelboim says closure of the time rule forces
  λ = 1 in the continuum; whether the lattice closure forces α = −β/2 is
  open, and is programme A's step A1 again.
- It does not show that the knife edge survives interactions, where the
  negative-energy channel can feed instabilities.
- It does not cover the exact-momentum-rule branch. There the TT wave is
  slow regardless (route F1), so this route helps only the broken branch.

## Checks run by the kill-round agents

Same family, unrefereed. The scripts are in `scripts/agents/`.

| Check | Script | Result |
| --- | --- | --- |
| Smith invariant factors of the open-box stencils G, S | `snf_torsion.py` | all 1; torsion only on periodic tori (global sectors), so local mod-N-invariant characters are lifted kernel characters |
| Cauchy–Schwarz bound linking a local conjugate to the static TT response | `bogoliubov_check.py` | χ_h ≥ \|⟨[h, E]⟩\|² / (C_H q⁴): an O(1) conjugate would force an anti-Newtonian static response |
| The inverted channel in probe 18's model | `kill2_checks.py` | α* = −β/2 reproduces (v₂, v₁, v₀) = (1, 0, −⅓). The helicity-0 mode is a tachyon, with growth rate 2.45 m at the zone corner. Detuning by 1 % gives a partner or a tachyon. The walker-side defect's kernel is the uniform lapse |
| Area-law coefficient anisotropy, cubic Dirac sea | `kill3_area_law_anisotropy.py` | S/Area for a (110) cut is 1.161–1.175 × the (100) value, converged in slab thickness: not universal |
| PPN coordinates | `kill3_ppn_coordinates.py` | 0.834 × GR is a gauge splice; consistently transformed, the factor is 1 |
| Helicity coupling of radiating sources; power ratios | `kill4_checks.py`, `agent4_checks.py` | direction-averaged ±1/TT coupling = 1; the double pulsar excludes partners slower than ≈12.4 × c_TT; static conserved sources decouple from ±1 |
