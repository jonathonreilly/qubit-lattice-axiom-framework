# Exact local Gauss constraints with mobile, permanently labeled records

2026-09-21. Primary construction and exact finite controls; independent
reconstruction pending. This is a new supplied microscopic model, separate
from the fifteen-state positive-floor transverse-wave generator. Its limit
theory has not been proved. The purpose is to test whether departure and
fresh formation can coexist with an exact local divergence constraint.

## 1. The charge impulse of a two-site swap

On a cubic torus of side N>=5, define the centered discrete divergence

    D F(z)=(1/2) sum_j [F_j(z+e_j)-F_j(z-e_j)].

This is an explicitly chosen encoding of a local Gauss quantity. It is
covariant under the usual signed cubic action on positions and polar
vectors. For an axial vector its divergence is a pseudoscalar, whose zero
constraint is also invariant. At even N it has additional high-frequency
zeros at components k_j in {0,pi}; no continuum claim discards those modes.

Swap two whole records at x and x+e_i. If the feature difference between
the arriving and departing label is d, then

    Delta F(z)=d [1_(z=x)-1_(z=x+e_i)].

For the unhalved divergence 2D, the three columns mapping d into its
charge impulse have Gram matrix 4I. The column for component i has support
x-e_i,x,x+e_i,x+2e_i, with unit coefficients. A component j!=i has support
x-e_j,x+e_j,x+e_i-e_j,x+e_i+e_j. Those three supports are disjoint for
N>=5. Each column has four unit-magnitude entries. Therefore exactly

    sum_z |Delta D F(z)|^2=|d|^2.                         (1)

For the original fifteen-state label features (e,b), this gives

    ||Delta D e||_2^2+||Delta D b||_2^2
        =|e(a)-e(d)|^2+|b(a)-b(d)|^2.                    (2)

The combined feature map distinguishes all fifteen labels. A swap of
distinct labels has a positive impulse in (2), regardless of the external
read context or its rate. This statement is only about this site-feature
encoding and a single two-site event. It does not rule out other gauge
encodings, collective events, effective constraints or the previously
proved finite-mode preparation. The constructive alternative below changes
the microscopic event support explicitly.

## 2. Four permanently labeled records make a closed loop

For a center c and the xy plane, put four A records at

| Site | Immutable vector feature |
|---|---|
| c-e_y | +e_x |
| c+e_x | +e_y |
| c+e_y | -e_x |
| c-e_x | -e_y |

Every other site is vacant. Call this field L_c. Direct substitution gives
D L_c=0: at the four corners c+/-e_x+/-e_y, the two incident contributions
cancel; there are no other nonzero charges. Its opposite circulation also
has zero divergence. This uses four distinct occupied sites and one record
per site. No feature is a superposition of two records.

Exchange the two opposite horizontal sites simultaneously with the two
opposite vertical sites. The resulting field is -L_c, but each individual
record kept its own label and merely changed position. Doing just one of
the two swaps produces a nonzero charge; the combined event matters.

Translate all four records by any one nearest-neighbor displacement a.
The old and new sets of four sites are disjoint: in an unwrapped local footprint the old cross has one
parity of x+y+z, while translation changes it; N>=5 prevents a modular alias. Require every destination
vacant. Each record makes a nearest-neighbor hop and all four hops happen
as one event. The field becomes L_(c+a), so the divergence stays zero and
the old four sites are vacant. This is a bounded eight-site update, not a
sequence of separately Gauss-preserving single-record hops.

The same formulas work in all three coordinate planes and for either
circulation. The entire template family is closed under all signed cubic
actions. A reflected axial feature changes the circulation assignment;
both assignments are already present.

## 3. A two-sector alphabet with capacity, transport and fresh formation

For this construction choose vacancy plus two six-label axis orbits:

    A_(+/-i): e=+/-e_i, b=0;
    B_(+/-i): e=0, b=+/-e_i.

This is a thirteen-state alphabet. In particular the B cube orbit of the
earlier fifteen-state model is replaced by an axis orbit. The new alphabet
and the collective events are supplied additional choices. Neither the
old full-field formulas nor its positive-floor mixing theorem can simply
be transferred to this generator.

For each species, plane, circulation and center, permit:

1. Translation of the four-record loop to four vacant destination sites,
   at a fixed symmetric rate kappa for each nearest-neighbor displacement.
2. Reversal by the opposite-site record permutation, at a fixed rate nu.
3. Formation of a new four-record loop when all four template sites are
   vacant, at microscopic rate beta/N per species/plane/circulation.

Templates examine actual labels, not a permanently assigned loop identity.
In a dense configuration they can overlap; every enabled event must satisfy
the full footprint conditions. The finite generator is the sum of these
bounded local event rates. Simultaneous Poisson events have probability zero,
so conflicting enabled templates do not violate site capacity.

Every transport or reversal event is a permutation of whole records and
vacancies. Formation creates four new record identities; it does not remove
or relabel an existing record. Every event has zero change in both D e and
D b. Thus these two entire microscopic charge fields are conserved exactly,
including during birth. Starting from empty sites gives the source-free
sector at every finite time and volume, without conditioning an ensemble.

An explicit departure-and-reformation sequence is:

    empty -> A loop at c -> same four A records at c+e_z
          -> four new B records at c.

The eight final records occupy eight different sites. The original four
labels and identities are unchanged. Both divergence fields vanish at
every step. All three events have positive rates when kappa,beta>0, so this
is an allowed finite history, not merely a proposed final configuration.

This does not prove endless formation in finite volume: the record count
is monotone and bounded by the number of sites. Nor does it prove ergodicity
or the absence of jammed configurations in the infinite system.

## 4. Exactly invariant conditional ensembles for conservative moves

Turn births off. Each translation has the reverse translation with the
same kappa, and each reversal is its own inverse. All events preserve every
label count. Consequently an arbitrary homogeneous positive product law
has equal probability on the configurations before and after an event.
Eventwise detailed balance proves its invariance under these conservative
moves, even though the generator is highly reducible.

Condition that product on any nonempty joint charge sector (D e,D b).
The sector is closed under the generator and the same pairwise equalities
still hold, so the conditional law is invariant. The source-free sector is
nonempty because it contains the vacuum. It also contains the explicitly
constructed nonempty loops. Product stationarity here is not a proof of
mixing within a sector, a canonical spectral gap or a Coulomb phase.

Births preserve charges but not the conditional product law established
for conservative moves. A density-only product closure is not justified.
For example, on macroscopic Euler time, the exact mean record-count rate
per site for a translation-invariant law is

    rho'(t)=16 beta sum_(three coordinate planes)
                  P(the four sites of that plane's cross are vacant).

There are two circulations and two species for each cross and four records
per event. At empty start rho'(0)=48 beta. Replacing each four-vacancy
probability by (1-rho)^4 would be an additional approximation; it has not
been made in this calculation.

## 5. Exact Fourier form factor and the cost of small local loops

With convention exp(-i k.x), the xy loop has Fourier feature

    Lhat_c(k)=2i exp(-i k.c)
                    [sin(k_y)e_x-sin(k_x)e_y].           (3)

The centered divergence symbol is i s(k), where s_j=sin k_j, so
s(k).Lhat_c(k)=0 exactly. Also

    |Lhat_c(k)|^2=4[sin^2(k_x)+sin^2(k_y)].               (4)

For a fixed continuum mode K with k=K/N this is O(N^-2). Each fixed-size
loop has zero total feature and a dipolar long-wavelength form factor.
An independent dilute gas of such bounded loops with bounded density and
orientation variance therefore has vanishing N^(3/2)-normalized vector
variance at a fixed continuum mode. This conditional dilute-gas observation
does not classify the interacting model: long loops or long-range
correlations of the local loops could change that conclusion.

The birth martingale can be bounded without assuming product independence.
Let the Fourier fluctuation normalization be N^(-3/2). At a fully vacant
configuration, the exact instantaneous covariance of the birth increments
in each vector sector is

    Q_E(k)=Q_B(k)=8 beta [|s(k)|^2 I-s(k)s(k)^T],
    Q_EB(k)=0.                                          (5)

Each plane has two opposite circulations. Summing their outer products
in (3) gives (5). Under an arbitrary law, each template is multiplied by
its vacancy indicator; hence its predictable covariance is bounded above
by the matrix in (5), in the positive-semidefinite order. The combined
instantaneous trace is at most32 beta |K|^2/N^2. Its integral to a fixed
macroscopic time T is at most32 beta T |K|^2/N^2.
Thus these loop births have no leading vector birth noise at that scale,
and the discrete Gauss projection vanishes exactly at every N.

This bracket calculation alone is not a fluctuation limit: tightness,
drift replacement, state selection and possible long-range correlations
remain unproved. In particular, it cannot be combined with the earlier
product fluctuation theorem after changing that theorem's generator.

## 6. The simplest isolated-loop dynamics is diffusive

With births disabled and only one loop present, its center jumps by each
of the six unit displacements at rate kappa. Reversal does not change the
center. Its exact Fourier generator eigenvalue is

    -2 kappa sum_i(1-cos k_i).

At k=K/N it becomes a heat symbol on N^2 time, while N time gives zero
limiting motion of the center. This exact one-loop test does not provide
a ballistic transverse wave. It is a useful distinction: compatibility
of permanent records, site reuse and a microscopic Gauss constraint is
established for the supplied events; a wave-supporting collective phase
of those events is still a separate research problem.

## 7. Evidence and next decisions

`microscopic_gauss_record_loop_check.py` has thirteen completed exact local
and symbolic control groups. It tests all630 ordered distinct-label swaps
in the original fifteen-state menu, the Gram identity, all six translations,
an explicit history with persistent record IDs, all48 signed cubic template
actions, Fourier form factors and birth covariance, product weights and the isolated-loop symbol.
No failed execution was discarded. These are primary controls, not an
independent review or a proof of a continuum gauge theory.

Next: separately reconstruct the collective construction; analyze whether
the admissible Gauss sectors have a nontrivial long-wavelength covariance
and a controlled mixing mechanism; determine whether coupling the two
sectors can give a first-order curl evolution without importing it. The
new rates and alphabet have no axiom-selection argument. Quantum dynamics,
physical charges, field units, Lorentz symmetry and gravity remain open.
