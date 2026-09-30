# A regular change of Poisson structure with the fixed walker sources

Provisional analytic result, root derivation; independent check pending. This
is a bounded internal route test, not a new formal no-go packet or audit status.

## Actual source and target

Main e75578f7136401d4bd750131671aed9212c06291, refreshed2026-09-30T00:28:03Z,
remains the authority. The complete September25 two-step symmetric-books source
was read, including its prescribed-source and nonzero-mode boundaries. It
supplies H=sum sigma_j sin(k_j), P_j=sin(k_j)cos(k_j), E_N={f_N,H}/2 with
f_N=C1C2C3N and total P^B_j=P_j. It does not supply a full canonical matter gauge
action. The sign J=-P^B is the explicit positive-Lie smooth completion choice,
not the literal plus-current branch of its displayed field action.

The prior independent matter check reconstructed these operators in position
space and proved an exact CC repair and a direct-product GC obstruction. Its
REPORT.md SHA256 is8ddaafb14195d4c90f8bae4892310e70fd5770718738711bff99e7e0dbcc99fe.
The cos(2k) multiplier itself is older landed prior art. This calculation tests
the additional regular mixed-Poisson escape; no novelty beyond that extension
is claimed. Main searches for symplectic/noncanonical/Poisson in the actual
admissibility-law corpus found no such completion. PR9363 remains provisional
prior art atfd51a1f4c7f38c124d6f0f7dde396198eadf8b36; none of its restrictions
is a premise. Current axioms/primitives do not select this comparator structure.

## Why mixed entries cannot repair the first matter jet

Give gravity fields U(1) charge0 and psi charge1. At psi=0, equivariance forces
all gravity/psi Poisson entries to vanish; their first possible Taylor terms
are orderpsi. The anomalous {psi,psi} block has charge2 and starts at orderpsi².
The matter Hermitian block is -iZ at orderzero, with next allowed corrections
of orderpsi². Neutral pure-gravity blocks may also have orderpsi² corrections.
No locality assumption is needed for this degree count, only regularity and
equivariance.

At flat gravity and constant shift, the supplied G1 has identically zero
functional differential. For constant or affine lapse, the supplied C1 also
has zero differential. Every higher pure-gravity term has zero first derivative
at h=P=0. Gravity-linear matter terms have gravity derivatives orderpsi² and
matter derivatives proportional to a gravity field. Pairing such a derivative
with E's orderpsi derivative through a mixed bracket costs at least orderpsi⁴.
The pure-gravity bracket of two gravity-linear matter terms is likewise orderpsi⁴.
Thus at matter degree two, both uniform and affine mixed equations depend only
on Z and the unchanged flat E and J. This includes arbitrary regular mixed
symplectic entries; no Darboux map is assumed. All other relevant constraint and mixed-bracket kernels have finite support;
the Z kernel alone may have a finite first absolute moment. Compact plateaux
then remove the seed-boundary terms, and the weighted Z kernel admits the
affine convolution commutator on compact matter fields.

## Complete matrix-symbol necessary equations

Let X multiply the coordinate x_j. Affine averaging leaves x_j unchanged, so
E_1=H and E_(x_j)=(XH+HX)/2. For quadratic matter functionals the flat bracket is

    {psi* A psi,psi* B psi}=-i psi*(A Z B-B Z A)psi.

Write the scalar smearing moments as U(e_j,1)=mu0 and
U(e_j,x_j)=mu0*x_j+mu1, with mu1 nonzero. The uniform equation reads

    i P_j [Z,H] = mu0 H.                                (1)

Multiply by H and take the trace: cyclicity gives zero on the left, and
tr(H²)=2 sum sin²(k_l). On every nonzero-H momentum this forces mu0=0.
Since P_j is nonzero on a dense set, continuity then gives [Z,H]=0 everywhere.
Set F=P_j Z; it too commutes with H. The affine equation becomes

    i[F,(XH+HX)/2] = {partial_j F,H}/2 = mu1 H.          (2)

The identity i[F,X]=partial_j F follows directly from convolution shifts, with
(Sf)_x=f_(x+1). It requires the stated first absolute moment on the kernel.
Choose any fixed transverse momenta with sum_(l!=j) sin²(k_l)>0. Along this full
periodic k_j circle, H is nowhere zero and every commuting Hermitian2x2 matrix
has the unique form F=uI+vH, where u=tr(F)/2 and v=tr(FH)/tr(H²). Both u and v
are C1 periodic. Pauli multiplication gives

    {F',H}/2 = u' H + [v' omega² + v (omega²)'/2] I,
    omega²=sum sin²(k_l).

The linearly independent matrices I,H therefore force u'=mu1. Integrating
around the periodic circle gives0=2pi*mu1, a contradiction. This uses neither
positivity nor invertibility of Z, nor a diagonal/scalar ansatz for it. A finite
kinetic/symplectic kernel is a special case. It is a necessary-identity failure
for the fixed energy/current pair and scalar nonzero affine lapse action.

The argument also works for the literal plus-current branch with the sign of
mu1 reversed. It does not repair that branch's earlier lapse-bracket mismatch.
No complete Jacobi solution, weak constraint algebra, or physical theory is
excluded. The mathematical route changes no axioms or primitives.

## Preserving the actual uniform-clock law is still stricter

If one additionally requires the actual linear walk dot(psi)=-iHpsi to be the
flow of its unchanged total energy psi*Hpsi, the flat Hamilton equation is
-iZHpsi. The same degree argument removes mixed terms at linear order. Thus
ZH=H. Wherever omega² is nonzero, H is invertible and Z=I. Continuity extends
this to all momenta. The isolated zero-energy modes do not supply an independent
continuous convolution freedom. Singular/distributional brackets supported on
those modes fall outside the declared regular class. This uniqueness statement
is about a fixed energy and vector field, not a premise that all matter must
use canonical phase space.

## Live alternatives and exact remaining obligation

This extension does not cover additional charged/carrier species, U(1)-breaking
constant gravity-matter brackets, singular or insufficiently decaying kernels,
changing the flat energy/current definitions, operator-valued lapse structure,
constraint-surface-only identities or controlled infrared sectors. These are
actual changes to the target contract, not impossible theories. In particular
retaining an actual source law requires explicitly rederiving its observables
and action if their generator meaning changes. A local Poisson redefinition
alone, with the unchanged flat generators and regular charge grading, does
not provide that bridge.

Strongest remaining construction: a changed-source or emergent-symmetry common
action whose actual constraints, matter transformations and record-energy
supplier are compatible. Naming that whole construction as a lemma would be
target-equivalent, not progress toward a proof. No separate PR is justified by
this internal extension until it supports a coherent new milestone.
