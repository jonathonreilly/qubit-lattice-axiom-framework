# Coherent ring motion can complete formation without occupation monitoring

Date: 2026-09-22. Status: author conditional theorem and exact finite
observability certificates; independent scrutiny pending. The ring geometry,
Hamiltonian phases, local carrier and irreversible pair-birth law are
supplied. This does not select a native cubic-lattice dynamics.

## 1. A precise coherent alternative to the monitored construction

Consider hard-core vacancies on an even cycle with K>=4 vertices. In a fixed
h-vacancy sector use basis |A>, A a subset of Z/K of cardinality h. A vacancy
moving from x to x+1 has a nonzero complex amplitude t_x; the reverse has
its conjugate. Add any real diagonal configuration energy V(A). Let Gamma
be a positive diagonal loss supported on configurations with at least one
adjacent vacancy pair, and strictly positive on all such configurations.
Pair formation removes two vacancies and creates two permanent records.

Define the phase of the hopping product by

    exp(i Phi) = product_x t_x / |product_x t_x|.

The result is:

* For h>=3, no nonzero H-invariant subspace is contained in ker Gamma,
  for any choices of these nonzero amplitudes and diagonal energies.
* For h=2, the same statement holds whenever exp(2i Phi)!=1.
* Thus, with even initial h and this generic phase condition, coherent
  hopping plus the pair births completes occupation with probability one,
  a finite-model exponential survival bound and finite mean. No additional
  occupation-monitoring term is required.

Here and below, a loss at every possible contact is essential. A single
selected absorbing edge is a different model. These are finite-system
statements with no claim that the exponential rate is uniform in K or in
distance of Phi from the excluded values.

## 2. Amplitude induction with a third vacancy

It suffices to exclude an eigenvector psi of the self-adjoint H that
vanishes on every contact configuration. An invariant subspace of a finite
self-adjoint H has an eigenbasis. Let the minimum cyclic distance between
successive vacancies be m(A). Contact vanishing is the assertion

    psi(A)=0 whenever m(A)<=1.

Suppose inductively that amplitudes vanish whenever m(A)<=r. Choose a
configuration A with m(A)=r+1 and a consecutive pair x,y=x+r+1, with cyclic
indices. Keep all other vacancies fixed. Form B by moving x to x+1. Its
chosen pair has separation r, so psi(B)=0. In the eigenvalue equation at B,
the diagonal term vanishes. Every hop other than the two moves increasing
this pair separation produces a configuration still having distance at most
r, and hence zero amplitude. The remaining equation is

    t_x psi(A) + conjugate(t_y) psi(A')=0,

where A' translates the selected pair one step forward, from (x,y) to
(x+1,y+1), leaving the other vacancies fixed. At this stage both outward
moves are allowed, since all distances in A are at least r+1>=2.

When h>=3, at least one other vacancy remains fixed ahead of the pair.
Repeat this translation relation while all distances remain at least r+1.
After finitely many translations, the leading member approaches that fixed
vacancy to distance r. The last translated configuration then has zero
amplitude by the induction hypothesis. Every intervening coefficient is
nonzero, so the original amplitude is also zero. This kills every
configuration of minimum distance r+1. Induction proves psi=0.

This argument uses neither translation symmetry nor a rate approximation.
Arbitrary diagonal energies multiply amplitudes already known to be zero
and therefore do not enter the induction. It does require ordinary
nearest-neighbor hard-core hopping with the stated nonzero matrix elements;
extra off-diagonal terms could add terms to the boundary equations.

## 3. Two vacancies and the phase around the cycle

For h=2 there is no fixed third vacancy to terminate that translation.
Instead apply the same relation K times. The pair returns to its original
configuration. Each edge appears once in the numerator and once in the
conjugated denominator, so

    psi(A)=(-1)^K [product_x t_x / conjugate(product_x t_x)] psi(A)
          = exp(2i Phi) psi(A).

The last equality uses even K. If exp(2i Phi)!=1, this forces psi(A)=0.
It supplies the induction step for each possible pair separation, again
allowing arbitrary diagonal energies and nonuniform nonzero magnitudes.
A shorter translation orbit of an antipodal pair does not invalidate the
K-step identity. This proves the stated sufficient condition.

When exp(2i Phi)=1, this argument stops; it does not prove that a dark state
must exist for every possible diagonal energy or hopping magnitude. In the
uniform real-hopping H0=0 model, exact dark states are known and their
projection/dimension are given in TWO_VACANCY_QUANTUM_COMPLETION_CLOCK.md.
That preserved counterexample is precisely why generic connectivity of the
classical hopping graph alone was insufficient.

## 4. From the coherent contact result to continued formation

In each fixed positive even h sector, absence of an H-invariant subspace
in ker Gamma makes H-i Gamma/2 strictly decaying: an eigenvector with a
real eigenvalue would have zero expectation of Gamma, hence vanish on
contact and yield a forbidden dark H eigenvector. The finite-dimensional
no-birth semigroup therefore loses all of its trace exponentially. The
next pair birth occurs with probability one and finite mean.

There are at most K/2 such births before the vacancy count reaches zero.
The sector laws and birth gains together form a finite triangular transient
Lindblad generator. Each diagonal block has strictly negative spectral real
part, so the whole transient semigroup has an exponential bound (with a
possibly enlarged prefactor for Jordan blocks), and its time integral is
finite. This also follows from the stationary count-drift argument and
finite absorbing-corner analysis used in the earlier monitored theorem.

The coherent evolution conserves existing record contents while exchanging
vacancies with records. The specified irreversible gain creates two new
records only at vacant endpoints. Permanent record number is retained;
occupation of a particular site can change as records move away.

## 5. Application to the physical gauge ring and its preserved phase

Use the physical bit-word representation

    Q_i=b_i-b_(i-1),  n_i=1_(b_i!=b_(i-1)),  T:b->complement(b).

Every occupation pattern of even record number has a two-dimensional gauge
fiber. Give an ordinary bit flip at edge i the amplitude t_i if the hole
moves from i to i+1, and conjugate(t_i) for the reverse move. Both
complementary field words have the same occupations and therefore the same
amplitude. This Hamiltonian commutes with T, all Gauss constraints and record
number. It is still a local gauge-dressed content-preserving hop. Add any
H0 commuting with every n_i and with T.

Choose as representatives the field words with b_0=0. In the T=+1 fiber
basis (|b>+|complement b>)/sqrt(2), every hop has exactly the bare vacancy
amplitude t_i. In the T=-1 basis the hop at edge zero acquires one extra
minus sign, because that bit flip requires taking the complementary
representative. Thus the two sectors have total phases Phi and Phi+pi.
Both satisfy exp(2i Phi)!=1 simultaneously. H0 is a scalar configuration
energy within each of these one-dimensional T fibers, so it is covered
by the preceding proof.

The local birth family with common real chi and positive edge rates has
Gamma equal to its vacant-edge loss for every chi. Hence the completion
result holds in the full physical gauge space, including coherences between
T sectors. The usual positive count-drift argument eliminates all birth
support in a stationary state; any surviving H-invariant dark component
would have a nonzero projection into one of the two excluded T sectors.

The formation-count identity is unchanged: the Hamiltonian commutes with
T, and the coarse birth coefficient matrix is real and invariant under
orientation exchange. Starting from the supplied empty gauge cat, the
terminal density in the two alternating full-occupation words is therefore

    rho_F=(1/2) [[1,chi^(K/2)],[chi^(K/2),1]].

In particular chi=1 preserves its supplied positive cat phase while
occupation completes under coherent motion and birth alone. This uses the
count identity and charge-conjugation covariance, not translation symmetry.
It does not prepare a phase from a classical vacant mixture. The phase
around the hopping cycle is a supplied resource and is not predicted by
the framework; its spatial symmetry and native implementation remain open.

## 6. A second sufficient mechanism: monitor one site's occupation

There is also a finite-ring alternative that permits any Phi. Supply one
positive occupation-monitoring jump sqrt(d) n_z at one vertex z, retaining
the same ordinary hopping and diagonal-energy conditions. This suffices
for completion; monitoring every site is unnecessary in this ring model.

Only h=2 needs an additional argument, since h>=3 is already contact
observable coherently. A positive stationary transient density has zero
birth loss. The Hilbert-Schmidt identity then gives [n_z,rho]=0 and
[H,rho]=0. Its support would therefore have to be invariant under H and
n_z and contained in the contact-free space.

Split that support into n_z=1 and n_z=0. In the first block one vacancy is
fixed at z and the other moves on the open path formed by deleting z. The
two endpoints of this path are contact states. A tridiagonal path with
nonzero off-diagonal entries has no eigenvector vanishing at an endpoint:
the eigenvalue equation successively forces every entry to zero, regardless
of diagonal energies. In the second block the two vacancies move on the
same open path. The two-vacancy amplitude induction now terminates at a
path boundary: in the last boundary equation the outward move beyond the
endpoint is absent, leaving the nonzero coefficient of the candidate
amplitude alone. Back-propagation and induction on separation again kill
every amplitude. Thus neither block can contain the required invariant
subspace. Compressing H to these blocks is legitimate because the original
support is invariant under both H and the projector n_z.

The same argument applies separately in the two gauge T sectors, and n_z
commutes with T. This single-site monitoring retains the formation-count
coherence identity. Its location, strength and environment remain supplied,
and no size-uniform completion speed has been shown.

## 7. Exact finite checks and limits

coherent_ring_contact_observability_check.py constructs the ordinary hopping
matrices from subsets directly, without importing the earlier gauge or
mean-time runners. It starts with contact basis rows and closes their span
under H, and under n_0 where specified. Calculations use the proven prime
65537 and i->256, whose square is -1 modulo that prime. A full-rank minor
over this field certifies a nonzero minor over Q(i); a modular rank deficit
alone is not interpreted as a dark space.

For even K=4,...,14 it checks every even hole sector with uniform real,
quarter-turn and negative-quarter-turn hopping products. All generic-phase
cases and all sectors with h>=4 have full observable rank. The real two-hole
deficits are separately matched by exact rational dark projectors. It also
checks nonuniform real hopping magnitudes and a nonconstant diagonal energy
with one occupation monitor, analogous open paths without that monitor,
and a nonuniform generic-phase two-hole ring. These are 111 complete finite
cases. The gauge T-sector identifications are reconstructed directly for
K=4,6,8 and every even hole count. The first full execution passed.

The all-size amplitude induction is the load-bearing theorem; these finite
certificates are checks, not its replacement. The result removes a supplied
monitoring requirement for a conditional ring family. It neither removes
the irreversible birth environment nor proves a three-dimensional photon
phase, a native qubit-site realization, or a unique physical law. The
preserved real-hopping dark counterexamples retain their scoped meaning;
no universal negative conclusion or formal audit status is assigned here.
