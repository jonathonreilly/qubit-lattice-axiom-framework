# One literal endpoint product code for a supplied six-qubit program cell

New bounded author derivation requiring a distinct check. ROOT suggested the unconditional compensations, programmed endpoint potential and tuning a0=2b²/D0 as a possible common-product route. They were hypotheses, not independently checked conclusions. The finite matrices below support that route for an isolated supplied cell, including double occupation. The common literal code is approximate, not invariant: all mediator output is paid in a full physical norm.

Fix b>0 and D1>D0>2b. Set a0=2b²/D0 and a1=0. One fixed real positive Hamiltonian on six qubits, with conserved program patterns000 and111, obeys for every |t|<=T

 ||exp(-itH)J-J U_tar(t)||<=max{min(2,2beta0),
                                   min(2,2beta1+epsilon1 T)}, (1)

where J is the SAME literal endpoint/vacant-mediator injection in both settings, beta0<sqrt(2)b/D0, beta1<sqrt(2)b/D1, epsilon1<2b²/D1, and

 U_tar(t)=exp(-i2bt)[|0><0| tensor exp(-it Q_(a0/2))
                              +|1><1| tensor I4].          (2)

All six output qubits and arbitrary passive references are retained. The positive compensation scalar2b is common to both settings and must remain in a fixed-phase vector comparison. No encoder for a program-dependent dressed head state is required by J. Program preparation, supplied interactions/coefficients, occupation basis and isolation still are premises. No native law, network compatibility or existing apparatus performance is established.

## 1. Actual local positive realization

Use the earlier cell's cubic positions: u=(-1,0,0),m=(0,0,0),v=(1,0,0); c_u=(-1,1,0),c_m=(0,1,0),c_v=(1,1,0). Let n=|1><1|, P0=I-n and P1=n on program bits. On head qubits define the FULL positive block

 Q_b(x,y)=b[n_x+n_y-a_x* a_y-a_y* a_x],
 a=|0><1|.

Its00,10,01,11 matrix has one-head [[b,-b],[-b,b]], vacuum0 and double-occupation2b; spectrum0,0,2b,2b. This is not a projector with a zero double-occupation diagonal.

Supply the fixed Hamiltonian

 H=Q_b(u,m)+Q_b(m,v)
     +b(I-n_u)+b(I-n_v)
     +[(D0-2b)P0_(c_m)+(D1-2b)P1_(c_m)] n_m
     +a0 P0_(c_u)n_u+a0 P0_(c_v)n_v.                (3)

Every displayed term is positive on its entire support. The mediator coefficients are positive because D0>2b; the endpoint terms are positive program/head projectors, and the two unconditional compensations are positive one-site projectors. All two-site supports are nearest neighbors on the displayed cubic patch. No u-v interaction is directly installed. Geometrically adjacent program-row pairs have no installed interaction; their absence and the site roles are supplied, not consequences of geometry.

Each program occupation and total head number commute with H. No control changes in time. The legal settings are three supplied equal values000 and111; mixed patterns have definite positive dynamics from(3), but are not asserted to implement the interface. For any pattern q, let a_u=a0(1-q_u),a_v=a0(1-q_v),D=D_(q_m). Exact expansion of the unconditional compensations gives

 H_q=2b I8+a_u n_u+D n_m+a_v n_v
                 -b(X_h,um+X_h,mv),                  (4)

where X_h,xy=a_x* a_y+a_y* a_x. Thus the vacuum has energy2b even in the enabled setting. This is a true scalar on the entire head Hilbert space and every program sector; no head-number-dependent phase is discarded.

For legal q=ppp, a=a_p, the relative one-head matrix is

 h1=[[a,-b,0],[-b,D,-b],[0,-b,a]]

in |100>,|010>,|001>. The relative two-head matrix in |110>,|101>,|011> is

 h2=[[a+D,-b,0],[-b,2a,-b],[0,-b,a+D]].             (5)

The relative vacuum is0 and three-head energy2a+D. These follow by hard-core occupation counting: a hopping acts only on10/01 and every occupied diagonal is paid. Together with(4), they specify all64 physical columns, including unequal programs. No free-particle assumption about occupied mediator sites is needed.

## 2. Exact low modes and the double-occupation check

Put S=(|100>+|001>)/sqrt(2), A=(|100>-|001>)/sqrt(2), M=|010>, E=|101>, and B=(|110>+|011>)/sqrt(2). The one-head A has relative energy a; on(S,M) the matrix is [[a,-sqrt(2)b],[-sqrt(2)b,D]]. On(E,B) the two-head matrix is [[2a,-sqrt(2)b],[-sqrt(2)b,a+D]]. The remaining antisymmetric two-head mode has energy a+D.

Enabled p=0: a=a0=2b²/D0. Define

 r0=sqrt(2)b/D0, alpha0=(1+r0²)^(-1/2), beta0=r0 alpha0.

Then f0=alpha0 S+beta0 M has relative energy0. The orthogonal symmetric high mode has energy D0+a0. Direct substitution in the TWO-head matrix gives g0=alpha0 E+beta0 B with relative energy a0, and its symmetric high mode has energy D0+2a0. Indeed a0 alpha0=sqrt(2)b beta0 and D0 beta0=sqrt(2)b alpha0. The same mixing angle is exact in both number sectors; this is the load-bearing tuning.

Define the auxiliary dressed isometry J0^d by vacuum|000>, logical symmetric one-head mapped to f0, antisymmetric mapped to A, and logical double occupation mapped to g0. Its exact intertwiner, after the scalar2b, is

 (H_0-2b I)J0^d=J0^d a0 R_-,
 R_-=(n_L+n_R-X_h,LR)/2,
 a0 R_-=Q_(a0/2).                                  (6)

R_- is a projector on the FULL logical four-state space: vacuum0, symmetric one-head0, antisymmetric one-head1, double occupation1. Thus(6) includes the positive Q double-occupation energy a0. It is not a statement only in the one-head sector.

Disabled p=1: a=0,D=D1. Set

 epsilon1=(sqrt(D1²+8b²)-D1)/2
          =4b²/[sqrt(D1²+8b²)+D1],
 r1=epsilon1/(sqrt(2)b)=sqrt(2)b/(D1+epsilon1),
 alpha1=(1+r1²)^(-1/2), beta1=r1 alpha1.

Both f1=alpha1 S+beta1 M and g1=alpha1 E+beta1 B have relative energy -epsilon1, while A has energy0. The high symmetric modes have energy D1+epsilon1. The exact dressed isometry J1^d therefore satisfies

 (H_1-2b I)J1^d=-J1^d epsilon1 R_+,
 R_+=(n_L+n_R+X_h,LR)/2.                            (7)

R_+ is also a full four-state projector, with double-occupation eigenvalue1. Epsilon1(D1+epsilon1)=2b², so epsilon1<2b²/D1. The negative relative energy is consistent with the positive physical Hamiltonian because scalar2b remains; in particular epsilon1<b for D1>2b.

## 3. The common literal code and full physical error

The actual preparation is the program-independent product injection

 J_lit|00>=|000>, J_lit|10>=|100>,
 J_lit|01>=|001>, J_lit|11>=|101>.                 (8)

Equivalently it tensors the arbitrary two-endpoint state with a vacant mediator. It permits coherent superpositions of all four endpoint occupations and arbitrary reference entanglement. The auxiliary dressed maps are proof devices, not prepared states. Their differences from J_lit have exact operator norm

 ||Jp^d-J_lit||=sqrt(2-2alpha_p)<=r_p.             (9)

The vacuum and A columns agree, and the symmetric one-head and double-head differences occupy orthogonal head-number sectors with the same norm. Triangle through the invariant dressed code already proves a uniform enabled discrepancy<=2r0 and a disabled discrepancy<=2r1+epsilon1|t|. There is no sum over the four columns.

A direct two-mode calculation slightly sharpens the leakage factor and verifies the complete physical target. Write the orthogonal high mode as h_p=-beta_p S+alpha_p M, so S=alpha_p f_p-beta_p h_p; use the identical formula for E,B. In the enabled branch the low-to-high gap is D0+a0 in BOTH sectors. Vacuum and A evolve exactly according to a0R_-. Therefore

 ||exp(-itH_0)J_lit-exp(-i2bt)J_lit exp(-it a0R_-)||
       =2beta0 |sin[(D0+a0)t/2]| <=2beta0.         (10)

In the double-head sector the comparison includes exp(-ia0t) on E; the gap to D0+2a0 is again D0+a0, proving the same formula rather than ignoring its relative phase.

For the disabled branch first compare against its residual logical generator -epsilon1R_+. The analogous exact full-map error is

 ||exp(-itH_1)J_lit
          -exp(-i2bt)J_lit exp(+it epsilon1R_+)||
       =2beta1 |sin[(D1+2epsilon1)t/2]|.           (11)

Since R_+ is a projector, its difference from identity has norm2|sin(epsilon1 t/2)|. Hence the disabled identity error is bounded by

 min{2,2beta1+2|sin(epsilon1t/2)|}
                  <=min{2,2beta1+epsilon1|t|}.     (12)

The trivial2 cap uses that both physical maps are isometries. No mediator output is traced away. The literal subspace is not invariant: for b>0 the hopping produces a mediator component from S immediately. Equations(10)--(12) pay that component at every time; they assert approximate output vacancy, not an exact dark-state preparation.

For an abstract program qubit define J(|p>tensor psi)=|ppp>tensor J_lit psi. Orthogonal conserved program sectors yield(1) with ideal(2) by a maximum, not by summing program errors. The phase2b is now COMMON, unlike the earlier cell's different vacuum energies between settings. Arbitrary passive references preserve the norm. The corresponding unhalved output trace or channel diamond bound is at most twice(1). No output postselection or renormalization is used. Mathematical coherent program superpositions are covered; whether such states are lawful framework Records is an additional physical question. Three equal classical contents are also a supplied preparation, not produced by this Hamiltonian.

## 4. Finite horizon and resource tradeoffs

A transparent sufficient error condition for0<eta<2 is

 D0>=2sqrt(2)b/eta,
 D1>max{D0,(2sqrt(2)b+2b²T)/eta},                 (13)

together with D0>2b and exact a0=2b²/D0. These conditions imply(1)<=eta with the strict margins as stated. They are sufficient, not necessary or optimized, and no parameter point is selected here. Enabled error is uniform for all real times; disabled identity has a finite-horizon guarantee only. The residual generator is not a common scalar on the logical space, so this proof does not turn finite D1 into an exact permanent-off operation.

The enabled positive exchange strength is k_eff=a0/2=b²/D0. Improving product-code accuracy by raising D0 at fixed b also weakens the intended interaction. For a fixed desired k_eff, b²=k_eff D0 and beta0 scales as sqrt(2k_eff/D0); growing D0 then increases b. Neither tradeoff is a free speed or precision gain. At t=pi/a0 the ideal one-head action exchanges endpoints, but the double-occupation column has phase -1, so the full operation is not ordinary SWAP.

The cell uses six qubits: three dynamic heads and three supplied program bits. There are seven listed positive blocks if the two mediator projectors are combined as the one positive two-site block in(3): two Q blocks, two one-site compensation projectors, one mediator/program block and two endpoint/program blocks. Resolving the mediator block into its P0 and P1 terms gives eight positive blocks on the same supports. Norms are2b,2b,b,b,D1-2b,a0,a0. Thus a safe total norm bound is D1+4b+2a0. Incident norm sums are3b+a0 at u,v; D1+2b at m; a0 at c_u,c_v; and D1-2b at c_m. Since a0<b and D1>2b, the mediator load dominates. An incident cap Lambda therefore requires D1+2b<=Lambda; an individual-block cap instead requires max(2b,D1-2b,a0)<=Lambda. If counted as two separate mediator projector blocks, the listed incident-norm sum is correspondingly larger; the combined-block convention is explicit.

This model supplies b,D0,D1 and the exactly correlated a0. Program couplings for the two endpoint controls must use that same a0. Preparation saves a program-dependent dressed-head encoding relative to the earlier proposal, but still requires mediator vacancy, correctly supplied endpoint input and three correlated program contents. No procedure creates these states or decodes the endpoints. All six outputs are compared, including the unchanged physical program contents.

### One sufficient bounded-strength exchange-time scaling

ROOT additionally suggested examining the ratio D0/D1 at an enabled exchange time; this is a proposed route, not independent evidence. At T_gate=pi/a0=pi D0/(2b²), the disabled residual allowance is less than pi D0/D1. This explicitly exposes a second detuning ratio beyond the product-code mixing b/D0.

For any supplied incident-load cap Lambda>0 and desired 0<eta<=1, one analytical sufficient family under the combined-block convention above is

    R=8pi/eta, D1=Lambda/2, D0=D1/R,
    b=D0 eta/(8sqrt(2)), a0=D0 eta²/64.

Then D1>D0>2b and the largest incident load D1+2b is strictly below Lambda. The enabled complete error is at most2sqrt(2)b/D0=eta/4. At T_gate, disabled error is bounded by eta/(4R)+pi/R=eta/(4R)+eta/8<eta/2. Thus the same common product interface has error below eta throughout |t|<=T_gate, where

    T_gate=64pi/(D0 eta²)=1024pi²/(Lambda eta³).

This is one explicit sufficient scaling, not a numerical operating point, a sweep, an optimal tradeoff or a lower bound. It requires the exact supplied hierarchy and correlation a0=2b²/D0; reducing the certified error increases the sufficient time. The ideal operation is still the full positive-Q exchange with the double-occupation phase, not ordinary SWAP. No native mechanism producing this coefficient family or preserving it in a network follows.

## 5. Boundaries of the positive result

This is a new isolated candidate microscopic Hamiltonian, not a consequence of a native lattice law. It assumes exact local projectors, occupation frame, selectively absent interactions, role labels, coefficient relations and isolation. Conserved program values establish content preservation under this H, not Record formation or stability under unspecified couplings.

The common literal input removes one particular preparation obstruction in the previous dressed-code interface. It does not make the literal subspace invariant, eliminate mediator leakage, provide exact disabled identity, or demonstrate superiority under a shared norm/time/error metric. The two-head calculation succeeds only because the proposed tuning matches its low energy to a0; a one-head Schur calculation alone would not establish the full result.

Coupling the endpoints to other cells can populate excluded modes or change the eigenvectors and gaps. The isolated spectral bounds are not a network replacement theorem. Multiple shared mediators, additional onsite terms, old internal operators that do not commute with the cell, or a prescribed processor seed require new compatibility and full-output proofs. A strictly independent environment with total Hamiltonian H tensor I+I tensor H_env can be included by tensoring its exact evolution on both sides; interacting environments are not covered. Full initial joint trace error can be added by contractivity, but correct marginals alone are not a preparation certificate.

No all-late capture/reset, permanent finite output, actual apparatus runtime, native supplier or universal negative conclusion is asserted. Existing campaign certificates are neither improved nor modified by this local result.

## 6. Source exposure and check obligation

Read the full earlier mediated_program_cell/PROPOSAL.md, SHA0e665329d8034e1bf2dfbbd4cfd918fc7f95451060906562d56fe04e5ff5928d, and its recorded check. That check supports the earlier DIFFERENT encoded construction and reports its own exact symbolic verification; I did not run or reuse its program as a check of the present matrices. Only its full positive Q convention, six-site coordinates and supplied-law boundaries are used as context. The present tuning, literal-code estimate and resource counts were derived analytically here. The optional native-exchange context is not a premise for this theorem.

ROOT supplied the proposed algebraic route, including the intended low one-head energies. I independently reconstructed all number-sector matrices, the low/high two-head energies, physical scalar, common injection and error bounds. This is still author derivation with explicit design exposure, not an independent check. A distinct reviewer should verify(3)--(12), especially double occupation, common scalar on vacuum, positive block supports, and the two-sector exact product-code error. It should also check the norm/load convention and that no network claim is inferred.

Only this proposal was written. No numerical program, symbolic solver, eigensolver, dynamics, parameter sweep, delegation, canonical/W/Git/PR/checkpoint/prompt/model change occurred. No retained status or publication is assigned.
