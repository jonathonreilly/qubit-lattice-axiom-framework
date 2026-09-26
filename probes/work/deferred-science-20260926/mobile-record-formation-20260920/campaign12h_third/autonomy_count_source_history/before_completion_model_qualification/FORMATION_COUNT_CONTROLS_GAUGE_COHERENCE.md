# Formation count controls a specified gauge-conjugation coherence

Date: 2026-09-22. Status: author conditional theorem and executed exact
controls; independent checking pending. The Lindblad law, gauge carrier,
monitoring, and initial phase are supplied. The observable below is a global
charge-conjugation coherence, not a derived photon correlation function.

## 1. An exact conserved observable for the instrument family

Work in a finite physical gauge sector with an even maximum record number
K and only even record-number sectors. Let N count existing records. Supply
a unitary involution T that conjugates every charge and electric field,
preserves the physical sector, and commutes with N. For every birth edge,

    T V_(e,+) T=V_(e,-),
    V_(e,+)^dagger V_(e,-)=0,
    V_(e,+)^dagger V_(e,+)+V_(e,-)^dagger V_(e,-)=P_e,
    [N,V_(e,+/-)]=2 V_(e,+/-),  [T,P_e]=0.

Here P_e is the vacant-edge projector. The edge birth generator has rate
beta_e>0 and the same real chi in [-1,1] on every edge:

    B_e(rho)=beta_e [V_+rho V_+^dagger+V_-rho V_-^dagger
                 +chi V_+rho V_-^dagger+chi V_-rho V_+^dagger
                 -(1/2){P_e,rho}].

Suppressing e on the operators in this formula does not combine different
edges into one nonlocal jump. This is the local completely positive
coarse birth-map family already classified in the preceding note. Individual
Kraus outcome labels need further instrument data beyond this map.

Assume [H,N]=[H,T]=0. Every other jump must commute with both N and T;
occupation monitoring has this property. Define the polynomial-in-chi
observable, using the spectral projectors of N,

    O_chi = sum_(n even,0<=n<=K) chi^((K-n)/2) P_(N=n) T.

The exponent is a nonnegative integer. At chi=0 its n=K coefficient is
one, and every other coefficient is zero. No division by chi is needed.
Then exactly

    L^dagger(O_chi)=0.

To prove it, for an arbitrary scalar function f of N the jump gain gives

    B_e^dagger[f(N)T]
      = beta_e P_e [chi f(N+2)-f(N)] T.

Indeed T exchanges V_+ and V_-. The two diagonal coefficient terms in the
gain therefore vanish by orthogonal input/output supports, whereas the
cross terms sum to chi P_e T. Moving f through a birth shifts N by two.
On every sector where P_e is nonzero, f(n)=chi^((K-n)/2) obeys
chi f(n+2)=f(n), including chi=0. On n=K, P_e=0, so f(K+2) need not be
defined. Hamiltonian and other-jump contributions vanish by their stated
commutators. This proves the identity without assuming a classical trajectory.

At chi=1, T commutes with each coherent birth jump, an example of a strong
Lindblad symmetry. The distinction between symmetry of the entire generator
and commutation with each jump is established terminology; see Appendix
equations (11)-(12) of
[Buca and Prosen, arXiv:1203.0943v3](https://arxiv.org/abs/1203.0943v3).
The count-weighted identity for the present birth family is derived above;
no transport theorem from that paper is imported.

## 2. What follows when full occupation is reached

Start in a fixed even record-number sector n0. If the specified dynamics
satisfy Prob[N=K]->1, conservation of O_chi implies

    lim_(t->infinity) <T>_t
      = chi^((K-n0)/2) <T>_0.

This is valid for arbitrary coherent initial records within that sector and
arbitrary allowed motion satisfying the hypotheses, without specifying their
transient populations. A direct finite-time bound is

    |<P_(N=K)T>_t - chi^((K-n0)/2)<T>_0|
       <= |chi| Prob[N<K]_t.

For chi=0 the right side is zero: the full-sector coherence is exactly zero
at every time unless the initial state was already full. For |chi|=1 the
formula preserves magnitude, with the parity of the number of pair births
setting the sign when chi=-1. For |chi|<1 each required birth contributes to
the final reduction. The formula requires a common chi; spatially varying
instrument overlaps require a different calculation.

This theorem does not establish completion. The extreme-flux trapped sectors
in the earlier three-dimensional model prevent using a completion premise
there without an additional argument. The invariant itself remains true in
any charge-conjugation-invariant finite model satisfying its algebra, whether
or not some states become trapped. A fixed boundary electric field that is
not preserved by T falls outside this symmetry statement.

Electric-field monitoring differs from occupation monitoring in a checkable
way. Add jumps sqrt(delta_e) E_e on the spin-half links. Each E_e commutes
with N, obeys E_e^2=I/4 and anticommutes with T. Therefore

    L_total^dagger(O_chi)=-lambda O_chi,
    lambda=(1/2) sum_e delta_e.

With these additional jumps, its expectation is exactly
exp(-lambda t) chi^((K-n0)/2)<T>_0. The finite-time full-sector formula
above has this decaying quantity in place of the constant. If occupation
still completes and lambda>0, the terminal conjugation coherence is zero.
This concerns the specified global observable; it is why a completion proof
that does not require electric-field measurement is useful for this model.

## 3. A family with completion proved: an even gauge ring

Take an even cycle of length K>=4 with cyclically oriented spin-half links
and qutrit matter. In the zero-Gauss sector, link bits b_i determine

    Q_i=b_i-b_(i-1),
    n_i=1 if b_i!=b_(i-1), and n_i=0 otherwise.

All 2^K bit words are physical, and N is always even. Each even occupation
pattern has exactly two physical link words, related by complement. In this
representation T complements all link bits; it also reverses all the
determined matter charges.

The supplied ordinary gauge hopping flips b_i precisely when b_(i-1) and
b_(i+1) differ. It swaps one adjacent occupied/vacant pair, preserving N
and the charge carried by the moving record. Between the two corresponding
occupation patterns it is a unitary bijection of the entire two-dimensional
gauge fiber, with the same nonzero hopping amplitude kappa. It is a
three-link local operator in the reduced bit representation. The two birth
orientations flip b_i when the three bits b_(i-1),b_i,b_(i+1) are all equal;
this creates two opposite charges and increases N by two. Their total loss
is beta_i(1-n_i)(1-n_(i+1)).

Supply kappa!=0, positive occupation-monitoring strengths at every vertex,
and positive birth rates on every edge. Any H0 commuting with every n_i may
be included for the completion statement. The fixed-cardinality vacancy
exchange graph on the connected cycle is connected. For each even positive
hole count, it contains a pattern with two neighboring holes. The monitored
fiber-completion proof therefore applies to every initial physical density:
full occupation tends to probability one, with a finite-model exponential
survival bound and finite mean. Neither constant is claimed uniform in K.

For clarity, the proof uses stationary record-count drift to eliminate
birth support, the Hilbert-Schmidt dephasing identity to eliminate
occupation-pattern coherences, and the whole-fiber unitary hopping blocks
to equate the remaining positive block traces across all vacancy patterns.
One birth-contact pattern forces the nonfull sector's common trace to zero.
Finite-dimensional Cesaro compactness and the transient CP semigroup give
convergence and the stated finite-time integrability, as in the already
independently checked occupation-monitoring theorem. A connected classical
transition graph alone is not the quantum proof.

For the coherence identity and terminal density, also require [H0,T]=0.
No ordinary hopping is omitted in this ring family.

## 4. The complete terminal state from a supplied vacant gauge cat

Start in

    |Omega_empty>=(|00...0>+|11...1>)/sqrt(2).

It has N=0 and T=+1. The full-occupation sector contains just the two
alternating field words A=0101... and B=1010..., together with their
Gauss-determined matter charges. T acts as Pauli X on this sector.
The entire generator is covariant under rho -> T rho T: the real-chi birth
coefficient matrix is invariant under exchanging its two orientations,
the Hamiltonian commutes with T, and the other jumps commute with T.
The initial density is T-invariant, so every later density is T-invariant.
On this two-dimensional full sector, that forces equal diagonal weights
and a real off-diagonal entry. Completion and the conserved observable
therefore determine the entire limiting density:

    rho_F = (1/2) [[1,chi^(K/2)],[chi^(K/2),1]],
    <T>_F=chi^(K/2),
    Tr(rho_F^2)=[1+chi^K]/2.

The remaining full-sector H0 commutes with T, hence with this density, so it
is stationary. Off-diagonal full/nonfull blocks vanish as the nonfull
probability tends to zero by positivity. Thus the displayed matrix is the
limit of the complete density, not merely its time average.

At chi=1 this converts the supplied empty gauge cat into a pure alternating
matter/field cat while all sites acquire records. It transports a prepared
phase; it does not create that phase from a classical vacant field.
For 0<=chi<=1 the fidelity with the positive cat is
(1+chi^(K/2))/2. Retaining at least a prescribed coherence c in (0,1]
requires chi>=c^(2/K). At fixed |chi|<1 the specified global coherence
vanishes as K grows. This is a global-cat sensitivity, not an exclusion of
local quantum correlations or of a photon phase in another model.

Inhomogeneous positive birth and monitoring rates, and nonzero hopping
couplings, preserve this full terminal density whenever they satisfy the
stated charge-conjugation hypotheses. Translation symmetry is unnecessary.
The original draft's claim that such inhomogeneity could yield unequal final
populations was incorrect; its bytes are preserved in the source history.

The accompanying exact checker constructs every physical operator for
K=4,6,8. It checks each birth's symbolic dual identity, whole-fiber hopping,
occupation-graph contacts, the field-monitoring eigenvalue, terminal purity
and stationarity, and an explicitly translation-breaking Hamiltonian that
preserves T. An occupation-preserving electric term that breaks T is a
countercontrol. These finite checks support the general analytic arguments;
they do not substitute for them or constitute independent review.

## 5. Meaning for the campaign

Record formation and mobile-site reuse can coexist with preserved gauge
coherence in this conditional model. The environment's information about
charge orientation is a physically consequential part of the birth rule,
even when all instruments have the same instantaneous formation loss.
The primitive axioms do not select chi, the supplied gauge carrier or the
monitoring law; no empirical value is inferred here.

The ring is a one-dimensional test family. Its reduced link bits are not
an implementation of the fundamental three-dimensional site record algebra.
The global observable has an explicit meaning in the physical gauge sector,
but no native record-only readout or continuum electromagnetic identification
has been constructed. The negative large-size statement remains scoped to
this observable and instrument family and private pending the publication gate.
