# Source-accessible dark fast sectors and finite occupied islands

Research result on the supplied compensated original microscopic model. No formal review, audit grade, microscopic local-limit theorem, or native-axiom adoption is asserted. This report is provisional pending a focused independent check.

The actual leading fast generator has source-accessible backgrounds on which no background-uniform absorption estimate can hold. There are two different concrete results. A finite B-filled island around one A hole gives arbitrarily long exact dark Krylov prefixes and a quantitative survival bound uniform in volume and integer spin. On a finite torus with every B occupied and two A holes, the leading fast evolution is exactly lossless yet changes an actual bounded link-field observable. The second sector has the correct record-number parity to occur in the original source algebra. Neither result says that the full microscopic evolution is dark, or that its local limit from bare Omega fails.

## 1. Source, conventions, and prior scope

The scientific main revision is `30a9461ee19a49b99fa6628fe942f08e504e8903`; the campaign procedure selection is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Exact file identities are in SOURCE_IDENTITIES.json. Mathematical working bytes are matched to the scientific main source; local campaign HEAD is not identified with main.

Use even cubic tori, A the even sublattice, B the odd sublattice, three site charges q=0,+1,-1, n=q², W=sum_A(1-n_a), and the physical Gauss law div E+1_A-q=0. All links below are oriented A to B; this is an allowed explicit orientation convention. The spin shifts are U=S_+/sqrt(S(S+1)), and U†, with their actual zero boundary weights. The rotor shifts have unit amplitude. Tensor composition, the quantum dynamics and the instrument are supplied assumptions.

Write f_ab for the unsigned charge-preserving hop from occupied A site a to vacant B site b, with link shift -q_a. Then

    F_a = sum_(b~a) f_ab,   F = sum_a F_a,   T = -F-F†,
    [W,F] = F,   ||f_ab|| <= 1,   ||F_a|| <= 6.

The original birth j_ab,s fills vacant a,b by +s,-s and shifts E_ab by s. Marks are either resolved s=±1 or the single unnormalized coherent j_ab,+ + j_ab,- for each edge. Different edges remain distinct. Because the two final charge words are orthogonal, their loss is the same, though their recycling maps are different. We use this equality only for loss:

    G = sum_m j_m†j_m.

Let Q_a be the product of n_c over the eighteen other A sites at distance two from a. Define D_a,S as the actual diagonal part of F_a†F_a and D_a,infinity=n_a sum_(b~a)(1-n_b). The compensation and full W-preserving second-order coefficient are

    C_S = sum_a [F_a†F_a + D_a,infinity-D_a,S] Q_a,
    H2_S = C_S + [F,F†].                                      (1)

The sign follows by A1=F†-F, [A1,W]=-T, and H2=C+[A1,T]/2. The present proof uses (1), not the low-block expression C0-A†A outside its domain. The leading no-original-event amplitude at fast time u=t/epsilon² is

    Z_S(u) = exp[u(-i delta H2_S-kappa G_S/2)].                (2)

This is the leading grade-preserving fast problem, not the exact microscopic no-event propagator. The omitted higher-order Hamiltonian, dressed jump corrections, initial dressing and W-changing remainders still matter to the microscopic comparison.

Closest actual main prior arguments read: the fast-vacancy six-ring source has an uncompensated P-sector H2=-A†A, a normalizable unwrapped electric-flux path and rapid postbirth vacancy motion; the repeated-record source section5a has finite-star exact ker A3 dark P states. They establish relevant warnings about fast motion and waiting laws but do not establish (or refute) the compensated cubic assertions below. The compensation source was read fully and its gates retained. The new author's complete dark cubic control was read before our reconstruction; its disclosed coefficient2 word, loss0 and selected matrix element1 were not blind-test predictions. Our control separately constructs literal global C+[F,F†] and the local identity below without importing its model code. The author's later low-global-N_B<=9 theorem is a distinct provisional result; its proof is not imported here.

Focused refreshed searches included filled/dark islands and clusters, background absorption/observability, all-B occupation, and fast-vacancy/dark rows in actual main sources and relevant obligation/ledger paths. The finite-star and uncompensated-ring hits are the closest matched physics, with the scope differences above. Broad unrelated record-gas and lattice-model hits were not treated as evidence. Open PR inventory: 9398 at6515ffa8570f21a0b3a8790fdd8a2879347550b8 (analytic gravity), 9397 at72e8656de1a34d236db62f2443b23cd15c2d5f25 (finite-volume energy supplier), and draft9008 atc2f56b729f4aae3eb8acf115c2be4fa074269d46 (cubic covariance). None is imported as a fast-absorption theorem; no exhaustive literature novelty claim is made.

## 2. Exact cancellation on the complete one-hole carrier

Let P_h project onto the A-occupancy word with its sole hole at h, allowing every B charge word and all physical electric fields. Set

    Delta_S = sum_a (D_a,infinity-D_a,S) Q_a,
    Hbar_S = H2_S-Delta_S.

Delta_S is diagonal, commutes with G, and is zero for the rotor. Its norm can be extensive and is not discarded or bounded uniformly. In the one-hole sector, the exact diagonal hole-position blocks are

    P_h Hbar_S P_h =
      P_h [F_h F_h† - sum_(a:dist(a,h)=2) F_a†F_a] P_h.     (3)

For a≠h the only off-diagonal hole-position block is

    P_a Hbar_S P_h = P_a [F_a,F_h†] P_h.                    (4)

It vanishes unless a,h share a B neighbor. These are operator identities including spin-boundary zeros. To verify (3), F_a† cannot refill an occupied A site; C_a cancels -F_a†F_a whenever Q_a=1. For the eighteen a near h its gate is zero; for a=h, F_h†F_h is zero on the input. For (4), refilling a distinct hole must refill h. Terms on disjoint edges commute and cancel, so only common B neighbors survive. No electric or charge sector is projected away.

There are six axial distance-two A neighbors with one shared B each, and twelve face-diagonal A neighbors with two shared B each: thirty shared paths in total. Each single-edge hop has norm at most one. Thus (3) has norm at most19*36=684. In (4), each common-B commutator has norm at most2, and the row and column sums of block norms are at most60. Operator Schur/Cauchy-Schwarz on the orthogonal sum over hole positions gives

    ||Hbar_S||_(W=1) <= 744,       0 <= G_S <= 12 I.         (5)

These constants are uniform in volume, B occupation, fields and integer spin. They are deliberately loose. Rotor electric space may be infinite; the block bound still defines a bounded operator. In finite spin, the possibly large diagonal Delta_S is handled exactly in an interaction picture.

## 3. Finite occupied-island survival, with explicit constants

Fix m>=1 and R=2m+3. Take a normalized physical one-hole vector with hole h=0 and every B site in the cube [-R,R]^3 occupied. Arbitrary coherent charge/field vectors satisfying these occupation constraints are allowed. Choose the torus large enough that this cube and its three-neighborhood do not alias.

Whenever all B sites within distance three of the hole are occupied, the terms -F_a†F_a in (3) vanish: every such a has only occupied B neighbors. F_h F_h† can only refill h from a B and return to that same B, since no other neighbor is vacant. The off-diagonal positive path refills h from an occupied shared B and empties another occupied A into that newly vacated B. It moves the A hole at most two lattice steps and preserves every B occupancy. The negative path in (4) is blocked because its shared B is occupied. Link fields and charges can change and are retained.

Consequently any word of k<=m factors Hbar, each optionally conjugated by arbitrary diagonal field/charge unitaries, remains supported on the same B mask, with hole distance at most2k. Its states are annihilated by G. In particular,

    G^(1/2) H2_S^k psi = 0,        k=0,...,m,               (6)

since diagonal Delta insertions do not move any occupation. This is an exact zero, not a small-field or semiclassical assertion.

For a quantitative bound, use the diagonal interaction picture

    U(u)=exp(i delta Delta_S u) Z_S(u),
    U'(u)=A(u)U(u),
    A(u)=-i delta exp(i delta Delta_S u) Hbar_S
                    exp(-i delta Delta_S u)-kappa G/2.

It is contractive and ||A(u)||<=b, where

    b=744 delta+6 kappa.

Every ordered Dyson term through degree m is dark by the preceding support statement. Diagonal conjugation changes phases, never a matrix zero. The norm of the remaining series and ||G^(1/2)||<=sqrt(12) give

    ||G^(1/2) Z_S(u) psi||
      <= sqrt(12) exp(bu) (bu)^(m+1)/(m+1)!.

The exact loss identity for (2) now yields

    1-||Z_S(u)psi||²
      <= 12 kappa u exp(2bu) (bu)^(2m+2)/[(m+1)!]².        (7)

It holds for every u>=0; a bound larger than one is simply uninformative. For n=m+1, choose u_m=n/(8b). Using n!>=(n/e)^n,

    1-||Z_S(u_m)psi||²
      <= [3 kappa n/(2b)] [exp(9/4)/64]^n -> 0.            (8)

Thus a family of finite filled islands has survival approaching one over fast times growing linearly in island radius. In physical time these windows are epsilon² u_m. For any fixed u>0, (7) also makes the integrated original loss arbitrarily small by increasing m.

Equations (6)-(8) exclude a positive background-independent finite-order observability constant on the full one-hole carrier, and exclude bounds ||Z(u)psi||<=C exp(-lambda u) with fixed positive C,lambda for all of these backgrounds. A bound depending on island size is compatible. Finite-spin boundary zeros cannot repair these exclusions; they remove paths, and the entire proof was uniform in their actual weights.

## 4. These island words are in the original source algebra

The following explicit construction avoids introducing a populated island as an unrelated preparation. Let M=ceil((R+3)/4). On each line with -R<=y,z<=R, pair B sites along x at spacing two.

For a noncentral line put p=(1-y-z) mod2 and take the4M sites

    x=-4M+p, -4M+p+2, ..., 4M+p-2,

paired consecutively. On y=z=0 take the4M+1 odd sites from -4M+1 through4M+1, leave x=1 unpaired, and pair the2M sites to its left and2M sites to its right consecutively. Every pair has a distinct intervening A center c.

Starting at bare Omega, for each pair choose the contribution which hops the plus charge from c into its left B endpoint and then performs the original + birth at c and the right endpoint. This is a nonzero contribution of the actual B_(c,right,+)=j_(c,right,+)F_c mark, not a new measurement of the hop. The center is restored to plus. Targets are disjoint and centers are distinct; every selected link is used exactly once, from0 to+1 or-1. Finally hop from a=0 into the previously unpaired b=(1,0,0). The resulting physical basis word has

    W=1,   N_B=4M(2R+1)²+1,
    original marks=2M(2R+1)²,

and every B in [-R,R]^3 occupied. All its selected step amplitudes are exactly one for every integer S>=1 as well as for the rotor. Gauss law holds after each elementary operation. Total record parity is correct: N=N_A-1+N_B=N_A+2*(number of marks).

Every chosen local path has positive unsigned amplitude. For resolved + marks it is a nonzero component of the specified original mark word. In the coherent instrument the all-plus component is still present; different birth signs leave distinct charges at these distinct A centers, so cannot cancel it. There is no observation or postselection on these internal fields/signs in the original output claim.

At fixed finite S and volume, the same algebraic component occurs in the actual microscopic time-ordered marked expansion from bare Omega. Before each mark at least one hop is needed to empty its A center, and the selected contribution uses exactly one; the final one-hole component needs one more hop. These minimal Taylor terms have the same hopping sign and time phase, with nonnegative link weights. W, C and no-event loss preserve W and cannot replace a required hop. Therefore the coefficient is nonzero. This proves finite-source accessibility, not a probability bounded below uniformly in R, S, epsilon or physical time. Its probability can be extremely small. The use of a basis component is a test of operator geometry, not an altered observed process.

The same source construction displays nonzero field-changing fast paths. The unpaired b=(1,0,0) has E_(0,b)=-1 after the last hop. Refill a=0 from b and empty c=(2,0,0) into b. The first field returns to zero, the second changes from zero to-1, and the matrix element of H2 is one. Both links are strictly unit-weight steps for every S>=1. Dark occupation does not imply absent field motion.

## 5. A persistent leading fast sector with correct source parity

There is an exact invariant sector, separately from the finite-island estimate. Let the torus side L be divisible by4 and at least8. Then |A|=|B| is even. On

    K_2 = {W=2, every B occupied},

total record number is N=2|A|-2, which differs from initial N_A by the even number |A|-2. Thus the sector is not excluded by the original even record increments.

For every vector in this complete physical sector, F annihilates the input, all F_a†F_a and both D_a diagonals vanish, hence C_S=0, and every original j_m vanishes. Both C and [F,F†] preserve W and total N, so they preserve N_B=N-N_A+W. Saturated N_B=|B| therefore stays saturated. It follows, on the full sector rather than a selected finite matrix,

    H2_S|K_2 = F F†|K_2,     G_S|K_2=0,
    Z_S(u)|K_2 = exp(-i delta u F F†)|K_2.                 (9)

The result holds for finite spin including its boundary zeros, and for the rotor. It does not claim K_2 is invariant under the full microscopic hopping T, which changes W. Higher-order dressed losses can also act. Calling this a full microscopic dark sector would be incorrect.

For an explicit source word, pair all B sites along x as (p+4k,y,z),(p+4k+2,y,z), p=(1-y-z) mod2, with intervening A centers. Omit the pair (1,0,0),(3,0,0). Apply the selected original + mark contribution for every other pair, then hop from (2,0,0) into (1,0,0), and from (4,0,0) into (3,0,0). There are (|B|-2)/2 marks and two final hops. Every chosen link again goes0 to±1 exactly once. The minimal original marked Taylor coefficient is nonzero for the same reason as section4. Coherent marks retain this component with no inserted sign/field readout.

Let gamma be that physical basis word. Refill its hole h=(2,0,0) from b=(1,0,0), then empty d=(0,0,0) into b, obtaining beta. The matrix element <beta|H2|gamma>=1, with E_(h,b) changing from-1 to0. Other shared-path phases are actual electric translations; none was replaced by an effective scalar hopping model. For the bounded local observable

    P_e = 1_(E_(h,b)=0),

P_e gamma=0 and

    d²/dv² <gamma|exp(i v H2) P_e exp(-i v H2)|gamma>|_(v=0)
        =2||P_e H2 gamma||² >=2.                          (10)

Thus a full actual field output evolves on a lossless leading fast sector. The exact L8 control gives the value10 for both the rotor and spin one. Equation (10) uses a bounded spectral projector, so it needs no unproved electric moment estimate. Counting outputs alone would miss this fast field behavior.

The first omitted dressed jump already gives a concrete escape mechanism. For the same normal-form convention A1=F†-F,

    J_m = j_m + epsilon [A1,j_m] + O(epsilon²),
    [A1,j_m]psi = -j_m F†psi,        psi in K_2.             (11)

The equality uses j_m psi=F psi=0. It has grade-2: one hole is refilled from a B, then an original birth fills the other hole and that newly vacant B. It can occur only if the two A holes share a B neighbor. For gamma above they share b=(3,0,0). In the rotor there are four unit paths: two original edge marks, each with two charge signs. At finite S, three have unit weight and the fourth has squared weight1-2/[S(S+1)]. Consequently on this particular normal-form basis input,

    kappa sum_m ||[A1,j_m]gamma||²
        = kappa (4-2/[S(S+1)])                           (12)

for either actual instrument, with rotor value4kappa and spin-one value3kappa. Distinct edge marks are added as separate channels; the two signs of a coherent edge end in orthogonal charge words on this input. In physical units the epsilon in (11) cancels the epsilon^-1 jump scaling, so (12) is an order-one escape rate, not a fast order-epsilon^-2 rate. All its outputs have W=0 and every site occupied. The sparse control reconstructs these channels directly.

Equation (12) is an instantaneous dressed-coordinate statement at gamma. The rapid FF† dynamics can change its contact weight; no uniform physical-time decay rate is inferred. It explicitly prevents mistaking (9) for an all-orders persistent microscopic mode. It also identifies a real next many-hole obligation: contact observability for the actual grade-2 original marks along the fast, field-changing evolution, with source weights retained.

## 6. Exact controls and their coverage

check.py is independently implemented from site charges and oriented link shifts; it imports no other builder. In the author's actual one-hole/seven-B cubic word, direct global evaluation of C+[F,F†] agrees entry-by-entry with (3)-(4). Rotor output has161 basis words, spin one159; both have initial loss0 and the selected hole-transfer element1 to an original-loss8 word. All resulting words satisfy Gauss law and W=1. This checks the compensation cancellation and boundary effects, not just a projected hopping matrix.

On L8 the source construction uses127 original marks plus two hops, giving W=2, N_B=256 and |E|<=1. The actual FF† output has59 rotor words and54 spin-one words; every output remains in the full-B sector with original loss zero. The selected field matrix element is one and the bounded field-projector second derivative is10 in both carriers. Tests retain every FF† output of that input; they do not enumerate the exponentially large whole sector. Its invariance is the analytic proof in section5.

The support-only control enumerates possible hole positions through m=1,2,3,4,8 and checks the three-neighborhood inclusion, as well as the18 neighboring A sites and30 shared paths. It is labelled geometry, not a replacement for electric/charge dynamics. source_island_check.py separately replays actual selected hop/birth operations for R=5,7,19, with484,1350,18252 marks respectively. Every intermediate Gauss equation, unused-link/unit-weight condition, final one-hole count and required B-cube occupation is checked. This is source accessibility, not a large probability estimate.

Resource receipts: the final main control, including the first dressed-jump extension, used12.190326 CPU seconds,12.206996 wall seconds and34,750,464 bytes peak RSS. The earlier run used11.772269 CPU seconds,11.796128 wall seconds and34,832,384 bytes peak RSS; its exact script/results are preserved in historical/pre-first-dressed-jump-extension. The source-island control used0.617211 CPU seconds and57,819,136 bytes peak RSS. Both runners have hard CPU limits, actual deadline/STOP checks and memory assertions. The matrix control sets one BLAS/OpenMP thread; the source control uses only standard-library integer/set operations. No failed scientific run, relaxed assertion, dense global enumeration or unmanaged worker occurred. A mechanical patch-context mismatch before the extension changed no file and ran no control.

## 7. What remains for the original bare-Omega local limit

The accepted defect/activity lemma bounds a dressed-hole density by O(epsilon²), actual unconditional local activity, and an integrated dressed negative-grade loss. It deliberately does not assert G>=cW. Equations (7)-(10) show why extending that lemma by a background-uniform fast absorption gap is invalid. Even the one-hole lifetime is not bounded independently of its occupied surroundings; a leading fast two-hole sector may never lose a record at all.

This is not a counterexample to the source-averaged microscopic local limit. The constructed large backgrounds need O(R³) marks; bare Omega does not initialize them with fixed weight. The dense two-hole component appears only very late in a finite system and may have small dressed amplitude. Higher-order terms can escape the leading dark sector. A time scale growing in u need not survive at fixed physical t. No order of epsilon, S, R, volume or observation-resolution limits has been exchanged.

Three genuinely different live approaches remain:

| Family tuple | Concrete gain here | Terminal obligation and strength |
| --- | --- | --- |
| (one-hole block operator; exact compensation and occupation support; integrated no-event observability) | Equations (3)-(8), including spin-uniform constants | A background-dependent decay/current bound weighted by the actual evolving source. Strictly weaker than the full local-output theorem by itself; full closure additionally needs dressing/remainder and recorded-map control. |
| (original marked expansion; finite saturated islands and source parity; distribution of occupied neighborhoods) | Explicit nonzero source words of O(R³) marks | Uniform source-weighted tails or an equivalent occupation-coherence estimate, strong enough to offset residence and propagation. Not proved by the first moment of counts, not proved by a fixed-global-N_B result, and not supplied by imposing independent births. Relation to the full target is unknown/comparable; using the effective process to assume the needed microscopic tail would be circular. |
| (oscillatory quantum propagation; exact fast resolvent/current rather than loss domination; local Duhamel term) | The field witness demonstrates that lossless motion remains in the actual output algebra | Bound the fast contribution for the actual dressed microscopic source and target-evolved local observables, including mark-word maps. The complete such estimate with all residuals is target-equivalent; it is an unresolved reformulation, not near closure. |
| (multiple-hole full carrier; conserved W,N_B and leading dark subspaces; higher-order escape) | Exact (9) with correct source parity | Quantify source weight and D4/dressed-jump escape on the full dark sector, with local field effects. Weaker than full closure alone; no uniform global-sector inverse exists at orderH2,G. |

For specificity, one stronger sufficient current condition in a one-hole reduction would control absolute integrals of epsilon^-2 times the unwanted commutator i[Hbar,O_X] against the actual source, uniformly in volume/spin and uniformly over the quasi-local observables and instrument-weighted maps entering the comparison. The O(epsilon²) hole-density bound only gives O(1) before this integration. A signed oscillatory estimate could suffice even when the stronger absolute estimate fails. Neither estimate has been established here. A bound for a single no-event initial vector cannot be substituted for coherent injection, recurrent births, changing backgrounds and off-block terms in the full process.

Small density alone also does not exclude rare extended islands. Conversely, the existence of such islands does not show they carry enough source weight to matter. A possible positive route on a sufficiently short common physical interval is an actual microscopic cluster-tail estimate plus a compatible background-dependent propagation bound. Its proof must preserve the original coherent marks and supply its higher moments/locality rather than infer them from a global mean count. No new dilution, independent-event, random-background, energy cutoff or preparation assumption is silently added.

## 8. Scope discipline

N1: the refuted proposition is a background-independent leading fast absorption/finite-order observability bound on the stated full carriers. Pointwise loss domination, finite-order observability, uniform exponential absorption, source-weighted cluster control, oscillatory cancellation and higher-order escape are distinct approaches; the last three remain open. No general phase, microscopic-limit or original-instrument no-go is claimed.

N2: the failed pointwise bound, dark Krylov prefix and failed uniform exponential bound are related consequences of occupation geometry, not three independent walls. The dense-sector invariant and source-weight question are explicitly separate.

N3: supplied premises are the exact quantum carrier/law, compensation, torus, marks and bare source. Rotor unit weights are never imposed on finite spin. P, W and N_B definitions are not replaced by bosons or by a random walk.

N4: the old star/ring statements are prior context at their original hypotheses, not matching-scope proof imports. The low-N_B<=9 proposal is neither contradicted nor extrapolated.

N5: individual matrix elements and a bounded single-link output are checked; the one-hole block identities and filled-sector invariance are analytic at all volume; finite supports are corroborated; no ensemble/timestamp/thermodynamic convergence conclusion is tested by a finite runner.

N6: no primitive-adoption wall is introduced. Existing minimal/scale/kinetic/realized primitive boundaries remain as read; the enlarged model and dynamics are supplied. Naming the gap differently does not establish a source-weight estimate, but a valid estimate could close this part without new axioms.

N7: the strongest counterargument to a broad negative reading is that source-generated large islands may be so suppressed on a small common physical interval, and higher-order losses so effective on their actual weights, that all dangerous fast field terms vanish locally. This is mathematically live and would not conflict with any theorem here. It is why this report does not claim failure of the original local limit.

N8: finite-star dark outputs and uncompensated rapid winding were already known; compensation removes the unwanted low-P motion but does not remove the high-W geometric mechanism in (1). Their resolution would require actual source-sensitive propagation or oscillation control. No formal no-go packet status or audit outcome is manufactured.
