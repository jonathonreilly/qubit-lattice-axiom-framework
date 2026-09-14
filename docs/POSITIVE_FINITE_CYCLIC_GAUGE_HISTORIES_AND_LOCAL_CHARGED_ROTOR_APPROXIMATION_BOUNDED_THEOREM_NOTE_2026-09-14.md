# Positive finite cyclic gauge histories and local charged-rotor approximation

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author proposal; independent scientific review is pending. No audit verdict,
axiom, primitive or established TOE status is changed.

A supplied finite cyclic gauge Hamiltonian with opposite-charge conjugate CAR
matter has a nonnegative, exactly Gauss-projected finite-slice history sum.
An explicit norm estimate compares this same cyclic regulator with the charged
compact rotor for initially bounded electric flux. Locality makes the required
payload independent of the surrounding spatial volume for a fixed observable,
observation time and tolerance. The interacting ground-state and infrared
phase problem remains open.

The construction includes a free four-node comparison with matching bare
metrics and cancelling Hall responses. It also exposes two precise limits:
positive paired weights need not be of positive Fourier type, and the
mathematical antiunitary does not forbid a gauge-neutral gapping pair term.
These are counterexamples to automatic inference rules, not an exclusion of
a Coulomb phase or an axiom-forcing wall.

**Runner:** [self-contained primary runner](../scripts/positive_finite_cyclic_gauge_histories_and_local_charged_rotor_approximation_2026_09_14.py).
**Receipt:** [canonical execution cache](../logs/runner-cache/positive_finite_cyclic_gauge_histories_and_local_charged_rotor_approximation_2026_09_14.txt).
**Recovery and review:** [campaign handoff](../.claude/science/physics-loops/toe-charged-phase-20260914/HANDOFF.md).

## Premises, imports and proof obligations

| Input or machinery | Provenance and role | Open framework bridge |
|---|---|---|
| Finite oriented graph, CAR cells, cyclic links, chosen couplings and modular invariant sector | Supplied model data, explicitly defined below | Selection, physical implementation and identification are not derived |
| Fock determinant identity and conjugate species | Elementary finite exterior algebra, proved by second quantization below; Wu-Zhang is prior art | No physical time reversal is inferred |
| Weighted electric estimate, Duhamel comparison and local commutator iteration | Direct bounds below, checked against the named truncation and locality literature | No ground-state or long-time limit is supplied |
| Four-node Wilson symbol, number symmetry and filling | Supplied free comparison with explicit parameter domain | Interacting stability and observed matter identification remain open |
| Framework axioms and approved primitives | Current [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md); context only | None selects this Hamiltonian or proves its phase |

The proof chain is finite model -> projected trace, and independently finite
model -> weighted electric bound -> cyclic comparison -> local approximation.
The Fourier and pairing counterexamples constrain the proposed phase argument;
they are not premises of the two positive implications. No unmerged campaign
PR is a load-bearing dependency. Every general theorem statement below has an
analytic proof; the finite runner challenges its conventions and constants.

## Exact finite model

Fix a finite oriented graph without self-links, incidence D with +1 at the
tail and -1 at the head, and plaquette boundaries B with DB=0. Fix an integer
N>=3 and omega=exp(2 pi i/N). Each link has basis |q>, q in Z_N, and

```text
Z|q>=omega^q|q>,       X|q>=|q+1>.
```

Then XZX^dag=omega^(-1) Z. Each vertex has m plus and m minus CAR orbitals.
Let Q_x=N_{+,x}-N_{-,x}, and define commuting local gauge transformations

```text
Gamma_x = product_l X_l^(D_xl) exp(2 pi i Q_x/N),
P = N^(-|V|) sum_{s in Z_N^V} product_x Gamma_x^(s_x).
```

Gamma_x^N=I, so P is the orthogonal projection onto the invariant space.
It is nonzero: zero-occupation matter and all links in the X=1 state are
invariant. The constraint is div E=Q modulo N if X has eigenvalue omega^(-E).
It is not an exact integer Gauss constraint.

Let h_+(Z) be a finite-range Hermitian one-particle matrix built from onsite
Hermitian matrices v_x and nearest-neighbor directed hopping T_l Z_l, with
its Hermitian reverse. Precisely, h_(tail(l),head(l))=T_l Z_l; multiple
contributions are added if present. At fixed phases q it becomes h(q). Define

```text
H_m = c_+^dag h(Z)c_+ + c_-^dag h(Z)^* c_-.
```

Here star conjugates numerical coefficients AND sends each Z to Z^dag;
there is no transpose of the ordering of products. The minus onsite matrix
is v_x^*, and its directed hopping is T_l^* Z_l^dag. Each hopping and onsite
term is gauge invariant with the above Gamma. Opposite charges are necessary
for this displayed local realization of the fixed-history conjugation.

Take t_l>=0 and K_p>=0 and

```text
H_E = sum_l t_l(2-X_l-X_l^dag),
H_B = sum_p K_p(1-Re product_l Z_l^(B_lp)),
H = H_E+H_B+H_m.
```

All are Hermitian finite matrices, gauge invariant, bounded and local. The
full finite time evolution and the physical Gibbs operator are well-defined.
An even-CAR tensor-qubit realization, native formation law, chosen vacuum and
physical identification remain separately supplied obligations.

## Positive electric kernel

In the q basis, for tau>=0,

```text
exp[-tau t(2-X-X^dag)]
  =exp(-2 tau t) sum_{a,b>=0} (tau t)^(a+b)/(a! b!) X^(a-b).
```

All matrix entries are nonnegative. For tau t>0 they are strictly positive
because every residue is attained by a walk. The entries sum to one. The
Fourier eigenvalue is exp[-tau t(2-2 cos(2 pi n/N))]. This is a cyclic random
walk heat kernel, not the hard-truncated quadratic-electric heat kernel.
The finite link has ceil(log2 N) encoding qubits, with unused words excluded.

## Exact projected finite-slice trace

Take beta>=0 and an integer M>=1, with delta=beta/M.
Set K_delta=exp(-delta H_E), M_delta(q)=exp(-delta V_B(q)), and
A_delta(q)=exp(-delta h(q)). A convenient nonsymmetric slice is

```text
T_delta=exp(-delta H_E) exp(-delta H_B) exp(-delta H_m).
```

Each factor commutes with P. T_delta need not be Hermitian; its projected
trace still has the positive expansion below. The finite-dimensional Lie
product formula gives Tr(P T_(beta/M)^M) -> Tr(P exp(-beta H)). A symmetric
slice can be obtained by conjugation by exp(-delta H_E/2), with the same trace
of powers since H_B and H_m commute in the q representation.

For histories q_0,...,q_(M-1) and s in Z_N^V, let d_s=D^T s modulo N and
R_s=diag_x exp(2 pi i s_x/N) tensor I_m. The precise boundary kernel orientation
is fixed by <q|X^(d_s)=<q-d_s|. With q_M=q_0-d_s, one expansion is

```text
Z_M = N^(-|V|) sum_s sum_(q_0,...,q_(M-1))
   [product_(j=0)^(M-1) K_delta(q_(j+1),q_j) M_delta(q_j)]
   |det(I+R_s A_delta(q_(M-1)) ... A_delta(q_0))|^2.       (1)
```

The displayed boundary sign and ordering agree with independently constructed
full Fock projected traces, including the two-orbital Wilson hopping matrices. The
fermionic identity follows because second quantization obeys
Gamma(A)Gamma(B)=Gamma(AB) and Tr_Fock Gamma(C)=det(I+C), including temporal
gauge factors. The minus block has the SAME ordered product conjugated,
R_s^* A(q_(M-1))^* ... A(q_0)^*. This is not the adjoint of the plus product;
adjoint would reverse the order and is not the needed operation.

Every summand in (1) is nonnegative. The finite-slice representation is exact
for this Trotter product; M->infinity gives the physical finite-volume Gibbs
trace. Positivity does not by itself give a Coulomb or Weyl phase, a gap,
correlation decay, an efficient sampler, or an infrared-uniform expansion.

## Free four-node comparator and its actual supplier

Take m=2 and a simple two-node Wilson symbol

```text
h0(k)=sin kx sigma1+sin ky sigma2
     +(2+zeta-cos kx-cos ky-cos kz)sigma3,
0<zeta<1,  0<b<pi.
```

Let h_+(k)=h0(k-b xhat) and h_-(k)=h_+(-k)^*. At Z=1, a zero requires
both sine terms to vanish. The cases with either
shifted kx or ky equal to pi require cos kz>1 when 0<zeta<1 and are
excluded. Thus the plus nodes are
(b,0,+/-acos zeta) and the minus nodes (-b,0,+/-acos zeta). For b not 0 or pi
these are four distinct nodes. The local metric is diag(1,1,1-zeta^2) for all
four. Each species separately has opposite node chiralities, so its cubic
and mixed U(1) anomaly sums vanish. Their occupied-band Berry curvatures are
opposite after k->-k, hence charge-squared Hall responses cancel at equal
filling. This comparison uses the free symbol, not the interacting spectrum.

This supplied model conserves N_+ and N_- separately. The gauge symmetry
alone also allows a neutral pairing term c_+^dag Delta c_-^dag+h.c. Under
a compatible local identity pairing, the zero-field Nambu block is

```text
[[h_+(k), Delta I],[Delta I,-h_+(k)]],
```

whose square is h_+(k)^2+Delta^2 I. Thus a nonzero real Delta opens a gap in
this enlarged Hamiltonian family. This pairing also preserves the mathematical
antiunitary of the normal
paired model. In the local real occupation basis let J=[[0,I],[-I,0]]
on species and Theta=Gamma(J) K. Then Theta^2=(-1)^(N_++N_-),
Theta c_+^dag Theta^(-1)=-c_-^dag and
Theta c_-^dag Theta^(-1)=c_+^dag. Fermion reordering therefore leaves
sum_alpha c_(+,alpha)^dag c_(−,alpha)^dag invariant for real Delta.
It also leaves the gauge transformations invariant. At fixed gauge history,
the one-particle antiunitary squares to -I. Neither this observation nor
its Fock counterpart proves positivity for the enlarged pairing Hamiltonian:
the number-conserving determinant identity used in (1) would need replacement.
Other supplied physical symmetries must be checked separately. Exact total
matter-number conservation excludes this explicit
bilinear but does not exclude spontaneous pairing of its interacting ground
state. Weak-coupling stability must address that channel.

## Relation to known phase arguments

The pure finite Z_N Euclidean phase construction in Frohlich-Spencer is not
already a theorem about (1). Its action, source observables, time anisotropy
and matter hypotheses must be matched. The full source gives separate
Wilson/disorder loop bounds, and explicitly cautions that perimeter behavior
alone with dynamical light charges is not a deconfinement criterion. Even a
positive determinant can destroy a correlation inequality or obstruct a
local polymer estimate. These are the next mathematical questions.


## Finite-time rotor approximation by the positive cyclic model

This establishes which rotor is approximated; it does not replace its
magnetic cosine by a harmonic theory or supply an infrared phase theorem.
Take a>0, g>0, w_l>=0, odd N=2S+1, representatives n=-S,...,S, and set

```text
t_l = g^2 w_l N^2/(8 pi^2 a).
```

The cyclic electric eigenvalue is

```text
lambda_N,l(n) = (g^2 w_l/(2a)) n^2 sinc^2(pi n/N).
```

For every real x, 0<=1-sinc^2 x<=x^2/3. One direct proof uses
sinc^2 x=2 integral_0^1 (1-u)cos(2xu) du and 1-cos y<=y^2/2.
Consequently, for every representative n,

```text
0 <= g^2 w_l n^2/(2a)-lambda_N,l(n)
   <= pi^2 g^2 w_l n^4/(6a N^2).                         (2)
```

The rotor comparator has identical CAR, hopping and plaquette coefficients,
untruncated integer E, unitary U|n>=|n+1>, and quadratic electric energy.
Assume normalized initial psi with every |E_l|<=M0<=S. It may be entangled
and can satisfy exact integer Gauss. Embed the cyclic Hilbert space by its
representative electric basis into the full rotor space. The embedding is
not invariant under rotor evolution and maps modulo-Gauss alias states to
nonphysical integer-Gauss sectors; their amplitudes are counted as error.

Write J_l=sum_(alpha:l in alpha)||V_alpha||, where H_interaction is the sum
of V_alpha+V_alpha^dag, each V shifts the participating E_l by +/-1, and a
link occurs at most once per monomial. For any lambda>0 and T=|t|, put

```text
C_l(T,lambda)=exp(lambda M0+2 J_l T sinh lambda),
A_4(lambda)=(4/(e lambda))^4.
```

For a Hamiltonian with any real diagonal electric energies, including the
hard finite restrictions used below, the exponential-weight estimate is

```text
||exp(lambda |E_l|) exp(-itH)psi|| <= C_l(T,lambda).       (3)
```

Indeed conjugate the generator by W=exp(lambda|E_l|). Its anti-Hermitian
part has norm at most 2J_l sinh lambda, because each allowed matrix element
changes |E_l| by at most one. Integrating the norm differential inequality
proves (3). The infinite rotor case follows from finite restrictions on a
common core and the bounded-interaction self-adjoint construction. This
also yields endpoint tails <=e^(-lambda S) C_l and
||E_l^4 exp(-itH)psi||<=A_4(lambda) C_l.

Compare successively the full rotor, its hard box with quadratic E, the
same hard box with lambda_N(E), and the cyclic model. The first Duhamel
comparison loses only raising/lowering matrix elements that leave the box.
The last gains only wrap matrix elements with an input at an endpoint. By
telescoping each plaquette product, either comparison has norm error at
most 2T sum_l J_l e^(-lambda S) C_l. The middle comparison uses (2)-(3).
Thus the state-norm difference, after the stated embedding, is bounded by

```text
epsilon_N(T) := min{2,
   4T sum_l J_l exp[-lambda(S-M0)+2J_l T sinh lambda]
   + (pi^2 g^2 T/(6a N^2)) A_4(lambda)
                     sum_l w_l C_l(T,lambda)}.          (4)
```

This is uniform over the declared initial states and holds for fixed finite
spatial graphs, all T>=0 and odd N>=2M0+1. At fixed graph, T, g and initial
cap it tends to zero as O(N^-2), plus an exponential wrap/truncation bound.
The approximation is not operator-norm convergence on unrestricted states.
It does not assert a rate uniform in T->infinity or volume->infinity.
For a bounded observable A and its compressed cyclic counterpart J^dag A J,
the expectation error is at most 2||A|| epsilon_N(T). A usual cyclic word
in Z is a different observable at wrap endpoints and needs its own endpoint
estimate before it can replace this explicitly compressed observable.

The local reduction below uses onsite electric terms and N-independent
bounded interaction norms to replace this global finite-graph estimate
by a local one, while retaining its fixed-time quantifiers.

## A positive weight need not have positive Fourier coefficients

For the one-orbital four-site ring with real unit hopping and total flux phi,
let x=beta t>0. Its one-species grand canonical trace is

```text
d(phi)=4[1+cosh(2x cos(phi/4))]
         [1+cosh(2x sin(phi/4))],  0<=phi<=2pi.
```

In particular d(0)=16 cosh^2 x and d(pi)=16 cosh^4(x/sqrt(2)). The Taylor
series of cosh^2(x/sqrt(2))-cosh x has vanishing constant and quadratic
terms and positive coefficients (2^(n-1)-1)/(2n)! for every x^(2n), n>=2.
Therefore d(pi)>d(0), and the positive paired weight F(phi)=d(phi)^2 also
has F(pi)>F(0). A continuous positive-type function on U(1), with nonnegative
Fourier coefficients, must satisfy |F(phi)|<=F(0). Hence F is not of positive
type. For even finite N the same two values disprove positive type on Z_N.
This is an exact counterexample to deriving positive Fourier coefficients
from nonnegative paired determinants, within the broad finite model family;
it is not a claim about every member or every proof of a Coulomb phase.
The underlying expansion gives

```text
log d(phi)=4 log 2+x^2-x^4(1/8+cos phi/24)+O(x^6).
```

This ring is a separate diagnostic from the three-dimensional two-orbital
Weyl carrier. It retires an automatic transfer of a positive-type inequality
from the mere positivity of the measure, not the entire positive-model route.


## Local approximation independent of ambient spatial volume

Here is the explicit completion of the local reduction suggested above.
Use carrier units consisting of the matter cells and link registers, with a
fixed finite-range graph metric. Let b_Y be common upper bounds for the norms
of the hopping/plaquette terms Phi(Y) in both regulators; twice the sum of
raising-half norms on that support is one choice. Put all onsite terms into
an interaction picture; this changes neither supports nor norms. For mu>0 define

```text
C_mu = sup_x sum_(Y contains x) |Y| b_Y exp(mu diam Y).
```

It is finite on the fixed-degree cubic carrier graph and independent of N,
including the N-dependent onsite electric energy. Assume A is even, bounded
and supported on a fixed finite carrier set X. Define R containing X and

```text
W_R(mu) = sum_(Y crosses R) b_Y exp[-mu dist(X,Y)],
B_R(T) = ||A|| |X| [(exp(2 C_mu T)-1)/C_mu] W_R(mu),     (5)
```

with the continuous limiting expression if C_mu=0. Only interactions crossing
R enter; onsite terms outside R commute with the restricted evolved A.
For either dynamics, full or restricted to terms wholly inside R,

```text
||tau_T(A)-tau_T^R(A)|| <= B_R(T).                       (6)
```

A direct derivation avoids any ground-gap assumption. Set
M_xy=sum_(Y contains x,y)b_Y. The usual commutator integral inequality,
iterated in the interaction picture, bounds the commutator with a local B by
2||A||||B|| sum_(x in X,y in supp B) [exp(2T M)]_xy. Weighted row sums of
M are <=C_mu. The triangle inequality for distances then bounds this sum by
|X| exp(2C_mu T-mu dist(X,supp B)). Duhamel's formula for deleting crossing
terms and time integration gives exactly (5)-(6). This applies to even CAR
observables because disjoint even observables commute. Projection onto a
Gauss sector does not enlarge the full-Hilbert-space norm bound.

For cubic boxes R expanding about fixed X, W_R(mu)->0: the number of crossing
finite-range terms grows polynomially while their distance from X grows
linearly. This statement uses the declared finite-range graph and coefficients,
not a volume-dependent interaction norm.

Take any initial density matrix with all links supported in |E_l|<=M0 and
embed it into the cyclic model, N>=2M0+1. Its restriction to R has the same
support bound; arbitrary entanglement with the exterior is allowed by
purification. For the local compression A_N=J_N^dag A J_N and the cyclic
counterpart rho_N, (4)-(6) give

```text
|Tr rho tau_T(A)-Tr rho_N tau_T^N(A_N)|
   <= 2 B_R(T)+2||A|| epsilon_(N,R)(T),                 (7)
```

where (4) is evaluated only on links and interactions of R. The bound holds
uniformly in every finite ambient box containing R and its crossing terms.
Thus for each fixed T, finite X, initial cap and tolerance, first choosing R
and then one finite N gives the tolerance independently of the ambient volume.
No independent-cell, product-state or gauge-fixed ground-state hypothesis is
used. It still does not control a fixed N at arbitrarily large times or prove
vacuum convergence or phase stability. The observable is the explicit local
compression; a cyclic word that wraps requires its additional endpoint bound.

For completeness, the untruncated rotor dynamics in this proof can be built
in the interaction picture of the diagonal electric terms. At finite volume
the interaction is bounded and strongly continuous in that picture. Its
strongly integrated Dyson series has an operator-norm-convergent tail, bounded
by the exponential-series tail; norm continuity of the individual
interaction-picture shifts is not assumed. Starting
from a finite electric cap, its nth term changes each electric number by at
most n. Hard-box approximants therefore converge on that dense initial domain.
This justifies passage from the finite weighted estimate to (3) without an
unproved interchange of an infinite weighted operator and its dynamics.

## Additional local charge interaction

The positive representation also allows the genuine quartic interaction

```text
H_U = (1/2) sum_x u_x Q_x^2,  u_x>=0.
```

For each site and slice,

```text
exp(-delta u Q^2/2)
   = integral dphi exp(-phi^2/2)/sqrt(2pi)
                     exp(i sqrt(delta u) phi Q).        (8)
```

Use the slice exp[-delta(H_E+H_U)] exp[-delta(H_B+H_m)]. Each group is
Hermitian, and its positive exponential makes this slice similar to a
positive symmetric slice. The plus and minus auxiliary one-particle factors
are conjugate unitary diagonal matrices. Insert them in the same relative
position in the ordered products
in (1); their determinants remain conjugate for each real auxiliary history.
The Gaussian measure is positive and the integrand is bounded by a finite
volume exponential in beta||h||, so the finite-slice integral is well-defined.
Lie product convergence supplies the exact finite-volume physical Gibbs trace
with H_U. H_U is onsite and commutes with every E_l, so it does not increase
J_l or the hopping/plaquette C_mu used in (3)-(7).

For one orbital per species per site, Q is -1,0,1. There is also an exact
two-point decomposition with cos(theta)=exp(-delta u/2):

```text
exp(-delta u Q^2/2)=(exp(i theta Q)+exp(-i theta Q))/2.
```

This last finite sum does not apply unchanged to the two-orbital Weyl cell,
where |Q| can reach 2. Equation (8) covers that cell without this restriction.


## Representation limits and source credit

Determinant conjugation is standard prior art, including Wu and Zhang,
cond-mat/0407272, section III. The construction here uses the elementary
factorized subcase. Its new research role is the explicitly projected finite
gauge carrier together with the stated rotor approximation; no claim of
inventing determinant positivity is made. Neither the mathematical
antiunitary nor the model Hamiltonian is a derived framework time reversal.

The pure-gauge phase results in the cited Frohlich-Spencer preprint are read
as comparators, not imported hypotheses. Their four-dimensional Euclidean
action has no light dynamical fermion determinant. Even the temporal
anisotropy needed to match this Hamiltonian must be checked. In particular,
fixed-N behavior as g tends to zero is not controlled by the fixed-g finite
time approximation. No conclusion about that order of limits is asserted.

At N=3 on two Wilson cells, the physical Fock space has dimension 86,
including 16 basis states with nonzero integer total charge divisible by 3.
At N=5 the corresponding dimension is 70 and no such total-charge states
are available on this small graph. This finite count is not a thermodynamic
suppression argument. Both populations are included in the projected trace.

The first exploratory trace implementation's real dtype discarded complex hopping
entries and failed its Gauss commutator check. Its failed source and output
are preserved in the accompanying campaign packet.
After correcting the dtype, the full-Fock, charge-interaction and Wilson
carrier comparisons ran successfully with their nonzero finite-slice errors
reported. Distinct author implementations are not independent review.


## Matched prior art and remaining research value

Current main at b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf already supplies the
finite cyclic gauge-matter carrier and no-wrap Maxwell tangent in
`U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`.
That complete source was read, including its corrected fixed-g anharmonic
floor and open many-link phase. The present construction does not invent
finite clock gauge theory. It joins conjugate full CAR matter, the nonzero
Gauss projection, and nonnegative temporal histories to an explicit local
finite-time cyclic-to-rotor error bound.

Hard truncation and bounded local-quantum-number growth are established
machinery; Tong, Albert, McClean, Preskill and Su, arXiv:2110.06942, sections
2-3, treat a broader family and sharper asymptotic thresholds. The present
bound is an explicit conservative specialization with an additional cyclic
wrap and cosine-electric comparison. It is not a new general truncation
principle. The unbounded-onsite locality argument was checked against
Nachtergaele and Sims, arXiv:1410.8174, section 3, equations (67)-(76).
Their commutator iteration is majorized here by the explicitly defined
nonnegative matrix M; no F-function convolution constant is silently
substituted for C_mu.

The main SU(3) Wilson-staggered constrained-fiber two-layer KP note dated
2026-07-12 was also compared. Its small-beta, large-mass, supplied hidden-fiber
region and coarse gauge-body cumulant theorem do not establish the weakly
coupled dynamical-photon phase of this Hamiltonian. No failure of that
particular KP inequality is claimed, and no such theorem is imported here.


## Additional discriminator: the electric-density spectral moment

On the integer-flux rotor or hard-cutoff carrier, take a charge-one directed
hop V_l with [E_l,V_l]=V_l and
[rho(h),V_l]=(D^T h)_l V_l. Set h_l=V_l+V_l^dag,
F=E(f)-rho(h), v=f-D^T h and b=B^T f, with real f,h. Assume the onsite terms
commute with rho(h). Commuting each monomial twice gives

```text
[F,[H,F]] = -sum_l v_l^2 h_l + sum_p K_p b_p^2 Re W_p.
```

Indeed [F,V_l]=v_l V_l and [F,W_p]=b_p W_p, so reversing the inner
commutator fixes the two displayed signs. In a ground vector, half the
expectation equals the first spectral moment of F. Gauss gives F=E(v) on
its physical subspace. For a transverse long-wavelength test, the plaquette
term has a curl-squared factor but the hopping term generally does not.
A pure-link variational argument therefore needs a new control of that
term, together with a lower bound on nonzero-energy spectral weight. This
identity is not a no-go and is not asserted for a globally additive electric
operator on cyclic wrap states. The direct analytic calculation is separate
from the runner's finite trace tests.

## Executable evidence and falsifiers

Run the linked primary runner with Python, NumPy and SciPy. It reads no
scientific repository files and contains all finite comparison constructions.
It reports eight check families, with their finite domains printed in the
receipt. Internal assertions are not independent scientific results.

- Complete one-bond Fock traces at N=3,4,5 and one through four slices match
  the projected positive history sum; wrong temporal conjugation retains a
  nonzero complex-weight witness.
- The actual two-orbital Wilson bond is tested at N=3,5 and one through
  three slices, including all modular Gauss sectors.
- A four-link N=3 plaquette uses a separately assembled flux/CAR Hamiltonian.
  One- and two-slice traces agree to relative error below 7e-15; a full
  unfixed one-slice sum checks the static gauge-fixing multiplicity.
- A one-orbital quartic charge interaction is compared with the exact
  two-point auxiliary-field sum. Its finite-slice error is reported; the
  two-point identity is not asserted for the two-orbital cell.
- A charged four-cycle compares N=3 through 65 with a hard rotor reference.
  The latter's analytic truncation error bound is below 2e-31 at the declared
  parameters. At N=65 the observed state error is about 8.70e-4, below the
  derived 2.38e-2 bound; alias probability is counted as error.
- Noncommuting electric raising blocks challenge the weighted-generator
  constant. Matrix ring traces challenge the positive-type counterexample;
  node Jacobians, Nambu spectra and full Fock antiunitaries challenge the
  pairing and free-symbol statements.

The proposal fails if its exact projected trace differs from the Fock trace,
if a negative history weight occurs under the stated hypotheses, if the
weighted or locality estimates fail in their declared domains, or if the
explicit pairing fails to commute with charge or preserve its stated
antiunitary. Agreement in finite examples does not exclude an error in a
general proof. Independent review must check the weight, endpoint,
commutator-path and limit arguments directly.

## No-Go Discipline Gate

### N1 — Alternative routes actually examined

| Route family | Status | Discriminating result or obligation |
|---|---|---|
| Conjugate charged cyclic histories | ATTEMPTED, positive in scope | Exact nonnegative projected trace with noncommuting temporal factors |
| Hard-box and cyclic rotor approximation | ATTEMPTED, positive in scope | Explicit state and local-observable error bounds; fixed-time quantifiers |
| Positive-type correlation-inequality transfer | ATTEMPTED, automatic inference refuted | Positive paired ring determinant exceeds its zero-flux value |
| Symmetry protection of free Weyl nodes | ATTEMPTED, automatic inference refuted | Neutral pairing respects gauge and antiunitary and opens the displayed gap |
| Direct electric-density variational moment | ATTEMPTED, phase estimate open | Exact charged hopping term survives the proposed long-wavelength test |
| Controlled massive-fermion expansion and charged infrared RG | OPEN | Exact source hypotheses and infrared-uniform estimates still needed |

These routes differ in their mathematical objects and terminal proof
obligations. Their count says nothing about completeness of the search.

### N2 — Wall dependence

Vacuum convergence, the interacting photon phase and absence of pairing are
coupled parts of one infrared problem, not independent exclusion theorems.
Native Hamiltonian selection and physical identification are other open
obligations; no pairwise independence theorem or number of necessary axiom
updates is claimed. Let I denote that collapsed infrared problem, L native
law selection and P physical identification. Their logical relations are:

| Pair | First closes second? | Second closes first? | Independence proved? |
|---|---|---|---|
| I, L | unresolved | unresolved | unresolved |
| I, P | unresolved | unresolved | unresolved |
| L, P | unresolved | unresolved | unresolved |

### N3 — Hidden conditions

The carrier, opposite charges, normal-number symmetry, hopping matrices,
filling, couplings, initial flux cap, fixed observation time and compressed
observable are supplied explicitly. Locality uses bounded finite-range
interactions and even observables. The word positive describes weights or
operators, with neither an efficiency nor a phase implication attached.
The phrase scan found explicit mathematical assumptions on initial support,
evenness and onsite commutation, all stated in their theorem domains.
"Canonical" names the execution cache or the grand canonical trace; those
uses supply no physical premise. No framework-supplied law or hidden
background field is asserted.

### N4 — Residual matching

The main finite-clock note leaves the full phase open; this note closes a
positive charged-history construction and local finite-time comparison only.
The pure-gauge Frohlich-Spencer source has no light fermion determinant, the
main KP source is in a different high-mass/small-beta region, and the hard
truncation literature does not prove this cyclic regulator's ground phase.
None is cited as if its unmatched hypotheses had been discharged.

### N5 — Resolution and rhetoric

The runner prints per_element, per_site, per_mode, per_block and lattice_wide
certificates. The lattice-wide statement is uniformity of a fixed local
finite-time approximation over ambient boxes. No finite trace, mode count,
cutoff ladder or PASS count is a thermodynamic proof. The two counterexamples
reject specified inference rules within explicitly supplied model families.

### N6 — Partial-closure routes and primitive boundary

Controlled charged infrared RG, a matched massive-fermion compact-gauge
expansion, a different symmetry class or an independently established
finite-payload Coulomb phase could advance the remaining problem. None is
excluded here. No axiom or primitive update is requested.

### N7 — Hostile steelman

A reviewer should reject an interacting-photon claim inferred from positivity,
a bare dispersion or a fixed-time norm limit. That objection is accepted and
sets the boundary throughout the note. A reviewer should also reject reuse
of the pairing example as a perturbation preserving exact matter-number
symmetry: it explicitly breaks that symmetry, while spontaneous breaking
inside the number-conserving model remains an open dynamical question.

### N8 — Cross-cycle echo

Earlier hard-flux work isolates boundary truncation and a nonunitary raising
operator. The present cyclic regulator keeps exact unitarity and pays modular
aliasing plus cosine-electric error instead. Both errors are bounded only for
the stated finite-time comparison. Earlier free-node and ground-energy
results remain distinct from the present charged phase obligation; they are
not promoted by this construction.

Gate disposition: author scope review complete for the displayed positive
and counterexample implications. No broad negative theorem is submitted.
Independent scientific review is pending.

## References and exact use

- [Wu and Zhang, sufficient condition for absence of the fermion sign problem](https://arxiv.org/abs/cond-mat/0407272), section III: prior art for conjugation and antiunitary criteria.
- [Tong et al., provably accurate simulation of gauge theories and bosonic systems](https://arxiv.org/abs/2110.06942), sections 2-3: prior art for electric truncation and local quantum-number growth.
- [Nachtergaele and Sims, dynamics with unbounded onsite terms](https://arxiv.org/abs/1410.8174), section 3: checked commutator-iteration machinery underlying the direct local bound.
- [Frohlich and Spencer, IHES/P/81/40](https://omeka.ihes.fr/files/original/c59d65f61f9b1aba2d8eb6f4c01ceb88.pdf), sections 2.11-2.12 and 3: pure-gauge phase-method comparison, not a charged theorem import.
- [Current main finite-clock gauge-matter note](U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md): matched repository prior art, with its corrected fixed-coupling spectral boundary.
- [Current main constrained-fiber KP note](WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md): scope comparison only.

## Review record

The author corrected the exploratory real/complex dtype error, stated the
modular total-charge aliases, separated fixed-time bounds from a phase theorem,
and checked that the neutral pairing preserves the mathematical antiunitary.
The self-contained runner combines distinct author implementations; this is
not independent review. Exact source and failed-attempt preservation are in
the campaign packet. Formal audit remains deferred to the independent path.
No editable prompt or workflow files were changed by this science proposal.

## Source status and trace

```yaml
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "A controlled interacting charged gauge phase on the supplied finite-payload carrier, with matched local observables and physical identification."
source_of_blocker_text: "frontier_question"
reachability_to_target: "supports"
artifact_role: "theorem"
next_trace_action: "Independently review the positive projected trace and explicit local bound, then test a matched interacting vacuum/infrared construction."
conditional_surface_status: "Supplied cyclic links, conjugate opposite-charge CAR matter, bounded finite-range interactions and initial electric cap; exact positive finite-volume histories and local fixed-time rotor approximation, with the ground-state and infrared phase unproved."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Direct conditional mathematical implications and explicit counterexamples; neither author checks nor provisional source status grants retention."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
