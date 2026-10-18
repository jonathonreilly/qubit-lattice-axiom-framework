# Check of normalized source L1 and conditional record-branch transfer

Disposition: SUPPORT the scalar inequalities and the conditional branch interface at their stated scopes. No required correction found. Equation (4) applies only after the separately assumed complete finite comparison on [t0,t_plus]. It is not itself a finite loader theorem or an early-time flag theorem. The output-ray restriction uses the external n>=1 coordinates; origins belong to the complete internal map and are charged there.

## Source and exposure

Read the complete source and verified its SHA-256:

    common_product_direct_loader_uniform_branch/PROPOSAL.md
    51872d1fa2af85f915d792b47e333c6539339ed75194ebaa666e691bf1941403.

N is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. The checked stationary source common_product_direct_two_body_loader/PROPOSAL.md, SHA89489c13a6450f142c8ac2212ee680bc7272addcff30c53fcb01e52dff4ee7a9, and my immediately preceding complete review common_product_direct_two_body_loader_check/REVIEW.md, SHA9818c72551eec2d2be17224dde6e07335f1ff7157b94a91c4a372aff3873343d, are reused only for the full-fiber scattering map, scalar and forward ideal word. Neither proves the assumed finite comparison here.

The exact source formula and its normalization were previously fully read in common_product_endpoint_launch/PROPOSAL.md, SHAfb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4, with check51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1. The cutoff ancestry is source550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3/check6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4. Those unchanged hashes were refreshed in the preceding coherent task. The new scalar calculation below needs only the formula displayed in the present source, its support, and p>=1/2; it does not import a derivative estimate or source-decay theorem.

ROOT authored the candidate after proposing the architecture. I read that candidate and have author ancestry in the scalar launch, cat-preparer and finite-interface work; this is a distinct source-exposed same-model check, not independent lineage, blind replication or a retained audit. No favorable outcome was used as a premise. No scientific solver or executable was run. Text reads and deterministic hashing were the only execution.

## Independent integration and normalization check

Put q=k-pi/2 and c0=sqrt(2/pi). The exact modulus is

    |F(k)|=c0 rho sin(k)
       /sqrt((2-rho^2)^2 cos^2(k)+rho^4 sin^2(k)).

On |q|<=3h/4<=0.00075, sin(k)=cos(q)>=1/2, |cos(k)|=|sin(q)|>=2|q|/pi, and 2-rho^2>=1. The numerator is at most c0 rho. Multiplication by chi<=1 and division by sqrt(p)>=1/sqrt(2) therefore give

    |g(k)|<=2rho/sqrt(pi) /sqrt((2q/pi)^2+(rho^2/2)^2).

This retains the normalization loss; replacing g by F without that factor would not prove the claimed normalized result. The integrand outside the given support is zero.

For A=2/pi, B=rho^2/2 and H=3h/4, direct integration uses

    integral_(-H)^H dq/sqrt(A^2 q^2+B^2)
          =(2/A)asinh(AH/B)=pi asinh(3h/(pi rho^2)).

Thus ||g||_1<=2sqrt(pi)rho asinh(3h/(pi rho^2)). For x>=0, sqrt(1+x^2)<=1+x, so asinh(x)<=log(1+2x). Since 2sqrt(pi)<4 and 6/pi<2, monotonicity of the nonnegative logarithm proves

    ||g||_1<=4rho log(1+2h/rho^2).

Every comparison is in the safe direction; no replacement of a finite-band integral by an unnormalized whole-line resonance is involved. The rho^2<=h hypothesis is allowed but is not needed to improve any of these integration inequalities. The assumed p>=1/2 is essential; it is not proved for arbitrary chi by this lemma and remains an explicit premise.

For the illustrative policy, rho=10^-7 epsilon^(3/2) and 2h/rho^2=2*10^8/epsilon^2. Hence L/epsilon=4*10^-7 x log(1+A/x^4), x=sqrt(epsilon), A=2*10^8. Differentiation gives

    d/dx [x log(1+A/x^4)]
      =log(1+A/x^4)-4A/(x^4+A)
      >log(1+A)-4>0,

for 0<x<=1. Its value is at most log(1+A)<20, giving L<=8*10^-6 epsilon. These numerical comparisons have large analytical margins: 1+A>e^4 and 1+A<e^20. The domain rho^2/h=epsilon^2/10^8<=1 and rho<=1 is satisfied. This does not establish p>=1/2 for an unspecified cutoff; that premise is still assumed, or must be provided by the checked concrete cutoff in an application. Nor does it select the final finite-loader policy.

## Complete projection argument

The assumed infinite packet is normalized on its COMPLETE one-head head-position space with the whole Q,P,R/reference fiber. Its incoming term has R=0 because I_in imposes that input condition and the freely degenerate incoming field has no record evolution. Consequently P1 annihilates that term for every time, including negative times. This statement would not be true for an arbitrary unknown initial R or an unaccounted record free Hamiltonian.

The forward ideal stationary word is X_R C_P SWAP with no reflected block. On the selected left incoming rays and R=0 input it lies entirely on right outgoing rays with R=1. Let O denote its full-integer outgoing Fourier field. Normalized g and the unitary ideal word give ||O||=1 for each normalized allowed input, by Parseval. Restricting O to the physical external output sites n>=1 gives the source's V after the common phase. Thus ||V||<=1, with no division by its potentially small norm.

The difference of exact and ideal outgoing external integrals has norm at most d_s on the full integer line by Parseval, since ||S-S0||<=d_s pointwise. Projection to physical n>=1 sites and then to R=1 are contractions. All ports, target outputs and passive references are retained in this vector estimate; a factor for their dimension is unnecessary. The ideal outgoing field is zero on the other exterior ports.

The complete internal field, INCLUDING port origins n=0 and any internal head that might carry R=1, is bounded uniformly in time by

    (2pi)^(-1/2) integral ||T(k)|| |g(k)| dk
       <=T0 ||g||_1/sqrt(2pi).

No outgoing-ray estimate is substituted for that internal population. This also clarifies the output convention: V is restricted to the physical EXTERNAL output sites used by the packet decomposition. If an application adds an origin amplitude to its ideal output target, that is a changed target and its added norm must be charged separately; the present formula does not silently include an n=0 plane wave in place of T.

Apply Pi_fin and P1 to the assumed full-vector estimate (3). They commute because the former selects head positions while retaining the data registers, and the latter selects only R. Their norms are one. The finite embedding J is an isometry adjoining vacant head sites and retaining all physical data/reference systems. Combining its contracted comparison error with the external and internal bounds just obtained gives exactly

    ||P1 psi_fin(t)-V(t)||
      <=E0+Ecut(t)+d_s+T0 L(rho,h)/sqrt(2pi),

throughout the assumed interval [t0,t_plus]. The common scalar exp(-ict) multiplies both comparison fields and cancels in this norm; it remains part of V itself. Reference systems are identities throughout, not traced outputs. This proof needs no conservation of R under the actual runtime and does not misidentify the projected branch with a stationary invariant sector.

## Pure, mixed and channel bounds; missing early interval

Let A and B be the two linear input-to-output contractions P1 U_fin E_seed and V on the specified input contract. The conditional estimate gives ||A-B||<=Ebr, also with a passive ancilla. For a unit vector xi, write a=Axi and b=Bxi. The identity

    |a><a|-|b><b|=|a-b><a|+|b><a-b|

gives trace norm at most (||a||+||b||)||a-b||<=2Ebr. These are subnormalized output operators: their traces can differ, and the trace bound pays that difference. It is not a claim about normalized postselected states.

The corresponding channel difference can also be written directly as (A-B)X A*+B X(A*-B*). The trace ideal inequality bounds it by 2Ebr||X||_1, with the same argument after adjoining any passive input ancilla. Thus the unhalved stabilized channel bound is 2Ebr on this fixed linear input contract. For a fixed mixed old apparatus state, a passive purification supplies the same proof if the separate finite theorem is uniform on that purification and keeps its reference output. No manipulation or erasure of the purifying environment is required. An input-dependent choice of preparation or target map would require a different contract and is not justified by this calculation.

No statement for t<t0 follows from equation (3). On that interval one can only use a separately proved inequality

    ||P1 psi_fin(t)-V(t)|| <= ||P1 psi_fin(t)||+||V(t)||.

Both summands require their own estimates. A precontact argument for the actual blank record alone does not bound the nonzero comparator. Conversely a small early outgoing tail does not bound an actual early writer population. The source correctly leaves both obligations, as well as an actual whole-interval cut estimate and complete packet normalization, to the later finite construction.

In particular (4) must not be restated as ||P1 psi_fin||<=Ebr: its desired branch can be order one at late time. No lower bound on success, eventual high success, finite runtime or permanent record behavior follows from this interface alone. Those require additional estimates, even though a separately supplied final normalized-output theorem could later provide them.

Only this REVIEW.md was created. No source, Git/W, checkpoint, axiom, editable prompt, model or publication change occurred; no delegation or scientific solver was used. The support disposition is conditional analytical support, not acceptance of a finite loader theorem.
