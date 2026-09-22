# Uniform local ring dynamics: bounded source comparison

Date: 2026-09-22. This is a post-seal scientific comparison, not an audit,
retention or publication decision. The independent reconstruction in
`REPORT.md` and `PRE_COMPARISON_SEAL.json` is unchanged.

**Disposition: no mathematical correction is required by this check.** The
author's finite circuit proof supports its stated uniform-volume local limit
for both supplied penalties and its prepared initial family. In particular,
the schedule `beta=beta_0 epsilon^(2d)` is justified. My blind reconstruction
used an operator-norm comparison and the more restrictive sufficient schedule
`beta=O(epsilon^(2d+1))`. The author obtains the extra power by bounding the
full dissipator on the code-supported reference trajectory. That distinction
is substantive and valid; the two sufficient statements do not conflict.

## 1. Exact sources and comparison boundary

The authorization followed the independent PRE seal
`928e25108e5482c4a8d555323e55cda2a6f3b0a5b9cbdcf4e0c1b2550e84fd6b`.
All 24 of its source/artifact bindings still authenticate. Its report is
`4dc693c1b9cadd94ea95ce01108a72570482ad82c10c4b3f5f611169f749621e`.

The author seal is `UNIFORM_LOCAL_RING_AUTHOR_SEAL.json`, SHA-256
`4b52f52f820ed5efbe01b18d47c0166018f0c421cd507fb55f171d893f8a7ce5`.
All 17 bound artifacts authenticate, including the preserved failed diagnostic.
The principal source identities are:

| Source | SHA-256 |
|---|---|
| `UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION.md` | `e03793ab0cc06bcc0d536db5b846addf3a999733c6dc25cc4d08ae457263e16e` |
| `local_normal_form_record_check.py` | `9507de54429615ccc0256da4965f9a4e093787797d635e53c751d3279028d3ec` |
| `finite_circuit_normal_form_record_check.py` | `17c238c8ac4a7c8517068c7dfe26b5eb50872e9325ec1b0f41bbf95c338aae6b` |
| `LOCAL_NORMAL_FORM_RECORD_RESULTS.json` | `b7776666d455926c77a55bfa884f0399fc4bec5d041de1633143f7cea7d1abf6` |
| `FINITE_CIRCUIT_NORMAL_FORM_RECORD_RESULTS.json` | `6f374492bb6c2df490ec97bc8fa2ef1d7ceced58c41ee20a864a9603990e23b8` |

I read the complete 356-line note, both complete runners, source-context
receipt, complete run streams/receipts and preserved failure diagnosis. All
stored rational matrices were parsed and independently recomposed as described
below. All numerical table fields were read; their recorded arithmetic was
checked, without rerunning the author's high-precision exponentials. The full
old-to-current runner delta was inspected. The already checked ring and
field-star premises retain their pinned identities.

The source-context receipt lists `BALLISTIC_FIELD_SIGNALS_FROM_RECORD_FORMATION.md`
as a separate diagnostic. That source remains unopened and is not used here.
The newer large-spin, weak-field, transport and ramp packets, campaign
checkpoint and registry likewise remain unopened. The final seal records
complete paths, sizes and hashes, rather than treating a short filename as
an identity.

## 2. Integer onsite extension and finite circuit

The improved field-star extension in Eq. (8) is exact. On the physical
periodic sector, `div E=q-1_A` and `sum q=|A|`. Consequently

    (1/2) sum (div E)^2 = N_(A,-) + N_(B,+).

One can derive this by adding `(sum q-|A|)/2=0` to the quadratic expression
and collecting the two onsite charge projectors. It is useful that the
right-hand side has integer spectrum on the entire unconstrained tensor
space. It differs off the chosen charge sector from the half-integer onsite
representative used in my PRE; either is a valid extension on the physical
sector. Every legal hopping term changes the new integer penalty by one.
At fixed signed charge `|A|`, its zero eigenspace has plus records at all A
sites and vacancies at all B sites. Gauss then imposes the ice constraint.
Births preserve signed charge and Gauss, so the extension remains valid after
formation, not merely on the initial no-minus sector.

The circuit in Section 3 addresses an obligation absent from a mere
finite-volume spectral argument. Here is the reconstructed induction.

* At a fixed order r, each Hermitian coefficient can be indexed by an
  original local term and its previous circuit light cone. Support size,
  range and the number of such indices meeting any site are bounded by
  constants depending on the fixed order and dimension.
* The onsite average removes nonzero integer grades. The integral kernel
  `i(theta-pi)/(2pi)` divides grade k by k, has absolute integral `pi/2`,
  and enlarges no support. The resulting S is anti-Hermitian and obeys
  `[S,N]=-(A-P_N A)`.
* A bounded coloring of the support-intersection graph gives a bounded
  number of disjoint-gate layers. All order-r generators must be frozen
  before applying that order's gates. Their leading effect is the sum
  of their commutators with N; their higher-order ordering effects remain
  in the next coefficients. No equality with the exponential of their
  sum is needed.
* Conjugating each original local term by the final finite circuit uses
  finitely many gates in a uniformly bounded cone. The inverse products
  furnish its analytic extension to complex epsilon. A common small
  complex disk and Cauchy remainder estimate therefore bound each
  indexed remainder by `C_n epsilon^(n+1)`. Bounded index density gives
  the local interaction norm, without a factor V.

The symmetry and parity claims survive this construction. The original
terms, onsite averages and gates preserve charge, record number and Gauss.
Conjugation by `exp(i pi N)` assigns parity `(-1)^r` to the order-r
coefficient. With epsilon-independent coloring, this covariance persists
through the ordered gates; a penalty-diagonal odd coefficient is zero.
When a local decomposition of an already diagonal total coefficient is
needed, its individual terms may be averaged over N. This preserves its
sum and bounds and makes penalty commutation termwise explicit.

Only local closeness to the identity is used. There is no volume-uniform
claim about the global operator norm of `Y-I`, nor an unproved replacement
of a finite circuit by a single global-generator pulse. The finite-depth
construction is thus a valid strengthening of the quasi-local preparation
used in my blind proof.

## 3. Code Hamiltonian and locality import

The checked two-hop and complete normalized four-hop coefficients are
`D_2=-M I` and `D_4=M(2d-1)I-2 sum_p X_p` on the ice code, where
`M=dV/2`. A near-identity block-identification change cannot alter the first
non-scalar coefficient when the lower nonzero coefficient is scalar.
Hence the circuit and the previously normalized perturbative calculation
have the same ring term. Odd coefficients vanish, so after restoring Delta
the next local correction starts at `Delta epsilon^6=O(J epsilon^2)`.

Taking fixed-matter matrix elements preserves locality and does not
increase a term's norm. Gauge commutation becomes field-divergence
commutation. Removing the scalar second-order block and using the equal
fourth-order ring expression on ice gives a local field extension whose
velocity is bounded at fixed J. Thus the `O(epsilon^2)` code-dynamics
comparison does not retain the much larger velocity of excited sectors.
No factorization of the ice density or irreducibility of its loop sector
is required.

For the open comparison I checked the actual hypotheses and complete
Theorem 1 proof of
[Barthel and Kliesch, arXiv:1111.4210v2](https://arxiv.org/html/1111.4210v2).
The needed result permits time-dependent bounded local Lindblad terms on
finite-dimensional tensor factors, with bounded range and overlap. Its
backward Heisenberg propagators are norm contracting. Sections II-III,
Section V and Appendices A-D were read; no Trotter theorem is imported.
The stored primary source and read receipt are separately hashed.

These hypotheses hold after assigning matter and a bounded number of links
to each lattice cell, extending the onsite penalty as above, and removing
`Delta N` by an exact product of onsite unitaries. That interaction picture
does not enlarge supports or term norms. Rapid time dependence introduces
no additional hypothesis on time derivatives. Each dissipative term retains
its actual local jump, and each Hamiltonian term remains Hermitian. The
resulting bound has velocity `v<=C_n(h+delta_R+beta)`, with
`h=Delta epsilon^2`. This use of the theorem does not assume a tensor
factorization of the constrained physical subspace.

## 4. State-dependent source and the beta schedule

This is the central valid improvement over my PRE estimate. If
`B=Y j Y^dag`, then `jP=0` and local circuit closeness imply
`u=||BP||<=C_n epsilon`. For any density `sigma=P sigma P`, positivity and
the trace-ideal inequalities give

    ||B sigma B^dag||_1 <= u^2,
    ||B^dag B sigma||_1 <= ||B|| u,
    ||sigma B^dag B||_1 <= ||B|| u.

Thus `||D[B]sigma||_1 <= u^2+||B||u=O(epsilon)`, including both
anticommutator terms. This argument applies to arbitrary entanglement in
the reference code. It remains valid in the onsite interaction picture,
which preserves P and the relevant norms.

Variation of constants can be written with the full open propagator acting
on the observable and the difference generator acting on the closed
code-supported reference state. For a near source, use this trace norm;
for a distant source, move the local difference generator onto the backward
observable and use the Lindblad locality bound. The full state need never
be assumed to stay in P. Repeated births and no-event evolution are already
included in that full propagator.

The needed spatial sum has a volume-uniform proof. With unit-radius shell
counts bounded by a constant times `(1+r)^(d-1)`, set a splitting radius
`r_0=C(vT+|log epsilon|+1)`. Inside it, the small source contributes at most
`C epsilon(1+r_0)^d`. Outside it, the exponential tail contributes at most
the same order. Finite periodic distances only reduce the number of sites
relative to the lattice shell bound, even when the cone crosses a period.
The analogous bound with cutoff 1 controls R. This yields exactly the
structure of author Eq. (22):

    C_X ||O|| T [delta_R(1+vT)^d
        + beta epsilon(1+vT+|log epsilon|)^d].

For fixed J and order `n=2d+6`, `h=O(epsilon^-2)` and
`delta_R=O(epsilon^(2d+3))`. The two terms are respectively
`O(epsilon^3)` and `O(epsilon)` when `beta=beta_0 epsilon^(2d)`.
The local observable dressing costs `O(epsilon)` and the code comparison
costs `O(epsilon^2)`. Constants can depend on the fixed support and time
interval, not on volume or the chosen ice density. The author schedule and
claimed bound therefore follow, including beta_0=0.

An exact independent countercontrol confirms why the full dissipator must
be used. Set `P=|0><0|` and
`B=|2>(s<0|+sqrt(1-s^2)<1|)`, `0<s<1`. Then

    Tr(B P B^dag)=s^2,
    ||D[B]P||_1=s+s^2.

The anticommutator supplies a first-order coherence. This saturates the
general source estimate and refutes a jump-count-only second-order bound;
the author does not make that invalid replacement.

## 5. Executable coverage, failures and limits

`comparison_check.py` is new independent code. It imports only the previously
sealed independent physical-sector builder; neither author runner is executed
or imported. It authenticates all 17 author bindings and all 24 PRE bindings,
and checks the unchanged relevant source-context prerequisites.

The independent square enumeration is reordered to the author basis. I then
multiply Taylor series of the gate matrices and their inverses directly,
rather than using the author's nested-commutator update. This recomposes
every stored rational normal coefficient and the entire first omitted
coefficient: through order 17 for both global-generator penalties and order
13 for both circuit penalties. Gate anti-Hermiticity, penalty parity, record
number, all normal-coefficient commutators and the low second/fourth blocks
are also checked. There are four noncommuting pairs among the first-order
circuit gates, so this actually tests ordering corrections.

The exact squared Frobenius norms of the omitted coefficients are

    global order 17:
      289311215188902702903038845891 / 17736670201250,
    circuit order 13:
      1032255336369062785103735305993 / 1077105223434240000.

Their square roots are approximately `1.2771637676e8` and `9.7895899761e5`.
The former independently confirms the diagnosis of the author's preserved
failed guessed threshold `1e8 epsilon^17`. The original code/streams/receipt
are intact; the fix derives the omitted coefficient rather than silently
relaxing the perturbative order. The numerical tables approach those exact
leading coefficients. Their high-precision exponentials are authenticated,
not independently rerun or treated as evidence for uniform constants.

Additional independent controls verify the integer-penalty identity and
unique zero pattern on every fixed-charge four- and six-site matter word,
the exact three-level dissipator countercontrol, and the clipped-cone sum
on four even rectangular tori, including radii larger than their periods.
The exponent arithmetic is checked for dimensions 2, 3 and 4. These finite
controls test formulas; the preceding locality proof supplies the general
volume assertion.

One new helper attempt failed on SymPy structural equality between
`s^4/4-s^2/4` and `-s^2(1-s^2)/4`. Its complete source, stdout, stderr and
receipt are preserved under
`failed_attempts/dissipator_structural_equality/`. Exact simplification gives
zero difference. Replacing structural equality by that exact polynomial
test changes no mathematical assertion or tolerance. The subsequent run
exited zero; all result fields were inspected. No source correction is
being requested on the basis of this helper failure.

The reviewed conclusion remains restricted to the stipulated Hilbert space,
bosonic statistics, Gauss sector, supplied rates/Hamiltonians, finite local
prepared family, vanishing positive birth rates, and fixed local observation
times/supports. It does not establish a bare-quench result, fixed-beta limit,
optimal scaling, practical preparation cost, thermodynamic Coulomb phase,
photon dispersion, native primitive compilation or increasing-time theorem.
It also does not require the probability of no birth anywhere in a large
torus to approach one. No unresolved load-bearing proof gap was found within
that scope.
