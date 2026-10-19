> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# C6 findings: what takes rung 0 (one qubit per site, formation) to rung 1 (the corner model)?



| Runner | Result |
|---|---|
| `c6_A_flux_is_a_free_sector_label.py` | 20/0 |
| `c6_B_flux_energetics.py` | 3/0 (39 min under CPU contention) |
| `c6_B5_corner_sector_stability.py` | 1 |
| `c6_B6_verify_nonuniform.py` | 3 |
| `c6_C_no_registration_illustration.py` | 3 |

The shared geometry is in `c6_corner_graph.py`, built independently of the repo runners.

**Answer: no map is derived.** The 12-corner space, the π-flux background and the block embedding are all supplied, and the flux pattern was chosen to meet design targets.
- Local fermionization does not force π flux: the flux is a free sector label.
- The specified finite free-fermion sector comparisons do not select it at the tested node filling.
- Formation by translation-covariant rules from an empty start cannot register the coarse block lattice (the registration lemma, as restated by the check).

## 1. How the corner model is supplied

0. Also supplied (check): the U(1)-twisted rotation realization W, and the hopping family.
1. **Corner graph** (canonical as site–plaquette incidences). It was chosen for C4-axis avoidance, which the corner-code note itself calls "not an exclusion theorem".
2. **BKSF encoding with repetition halves:** 48 qubits per site.
3. **Signed loop stabilizers i^n F ∏A.** F is a free sign per face type.
   - The code note's default is square = plaquette = π, triangle = tube = 0.
   - The long-wavelength and scale-ladder notes use tube = π.
   - F is imposed as a static background, and loop terms commute with hops.
4. **Rung-1 dynamics:** supplied one-fermion Hamiltonians.
5. **Rung 0 → 1 map:** a hand-placed O-equivariant 5×5×5 block with 77 spectators. It breaks fine translations.

None of these is derived from rung 0.

## 2a. Local fermionization does not force π flux (exact)

- **A1** (GF(2), L = 3, 4, 6). The face types generate the cycle space except the noncontractible classes. On even L, all 16 uniform patterns are valid sectors. Odd L adds a wrapped constraint.
- **A2** (explicit BKSF Pauli algebra on the corner graph, L = 3).
  - The "natural vacuum" flux F_C = i^n(∏ε)φ_C depends on the arbitrary labelling and order conventions. Two random conventions differ on about half the faces.
  - The canonical Bravyi–Kitaev convention gives a non-uniform pattern that is not the corner pattern.
- **A3.** Flipping one hop's dictionary sign preserves the algebra and flips F on the faces through that edge.
- **A4 (what selects the pattern: design targets).** On L = 4, with the worker's own PSG:
  - C4⁴ = −1 forces square = π;
  - commuting translations force plaquette = square;
  - an O-fixed momentum forces tube = π.

  So {1011, 1111} survive and the triangle is free.
- **Gauge-invariant statement in the standard convention:** the repo's corner model with t1 = −1 has flux π through every elementary face (real background, λ = 0). With the chiral term the triangle phase is π + 3 arctan λ.

## 2a'. Energetics does not select it

Hop-only Hamiltonians are block-diagonal over flux sectors. The method used Bloch on a 2³ supercell, cross-checked by real-space diagonalisation at L = 4, plus diamagnetic and particle–hole checks.

| Filling | Result |
|---|---|
| ν = 1 (node filling) | The corner pattern ranks 15th–16th of 16 uniform patterns, 1.5–1.9 per site above flux-free. Descent drives squares and triangles to about 0, but plaquette (~0.5) and tube (~0.3) remain (check). With the chiral term it ranks 6th of 16 |
| ν = 7, t2 = 1 | Best uniform pattern, but unstable: 192 of 288 flips lower it; a non-uniform sector is 0.125 per site lower |
| ν = 8 | A local minimum, but 1101 is 1e−4 below it |
| ν = 6 | Non-uniform sectors beat all uniform ones by 0.78 per site |

Hop dynamics conserves flux, so a formation-random sector would stay frozen.

**Scope:** free fermions; uniform and period-2 sectors; greedy search; hop magnitudes only. The Lieb / Macris–Nachtergaele 4-cycle rule does not apply, because the corner graph is not bipartite.

## 2b. Formation

- **Flux background.** It is deterministic Z2 data. A noise-blind rule can write it with coding radius 0, so B3 neither excludes nor supplies it. B3 controls connected correlations. A symmetry-qualified order statement additionally requires the label-symmetric rule and invariant joint noise; biased radius-zero rules are allowed.
- **Registration-factor argument for jointly iid covariant empty-start formation (not an exclusion of every encoding).**
  - *Dimension bound.* A corner site's even mode algebra needs ≥ 12 qubits, a density bound. For a registered embedding the coarse sites form a sublattice of index m ≥ 12 (the smallest O-invariant index ≥ 12 is 16). The earlier corollary "no fine-translation-covariant encoding exists" is not proved: fractional-translation encodings are not excluded (check).
  - *Mixing (as restated by the check).*
    - For any measurable equivariant factor of iid noise (finitarity is not needed), there is no a.s. map o into Z³/Λ with o∘T^v = o − v for index m ≥ 2. Nor is there one into R³/Λ′, by weak mixing, so there are no Bragg peaks off 2πZ³.
    - The hypotheses are load-bearing: an empty start and a translation-covariant rule. A periodic deterministic B or a y-dependent rule registers trivially.
    - The flux background's radius-0 writing presupposes such a registering rule.
  - The same applies to translation-invariant finite-depth circuits from product states.
  - A planted start slice is forgotten at the factorial rate (B3 T3).
  - **Illustration:** the most block-favouring B3 packing gives registration amplitude ≤ 0.16.
- **Not excluded:** polycrystals, defective or amorphous packings.
- **Remaining routes, all outside covariant empty-start formation:**
  - a supplied dictionary;
  - correlated clocks;
  - global conditioning;
  - spontaneous translation breaking in a ground state;
  - corner fermions as emergent quasiparticles of a translation-invariant fine Hamiltonian, which escapes the dimension bound and is open;
  - fractional-translation encodings, where a fine translation acts as a non-translation automorphism of the corner algebra (open).

## Caveats

- A2 shows convention dependence, but not the absence of a special symmetric convention.
- The energetics covers free fermions in restricted sectors only.
- The repetition sectors are not modelled.
- The registration proof is unchecked.

## Prior art

- Bravyi–Kitaev 2002; Ball 2005; Verstraete–Cirac 2005.
- Chen–Kapustin–Radičević 2018; Chen–Kapustin 2019.
- Levin–Wen 2003; Kitaev 2006; Lieb 1994; Macris–Nachtergaele.
- O'Brien–Hermanns–Trebst 2016; Holroyd–Schramm–Wilson.

## Registration-factor proof and corrected formation boundary

For a jointly iid site field the translation action is mixing and hence weakly mixing. Suppose an equivariant measurable registration o takes values in a finite quotient Z^3/Lambda or a compact torus R^3/Lambda' with the stated nontrivial translation action. Choose a nontrivial character chi of that factor. Then f=chi(o) has modulus one and obeys f(T^v omega)=chi(−v)f(omega). It is a nontrivial translation eigenfunction, contrary to weak mixing. Thus that registration-factor premise is incompatible with jointly iid equivariant noise. This argument concerns the specified global registration variable. It does not classify fractional-translation encodings, emergent quasiparticles, defective packings or correlated starts.

A deterministic biased local rule may write a fixed label with radius zero. The connected-correlation estimate does not forbid it. Statements about a vanishing label order parameter additionally require the corresponding label-covariant rule and invariant joint noise law. The finite energy tables concern only their free-fermion sectors and tested sizes. They do not settle every dynamical flux supplier. Likewise, convention dependence of bare loop signs does not prove that all-positive bare signs are always inconsistent: special, even translation-invariant, orderings exist, as the preserved original NOTE_C6_review report records.
