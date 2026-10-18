# Complete finite resonant launch from endpoint seeds

Status: selectively checked conditional finite-source theorem; unaudited. Supplied-device mathematics, not a native implementation.

This result isolates the source stage of the [biased finite operation](COMMON_PRODUCT_BIASED_OPERATION_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9719 at `f0bd96dbe873e9fcab215dca22e6e1e3654df434`. It derives a phase-fixed complete launch window and finite source size directly from the endpoint seed. It does not replace the router's time or preparation bounds: its outgoing target, graph and boundary estimates differ.

## Physical device and supplied state

For j>0 and 0<gamma<j, use an emitter s and lead sites0,...,M along a nearest-neighbor line. The listed positive blocks are

    B=Q_gamma(s,0)+(2j-gamma)n_s+(j-gamma)n_0,
    Q_j(n,n+1), n=0,...,M-1,
    j n_M.

Here Q_c=c(n_x+n_y-a_x* a_y-a_y* a_x), including its double-occupation diagonal2c. The combined B has full norm3j. Every one-head diagonal is2j, including the capped endpoint. There are M+2 qubits and M+2 listed blocks. Incident full-support norm loads are3j at the emitter,5j at site0,4j at interior sites and3j at the end. Thus j<=Lambda/5 suffices under this explicitly stated combined-block convention.

Supply the emitter occupied and every other head vacant. Two identical disjoint copies allow arbitrary coherent path input and passive program/reference systems. The coherence is supplied; a superposition of the two occupied emitters is not a sitewise product state. The unused copy remains in its zero-energy vacuum. No outgoing spectral packet is physically prepared.

## Exact source and paid geometric comparison

The inherited checked half-line source measure gives the complete state as emitter amplitude plus outgoing and incoming lead integrals. With rho=gamma/j,

    E(k)=2j(1-cos k),
    F(k)=-i sqrt(2/pi)rho exp(ik)/[(2-rho^2)cot k-i rho^2],
    exp(-itH)|s>=A(t)|s>+O_t F+I_t conjugate(F).

The physical F has norm1 on0<k<pi; the two lead terms interfere. For0<rho<=1/2 the [survival estimate](../outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/PROPOSAL.md) gives

    |A(t)|<=exp[-j rho^2 |t|/sqrt(1-rho^2)]+4rho^2/3.

The band-edge remainder is retained. This is not pure exponential decay.

Let a=sqrt(1-rho^2). The [geometric comparison](../outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/PROPOSAL.md) compares the zero-extended physical F with the separately normalized full-circle profile U=i rho/[sqrt(2pi)(1+i a exp(ik))]. Their distance is at most29rho/8. In contrast, the full-circle rational continuation of F has squared norm2 and is not a valid normalized replacement; that failed shortcut remains explicit.

The inverse Fourier coefficients of U are u_n=i rho(-ia)^(-n) for n<=0 and zero otherwise. For m(t)=floor(2jt+1/2), its phased translated comparison is

    G_n(t)=exp(-i2jt)exp(im(t)pi/2)u_(n-m(t)).

Exact free evolution of U differs from G by at most rho+2rho(j|t|)^(1/6). This pays dispersion and rounding; it is not rigid propagation. The incoming physical term is conjugate to the outgoing free profile at negative time. For t>1/(4j), G(-t) has no support on the physical nonnegative lead. This bounds the full incoming remainder as well as the outgoing comparison error.

## Complete uniform window

For0<epsilon<=1 define

    L=log(32/epsilon), rho=(epsilon/64)^(3/2)L^(-1/4),
    gamma=rho j, u0=rho^-2 L=(64/epsilon)^3 L^(3/2),
    t_minus=u0/j, T=2u0/j.

Throughout this closed interval, the emitter allowance is at most33epsilon/1024. The sum of incoming and outgoing profile allowances is at most181epsilon/2048. The entire seeded vector therefore differs from P_(n>=0)G(t), with zero emitter coordinate, by less than epsilon/8. Positive normalization costs at most the same error, giving complete half-line vector error below epsilon/4. This [composition](../outputs/common_product_resonant_launch_2026_10_18/source_checks/window/PROPOSAL.md) includes both lead terms and the emitter; it is not a marginal or postselected statement.

The common normalized comparison is explicitly

    beta_n(t)=exp(-i2jt)exp(im pi/2)i rho(-ia)^(m-n)
                   /sqrt(1-a^(2(m+1))), 0<=n<=m,
    beta_n(t)=0 otherwise.

Its normalization is positive real. The diagonal phase, rounding phase and factor i are fixed. The integer center may jump; no physical Hamiltonian or control changes then. A separately supplied common scalar cI would require the additional exp(-ict) on the entire comparison.

## Finite transfer and costs

Choose

    d=ceil(max{2,8e jT,log(8jT/epsilon)}), M=d-1.

The [finite transfer](../outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/PROPOSAL.md) compares the actual device with the half-line by removing only the M,M+1 hopping. The physical cap j n_M preserves diagonal2j; the decoupled comparison exterior has its matching endpoint onsite. A Laplacian bond deletion without these diagonal corrections would be a different operator.

The centered half-line hopping operator has norm<=2j. Its powers of degree below d cannot reach lead sites n>=M from the emitter. The whole far-projection norm is therefore bounded by R_d(2jt)=sum_(p>=d)(2jt)^p/p!. It includes both boundary coordinates. Duhamel gives full finite/infinite vector error at most jT R_d(2jT). The stated d makes this at most epsilon/8 throughout[0,T], using R_d(2jT)<=exp(-d). No number-of-sites factor or infinite-many-head operator is used.

On the launch family, m(t)<=M, so beta already belongs to the finite device. No additional truncation normalization is needed. Consequently the complete finite vector error is below3epsilon/8 on[t_minus,T]. The probability of an empty emitter and a head in the target support exceeds1-9epsilon^2/64. For two identical copies, orthogonal path sectors give the same operator bound with arbitrary passive references, without a path-count factor. The unhalved complete output-channel/diamond discrepancy is below3epsilon/4. Every physical emitter and lead site remains in the output.

The sufficient family has

    size=Theta(epsilon^-3 [log(1/epsilon)]^(3/2)),
    T=Theta(j^-1 epsilon^-3 [log(1/epsilon)]^(3/2)).

The exact formula uses log(32/epsilon) and large constants. These are sufficient costs, not lower bounds, optimality or practical estimates. Setting j=Lambda/5 gives the stated incident cap. Gamma's magnitude is not a coefficient-tolerance guarantee. The observation window has relative width1; no measurement mechanism is supplied.

## Cutoff, scope and checks

A later compact central-band requirement must be paid separately. For real0<=chi<=1, p=||chi F||² and g=chi F/sqrt(p), the exact normalized spectral distance is at most sqrt(2(1-sqrt(p))). The window source states a sufficient hard-band condition for this cost. Such an outgoing cutoff target generally has infinite spatial support; the finite geometric target's compact-support argument cannot be reused without a new tail estimate.

The finite construction does not route a gate, write a record, implement cooling/loading/readout, derive native blocks or identify physical Record. Seed vacancy, input coherence, exact compensated coefficients, occupation bases and absence of other couplings remain premises. Later reflections and recurrences are uncontrolled. No permanent halt, capture, reset/reuse or old literal processor transfer follows. Sharper incoming/outgoing boundary research is not a premise of this publication.

Source and distinct-check files are preserved with hashes and exposure in the packet manifest. Checks are same-model and source-exposed, with shared upstream ancestry and ROOT's design suggestions; they are not blind replication, experiments or retained audit. Historical pending labels in frozen arguments record drafting chronology and must be resolved only by the named scoped reviews. Mechanical provenance/link/graph validation is separate from the analytical checks. No physical axioms or editable prompts change.

Scoped reviews: [survival](../outputs/common_product_resonant_launch_2026_10_18/source_checks/survival/REVIEW.md), [geometric profile](../outputs/common_product_resonant_launch_2026_10_18/source_checks/geometric/REVIEW.md), [complete window](../outputs/common_product_resonant_launch_2026_10_18/source_checks/window/REVIEW.md), and [finite transfer](../outputs/common_product_resonant_launch_2026_10_18/source_checks/finite/REVIEW.md).
