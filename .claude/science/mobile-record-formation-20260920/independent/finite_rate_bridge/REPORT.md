# Independent quantitative finite-rate check

Completed 2026-09-20 without reading new primary campaign calculations.
`DERIVATION.md` preserves the complete analytical derivation written before
the computational checks. This is a conditional finite-chain result, not a
formal audit or landing review.

Let `Q` be a reversible irreducible motion generator with invariant law `pi`
and positive spectral gap `lambda`, let `0<b_min<=B<=b_max`, and set
`mu=E_pi B`, `sigma_B^2=Var_pi B`, `f=alpha/pi`, and `nu_0=pi B/mu`.
Then for every `epsilon>0`,

```
TV(nu_epsilon,nu_0)
 <= min{1, epsilon sqrt(mu*b_max)/(2(lambda+epsilon*b_min))
                 * ||f-B/mu||_(L2(pi))}.
```

The mismatch norm is at most
`sqrt(chi^2(alpha||pi))+sigma_B/mu`. In particular, stationary entrance
`alpha=pi` gives

```
TV(nu_epsilon,nu_0)
 <= min{1, epsilon sigma_B sqrt(b_max/mu)
                 /(2(lambda+epsilon*b_min))}.
```

This bound vanishes for stationary entrance with constant hazard. More
strongly, `alpha=nu_0` makes the exact error zero at every epsilon, even for
nonconstant B. A singleton class has zero error without a gap convention.

The proof uses reversibility to write the occupation density as
`r=epsilon(L+epsilon B)^(-1)f`, with `L=-Q`. Set
`h=r-1/mu`, `g=f-B/mu`, and `u=Ph` for the mean-zero projection P.
Normalization gives `E_pi(Bh)=0`, hence
`h=u-E_pi(Bu)/mu`. The exact projected equation is

```
(L+epsilon T)u=epsilon g,
T=P B P-[(B-mu) tensor (B-mu)]/mu.
```

On mean-zero functions,
`<u,Tu>=min_c E_pi[B(u-c)^2]`, so `b_min I<=T<=b_max I`.
Therefore `||u||<=epsilon||g||/(lambda+epsilon b_min)` and
`TV<=sqrt(mu<u,Tu>)/2<=sqrt(mu b_max)||u||/2`. No commutation assumption is
used. Omitting the rank-one term or assuming `E_pi h=0` is unjustified.

A separate exact representation provides a complementary bound. The
generator `R=diag(B)^(-1)Q` is reversible for `nu_0`, and
`nu_epsilon=epsilon alpha(epsilon I-R)^(-1)`. If its gap is gamma, then

```
TV <= epsilon/[2(epsilon+gamma)] sqrt(chi^2(alpha||nu_0)),
gamma >= lambda/b_max,
chi^2(alpha||nu_0)=mu E_pi[(f-B/mu)^2/B].
```

Thus gamma can be replaced by `lambda/b_max` for a bound requiring only
the original motion gap. Either bound may be smaller; taking their minimum
is valid. Given the pre-birth state, the insertion channel is `A(s,t)/B(s)`
at every epsilon, so the same TV bound also controls any subsequent
birth-mark or destination-class marginal.

## Exact checks and counterexample search

The independent `check.py` checked 90 rational cases: three reversible
generators, entrance point masses and mixed/stationary laws, and six
epsilons from `1/1000` to `100`. It forms the exact killed-generator law,
checks the projected equation and time-change identity, and compares squared
nonnegative bounds by rational arithmetic. All inequalities hold.

For `Q=[[-2,2],[3,-3]]`, `pi=(3/5,2/5)`, and `B=(1,4)`, the exact answer
for every entrance `alpha=(a,1-a)` is

```
TV = |a-3/11| epsilon/(epsilon+11/4).
```

The main bound squared minus this exact TV squared is

```
epsilon^2 (a-3/11)^2 (784 epsilon^2+3880 epsilon+4255)
 / [6(epsilon+5)^2(4 epsilon+11)^2],
```

which is nonnegative for every positive epsilon and every a. At epsilon 1
and stationary entrance, the true TV is `24/275`, while the main bound is
`sqrt(3/110)`. Consequently a proposed bound proportional only to
`sqrt(chi^2(alpha||pi))` is false: it predicts zero here. Also
`E_pi h=18/275`, explicitly refuting an unweighted centering shortcut.

The three-state path generator with unit edge rates, uniform pi and
`B=(1,2,5)` has original gap 1. Its projected T and L do not commute;
the exact tests still satisfy the derivation and bounds. At epsilon 1
and stationary entrance, TV is `5/24`, below the main bound
`sqrt(65/192)` and clock-comparison bound `sqrt(115/1296)`.

For the symmetric two-state generator with unit transition rates and
constant B=3, the main bound is attained for point-mass entrance:
`TV=3 epsilon/[2(2+3 epsilon)]`. Stationary entrance gives exactly zero.
These controls test both a nonzero sharp case and the requested vanishing
case, rather than treating the bound's nonnegativity as a check.

## Reproduction and source identity

Run from `/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920`:

```bash
python3 .claude/science/mobile-record-formation-20260920/independent/finite_rate_bridge/check.py > .claude/science/mobile-record-formation-20260920/independent/finite_rate_bridge/RUN.log 2>&1
```

The run exited 0. Full exact results are in `RESULTS.json`, with runtime and
source hashes in `MANIFEST.json`. Runtime: Python 3.13.5 and SymPy 1.14.0.

* Current HEAD used for source identity:
  `22e6df1c55c99434410b37d936991c7227bf591c`.
* Previously read planning instruction revision, unchanged:
  `068e916ca37b004757ad3a3c082857a91dc37215`.
* Workflow SHA-256, unchanged:
  `d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`.
* Earlier sealed independent report SHA-256:
  `3d31d272951642dc36812dec7a5404f5150f51bd084a947e937ae1f4846aeb44`.
* Initial `DERIVATION.md` SHA-256:
  `f61aded69fe4cc20842d7be07cf5ff27a352269ee409ae5463c16598acb1f990`.
* Executed `check.py` SHA-256:
  `a4934eff48706a7e2c6ac978a3e75a2441ae87460a2d78b947aa2590352c40a1`.

Only the stated model/handoff, unchanged workflow identity, earlier
independent artifacts, and locally specified test matrices were used.
No new primary calculation, external literature, or new physical premise
was imported. `BOUND_SEAL.json` preserves this result before any subsequent
target is pursued. The bounds are O(epsilon) for fixed finite inputs, with
explicit dependence on the motion gap, hazard and entrance density;
these quantities may worsen as the graph grows. No volume-uniform or
finite-density physical conclusion follows from this check.
