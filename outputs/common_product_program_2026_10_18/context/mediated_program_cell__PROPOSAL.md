# A conditional six-qubit mediated program cell

**Bounded author construction, pending distinct checking.** One fixed, real, positive Hamiltonian on a six-site cubic patch has a conserved three-bit program. On an explicitly supplied four-dimensional head code, program000 gives the full positive two-head exchange `Q_(b/2)`. Program111 gives the identity up to its actual common phase and a residual bounded by `2b^2 T/(Delta+2b)` over `|t|<=T`. Both code spaces have exact zero leakage. The encodings depend on the program and include the mediator; they are not the same literal endpoint product states.

This is a newly supplied conditional microscopic model. Its interaction terms, selected site roles, program Records, occupation frame, isolation and encoded preparation are assumptions of the construction, not consequences of the repository axioms. It does not establish native Hamiltonian supply, a permanent output Record, network assembly, a product-seed preparation or a performance theorem. No scientific computation was run.

## 1. Actual sites and one fixed positive Hamiltonian

Use three dynamic head qubits and three program qubits at these cubic-lattice positions:

| Qubit | Position | Supplied role |
|---|---|---|
| u | (-1,0,0) | left dynamic head site |
| m | (0,0,0) | mediator head site |
| v | (1,0,0) | right dynamic head site |
| c_u | (-1,1,0) | left compensation program bit |
| c_m | (0,1,0) | mediator-detuning program bit |
| c_v | (1,1,0) | right compensation program bit |

For each qubit put `n=|1><1|` and `a=|0><1|`. Let `b>0` and `Delta>0` be fixed supplied coefficients, and define

    Q_b(x,y)=b[n_x+n_y-a_x^*a_y-a_y^*a_x],

    H=Q_b(u,m)+Q_b(m,v)
        +Delta n_(c_m)n_m
        +b n_(c_u)(I-n_u)+b n_(c_v)(I-n_v).             (1)

The same H acts in every program sector; nothing is switched during evolution. All five displayed pairs are at lattice distance one. Other geometrically adjacent pairs, including the program-row edges, have no interaction in this specified finite model. Their absence and the role assignment are supplied, not inferred from a homogeneous law or from geometry alone. A translated copy has the same matrix, but that observation does not derive a covariant microscopic supplier for the roles.

All five terms are positive on their FULL two-qubit spaces. In the order `00,10,01,11`, the head block is

    Q_b=b [ 0  0   0  0 ]
          [ 0  1  -1  0 ]
          [ 0 -1   1  0 ]
          [ 0  0   0  2 ].                              (2)

Its eigenvalues are `0,0,2b,2b`. The detuning is `Delta|11><11|` on program/mediator, and each compensation is `b|10><10|` on program/head, with program listed first. Thus their norms are Delta and b. This is the full positive head-bond convention used in the existing supplied apparatus; it is NOT the exchange projector whose double-occupation energy would instead vanish.

In particular the endpoint compensation is not an uncharged negative onsite. Algebraically,

    b n_c(I-n_x)=b n_c-b n_c n_x.                      (3)

The first term in (3) contributes a real program-sector energy and will be retained. The specified object is the positive two-site projector, not a negative block silently added to (1). A safe total norm bound is `||H||<=6b+Delta`.

Every program occupation commutes exactly with H, as does

    N_head=n_u+n_m+n_v.

The intended settings are the three equal, already supplied values000 and111. The Hamiltonian also preserves each unequal program pattern, but no on/off interface is asserted for those patterns. No copy operation, Record formation, or mechanism preparing the three equal contents is provided.

## 2. Exact physical matrices, including all number sectors

For fixed program values `q=(q_u,q_m,q_v)` define

    C_q=b(q_u+q_v),
    d_u=b(1-q_u), d_m=2b+Delta q_m, d_v=b(1-q_v).

After retaining the scalar C_q, the one-head matrix in the order
`|100>,|010>,|001>` of u,m,v is

    h_q=[ d_u  -b    0 ]
        [ -b   d_m  -b ]
        [  0   -b   d_v ].                            (4)

The two-head matrix in the order `|110>,|101>,|011>` is

    h_q^(2)=[ d_u+d_m    -b        0    ]
            [   -b     d_u+d_v    -b   ]
            [    0        -b    d_m+d_v].             (5)

The vacuum block is0 and the three-head block is `d_u+d_m+d_v`. Thus the entire eight-dimensional dynamic-head matrix for each of the eight conserved programs is

    H_q=C_q I_8 + [0] directsum h_q
                        directsum h_q^(2)
                        directsum [d_u+d_m+d_v].     (6)

Equations (4)--(6) specify all64 physical columns of (1). They follow directly from hard-core qubit raising/lowering matrices: an adjacent hopping changes10 to01 with coefficient-b, never changes00 or11, and (2) retains its double-occupation diagonal. No fermionic sign convention or elimination of an occupied mediator is assumed. The encoded columns below can consequently be checked directly in (4) and (5).

Use the same abstract logical two-head space in both programs, with computational states `|00>,|10>,|01>,|11>`, occupations `n_L,n_R`, and

    X_h=a_L^*a_R+a_R^*a_L,
    R_-=(n_L+n_R-X_h)/2,
    R_+=(n_L+n_R+X_h)/2.                              (7)

Both R_- and R_+ are projectors on this FULL four-dimensional space. Each annihilates the vacuum, has eigenvalues0,1 on the one-head sector, and has eigenvalue1 on double occupation. In particular `b R_-=Q_(b/2)(L,R)` includes double-occupation energy b. No sector-dependent identity is being mistaken for a global scalar.

## 3. Enabled program000: all four encoded columns

Put

    |S>=(|100>+|001>)/sqrt(2),
    |A>=(|100>-|001>)/sqrt(2),
    |M>=|010>.

For program000, `C_0=0` and (4) has eigenpairs

    f_0=(|100>+|010>+|001>)/sqrt(3), energy0,
    A,                                           energy b,
    f_3=(|100>-2|010>+|001>)/sqrt(6), energy3b.      (8)

The lowest two-head eigenvector of (5) is

    g_0=(|110>+2|101>+|011>)/sqrt(6), energy b.      (9)

For example, the two-head matrix is

    b [ 3 -1  0 ]
      [-1  2 -1 ]
      [ 0 -1  3 ],

and its action on `(1,2,1)^T` is `b(1,2,1)^T`. This explicitly checks the double-occupation column; it is not inferred by treating hard-core qubits as independent classical particles.

Define an isometry J_0 from the full logical two-head space by

    J_0|00>=|000>,
    J_0|10>=(f_0+A)/sqrt(2),
    J_0|01>=(f_0-A)/sqrt(2),
    J_0|11>=g_0.                                     (10)

The columns are orthonormal. Equations (8)--(10) give every encoded Hamiltonian column:

    H_0 J_0|00>=0,
    H_0 J_0|10>=(b/2)J_0(|10>-|01>),
    H_0 J_0|01>=(b/2)J_0(|01>-|10>),
    H_0 J_0|11>=b J_0|11>.

Consequently

    H_0 J_0=J_0 bR_-,
    (I-J_0J_0^*)H_0 J_0=0.                           (11)

The enabled exchange coefficient b/2 is computed from the actual0,b,3b single-head spectrum and checked two-head column. It has not been inserted by defining H to be the logical target. No physical operation preparing or decoding J_0 is claimed. In particular its one-head states are distributed over all three physical head sites.

## 4. Disabled program111: exact dressed code and residual

Here `C_1=2b`, `d_u=d_v=0`, and let

    d=Delta+2b,
    epsilon=(sqrt(d^2+8b^2)-d)/2
           =4b^2/[sqrt(d^2+8b^2)+d].                 (12)

Then `epsilon>0`, `epsilon(d+epsilon)=2b^2`, and

    epsilon<2b^2/d.

The antisymmetric state A has relative energy0. In the S,M basis the relative one-head matrix is

    [ 0       -sqrt(2)b ]
    [-sqrt(2)b    d     ],

with eigenvalues `-epsilon,d+epsilon`. Set

    r=epsilon/[sqrt(2)b]=sqrt(2)b/(d+epsilon),
    alpha=1/sqrt(1+r^2), beta=r/sqrt(1+r^2),
    f_1=alpha S+beta M.

Then f_1 has relative energy `-epsilon`. The exact two-head vector

    g_1=alpha|101>+beta(|110>+|011>)/sqrt(2)           (13)

also has relative energy `-epsilon`. Indeed the two-head matrix after removing ONLY C_1 is

    [ d -b  0 ]
    [-b  0 -b ]
    [ 0 -b  d ],

and its three equations follow from
`sqrt(2)b beta=epsilon alpha` and
`(d+epsilon)beta=sqrt(2)b alpha`.

Define

    J_1|00>=|000>,
    J_1|10>=(f_1+A)/sqrt(2),
    J_1|01>=(f_1-A)/sqrt(2),
    J_1|11>=g_1.                                     (14)

These four columns are orthonormal and give

    H_1 J_1|00>=2b J_1|00>,
    H_1 J_1|10>=2b J_1|10>
                       -(epsilon/2)J_1(|10>+|01>),
    H_1 J_1|01>=2b J_1|01>
                       -(epsilon/2)J_1(|10>+|01>),
    H_1 J_1|11>=(2b-epsilon)J_1|11>.

Therefore the exact full-code relation is

    H_1 J_1=J_1(2b I_4-epsilon R_+),
    (I-J_1J_1^*)H_1 J_1=0.                           (15)

No negative physical block is specified in (1). The negative relative eigenvalue in (15) results from retaining and then displaying the actual positive-sector baseline2b separately. Positivity is already proved term by term in (1); for example `epsilon<2b^2/d<b` here, so the displayed code energies are positive. The excluded high one-head mode has energy `2b+d+epsilon`; its initial absence is part of the exact code premise, not a dissipative preparation mechanism.

The legal encodings have the same abstract occupation labels and exactly preserve total head number:

    N_head J_p=J_p(n_L+n_R), p=0,1.                  (16)

They do not identify logical n_L,n_R separately with physical n_u,n_v. Those encoded number operators depend on J_p. Thus (11),(15) prove a program-dependent encoded interface, not literal endpoint-head gating with a common physical product code.

## 5. Complete-output time bound, phases, program and references

Equations (11),(15) are exact invariant-subspace relations, so for every real t,

    exp(-itH_0)J_0=J_0 exp(-it bR_-),
    exp(-itH_1)J_1
       =exp(-i2bt) J_1 exp(+it epsilon R_+).          (17)

Because R_+ is a projector, the disabled error relative to its correctly phased identity is exactly

    ||exp(-itH_1)J_1-exp(-i2bt)J_1||
       =|exp(i epsilon t)-1|
       =2|sin(epsilon t/2)|
       <=min(2,epsilon|t|).                          (18)

For every `|t|<=T` this is bounded by

    delta_T=min(2,epsilon T)
           <=min(2,2b^2 T/(Delta+2b)).               (19)

Thus, for a requested vector-map tolerance `0<eta<2`, the sufficient choice

    Delta>max(0,2b^2 T/eta-2b)                       (20)

gives a disabled error below eta. This is a finite-horizon sufficient condition, not a necessity or a permanent-off theorem. For any finite Delta, epsilon is nonzero; arbitrarily long uniform closeness to identity does not follow. Special recurrence times do not change that finite-interval qualification.

The scalar in (17) is obligatory. On program111 with all dynamic heads vacant, the two compensation projectors contribute exactly b each, so the actual vacuum energy is2b. It cannot be discarded when comparing different programs, and it is not a head-number phase. The logical residual `-epsilon R_+` is likewise not a removable common phase: its action on vacuum and the occupied symmetric mode differs.

For an explicit joint statement, let the abstract program space have basis `|0>,|1>` and define the controlled isometry

    J(|p> tensor psi)=|ppp>_(c_u,c_m,c_v) tensor J_p psi.

The ideal code-space target is

    U_tar(t)=|0><0| tensor exp(-it bR_-)
              +exp(-i2bt)|1><1| tensor I_4.           (21)

Orthogonality of the conserved program sectors and (17)--(19) give

    ||exp(-itH)J-J U_tar(t)||<=delta_T, |t|<=T.       (22)

This compares all six physical output qubits. The mediator is neither traced out nor reset, and no output is postselected or renormalized. Every already supplied program bit remains unchanged exactly. Equation (22) extends unchanged after tensoring any passive reference. For any density operator on the encoded logical/program domain jointly with that reference, the unhalved output trace-norm error is at most `2 delta_T`.

Mathematically (22) also covers coherent superpositions of the two redundant program sectors, with their relative phase in (21) retained. It does not assert that a coherent superposition of permanent framework Records is lawful. If the program is supplied as classical fixed contents or a correlated classical mixture, the same block result applies without that additional interpretation. Preparing three equal classical contents, or a coherent encoded program, is not derived here and is not an implicit cloning procedure.

An additional environment may have a supplied, input-independent Hamiltonian H_env and arbitrary initial correlations with the logical/reference input, provided the total Hamiltonian is exactly `H tensor I+I tensor H_env`. Its full evolution `exp(-itH_env)` then tensors both sides of (22), so the same bound holds without discarding that environment. Interactions with the patch are NOT covered by this isolated-cell theorem. Nor is an approximate code preparation silently exact: a supplied full initial joint unhalved trace-norm error epsilon_init adds to `2 delta_T` by contractivity and the triangle inequality, rather than being inferred from correct marginals.

## 6. Why the compensating copies and conditional encoding matter

The detuned-mediator shortcut without endpoint compensation fails as an arbitrary-four-state identity interface. For

    H_bare=Q_b(u,m)+Q_b(m,v)+Delta n_(c_m)n_m,

the program1 one-head matrix has endpoint diagonal b. Subtracting bI only within that sector gives the same two-by-two reduction with `d_0=Delta+b`. Its two low energies are `b-epsilon_0,b`, where

    epsilon_0=(sqrt(d_0^2+8b^2)-d_0)/2.

The corresponding four-dimensional low-mode code has generator

    b(n_L+n_R)-epsilon_0 R_+.                        (23)

Its vacuum energy is0 and double-occupation energy is `2b-epsilon_0`. As Delta increases, the unwanted `b(n_L+n_R)` does not tend to a common scalar. For example the vacuum and antisymmetric one-head state have exact relative phase `exp(-ibt)` for every Delta. At `t=pi/b`, their equal superposition is carried to the orthogonal relative-sign superposition. Increasing detuning alone does not repair this full-domain failure. Equation (3)'s two positive compensation terms are what replace that head-number baseline by the explicitly retained program scalar2b in the proposed family.

The program dependence of J_p is another real premise. It cannot be hidden by using J_0 for both settings. For instance `f_0=J_0(|10>+|01>)/sqrt(2)` has a nonzero off-sector coupling to the excluded vector f_3 of (8):

    <f_3|H_1|f_0>=-sqrt(2)(Delta+b)/3.               (24)

The scalar2b contributes zero to this matrix element. Directly, after removing it, H_1 sends f_0 to
`[-b|100>+Delta|010>-b|001>]/sqrt(3)`, which proves (24). Thus the common J_0 subspace is not invariant in the disabled setting, and the large barrier does not itself justify using the enabled code unchanged. No assertion of a common product encoding is made by this proposal.

Conversely, J_1 approaches the literal endpoint/blank-mediator encoding as Delta tends to infinity: `r<sqrt(2)b/d` implies beta tends to zero, so f_1 tends to S and g_1 tends to `|101>`. This limit does NOT prepare either finite-Delta J_1 or the enabled J_0, and is not a product-seed transfer theorem. It only locates the explicit code in physical coordinates.

The retained full two-head convention also matters in the enabled branch. At `t=pi/b` its one-head block exchanges the two logical states, but its double-occupation column has phase-1. That phase is part of `exp(-it Q_(b/2))`; calling the action an ordinary full SWAP would be incorrect.

## 7. Resources, remaining physical obligations and decisive check

This one cell uses six qubits, five positive nearest-neighbor two-qubit blocks, two fixed real coefficients b,Delta and two legal three-bit program patterns. There are no time-dependent controls after the stipulated preparation. If a block-norm cap Lambda is additionally imposed, it requires `2b<=Lambda` and `Delta<=Lambda`; the compensation norms b then obey the same cap. The sums of incident block norms are3b at u,v, `4b+Delta` at m, b at c_u,c_v and Delta at c_m. Thus an incident-load cap Lambda would instead be satisfied by `4b+Delta<=Lambda`. Equation (20) cannot be met for arbitrarily small eta at fixed b,T and fixed Delta cap by silently increasing a forbidden coefficient. No optimized resource or runtime claim is made.

The construction supplies an actual algebraic alternative to the range/occupation mismatch of the native-square shortcut. It establishes the following conditional interface only: under the five-term Hamiltonian (1), an isolated correctly encoded patch with three matching conserved program values has exact enabled dynamics and the phased approximate disabled dynamics (22), including all logical head numbers and passive references.

The premises it retains are substantial:

- The candidate microscopic law, selected pair pattern, roles, coefficient values and occupation basis are externally supplied. The existing axioms and primitive registry have not been shown to generate them.
- The already formed program contents and their lawful interpretation as Records are supplied. Commuting with their Z values proves content preservation under this candidate H, not Record occurrence, preparation or native permanence under an unspecified larger law.
- The input is in J_p, including its program-dependent mediator correlations and excluded-mode vacancy. An encoder, decoder or lawful source delivering that family is not supplied. The same abstract logical occupations in (16) are not the same two physical endpoint occupations.
- Isolation or the explicit independent-environment condition is supplied. Attaching further hopping cells can disturb the code and needs a new leakage/compatibility calculation. This is not a network compiler or permission to replace every apparatus edge by this patch.
- No shared old/source contact, prescribed product seed, output measurement or permanent storage is provided. Nothing in this local result transfers a previous complete-device certificate.

The first distinct check should reconstruct (4)--(6), all four columns in (10),(14), the positive compensation scalar, and (18),(24), keeping the full double-occupation column. A dropped factor of two, a hidden head-number phase, a wrong two-head sign, or a nonzero code-leakage column would directly falsify the stated interface. No large simulation or parameter sweep is needed for that check. A later physical advance would need an actual preparation/encoding or an interoperable code-preserving neighbor coupling, not another assertion that an endpoint product seed already has this code.

## Exact sources and exposure

Root suggested the three-head detuned-mediator candidate and explicitly raised the full-head `b N` phase and possible compensating program copies. The precise six-site family, encoded columns and bounds above are new author work, not independent validation of that suggestion. They are self-contained finite matrices, with the supplied head-block convention pinned below. The earlier native-square proposal remains unchanged and is context, not a proof that the present model is native or lawful.

| Source | SHA256 |
|---|---|
| native_realization_next/ASSESSMENT.md | e46f6cdd8a3d1f8132b263ba6f52b006a40d931366d228d4ae68b7e83cf6b915 |
| native_exchange_cell/PROPOSAL.md | 48ed290a9071a508c7a1a82ea2d55508f7b846b53393ecccb58eb18e6f225923 |
| correlation_worktree/docs/THREE_SITE_PRODUCT_SOURCE_COMPLETE_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md | 9664da772e44fda23f62ba098d393f6b00676717e83fc75f2cce1caae126ae3c |
| correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md | 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff |
| correlation_worktree/docs/MINIMAL_AXIOMS_2026-06-29.md | 93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753 |
| correlation_worktree/docs/audit/data/axiom_premise_nodes.json | 615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37 |

The assessment and native-cell argument were read completely in this sequence. The temporal note's head definition and the original endpoint note's geometry/positive-block passages were refreshed; their unchanged full-theorem claims are not premises for the new finite-cell proof. The axiom memo and registry were read in the preceding assessment and reused only for the explicit supplied-law boundary. All six source hashes were verified from actual bytes.

Only this proposal was created. The displayed matrices, eigenvectors and bounds were derived analytically. No scientific program, numerical eigensolver, simulation, sweep, network assembly, Git/W/canonical change, PR, checkpoint, editable prompt, axiom amendment, model override or delegation occurred. The result is provisional author mathematics requiring a distinct load-bearing check, not formal retained status or a native-realization claim.
