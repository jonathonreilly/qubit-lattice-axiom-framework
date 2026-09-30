# Independent precomparison reconstruction: original continuous histories

This PRE is frozen before opening WORKING_PROOF.md or CAUSAL_CURRENT_EXTENSION.md in the new author route. Exposure: the parent disclosed the target, titles, hashes and proposed count-UI/two-grid/trace-class/causal-current mechanisms. I read both contracts. I authored the older defect, first-field and gain components and independently checked the older trajectory and rotor-limit components; I am not blind to those inputs. I also composed the just-reviewed microscopic-output milestone. That unit remains unchanged; this check is separate and confers no formal review/audit grade.

The actual current compensation/formation definitions and the prior component proofs are reused at their frozen hashes. I freshly read the entire main LOCAL_BACKGROUND_AND_UNRESTRICTED_ORIGINAL_RECORD_COUNTS note, including its fixed-graph finite-grid/mesh order. That prior neither supplies a common-time microscopic conditional-intensity bound nor substitutes an effective state here. No new computation is needed or performed. The two new candidate proofs, code, numerical results and conclusion text have not been read.

## 1. Exact consumer and notation

Keep the finite-spin compensated law from bare Omega, all later and unmonitored births, fixed positive K,delta,kappa, epsilon^2 S(S+1)=delta/K, and arbitrary safe growing even tori. Fix a finite original mark alphabet I and a finite horizon T. Resolved and original unnormalized coherent instruments are separate choices. A_mu=sqrt(kappa) epsilon^-1 j_S,mu and B_S,mu=sqrt(kappa) j_S,mu F_S,a are the actual words. Put beta_mu=sup_S ||B_S,mu||^2 and Lambda=sum_I beta_mu, finite independently of volume and spin.

The checked amplitude/gain input gives, for each original mark and any extension with the actual physical marginal,

 integral_0^T ||A_mu eta_s A_mu* - B_S,mu eta_s B_S,mu*||_1 ds <=alpha_epsilon,mu,
 alpha_epsilon=sum_I alpha_epsilon,mu <=C_I,T epsilon ->0.       (P1)

The constant is independent of classical register cardinality/cap/partition. This is a gain measure estimate, not an actual pointwise conditional-intensity bound. The exact microscopic ensemble is used on both sides. The first-field input gives sup_s sum_(e in X) E|E_e|<=C_X,T for fixed X. All constants here may depend on I,T and fixed local geometry. Nothing is uniform in an increasing monitored set or horizon.

## 2. Extending the gain estimate without a fictitious diagonal density

At each fixed epsilon and finite volume the Hilbert space is finite dimensional and the exact GKSL jump construction is nonexplosive: all Hamiltonian and jump norms are finite. Its chronological original-mark instrument defines a positive matrix-valued measure M_s(dh) on observed PAST histories h before s, with trace p_s and physical marginal rho(s). This can be constructed directly by the convergent finite-volume Kraus/Dyson jump expansion and summing unobserved events. Original coherent marks stay whole operators.

Use its finite-dimensional Radon-Nikodym density M_s(dh)=sigma_s(h) p_s(dh), with sigma positive and trace one almost everywhere. No trace-class diagonal multiplication operator on nonatomic L2 is introduced. The elementary gain factorization at each h gives

 ||A sigma A* - B sigma B*||_1
 <=||(A-B)sigma^(1/2)||_2 (||A sigma^(1/2)||_2+||B sigma^(1/2)||_2).

Integrating in (s,h), time/measure Cauchy bounds the first squared factor solely through rho(s). This reproduces P1 for the trace-class variation norm of the continuous-past current measure. The other factors are the actual total activity and bounded B activity. This direct disintegration proof is my chosen route; alternatively finite causal partitions followed by a monotone-class argument must pay the error only once, not once per bin or cap value.

Consequently, for every bounded nonnegative predictable original-history test 0<=f_mu<=1,

 E integral sum_mu f_mu(s,H_(s-)) dN_mu(s)
 <= sum_mu beta_mu integral_0^T E f_mu(s,H_(s-)) ds +alpha_epsilon. (P2)

Signed tests have the corresponding absolute error against B in the SAME history/system measure. This is not obtained by dividing by a rare-history probability. Measurable disintegration in both variables can first be taken for the positive finite measure ds M_s(dh); finite dimension makes the entrywise construction explicit.

## 3. Count tails and uniform integrability

Let N count all monitored original marks. From P2 with f=1,

 E N_T <=Lambda T+alpha_epsilon=:C_epsilon.                    (P3)

With the single predictable test f(s,h)=1_{N(h)>=R}, the exact counting identity is

 E(N_T-R)_+ <=Lambda integral_0^T P(N_(s-)>=R) ds+alpha_epsilon
             <=Lambda T C_epsilon/R+alpha_epsilon.            (P4)

No count second moment or Poisson law is assumed. Since n 1_{n>2R}<=2(n-R)_+,

 limsup_(epsilon->0) E[N_T 1_{N_T>2R}] <=2(Lambda T)^2/R.       (P5)

Thus each joint spin/volume sequence with epsilon->0 is uniformly integrable after adding finitely many initial members; those finite-volume members have integrable counts. A fixed epsilon error must not be silently set to zero before taking the limit. This argument proves first-moment UI, not a microscopic second-moment bound or factorial domination. Total occupancy is preserved by the Hamiltonian and increased by two per birth, but no monotonicity of the B-only number is required.

## 4. Coincidences and endpoint mass: a different counting bound

Choose the predictable lookback test

 f_r(s,h)=1_{there is a monitored time u in h with s-r<=u<s}.

The prehistory version is predictable; using left limits at s-r avoids a convention issue. Pathwise, the Lebesgue measure of times with this flag on is at most r N_T. Every event that has a preceding event less than r earlier is counted by integral f_r dN. Therefore P2 gives the direct bound

 P(exists two monitored events with positive separation <r)
 <=E integral f_r dN <=Lambda r E N_T+alpha_epsilon.           (P6)

This avoids a summed per-window error entirely. For a proof restricted to finite encodings, one can dominate this flag by overlapping-bin flags: use two grids of width 2r, shifted by r. A pair closer than r lies together in at least one grid cell. For each grid the repeat-event flag occupies at most 2r N_T time; the two tests then cost at most 4Lambda r E N_T+2alpha_epsilon. Exact grid endpoints can be assigned consistently and deterministic endpoint events have zero finite-volume probability. Both approaches suffice; the direct lookback estimate is sharper but needs the continuous-past measure argument above.

Likewise for any deterministic time interval J,

 E N(J)<=Lambda |J|+alpha_epsilon.                             (P7)

This excludes limiting atoms at 0,T or any fixed time, by neighborhoods and the order epsilon->0 then neighborhood length->0. It does not bound the actual microscopic conditional hazard.

## 5. Classical event-list topology

Use the disjoint union over finite m of the finite label words with strictly ordered times 0<t_1<...<t_m<T, with Euclidean time topology on each fixed word. This is a separable complete-metrizable locally compact space after a compatible metric choice. Compact sets can require m<=M, endpoint distances>=r and neighboring times separated by>=r. P3, P6 and P7 bound their complements by C/M+C' r+o_epsilon(1). Hence classical path laws are tight. Subsequential limits are finite simple original-mark point processes, with no fixed-time atoms. This event-alignment topology agrees with the usual jump-time alignment for such finite counting paths; no timestamp total variation is claimed.

The conclusions hold along arbitrary joint volumes/spins after subsequence extraction. UI in P5 passes first-count integrals for bounded continuous event functions after truncation. It does not establish an autonomous effective law or uniqueness.

## 6. Positive trace-class history measures at fixed observation times

At observation time t, use only the actual history through t and the quantum output at t; full future histories together with an earlier undisturbed quantum state are not automatically positive physical outputs. In particular no joint quantum intervention process at several times is inferred.

For a fixed local quantum region X, its positive trace-class-valued history measure has trace equal to the classical observed-history law. Let P_R be a finite field/matter projection. The first-field moment and gentle projection give

 ||M_epsilon,X-P_R M_epsilon,X P_R||_(variation,T1)
 <=2 sqrt(Tr[(I-P_R)rho_epsilon,X(t)]) <=C_X,T R^(-1/2).        (P8)

Here integration over conditional histories uses Cauchy; no conditional field bound is assumed. On a compact history set, each finite-matrix entry is a tight finite complex measure dominated in variation by the trace law. A finite-dimensional weak-measure extraction, then diagonal extraction in R and X, gives a positive T1-valued countably additive limit. For each bounded continuous scalar f on event histories, the integral of f against the matrix measure converges in trace norm. Tail P8 prevents loss of quantum trace and supplies local normality.

An explicit density construction avoids invoking a Banach-valued Radon-Nikodym theorem without checking it: take scalar limiting trace measure p, finite-matrix densities sigma_R relative to p, consistent under compression. Positivity and the vanishing total trace tail imply a positive trace-one infinite matrix almost everywhere. Finite-rank compression converges in T1, giving a measurable T1 density sigma_X(h). Partial traces and local Gauss projections pass through finite-rank/weak limits, so a countable local-region exhaustion gives compatible normal state measures. Countable observation times may be extracted together, but this alone does not create a multitime quantum process.

## 7. Causal time-averaged state and current measures

Define Q_epsilon,X(ds,dh)=ds M_epsilon,X,s(dh) for h=H_(s-). Its trace has total mass T. If full classical event-list laws tend to P, the restriction map (s,whole history)->(s,past before s) is continuous except when s equals an event time. For ds times any finite-list law that exceptional set has zero measure. Thus its scalar limit is

 q(ds,dh)=ds P(H_(s-) in dh).                                 (P9)

The integrated field bound gives P8 for Q as well. The same finite-cut extraction produces compatible local positive T1 measures Q_X with trace q. Disintegrating by finite matrices supplies sigma_X(s,h), positive trace one for q-almost every (s,h), compatible on a single common full-measure set for countably many X. This is conditioning on actual PAST history only. If simultaneous uniform-time unconditional limits are also extracted, integrating away h recovers those marginals almost everywhere in s.

The exact pre-append gain current is A_mu Q_epsilon A_mu*. P1 controls its total T1-variation error from B_S,mu Q_epsilon B_S,mu*. The already checked common-carrier word inequality

 (B_S-B_infinity)*(B_S-B_infinity)
 <=(C/S)(1+sum_source |E|)

gives an integrated gain replacement error O(S^(-1/2)) through the first moment. B_infinity is bounded and local. Consequently the weak T1 measure limit is

 J_mu(ds,dh)=B_infinity,mu Q_(Xprime)(ds,dh) B_infinity,mu*,    (P10)

followed by the declared partial trace for output X. This identifies an original marked CURRENT; no independent effective state has been introduced. Exact marked append is continuous on separated histories when the prefix times are strictly before s. Its possible discontinuity set has q measure zero; J is dominated in trace by beta_mu q. Therefore the same weak statement passes to post-append histories, with the unchanged original mark labels and coherent payload.

## 8. Causal intensity identification needs an actual Campbell passage

For bounded continuous f(s,past,mu), the finite-volume exact counting identity is the trace of the pre-event gain measure. The corresponding event-list functional sum_i f(t_i,h_<t_i,mu_i) is continuous on each separated fixed-word stratum and bounded by ||f|| N_T. Classical weak convergence plus P5 therefore passes its expectation. Combining this with P10 yields

 E_P sum_i f(t_i,H_(t_i-),mu_i)
 =sum_mu integral f(s,h,mu) Tr[B_infinity,mu*B_infinity,mu
                                      sigma_(source)(s,h)] q(ds,dh). (P11)

Equality of the finite Radon Campbell measures extends this to bounded measurable predictable tests. The coefficients lambda_mu(s,h)=Tr(B*B sigma) have a Borel version on causal histories, hence lambda_mu(s,H_(s-)) is predictable up to completion, and 0<=lambda_mu<=beta_mu. Thus N_mu minus its integrated lambda is a martingale for the observed-history filtration. This conclusion concerns a subsequential limit and a conditional local quantum state defined only q-almost everywhere. It supplies neither a finite-epsilon hazard approximation nor a closed or unique quantum filter. A proof using future-history-conditioned states in P11 would be invalid without an additional construction.

## 9. Comparison checklist and independence limits

Before adopting either candidate I will check: one global error rather than error per bin; both orders of the UI limit; all-grid cross-boundary pairs; the actual event-list topology; positive countably additive trace-class measures rather than nonatomic diagonal density operators; complete source support and zero-extended spin words; compatible scalar disintegration for all local regions; causal prehistory restriction; Campbell convergence via UI; original coherent labels; and explicit exclusions of full generator, energy/W1, conditional microscopic hazards and quantum multitime interventions. No target theorem is inferred merely from mean tightness or from a finite register limit.

This PRE independently supports a plausible proof route at the stated supplied-law scope. It is not yet a comparison verdict on either candidate, which remains unread at this freeze. No numerical controls or resource claims are fabricated.
