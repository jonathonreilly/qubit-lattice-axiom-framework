# Repo search

Terms: `kurtosis`, `KURT-E`, `FUSE-E`, `hidden.{0,8}bit`,
`moment hierarchy`, `transitive multiplet`; then `ground.state.transform`
and `carr[eé].du.champ`. The broad searches reached their 70/45-line caps;
they are discovery only. The narrower completed search
`kurtosis.energy|KURT-E|FUSE-E|hidden centre bit|transitive multiplet|fusion by squaring|fusion by the product rule`
returned **no hits** on all five refs. Commands were bounded `git grep -n
-i -E ... -- '*.md' '*.tex' | head`, in the owner's specified full repository.

| Ref | Revision searched |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Relevant hits, with their statements checked at the source:

- `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_CONSTRUCTION_ASTRA.md:145–204`
  defines the actual transfer Hamiltonian by `-a^-1 log(T/lambda_0)`;
  (6) gives its ground-state Markov transform, and (7)–(9) give the
  finite-volume minorization `epsilon=exp(-2 beta n_s)`. This is prior
  transfer structure, not a flux kurtosis bound. The search also hits its
  pr/10133 copy. No new ground-state-transform construction is needed here.
- `origin/main:docs/COMPACT_ROTOR_SPATIAL_GROUND_PATH_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-16.md:24–66`
  gives `L=(g^2/2)Delta+g^2 grad(log psi).grad` for a supplied compact rotor
  Hamiltonian. This is a genuine diffusion with invariant law `psi^2 Haar`.
  Its martingale fourth-moment bound concerns path increments, not the flux
  eigenfunction. It does not make `-log P` a diffusion for a discrete transfer.
- Other broad hits include `SRCREAL.md:332`, `CODEX_REVIEW_P4.md:282`,
  `docs/CLOSURE_T2_M1_M2_DISTINGUISHER_NOTE_2026-05-10_t2m1m2.md:72`,
  and native Ward/hidden-bit notes. These are search-level exclusions:
  Schwinger moment hierarchies, beta-distribution kurtoses, or other models.
  Their proofs are not imported.

The checkout search found the **existing relevant work**:
`gap-brainstorm2-max.md:389–422,486–500` (Claude Fable 5.2), its Codex check
`gap-brainstorm2-check-astra.md:34–199,247–264`, and the earlier hand
counterexample `gap-loop-eq-check.md:466–512`. The first already has SQ and
the diffusion 4/3 identity. The check already separates discrete deficits
from logarithmic energies, retains the half-time prefactor, and identifies
the missing consumer inputs. I reuse those results and their original
counterexample below; I do not reopen their proof tasks. Row 889 instead
checks the new statements and their use in row 886.

`prior/gap-kurt-check-astra.md` is absent. The whole
`prior/repo-search-2026-11-08.md` was read: its thirteen targets concern RG
admission, covariance and history formation, not this flux check. Row 889
has no separate “Repo prior work” line. Searching `open-registry.md` for
`gap-kurt|KURT|FUSE-E|hidden.bit` found no ownership conflict.

The SA-index README was read first. Searches of the chunk files,
`obligations.md` and the complete-account index for the above objects,
`electric flux`, `flux sector`, `fourth.moment` and `ground.state` found no
indexed supplier of the new statements. Neighbouring rows were read:
chunk-02:97–111, chunk-25:56–64, and the corresponding obligation ranges.
The cited outline passages were then read:

- SA 2313–2383: `L=P C_E^(1/2)e^(-V)C_E^(1/2)P` is positive and trace
  class, `Z_s=Tr L^s` (GL8), and contractions satisfy GL10. These are prior
  transfer/trace facts, not a kurtosis lower bound.
- SA 27533–27568: GCB24 is the fourth-moment recursion for **linear Gaussian
  statistics with a cutoff defect**. It is not a flux-eigenfunction theorem.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text. No CA theorem or Balaban quotation is needed as a premise here.
Tadeusz Balaban's work remains background to this lane; no unavailable paper
was imported. These searches are bounded retrieval results, not absence
theorems.

## Provenance and scope

Codex, gpt-6-astra, xhigh; 2026-11-13. Check of Claude Fable 5.2's row 886
at checkout `820cd9da23f6258edc17d2000d54f97514b63a31`.
Line numbers below refer to `library/gap-kurt-max.md` at that revision.
Source SHA-256: `933e81dec3f7ee25eed078b90545750e9fc7228b1a8fee45ac5c38a75d616acf`.
Final byte comparison confirmed that the source still matches the pinned
commit. The report has twelve numbered check sections and one final RESULT.
Research text only; not an audit and no status grant. No numerical run,
machine enumeration, or computer-assisted proof was used.

The named statements are checked below, one at a time. Recalled phase
physics, the guide runs, (HB), and a physical SU(2) proof of (KURT) are
outside this check. Only this output file is changed. The pinned working
branch is retained. Repository workflow files are absent in the sparse
checkout; the main workflow map, RULES and check procedure were read via
the explicitly authorized full-repository location. This report follows
the owner's requested path and verdict vocabulary, not the formal status
record format.

## 1. Theorem 4.1 — HOLDS

Lines 193–214. Put `u=|g|^p-M_p`. Conditional Jensen gives
`theta^(pt)|g|^p <= P^t|g|^p`. Thus
`theta^(pt) M_(2p) <= M_p^2 + <u,P^t u>`.
The character has order two, so u is in the full invariant sector.
Its spectral measure is supported below rho; for t>=2 the stated `P>=0`
puts it in `[0,rho]`. Therefore the last term is at most
`rho^t(M_(2p)-M_p^2)`. This verifies every step and every p>=1.
At t=1 nonnegative spectrum is unnecessary, as stated.

The p=1 and window corollaries follow by subtraction and division.
The displayed division by `1-rho^t` requires `rho^t<1`; retain the
undivided inequality otherwise. The exact flatness criterion is
`(1-theta^p)/(1-rho) -> 0`, not `E/m -> 0` in unrestricted discrete time.
The latter distinction and its counterexample already appear in
`gap-brainstorm2-check-astra.md:99–122`. The p=2 case is precisely prior SQ,
not a new result of row 886.

## 2. Theorem 4.2 with 7.1 — HOLDS AFTER CORRECTION

Lines 216–227 and 419–425. The original theorem, with `mu(g=0)=0`, holds.
Under the stationary reversible pair law J, subtract
`theta c=E_J[s(X)g(Y)]` from `c=E_J[s(Y)g(Y)]`. This gives exactly
`(1-theta)c=E_J[|g(Y)|(1-s(X)s(Y))]`.
For signs in {-1,1}, the bracket is twice the sign-change indicator.
Reversibility then gives (FLIP). Also
`1-2 qbar=<s,Ps><=theta`, since s is a unit vector in the chi sector.
Equality holds precisely when `(theta-P)s=0`: use the positive square root
of `theta-P` restricted to that sector. This verifies the stated iff.
“Flips sit where |g| is small” means only
`Cov(q,|g|)=c[(1-theta)/2-qbar]<=0`, not a pointwise assertion.

The general identity in 7.1 remains valid with `sign(0)=0`.
The overlap inequalities in 4.5(c) also survive that convention.
However, “4.5(c) holds as stated” at line 424 must exclude its **bit-flip
interpretation** when the zero set has positive measure.
Then `(1-<s,Ps>)/2` is not the probability that s changes.

Here is a hand counterexample to that interpretation, also used in section 6.
Take X={-1,0,1}, mu=(1/4,1/2,1/4), z(x)=-x, `g(x)=sqrt(2)x`, and the
kernel density `K(x,y)=1+(1/4)g(x)g(y)` relative to mu.
It is at least 1/2, reversible, Markov and positive semidefinite.
Its eigenvalues are 1,1/4,0; g is the top odd eigenvector and kappa=2.
For s=sign(g), `<s,Ps>=1/8`. The change probability is
`1/2+1/16=9/16`, whereas `(1-<s,Ps>)/2=7/16`.
The claimed 4.5(c) upper flip bound with eta=1 is 1/2 and is violated.

Correct text: keep the general 7.1 identity for the three-valued sign;
keep the 4.5(c) overlap bounds; interpret them as bit-flip bounds only for
a measurable chi-equivariant {-1,1}-valued extension on the zero set.

## 3. Theorem 4.3 — HOLDS

Lines 229–243. Write `eta=kappa-1`, `A=1-theta^2`.
Stationarity gives `E_mu V=A`, while the joint-law calculation gives
`E_mu[g^2 V]=<g^2,Pg^2>-theta^2 kappa=A kappa-lambda_bar eta`.
Subtract A to obtain
`Cov(g^2,V)=eta(A-lambda_bar)`, which is (KE) with the printed sign.
Conditional variance gives V>=0, hence
`lambda_bar eta<=A(eta+1)`.
The function `1+1/eta` decreases, proving (i); subtracting `A eta` and
dividing by the positive `lambda_bar-A` proves (ii).
The even-sector Rayleigh bound gives `lambda_bar>=1-rho`.
All quantities are finite under (S). This is an energy for `I-P`, not for
`-log P`; no linear logarithmic-energy comparison follows from it alone.

## 4. Theorem 4.4 — HOLDS AFTER CORRECTION

Lines 245–264. The exact formula and both companion identities hold for a
**conservative symmetric diffusion with the required form domains**.
The chain rule and testing `Hg=Eg` against g cubed must be legitimate;
g squared must be in Dom(H) for the variance identity, with Gamma(g) in L2.
Read `<h,(H-2E)^2h>` as `||(H-2E)h||^2`; a literal operator square would
need the stronger domain Dom(H squared). Smooth compact diffusion
eigenfunctions satisfy these conditions. Unbounded examples need their
integrability checked separately. These analytic qualifications were already
identified in `gap-brainstorm2-check-astra.md:77–97`.

Reuse its checked identity `Ecal(g^2,g^2)=(4/3)E kappa`.
Consequently `lambda_bar( kappa-1 )=(4/3)E kappa`. Since E>0 and
1<kappa<infinity, `lambda_bar>4E/3`; solving gives exactly
`kappa=lambda_bar/(lambda_bar-4E/3)=3r/(3r-2)`.
The product rule gives
`Gamma(g)-E=E h-(1/2)Hh`. Its mean is zero because `E_mu Gamma(g)=E`.
Taking its squared norm verifies the variance identity.
Finally `2E(kappa-1)-(4/3)E kappa=(2E/3)(kappa-3)`, with the printed sign.
Thus (KURT-E) is indeed equivalent to KURT in this diffusion setting.

The OU and circle entries are prior exact hand examples. As another check,
on S^(d-1), d>=2, `-Delta x_1=(d-1)x_1` and
`-Delta(d x_1^2-1)=2d(d x_1^2-1)`.
Rotational invariance gives A=E x_1^4=3B, B=E x_1^2 x_2^2:
expand `E[(x_1+x_2)/sqrt(2)]^4=A`. Then
`1=d A+d(d-1)B`, so `A=3/[d(d+2)]`.
Hence `kappa=3d/(d+2)` and `r=d/(d-1)`, exactly as printed.

Correct the table's “Autonomous bit: r=infinity”: for a bit, h=0 and r is
**undefined**, and its generator is not a diffusion. It is only a formal
limit of the displayed rational function. Also replace “in Hamiltonian
form” at lines 155–158, 261, 539 and 598 by “for a diffusion generator”.
The identity does not apply to a general transfer Hamiltonian `-log P`.

## 5. Theorem 4.5 and its hidden-bit reading — HOLDS AFTER CORRECTION

Lines 266–281. **(a), (b), and (c) under their printed hypotheses hold.**
Holder with exponents 3/2 and 3 gives `1<=c^(2/3) kappa^(1/3)`.
Pointwise maximization gives `sup_|s|<=1 <s,g>=E|g|=c`;
sign(g) is chi-equivariant, so the odd-restricted supremum is also c.
Further, `kappa-1=E[(|g|-1)^2(|g|+1)^2]>=2(1-c)`.
For a sign extended to {-1,1} this last quantity is exactly `||g-s||_2^2`.
For the convention sign(0)=0, the correct equality is instead
`||g-sign(g)||_2^2=2(1-c)-mu(g=0)`; the claimed upper bound still holds.

For (c), write s=g+d. The eigen-equation gives
`<s,Ps>=theta(2c-1)+<d,Pd>>=theta(2c-1)>=theta(1-eta)`.
The sector maximum gives the upper bound theta. With a two-valued odd s,
these are exactly the stated flip-probability bounds. Section 2 records
the necessary correction to 7.1's extension to a three-valued sign.
The sufficient condition `c<=1-c_1` correctly gives
`kappa>=(1-c_1)^(-2)`, for 0<c_1<1.

**The “exactly when” at lines 277–278 FAILS**, as does the equivalence at
180–182. The direction proved is small kurtosis => small sign distance.
The reverse direction needs uniform control of tails.

An explicit example within (S): let sigma be a uniform independent sign.
For integer n>=2 let A=n with probability n^-4, and
`A=n/sqrt(n^2+1)` otherwise; set g=sigma A. Then

`E g^2=1`, `kappa=2n^2/(n^2+1)->2`, and
`c=(1-n^-4)n/sqrt(n^2+1)+n^-3 ->1`.

On these four atoms use the kernel density
`K(x,y)=1+theta g(x)g(y)`, `theta=1/(2n^2)`.
It is at least 1/2, has eigenvalues 1,theta,0,0, and commutes with the free
sign flip. Thus g is a bounded top odd eigenfunction for each n, yet
`||g-sigma||_2^2=2(1-c)->0` while `kappa-1->1`.
This is exact hand algebra, not a run.

Correct reading: near-minimal kurtosis forces a hidden sign bit; excluding
all such near signs suffices for KURT. Mere L2 closeness to a sign does not
force near-minimal kurtosis. With a uniform bound |g|<=M one additionally
has `kappa-1<=(M+1)^2 ||g-s||_2^2`, which explains the missing tail input.

## 6. Corollary 7.2 — HOLDS AFTER CORRECTION

Lines 427–439, with the author's erratum at 510–511. Require a measurable
chi-equivariant {-1,1}-valued extension of sign(g) over its zero set.
“Odd” throughout the infimum must mean this same full character chi.
A free measurable finite-group action on a standard Borel space suffices:
choose one representative per orbit, choose its sign, and extend using chi.
Freeness is stronger than necessary; stabilizers lying in ker(chi) suffice.

This hypothesis is not implied by (S). In the three-state example of
section 2, the positive-mass point 0 is fixed by z. No odd two-valued sign
exists there. The infimum is over an empty set, so the uncorrected finite
inequality cannot hold. This verifies the need for the author's erratum.

Under the corrected hypothesis, every admissible s has
`q_1(s)>=(1-theta)/2`. The sign extension s_* of g has
`<s_*,P s_*>>=theta(2c-1)` by the calculation in section 5. Hence
`0<=h_odd-(1-theta)/2<=theta(1-c)`.
Division by theta>0 and `kappa-1>=2(1-c)` prove the printed constant 2.
No attainment of the infimum is required.
For a two-valued sign, `Ps(x)=s(x)[1-2q(x)]`; constant q is precisely
an eigen-cut, with the corresponding eigenvalue specified by this formula.
The “no converse” reading is sound: in section 5's four-atom example,
`delta=(1-c^2)/2->0` while `kappa-1->1`.

## 7. Proposition 4.6 — HOLDS AFTER CORRECTION

Lines 283–299. Retain section 4's diffusion and form-domain qualifications.
For bounded measurable psi, its Lipschitz primitive must be an admissible
form test; the diffusion chain rule then gives
`E_mu[psi(g) Gamma(g)]=Ecal(Psi(g),g)=E E_mu[Psi(g)g]`.
Adding a constant to Psi changes nothing, since E>0 implies E_mu g=0.
For the interval indicator, use the clipped primitive. Its product with g
is `min(|g|,delta)|g|`. This is at least `delta |g|-delta^2` for delta>0,
so (a) holds. For completeness, the identity first holds for smooth psi.
Its right side is integration of psi(r) against the finite measure with
density `E E_mu[|g| 1_{r between 0 and g}]` with respect to dr, by Fubini.
Equality of finite measures extends the identity to bounded Borel psi.
In particular the energy-weighted law of g has no atom at an endpoint,
which justifies the open-interval indicator and the clipped test.

Here is a direct check of (b), without its spectral-measure Jensen step.
Let eta=kappa-1. Section 4 gives
`<h,Gamma(g)-E>=E(eta-2)/3` and `||h||^2=eta`.
Cauchy–Schwarz therefore yields

`eta Var(Gamma(g)) >= E^2(eta-2)^2/9`.

If 0<eta<=1 this is `Var(Gamma(g))>=E^2/(9 eta)`.
Combining with `Var(Gamma(g))<=(C_2^2-1)E^2` proves the printed bound when
`C_2^2>1`; if eta>1 the other branch is immediate.
**Correct the endpoint:** when `C_2^2=1`, the printed fraction is undefined.
Instead Gamma(g)=E almost surely, and the displayed identity forces
eta=2, hence kappa=3. `C_2^2<1` is impossible by Cauchy–Schwarz.

The informal quarter-energy reading can also be quantified. At delta=1/2
the exact clipped identity gives the lower bound `E(c/2-1/16)`, because
`r(1/2-r)<=1/16` on [0,1/2]. Thus c>=5/8 suffices for at least E/4 in
`{|g|<1/2}`. This is a statement about the eigenfunction's diffusion
energy; it supplies no estimate on that energy density for Wilson transfer.

## 8. Theorem 5.1 — HOLDS

Lines 303–317. Interpret W as the nonzero real eigenspace in the odd sector
(or an explicitly circle-invariant real subspace), and the circle action
as measurable, hence continuous in its finite-dimensional unitary
representation. Its complexification splits into integer weights.
The half-turn acts by -1, so every occurring weight is odd and nonzero.
For a weight vector G, invariance gives `E G^2=0`; thus real and imaginary
parts are orthogonal and have equal positive norms. Scale `E|G|^2=2`.
In the expansion of `(G+conj(G))^4/16`, only the term
`6|G|^4/16` survives circle averaging. Hence
`E(Re G)^4=(3/8)E|G|^4>=3/2`.
Equality in the last step is exactly constancy of |G| almost surely.
This checks both constants by weight cancellation, independently of the
printed cosine integration.

The theorem guarantees a **choice** of unit eigenfunction in W, not the
bound for every superposition in a degenerate odd eigenspace. For the
consumer, choose this vector in the top odd eigenspace. The result does
not prove which U(1) charge or which O(4) multiplet is the lowest one.

## 9. Theorem 5.2 — HOLDS

Lines 319–328. The mu-preserving group acts orthogonally on the real space W.
Transitivity makes the homogeneous quartic
`Q(v)=E(sum v_i g_i)^4` constant on its unit sphere.
For d>=2, uniform sphere coordinates obey `E v_1^4=3 E v_1^2 v_2^2` and
`1=d E v_1^4+d(d-1)E v_1^2 v_2^2`, by the hand calculation in section 4.
Thus their fourth moment is `3/[d(d+2)]`.
Averaging Q over that sphere gives exactly the stated formula.
Since `E sum g_i^2=d`, Cauchy–Schwarz gives `kappa>=3d/(d+2)`.
For d=1 the formula holds directly and the lower bound is only 1.
The d=4 value is 2. Applying it to the twin's *top* odd level still needs
the stated, unproved vector-multiplet identification; the theorem alone
does not provide that identification.

## 10. Example 6.1 — HOLDS AFTER CORRECTION

Lines 361–371. The counterexample works. For a complete finite realization
choose Y={-1,1}, uniform nu, and
`P_Y=[[1+rho,1-rho],[1-rho,1+rho]]/2`, 0<rho<1.
Together with the bit eigenvalue theta=1-2b, the four product eigenvectors
are 1, y, sigma, sigma y, with eigenvalues 1,rho,theta,theta rho.
The odd top is g=sigma and kappa=1. The even trace is `1+rho^a`.
This also justifies `S_ev(a)->0` without any unproved inference from a
spectral maximum to a trace on an infinite-dimensional space.

**Normalize p explicitly.** With the full trace in the denominator,
`p_odd=theta^a/(1+theta^a)`, hence 1/3 when theta^a=1/2.
For FUSE-suff and row 876, the denominator is the even trace, and
`p_chi=Z_chi/Z_0=theta^a=1/2` instead. Either convention disproves a
uniform positive-power bound as rho tends to zero. Keep the second when
invoking the consumer. The unrestricted phrase “P_Y any” needs trace-class
powers wherever traces are used; a two-state Y already proves the example.

Finally, line 371 must say “every applicable **discrete** inequality of
Step 4”. The diffusion results do not apply to this jump chain, and
lambda_bar is undefined at h=0. Heavy here means a sector whose thermal
ratio stays a fixed distance below 1, not a new numerical definition of
the consumer's four-sector light set. This is not a Wilson SU(2) example.

## 11. Example 6.2 — HOLDS AFTER CORRECTION

Lines 373–409. The anisotropic counterexample holds. At beta_t>0 the
ungauged temporal kernel is a tensor product of two-state kernels with
positive eigenvalues `cosh(beta_t)` and `sinh(beta_t)` (up to a common
normalization). Gauge averaging is an orthogonal projection commuting
with that kernel. Thus Kt is **positive semidefinite on all link functions,
and positive definite on the gauge-invariant space**. Correct line 378
accordingly. At beta_t=0 only the constant survives.

At beta_s=infinity, flatness makes the product of links around any
contractible loop equal to 1. After fixing a spanning tree, path products
are determined by the three fundamental torus cycles; their independent
signs give exactly eight gauge classes. All classes have the same orbit
size. Multiplying both arguments by a flat connection leaves the temporal
kernel unchanged. Thus the induced kernel is convolution by a strictly
positive w on Z_2^3. Characters diagonalize it; the normalized vacuum is
constant, and every normalized character has kappa=1. Under the full group
of three centre flips, the invariant subspace is one-dimensional, so its
excited thermal sum is zero.

For beta_t>0, compression of the strictly positive form to the flat
gauge-invariant subspace remains positive definite. Hence every Fourier
eigenvalue is positive. Perron simplicity gives `0<theta_chi<1` for
nontrivial chi. At beta_t=0 their ratios are zero. At large beta_t the
diagonal class term dominates: if two flat classes differ, no gauge
transformation makes every bond equal, so at least one factor loses
`exp(-2 beta_t)`. There are finitely many gauge transformations at fixed
box. The diagonal leading coefficient is the same in every class.
After a common normalization w therefore tends to a delta mass, and all
theta_chi tend to 1. Continuity and the intermediate value theorem give
each specified ratio in (0,1), separately for each chi. No monotonicity or
simultaneous prescription of all seven ratios is asserted.

For finite beta_s put `D(s)=exp(-V(s)/2)`. Then `T=D Kt D` converges to
its flat compression. Each nonzero sector top in the limit is simple
within that sector. Finite-dimensional spectral continuity gives the
vacuum and sector eigenvector limits. Their eigen-equations give exactly
the ratio bound at 394–395 after cancelling the positive D(s).
Its denominator tends to the positive flat vacuum sum; its numerator is
bounded, and the fixed-beta_t sector eigenvalue stays positive. Thus g is
bounded uniformly as beta_s tends to infinity. The vacuum mass off the
flat set tends to zero. On the flat set g tends to its character, proving
`kappa->1`. All even excited eigenvalues tend to zero, so `S_ev(t)->0`
for each fixed t>=1. In the consumer convention `p_chi(t)->theta_chi^t>0`.
This proves the finite-coupling approximation, without a guide run.

An independent exact hand check is the allowed one-cell torus. All spatial
plaquettes are 1 and its three link holonomies are independent bits.
The temporal eigenvalues are products of tanh(beta_t); with
`beta_t=(log 3)/2`, a single-flux ratio is `(3-1)/(3+1)=1/2`, its kappa is
1, and the fully even sum is zero. The general argument above also covers
nondegenerate larger tori and their nonflat configurations.

Scope is exactly the anisotropic Z_2 model in the source. It does not
refute the isotropic SU(2) target. Lines 411–415 do not follow as a necessity:
an SU(2)-specific hypothesis alone could exclude this Z_2 example. The
example does not prove that every successful argument must use isotropy
and a group distinction “in the same step”; the suggested Q_8/2T extensions
are expressly unworked and receive no verdict here.

## 12. Claim 7.6 — HOLDS AFTER CORRECTION; its claimed implication FAILS

Lines 497–505. Write alpha>0 for the exponent called g there.
**The displayed sufficient estimate HOLDS**, conditional on the cited
sector-trace bound, with matching operator, background and normalization:

`p_chi(a)<= [1+S_ev(a/2)] theta^(a/2)` and `theta<=rho^alpha`
give `p_chi(a)<= [1+S_ev(a/2)] S_ev(a)^(alpha/2)`.

The first bound belongs to `gap-brainstorm2-max.md:489–492`, checked already
at `gap-brainstorm2-check-astra.md:138–171`: periodic magnetic background,
even a>=6, and `p_chi=Z_chi/Z_0`, not a fraction of the full trace.
The second step uses `rho^a<=S_ev(a)` and no fourth moment. Thus FUSE-E
can replace an eigenfunction input for this estimate. Zero sectors are
handled before taking logarithms.

**FUSE-E does not imply KURT — HOLDS.** Use the finite product example of
section 10 with theta=rho^alpha. Its kappa is exactly 1. Choose rho so that
theta^a<=1/2 if a heavy, rather than nearly-vacuum, sector is required.
This checks the direction claimed by the example at 502–503.

**“KURT implies FUSE-E by SQ” at line 502 — FAILS in the discrete setting.**
This is already decided by the prior kernel in `gap-loop-eq-check.md:466–512`,
reused by `gap-brainstorm2-check-astra.md:99–122,173–199`.
Use that exact construction on Haar SU(2):

`f=tr U`, `h=f^2-1`,
`K_tau(U,V)=1+(1/8)f(U)f(V)+tau h(U)h(V)`, 0<tau<1/36.

The source's hand proof gives `kappa=2`, theta=1/8, rho=tau and
`K_tau>1/4`, with nonnegative spectrum. Thus KURT holds uniformly, but
`E/m=log(8)/log(1/tau)->0`. No fixed positive alpha works across this
family. This is prior work, not a new counterexample or a Wilson-action
refutation. The two hypotheses are **incomparable** on (S), rather than
FUSE-E being strictly weaker there.

Correct comparison: for a diffusion, section 4 does imply
`E>=[3c_0/(4(1+c_0))]m`. In discrete time, SQ gives only
`E>=[c_0/(2(1+c_0))](1-exp(-m))`. An additional uniform upper bound
`0<m<=M` converts this to FUSE-E with
`alpha=c_0(1-exp(-M))/[2(1+c_0)M]`. No such bound is supplied by 7.6.

**“The consumer needs FUSE-E only” — FAILS literally.** This same consumer
scope error is already recorded at `gap-brainstorm2-check-astra.md:247–264`.
The source consumer `gap-es1-opus.md:204–217` requires a fixed four-sector
light set, F-l, and F-h for all twelve heavy crossed sectors at all three
shapes, with the stated smallness condition. For a uniform pure power from
the displayed estimate one still needs a uniform bound on
`1+S_ev(a/2)`, a uniform positive alpha, and the other backgrounds' matching
estimates. Small S_ev(a) alone does not provide that half-time bound.

Correct text: **given those remaining inputs**, FUSE-E and the matching
sector-trace bound provide the covered electric heavy-sector estimate,
with exponent alpha/2 and its explicit half-time prefactor. They require
no KURT assumption. This supplies neither the full consumer nor a
cutoff-uniform isotropic SU(2) estimate by itself.

## Disposition

| Statement | Verdict | Exact qualification |
|---|---|---|
| 4.1 moment hierarchy | HOLDS | Printed spectral-positivity assumption; no division by zero in corollaries. |
| 4.2 with 7.1 | HOLDS AFTER CORRECTION | General identity holds; three-valued signs do not have the stated bit-flip interpretation. |
| 4.3 discrete energy relation | HOLDS | Energy is for I-P. |
| 4.4 diffusion relation and identities | HOLDS AFTER CORRECTION | Diffusion/form domains; bit row is a formal limit, not an example of the theorem. |
| 4.5(a)–(c) | HOLDS AFTER CORRECTION | Fix the norm equality at zeros; retain the two-valued-sign condition for flip rates. |
| 4.5 “exactly when” / 3.7 equivalence | FAILS | First unsupported converse at 277–278; section 5 gives a four-atom counterexample. |
| 7.2 Cheeger form | HOLDS AFTER CORRECTION | Include the author's sign-extension erratum, with measurability and the full character. |
| 4.6 energy-density form | HOLDS AFTER CORRECTION | Form tests and the C_2^2=1 endpoint. |
| 5.1 circle symmetry | HOLDS | Existence of a suitable vector in an invariant eigenspace. |
| 5.2 transitive multiplet | HOLDS | d=4 value requires that multiplet to be the relevant top level. |
| 6.1 product example | HOLDS AFTER CORRECTION | Finite/trace-class realization; distinguish full-trace probability from Z_chi/Z_0. |
| 6.2 gauge example | HOLDS AFTER CORRECTION | Positive definite on gauge-invariant functions; anisotropic scope only. |
| 7.6 displayed estimate | HOLDS | Matching trace input and explicit half-time prefactor retained. |
| 7.6 FUSE-E does not imply KURT | HOLDS | Product example, including a heavy sector. |
| 7.6 KURT implies FUSE-E | FAILS | First failing line 502; existing discrete kernel refutes a uniform exponent. |
| 7.6 full-consumer sufficiency “only” | FAILS | First overclaim at 504; half-time, light-sector and remaining-sector inputs are still needed. |

The main changes are to implications, not the elementary constants.
The diffusion equivalence survives. The general discrete “strictly weaker”
ordering does not. The near-sign reading is one-way without tail control.
All original numerical runs and recalled phase claims remain unchecked;
none was used. The mathematical counterexamples here are hand-checkable.
The source note, registry, FINISH, audit surfaces and remote refs were not
edited. This report remains a local, uncommitted output in the pinned
checkout; no push was performed.

RESULT: Row 889 checked line by line by Codex (gpt-6-astra, xhigh): the moment hierarchy, discrete energy identity and symmetry theorems HOLD; the diffusion, sign, energy-density and counterexample statements HOLD AFTER the corrections above; the hidden-bit converse, discrete KURT => FUSE-E, and unqualified full-consumer sufficiency FAIL. KURT, FUSE-E and HB for isotropic SU(2) at the seed size remain open; no scientific or audit status is granted.
