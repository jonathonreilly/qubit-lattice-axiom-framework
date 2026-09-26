# Permanent record contents and symmetric field dynamics

Date: 2026-09-22. Author derivation and finite exact controls; independent
comparison is pending. This extends the supplied bosonic gauge model, not
the native site axioms. It does not establish a phase, a naturally selected
initial state, or an autonomous preparation apparatus.

The identical-content premise can be weakened: all existing records may
have different internal contents, provided their joint state has support
in the fully symmetric permutation sector. There is an exact microscopic
intertwiner in that sector, not only a fourth-order coincidence. A supplied
local exchange reservoir can prepare the required state at fixed content
counts. A classical mixture invariant under permutations does not satisfy
this premise.

## 1. Supplied extension and the exchange carried by a loop

Keep the hard-core constraint, bosonic hopping, gauge links, Gauss law,
checkerboard initial occupation, and either penalty from
HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md. Replace a plus record by
k orthogonal internal states |+,alpha>, alpha=1,...,k, with the same charge.
The closed Hamiltonian transports alpha unchanged and its matrix elements
do not depend on alpha. Initially there are N=|A| plus records, no minus
records, and the usual divergence-free field. This adds local states; it is
not a qubit encoding derived from the site axioms.

Every nontrivial four-hop plaquette return exchanges its two initially
occupied A corners a(p),b(p). The field operator is therefore accompanied by
their content swap P_ab:
\[
 H_{\mathrm{ring,col}}
   =-J\sum_p (W_p+W_p^\dagger)\otimes P_{a(p)b(p)},\qquad
 J=2t^4/\Delta^3.                                      \tag{1}
\]
The second-order return and the fourth-order diagonal returns leave the
contents in place. Their coefficients are unchanged. With spin-half links,
the checked scalar fourth-order term is unchanged as well. With integer
spin links, the electric-square and weighted diagonal terms from
ELECTRIC_AND_MAGNETIC_DYNAMICS_FROM_RECORD_MOTION.md multiply the identity
on contents. The four directed path orderings have the same content swap,
so no extra factor of two or averaging over contents is allowed in (1).

On a single plaquette the independently constructed author control uses
the complete 7-state two-record spin-half sector and all four two-color
words, hence 28 microscopic states and 8 code states. Exact normalized
perturbation gives
\[
 H_2=-2I_8,\qquad H_4=2I_8-2X_{\mathrm{loop}}\otimes P_{12}. \tag{2}
\]
These checks verify the content action; the general locality statements
below use the analytic construction, not this small example.

## 2. Exact symmetric-sector intertwiner

A base configuration c specifies all occupied sites and the electric word.
Order the occupied sites by a fixed total order. Its content fiber is
\((\mathbb C^k)^{\otimes N}\). A hopping edge from c to c' has its original
scalar field amplitude multiplied by a permutation \(P_{\pi(c',c)}\) of
these N content slots: the record carries its content while the slot list
is reordered. All penalties and other stipulated diagonal terms are
content independent.

For any normalized \(v\in\operatorname{Sym}^N(\mathbb C^k)\), define
\(R_v|c\rangle=|c\rangle\otimes v\). Every permutation fixes v, so termwise
\[
 H_{\mathrm{col}}R_v=R_v H_{\mathrm{base}},\qquad
 e^{-i\tau H_{\mathrm{col}}}R_v
       =R_v e^{-i\tau H_{\mathrm{base}}}.               \tag{3}
\]
This holds at finite hopping and link spin, in the entire fixed-number
all-plus sector. It does not require perturbation theory. It also holds
with a mixed state supported in the symmetric subspace, including
entanglement between base configurations and that subspace. There the
Hamiltonian is \(H_{\mathrm{base}}\otimes I_{\mathrm{sym}}\). Field and
occupation expectations evolve exactly as those of the base marginal.

At fixed counts \(\mathbf n=(n_1,\ldots,n_k)\), \(\sum n_\alpha=N\),
the symmetric sector is the single Dicke vector
\[
 |D_{\mathbf n}\rangle=
 \binom{N}{n_1,\ldots,n_k}^{-1/2}
 \sum_{\mathrm{words\ with\ counts}\ \mathbf n}
       |\alpha_1,\ldots,\alpha_N\rangle.               \tag{4}
\]
Different contents are present. Their locations have coherent exchange
amplitudes. No hopping operation changes a content value. An extra
classical identity tag that resolves all these alternatives is an
additional degree of freedom and cannot be silently discarded.

The same intertwiner holds for each penalty projector, its homological
inverse, products, commutators and the finite local dressing gates.
Consequently the prepared symmetric family inherits the checked
closed-field comparison, with exactly the original target dynamics.

## 3. Ground-energy existence, without a selection assumption

There is also a finite-graph variational statement. Suppose the base
Hamiltonian, in a specified connected configuration component, has real
diagonal V_c and nonpositive off-diagonal hopping amplitudes -a_cc',
with a_cc'>=0. Each colored hopping is the corresponding permutation
matrix times -a_cc'. Parallel hopping channels can be kept separate.

For a colored vector with fiber components \(\Psi_c\), put
\(r_c=\|\Psi_c\|\). Cauchy-Schwarz gives
\[
 \langle\Psi,H_{\mathrm{col}}\Psi\rangle
 \ge \sum_c V_c r_c^2
       -2\sum_{\{c,c'\}}a_{cc'}r_c r_{c'}
 =\langle r,H_{\mathrm{base}}r\rangle
 \ge E_0\|\Psi\|^2.                                    \tag{5}
\]
A base ground vector tensored with any symmetric v attains E_0 by (3).
Thus each nonempty fixed-content-count fiber admits a colored ground state
with exactly the base ground energy. No irreducibility of the lifted graph,
uniqueness, thermal order, or relaxation into this ground state follows
from (5). This sign premise is satisfied by the stipulated bosonic model
with positive spin-shift matrix elements and the chosen negative hopping
convention. It is not a theorem for arbitrary fermionic or frustrated phases.

This is an application of familiar bosonic polarization reasoning, not a
new physical mechanism. See the positivity argument and lattice
generalization in [Eisenberg and Lieb, 2002](https://www.tau.ac.il/~elieis/PDFS/p33.pdf).
The finite-fiber proof (5) supplies the precise statement used here.

## 4. Why a classical content mixture is different

For one loop use \(H=-JX\otimes P\), initially field |0> and a content density
rho. Set \(\eta=\operatorname{Tr}(P\rho)\in[-1,1]\). Direct exponentiation
gives, with theta=J tau,
\[
 \rho_F(\tau)=
 \begin{pmatrix}
 \cos^2\theta&-i\eta\cos\theta\sin\theta\\
 i\eta\cos\theta\sin\theta&\sin^2\theta
 \end{pmatrix},\qquad
 \operatorname{Tr}\rho_F^2
 =1-\tfrac12\sin^2(2\theta)(1-\eta^2).                  \tag{6}
\]
Two distinct definite contents |alpha beta> have eta=0, so the field is
maximally mixed at theta=pi/4. The symmetric fixed-count superposition
has eta=1 and gives the base coherent dynamics. The antisymmetric vector
has eta=-1 and reverses the phase in this example.

The mixture of |alpha beta> and |beta alpha> with equal weights commutes
with P but still has eta=0. Permutation invariance of a density operator is
therefore weaker than support in the symmetric subspace. For independent
identically distributed contents rho=tau tensor tau, eta=Tr(tau^2);
tau=diag(0.7,0.3) gives eta=0.58 and field purity 0.6682 at theta=pi/4.
These are explicit finite controls for (6), not a general no-go for
classical records or a statement about all interacting colored phases.

## 5. A local preparation channel at fixed counts

Supply a connected bounded-degree graph on the initially occupied A
sites. A face-diagonal graph has range two in the original cubic metric
and is connected for d>=2 on the stated even tori. Indeed the moves
e_i+e_j and e_i-e_j generate all integer vectors with even coordinate
sum, including 2e_i; their images generate the A sublattice modulo even
periods. A connected subgraph is enough.

For each edge (a,b) and alpha<beta define the local jump, with identity on
all other content slots,
\[
 L_{ab}^{\alpha\beta}
   =\frac{(|\alpha\beta\rangle+|\beta\alpha\rangle)
           (\langle\alpha\beta|-\langle\beta\alpha|)}2,
 \quad
 {\cal L}_{\mathrm{col}}=\sum_{ab,\alpha<\beta}
                    \gamma_{ab}^{\alpha\beta}{\cal D}[L_{ab}^{\alpha\beta}],
 \quad \gamma_{ab}^{\alpha\beta}>0.                    \tag{7}
\]
It is zero on other pair contents. Each jump preserves the content
multiset and all charges. It commutes with the field and Gauss operators.
The Hamiltonian is switched off during this preparation stage. The
resulting unique attractor in each fixed-count sector is (4), with
exponential convergence at each fixed finite graph.

Here is a complete attraction argument, specialized from the previously
checked fixed-displacement cooling theorem. The configuration set Omega
consists of all words with counts n. Exchanges on a connected graph
generate all permutations, hence its exchange graph is connected. In the
one-hot coordinates \(x_{a,\alpha}=1_{\{\text{content at }a=\alpha\}}\),
each oriented exchange alpha beta -> beta alpha has a fixed displacement
\[
 z=e_{a,\beta}+e_{b,\alpha}-e_{a,\alpha}-e_{b,\beta}.     \tag{8}
\]
For a fixed jump label, its pairs of configurations are a disjoint
matching with this same displacement, regardless of the spectators.
Write each pair as \(s=(|x\rangle+|x+z\rangle)/\sqrt2\),
\(d=(|x\rangle-|x+z\rangle)/\sqrt2\).
Then \(L=\sum|s\rangle\langle d|\) and \(L^\dagger L=P_-\).
The positive operator \(K=\sum\gamma P_-\) has kernel exactly the
uniform vector u, by graph connectivity.

It remains to exclude invariant subspaces orthogonal to u; uniqueness of
the common dark vector alone would not suffice. Suppose W is such a
subspace invariant under every L and the no-jump generator -K/2.
Then S=W-perp contains u and is invariant under every L-dagger and K.
K is invertible on u-perp, so \(K f\in S\) implies \(f\in S\), after
separating the component along u.

Restrict polynomials of the one-hot coordinates to Omega. Constant
polynomials give u. If all degree less than m restrictions lie in S,
let f have degree m. Translation \(T_z f(x)=f(x+z)\) has
\(\Delta_z=T_z-I\) lowering polynomial degree. Thus
\[
 g_z=(I+T_z)^{-1}(I-T_z)f
   =-\tfrac12\sum_{r=0}^{m-1}(-\Delta_z/2)^r\Delta_z f \tag{9}
\]
is a polynomial of degree at most m-1 and satisfies
\(g_z(x)+g_z(x+z)=f(x)-f(x+z)\).
It follows pair by pair that \(P_-|f\rangle=L^\dagger|g_z\rangle\).
Therefore \(K|f\rangle\in S\), and hence \(|f\rangle\in S\).
Induction gives every polynomial restriction in S. Polynomials separate
the finite distinct points of Omega and span all their functions, so
S is the whole space and W is zero.

For completeness this implies attraction, not just stationarity.
The u-perp corner is a completely positive trace-nonincreasing
semigroup. If a positive initial state retained nonzero trace there
indefinitely, its Cesaro averages would have a nonzero positive fixed
point. Zero leakage to u then makes its support invariant under the
full jumps and K, giving the forbidden W. Thus the corner trace decays
to zero. Finite dimensionality gives an exponential bound, with a
possibly smaller exponent than the spectral decay gap to absorb Jordan
polynomials. The off-diagonal corners vanish by positivity. This proves
convergence in trace norm. Since K u=0 and K is bounded, the integral
of Tr(K rho(t)) is finite: the expected total number of cooling jumps
is finite at fixed volume. No volume-independent preparation time,
gap or event budget is asserted.

Local antisymmetric-to-symmetric pumping is established reservoir
engineering. The bosonic construction in
[Kraus et al., 2008, Section V.1](https://arxiv.org/html/0803.1463v3)
uses the same principle. Its bosonic occupation space is different
from these fixed local contents; equations (8)-(9) check the relevant
hypotheses directly instead of importing that model's uniqueness proof.

A supplied fresh two-state ancilla realizes an individual jump exactly:
\[
 C=L\otimes|\mathrm{spent}\rangle\langle\mathrm{fuel}|+\mathrm{h.c.},
 \quad C^3=C,\quad
 A_0=I+(\cos\theta-1)P_-,\quad A_1=-i\sin\theta L.       \tag{10}
\]
With a fresh fuel state and \(\cos\theta=e^{-\gamma\,dt/2}\), discarding
the outgoing ancilla gives \(e^{\gamma dt{\cal D}[L]}\).
This exports entropy and requires fuel, routing and outgoing storage.
Interpreting outgoing ancillas as permanent records does not provide an
autonomous local implementation of these controls from the original
record-motion rule. Nor has a direct A-to-A content-swap control been
compiled from the original nearest-neighbor hopping. The preparation
stage is an explicit additional capability.

## 6. Slow births and what can be inherited

The exact intertwiner (3) is a closed fixed-number statement. Appending
new records with a definite local content does not generally map
Sym^N into Sym^(N+2), and no exact intertwiner for the full birth process
is claimed.

There is nevertheless a conditional extension of the already checked
uniform finite-time field estimate. Fix k and stipulate a bounded number
of local birth channels per edge, each with bounded norm before its
sqrt(beta) factor, preserving the charge rules and annihilating the
checkerboard code. The new plus contents may be chosen locally in any
fixed normalized state. Minus contents can be a single state or any
fixed finite extension. Use the same integer penalty, dressing order
n=2d+6, prepared symmetric state, and beta=beta_0 epsilon^(2d).

The proof changes are explicit. Hopping remains bounded independently
of volume and link spin; adding fixed k changes at most local constants.
The homological grading is determined by charges and occupations, not
contents. The local circuit is natural under R_v as in Section 2.
Dressed births still obey \(\|B P_{\mathrm{code}}\|=O(\epsilon)\);
therefore their full dissipator source on the symmetric code reference
has trace norm O(beta epsilon), including its anticommutator. Locality
estimates use operator norm bounds, which remain valid. The reference
code Hamiltonian preserves the symmetric sector exactly. The previously
checked clipped light-cone sum is therefore unchanged in its powers of
epsilon. It controls symmetry-breaking birth histories as errors, without
assuming that a birth preserves the symmetric sector.

Thus the spin-half local-field conclusion extends to this specified
finite-content family. Conditional on the large-spin moment theorem,
its rotor conclusion extends too: content permutations commute with
electric weights, and the weighted source estimates have unchanged
powers of S. This is a composition of stated proofs, not a separate
simulation of a finite density of colored births. An additional initial
trace-distance error delta in preparing the symmetric state contributes
at most \(2\delta\|O\|\) to the final expectation by channel contraction.

The formation rate tends to zero in that field limit. This result does
not prove that ongoing formation at a fixed rate can maintain the
symmetric sector, that local content readout preserves it, or that the
cooling channel selects it without supplied resources. Those remain
physical selection and implementation questions.

## 7. Evidence and claim boundaries

The companion record_content_permutation_check.py independently assembles
the complete colored square from microscopic transport rules. It checks
(2), exact hopping and penalty intertwiners, three finite-hopping ground
energies, six content densities at three times, and a five-vertex graph
whose hopping labels include noncommuting S3 permutations. The latter
has 30 colored states and reproduces the scalar ground energy to floating
precision. It is corroboration of (5), not a connectivity or phase theorem.

The companion local_record_content_symmetrization_check.py uses path graphs
with counts (2,1), (2,2), (1,1,1), (2,1,1), and (3,2), with configuration
dimensions 3,6,6,12,10. It checks the one-hot displacement identity for
every local matching, exact dark-state and trace identities, and exact
uniqueness of the stationary operator via modular rank of the integer
matrix 4L over the prime 65521. Rank D^2-1 over that field, together with
the exact nonzero dark vector, certifies rank D^2-1 over the complex
numbers. Finite-time matrices are then evolved numerically with positivity
and trace checks. The decay gaps in these controls range from about
0.09549 to 0.25. They are not a uniform asymptotic bound.

The first scientific executions of both runners passed with empty stderr.
One attempted tool patch was rejected before writing any checker file
because of an extra blank patch line; no computation or assertion failed.
All scientific outputs, execution receipts and source identities are
retained. This author packet requires independent comparison before it
can strengthen a publication claim. It preserves the distinction between
an exact invariant sector, a supplied preparation channel, a conditional
field limit and a physical mechanism selected by the native framework.
