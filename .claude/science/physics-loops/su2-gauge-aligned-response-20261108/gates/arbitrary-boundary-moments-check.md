# Independent check of arbitrary-exterior compact moments

2026-11-09. Research signal **advance** for the complete frozen 363-line
argument, including section 7. No material mathematical defect was found.
This is an independent research check, not an audit verdict, retained status,
or a mixing/connected-response result.

## Source identity and review boundary

Checked source: `parts/arbitrary-boundary-interior-moments.md` in
`.claude/science/physics-loops/su2-gauge-aligned-response-20261108`, SHA-256
`c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11`.
This hash matched in both worktrees:

- `/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics`
- `/Users/jonreilly/.codex/worktrees/su2-four-response-gluing/Physics`

The source was read in full from the gluing worktree. The inherited base is
`55fd670ff8995427b24617b2273bd3f78b7559d9`, with main pin
`1e0d3b58dcda7f83152b0bb51729260247454d65`. The finite lattice domain is the
one of the supplied compact-coercivity theorem, including odd L>=3, kappa>0,
fine side `N=L^2 m` with m>=3, terminal identity and the specified nested
forest/ownership convention.

| Mathematical input | SHA-256 |
|---|---|
| compact-energy-coercivity.md | 7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa |
| local-conditional-tail.md | cf47acdfe0deea09fe49f7b08d90d45a3aac0df3251062ba4f67f566e639072d |
| rough-component-bound.md | 1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44 |

The exact compact-coercivity, conditional-density and full-reader arguments
at these hashes were already read and checked in this session; that matching
coverage is reused. This proof does not use the relative small-collar
stationary-field theorem or a rough-component probability estimate. The
rough-component source supplies the geometric reader radius only.

The applicable instructions and inherited supervising model/effort remain
unchanged. There was no model substitution, numerical job, source edit,
Git/network mutation, formal verification or status operation. Only this
report was written. Earlier gate reports remain immutable, and no editable
prompt changed.

| Severity | Finding |
|---|---|
| Critical / high | None found. The signed tilted energy retains strictly positive residual damping, and the conditional Gibbs/tower steps are compatible. |
| Medium | None found. No missing normalizer, profile-dependent constant, total-volume factor or invalid infinite-radius limit was found. |
| Scope boundary, already explicit | The all-set rare-event bounds are bounds on deterministic simultaneous rough events. They are not arbitrary-exterior one-site domination, mixing, or connected-cumulant decay. |

## 1. Reconstructed factor and local-energy inequalities

For a unitary word of length l, the product telescoping inequality and
Cauchy–Schwarz give `|I-product A_j|^2 <= l sum |I-A_j|^2`. Dividing by two
gives equation (4), with inverse occurrences unchanged. For a kernel, first
use `|M|<=1` to majorize the centered gap by the average of
`1-w(v^dagger P)`, then apply the word inequality to the output-inclusive
word. Likewise `1-|M|<=1-w(M)` bounds the radial deficit by input words.
No division by a possibly vanishing mean occurs.

I checked the conservative coefficients rather than assuming a factor count
also counts occurrences. A fine link is in six plaquette factors, each with
word coefficient four, giving 24. A retained link is in at most nine kernels
including a hidden output. Each output-inclusive word has length at most
p+1, and one coordinate can occur at most p+1 times in it, giving
`9 kappa (p+1)^2`. For the input deficit, `9 kappa p^2` is conservative.
These bounds apply to subfamilies because each original energy factor is
nonnegative and incidence/occurrences only decrease when factors are removed.

The full reader radius also matches the ownership convention: a plaquette's
owner cells have l-infinity diameter at most one, and each kernel's paired
paths and hidden output stay in its two endpoint blocking cubes. Nested
centered odd-L cubes preserve that property at both steps. Consequently a
factor meeting J_R reads only J_(R union B), `B=N_1(R)\R`. Reversed
occurrences keep the positive-link owner, still within that set.

For the local lower bound, replace the field outside R union B by I. Selected
factors are unchanged. Every omitted factor reads no coordinate in R, so its
nonidentity readers are a subset of B and its total energy is at most
`K_E T_B`. Applying global compact coercivity to this extended field gives

```
E_R + E_omitted >= c_E (T_R+T_B),
E_R >= c_E T_R - K_E T_B.
```

This uses nonnegativity of the *original* omitted factors and the global
factor bound, not a guessed local coercivity witness contained in R. The
same upper-bound argument gives `E_R<=K_E(T_R+T_B)` and the radial-deficit
bound. Disconnected R, periodic overlaps and empty collars cause no change.

## 2. Exact radial comparison and conditional exponential moment

The identity `d/dt log H(t)=1-E_t w` follows by differentiating the compact
Haar integral. Pairing opposite scalar coordinates gives `E_t w>=0` for
t>=0, while `w<=1` gives the other endpoint. Integrating the derivative from
`kappa u r` to `kappa u` proves

```
H(kappa u) exp[-kappa u(1-r)] <= H(kappa u r) <= H(kappa u).
```

This checks the signs and both endpoints, including r=0. In particular this
is an exact common-factor comparison; no asymptotic estimate for H is needed.

On the identity product cap of chord radius `d0/sqrt(u)`,
`T_R<=n d0^2/(2u)` and its Haar mass is at least
`(c_cap d0^3)^n u^(-3n/2)`. Multiplying the lower radial comparison with the
upper energy bound gives the denominator loss
`(K_E+K_r)u T_B + (K_E+K_r)n d0^2/2`, with common factor `H(kappa u)^k`.
This cap does not require the exterior or any selected mean to be small.

For the numerator with exponent `lambda0 u T_R`, `lambda0=c_E/2`, the local
energy lower bound leaves damping `(c_E/2)u T_R`. The reference Haar integral
then factors, not the posterior. Direct radial integration bounds each
integral by `K0 u^(-3/2)` for every u>=1. One can see this without an
asymptotic argument from
`1-cos(theta)>=2 theta^2/pi^2` and `sin^2(theta)<=theta^2`, followed by the
Gaussian integral on the positive half-line. Small positive c_E changes K0
only; it creates no lower-u exception.

The ratio cancels the exact common factor `H(kappa u)^k` and the n-coordinate
Haar power `u^(-3n/2)`. This includes selected kernels with conditionally
constant normalizers. The remaining collar coefficient is precisely
`K_E+(K_E+K_r)=2K_E+K_r`; the remaining cap/integral cost is exponential
only in n=M|R|. Thus equations (1), (13) have the claimed constants. Jensen
then gives the mean inequality with the stated direction and the factor
`1/(lambda0 u)`.

## 3. Gibbs conditioning, recurrence and the finite-torus limit

Inside the exact conditional law on Omega, condition further on all variables
outside J_(N_r(x)). Every factor which reads an interior coordinate is still
present whole; all other factors cancel between numerator and denominator.
Thus this is exactly the conditional to which the derived inequality applies.
For r<s with `N_s(x) subset Omega`, its collar is
`N_(r+1)(x)\N_r(x)`, all of whose variables are random inside Omega. The tower
property therefore produces `m_(r+1)-m_r` for the mean collar sum, regardless
of correlations or overlaps with other balls.

Rearranging gives
`m_r <= q m_(r+1) + a |N_r(x)|/((1+b)u)`, `q=b/(1+b)<1`.
Iteration and `T_(N_s)<=2M|N_s|` give the displayed polynomial times q^s
boundary term and a summable geometric-polynomial series. This is an algebraic
iteration of expected sums; no independent-site estimate is used.

On a finite torus, once the ball is the whole torus, the next collar is empty
and `m_(r+1)=m_r`. The same recurrence remains valid: it is then equivalent
to the already proved whole-torus mean inequality. Iteration for arbitrarily
large s is consequently legitimate. The upper bound
`|N_r(x)|<=(2r+1)^4` remains true after saturation. Hence
`(2s+1)^4 q^s -> 0` and the remaining series is independent of the torus size.
This verifies the uniform one-cell conclusion without translation invariance.
For a proper Omega, only radii contained in Omega are used; the arbitrary
exterior remainder is not discarded as u increases.

## 4. Inhomogeneous radial profiles and signed leading energy

Conditioning a profile tilt to R leaves exactly
`E_R^theta=E_R-sum_(x in R) theta_x T_x`. Ownership is essential here: an
outside-cell tilt is constant under this conditional, while every coordinate
owned by an inside cell is integrated. No part of a crossing original kernel
or its normalizer disappears.

For every profile in the closed box `0<=theta_x<=c_E/2`, the local lower
bound becomes
`E_R^theta >= (c_E/2) T_R-K_E T_B`. Its possible negative values do not
invalidate the estimate. Because the added tilts are nonnegative,
`exp[-u E_R^theta]>=exp[-u E_R]`; the untilted cap denominator lower bound is
still valid. With `lambda_*=c_E/4`, the numerator retains strictly positive
`(c_E/4)u T_R` damping, even at the endpoint profile. The same two exact
cancellations apply. Thus the exponential-moment and mean constants are
uniform over the entire inhomogeneous profile box.

The tower argument uses successive conditionals of that *same* fixed profile.
It does not change the profile while passing between radii. All constants and
the resulting q_* can consequently be chosen once. Applying the verified
finite-torus limit gives `E_theta T_x<=C_*/u` uniformly in x and profile.

## 5. Integrating the profile and all-set events

For a deterministic cell set A, compactness permits differentiating its
normalized moment-generating integral at every real t. Its derivative is
exactly `u E_(theta=t 1_A) T_A`, since the density tilted by this moment is
the same allowed profile law. Summing the uniform one-cell bound gives
`f_A'(t)<=C_* |A|` for `0<=t<=c_E/2`. Integrating from `f_A(0)=0` proves
equation (23); this step does not differentiate an inequality or replace any
expectation by products of means.

On the event that each cell in A has a chord-distance-delta witness, ownership
ensures distinct witnesses. Therefore `T_A>=delta^2 |A|/2`. Markov applied to
the just-derived normalized exponential moment gives exactly equation (24),
including its factor 1/2 and exponent sign. A can be disconnected or wrap
around the torus. The empty set is the probability-one event, and delta=0
gives only the trivial bound as stated. The proof concerns deterministic A;
it does not grant a conditional one-cell estimate after fixing arbitrary
neighboring rough coordinates.

For one coordinate, `b_e<=T_x` yields the Gaussian chord tail. Integrating
`p h^(p-1) exp[-tu h^2/2]` on the positive half-line produces
`Gamma(1+p/2)(2/(tu))^(p/2)`, verifying the coefficient in (26) for every
fixed real p>0. This is an alternative full compact moment proof, independent
of the earlier small-collar/component route once the shared compact energy
and exact-law inputs are accepted.

Finally, in an arbitrary-exterior region Omega, the same derivative identity
uses the profile-uniform interior estimate separately for each x. Summing its
boundary remainders and integrating in t gives equation (27). Overlap of the
chosen balls introduces no additional term because only a sum of expectations
is taken. The additional cost can be large near a rough exterior and remains
explicit.

The entire strengthened chain is therefore supported within its stated finite
two-step domain. It proves radial-profile moments and simultaneous rare-cell
events; it proves neither decay of dependence nor a normalized connected
rough-sector expansion. Reopen this check if a source hash, factor/ownership
convention, global coercivity hypothesis, profile range or conditional domain
changes.
