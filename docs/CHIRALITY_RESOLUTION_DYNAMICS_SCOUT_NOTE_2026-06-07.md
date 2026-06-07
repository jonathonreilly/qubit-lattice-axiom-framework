# Chirality Resolution Dynamics Scout Note

**Date:** 2026-06-07
**Claim type:** meta
**Role:** frontier scout / methodology note
**Actual current-surface status:** open
**Trace class:** frontier_discovery
**Primary runner:** [`scripts/frontier_chirality_resolution_dynamics_scout_2026_06_07.py`](../scripts/frontier_chirality_resolution_dynamics_scout_2026_06_07.py)
**Cached runner output:** [`logs/runner-cache/frontier_chirality_resolution_dynamics_scout_2026_06_07.txt`](../logs/runner-cache/frontier_chirality_resolution_dynamics_scout_2026_06_07.txt)

This note starts the chirality-resolution lane suggested by the enzyme analogy:
manufacturing can begin with a blend of hands; a flip/racemization mechanism can
interconvert hands; a filter can remove or pass one hand; a dynamic kinetic
resolution combines flip plus filter to enrich the surviving composition toward
one hand while tracking retained mass.

The framework translation is useful, but conservative:

- A **blend** is just coexistence of two candidate chirality/orientation sectors.
- A **flip** is a symmetric involution or transfer between sectors.
- A **filter** is an asymmetric section, sink, chiral anticommutation, source
  character, boundary condition, or readout rule.
- A **dynamic resolution** is flip plus filter. The filter is still the
  load-bearing selector.

The runner verifies the finite boundary:

- a racemic blend has zero signed excess;
- a symmetric flip relaxes toward the unbiased fixed point;
- a symmetric sink changes retained mass but not handedness;
- an asymmetric sink enriches one hand in the surviving composition;
- flip plus asymmetric sink gives dynamic kinetic resolution, but only because
  the asymmetric sink has already been supplied;
- in the staggered one-bond model, the runner computes the matrix
  anticommutator and verifies that `{D,gamma5}=0` is precisely the filter that
  collapses trivial/vector-like and staggered/chiral sign classes to the
  staggered class up to global sign; the full bipartite uniqueness route is the
  existing
  [staggered chirality selector enumerator](STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md);
- an orientation line hosts both sections until a source-section theorem chooses
  one;
- Record can append realized chirality labels, but does not produce carrier
  chirality;
- a signed C3 readout can commute with the C3 labels, so signed readout is not
  automatically an anticommuting chirality.

## Consequence

The enzyme concept is scientifically useful as a route map, not as an automatic
new principle.  It says where to look:

1. **Staggered chirality:** prove a framework-native reason that the physical
   kinetic operator must satisfy `{D,gamma5}=0`.  Existing finite enumeration
   then forces `epsilon(x)` up to global sign.
2. **Signed gravity:** prove a canonical orientation section or native source
   action.  The determinant/orientation line hosts the sign data, but hosting is
   not choosing.
3. **Record interface:** keep Record downstream of realized carrier chirality.
   It can tally/filter after a supplied instrument, not derive the carrier.
4. **Koide / generation readout:** separate signed spectral classifiers from
   anticommuting chirality or first-order holomorphic readout.  A readout filter
   must be selected by a theorem, not by desired outcome.
5. **Eta / spectral-flow route:** a topological asymmetry theorem could be a
   real filter if it supplies an oriented boundary/index sector without adding a
   new axiom.

## Literature used as analogy, not authority

- Schober and Faber,
  ["Inverting hydrolases and their use in enantioconvergent biotransformations"](https://pmc.ncbi.nlm.nih.gov/articles/PMC3725421/),
  for the kinetic-resolution / enantioconvergent-process distinction.
- Bearne and coauthors,
  ["Racemases and epimerases operating through a 1,1-proton transfer mechanism"](https://pmc.ncbi.nlm.nih.gov/articles/PMC8142540/),
  for reversible stereochemical flip mechanisms.
- Catterall,
  ["Chiral Lattice Fermions From Staggered Fields"](https://arxiv.org/abs/2010.02290),
  as a lattice-fermion proof-template pointer only.
- Fukaya et al.,
  ["The index of lattice Dirac operators and K-theory"](https://arxiv.org/abs/2407.17708),
  as a pointer that eta/spectral-flow index routes are mathematically active.
  No result from that paper is imported as a framework derivation here.

## Honest Status

This note adds no axiom and proposes no retained claim.  Its value is a sharper
frontier target: **blend and flip are not enough; a native chirality lane must
derive the asymmetric filter/section.**  If a later theorem supplies such a
filter from `{Lattice, Quantum, Record}` plus retained admissions, this packet
identifies the downstream places where it would immediately matter.
