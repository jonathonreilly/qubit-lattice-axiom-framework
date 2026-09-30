# Focused independent check of the native canonical block transfer

This is a source-bound analytic check, not a formal review, audit verdict,
retention decision or independent derivation of every imported theorem.
No material error was found in the frozen transfer proof at its stated
ordered-limit scope. No correction is required by this check.

The checked author proof is
`native-canonical-block-transfer-route/WORKING_PROOF.md`, SHA256
`0d58d27217fa2f0d22daec41436370abe3cb888815d4650ceb65b0e9b2792be1`.
The actual supplied Hamiltonian and its normalization are unchanged. The
new consequence is an exact-particle-number dilute upper bound for every
integer sequence with a fixed limiting positive density. Combined with the
separately checked all-state lower bound, it identifies the two ordered
canonical dilute energy envelopes. It does not establish equality of those
envelopes at each fixed nonzero density.

## 1. Independence, exposure and source closure

`PRE.md`, SHA256
`8f3248a2654c03ece2ea0d67f4b811c63992381297e2f709eeb8ed5f9311ca15`,
was frozen before opening the author's proof. The parent brief and contract
had already disclosed the block-sector method, reserved sites, the intended
seam coefficient and order of limits. This is an independent reconstruction
with that method exposure, not a claim of blind discovery.

I authored the earlier particle-tail/lower composition and the separate
mean-density composition. That authorship is not independent validation of
those inputs. The lower's parent focused check is an explicit dependency.
My separate mean-density composition is not needed as a premise of this
canonical check. I also performed an earlier focused check of the actual
unitary upper construction; both that receipt and its author proof were
freshly read in full for the present task. The present precomparison used a
vacuum-remainder rounding convention, whereas the author places the final
rounding remainder in the full-occupancy sector. I checked the author's
actual convention independently after the PRE freeze.

The actual landed native density note was refreshed at main
`fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7`; its exact bytes have SHA256
`7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0`.
The complete relevant old upper and lower arguments and their receipts
were read; selected methodology revision remains
`7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Full identities and read scopes
are in `SOURCE_BINDINGS.json`. No author code was executed or imported.

## 2. Actual carrier and upper normalization

The carrier is one qubit at each physical lattice site, with number
spectrum 0 through V. On a periodic cube of side at least five the actual
native Hamiltonian has the finite-range grouping

    H_L = sum_x h_x,       [H_L,N] = 0,
    supp h_x subset x+[-2,2]^3,
    ||h_x|| <= h_* = 182 mu + 240 tau.

The actual SOS gives H_L >= 0. The comparison below uses only the stated
norm bound on each grouped term, not positivity of each h_x. Every integer
number sector is nonempty on the original qubit tensor product. No dimer
isometry, bosonic commutation relation or independent-pair carrier occurs.

Let t_0 be the minimum of the physical full fifteen-channel threshold form
on normalized coherent tensors z tensor z. For a fixed normalized z and a
fixed compact physical correction chi, the checked actual uniform unitary
trial has threshold value t_chi and bounds

    energy per site <= (t_chi/2) u^4 + D_chi |u|^6,
    |density - 2u^2| <= B_chi u^4.

The factor 2 in the number expansion and the factor 1/2 in its quartic
energy are those of the actual pair pulse and physical incoming threshold
normalization. They give t_chi/8 after elimination of u. Constants are
uniform in sufficiently large periodic volumes for each fixed compact
chi; no uniformity as chi approaches the relaxed infimum is imported.
Finite compact corrections approximate t_0 without requiring an l2
threshold minimizer. The earlier upper proof supplies that assertion.

Put v=u^2 and take B rho <= 1. At v=rho/4 the upper density bound is below
rho, and at v=rho the lower density bound is at least rho. Finite-volume
continuity supplies an exact mean-density parameter v in this interval.
This argument requires no monotonicity or typical-number concentration.
It gives

    |v-rho/2| <= B rho^2/2,
    v^2 <= rho^2/4 + B rho^3/2 + B^2 rho^4/4,
    v^3 <= rho^3.

Consequently the author's bound

    e_ell <= t_chi rho^2/8 + (D_chi+3t_chi B_chi/8) rho^3

is valid uniformly over the allowed block sizes. The displayed constant
is safe; B rho <= 1 is exactly what bounds the last quartic contribution.

## 3. Exact integer transfer, including odd target numbers

Fix the block side ell, let m=ell^3, and dephase the tuned block state in
N. Commutation of H and N preserves its mean and energy. For its sector
probabilities p_k choose normalized sector states tau_k. If p_k=0, any
state in that nonempty sector can be chosen. Write E_k=Tr(H tau_k), so
sum p_k E_k=m e and |E_k|<=h_*m.

After reserving r of the B=floor(L/ell)^3 full cubes, the author uses B'=B-r
active cubes and the literal integers

    n_k=floor(B' p_k) for k<m,
    n_m=B'-sum_(k<m) n_k.

They are nonnegative and sum to B'. The first m rounding errors lie in
(-1,0], and their opposite sum is the last error. Therefore

    sum_k |n_k-B'p_k| <= 2m,
    |N_reg-rho m B'| <= 2m^2 = D_m,
    |sum_k n_k E_k-B'm e| <= 2h_*m^2.

These estimates are deliberately loose but valid. In particular, using
the last sector when p_m=0 is legal: its full-occupancy state exists. A
tensor product of the selected sector density matrices has exactly N_reg
particles, even when an individual density matrix is mixed within its
sector. There is no variance or normalization penalty to suppress.

For any prescribed integer sequence N_L with N_L/L^3 -> rho, write

    d_L=N_L-rho L^3,       q=min(rho,1-rho)>0,
    r_L=ceil((|d_L|+D_m+2)/(q m))+1.

At fixed rho and ell, d_L=o(L^3), whence r_L/B -> 0 and eventually r_L<B.
With R_L=L^3-mB leftover sites and U_L=R_L+r_L m free sites, this choice
ensures q U_L>|d_L|+D_m+1. The required free-site number is the integer

    N_L-N_reg = rho U_L+d_L-(N_reg-rho m B').

The inequality above bounds it both below by zero and above by U_L,
regardless of the sign of d_L. Each integer in that interval is attained
by a literal occupation state on the free physical sites. The final
product density matrix is thus supported in the exact N_L sector.
Odd N_L is included, even if the original pair pulse had only even sectors.
A global number projection, postselection probability and a coherent
factorization across blocks are all unnecessary.

## 4. Seam bound on the actual Hamiltonian

Compare H_L with the sum of periodic block Hamiltonians on all B cubes,
including the reserved cubes, and zero on the R_L leftover sites. A center
at distance at least two from each block face has exactly the same local
term in both operators. At most

    ell^3-(ell-4)^3 <= 12 ell^2

centers per cube can differ. For every such center the norm of the actual
term minus the artificial periodic block term is at most 2h_*. Terms
centered in the leftover set cost at most h_*R_L. Thus

    ||H_L-sum_blocks H_ell|| <= 24h_*B ell^2+h_*R_L.

This counts cross-block interactions, original large-torus wraparound
and the added block-periodic wraparound. No interaction is deleted on a
positivity assumption. The radius-two grouping, rather than a scalar
pair model, controls this comparison.

Each reserved block state has periodic-block energy at most h_*m. The
exact-sector trial therefore obeys the author's full finite-volume bound

    E_L(N_L) <= B'm e + 2h_*m^2 + h_*r_L m
                           +24h_*B ell^2+h_*R_L.

Divide by L^3 and take L to infinity at fixed ell,rho. The rounding and
reservation errors vanish, B'm/L^3 tends to one and B ell^2/L^3 tends to
1/ell. This proves the transfer inequality e+24h_*/ell. It applies to
arbitrary large integer L; divisibility and particle parity are irrelevant.

## 5. Ordered limits and the lower input

For each fixed compact chi and sufficiently small fixed rho, the uniform
block trial gives, for every sufficiently large fixed ell,

    limsup_L E_L(N_L)/L^3
      <= t_chi rho^2/8+C_chi rho^3+24h_*/ell.

The left side does not depend on ell. Letting ell tend to infinity after
the thermodynamic limsup removes the seam term. Then rho tends to zero
at fixed chi, and only afterward is the compact correction improved to
t_0. Divergent remainder constants during that final improvement do not
invalidate this order. An unrestricted simultaneous dilute/volume limit
would require estimates that are not provided here.

The all-state lower is a separate source-bound input, author
`PARTICLE_TAIL_AND_LOWER_COMPOSITION.md` SHA256 `2e4d9f8b...`, with parent
focused receipt `124091e9...`. Its finite-volume polynomial inequalities
apply to exact-sector states. At fixed choices of its mesoscopic
parameters, N_L/L^3 -> rho is substituted by ordinary continuity after
its volume errors vanish. Its subsequent parameter order and dilute
limit are unchanged. This is a valid application of that lower bound;
the canonical upper itself does not prove it.

Together they imply, for every family of integer sequences having
N_L(rho)/L^3 -> rho at each fixed rho>0,

    lim_(rho down 0) liminf_(L->infinity) E_L(N_L(rho))/(L^3 rho^2)
      = lim_(rho down 0) limsup_(L->infinity)
                              E_L(N_L(rho))/(L^3 rho^2)
      = t_0/8.

The full lower's treatment of internal fragmentation is retained as an
input. Nothing in this transfer assumes that the actual minimizing state
is a coherent pair condensate or chooses a specific internal direction.

## 6. Actual checks, resource use and remaining boundaries

The new work is the independent precomparison, complete proof read and
analytic reconstruction of the density tuning, all rounding estimates,
reserve capacity, seam count, normalization and limit order above. The
actual old upper and its complete prior receipt were freshly read. The
necessary actual lower and focused receipts were read; their own source
identities and dependency limits remain in force. No numerical control
was needed, no author code was run, and no heavyweight job was launched.
Runtime deadline and STOP guard were checked; the original deadline is
unchanged. Metadata hashing and file reads are not scientific reruns.

There is no finding requiring a repair to the frozen candidate. This
receipt establishes no fixed-rho canonical thermodynamic-limit theorem,
rate uniform in rho and L, efficient state preparation, phase transition,
ODLRO, state polarization, or physical record/source law. It does not
convert provisional campaign inputs into retained or audited claims.
The actual optional native Hamiltonian and its supplied positive mu,tau
remain hypotheses. Integration and formal source review, if pursued,
remain separate requirements.
