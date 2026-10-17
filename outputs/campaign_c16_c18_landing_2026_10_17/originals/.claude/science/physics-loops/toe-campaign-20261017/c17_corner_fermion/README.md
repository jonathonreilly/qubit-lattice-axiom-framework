# C17 exploration: a fermion on the 12 corners of each site (off the C4 axes)

Status: exploration at the emergent-fermion level. The qubit encoding is in progress.

## Setup
- Spinless fermions live on the corners (v; d, d'): pairs of perpendicular directions, 12 per site.
- They hop on the cuboctahedron at each site (on-site, t1) and along plaquette links (t2).
- They sit in a Z2 background flux, uniform per cycle type: squares around the C4 axes, triangles around the octants, plaquettes and edge tubes.

## Findings (`corner_psg.py`, L = 4, all 16 flux patterns)
- Every pattern is consistent and invariant under O and translations.
- **With square flux π:**
  - the PSG class of the site rotations O is w2 + w1^2 (axis C2 -1, edge C2 +1, C4^4 = -1);
  - the U(1) twist i^{w1} (number-conserving hopping) gives w2;
  - the lift to 2O is verified (`shell.py`).
- **Translations.** They commute (TxTy = +1) exactly when square and plaquette fluxes are equal.

## Spectra
- **Shell (site cluster):** E1/2 + E5/2 + 2 G3/2.
- **Real hopping:** the lowest cluster level is E1/2 + E5/2, paired by complex conjugation.
- **Cluster with the O-invariant chiral term** (i lambda around the oriented triangles), from `cluster.log`:
  - triangle flux 0, t1 = -1, lambda = -0.5: single E1/2 ground doublet, gap 2.54;
  - lambda = +0.5: E5/2.
- **Bloch scan with intersite links t2** (`scan.py`): in this simple family the band minimum leaves the symmetric momenta. A mobile doublet at a symmetric momentum appears only at t2 = 0.

So a mobile doublet ground state is not established. The class and the localized doublet are.

## Why corners, not direction qubits
A fermion position fixed by a C4 rotation gets real PSG signs, possibly times i^{w1}. Then M(C4)^4 = +1 on it, so the class is trivial on that C4.

The direction positions (half-edges) lie on C4 axes. The corners lie only on edge-C2 axes.

## Space group (`sg.py`, `space_group_invariants_L4.log`)
- **The 16 patterns are all of them.** The listed cycles span the contractible cycle space: rank 1534 = 1537 − 3 torus holonomies. So the 16 uniform patterns are all the space-group-invariant flux patterns.
- **Invariants (pullback of a spin-1/2 class needs all three = +1):**
  - I1 = Tx Ty Tx^-1 Ty^-1;
  - I2 = C4z Tz C4z^-1 Tz^-1;
  - I3 = C2z Tx C2z^-1 Tx.
- **Result.** Square flux π, needed for C4^4 = −1 about a site, forces I3 = −1 in every pattern. So a bond-centred C2 squares to +1.
  - Square = plaquette = tube = π gives I1 = I2 = +1, but still I3 = −1.
  - Adding vertices or edges cannot change this. I3 is a global sign fixed by the fluxes of existing cycles.
- **Conclusion.** No flux pattern on the corner graph gives the pullback (ordinary spin-1/2) space-group fractionalization.

## Large-fermion view (`lowk.py`, `low_energy_valleys.log`)
For square = plaquette = tube = π, triangle 0, t1 = -1, chiral -0.5 and t2 = ±0.1, ±0.3:
- Superseded (C18). For tube flux π the minimum is a single 2-fold level at one affine-fixed momentum. The earlier reading of 8 valleys came from not accounting for the momentum shifts.
- So a fermion much larger than the grid would carry an 8-valued valley label times a doublet. The lattice-scale space-group data then appear as which momenta the valleys sit at, as with staggered-fermion tastes.

Next: band-engineer a single doublet minimum at Γ or R. Then derive its k·p theory: in O without inversion, the E1/2 doublet allows a k·σ term.
