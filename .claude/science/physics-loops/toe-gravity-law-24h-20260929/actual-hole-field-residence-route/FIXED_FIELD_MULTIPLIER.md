# Fixed-field first-moment multiplier and its exact localization cost

Author analytic candidate. This is a distinct conditional response lemma for the ORIGINAL leading one-hole no-event law, not the complete microscopic ensemble. The actual microscopic bright-residence result is in BRIGHT_RESIDENCE. This note does not claim that its auxiliary positive injection equation is the actual full microscopic hole equation.

## 1. Actual rotor inputs and a weight which does not follow the hole

Use the full physical W=1 rotor sector on even tori L>=12, arbitrary B background, arbitrary fields and ancillas. H is the exact cancelled C+[F,F*] operator; A=-i delta H-kappa G/2, G=sum(original j_mu* j_mu). The checked sparse-dark construction supplies

    Pi=bright+sparse_dark,
    T=aI-O/delta, 0<=T<=C_loc I,
    A*T+TA<=-Pi,
    O=i(V*-V).

The same a,C_loc,actual two-hop V and local sparse count cap nine are used. O has at most one entry of modulus one in each row and column. Each such entry shifts at most two electric links. Complete source/receipt identities are bound separately. Pi is a diagnostic reward, not a new mark.

Fix ANY set D of links on the finite torus and put

    q=1+sum_(e in D)|E_e|.

D is fixed in space; it does not depend on the position of the hole or on a B mask. Its cardinality can grow; constants below do not count |D|. Every elementary actual two-hop H path changes q by at most2, and the absolute row/column path budget is at most M_0=756. Diagonal terms cause no change. These statements follow from the actual36+648+72 path classification, before combining interfering paths. Every O entry also changes q by at most2. Pi,G and q commute.

Define U=q^(1/2) T q^(1/2). As a positive form, 0<=U<=C_loc q. The claim is

    A*U+UA <= -q Pi + c_0 I,
    c_0=4 M_0 (delta a+sqrt(3)).                             (F1)

The constant is independent of D, fields, torus volume and global B count. It is not independent of delta,kappa through a.

## 2. Direct commutator proof and domain

First use q_R=min(q,R), R>=1, so every operator is bounded. Its path changes are still at most2. Let C_R=[H,sqrt(q_R)]. For a matrix entry x,z,

 |sqrt(q_R(z))-sqrt(q_R(x))| sqrt(q_R(z)) <=2

whenever it belongs to an H word. Row and column Schur bounds give

    ||C_R sqrt(q_R)||<=2 M_0.

For an O step z to y, q_R(y)<=q_R(z)+2<=3q_R(z). There is at most one such step in each row and column. The same path sum therefore gives

    ||C_R O sqrt(q_R)||<=2 sqrt(3) M_0,
    ||C_R T sqrt(q_R)||<=2 M_0(a+sqrt(3)/delta).              (F2)

These bounds use the entrywise displacement of the actual words. They do not assume that square root is operator Lipschitz for arbitrary operators.

Since G commutes with q_R, the exact product identity is

 A*sqrt(q_R)T sqrt(q_R)+sqrt(q_R)T sqrt(q_R)A
   =sqrt(q_R)(A*T+TA)sqrt(q_R)
       +i delta[C_R T sqrt(q_R)+sqrt(q_R)T C_R].             (F3)

C_R is anti-Hermitian. The last Hermitian term has norm at most twice delta times the second bound in(F2), proving(F1) with q_R.

For Z(u)=exp(uA), integrate the bounded identity and drop its positive endpoint. For a vector with <q> finite,

 integral_0^U <Z(u)psi,q_R Pi Z(u)psi>du
       <= C_loc<psi,q_R psi>+c_0 integral_0^U||Z(u)psi||²du.

The integrand is increasing in R because Pi commutes with q_R. Monotone convergence proves

 integral_0^U <Z(u)psi,q Pi Z(u)psi>du
       <= C_loc<psi,q psi>+c_0 integral_0^U||Z(u)psi||²du.    (F4)

This is the rigorous form meaning of(F1); it does not assume norm continuity of an unbounded conjugation. Mixed states follow by positive trace and ancillas tensor throughout. If an endpoint is wanted, it has finite q expectation: directly i[H,q_R] has norm at most2M_0, while -kappa G q_R<=0, so <q>_u<=<q>_0+2delta M_0 u||psi||². Strong convergence of sqrt(q_R) on that vector then passes the positive endpoint as well.

The total unweighted lifetime on the right may be infinite. Equation(F4) is not a replacement for it. It is stronger than taking a norm of q or invoking a quadratic input moment: a fixed FIRST-field weight costs only its input first moment and unweighted residence.

## 3. Positive injection and physical-time scale

At finite volume let a positive trace-class eta obey the actual no-event kernel with a separately specified positive injection,

    dot eta=epsilon^-2(A eta+eta A*)+tau(t), tau(t)>=0.

Assume its initial and injected q moments are finite/integrable. Differentiation of the bounded q_R multiplier and monotone passage give

 epsilon^-2 integral_0^T Tr[q Pi eta]dt
   <= C_loc Tr[q eta(0)] + C_loc integral_0^T Tr[q tau]dt
                            +c_0 epsilon^-2 integral_0^T Tr eta dt. (F5)

No independence of the source and background is used. Original source labels can remain in direct-sum registers; the same kernel uses the original j_mu and its true terminal output. But(F5) alone does not identify the actual transformed microscopic state with this one-hole equation. Multiple exterior holes, higher normal-form terms and off-grade feedback still require their original proof obligations.

A uniformly priced actual unweighted hole residence would pay the last term for an appropriate positive component. However q is anchored to D, not to that component's moving hole. Summing q over unrelated anchors can cost volume squared. Neither exchange is made here.

## 4. Exact finite-spin version and its remaining weight

On even tori L>=28 and the complete spin box keep H_S=Hbar_S+Delta_S, with the original diagonal compensation. The checked refinement gives

 L_S(T_S)<=-Pi_S+(K_loc/C_S)Pi_S Q_loc² Pi_S.

Delta_S commutes with fixed q_R and so does not enter(F2); Hbar_S has the same safe756 path budget with its exact boundary zeros. O_S is the compressed signed partial permutation. The same calculation proves

 L_S(sqrt(q)T_S sqrt(q))
    <=-q Pi_S+(K_loc/C_S)q Pi_S Q_loc² Pi_S+c_0 I.            (F6)

All operators are finite matrices here; no rotor boundary transition is restored. This is a real residual, not a bound on its expectation. Even if q dominates Q_loc, its error is potentially cubic in the first-field weight. On a selected good-field region Q_loc²<=C_S/(2K_loc) that region's reward can be absorbed, but the complement remains an actual high-field reward. That projection need not be dynamically invariant. No source-varying good-field bound or weighted preparation is imported.

## 5. Why the moving-hole substitution is invalid

For q_mov=sum_h P_h[1+sum_(a(e):dist(a(e),h)<=2)|E_e|], moving the hole changes the set of sampled links even if all those links are unchanged by H. Thus the displacement estimate |q_out-q_in|<=2 fails. MOVING_FIELD_TRANSPORT gives actual physical dark words, with full original gates, such that H_beta,alpha=1, Pi alpha=Pi beta=0 and q_mov(alpha)-q_mov(beta)=2m. The corresponding moving congruence has an arbitrarily large positive dark-block derivative. Consequently no field-independent c_0 extension of(F1) to q_mov follows, even on the physical Gauss carrier.

This failure is a localization obstruction to this particular multiplier, not a counterexample to the actual bare-Omega residence target. It leaves a genuinely conditional dark source/transport estimate open. No new computation is needed for(F1)-(F6).
