# F4 route agent: pre-registration (written 2026-10-14 13:38Z, before any run)

## T-F4-1: where does the mirror's index go when a free, local far-wall term "gaps" it?

Object: the tuned Wilson 4+1D slab (4 components per layer-site, mu = 3, one flavour, L layers;
the same slab family as SPIN10 section 3), plus one of:
 (a) an on-site Hermitian far-layer term lambda*V, V in {Gamma5, Gamma4, random Hermitian}, lambda in {0.3, 3, 30, 3000};
 (b) a dispersive auxiliary partner layer chi (2 components, h_chi = + sum_i sigma_i sin k_i) coupled with
     strength g to the mirror spinor of layer L;
 (c) a flat (on-site, dispersionless) partner chi coupled the same way.
Diagnostic: Chern number of the occupied (E < 0) bundle of the full one-body Hamiltonian on small spheres
(radius rho) around the 8 Brillouin corners; layer centroid of the zero-energy states at k = 0; for (c) a scan
for zero-energy Fermi surfaces and the Chern number on a sphere enclosing them.

Readings fixed now:
 - LEMMA-CONSISTENT: in every configuration the total index of the omega = 0 gapless set is 0; whenever the
   k = 0 sphere carries net +1 (near Weyl uncompensated there), a -1 appears elsewhere (other corners, or a
   Fermi surface), or the mirror relocates (layer centroid moves inward).
 - LEMMA-FALSE: some configuration with net +1 at k = 0 and no compensating -1 anywhere in the omega = 0
   gapless set.
Honesty note fixed now: for a finite free slab this outcome is forced by Nielsen-Ninomiya, so the test checks
the instrument and shows WHERE the index goes (relocation / partner doublers / Fermi surface); it is not
evidence about interacting symmetric mass generation.

## T-F4-2 (arithmetic): the infrared price of decoupling without gapping
Reading fixed now: compute L_min = (largest length on which a massless gauge field is observed, in Planck
lengths)^z for z = 1 (light-cone-limited local recursion) and z = 2 (diffusive gradient flow), using the PDG
photon-mass bound m_gamma < 1e-18 eV as the length scale 1/m_gamma. PRICE-PROHIBITIVE if L_min > 1e30
layers per site; otherwise PRICE-FINITE.

## T-F4-3 (added 13:50Z, before running): the folded slab (twisted I-bundle) has ONE Weyl and no mirror?

Object: the tuned Wilson 4+1D slab (mu = 3, one flavour) on T^3 (N x N x N, periodic) x {-L..-1, 1..L}, quotiented by
Phi: (x, y, z, t) -> (x + N/2, -y, z, -t) with spinor S = Gamma2 Gamma4 (S^2 = -1, sector lambda = i). Phi is a free,
orientation-preserving isometry of the 4D bulk; it reverses the orientation of the boundary torus, so the quotient W is
orientable with ONE connected boundary (the t = L face). Bloch momenta kx, kz; y and t in real space.
Diagnostics: (i) number of (near-)zero modes at kx = kz = 0, quotient vs the unglued slab (same N, L);
(ii) number of states with |E| < delta over all (kx, kz), quotient vs unglued slab vs the count expected for one
lattice-free Weyl cone; (iii) layer centroid of every |E| < delta state; (iv) the nonlocal (y <-> -y) splitting of the
boundary branch versus L and momentum.
Readings fixed now:
 - PASS (free level): quotient has half the low-energy states of the unglued slab (2 vs 4 zero modes at k = 0;
   |E| < delta count within 10% of one Weyl's), all of them on the boundary face (centroid > L - 1), none at the midplane.
 - FAIL: extra gapless states (midplane-localized, or at other momenta) restoring a vector-like count.
Scope fixed now: free fermions, no gauge field. A PASS says the geometry removes the mirror at the free level; it
says nothing yet about the gauge field, which is where Lemma D bites (see report).

## T-F4-4 (added 13:57Z, before running): size of the induced nonlocal term of the folded slab vs depth L
Object: T-F4-3's quotient, half filling (all E<0 occupied), with a U(1) phase phi on the gluing bonds for rows
y in [0, N/2) only (a step in the slaved gluing connection = flux through the strips between neighbouring gluing
paths). Measure DeltaE(L) = E(phi = pi/2) - E(0) per gluing bond, N = 16, L = 2..8.
Reading fixed now: DECAYS if |DeltaE| falls by >= 10x per 2 added layers (exponential in L); otherwise SLOW.
This sizes the coefficient c(L) of the flux-dependent nonlocal term; it is a free-fermion estimate only.

## T-F4-4b (added 14:00Z, after seeing T-F4-4; a new dated follow-up, T-F4-4's reading unchanged)
T-F4-4 put the whole holonomy step on the gluing bond (a flux sheet at the midplane), so it measured a bulk
response, not tunnelling. The energetically optimal slaved connection spreads the holonomy phi evenly over the
2L-1 bonds of each fibre segment. Measure DeltaE(L) for the spread version, same rows, N = 16, L = 2..8.
Reading fixed now: INVERSE-L if DeltaE * (2L-1) is constant within 20% for L >= 3 (penalty ~ c phi^2/(2L-1));
EXPONENTIAL if DeltaE falls >= 10x per 2 layers; OTHER otherwise.
