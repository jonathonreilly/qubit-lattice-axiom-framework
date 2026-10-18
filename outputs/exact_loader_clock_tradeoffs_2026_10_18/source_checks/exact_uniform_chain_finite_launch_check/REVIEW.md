# Exact scalar finite launch: distinct composition check

Disposition: SUPPORT for the proposed complete normalized finite-window theorem and its displayed sufficient resource policy. No required correction found. The filtered spectral state, all-time-to-horizon far cut, exact output endpoints and normalization argument are supported. No physical network realization or gate theorem follows without the separately specified unitary interface.

## Evidence and exposure

Completely read `exact_uniform_chain_finite_launch/PROPOSAL.md` and verified SHA256 `bda916e331d0bf3863feac8e0b7dce279df6f2eaa94f0dd17daf651cad51545a`. Paths below are under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The exact endpoint source was completely reread. The scalar pole/half-line/late source arguments and their checks retain the complete recent reads from the resonant-policy check, refreshed at unchanged identities. Only their scalar coefficient versions are reused. The following hashes were verified for this task:

| Source directory | PROPOSAL.md | Sibling check REVIEW.md |
|---|---|---|
|common_product_endpoint_launch|fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4|51247de9ba58bbfeb7f731c478d939e05e2e9d90956192d2e9e6f612401662c1|
|common_product_outgoing_pole_tail|b2622fbb513ef30840ba719fb6f7725e9dba24cf74ebe48be5e790c0fa3e4b80|0071e81532263d56c37690be97aa25e30ed56a7fa6c394dbfc9243a646e62d00|
|common_product_resonant_halfline_tails|43c0cc0560ccd6b9ce33345796f511fba63c5fa7360f9225e8d9b30ec1bf33b1|1fa285544e38728389fb6bb9928b8bbd1e6a9612beb12cfde7532439b0935f9b|
|common_product_resonant_late_tails|a03139261c649546c00b7a15bef01c4a7387dfa6cc267f5c20e82f88b65f02d9|ef27352b742abe064e5b8d71d09d7904182cea49c9dce2c77187aab8494b34cd|

I authored several of these scalar ancestors and checked earlier finite/gauge work. Another author wrote this new finite composition after ROOT's design suggestions. I reconstructed its new filtering, cut and normalization interface independently after reading the source. This is source-exposed same-model checking with shared ancestry, not blind replication or an independent re-audit of all adopted spectral machinery. No older finite runtime theorem, router measure or microscopic scattering completeness is imported.

## 1. Physical finite operator and count

The source block has vacuum0, one-head matrix [[2J,-gamma],[-gamma,J]] and double-head energy3J. For gamma<=J its largest one-head eigenvalue is at most (3+sqrt(5))J/2<3J, so its full norm is exactly3J. The preceding ordinary bond adds J to site0's source-block diagonal, leaving2J at both source-adjacent sites. At the other end, the explicit cap J n_N repairs the ordinary endpoint diagonal from J to2J. Adding the positive common occupations gives2J+mu on every one-head coordinate.

There are N+2=2ell+K+1 heads, N+1=2ell+K edges and N+2 blocks before the separate shift, counting the source as one combined block. Positive mu contributes one further block per head. The incident sums3J+mu,5J+mu,4J+mu and3J+mu follow from the actual full-support block norms. Thus J=Lambda/(5+c_mu) enforces the stated cap under that convention. The graph itself is a line; its scalar geometry/counts are not automatically the geometry/counts of any different physical realization.

## 2. Normalized filtered state and its initial cost

The adopted cyclic source representation has emitter column sqrt(w), normalized measure w=|F|^2 and exact lead columns giving outgoing F and incoming conjugate(F). Multiplication by the real spectral function chi(E) multiplies every source spectral amplitude by chi. Therefore the normalized state chi(H)|s>/sqrt(p) has norm one with p=integral chi^2 w, but its emitter coordinate at time t is integral chi w exp(-iue)/sqrt(p), with only ONE chi. Its lead amplitudes are precisely g=chi F/sqrt(p) and conjugate(g). This proves equation(8) without assuming that the outgoing half-line alone has unit norm.

The direct tail estimate from w is also correct. Its denominator is (2-rho^2)^2 tan(q)^2+rho^4. On |q|>h/2, replacing |tan q| by |q| and integrating both infinite q^-2 tails gives8rho^2/[pi(2-rho^2)^2 h]<3rho^2/h. Consequently both1-p and the squared norm of (1-chi(H))|s> are at most P. Splitting the initial difference through chi(H)|s> gives sqrt(P)+|1-sqrt(p)|<=sqrt(P)+P<=2sqrt(P).

This is a single initial state error, invariant under subsequent common unitary evolution. A filtered tail beyond a future cut may already be present at t=0; no assumption that it vanishes is made. Positivity of p is established independently by P<1/2. The cutoff is an analytical comparison state, not a physical pulse inserted into the experiment.

## 3. Scalar constants and favorable far-cut signs

For scalar M=1, the product of the exp(ik(x)) and k'(x) derivative ceilings gives C=(1,2,7,30). For example C3=5+6+9+10=30. The cutoff product then yields D=(2,24,394,6280): D2=300+80+14 and D3=4000+1800+420+60. These are the actual W^{3,1} quintic bounds, not a claim about arbitrary C2 cutoffs. The stated P_star and Q_star reproduce the checked three-IBP coefficients and the auxiliary-frequency integrals. The larger higher-phase constants64,512,2048 safely dominate their smaller scalar boundary applications.

The exact pole substitution gives F proportional to1/(x+ib), hence auxiliary phase+vx. Conjugate(F) gives-vx. At n=N,N+1 and0<=u<=7ell/8, the geometry implies2ell<=n<=2.01ell. Therefore outgoing phase derivative n-2u sin k is at least ell/4, while incoming derivative -n-2u sin k is at most-2ell. Their absolute first derivatives are below4ell and subsequent k derivatives below2ell. Atan differentiation preserves a margin greater than .23ell and fits the4ell,32ell,128ell derivative ceilings. Thus both auxiliary signs are favorable, including at time zero; no adverse-pole exponential is needed for this far boundary.

Each of the outgoing and incoming amplitudes at either cut coordinate is bounded by rho Q_star/(h^2 ell^2). The cut operator is the hopping-only J Adj(N,N+1), of norm J. The two coordinates and two amplitudes give2sqrt(2)J times that scalar ceiling. Integrating for7ell/(8J) gives7sqrt(2)/4 times rho Q_star/(h^2ell), less than the advertised factor3. This is a norm integral, not cancellation inside Duhamel.

The cap makes the finite restriction exactly the cut half-line operator with unchanged diagonal2J. Evolving the actual seed by that cut operator keeps it in the finite component. Comparing its evolution first with the cut evolution of the filtered initial state, then with the uncut filtered evolution, gives equation(15). This pays the initial filtered tail and finite returns on the specified horizon without integrating an omitted spectral mass over time. No early-contact approximation, unfiltered survival bound or finite-spectrum assertion is required.

## 4. Output sets and complete sequence tails

The retained F interval is ell+K through2ell+K-1 inclusive, with ell sites. Its complement on the full Fourier integer line is exactly the union n<=ell+K-1 and n>=2ell+K. These include negative Fourier indices, all physical input/interior positions and the tail beyond the actual cap.

For the incoming conjugate half-line, the favorable estimate2rho Q_star/(h^2 u^(3/2)) is below4rho Q_star/(h^2 ell^(3/2)) because u>=3ell/4. It includes n=0.

For the outgoing left complement let L=ell+K-1 and n=L-r. Then Q_left=1.98u-L>=.485ell-K+1>=.4ell, using ell>=100(K+1). Also L+u<=1.885ell<=16Q_left. The negative-gap lemma with scalar coefficient1 therefore gives an algebraic coefficient at most .4^-3/2<4 and exponential exp[-rho^2 Q_left/(2(2-rho^2))]<=exp(-rho^2 ell/10). The high-frequency norm is taken before summation/integration; it is not an infinite sum of a sitewise constant.

For the right complement R=2ell+K and n=R+r, Q_right=.99R-2u>=.23ell and R+u<=2.885ell<16Q_right. The positive-gap coefficient satisfies2*.23^-3/2<20. Adding the two tail norms gives precisely D_star=4P_star+20Q_star in equation(23). All gap quantities exceed one under the policy. No extra fixed-interior residual remains uncounted: those K sites belong to the left omitted interval.

## 5. Normalization pays the actual filtered emitter

Full-integer Parseval gives norm one for b. Its F restriction has norm q_F=sqrt(1-d^2). Let z be that restriction divided by its positive norm. The exact normalized filtered state has F component b_F plus the incoming restriction. Therefore

    Re<z,Phi_chi> >= q_F-i,
    ||Phi_chi-z||^2 <=2(1-q_F)+2i <=2d^2+2i.

The first inequality is an inner-product bound with the fixed complex phase; it is not an addition of probabilities. Since both compared full vectors have norm one, it controls EVERY coordinate outside F, including the occupied source. When q_F>=i, the separate residual estimate follows from ||P_F Phi_chi||>=q_F-i and1-(q_F-i)^2<=d^2+2i. In particular it bounds A_chi, not the different unfiltered source amplitude A.

The complete finite comparison follows by combining this norm estimate with the initial spectral cost and the cut Duhamel bound. Actual finite evolution is not projected or renormalized. The comparator alone is normalized mathematically, with no fitted phase. Extending vectors by zero outside the finite physical space preserves the estimate. This resolves the emitter through exact filtered-state normalization rather than assuming it is empty.

## 6. Simultaneous policy and orders

With h=10^-3 and rho=epsilon sqrt(h)/1024, P=3epsilon^2/1024^2<1/2. The geometric entries ensure ell>=1000 and ell>=100(K+1). The remaining length entries independently imply:

- 2sqrt(P)=2sqrt(3)epsilon/1024<epsilon/256.
- 3rho Q_star/(h^2ell)<=epsilon/64 from the factor192 term.
- rho D_star/(h^2ell^(3/2))<=epsilon/128.
- 4sqrt(h)exp(-rho^2ell/10)/rho<=epsilon/128 from the stated logarithm.
- 4rho Q_star/(h^2ell^(3/2))<=epsilon^2/8192 from the factor32768 term.

The log argument is exactly524288/epsilon^2>1. Hence d<=epsilon/64<1 before z is defined, q_F>i, and sqrt(2d^2+2i)<=sqrt(3)epsilon/64<epsilon/32. The sum is strictly below(1+4+8)epsilon/256=13epsilon/256<epsilon/16<epsilon/8. All inequalities are uniform on the closed time interval, whose relative width is1/6.

Projection onto the complement of F contracts the actual full-vector error because the target is wholly in F. Its norm is therefore below epsilon/8 and its probability below epsilon^2/64. The pure-state unhalved trace bound is below epsilon/4 under that conservative contract. These success statements follow from the proof rather than entering its normalization step.

For fixed K and c_mu, rho is proportional to epsilon. The cut and algebraic d length entries are constant in epsilon, the incoming square-root-cost entry has order epsilon^-2/3, and the last logarithmic entry has order epsilon^-2 log(1/epsilon). Its positive inclusion in the maximum gives matching upper and lower orders for this recipe. Counts and dimensionless times share that order; physical times divide by fixed J. Gamma has order J epsilon. This is a sufficient-policy Theta statement, not an optimal lower bound. Variable K requires the exact maximum, as the source states.

## 7. Identical rails and realization limits

Identical rail copies have the same scalar error vector. Their error images occupy orthogonal rail sectors, so the induced error norm is the scalar norm rather than a sum or sqrt(number of rails) penalty. Passive references do not change it. Supplied coherent emitter amplitudes are allowed; this is not simultaneous excitation of multiple emitters or a derivation of their coherence.

A separate exact unitary identification including every source, cap, physical head, data coordinate and onsite repair can transfer the inequality by norm invariance. The stated interface requires its action on both source and every retained F coordinate, which is sufficient to fix the complete target and phase. It does not follow from a local gate identity alone. For K=74, x=n-ell indeed places the emitter at-ell-1, the last internal coordinate at73 and output at74 through73+ell. Source-to-cap distance is2ell+74. These coordinate facts do not supply a physical global gauge or its counts/cap.

Only this REVIEW.md was written. Work consisted of analytical reconstruction, complete source reads and deterministic identity/directory bookkeeping. No scientific executable, solver, simulation, sweep, delegation, Git/publication/W/checkpoint/axiom/editable-prompt change or model override occurred. No editable prompt file changed. This is scoped analytical support for the scalar conditional theorem, not a native preparation, capture/reset, permanent halt, active-environment or formal retained-audit claim.
