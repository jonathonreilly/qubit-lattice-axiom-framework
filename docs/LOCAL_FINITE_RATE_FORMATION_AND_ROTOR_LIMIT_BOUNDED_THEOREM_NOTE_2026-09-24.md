---
claim_id: local_finite_rate_formation_and_rotor_limit_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - finite_rate_repeated_record_formation_bounded_theorem_note_2026-09-24
runner: scripts/local_finite_rate_formation_and_rotor_limit_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# Local finite-rate formation and the finite-volume rotor limit

Author conditional addendum, 2026-09-22. Independent reconstruction pending.
This note depends on the explicit model and complete embedding proof in
FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md, bound by
FINITE_RATE_FORMATION_AUTHOR_SEAL.json
(e0f07e9879e8332d17b1e96884c8942d21db4bdb4f7fe547d0bad3ed90ddd6ab).
It does not change that frozen theorem or its supplied physical assumptions.

The results below identify an exactly local effective generator and remove
the finite-spin cutoff at fixed finite volume. They do not establish a
volume-uniform microscopic approximation, a photon regime, an autonomous
energy source, or indefinite record production.

## 1. The apparent global resolvent is a local star operator

Keep the finite bipartite graph, hard-core states 0,+,-, integer spin S>=1,
normalized link shifts, staggered Gauss sector and two possible per-edge
birth instruments from the parent note. Write z_a for the degree of a site
a in A and M for the number of edges. Assume P=1_(W=0) is nonzero.

On the one-hole sector Pi_1, let Pi_a project onto states whose unique empty
A site is a. A birth on an edge incident to a can act only if a is empty.
The loss of a birth does not change any site occupation. Indeed the two
charge outputs of j_(e,+) and j_(e,-) are orthogonal, so

(j_(e,+)+j_(e,-))†(j_(e,+)+j_(e,-))
 =j_(e,+)†j_(e,+)+j_(e,-)†j_(e,-).

Each summand is a product of endpoint-vacancy projections and a diagonal
link weight. Thus the same loss operator applies to coherent and resolved
births. On Pi_1,

Gamma_1 = direct_sum_a Gamma_a,
Gamma_a = kappa sum_(e incident a),channels j_e†j_e |_(Pi_a).

There is no off-diagonal coupling between distinct empty-A locations in
this loss operator. Let h_a be the sum of outward hops from a, including
the sign convention of T. It acts only on a, its neighboring B sites and
their connecting links. Restricted to P, h_a=Pi_a T P, and

A_1=sum_a h_a,  D_1=direct_sum_a d_a,
d_a=delta I-i Gamma_a/2.

Here d_a^-1 can be computed within the local star algebra: take the loss
sum on the star, restrict a to be vacant, and invert delta I-i Gamma_a/2
on that local subspace. All other degrees of freedom are spectators.
Equivalently extend it to the other local occupation blocks before
sandwiching with h_a. Its inverse exists with norm at most 1/delta.

Orthogonality of the one-hole blocks gives exactly

H_eff=sum_a H_a,
H_a=-(delta²/2) h_a†(d_a^-1+d_a^-†)h_a,                (1)

l_(e,channel)=sqrt(kappa) delta j_(e,channel)
                         d_a^-1 h_a,                (2)

where a is the A endpoint of e. Restrictions to the P/Gauss sector are
understood. The formulas can first be defined on the full tensor product
by the local expressions above, then restricted. A global physical-sector
constraint does not turn their support into a nonlocal interaction.

Every term in (1) and every jump in (2) is supported on one A-centered
star. H_a preserves N, each l raises N by two, and all commute with Gauss.
The inverse in the compact global formula therefore introduces no
dependence on arbitrarily distant occupations or electric fields.

## 2. Bounds independent of the spin cutoff and total volume

The normalized integer-spin shifts have norm at most one. On a single
edge the two charge-conserving outward maps act between orthogonal
charge sectors and have norm at most one as a combined map. Consequently

||h_a||<=z_a.

A resolved birth has norm at most one, and a coherent per-edge birth has
norm at most sqrt(2). In both conventions the sum of squared channel
norms over one edge is at most two. Using ||d_a^-1||<=1/delta,

||H_a||<=delta z_a²,
sum_(e incident a),channels ||l_e||²<=2 kappa z_a³.    (3)

The induced trace-norm bound for a star's Lindblad generator is therefore

||L_a||_(1->1)<=2 delta z_a²+4 kappa z_a³.             (4)

These bounds hold uniformly in S and in the rest of the graph at fixed
degree. They prove that the target dynamics is generated by uniformly
bounded local terms. They alone do not supply a volume-uniform error
bound between the original fast microscopic dynamics and this target.

For the finite-volume approximation in the parent note, the constants
can also be chosen independent of S. The full self-adjoint hopping on
one edge decomposes into the two charge sectors and, in each, into
two-by-two weighted swap blocks with norm at most one. Thus ||T||<=M.
With Y and Y_2 defined in that note,

||Y||<=M,   ||Y_2||<=M²/2,
a_1<=2M,   a_2<=2M²,
||H_eff||<=delta M²,
sum_j ||l_j||²<=2 kappa M³,
ell<=2 delta M²+4 kappa M³.                           (5)

Substitution in its equation (6) gives an explicit O(epsilon) bound
uniform in S on each fixed finite graph and finite time interval.
The constants grow with M; there is no large-volume estimate here.

## 3. Removing the finite-spin cutoff

Replace each link by l²(Z), E|m>=m|m>, U|m>=|m+1>.
Retain the supplied Gauss constraint, the same hard-core site factors,
W, hopping, and birth channels. All operators in the generator other
than the kinematic Gauss/E labels are bounded: W has finite integer
spectrum, U is unitary, and there are finitely many terms.

In particular this model has no unbounded electric-energy term E².
No estimate for adding such a term is being asserted.

The physical Gauss sector is the closed span of the admissible integer
electric-field/site words. Hops and births map that sector into itself.
On its trace-class operators the two finite-volume Lindblad generators
are bounded. The identities in the parent note use only bounded operator
multiplication and the finite W grading, so they hold without a
finite-dimensional Hilbert-space assumption. The maps E_i remain bounded,
preserve Hermiticity, and satisfy exactly the same residual identity.

For completeness, bounded Lindblad generators with finitely many jumps
generate CPTP semigroups on trace class, as follows from the no-jump
propagator plus its norm-convergent jump/Dyson expansion. Trace preservation
follows by differentiating the trace of this bounded evolution. Positivity
and trace preservation give trace-norm contraction on Hermitian inputs.
The same Duhamel proof consequently proves the parent equation (6) for
unit rotors, with the constants in (5), for every P-supported density.
No electric moment hypothesis is needed in this bounded-generator result.

There is also a simultaneous limit from finite spin. On the rotor space
extend the finite-spin shift by zero outside [-S,S]:

U_S|m>=sqrt(1-m(m+1)/[S(S+1)]) |m+1>,
             -S<=m<=S-1,
U_S|m>=0 otherwise.

These operators and their adjoints converge strongly to U and U†, and
all have norm at most one. The electric box projection Q_S commutes with
the site projection P and the physical Gauss projection. Its range is
preserved by the extended finite-spin dynamics; on that range the
original finite-spin model is exactly recovered.

Strong convergence follows first on finite electric-support vectors and
then on all vectors by the uniform norm bound. Finite sums and products
therefore give strong convergence of hopping and birth operators and
their adjoints. Gamma_(j,S) converges strongly to Gamma_j. The identity

D_(j,S)^-1-D_j^-1
 =D_(j,S)^-1 (D_j-D_(j,S)) D_j^-1

and the uniform inverse bound 1/(j delta) prove strong convergence of
these inverses, and similarly of their adjoints. Hence the effective
Hamiltonians and jumps converge strongly with their adjoints.

If A_S,B_S converge strongly together with their adjoints and are
uniformly bounded, then A_S X B_S converges to A X B in trace norm for
every trace-class X. This follows on rank-one X directly and extends by
finite-rank approximation. It gives strong convergence on trace class
of the effective generators. Their operator norms are uniformly bounded
by (5), so the exponential series, with a uniformly summable bound,
gives convergence of effective semigroups uniformly on each fixed
finite time interval.

Let rho_S be physical P-supported finite-spin densities embedded in the
rotor space with ||rho_S-rho||_1 tending to zero. Such approximants exist
for every physical P density, by normalized Q_S rho Q_S when its trace
is nonzero. If epsilon(S)>0 tends to zero by any rule, triangle inequality
between the microscopic spin evolution, its effective spin evolution,
and the effective rotor evolution proves

sup_(0<=tau<=T_0)
 ||rho_(epsilon(S),S)(tau)-exp(tau L_eff,rotor)rho||_1 -> 0.  (6)

The first error is bounded uniformly in S by the parent theorem and (5).
The second follows from the strong semigroup limit just proved; the
initial-state error is controlled by trace-norm contraction.
No relation between the rates S->infinity and epsilon->zero is needed.
This assertion keeps the graph and T_0 fixed.

## 4. Local birth intensity is not a closed classical occupation law

For a unit-rotor site/electric basis state in P, suppose a has k empty B
neighbors. An outward hop has k orthogonal possible destinations.
After such a hop, there are k-1 still-vacant neighbors of the empty a.
The one-hole loss is then the scalar 2 kappa(k-1). For a fixed birth
edge and charge channel, distinct old-record destinations have
orthogonal final occupations. The two coherent charge outputs are also
orthogonal. Squaring (2) and summing the marks therefore gives the
instantaneous formation intensity at a,

r_a(k)=2k(k-1) kappa delta²/[delta²+kappa²(k-1)²],      (7)

for k>=1, and r_a(0)=0. The same expression applies to the complete
spin-one tree controls whose legal shifts all have unit weight.

Both instruments have the same H_eff and the same total effective loss
operator, because their original losses coincide. They need not have the
same recycling map sum l X l†. Equation (7) is a statement about a basis
state at one instant, not a closed Markov law on occupations. Coherences
created by motion and prior formations can affect later intensities.
The exact four-leaf dark states in the parent note provide a direct
counterexample to guaranteed completion based on vacancies alone.

## 5. Checks, dependencies, and limits

formation_locality_check.py uses the author's complete physical tree-sector
builder already bound by the parent seal. Exact SymPy rational arithmetic
checks the two- and four-leaf stars and the path with two A sites, for both
birth instruments. It verifies:

* the one-hole loss has no matrix elements between different empty-A sites;
* the global resolvent Hamiltonian and every effective jump equal (1)--(2);
* coherent and resolved effective loss matrices agree;
* all P-basis star formation intensities equal (7).

All six model/instrument controls passed the first execution. Full outputs
and source identities are in FORMATION_LOCALITY_RESULTS.json and its
execution receipt. The calculation reuses an author builder; it is not an
independent reconstruction. The general bounds and rotor convergence are
proved above rather than inferred from the small models.

This is a local finite-volume matter/formation construction under supplied
quantum and instrument assumptions. The original energy cost per new pair
still scales with Delta=delta epsilon^-2. The previous fourth-order field
scale is delta epsilon² and vanishes. A simultaneous propagating-field
regime, volume-uniform microscopic approximation, autonomous reservoir,
law selection from the native axioms, and experimental matching remain
open. No theorem of everything or new fundamental physical law is claimed.



## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [finite_rate_repeated_record_formation_bounded_theorem_note_2026-09-24](FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8672, frozen head `fe6dc2c5ef061fa1e0051063d49178f23b872c13`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/local_finite_rate_formation_and_rotor_limit_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
