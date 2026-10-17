# Fixed-q sparse conserving compilation with qualified finite fixture evidence

This source proposal packages a conditional compiler bound and one emitted circuit. The mathematical result has [qualified analytical acceptance](source/sparse_root_decision/QUALIFIED_ACCEPTANCE.json); the fixture now has its own [qualified evidence decision](source/fixture_root_decision/QUALIFIED_ACCEPTANCE.json). Neither decision is retained audit, empirical control identification, or publication approval. This new wrapper remains **UNBOUND**: its canonical parent, actual Git base, canonical binding, current wrapper review and publication are null.

The seven complete immutable bodies are directly recoverable through [BODY_RECOVERY_MAP.md](BODY_RECOVERY_MAP.md): the [derivation](source/sparse_author/DERIVATION.md), [analytical review](source/sparse_exposed_review/REVIEW.md), [sparse qualifications](source/sparse_root_decision/FINAL_QUALIFICATIONS.md), [runtime qualifications](source/control_parent_decision/FINAL_QUALIFICATIONS.md), [fixture report](source/emitted_fixture/REVIEW.md), [fixture review](source/fixture_exposed_review/REVIEW.md), and [fixture qualifications](source/fixture_root_decision/FINAL_QUALIFICATIONS.md). Those complete arguments and controlling qualifications govern the summary below. Earlier pending statements remain unchanged as historical records; the later decisions are additive.

## Conditional mathematical statement

Fix q>=1 and the actual old generator K_S=E0 I+Delta N_S, E0>=0, Delta>0, in a supplied physical computational basis. Use M=L+2q equal-gap battery qubits, L>=1, and one clean synthesis ancilla: n=L+3q data sites and m=n+1 total sites. The permissions are a connected path through every site; prescribed positive exchange, full physical adjacent SWAP and onsite phase controls; simultaneous final onsite access; a coherent ready packet; isolation and external timing. Strict-path XY+Z alone does not supply full SWAP. No generic interacting H or single accessible old port is covered.

For d=2^q and V in U(d), U_L(V) acts as V on each complete block

    span{|x> |1^(a-w(x)) 0^(M-a+w(x))>: x in {0,1}^q}, a=q,...,M,

and as identity on its entire orthogonal complement. There are (L+q+1)d selected basis vectors, not necessarily that many changed columns. All nonprefix states and the upper block are included. With J_A appending ancilla zero, an exact finite-real word C satisfies

    C J_A = J_A U_L(V).

Its scalar is one, the clean ancilla returns for every data input, and every output row is retained. The operator-isometry comparator extends to arbitrary data/reference correlations. The one-ancilla phase correction implements the determinant relative to the identity complement; it cannot be discarded as a global phase.

Let p=d(d-1)/2, T(1)=1 and T(k)=2T(floor(k/2))+2T(ceil(k/2)). In the forward A=exp[i pi(XX+YY)/8] and onsite Z(phi)=exp(i phi Z) alphabet, the accepted sufficient bounds are

    G0=(L+q+1){p[152T(n-2)+68(q-1)]+152T(n-1)},
    G <= Gbar=(2n-1)G0 <= K_q L^4,
    K_q=2(3q+1)(q+2){171(p+1)(3q+1)^2+68p(q-1)}.

The proof pays for inverse powers, split-control cancellation on all spectator sectors, logical pair-transport phases, determinant compensation, and full-SWAP routing. Chronological emission applies the residual diagonal first and then elimination adjoints in reverse order. These are fixed-q laboratory counts; p is exponential in q.

The synthesis parent is Bai–Marvian [arXiv:2309.11051v3](https://arxiv.org/pdf/2309.11051v3), saved with SHA256 `add4e97c6c0a1939d159924088c45481d54c2c54646d5cfebbbc7faa471154e8`. The source packets record necessary theorem, construction and strict-path passages; they do not claim revalidation of all 38 pages. The finite energy lift was already known and is not presented as a new result here.

For computable V with certified enclosures and positive requested error, the accepted finite-grid search uses strict operator-norm certificates for C J_A-J_A U_L(V), without fitted phase. Trace powers of E*E supply the needed upper bounds. This is termination of a finite-error supplier, not polynomial classical compilation time, memory, oracle latency or an exact-zero decision procedure. No target-specific rigorous program certificate follows merely from that existence result. The ready-input laboratory runtime begins after compilation; storage of an unknown input while compiling needs its own time account.

## Physical duration, phase and accuracy requests

For R=(XX+YY)/2 use the positive integrated generators

    Q_A=(pi/4)(I-R), Q_phi=|phi|I-phi Z, Q_SWAP=(pi/2)(I-SWAP).

Every reserve is counted. Let Q*=6pi, f_h(t)=(1-cos(2pi t/h))/h on a slot, and use H_control=hbar f_h Q with fixed

    h >= max(4 hbar Q*/g, sqrt(4pi hbar Q*/sigma)).

Pad to Gbar serial slots, then apply one simultaneous all-site number-phase layer. Set tau=(Gbar+1)h first. Choose rational r within 1/4 of Delta tau/(2pi hbar), k=floor(r)+2 and lambda=2pi k-Delta tau/hbar, so 3pi/2<lambda<=9pi/2. The last layer uses lambda n on every site, including the ancilla. Literal K_S stays installed. On the full space,

    U_lab(tau)=exp[-i(E0 tau/hbar+Phi)] C,
    Phi=(pi/4)N_A+sum_actual_word |phi|.

Full SWAP has endpoint scalar one under its paid positive generator. The final number-generator reserve is already in exp(-i lambda N_tot); it is not deleted or counted twice. All old, battery, ancilla and reference outputs remain in the comparator.

For unhalved joint trace error the budget is

    e <= 4pi q/(L+1)+epsilon_p+2eta_C+2eta_H+2eta_t.

For 0<epsilon<=1 take rational rho within 1/4 of 20pi q/epsilon, L=floor(rho)+2, epsilon_p<=epsilon/5 and each eta<=epsilon/10. Put A_q=20pi q+3, C_q=K_q A_q^4 and D_q=A_q+3q+1. Then

    Gbar<=C_q epsilon^-4, tau<=h(C_q+1)epsilon^-4, m<=D_q/epsilon.

The ideal added incident cap is Delta+g/2; calibrated headroom is Delta+2g with actual support, positivity, norm and slew separately certified. Including the old scalar allocation gives the safe full cap E0+Delta+2g. Global installed norm and energy range grow with m.

Explicit sufficient requests in the full derivation include

    b*=hbar epsilon^5/[30h(C_q+1)],
    delta*=epsilon^5/[30(C_q+D_q)], area*=delta*/Q*,
    time*=hbar epsilon^2/[10(E0+D_q Delta)].

These give order epsilon^5 global static/generator/area requests, epsilon^6 per-new-field requests, and epsilon^9 cancellation-sensitive Delta/pi evaluation for lambda. They are requested numerical precisions, with the source's unit, arithmetic and cross-term allowances; they do not bound oracle walltime. Scalar-phase reporting also pays for E0 tau/hbar and every actual angle.

The endpoint timing bound applies after all controls are off. Supply a sampling margin or charge the active-control timing integral. The optional guarded schedule uses tau_g=(Gbar+3)h, recomputes lambda, and charges eta_shift<=(4Q*/h)(Gbar+m)delta_s with its revised half-budget allocation. Absolute start requests of order epsilon^5 and accumulated period requests of order epsilon^9 do not supply a microscopic clock. Actual positive coefficients and derivative caps remain separate from a small Duhamel error.

## Energy and later evolution

The nominal conserved observable is the same physical free F=E0 I+Delta N_tot. Its whole distribution is conserved. Modeled net prescribed-drive work is zero with both endpoints F, while absolute work is at most g(Gbar+m). The external actuator's microscopic energy/output is not thereby supplied.

For initial old-marginal error epsilon_S0 and final old-marginal error e_out, the controlling allowance is

    |actual old-energy gain - declared target gain|
      <= (q Delta/2)(e_out+epsilon_S0), epsilon_S0<=epsilon_p.

Final-only energy allowances require exact initial old-marginal agreement. The explicit q=1 mixture counterexample to the overextended formula is preserved in the runtime qualifications. Moment estimates need actual operator weights and covariances; growing battery range makes trace readiness insufficient for uniform moment accuracy. Post-off error remains unchanged only under the same actual F for both state and comparator. Persistent field mismatch or noise adds its storage integral. Native preparation, autonomous halt, microscopic controller closure and indefinite reuse are not supplied.

## What the finite fixture establishes

The separate q=1,L=1,M=3 fixture uses

    V=((5+12i)/13)[[3/5,4i/5],[4i/5,3/5]], det V=(-119+120i)/169.

Its complete 32-by-16 input isometry includes the three selected pairs (4,8), (6,12), (7,14), all ten other data states, and all ancilla output rows. It emits 6,384 logical A/Z gates and 24,720 adjacent/onsite gates, below Gbar=44,688. One actual complex128 propagation reports residual 2.9508448902312835e-13, ancilla-one norm 1.203455149051588e-14, and paid endpoint illustration residual 5.44294855010996e-12. No fitted scalar is used. Its illustrated duration uses the actual route count: 24,721 slots, including five final phase generators in one slot.

The determinant-omission mutant retains exactly the nominal Givens segments and has observed residual 1.8461538461538018, consistent with the exact prediction 24/13. Complement action and ancilla return alone would miss it. All words, matrices, code, source-at-launch, receipts and streams are preserved.

The exposed checker independently inspected every saved route's integer wire permutation, operand order and inverse return; rebuilt the target; and reanalyzed saved matrices. It did **not** independently emit or propagate a second circuit. Different Python/NumPy versions do not change that limit. Neither execution is interval-certified, pulse integration, laboratory calibration, or an implemented general certifying compiler. L=1 gives no useful small-error unchanged-battery guarantee. q>1 elimination, larger logical-pair distance, deeper recursion and arbitrary branch behavior are untested here.

The earlier exact-algebra source has a preserved preexec launch failure with unknown cause and a successful retry of the same source. That failure is not a failure of this fixture. Historical reports are unchanged. [EXPOSURE_AND_SCOPE.md](EXPOSURE_AND_SCOPE.md) and [EVIDENCE_MAP.json](EVIDENCE_MAP.json) distinguish each actual execution and the same-model, source-exposed review limits. Packaging runs only metadata checks. Root must separately review this exact wrapper and supply any actual canonical binding; no such decision is inferred from the earlier wrapper review.
