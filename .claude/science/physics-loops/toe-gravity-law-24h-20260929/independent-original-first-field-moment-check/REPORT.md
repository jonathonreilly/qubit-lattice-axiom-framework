# Focused independent check: microscopic first electric moment

Root found no substantive error in FIRST_FIELD_MOMENT.md, SHA256
acf0f4efaecdefac46205b3d874e76102f64d60df21e921654faa0b3a8973d1a.
The common physical-time first-moment bound and fixed-output compactness
consequence check at the stated supplied-law scope. This is a focused
analytic check, not formal review, audit or retained status.

## Independence and actual reads

Root PRE 2b724ee01f4ed1741b69c5a06c1b6b6c8472c91e472c845606a264b641f7b485
was frozen before opening the new proof. It disclosed the author brief's
observable, proposed constants and correction mechanism. It reconstructed
the bounded-displacement drift, physical return and cutoff argument before
comparison; this was not a blind check. The entire new proof and the entire
old DEFECT_LEMMA fbbf36c26413f3f678f071d610338c0fcc78ea9fa587c6874c4b19791d8351af
were read. The exact current law and finite-circuit construction were already
fully read in this continuing campaign and are unchanged.

Main has advanced to fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7 through an
external audit pipeline refresh. Root compared the affected closure: all six
model/normal-form sources, axiom memo, primitive registry and selected loop
procedures keep their actual bytes. Root read all six relevant current
ledgers completely; they remain unaudited and add no verdict or blocker.
SOURCE_BINDINGS.json records those identities. This check creates no audit
state and does not adopt the supplied law as an axiom consequence.

No new numerical job was run by root. The author announced a separate
corroborative control after this proof was read; it is not an input here and
has not yet been read. The mean-mark balance and quadratic initial-layer
lemma are not premises of this proof.

## Bounded displacement and the exact fast drift

For V=sum_e |E_e|, entrywise field displacement bounds
|V(alpha)-V(beta)| by d_E(alpha,beta). Both Schur row and column estimates
therefore give a uniform norm for [V,A] whenever A has bounded first
displacement norm. This is valid for the actual normalized spin shifts,
including their boundary zeros. The diagonal normalized compensation has
no field displacement and bounded supremum. Products, commutators, local
gate exponentials, grade projections and the integer grade inverse preserve
the required norms. Only a bounded circuit cone is used per original term;
no bound on the global circuit's Schur norm occurs.

The complete adjoint dissipator identity
D[J]*V=(J*[V,J]+[J*,V]J)/2 retains both recycling and loss. Its cross-map
version has the same bounded local estimate. Disjoint terms cancel before
summing. Thus the extensive bound is C|A|, independent of S, rather than a
product of extensive norms or a bound proportional to ||V||.

Root checked the full leading D2 path classification: 36 positive same-hole
paths, at most 18*36 gated negative paths assigned to an input hole, and
18*2*2 moving-hole commutator paths. Every two-hop word changes V by at
most two. The absolute row bound is consequently 1512 times the input hole
count. Hermiticity and symmetric absolute entries give the two-sided form
bound with the safe constant 1600. The diagonal electric term commutes
with V and contributes zero. This argument holds on the full carrier and
its Gauss subspace, with arbitrary coherent inputs.

The bare original jump changes V by at most one; its total loss is bounded
by 12W. For this diagonal observable, coherent sign cross terms vanish
because their final A charges are orthogonal. No sign measurement or
replacement of the original coherent recycling map is made. The actual
leading fast drift is therefore bounded by
(1600 delta+12 kappa) W in both directions. This hole factor is the
essential improvement over a generic epsilon^-2 volume bound.

## Corrected drift and uniform time scale

The exact finite-circuit parity in DEFECT_LEMMA removes odd diagonal
Hamiltonian orders. The diagonal generator after epsilon^-2 B2 consequently
has strength O(1). In the jumps, the first derivative has grades zero and
minus two, while the original jump has grade minus one. Grade averaging
of the complete dissipator retains equal grades, so its correction to the
bare leading drift also has strength O(1), not O(epsilon^-1).

The remaining offgrade drift R_E has local norm strength O(epsilon^-1).
The displayed K1 and K2 have strengths O(epsilon^3) and O(epsilon^5).
Multiplying by i times the inverse grade gives Hermitian corrections with
i delta epsilon^-4[W,K1]=-R_E. Direct substitution gives

 L'*(V+K1+K2)=P_W L'*V+P_W B_epsilon K1+B_epsilon K2.

B2 preserves grades, so its apparently order-epsilon averaged action on
K1 is exactly zero. The remaining strengths are O(epsilon^2) and
O(epsilon^3). Thus the drift is bounded above by
c0 epsilon^-2 W+C|A| with bounded correction endpoints. The averaging is
a diagnostic algebraic operation; the ensemble remains the exact original
rotated ensemble throughout.

The checked bound <W>_sigma/|A|<=C epsilon^2(1+t) now gives the integral
C(t+t^2). No field moment is fed back into its own drift, and no
exp(t/epsilon^2) factor is needed. This is why the result has a common
physical-time scope whereas the quadratic weighted estimate did not.

## Preparation and return to physical fields

For each link, the difference Y*|E_e|Y-|E_e| is a bounded local operator.
One first integrates its bounded commutator through the finite local gates,
then Taylor expands the resulting bounded expression. This justifies the
uniform second-order remainder despite ||E_e||=S. The first derivative is
the offgrade commutator with S1=-F+F*.

Since |E_e| annihilates Omega, the linear expectation at preparation is
zero. The rotated first moment starts at O(epsilon^2|A|). For physical
return, the first commutator has vanishing compression to the local
all-A-occupied subspace. Decomposing a bounded operator into the two local
projector blocks bounds its expectation by 3||A||sqrt(p_hole). The actual
physical defect bound gives p_hole<=C epsilon^2(1+t), uniformly in S and
volume. Multiplication by epsilon and inclusion of the quadratic remainder
gives O(epsilon^2[1+sqrt(1+t)]) per link.

Translation symmetry is invoked only for the actual physical generator and
Omega, after return. A fixed link orientation's nonnegative translated sum
is bounded by V. The circuit coloring need not be translation invariant.
These steps verify E1, including the explicit uniform spin/volume scope and
the allowed coupled scaling. At t=0 the physical moment is exactly zero;
the displayed bound is deliberately an upper estimate.

## Local outputs and what compactness means

Markov's inequality and a union bound give the stated tail for each fixed
finite link set. The elementary finite-spin inequality E^2<=S|E| gives
the normalized second-moment bound O(1/(S+1)); it does not bound E^2 itself.

Embed each integer-spin field basis in l2(Z), keeping the original matter
factors and mark alphabet. DEFECT_LEMMA D3 supplies the independent local
unconditional count tail for finitely many monitored centers. Moving
overflow history blocks to a disjoint flag costs at most 2p_N. Projecting
the quantum fields costs at most 2sqrt(p_E); optional normalization with
a refusal state adds at most p_E. The remaining binned, capped, cut-off
carrier is finite dimensional. Uniform approximation by these finite
carriers proves subsequential trace-norm compactness for each specified
joint output. For classical-quantum blocks, summing the conditional field
tails gives the unconditional marginal moment; no conditional moment bound
is needed. Actual coherent signs remain within their original mark.

This does not establish uniqueness, boundary independence, continuous-time
total-variation convergence, or any effective-law identification. A bounded
first moment permits second moments to grow with spin and does not give
electric-energy uniform integrability. In particular epsilon^-2 rare-hole
weights and the fast-response integral of hole-weighted local field squares
remain uncontrolled. Those are substantive remaining consumers.

Permitted reuse is the actual supplied-law first-moment/tightness statement
with these source and output specifications. No current axiom inconsistency,
new selected source law, selected clock or completed TOE follows.
