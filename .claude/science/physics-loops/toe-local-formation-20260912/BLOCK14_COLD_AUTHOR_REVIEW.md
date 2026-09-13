# Cold source review of the native spectral proof

2026-09-13 around07:55UTC. Same author; independent review remains pending.
The entire final derivation and finite comparator were read. The new result
is for the explicitly defined odd star vector in the supplied Gaussian bath.
Its interpretation as a coefficient of a larger native electric Hamiltonian
still has the separate dictionary/perturbation-source obligations.

The domain step is load bearing and has been made explicit. B_A and g are
norm smooth under conjugation by total Fock number N. Positive-gap resolvents
inherit this property, preserve every finite number domain and therefore
make chi smooth. The annihilation-map identity is an equality in the direct
integral of Fock spaces; its positive operator D_A+z+omega is invertible
uniformly by the same delta. Integrated graph norms are controlled by number
moments because the one-particle frequency is bounded. This avoids treating
a generalized plane-wave annihilator as a bounded operator or presuming the
regularity that the spectral estimate is meant to prove.

The word recursion uses assigned product bounds, not an assumed lower bound
on an actual operator-word norm. Each inverse insertion adds one inverse
and one linear field; a field contraction removes a field. All shifts are
nonnegative. The bounds 5h on L and8h on its next contraction justify the
common multiplier43+23j, including complex coefficients and repeated labels.
The final vector estimate includes all remaining Fock sectors. The factorial
moment divides the ordered triple integral by6 and dominates the full
low-energy projector in sectorsN>=3; particle independence is unnecessary.

The Fourier normalization has four positive bands per8-site cell. Local
Majorana amplitude sqrt2 and diagonal P_+=1/2 give unit spectral amplitude
for gamma_0 Omega. This fixes the one-particle coefficient without a factor
of two ambiguity. The paired half-Ward identity is separately checked on
the finite comparator. Reflection gauges act on a bounded coefficient
functional defined for all cell labels; no band projector is assigned at
zero. Its only invariant component is the origin, exactly the certified
real scalar alpha.

For the Lipschitz bound, only negative-neighbor cell phases change, and
selected negative neighbors have distinct cell components (one in the
opposite case). Thus their Cauchy–Schwarz bound is sqrt2h|k|. The source
terms contain one and two shifted inverses, giving three shifts in total.
The lower spectral bound integrates an inner ball |k|<=E/h; it does not
pretend that this is the entire omega<=E sublevel set. The upper DOS uses
the separate enclosing ball pi E/(2h). Every dimensionful coefficient
scales consistently with chi proportional to h^-2.

The sharpness example is a comparison source with its one-particle part
Wick-subtracted. A small cone supplies a continuous local band frame and
a nonzero exterior product; three fixed radial shells give E^9 measure.
It does not assert a nonzero cubic coefficient for the symmetric native
star itself. The literal fixed-gauge positive-z projector is(I-Γ_z)/2;
the earlier sign-flexible wording was clarified to that convention. Both
signs have the same3-column Gram, so no bound or earlier check failed.
The literal cell derivative now explicitly checks the sign as well.

The complete measure bound, not a simulated tail, gives the Laplace and
inverse-power domain statements. Physical bath selection, actual electric
coefficient interpretation, fixed-coupling interacting phase and physical
clock stay outside this theorem. No axiom-forcing conclusion follows.

The first30 then32 checks passed. The final33-check rerun includes the fixed
native projector sign; source-bound output records its actual status. No
failed mathematical predicate was suppressed. Same-author checks remain
separate from a future independent source review and formal audit.
