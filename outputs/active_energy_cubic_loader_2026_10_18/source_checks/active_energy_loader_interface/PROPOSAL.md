# Autonomous delayed suffix for the local active-energy SWAP

New bounded author construction requiring a distinct check. A long engineered head clock can apply only the diagonal-P path/record suffix near the revival of the continuously installed local-reference SWAP. No interaction is switched off, and no standalone observation time is treated as physical release. A gauge comparison bounds the overlap of the running SWAP with the late suffix by an explicit binomial tail integral. The construction uses supplied static positive real one-/two-body blocks, one coherent head, a product reference, and the literal active omega n_P. It provides a complete finite-window approximation to U_f, with all reference and head outputs retained.

This is a new proposed composition, not an already checked transfer. The reference portion remains nearest-neighbor, but the complete device uses a supplied finite-range suffix with degree eight at R. No full nearest-neighbor realization, arbitrary active H_PE, native preparation, permanent capture, reset or halt is claimed.

## 1. Exact sources and the obstruction to a naive attachment

N_root is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`; W is its sibling `correlation_worktree`. The following complete arguments were read and their identities refreshed:

- `local_reference_static_swap/PROPOSAL.md`, 16601 bytes, SHA256 `9e68a0eb2f81955e900a23bd88b05321b75ea4e2741da89f812ef2eda59b5c70`, and its complete check `bc0e54499663904538b862421d7338c31131cd9dc2923519b7d45fffb323a00b` (13502 bytes). They supply the finite local-reference comparison under explicit gap/weak-coupling hypotheses.
- `product_reference_static_swap/PROPOSAL.md`, 9995 bytes, `1a9e0ee47c8cc5b4f874abb2c8fa47258ee00fbe3cf77a87a2c968b407f0a825`. Its exact effective SWAP is unchanged.
- W/`docs/EXACT_TWO_BODY_ENGINEERED_LOADER_BOUNDED_THEOREM_NOTE_2026-10-18.md`, 31454 bytes, `43558ea59ebee23bf539d27ba1818a06b914fff52bb87d251b959b4889f3b868`, fully read here. Only its actual diamond/mixer/structured positive-block interfaces and scalar engineered-chain representation are used, not its 26-layer finite theorem or record guarantee.

The underlying exact sources were previously fully read and checked by this author and are reused at their unchanged scopes: matched extension `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e`, global composition `f874302baf42f962939fb0c9497b2c4f55283ed9189671048faadeeb04eca946`, and structured family `515c9e17df0a0c12e7df0dab6431015348af4140cef69189d334cd3574ea3de2`. Their detailed phase and positive-compensation formulas are also reproduced in the current canonical source just read. The new timing, tail, combined cap and composition below are not consequences of those reviews by analogy.

One cannot simply declare the local SWAP finished at its revival and then start the old loader. Its Hamiltonian remains installed and continues to evolve. Nor does diagonality of C_P^(b) mean it commutes with the local SWAP interaction W: the P-reference exchange changes P. Conjugation by C_P^(b) attaches X_b to that exchange. The following construction pays this difference while the head traverses the suffix; it does not replace it with a higher-body installed gate.

## 2. Actual continuously installed local SWAP

Use ordinary qubits Q,P,R and reference qubits B_1,...,B_N. Q and R are freely degenerate; P and each B_j have equal gap omega>0. Put

 a=lambda/sqrt(2), b=sqrt(5)lambda/4, c=3lambda/4,
 g=sqrt(2)lambda, s=a+2b+c+g,
 H_E=omega(n_P+sum_j n_Bj),
 H_F=kappa sum_(j=1)^(N-1)(I-SWAP_(Bj,B(j+1))),
 H_S=a X_Q+b(Z_Q+Z_P)+c Z_Q Z_P,
 V_loc=g exchange_(P,B1), W_loc=H_S+V_loc.

The actual local apparatus is H_loc=H_E+sI+H_F+W_loc, realized by the five positive data/exchange blocks and N-1 ferromagnetic plus N+1 occupation blocks of the pinned local source. It stays installed throughout. Its interaction norm obeys ||W_loc||<4lambda and it has no R interaction. All its terms commute with H_E.

For Pi the symmetric reference projector, that source proves H_F>=Delta(I-Pi), Delta=kappa/N^2, and Pi W_loc Pi equals the projected symmetric reference star. For lambda<=Delta/8, its complete elimination error is <512lambda/Delta throughout 0<=t<=2pi/lambda. The star comparison residual is g/(2sqrt(N)). Its effective gate is

 H_eff=a(X_Q+X_P)+b(Z_Q+Z_P)+c Z_Q Z_P,
 exp[-i(pi/lambda)H_eff]=exp(-i pi/4)SWAP_QP,
 ||H_eff||=9lambda/4.

These statements apply to arbitrary QP/passive-reference inputs and retain every reference qubit. In particular, with beta=|+>^N, at a free revival tau=pi/lambda=2pi m/omega the normalized local comparator is exp[-i(st+pi/4)]SWAP psi tensor beta(t), where beta(t)=(exp(-it omega n)|+>)^N. The same comparator near tau has error

 E_loc(t)<=512lambda/Delta+gt/(2sqrt(N))
                         +(omega+9lambda/4)|t-tau|.       (1)

The positive identities in H_F remain inside H_F; its symmetric-sector ground energy is zero, so no extra kappa(N-1) phase is appended.

## 3. A five-layer suffix at the clock's end

Use four head rails (a_path,b_path) as in the exact loader, with a_path initially1 and b_path an arbitrary coherent input label, possibly correlated with QP/passive references. These are head-position labels, not extra data qubits. The suffix is the chronological sequence

 H_b, CZ_(b,P), H_b, X_b, all-rail X_R.                 (2)

The controlled-Z layer is four diamonds: two P-gated and two identity. The final layer is four R-gated diamonds. There are two four-rail Hadamard layers and one four-bond permutation layer. A diamond gives a minus times its involution; consequently the first four layers give -C_P^(b), the final layer gives -X_R, and their full forward word is

 G_out=+X_R C_P^(b),
 C_P^(b)=|0><0|_P X_b+|1><1|_P I_b.                   (3)

There is NO remaining overall diamond minus in (3). After the local SWAP, (3) yields the desired U_f=I_a X_R C_P^(b)SWAP_QP. The unused 21 SWAP layers of the old loader are absent, not duplicated.

The suffix contains14 virtual slices and13 successive links: H occupies2, CZ4, H2, permutation2, final X_R4. Let the complete scalar clock coordinates be x=0,...,L with L>=16. Place these14 slices at x=L-14,...,L-1. Coordinates0,...,L-15 are ordinary input heads, and x=L is one external output head on each rail. All four rails have identical scalar coefficients and boundaries, including the unused a_path=0 inputs.

The ordered prefix G_x is identity before the suffix. Within it the positions are

 H: L-14,L-13;
 CZ: L-12=L_port,L-11=B,L-10=C,L-9=R_port;
 H: L-8,L-7;
 permutation: L-6,L-5;
 final X_R: L-4=L_port,L-3=B,L-2=C,L-1=R_port.

The first data-dependent prefix occurs exactly at x=L-10, the CZ C coordinate. Earlier prefixes are identity or H_b and commute with W_loc. Every prefix, including the final G_out, commutes with H_E and H_F: its only P operation is diagonal Z_P control, and R is degenerate and disjoint from the reference. Prefixes need not commute with W_loc.

## 4. Literal positive clock realization and its scalar solution

Set alpha=lambda/2. Define the positive engineered links

 k_r=alpha sqrt[r(L+1-r)], r=1,...,L,
 J_c=lambda(L+1)/4, C_head=4J_c.

Then k_r<=J_c. Realize each suffix link by the exact structured family: diamond outer weights k/sqrt(2), middle paired contact weight k, Hadamard bond weights k/sqrt(2), and permutation/cable weights k. All ordinary input/output links use Q_+(k). Repeat module parameters across rails. Add one occupation per physical head to make every virtual diagonal C_head, using the actual coefficient formulas

 p_terminal=C_head-(2a_end+k_cable),
 p_arm=C_head-(a_left+a_right+g_middle),
 p_H=C_head-(sqrt(2)k_H+k_cable),
 p_permutation=C_head-(k_link+k_cable),
 p_ordinary=C_head-(k_left+k_right).

Missing endpoint bonds are zero. Each subtraction is <=(sqrt(2)+1)J_c<C_head, or <=2J_c for ordinary sites; all added occupations are strictly positive. Identity diamonds retain their separate2g_middle n_u and omitted zero v contact. No uniform-matching mu repair is added on top of these compensations.

Let A be the physical B/C arm rotation and G=direct-sum_x G_x. On the one-head space, including the entire rail/data/reference fiber, the head-only suffix device has exact reduction

 (AG)^*H_head(AG)=h_L tensor I,
 h_L=C_head I-sum_(r=1)^L k_r(|r><r-1|+h.c.).          (4)

All physical head blocks are positive real two-body/onsite and preserve head number. They annihilate the head vacuum; the local apparatus does not need that property. No analytical prefix is installed as a higher-body interaction.

The scalar endpoint seed has the exact profile

 f_x(t)=exp(-i C_head t)sqrt(binomial(L,x))
                   [i sin(alpha t)]^x[cos(alpha t)]^(L-x). (5)

One derivation represents |x> as the symmetric weight-x vector of L mathematical spins: sum X has adjacent element sqrt[(x+1)(L-x)], and the commuting spin rotations give (5). Those spins are not additional apparatus. At tau=pi/lambda=pi/(2alpha),

 f(tau)=exp(-i C_head tau)i^L |L>.                     (6)

This synchronization is a constant Hamiltonian parameter relation, not a timed control action.

## 5. Exact transformed Hamiltonian and bounded overlap

A acts only on head coordinates and commutes with the local apparatus. Since every G_x commutes with H_E,H_F and sI, the actual combined Hamiltonian H_tot=H_head+H_loc is exactly, in this gauge,

 H_tilde=h_L+H_E+sI+H_F+W_loc+E,
 E=sum_x |x><x| tensor(G_x^* W_loc G_x-W_loc).          (7)

The fiber notation includes the rails and ordinary data; scalar head factors are understood. E vanishes for x<L-10. For every x its fiber norm is <=2||W_loc||<8lambda. This is an exact difference of two supplied Hamiltonians after a unitary change of representation, not a physical higher-body interaction being added.

Choose the benchmark H_0=h_L+H_loc. It factorizes into the scalar clock and the ACTUAL continuously acting local SWAP apparatus, not its effective approximation. For any normalized encoded logical/reference input, including arbitrary passive correlations, Duhamel gives

 ||[exp(-it H_tilde)-exp(-itH_0)]E_in||
 <=8lambda integral_0^t sqrt(p_tail(v))dv,
 p_tail(v)=sum_(x=L-10)^L |f_x(v)|^2.                 (8)

The estimate uses the full local state norm1 and the scalar clock probability. It does not assume the actual combined state factorizes, nor use any probabilistic independence of the logical input. The initial gauge is identity at x=0, so E_in is the physical supplied source input.

For 0<=v<=tau, X~Bin(L,sin^2(alpha v)) and Y=L-X~Bin(L,cos^2(alpha v)). Markov applied to exp(-Y) gives

 p_tail(v)=Pr(Y<=10)
 <=exp(10)[1-(1-exp(-1))cos^2(alpha v)]^L
 <=exp[10-(L/2)cos^2(alpha v)].                       (9)

The last inequality uses 1-exp(-1)>1/2; an upper bound greater than1 near tau is harmless. Thus sqrt(p_tail)<=exp(5)exp[-L cos^2(alpha v)/4]. For theta in[0,pi/2], cos theta>=2(pi/2-theta)/pi. Integrating the resulting Gaussian yields

 integral_0^tau sqrt(p_tail(v))dv
 <=pi sqrt(pi) exp(5)/(lambda sqrt(L)).               (10)

Multiplication by8lambda is <8192/sqrt(L): for example exp(5)<149, pi<22/7 and sqrt(pi)<2 already verify this conservative constant. For t<=tau+w, the remaining integral after tau is at most w because p_tail<=1. Hence the whole combined-device discrepancy satisfies

 E_join(t)<=8192/sqrt(L)+8lambda w,
                          0<=t<=tau+w.              (11)

This is an integral of norms of the actual gauge defect. There is no cancellation assumed in Duhamel, time switch, physical removal of W_loc, or claim that the head has zero early suffix amplitude. That early tail is explicitly paid.

## 6. Explicit simultaneous policy and complete full-loader output

Fix Lambda>omega>0 and0<epsilon<=1. Write M=Lambda-omega and choose

 N=ceil(8192pi^2/epsilon^2), kappa=M/16, Delta=kappa/N^2,
 L=ceil max{16,(2^20/epsilon)^2}, J_budget=M/64,
 C_P=(sqrt(5)+3)/2+2sqrt(2),
 lambda_max=min{omega/2, M/(4C_P),
                        epsilon Delta/65536,4J_budget/(L+1)},
 m=ceil[omega/(2lambda_max)], lambda=omega/(2m),
 tau=pi/lambda, alpha=lambda/2,
 w=min{epsilon/[128(omega+9lambda/4)],
                         epsilon/(1024lambda),epsilon/(64lambda L)}.
                                                               (12)

All quantities are determined before evolution. The same lambda sets the local SWAP and engineered clock. In particular J_c<=J_budget, lambda<=Delta/8, the clock is finite, and w<tau. The local bound(1) applies up to tau+w<2tau with

 512lambda/Delta<=epsilon/128,
 gt/(2sqrt(N))<epsilon/64,
 (omega+9lambda/4)w<=epsilon/128,
 E_loc(t)<epsilon/32.                                (13)

These are the baseline local budgets with its accuracy parameter epsilon/4; the smaller kappa and additional lambda restriction preserve its proof hypotheses rather than importing its previous cap formula.

From (11),(12), E_join<=epsilon/128+epsilon/128=epsilon/64 throughout the window. For a common head comparator concentrated at the external endpoint, write h_L=C_head I+h_bar. Its mathematical-spin representation gives ||h_bar||=alpha L=lambda L/2. Equation(6) and a one-unitary difference bound imply

 ||f(t)-exp(-i C_head t)i^L|L>||
 <=(lambda L/2)|t-tau|<=epsilon/128.                  (14)

This pays the entire actual benchmark head complement; it is not normalization of a successful branch. On the physical endpoint A is identity and G_L=G_out. Combine the exact physical gauge, (11), the local comparison(13), and (14). For every coherent input with a_path=1, arbitrary b_path, arbitrary QP/passive references, blank R, beta and every other head vacant, define

 V_t xi=exp[-i(C_head+s)t] i^L exp(-i pi/4)
       [external endpoint embedding of U_f xi] tensor beta(t),
 U_f=I_a X_R C_P^(b)SWAP_QP.                          (15)

All other physical heads are vacant in this normalized target. Every Q,P,R and reference-qubit output is retained. The path label is still a physical head rail, not a traced classical output. The scalar i^L, the positive-block shift s, the engineered diagonal C_head and effective gate phase exp(-i pi/4) each appear exactly once. There is no uniform mu phase and no remaining suffix minus.

Uniformly on the positive-width closed interval[tau-w,tau+w],

 ||exp(-itH_tot)E_in-V_t||
 <epsilon/64+epsilon/32+epsilon/128=7epsilon/128<epsilon/16.
                                                               (16)

The unhalved stabilized complete-output channel error is <7epsilon/64<epsilon/8. The actual probability of external endpoint AND R1 is >1-(7epsilon/128)^2, by projecting the normalized complete-vector error onto its complement. No claim concerns a computational-bit value for arbitrary input. No conditional normalization or reference discard appears in the proof.

The actual current R1 branch is NOT claimed to have the old exact all-time logical factorization: the gauge defect E is nonzero. Approximate full-window success follows from(16). Any rare-event or earlier-time normalized record claim would require its own proof. The entire Hamiltonian is constant in time; w is an observation window, not a schedule that switches the interactions or causes release. Beyond the horizon it may continue evolving and undo the operation.

## 7. Counts, full-support cap and explicit bounded-range placement

There are14*4=56 suffix heads. Its blocks before compensating occupations are22 in the controlled-Z diamonds (two gated, two identity),24 in the four record diamonds,16 in the two Hadamard layers,4 permutation bonds and16 interlayer cable bonds:82 total. The 56 positive head compensations bring that to138. The other 4(L+1)-56=4L-52 heads are ordinary exterior heads. The L-13 virtual links outside the suffix provide4L-52 additional ordinary bonds; each exterior head has one positive compensation. Thus

 head qubits=4(L+1), H_head blocks=8L+34,
 total qubits=4L+N+7,
 total blocks=(8L+34)+(2N+5)=8L+2N+39.               (17)

Reference qubits are physical B_j; the mathematical spins used for (5) are not counted. Q,P,R are shared actual qubits. The two a_path=1 endpoint positions encode one head, not two simultaneous head excitations. All four rays exist physically.

The head-block incident bound from the actual positive compensation is <=(5+sqrt(2))J_c at any head. There are four P contacts of norm<=2J_c and eight R contacts of norm<=2J_c. Hence their extra loads are <=8J_c and16J_c. On adding the local apparatus,

 load(P)<=omega+C_P lambda+8J_c
                         <=omega+M/4+M/8<Lambda,
 load(Q)<=lambda[sqrt(2)+(sqrt(5)+3)/2]<M/4,
 load(R)<=16J_c<=M/4,
 load(B1)<=omega+2kappa+2sqrt(2)lambda<omega+M/8+M/4,
 load(Bj)<=omega+4kappa=omega+M/4  (j>=2).

The B1 strict inequality uses sqrt(2)/(2C_P)<1/4. Head loads are below (5+sqrt(2))M/64<Lambda. All are full-support norms; no symmetric-sector or one-head cancellation reduces these physical sums. Every actual term commutes with H_E, including suffix contacts because they use Z_P and degenerate X_R. Exact energy conservation and approximate SWAP therefore coexist with reference energy/correlation changes.

An explicit finite-range cubic placement is available. Put P=(0,0,0), R=(1,0,0) in the cube{0,1,2,3}^3. Reserve the four left suffix ports at(i,3,3) and four right ports at(i,2,3), i=0,...,3 in rail order. Place the other48 suffix heads injectively at48 of the remaining54 cube sites (after removing P,R and those eight ports). This puts all suffix pairs within Manhattan range9, with unused sites permitted. Attach the ordinary input ray of length L-14 to each left port along increasing z and one output head at z=4 above each right port. All eight vertical rays have distinct horizontal coordinates. They do not meet the cube except at their own ports.

Put Q=(0,0,-1) and B_j=(-j,0,0), j=1,...,N. Then QP,PB1 and successive reference bonds are nearest-neighbor, outside the suffix cube except for P. No reference site or Q collides with any head or R. All installed interactions have range<=9. The full maximum graph degree is eight at R (P has four head contacts plus Q and B1); the device is NOT claimed to be an all-nearest-neighbor cubic graph. Uninstalled geometric adjacency supplies no coupling. These range/degree premises are no stronger in kind than the exact loader's supplied finite-range interactions; they do not identify a native realization.

At fixed omega and M>0, the explicit N,L are both Theta(epsilon^-2), with a very large constant in L. As epsilon tends to zero, epsilon Delta/65536=Theta(M epsilon^5) eventually dominates the other lambda_max entries, including the clock cap O(M epsilon^2). Integer rounding changes lambda by at most a factor two. Thus this sufficient family has total size Theta(epsilon^-2) and tau=Theta(M^-1 epsilon^-5). These are not optimal or practical claims; the finite prescription(12), including its huge floor, is the operational statement. No previous full-loader runtime has been imported. The chosen window remains shrinking, and does not certify permanent dwell or storage.

## 8. Scope, failed shortcuts and exposed derivation

The narrow naive shortcut fails because W_loc does not commute with C_P^(b), and a stand-alone SWAP revival does not release its continuously coupled data. Neither fact is a general no-go. The concrete alternative here keeps W_loc on and bounds its noncommutation through a late, explicitly engineered head distribution. There is no timed switch, hidden projective measurement, discarded old P or reference, or higher-body installed conditional Hamiltonian.

The exact old26-layer gauge does not survive unchanged after adding active P dynamics. It is replaced by a five-layer diagonal-P suffix and the explicit defect(7). The suffix's commutation with H_E and H_F is essential. Substituting earlier P-flipping gates or an arbitrary active environment would change that argument and could introduce large unsuppressed terms. Likewise a plain additive-norm bound integrated over the entire tau would not close; the proved head-tail integral is the decisive new interface.

The product reference, coherent logical endpoint input, blank heads/R, exact equal gaps and coefficient correlations, and selective positive finite-range interactions are still supplied. The reference is not prepared thermally or by the ferromagnetic chain; its actual output may be correlated and have changed energy moments. No reset, reusable reference, active arbitrary H_PE, native control synthesis, permanent halt or receiving-apparatus capture is established. This bounded construction does not license the historical processor or Record interpretation.

ROOT requested an autonomous composition investigation and suggested exploiting the diagonal-P suffix. I authored the local-reference source and had prior authorship/review exposure to the exact loader, engineered clock and finite-window arguments. The late-suffix placement, exact transformed defect, binomial norm integral, synchronized parameter family, combined finite-range placement and resource accounting are new source-exposed author calculations. They require a distinct check; no independent acceptance or novelty judgment is asserted.

Only this PROPOSAL.md was created. Source hashes were checked by Python3 pathlib/hashlib, and work otherwise comprised complete text reads and analytical derivation. No scientific executable, symbolic solver, simulation, sweep, external search, delegation, source overwrite, Git/canonical/checkpoint/axiom/editable-prompt/model change or publication occurred. No editable prompt changed. The campaign deadline was checked during work; this bounded candidate was completed before it.
