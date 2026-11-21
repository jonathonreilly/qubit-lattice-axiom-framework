# One rough plaquette with the parent in a window
Provenance: OpenAI Codex / GPT-6 (exact serving variant and effort setting not exposed to this session); commit `c1ac3f6d2957928fb1b369c79b44f850ab8075d6`; research text, not an audit; grants no status.

## 1. Scope and conventions

**Discharged — source and execution boundary.** This note concerns only (ONE) in `fill-supply.md`, Section 6, at the stated commit. GOAL and FINISH's independence, efficiency and rules sections were read first. Only this file is written. There are no numerical experiments, computer-assisted proof steps, commits, pushes, audits or subagents. Source retrieval and text editing are not mathematical evidence. The mapped-side exclusions in the request apply throughout. The machine's general physics-loop skill supplies claim-labeling discipline; the user's pinned, single-file research instruction overrides its campaign and delivery defaults. The referenced repository `SCIENCE_WORKFLOW.md` is absent from this checkout.

**Discharged — notation.** Haar measures are normalized. Write

    A(U) = sum_q [1 - (1/2) tr U_q],
    h_epsilon(U) = K_0(U, W_epsilon),
    Z_epsilon(F) = integral dU exp(-x A(U)) F(U) h_epsilon(U),
    mu_epsilon(F) = Z_epsilon(F)/Z_epsilon(1).

Here `W_epsilon = {W: angle(W_e)<epsilon for every coarse bond e}`; `0<epsilon<=min(T_2/8,1/16)`; `E_p={angle(U_p)>=2T}`; `0<T<=1/2`. There is one blocking step, with the actual label sum, line rerouting and Haar-parent branches, and no frozen fine datum. All fine bonds are integrated. Constants in (ONE) may depend on the fixed block factor and thresholds, but not on the volume, epsilon, the plaquette or x.

**Gap — question to decide.** The requested assertion is

    mu_epsilon(E_p) <= C x^p_0 exp(-c x T^2),  x>=x_* .       (ONE)

Every argument below distinguishes this full measure from a one-link conditional law, a single chart and a single label branch. Statements imported from a source are conditional unless rebuilt here. Anything recalled from memory is explicitly marked; no remembered theorem is used as a discharged premise.

## 2. Local surgery: the adversarial neighbourhood and the actual price

**Discharged — a one-link energy gain can be exactly zero.** Fix an oriented fine bond b. Orient its six incident plaquettes so their action is

    e_b(V) = sum_(i=1)^6 [1-Re tr(V S_i)/2],  V=U_b.

The other links can realize `S_1=S_2=S_3=1`, `S_4=S_5=S_6=-1`: set the transverse links to identity and choose the six distinct parallel bonds opposite b in its six plaquettes to have these signs. All remaining links can be identity. This is a valid finite-torus configuration when the neighbourhood does not wrap. The other plaquettes may be expensive; they do not change when only b changes. For every `V in SU(2)`,

    e_b(V)=3(1-Re tr V/2)+3(1+Re tr V/2)=6.             (2.1)

Consequently **every** transformation changing only b has action gain zero, even before parent preservation is imposed. The Wilson conditional law of b is exactly Haar. For the plaquette with `S_1=1`,

    P(angle(U_p)>=2T | rest)
      =1-(2/pi) integral_0^(2T) sin^2 t dt
      >=1-16T^3/(3pi)>0.                              (2.2)

The inequality uses `sin t<=t`; the last bound is positive for `T<=1/2`. This is an obstruction to a uniform one-link conditional upper bound or a one-link repair, **not** a counterexample to (ONE): (ONE) integrates the costly surrounding links, and its window changes this conditional law.

**Discharged — an explicit contraction, its Jacobian and its failed gain.** For general neighbours write `sum_i S_i=sR`, so `e_b(V)=6-s cos(phi)` with `VR=exp(phi n)`, `0<=phi<pi`, and n a unit imaginary quaternion. For `0<lambda<1` the radial map

    Phi_lambda(V)=exp(lambda phi n) R^(-1)

is injective away from the one antipodal point. Its Haar Jacobian is

    J_lambda(phi)=lambda sin^2(lambda phi)/sin^2(phi)
                   >=lambda^3,                     (2.2a)

with the continuous value at phi=0. The inequality follows from concavity of sin on `[0,pi]`, which gives `sin(lambda phi)>=lambda sin phi`. Its overlap is one and its inverse-Jacobian loss is at most `lambda^(-3)`, a constant. Its exact energy gain is

    e_b(V)-e_b(Phi_lambda(V))
                   =s[cos(lambda phi)-cos phi].      (2.2b)

It vanishes identically in (2.1). Moreover E_p need not force phi away from zero: choose the staple of p to be `-1` and the other five staples to be `1`. Then `s=4`, the minimum occurs at `V=1`, and p has angle pi at that minimum. This gives a second explicit failure of a one-link rough-event gain. The radial map generally changes parents, so it is not a candidate proof of (ONE). Even on a branch where b is entirely unread by retained parents, making the core smooth can give `P(l|Phi_lambda U)=0`; preserving the old map then preserves a branch of zero weight. A valid patch repair has to solve the changed constraints when it changes that label, as well as overcome (2.2b).

**Discharged — what the change-of-variables argument must bound.** For an injective differentiable transformation `Phi` between equal-dimensional regions of one fixed branch, with density `w`, substitution gives the needed comparison if

    A(U)-A(Phi U)>=delta,
    [P_l(U) J_l(U)]/[P_l(Phi U) J_l(Phi U)
                           |det D Phi(U)|] <= C x^a.  (2.3)

Here `J_l` is the density of the constrained measure in the chosen coordinates, not just product Haar, and the transformation must preserve every parent value read by the window. Indeed multiply (2.3) by `exp(-x A(U))`, substitute, and integrate; the result is `C x^a exp(-x delta)` times the image mass. A map of multiplicity at most M adds M. For a label-changing map the corresponding statement is a comparison of the full augmented measures, including the new constraints and the Haar-parent variables; (2.3) is not its proof.

**Gap — where a fixed small repair stops.** The action difference for a patch is the difference of *all* plaquettes meeting its changed bonds. A decrease of the marked plaquette alone is insufficient by (2.1). Enlarging the patch encounters more boundary plaquettes and more parent read supports. The label probabilities can vanish, excluded lines depend on the hull, and restoring a Haar parent adds three constraint coordinates. Thus neither a Jacobian bound on the class chart nor locality of the Wilson action supplies (2.3) on the actual mixture.

**Implication — the precise Peierls bookkeeping, if a component repair exists.** Choose a fixed finite-range adjacency on fine plaquettes large enough to include their one-step read neighbourhoods, and let its degree bound be D. Let S be a connected component containing p of the set of plaquettes with angle at least T. Such a component has action at least `|S| T^2/4`: on `[0,1]`, `1-cos t>=t^2/4`, and outside that interval monotonicity supplies the same bound for `T<=1/2`. The *absolute* action lower bound is not yet an action difference. Suppose, additionally, a repair with the same exterior and the same parents gives, for every such specified component,

    mu_epsilon(component at p is S)
       <= [B x^a exp(-b x T^2)]^|S|.                  (2.4)

The number of connected sets of size n through p is at most `D^(2n-2)`: order the neighbours, take the deterministic depth-first spanning tree of the set, and encode its traversal by a walk of length `2n-2`; that walk records every vertex of the set, so the encoding is injective. With `z=B x^a exp(-b x T^2)` and `D^2 z<=1/2`, summing (2.4) gives

    mu_epsilon(E_p) <= sum_(n>=1) D^(2n-2) z^n <=2z.  (2.5)

This is the requested entropy per plaquette, with the volume absent. Disjoint extra rough components must remain integrated and cancel in the comparison; summing their locations absolutely would reintroduce the volume. Establishing (2.4), including boundary action and constrained entropy, is stronger than the one-point target and is not discharged here. A completely rough torus is also among its obligations; no quiet boundary may be assumed for it.

**Discharged — RARE's scope and a hand check of its scale.** In the ordinary Wilson one-link law, write `sum_i S_i=s R`, `0<=s<=6`, and `phi=angle(VR)`. If every incident plaquette has angle at most t, then `s cos phi>=6 cos t`, so `phi<=t`. The angular density is proportional to `sin^2 phi exp(k cos phi)`, `k=xs<=6x`. For `0<t<=1/2`, integrate its numerator on `[t,2t]`, where `sin phi>=2t/pi` and `cos phi>=1-2t^2`; bound its denominator by `exp(k) pi/2`. This gives

    P(some incident angle>t | rest)
      >= (8/pi^3)t^3 exp(-12xt^2)
      >= (t^3/12) exp(-12xt^2).                       (2.6)

For the last inequality `pi<4` suffices. This rebuilds the simpler proof recorded in `gates/explicit-region-codex-00f9df685.md`. At the requested threshold use `t=2T` when `T<=1/4`; it gives an exponent `48xT^2`. This is consistent with a sufficiently small b in (2.4). **It is not a conditional lower bound under `mu_epsilon`**: multiplying the link density by `h_epsilon` invalidates the angular-density calculation. In particular RARE alone does not put a numerical upper bound on c in (ONE). It prevents treating roughness as impossible and identifies the ordinary Wilson exponential scale, rather than supplying the missing window comparison.

## 3. Chessboard: a negative reflection form already on the class branch

**Discharged — locality is not the positivity condition.** For a site reflection r write the fine links as `(X_+,Y,X_-)`, where Y lies on the two reflection planes. The Wilson weight alone factors as `g(Y) w(X_+,Y) w(rX_-,Y)`. This follows by assigning every plaquette to a closed half; no plaquette crosses a site plane. Its reflection form is an integral of squares. After inserting `h_epsilon`, the remaining kernel in `(X_+,rX_-)`, at fixed Y, must be positive semidefinite to repeat that proof. A product of local nonnegative functions does not have this property merely because it is nonnegative or reflection covariant.

**Discharged — the class-map linearization needed for an explicit test.** Use a torus with an even number of coarse blocks across each direction, sufficiently large for the one-step supports. The mapped reflection-covariance specifications at lines 240 and 842 explicitly use odd L, site-centred blocks and a reflection-invariant contour family. Reflect the normal coordinate t through a block centre, `r:t->-t`. This is precisely a coarse-site reflection of the kind used by the closed-block chessboard argument. Choose a tangential direction mu. Let `H_+` be the real bond field equal to 1 on mu-bonds in the fine slice `t=1` inside the centre block, zero on other bonds, and constant in all tangential coordinates. The reflected slice `t=-1` is also inside that block, and neither slice lies on a reflection plane. The mapped large odd block factor allows both slices.

The derivative Q of the all-lines map at identity is the defining path sum in mapped Text 3.1:

    Q H(c) = Q_path H(c)+Phi_H(y)-Phi_H(y'),
    Q_path H(c) = average_(z in B(y)) H([z,z']),
    Phi_H(y) = average_(z in B(y),Gamma:y->z) H(Gamma). (3.1)

These formulas follow by differentiating the finite products at identity, where their derivatives add, and the logarithm has derivative the identity. For `H_o=H_+-rH_+`, the two slices cancel in every path average, so `Q_path H_o=0`. The contour average at a centre on `t=0` is zero: reflection pairs paths with opposite `H_o` sums. At other coarse centres the centre block misses the two slices, so it is zero there too. Thus `Q H_o=0`. For `H_e=H_++rH_+`, on a tangential coarse bond c in `t=0`, translation invariance in direction mu gives `Phi_H(y)=Phi_H(y')`, whereas the two positive slice contributions give

    (Q H_e)(c)=2kappa,  kappa>0.                      (3.2)

Here kappa is the positive weight of one slice in the finite path average, multiplied by its path length L; for uniform L-site transverse averages it is 1. This computation uses the actual rooted-contour map, not the contour-free map or a changed gauge. It uses only the reflection-symmetric centre blocks and contour averages specified by that map.

**Discharged — the window measure fails this reflection-positivity test.** Set `Z=diag(i,-i)` and form `U(a,b)` by putting `exp(a Z)` on the `H_+` bonds, `exp(b Z)` on the reflected bonds, and identity elsewhere. The common plane data Y are identity. The all-lines formula is a finite smooth formula near identity: products, exponentials and logarithms with arguments away from their cut. In a sufficiently small neighbourhood its Taylor remainder in the parent log coordinates is bounded by `C(|a|+|b|)^2`, simultaneously on the finitely many parents, for some finite C. This is a finite-dimensional Taylor estimate, not a numerical approximation.

Put `a=epsilon/kappa`. For sufficiently small positive epsilon, all four fields `U(a,a)`, `U(-a,-a)`, `U(a,-a)`, `U(-a,a)` have all cell fluxes below T; their label pattern is therefore class with probability one. Equations (3.1)–(3.2), after decreasing epsilon so `4C epsilon^2/kappa^2<epsilon/2`, give:

    angle(M U(a,a)(c)), angle(M U(-a,-a)(c)) > epsilon;
    max_e angle(M U(a,-a)(e)),
    max_e angle(M U(-a,a)(e)) < epsilon/2.             (3.3)

For the first line the linear magnitude is `2epsilon`; for the second it is zero on every parent. Also choose epsilon below the requested epsilon_0 and the class-neighbourhood radius. Hence `h_epsilon` is zero on the two diagonal configurations and one on the two off-diagonal configurations. The inequalities have strict margins. By continuity there are disjoint product neighbourhoods `A_+,A_-` of the two positive-half configurations and a common neighbourhood B of Y=1 such that these same zero/one conclusions hold on the four sewn neighbourhoods. All have positive product Haar measure and remain class. Define the bounded positive-half test

    F(X_+,Y)=1_B(Y)[1_(A_+)(X_+)-1_(A_-)(X_+)].

The diagonal terms of `integral exp(-xA) h_epsilon F Theta F` vanish; each off-diagonal term has sign minus, `h_epsilon=1`, and strictly positive Wilson weight on a positive-measure set. Therefore

    mu_epsilon(F Theta F)<0                          (3.4)

for every finite x, with these sufficiently small windows. This is a hand-checkable failure of the full half-link-algebra reflection positivity used in upper-chain Lemmas 1.1–1.2. The test F need not be gauge invariant; those lemmas are stated on that full algebra.

**Discharged — exactly what breaks, and what does not follow.** A parent bond tangent to the reflection plane averages fine fields on *both* sides. Opposite fields cancel into the window; reflected equal fields do not. The failure occurs with all labels class. No rerouted or Haar-parent term can repair (3.4), since its test is supported where their probabilities are exactly zero. Conversely a genuinely independent Haar-parent factor alone contributes the constant `h:=Haar{angle<epsilon}`, which cannot spoil a positive form. The mixture and hull rules offer no positivity theorem, but it is unnecessary to allege that they are the cause: the deterministic window constraint already fails at the required centre planes. This refutes the proposed direct application of that chessboard estimate to the window law, **not (ONE)**. A special inequality restricted to gauge-invariant plaquette tests, or a different reflection construction with new boundary variables, has not been proved or refuted by this test.

**Implication — what a hypothetical chessboard proof would still owe in epsilon.** Let m be the number of coarse parent bonds and `h=Haar{angle<epsilon}`. Direct Haar integration on a branch with H Haar parents gives

    h^H integral dU exp(-xA(U)) P_l(U)
              product_(e non-Haar) 1_(B_epsilon)(M_l(U)_e). (3.5)

A regular map onto the other `m-H` parents would contribute `h^(m-H)`, with a density factor. Thus the common desired window power is `h^m` for every branch. This is a coarea/rank assertion about those maps, not a consequence of the Markov normalization. At fixed label the parent output factors are products, but their fine-link read supports overlap.

If there were n reflected tiles, and matching pressure bounds of the form

    Z_epsilon(all) >= h^m [a_0 x^(-d)]^n,
    Z_epsilon(disseminated bad)
          <= h^m [a_1 x^(-d+b_0) exp(-b_1 x T^2)]^n, (3.6)

then the chessboard nth root would give `a_1/a_0 x^b_0 exp(-b_1 xT^2)`. This shows the exact cancellation required. A denominator containing an extra factor `epsilon^(alpha n)`, `alpha>0`, leaves `epsilon^(-alpha)` after taking that root. No fixed power of x absorbs it for all positive epsilon. Restricting every fine bond to an epsilon-sized ball makes precisely this kind of excess loss. The negative form (3.4) already blocks this proposed proof; even an alternative reflection argument would still need matching powers in (3.6).

## 4. One fibre, its chart and the marginal of the parent

**Discharged — the exact finite-window formulation.** Define two measures on parent fields, without selecting a conditional probability at an exact parent:

    rho_x(D) = integral dU exp(-xA(U)) K_0(U,D),
    rho_x^p(D) = integral dU exp(-xA(U)) 1_(E_p) K_0(U,D).

They obey `0<=rho_x^p<=rho_x`. In the density language, whenever both have Haar densities `r_x^p,r_x`, their ratio `f_x(W)=r_x^p(W)/r_x(W)` is the fibre rough probability wherever `r_x>0`, and

    mu_epsilon(E_p)
      = [integral_(W_epsilon) f_x(W) r_x(W) dW]
                                /[integral_(W_epsilon) r_x(W) dW]. (4.1)

The measure version is valid even without densities. A uniform pointwise fibre bound would imply (ONE), but is stronger: (ONE) averages over a particular nested family of windows. If the two densities are continuous at identity and `r_x(1)>0`, division of each integral by the Haar volume of the window and continuity show that its limit as epsilon decreases to zero is `r_x^p(1)/r_x(1)`. Existence and continuity of those *full-mixture* densities are hypotheses of this last statement, not supplied by a class chart.

**Unchecked — the remembered local Laplace expression.** On a regular class chart G over W, use coordinates eta and its full reference density `J_W(eta)`. The familiar proposed expression around a critical centre with positive quadratic form is

    r_(x,G)(W) approximately
       exp(-x A_*(W)) x^(-d/2)
                     J_W(0) (2pi)^(d/2)/sqrt(det H_W). (4.2)

Here d is the real number of free coordinates, after solving constraints and removing only the permitted gauge directions. Formula (4.2) is a description of the proposed local expansion, **not a discharged asymptotic theorem here**. Its uniform errors require the chart hypotheses and their proofs. It explains the cancellation one seeks: compare an exit with the same exterior integral and the same constrained Gaussian factors; changing only finitely many integrated coordinates should cost finitely many powers of x. An extensive bound on each factor separately fails to establish that cancellation.

**Discharged — why a chart tail is not (ONE).** At each parent split the unnormalized full measure into G and its complement, including all label branches. In any density realization this reads

    r_x(W)=r_(x,G)(W)+r_(x,out)(W),
    r_x^p(W)=r_(x,G)^p(W)+r_(x,out)^p(W).              (4.3)

The base chart in this problem has flux at most T. Consequently `r_(x,G)^p=0`, since `E_p` starts at `2T`. Concentration *inside that chart* gives no bound on the remaining numerator. An enlarged-chart argument could estimate the part of the exit that stays in the enlarged chart, with its Jacobian and conditional modes controlled. It still leaves every branch outside that chart. A lower Hessian bound at a stationary point does not compare the full integrals in (4.3), and the parent marginal in (4.1) cannot be replaced by Haar or by the chart marginal.

**Discharged — fixed N and fixed epsilon are elementary, which isolates the uniformity problem.** Near U=1 the map is class, smooth and takes value 1. For every fixed finite torus and fixed positive epsilon, there is an open product neighbourhood O of identity with `M(O) subset W_epsilon` and `A(U)<=T^2/2` on O. Its Haar mass v is positive. On `[0,1]`, `cos u>=1-u^2/2>=1/2`; integrating twice gives `1-cos u>=u^2/4`. Taking `u=2T` and using monotonicity of `1-cos` on `[0,pi]` gives `A(U)>=T^2` on E_p. Hence

    Z_epsilon(E_p)<=exp(-xT^2),
    Z_epsilon(1)>=v exp(-xT^2/2),
    mu_epsilon(E_p)<=v^(-1) exp(-xT^2/2).             (4.4)

The product neighbourhood and v depend on N and epsilon. This proves exponential decay at each fixed pair `(N,epsilon)`; it does not bound the prefactor uniformly in either variable. It also shows why neither an expensive adversarial fixed exterior nor the negative reflection form alone refutes the target.

**Discharged — TYP's extensive energy is a different quantity.** TYP, with the support-count repair in its gate, concerns the ordinary Wilson law and an action sum over many fine plaquettes. No factorization of the selected links after multiplication by `h_epsilon` was proved there. Its conditional density therefore cannot be reused on a hard-parent fibre. Even on a convex quadratic chart, a coordinate with density proportional to `exp(-x a t^2/2)` contributes energy `1/(2x)`: integration of `(t exp(-x a t^2/2))'` on the real line gives `x a E[t^2]=1`. Thus d such coordinates have mean energy `d/(2x)` while an excursion of one fixed coordinate still pays an exponential cost of order `xT^2`. This hand calculation explains compatibility of extensive fine energy with local rarity. TYP supplies neither a local counterexample to (ONE) nor its constrained entropy comparison. It does warn against treating an extensive raw-action bound as the quietness test.

## 5. The smaller inequality at which this investigation stops

**Gap — one prescribed core, Haar input, fixed geometry (JW).** Fix an interior fine bond b of one coarse block. Set b to `-1` and every other fine bond to identity, and let C_0 be the cells whose flux test is nonzero in this field: they read its six incident rough plaquettes. Choose b far enough inside the block that this finite set lies in the block. Define the one fixed label pattern l_0 to be rough on C_0 and class elsewhere. Equivalently C_0 is the cell support of this one-bond defect; all its nonzero plaquette angles are pi, so this pattern has positive probability on an open neighbourhood of the displayed field. Let H_0 be its set of Haar parents, R_0 its set of retained parents, and `h(epsilon)=Haar(B_epsilon)`.

Fix **one** finite torus `Lambda_0` with an even coarse side N_0 larger than twice this core's one-step read diameter plus four. N_0 is now fixed, not a uniformity parameter. All fine links on this torus are integrated; there is no frozen datum. The single unresolved inequality is

    integral_(SU(2)^fine bonds of Lambda_0) dU P(l_0|U)
       product_(e in R_0) 1_(B_epsilon)(M_(l_0)(U)_e)
          <= B_0 h(epsilon)^|R_0|,
                    0<epsilon<=epsilon_0,             (JW)

for some finite B_0 depending on this fixed geometry, L and the thresholds. The expression uses the actual rerouted map for this single pattern. Multiplying by the exact factor `h(epsilon)^|H_0|` makes its full parent-window mass at most `B_0 h(epsilon)^m_0`, `m_0=|R_0|+|H_0|`. There is no Wilson weight in (JW), no large parameter x and no rough-event estimate. It asks whether one explicitly fixed branch has a bounded **averaged** parent density at the identity; a pointwise density bound on a neighbourhood would be sufficient but stronger.

**Discharged — why this is a strictly smaller task, rather than a renaming of (ONE).** The local-repair proposal needs such entropy control for arbitrary components, their exterior data and their multiplicities, together with a positive action difference. (JW) retains just one finite component, one fixed finite torus and one fixed label pattern, discards the action altogether, and asks only for the power of the shrinking window. It contains no volume limit, contour sum, energy comparison, coupling asymptotics or second blocking step. A proof of (JW) alone cannot yield (ONE). Nor is it asserted that every possible proof of (ONE) must pass through (JW): this is a smaller, concrete analytic step of the tested local-comparison route, not an equivalent reformulation of the target.

**Discharged — the flat chart required for the comparison is finite-dimensional.** At identity the path-average operator has a right inverse on this fixed lattice. To see this in the mapped designated-bond geometry, select the fine bond at the peak for each parent row, transversely inside its block. It has positive coefficient w_c in that row and zero coefficient in the other rows of the same component; the other components do not read it. For the uniform odd-L block, take the longitudinal fine bond with midpoint `y_mu+L/2` and transverse coordinates y: all L starting points along its line read it, so `w_c=L/L^4=L^(-3)`, and the neighbouring parent lines stop before or start after that bond. Assigning `H(b_c)=Y(c)/w_c` therefore gives `Q_path H=Y`. This is the peak-coordinate property specified in mapped Text 5.1. The contour part is removed algebraically: choose a fine site field omega equal to `-Phi_H` at coarse centres and zero at other sites. A gradient sums to its endpoint difference on every path, so `Q D omega=D' omega|_centres`. Consequently `S Y:=H+D omega` obeys `Q S Y=Y`.

Split the finite real fine-bond space as `image(S) + kernel(Q)`, and use coordinates `(w,z)` in that splitting. The map taking a small fine field to its parent logs and its kernel coordinates has the form `F(v)=v+R(v)` after this linear change, with `R(0)=0`, `D R(0)=0`. Smoothness of the finite class formula gives a radius r with `||D R||<=1/4` on the ball of radius r. For `|y|<=r/2`, the iteration `v_(n+1)=y-R(v_n)` stays in that ball and its successive differences shrink by at least a factor 1/4. It converges to the unique solution of `F(v)=y`. The derivative is invertible by the geometric series for `(I+D R)^(-1)`; on a smaller closed ball its determinant and the Haar coordinate densities have positive upper and lower bounds. Thus the exact chart `(w,z)` has a measure-density lower bound j>0. All its fields are class after shrinking the ball. Each plaquette angle is bounded by the sum of its four fine-link angles, and `1-cos t<=t^2/2`; the locally Lipschitz inverse just constructed therefore gives a finite constant C_A with

    A(U(w,z))<=C_A(|w|^2+|z|^2).                    (5.1)

No uniformity in the size of this chart as N varies is claimed. Gauge directions have not been discarded: d is the full fine-coordinate dimension minus `3m_0`.

**Implication — the exact limited payoff of (JW).** Assume (JW). Use only the preceding flat chart on the fixed torus, not a chart covering the rough branch. Choose a fixed u>0 small enough that the coordinate boxes below stay inside its class neighbourhood and `u<=epsilon_0`. For x>=1, integrating over `|z_i|<=u/sqrt(x)` and over parents of angle at most `min(epsilon,u/sqrt(x))` gives a constant `a_0>0`, independent of epsilon and x, with

    Z_epsilon(1)>=a_0 x^(-d/2)
                      h(min(epsilon,u/sqrt(x)))^m_0. (5.2)

Indeed (5.1) bounds xA there by the fixed number `C_A(d+m_0)u^2` (absorbing the coordinate convention in C_A); the z-volume is `(2u)^d x^(-d/2)`, and the coordinate-density lower bound converts the parent integral to Haar with a fixed positive factor. On the l_0 part of E_p, the numerator is at most

    B_0 h(epsilon)^m_0 exp(-xT^2).                   (5.3)

For `0<r<=1`, `r^3/(6pi)<=h(r)<=2r^3/(3pi)`: use `r/2<=sin r<=r` in the angular Haar integral. If `epsilon<=u/sqrt(x)`, (5.2)–(5.3) cancel the window factor exactly. Otherwise use `h(epsilon)<=1` and the lower bound on `h(u/sqrt(x))`. In both cases the contribution of this **one branch on this one torus**, divided by the full denominator, is bounded by

    C_0' x^((d+3m_0)/2) exp(-xT^2).                  (5.4)

Thus (JW) would remove epsilon from this isolated finite-dimensional comparison. The displayed exponent depends on the fixed torus; copying this proof in a variable volume would fail (ONE). The flat-chart construction supplies no regularity of the rough branch in (JW).

**Gap — the exact unproved step in (JW).** One must control the pushforward of the *whole support* of `P(l_0|U)dU` by the retained-parent map. The designated-bond inverse in a chart around the flat lift proves no such global bound. A sufficient route is a finite cover on which retained-parent coordinates can be solved with a uniform lower bound on the normal Jacobian and a bounded number of sheets, with the label weights included. Neither a vanishing normal Jacobian nor a many-to-one concentration near parent identity is excluded by the material read. Compactness without a rank bound is insufficient: the scalar map `v->v^2` sends Lebesgue mass in `[-1,1]` into `[0,epsilon]` with mass `2sqrt(epsilon)`, instead of order epsilon. This scalar example illustrates the missing inequality; it is **not** a counterexample to this SU(2) kernel.

**Unchecked — expectation, with its reason.** I expect (JW) to be true. At fixed L the core affects finitely many line choices; retained parents keep at least half their lines, and parents whose lines fail that test are integrated with Haar. These facts suggest enough independent retained line coordinates to control the normal Jacobian, with constants allowed to depend on the fixed geometry. What is missing is the written bound for those coordinates on the entire nonzero-label support, including changes of the fine gauge and possible winding around the hull. I also expect (ONE) to be true, but with less confidence: the finite-branch rank problem would still leave the action gain and cancellation for arbitrarily large connected rough sets. Neither expectation is a proof or a status judgment.

## 6. Marks and another level: exactly what is and is not delivered

**Implication — individual bounded marks.** If (ONE) were proved and a measurable insertion F obeyed `|F|<=M`, then `|Z_epsilon(F 1_(E_p))|<=M Z_epsilon(E_p)<=M q_x Z_epsilon(1)`, where `q_x=Cx^p_0 exp(-cxT^2)`. This is just the triangle inequality and positivity. Arbitrary non-quiet or amplitude marks are not necessarily contained in E_p. Unbounded insertions need their own moment estimates. Nor does this prove rarity under an arbitrarily tilted or previously marked law: taking the tilt to be `1_(E_p)` makes that conditional probability one.

**Discharged — separated one-point bounds do not give a product.** Even if every chosen plaquette had probability at most q, this only bounds their intersection by q. As a logical example, events `E_i={B=1}` for one Bernoulli variable of parameter q all have marginal and joint probability q, regardless of how their labels are placed. This is not a claim about the Wilson measure; it demonstrates the missing inference. A product bound `q^k` follows if the same q bounds each next event conditioned on all previous marks: multiply the successive conditional probabilities. Physical separation alone supplies no such conditional inequality here, because constraints and the surrounding integrated field are shared. A component comparison stable under compatible marks, or a valid marked chessboard estimate, would have to supply it. Neither is proved in this note.

**Discharged — why a second blocking step is not an iteration of (ONE).** With U -> V -> W and the true kernels, put `h_1(V)=K_1(V,W_epsilon)`. In the density notation of (4.1), the two-step probability is

    [integral f_x(V) h_1(V) rho_x(dV)]
                              /[integral h_1(V) rho_x(dV)]. (6.1)

The one-step statement bounds averages of f_x over identity-centred windows in V. The weighting h_1 is a different function; it is not asserted to be a positive mixture of those windows. V can be rough while W is in the window, in particular through the Haar-parent branches. Furthermore rho_x is an effective marginal, not a Wilson weight to which the same one-step proof may simply be reapplied. Even a pointwise estimate over all regular V would leave the rough V part of (6.1) to price. Joint events involving U and V also require the estimates to survive the intervening mark.

**Gap — consequence for the consumers.** No unconditional clause of RAR^1 or RAR^ch is supplied. A proof of (ONE) would give just its stated single-step, one-plaquette window consequence and the bounded insertion consequence above. The consumers still need their actual non-quiet marks, product estimates for compatible prescribed marks, control through rough intermediate parents, and the corresponding joint law at the next level. The full-mixture chart/marginal distinction cannot be bypassed by the tower property.

## 7. Reading boundary and decision

**Discharged — bounded source record.** The mathematical sources were `fill-supply.md`, Section 6 and bounded excerpts of Sections 2–3; mapped Text 3.1, the one-step part of Lemma 3.9, Texts 5.1–5.3, the requested chessboard remarks at lines 554 and 708, and the reflection-covariance specifications at lines 240 and 842; `explicit-region-two-step.md`'s TYP/RARE, CONC/FIB and two-step definitions; and the specified explicit-region gate's verdict rows and bounded defect discussion. Supporting bounded reads/searches covered `block-poincare-energy-package.md`'s weights and contour construction, `fibre-propagator.md` through its torus statement, `convex-laplace-tree-decay.md`'s hypotheses, and headings/selected excerpts of `lift-nonlinear.md`. Upper-chain reads covered the ordinary Wilson reflection/chessboard statements and proofs, pressure statements, and the neutral consumer/interface descriptions. Some searches and neighbouring text exposed summaries referring to both attempts; no independent-attempt proof was opened or used. Truncated retrievals were not treated as complete reads. None of the large-field producer claims in those files is imported as a proved premise.

**Discharged — procedural and memory boundary.** The general physics-loop skill and its bounded discovery, claim-status and delivery references were read as procedure, not as mathematical premises. The cached planning `AGENTS.md` and cached `origin/main` workflow were read to recover the missing operating map; no moving-branch science was imported. The explicitly excluded independent file, its gates, the prohibited library notes and prohibited cross-attempt gates were not opened. No external literature was consulted. The familiar Laplace expression (4.2) is **recalled from memory, unchecked as an asymptotic theorem here**, and carries no implication used to bound a full mass. The other discharged calculations above are written out; no numerical result or remembered literature theorem discharges a step.

**Gap — decision on (ONE).** No full proof and no family refuting (ONE), including its epsilon uniformity, has been obtained. The one-link obstruction kills a proposed uniform local gain; the negative reflection form kills the stated full-algebra centre-plane chessboard route, already on class fields. Neither kills the probability estimate. The stopping inequality is specifically (JW), the one-pattern, fixed-torus, Haar-input parent-window bound in Section 5. Its smaller scope, its concrete consequence (5.4), and the reason for expecting it to hold are stated there. The unanswered work is not being relabelled as a proof of the original exit bound or of either rarity consumer.

STOPPED
