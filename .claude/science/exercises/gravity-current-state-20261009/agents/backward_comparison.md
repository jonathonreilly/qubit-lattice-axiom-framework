# Backward reasoning: supervisor comparison of B1, B2 and the supervisor thread (2026-10-09, before the referee)

**Provenance.**
- B1 (physics-first) and B2 (framework-first) are Claude Opus 5.5 at xhigh. They ran independently, and neither read the other.
- B1 also did not read the supervisor thread.
- The supervisor thread was written before either reported (`supervisor_thread.md`, "Follow-up 2").
- All three are the same model family. The referee (codex sol) is pending.

## Where all three agree (suggested; each step rests on theorems whose hypotheses are listed in the reports)

1. **No physical coordinates.** The grain of the substrate must not act as a physical coordinate system.
   - Fixed, readable labels are the "gravitational Higgs" phase: the TT mass equals the shear modulus.
   - Only a gauge redundancy forbids every local mass form. B1 c2 proves this: the gauge directions span Sym². Finite point groups and Lorentz symmetry never forbid it (B1 c2, B2 c2).
2. **Time and space alike.** One light cone without tuning needs Lorentz invariance in law, or a time–space symmetry (hypercubic) together with exact gauge invariance in every sector (Collins; T1; K7a).
3. **The graviton is a gauge mode of the geometry itself** (Weinberg–Witten). With a Lorentz-invariant infrared, universality (Weinberg) and nonlinear GR (Deser/Wald) come free. So the hard core is: a gauge redundancy acting on h, plus one cone.
4. **Symmetry "in law" is not enough. The noise must be handled in each realization.**
   - **B1:** the gauge redundancy must hold per realization; noise may couple only through operators of dimension ≥ 4. Its c5 closes the 4D Euclidean random lattice: white noise, about 0.06 per site.
   - **B2:** no classical locally finite configuration carries the continuous symmetry (Lemma Q, which needs narrowing; see below), so either a per-realization gauge-invariant coupling or a coherent (unrecorded) micro-geometry is required. The response must vanish at least as ω³ (c1).
   - **Supervisor:** the noise must be removed by the dynamics (a quantum sum over patterns), not by freezing.
5. **Records help only as spacetime events** (counted and ordered; count = volume, which gives unimodular gravity and Λ ~ 1/√N of the observed order). As persisting located objects they hurt: they are labels, they define a rest frame, and they are quenched noise.
6. **The owner's "neighbourhood moves across the substrate" helps only in its relational reading,** where the law never sees the sites. It then has to become spacetime-causal (B1: class II) or coherent (B2: candidate C).

## Where they differ, or add something

- **B1's classes.** B1 adds explicit substrate classes: III (discretization as a summed gauge: spin foams, CDT, Regge sums) and IV (discreteness only in spectra: LQG). B2's candidate C, the coherent relational substrate, is the framework-language version of III/IV.
- **B1 c4 (checked arithmetic): geometry-bearing records cannot lock matter.** At Planck density, records that lock non-conserved matter possibilities would heat or Zeno-freeze matter by more than 100 orders of magnitude.
  - **This is in tension with B2's candidate wording B** ("each record is an event … locks exactly one admissible possibility"). It is consistent only if the possibility an event-record locks is not a non-conserved matter observable.
- **B1 c4: a frozen-box volume law exceeds S_BH by about 2.4e38** for a solar-mass hole. B2 reaches the same direction from the branch note.
- **B2's recorded-vs-unrecorded fork, and its two cheap tests** (T-2: coherent against frozen substrate; T-3: classical record substrates' response exponent). B1's Test 1 is E1′(b) done analytically; Test 2 asks whether the hypercubic tick keeps one graviton speed under interactions.
- **The tuning number, reconciled.**
  - B1 gives μ ≤ 1.1e-104 M_Pl⁴ per Planck cell (non-reduced M_Pl).
  - SUMMARY §5 gives "about 1e-98", which is relative to the natural size with K3a″'s coefficient of about 1e-3 per cell and the reduced Planck mass.
  - These are the same bound in different normalizations. The summary should state both.

## What I check or flag for the referee

- **B2's Lemma Q is too strong as written.** A one-parameter boost or shear subgroup fixes points: an x-boost fixes the transverse plane, and the shear exp(t e₁e₂ᵀ) fixes e₁. So {0, e₁} is invariant under a one-parameter group. A correct version needs the full SL(d) (or AN, or the Lorentz group), or a group acting without fixed points on the configuration. The use B2 makes of it, the full protecting group, survives.
- **B1 §2.10 (annealed vs quenched).** The "no scattering in a Lorentz-invariant translation-invariant state" argument has to be stated with its hypotheses: on-shell massless probe, energy–momentum conservation, a gapless vacuum, collinear exceptions.
- **The class table.** Check the entries "CDT foliated: ✗ C" and "spin foams Lorentz covariant ✓?".
