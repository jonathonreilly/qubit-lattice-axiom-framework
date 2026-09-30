# Focused independent check of the physical phase and slab arguments

No material mathematical error was found in the frozen staircase/slab proof
47ab6e271099bd675216c0e82f16f580fad76a8642b6f1b8eafbbf2ca35ef533,
Laurent criterion fa1798cc1eaf4e873214627aa90b3ad289267dd48873a7523b9d19d17a3ca4ee,
and report 0f7870cf8d652d6da2f0a02e08ae30f32f63b15afd3491f545489c8df91a1efd.
The generic-phase exclusion holds for a dark eigenvector confined to the
declared hole slab. The full Laurent observability statement is an exact
criterion, with its decisive rank/source-overlap hypothesis still open.
The Krylov bound is a necessary depth bound, not an observability proof.
This is a focused mathematical check, not formal review, audit, a retained
judgment, or permission to infer microscopic closure.

## Reconstruction, exposure and complete source coverage

PRE be8b821fd74aa440329fcb33aefbde1d7386baa9228aa27c33403ba694185abc
was frozen at 2026-09-30T20:05:24.168945+00:00, before opening the new proofs,
report, code or results. Its exposure was the root task, CONTRACT, source
manifest, and target descriptions. It independently derived the physical
Laurent-kernel alternative, the two-matching staircase monodromy and the
highest-layer strategy. Its tentative Krylov approach used finite propagation;
the author's sharper dimension count was reconstructed after proof exposure.
No claim of pre-exposure discovery of that exact count is made.

I authored the older finite-cluster/periodic, response-geometry and actual
source late-tail arguments and checked other related responses in this
campaign. Those are disclosed shared prior inputs, not independent new
discoveries here. The new argument was reconstructed before comparison.
Root's independent PRE was not opened. An initial clock-prose typo in my PRE
was repaired before new-proof exposure; its original bytes and freeze remain
in historical/pre-time-wording. No mathematical PRE change occurred.

The entire new packet, including both contracts, attempts, proofs, report,
runner, guard, raw output and execution/preflight/failure records, was read.
The five bound current-main scientific notes were freshly read completely,
as were all eleven bound campaign inputs and the additional periodic
extension. In particular the actual cube proofs and their distinct
compensation/preparation were read, not inferred from their headlines.
The selected physics-loop entry, claim-status, discovery guidance, current
axiom registry and actual primitive declarations were read. Other unchanged
triggered procedural reads are reused from the continuous campaign and
identified in SOURCE_READ_AND_BINDINGS.json.

All 18 author frozen members, five main inputs, eleven campaign inputs and
twelve procedural/primitive bindings match their declared bytes. The author
freeze itself and additional periodic proof make 48 recorded identities.
Selected science is fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7; selected
method is 7146fe17a76de41badcaca3c3c7cac6d11eb2a00. Working scientific
bytes were compared with that main revision, rather than assigning its SHA
to the campaign working HEAD. No author scientific code was run, imported
or modified. No new scientific computation was needed.

## Actual physical domain and canceled operator

Use the contract's even cubic L>=8 torus, n=L^3/2, W=1, physical odd
1<=k=N_B<=n-1, total charge n, supplied qutrit matter and integer rotors.
There are M=n-1+k occupied sites and r=(k-1)/2 minus charges. Every B mask,
hole position, charge assignment and Gauss field remains in the carrier.
The six B neighbors are distinct on this domain.

I reconstructed the exact blocks of H=C+[F,F*], with
C=sum_a F_a*F_a Q_gate,a:

    P_h H P_h = P_h(F_h F_h* - sum_(d(a,h)=2) F_a*F_a)P_h,
    P_a H P_h = P_a[F_a,F_h*]P_h, a!=h.

On a dark input every B neighbor of h is occupied. For a shared B
intermediate, the negative ordering starts with an outward hop into that
occupied B and is blocked. The positive ordering first fills h, then moves
the occupied charge at a into the freed B. Distinct-intermediate paths
cancel with their actual charge/field translations. The surviving moving
block preserves the B mask. Same-hole negative reshuffles do remain in H;
they are not removed from general dynamics or eigenvector equations.

Original resolved and unnormalized coherent marks have the same diagonal
loss G=2 times the number of vacant B neighbors of h. They do not have the
same recycling instrument. This check uses the common loss for no-event
stability and retains complete original marks in the source discussion.

A fixed integer spanning tree supplies a Gauss completion for every charge
word of total charge n. The independent integer cycle lattice has dimension
3L^3-L^3+1=2L^3+1=4n+1. A chord hop changes one coordinate by its charge;
a tree hop changes no chord coordinate. Thus two-hop H entries are Laurent
polynomials of total absolute degree at most two. Charge-dependent tree
flows are part of this physical representation, not a scalar-charge
substitution. The qutrit/rotor dynamics, preparation, GKSL law, original
marks and clock remain supplied model premises; the actual axiom and
primitive declarations do not derive them or assign this packet status.

## Charge-coherent winding and broken domains

At fixed x and layer y+z=j, the alternating ring contains L A sites and
L B sites. U_y and U_z are bijections between the complete corresponding
charge fibers, with their exact unit phases. Consequently

    K=U_y+U_z=U_y(I+W),  W=U_y*U_z

is an identity of physical fiber operators. In each W step the vacancy
moves to the next A site through the intervening occupied B. After L
steps the vacancy returns and the 2L-1 charges are cyclically permuted;
after N_c=L(2L-1) steps all individual charges return. Counting primitive
transfers gives one complete circulation per charge and therefore

    W^N_c=exp(i Q_c Phi_c),  Q_c odd and nonzero.

The ring charge is conserved by W. It is a diagonal operator on the full
charge space, so the identity applies to arbitrary coherent charge
superpositions. Identical charge labels may return sooner; the common
power N_c remains valid. No probabilistic charge averaging is involved.

Since N_c is even, the alternating geometric sum gives I-W^N_c when
multiplied by I+W. Its norm is at most N_c. This proves the stated lower
bound min_odd_q |1-exp(iq Phi_c)|/N_c. Taking the minimum over odd charges
not realized in a particular global sector is conservative. The pi
holonomy on z-cut links is a simultaneous physical phase point: every
staircase has one z winding, and every allowed odd Q_c sees phase -1.
Gauging its tree links to one is a charge-basis unitary. The character is
nontrivial in the full physical cycle lattice, so its finite exceptional
union has Haar measure zero.

Missing occupied B sites produce open alternating chains. For r occupied
B sites, dark input holes occupy at most r-1 internal A sites. Successive
endpoint equations, after unitary edge transports, give
||x_j||<=sum_(i<=j)||v_i|| and hence ||x||<=r||Kx||.
The reverse map has r B-hole variables and r+1 A-hole output rows and
has the same bound by its endpoint equations. This reverse-domain check
matters: injectivity of a rectangular forward map alone would not imply
injectivity of its adjoint. The proof supplies both actual maps. Full
cycles are square and use the winding bound. Since r<=L, 1/L is safe.

## Highest-layer factorization and exact support limit

For a dark input on layer j, a move to j+2 must take two positive
transverse steps. With original B mask S kept as a proof-space tag, its
full block is exactly

    P_(j+2) H D P_j = K_out* K_in D P_j.

Both maps use all y/z paths and complete charge fibers. Different masks
give orthogonal final physical output masks, so their bounds combine
without cross-mask cancellation. The temporary tag prevents the false
global F* factorization; it is not a new physical label or an invariant
mask assumption. The reverse-map bound above yields eta(theta)^2 for
the product, including every output row. Neither compensation nor
same-hole reshuffles can change j to j+2.

For support in layers 0,...,w with w<=L-5, choose maximal nonzero j.
The j+2 eigenvalue row has no input at that layer and no other occupied
input within two layers, including periodic wrap. In particular j+4
does not wrap into the allowed lower support; the four-layer omitted
gap is sufficient. With only three omitted layers, a reverse two-step
path from the lower endpoint can reach that row in the limiting geometry.
The support margin is not silently weakened. Injectivity then contradicts
the maximal nonzero layer.

For the seven-layer occupied-B strip plus one parity site, a boundary A
hole has two distinct outward missing B neighbors. One extra B site
cannot fill both; more distant A holes have other vacant neighbors.
Thus dark holes are confined to the five inner layers. At L>=16 the
stated slab theorem applies, even to coherent mask/charge combinations
within that support family. The old flat-phase strip eigenmode lies on
the excluded phase set, with no contradiction.

The conclusion is about an eigenvector's full hole support. Absence of
such an eigenvector does not make an initially slab-supported state
orthogonal to extended dark eigenvectors. Nor does it prohibit a branch
through the flat-phase vector from expanding its support when phase
changes. These limitations are explicit in both new proof and report.

## Full Laurent criterion and actual-source certificate

For d_f=n binomial(n,k) binomial(M,r), stacking GH^j for
0<=j<d_f gives the maximal H-invariant subspace in ker G by
Cayley-Hamilton. Hermiticity makes it reducing for H; G also reduces it
because it vanishes there. On its orthogonal complement, a putative
imaginary-axis eigenvector of -i delta H-kappa G/2 would have zero loss,
and therefore belong to the excluded invariant dark space. Finite
matrix stability gives decay on that complement, including Jordan
blocks. On the dark space evolution is unitary.

Contractivity allows dominated convergence of fiber norms for every
normalizable physical vector. Positive rank-one decompositions extend
the terminal-mass formula to every positive trace-class input:

    terminal mass = Tr(P_N rho).

This argument does not replace rho by a phase-diagonal density or assume
that a trace-class operator is a multiplication operator. The integrated
original first-mark mass is Tr rho minus this terminal mass, by the exact
loss identity. It is independent of any unproved uniform phase rate.

The fraction-field rank alternatives are correct. A nonzero maximal
Laurent minor is nonzero almost everywhere on the unit torus. Deficient
generic rank supplies a rational null vector; clearing denominators
gives a nonzero Laurent vector killed by every GH^m. Its inverse Fourier
transform has finite support in actual cycle coordinates and finitely
many charge-dependent tree flows. It is a normalizable finite-field
physical vector with a dark H orbit, though not necessarily one H
eigenvector. No such null vector or full-rank minor is produced here.

The additional source certificate is genuinely additional. If a complete
legal zero-waiting original word Phi has nonzero Laurent overlap v*Phi,
a scalar Laurent shift of v selects a nonzero Fourier coefficient and
therefore a nonzero Hilbert overlap. Strong continuity of the actual
effective electric-plus-bounded no-event propagation preserves it for
small total waiting time, uniformly over this finite word's simplex.
The positive original quantum-jump expansion then gives positive source
weight for every sufficiently small s>0. No field point evaluation is
needed for this argument. Complete coherent marks must remain inside
Phi; a selected nonzero path alone would not prove the hypothesis.
Conversely, zero-waiting orthogonality cannot control the full source
orbit with interspersed electric/H4 dynamics. The proof preserves both
directions of this scope distinction.

## Krylov depth, evidence and remaining consumer

For a fixed hole, darkness means its six B neighbors are included in the
k-set. Hence the dark count is n binomial(n-6,k-6) binomial(M,r) for
k>=6. At k=n-1 the full-to-bright dimension ratio is n/6. Since every
block GH^j has rank at most d_bright, the stack through R can be full
column rank only if (R+1)d_bright>=d_f, or

    R>=ceil(n/6)-1.

For smaller R, fraction-field elimination indeed supplies a Laurent
null vector of that finite prefix. It does not supply an invariant
dark state or an Omega source. This count explains why the cube's
72-by-24 first bright/dark block cannot prove the torus assertion.
The cube's zero dark-dark block, exact minor, five-angle tail and
canonical input were not imported into the torus argument.

The complete author runner and actual capture were inspected without
execution. It checks formal integer charge coefficients in primitive
Gauss updates and circulation on L=8,16,24,32, restoring charge labels
after 120,496,1128,2016 two-hop steps. The actual run used 0.535318 child
CPU seconds, 0.549306 wall seconds and 15,532,032 bytes peak RSS, exit 0.
Its CPU/wall limits and postchecked RSS are stated accurately. The
earlier absent-python setup failure is preserved. All pre-execution
source hashes and output hashes match. These finite controls corroborate
monodromy; they neither establish full Laurent rank nor replace the
general charge/mask proof. This receipt adds analytic reconstruction and
source-integrity verification, not another scientific run.

The exact remaining fixed-torus consumer is a full observability
certificate or the weaker orthogonality of the actual evolving source
to P_N. The former is equivalent to all-sector strong no-event decay;
the latter is source-specific and needs its complete orbit. The slab
theorem closes neither. The old smooth-packet norm obstruction and actual
polynomial lower tail leave both possibilities open. Quantitative age,
field, spatial, finite-spin and full microscopic response estimates
remain separate even if strong rotor decay is eventually proved.
No normalizable sourced persistent dark mode, uniform rate, low-moment
failure, finite-spin conclusion, full energy bound or physical law
selection follows from this packet. No author correction is requested.

Only this assigned independent directory was written. The PR9412
worktree, author packet, root evidence, science sources and authority
surfaces were left untouched.
