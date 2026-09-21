# Finite-qubit positive curl: bounded independent review

**Disposition:** no actionable mathematical error or source/checker drift found
within the supplied fixed-volume, fixed-time construction. The common-Fock
operator estimate and its Duhamel consequence hold with their stated ordering
of limits. This is an independent scientific check, not formal retained status
or evidence of an implementation by the original immutable-record dynamics.

The complete primary note was read before author controls. The reconstruction,
independent checker and raw results were sealed first in
`PRE_COMPARISON_SEAL.json`, SHA-256
`5442ffb34a2506081b3bc07bcb6c1b36a9f8c6e262f5c4ef74f781f02dc9ee23`.
Only afterward were the complete author checker, all result groups, run logs
and analytic-vector receipt read. Primary files were not edited or executed.

## Mathematical reconstruction

The supplied occupation representation is an exact invariant subspace of
actual qubits: K two-qubit singlet/triplet factors give
Sym^K(C^4), dimension binomial(K+3,3). Counting normalized words gives the
source's lowering and raising coefficients. The common-space formula must
have the stated order `f_K(N_x) a_i`; its adjoint is `a_i^* f_K(N_x)`.
The physical sector N_x<=K is reducing, including its upper boundary. The
extension annihilates the one-cell sector above K. The exact finite-K
commutator is deformed, and no finite-dimensional canonical CCR is assumed.

The scalar cutoff estimate holds both below and above K. Writing N for total
occupation, each annihilation/creation defect is bounded by
`K^-1 ||(N+1)^(3/2) psi||`. For quadrature products, the decomposition
`A_K B_K-A B=(A_K-A)B_K+A(B_K-B)` gives a sufficient coefficient
`2+3 sqrt(2)` in front of `K^-1 ||(N+1)^2 psi||`, multiplied by the two
linear coefficient l1 norms. Thus, for M=3|Lambda|,

    ||(H_K-H)psi|| <= C_Lambda/K ||(N+1)^2 psi||,
    C_Lambda=(5M/2)(2+3 sqrt(2))

is one explicit, unoptimized valid bound for the supplied centered curl.
The finite-particle-core inequality extends to the stated weighted domain.

The finite quadratic H is symmetric and positive on a dense invariant
finite-particle domain. Repeated action costs at most a constant times
`m+2j+1`, giving analytic vectors and essential self-adjointness. The external
criterion was subsequently checked against Simon's Theorem 1.7; see
`LITERATURE_RECEIPT.json`. Its hypotheses are met. This use is an established
theorem import with a verified application, not a new proof of the external
functional-analysis theory. [Simon, PDF pages 9–10](https://math.caltech.edu/SimonPapers/R4.pdf)

Orthogonally diagonalizing the finite real symmetric curl reduces the moment
question to finitely many oscillators and free coordinates. Their exact
linear Heisenberg evolution preserves Schwartz vectors, with bounded
polynomial moments on compact time intervals. Zero frequencies therefore
cause no missing fixed-time domain argument. Duhamel yields

    sup_|t|<=T ||(exp(-itH_K)-exp(-itH))psi||
      <= C_Lambda T/K sup_|s|<=T ||(N+1)^2 exp(-isH)psi||.

For fixed finite-particle psi this is O(1/K). Bounded observable expectations
inherit convergence. The same weighted estimate for linear generators gives
Weyl convergence. Finite products can be telescoped using canonical
intermediate Schwartz vectors; this avoids an unproved uniform moment bound
on H_K-evolved states. No claim about arbitrary unbounded observables is
needed. `INDEPENDENT_DERIVATION.md` records the details and explicit constants.

The real-space curl is self-adjoint, with div C=0. In the limit E=-P and
B=CQ, the cross commutator is iC and the equations are
E_dot=C B, B_dot=-C E. The Fourier symbol is i[sin(k) cross]. Its zero modes
are retained: one momentum on odd tori and eight on even tori. Magnetic Gauss
is an identity for this readout; electric Gauss is conserved but not imposed.
The occupation vacuum is not asserted to be the Hamiltonian ground state.

## Independent and post-comparison controls

The pre-comparison checker explicitly embeds normalized symmetric occupation
states in full pair tensor spaces for K=1,2,3, verifies all three lowering and
raising intertwiners and all nine commutators, and checks coefficient errors
at, below and above four selected cutoffs. Actual spatial curl and divergence
matrices for side lengths 3 and 4 have exact ranks (52,26) and (112,56), and
the corresponding E/B bracket ranks are 104 and 224. These exact controls
include the even-torus extra zeros.

An independently chosen one-cell positive quadratic example C=diag(1,0,1)
tests the shared occupation cutoff and a free coordinate. It includes each
entire finite physical sector for K=2,4,8,16,32,64, and uses two distinct
finite-particle initial states at three times. Canonical reference cutoffs
80 and 100 differ by at most 3.89e-15. All 36 finite evolutions stay in the
physical sector; the observed K-scaled errors are at most 6.122. This is a
numerical corroboration of the fixed-time proof, not a simulation of the
full spatial lattice or evidence for uniformity in time/volume.

After the seal, `compare_author.py` authenticated the author's source bindings
and all three group JSON files against the combined result. It independently
assembled the quadratic matrix directly from monomial coefficients, reproducing
all six reported weighted core norms to at most 5.56e-17. A dense spectral
calculation independently reproduced all six K=4 Weyl rows to at most
6.72e-16. All 24 Gaussian targets, dimensions and saved error calculations
were checked. The K>4 finite-Weyl trajectories were authenticated, not rerun.
The author's sparse matrix controls and our comparisons clearly distinguish
floating-point dynamics from exact occupation/curl identities. Their numerical
frequency example is explicitly scoped to one block.

Both independent runs exited zero with empty stderr. There were no failed
attempts in this packet. A combined tool display truncated unrelated portions
of the web PDF output; the required two PDF pages were then read separately
from the authenticated local PDF. No mathematical conclusion depends on that
truncated display.

## Scope and remaining obligations

The proof fixes volume, time horizon, initial vector and smearing list before
K tends to infinity. Its constant grows with volume and its number moments
can grow with time. It supplies neither a uniform thermodynamic estimate nor
a joint continuum limit. The common-space representation is a tool for a
specific invariant block of a newly stipulated positive Hamiltonian.

The source correctly leaves fine-lattice locality/interaction control as block
size grows, preservation of the original record projectors, coupling to
formation and electric-Gauss state selection unresolved. Centered-difference
zeros, longitudinal/free coordinates and the difference between coarse
couplings and fine local interactions remain explicit. The finite controls
do not supply those missing physical bridges.

## Identities and reproduction

All exact source/artifact bindings are in `FINAL_SEAL.json`. Principal sources:

| Source | SHA-256 |
|---|---|
| DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md | 2448a007eb36de39c3b71db88190af5eec858b6c21a65d005f4229f4ff477010 |
| dimer_finite_qubit_curl_check.py | ece62b774654458b29c94fe07766742d586a483c45e4711ff25157076a8cee3d |
| Author RESULTS.json | 2812c4143491b41996fc8380c6b0f535f6ca568ba55bc5615204dacd83a74487 |
| Author analytic-vector receipt | 95560e69c1ab9c3501ccc4341ad9161ec37ef308e3801edace2bbfbc230e6db0 |
| Independent checker | 083a35b54c5774dbdd1ba4edc06d6e8f3462c8052fc2432bc364a8319f536a9c |
| Independent comparison | 63d9198e83b662db4a493817bb50f7b3dc6894720de9bfcf311b4aaa17501eec |

Run `python3 independent_check.py` and `python3 compare_author.py` from this
directory with NumPy, SymPy and SciPy available. They write only their own
result files. Original raw stdout/stderr and command/source-hash receipts are
preserved. Reproduction may refresh local result timestamps; the original
seal records the reviewed bytes. Previously sealed mixed-encoding evidence
was reused at its recorded identities and was not changed.
