---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
source_science_acceptance_complete: true
canonical_parent_binding_complete: true
audit_required_before_effective_retained: true
bare_retained_allowed: false
---
# A supplied finite weak mediator for one fixed two-qubit target

Claim type: bounded_theorem.

**Primary runner:** `scripts/weak_mediator_fixed_target_2026_10_16.py`

## Conditional result and status

This canonical source packet packages one self-contained conditional construction for
literal old `K=2I+Z1Z2` and the full-phase target
`W=((9+12i)I+(-16+12i)X1X2)/25`. It supplies two additional qubits, a Bell
projector interaction and four positive XX/YY ports on a square. These are new
microscopic permissions. The construction does not derive them from the
original four onsite rays or the repository's bare microscopic assumptions.
It retains every old/source/reference output and gives an actual-time finite
window, explicit finite coefficients and a known finite reuse budget.

Root accepted the conditional science in ACCEPTANCE.json `ba201403`, controlled
by QUALIFICATION.md `e367c861`, reproduced as the twelfth complete body below.
The frozen source draft preserves its historical null publication decisions.
Actual wrapper, integration, selected-base and canonical review records must be
bound separately before the provenance primary runs. Staged review, publication
and retained audit remain separate gates. Historical proposed/unchecked language
remains unchanged evidence of the original stage.

The complete six root bodies and five analytic reviews are preserved byte for
byte before the controlling qualification. They are all part of this root
argument, not eleven external theorem parents. The proof starts from the
displayed finite matrices; it has **zero direct mathematical parents**. Other
campaign results, including the previous onsite word and direct static edge,
are context only. No previous publication archive or negative-science packet
is imported by the machinery reuse.

## Hamiltonian, full phase and finite window

Write `theta=atan(4/3)`, `delta=theta/pi`, `Delta=2-delta`, `q=theta/T`,
`gx=sqrt(q Delta/2)`, `gy=sqrt(q)` and `r=2(gx+gy)`. The source starts in
`Phi+=(00+11)/sqrt(2)` independently of the arbitrary old/reference input,
and `J psi=psi tensor Phi+`. Install

    H = K + Delta(I-|Phi+><Phi+|) + r I + V,
    V = gx(X1 XA + X2 XB) + gy(Y1 YA - Y2 YB).

The positive blocks are the source projector term, `gx(I+X1XA)`,
`gx(I+X2XB)`, `gy(I+Y1YA)` and `gy(I-Y2YB)`. Their identity reserve is
already `rI`, not a further block. Each old vertex has added incident load r;
each source vertex has Delta+r. Both are below 2 in the specified family.
The old norm-3 K block remains separately counted: its old total is 3+r.
Runtime coefficients are static and have zero slew. Physical units require
an explicit energy unit E0 and physical duration hbar*T/E0; no rescaling of
the literal old term is used to meet the added cap.

The full comparator at `t=T+s` is

    J exp(-irt) exp(-isK) W exp(-iTK).

For installed lower rounded coefficients it uses **actual**
`rhat=2(gxhat+gyhat)` in place of r. The literal old scalar and actual source
reserve are both retained. The proposal's phrase “source triplets” is corrected
here to **orthogonal Bell complement**: V reaches Psi+ and the spin-singlet
Psi−. The already-defined projector penalizes both correctly.

The exact first and second Sylvester correctors yield the identity
`(H0+V)F-F(K+H2)=VS2-S1H2-S2H2` for `F=J+S1+S2`.
The compressed second-order operator is

    H2 = ((2pi-theta)/T) I + (2pi/T) ZZ - (theta/T) XX,
    exp(-iT H2) = W.

The full cross-spectrum gap is delta; the input band need not be globally
lowest. Frobenius inverse bounds and exact Duhamel propagation give
`R(T)=12352/sqrt(T)+132096/T` for times at most 2T. Thus the proof uses an
exact residual, not an unbounded-time assertion about a truncated expansion.

For integer m>=0 set epsilon=2^-m and T=2^(2m+32). Equality-safe lower
rounding at p=3m+39 gives each coefficient error below 2*2^-p. On the fixed
24 window the full-isometry error is below 13epsilon/32. On the larger window
`w=epsilon*T/256`, it is below 15epsilon/32, hence unhalved full joint trace
error below 15epsilon/16. Tensoring arbitrary references preserves the norm;
mixed inputs follow by purification. A full initial joint trace defect adds
once. A source-marginal error alone is insufficient with arbitrary initial
correlations; the preserved review supplies a counterexample.

The sharper structured result keeps the same supports, signs, paired port
coefficients, source projector and exact K, and only lowers the three shared
coefficients. Port errors at most `hg=epsilon/(4096 sqrt(T))` and source error
at most `hD=epsilon/8192` give isometry error below 7epsilon/16 on the larger
window. The proof prices `||H2hat-H2||<128hg/sqrt(T)+256hD/T` and the actual
corrector residual. Its norm monotonicity uses this commuting Pauli family;
its gap bound uses Deltahat>3/2. It is not a generic fault estimate. Generic
self-adjoint residual E retains a separate `(T+w)||E||` allowance. Using the
original r instead of actual rhat can give an order-one phase defect, as the
unchanged review demonstrates.

## Finite compiler, reuse and energy

Three fixed alternating sums for atan(1/5), atan(1/239), atan(1/7), signed
Machin intervals and exact rational lower endpoints supply the coefficients.
Integer quotient and isqrt operations avoid any irrational grid-equality
oracle. Uniform n=p+8 or mixed grids `pg=2m+29`, `pD=m+14`,
`n=max(pg,pD)+8` meet the stated bounds. Each scenario uses **3n summed terms
plus three first-omitted remainders**, three final rounding quotients and two
isqrt calls. Those primitive counts exclude rational internals/GCD and do
not establish a total bit-complexity optimum. Output coefficient bit bounds
are not intermediate arithmetic bounds or physical calibration guarantees.

For known finite L, the unitary hybrid argument accumulates at most L times
the one-use isometry error with the same source retained. It does not assume
that the actual source resets or remains uncorrelated. Optional interventions
are supplied unitaries on old/reference registers acting as identity on the
source; their duration, apparatus, aging and error are separate interfaces.
Taking `m=m0+ceil(log2 L)` gives final trace error below epsilon0=2^-m0
with mediator endpoint duration below `2^34 L^3 epsilon0^-2` and window-inclusive
duration below `2^35 L^3 epsilon0^-2`. This excludes physical intervention time.
The window compares actual old aging, not a stationary output. It supplies
neither permanent halt nor indefinite reuse of one fixed device.

For the intended Bell product input the exact mean is `<K>+r`; the variance is
`Var(K)+2gx^2(1+<XX>)+2gy^2(1+<YY>)`, with hats for the actual rounded model.
The full static moments are conserved. Old K energy can change during runtime;
an endpoint bound follows from the joint trace error and half-width 1 of K.
Zero prescribed drive work during the static interval does not price source
preparation, installation, calibration, timing, reset or discarded apparatus.

## Actual evidence and limits

Two author scientific programs ran once each, with no replay here. The symbolic
fixture took 0.2838803748600185 seconds and records 60 finite exact polynomial
checks, including wrong-sign and bare-denominator mutants; its complete report
is 247777 bytes at SHA256 `4369fa1d5a970bf4e01ea00cc7db000779cab1d1f26be9bcbd26e1c4bc292a7d`.
The coefficient compiler took 0.131953792180866 seconds and records 64 checks
for two predeclared m44 outputs: T=2^120, uniform p171/n179/window24 and mixed
pg117/pD58/n125/window2^68. Its 1188206-byte report is
`0b108a9605e02b8b907ea13b364875b6282fc727c368dbed862ecb5d67149564`.
The latter observed 912 summed terms, six remainders, six final quotients,
four isqrt calls, 6111 guarded integer operations and maximum guarded integer
size 20857 bits. Both had actual 60-second wall limits, exit 0 and no timeout;
neither had an OS CPU/RAM quota.

All original and captured sources, inputs, reports, actual argv/cwd/version,
complete streams and freeze inventories are recoverable from SOURCE_MANIFEST.
Large polynomial and rational report bytes are preserved and hashed, not
described as manually checked entry by entry. The analytic reviews are separate
source-exposed reconstructions using the same selected model; the reviewer
contributed the lower-rounding strategy. This packaging author wrote both
scientific programs. There is no blind/model-independent validation or physical
experiment. Analytic gap, exponential and remainder proofs remain distinct
from finite assertions; provenance checks prove no physics.

A separately implemented saved-certificate validator subsequently ran once in
0.07717579184100032 seconds, exit 0, with 429 arithmetic predicates. Its exact
receipt is `73c9f6544f7530f3e8106b6f4f1dc523098e2bf107312bae88644bf8a88358a0`
and result is `ea2b9b99c64e6e3eecadde5a9eec34a50a589afb26a0ce40f1e378d0dab3fdb5`.
It checks saved endpoint algebra, integer inequalities, loads, actual phases
and conditional budgets without rerunning the compiler, calling isqrt or
regenerating the series. Saved endpoint truth remains an analytic premise.
Its report-derived implementation shares the model and Python integer trust
base; it is not blind, physical or an independent enclosure proof. The original
failed metadata inspection and corrected schema attempt are preserved with
their actual sources and streams. Root acceptance predates this check; neither
that acceptance nor any of the twelve bodies is rewritten by the new evidence.
Bell preparation, supplied microscopic couplers, physical precision and
observation timing remain explicit obligations. Actual source, integration,
selected-base and canonical review records are supplied by root; staged review,
publication and retained audit are distinct later records. This milestone
changes no editable prompt or physical axiom and grants no retained audit status.


<!-- Unchanged complete source: original_proposal -->

# Provisional two-qubit weak-mediator construction
Created by root 2026-10-16. UNCHECKED PROPOSAL; not retained, not yet independently checked.

## Scope and fixed inputs
Old system S comprises two qubits on an edge, with literal K=2 I+Z1 Z2.
W=((3+4i)/5)(3 I+4i X1 X2)/5; theta=atan(4/3), alpha=pi-theta.
T=350208522228384946904887108861751911074590975328100424043350794320, window w=24.
This T is the saved target-compilation schedule duration; this construction does not execute that external schedule. It uses its fixed target and duration only.
Intended comparison for every s in [0,w], t=T+s:
exp(-it Hphys) J versus J exp(-irt) exp(-is K) W exp(-iT K),
as full isometries for arbitrary old/reference input, not only density channels or postselection.
J psi=psi tensor Phi+, Phi+=(00+11)/sqrt(2) on two source qubits A,B. All four qubits are retained.
Tensor order S1,S2,A,B. Sources occupy the opposite edge of a square with edges (1,2),(1,A),(2,B),(A,B).
No added old-edge XX term. NEW PERMISSION: the specified two-qubit source Bell-projector block and old-source XX/YY port terms are available. These are additional microscopic coupling assumptions and are not the original four positive onsite control rays. Native availability, Bell preparation, installation, precise coefficients, external timing and final reuse are open.

## Supplied positive Hamiltonian
Set delta=theta/pi, Delta=2-delta, q=theta/T,
gx=sqrt(q Delta/2), gy=sqrt(q), r=2(gx+gy).
Let Hc=Delta (I-|Phi+><Phi+|) on A,B and
V=gx(X1 XA+X2 XB)+gy(Y1 YA-Y2 YB).
Hphys=K+Hc+r I+V is the sum of literal K, positive Hc, and the four positive port blocks
gx(I+X1 XA), gx(I+X2 XB), gy(I+Y1 YA), gy(I-Y2 YB).
Each port block has norm twice its coefficient. Each old vertex has added incident norm r; each source vertex has added incident norm Delta+r. Since 1/4<delta<1/2, 3/2<Delta<7/4. theta<1 follows from theta=pi/4+atan(1/7), pi<22/7. Thus r<4/sqrt(T). For T>2^128, r<delta, so every vertex has added incident norm <2. K remains a distinct old block of norm3. All coefficients are constant: runtime slew zero. No internal clock, driving waveform, high-strength penalty, measurement or discarded output is used.

## Second-order candidate, including scalar phase
P=JJ*, Q=I-P, H0=K+Hc. H0 J=J K and J* V J=0.
On old ZZ parity z=+/-1, K=2+z. V flips this parity and sends Phi+ into source triplets with Hc energy Delta.
The old-to-complement spectral denominators for H0 versus K are Delta and Delta+/-2; their absolute values are >=delta.

Define S1 in Q by H0 S1-S1 K=-VJ. Explicitly S1 P_z=-VJ P_z/(Delta-2z).
Define H2=J* V S1.
Bell correlations <XA XB>=1, <YA YB>=-1, mixed correlations zero give
J* V^2 J=2gx^2(I+XX)+2gy^2(I+YY).
Since YY=-ZZ XX,
H2 restricted to parity z =
 -2(gx^2+gy^2)/(Delta-2z) I
 -2(gx^2-z gy^2)/(Delta-2z) XX.
The chosen relation gy^2=2gx^2/Delta makes the XX coefficient -q for both parities.
Consequently
H2=s0 I+d ZZ-q XX,
s0=q Delta/(2-Delta)=(2pi-theta)/T,
d=2q/(2-Delta)=2pi/T.
This H2 is Hermitian and commutes with K.
Its four Bell eigenvalues are (4pi-2theta)/T,4pi/T,-2theta/T,0, so ||H2||=4pi/T<16/T.
Thus exp(-iT H2)=exp(i theta) exp(i theta XX)=W, including the scalar phase, because exp(-i2pi ZZ)=I.
The large scalar reserve r is NOT deleted: the comparison source state is chi(t)=exp(-irt)Phi+.

## Elementary residual bound proposed for checking
Define S2 in Q by H0 S2-S2 K=-Q V S1 (entrywise Sylvester inverse across the nonzero gap).
Let F=J+S1+S2 and G=K+H2.
Exact expansion should give
(H0+V)F-FG=R=V S2-S1 H2-S2 H2.
No normalization of F is needed for the following variation-of-constants comparison, since H0+V and G are Hermitian:
||exp(-it(H0+V))J-J exp(-itG)|| <=2||F-J||+t||R||.
With v=||V||<=r, dim(S)=4 and Frobenius norm, proposed bounds are
||S1||<=||S1||F<=2v/delta,
||S2||<=||S2||F<=2v^2/delta^2,
||H2||<=2v^2/delta,
||R||<=6v^3/delta^2+4v^4/delta^3.
Therefore error <=4v/delta+4v^2/delta^2+t(6v^3/delta^2+4v^4/delta^3).
For t<=T+24<=2T, v<4/sqrt(T), delta>1/4, this is
<=12352/sqrt(T)+132096/T.
For T>2^128 it is <2^-49.
During the additional w window, the effective target comparator incurs at most w||H2||<384/T.
The total proposed uniform isometry error is then <2^-48, hence <2^-44.
The unhalved joint-reference trace error is at most twice the actual isometry bound. No exact halt or indefinite source reuse follows.
These coarse powers need exact checking; no numerical execution has occurred.

## Energy statements to check
J* Hphys J=K+rI; for old state rho, full initial mean is Tr(rho K)+r.
J* Hphys^2 J=(K+rI)^2+J* V^2 J, so initial full variance is
Var_rho(K)+2gx^2(1+<XX>)+2gy^2(1+<YY>).
Full-Hphys moments are conserved by the static evolution.
Old K need not commute with V. Old-energy error at the output can instead be bounded from the joint-state error and old spectral width2.
Modeled runtime drive work is zero because dHphys/dt=0. Bell preparation, installation/removal, microscopic actuation and resets are separate and are not declared free.

## Precision and remaining obligations
Any actual Hamiltonian perturbation E adds at most (T+w)||E|| to the isometry budget (static bounded E), by Duhamel. This is a sufficient absolute calibration requirement, not a necessity theorem.
The ideal coefficients include pi, atan and square roots; they are computable but a finite rational compilation/encoding bound is not yet supplied.
The scalar rT belongs to the retained source output. A density-channel statement alone would not check it.
This is a proposed concrete four-qubit model with newly supplied port/source couplings, not a native realization of the original onsite-only controller, general autonomous compiler, clock or halt/reuse theorem.
Check all tensor signs, Sylvester inverses, exact residual cancellation, positivity/local incident norms, full source phase and energy identities independently before promotion.



<!-- Unchanged complete source: dyadic_addendum -->

# Root correction and proposed finite dyadic coefficient corollary
Source extension to PROPOSAL.md22e62c14, written after the independent checker reported its initial reconstruction. This addendum remains provisional until separately reviewed.

## Terminology correction
Replace the original phrase "source triplets" by "excited Bell states" or "the orthogonal Bell complement." VJ reaches Psi+ and Psi-, and Psi- is the spin singlet. The exact declared Hc=Delta(I-|Phi+><Phi+|) already assigns the same energy Delta to all three orthogonal Bell states; no Hamiltonian or denominator is changed. The original frozen proposal remains immutable and records this wording defect. The added incident norm is <2; total old-site incident norm including its literal norm3 K block is3+r.

## Finite coefficient representation proposed for checking
Let D0=2^400 and set gxhat=floor(D0 gx)/D0, gyhat=floor(D0 gy)/D0, Deltahat=floor(D0 Delta)/D0. This specifies exact dyadic rationals; it is not yet a concrete interval implementation that decides a floor at an equality boundary. Alternatively, any supplied lower dyadic approximants with absolute error <=2^-400 suffice, so no equality oracle is a physical premise of the approximation theorem.

Because3/4<theta<1,3/2<Delta<7/4 and T<2^300, gx,gy>2^-151. Thus the displayed rounded values are strictly positive. They do not increase the incident norm: rhat=2(gxhat+gyhat)<=r and Deltahat+rhat<=Delta+r<2. All positive port blocks and positive source block retain their stated supports. Each rational numerator has at most401 bits and common denominator2^400 has401 bits. All blocks remain static.

Use the retained source comparison chihat(t)=exp(-irhat t)Phi+. Separate the actual scalar rhat exactly. The nonscalar generator differs from the ideal H0+V by
E=(Deltahat-Delta)Qc+(gxhat-gx)(X1XA+X2XB)+(gyhat-gy)(Y1YA-Y2YB),
so ||E||<=5*2^-400. Duhamel adds at most5(T+w)2^-400<10*2^-100<2^-96 on [T,T+24], using T<2^300 and T+24<2T. Combined with the ideal proposed <2^-48 bound, the rounded full-isometry error is <2^-47<2^-44. The generic unhalved joint-reference trace bound is twice that.

These dyadic coefficients need not preserve the exact H2 cancellation; the full-Hamiltonian Duhamel comparison handles their changes. The source reserve phase is the actual rhat, not an untracked deletion. Exact full initial mean/variance formulas apply with rhat,gxhat,gyhat and the actual Deltahat because Phi+ remains the exact source-block zero state.

A finite supplied coefficient description is obtained, conditional on a correct approximant certificate. This does not establish physically achievable precision, a runtime-efficient parameter compiler, Bell preparation, native ports, internal timing or reset. A source-only exact checker may verify the symbolic formulas/bounds; do not silently claim it computed these actual400-bit coefficients unless a separately authorized recorded computation actually does so.



<!-- Unchanged complete source: scaling_addendum -->

# Proposed accuracy-scaled weak-mediator family
New root-original corollary to PROPOSAL.md22e62c14 and DYADIC_ADDENDUM.md2ad3573f. UNCHECKED until separately reviewed. The same fixed old K and fixed full target W are retained, but the runtime is now chosen independently of the earlier external target word.

For each integer m>=0 set epsilon=2^-m and T_m=2^(2m+32), w=24. Keep theta=atan(4/3), delta=theta/pi, Delta=2-delta, q=theta/T_m, gx=sqrt(q Delta/2), gy=sqrt(q), r=2(gx+gy), and the same positive four-port plus Bell-complement Hamiltonian. All extra microscopic coupling permissions, supplied Bell state, input/time interface and native-identification limits remain.

The ideal residual proof requires only T>=24, delta>1/4, v<4/sqrt(T), and the stated spectral identities. Its actual comparator error on [T,T+24] is bounded by
A(T)=12352/sqrt(T)+132480/T,
where132480=132096+384 includes the quiet-window effective drift.

For T=T_m,
A(T_m)/epsilon <= 12352/2^16 +132480/2^32 <1/4.
The second summand has an extra2^-m factor, bounded by1. Thus the full ideal isometry error is <epsilon/4 for every m>=0. Since r<4/2^(m+16)<=2^-14<delta, source and old added incident caps remain<2. The old total incident load includes the fixed norm3 K block. The exact endpoint H2 and scalar proof remain valid at this T_m; no recurrence integer or huge target word is needed.

Let p=3m+38. Supply positive lower dyadic approximants gxhat,gyhat,Deltahat with common denominator2^p and absolute error<=2^-p. The floor-defined coefficients are one mathematical choice; a concrete equality-safe interval compiler has not yet been supplied. gx,gy>2^-(m+17), so the lower rounded coefficients remain positive. Coefficient numerators need at mostp+1 bits and the common denominator hasp+1 bits. Lower rounding preserves added incident caps.

Retain actual reserve rhat=2(gxhat+gyhat) in source output chihat(t)=exp(-irhat t)Phi+. The nonscalar Hamiltonian defect is at most5*2^-p. Since t<=T_m+24<2T_m, its Duhamel allowance is
5(T_m+24)2^-p <10*2^(2m+32)*2^-(3m+38)=(5/32)epsilon.
Hence total full-isometry error is <(1/4+5/32)epsilon=(13/32)epsilon<epsilon/2, and the generic unhalved joint-reference trace error is <epsilon. The initial supplied source may instead have unhalved trace defect delta_init, yielding final trace error<epsilon+delta_init by contractivity and the triangle inequality; no source is discarded.

Consequently this supplied-model family uses exactly two source qubits, constant positive incident caps, zero runtime slew, time T_m=2^32 epsilon^-2, couplings O(epsilon), and sufficient absolute coefficient accuracy O(epsilon^3), with O(log(1/epsilon)) rational bit lengths. These are conditional asymptotic resource statements for a fixed target, not efficient physical implementation or necessary calibration laws. No actually computed dyadic coefficient list, native coupling supplier, Bell preparation, internal clock, exact halt or reuse is claimed. The large numeric prefactor and unspecified physical E0/time units remain explicit.

For epsilon=2^-44, T_m=2^120, smaller than the prior fixed target duration. This is a changed runtime contract, not a correction or optimization of the earlier external positive-onsite word. The unchanged full-energy initial moment formulas and static conservation apply at each m; resource comparisons must keep new interaction permissions visible.



<!-- Unchanged complete source: finite_compiler_addendum -->

# Proposed equality-safe finite coefficient compiler

Root-original extension of SCALING_ADDENDUM.md7a48fcff, written2026-10-16 after the independent checker proposed lower-endpoint rounding. This algorithm and its bounds are proposed for separate review; no execution or coefficient certificate is asserted here. Earlier frozen proposals remain unchanged.

## Initial-state qualification

The additive delta_init trace statement requires an independent supplied source state sigma with ||sigma-|Phi+><Phi+|||_1<=delta_init, tensored with the arbitrary old/reference input, or directly a bound delta_init on the full initial old/reference/source state relative to that product. A source-marginal error alone does not bound arbitrary pre-existing source correlations by delta_init. This corrects the insufficiently qualified sentence in the original scaling addendum.

## Finite rational construction

For integer m>=0, take epsilon=2^-m, T=2^(2m+32), p=3m+39, h=2^-p, and n=p+8. The extra bit relative to the earlier floor-defined version pays for the safe two-h approximation error. For a in {5,239,7}, form the exact rational

S_a(n)=sum_{j=0}^{n-1} (-1)^j/((2j+1)a^(2j+1)).

The alternating-series interval for atan(1/a) has endpoints S_a(n) and S_a(n)+(-1)^n/((2n+1)a^(2n+1)); sort them as L_a,U_a. Form

pi_L=16L_5-4U_239, pi_U=16U_5-4L_239,
theta_L=pi_L/4+L_7, theta_U=pi_U/4+U_7.

Machin's identity and theta=pi/4+atan(1/7) give certified enclosures for pi and theta. With n=p+8 and p>=39, both interval widths are <w=2^-(2p+12): each is bounded by20*5^-(2n+1), which is <20*2^-(4n+2)<2^-(2p+12). The same enclosures also have pi_L>3 and 0<theta_L<theta_U<1; these coarse inequalities follow already from the first terms and their alternating remainder bounds, or can be checked as rational guards.

Set

Delta_L=2-theta_U/pi_L, Delta_U=2-theta_L/pi_U,
y_L=theta_L/T, y_U=theta_U/T,
x_L=theta_L*Delta_L/(2T), x_U=theta_U*Delta_U/(2T).

The true values Delta, gy^2, gx^2 lie in these respective intervals. The guards0<Delta_L<=Delta_U<2 and0<theta_L<theta_U<1 hold. Since pi_L>3, the Delta width is <w/3+w/9<w/2. The y width is <w/T; the x width is <(2w+w/2)/(2T)<2w/T. These conservative bounds suffice without computing a square root of an interval width.

For a positive rational a=A/B, define

k_p(a)=isqrt(floor(2^(2p) A/B)).

Here isqrt is the exact integer floor square root. Then k_p(a)/2^p is a lower dyadic approximation to sqrt(a) with error <h. Because |sqrt(u)-sqrt(l)|<=sqrt(u-l), the x and y intervals have square-root width <sqrt(2w/T)<h/2. Define

gxhat=k_p(x_L)/2^p,
gyhat=k_p(y_L)/2^p,
Deltahat=floor(2^p Delta_L)/2^p.

All three values are lower approximants to the ideal coefficients with error <2h. The earlier lower bound gx,gy>2^-(m+17), together with2h<2^-(m+17), ensures strictly positive values. Lower rounding preserves every added incident cap, including Deltahat+2(gxhat+gyhat)<2. Each coefficient numerator uses at mostp+1 bits, and the common denominator2^p usesp+1 bits. The algorithm uses exactly3n alternating-series terms, rational arithmetic, three integer divisions and two integer floor square roots after the enclosures are built; it has no equality oracle, adaptive floor decision, floating-point approximation or unbounded convergence search. This is not a bit-complexity optimum claim.

Retain rhat=2(gxhat+gyhat) exactly in the comparison source phase. The nonscalar generator defect is <10h. Thus on[T,T+24] its Duhamel contribution is

10(T+24)h<20*2^(2m+32)*2^-(3m+39)=(5/32)epsilon.

Combining with A(T)<epsilon/4 gives full-isometry error<13epsilon/32 and generic unhalved joint-reference trace error<epsilon. The constants and resource statements of the original scaling corollary remain, with sufficient precision O(epsilon^3) and coefficient bit lengths O(log(1/epsilon)). No actual coefficient list is claimed until an execution is separately reviewed and recorded.

The compiler supplies mathematical rational coefficients. Physical calibration, new microscopic port/source permissions, product-state initialization, installation, external timing and final halt/reuse remain independent premises or obligations. It does not identify these interactions with the original four onsite positive control rays or modify any framework axiom.


<!-- Unchanged complete source: window_reuse_addendum -->

# Proposed longer quiet window and bounded coherent reuse

Root-original corollary,2026-10-16. This is a new proposal for separate checking, not yet a published or independently accepted result. It uses the same supplied square Hamiltonian, product Bell-source interface, equality-safe lower dyadic coefficients, and actual retained scalar from FINITE_COMPILER_ADDENDUM.md7c546393. New microscopic coupling permissions and all physical supply limits remain.

## Longer window relative to literal old aging

Let epsilon=2^-m, T=2^(2m+32), p=3m+39, and set

w_m=epsilon*T/256=2^(m+24).

For every m>=0 this window exceeds24 and is belowT. The original residual argument used only t<=2T, so on[T,T+w_m] its bare residual error is bounded by

R(T)=12352/sqrt(T)+132096/T<epsilon/4.

The effective-Hamiltonian drift over the window contributes at most16w_m/T=epsilon/16. The equality-safe coefficient error<2*2^-p in each of the three scalar coefficients gives nonscalar generator error<10*2^-p; sinceT+w_m<2T, this contributes less than(5/32)epsilon. Thus the actual rounded full-isometry discrepancy against

J exp(-irhat(T+s)) exp(-isK) W exp(-iTK)

is strictly below(1/4+1/16+5/32)epsilon=(15/32)epsilon for every0<=s<=w_m. The generic unhalved joint-reference trace error is therefore below(15/16)epsilon<epsilon. This enlarges the proved window without changingT,p,source count,positivity or added incident caps. For m44 the window is2^68 in the same dimensionless time units, andT=2^120.

This comparison keeps literal old aging for the actual elapsed timeT+s and the actual scalar phase. It is not a statement that an uncertain observation time yields the same fixed-time full vector Wexp(-iTK). A separate fixed-time clock contract must also pay for old drift and its scalar. Nor does this finite window provide a stopping mechanism, permanent halt, switched-off interaction or infinite reuse.

## Bounded coherent reuse with the source retained

LetV_s=exp(-i(T+s)Hhat) on old plus source andU_s=exp(-irhat(T+s))exp(-isK)Wexp(-iTK) on the old factor with its scalar. The established uniform operator inequality is

||V_s J-J U_s||<eta, eta=(15/32)epsilon, 0<=s<=w_m.

Tensoring an arbitrary reference preserves this norm. For any finiteL, composeL such runtime intervals and allow arbitrary supplied unitary interventionsA_j on old plus retained reference registers only, with identity action on the source. The embedding intertwines each such intervention: (A_j tensor I_source)J_R=J_R A_j. A telescoping product expansion therefore bounds the full isometry difference from the corresponding ideal sequence byL eta. Each factor in the expansion has norm1; no assumption that the actual source is exactly restored, uncorrelated or reset between uses is introduced. The unhalved joint trace error is below2L eta<L epsilon, retaining all source/reference registers. With no interventions ands_j=0 the actual process is just exp(-iLT Hhat), compared withJ exp(-irhat LT)(Wexp(-iTK))^L.

For a desired final trace allowance epsilon0=2^-m0 andL>=1, choosek=ceil(log2 L), m=m0+k, soepsilon=2^-m<=epsilon0/L. Then the total error is belowepsilon0. The source still has exactly two qubits; p=3(m0+k)+39. Each duration isT=2^32*2^(2k)*epsilon0^-2, and total runtime for exact endpoint intervals satisfiesLT<2^34 L^3 epsilon0^-2. The strict bound holds also forL1. For intervals anywhere in the enlarged windows, total duration is less than twice this endpoint bound. These are sufficient upper bounds for this fixed target and supplied model, not optimality or a generic programmable compiler.

The optionalA_j are mathematical interfaces, not internally generated operations or unpriced physical controllers. A finite-duration implementation, installation work, source preparation, timing/calibration faults and any discarded intervention outputs need separate budgets. Without such supplied interventions this is a repeated fixed-gate/power statement only. It gives bounded coherent reuse at a stated accumulated error; it does not establish exact reset, indefinite reuse or an autonomous halt.


<!-- Unchanged complete source: structured_coefficient_addendum -->

# Proposed sharper bound for three structured coefficient errors

Root-original proposal2026-10-16, requiring a separate independent check. This concerns only lower coefficient replacements within the same specified Bell-projector and four-port family; it does not sharpen the bound for an arbitrary Hamiltonian fault. No actual coarser coefficient list is asserted here.

Keep epsilon=2^-m, T=2^(2m+32), the idealDelta,gx,gy and the longer windoww=epsilon*T/256. Suppose the actual three coefficients obey

0<=gx-gxhat<=h_g, 0<=gy-gyhat<=h_g,
0<=Delta-Deltahat<=h_D,
h_g=epsilon/(4096 sqrt(T))=2^-(2m+28),
h_D=epsilon/8192=2^-(m+13).

These bounds leave all coefficients positive andDeltahat>3/2. Lower replacements preservevhat<=v<4/sqrt(T), every added incident cap, andthe new cross-spectrum gapdeltahat=2-Deltahat>=delta>1/4. The old generatorK remains literal, and the actual reserve rhat=2(gxhat+gyhat) stays in the source comparison phase.

## Effective-Hamiltonian comparison

The same Sylvester proof works for independent positive gxhat,gyhat,Deltahat; it does not need the ideal tuning relation to obtain a residual estimate. Let

M=J*V^2J, Mhat=J*Vhat^2J,
D=Delta I-2ZZ, Dhat=Deltahat I-2ZZ.

Both compressed squares commute withZZ, and the exact second-order operators areH2=-M D^-1 andH2hat=-Mhat Dhat^-1. They are Hermitian and commute withK for any such three coefficients. The tuned formula yielding the exact targetW is needed only for the idealH2.

The port difference satisfies||Vhat-V||<=4h_g. Therefore

||Mhat-M||<=||Vhat^2-V^2||
 <=(||Vhat||+||V||)||Vhat-V||<=8v h_g.

Here the square-difference inequality usesVhat^2-V^2=Vhat(Vhat-V)+(Vhat-V)V; it does not assume the two full port operators commute. Also

||Dhat^-1-D^-1||<=h_D/delta^2,
||Dhat^-1||<=1/delta, ||M||<=v^2.

Consequently

||H2hat-H2||<=8v h_g/delta+v^2 h_D/delta^2
 <128h_g/sqrt(T)+256h_D/T.

For t<=T+w<2T, the effective-phase error is strictly below

256sqrt(T)h_g+512h_D=epsilon/16+epsilon/16=epsilon/8.

The bare full-isometry residual for the actual rounded model remains bounded byR(T)=12352/sqrt(T)+132096/T<epsilon/4, since the actual coupling bound is smaller and the actual spectral gap is larger. The ideal window drift is at most16w/T=epsilon/16. Thus the same full comparator with actualrhat and literal actual old aging has full-isometry error<7epsilon/16 and generic unhalved joint-reference trace error<7epsilon/8<epsilon on the longer window. No exact cancellation or exact target phase is claimed forH2hat itself.

## Finite coefficient route and limits

The equality-safe finite algorithm may use port gridbits p_g=2m+29 and source gridbits p_D=m+14, with the same enclosure construction at n=max(p_g,p_D)+8. The arctangent intervals then have width<2^-(2max(p_g,p_D)+12). Apply the two integer-square-root lower roundings atp_g and the rationalDelta lower rounding atp_D. Their errors are below2*2^-p_g=h_g and2*2^-p_D=h_D by the same interval argument. Output numerator and denominator lengths are bounded separately byp_g+1 andp_D+1. At m44 these grid exponents are117 and58; no such coarser list has been computed by this proposal.

This gives sufficient structured absolute error allowances O(epsilon^2) for each port coefficient andO(epsilon) for the source coefficient, improving on the unstructured full-generator Duhamel allowanceO(epsilon^3). It is a conditional upper-bound construction, not a necessary precision law. An arbitrary residual self-adjoint faultE beyond this three-coefficient family still costs at most(T+w)||E|| in isometry norm. Unknown sign, support, time dependence, unbounded noise or calibration outside the stated lower intervals is not covered automatically. Initial source faults require the independent-source/full-joint-state contract already stated. Added microscopic permissions, physical energy/time units, preparation/installation, observation timing and exact halt/indefinite reuse remain unresolved.


<!-- Unchanged complete source: original_analytic_review -->

# Source-exposed analytical review of the four-qubit weak mediator

This is an analytical reconstruction of the root-authored proposal at SHA256 `22e62c1408387329d172d7c3b1e6dc5591fc550b639756db7f92f1e3b159649b`. It is not a blind check, numerical experiment, retained-status verdict, or approval of a native physical implementation. I read the complete proposal before reconstructing the calculation. I did not execute or import scientific source, simulate the evolution, or use a numerical result to establish the argument below. The root retains the decision about qualification and publication.

**Finding.** Under the explicitly supplied Bell-projector source block, the four specified port blocks, exact coefficients, and the supplied initial Bell state, the stated finite-dimensional approximation follows. The second-order signs, scalar phase, Sylvester cancellation, norm constants, full-reference scope, and initial energy identities check out. One literal terminology correction is required: “source triplets” must be replaced by “the orthogonal Bell complement” or “excited Bell states.” The coupling reaches the spin singlet as well as a spin triplet. This correction changes no Hamiltonian or bound.

The proof does not supply the new interactions from the original positive onsite rays, prepare the Bell state, realize the exact coefficients with finite hardware, provide autonomous timing, or establish an exact halt or reusable controller. The cap below applies to **added** incident blocks; it does not bound the old vertex's literal `K` plus additions by 2. The external-drive work identity does not assert that the old subsystem's energy remains constant at intermediate times.

## 1. Exact scope and conventions

The old two-qubit Hilbert space has dimension four. The source also has dimension four; tensor order is `S1,S2,A,B`. Use the standard Pauli convention `Y|0> = i|1>`, `Y|1> = -i|0>`, and define

\[
\Phi_\pm=(|00\rangle\pm|11\rangle)/\sqrt2,
\qquad \Psi_\pm=(|01\rangle\pm|10\rangle)/\sqrt2.
\]

The embedding is `J psi = psi tensor Phi+`; `P=JJ*`, `Q=I-P`. The actual old Hamiltonian is `K=2I+Z1 Z2`, with eigenvalues 1 and 3. The source penalty is exactly `Hc=Delta(I-|Phi+><Phi+|)`, rather than an unspecified isotropic triplet penalty. Set

\[
\theta=\arctan(4/3),\quad \delta=\theta/\pi,\quad
\Delta=2-\delta,\quad q=\theta/T,
\quad g_x^2=q\Delta/2,\quad g_y^2=q,
\quad r=2(g_x+g_y),
\]

where the positive square roots are used and the supplied exact integer is

`T=350208522228384946904887108861751911074590975328100424043350794320`.

The target is `W=e^(i theta) e^(i theta X1 X2)`, exactly the rational complex matrix written in the proposal, since `cos(theta)=3/5` and `sin(theta)=4/5`. The target and `K` commute. This is therefore a particular energy-preserving target with respect to the literal old `K`, not an arbitrary energy-changing operation. The previously selected duration is a fixed input here; no endpoint compilation schedule or its proof is executed or imported into this construction. The unused definition `alpha=pi-theta` has no role in this proof.

## 2. Bell channels and the terminology correction

Directly applying each source Pauli gives

\[
X_A\Phi_+=X_B\Phi_+=\Psi_+,
\qquad Y_A\Phi_+=-i\Psi_-,\quad Y_B\Phi_+=i\Psi_-.
\]

Consequently the actual signed port operator satisfies

\[
VJ=g_x(X_1+X_2)\otimes\Psi_+
       -i g_y(Y_1+Y_2)\otimes\Psi_-.
\tag{1}
\]

The two source output states in (1) are orthogonal and both have source energy `Delta`. In the usual spin terminology `Psi-` is the singlet; hence “source triplets” is not literally correct. The three-dimensional complement of `Phi+` contains it. The stated projector `Hc` already assigns the right common energy, so the correction is prose only. Replacing `Hc` by a different physical “triplet penalty” without adjusting the proof would not be justified.

Equation (1) proves `J*VJ=0` and, by taking its Gram operator,

\[
J^*V^2J=g_x^2(X_1+X_2)^2+g_y^2(Y_1+Y_2)^2
=2g_x^2(I+XX)+2g_y^2(I+YY).
\tag{2}
\]

The minus sign in the second physical port and the opposite signs of `Y_A Phi+` and `Y_B Phi+` are both essential to the plus sign before `YY` in (2). The vanishing mixed terms follow from source-state orthogonality, rather than an assumption about the old input state.

For a second direct check of all four old sectors, (1) gives

| Old input | `VJ` applied to that input |
| --- | --- |
| `Phi+` | `2 gx Psi+ tensor Psi+` |
| `Phi-` | `2 gy Psi+ tensor Psi-` |
| `Psi+` | `2 gx Phi+ tensor Psi+ - 2 gy Phi- tensor Psi-` |
| `Psi-` | `0` |

Here the first ket in each product is old and the second is source. These are analytical identities, not output from a matrix program. In particular, the old singlet is an exact dark input, a useful check on the zero effective eigenvalue below.

## 3. Spectral denominators and the full second-order Hamiltonian

Write `P_z` for the old `ZZ` parity projector, `z=+1,-1`. Every term of `V` flips old parity. Thus `VJP_z` has unperturbed energy `2-z+Delta`, whereas `JP_z` has energy `2+z`. Their difference is

\[
D_z=\Delta-2z.
\]

It is **negative** for the even sector (`D_+=-delta`) and positive for the odd sector (`D_-=Delta+2`). The `P` block is not the globally lowest spectral band: a `Q` level `1+Delta` lies below the old level 3. No low-energy ordering assumption is used. What is needed is separation of the spectra of `H0|Q` and `K` as sets. Every difference belongs to `{Delta,Delta-2,Delta+2}`, and every absolute value is at least `delta`.

The equation `H0 S1-S1 K=-VJ` therefore has the stated solution

\[
S_1P_z=-\frac{VJP_z}{D_z}.
\tag{3}
\]

Using (2), `YY=-ZZ XX`, and the fact that the compressed square preserves parity,

\[
H_2|_z=-\frac{2(g_x^2+g_y^2)}{D_z}I
       -\frac{2(g_x^2-zg_y^2)}{D_z}XX.
\tag{4}
\]

The `XX` numerator in (4) is `q(Delta-2z)`, so its coefficient is exactly `-q`. The scalar coefficients in the two sectors are

\[
a_+=q(\Delta+2)/\delta=4\pi/T-q,
\qquad a_-=-q.
\]

Their half-sum and half-difference yield

\[
H_2=(2\pi-\theta)I/T+(2\pi/T)ZZ-(\theta/T)XX.
\tag{5}
\]

This verifies the proposed `s0` and `d`, proves Hermiticity, and proves commutation with `K`. The old Bell basis gives, in order `Phi+,Phi-,Psi+,Psi-`,

\[
\operatorname{spec}(H_2)=
\{(4\pi-2\theta)/T,\ 4\pi/T,\ -2\theta/T,\ 0\}.
\]

Thus `||H2||=4pi/T<16/T`. Because all three terms of (5) commute,

\[
e^{-iTH_2}=e^{-i(2\pi-\theta)}e^{-i2\pi ZZ}e^{i\theta XX}
=e^{i\theta}e^{i\theta XX}=W.
\tag{6}
\]

The scalar is not dispensable. If one deletes `s0 I` from (5), the resulting full isometry differs at the target time by the non-small factor `|e^(i theta)-1|=2 sin(theta/2)`. Ordinary density channels would hide that error; the requested vector/isometry comparison does not.

## 4. Exact residual cancellation, including the projected term

The global Sylvester inverse on maps from the old space into `Q` exists by the spectral separation above. Define `S2` in `Q` by

\[
H_0S_2-S_2K=-QVS_1.
\]

For `F=J+S1+S2`, `G=K+H2`, expansion gives

\[
\begin{aligned}
(H_0+V)F-FG
&=(H_0J-JK)+(H_0S_1-S_1K+VJ)\\
&\quad +(H_0S_2-S_2K+VS_1-JH_2)
       +VS_2-S_1H_2-S_2H_2\\
&=VS_2-S_1H_2-S_2H_2=:R.
\end{aligned}
\tag{7}
\]

The third bracket vanishes because `-QVS1+VS1=PVS1=J(J*VS1)=JH2`. This is the cancellation that would be lost by forgetting either the projection in the `S2` equation or the `JH2` term. No claim that `F` is an isometry is required.

Both `A=H0+V` and `G` are Hermitian. Exact variation of constants gives

\[
e^{-itA}F-Fe^{-itG}
=-i\int_0^t e^{-i(t-u)A}R e^{-iuG}\,du.
\]

Adding the two endpoint corrections for `F-J` proves

\[
\|e^{-itA}J-Je^{-itG}\|
\le 2\|F-J\|+t\|R\|\quad(t\ge0).
\tag{8}
\]

This proof uses unitarity of the two evolution operators, not invertibility, normalization, or spectral completeness of `F`.

## 5. Norm proof and integer constants

Let `v=||V||`. The triangle inequality gives `v<=2(gx+gy)=r`. In eigenbases of `H0|Q` and `K`, the Sylvester inverse divides each matrix entry by a real number of magnitude at least `delta`. Its Frobenius-norm bound is therefore `1/delta`. This is a Frobenius argument; it does not silently assume an operator-norm Schur multiplier bound.

Since `J` has four orthonormal columns,

\[
\|VJ\|_F\le2v,\quad
\|S_1\|\le\|S_1\|_F\le2v/\delta,
\quad \|S_2\|\le\|S_2\|_F\le2v^2/\delta^2.
\]

Also `||H2||<=||J*V|| ||S1||<=2v^2/delta`. Applying these bounds to the three terms in (7) gives respectively `2v^3/delta^2`, `4v^3/delta^2`, and `4v^4/delta^3`, hence

\[
\|R\|\le6v^3/\delta^2+4v^4/\delta^3.
\tag{9}
\]

Equations (8) and (9) reproduce the proposed error bound exactly. For `t<=2T`, `v<4/sqrt(T)` and `1/delta<4`, the four contributions are bounded by

| Contribution | Bound |
| --- | --- |
| `4v/delta` | `64/sqrt(T)` |
| `4v^2/delta^2` | `1024/T` |
| `t 6v^3/delta^2` | `12288/sqrt(T)` |
| `t 4v^4/delta^3` | `131072/T` |

The sums are `12352/sqrt(T)+132096/T`, as written. The supplied decimal integer exceeds `2^128` and 24. Therefore `T+24<=2T`. Since `12352<2^14` and `132096<2^18`, this sum is strictly smaller than `2^-50+2^-110<2^-49`. No floating-point estimate is needed for these inequalities.

## 6. Full output, retained scalar and reference systems

For `t=T+s`, `0<=s<=24`, equations (5) and (6) give

\[
e^{-itG}=e^{-isK}W e^{-iTK}e^{-isH_2}.
\]

Dropping only the last factor costs at most `s||H2||<384/T<2^-119`. Since `Hphys=A+rI`, multiplying both comparisons by `e^(-irt)` preserves every norm. Thus the desired full-isometry error is uniformly bounded by

\[
\epsilon_*(T):=12352/\sqrt T+132480/T<2^{-48}.
\tag{10}
\]

The source comparison vector is exactly `chi(t)=e^(-irt)Phi+`. Assigning the common scalar to this source vector fixes the stated comparison convention; it does not make a global scalar observable in an ordinary density experiment or supply a source clock. In particular, the proof has not erased `rT`.

Tensoring an operator difference with an identity on an arbitrary reference preserves its operator norm. For every normalized old/reference input, (10) bounds the full four-qubit/reference output vector error. Both comparison maps are isometries, so the unhalved joint trace-norm error is at most `2 epsilon_*(T)<2^-47`. Purification and partial trace extend this to mixed old/reference inputs. The source is retained in this statement; no measurement, successful branch, source trace-out, or postselection is used to obtain it.

The dark old input `Psi-` gives the exact evolution `exp[-it(1+r)] J Psi-`, and the target comparator gives the same vector. This independently checks the zero effective eigenvalue and scalar convention in one sector. The uniform argument above, rather than this particular input, supplies the arbitrary-input guarantee.

The window is finite. No estimate for arbitrary later times, exact switch-off, indefinite source reuse, or accumulated error after repeated uses follows from (10).

## 7. Positivity, geometry, and what the cap actually counts

The angle identity `theta=pi/4+atan(1/7)` follows from the tangent addition formula in the correct first-quadrant branch. Hence `pi/4<theta<pi/2`, and using `atan(x)<x`, `pi<22/7` gives `theta<11/14+1/7=13/14<1`. It follows that `1/4<delta<1/2` and `3/2<Delta<7/4`.

Each of `XX` and `YY` on a port is a Hermitian involution. Thus `g(I+P)` and `g(I-P)` have eigenvalues 0 and `2g`, for positive `g`. Their sum is exactly `rI+V`, with no missing or doubled identity reserve. The source projector term is positive with norm `Delta`; literal `K` is positive with norm 3. Therefore the full displayed Hamiltonian is positive.

Each old vertex has two added incident blocks with norm sum `2gx+2gy=r`. Each source vertex has the source block and two ports, with sum `Delta+r`. Since `gx<1/sqrt(T)` and `gy<1/sqrt(T)`, `r<4/sqrt(T)<2^-62<delta`, proving `Delta+r<2`. The old added sum is also below 2. If literal `K` is counted, the old incident sum is **3+r**, so a total per-vertex cap of 2 would be false. The proposal correctly distinguishes the old block; that distinction must survive packaging.

All interaction supports are among the stated square edges. No direct old-edge `XX` term is present. Constant coefficients have zero runtime slew, and `Delta<7/4` is not an arbitrarily large penalty. These facts do not derive the Bell-projector interaction or either `XX/YY` port from the original four positive onsite rays. Their availability is an additional microscopic permission. Bell preparation, installation, parameter setting, external timing, and reset remain separate obligations.

## 8. Energy and work identities

Let `C=K+rI`. On the initial embedded subspace, `Hphys J=JC+VJ`, with `J*VJ=0`. Taking the compression and the Gram operator gives exactly

\[
J^*H_{\rm phys}J=C,
\qquad J^*H_{\rm phys}^2J=C^2+J^*V^2J.
\]

For any old density operator (the reduced state of any old/reference input), subtraction of the square of the mean yields

\[
\operatorname{Var}(H_{\rm phys})
=\operatorname{Var}_\rho(K)
 +2g_x^2(1+\langle XX\rangle_\rho)
 +2g_y^2(1+\langle YY\rangle_\rho).
\tag{11}
\]

This is the variance in the full initial state `rho tensor |Phi+><Phi+|`, not an operator-valued variance or a claim that every pure input has the same variance. All full-Hamiltonian moments are conserved by the static evolution. The scalar `r` changes the mean, as specified, and cancels from the variance.

Because the ideal old output commutes with `K`, its old energy expectation equals the input expectation. The actual output obeys

\[
|\Delta\langle K\rangle|
\le \|\rho_{\rm actual}-\rho_{\rm comparator}\|_1
\le 2\epsilon_*(T),
\]

using `K-2I=ZZ` of norm 1, i.e. half the spectral width 2. This bound holds for the old marginal as well by contraction. It is an output-window estimate, not exact old-energy conservation.

For an explicit counterexample to that stronger interpretation, take the old input `|00>`. Equation (2) gives `||VJ|00>||^2=2(gx^2+gy^2)`, all in old parity minus. At small physical time `u`, ordinary Taylor expansion therefore gives

\[
\langle K\rangle_u=3-4(g_x^2+g_y^2)u^2+O(u^3).
\]

The old energy changes even though the total Hamiltonian is static. Zero modeled drive work means the prescribed-Hamiltonian term `integral Tr(rho(t) dHphys/dt) dt` vanishes. It does not set internal energy exchange, absolute energy variation, Bell preparation work, or switching/installation work to zero. Those distinctions are consistent with the proposal and necessary for its use.

## 9. Precision and limitations of the reconstruction

For a static bounded **self-adjoint** perturbation `E`, Duhamel gives `||exp[-it(Hphys+E)]-exp(-it Hphys)||<=t||E||`. Thus the stated `(T+24)||E||` addition is a sufficient absolute error budget. It is not a necessity result. Nor does it prove that a perturbed realization preserves the specified positivity, local support, or caps; those are separate checks for an actual realization. The exact initial energy identities refer to the stated ideal Hamiltonian.

A concrete cancellation example shows why necessity must not be inferred: let `E=(2pi/T) I`. At `t=T+s` the extra scalar is `exp(-i2pi s/T)`, so the uniform isometry difference on the window is at most `48pi/T`, despite the crude Duhamel budget being about `2pi`. This example concerns the stronger necessity claim, not a failure of the proposal's explicitly sufficient bound.

This review checks the exact ideal coefficients and the displayed error proof. It does not compute or certify finite representations of `pi`, `atan`, square roots, `gx`, `gy`, or `r`; derive a calibration algorithm; assess hardware noise or source preparation error; run a second evolution solver; or certify native microscopic availability. A Bell-preparation error is a separate input-embedding error, not automatically included in `E`. The existing exact irrational-parameter model and its conditional approximation are analytically supported within these limits.

## 10. Disposition and source exposure

No internal algebraic or bound counterexample was found under the stated assumptions. The required textual correction is “source triplets” to “the orthogonal Bell complement”; the operator definitions and constants need no change on this reconstruction. The full-isometry scalar, added-only cap, fixed target, finite window, new port/source permissions, supplied Bell state and timing, and energy/work qualifications are load-bearing scope boundaries.

This agent had prior exposure to the campaign's endpoint target and duration through earlier packaging work. For this check, the complete new root proposal was exposed before analysis; no author computation or independent numerical check of this new model was available or used. The derivation and counterexamples above were reconstructed analytically. Hashing, copying and freezing this review are metadata actions only. The metadata receipt is not a scientific test or an author's root approval. No original source, repository file, prompt, audit record, Git state, cache, graph, or publication was changed.

The review is sealed before reading the separately announced dyadic addendum. Any later addendum assessment is an additive document with separate exposure and pins; it does not rewrite this original reconstruction.


<!-- Unchanged complete source: dyadic_scaling_analytic_review -->

# Separate analytical review of finite coefficients and the scaled family

The original reconstruction in `REVIEW.md` was completed and sealed as `ORIGINAL_REVIEW_FREEZE.json`, SHA256 `42def22e10aa3e120a3bdf0ae4e2d7d8b8bc151f240543cfcb5ee82d18b34192`, before either addendum was read. That reconstruction remains unchanged. This document separately reviews:

- `DYADIC_ADDENDUM.md`, SHA256 `2ad3573fe74805c1f25be99f18a2eb7e70e405ebff295182557a386a6bbdf517`;
- `SCALING_ADDENDUM.md`, SHA256 `7a48fcff7b3b4c27fbf4f4e01f280293b79b69b3f11421e14118ba06be773dda`.

Both complete root-authored texts were exposed before their respective analysis. No coefficient list, interval computation, Hamiltonian evolution, or scientific program was executed. The scalar, residual and full-reference facts used below are reconstructed in the separately sealed original review, rather than inherited from a root acceptance verdict.

**Finding.** The fixed-duration dyadic bound and the accuracy-scaled error allocations are valid under the stated certified-approximant interface. A floor expression does not constitute a computed coefficient list or a uniformly terminating interval-floor algorithm at equality. An explicit lower-endpoint interval variant avoids that boundary issue by allowing twice the grid spacing as error; its constants are given below. The scaling addendum's initial-source trace allowance additionally needs an independent supplied source state, or a bound on the full initial joint-state error. A source-marginal trace bound alone is insufficient if arbitrary initial correlations are admitted. Neither qualification changes the exact ideal Hamiltonian.

## 1. Fixed-duration dyadic parameters

Let `h=2^-400`, with the original fixed `T`, and suppose the three coefficients satisfy

\[
0\le g_x-\widehat g_x\le h,\quad
0\le g_y-\widehat g_y\le h,\quad
0\le\Delta-\widehat\Delta\le h.
\tag{A1}
\]

The floor definitions have strict error below `h` and are one mathematical choice. The more general certified lower approximants in (A1) are also sufficient.

The displayed integer `T` has 22 groups of three decimal digits. Thus `10^65<=T<10^66`, and certainly `T<2^300`: `2^300=(2^10)^30>10^90`. Its lower bound `T>2^128` used in the original review also follows, for example from `2^128<2^130=(2^13)^10<10^40`. These are comparisons of the supplied literal integer, not numerical evolution or coefficient computation.

Since `theta>pi/4>3/4` and `Delta>3/2`,

\[
g_x^2=\frac{\theta\Delta}{2T}>\frac9{16T},\qquad
g_y^2=\frac\theta T>\frac3{4T}.
\]

Using `T<2^300` gives `gx>3*2^-152>2^-151` and `gy>sqrt(3)*2^-151>2^-151`. Thus subtracting at most `2^-400` cannot make either coefficient zero or negative. The source coefficient is also strictly positive. Lower rounding preserves every added incident cap because

\[
\widehat r=2(\widehat g_x+\widehat g_y)\le r,
\qquad \widehat\Delta+\widehat r\le\Delta+r<2.
\]

The same supports, positive-block form and zero runtime slew therefore remain valid.

The tunable coefficients `gxhat,gyhat,Deltahat` have denominator `2^400`. Since each is less than 2, their integer numerators have at most 401 bits; the denominator also has 401 bits. The smaller port coefficients in fact need fewer numerator bits. This is an encoding statement for those scalar coefficients. If the complete matrix entries are expanded, the fixed Bell projector has factors of `1/2`, so an additional denominator bit can appear. That does not invalidate the coefficient claim or the finite encoding statement, but one must not identify the coefficient denominator with every expanded matrix-entry denominator without this distinction.

## 2. Scalar separation and the rounded error budget

Define the actual rounded nonscalar generator

\[
\widehat A=K+\widehat\Delta Q_c
 +\widehat g_x(X_1X_A+X_2X_B)
 +\widehat g_y(Y_1Y_A-Y_2Y_B),
\]

where `Qc=I-|Phi+><Phi+|` on the source, and the actual full Hamiltonian is `Hhat=Ahat+rhat I`. The ideal nonscalar generator is `A=H0+V`. The three operator factors in `E=Ahat-A` have norms 1, 2 and 2 respectively: the two terms within each port sum commute, and the triangle bound already suffices. Hence (A1) proves

\[
\|E\|\le (1+2+2)h=5h.
\tag{A2}
\]

Multiplying both comparisons by the actual scalar `exp(-i rhat t)` gives

\[
\begin{aligned}
&\|e^{-it\widehat H}J-J e^{-i\widehat r t}e^{-isK}W e^{-iTK}\|\\
&\qquad\le \|e^{-it\widehat A}J-e^{-itA}J\|+\epsilon_*(T)
\le 5th+\epsilon_*(T).
\end{aligned}
\tag{A3}
\]

This explicitly justifies why the scalar rounding error is absent from (A2): the required source comparison is `chihat(t)=exp(-i rhat t)Phi+`. It has not been deleted from the actual evolution. If the specification instead insisted on the original `exp(-irt)Phi+`, one would need the additional scalar difference bound; that is a different output specification.

On `T<=t<=T+24<2T`,

\[
5th<10\,2^{300}2^{-400}=10\,2^{-100}<2^{-96}.
\]

Combining this with the already proved ideal `epsilon_*(T)<2^-48` yields a rounded full-isometry error strictly below `2^-47`, as claimed. The unhalved joint-reference trace error is at most twice this isometry error, hence below `2^-46`. All source qubits and the reference remain in that comparison.

The rounded coefficients need not satisfy the exact second-order tuning equation. Equation (A3) compares the two full Hamiltonians, so it does not assume that the ideal effective `H2` is unchanged after rounding. The exact initial mean and variance nevertheless retain their stated forms with hats: `Hhat J=J(K+rhat I)+Vhat J`, while the source block still annihilates `Phi+`. Full moments are conserved by the actual static `Hhat`. These conclusions require the same supplied source preparation and do not price its preparation or installation work.

## 3. Equality boundary: what is established and what is not

The real-number expression `floor(2^400 x)/2^400` defines a rational number. It does not exhibit its numerator or certify that a particular computed integer is correct. Computability of a real number alone does not give a general terminating method for deciding its floor at a grid boundary from successively narrower enclosing intervals.

Allowing a lower `h`-grid approximant with error **at most** `h` still does not, by itself, solve that algorithmic issue. At `x=k h`, the valid grid choices are `(k-1)h` and `kh`; in a strict interval that straddles `kh`, values just below the boundary require the former and values just above require the latter. No single candidate can be certified for both sides with error at most `h`. Thus an interval procedure whose stopping criterion requires that certificate need not terminate at equality. The addendum correctly leaves its coefficient certification conditional and explicitly disclaims a concrete floor implementation.

There is a simple constructive **variant**, with a slightly relaxed coefficient error, that does not need an equality decision. Compute a certified rational interval `[L,U]` containing `x`, of width at most `h`, and set

\[
a=h\lfloor L/h\rfloor.
\]

Rational floor is an ordinary exact integer operation. Then

\[
a\le L\le x,\qquad x-a\le U-L+(L-a)<2h.
\tag{A4}
\]

This always terminates once a width-`h` enclosure is supplied, including when `x` is exactly a grid point. Certified arbitrarily narrow enclosures for the specific coefficients can in principle be obtained by rational arithmetic, alternating-series enclosures for arctangents (including `pi/4=atan(1)`), and rational square-root bisection on positive intervals. This is an existence recipe, with no runtime-efficiency claim and no actual evaluation performed here.

For the fixed-duration problem, using (A4) with the same 400-bit grid gives `||E||<10*2^-400` and Duhamel error below `20*2^-100<2^-95`. The final full-isometry bound is still below `2^-47`; positivity and lower-rounding caps also survive. Thus a theorem using error below twice the grid spacing has an equality-safe construction and keeps the same scalar-coefficient bit limit. Alternatively, a 401-bit grid and a width-`2^-401` enclosure preserve the original absolute error `2^-400`, at the cost of one extra grid bit. Neither alternative is a claim that its actual coefficient integers have been computed, certified, or supplied to hardware.

## 4. Accuracy-scaled family and the changed runtime contract

The scaling addendum changes the runtime from the previous fixed external-word duration to

\[
\epsilon=2^{-m},\quad T_m=2^{2m+32},\quad m\in\mathbb Z_{\ge0},
\qquad w=24.
\]

It keeps the same fixed `K`, `W`, `theta`, `delta`, source Hamiltonian form and port permissions, with `q=theta/T_m`. The exact spectral and scalar identities in the original reconstruction are algebraic in `T` and hold at this new positive `T_m`. The residual proof itself needs `T>=24`, not `T>2^128`; the latter was only a convenient numerical error bound for the old duration. Already at `m=0`, `T_m=2^32>24`.

With `A(T)=12352/sqrt(T)+132480/T`, direct division gives

\[
\frac{A(T_m)}\epsilon
=\frac{12352}{2^{16}}+\frac{132480}{2^{32}}2^{-m}
\le \frac{193}{1024}+\frac{1035}{2^{25}}
=\frac{6325259}{33554432}<\frac14.
\tag{A5}
\]

The last strict inequality compares the numerator with `8388608`. It includes the entire window contribution `384/T`; that term has not been omitted or counted twice.

The ideal port norm sum satisfies

\[
r<4/\sqrt{T_m}=2^{-(m+14)}\le2^{-14}<\delta.
\]

Thus the caps are valid even at `m=0`; the old total still includes its separate norm-3 `K`. The coefficients satisfy

\[
g_x>3\,2^{-(m+18)}>2^{-(m+17)},
\qquad g_y>\sqrt3\,2^{-(m+17)}>2^{-(m+17)}.
\]

For `p=3m+38`, the proposed lower coefficient error `2^-p` is strictly smaller than either port coefficient for all `m>=0`. Hence the rounded positive blocks remain strictly positive in their nonzero eigenvalue and retain the same supports. Their scalar numerators have at most `p+1` bits because the coefficients are below 2.

For certified lower errors at most `2^-p`, (A2) and `t<2T_m` give

\[
5t2^{-p}<10\,2^{2m+32}2^{-(3m+38)}
=\frac5{32}\epsilon.
\]

Together with (A5), this yields

\[
\text{full-isometry error}<\frac{13}{32}\epsilon<\frac\epsilon2,
\qquad
\text{unhalved joint trace error}<\frac{13}{16}\epsilon<\epsilon.
\tag{A6}
\]

These constants are correct. With the equality-safe lower-endpoint algorithm (A4), use instead `p=3m+39` and interval width at most `2^-p`. Its error is below `2*2^-p`; consequently `||E||<10*2^-p`, and

\[
t\|E\|<20\,2^{2m+32}2^{-(3m+39)}
=\frac5{32}\epsilon,
\]

preserving (A6). This one-bit variant is an explicit algorithmic adjustment, not an assertion that the original `p=3m+38` floor procedure has already been implemented. No list of actual rounded coefficients is part of this review.

## 5. Initial-source defect and arbitrary references

The addendum's extra `delta_init` allowance is valid when the supplied source is an independent state `tau_AB` with

\[
\|\tau_{AB}-|\Phi_+\rangle\langle\Phi_+|\|_1\le\delta_{\rm init},
\]

and the full initial state is `rho_SR tensor tau_AB`. The product trace norm equals the source trace norm, and the common unitary on old plus source (tensored with the identity on the reference) preserves the difference. The triangle inequality with (A6) then gives final unhalved joint trace error below `epsilon+delta_init`. The same reasoning works if a bound of `delta_init` on the **full** initial old/reference/source deviation from the intended product state is supplied directly.

If only the source marginal is controlled while arbitrary pre-existing correlations are allowed, that linear allowance is not justified. For example, choose an orthogonal source vector `Xi` and let

\[
|\Omega\rangle=\sqrt{1-\eta}\,|0\rangle_S|\Phi_+\rangle
 +\sqrt\eta\,|1\rangle_S|\Xi\rangle,
\qquad 0<\eta<1/2.
\]

Its source marginal has trace defect `2 eta`. The full state differs from `rho_S tensor |Phi+><Phi+|` by at least `2 sqrt(eta(1-eta))` in trace norm: the norm-1 Hermitian witness `|0,Phi+><1,Xi|+|1,Xi><0,Phi+|` has that expectation difference. This is larger than `2 eta` for the stated range. Consequently source-marginal closeness alone cannot be substituted for the full initial error bound. This example does not contradict the original product-source embedding; it identifies the assumption needed when extending it to an imperfect source.

## 6. Resource and decision limits

For this fixed target in the newly supplied interaction model, `gx` and `gy` are constant multiples of `epsilon`, `T_m=2^32 epsilon^-2`, and the sufficient absolute coefficient tolerance is a constant multiple of `epsilon^3`. The bit lengths are `O(log(1/epsilon))` as `epsilon` tends to zero. These are constructive upper bounds within the conditional model, not optimality, necessary precision, efficient parameter synthesis, laboratory availability, or preparation/reset bounds. The fixed numerical prefactors and the unassigned physical energy/time units must remain visible.

At `epsilon=2^-44`, `T_m=2^120` follows from `2m+32=120`. This is smaller than the old supplied duration, but it changes the runtime and interaction contract. It does not shorten or re-execute the earlier positive-onsite target word, and it does not realize the new port/source interactions from those onsite rays. The ideal target still commutes with `K`; the full energy identities and static work qualifications remain those of the original review, with actual rounded coefficients where applicable.

The addenda are therefore analytically supported with the certified-approximant/equality-boundary and initial-source independence qualifications above. The optional interval construction has been proved symbolically here, but it has not been run. Root qualification, actual coefficient computation, physical realization, canonical integration, publication and retained audit status remain outside this review.


<!-- Unchanged complete source: finite_compiler_analytic_review -->

# Analytical review of the proposed finite rational coefficient compiler

Source: `weak_mediator_candidate/FINITE_COMPILER_ADDENDUM.md`, SHA256 `7c54639374626757ac9aa4d32a5bf23b317a62e2560d8ed4c4c1651f15babed8`. The complete source was read before this reconstruction. The prior review packet, final freeze `ef8dce286398c515be38142b54917e2b82d8ea3363709f78f37e70f11a71511c`, remains unchanged.

**Finding.** The proposed finite construction has valid rational enclosures, a valid equality-safe integer-square-root rounding rule, positive lower coefficients, and the claimed scaling error budget. No mathematical counterexample to those statements was found. The operation count requires a precise qualification: there are `3n` terms in the three partial sums **plus three first-omitted remainder terms** used to form the intervals. If “exactly 3n terms” means all evaluated term values, it is incomplete. The three integer divisions are the three explicit final floor-quotient calls, rather than the total divisions performed by rational arithmetic or an implementation of `isqrt`. These accounting issues do not alter the coefficient error bound.

This is a source-exposed analytic check, not a run of the compiler or a certificate for actual output numerators. The reviewer previously proposed the lower-endpoint rounding strategy and the extra scaling bit; thus this is not an independent invention of that strategy or a blind review. The root's new fixed-term arctangent construction, interval algebra and integer-square-root realization are reconstructed below. No scientific program, coefficient computation or evolution was executed. Root qualification, physical implementation and retained audit status remain separate.

## 1. Definitions and reused mathematical premises

For integer `m>=0`, the addendum sets

\[
\epsilon=2^{-m},\quad T=2^{2m+32},\quad p=3m+39,
\quad h=2^{-p},\quad n=p+8.
\]

The fixed target uses `theta=atan(4/3)`, `delta=theta/pi`, `Delta=2-delta`, and

\[
g_y^2=\theta/T,\qquad g_x^2=\theta\Delta/(2T).
\]

The earlier source-exposed reconstruction established, under the supplied Bell-projector/port Hamiltonian and product Bell source, the ideal full-isometry bound

\[
A(T)=12352/\sqrt T+132480/T,
\qquad A(T)/\epsilon<1/4,
\tag{1}
\]

on the entire window `[T,T+24]`. Its source pins are recorded as an explicit bounded reference rather than recursively copying the prior evidence archive. The present check does not assume a root acceptance verdict for these premises. It reuses the exact prior analytic identities at their unchanged hashes; no earlier science process is replayed.

## 2. Alternating intervals and Machin signs

For `a` equal to 5, 239 or 7, define the positive term

\[
t_{a,j}=\frac{1}{(2j+1)a^{2j+1}}.
\]

The terms decrease strictly to zero. The alternating-series theorem gives

\[
\arctan(1/a)-S_a(n)
\text{ has sign }(-1)^n
\quad\text{and magnitude }<t_{a,n}.
\]

Therefore sorting `S_a(n)` and `S_a(n)+(-1)^n t_{a,n}` indeed gives a strict enclosure `[L_a,U_a]`, of exact width `t_{a,n}`. These endpoints are the two consecutive partial sums `S_a(n),S_a(n+1)`. No decision about a transcendental equality is involved.

The Machin identity can be checked directly, including its branch. Let `a0=atan(1/5)` and `b0=atan(1/239)`. Tangent doubling gives

\[
\tan(2a_0)=5/12,\qquad \tan(4a_0)=120/119.
\]

Thus

\[
\tan(4a_0-b_0)=
\frac{120/119-1/239}{1+120/(119\cdot239)}=1,
\]

since both numerator and denominator, on common denominator `119*239`, are `28561`. Also `4a0-b0>0` using `a0>1/5-1/375` and `b0<1/239`, while `4a0-b0<4/5<pi/2`. The angle is consequently `pi/4`, proving `pi=16 atan(1/5)-4 atan(1/239)` with the displayed signs. Similarly, the first-quadrant tangent addition formula proves `theta=pi/4+atan(1/7)`.

Positive and negative coefficients must use opposite enclosure endpoints. The proposed

\[
\pi_L=16L_5-4U_{239},\qquad
\pi_U=16U_5-4L_{239}
\]

have exactly that ordering. Adding the positive arctangent term then gives the stated valid `theta_L,theta_U`.

## 3. Widths and rational guards

Write `k=2n+1`. The exact pi width is

\[
16t_{5,n}+4t_{239,n}<20\,5^{-k}.
\]

The theta width is one fourth of this width plus `t_{7,n}`; it is also smaller than the common bound `20*5^-k` (a constant 6 would already suffice). Since `5>4`,

\[
20\,5^{-(2n+1)}<20\,2^{-(4n+2)}
<2^{-(2p+12)}=:w.
\tag{2}
\]

For the last inequality, substitute `n=p+8`: the ratio of the preceding bound to `w` is `20*2^(-2p-22)<1`. This is valid in particular for `p>=39`. The value `w` here is an interval-width bound, distinct from the physical window length 24.

The guards are provable without running a rational test. Since `n>=47`, the alternating partial-sum ordering gives

\[
L_5\ge1/5-1/375=74/375,
\quad U_{239}\le1/239,
\quad U_5\le1/5,
\quad L_{239}>0,
\quad 0<L_7<U_7\le1/7.
\]

It follows that

\[
\pi_L\ge16(74/375)-4/239>3,
\qquad \pi_U<16/5.
\]

The first strict comparison reduces to `59/375>4/239`. Consequently

\[
0<\theta_L<\theta_U<4/5+1/7=33/35<1.
\tag{3}
\]

In fact `theta_L>3/4`, which is more than is needed for interval ordering. These facts justify all positive divisions below. They could also be retained as exact rational runtime guards without changing the mathematics.

## 4. Delta and product intervals

For positive numerator and denominator intervals, the minimum of `theta/pi` uses `theta_L/pi_U` and the maximum uses `theta_U/pi_L`. Thus

\[
\Delta_L=2-\theta_U/\pi_L,
\qquad \Delta_U=2-\theta_L/\pi_U
\]

correctly enclose `Delta`. Moreover `Delta_L>2-1/3=5/3>0`, and `Delta_U<2`. The interval is ordered. Its width obeys

\[
\begin{aligned}
\Delta_U-\Delta_L
&=\frac{\theta_U-\theta_L}{\pi_L}
 +\frac{\theta_L(\pi_U-\pi_L)}{\pi_L\pi_U}\\
&<w/3+w/9=4w/9<w/2.
\end{aligned}
\tag{4}
\]

Both factors in `theta Delta` are positive throughout their intervals. Their correlation does not invalidate interval multiplication: the containing rectangle still contains the true pair. Hence

\[
y_L=\theta_L/T\le g_y^2\le\theta_U/T=y_U,
\]

\[
x_L=\theta_L\Delta_L/(2T)\le g_x^2
\le\theta_U\Delta_U/(2T)=x_U.
\]

The widths satisfy

\[
y_U-y_L<w/T,
\]

\[
x_U-x_L
=\frac{\Delta_U(\theta_U-\theta_L)+\theta_L(\Delta_U-\Delta_L)}{2T}
<\frac{2w+w/2}{2T}<2w/T.
\tag{5}
\]

In particular, no unproved monotonicity of the composite function `theta(2-theta/pi)` is needed; the positive interval product is sufficient.

## 5. Exact nested floor and square root

Let the positive rational lower endpoint be `a=A/B`, with positive integers `A,B`, and set `D=2^p`, `z=D^2 A/B`, `N=floor(z)`, `k=isqrt(N)`. Then

\[
k^2\le N<(k+1)^2.
\]

The upper endpoint is an integer, so `N+1<=(k+1)^2`. Since `N<=z<N+1`,

\[
k^2\le z<(k+1)^2,
\qquad k/D\le\sqrt a<(k+1)/D.
\tag{6}
\]

Thus `k_p(a)/2^p` is a lower approximation with error **strictly below** `h`. This proves the nested-floor identity rather than assuming that two floors can generally be interchanged. It remains valid when the rational argument is a perfect square, when `D^2 a` is an integer, and when the coefficient is exactly on a grid boundary. Only integer comparisons/division and the integer floor square root are required.

For positive interval endpoints, `sqrt(u)-sqrt(l)<=sqrt(u-l)`. Equation (5) and `T>=2^32` give

\[
2w/T\le h^2 2^{-43}<h^2/4,
\]

so both square-root intervals have width strictly below `h/2`. Combining that uncertainty with (6) yields

\[
0\le g_x-\widehat g_x<3h/2<2h,
\qquad 0\le g_y-\widehat g_y<3h/2<2h.
\tag{7}
\]

The direct rational floor for Delta satisfies

\[
0\le\Delta-\widehat\Delta
<(\Delta_U-\Delta_L)+h<w/2+h<2h.
\tag{8}
\]

This is a finite equality-safe realization of the previously proposed lower-endpoint strategy. It does not require computing the floor of an irrational coefficient itself, detecting its equality to a dyadic number, or iterating an analytic enclosure until such a decision becomes possible.

## 6. Positivity, caps and output bit lengths

The previously derived bounds follow here from `theta>3/4`, `Delta>3/2` and the exact `T`:

\[
g_x>3\,2^{-(m+18)}>2^{-(m+17)},
\qquad g_y>\sqrt3\,2^{-(m+17)}>2^{-(m+17)}.
\]

Since `2h=2^(-3m-38)<2^(-m-17)` for every `m>=0`, equations (7) and (8) leave all three coefficients strictly positive. For Delta, its lower bound above `3/2` is much larger than `2h`; this covers the third coefficient separately. The exact lower ordering gives

\[
\widehat r=2(\widehat g_x+\widehat g_y)\le r,
\qquad \widehat\Delta+\widehat r\le\Delta+r<2.
\]

At `m=0`, `r<2^-14<delta`, so there is no small-`m` cap exception. These are added-block incident caps. The old vertex also has the distinct norm-3 literal `K`; the total old incident sum is not below 2.

Each reported scalar coefficient is positive and less than 2. When expressed on denominator `D=2^p`, its numerator is an integer less than `2D=2^(p+1)`, and therefore uses at most `p+1` bits; `D` itself uses `p+1` bits. The two ports admit an even smaller numerator bound because their coefficients are below 1. This proves the stated uniform output encoding bound. It does not bound intermediate rational numerators/denominators, nor every expanded Hamiltonian matrix-entry denominator: the fixed Bell projector contains a factor `1/2`.

## 7. Error allocation, scalar and initial state

After separating the actual `rhat I`, the three nonscalar error operators have norms 1, 2 and 2. Equations (7) and (8) therefore give

\[
\|\widehat A-A\|<10h.
\]

For `t in [T,T+24]`, one has `t<2T`, and the Hermitian Duhamel bound gives

\[
t\|\widehat A-A\|<20T h
=20\,2^{2m+32-(3m+39)}
=\frac5{32}\epsilon.
\tag{9}
\]

The comparison uses the actual source vector `exp(-i rhat t)Phi+`. Multiplying both nonscalar evolutions by that common actual scalar is legitimate; no reserve phase has been silently discarded. The ideal second-order tuning need not survive rounding, because (9) compares the full Hamiltonians.

For completeness the reused ideal allocation is

\[
\frac{A(T)}\epsilon
\le\frac{12352}{2^{16}}+\frac{132480}{2^{32}}
=\frac{6325259}{33554432}<\frac14.
\]

Combining it with (9) proves full-isometry error below `13 epsilon/32`. Tensoring with an arbitrary reference preserves the operator norm, and the unhalved joint trace error is at most twice the isometry error, hence below `13 epsilon/16<epsilon`. All four system/source qubits remain in the comparison.

The initial-state qualification now states the correct premise: an independent supplied source state with trace defect `delta_init`, or directly a full initial old/reference/source trace defect bound. Unitary invariance and the triangle inequality then add at most `delta_init`. The earlier marginal-only correlated-source counterexample is excluded by that premise. Exact initial mean/variance identities continue to apply to the intended exact Bell input and the actual rounded Hamiltonian; an imperfect source is covered by the trace-error extension, not by an assertion that its exact initial moments are unchanged.

## 8. Operation accounting and remaining obligations

There are three partial sums, each containing `n` terms, so **3n summed terms** is correct. Each interval also needs its first omitted term `t_(a,n)`. Thus a count of evaluated alternating-series term values is `3n+3`, not just `3n`. With `n=3m+47`, these counts are `9m+141` summed terms and three additional remainder terms. Power or denominator recurrences can reuse arithmetic, but they do not remove the need to evaluate the three remainder magnitudes.

Once the rational lower endpoints have been built, final rounding makes exactly three explicit floor-quotient calls:

1. `floor(2^(2p) A_x/B_x)`;
2. `floor(2^(2p) A_y/B_y)`;
3. `floor(2^p A_Delta/B_Delta)`.

It also makes two `isqrt` calls. This is a valid high-level count of these final primitives. It is not a count of every integer division in the whole implementation: forming rational sums, quotients, common denominators or gcd reductions, and implementing `isqrt`, can require further divisions and other operations. A particular integer-square-root routine may have a finite discrete loop; the claim that survives is the absence of an open-ended **real-enclosure equality search**, not the absence of loops inside arithmetic primitives.

The fixed term count and exact rational/integer operations do specify a finite mathematical algorithm. The output coefficient bit lengths are `O(log(1/epsilon))`; that does not by itself establish an `O(log(1/epsilon))` running time, an intermediate bit-size bound, or a bit-complexity optimum. No actual coefficient numerator or output certificate was generated by this review. Source/exposure capture and hash validation are metadata evidence only.

The conditional physical boundaries remain unchanged: the Bell-projector source block and the four port interactions are newly supplied permissions, not consequences of the original positive onsite rays. Source preparation, installation, exact-to-physical calibration, energy/time units, external timing and halt/reset/reuse remain independent premises or obligations. The fixed-target time and precision bounds are sufficient upper bounds in this supplied model, not universal lower bounds or native availability claims. No original source, previous review, repository state, prompt, audit record, cache, graph, Git ref or publication was modified.

The analytic conclusion supports the finite compiler formulas with the operation-count qualifications above. It is not a root acceptance record, an execution certificate, or a retained-status verdict.


<!-- Unchanged complete source: window_reuse_analytic_review -->

# Analytical check of the enlarged window and finite coherent reuse

The complete root-authored `WINDOW_REUSE_ADDENDUM.md`, SHA256 `fb9c0e08fbfa8337fe9c8c64cac29c216f0424046846e7361174f3681950dc33`, was read before this reconstruction. The original weak-mediator and finite-compiler review packets remain frozen and unchanged. This is a separate source-exposed analytic check, not a blind review, a numerical experiment, an execution of the compiler, a root approval, or a retained verdict.

**Finding.** The enlarged-window allocation `15 epsilon/32`, the full-reference telescoping bound with the source retained, and the stated sufficient finite-use runtime bounds follow. The reuse proof does not assume that the actual source is exactly restored or uncorrelated after a use. It does require the initial product-source interface (or a separately budgeted full initial-state defect), and each supplied intervention must act as the identity on the source. The window compares against literal old aging at the actual elapsed time, not a time-independent output plateau. Runtime bounds count the Hamiltonian intervals; physical implementations of the optional intervention interfaces need their own duration and error budgets.

I found no mathematical defect in the stated window/reuse inequalities under these qualifications. The result is a finite-budget, fixed-target statement within the newly supplied interaction model. It does not provide permanent halt, an internal clock, native arbitrary controls, exact reset, or a fixed device that can be reused indefinitely at a fixed error allowance.

## 1. Exact reused scope

The initial old/source embedding remains `J psi=psi tensor Phi+`, where the source consists of two qubits. The literal old Hamiltonian is `K=2I+ZZ`, with eigenvalues 1 and 3, and `W=e^(i theta)e^(i theta XX)` commutes with `K`. The actual rounded Hamiltonian `Hhat` has positive lower dyadic coefficients and an actual identity reserve `rhat I`. Its source comparison phase is `exp(-i rhat t)Phi+`.

The prior analytic proofs establish the residual, effective Hamiltonian, positivity/caps and equality-safe coefficient error without running the model. Their exact review and freeze identities are recorded in `SOURCE_EXPOSURE.json`. The current check reuses those unchanged proofs rather than asserting an author or audit verdict. It does not import a different target, microscopic plant or physical controller.

For `m` a nonnegative integer, put

\[
\epsilon=2^{-m},\quad T=2^{2m+32},\quad p=3m+39,
\quad w_m=\epsilon T/256=2^{m+24}.
\]

Then `w_m>=2^24>24` and `w_m/T=epsilon/256<=1/256<1`. Thus every allowed `t=T+s`, `0<=s<=w_m`, is strictly less than `2T`. No previous step of the bare residual proof depended on an upper window length of 24 except when its separate effective drift was estimated.

## 2. Window constants and retained scalar

The bare residual and endpoint-correction bound is

\[
R(T)=12352/\sqrt T+132096/T.
\]

It is below the previously checked `A(T)=R(T)+384/T`, so `R(T)<epsilon/4`. Direct substitution also checks this independently:

\[
\frac{R(T)}\epsilon
\le\frac{193}{1024}+\frac{1032}{2^{25}}
=\frac{6325256}{33554432}<\frac14.
\tag{1}
\]

The ideal second-order Hamiltonian has norm `4pi/T<16/T`. Therefore its extra drift on the larger window is bounded by

\[
s\|H_2\|<16w_m/T=\epsilon/16.
\tag{2}
\]

The finite compiler yields a lower error strictly below `2*2^-p` in each of three scalar coefficients. After separating the actual `rhat I`, the nonscalar generator defect is strictly below `10*2^-p`. Duhamel on `t<2T` gives

\[
t\|\widehat A-A\|<20T2^{-p}
=20\,2^{2m+32-(3m+39)}
=5\epsilon/32.
\tag{3}
\]

Adding (1), (2) and (3) proves the proposed uniform full-isometry bound

\[
\left\|e^{-i(T+s)\widehat H}J
-J e^{-i\widehat r(T+s)}e^{-isK}W e^{-iTK}\right\|
<\eta,\qquad \eta=15\epsilon/32.
\tag{4}
\]

The coefficient of `epsilon` is exactly `1/4+1/16+5/32=15/32`. The actual reserve phase multiplies both nonscalar comparisons; it has not been dropped. Since both maps are isometries, their unhalved joint-reference trace discrepancy is at most twice the norm difference, hence below `15epsilon/16<epsilon`.

The parameters `T,p` and all coefficient/positivity/cap constructions are unchanged by extending the window. At `m=44`, the exponents give `T=2^120` and `w_m=2^68`, as claimed. These are in the same dimensionless units; no physical clock precision or energy unit is supplied by the exponent arithmetic.

## 3. Actual elapsed aging is load-bearing

Since `W` commutes with `K`, the ideal old factor in (4) can be written as

\[
U_s=e^{-i\widehat r(T+s)}W e^{-i(T+s)K}.
\tag{5}
\]

Thus the gate is compared relative to the old evolution for the actual duration `T+s`. The literal `2I` inside `K` and the actual reserve both retain their full scalar phases. The statement does not imply closeness, uniformly in `s`, to the single fixed vector `W exp(-iTK) psi`, nor does it identify different observation times.

There is a simple exact counterexample to the stronger fixed-output interpretation. Choose an old input with equal norm in the two `K` eigenspaces, for example `(|00>+|01>)/sqrt(2)`. The commuting `W exp(-iTK)` preserves these weights. Ignoring only a common scalar in the inner product, the two ideal outputs at `s=0` and `s=pi/2` have overlap

\[
\tfrac12(e^{-i3\pi/2}+e^{-i\pi/2})=0.
\]

Their density states are orthogonal and have unhalved trace distance 2. Both observation times lie in every stated window. This is not a counterexample to (4); it establishes why the aging term cannot be suppressed even at the density-channel level. A separate fixed-time clock or compensation contract must account for old drift and the full phases.

The enlarged window is finite. Its estimate does not describe switched-off interactions, an exactly stationary output, permanent halt, or arbitrary late observation times.

## 4. Source-retaining telescoping argument

Let `R` denote all retained reference registers, and `J_R` append the fixed Bell source to the arbitrary old/reference input. Extend each actual runtime unitary by the identity on `R`, and each ideal `U_j=U_(s_j)` by the identity on `R`. Equation (4) gives

\[
\|V_jJ_R-J_RU_j\|<\eta
\tag{6}
\]

for every specified `s_j` in the allowed window. Tensoring with a reference preserves the operator norm.

For an old/reference-only unitary `A_j`, put `Atilde_j=A_j tensor I_source`. The exact intertwining identity is

\[
\widetilde A_j J_R=J_R A_j.
\tag{7}
\]

Let `M_j` be the actual isometry after `j` runtime intervals and the intervening supplied unitaries; let `N_j` be the corresponding ideal old/reference unitary. With `M_0=J_R`, `N_0=I`, and `A_0=I`, the recursions are

\[
M_j=V_j\widetilde A_{j-1}M_{j-1},
\qquad N_j=U_j A_{j-1}N_{j-1}.
\]

Using (7) gives the exact difference identity

\[
\begin{aligned}
M_j-J_RN_j
={}&V_j\widetilde A_{j-1}(M_{j-1}-J_RN_{j-1})\\
&+(V_jJ_R-J_RU_j)A_{j-1}N_{j-1}.
\end{aligned}
\tag{8}
\]

The operators multiplying the two differences have norm 1. Iterating (8), starting from zero initial difference, proves

\[
\|M_L-J_RN_L\|<L\eta
\tag{9}
\]

for every positive finite integer `L`. This is the telescoping product proof in recursive form.

Crucially, (6) is applied to the **ideal embedded prefix** in the second line of (8). It is not applied directly to a potentially correlated actual source. All actual source errors and correlations are contained in the first-line difference and propagated by a unitary. Consequently no exact source reset, independence or fresh Bell preparation between uses is assumed. The source is retained throughout. Arbitrary old/reference entanglement, including that created by earlier supplied `A_j`, is already within the domain of (6).

The composed maps are isometries. Therefore the unhalved full joint trace error is strictly below `2Leta=(15/16)Lepsilon<Lepsilon`, with mixed inputs handled by purification. No source or reference register is discarded to obtain this bound.

If the initial product-source state is imperfect, a full initial joint trace defect `delta_init` adds only once to the whole sequence by unitary invariance and the triangle inequality. An independent imperfect source is a sufficient way to provide that bound. A source-marginal defect alone is not sufficient when pre-existing source correlations are allowed. The stated final allowance without an extra term assumes the exact initial Bell source; an imperfect-source allowance must be reserved separately.

## 5. No-intervention case and ordered interfaces

With no interventions, the actual unitaries are generated by the same constant Hamiltonian, so their product is exactly

\[
\exp\left[-i\left(\sum_j(T+s_j)\right)\widehat H\right].
\]

Because the corresponding ideal interval factors commute in this special case, their product is

\[
e^{-i\widehat r\sum_j(T+s_j)}W^L
e^{-iK\sum_j(T+s_j)}.
\tag{10}
\]

For all `s_j=0`, this is exactly the proposed `exp(-i rhat LT)(W exp(-iTK))^L`. The isometry embedding and retained source remain present. This is a repeated fixed-gate/power guarantee; it does not supply an arbitrary programmable target family.

With interventions, their order in `N_L=U_L A_(L-1) ... U_2 A_1 U_1` must be preserved. Generic `A_j` do not commute with `K` or `W`, so (10) cannot then be used. Each interface is explicitly a supplied unitary on old plus retained reference, with identity on the source. A physical intervention performed while the mediator interaction remains on need not have that form. A finite-duration realization must include its full action, old aging, reserve phase, source disturbance and errors in a separate interface contract. Its duration is not silently part of the `L` mediator intervals.

The proof covers common specified unitary interfaces and interval durations. Source-acting operations, discarded measurement outputs, or unmodeled adaptive timing mechanisms require an enlarged model and an error budget. The optional reference registers and supplied controllers are also not included in the claim that the **source** contains exactly two qubits.

## 6. Finite-use accuracy and resource scaling

Take `m0` to be a nonnegative integer, `epsilon0=2^-m0`, and `L` a positive integer. Set `k=ceil(log2 L)`, equivalently the least nonnegative integer with `2^k>=L`, and let `m=m0+k`. No floating-point logarithm is required to define or determine that integer.

Then

\[
\epsilon=\epsilon_0/2^k\le\epsilon_0/L.
\]

Equation (9) gives a final unhalved joint trace error strictly below `(15/16)Lepsilon<=15epsilon0/16<epsilon0`, assuming the exact initial source and exact supplied intervention interfaces. The controller parameters are chosen for this known finite use budget; they are not fixed independently of arbitrary future `L`.

The coefficient precision is `p=3(m0+k)+39`. Since `2^k<2L` for every `L>=1`, including `L=1`,

\[
T=2^{32}2^{2k}\epsilon_0^{-2},\qquad
LT<2^{34}L^3\epsilon_0^{-2}.
\tag{11}
\]

The strict bound indeed holds for `L=1`: the exact endpoint duration is `2^32 epsilon0^-2`, less than the stated `2^34` upper bound. For durations chosen anywhere in their enlarged windows,

\[
\sum_j(T+s_j)\le L(T+w_m)<2LT
<2^{35}L^3\epsilon_0^{-2}.
\tag{12}
\]

Equations (11) and (12) count mediator-evolution time. They exclude implementation time for the optional supplied interventions, preparation, installation, measurement/reset or other external operations. This qualification is necessary if “total runtime” is used on a physical publication surface.

The source count remains two; the added incident caps and zero slew during each runtime interval remain valid. With the finite budget specified in advance, the port couplings scale as `O(epsilon0/L)`, sufficient coefficient accuracy as `O((epsilon0/L)^3)`, and coefficient bit lengths as `O(log(1/epsilon0)+log L)`. These are upper bounds within the supplied model, not optimality, necessary precision or a proof of an efficient physical implementation.

At fixed `m`, the bound grows with `L` and eventually ceases to give a small error. Choosing a new `m` for a larger planned `L` is a family of finite-budget constructions, not indefinite reuse of one fixed implementation. No exact reset or autonomous stopping mechanism follows.

## 7. Exposure and verification limits

The whole new argument was checked analytically after exposure to the root's proposal. Prior exact residual and compiler proofs are reused at their pinned identities. No compiler, Hamiltonian evolution, numerical coefficient generation, simulation or scientific source import occurred. The newly announced structured-coefficient proposal was not read before this window/reuse review was completed and sealed.

Only metadata scripts copy the new source, verify prior freezes and record this packet's exact identities, source-at-launch captures and complete streams. They are not physical experiments, mathematical proof assistants or author approvals. The original candidate, both previous review packets, repository files, editable prompts, Git state, cache, graph, PRs and audit records remain unchanged.


<!-- Unchanged complete source: structured_analytic_review -->

# Analytical review of the three-coefficient perturbation bound

The complete root-authored `STRUCTURED_COEFFICIENT_ADDENDUM.md`, SHA256 `052bcf3f2b5577ab5f8d4988f42d25cbb0f52ec6d61999a7a269072f44f14395`, was exposed before this reconstruction. The original, finite-compiler and window/reuse review packets remain unchanged. In particular, the window/reuse review was sealed before this source was read.

**Finding.** The stated `7 epsilon/16` full-isometry bound follows for the specified three lower coefficient replacements, with the actual reserve phase in the comparator. The mixed grids `p_g=2m+29` and `p_D=m+14` give the claimed sufficient errors, including at `m=0`. No internal algebraic or constant defect was found. Two proof details are essential: the port norm is monotone here because of this particular commuting Pauli family, and lowering Delta preserves the claimed cross-spectrum gap only because the allowed range keeps `Deltahat>3/2`. The improved tolerances do not apply to an arbitrary generator fault or to a comparator that silently replaces the actual reserve phase by the original one.

This is a separate source-exposed analytic check. It is not a blind review, an execution certificate, a computed coarse coefficient list, a root approval or a retained verdict. The reviewer contributed the earlier lower-endpoint rounding strategy; the new Gram/resolvent perturbation proof and mixed precision allocation were reconstructed from the complete root source. No scientific program or coefficient computation was executed.

## 1. Parameter range, positivity and the actual gap

For integer `m>=0`, use

\[
\epsilon=2^{-m},\quad T=2^{2m+32},\quad
\theta=\arctan(4/3),\quad\delta=\theta/\pi,
\quad\Delta=2-\delta,
\]

\[
g_x=\sqrt{\theta\Delta/(2T)},\qquad
g_y=\sqrt{\theta/T}.
\]

The exact angle facts checked previously include `3/4<theta<1`, `pi>3`, and `1/4<delta<1/2`. In particular, the stronger bound

\[
\Delta>2-1/3=5/3
\tag{1}
\]

is available here. The proposed allowances are

\[
h_g=\frac\epsilon{4096\sqrt T}=2^{-(2m+28)},
\qquad h_D=\frac\epsilon{8192}=2^{-(m+13)}.
\]

All errors are one-sided: `0<=gx-gxhat<=h_g`, and likewise for `gy`, while `0<=Delta-Deltahat<=h_D`. The prior lower port bound `gx,gy>2^(-(m+17))` implies positivity after these replacements, because `h_g/2^(-(m+17))=2^(-m-11)<1`.

For the source coefficient, (1) gives

\[
\widehat\Delta>5/3-2^{-13}>3/2,
\qquad \widehat\Delta\le\Delta<2.
\tag{2}
\]

Thus `deltahat=2-Deltahat` lies between `delta>1/4` and `1/2`. The full old-to-source-complement Sylvester differences are

\[
\widehat\Delta,\quad\widehat\Delta-2,
\quad\widehat\Delta+2.
\]

Their minimum absolute value is exactly `deltahat`, because (2) keeps it smaller than `Deltahat`. Therefore the actual cross-spectrum separation is at least the original `delta`. Lowering a source coefficient in an unrestricted range would not by itself prove this fact: if it approached zero, the difference `Deltahat` would become the small gap instead. The explicit lower bound (2) rules out that failure.

The positive-block supports are unchanged. Lower coefficients give `rhat=2(gxhat+gyhat)<=r` and `Deltahat+rhat<=Delta+r<2`. These remain added incident caps; the old vertices still have the separate norm-3 literal `K`. Constant coefficients preserve zero runtime slew. None of these facts supplies the new interactions from the original onsite control rays.

## 2. Why the port norm decreases in this family

Write

\[
P_1=X_1X_A,\quad P_2=X_2X_B,\quad
Q_1=Y_1Y_A,\quad Q_2=Y_2Y_B,
\]

so `V=gx(P1+P2)+gy(Q1-Q2)`. All four displayed port Pauli operators commute. Operators on different pairs `(1,A)` and `(2,B)` have disjoint supports. On a single pair, the two local anticommutations cancel, giving `[XX,YY]=0`.

The norm triangle bound gives `||V||<=2(gx+gy)`. It is attained: choose the Bell state on pair `(1,A)` with `XX=YY=+1` (`Psi+`), and on pair `(2,B)` with `XX=+1,YY=-1` (`Phi+`). Their tensor product is an eigenvector of `V` with eigenvalue `2(gx+gy)`. Consequently

\[
v:=\|V\|=2(g_x+g_y)=r,
\qquad \widehat v:=\|\widehat V\|=2(\widehat g_x+\widehat g_y)=\widehat r\le v.
\tag{3}
\]

This supplies the needed justification for the norm monotonicity used in the addendum. Monotonicity does not hold merely because some coefficients of an arbitrary sum are lowered. Only the port terms commute here; this is not a claim that the ports commute with `K` or the source Bell projector.

The port difference obeys

\[
\|\widehat V-V\|\le2|\widehat g_x-g_x|+2|\widehat g_y-g_y|
\le4h_g.
\tag{4}
\]

## 3. Generic second-order operator without the tuning relation

The source embedding and Pauli signs remain exactly those of the original model. For any positive common port coefficients of this form, the Bell calculation gives

\[
M=J^*V^2J=2g_x^2(I+XX)+2g_y^2(I+YY),
\]

and the same expression with hats gives `Mhat`. Both commute with old `ZZ`. For an old parity `z`, the first Sylvester denominator is `Delta-2z`, so with

\[
D=\Delta I-2ZZ,
\qquad \widehat D=\widehat\Delta I-2ZZ,
\]

the exact second-order operators in the respective residual constructions are

\[
H_2=-MD^{-1},\qquad
\widehat H_2=-\widehat M\widehat D^{-1}.
\tag{5}
\]

These are Hermitian because the two factors in each product commute and are Hermitian. They commute with literal `K=2I+ZZ`. The special ideal relation between `gx,gy,Delta` is not needed for these properties. It is needed to identify `exp(-iT H2)` with the exact target `W`; no such exact target equality is asserted for `H2hat`.

The actual Sylvester construction can therefore use `Ghat=K+H2hat` as a Hermitian comparison generator. With its own `S1hat,S2hat`, the same exact cancellation gives `Rhat=Vhat S2hat-S1hat H2hat-S2hat H2hat`. The Frobenius inverse uses the actual gap from (2). This justifies reuse of the residual estimate for generic independent lower coefficients, rather than assuming exact tuning survived rounding.

## 4. Gram and resolvent estimates

Compression by the isometry `J` cannot increase the operator norm. The exact noncommutative square identity is

\[
\widehat V^2-V^2
=\widehat V(\widehat V-V)+(\widehat V-V)V.
\]

Thus (3) and (4) give

\[
\|\widehat M-M\|
\le(\widehat v+v)\|\widehat V-V\|
\le8v h_g.
\tag{6}
\]

This calculation does not need to replace the square difference by a product of commuting factors. Also `M=(VJ)*VJ`, so `||M||<=v^2`.

Because `Dhat-D=(Deltahat-Delta)I`, the resolvent identity gives

\[
\widehat D^{-1}-D^{-1}
=\widehat D^{-1}(D-\widehat D)D^{-1}.
\]

The actual inverse bounds are `||D^-1||=1/delta` and `||Dhat^-1||=1/deltahat<=1/delta`. Therefore

\[
\|\widehat D^{-1}-D^{-1}\|
\le\frac{h_D}{\widehat\delta\delta}
\le h_D/\delta^2.
\tag{7}
\]

Subtracting (5) in the order

\[
\widehat H_2-H_2
=-(\widehat M-M)\widehat D^{-1}
  -M(\widehat D^{-1}-D^{-1})
\]

and applying (6), (7) yields

\[
\|\widehat H_2-H_2\|
\le8v h_g/\delta+v^2 h_D/\delta^2
<128h_g/\sqrt T+256h_D/T.
\tag{8}
\]

The last constants use only `v<4/sqrt(T)` and `1/delta<4`: `8*4*4=128` and `4^2*4^2=256`.

## 5. Effective phase and full-isometry comparison

For `t=T+s`, `0<=s<=w=epsilon T/256`, one has `t<2T`. Hermitian Duhamel applied to `Ghat` and `G=K+H2` gives

\[
\|e^{-it\widehat G}-e^{-itG}\|
\le t\|\widehat H_2-H_2\|
<256\sqrt T h_g+512h_D
=\epsilon/8.
\tag{9}
\]

Each summand is `epsilon/16`. No commutation between the two effective generators is required for this estimate, although in this family both are Bell diagonal.

The actual residual construction uses `vhat<=v` and `deltahat>=delta`, so its bound remains

\[
R(T)=12352/\sqrt T+132096/T<\epsilon/4.
\]

The ideal extra-window drift is still bounded by `16w/T=epsilon/16`. Combining the actual residual, (9), and the ideal drift proves

\[
\left\|e^{-it\widehat H}J-
J e^{-i\widehat r t}e^{-isK}W e^{-iTK}\right\|
<\left(\frac14+\frac18+\frac1{16}\right)\epsilon
=\frac7{16}\epsilon.
\tag{10}
\]

This retains literal old aging and the actual reserve scalar. Tensoring an arbitrary reference preserves the isometry norm, so the unhalved full joint trace error is below `7epsilon/8<epsilon`. Source and reference registers have not been discarded.

The actual reserve is especially important for this sharper tolerance. The allowed errors only give `|r-rhat|<=4h_g`, and `4T h_g=64`, which is not a small `O(epsilon)` phase allowance. Thus the bound does not also establish closeness to a comparator using the original `r`.

For an explicit counterexample to that stronger interpretation within the general real-coefficient interval hypothesis, take `gxhat=gx-pi/(2T)`, keep `gyhat=gy` and `Deltahat=Delta`. This is an allowed positive lower replacement because `(pi/(2T))/h_g=pi/32<1`. It changes the reserve by `r-rhat=pi/T`, so the two source-phase comparators at `t=T` differ by a factor `-1`. Equation (10) is still valid for the actual-reserve comparator, whereas the isometry distance to the fixed-original-reserve comparator is at least `2-7epsilon/16`. This is not a claim about a computed dyadic list; it shows why the actual-phase convention is indispensable for the general structured interval theorem. No necessity claim about precision follows from this example.

## 6. Mixed-grid compiler and the smaller term count

Set

\[
p_g=2m+29,\qquad p_D=m+14,\qquad P=\max(p_g,p_D)=p_g,
\qquad n=P+8=2m+37.
\]

Thus `n>=37`, rather than the previous construction's `n>=47`. This does not invalidate the enclosure proof. Its coarse rational guards use only `n>=2`: consecutive alternating partial sums give `L5>=74/375`, `U239<=1/239`, `pi_L>3`, and `0<theta_L<theta_U<1`. The width proof also remains valid: for `P>=29`,

\[
20\,2^{-(4n+2)}<2^{-(2P+12)}=:w_0,
\]

because the ratio is `20*2^(-2P-22)<1`. The variable `w_0` denotes enclosure width, not the observation window.

The same positive interval arithmetic gives Delta width below `w_0/2`, `gy^2` width below `w_0/T`, and `gx^2` width below `2w_0/T`. With the port grid step `d_g=2^-p_g`,

\[
2w_0/T\le d_g^2 2^{-43}<d_g^2/4.
\]

Hence the port square-root interval width is below `d_g/2`. Integer-square-root lower rounding at precision `p_g` costs strictly less than another `d_g`. The port coefficient errors are therefore below `3d_g/2<2d_g=h_g`.

For the source grid step `d_D=2^-p_D`, one has `w_0/2=2^(-(4m+71))<2^(-(m+14))=d_D`. The rational lower floor at precision `p_D` consequently has total Delta error below `d_D+w_0/2<2d_D=h_D`.

The mixed grids therefore meet the hypotheses of (10), with strict rather than merely weak coefficient errors. Equality at a grid boundary is harmless: the integer quotient and integer floor square root operate on rational lower endpoints, as proved in the previous finite-compiler review. No floor of an irrational coefficient must be decided.

The port scalar numerators and denominators use at most `p_g+1` bits; the source coefficient uses at most `p_D+1` bits. At `m=44`, the grid exponents are indeed `117` and `58`, so the corresponding uniform coefficient encoding bounds are `118` and `59` bits. These are separate output-coefficient bounds, not bounds on intermediate arithmetic or every expanded matrix-entry denominator.

The prior operation-count qualification still applies: there are `3n=6m+111` terms in the three partial sums, plus three first-omitted remainder terms. The final stage has three explicit integer floor quotients and two integer-square-root calls, with the two distinct grid exponents used in the appropriate quotients. This is not a total bit-operation count. No actual coarse coefficient integers have been computed or certified here.

## 7. What has and has not improved

The sufficient absolute allowances are `h_g=2^-28 epsilon^2` for each shared port coefficient and `h_D=2^-13 epsilon` for the source coefficient. The improvement comes from controlling the quadratic compressed Gram operator and the source resolvent, together with an unchanged small residual. It is not a general replacement of the full-Hamiltonian Duhamel bound by a sharper universal fault bound.

The theorem keeps the exact old `K`, the source projector onto the specified Bell complement, the port axes/supports and common paired coefficients, the lower-error signs, and the initial-source and timing interfaces. A generic residual self-adjoint fault outside this family still admits the usual `(T+w)||E||` isometry allowance. Unknown changes of sign, support, time dependence, arbitrary noise or source preparation are not automatically included in (8). The earlier independent-source/full-joint-state condition remains necessary for an additive initial trace error.

No finite compiled list has been run, no physical calibration has been demonstrated, and no native realization of the new Bell-projector/port permissions has been established. Energy/time units, preparation/installation, actual observation timing and halt/indefinite reuse remain separate obligations. As before, these tolerances are sufficient bounds, not necessary precision laws or an optimization result.

This review analytically supports the structured coefficient proposition and its mixed-grid route with the explicit norm, gap, actual-phase and scope qualifications above. It leaves root qualification and any separately recorded coefficient execution to subsequent action. Original sources, all prior review packets, canonical files, editable prompts, Git state, cache, graph, PRs and audit records were not modified.


<!-- Unchanged complete source: controlling_root_qualification -->

# Root qualification of the finite weak-mediator construction

This controls the historical proposal and exposed review bodies preserved with it. It accepts a conditional finite-dimensional construction and its explicitly bounded compiler, observation-window and finite-reuse consequences. It does not identify new interactions with the repository's microscopic axioms, establish retained audit status, or claim a physical experiment. Historical `proposed`, `unchecked`, and source-only status fields remain evidence of their original stage; current acceptance is separate.

## Supplied model and exact comparison

The old system consists of two qubits with literal `K=2I+Z1Z2` and fixed target `W=((9+12i)I+(-16+12i)X1X2)/25`. Two additional qubits A,B start in a Bell state independently of any unknown old/reference input. All four output qubits and arbitrary old references are retained. The new model supplies the positive source block `Delta(I-|Phi+><Phi+|)` and four positive ports `gx(I+X1XA)`, `gx(I+X2XB)`, `gy(I+Y1YA)`, `gy(I-Y2YB)`. Their scalar reserve is already `r=2(gx+gy)`; it is not an additional installed block. The graph is the square with the old pair and source pair as opposite edges.

Let `theta=atan(4/3)`, `delta=theta/pi`, `Delta=2-delta`, `q=theta/T`, `gx=sqrt(q Delta/2)`, and `gy=sqrt(q)`. For the specified parameter range, every added incident load is below2 and runtime coefficients are constant. The old vertices retain the separate norm-3 K block; an added cap is not a total cap. Physical time would be `hbar*T/E0` if physical energies are E0 times the displayed blocks. The theorem does not rescale K to meet a cap.

The complete isometry comparator at `t=T+s` is

`J exp(-irt) exp(-isK) W exp(-iTK)`, with `J psi=psi tensor Phi+`.

For installed rounded coefficients, replace the reserve in this comparator by the **actual** `rhat=2(gxhat+gyhat)`. Neither the scalar nor literal old aging is omitted. Source excitation under V includes Psi+ and Psi−; the proposal's use of “triplets” is a terminology error because Psi− is a singlet. The complementary source block penalizes all three orthogonal Bell states equally, so the formulas and support are unchanged by this correction.

## Why the small residual suffices

Root and the exposed analytic reviewer checked the displayed first and second Sylvester equations, their cross-spectrum gap, Hermiticity of the effective comparison and the residual identity. The source sector need not be the globally lowest band. The relevant gap is `delta`, and the Frobenius inverse bound uses the old input dimension4. Writing `F=J+S1+S2`, `G=K+H2`, one has exactly

`(H0+V)F-FG = V S2-S1 H2-S2 H2`.

Duhamel therefore bounds the two propagated embeddings by `2||F-J||+t||residual||`; F need not be an isometry. This avoids assuming a truncated perturbation expansion remains exact for the long runtime. The tuned second-order operator is `H2=s0 I+d ZZ-q XX`, with `s0=(2pi-theta)/T`, `d=2pi/T`. Its exponential at T is exactly the full-phase W. Both the analytic Bell calculation and the separately implemented finite polynomial fixture support these identities. The fixture does not by itself prove the analytic gap or norm estimates.

For `0<=t<=2T`, the residual construction yields `R(T)=12352/sqrt(T)+132096/T`. A fixed24 observation window adds384/T. The original supplied huge integer T consequently gives the stated finite small error. The scalable family instead sets `epsilon=2^-m`, integer `m>=0`, and `T=2^(2m+32)`; it is a separate explicit runtime, not the earlier externally controlled word's duration.

## Finite coefficients, longer windows and structured errors

The equality-safe compiler uses rational intervals from three alternating arctangent sums and integer quotients/square roots of rational lower endpoints. It never requires an oracle deciding whether an irrational coefficient equals a dyadic boundary. At uniform precision `p=3m+39`, `n=p+8`, each coefficient error is strictly below `2*2^-p`. This supports the uniform finite-precision bounds in the source. The earlier conditional floor construction with one fewer bit remains historical and is not falsely described as the implemented equality-safe algorithm.

For `w=epsilon*T/256`, literal old aging is still kept throughout `[T,T+w]`. The uniform rounded construction has full-isometry error below `15epsilon/32`, hence unhalved full joint trace error below `15epsilon/16`. This is not a fixed-output plateau: the independent review gives old states whose K evolution becomes orthogonal inside such a window.

The sharper structured theorem allows only lower replacements of the same three shared positive coefficients, keeping the source projector, paired port coefficients, signs, supports and old K exact. Port errors at most `h_g=epsilon/(4096 sqrt(T))` and source error at most `h_D=epsilon/8192` give full-isometry error below `7epsilon/16` and full joint trace error below `7epsilon/8` on the longer window. The effective-Hamiltonian bound is

`||H2hat-H2|| < 128 h_g/sqrt(T)+256 h_D/T`.

Two details of the exposed check are required. First, the four port Pauli operators commute, and their Bell eigenvectors attain `||V||=2(gx+gy)`, so lowering these coefficients really gives `||Vhat||<=||V||`. Such monotonicity is not assumed for an arbitrary operator sum. Second, `Delta>5/3` and `h_D<=2^-13` ensure `Deltahat>3/2`; consequently the actual minimum cross-spectrum gap is `2-Deltahat>=delta`. The effective formula `H2hat=-Mhat(Deltahat I-2ZZ)^-1` remains Hermitian without exact tuning. Its Gram/resolvent estimate and the actual residual justify the rounded model directly.

The mixed grids `p_g=2m+29`, `p_D=m+14`, `n=max(p_g,p_D)+8` implement these sufficient errors. The interval proof also works at m=0,n=37. Coefficient bit lengths are output-description bounds; they are not intermediate arithmetic or total bit complexity. Each scenario uses `3n` summed terms **plus three first-omitted remainders**, three final rounding quotients and two integer-square-root calls. Internal rational normalization, GCD and square-root operations are not included in those last small counts.

Using the original r in place of actual rhat would invalidate the full-isometry claim. The review preserves an allowed real coefficient change with `(r-rhat)T=pi`, giving opposite comparator phase at T. A general additional self-adjoint fault E outside the restricted coefficient family retains its separate `(T+w)||E||` isometry allowance. These are sufficient bounds, not necessary precision laws or an optimization theorem.

## What finite reuse establishes

For a prescribed finite number L of runtime intervals, a unitary hybrid argument accumulates at most L times the per-interval error, without resetting the actual source or assuming it stays product after earlier use. Optional interleaved unitaries act on the old system and retained reference and as identity on the source; their physical implementation, elapsed time, errors and controllers are supplied interfaces. With `m=m0+ceil(log2 L)`, the stated total error target is met with the explicit cubic-in-L runtime bound. The known finite-L construction is not indefinite reuse of a fixed device, permanent halt, or an autonomous intervention schedule.

An additive initial trace error requires an independently prepared product source or an explicit bound on the full initial old/reference/source state. A small source marginal alone does not provide that joint bound; the review's correlated counterexample is retained. The total static Hamiltonian's energy moments are conserved, and initial mean/variance include the port contribution and old-state covariance. Old K energy can change during runtime. Zero prescribed drive work during a static interval does not make Bell preparation, installation, timing or reset free.

## Actual checks and their limits

Root read all six proposal/addendum bodies and five separate analytic review bodies, including complete arguments and counterexamples. The reviewer had source exposure and contributed the lower-endpoint rounding strategy; the checks use the same selected model. They are separate analytic reconstructions, not blind or model-independent reviews. Four frozen analytic packets preserve the original chronology and actual metadata receipts. No review-count claim substitutes for the arguments.

The symbolic author fixture ran once for0.2838803748600185 seconds with exit0,60 finite checks and a60-second wall limit. It checked the finite Pauli/Gram/Sylvester/full residual identities and the displayed wrong-sign and bare-denominator mutants in an exact polynomial representation. The complete247777-byte report is preserved at SHA256 `4369fa1d5a970bf4e01ea00cc7db000779cab1d1f26be9bcbd26e1c4bc292a7d`. It did not evaluate long-time matrix exponentials or execute the later scalable/window/structured theorems.

The exact coefficient compiler then ran once for0.131953792180866 seconds with exit0 under its own60-second wall limit. Its two predeclared m=44 cases use T=2^120: uniform p171,n179,window24, and mixed pg117,pD58,n125,window2^68. The actual1,188,206-byte report at SHA256 `0b108a9605e02b8b907ea13b364875b6282fc727c368dbed862ecb5d67149564` contains both complete coefficient lists, rational intervals, integer certificates and conditional budgets. There were64 finite checks,912 summed terms,6 remainder terms,6 final quotients,4 integer-square-root calls and6111 guarded integer operations. Maximum observed guarded integer size was20857 bits. The coefficient compiler is an author implementation; its checks do not independently prove the mediator or physical premises.

Both executions retain their exact source and inputs at launch, interpreter identity, argv, cwd, full streams, wall time and original receipt schemas. No OS CPU/RAM quotas were imposed. Root inspected source, receipts, streams, selected exact certificate structure and result ledgers; large polynomial/rational report bodies are preserved by hash rather than described as manually checked entry by entry. There was no numerical evolution, physical test or Lean formalization. Any later independent saved-certificate check has a separate result and does not retroactively change these historical execution claims.

## Remaining physical identifications and publication boundary

The construction supplies a finite source/port Hamiltonian model with explicit resource and error accounting. It does not derive the Bell projector or XX/YY ports from the original four onsite rays or from the repository's bare microscopic premises. Bell preparation independent of unknown input, installing and calibrating the supplied interactions, external observation timing, generic noise, and final halt/reset remain unresolved physical interfaces. The downstream autonomous composition and other campaign PRs are not mathematical premises of this self-contained fixed-target theorem.

The publication may preserve these exact source bodies and qualifications as one coherent regular milestone PR with zero direct mathematical parents. Source packaging, canonical integration, actual staging, publication and retained audit each remain separate evidence. No science merge, main push, audit verdict, physical axiom, editable prompt or model setting changes are part of this acceptance.


The new wrapper and final root qualification control the historical status and scope. Source integrity is not proof, native supply, canonical binding or retained status.
