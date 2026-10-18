# C6 findings: what takes rung 0 (one qubit per site, formation) to rung 1 (the corner model)?

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back.

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
- Energetics does not select it at the node filling.
- Formation cannot produce the coarse rung at all (the registration lemma).

## 1. How the corner model is supplied

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
- **Convention-free statement:** in the standard convention the repo's corner model with t1 = −1 has flux π through every elementary face.

## 2a'. Energetics does not select it

Hop-only Hamiltonians are block-diagonal over flux sectors. The method used Bloch on a 2³ supercell, cross-checked by real-space diagonalisation at L = 4, plus diamagnetic and particle–hole checks.

| Filling | Result |
|---|---|
| ν = 1 (node filling) | The corner pattern ranks 15th–16th of 16 uniform patterns, 1.5–1.9 per site above flux-free; descent goes to near flux-free. With the chiral term it ranks 6th of 16 |
| ν = 7, t2 = 1 | Best uniform pattern, but unstable: 192 of 288 flips lower it; a non-uniform sector is 0.125 per site lower |
| ν = 8 | A local minimum, but 1101 is 1e−4 below it |
| ν = 6 | Non-uniform sectors beat all uniform ones by 0.78 per site |

Hop dynamics conserves flux, so a formation-random sector would stay frozen.

**Scope:** free fermions; uniform and period-2 sectors; greedy search; hop magnitudes only. The Lieb / Macris–Nachtergaele 4-cycle rule does not apply, because the corner graph is not bipartite.

## 2b. Formation

- **Flux background.** It is deterministic Z2 data. A noise-blind rule can write it with coding radius 0, so B3 neither excludes nor supplies it. B3 excludes only spontaneously selected background data, such as the sign of the chiral term.
- **The coarse rung is unreachable from formation (proof sketch, the worker's own, unchecked).**
  - *Dimension bound.* A corner site's even mode algebra needs ≥ 12 qubits. So rung-1 sites form a sublattice of index m ≥ 12, and no fine-translation-covariant encoding exists.
  - *Mixing.* A finitary factor of iid is mixing. An equivariant registration map into Z³/Λ would give P(o = 0 and T^λ o = 0) = 1/m along λ ∈ Λ, against the mixing limit 1/m².
  - The same applies to translation-invariant finite-depth circuits from product states.
  - A planted start slice is forgotten at the factorial rate (B3 T3).
  - **Illustration:** the most block-favouring B3 packing gives registration amplitude ≤ 0.16.
- **Remaining routes, all outside formation:**
  - a supplied dictionary;
  - correlated clocks;
  - global conditioning;
  - spontaneous translation breaking in a ground state;
  - corner fermions as emergent quasiparticles of a translation-invariant fine Hamiltonian. This escapes the dimension bound and is open.

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
