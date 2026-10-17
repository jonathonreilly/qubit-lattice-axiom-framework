# Finite transfer controlled only by head-moving hoppings

Status: proposed analytical improvement, requiring selective independent checking. For the SAME nominal converted apparatus and exact finite cap, the complete finite/infinite seed evolution difference is bounded, for every a>0, by

    min{2, j exp[-a(M+104)]
                  [exp(C sinh(a)|t|)-1]/[C sinh(a)]},
    C=.075.                                                   (1)

The proof retains arbitrary noncommuting internal onsite dynamics exactly. It does not remove source loads from the physical inventory or comparator. At a=1, a convenient sufficient uniform bound for 0<=t<=2T is

    min{2, .1 exp[-(M+105)+.15 T sinh(1)]}.                     (2)

T is an independently specified horizon parameter, not a selected onset. The coefficient of T in this sufficient length condition is 240 times smaller than the fresh radius-18 Chebyshev condition. This is not an optimal length, practical implementation or new temporal-escape claim.

## Sources and exposure

Read completely and hash-verified `../bandcenter_resources/PROPOSAL.md`, SHA256 `96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7`, and its fresh selective check `../bandcenter_resources_check/REVIEW.md`, SHA256 `01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd`. Those supply the explicit graph, positive blocks, exact cap compression, shared internal fiber and distance M+105. Their canonical ancestor at file SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff` remains conditional; no unrelated current W revision or old runtime is imported.

Root proposed both hopping-only interaction-picture locality and subsequently the weighted finite evolution/Duhamel route. I reconstructed both below after source exposure. This is an authored proposal, not an independent review or origin claim. Applicable previously read instructions/workflow are reused. No scientific execution, numerical experiment, parameter search, new agent, model override, W/Git/checkpoint/prompt edit or publication occurred. This file is the sole deliverable. The checked radius-18 Chebyshev estimate remains available independently as a fallback.

## 1. Exact common one-head Hilbert spaces

Work in the invariant one-head sector used by the supplied emitter product seed. Write the infinite Hilbert space as ell2(V_infinity) tensor H_internal, with the SAME four old/source qubits in H_internal, and tensor any passive reference afterward. This direct-sum description of head-conditioned blocks does not duplicate physical B or the source qubits.

Let P retain precisely the finite graph of the resource proposal: M new output sites n=0,...,M-1, integer M>=1, and all source, arms, converters, buffers, input and emitter sites. Its checked cap j n_last ensures EXACTLY

    H_M=P H_infinity P restricted to ran(P).

This includes the same endpoint diagonal2j, full internal operators and common physical scalar. Without this cap, the argument's equality of retained diagonal blocks would fail. The first omitted vertex n=M is graph distance

    d=M+105

from the emitter; the last retained output vertex is distance L=d-1=M+104. Only ONE installed head edge crosses P to its complement, with hopping magnitude j<.003. Its sign is irrelevant for the norm but is not altered in the Hamiltonian.

Decompose

    H_infinity=D+A,
    D=sum_x |x><x| tensor D_x,
    A=sum_{x,y adjacent} |x><y| tensor H_xy,
    H_yx=H_xy^*, ||H_xy||=|h_xy|.

Each D_x is the complete self-adjoint block at fixed head location, including B, head-conditioned VA/VB, clock diagonal, vacancy scalars and all other head-diagonal terms. D is bounded in this supplied one-head model; its possibly large norm is not approximated. Every off-diagonal head block is the installed real scalar hopping times the internal identity. The proof below also accommodates arbitrary internal hopping blocks with the same norm ceilings and adjoint symmetry.

Set D_M=PDP and A_M=PAP on the retained space. The cap identity gives H_M=D_M+A_M. No assumption that D_x and D_y commute is made.

## 2. Uniform absolute hopping row sum

The absolute head-hopping row sum is bounded by C=.075, independently of M:

| Head-site type | Sum of incident hopping magnitudes | Bound |
|---|---:|---:|
| Ordinary old site | 2J | <.062 |
| Junction arm-end or port-start | J+sqrt(2)J | <.075 |
| Filter site | J+t_filter=J(1+S0/C0) | <.049 |
| Old converter site | J+tau | <.038 |
| First new converter site | tau+j | <.010 |
| Ordinary new site | 2j | <.006 |
| New input endpoint | j+kappa | <.00300001 |
| Emitter | kappa | =1e-8 |

Entrance and finite last-output rows are smaller. At M=1 the first new output site has only its converter hopping; the cap is diagonal. The source A--B hopping is entirely inside D_x and does NOT move the head.

For the maximal junction row, J<.031 and sqrt(2)<1.415 give J(1+sqrt(2))<.074865. The filter bound uses C0>.9 and S0<.5. The converter bound uses tau<.007. Thus C is an explicit safe scalar ceiling, not an inferred spectral radius or cancellation of hopping signs. Symmetry gives the same column bound. The block Schur test gives ||A||<=C and ||A_M||<=C.

Large B/contact loads remain in D. This fact improves propagation estimates without lowering the actual physical incident-load inventory or asserting any new native coupling cap.

## 3. Same-time interaction-picture edges and Dyson cancellation

Use the exact diagonal interaction picture

    U_infinity(t)=exp(-itD) V_infinity(t),
    dV_infinity/dt=-i A_I(t) V_infinity(t),
    A_I(t)=exp(itD) A exp(-itD).

Its edge block is

    [A_I(s)]_xy=exp(isD_x) H_xy exp(-isD_y),

with norm exactly ||H_xy||. The finite interaction picture uses the IDENTICAL D_x for every retained site, by compression and cap. Consequently

    A_I,M(s)=P A_I,infinity(s) P

at the SAME time s on every retained edge. Internal rotations may fail to commute with one another; they are not commuted, scalarized or averaged. The block row-sum bound remains C for every real s.

For a fixed ordered tuple 0<=s_n<=...<=s_1<=t, the n-fold Dyson product sums head walks of exactly n hopping steps. Every walk from the emitter with n<d remains retained. Its ordered internal edge factors are identical in the two pictures, at exactly the same integration times. Therefore the corresponding Dyson coefficients agree on the ENTIRE seed subspace for n<d, after finite embedding. This is operator equality for arbitrary old/reference inputs, not only the four stationary columns.

Each n-fold coefficient has norm at most (C|t|)^n/n!. Norm convergence is absolute because the interaction is uniformly bounded. Thus an independently useful fallback is

    ||U_infinity(t)V_seed-embed U_M(t)V_seed||
       <=min{2, 2 sum_(n>=d) (C|t|)^n/n!}.                    (3)

The common factor exp(-itD) agrees on the embedded finite space, so it does not spoil the cancellation. For negative t the reversed time-ordered expansion gives the same |t| bound. No commuting-onsite assumption or perturbation of the large onsite norm appears. This Dyson bound is not replaced by an unjustified sinh estimate; the sharper bound below has a separate weighted-unitary proof.

## 4. Weighted finite evolution

Define f(x)=dist_infinity(emitter,x) on retained sites and

    W_a=sum_(x retained) exp[a f(x)] |x><x| tensor I_internal,
    a>0.

Adjacent vertices satisfy |f(x)-f(y)|<=1. The shortest path to the last output vertex has f(last)=L. The finite W_a is bounded and invertible for each finite M; no unbounded weight on the infinite Hilbert space is required. W_a commutes with D_M, all internal operations and a passive reference. Also W_a V_seed=V_seed.

In the interaction picture, the weighted generator uses

    B_a(s)=W_a A_I,M(s) W_a^-1.

Its Hermitian imaginary part has edge blocks

    [(B_a-B_a^*)/(2i)]_xy
       =sinh[a(f(x)-f(y))] [A_I,M(s)]_xy / i.

The resulting row and column sums of block norms are <=C sinh(a), so

    ||(B_a-B_a^*)/(2i)||<=C sinh(a).

For each vector, differentiating its weighted squared norm and applying this Hermitian bound gives Gronwall's estimate

    ||W_a U_M(s)V_seed||<=exp[C sinh(a)|s|].                (4)

The left-side operator norm is over the entire old/reference seed space. The same inequality can be obtained directly from W_a H_M W_a^-1, whose onsite part is self-adjoint and therefore has zero imaginary part. It is not a bound of ||W_a H_M W_a^-1|| by a small constant: the onsite terms remain large and exactly unitary.

Let P_last project onto the last retained output vertex with ALL internal coordinates. Equation(4) implies

    ||P_last U_M(s)V_seed||
       <=exp[-aL+C sinh(a)|s|].                            (5)

This probability-amplitude bound includes arbitrary internal entanglement. It neither projects the delivered state onto an output computational basis nor assumes that source registers have become blank.

## 5. Exact one-edge Duhamel comparison

For clarity form the decoupled self-adjoint operator

    H_dec=H_M direct_sum H_out,
    H_out=(I-P) H_infinity (I-P)

on the common infinite Hilbert space. The actual difference H_infinity-H_dec consists only of the two adjoint orientations of the single cut edge. On a vector supported in P, only the retained-to-omitted orientation acts, with norm

    ||(H_infinity-H_dec) U_dec(s)V_seed||
       =j ||P_last U_M(s)V_seed||.

There is NO factor two here: the reverse edge acts on a zero omitted component. The internal factor on this edge is the identity, and all internal amplitudes in P_last are retained. The onsite cap already ensured no diagonal perturbation at the cut. H_out need not approximate a physical reset or absorbing bath; it is only a self-adjoint direct-sum comparison operator.

Duhamel and the unitarity of the full infinite evolution give, for t>=0,

    ||[U_infinity(t)-U_dec(t)]V_seed||
      <=j integral_0^t ||P_last U_M(s)V_seed|| ds
      <=j exp(-aL)[exp(C sinh(a)t)-1]/[C sinh(a)].

For t<0 the same argument runs backward and gives |t|. Since U_dec(t)V_seed is exactly the embedded finite state, this proves (1), including the universal cap2. This is the full finite/infinite state-operator difference, not just leakage probability. Returns from the omitted region and all finite/infinite spectral components are included by Duhamel's exact identity.

## 6. Explicit size-versus-horizon condition

For any fixed a>0 and independently supplied horizon2T, a sufficient transfer budget epsilon_tr>0 is

    M+104 >= [ log{j[exp(2C T sinh(a))-1]/
                            [C sinh(a) epsilon_tr]} ]/a,     (6)

with integer M>=1. For T=0 the transfer is exactly zero and no logarithm is needed. This formula is a bound, not a request to optimize a or sweep graph sizes.

A simpler condition uses a=1 and exp(x)-1<=exp(x). Since L=d-1,

    transfer <=[j e/(C sinh1)] exp[-d+2C T sinh1].

Here j/C<.04 and e/sinh1=2/(1-e^-2)<2.5, using e>5/2. Thus the prefactor is <.1, proving(2). In particular

    M+105 >= .15 T sinh1+log(.1/epsilon_tr), M>=1,            (7)

is sufficient. The fresh checked Chebyshev condition used36 T sinh1 plus its logarithmic prefactor. The reduction of the leading coefficient is exactly36/.15=240. This compares two sufficient inequalities for the SAME horizon and SAME graph family; it does not identify the minimum physically necessary size or change the number of head/internal qubits at a given M. Those remain M+194 and M+198 respectively, with the checked positive-block inventory unchanged.

Once an independently established complete infinite-output error epsilon_infinity(t) is supplied, the finite device satisfies that error plus(1), with the SAME infinite normalized output comparator embedded in the infinite space. No finite-output renormalization or postselection is introduced. Passive-reference tensoring preserves all estimates; the corresponding unhalved trace-distance ceiling is at most twice the resulting operator error.

The scalar c_total and full exp(-itK) aging cancel only when comparing the two exact evolutions with identical supplied Hamiltonian data. They must still appear in the separate output comparator. No time-dependent physical drive was introduced: the interaction picture is a proof device for a static Hamiltonian.

## Scope and decisive check

This result requires neither scattering completeness nor absence of point spectrum, and it does not assert escape from the source or permanent halt. It uses head-number conservation, the checked exact cap compression, one cut edge, head-diagonal onsite blocks, and the explicit absolute hopping row sum. It remains independent of unqualified temporal or mass proposals. It does not lower physical source loads, derive a native supplier, assign physical units or improve coefficient precision.

The selective check should reconstruct the identical retained interaction-picture edges, weighted-generator imaginary-part norm, exact one-edge Duhamel forcing and distance L=d-1. The independently checked radius-18 Chebyshev estimate remains a fallback if any of these hypotheses fails in a changed architecture. No onset, numerical finite instance or publication is selected here.
