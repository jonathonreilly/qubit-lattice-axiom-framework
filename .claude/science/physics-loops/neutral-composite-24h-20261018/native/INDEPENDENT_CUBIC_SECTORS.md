# Focused symmetry check: periodic 3x3x3 native compass cube

The proposed sector classification is exact at isotropic couplings. I independently checked the binary Pauli ranks and enumerated the character orbits; no spectrum was used to infer the classification.

## Plane algebra and block dimensions

Same-axis planes commute. Planes from different axes intersect in three sites, so the corresponding distinct Pauli operators anticommute. Products of two planes in one family therefore commute with every plane and with the native Hamiltonian. Taking two neighboring relative products in each of the three families gives six independent commuting Pauli generators.

Independent binary calculation gives plane-vector rank 8, restricted symplectic rank 2, and relative-generator rank 6. The nine plane vectors have one binary relation (the sum of all X, Y and Z planes); its phase does not remove any of the six independent relative characters. The radical of the plane algebra has dimension six, and its noncentral part supplies one protected Pauli factor.

Each of the 64 central-character sectors has dimension 2^(27-6)=2^21. Fixing an additional commuting noncentral plane character, or equivalently the overall Z character once the Z relative characters are specified, halves this to a representative space of dimension 2^20. The remaining plane operator maps the two representative signs isospectrally. This is an exact representation reduction, not a physical removal of qubits.

## Four isotropic symmetry orbits

Within one axis, the three cyclic relative signs multiply to +1. The four possibilities are the all-positive pattern and three patterns with two negative signs. Translation along that axis cyclically permutes the latter three and leaves the other axis families' relative characters unchanged.

At isotropy, proper cubic spatial rotations accompanied by the corresponding spin rotations permute the axis families. Any axis permutation can be realized by a proper signed rotation, with a coordinate inversion if required. A spin sign sigma^a -> s_a sigma^(pi(a)) multiplies an individual nine-site plane by s_a, but a relative product contains two planes and its sign factor is s_a^2=1. Coordinate inversion only permutes plane indices. Thus neither chirality nor the spin rotation introduces an additional relative-character twist.

The only orbit invariant is therefore the number k of nontrivial axis patterns. The four orbit sizes are choose(3,k)*3^k:

k=0: 1; k=1: 9; k=2: 27; k=3: 27.

An independent enumeration using each axis's cyclic action on its two independent sign bits and all axis permutations yields exactly [1,9,27,27]. These are four guaranteed isospectral classes; different classes could still coincide accidentally in some spectral data.

If a symmetry maps a chosen overall-Z representative to its opposite sign, a plane symmetry repairs that choice without altering any central relative character. Thus the representative spectra retain the same equivalence classification.

## Code and scope

The inspected `sector(3)` fixes all three Z-plane signs and positive X/Y relative products, giving the all-trivial central sector with one protected-factor representative. The dimensions and Y-pair phases match that construction. It does not yet parameterize the other three class representatives; those need the intended signed-generator extension.

The four-class reduction applies to isotropic couplings. The anisotropic points in the existing probe do not admit unrestricted axis permutation, so k alone does not classify their sectors. This result establishes no ordering of class ground energies. Even a completed four-representative calculation would concern only the finite periodic 27-site Hamiltonian; it would not identify an infinite-volume phase, a bulk scalar pole or a selected physical state.
