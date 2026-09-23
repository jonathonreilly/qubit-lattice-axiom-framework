# Source-bound balanced-formation and locality comparison

No required mathematical correction was found in the two authorized theorem
notes. The effective generator, complete finite-time error proof, repeated-star
dark weights and later-event law, local decomposition, and fixed-volume rotor
passage agree with the independently sealed reconstruction, subject to the
explicit hypotheses and limits below. This is a bounded scientific comparison,
not formal retained/audit status or a publication decision.

The blind REPORT.md and PRE_COMPARISON_SEAL.json remain byte-identical:

- REPORT: `89210e10b9568544b9ffc4850c4c5402f4c901e8294819cdf60f96d4c0c238d3`.
- PRE: `f86695b6172745df8dc9ba8a1bfeaa60492ef7baf63a56bc55d045c5e8db951b`.

The comparison was authorized after that seal. It does not retroactively make
the new checks part of the blind reconstruction.

## 1. Source identity and actual read boundary

The two authorized author seals are:

- FINITE_RATE_FORMATION_AUTHOR_SEAL.json:
  `e0f07e9879e8332d17b1e96884c8942d21db4bdb4f7fe547d0bad3ed90ddd6ab`.
- FORMATION_LOCALITY_AUTHOR_SEAL.json:
  `150c0877855ba00dd7369733c0cefd0639a003cce6b290873ee59f14f415acd2`.

All 29 listed binding rows, representing 27 unique paths, authenticate. The
first seal itself is a dependency listed by the second. All 34 PRE bindings
also authenticate unchanged. The fully read scientific notes are:

- FINITE_RATE_REPEATED_RECORD_FORMATION.md:
  `b577c14e992fe74feb8a9f17c33e503f446f7052f83512031c2bf82cf2e3538d`.
- LOCAL_FINITE_RATE_FORMATION_AND_ROTOR_LIMIT.md:
  `1d3aad074b15777a20ef09f90bc1ca1ce4a55f441299ad2187b50b4b3cc6b976`.

The complete balanced runner repeated_formation_check.py, dark-law runner
repeated_formation_dark_check.py, locality runner formation_locality_check.py,
balanced working specification, source-context receipt, and their relevant
complete logs/receipts were read. Both complete balanced/locality JSON result
objects were parsed; all basis words and all 144 numerical evolution rows were
consumed by the comparison checks. The complete dark-weight result was read
and independently reconstructed.

The separate FINITE_RATE_RENEWED_FORMATION_EXACT_STAR.md, its working
specification, finite_rate_record_formation_check.py and associated result,
streams and receipt were **authenticated only**. Their different-scaling
theorem was not mathematically reviewed here. The shared seal does not extend
this comparison's disposition to that theorem. The contextual Reiter--Sorensen
citation is not a theorem import in the reviewed proof; this comparison did
not undertake a separate literature read or verify the author's historical
read receipt.

The newer fixed-fourth-order/repeated-formation notes, their runners/results,
campaign checkpoint and registry were not opened. No author source or previous
independent artifact was edited.

## 2. Model, number offset and effective generator

The author uses exactly the supplied bipartite charge/spin model, with W
counting A vacancies and the coherent channel j_++j_- carrying no extra
normalization. Both instruments have the same Gamma and different recycling.
Gauss, unchanged transported charge, [W,j]=-j, [N,j]=2j and PTP=jP=0 are used
correctly. The non-Hermitian resolvent exists because its Hermitian real part
is m delta I, even when a fast excited basis state cannot decay. This covers
the lossless W=1 and W=2 configurations in the independently checked path.

The author's A1 is this packet's V_+/delta, its D_m is our K_m, and its Y,Y2
are our X,Z. Its effective jumps have the common opposite sign to ours;
D[J]=D[-J], so the generators agree. No relative channel or route sign was
discarded. The checker verifies all bare hopping, W and birth matrices on
the complete 6-,45-,9-dimensional sectors after the necessary basis mapping.
On the path, the author's middle edge is B1->A2, while the blind builder used
A2->B1. The electric coordinate and resolved charge mark on that edge both
reverse. The comparison checks this orientation conversion exactly; it does
not compare unmatched basis entries or silently change the convention.

The relation to H=Delta N_B+tT is correctly restricted. Since
N_B=W+N-|A|, the difference is Delta(N-|A|). It has no effect on densities
commuting with N, and the stated generators preserve that number-block
property. It need not be dropped for arbitrary coherences between different
N sectors. The formal balanced theorem for H'=Delta W+tT itself allows any
P-supported density, as stated. The energy-offset identity is not a fuel
construction; the original energy per produced pair still scales with Delta.

## 3. Embedding normalization and full error argument

The sole embedding difference is

    S2_blind(rho)-E2_author(rho)
       = -1/2 P{X^dagger X,rho}P.                           (1)

This lies wholly in the slow P block and is annihilated by L0. Thus it changes
neither the three cancellation identities nor L_eff. The author's embedding
has trace 1+epsilon^2 Tr(X^dagger X rho) on a density; it was never required
to be trace preserving or positive. Both embeddings are Hermiticity preserving.
The author applies trace-norm contraction only to the actual CPTP semigroups
and their Hermitian defects, which is valid without positivity of the
polynomial embedding.

The author's smaller bound a2<=2M^2, versus this packet's convenient
trace-normalized bound 3M^2, is consequently valid. It is not a discrepancy
in convergence constants: the maps being bounded are different.

All the load-bearing blocks in the proof were reconstructed: Q1-P cancellation;
Q1-Q1 cancellation with recycling back to P; Q2-P and P-Q2 cancellation; and
the resulting P Lindblad operator. The resolvent identity supplies exactly
the anticommutator loss matching the returned jump term. The defect is

 epsilon(L1 E2-E1 L_eff)-epsilon^2 E2 L_eff.

Including both endpoint embedding errors gives the displayed O(epsilon)
finite-time bound. No fast population gap, factorization, asymptotic kernel
projection, or long-time limit is hidden in this step. As a selective new
control, all 16 path matrix units for each instrument were checked exactly
at the author's delta=13/10,kappa=7/10, with the author's unnormalized map;
the normalization difference in (1) is separately annihilated exactly.

The finite-register extension is also sound in its stated form. Register
updates attached to jumps have the same loss on the physically reachable
subspace before overflow. The finite capacity bounds the number of possible
marks, and piecewise interval tags yield a finite concatenation of the same
estimate. This controls joint register/output states and a fixed finite list
of event CDFs. It does not assert total variation convergence of unrestricted
continuous-time histories or a uniform bound on normalized conditional states
after arbitrarily rare postselection. The final theorem's wording preserves
that distinction.

## 4. Exact dark weights and the complete later-event law

The blind packet independently obtained the six-dimensional exact dark kernel
and the trapped weights 1/3 and 4/15 before author access. The additional
post-comparison calculation reconstructs every spectral weight from the
independent electric-sector builder. For M=A3^dagger A3 the multiplicities
are 0(6),1(3),2(3),3(2),5(3),6(1). Its spectral weights are exactly:

| Instrument | w0 | w1 | w2 | w3 | w5 | w6 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Resolved | 1/3 | 0 | 1/6 | 0 | 1/3 | 1/6 |
| Coherent | 4/15 | 0 | 1/3 | 0 | 1/15 | 1/3 |

These agree with the full author table. The initial N=1 no-event state has
one bright excited direction, so the normalized density after the first
event is independent of its time. In N=3, the effective Hamiltonian and
total loss are scalar multiples of M. Therefore the trace of the subsequent
no-event state is w0+sum_{lambda>0} w_lambda exp(-b lambda u), with
b=2kappa delta^2/(delta^2+kappa^2). Convolution with the first exponential
clock yields equation (8), including its coincident-rate limit. This uses
the actual post-jump density rather than assuming independent identical
waiting times or a closed classical occupation process.

The finite microscopic proof also holds. In a positive singular-value block,
the non-Hermitian excited energy is Delta-i beta: its *amplitude* damping
is beta, because the total population loss there is 2 beta. This is the
consistent interpretation of the author's phrase "excited decay beta".
Nonzero t sqrt(lambda) prevents a loss-free eigenvector in any bright block.
Only ker A3 survives, and it is an exact dark subspace of the full microscopic
Hamiltonian and births. Thus the all-positive-parameter eventual second-birth
probabilities 2/3 and 11/15 are established independently of the scaling
limit. Neither statement asserts filling of a different graph or a different
Hamiltonian/instrument.

The comparison independently reconstructs every one of the 144 stored
effective event-count rows (both stars, instruments, four epsilon labels and
nine times). The largest discrepancy is 5.56e-16. All stored effective
energy/count identities agree within 4.45e-16. Stored full-dynamics rows were
also checked for normalization, nonnegative probabilities up to roundoff,
error/epsilon bookkeeping and the elementary energy comparison bound.

Two quoted full 45-state endpoints were independently evolved from this
packet's microscopic matrices, at delta=1.3,kappa=0.7,epsilon=0.025,t=2:

| Instrument | Independent full probability | Independent trace error |
| --- | ---: | ---: |
| Coherent | 0.7250237000531465 | 0.002394762842062983 |
| Resolved | 0.6623528314098517 | 0.0012154613901256255 |

The respective author differences are below 7.0e-14. The entire author
evolution grid was not rerun. Those two finite endpoints corroborate the
implementation and quoted values; they are not the proof of convergence or
the exact infinite-time dark weights.

## 5. Locality, uniform spin bounds and rotor passage

The one-hole loss is block diagonal in the vacant A site. Its inverse acts
within the corresponding star; two-hop return or a birth must refill that
same A site to reach P. This proves the author's exact local H_a and l_e
decomposition, including coherent interference within each channel. A
restriction to the physical Gauss subspace does not enlarge the support of
these local tensor-product operators.

The degree-dependent estimates are correct: ||h_a||<=z_a,
||H_a||<=delta z_a^2 and sum ||l_e||^2<=2kappa z_a^3. Normalized integer-spin
shifts have norm at most one; combining the two resolved outward charge maps
does not double their norm because their charge sectors are orthogonal. A
coherent birth has norm at most sqrt(2). The induced generator bound and the
global fixed-volume bounds follow. Uniform local coefficients at fixed
degree do not constitute a volume-uniform microscopic approximation, and the
note explicitly avoids that inference.

The comparison checks the local decomposition exactly on all three complete
models for both instruments, coherent/resolved effective-loss equality, and
all 66 stored star basis rates. The rotor basis-state intensity formula is
an instantaneous statement with unit link amplitudes and available charge
shifts. The named star controls satisfy those conditions. It is not a rate
law for arbitrary coherent densities, nor may unit weight of the *remaining*
legal finite-spin shifts alone justify ignoring blocked channels on some
different graph. The general finite-spin theorem instead uses the complete
Gamma-dependent resolvent and remains valid with blocked births.

The rotor extension is valid on the stated fixed graph. W, shifts, hopping,
births and the resolvents are bounded; no E^2 energy term is included. The
zero-extended U_S and adjoints converge strongly, and the uniformly bounded
resolvents converge by their exact resolvent identity. Multiplication on
trace class converges by finite-rank approximation, yielding the effective
semigroup limit uniformly on compact times. Electric cutoffs commute with
P and Gauss and preserve the finite-spin dynamics, so normalized cutoff
initial densities approximate every physical P trace-class density. The
S-independent O(epsilon) estimate then proves the joint limit without a
required relation between S and epsilon. Operator-norm convergence of spin
shifts is neither used nor asserted.

## 6. Failures, evidence limits and disposition

The first comparison helper failed because it used structural symbolic
equality between a rational rate and the author's equivalent unevaluated
complex-factor expression. The exact diagnostic showed zero mathematical
difference. It was repaired by testing simplify(lhs-rhs)==0, with no
tolerance or model change. The old helper, exit-one receipt, streams and
diagnostic are preserved under failed_attempts/comparison_rate_equality/.
The earlier blind helper-labeling failure and PRE files remain untouched.

The final comparison checker exits zero in 5.76 seconds; its full streams,
receipt and COMPARISON_RESULTS.json are retained. It loads only the already
read balanced author's function definitions for operator mapping; it does
not execute the author's main routines or overwrite any author result. The
independent physical matrices, spectral reconstruction and two selective
Liouvillian evolutions use this packet's separate builder.

No unresolved mathematical repair remains for these two notes within their
stated finite-graph/model scope. This does not close a photon coexistence
limit, fuel/energy supply, native model selection, unrestricted path-law
limit, general completion theorem, or a volume-uniform microscopic estimate.
In particular, this balanced scaling sends the earlier fourth-order scale
delta epsilon^2 to zero. The authenticated different-scaling three-site
theorem and unopened later fourth-order packets retain their separate proof
obligations. Source/evidence identities and exact comparison scope are bound
in FINAL_SEAL.json.
