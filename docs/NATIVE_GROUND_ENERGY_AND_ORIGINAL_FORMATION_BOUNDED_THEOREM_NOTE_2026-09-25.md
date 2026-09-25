---
claim_id: native_ground_energy_and_original_formation_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Conditional finite-volume mathematics of the supplied common rotor model and original formation instrument; no physically selected vacuum, finite-spin energy theorem, fitted prediction or empirical confirmation."
upstream_dependencies:
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24
runner: scripts/native_ground_energy_and_original_formation_2026_09_25.py
---

**Type:** bounded_theorem
**Status:** conditional mathematics, selectively checked; no retained audit status.

# Native ground energy and original formation

The supplied model's empty-record reference cannot be identified with a
stable energetic vacuum by assertion. On fixed degree-six cubic tori in
the stated weak-coupling regime, a sector with an actual newly formed pair
has a lower leading spectral edge, global energy minimization requires an
extensive population of records, and globally near-ground states must still
form records under the original dynamics. These are constraints on that
identification, not a claim about the measured vacuum or all possible models.

The complete arguments below keep the vacancy-gated electric operator,
physical Gauss law, all color and winding sectors, and the supplied resolved
or unnormalized coherent formation instrument. A localized cycle-angle trial
is a variational comparison; it does not replace an actual incoming state's
harmonic-angle distribution. Hamiltonian evolution preserves record number,
so a lower sector energy does not imply spontaneous unitary creation.

The root personally derived all three source arguments. Each has a separate
sealed blind PRE and a released-source POST. Their scopes differ. The
one-pair checker reconstructs leading spectral/support statements and exact
local bounds; equality of the full finite-coupling cyclic and sector infima
is not asserted. The filling checker reconstructs the finite incidence and
variational logic, adding its own sharper rectangular-volume result in PRE.
The activity checker's blind PRE uses a distinct affine operator inequality;
its POST separately reconstructs the author's phase-deficit argument and all
72 stored primitive columns after author access. These are not multiple
independent derivations of every part. No retained-grade authority follows.

Part III's two provisional filling imports are proved explicitly in Part II
and have that part's separate scoped PRE/POST. Their joint use remains
conditional on the same supplied model and fixed-graph limits; neither an
audit verdict nor an independently checked physical premise is imported.
Independent-only stronger constants and counterexamples retain their PRE
provenance in the accompanying evidence rather than being attributed to the
root derivations. The exact source histories and earlier status wording are
preserved unmodified in the evidence packet.

The source arguments use two normalizations of the positive path matrix:

| Part | Positive operator convention | Physical fourth-order Hamiltonian |
|---|---|---|
| I: one-pair spectrum | Colored/occupation matrix includes twice each pair Gram | H4 is minus that matrix |
| II: filling | Q is the sum of unordered overlapping pair Grams | H4 = -2 Q |
| III: activity | Same Q as Part II | H4 = -2 Q |

There is no change of Hamiltonian between the parts. With n=|A|, the empty
sector has positive row 642n in Part I and 321n in Parts II/III. Every energy
and rate formula below uses the displayed convention of its own argument.
The common parameterization K=g^2/(2 tau), delta=1/(4 tau g^2) is supplied;
no observed length, time, mass, temperature or coupling is fitted here.


## Part I — actual birth support and the one-pair edge

### Actual formation outputs reach a lower matter-sector spectral edge

Personally derived conditional result, September 25, 2026. Sealed PRE and
released-source POST support the scoped mathematics; no retained audit status.

This note tests a missing physical identification: whether the supplied model's
all-A-plus/B-empty reference sector can be its energy vacuum when the original
instrument forms matter. The answer below concerns the full common rotor
Hamiltonian and actual resolved birth outputs. It does not identify a particle
mass, select physical units or replace the finite-spin fast Hamiltonian by this
effective energy observable without an additional energy-convergence theorem.

#### 1. Model, spectral objects and result

Use exactly the original supplied tensor-product hard-core records, integer
rotor links, Gauss law div E=q-1_A, all-A-occupied space P and formation marks

    B_(a,b,sigma) = P j_(a,b,sigma) F_a P.

The unsigned outward sums F_a commute on different A centers. Keep every matter
component and every electric winding. The full common Hamiltonian is

    h_g = g² D/(2 tau) + H4/(4 tau g²), tau>0,
    D = sum_(a->b) 1_(q_b=0) E_ab(E_ab-q_a) >= 0,
    H4 = -2 sum_(unordered overlapping A pairs a,c) S_ac* S_ac,
    S_ac = F_c F_a P.                                      (1)

These are supplied model premises. There is no field-only postbirth dynamics,
new number-sector offset, altered exchange algebra or new axiom. The original
full fast spin generator remains a different spectral object; convergence of
its finite-time records does not by itself prove convergence of energy spectra.

Let N0=|A|. Write e_n(g)=inf spec(h_g restricted to record number n). An infimum
is used: no normalizable ground eigenvector or compact-resolvent assertion is
needed for the possibly degenerate postbirth electric operator. For a normalized
state psi define its cyclic energy edge

    c_psi(g) = inf support of <psi,1_(dE)(h_g)psi>.

Take an even cubic torus of side L>=10. At each FIXED L and tau, the limit

    Delta_L = lim_(g->0) g² tau [e_(N0+2)(g)-e_N0(g)]       (2)

exists and satisfies the static bounds

                     -3062 <= Delta_L <= -2878.           (3)

Let phi be one all-A-plus/B-empty electric basis state with fixed, finite,
divergence-free integer E. Let psi=B_(a,b,sigma)phi/||B_(a,b,sigma)phi|| for
any original resolved sign and edge. Its norm is nonzero on this graph.
The SAME leading edges are present in these actual input/output spectral laws:

    lim g² tau c_phi(g) = lim g² tau e_N0(g),
    lim g² tau c_psi(g) = lim g² tau e_(N0+2)(g).            (4)

This is a statement about support near a spectral edge. It is not a probability
atom at the edge, a narrow birth-energy line, a typical event energy or the
mean energy change. The input is a fixed electric basis state, not the previous
g-dependent reference oscillator packet. No uniform-in-volume error follows.

The simple degree-three cube has a different exact leading difference, +5/2.
It is preserved below as a geometry-dependent counterexample to extending the
negative cubic degree-six claim to every graph.

#### 2. Full physical space and flat magnetic minimum

For each allowed matter word choose a fixed integer spanning-tree flow with
divergence q-1_A. Any other flow differs by an integer cycle. Fundamental cycles
of a spanning tree are an integral basis, so Fourier transform identifies that
word's field space with L² of a beta-dimensional torus, beta=|E|-|V|+1. This
includes the harmonic cycles; it does not set their initial state to zero angle.

At fixed record number, H4 is a finite Hermitian matter matrix M_n(theta) of
Laurent polynomials in these cycle variables. Each entry of -M_n is a sum of
path phases with nonnegative integer coefficients. Thus for every complex v,

    <v,M_n(theta)v> >= <|v|,M_n(0)|v|>
                    >= lambda_n ||v||²,
    lambda_n = min spec M_n(0).                            (5)

Indeed each phased entry has modulus at most its sum at zero; the diagonal
inequality is included. The finite nonnegative symmetric matrix -M_n(0) has
a nonnegative eigenvector for its top eigenvalue, giving the second bound.
Since D>=0, h_g>=lambda_n/(4 tau g²) on the entire sector.

For the reverse asymptotic bound choose such a real normalized eigenvector u
and a smooth normalized even packet f_g(theta), supported in one chart around
zero with width proportional to g in ALL cycle directions. Use the finite
fixed Gauss flows in each component. This is a variational trial, not a claim
that the original instrument prepares it. Its derivatives have norms O(g^-1),
so <u f_g,D u f_g>=O(g^-2). The scalar u* M_n(theta)u is real and even; its
linear term vanishes. Its expectation is lambda_n+O(g²). Therefore

    e_n(g) <= lambda_n/(4 tau g²) + O_L(1/tau),
    lim g² tau e_n(g) = lambda_n/4.                        (6)

All these vectors are in the electric form domain (in fact smooth). An initial
harmonic-angle Haar state was not replaced by this variational packet. The
trial supplies an upper bound on a spectral infimum only. On a tree beta=0,
the same statement uses the finite matter vector and its fixed integer flow.

At N0 the unique matter word is all A plus and B empty. On a generic degree-six
cubic torus (L>=6), the parent local formula gives

    lambda_N0 = -q0, q0=321 L³.                            (7)

To count directly: 3L³/2 overlapping A pairs have one common B neighbor and
3L³ have two. For degree z and common-neighbor count r the flat outgoing Gram
contribution is 2[z²+r²-2r]; it is 70 for r=1 and 72 for r=2. This gives (7).

#### 3. Exact one-minus reduction, with all matter retained

Global Gauss fixes total charge N0. In sector N0+2 there are exactly two
occupied B sites, a pair X, and exactly one minus among the N0+2 occupied sites.
For each X let its color space contain all N0+2 possible locations of that minus.

At theta=0 each allowed outward-outward-return-return path bijects the occupied
sites of its input and output. On the single-minus color spaces it is a
permutation matrix. This uses the unsigned tensor-product hard-core algebra;
there is no unmentioned fermionic exchange sign. Let Q be the nonnegative
matrix on B occupancy pairs formed by counting these paths with coefficient 2.

For a full color vector v, put w_X=||v_X||. Each permutation has norm one, so

    <v,-M_(N0+2)(0)v> <= <w,Qw> <= rho(Q)||v||².            (8)

Conversely, embed an occupancy vector as a vector uniform over all minus
locations at every X, with normalization 1/sqrt(N0+2). Every path preserves
this uniform vector, so the embedding intertwines Q and -M_(N0+2)(0). Hence

                   lambda_(N0+2) = -rho(Q).               (9)

This proves equality of the spectral bottoms, not equality of the whole color
spectrum or deletion of matter dynamics. In particular it is sufficient for
(2), while the actual formation vector generally has nonuniform minus location.

For an overlapping A pair (a,c), define for an unordered distinct B pair d

    m_ac({u,v}) = 1_(u in N(a), v in N(c))
                +1_(v in N(a), u in N(c)).

Starting at X, an outward pair d disjoint from X gives Y=X union d with amplitude
m_ac(d). Returning via d' subset Y leaves X'=Y minus d' and contributes
2 m_ac(d)m_ac(d') to Q_(X',X). This includes returns of previously occupied B
records and their colors; keeping only the outgoing pair's reverse would miss
the large off-diagonal contribution. If X misses both neighbor stars, the
contribution is only the vacuum scalar on X. Local subtraction thus computes
R=Q-q0 I from finitely many A pairs near the two occupied B sites.

#### 4. Exact row polynomial and static bound for every L>=10

For one overlapping A pair let z=6, r=|N(a) intersect N(c)|, and let
sa=|X intersect N(a)|, sc=|X intersect N(c)|, t=|X intersect N(a) intersect N(c)|.
Set na=z-sa, nc=z-sc, ni=r-t and J=na nc-ni. Its contribution to the row sum
of R is the integer polynomial

    T(r,sa,sc,t) = 2 { J[(sa+1)(sc+1)-t]
                    +sa ni(nc-1)+sc ni(na-1)+ni(ni-1)
                    -(z²+r²-2r) }.                       (10)

Derivation: sum over ordered outward u in N(a) minus X, v in N(c) minus X,
u!=v. The number of return assignments within Y=X union {u,v} is
|Y intersect N(a)| |Y intersect N(c)|-|Y intersect N(a) intersect N(c)|.
Writing x=1_(u in N(c)), y=1_(v in N(a)), this is
(sa+1)(sc+1)-t+sa x+sc y+xy. The four sums of 1,x,y,xy over outward
assignments are respectively J, ni(nc-1), ni(na-1), ni(ni-1).
Subtract the vacuum squared-multiplicity sum to obtain (10).

For an isolated occupied B site the four possible active A-pair types have
the following counts. They are abstract local contributions to a physical
two-B row, not an adopted odd-charge physical sector.

| r | (sa,sc,t), up to interchange | Count | T |
|---|---|---:|---:|
| 1 | (0,1,0) | 30 | 56 |
| 1 | (1,1,1) | 3 | 80 |
| 2 | (0,1,0) | 48 | 64 |
| 2 | (1,1,1) | 12 | 88 |

The sum is 6048. For example the six A neighbors each have six axial second
neighbors and twelve face-diagonal second neighbors. Their double incidences
are respectively the 3 opposite and 12 nonopposite pairs among those six A
neighbors. This gives exactly the four counts in the table.

Two occupied B sites farther than four graph steps cannot lie in the same
two-star union, so their total row sum is 12096. If they are nearer, cubic
symmetry leaves exactly six nonzero even-parity displacement types. Applying
(10) only to A pairs touching both gives:

| Absolute sorted displacement | Number of oriented displacements | Common A pairs | Correction to 12096 | Row sum |
|---|---:|---:|---:|---:|
| (0,0,2) | 6 | 22 | -196 | 11900 |
| (0,1,1) | 12 | 37 | -584 | 11512 |
| (0,0,4) | 6 | 1 | 26 | 12122 |
| (0,1,3) | 24 | 3 | 72 | 12168 |
| (0,2,2) | 12 | 4 | 92 | 12188 |
| (1,1,2) | 24 | 7 | 152 | 12248 |

The retained certificate gives all constituent counts indexed by
(r,min(sa,sc),max(sa,sc),t), their integer per-pair corrections and their sums.
It checks (10) against 180 exhaustive finite local occupancy cases and the
separate direct path enumeration for all 84 near displacements and four far
controls. No floating eigenvalue supplies a sign in this bound.

For L>=10 a radius-four local coordinate patch has no periodic identification,
and a displacement of length at most four has no second periodic image in that
patch. The above single-site and common-pair counts therefore apply to every
two-B configuration on the torus. If the torus distance is greater than four,
the far case applies. This argument concerns row sums; distinct final targets
may share a translation orbit without changing the sum. It gives

    11512 <= sum_Y R_(X,Y) <= 12248  for every X.           (11)

For a nonnegative finite matrix Q the spectral radius lies between its minimum
and maximum row sums: apply Q to the positive constant vector, or iterate the
two componentwise inequalities. Thus

    q0+11512 <= rho(Q) <= q0+12248.                        (12)

Equations (6), (7), (9) and (12) prove (2)--(3). The constants are static and
independent of L, while the passage g->0 is still at each fixed graph.

#### 5. The edge is in the actual birth's cyclic spectrum

First, the flat magnetic bottom has a strictly positive matter vector on these
cubic graphs. For any occupied B site b, another occupied B site x and an empty
B target d sharing an A neighbor a with b, choose a second A neighbor c of b,
c!=a. Choose e in N(c) outside {b,d,x}; degree six leaves such choices. The
four-hop path a->d, c->e, e->c, b->a is allowed and has positive coefficient.
It implements the occupancy move {b,x}->{d,x} in Q.

The B graph of two-step moves through A is connected. The graph of unordered
two-site occupancies on a connected graph is also connected: on a spanning
tree, bring the nearest vacancy to a chosen leaf by successive allowed slides,
then induct on the tree with that leaf removed. If two configurations disagree
on the leaf, first clear it in the occupied one and use the same induction;
reverse that path when needed. This proves connectivity for every particle
number strictly between zero and the vertex count, including two here.
Consequently Q is irreducible and has a strictly positive Perron vector.
Its uniform-minus embedding is a strictly positive ground vector of M_(N0+2)(0).

For the actual birth of a fixed electric basis state, the Fourier vector
psi(theta) is a finite Laurent vector. At theta=0 its nonzero entries all have
the same sign (an overall phase is irrelevant), because the original resolved
hop and creation amplitudes are unsigned. It therefore overlaps the positive
flat ground vector. For any eta>0 choose a nonnegative continuous function f
supported in (lambda_(N0+2)-eta,lambda_(N0+2)+eta), with f(lambda_(N0+2))>0.
The continuous function

    psi(theta)* f(M_(N0+2)(theta)) psi(theta)

is positive at zero, hence positive on a set of nonzero Haar measure. Its
integral is positive. Equation (5) then proves that the H4 spectral measure
of this actual state has lower edge lambda_(N0+2). The same argument in the
unique N0 matter component applies to the initial electric basis state.

It remains to keep D in the actual energy rather than substituting H4 for it.
Put A_s=H4+sD, s=2g^4, so A_s=4 tau g² h_g. On any fixed finite-electric-support
vector psi, every power A_s^k psi has finite support independent of s. This is
because D is diagonal and H4 is a bounded finite sum of finite integer shifts
and finite matter transitions. Each moment is therefore a polynomial in s,
and as s->0 it tends to the corresponding H4 moment.

For completeness, this implies weak convergence of the spectral measures
without interchanging an unbounded energy operator with a density limit. The
uniform second-moment bound makes the measures tight. Uniform higher even
moments give uniform integrability for each lower moment, so every weak limit
has all the moments of the bounded H4 measure. Its even-moment bounds force
support inside [-||H4||,||H4||]: any positive mass outside a larger interval
would contradict the bounds at sufficiently high even order. On this compact
interval polynomials determine the measure by uniform approximation. Hence
the entire family converges weakly to the H4 measure.

The positive continuous test f above consequently has positive expectation
also for A_s at every sufficiently small s. Thus the actual A_s spectral
support reaches below lambda_n+eta. The operator bound A_s>=lambda_n supplies
the reverse edge bound. Let eta->0 to prove (4). This includes the original
electric gates and all matter transitions throughout; there is no postbirth
projection to a field sector and no microscopic time-derivative interchange.

Only fixed finite-electric-support inputs are covered by this argument. It
does not establish these relative spectral weights for a g-dependent weak-field
packet, high-flux scaling family, delivered photon or finite-spin birth. It
also supplies neither a rate of weak convergence nor a nonvanishing atom at
the lower edge.

#### 6. Exact finite controls and geometry counterexample

The root enumerates all 36 one-minus matter states of the simple degree-three
cube and builds -H4 by a direct S* S construction. Its positive matrix has
constant row sum 98. The six-state occupancy matrix has the same row sum and
intertwines with the full matrix by the integer uniform-minus embedding.
The initial flat value is -108. Thus the cube has leading difference
(-98+108)/4=5/2, not the negative large-torus bound. Its positive full constant
ground vector also gives the actual-birth overlap used in Section 5.

For even cubic tori, translation-invariant nonnegative ground vectors exist
by averaging a Perron vector. Occupancy-pair orbits are nonzero even-parity
displacements modulo d~-d. Generic orbit size is |B|; self-inverse displacements
have size |B|/2. The integer quotient Rbar obeys w_i Rbar_ij=w_j Rbar_ji.
The corresponding symmetric matrix is diag(sqrt(w)) Rbar diag(1/sqrt(w)).

The root's floating eigensolver only proposes a positive integer vector v.
Adding a recorded scalar C makes Rbar+C I nonnegative. Exact rational minimum
and maximum of ((Rbar+C I)v)_i/v_i enclose its Perron eigenvalue; subtract C
and divide by -4 for the leading gap interval. All integer rows and vectors
are retained. Selected outward-rounded decimal summaries are:

| Side | Quotient dimension | Leading difference interval, g² tau units |
|---|---:|---|
| 2, simple cube | 3 | exactly 2.5 |
| 4 | 19 | (-2560.193783122, -2560.193783119) |
| 6 | 55 | (-3021.430258607, -3021.430258602) |
| 8 | 131 | (-3022.937153603, -3022.937153598) |

The exact fractions, not these decimal renderings, define the certificates.
L=4 has vacuum flat value -270 L³ because its axial second neighbors wrap;
the source code checks that exception. L=6 and L=8 have further wrapped
interaction row sums and are not used to justify the L>=10 local-patch proof.
No extrapolated L->infinity number or many-pair spectrum is claimed.

#### 7. Physical meaning and scope stress test

Within (1), for every fixed cubic L>=10 and sufficiently small g, the N0+2
sector extends below the N0 sector. Actual original resolved births from the
declared basis inputs have energy spectral support reaching that lower edge
at leading order. The N0 sector therefore cannot be the global energy-ground
sector in this regime. This is a substantive obstruction to identifying that
particular reference as the physical vacuum of the supplied Hamiltonian.
The isolated Hamiltonian conserves N, so the cross-sector inequality does not
prove spontaneous unitary decay. The original birth law changes N; assigning
its energy exchange to an autonomous reservoir remains a separate obligation.

N1: the claim is restricted to (1), fixed L/tau, the stated sectors and the
specified input class. N2: other states, physical vacua, parameter regimes,
graphs and differently supplied Hamiltonians remain possible. The cube's
opposite sign is retained. A number-dependent energy offset would alter this
comparison and is not adopted. N3: the compensated Hamiltonian, signs and
quantum kinematics are premises, not derived axioms or measured parameters.
N4: the full Gauss space, electric gates and actual output cyclic support are
checked; a selected probe expectation is not substituted for the sector edge.
N5: exact integer and rational controls support finite combinatorics, while
the operator and moment arguments bear the limiting claim. Independent review
is still required. N6: an energy floor is not a stable particle, a selected
line, a typical output, heat, work or a stationary source. The true selected
many-matter state and its excitation spectrum remain open. N7: the strongest
alternative is that the physically appropriate vacuum lies in another sector
or regime; that is a further derivation, not evidence supplied here. N8: prior
reference-wave and detector formulas retain their conditional mathematical
scope. Their identification with real light or real detectors cannot be
promoted by this result, and needs reconsideration of the physical vacuum.

No observed mass, astronomical constraint, laboratory event rate, empirical
agreement/exclusion, energy-conserving microscopic completion or TOE completion
is inferred. This is progress on a missing prerequisite to observation, not
the completed observation bridge.

## Part II — necessary population at the global energy minimum

### Native ground-sector filling in the supplied common Hamiltonian

Personally derived conditional result, 2026-09-25. Scoped PRE and POST are complete.
This is conditional mathematics about the supplied compensated model. It
does not select the physical vacuum or identify an observed particle.

#### Premises and provenance

Use an even cubic torus of side \(L\ge6\), with nearest-neighbour bipartition
\(A\cup B\), \(n=|A|=|B|=L^3/2\), integer rotor electric fields, the original
unsigned tensor hard-core matter, and Gauss law
\(\operatorname{div}E=q-\mathbf1_A\). The \(P\) space has every \(A\) site
occupied by a charge \(q_a=\pm1\), and each \(B\) site empty or occupied by
\(\pm1\). Keep the full original formation channels and every output sector.

The load-bearing main sources are the local-pair/general-graph magnetic
dynamics and local-compensation common-field-record limit notes, pinned in
SOURCE_PINS.json. Their supplied Hamiltonian is
\[
h_g=\frac{g^2}{2\tau}D+\frac{1}{4\tau g^2}H_4,\qquad
D=\sum_{a\to b}\mathbf1_{\{q_b=0\}}E_{ab}(E_{ab}-q_a),\qquad
H_4=-2\sum_{\{a,c\}}(F_cF_aP)^*F_cF_aP.                 \tag{1}
\]
The sum is over distinct overlapping \(A\) stars. Fix \(\tau>0\), then take
\(g\downarrow0\) at fixed \(L\). The empty-\(B\) gate in \(D\) is essential;
no field-only replacement is made. On the electric basis \(D\ge0\), because
each integer \(e\) obeys \(e(e-1)\ge0\) and \(e(e+1)\ge0\).

The earlier personally derived one-pair calculation supplied a local row
polynomial. The independently reconstructed PRE for that calculation, read
before this extension, supplied a general two-particle uniform trial. These
motivated asking about arbitrary occupancy. This note proves its general
occupancy identities and estimates explicitly; the earlier work is
provisional context, not a retained audit or an independent check of this
extension. This convention uses \(H_4=-2Q\) in the occupation representation,
as in that PRE; the earlier root's \(Q\) was twice this \(Q\).

#### Claim

Let \(m\) be the number of occupied \(B\) sites. A physical \(P\) sector has
\[
N=n+m,\qquad m\in\{0,2,\ldots,n\},\qquad
\#\{\hbox{minus charges}\}=m/2.                         \tag{2}
\]
Let \(e_m(g)\) be the spectral infimum of (1) in this sector, over all
allowed charge assignments and electric flows. For every fixed even
\(L\ge6\), there is \(g_0(L,\tau)>0\) such that, for \(0<g<g_0\), every
sector satisfying \(e_m(g)=\min_k e_k(g)\) obeys
\[
\boxed{\quad \frac{421}{2640}<\frac mn<
                    \frac{4103}{6008}\quad}             \tag{3}
\]
(approximately \(0.1594697<m/n<0.6829228\)).

The finite set of sectors has at least one minimizing spectral infimum.
This does not assert a normalizable ground eigenvector. The bound proves
that both occupied and vacant \(B\) sites have a finite fraction in any
energetically minimizing sector of this specified regime. The threshold
is not uniform in \(L\); there is no fixed-\(g\) thermodynamic conclusion.

#### Physical color space and occupation representation

Summing Gauss law gives total charge \(n\), proving (2). Conversely every
assignment satisfying (2) admits an integer Gauss flow: route its
zero-total divergence along a spanning tree. For each matter word choose
one such flow. All other flows are an affine integer cycle lattice. Fourier
transformation in the full cycle lattice, including harmonic winding
directions, gives a finite matter matrix for \(H_4\) at each angle \(\theta\).

Every legal four-hop path in (1) moves occupied charge slots bijectively:
two distinct \(A\) charges leave for vacant \(B\) sites, and two occupied
\(B\) charges return to the vacant \(A\) sites. The returning charges may
be pre-existing records. Allowedness depends on occupancy, not charge sign.
At \(\theta=0\), every path has a positive integer coefficient. For a
fixed occupied set \(X\subset B\), \(|X|=m\), there are exactly
\(\binom{n+m}{m/2}\) allowed minus assignments, independent of \(X\).
Their normalized uniform sum gives an isometry \(J_m\) from occupation
space into the full color space.

Write the full magnetic matrix as \(-2K_m(\theta)\). The path bijections
give \(K_m(0)J_m=J_mQ_m\). Here \(Q_m\) is a Gram matrix of auxiliary
unordered-pair creation maps on \(m\)-element subsets of \(B\).
This is only a combinatorial representation of the Hamiltonian.
It does not replace the physical matter or formation instrument.
Full colored row sums equal occupation row sums, independently of the
minus assignment. Moreover
\[
|K_m(\theta)_{\eta\xi}|\le K_m(0)_{\eta\xi}.
\]
For any vector, the quadratic-form modulus bound and the symmetric
nonnegative row-sum bound therefore give
\[
\lambda_{\max}(K_m(\theta))
 \le\max_X\operatorname{rowsum}_X Q_m.                  \tag{4}
\]
No irreducibility or full color-spectrum reduction is needed here.

#### Uniform-occupation trial

For one overlapping pair of \(A\) stars, define
\[
w(D)=\#\{(b,d):b\in N(a),\,d\in N(c),\,b\ne d,\,
                         \{b,d\}=D\}.
\]
If \(u_m=\binom nm^{-1/2}\sum_{|X|=m}|X\rangle\), the pair-creation map
has amplitude \(\binom nm^{-1/2}\sum_{D\subset R}w(D)\) at an intermediate
set \(R\) of size \(m+2\). Squaring and summing over \(R\) gives three
terms, according to whether \(D,D'\) coincide, share one site, or are
disjoint. With ordered pairs \(D,D'\), define
\[
v=\sum_Dw(D)^2,\quad
a=\sum_{|D\cap D'|=1}w(D)w(D'),\quad
d=\sum_{D\cap D'=\varnothing}w(D)w(D').
\]
The contribution is exactly
\[
\frac{v\binom{n-2}{m}+a\binom{n-3}{m-1}
                    +d\binom{n-4}{m-2}}{\binom nm}.     \tag{5}
\]
Binomial coefficients outside their range are zero.

For two degree-six stars with overlap \(r=1,2\), the total weight is
\(36-r\). Each common vertex has weighted incidence 10 and each exclusive
vertex incidence 6. Thus
\[
v=36+r^2-2r,\quad
a=100r+36(12-2r)-2v,\quad d=(36-r)^2-v-a.
\]
For \(r=1\), these are \((35,390,800)\); for \(r=2\),
\((36,416,704)\). An even cubic torus \(L\ge6\) has \(3n\) overlap-one
pairs (axial displacement two) and \(6n\) overlap-two pairs (two unit
coordinate displacements). There are no side-four wrap coincidences.
Summing (5), put
\[
V=321n,\quad A=3666n,\quad D_4=6624n,\qquad
R_m=\langle u_m,Q_mu_m\rangle
 =\frac{V\binom{n-2}{m}+A\binom{n-3}{m-1}
                         +D_4\binom{n-4}{m-2}}{\binom nm}. \tag{6}
\]

Since \(n=4(L/2)^3\), \(m=n/2\) is an allowed even occupancy. Direct
rational simplification of (6) gives
\[
\begin{split}
\frac{R_{n/2}}n
 &=\frac{321(n-2)}{4(n-1)}
   +\frac{3666n}{8(n-1)}
   +\frac{414n(n-2)}{(n-1)(n-3)}\\
 &=\frac{1905}{2}+\frac{378}{n-1}
                  +\frac{414(2n-3)}{(n-1)(n-3)}
 >\frac{1905}{2}.                                      \tag{7}
\end{split}
\]
This is a variational quotient, not a computed Perron eigenvalue.

#### Uniform row bounds at arbitrary occupancy

For a fixed occupied set \(X\), define
\[
s_a=|X\cap N(a)|,\ s_c=|X\cap N(c)|,\ t=|X\cap N(a)\cap N(c)|,
\quad n_a=6-s_a,\ n_c=6-s_c,\ n_i=r-t.
\]
There are \(n_an_c-n_i\) legal ordered outward pairs. After an outward
pair \(b\in N(a)\setminus X,d\in N(c)\setminus X\), the return multiplicity
is
\[
(s_a+1+\mathbf1_{\{d\in N(a)\}})
(s_c+1+\mathbf1_{\{b\in N(c)\}})
-t-\mathbf1_{\{b\in N(c)\}}-\mathbf1_{\{d\in N(a)\}}.
\]
The subtraction excludes returning the same occupied \(B\) charge twice.
Summing this expression over distinct \(b,d\) gives the exact row polynomial
\[
P_r=(n_an_c-n_i)[(s_a+1)(s_c+1)-t]
       +s_an_i(n_c-1)+s_cn_i(n_a-1)+n_i(n_i-1).          \tag{8}
\]
The term with product of the two indicators counts distinct vacant
common neighbours. In particular, (8) retains all returns of old records.

Put \(\ell=s_a+s_c-t\), \(z=12-r-\ell\), the occupied and vacant sites in
the two-star union. The complete pattern set is
\[
0\le t\le r,\qquad 0\le s_a-t,s_c-t\le6-r.
\]
It has 72 patterns for \(r=1\) and 75 for \(r=2\). Substitution into (8)
gives the following exact maxima, excluding a zero denominator:

| overlap \(r\) | common occupancy \(t\) | patterns | maximum \((P_r-v)/\ell\) | maximum \(P_r/z\) |
|---|---|---|---|---|
| 1 | 0 | 36 | \(69/2\) | \(28\) |
| 1 | 1 | 36 | \(40\) | \(24\) |
| 2 | 0 | 25 | \(37\) | \(104/3\) |
| 2 | 1 | 25 | \(44\) | \(80/3\) |
| 2 | 2 | 25 | \(38\) | \(23\) |

When \(\ell=0\), \(P_r=v\); when \(z=0\), \(P_r=0\).
Thus the finite substitutions, also preserved individually in the exact
certificate, prove
\[
P_1\le35+40\ell,\quad P_2\le36+44\ell,\qquad
P_1\le28z,\quad P_2\le(104/3)z.                         \tag{9}
\]
This is a finite exhaustive proof with explicit domain, not a
floating-point search. The source program also compares (8) to direct
intermediate-set Gram counting for every one of the \(2^{11}+2^{10}=3072\)
local occupied subsets; the two calculations have distinct counting forms.
This root control is not an independent review.

Translation transitivity on \(B\), the pair counts above, and union sizes
11 and 10 show that every \(B\) site belongs to exactly 33 overlap-one
and 60 overlap-two unions. Hence
\[
\max_X\operatorname{rowsum}_XQ_m
 \le B_m:=\min\{321n+3960m,\;3004(n-m)\}.                \tag{10}
\]
The coefficients are \(33(40)+60(44)=3960\) and
\(33(28)+60(104/3)=3004\). Equations (4), (10) and \(D\ge0\) imply
\[
e_m(g)\ge-\frac{B_m}{2\tau g^2}.                       \tag{11}
\]

#### Physical variational comparison and proof of (3)

The occupation-color vector \(J_{n/2}u_{n/2}\) at zero angle is not a
normalizable rotor state. Multiply it by a normalized smooth real even
bump \(\phi_g\), supported in a width-\(g\) chart about zero in all cycle
angles. This is a legitimate Gauss-compatible finite-graph trial.
Every chosen reference flow is finite, every relevant cycle shift is finite,
and the matter fiber is finite. In this representation each electric
operator is an affine first derivative. Therefore
\[
\langle D\rangle_{\phi_gJ u}=O_L(g^{-2}).
\]
The finite Laurent magnetic matrix is analytic in the angles. Its scalar
expectation in the real vector \(Ju\) is even in \(\theta\), so
\[
\langle K\rangle_{\phi_gJ u}=R_{n/2}+O_L(g^2).
\]
The trial belongs to the electric operator domain. Substitution in (1)
gives, at fixed \(\tau\),
\[
e_{n/2}(g)\le-\frac{R_{n/2}}{2\tau g^2}+C_{L,\tau},     \tag{12}
\]
for a finite constant independent of sufficiently small \(g\).
Localizing harmonic angles is permitted for this variational comparison;
it is not an assertion about the initial zero-electric-winding state,
whose harmonic-angle distribution is Haar.

If \(m/n\le421/2640\), the first bound in (10) is at most
\((1905/2)n\). If \(m/n\ge4103/6008\), the second bound is at most the
same quantity. Equation (7) leaves a strictly positive gap
\(R_{n/2}-(1905/2)n\) for every fixed graph. For sufficiently small \(g\),
this gap divided by \(2\tau g^2\) exceeds the finite error in (12).
Equations (11) and (12) then imply \(e_m(g)>e_{n/2}(g)\) in either
excluded range, proving (3), including strict endpoint exclusion.

#### Exact controls and scope

The root program and complete output verify all 147 pattern rows with their
multiplicities, all 3072 local subsets, 26 uniform-occupancy averages for
artificial 12-site ambient sets, and the actual torus geometry for
\(L=6,8,10,12\). The artificial ambient sets check (5); they are not
physical torus simulations. Seven even occupancies per torus check (6),
(7), (10), including zero and full occupancy. These are not full many-body
diagonalizations. Timers, exact fractions and source hashes are preserved.
No scientific numerical failure occurred in this control. The unsealed
working derivation is retained verbatim, including a typographical artifact.

#### Consequence for the observational bridge

If a physical identification requires the energy-minimizing vacuum of
(1), the empty sector cannot be repaired merely by adding a fixed small
number of pairs in this fixed-graph small-\(g\) regime. A collective
matter-field sector with appreciable records and vacancies must be treated
before assigning its excitation energies to observed particles.

The conditional premise is not adopted here. A prepared metastable sector
can be physically relevant without minimizing the entire Hamiltonian.
The original unitary dynamics conserves \(N\), while the formation channels
raise it; neither (3) nor a lower energy proves spontaneous unitary decay,
relaxation to the minimum, or a stationary source. No reservoir, physical
scale, laboratory vacuum, photon absorption, observed mass or empirical
exclusion is established. A selected nonequilibrium preparation and a
justified observation functional remain alternative routes.

#### No-Go Discipline Gate — bounded claim audit

- N1, alternatives: retain the original model and distinguish a selected
  metastable preparation, a different supplied Hamiltonian, and the
  global spectral minimum. Only the last is constrained by (3).
- N2, wall independence: this estimate concerns number-sector energetics.
  It does not strengthen count identifiability or optical calibration
  bounds merely because those also leave observation work open.
- N3, hidden assumptions: even \(L\ge6\), exact degree six, unsigned
  hard-core paths, full Gauss/color/cycle space, the actual gated \(D\),
  and fixed graph before small \(g\) are explicit.
- N4, residual matching: all sectors use the same \(g,\tau\), Hamiltonian
  and zero of energy. No number-dependent energy offset is introduced.
  A finite variational \(O_L(1)\) remainder is beaten at each fixed graph;
  no uniform macroscopic error is asserted.
- N5, resolution: per-element and local-pattern counting is exact; all
  sites of four finite tori are checked for incidence. No full energy
  spectrum, fast-generator spectrum, large-volume convergence or
  experimental dataset is executed by this runner.
- N6, partial closure: (3) bounds possible minimizing sectors but does
  not identify their phases, degeneracy, excitations or dynamics.
- N7, strongest alternative: an observed vacuum or detector could be a
  stable prepared or driven state in a conserved-number sector. The
  present proof does not exclude that identification; its preparation,
  stability and response would still need derivation.
- N8, prior-result boundary: the previous one-pair edge is not counted
  as another independent reason. The new content is the arbitrary
  occupancy average, two all-occupancy row bounds and their finite
  fraction consequence. No framework no-go or TOE completion follows.

## Part III — energy versus original formation activity

### Ground energy and original formation activity in the supplied common law

Personally derived conditional result, 2026-09-25. Scoped PRE and POST are complete.
This conditional result addresses a necessary choice in the observational
bridge: whether the global Hamiltonian minimum can be identified with a
stationary vacuum of the same original formation dynamics. No such physical
identification is assumed or established here.

#### Premises, domains and provisional dependency

Fix an even cubic torus of side \(L\ge6\), with
\(n=|A|=|B|=L^3/2\). Use the unsigned tensor hard-core matter, integer
rotor electric fields, and full physical Gauss space
\(\operatorname{div}E=q-\mathbf1_A\). In \(P\), every \(A\) site is
occupied with charge \(\pm1\), while each \(B\) site is empty or occupied
with either sign. All matter sectors and electric windings are retained.
If \(m\) is the number of occupied \(B\) sites, then
\(N=n+m\), \(m\) is even, and the total number of minus charges is
\(m/2\). Each such charge assignment has integer Gauss flows.

The three pinned main sources supply the original formation instrument,
the local-compensated common Hamiltonian, and formation balance. Write
\[
h=KD-2\delta Q,\qquad
D=\sum_{a\to b}\mathbf1_{\{q_b=0\}}E_{ab}(E_{ab}-q_a),\qquad
Q=\sum_{\substack{a<c\\N(a)\cap N(c)\ne\varnothing}}Q_{ac},\quad
Q_{ac}=(F_cF_aP)^*F_cF_aP.                         \tag{1}
\]
Here \(K,\delta,\kappa>0\), and \(F_a\) moves the charge at \(a\)
out to any empty neighbouring \(B\) site, with its exact rotor shift.
Distinct outward star maps commute. The sum in (1) is only over overlapping
stars; distant pairs are not added. On the physical electric basis, \(D\)
is diagonal and nonnegative. The integer identities
\(e(e-1)\ge0\) and \(e(e+1)\ge0\) apply on every retained edge.
The empty-\(B\) gate is not removed.

The resolved channels are
\[
L_{ab,\sigma}=\sqrt\kappa\,Pj_{ab,\sigma}F_aP,
\qquad\sigma=\pm1.                                  \tag{2}
\]
We also cover the specified **unnormalized** coherent edge channel
\(L_{ab,+}+L_{ab,-}\). An independently rescaled coherent channel is a
different convention and is not silently included. Define the total
formation intensity operator
\[
\Gamma=\sum_jL_j^*L_j.                              \tag{3}
\]
The operators \(Q\) and \(\Gamma\) are bounded on each fixed finite
graph, and preserve \(N\). The Hamiltonian is the self-adjoint operator
\(KD\) plus a bounded perturbation. Energy expectations below are its
lower-bounded quadratic-form expectations; finite energy is equivalent
to membership in the form domain of \(D\). For normal densities the
corresponding condition is \(\operatorname{Tr}(D\rho)<\infty\).
The notation uses the Hamiltonian's existing units, with no laboratory
energy calibration or reservoir interpretation.

The sector result below follows directly from (1)--(3). The global result
additionally uses exactly two estimates from the sealed, provisional
personal ground-filling note, explicitly restated in (13). That note's
independent PRE was sealed and its summary reached the root before the
present final seal, but its proof and code have not been read or used for
this derivation. The working derivation and successful primitive controls
preceded that summary; the constants in (13) are the original personal
constants, not the stronger bounds reported in the independent summary.
The separate PRE and POST scopes are recorded in the publication overview;
the earlier exposure chronology remains part of the sealed source history.

#### Results

Let \(e_m=\inf\operatorname{spec}(h|_{N=n+m})\). Every normalized
finite-energy state in this sector, pure or mixed, obeys
\[
\boxed{\displaystyle
\langle\Gamma\rangle\ge
4\kappa(5n-6m)-\frac{4\kappa}{5\delta}
                    (\langle h\rangle-e_m).}          \tag{4}
\]
This holds for all positive \(K,\delta,\kappa\). Its lower bound is
useful only where its right side is positive. In particular, any
formation-dark finite-energy state with \(m<5n/6\) must be at least
\(5\delta(5n-6m)\) above that sector's spectral infimum.

Let \(e_* = \min_m e_m\), the global Hamiltonian infimum. At each fixed
permitted torus, there exists \(\eta_0(L)>0\) such that for
\(0<K/\delta<\eta_0(L)\), every normalized finite-energy physical
state obeys
\[
\boxed{\displaystyle
\langle\Gamma\rangle\ge\frac{16}{5}\kappa n
 -\frac{4\kappa}{5\delta}(\langle h\rangle-e_*).}      \tag{5}
\]
This includes arbitrary mixtures and coherences between number sectors.
Consequently, in this regime,
\[
\langle\Gamma\rangle=0
\quad\Longrightarrow\quad
\langle h\rangle\ge e_*+4\delta n.                   \tag{6}
\]
Every normal stationary state of the original common dynamics is dark
by the existing formation-balance theorem. Thus any stationary state
with finite energy satisfies (6). A global ground eigenstate, if one
exists, cannot be stationary. The same obstruction applies to a sequence
approaching the ground infimum, without assuming the infimum is attained:
if \(\langle h\rangle-e_*\le2\delta n\), then
\(\langle\Gamma\rangle\ge8\kappa n/5\).

#### Exact primitive comparison

For an oriented edge \((a,b)\), let
\[
M_{ab}=PF_a^*\mathbf1_{\{q_b=0\}}F_aP.                \tag{7}
\]
After \(F_aP\), site \(a\) is empty. In the rotor basis a primitive
pair-creation jump has unit nonzero amplitude, and
\(j_{ab,\sigma}^*j_{ab,\sigma}
=\mathbf1_{\{q_a=0,q_b=0\}}\). The two sign outputs have opposite
created charges at \(a\), so
\(j_{ab,+}^*j_{ab,-}=j_{ab,-}^*j_{ab,+}=0\).
The outer \(P\) projections retain all these outputs. Therefore both
the resolved and specified coherent convention give the exact identity
\[
\Gamma=2\kappa\sum_{a,b\sim a}M_{ab}.                \tag{8}
\]

Use the full orthonormal charge/electric basis of the physical space.
All entries of \(F_a\), its adjoint, and the primitive jumps in that
basis are nonnegative real integers. Thus \(Q_{ac}\), \(M_{ab}\) and
\(\Gamma\) have nonnegative entries, including their electric shifts.
For any \(c\ne a\) adjacent to \(b\), consider the paths in
\(Q_{ac}\) in which \(F_c\) hops out along \((c,b)\) and
\(F_c^*\) returns along the same edge. The intermediate \(c\) charge
is occupied and unaffected by \(F_a\). The two rotor shifts cancel
exactly. This subset of the four-hop paths is precisely \(M_{ab}\).
All other paths have nonnegative entries. Hence
\[
(M_{ab})_{yx}\le(Q_{ac})_{yx}
\quad\hbox{for every physical pair of basis states }x,y.       \tag{9}
\]
For the analogous \(M_{cb}\) comparison, commute the two outward stars
and their adjoints. This keeps all return paths involving old records.

Each \(b\) has six \(A\) neighbours, and each pair of overlapping
stars has overlap \(r_{ac}\le2\) for the specified tori. Counting the
five other neighbours of each \((a,b)\) gives, entry by entry,
\[
5\sum_{a,b\sim a}M_{ab}
=\sum_{a<c}\sum_{b\in N(a)\cap N(c)}(M_{ab}+M_{cb})
\le\sum_{a<c}2r_{ac}Q_{ac}\le4Q.
\]
Combined with (8),
\[
\boxed{\quad\Gamma\le\frac{8\kappa}{5}Q
                       \quad\text{entrywise}.\quad} \tag{10}
\]
Equation (10) is **not** a Loewner-order inequality. It will only be used
on nonnegative phase-deficit terms, as justified next.

#### Phase cost, intensity and sector energy

For a finite-support normalized physical vector \(\psi\), set
\(\phi_x=|\psi_x|\). These vectors have the same charge sector and
the same electric expectation. Define
\(d_{xy}=|\psi_x||\psi_y|-\operatorname{Re}(\overline{\psi_y}\psi_x)
\ge0\). Symmetry and nonnegative matrix entries imply
\[
\begin{split}
\Delta Q&=\langle\phi,Q\phi\rangle-\langle\psi,Q\psi\rangle
             =\sum_{x,y}Q_{yx}d_{xy}\ge0,\\
\Delta\Gamma&=\langle\phi,\Gamma\phi\rangle
                -\langle\psi,\Gamma\psi\rangle
             \le\frac{8\kappa}{5}\Delta Q,\\
\langle h\rangle_\psi-\langle h\rangle_\phi
             &=2\delta\Delta Q.
\end{split}                                                    \tag{11}
\]
The absolute sums are bounded by the corresponding nonnegative-vector
expectations because \(Q\) and \(\Gamma\) are bounded. Finite-support
truncations converge in the diagonal electric form norm. Taking moduli
preserves that norm, so (11) extends to every finite-energy vector.

For a basis configuration \(x\), let \(h_a(x)\) count empty \(B\)
neighbours of \(a\). A diagonal original-formation loss path must move
out along one of these edges and create the pair on a different one;
undoing it restores the same electric word. Hence
\[
\Gamma_{xx}=2\kappa\sum_a h_a(x)(h_a(x)-1).
\]
At occupancy \(m\), \(\sum_a h_a=6(n-m)\). For every nonnegative
integer \(k\), including zero, \(k(k-1)\ge2(k-1)\). Therefore
\[
\Gamma_{xx}\ge4\kappa(5n-6m),\qquad
\langle\phi,\Gamma\phi\rangle\ge4\kappa(5n-6m).      \tag{12}
\]
The second inequality uses the nonnegative off-diagonal entries and
\(\|\phi\|=1\). Subtract the second line of (11), substitute its
third line, and use \(\langle h\rangle_\phi\ge e_m\). This proves
(4). Destructive interference may make formation dark, but its energy
cost is controlled by the same path coefficients. Neither positivity
of an arbitrarily selected ground vector, uniqueness, irreducibility,
nor existence of a ground eigenvector is assumed.

#### Passing to the global minimum

The only additional estimates used from the sealed personal ground-filling
note are
\[
\begin{split}
e_m&\ge-2\delta\,3004(n-m),\\
e_*&\le-2\delta R_{n/2}+\delta r_L(\eta),\qquad
R_{n/2}>\frac{1905}{2}n,\quad
\eta=K/\delta,\quad r_L(\eta)\longrightarrow0.
\end{split}                                                   \tag{13}
\]
The first follows from its full color/cycle vacancy row bound and
\(D\ge0\). The second is its Gauss-compatible half-occupancy uniform
color trial localized in all cycle angles. Its finite-graph derivative
estimate gives electric contribution \(O_L(\eta/s^2)\) and magnetic
error \(O_L(s^2)\) in \(h/\delta\); take \(s=\eta^{1/4}\).
These are physical variational vectors, not an asserted initial state
or a harmonic-angle replacement. The exact formula there is
\[
\frac{R_{n/2}}n=\frac{1905}{2}+\frac{378}{n-1}
       +\frac{414(2n-3)}{(n-1)(n-3)}.
\]
The supplied parameterization \(K=g^2/(2\tau)\),
\(\delta=1/(4\tau g^2)\) has \(\eta=2g^4\), so this is the same
fixed-graph small-\(g\) regime. No physical scale is inferred.

For \(m>7n/10\), (13) gives
\[
e_m-e_*\ge\delta\bigl[(513/5)n-r_L(\eta)\bigr].       \tag{14}
\]
At fixed \(L\), this is at least \(4\delta n\) for sufficiently
small \(\eta\). In these sectors, the right side of (5) is nonpositive,
so (5) follows from \(\Gamma\ge0\). For \(m\le7n/10\), (4) has
first term at least \(16\kappa n/5\). Replacing \(e_m\) by the smaller
\(e_*\) only weakens that bound, proving (5) in these sectors as well.

Because \(h\) and \(\Gamma\) preserve \(N\), pinching a density
matrix by its finitely many number projections changes neither
expectation. A spectral decomposition of each block expresses it as a
mixture of vectors. Finite electric form expectation ensures that all
positive-weight vectors in this decomposition have finite form energy;
linearity and summation of (5) then prove the stated mixed-state version.
No loss of inter-number coherences is assumed about the actual dynamics.
For infinite positive energy, the lower energy statement (6) is trivially
satisfied in the extended sense; it does not define a finite energy flux.

Finally, the original common generator satisfies
\([N,h]=0\), \([N,L_j]=2L_j\). Its bounded number observable obeys
\(d\langle N\rangle/dt=2\langle\Gamma\rangle\), including the
normal-state version already proved in main. Stationarity therefore
implies \(\langle\Gamma\rangle=0\). Using \(\kappa>0\), (5) yields
(6). A zero formation coupling is outside this conclusion.

#### Exact controls and failed route

The personal program constructs the primitive \(F_a,F_a^*,j_\sigma,
j_\sigma^*\) in the full charge/electric basis. Its output preserves
every relative integer electric-shift word. Since rotor amplitudes do
not depend on absolute electric flux, each affine column describes every
compatible background flow for that matter word; no electric cutoff is
introduced. A spanning-tree integer flow and every output's Gauss law,
number, and \(P\) support are checked explicitly.

All 65 physical matter words on the degree-three cube are enumerated:
one at \(m=0\), 36 at \(m=2\), and 28 at \(m=4\). There the control
uses the appropriate \((3-1)\Gamma\le8Q\), or \(\Gamma\le4Q\)
at \(\kappa=1\), not the degree-six constant of (10). Seven selected
side-six words cover empty, two near/far pair configurations with distinct
minus placements, two half-occupied charge configurations, two distant
vacancies, and full occupancy. The 72 combined affine columns retain
43,970 entries. Resolved channels, coherent channels, and (8) agree
exactly; the entrywise inequality, diagonal formula, and all Gauss checks
hold in every stored column.

For example, the empty side-six word has \(\Gamma_{xx}=6480\) and
\(Q_{xx}=33372\), while its magnetic row sum is \(34668=321n\).
The diagonal is not the row sum. The half-occupied samples have
\(\Gamma_{xx}=2520\); the distant-vacancy and fully occupied samples
have \(\Gamma=Q=0\). These preserve, rather than contradict, the
known unsaturated dark-state possibility. The new result concerns their
energy relative to the global infimum in a specified regime.

The complete result, source hashes, wall-clock duration and summaries
are saved. The execution took 4.040057959 seconds, exited zero, and
produced no stderr. No failed scientific control occurred. These are
exact bounded path controls, not a simulation of the entire side-six
Hamiltonian, a weak-coupling threshold, a relaxation calculation, a
microscopic energy law, or a comparison with measurements.

An earlier proof idea only observed that nonnegative low-energy vectors
remain active. That does not control destructive phases or degenerate
ground choices, and is insufficient by itself. Equations (10)--(12)
replace that shortcut with a quantitative phase cost. The working note
is preserved unchanged. The global conclusion remains provisional on
(13) until that dependency and this extension receive their scoped checks.

#### Observational meaning and bounded-claim discipline

The supplied model cannot, in this regime, use its global Hamiltonian
minimum as a normal stationary state of its unchanged original formation
law. That closes one particular identification route; it does not rule
out a physical vacuum described by a prepared, metastable, driven, or
otherwise nonequilibrium state. Such an alternative needs a derivation
of its preparation, stability and measured response. No observed system
has yet been identified with the states in this theorem.

- N1, alternatives: preserve sector preparations, metastability, driven
  states and a separately supplied Hamiltonian as distinct options.
  No number-dependent energy offset is adopted to force a desired result.
- N2, independence: the global claim explicitly composes with the two
  provisional estimates (13); it is not an independent second proof of
  ground-sector filling or an amplification of unrelated optical bounds.
- N3, hidden premises: positive couplings, the original channel
  normalization, unsigned rotor amplitudes, degree six, \(L\ge6\),
  all matter/windings, and fixed graph before small \(K/\delta\) are
  load-bearing. Entrywise positivity is not operator ordering.
- N4, residuals: (14) beats one finite-graph vanishing remainder. No
  uniform thermodynamic, fixed laboratory time, or physical scale bound
  follows. All sectors use the same Hamiltonian and zero of energy.
- N5, evidence: exact primitive controls check the stated finite columns;
  the proof covers arbitrary physical form-domain states. No full
  many-body eigensystem or independent experimental evidence is claimed.
- N6, partial closure: (5) is an instantaneous state inequality. It does
  not provide a persistence time, heat/work ledger, ground-state phase,
  excitation spectrum, or apparatus calibration.
- N7, strongest alternative: unitary evolution preserves number, so lower
  global energy does not cause spontaneous unitary decay. The birth law
  drives the activity in this result. A justified alternative physical
  state could still support observations; that remains to be established.
- N8, scope: existing formation balance is reused, not republished as new
  discovery. The new content is the phase-cost comparison and resulting
  energy-versus-formation inequalities. This is not a framework no-go,
  experimental exclusion, newly adopted axiom, or TOE completion.

## Verification and physical boundary

The primary runner freshly executes the five exact root scientific sources
in temporary directories, preserving their helper dependencies and recording
full stdout and complete generated artifacts. It is source reuse, not a new
independent check. Some reused stdout retains its original provisional status
label; those bytes are historical provenance, not an audit disposition.
The separate PRE/POST evidence, failed routes, counterexamples, exact source
bindings and final publication comparison are kept with the review packet.

The spectral results concern fixed finite graphs before the weak-coupling
limit. The actual-birth support result uses a fixed finite-electric basis
input and is a leading edge statement, not a typical energy, narrow line or
conditional mean. The global filling window need not locate the exact
minimizing sector. The activity bounds do not give a relaxation time, a
reservoir ledger, absorbed photon energy or a law selecting a realized state.
The full microscopic finite-spin energy/stationarity bridge is a separate
unpublished obligation and is not presumed by this note.

A selected nonequilibrium preparation, an externally driven apparatus, or
an energy-constrained number sector could require a different comparison.
Those routes are not excluded. Relating this model to a measurement still
needs physical preparation and observable identification, scale calibration,
and finite-parameter/time/volume error bounds. No observational agreement,
whole-framework impossibility, new primitive or TOE completion follows.

## Imports

- [local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): supplied conditional parent within its explicit scope.
- [local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): supplied conditional parent within its explicit scope.
- [formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24](FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md): supplied conditional parent within its explicit scope.

## Reproduction and evidence

Run `python3 scripts/native_ground_energy_and_original_formation_2026_09_25.py` from the repository root. The complete fresh result
and full artifacts are under `outputs/native_ground_20260925/`. The original source histories,
separate scoped checker reports, and publication correspondence are in
[the evidence directory](../.claude/science/physics-loops/mobile-record-native-ground-20260925/).
