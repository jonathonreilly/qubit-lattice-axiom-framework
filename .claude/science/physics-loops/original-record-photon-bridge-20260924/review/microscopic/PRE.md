# Blind PRE: first-and-next original marked record in finite time windows

Independent bounded milestone check, 2026-09-24. No root candidate or active readout/checker packet was read before this report and its evidence were sealed. Earlier independent packets are unchanged. This report uses the explicitly supplied compensated microscopic law and the pinned parent theorems conditionally; it does not adopt a new axiom, construct a detector or apparatus, or apply a publication/audit verdict.

**Conclusion.** The two pinned statements, including their finite classical register extensions, suffice for convergence of the specified **joint recorded event probability**, for a fixed bounded interval, fixed positive lag, fixed finite graph/couplings, and trace-norm convergent physical initial preparations. The proof uses a finite time-bin register and inner/outer event brackets, then removes the bins using bounded target jump intensities. It does not require a uniform microscopic intensity bound or a limit of states conditioned on an exact jump time.

For an independently supplied positive contrast scale `r_n -> 0`, the resulting fixed-instance convergence permits a chosen diagonal microscopic approximation with error `o(r_n)`. It supplies no accuracy or resource guarantee for an arbitrary simultaneous schedule. A separately labeled six-state abstract-parent-class example below shows that a shrinking-window schedule can lose the entire relative contrast even while its absolute error vanishes.

## 1. Exact sources and the statement being checked

Both complete source arguments were read from exact git bytes at main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8` in `/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/campaign-working`:

| Source under `docs/` | SHA256 |
|---|---|
| `BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9` |
| `LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md` | `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b` |

`SOURCE_PINS.json` binds these snapshots and the unchanged applicable instructions. The repository AGENTS pointer and science workflow hashes are respectively `9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6` and `d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`. The already-read standing execution instructions at revision `eb1f1ca8338848cf2046582e13aef372d8540937` have unchanged SHA256 `b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7`. No parent numerical runner or author builder was imported or rerun.

The first parent supplies a uniform-in-S `O(epsilon)` trace-norm comparison of the actual bare microscopic density with its compensated spin target on each fixed finite time interval, from every P-supported density. Its hypotheses include the bounded T, C and original formation operators, the penalty selection rules, and the compensation acting trivially on any added register. It explicitly extends the argument to finite classical event/count registers with the stated conservation properties.

The second parent supplies the common full physical rotor generator

    L rho = -i[h,rho] + sum_j (J_j rho - {L_j* L_j,rho}/2),
    h = K D + delta H4_infinity^C,
    L_j = sqrt(kappa) B_j,
    J_j rho = L_j rho L_j*,
    B_j = -P j Pi_1 T P.                              (1)

Here D is the full matter-dependent electric multiplication operator and H4 is the bounded full compensated rotor coefficient. There is no replacement by an initial-sector field Hamiltonian. This parent proves the strong trace-class spin-target limit, uniformly on compact time intervals for each fixed trace-class input, and states the same finite event/count-register extension. It then combines that limit with the uniform-in-S microscopic comparison at

    epsilon_S^2 S(S+1) = delta/K,                     (2)

with K, delta, kappa positive and fixed during that limit. The underlying fixed finite graph, Gauss sector, complete matter/field spaces and actual original channels are retained.

The precise readout claim here is as follows. Let `rho` be a normal physical P-supported rotor density and `rho_S` physical spin-box/P-supported trace-one densities embedded in the rotor space, with `||rho_S-rho||_1 -> 0`. Ordinary normalized physical cutoffs give such approximants once their nonzero mass is included. No high-field moment is assumed. Fix a bounded interval `I` with endpoints `0<=a<c<infinity`, fix `0<b<infinity`, and take a horizon `H=c+b`. Open/closed endpoint conventions will have the same probability.

Let `T_1<T_2` be the first two events of the supplied original instrument, and `M_1,M_2` their original marks. A missing event has time infinity. The event under comparison is

    E = {M_1=j, T_1 in I, M_2=l, 0<T_2-T_1<=b}.       (3)

These are the first two events overall, so no event precedes T_1 and none intervenes between T_1 and T_2. Later events are unrestricted. The claim is

    Pr_(micro,epsilon_S,S,rho_S)(E) -> Pr_(rotor,rho)(E). (4)

“Original mark” means exactly the channel in the given instrument. A coherent edge mark remains its prescribed sum of signed formation operators throughout; its internal signs are not separately measured, tagged, or treated as a resolved mixture.

An unbounded interval I is not covered by a single finite horizon. Extending (4) to such a window would require a separate tail/tightness argument. If instead “first j” means the first occurrence of mark j with other earlier marks allowed, the same finite-register method can use that different prefix automaton, but it is a different event from (3), with a different waiting kernel. The present formulas refer to (3).

## 2. Target boundedness and the exact joint-event kernel

The original mark set is finite on a fixed finite graph. All effective B_j and their adjoints are bounded. For example,

    ||B_j|| <= ||j|| ||T||,
    lambda_j := ||L_j||^2 = kappa ||B_j||^2,
    Gamma = sum_j L_j* L_j,
    ||Gamma|| <= Lambda := sum_j lambda_j < infinity. (5)

The same bounds hold uniformly in S for the spin targets, with an appropriate fixed finite bound. Coherent-channel norms may be bounded by the sum of the component norms, without changing the actual coherent operator or its normalization.

The target no-event contraction is well defined even though h is unbounded:

    V(t) = exp[t(-i h-Gamma/2)],
    T_t(rho) = V(t) rho V(t)*.                         (6)

This follows from self-adjointness of h and boundedness/positivity of Gamma. The maps T_t are strongly continuous, completely positive and trace nonincreasing. The jump maps J_j are bounded on trace class, with induced norm at most lambda_j. These facts give a nonexplosive marked jump expansion on every finite horizon; normalized conditional intensity is at most Lambda. They do not require differentiating rho under the unbounded Hamiltonian.

The exact probability in (3) is

    p(E) = integral_(s in I) ds integral_0^b du
                   Tr[J_l T_u J_j T_s(rho)].          (7)

T_s excludes an earlier event, J_j makes the actual first marked output, T_u excludes any intervening event while retaining the full postbirth dynamics, and J_l supplies the next original mark. After that, the full trace-preserving semigroup can act for `H-s-u`; its trace is unchanged, so it drops out of (7). There is deliberately no no-event factor after the second event. Replacing it by one would incorrectly require no later events.

For fixed rho the integrand is continuous in `(s,u)` by strong trace-class continuity of T and boundedness of the J maps. It is nonnegative and uniformly bounded by

    0 <= Tr[J_l T_u J_j T_s(rho)] <= lambda_j lambda_l. (8)

Consequently the marked first-two-time measure has a bounded density on `0<s<t<=H`, in coordinates `t=s+u`. In particular the lines `s=a`, `s=c`, and `t-s=b` have zero target probability. The positivity of b and width of I do not require a small-time expansion.

For each fixed microscopic parameter the microscopic generator also has a well-defined jump record. Its intensity bound is finite, but can be as large as

    kappa epsilon^(-2) sum_j ||j_S||^2.                (9)

It is not a uniform microscopic bound as epsilon tends to zero. The proof below never multiplies a vanishing bin width by (9) and presumes the product is small. Only the **target** bound (8) is used when bins are removed.

## 3. A finite classical monitor of the actual marks

Let the original mark alphabet have size m. A finite prefix register has states

    empty;  (first mark i);  (first mark i, second mark k),

so at most `1+m+m^2` states. Upon a physical mark j, the deterministic register update f_j writes the first mark if empty, writes the second mark if exactly one has occurred, and leaves a completed pair unchanged. This saturation freezes only the memory of the first pair. Every subsequent physical jump still occurs with its original operator and rate.

One exact classical implementation on the extended Hilbert space uses the microscopic channels

    j_(j,r),S = j_j,S tensor |f_j(r)><r|               (10)

for every classical register value r, with Hamiltonian and compensation tensored by the register identity. On block-diagonal classical-register densities these maps are exactly the original marked process with deterministic bookkeeping. Summing over r gives the original quantum marginal: in particular the extended loss is the physical loss tensored by I. Splitting by a known classical source state r does not split the internal coherent components of an original channel j.

Every lifted channel satisfies

    j_(j,r),S (P tensor I)=0,
    [W tensor I,j_(j,r),S]=-j_(j,r),S,
    ||j_(j,r),S||<=||j_j,S||.

T and C have the same fixed bounds, C acts trivially on the register and preserves the physical record number/Gauss constraint, and the number of register states/channels is finite. Thus these are within the stated finite-register extension of the first source. Its canonical Hamiltonian rotation is the physical rotation tensored by I. The effective channel is exactly

    B_(j,r),S = B_j,S tensor |f_j(r)><r|,              (11)

so the comparison attaches to the same original marked record. In the spin-to-rotor passage, strong convergence of B_j,S and their adjoints extends to these finite tensor factors, and the common `K D` interaction-picture argument is unchanged. The completed memory does not project away the physical state after the second event.

To record time bins, choose finitely many deterministic grid times partitioning `[0,H]` with mesh at most eta. At each endpoint, copy the classical prefix state into a fresh finite classical archive slot. This is a trace-preserving classical copy map acting identically on the physical system. The register is already classical, so this copies bookkeeping and does not perform a new measurement of an internal coherent mark. The archive and prefix together still have a finite state set for any fixed partition. From their final value one recovers the first mark, second mark, the bin of T_1 and the bin of T_2, including the case of two events in the same bin and the cases of zero/one event by H.

The time-bin construction is not an assumption of an autonomous physical clock or a measurement apparatus. It is a finite mathematical encoding of the prescribed event record. Equivalently one may use piecewise constant classical writing rules, with the same finite-composition argument below.

## 4. Why convergence survives the finite grid operations

Between archive updates, each extended evolution is precisely a finite-register semigroup covered by the parents. Archive-copy maps are CPTP contractions in trace norm and commute with the physical P embedding. At a fixed finite partition, insert the target evolution at each grid step and telescope the differences. The actual microscopic intermediate state need not be P-supported: its difference from the P-supported target is propagated contractively, while each fresh local comparison is applied to the target starting state, which is P-supported. The uniform initial-state microscopic bound in the first source is therefore sufficient.

For a fixed partition with finitely many intervals, the microscopic-to-spin-target error tends to zero under (2); a bound of the form `C_eta epsilon_S` suffices. No bound uniform as eta tends to zero is asserted. For the spin-target-to-rotor part, use the strong convergence for each fixed input plus contractivity at each step; a finite product of these convergent evolutions and the fixed archive-copy maps converges on the given input. The convergent initial approximants contribute their trace-norm error. Uniformity over every input is not needed for this second part.

Thus the final finite classical record distribution converges in total variation at every fixed partition. In particular, every bounded indicator of its value has a convergent expectation. The full extended density remains trace one throughout; no conditioning on a rare record is involved in this step.

The finite-copy argument supplies precisely what is needed beyond a one-time unregistered density comparison. A bare GKLS density does not generally determine a chosen unraveling or its recorded marks. The channels and finite-register extension in the given sources are load-bearing premises, not optional interpretations.

## 5. Remove the bins by a target continuity-set argument

Let `D_H={(s,t):0<s<t<=H}`. For each ordered pair of grid bins, intersect the bin rectangle with D_H; retain the original first/second marks in the register. Define a lower event E_eta^- by including the marked cells whose possible time pairs all obey (3), and an upper event E_eta^+ by including all marked cells that can intersect (3). Empty cells are ignored. On actual records,

    E_eta^- subset E subset E_eta^+.                  (12)

These are finite-register events. The bounds are pathwise for strictly ordered event times; at fixed microscopic parameters, deterministic endpoint ties have zero probability. The corresponding target ties also have zero probability by (8). There is no need to know the microscopic density at the target boundary.

A cell in the bracket difference must lie within eta of a first-time endpoint a or c, or within `2 eta` of the relative-lag boundary b. The range of s within a cell has length at most eta, and the range of `t-s` at most `2 eta`. A deliberately loose area estimate in the triangle D_H therefore gives

    p(E_eta^+)-p(E_eta^-)
       <= 8 lambda_j lambda_l H eta                  (13)

(and of course at most one). If a boundary is outside the triangle the bound only improves. Strict positivity of the lag is already part of D_H; simultaneous events carry no target mass. This argument covers cells containing both events and requires no timestamp register with a continuum of states.

Let `p_S` denote the actual microscopic law with (2) and rho_S. For each fixed eta, section 4 gives `p_S(E_eta^+/-) -> p(E_eta^+/-)`. Hence

    liminf_S p_S(E) >= p(E_eta^-),
    limsup_S p_S(E) <= p(E_eta^+).                     (14)

Now send eta to zero and use (13). Both bounds tend to p(E), proving (4).

The order is essential to this proof: fix the graph, preparation, positive couplings, I and b; fix a finite grid; take the admissible microscopic/spin limit; only then refine the grid. One can choose a sufficiently slow diagonal refinement after these steps, but a prescribed simultaneous refinement requires separate estimates. The strong rotor limit in the second source has no general quantitative rate over arbitrary preparations, so (13) plus the parent `O(epsilon)` statement does not by itself give a rate for the exact continuous-time event.

This proves a particular bounded event probability, not pointwise convergence of a two-jump density, normalized states conditioned on exact event times, total variation convergence of an entire continuously recorded path, or arbitrary continuously conditioned histories. It is fully consistent with the first parent's explicit warning about that broader scope.

If a conditional probability given a first-mark/window event is wanted instead, its denominator must have positive target probability. For a fixed such denominator, convergence of numerator and denominator gives the ratio. If denominators themselves shrink in a family, relative denominator control is an additional accuracy requirement. The joint event (3) needs no such positivity hypothesis.

## 6. Abstract shrinking contrasts and a selectable diagonal

Suppose that for each n a finite collection of experiments satisfying the preceding fixed-instance premises is supplied. Preparations, positive couplings, positive windows and lags may depend on n, but are frozen during the microscopic limit for that n. Each experiment has its own trace-norm convergent physical initial approximants. Suppose, for example, that the supplied target contrast is

    Delta_n = p_n^+ - p_n^-,       |Delta_n|=r_n>0,
    r_n -> 0.                                           (15)

No derivation of Delta_n, its sign, or its physical interpretation is supplied by this convergence argument. Let `alpha_n>0` be any chosen sequence tending to zero. For each n, fixed-instance convergence provides a sufficiently large admissible resource threshold so that both microscopic probability errors are at most `alpha_n r_n/2`. Choosing resources above those thresholds gives

    |Delta_n^micro-Delta_n| <= alpha_n r_n = o(r_n).    (16)

One may also require the chosen resource to exceed n and epsilon to be below `1/n`, since each fixed-instance limit permits arbitrarily large S and small epsilon subject to (2). When a comparison shares K, delta and the spin resource, take the maximum of the finitely many thresholds. If different arms require different microscopic scaling ratios, each must obey its own admissible relation; a common physical apparatus is not established by this abstract selection.

The construction can be made explicit in quantifier order: for row n first choose a bin mesh whose target bracket error is a small fraction of `alpha_n r_n`, using (13); next hold that finite register fixed and choose the microscopic/spin resources and initial approximation sufficiently accurately. The constants, number of bins, preparation tails, horizon and intensity bound may depend on n. The sources provide no modulus from which a generally sufficient explicit S_n or epsilon_n scaling can be read off.

The same argument works for any fixed finite linear contrast in the row, allocating an error budget using the sum of the absolute coefficients. If some r_n is zero, only an absolute-accuracy statement is available there. A relative statement requires a positive comparison scale.

Nothing in (16) establishes that an arbitrary supplied schedule `S_n -> infinity`, `epsilon_n -> 0` preserves the contrast. Even absolute error tending to zero does not imply an error smaller than r_n. Uniform control of moving preparations, varying couplings, growing horizons or shrinking windows is absent. Nor does the existence of a tailored diagonal give an economical resource cost, feasible preparation procedure, sufficient statistical sample size, or physical/observational identification of the contrast.

## 7. Separate six-state abstract-parent-class example

This is **not** the physical cube, the local link-compensation construction, or a rotor simulation. It is an independently specified finite operator model in the bounded parent class, used to check the finite-bin reasoning and demonstrate the logical limit of an arbitrary simultaneous schedule. No root builder or parent computation is reused.

Use basis `g_0,e_0,g_1,e_1,g_2,e_2`. Let

    W = sum_(k=0,1,2) |e_k><e_k|,
    P = sum_(k=0,1,2) |g_k><g_k|,
    T = sum_k (|g_k><e_k|+|e_k><g_k|),
    C = P,
    j = |g_1><e_0|+|g_2><e_1|,
    N = sum_k 2k (|g_k><g_k|+|e_k><e_k|).             (17)

All three norms `||T||,||C||,||j||` equal one. The exact identities are `jP=0`, `[W,j]=-j`, `[C,W]=0`, `[N,T]=[N,C]=0`, and `[N,j]=2j`. A trivial constraint operator may be taken if desired; this is not a reconstruction of the lattice Gauss law. With delta=1, the microscopic law is

    H_epsilon = epsilon^(-4)(W+epsilon T+epsilon^2 C),
    L_epsilon = sqrt(kappa) epsilon^(-1) j.            (18)

The first parent's coefficients are `M=C0=P`, `C1=0`, `Z=0`, `H2=H4=0`, and

    B = -|g_1><g_0|-|g_2><g_1|.                      (19)

Starting at g_0, the target waits exponentially at rate kappa for each of its first two jumps. Every microscopic jump also resets exactly to the next ground stage; the first two stages have the same two-by-two no-jump evolution. Later dynamics is unrestricted and cannot change the already recorded pair.

For `I=[0,w]` and lag `b=w`, the target event probability is

    p_kappa(w)=(1-exp(-kappa w))^2.                    (20)

Let F_epsilon,kappa(w) be the actual microscopic first-wait cumulative probability. The exact microscopic event probability is `F_epsilon,kappa(w)^2`, by the reset just described. In either of the first two no-jump stages write the amplitudes as a(t), z(t). The no-jump norm is at most one and

    z'(t) = -i epsilon^(-3) a(t)
             -(kappa/(2epsilon^2)+i epsilon^(-4)) z(t),
    z(0)=0.

Variation of constants gives `|z(t)|<=epsilon^(-3)t`. Thus the actual waiting density and cumulative probability obey

    f_epsilon,kappa(t)=kappa epsilon^(-2)|z(t)|^2
                       <= kappa epsilon^(-8)t^2,
    F_epsilon,kappa(w)<= kappa epsilon^(-8)w^3/3.      (21)

Choose a simultaneous schedule

    e_n=1/sqrt(n(n+1)),       epsilon_n=e_n,
    w_n=e_n^5,               I_n=[0,w_n], b_n=w_n,

and compare the two fixed positive couplings kappa=2 and kappa=1. Its target contrast is

    r_n = p_2(w_n)-p_1(w_n) ~ 3 e_n^10 > 0.          (22)

But (21) proves

    |Delta_n^micro| <= p_2^micro+p_1^micro
                      <= (5/9)e_n^14,
    |Delta_n^micro|/r_n -> 0.                         (23)

The relative contrast is therefore lost under this particular schedule, despite every window being strictly positive for each n and despite absolute errors vanishing. Holding n and its window fixed before sending epsilon to zero instead falls under the parent fixed-instance convergence. This is not a contradiction: the schedule in (23) keeps the observation windows inside the microscopic initial transient. The six-state family has uniform operator bounds and can be treated as constant in an abstract resource index; using `1/sqrt(n(n+1))` does not make it an actual spin-link model. The example does not assert that the physical cube fails at a particular proposed schedule. It shows why a general relative guarantee cannot be inferred merely from fixed-instance approximation statements.

## 8. Independent control, complete evidence, and limits

`abstract_record_control.py` constructs (17) directly. Standard-library integer/Fraction operations check all penalty/record selection rules, operator products and the exact zero Hamiltonian coefficients. No spectral fit or author builder is used. The script then uses 80-digit mpmath two-by-two no-jump exponentials to corroborate (20)-(23), and separately sums finite-bin cells for a target event with `I=[1/4,1/2]`, `b=1/4`. Its target first-two-time density is `kappa^2 exp(-kappa t)` in coordinates `(s,t)`, so the diagonal-bin and off-diagonal-bin masses are independently integrated before the geometric classifier is applied.

The finite-bin control brackets the exact probability `0.03810601638715...`. Increasing the number of bins from 6 to 96 decreases the bracket gap from `0.01677051337145...` to `0.001048157085716...`, within the deliberately loose bound (13). A separate fixed-width `w=1/4` contrast approaches its target in the displayed parameter rows. Along the shrinking-window schedule, the microscopic/target contrast ratio decreases from about `0.00275123` at n=2 to `6.42033e-9` at n=64; the analytic upper bounds from (21)-(23) are also checked.

The actual successful control run took `0.16453558299690485` seconds, exited zero, and produced empty stderr. The complete stdout equals `ABSTRACT_CONTROL_RESULTS.json`. The code SHA256 is `c2df3043cc82f1744a4dc1667ce9fb10588b0a04943c3eedd99a201b874c5ac7`; the result/stdout SHA256 is `a50a95e9444cb0ff80cfeaeaf3cfcfb8e865c1fd019f728a0106070251ef6c7c`. The complete code and all output rows were inspected. No failed execution or adverse result has been discarded. The unfavorable arbitrary-schedule behavior is a preserved result, not a harness failure.

The finite numerical rows are corroborative, not interval enclosures, a proof of a uniform numerical rate, or data from the physical cube. The analytic finite-register/continuity-set argument proves the fixed-window implication from the supplied parents; the analytic amplitude bound proves the abstract schedule counterexample. The explicit source/evidence correspondence record and immutable PRE seal bind all files. Work stops at this seal pending source release.
