# Local-dilute reconstruction, before author controls

The complete supplied note at SHA-256
34ab30936006b553c778d9b050b226e8270a653d278875eab966b445d776043c
has been read; its author checker/results remain unopened. This reconstruction
finds no actionable error in the stated finite-particle limit. It preserves
the distinctions between active-cell locality, a rotating-frame energy and
the original record dynamics.

## Physical Hilbert space and positive energy

For two actual qubits per cell, the singlet plus Cartesian triplet basis is
orthonormal. The local matrix units t_i=|0><i| allow zero or one excitation
in total, regardless of component. A physical n-excitation basis vector is
identified isometrically with the normalized boson occupation vector having
the same occupied cells and components. If a particle hops into an empty
cell, both physical matrix units and boson creation/annihilation have unit
amplitude. A hop into an occupied cell is excluded. This proves exactly

    H|_n = mu n + P dGamma(c C_N) P on Ran(P).

It is not an assertion about compressing the full free unitary. The cell
exclusion is essential: allowing two different triplet components at a cell
would give the wrong physical subspace.

With D_j^T=-D_j and commuting D_j, the two antisymmetries in the curl give
C_N^T=C_N. The Fourier matrix is i[sin(k) cross], so its norm is at most
sqrt(3). Therefore |dGamma(c C_N)|<=n c sqrt(3) on each n-sector. Compression
preserves this quadratic-form bound. The strict hypothesis mu>c sqrt(3)
gives H>=(mu-c sqrt(3))N_exc. The n=0 sector of the stated active-cell
Hilbert space is one-dimensional, proving uniqueness of its singlet product
ground state and the stated gap lower bound. This holds up to full filling,
without a dilute approximation. Proper cubic covariance follows from the
ordinary proper-rotation covariance of curl and the physical Cartesian
triplet action; reflection covariance is not asserted.

All coefficients are independent of N, adjacent cell terms have support on
at most four qubits, and the supplied fine packing has support diameter at
most three Manhattan steps: the largest coordinate displacement between
sites in adjacent active pairs is 2e_i+/-e_1. Its preferred pair direction
does not have full fine-lattice cubic covariance. Also, if the six unused
qubits per coarse cube were retained as unconstrained decoupled degrees of
freedom, the enlarged Hamiltonian would have ground-state degeneracy. The
uniqueness claim belongs to the specified active two-qubit-cell system;
uniqueness on an enlarged fine Hilbert space would require fixed or pinned
spectators. The source uses the packing only to assert support locality.

N_exc is conserved. Removing mu N_exc is an exact rotating-frame change,
not an approximation. The laboratory Hamiltonian stays positive and gapped.
The carrier-subtracted one-particle curl has both signs when sin(k)!=0.
Thus positivity of the laboratory energy does not establish a positive
gapless electromagnetic energy in the rotating frame.

## Uniform collision bound and the growing-time estimate

Let E be the three-polarization span of s distinct Fourier wavevectors on
the N-torus, with V=N^3. Each compressed position projector E A_x E has
three rank-one blocks with sole nonzero eigenvalue s/V. In labeled
first-quantized n-particle coordinates, the pair-collision events commute.
The indicator of any collision is at most their sum, giving for every
normalized vector in Sym^n(E)

    ||Q psi||^2 <= sum_(a<b) sum_x <A_x^(a) A_x^(b)>
                 <= binomial(n,2) s^2/V = delta_N^2.

The product compression has norm (s/V)^2 even for an entangled n-particle
state; no factorization is assumed. C_N acts within polarizations at fixed
momentum, so free evolution preserves Sym^n(E). The same bound holds at
every real time, with no time-dependent spatial spreading estimate required.

Let U_0=exp(-itL), L=dGamma(c C_N), U_hc=exp(-itPLP) on Ran(P). The derivative
of P U_0(t)psi satisfies its projected evolution with source P L Q U_0(t)psi.
All sector operators are bounded, so variation of constants directly gives

    ||U_hc(t)Ppsi-PU_0(t)psi||
      <= |t| n c sqrt(3) delta_N.

Set alpha=||Ppsi|| and phi=Ppsi/alpha. For delta_N<1,
1-alpha=(1-alpha^2)/(1+alpha)<=delta_N^2. Adding the missing Q component and
the normalization change yields exactly

    ||U_hc(t)phi-U_0(t)psi||
      <= delta_N(1+n c sqrt(3)|t|)+delta_N^2.

There is no missing 1/alpha factor: normalize by comparing U_hc phi with
U_hc(Ppsi), whose norm difference is 1-alpha. At t=N tau, fixed n,s,T,
the bound is O(N^-1/2) in d=3. For n=0,1 the hard-core/free comparison is
exact. The subsequent sine-to-continuum comparison is still generally
inexact for n=1.

For Q=2pi q the one-particle symbol error is

    c ||N sin(Q/N)-Q||_2 <= c |Q|_2^3/(6N^2).

Here sum_j |Q_j|^6 <= (sum_j Q_j^2)^3. Its n-particle second quantization
has norm at most n times the largest fixed-mode error. Finite-dimensional
Duhamel on scaled time |tau|<=T gives the source's equation (9). The physical
state is compared after its isometric embedding, while the free fixed-mode
spaces are identified across N by their Fourier labels. Coefficients
independent of N specify the common target vector.

The proof neither estimates collision errors at positive density nor controls
a growing number of Fourier modes or unbounded scaled times. A small
per-time collision probability alone would not in general control arbitrary
long evolution; the explicit N factor in this estimate is load-bearing.

## Mode algebra and signs

Exact local algebra gives [t_i,t_j^*]=delta_ij(I-n)-|j><i| and [t_i,t_j]=0.
Summing its Fourier phases gives delta_ij delta_(q,q') minus a sum of two
operators supported on occupied cells, divided by V. On each fixed set of
at most m occupied cells, each of the two sums has norm at most m, including
arbitrary phases. The operators preserve that occupied set, so their direct
sum over sets has the same bound 2m/V. This proves equation (10) without
independence, and the diagonal constant can be sharp.

For a real symmetric one-particle curl h, dGamma(h) has real-space quadratic
form 1/2(Q^T h Q+P^T h P-tr h). Canonical commutators then give Q_dot=hP,
P_dot=-hQ. This proves the displayed signs after carrier subtraction, with
onsite canonical bracket rather than the derivative bracket of the previous
positive block construction. Longitudinal and extra sine-zero branches are
kept. Bounded-observable matrix elements follow from the vector norm bound;
general unbounded moment convergence is not inferred from it.

## Independent finite controls

The separate checker constructs actual three-dimensional side-3 and side-4
curl matrices using epsilon components and verifies all 24 proper signed
permutation symmetries. It assembles the physical two-excitation Hamiltonian
directly from allowed empty-cell hops, independently assembles the free
two-boson Hamiltonian with occupation square roots, and finds exact equality
of the compressed matrices. Dimensions are 3159/3321 and 18144/18528
(physical/free). This checks cell exclusion and the hopping coefficient.

An entangled superposition of a doubly occupied Fourier mode and a two-mode
state uses S={(1,0,0),(0,1,0)}. The checker evolves its free state by separate
3-by-3 polarization matrices and its physical state by the independently
built full two-particle generator. The initial collision probabilities are
1/27 and 1/64. At tau=.1,.5,1 all uniform collision, forcing and Duhamel
bounds hold. The independent one-particle free reconstruction agrees with
the free two-particle exponential to below 2.01e-16. The side-3 two-particle
laboratory bottom is approximately .81350713, above the proved .61435935
lower bound for c=.4, mu=1. These floating spectral/dynamic values are
corroboration, not exact rational bounds or a scaling proof.

The local commutator identities are checked exactly, including saturation
of the diagonal 2m/V estimate for m=2. The sine remainder is tested on three
modes at both side lengths. The sole independent run exited zero with
empty stderr; there was no failed attempt. Author controls remain unopened
at this document's pre-comparison seal.
