# A real transport network with threshold-formed records

Date: 2026-10-16. Author: /root personally in this chat.
Status: conditional candidate and falsifiable mathematical consequences.
This is not a derivation of quantum mechanics, an empirical fit, or a new
framework axiom. Standard wave interference and feedback quantization are
reconstructed here; no novelty is claimed for those elementary constructions.

## Purpose and separately stated premises

The first cache model lacked a current influence from one arm. This candidate
allows current real-valued relational variables to propagate along both local
paths. It asks how discrete records might form from those variables, without
beginning with a stochastic Born draw. Mathematical linear superposition of the
transport variables remains; this is a candidate underlying mechanism for the
formalism, not evidence that the formalism or observed interference is wrong.

Supplied candidate premises are:

1. Each path carries a real two-component variable. Local transformations are
   plane rotations, with the usual additive composition of angles.
2. A balanced junction mixes its two path inputs by the orthogonal matrix
   H=[[1,1],[1,-1]]/sqrt(2), acting separately on each real component.
   Recombination is the same H. This linear lossless junction is a chosen model,
   not a theorem of Record or nearest-neighbor dependence.
3. The relevant positive flux is radial in each two-component variable, vanishes
   at zero carrier, is additive over separate output channels, and is conserved
   under every linear splitter angle. Zero flux of a carrier is not a readable
   value assigned to a site with no record.
4. Each prepared trial supplies one unit of this flux in total, and local
   counters convert one unit of accumulated flux to one record. The unit,
   physical energy identification, source preparation and event cadence remain
   supplied. A common trial boundary is not derived.
5. To obtain exactly one record per trial, the two initial counter residues are
   complementary. The tie convention is explicit below. This correlation is
   an initial condition, not a derived law or consequence of locality.

These premises are deliberately exposed. The calculation may remove an
independent choice of the radial flux function within this class; it does not
remove the transport, preparation or detector assumptions.

## A. Lossless splitting fixes a radial flux function conditionally

Let q:[0,infinity)->[0,infinity) be a finite radial flux, q(0)=0. Suppose

    q(r)=q(r cos theta)+q(r sin theta)

for every r>=0 and theta in [0,pi/2]. Define f(s)=q(sqrt(s)). Taking
r=sqrt(s+t) and the corresponding splitter angle gives

    f(s+t)=f(s)+f(t),  s,t>=0.

Nonnegativity makes f monotone. Integer/rational additivity and monotone
squeezing by rational sequences then imply f(s)=c s, with c=f(1)>=0. Thus
q(r)=c r^2. For a nontrivial flux, c>0, and calibration can use c as its unit.
No differentiability or noise prior is needed. The universal linear-splitting
and positive additive-conservation premises do the work. The displayed single-input splitting identity only at
one splitter angle would not be enough to infer this full conclusion.

## B. Current relations produce the continuous interference pattern

Let u be any unit vector in R^2. The initial two-path vector is (u,0). After
the first H, the local rotations R(phi0),R(phi1), and the final H,

    v0 = (R(phi0)u + R(phi1)u)/2,
    v1 = (R(phi0)u - R(phi1)u)/2.

The derived radial-flux fractions are

    p=||v0||^2=(1+cos(phi0-phi1))/2,
    1-p=||v1||^2=(1-cos(phi0-phi1))/2.

These are flux fractions, not yet event probabilities. A common rotation of
both inputs changes no fraction. At phi0,phi1 in {0,pi}, one output carries
all the flux and the other zero, so current-setting parity is encoded without
a learned setting cache. Both current influences reach the junction.

The initial u, rotations and junction are explicit mathematical inputs. No
single-photon energy, particle ontology, multi-particle statistics, Bell
correlation, physical Hamiltonian or scalar action follows from this identity.

## C. Two local counters and exact record-frequency balance

At the beginning of a trial let r0 in [0,1), r1=1-r0 in (0,1]. The current
flux increments are p in [0,1] at counter 0 and 1-p at counter 1. Define

    Z0=1 if r0+p>=1, otherwise 0;
    Z1=1 if r1+1-p>1, otherwise 0;
    r0'=r0+p-Z0,   r1'=r1+1-p-Z1.

The strict/weak tie convention is a supplied detector convention; its asymmetry
does not follow from an unprivileged-site axiom. For t=r0+p, the other
pre-emission residue is 2-t. Hence Z1=1-Z0, and r1'=1-r0'. The domains of
both residues are preserved. Each counter uses only its own incident flux and
residue; their complementary initialization and synchronized unit-total input
are essential shared preparation conditions.

For any sequence of flux fractions p_t, telescoping gives

    N0(n) = sum_(t=1)^n p_t + r0(0)-r0(n),
    |N0(n)-sum p_t| < 1.

For constant p the long-run relative count tends to p for every initial r0,
without a probability measure on initial residue and without a stochastic
outcome draw. In fact N0(n)=floor(r0(0)+n p). This is a count-balance result
from a chosen threshold mechanism, not the full Born process law.

If the initial residues are not complementary, exactly one record for every
possible p is lost. The two output conditions become p>=1-r0 and p<r1;
they partition [0,1] for all p precisely when r1=1-r0, with the stated endpoint
conventions. With independent uniform residues and a fixed p, double-record
and no-record probabilities are both p(1-p). The uniform ensemble is an
explicit comparison fixture, not an adopted initial-state measure.

For arbitrary nonnegative incident flux increments e0_t,e1_t and ordinary
integer-threshold counters, total cumulative count differs from the total
incident flux by a bounded residual. Thus a persistent one-record-per-trial
claim also needs unit mean input flux; a different constant total flux cannot
be hidden indefinitely in bounded counter residues.

## D. A decisive consequence beyond the average fringe

At p=1/2, the complementary-counter rule alternates output ports exactly,
including the stated tie cases. Every even n has N0(n)=n/2 for every initial
residue. Its balanced-bin count variance is zero under any initial-residue
ensemble. Repeated independent Bernoulli half-probability outcomes instead
have variance n/4. The same mean fringe therefore conceals a different record
process. The Bernoulli process here is a comparison model for suitably
independently prepared trials, not an assertion about all physical detectors.

An explicit independent-loss fixture quantifies, rather than ignores, missed
records. Let genuine alternating outputs be retained independently with
probabilities eta0,eta1 in (0,1] at their two respective ports. Put
D=eta0+eta1-eta0 eta1. The next retained-port transition matrix is

    [[eta0(1-eta1)/D, eta1/D],
     [eta0/D, eta1(1-eta0)/D]].

Each entry follows by summing the geometric series over missed alternating
pairs. Its stationary port-0 fraction is eta0/(eta0+eta1), and its nontrivial
eigenvalue (also the stationary normalized lag-one binary correlation) is

    -eta0 eta1 / D.

For equal efficiency eta this is -eta/(2-eta). The correlation can become
small at poor efficiency; an uncalibrated lossy record stream cannot be treated
as the ideal full stream.

For fixed even n heralded input trials and independent loss eta0 at output 0,
the threshold model gives observed-count mean eta0*n/2 and variance
eta0(1-eta0)*n/2. The independent Bernoulli comparison gives the same mean
but variance n*(eta0/2)*(1-eta0/2). Their variance difference is n*eta0^2/4.
The heralded trial count, independent-loss model, stationarity and efficiency
need empirical calibration before applying this comparison.

This rejects the candidate as a universal replacement for independent quantum
record statistics at the mathematical benchmark level. It is not an empirical
rejection based on data opened in this campaign. Adding a fresh uniform random
residue each trial would yield Bernoulli probabilities p, but would introduce
an independent noise/initialization law and renewed complementarity. That
supplier cannot be called a derived physical mechanism.

## E. Record identity and next question

Operational counter residues change; permanent output records can instead be
appended at fresh sites. Implementing that computation by a covariant local
M2(C) rule, deriving resource renewal and the physical formation schedule are
open. No claim is made that the permanent content of an old record is changed.

The constructive result is limited but useful: under one explicit lossless
real-transport model, a conserved radial readout becomes quadratic, and a local
threshold mechanism turns it into the right long-run frequency without a Born
draw. Higher record correlations expose what remains wrong or supplied.

Next: determine whether local neighborhood geometry can fix transport rotations
instead of supplying each phase separately, and whether a physically justified
record mechanism can satisfy both intervention and fluctuation constraints.
The unchosen noise rule, correlated initialization and linear transport remain
live assumptions. All calculations here are development mathematics.
