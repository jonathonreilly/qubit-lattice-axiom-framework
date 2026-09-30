# Focused independent check: fixed-density canonical limit

No material mathematical error was found in the frozen composition at its
stated scope. No correction is required by this check. This is a source-bound
independent composition check, not formal review, an audit grade, or independent
revalidation of every imported lower/threshold theorem.

Checked author source: native-canonical-limit-composition-route/WORKING_PROOF.md,
SHA25672a793b33ca3a8c73482f8a9ff1af7d5d4f887ad601f7f11f72f9b38c228a522.
Checked contract: SHA256518cc50a23f6c228fffb80695b6891b90e6f838ffb8d58219b6b737f4b247047.

## Independence and actual source closure

PRE.md, SHA2568efe6af5d24cb1b417cb67a0259ec7b32e22746ae68b7efdac223a7d06efdad5,
was frozen before opening this new proof. The brief and contract already
exposed the intended minimizer/block mechanism. I authored the old mean-energy
composition and part of its lower input, independently checked the earlier
root block-transfer proof, and authored the integrated native delivery source.
Those roles are explicit dependencies and do not make this a blind check or
independent derivation of the old mean theorem. Root's focused mean-composition
receipt remains the independent input check for that author result.

For this task I reread the COMPLETE actual main native density source, old
mean composition and its root receipt, old general block-transfer proof and
my receipt, and the relevant source bindings. After the PRE freeze I read the
COMPLETE new proof, contract freeze and proof freeze. All referenced input
hashes and the new source identity were checked against actual bytes.
An initial batched display truncated part of the old-source output; those
sources were then read separately in full, rather than treated as read.
The selected procedure revision remains7146fe17; actual main isfb5da8dd.
Detailed identities and read roles are in SOURCE_BINDINGS.json.

The current check did not reopen every deep threshold/cell proof. Fixed-rho
canonical existence requires only the complete old mean theorem's section2,
the general transfer sections3–4 and the actual finite-range carrier. The
later t0/8 coefficient additionally inherits the already checked full mean
asymptotic, with its unchanged provisional inputs. No new calculation,
author-code import or runner execution was used or needed. All writes are
confined to this new check directory; the frozen delivery tree is untouched.

## Actual operator and minimizer domain

The actual carrier has every number sector0,...,V. The source Hamiltonian
commutes with N, is positive, and admits the translated radius-two grouping
H_L=sum_x h_x with ||h_x||<=h*=182mu+240tau for L>=5. These are direct facts
about the supplied full-qubit law. There is no effective pair Hilbert space
or bosonic replacement in the transfer.

At fixed ell and any real rho in[0,1], the finite mean-constrained density
matrix set is nonempty, closed and bounded, hence compact. The vacuum/full
mixture proves nonemptiness even when rho ell^3 is noninteger. A finite linear
energy functional attains its minimum there. Number dephasing preserves both
energy and mean because [H_ell,N]=0. Consequently any minimizer of e_ell(rho),
not only a tuned pulse state, is a valid input to the old general block lemma.
No typical-sector probability, variance bound, translation invariance, pure
state selection, differentiability or concentration assertion is needed.

The old general lemma itself states its arbitrary-density-matrix domain.
Checking its proof confirms that its quantitative constants depend only on
ell,rho,h*, not on the sector distribution or on the special unitary trial.
Its old application to that trial did not narrow the lemma's domain. The new
use therefore changes the proved consequence without silently changing a
hypothesis.

## Integer capacity, parity and physical seams

For a dephased block minimizer let p_k and tau_k be its sector weights and
states, m=ell^3. Every tau_k exists; if p_k=0 choose any state in that sector.
For B'=B-r regular blocks the original rounding convention is
 n_k=floor(B'p_k), k<m; n_m=B'-sum_(k<m)n_k.
It has nonnegative integer counts and bounds
 sum_k|n_k-B'p_k|<=2m,
 |N_reg-rho mB'|<=D_m=2m^2,
 |sum_k n_k Tr(H_ell tau_k)-B'm e_ell(rho)|<=2h*m^2.
These estimates hold uniformly in the minimizer. Populating a previously
zero-weight full sector is legal, not an undefined conditional state.

At fixed rho, q=min(rho,1-rho)>0, d_L=N_L-rho V=o(V), choose
 r_L=ceil((|d_L|+D_m+2)/(qm))+1.
Its block fraction vanishes. With R_L leftover sites and U_L=R_L+r_Lm,
 qU_L>|d_L|+D_m+1.
Writing delta=N_reg-rho mB', |delta|<=D_m, the missing integer is
 N_L-N_reg=rho U_L+d_L-delta.
Both this number and U_L minus it are nonnegative. Literal occupation states
on the free qubits realize every required integer, including odd numbers.
A product of block sector density matrices remains supported in one EXACT
total-number sector even if each factor is mixed. Its trace-one normalization
is exact. A mixed exact-sector trial is a valid variational upper for that
sector's least eigenvalue; no global projection or postselection is used.

The original Hamiltonian versus independent periodic block copies differs
only at radius-two seams and leftover centers. At most
 ell^3-(ell-4)^3<=12ell^2
centers per block are affected. Both the actual term and the artificial
periodic term cost at most h*, so the operator-norm difference is bounded by
 24h*B ell^2+h*R_L.
This includes original outer wraparound and artificial internal wraparound.
No positivity of individual deleted interactions is assumed. Nondivisible
volumes and arbitrary block correlations are covered by the same norm bound.
Together these facts reproduce the old general transfer upper, without using
any pulse remainder, threshold value or dilute estimate.

## The two limits and the moving density

Fix0<rho<1/2 and ANY allowed integer sequence rho_L=N_L/L^3->rho.
The exact-sector variational set is contained in the mean-rho_L set. Thus
 E_L(N_L)/L^3>=e_L(rho_L).
Eventually rho_L belongs to[0,1/2]. The separately checked UNIFORM convergence
of e_L on that interval and continuity of e imply
 e_L(rho_L)->e(rho).
This supplies the lower limit. Pointwise convergence at rho alone would not
justify this moving-density substitution; the actual input supplies the
required uniformity.

For each fixed ell choose a finite e_ell(rho) minimizer. The verified general
transfer gives
 limsup_L E_L(N_L)/L^3<=e_ell(rho)+24h*/ell.
This is a separate valid bound for every fixed ell, with a common left side.
Sending ell to infinity only AFTER the L limsup gives the upper limit e(rho).
No uniform selection of minimizers in ell and no interchange of infimum and
limsup is required. The result is therefore
 lim_L E_L(N_L)/L^3=e(rho)
for every such sequence, including both particle parities and all large L.
It is an energy statement; phase-separated trial constructions are allowed.
It does not establish a unique or homogeneous minimizing state.

## Compact-density uniformity: a second direct check

The author's subsequence proof of its equation(6) is valid: a violating
compact-interior sequence has a density accumulation point, and the just-
proved every-sequence limit contradicts the violation. It can be extended to
a full integer sequence by rounding rho L^3 at unselected volumes.

There is also a direct finite-volume verification from the actual rounding
bounds. Fix K=[a,b] with0<a<b<1/2 and delta=min(a,1-b)>0. At each L and integer
N with rho_L=N/V in K, use an e_ell(rho_L) minimizer. Fix ell first and reserve
 r=ceil((2m^2+2)/(delta m))+1
blocks; for large L there are enough blocks. Here d_L=0 exactly. The same
proof gives qU>=delta r m>2m^2+1, so its capacity test holds uniformly over
all these integers and all possible block minimizers. Since e_ell>=0,
dropping its prefactor B'm/V<=1 gives

 E_L(N)/V <= e_ell(rho_L)+24h*/ell
       +h*[2m^2+(2m^2+2)/delta+2m]/V+3h*ell/L.

The last inequality uses rm<=(2m^2+2)/delta+2m and
R_L=L^3-ell^3 floor(L/ell)^3<=3ell L^2. Each bound is state independent.
If epsilon_s=sup_[0,1/2]|e_s-e|, then uniformly on K the excess over e is
at most epsilon_ell+24h*/ell plus the two displayed finite-volume errors.
The deficit is at most epsilon_L. First L, then ell tending to infinity
proves the author's compact-interior absolute uniformity directly, with no
continuity of the selected minimizer required. This is an analytic check
of the claimed corollary, not a new numerical control or a quantitative
relative-error theorem.

## Dilute consequence and precise limits

For every fixed positive rho in the stated interval, division by rho^2 is
harmless AFTER taking L to infinity. The checked mean asymptotic
 e(rho)=t0 rho^2/8+o(rho^2)
then gives the stated ordered dilute t0/8 law with an actual inner limit.
The full fifteen-channel threshold and all-state lower hypotheses enter
through that mean theorem, not through an assumed coherent actual ground
state or a new threshold calculation here.

Neither compact-interior absolute uniformity nor the fixed-rho argument
provides an arbitrary simultaneous rho_L->0 relative limit: its reservation
constants involve1/delta or1/q, and its absolute errors have not been shown
to be o(rho_L^2). No numerical convergence rate, differentiability, unique
phase, ODLRO, polarization, dispersion, source/record identification or
Hamiltonian selection follows. The endpoint and larger-density extensions
are not asserted by the checked candidate.

The old native delivery unit explicitly excluded fixed-rho canonical-limit
existence; this focused receipt does not silently enlarge that frozen unit.
Any later integration must identify this new source and its own review scope.
The present outcome is no material correction at the stated composition
scope, with the input authorship and provisional status preserved.
