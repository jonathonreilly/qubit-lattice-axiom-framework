# Homogeneous charged-record motion and field response

This PR extends [PR 8650](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8650)
with an interacting charged-record target. A uniform repulsive occupation
penalty selects either checkerboard of occupied sites. There is no fixed
Gauss-charge background: div E=q, with total charge zero. Virtual record
hopping generates an electric term and plaquette operations that transport
and exchange the actual signed records.

The complete argument is
[HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS.md](HOMOGENEOUS_MOBILE_CHARGED_RECORDS_AND_FIELD_DYNAMICS.md).
On even cubic tori with periods at least six, the supplied penalty is
B=(1/2)sum_edges(n_x+n_y-1)^2 and H=V0 B+tT. Integer spin links carry
E=S_z and U=S_+/sqrt(S(S+1)). Records are bosonic hard-core qutrits.
These Hilbert spaces, Hamiltonian, formation instruments and energy scales
are stipulated model inputs, not derived native primitives.

At fixed K,J>0, C=S(S+1), gamma=(2d-1)/(d-1), choose
epsilon² C=J/(gamma K), Delta=(2d-1)V0=gamma K²C²/J,
t=epsilon Delta and beta=beta0 epsilon^(3d).
The resulting target is K sum E²-J sum(R_p+R_p†). Each R_p exchanges
the records at the two occupied corners and shifts the surrounding field
according to their charges. Oppositely charged and equally charged corners
have different interference; replacing R_p by a pure field loop would
change the model.

A finite local dressing of order 3d+6 and a uniform fourth electric-moment
bound give an O(epsilon) local-observable comparison at fixed time and support,
uniformly in volume. The proof keeps the O(t) resonant motion outside the
prepared sector and the complete formation dissipator. Formation is enabled
at finite parameters, but its coefficient vanishes in the stated limit.

## Independent evidence and remaining obligations

The separate derivation was sealed before author comparison:

- [REPORT.md](homogeneous_charged_independent/REPORT.md):
  88bef2c7814bacb3864eee220e245365b3207c9d8f189298f8e8ddf1e13a3582.
- [COMPARISON.md](homogeneous_charged_independent/COMPARISON.md):
  689a0d3bc19054fc5d7f4c95a7d3cf7796a405ccf0f84ec61458e95a9750ddb5.
- [FINAL_SEAL.json](homogeneous_charged_independent/FINAL_SEAL.json):
  fdcb0aea3a020ad2c71793dcd50e028e694c26a7c1cd12db590a20ffa9d18c05.

The check found no required correction. Complete guarded-square matrices,
nontrivial finite-spin weights, cubic path denominators, birth algebra and
the changed local-limit assumptions were independently reconstructed.
Two author boundary sectors were additionally rebuilt exactly after the
blind seal. Different earlier finite bases were reconciled through their
different exterior electric fields. The root read all arguments and
scientific checkers/results and authenticated all 58 final source identities.

The preserved initial author indexing error and its one-line repair are
included. The independent physical resonant-hop counterexample explains why
the older slower propagation estimate cannot be reused. Test counts are
not a proof of uniform locality; the explicit argument supplies that result.

## The charged target's prepared field response

[CHARGED_RECORD_EXCHANGE_BAND_FIELD_RESPONSE.md](CHARGED_RECORD_EXCHANGE_BAND_FIELD_RESPONSE.md)
analyzes the actual charge-exchanging target in the neutral Dicke matter band.
It derives the relaxed band Hessian, including the matter response rather
than holding the matter vector fixed. An exact local-star argument bounds
the curvature above and below on every physical field-angle direction,
including the harmonic directions, uniformly over the stated even boxes.

With K=omega0 h and J=omega0/h, compact Gauss-equivariant prepared packets
have a controlled fixed-box O(sqrt(h)) oscillator approximation. Their
frequencies have a positive lower bound. This specific band therefore does
not inherit the earlier soft transverse photon packet. This is not a gap
theorem for the complete many-body Hamiltonian or a thermodynamic phase
classification. Packet error constants remain box-dependent.

An exact even-torus pi-flux unitary also reverses the overall ring sign.
Simply flipping that sign therefore does not resolve this particular
band-response issue. Other bands, preparations and coupling regimes remain
open; no microscopic fermion-statistics theorem is claimed.

The separate [blind report](charged_band_independent/REPORT.md) was frozen
before the [author comparison](charged_band_independent/COMPARISON.md).
The comparison found no required correction and independently reconstructed
the additional all-direction bound and sign equivalence. It rebuilt one
auxiliary packet evolution with agreement to 7.4e-13, checked a complete
61-dimensional physical tangent space, and retained all failed/interrupted
attempts. The root read all three independent scientific checkers and their
full results, and authenticated the 68 final bindings. The final seal is
7cbff4724371985ca2750c21421fc52597f55a975325e6a2a43698c5d2f70150.

This publication does not establish a thermodynamic phase, retain a positive
limiting birth rate, select the prepared state autonomously, or account for
a finite fuel supply. Separate finite-rate formation work is outside this
publication. No formal audit verdict or retained status is applied.

## Portable evidence verification

Run python3 verify_homogeneous_charged_publication.py from this directory.
It checks the 113 unchanged new source/evidence artifacts and the selected
seal bindings using repository-relative paths. It confers no scientific
verdict and does not rerun the science.

PUBLICATION_UNIT_HOMOGENEOUS_CHARGED.json records the source private commit,
the stacked base, inherited dependencies and the explicit fulltext exclusion.
Original seals retain their historical absolute paths; raw sealing scripts
are provenance tools for that original workspace. The scientific runners
require Python with NumPy/SciPy/SymPy where imported; some write result
files, so use a disposable copy for reruns.

The inherited primary-literature HTML is excluded. Its bound metadata/read
receipt remains in the base publication. The new wrapper and verifier have
not had a separate independent publication review.
