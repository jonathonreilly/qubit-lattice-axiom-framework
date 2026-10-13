# Panel F synthesis: grid stretching, the grid's extra fermion mass, and the strain-covariant critical-mass rule (2026-10-13)

## Provenance

- **Panel:** five Opus 5.5 lenses at xhigh. Lattice field theory, GR/GW, condensed matter/emergent gravity, precision phenomenology, and a foundations skeptic.
- **Brief:** every lens received the same dossier (`DOSSIER.md`).
- **Not independent:** the panelists are the same model family as the supervisor and the C5 workers.
- **Synthesis:** written by the supervisor, also Opus 5.5. The supervisor's own thread is folded in and marked [sup].
- **Status:** none of this is refereed.
- **Statements:** `*_statement.md`. Scripts are in `scripts/C5/panel_F/<lens>/`.

## 1. Answers to Jon's questions (consensus)

**(a) What is "grid stretching"?**
- The sites never move. Z³ is fixed (`AX:37-41`).
- "Strain" is an effective metric field on the fixed grid, the graviton. It changes how matter hops, so that long waves travel as if lengths differed by direction. The condensed-matter comparator is strain in graphene, which acts through bond strengths.
- **Key point (all five lenses):**
  - In GR a uniform stretch is only a change of coordinates, so it cannot change a rest mass.
  - On a fixed grid it is physical, because the grid is an absolute ruler.
  - Every shear problem in C5 comes from that one fact.
- F1's "no volume-preserving flow on the torus" is the momentum-space form of this. The referee adds that it needs the origin-fixing hypothesis.

**(b) Why does the grid give fermions extra mass?**
- On a grid, each fermion naively comes in 8 copies (Nielsen–Ninomiya).
- The root removes the 7 extras with a Wilson-type term. It weighs them 0.36, 0.71 and 1.07/a, about 4e18–1.3e19 GeV at a = ℓ_P.
- That term breaks the chiral symmetry that would keep the real fermion light. Loops then give the real fermion an additive mass:
  - δm = 0.0419 e²/a ≈ 0.4% of the grid scale in QED, about 5e16 GeV, or 1e20 electron masses;
  - about 2% of the grid scale for quarks.
- The root cancels this by hand. The cancellation has to be right to about 1 part in 1e20.
- **This is not something every grid does.** Staggered fermions keep a remnant chiral symmetry and get no such mass. The condensed-matter lens proves this survives the SF strain.

**(c) How big is a fermion compared with the grid?** Taking a = ℓ_P, in grid sites across:

| particle | sites across |
|---|---|
| electron | 2.4e22 |
| light quark | ~5e21 |
| proton (radius) | 5e19 |
| top quark | 7e16 |

- A fermion is a smooth wave spread over about 1e66 sites.
- Its motion feels the grid only at (ma)² ~ 1e-45.
- The grid reaches it through loops, which see every wavelength down to a.
- **a = ℓ_P is load-bearing and not asserted by the axioms** (SRP:39-41). If G is held at its observed value, the Earth exceedance scales as ℓ_P/a and vanishes for 1/a ≲ 8e10 GeV. The campaign mapping instead builds in G = a².

**(d) How is a fermion built on this grid?**
- **Supplied, not derived.**
- Four components are forced: one site's M₂(C) gives only 3 anticommuting matrices, which is enough for a massless Weyl fermion but leaves no room for a mass.
- The root's 4-component Wilson band and its 22.5 Dirac fields per edge are put in by hand.
- **Owed:**
  - a qubit→fermion map, which in 3D needs an emergent Z₂ gauge field or strings;
  - a way to fit the root's ~90 fermion modes per site with one qubit per site, so a root "site" is at least a 90-qubit block;
  - chiral SM couplings, since a Wilson term is not SU(2)×U(1) invariant.
- The axioms' own named route is staggered (`AX:178`).

## 2. Corrections to the supervisor's plain explanation (all lenses agree)

| supervisor wording | correction |
|---|---|
| "the grid tries to give them a huge mass, about the grid's own energy scale" | **Half right.** It is this way of removing the copies, not grids in general. The copies sit at the grid scale. The real fermion gets 0.4–2% of it, still about 1e20 m_e. |
| "as … the strain inside the Earth does" | **Wrong.** The stretch is the passing wave's own. The Earth supplies the fermions. (Whether a static mass leaves a traceless stretch in the grid frame is a separate, open and possibly larger question; see §4.) |
| "drag" | **Wrong physics.** It is stiffness, which gives the graviton a mass inside matter. LIGO-band waves die off within about 55 m and are reflected: the Earth would be a mirror, not molasses. No energy is absorbed. |
| "GW170817 could not have passed" | **Conditional.** It assumes the canonical mapping, a = ℓ_P, and the U = 1 lift; the F1 referee recorded OPEN. The margin, ~1e8, is large. |
| "fermions stay exactly as light, however stretched" | **Overstated.** Better: "stretching the grid cannot give a fermion mass." Real masses still change by about α·t² times themselves, which is negligible. Only uniform stretch is covered, and only the additive part. |
| "what Einstein's theory already says" | **Right about the target, not the mechanism.** GR gets this from a symmetry; the rule imposes it in one channel. |

## 3. Verdict on P-R19-34a: 5/5 "sound with conditions"

**Consensus conditions:**
- **C1. State it on-shell.** "The pole mass at m₀ = m_c(h) vanishes at every uniform strain, every order." For confined quarks use a PCAC/Ward form. Cover all strain channels: trace, E_g and T₂g. Only E_g has been computed, and the registered photon law is singular for T₂g (G-F5a).
- **C2. It is necessary but not sufficient.** Power counting (condensed matter, phenomenology, GR, F5) says only channels with a Planck-size coefficient can reach the bounds:
  - the vacuum stiffness;
  - the **Higgs mass²** (pheno estimate: δv/v ~ 1e32 t², about 1e20 over clock bounds);
  - the Wilson additive mass, which this rule covers.

  Channels proportional to the particle's own mass (multiplicative, gluonic, Pauli/clover) are safe by about 1e10. F5 agrees: z″ μ_ρ ~ 8e-43.
- **C3. Add a companion light-cone clause** (lattice). Lattice QCD never re-tunes m_c(ξ) without also re-tuning ν(ξ). The strained speed rows are live: R19-31 has a scalar ∂_hκ and a birefringent photon.
- **C4. The vacuum knock-on must be absorbed by (Σ) or (S\*).** Otherwise the root moves (F5).
- **C5. Count honestly.** It is zero numbers under the law-functional convention, and a function per class per order under codimension counting. It "imposes rather than predicts", so after adoption, equivalence-principle and local-Lorentz tests stop testing the framework.

**The convergent proposal [sup + GR + skeptic + pheno].** Replace the growing list of clauses with **one primitive**:

> Every zero-strain renormalization condition holds on every uniformly strained law.

Equivalently: matter and vacuum see the grid's strain only as a metric.

- This one statement covers (Σ)/(S\*), the fermion critical mass, the Higgs mass², the vacuum stiffness and the light cones.
- GR gets all of this from diffeomorphism invariance; here it is imposed.
- It is honest bookkeeping: the framework then makes no prediction about how matter couples to gravity at low energy.

**Dissent and alternative (4/5 name it): the staggered route.**
- A staggered (one-mode-per-site) fermion, made from the root's own odd box symbol, keeps U(1)_ε under SF. So δm(t) ≡ 0 by symmetry: a mechanism, not a rule. This is proved by the condensed-matter lens and unrefereed.
- **Cost:** two same-mass twin copies ("tastes") per field. These run against R9-1's Z-width exclusion unless they are assigned to physical species. The four rows must also be re-solved with one fewer knob.
- The skeptic and the condensed-matter lens expect a taste wall.

## 4. New observational points raised

- **Clocks under the nHz background (pheno).** The uncorrected fermion channel makes m_p/m_e drift by about 1e-8 per year, against clock bounds of about 4e-17 per year. That is an exceedance of about 2e8, and it does not use the graviton-mass bridge. It is an independent second row.
- **Static fields (GR, pheno).** If a static mass leaves a traceless stretch in the grid frame, the uncorrected channel shifts m_e by MeV at the Earth's potential. That would be a catastrophic violation of the equivalence principle, so the rule matters more for static fields than for waves. Whether static fields do this is uncomputed.
- **Binary pulsar (pheno).** The rule's own m_f-proportional residual sits about 16× above F2's toy pulsar row. This is suggested; it was computed under H-cov only.
- **R19-21's Higgs-shifted vacuum-stiffness channel** is the same order as F1 in rock and is covered only by (S_loc), which is OPEN (GR, F5).

## 5. Proposed next tests (not registered; owner's call)

1. **F6, the Higgs mass² strain Hessian under SF** (pheno T4). Expected SCALAR-HAZARD by ≥1e20; if so, the single primitive (§3) is needed.
2. **NF-1, staggered strain control** (skeptic and condensed matter). Expected NF-ZERO on strain, then NF-TASTE-WALL overall.
3. **G1, the Earth-row closure budget** (GR): T₂g, the R19-21 channel, residuals, and a Noether check at a density step.
4. **F6-cone, a strain-covariant light cone plus the trace channel** (lattice).
5. **G-Λ, the gluonic channel** (condensed matter). Expected safe.

**Supervisor recommendation:** run 1 and 2 in parallel first. Test 1 decides whether "fermion rule only" is enough; it is very likely not. Test 2 decides whether a mechanism can replace the rules for fermions.

## 6. The supervisor's own thread, compared with the panel

- I had written "the grid tries to give a huge mass, about the grid scale", "drag", and "strain inside the Earth". The panel corrected all three; I accept the corrections.
- I had not flagged:
  - that a = ℓ_P is load-bearing and not asserted by the axioms;
  - the Higgs mass² channel as the larger hazard;
  - the clock row;
  - the staggered mechanism under SF.

  Those came from the panel.
- The panel did not dispute the F1, F2 and F5 numbers. All five reproduced or relied on F1's 3.6e-9 eV and its 1.6e8 exceedance.
- The F5 report's "Earth ≈ 5 MeV" for the Higgs channel is not reproduced by any lens. It is flagged to the F5 referee.
