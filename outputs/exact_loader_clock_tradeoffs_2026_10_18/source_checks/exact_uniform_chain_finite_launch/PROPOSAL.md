# Finite endpoint launch on an exactly uniform scalar chain

This is a new conditional finite-window theorem proposal requiring a distinct check. It concerns one scalar, number-conserving chain with a supplied weak endpoint emitter, exact equal diagonals and a fixed-diagonal far cap. It does not assume a router, a record, a data-dependent Hamiltonian or a global gauge realization. The complete normalized output comparison includes the actual emitter and every input/interior head as residual coordinates; none is discarded. For fixed interior length and constant hopping, the explicit sufficient policy below has length and dimensionless time of order epsilon^(-2) log(1/epsilon). This is an analytical upper-bound family, not an optimality or practical-resource claim.

The main simplification is exact: compare the physical seed once to a normalized, spectrally filtered state of the semi-infinite source operator, and then cut only the far hopping. There is no artificial early-contact interface. Complete normalization of that filtered state pays its actual emitter residual; it is not replaced by the unfiltered survival amplitude.

## 1. Literal finite operator, geometry and suppliers

Fix an integer K>=1, a hopping J>0, an integer ell>=100(K+1), and 0<rho<=1/2. Put

    gamma=rho J,  N=2ell+K-1.

The physical heads are the emitter s and the ordinary sites n=0,...,N. Exactly one head is excited initially, at s; all other heads are vacant. The ordinary sites are divided into input 0,...,ell-1, fixed interior ell,...,ell+K-1, and retained external output

    F={ell+K,...,2ell+K-1}.                         (1)

Thus F has exactly ell sites. There are 2ell+K+1 head qubits and 2ell+K source-to-cap edges. These are one finite chain's counts, without a later network or data encoding.

For two hard-core heads x,y define the positive real block

    Q_c(x,y)=c[n_x+n_y-(sigma_x^+ sigma_y^-
                                      +sigma_x^- sigma_y^+)].

Its full two-qubit norm is 2c. Use the actual combined positive source block

    B=Q_gamma(s,0)+(2J-gamma)n_s+(J-gamma)n_0.       (2)

Its one-head matrix on (s,0) is [[2J,-gamma],[-gamma,J]], and its full two-qubit norm is exactly 3J, including the doubly occupied sector. Define

    H_fin = B + sum_(n=0)^(N-1) Q_J(n,n+1)
                + J n_N + mu sum_(v=s,0,...,N) n_v,
    mu=c_mu J,  c_mu>=0 fixed.                      (3)

The cap term J n_N is essential. On the one-head space every diagonal is exactly 2J+mu, the source hopping is -gamma, and all ordinary hoppings are -J. The source and cap are not replaced by an ordinary bond. All blocks in (3) are real and positive on their complete local supports. No claim concerns a many-head preparation or operation.

Counting B as one supplied two-body block gives N+2=2ell+K+1 nonzero blocks before the common shift. If mu>0 and each uniform onsite term is counted separately, add 2ell+K+1 blocks; for mu=0 add none. This is a stated block convention, not a claim that the three positive summands of B are one native interaction. Counting them separately would add two blocks and change the corresponding incident accounting.

Under the combined-B convention, the full-support incident norm sums are 3J+mu at s, 5J+mu at 0, at most 4J+mu at ordinary nonterminal sites, and 3J+mu at N. Hence

    J=Lambda/(5+c_mu)                              (4)

enforces the common incident cap Lambda, independently of epsilon. With no cap requirement J is any fixed positive number. The scalar chain has maximum head degree two and is nearest-neighbor on a line. A later nonlocal change of physical architecture does not inherit those geometry/count assertions merely from having the same one-head scalar dynamics.

The exact coefficient correlations, endpoint excitation, empty remaining heads, one-head conservation, cap and common shift are supplied premises. No fabrication tolerance, autonomous preparation or native physical identification is established.

## 2. Exact half-line source and one initial spectral cost

Let H_infty^0 be the corresponding one-head operator on {s,0,1,...}, without the cap or common mu: diagonal 2J everywhere, source hopping -gamma, ordinary hoppings -J. Its normalized cyclic source spectral representation is the checked standalone endpoint result fb72f4ed / 51247de9. With k in (0,pi), write

    e(k)=2(1-cos k), E(k)=J e(k), u=Jt,
    F(k)=-i sqrt(2/pi) rho exp(ik)
                         /[(2-rho^2)cot k-i rho^2],
    w(k)=|F(k)|^2, integral_0^pi w(k) dk=1.          (5)

Its exact seeded evolution is

    exp(-it H_infty^0)|s>
       = A(t)|s> + O_t F + I_t conjugate(F),
    (O_t f)_n=(2pi)^(-1/2) integral exp(ink-iu e(k))f(k)dk,
    (I_t f)_n=(2pi)^(-1/2) integral exp(-ink-iu e(k))f(k)dk,
    A(t)=integral exp(-iu e(k))w(k)dk, n>=0.         (6)

The source phase exp(ik), Fourier factors and common energy 2J are retained in (5),(6). The two lead terms separately have full-integer Fourier norm one, but neither is asserted to be a unit half-line state. Their interference and the emitter coordinate are part of the exact identity.

Fix 0<h<=10^(-3), rho^2<=h. Use the actual real cutoff chi(k), with q=k-pi/2: it is one for |q|<=h/2, zero for |q|>=3h/4, and on each width-h/4 transition it is

    chi=1-10z^3+15z^4-6z^5,
    z=4(|q|-h/2)/h.

This cutoff is C2 and W^{3,1}, with its first two derivatives vanishing at the joins. It is not replaced by an analytic cutoff. The checked source mass estimate gives

    P=3rho^2/h,
    integral_(|q|>h/2) w(k)dk <= P,
    p=||chi F||_2^2 >=1-P,
    g=chi F/sqrt(p).                                (7)

Require P<1/2. Then p>1/2, and g has exactly unit L2 norm with its actual positive normalization.

The loose constant in (7) can also be read directly from (5): with a0=2-rho^2>=7/4, w(k)=(2rho^2/pi)/[a0^2 tan(q)^2+rho^4]. On |q|>h/2 use |tan(q)|>=|q| and extend the positive q^(-2) integral to both infinite tails. This gives at most 8rho^2/(pi a0^2 h)<3rho^2/h. Since chi=1 on the retained central interval and 0<=chi<=1, both 1-p and ||(1-chi)F||_2^2 obey the same bound.

The cutoff is a well-defined bounded spectral multiplier of H_infty^0 because E(k) is strictly monotone. Let

    Phi_chi(t)=exp(-it H_infty^0) chi(H_infty^0)|s>/sqrt(p).

It has norm one exactly, and its physical coordinates are

    Phi_chi(t)=A_chi(t)|s>+O_t g+I_t conjugate(g),
    A_chi(t)=integral chi(k)w(k)exp(-iu e(k))dk/sqrt(p). (8)

In particular the source integrand contains ONE chi, not chi squared. Multiplying the real source spectral column by chi gives (8); chi is real, so the incoming coefficient really is conjugate(g). The general cyclic spectral theorem and (6) give this identity, not a renormalization of the outgoing part alone.

At time zero,

    || |s>-Phi_chi(0)||
       <= ||(1-chi(H_infty^0))|s>|| + |1-sqrt(p)|
       <= sqrt(P)+P <=2sqrt(P).                     (9)

Here 1-p<=P and sqrt(p)>0. This is the single initial spectral omission cost. Under any later common unitary it remains at most (9), even if chi(H_infty^0)|s> already has a small tail beyond the future cap. No omitted spectral component is integrated over a long Duhamel interval.

The physical common shift contributes exp(-i mu t) to every vector in (6),(8). It will appear once in the final comparator. The factor exp(-iu e(k)) already includes exp(-2iJt); that phase is not added a second time.

## 3. Scalar pole constants and their exact signs

Only the scalar M=1 cases of checked half-line source 43c0cc05 / check 1fa28554 and late-negative-gap source a0313926 / check ef27352b are used. No network inverse, biased momentum, scattering matrix or data coefficient is imported. The following explicit constants reproduce their scalar hypotheses and are deliberately conservative.

Put a=23/100 and B2=64, B3=512, B4=2048. For scalar coefficient M=1 the ordered Leibniz bounds are

    C=(1,2,7,30), D=(2,24,394,6280).

Indeed C=(1,1,2,5) star (1,1,3,10), with
(x star y)_r=sum_l binomial(r,l)x_l y_(r-l); multiplication by the identity coefficient changes nothing. The cutoff product bounds then give exactly the displayed D. Define the fixed positive numerical constants

    P_star = D3/a^3 +6B2 D2/a^4
       +(4B3/a^4+15B2^2/a^5)D1
       +(B4/a^4+10B2 B3/a^5+15B2^3/a^6)D0,

    Q_star = D3/(2a^2)+2B2 D2/a^3
       +(4B3/(3a^3)+15B2^2/(4a^4))D1
       +(B4/(3a^3)+10B2 B3/(4a^4)+3B2^3/a^5)D0,

    D_star=4P_star+20Q_star.                          (10)

No numerical fitting, unspecified constant or rho dependence is hidden in these expressions.

For clarity, the mechanism is the exact real-axis substitution

    x=tan(k-pi/2), A=2-rho^2, b=rho^2/A,
    F(k(x))= i sqrt(2/pi)rho exp(ik(x))/[A(x+ib)],
    1/(x+ib)=-i integral_0^infty exp(ixv-bv)dv,
    1/(x-ib)= i integral_0^infty exp(-ixv-bv)dv.       (11)

Thus F adds +vx to a phase, while conjugate(F) adds -vx. The source signs cannot be exchanged just because their moduli agree. The amplitude after changing variable is chi(k(x))exp(+-ik(x))k'(x); its weak derivative L1 norms through order three are at most D_r/h^2. The actual cutoff supplies the required third weak derivative and boundary traces. For each rho>0 Fubini has the finite initial majorant ||amplitude||_1/b; uniform estimates are obtained afterward by real integration by parts.

Three such integrations have the seven absolute coefficients 1,6,4,15,1,10,15. If the phase derivative has magnitude at least a L+v and the next three derivatives are bounded by B2 L,B3 L,B4 L, integrating v>=0 gives a pointwise bound rho Q_star/(h^2 L^2). For an adverse sign, split v at half the proved negative gap, use the three-derivative estimate on the low range, and use complete Fourier Parseval before integrating the high range. The resulting half-line estimates below are the checked lemmas with their exact scalar phases. Their whole-sequence norms, rather than uniform pointwise bounds summed over infinitely many sites, are essential.

## 4. The only dynamical perturbation is the far cut

Embed the finite one-head space in the half-line and remove just the hopping between N and N+1. The extended decoupled operator is

    H_cut^0=H_infty^0+Delta,
    Delta=J(|N><N+1|+|N+1><N|).                     (12)

All diagonals remain 2J. Its finite restriction is precisely (3) minus mu I, because of the actual cap J n_N. Its other component is an unoccupied decoupled half-line. Extending the common shift as mu I on both components changes no estimate or finite physical statement.

Use the entire interval 0<=u<=7ell/8. At either n=N or n=N+1 one has

    2ell<=n<=2.01ell,
    d/dk[nk-u e(k)]>=ell/4,
    d/dk[-nk-u e(k)]<=-2ell.                       (13)

The latter uses sin k>0 on the cutoff support. Both original first derivatives have magnitude at most 4ell, and their second, third and fourth derivatives have magnitude at most 2ell. Since k'(x)>=.999, |k''(x)|<=.002, |k'''(x)|<=3 and |k''''(x)|<=.1, the x-phase first derivative has magnitude greater than .23ell, and the subsequent three derivatives have respective ceilings 4ell,32ell,128ell. These ceilings are smaller than those used in (10).

For the outgoing term the +vx from F strengthens the positive derivative; for the incoming term the -vx from conjugate(F) strengthens the negative derivative. Thus the favorable auxiliary-frequency integration applies to BOTH terms for every time from zero, including u=0. It does not apply the outgoing pole to the wrong incoming amplitude. At each of the two cut sites,

    |(O_t g)_n|, |(I_t conjugate(g))_n|
                           <=rho Q_star/(h^2 ell^2).

Consequently

    ||Delta Phi_chi(t)||<=2sqrt(2)J rho Q_star/(h^2 ell^2),
    E_cut := integral_0^(7ell/(8J)) ||Delta Phi_chi(v)||dv
                 <=(7sqrt(2)/4)rho Q_star/(h^2 ell)
                  <3rho Q_star/(h^2 ell).             (14)

This is an integral of norms. No oscillatory cancellation inside Duhamel, zero initial filtered tail, or finite-matrix absence of bound states is assumed. Combining (9) with Duhamel for the two exact evolutions gives, uniformly for 0<=t<=7ell/(8J),

    || exp[-it(H_cut^0+mu I)]|s>
                       -exp(-i mu t)Phi_chi(t)||
          <= 2sqrt(P)+3rho Q_star/(h^2 ell).           (15)

In particular the finite cap's later reflections are paid throughout this specified horizon. Nothing extends (15) to arbitrarily late times with the same bound.

## 5. Exact output packet and complete late tails

For all integer n define the full-line Fourier sequence

    b_n(t)=(2pi)^(-1/2) integral_0^pi
                                 exp(ink-iu e(k))g(k)dk.

Zero extension of g to a full Fourier period and Parseval give sum_(n in Z)|b_n|^2=1. Let

    d(t)=||(b_n(t))_(n notin F)||_2,
    q_F(t)=||(b_n(t))_(n in F)||_2=sqrt(1-d(t)^2),
    z(t)=q_F(t)^(-1) sum_(n in F)b_n(t)|n>.           (16)

The last definition will be licensed by a proved positive lower bound on q_F. Its denominator is positive real: no time-dependent phase adjustment or postselection is used to define the target. All other physical heads, including s, have zero amplitude in z. The physical normalized target is exp(-i mu t)z(t).

Restrict to the closed, positive-width time window

    u in [3ell/4,7ell/8].                            (17)

For the complete incoming half-line n>=0, the favorable conjugate lemma, with scalar M=1, gives

    i(t):=||I_t conjugate(g)||_(n>=0)
       <=2rho Q_star/(h^2 u^(3/2))
        <4rho Q_star/(h^2 ell^(3/2)).                (18)

This includes the origin n=0. The smaller checked incoming constants (4,32,128) are dominated by the constants in (10); u>=1 follows from our length requirement.

For the omitted left part of the full-line outgoing packet, write n=L-r with r>=0 and L=ell+K-1. This enumerates EXACTLY every integer n<=ell+K-1, including the physical input/interior and the negative Fourier indices. The phase is -rk+Lk-u e(k). The checked late-gap conditions hold with

    Q_left=1.98u-L >=.485ell-K+1 >=.4ell>=1,
    L+u<=1.885ell<=16 Q_left.                       (19)

Use Cgap=16, M=1 in the late lemma. Since 2(2-rho^2)<=4 and .4^(-3/2)<4, it gives

    d_left <=4rho P_star/(h^2 ell^(3/2))
                    +4sqrt(h)/rho exp(-rho^2 ell/10). (20)

The exponential term is a norm bound on the complete high-auxiliary-frequency sequence. It is not an exponential assertion about the exact physical emitter survival.

For the omitted right part, set n=R+r, r>=0, R=N+1=2ell+K. The phase is (r+R)k-u e(k). The positive-gap lemma uses

    Q_right=.99R-2u >=.23ell>=1,
    R+u<=2.885ell<=16 Q_right.                      (21)

It follows that

    d_right <=2rho Q_star/(h^2 Q_right^(3/2))
             <20rho Q_star/(h^2 ell^(3/2)).          (22)

Both tails begin at the correct endpoints: the omitted left interval ends one site before F, and the omitted right interval starts one site after F. Combining their norms conservatively by the triangle inequality gives

    d(t)<=rho D_star/(h^2 ell^(3/2))
                    +4sqrt(h)/rho exp(-rho^2 ell/10). (23)

There is no special uncontrolled interior: the K fixed sites are ordinary scalar coordinates already included in (19),(20).

## 6. Normalization closes the emitter and full-apparatus budget

The exact filtered state Phi_chi has norm one. Its component on F is the restriction of b+I_t conjugate(g), while its emitter coordinate is A_chi from (8). Therefore, whenever q_F>0,

    Re <z(t),Phi_chi(t)> >=q_F(t)-i(t),
    ||Phi_chi(t)-z(t)||^2
          <=2(1-q_F(t))+2i(t) <=2d(t)^2+2i(t).       (24)

The final inequality uses 1-q_F=d^2/(1+q_F)<=d^2. It does not replace a complex interference term by a probability. It retains the exact relative phase fixed in (5),(16).

There is also an explicit complete residual estimate. If q_F>=i, then

    ||(1-P_F)Phi_chi(t)||^2
       =1-||P_F Phi_chi(t)||^2
       <=1-(q_F-i)^2 <=d^2+2i.                     (25)

Thus (25) pays the actual filtered emitter, every physical input/interior coordinate and every tail beyond the finite cap simultaneously. In particular |A_chi(t)| obeys this bound; no estimate on the DIFFERENT unfiltered A(t) has been substituted. The square root of i in (24),(25) is explicitly paid by the policy below. Exact normalization, not an assumed eventual success or scattering completeness of a different graph, is the premise of this step.

The actual finite state is normalized and has no coordinates beyond N. Equations (15),(24) now give the full-vector estimate

    ||exp(-it H_fin)|s>-exp(-i mu t)z(t)||
       <=2sqrt(P)+3rho Q_star/(h^2 ell)
                                     +sqrt(2d(t)^2+2i(t)). (26)

Every vector is on the complete physical one-head space, using the harmless extension by zero when necessary. A passive reference or fixed data tensor factor is retained identically. No projection or normalization of the actual state is part of (26).

## 7. Explicit simultaneous policy and sufficient resource orders

For 0<epsilon<=1 choose

    h=10^(-3),
    rho=epsilon sqrt(h)/1024,
    ell=ceil max{
        1000, 100(K+1),
        192rho Q_star/(h^2 epsilon),
        [128rho D_star/(h^2 epsilon)]^(2/3),
        [32768rho Q_star/(h^2 epsilon^2)]^(2/3),
        (10/rho^2) log[512sqrt(h)/(rho epsilon)]
    },
    t_minus=3ell/(4J), t_plus=7ell/(8J).             (27)

This is noncircular: (10) consists only of fixed numerical constants, rho is fixed before ell, and the natural-log argument equals 524288/epsilon^2>1. All geometric and scalar lemma hypotheses follow: rho<=1/2, rho^2<=h, P=3epsilon^2/1024^2<1/2, p>=1-P>1/2, and the stated gaps exceed one.

The individual simultaneous allowances are

    initial spectral cost 2sqrt(P) <epsilon/256,
    far-cut integral                <=epsilon/64,
    algebraic part of d             <=epsilon/128,
    exponential part of d           <=epsilon/128,
    complete incoming i             <=epsilon^2/8192.

Consequently d<=epsilon/64<1, which proves q_F>0 BEFORE (16) is used; also q_F>i. Equation (24) gives

    sqrt(2d^2+2i)<=sqrt(3)epsilon/64<epsilon/32.

Hence the promised complete finite endpoint theorem holds throughout the closed window:

    ||exp(-it H_fin)|s>-exp(-i mu t)z(t)||
          <13epsilon/256<epsilon/16<epsilon/8,
                      t in [t_minus,t_plus].         (28)

In particular the physical probability of finding the head in F exceeds 1-(epsilon/8)^2, and the norm of its complete complement is less than epsilon/8. These are consequences of the normalized full-vector theorem, not premises used to close it. No record qubit is present. For normalized pure inputs the unhalved trace distance is at most twice the vector error, hence less than epsilon/4 under the stated conservative epsilon/8 contract.

For fixed K and fixed c_mu, as epsilon tends to zero, h is constant and rho=Theta(epsilon). The nongeometric entries in the length maximum have orders respectively 1, 1, epsilon^(-2/3), and

    rho^(-2) log[512sqrt(h)/(rho epsilon)]
                          =Theta(epsilon^(-2) log(1/epsilon)).

The final term therefore supplies both an upper and a matching lower order for THIS explicit policy. The ceiling and fixed K do not alter it:

    heads, positive-block count, Jt_minus, Jt_plus
                     =Theta(epsilon^(-2) log(1/epsilon)),
    t_minus,t_plus =Theta(J^(-1)epsilon^(-2) log(1/epsilon)),
    gamma=Theta(J epsilon).                           (29)

With (4), replace J^(-1) by the fixed multiple (5+c_mu)/Lambda. The window has width ell/(8J)>0 and width/t_minus=1/6. For K varying with epsilon, (27), not the fixed-K order in (29), is the statement to use. The large constants P_star,Q_star and all exact coefficient supplies remain visible; the order is not a lower bound, an optimization result, a numerical speed comparison or a practical apparatus proposal.

## 8. Conditional identical-rail and exact-gauge interface

For any fixed number of identical scalar copies, in particular four, a coherent endpoint input sum_r |s_r> tensor xi_r evolves with the SAME scalar profile and phase on every rail. Orthogonality of the rail errors gives an error operator whose adjoint-square is the one-rail squared error times the identity. Thus (28) holds without a factor sqrt(4), also after tensoring arbitrary passive references. The rail amplitudes and their initial coherence are supplied; four physical emitter excitations at once are not the one-head input considered here.

A further data operation follows only if a separate construction proves an exact, time-independent unitary identification G on an invariant physical sector, including source and cap, such that

    H_phys|sector = G[(H_fin on identical rails) tensor I_data]G^*,
    G(|source rails> tensor xi)=the actual supplied input,
    G(|n,r> tensor xi)=the claimed full output for every n in F. (30)

Then applying G to both sides of (28) proves the corresponding full-output theorem, with every data/reference subsystem, head, fixed sign and common phase specified by that SAME identification. Equation (30) may mix head coordinates or apply data unitaries; no local implementation, hidden active data supply, ordinary-control duplication or record statement follows from the scalar theorem alone. The operator identity must include all physical onsite repairs. The physical degree, range, qubit/block counts and incident cap must be checked for that separate realization.

For the intended coordinate convention x=n-ell, K=74 gives source x=-ell-1, ordinary left endpoint x=-ell, final internal origin x=73, cap x=73+ell, and retained EXTERNAL output x=74,...,73+ell. Equivalently F={ell+74,...,2ell+73}. There are 2ell+74 source-to-cap edges. This is an exact coordinate specialization of (1), not an independent proof that a proposed data graph satisfies (30).

The diamond and matched-extension sources listed below motivate such an interface: their scalar shift and fixed output signs must be retained if they are used. Their local exact identities alone do not imply a global network gauge, and no such global conclusion is used in (5)--(29). No normalized correctness conditioned on an arbitrarily rare early flag, permanent halt, all-time confinement, capture, reset or irreversible record is asserted.

## 9. Source identities, exposure and remaining check

All paths in this section are relative to
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.
The following complete source/review bodies were read for this task and their exact bytes refreshed before finalization. The role column identifies actual mathematical use rather than Git ancestry.

| Source | Bytes | SHA256 | Role |
|---|---:|---|---|
| `common_product_endpoint_launch/PROPOSAL.md` | 14099 | `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4` | Complete normalized scalar source, spatial columns and positive source block. |
| `common_product_endpoint_launch_check/REVIEW.md` | 12312 | `51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1` | Distinct support at that standalone scope, including exact phase and spectral completeness. |
| `common_product_outgoing_pole_tail/PROPOSAL.md` | 17300 | `b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80` | Real pole/three-IBP and actual-cutoff coefficient machinery; its network substitution is not used. |
| `common_product_outgoing_pole_tail_check/REVIEW.md` | 12246 | `0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00` | Distinct check of that machinery and its stated domains. |
| `common_product_resonant_halfline_tails/PROPOSAL.md` | 15197 | `43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1` | Scalar favorable conjugate-incoming and positive-outgoing full half-line norms, coefficient definitions. |
| `common_product_resonant_halfline_tails_check/REVIEW.md` | 9812 | `1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b` | Distinct support for these exact component interfaces. |
| `common_product_resonant_late_tails/PROPOSAL.md` | 13034 | `a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9` | Scalar negative-gap norm with explicit translation, low/high auxiliary split and complete high-frequency Fourier norm. |
| `common_product_resonant_late_tails_check/REVIEW.md` | 7992 | `ef27352b742abe064e5b8d71d09d7904182cea49c9dce2c77187aab8494b34cd` | Distinct support at that late-tail scope. |

The complete derivative alternative was also read, with a truncated aggregate display repaired by a bounded re-read: `common_product_narrow_cutoff_derivative/PROPOSAL.md`, 15964 bytes, `550946fdebc4e68522c997ed914e23a8baf40cb660dfc22e4f09e00add1216a3`, and its `_check/REVIEW.md`, 14861 bytes, `6a4866e76cc5c6c760284c9a3f6c07c71410f701d727e8765edc8f6a57d328a4`. Its absolute G2 derivative ceiling and old finite resource substitutions are not load-bearing in (10)--(29). The pole estimates avoid that unnecessary sufficient cost; no earlier frozen proof is changed.

The following complete motivation pairs were read, with no global realization or finite theorem imported from them:

| Source | Bytes | SHA256 |
|---|---:|---|
| `exact_two_body_gate_diamond/PROPOSAL.md` | 5208 | `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33` |
| `exact_two_body_gate_diamond_check/REVIEW.md` | 12143 | `da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945` |
| `exact_two_body_gate_matched_extension/PROPOSAL.md` | 5733 | `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e` |
| `exact_two_body_gate_matched_extension_check/REVIEW.md` | 10895 | `36a1f3585c9ddde455078c72e7f48dc2b2cd8bfd1165026f4d3f60c6dbc6c77f` |

ROOT proposed examining a direct scalar source-to-cap proof and subsequently suggested the already checked late pole interfaces. This author had written earlier direct-loader finite and record analyses and had seen campaign source/check results. This is new source-exposed author work using the same model and effort, not independent validation of those ancestors. The scalar proof deliberately does not use their finite theorem, contact estimate, runtime exponent, flag claim, apparatus counts or global data gauge. A later ROOT message reports a separately checked global composition; that reported result is not a load-bearing premise here, and its source/review were not audited in this scalar task. Equation (30) states exactly the separate identity needed for any transfer.

The new obligations for a distinct check are the normalized filtered state (8),(9); the two favorable signs and fixed-diagonal cut over the entire interval (12)--(15); the exact endpoints/gaps in (18)--(23); the full-state normalization argument (24),(25), including its square-root incoming cost; and all simultaneous maxima, counts, loads, phases and asymptotics in (27)--(29). The available component checks do not independently check this new composition, and no such check is claimed already complete.

Applicable previously read instructions were refreshed by hash and are unchanged: W/AGENTS.md, 1118 bytes, `febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0`; W/docs/ai_methodology/SCIENCE_WORKFLOW.md, 11788 bytes, `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`, where W is the shared correlation_worktree. Their bounded derivation/source-exposure requirements are reused; no instruction or editable prompt file was changed.

Work was analytical. Commands actually used were bounded `cat`/`sed` source reads, `rg` source-location searches, Python `pathlib`/`hashlib` byte/line/hash inventory, and `apply_patch` to write this one proposal incrementally. The saved proposal was then read and its final bytes hashed. There was no scientific executable, numerical evolution, matrix solver, parameter sweep, external search, delegation, W/Git/checkpoint/axiom/model change or publication. Metadata checks establish identity and read coverage, not the correctness of the theorem. Only `exact_uniform_chain_finite_launch/PROPOSAL.md` was created for this task. The new result remains a conditional author derivation awaiting distinct review; no retained or audit status is assigned.


