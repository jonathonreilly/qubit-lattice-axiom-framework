# Pre-exposure reconstruction: original gain and finite-register limit

Frozen before opening root's WORKING_PROOF fb35eaca. This is a focused analytic check, not a formal review. Exposure is substantial and explicit: I authored the previously checked field, gain and register lemmas, checked the time-compactness argument, and supplied root with the elementary normalized-spin shift inequality below. I have read the new CONTRACT b654610e, SOURCE_BINDINGS ad7b2d00, and the complete independent gain/register receipts ae43d702/6d4e46c8. I have not read the new proof or its results. This is a reconstruction of the composition and its delicate carrier/limit steps, not a blind discovery of the inputs. No computation is needed or claimed.

Actual source: the unchanged supplied compensated microscopic spin law, original resolved/coherent mark families separately, bare Omega, Gauss sector, positive fixed K,delta,kappa, epsilon²S(S+1)=delta/K and safe growing tori. Current main fb5da8dd and selected procedures7146. No effective process is substituted.

## 1. Compatible local subsequences must keep the register specification fixed

Fix monitored F, bins, cap and horizon once. Choose an increasing countable exhaustion of finite quantum regions containing F and all needed mark supports. Apply the checked local time compactness successively and diagonalize. Every finite-region state then converges uniformly on[0,T] in the common rotor-field trace-class carrier. Their partial traces agree because the original finite-spin states agree, local spin embeddings commute with the relevant partial traces, and partial trace is trace-norm contractive. This defines a projectively consistent family of local normal states with ONE common classical register, not a globally trace-class infinite-volume density operator.

It is not valid to assert arbitrary consistency between different monitored/capped registers: a word already overflowed at a larger monitored set need not determine the smaller set's unoverflowed word. Only actually existing fixed coarse-graining maps pass automatically. The target sensibly fixes the register specification. Local occupied-A support passes from vanishing hole probability. If Gauss support is claimed, its finite-star diagonal constraint projector is bounded and can be tested on a region containing that star; exact spin-basis embeddings preserve it, so local trace convergence preserves expectation one.

## 2. Exact normalized-spin shift estimate, including the wall

Let P_S be the link spin box in the rotor basis and U_s the rotor shift by s=+/-1. For integer |m|<=S the normalized spin shift has amplitude

    g_S(m,s)=sqrt(1-m(m+s)/[S(S+1)]).

The outward wall amplitude is exactly zero; the rotor comparison still shifts to m+s outside the spin box. Integer m gives 0<=m(m+s)/[S(S+1)]<=1 and

    (1-g_S(m,s))² <=m(m+s)/[S(S+1)]<=|m|/S.

Therefore, as a form on input spin-box vectors,

    [(U_(S,s)-U_s)P_S]*[(U_(S,s)-U_s)P_S]
                                             <=P_S |E|P_S/S.

A literal zero extension of a whole local spin word may also put box projectors on its spectator links. On the actual embedded input state they are identity; its action agrees with the word made from zero-extended spin shifts. They must not be silently compared in operator norm on arbitrary out-of-box rotor input.

For a finite physical source word use telescoping with ROTOR factors on the left of the differing shift and SPIN factors on its right. Each difference then acts on an intermediate vector still in the spin box, where the preceding inequality applies. The left factors have uniformly bounded norms. The right spin factors change fields by only a bounded number and have bounded coefficients, so their first-field quadratic forms are bounded by C(1+sum |E|) on the original input. The finite sum over actual hard-core source words and coherent signs only costs a finite Cauchy/path factor, not an observed channel split. In particular Bhat_S=j_S F_S has, on actual spin-box input,

    (Bhat_S-Bhat_infinity)*(Bhat_S-Bhat_infinity)
                            <=(C/S)(1+sum_(finite support)|E_e|).

This is a state-weighted statement with a bounded actual rotor word, not uniform operator-norm convergence. The actual first moment makes its expectation O(1/S), uniformly in time and volume. The full original coherent mark normalization is retained.

## 3. Strong gain-current limit in a fixed common carrier

On an enlarged finite region Y containing output X and the chosen mark's word support, let eta_j(t) converge uniformly in trace norm to eta(t), with the fixed register attached. All Bhat words are uniformly bounded. The preceding squared estimate and Hilbert-Schmidt Holder give

    sup_t ||Bhat_S eta_j Bhat_S* - Bhat_infinity eta_j Bhat_infinity*||_1
                                                           <=C_T/sqrt(S).

Next, bounded multiplication makes the rotor sandwich continuous in trace norm:

    ||Bhat_infinity(eta_j-eta)Bhat_infinity*||_1
                                         <=C||eta_j-eta||_1.

The checked microscopic gain theorem supplies the remaining difference between L_j eta_j L_j* and kappa Bhat_S eta_j Bhat_S* in L1 time at O(epsilon). Thus

 integral_0^T ||actual original gain_j - rotor-word gain on eta||_1 dt
 <=C_T epsilon+C_T/sqrt(S)+C_T sup_t||eta_j(t)-eta(t)||_1 ->0.

Appending the same actual original history label and partially tracing extra quantum factors are fixed CP trace-norm contractions. They therefore commute with this limit. Bin-dependent appends are piecewise fixed in time; their finitely many boundaries have measure zero and do not produce deterministic state jumps. Overflow does not stop the quantum source. Direct sum over a finite set of original labels gives the same convergence for the labelled gain current. This is a positive unnormalized event-flux measure, not a trace-one history law or a whole-process convergence statement.

## 4. Exact finite-register balance in the limit

The independently checked finite-register identity uses the SAME joint state and has vanishing error. Its positive source measures are

    nu_(mu,j)(z,t)=Tr[Bhat_(mu,S) eta_(j,z)(t) Bhat_(mu,S)*].

The gain convergence above (or its bounded-word portion) gives their ell1 convergence in L1 time. Register marginals converge uniformly in time. The finite original append maps and subtraction of the identity are bounded, so the approximate vector balance passes to the exact identity

    tau(t)-tau(0)=kappa integral_0^t sum_mu
                                 (append_(mu,s)*-I)nu_mu(s)ds,
    nu_mu(z,s)=Tr[Bhat_(mu,infinity)eta_z(s)Bhat_(mu,infinity)*].

The statement holds for all t by uniform convergence and integral convergence. The limiting register is absolutely continuous (indeed a bounded total source norm gives a Lipschitz envelope), but its source is correlated with an unidentified joint quantum trajectory. This is not a closed classical Markov law, uniqueness theorem or a proof of its quantum generator.

## Comparison risks

- Common-carrier source words must be extended and telescoped without applying an in-box amplitude inequality to an out-of-box intermediate rotor vector.
- Field moments apply to the actual quantum marginal; no conditional moment is required after attaching records.
- The growing-volume subsequence must include every finite word support, and compatibility is at a fixed register specification.
- Trace-class convergence of event flux is L1 in physical time, not automatic full timestamp/history total variation or no-event convergence.
- True signs, original mark labels, charge/Gauss maps and overflow behavior must survive every comparison.
- No quadratic-energy uniform integrability, fast Hamiltonian/loss closure, W1, boundary independence, new native carrier or primitive selection follows.
