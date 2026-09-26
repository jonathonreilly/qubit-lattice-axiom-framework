# Proposed finite-spin flat-sector limit: open proof obligations

Primary-author proposal during the fourth campaign, 2026-09-23. This is not
a checked theorem. The exact leading-spin probe has rejected invariance of
the rotor flat sector under D2, while confirming its compact projector. The
following is a possible averaging route that retains this coupling rather
than silently deleting it.

Set Cspin=S(S+1), eta=K Cspin=delta/epsilon^2. On a finite-field-moment core,

    eta H2_S = eta H2_rotor + K D2 + O(Cspin^-1 E^4).

The rotor flat projection P0 on the eight-site ring has rank twelve per
angle and can be represented by two compact configurations per word:
(|01,r,f>-|23,r-1,f+c0(r)>)/sqrt(2), and
(|12,r,f>-|03,r,f>)/sqrt(2). The projector is smooth and finite-range in
circulation, even though dispersive energies cross its energy -4.
Direct rational controls show Q D2 P0 != 0. This rejects exact D2 invariance,
not a dynamically averaged limit. On the tested basis vectors P0 D2 P0
appears diagonal, with quadratic coefficients 4 f^2 plus word-dependent
linear/constant terms. Numerical H4 flat eigenvalues at theta=.37 are
consistent with 12+4 cos((4 theta+2pi k)/12), k=0..11. Both structural
statements need general exact derivations before reuse.

Proposed limit for initial states in the flat sector, after removing its
common fast phase, is the no-event generator

    F_flat=P0(K D2+delta H4-i Gamma/2)P0,
    Gamma P0=4 kappa P0.

This would retain a generated electric operator and H4 after formation,
with second survival exp(-4 kappa t) for a prepared flat-sector state.
Actual first outputs have only half their rotor norm in that sector. A
projection/preparation is not supplied by the formation instrument; do not
claim the whole actual output follows this proposed dynamics.

Possible proof without a uniform gap:
1. Prove the compressed electric operator is selfadjoint on a suitable
   Fourier/Sobolev core and its evolution preserves sufficiently high moments
   on compact times. H4 is bounded finite-range in the compact flat basis.
2. For phi(t)=exp(-it F_flat)phi0, the residual is
   R(t)=Q F P0 phi(t), where F=K D2+delta H4-i Gamma/2. It is smooth in
   theta for smooth phi0 and has no flat component.
3. Let A=H2_rotor+4. Choose a smooth spectral cutoff excluding |A|<h,
   and a corrector chi_eta=-(1/eta) A^-1 chi_(|A|>=h) R(t).
   Smooth explicit ring eigenvectors should imply theta derivatives of this
   inverse/cutoff of order k are O(h^(-k-1)). Dispersive zero crossings
   are simple, so ||1_(0<|A|<h) R|| is O(sqrt(h)) for bounded smooth R.
4. Duhamel against the exact contraction should bound the approximate
   evolution residual by O(sqrt(h)+eta^-1 h^-3) for a second-order F.
   Choosing h=eta^(-2/7) suggests an O(eta^-1/7) core estimate. This exponent
   is only a proposed bound; check source derivatives, domains, endpoints,
   time regularity and every constant before stating it.
5. The finite-spin remainder on a smooth corrector may add
   O(eta^-2 h^-5), smaller at that choice of h. Spin translations extended
   by zero outside their physical interval permit weighted global Taylor
   bounds; show those bounds explicitly instead of invoking strong convergence
   after multiplication by eta. Check initial finite-spin embeddings, Gauss
   subspaces and the contraction/Duhamel domains.
6. Extend from a dense smooth flat core by contraction. If needed, prove an
   adjoint version to control cross terms with initial dispersive components;
   do not infer full survival or full-field convergence for those components.

This is a specific open positive route. No general obstruction or no-go has
been established by the nonzero D2 coupling. It must be independently checked
if the proof closes before any substantial downstream physics claim.
