# Focused check: perturbative support and third-order boundary mixing

## Exact Hamming-distance lemma

Represent a finite E8 configuration by an unordered pair of distinct columns A and a common interval I of length ell. Its flipped-spin set has size 2ell. For another such configuration (A',I'), if A' differs from A then their column sets share at most one column, so their spin-set intersection has size at most |I intersection I'|. Therefore

|S symmetric-difference S'| >= 2ell+2ell'-2|I intersection I'| >= 2ell.

This remains true when the final interval is shorter, and also gives the analogous lower bound 2ell' by symmetry. Every transverse V factor flips exactly two physical spins. A word containing n such factors cannot have a nonzero matrix element unless the Hamming distance is at most 2n. Hence different-column transitions require n>=ell (and n>=ell').

Canonical folded terms do not evade this count. In a fixed perturbative convention at order n, expanding the nested commutators, generator coefficients and normalization terms gives words with exactly n V insertions. H0 spectral projectors and resolvents are diagonal in the physical Z basis and change amplitudes or select intermediate configurations, but do not flip bits. Products corresponding to folded terms still have the same total perturbative degree and number of V factors. This argument concerns the bare configuration matrix of the canonical effective coefficient; arbitrary additional parameter-dependent basis rotations need not preserve that presentation.

## Third-order consequence for the axial arm

For an axial-distance-two interval of length ell>=4, K3 cannot change its column pair. Its unchanged pair has the same checkerboard color and therefore U=+ for every interval length. Odd-order equivariance then forbids every remaining same-pair K3 matrix element as well. Thus the entire E8 row and column of K3 for these long axial-arm configurations vanish, under the stated canonical symmetry convention.

This strengthens the earlier parity statement: direct K3 transitions from the long arm into either negative frozen states or the fast sector are absent exactly. Third-order cross-sector effects can originate only from the short interval boundary, ell<=3.

Calling this a finite boundary requires one further support observation. The interval-length lemma alone does not bound transverse separation. Starting from the axial arm, however, three transverse bonds can reach only finitely many nearby columns; after quotienting center translations at q=0 the accessible short configurations form a finite set. For the whole ell=2 slow host, the same conclusion for transitions to odd-length sectors also uses layer-by-layer path parity: removing or adding a whole layer leaves two odd flip endpoints on that layer, which must be connected by the union of transverse bonds used there. A path of at most three bonds cannot join arbitrarily separated columns. Thus distant host configurations do not secretly furnish an extensive third-order coupling into these different-length sectors. This geometric argument should accompany the Hamming count when describing the full host.

## Conditional effect on the confined-arm width

A K3 coupling to the negative frozen block, whose K2 coefficient is -4, gives a virtual physical correction of order (Jz lambda^3)^2/(Jz lambda^2)=Jz lambda^4 near coefficient energy -6, assuming a uniformly bounded separated inverse. The support result localizes this correction at the short boundary.

A K2/K3 cross term through the fast block nominally also has physical size Jz lambda^4: its numerator is order lambda^5 and its fast resolvent carries the fast energy unit lambda^-1. This scaling additionally requires control of the relevant finite-source continued fast resolvent; support alone is not that bound. Logarithmic factors or special resonant enhancements must be checked, not silently replaced by constants.

If these corrections induce a bounded O(lambda^2) perturbation of the slow-scaled endpoint self-energy, the regular Airy impedance result gives an energy displacement O(f_s lambda^2) in slow units. Since f_s=lambda^2/8 and the slow physical energy unit is Jz lambda^2, the displacement is O(Jz lambda^6). This includes the width correction when the boundary perturbation is complex. Accordingly a controlled finite-boundary physical lambda^4 self-energy does not generically change the leading physical lambda^4 Airy width; it is suppressed by the small endpoint probability, of order f_s.

The conclusion is conditional on the specified resolvent and boundary regularity bounds. It is not a pole-existence proof and does not eliminate direct K4 bulk terms, higher-order length-dependent potentials, state-selection assumptions or uniform control on growing intervals. Those are distinct from the now-excluded long-arm K3 transitions.
