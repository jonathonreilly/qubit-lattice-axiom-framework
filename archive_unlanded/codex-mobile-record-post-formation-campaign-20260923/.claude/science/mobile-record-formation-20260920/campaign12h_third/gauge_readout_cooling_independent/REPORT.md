# Independent gauge readout and finite-component cooling reconstruction

Date: 2026-09-22. This packet reconstructs the supplied models before access to
the new author notes, scripts, results, or seal contents. It is a conditional
mathematical check, not frontier-source authorship, a publication decision, or
an audit verdict. The complete neutral specification is in `SPECIFICATION.md`.

**Results.** Newly formed charge labels give exact ensemble estimators of X and
Y if opposite pulse settings are balanced independently of the input. A single
pulse generally retains a nonflippable-sector offset. The stated finite
plaquette cooler does attract every density on one connected physical
configuration component to its equal-amplitude vector, for all positive
gamma_p and real h_p. A degree-lowering polynomial argument supplies the
missing attraction step. Connectivity and a unique common dark vector alone
are insufficient when the constant-displacement move structure is removed;
an exact four-state counterexample is retained.

## 1. Plaquette algebra and the sign of the charge record

Let W=|b><a| on the flippable plaquette doublet, where a has the distinguished
raised link at E=-1/2 and b has it at E=+1/2. Spectator factors are implicit.
Put

    P = W†W + WW†,       Z_f=P Z,       Z_nf=(I-P)Z.

Then W²=0, X²=Y²=P, [X,Y]=2i Z_f, [Z,X]=2iY, and [Z,Y]=-2iX.
X and Y vanish on the nonflippable subspace, whereas Z need not vanish there.
These statements are operator identities, not assumptions on the density.

Take the distinguished edge to be oriented x->y. U raises E by one, so

    V_+ = |+,- ><0,0| U,       V_- = |-,+><0,0| U†.

Increasing the oriented E increases div E at x and decreases it at y, exactly
matching the created charges. Thus [G_v,V_q]=0 at every vertex. The two initial
field domains are complementary:

    V_q† V_q = P_vac (I-q Z)/2,       sum_q V_q†V_q=P_vac.       (1)

The charge q recorded at x therefore equals **minus** the initial edge Z value
on a field-basis input. A common coefficient beta for both jumps gives total
vacant-edge loss beta P_vac, not 2 beta P_vac. The initial endpoints must be
vacant, and the fresh probe must initially be independent of the system.

## 2. Exact readout for arbitrary field states

For a sign setting s=±1 define

    R_s^X = exp(+i s pi Y/4),       R_s^Y = exp(-i s pi X/4).

Direct doublet rotation, with identity action outside P, gives

    (R_s^O)† Z R_s^O = Z_nf + s O,           O=X or Y.          (2)

Apply the selected pulse and then a complete pair-formation instrument, reading
the newly formed charge q at x. For an arbitrary field density rho,

    Pr(q|s,O)=Tr[rho (I-q(Z_nf+sO))/2].                         (3)

With a fair sign s independent of rho, the retained binary value o=-s q obeys

    E[o|O]=Tr(rho O),       E_o^O=(I+o O)/2.                   (4)

Thus it is a valid binary POVM on the entire field space. On a nonflippable
input it adds a fair output coin; it does not wrongly identify that subspace
with a Pauli doublet. This binary POVM is a coarse graining of the actual
four outcomes (s,q). Retaining both the setting and charge is a finer
instrument and can reveal additional information; (4) alone does not
specify its disturbance. Equivalently, on identically prepared subensembles,

    <O> = -( E[q|s=+1,O]-E[q|s=-1,O] )/2.

For a single s=+1 pulse, -E[q]=<Z_nf>+<O>. The all-low local link word has
<X>=<Y>=0 but <Z_nf>=-1. It is an exact counterexample to the uncorrected
single-setting claim. This local word can occur in the all-low uniform field
on a periodic lattice with vacant matter and zero Gauss charge; the issue is
not an artifact of violating physical constraints.

The pulse and formation identities hold on the full local operator space and
therefore restrict to any compatible physical Gauss sector. They do not mean
that every arbitrary local density can be combined with a fixed external
field and still satisfy a prescribed Gauss constraint. The initial global
state must be physical when a physical interpretation is asserted.

If formation succeeds with a setting-independent probability p in (0,1),
conditioning on success leaves (3) unchanged. Alternatively give a failed
trial output zero and a successful trial output -s q/p; its expectation is
still <O>. Field- or setting-dependent success rates would require a different
analysis. These formulas concern the state presented to the pulse/instrument;
uncontrolled evolution during a waiting interval changes that state.

The setting may be held in an unchanged orthogonal classical record:
`sum_s |s><s| tensor R_s^O` does not change its label. Its independence from the
field and the availability of the controlled pulse are supplied resources.
Correlation between setting and input invalidates the simple pooled estimator.
Separate preparations/settings estimate X and Y; this is not a joint sharp
measurement of two noncommuting observables on one unknown copy.

## 3. Gauge-preserving fresh-probe dilation and disturbance

Use orthogonal neutral probe states f, s_+, s_- and define

    C = sum_q (V_q tensor |s_q><f| + V_q† tensor |f><s_q|).

The stipulated local algebra gives C³=C. Hence

    exp(-i theta C)=I+(cos theta-1)C²-i sin theta C.

For a fresh fuel state f, the boundary Kraus operators are

    M_0=I+(cos theta-1)P_vac,
    M_q=-i sin theta V_q.                                     (5)

For 0<=theta<=pi/2 they give success probability p=sin²theta on every vacant
input. A full readout uses theta=pi/2. A partial step equals the birth-only
semigroup with generator `beta sum_q D[V_q]` when
`cos theta=exp(-beta t/2)`. This correspondence is local and birth-only;
interacting simultaneous Hamiltonians are not silently included.

Both the loop pulses and C commute with every Gauss operator. Also

    [C,N+2|f><f|]=0,       channel†(N)-N=2p P_vac.              (6)

Fresh-fuel boundary maps leave an already occupied input unchanged by the
birth interaction. During the coherent pulse, the adjoint term is present;
an intermediate measurement or reuse of a spent probe is a different process
and can permit reverse transfer. Removal/reset of the probe, the controller,
vacant matter sites, and pulse timing cannot be omitted from the realization.
One may supply a rest-energy term proportional to N+2P_fuel, but (6) does not
establish conservation of an arbitrary interacting field/matter Hamiltonian.

The three-state pure probe is sufficient for the displayed coarse instrument.
For a nontrivial partial birth its no-event, plus, and minus Kraus operators
are linearly independent, so its coarse channel has Choi rank three. On an
input restricted to the vacant subspace at p=1 the no-event operator vanishes,
leaving rank two. If occupied inputs are also included, the identity action
there retains a third Kraus direction. Individually retained outcomes are
the ones explicitly specified in (5); a different refinement must not be
identified merely from its coarse map.

There is substantial backaction. For the symmetric flippable field state
(a+b)/sqrt(2), a charge-resolved complete birth without a preceding pulse
changes the field's X expectation from 1 to 0 after tracing the records.
Reading an orthogonal charge content can preserve that *new classical label*
while still disturbing the source field. Repeated measurements on the evolved
same field are not independent samples of its original density.

## 4. The finite physical cooler: statement and elementary facts

Let C be a nonempty finite set of distinct link-configuration vectors, and let
m=|C|. For each p the oriented disjoint pairs satisfy b=a+z_p with one fixed
vector z_p. No basis configuration occurs twice in one p's pairs. Define

    L_p=sum_pairs |s_ab><d_ab|,       P_p^-=L_p†L_p,
    H=sum_p h_p P_p^-,               B=sum_p gamma_p P_p^-.

Here gamma_p>0, h_p is real, and there are no other generator terms. Each L_p
has square zero, and P_p^- is an orthogonal projector. On a pair its matrix is

    L_p = (1/2) [[1,-1],[1,-1]],
    P_p^- = (1/2) [[1,-1],[-1,1]].

Let psi=m^(-1/2) sum_(c in C) |c>. Connectivity implies

    intersection_p ker L_p = ker B = span{psi},
    H psi=0.

The density P_0=|psi><psi| is stationary. This alone is not an attraction proof.
The following argument establishes that for every initial density on this
component,

    exp(t G)(rho) -> P_0 in trace norm.                         (7)

For each fixed finite model the convergence has an exponential bound with
model-dependent constants. No bound uniform in volume, component, rates, or
boundary sector is obtained here. A singleton component is the trivial case.

## 5. Load-bearing attraction proof

### 5.1 What obstruction would prevent attraction

Put K=H-iB/2. A surviving stationary density orthogonal to psi would have a
nonzero support S contained in psi-perp that is invariant under every L_p and
under K. This can be derived directly: in a positive stationary state, a
diagonal matrix element on the kernel of the density is a sum of nonnegative
jump terms. Each term must vanish, giving invariance under L_p; off-support
matrix elements then give invariance under K.

For precision, the same statement suffices even if a putative stationary
density initially has overlap with psi. Relative to psi plus psi-perp, L_p
has blocks `[[0,ell_p],[0,A_p]]`, while H and B are block diagonal. The
psi-perp corner evolves by a completely positive, trace-decreasing semigroup.
Its trace loss is `sum gamma_p Tr(ell_p†ell_p sigma)`. A stationary positive
corner has zero loss, so ell_p annihilates its support, and the preceding
support argument gives the required S for the full L_p and K.

If the transient corner retained a positive asymptotic trace, its time
averages would have a nonzero positive stationary limit point in finite
dimension. Thus exclusion of S implies vanishing transient trace. Positivity
also bounds the target/transient cross block by the square root of that
trace, proving (7). The transient finite-dimensional semigroup then has all
spectral real parts strictly negative: otherwise its norm could not tend to
zero on the positive cone, which spans its operator space. Finite Jordan
blocks can be absorbed into an exponential bound with a smaller exponent.

### 5.2 The constant displacement supplies a degree-lowering identity

For a polynomial f on the ambient real link-coordinate space, write f_C for
its values on configurations. Let T_p translate a polynomial's argument by
z_p. On polynomials of degree at most n, Delta_p=T_p-I is nilpotent and lowers
degree. Therefore

    g_p=(I+T_p)^(-1)(I-T_p) f
       =-(1/2) sum_(r=0)^(n-1) (-Delta_p/2)^r Delta_p f         (8)

is a polynomial of degree at most n-1 (zero for a constant). At every allowed
pair a->b=a+z_p it satisfies

    g_p(a)+g_p(b)=f(a)-f(b).

On nonflippable configurations both relevant operators vanish. Consequently
the following is an exact vector identity on the entire component:

    P_p^- f_C = L_p† (g_p)_C.                                 (9)

The same translation z_p for every spectator pair is essential to this
uniform polynomial construction. Merely drawing a connected configuration
graph does not supply (9).

### 5.3 Exclusion of every orthogonal invariant support

Suppose S as in 5.1 existed and put R=S-perp. Then R contains psi and is
invariant under every L_p† and under

    Q=K†=H+iB/2=sum_p(h_p+i gamma_p/2)P_p^-.

Q preserves psi-perp and is invertible there. Indeed Qv=0 would imply
`Im <v,Qv>=(1/2)sum gamma_p ||P_p^- v||²=0`, hence v is proportional to psi.
Since R intersect psi-perp is a finite-dimensional Q-invariant space, Q is
also invertible on that subspace, and its inverse preserves it.

Induct on polynomial degree. Constants lie in R. If all degree-(n-1)
polynomial value vectors lie in R, then (9) gives

    Q f_C = sum_p(h_p+i gamma_p/2) L_p†(g_p)_C in R

for any degree-n f. This vector is also perpendicular to psi. Subtract the
constant component from f_C and invert Q on psi-perp; the invariant inverse
shows that f_C lies in R. This completes the induction.

Polynomials separate the finite distinct vectors C. For example choose a
generic linear functional with distinct values on C and interpolate a
univariate polynomial at those m values. Hence their restrictions span all
of C^m. The induction gives R=C^m and S=0, a contradiction. This proves
attraction under the full stated hypotheses for arbitrary real h_p.

This proof does not substitute unique common darkness for an invariant-space
condition. Nor does it assume that the different P_p^- commute.

## 6. Counterexample if the physical move structure is discarded

Take four abstract configurations 0,1,2,3, with oriented pair families

    p: (0->1),(2->3),        q: (1->2),(3->0).

Both are disjoint pair families. Their undirected graph is connected and the
only common dark vector is the uniform one. Nevertheless S spanned by
`(1,0,-1,0)` and `(0,1,0,-1)` is invariant under both jumps and their loss
projectors. With equal rates and h_p=h_q=0, the density

    rho_S=(1/4) [[1,0,-1,0], [0,1,0,-1],
                [-1,0,1,0], [0,-1,0,1]]

is exactly stationary, has rank two, and has zero overlap with the uniform
target. In an orthonormal basis of S, the two jumps are amplitude raising
and lowering in opposite directions, which explains the stationary mixture.

These oriented pairs cannot be embedded as distinct real configuration
vectors with constant displacements z_p,z_q. The four displacement equations
would force c_0=c_2 and c_1=c_3. Thus the counterexample removes precisely a
load-bearing physical hypothesis; it does not refute (7).

## 7. Fresh collisions and finite expected jump records

For one p, a two-state fresh probe with ready state 0 and click state 1 gives

    C_p=L_p tensor |1><0| + L_p† tensor |0><1|,       C_p³=C_p.

Its reduced boundary map has

    A_0=I+(cos theta-1)P_p^-,       A_1=-i sin theta L_p.        (10)

It exactly equals `exp(t gamma_p D[L_p])` for
`cos theta=exp(-gamma_p t/2)`. Including the local Hamiltonian h_p P_p^- gives
the exact local semigroup Kraus choice

    A_0=I+(exp[-gamma_p t/2-i h_p t]-1)P_p^-,
    A_1=sqrt(1-exp[-gamma_p t]) L_p.                            (11)

The jump's overall phase is immaterial to this coarse map. One probe click
records p's jump without distinguishing its spectator pairs; a more refined
retained outcome instrument need not give the same CP map. Reusing the same
probe is not the fresh-probe evolution: two pi/2 interaction pulses take an
antisymmetric-to-symmetric transfer back to its initial antisymmetric state, up to
phase. The single interaction conserves `P_p^-+P_click`, but that local
identity is not conservation of an arbitrary overlapping many-body energy.

For multiple overlapping plaquettes, a finite ordered product of (11) is
generally not `exp(t G)`. Fresh local steps and local phase steps give the
specified generator in the ordinary small-step/Trotter limit: each map is
`I+dt G_p+O(dt²)`, and telescoping over fixed total time gives an O(dt) error
for each fixed finite model. No volume-uniform constant is asserted. The
ancillas, their fresh low-entropy state, reset/disposal, and timing are supplied.
With some h_p negative the preparation is still proved, but it is not thereby
thermal cooling to the ground state of an arbitrary physical Hamiltonian.

For the specified jump unraveling, the mean number of clicks up to time t is

    E J_t = integral_0^t Tr(B rho_s) ds.

B annihilates psi, and the transient corner decays exponentially. Hence

    R_J=integral_0^infinity exp(s G†)(B) ds

is a finite positive operator, `G†R_J=-B`, and `R_J psi=0`.
For every initial density, `E J_infinity=Tr(R_J rho_0)<infinity`; the total
number of clicks is consequently finite almost surely. The inequality
`G†(P_0) = sum gamma_p L_p† P_0 L_p <= B` also gives

    R_J >= I-P_0.

This is a jump-record statement for the chosen monitored realization. It is
not a representation-independent thermodynamic cost, a volume-uniform budget,
or a finite-time exact stopping certificate. An infinite-time fresh-collision
protocol can supply infinitely many no-click probes despite a finite expected
number of spent click records. Recording settings or every failed probe adds
other memory costs. The link-only cooler does not itself implement matter-pair
birth merely because a probe click can be stored as a record.

## 8. Literature boundary

[Weimer et al., arXiv:0907.1657v2](https://arxiv.org/pdf/0907.1657v2), PDF pages
4–5, Eq. (12), supplies the established local jump. With its B_p identified
with X, `Z(I-X)X/2=-Z P^- = L_p` for the raised-edge convention above, up to an
irrelevant overall sign for another link convention. Thus the local cooler
is not claimed as new here. The paper's finite demonstration is not imported
as the missing general attraction proof.

[Kraus et al., arXiv:0803.1463v3](https://arxiv.org/pdf/0803.1463v3), PDF pages
1–3, was read through Theorem 2 and its proof. Its sufficient condition
excludes an orthogonal subspace invariant under every jump; one common dark
vector alone is not that condition. Its dissipative convention uses twice
the present D[L], so g_p=gamma_p/2. Here sections 5.1–5.3 independently exclude
the necessary joint jump/effective-Hamiltonian invariant support and establish
convergence, without presuming the theorem's stronger stated hypothesis.

PDF bytes and selected extracts are preserved and hashed. No unrelated phase,
experimental performance, or thermodynamic result from either paper is used.

The two unchanged permitted local-instrument dependencies were reauthenticated:
`COHERENT_NEUTRAL_PAIR_FORMATION_AND_GAUGE_MEMORY.md`, SHA256
`9c71310bfe26b93ae5206d5a4525bc01dc6136be1d39e6f1b08ecfa08b83e6a4`, and
`FRESH_MOVING_MEMORY_DILATES_COHERENT_PAIR_BIRTH.md`, SHA256
`49b1abd18c3c793b4089de38055b447842a96e4f74317b04dc0b857aa78b901a`.
The pinned Weimer PDF is
`b0960af617c8b922382dbeccf97548427003812a3e5e3c8d546881bb90881e7b`;
the pinned Kraus PDF is
`2635be63106a6dca937a104e62af145e6f84e211887ee9d877fe95bfe198edb3`.
The local algebra needed here was reconstructed explicitly above rather than
being taken from any new author source.

## 9. Independent controls, attempts, and remaining boundaries

`readout_check.py` constructs the full 16-dimensional field algebra, the
144-dimensional matter/field maps and 432-dimensional neutral-probe unitary.
It checks the complete pulse/POVM identities, Gauss commutators, count
conservation, all three Kraus operators, and disturbance exactly. At
cos(theta)=3/5 the global Kraus Hilbert-Schmidt Gram diagonal is
`(3344/25,128/25,128/25)`, confirming rank three. The single-pulse nonflippable
countercontrol is exact.

`cooling_check.py` independently enumerates all 1,024 link configurations of
an open strip of three squares. It selects the lexicographically first
largest component, `[248,362,419,590,647]`, and verifies its disjoint pairs,
fixed displacements and common Gauss charges. These open-boundary charges
are fixed sector data; no zero-boundary-charge condition was assumed.
For gamma=(1,2,3) and h=(-2,1/3,4), it checks all polynomial identities through
degree four, exact common-dark dimension one, exact Liouvillian rank 24 of
25, and a full cyclic span under the adjoint jumps and Q. Its exact dual
jump-count solve gives uniform-input mean

    56244663196079466 / 36544212499516385.

The worst initial mean is numerically 2.51224084755. The largest nonzero
Liouvillian real part is numerically -0.594108109916. These numerical values
are finite controls, not general rates. The exact four-state counterexample
and reused-probe return are checked separately. The local semigroup formula
agrees numerically to `4.18e-16`, whereas the three overlapping finite steps
at dt=0.2 differ from the combined semigroup by about 0.107742 in spectral norm.

Both final checkers pass and their complete stdout, empty stderr, result
files, and command receipts are preserved. Two cooling helper failures were
preserved: an attempted row replacement on a SymPy immutable matrix, and a
structural equality test on uncancelled rational expressions. The diagnosed
25 Poisson residuals all cancel to exact zero. Repairs change representation
and exact-zero evaluation only, without changing the model or tests. A first
readout run was explicitly interrupted at an expensive immutable-dense times
sparse Gauss commutator; the rerun uses consistent sparse matrices with all
original dimensions and full identities retained. Original scripts and streams
are preserved under `failed_attempts/`.

The proof is finite and component-specific. It gives no intercomponent
selection, phase theorem, native qubit/site implementation, universal memory
economy, thermodynamic relaxation rate, or robustness to additional generator
terms. Pure plaquette moves preserve divergence and the fixed matter-charge
sector; adding formation changes that problem and requires a separate argument.
It does not alter the preceding record model or resolve other quantum
interface questions. The author13 seal is still known only by the hash in
the brief; its contents and all new author artifacts remain unopened.

Reproduction: run `python3 readout_check.py` and `python3 cooling_check.py`
from this packet, retaining its geometry input. `DEPENDENCIES.json` and
`PRE_COMPARISON_SEAL.json` bind the exact sources and evidence. No primary
file, earlier independent seal, Git state, or audit record was changed.
