# Adversarial scout round 2 (R2-1, R2-2, R2-4)

Date: 2026-08-26

## Construction and arithmetic contract

- Authority: the landed Block 190 construction, plus only the `Z_16 x Z_8` carrier definition recorded in scout batch 1; Block 197 is used solely for the specified completion `Y'` in R2-2.
- Arithmetic: exact SymPy `Rational` / `QQ` matrix algebra throughout. No floating-point conversion and no `nsimplify` call is used in any reported equality, sign, rank, factorization, discriminant, multiplicity, or bracket decision.
- Adversarial standard: every claimed structural leg is checked separately; a failed leg is reported even when the surrounding factorization survives.

Results are appended below as each independent check completes.

## R2-1 — genuine four-step pairing: claim confirmed; `W^2` does not realify the new quartet

On the scout-batch-1 carrier `T=16`, `X=8`, `(m,c)=(9/20,5/13)`, wrap-edge sign, and deep core `t0=3`, I rebuilt `Q`, inverted it exactly, and formed independently

```text
K_c = L_0,
W   = K_c^-1 L_2,
W4  = K_c^-1 L_4.
```

The construction controls remain exact: `d_K^2=0`, `P_s H P_s=H`, `P_s Q P_s=Q^T`, and the directed interior cross block is empty.

Let

```text
D = 4665286228862295792403731589707667277663851797971208707540169416045298468486986023231433751167751705133770813752562389709055423736572265625.
```

The **full** factorization over `QQ` is

```text
charpoly(W4) = D^-1
 (509376687890625 z^2
  -53564740315001986 z
  +509376687890625)

 (1562607064530625 z^2
  -8850303013421186 z
  +1562607064530625)^2

 (1095839897582324765625 z^2
  -86122212414722894199298 z
  +805422853255841015625)

 (1073279167574410953809362890625 z^4
  -48803501254703860104010652437500 z^3
  +749126008564815430786840792336646 z^2
  -48803501254703860104010652437500 z
  +1073279167574410953809362890625)

 (3189186037688162487174810027518614825390625 z^4
  -141948343290227405434128694826558234187387500 z^3
  +1883557212620165962479161889655050726151530102 z^2
  -122670265414397149851968073993738746247687500 z
  +2637321866031925337461270470189719981640625).
```

The degrees and multiplicities are therefore `(2,1), (2,2), (2,1), (4,1), (4,1)`. The first two quadratics are palindromic. The third quadratic is not:

```text
leading - constant = 290417044326483750000 != 0.
```

The first quartic is palindromic. For `u=z+z^-1`, its exact `u`-discriminant is

```text
-825088195432869613138145991446373196587966307289373081600000000 < 0.
```

It consequently has **zero real roots**: this is a nonreal reciprocal/conjugate quartet. The final quartic is non-palindromic in both independent coefficient tests:

```text
leading - constant
 = 551864171656237149713539557328894843750000 != 0,

z^3 coefficient - z coefficient
 = -19278077875830255582160620832819487939700000 != 0.
```

Thus the genuine four-step pairing does not restore positivity and strictly degrades palindromicity. The R2-1 factor-content claim is **confirmed**, with the advertised `u` inequality sharpened from `<=0` to `<0`.

For the alternative `W^2`, start from the scout-batch-1 new-sector quartic

```text
q(z) = 1035991876210625 z^4
       -10651994137075200 z^3
       +31207521664211586 z^2
       -10651994137075200 z
       +1035991876210625.
```

Eliminating `z` exactly between `q(z)=0` and `y=z^2` gives the primitive square-spectrum factor

```text
q_sq(y) = 1073279167574410953809362890625 y^4
          -48803501254703860104010652437500 y^3
          +749126008564815430786840792336646 y^2
          -48803501254703860104010652437500 y
          +1073279167574410953809362890625.
```

It occurs with multiplicity two in the new part of `charpoly(W^2)`. This is exactly the palindromic quartic appearing once in `charpoly(W4)`, but its `u`-discriminant is the same strictly negative integer displayed above. Hence it has zero real roots. **None of the four squared new-sector eigenvalues is real.** Reciprocal pairing/product one survives squaring; reality and positivity do not.

## R2-2 — canonical-metric cuts: `6 -> 2 -> 2`; the `Y'` cut is vacuous on the heavy sector

For the exact `T=16`, `X=4` interior window `D={2,3,4}`, I rebuilt the descended two-step operator and compressed to the four-dimensional `U=-1` sector. The ten-variable symmetric system

```text
Theta = Theta^T,
Theta T_h = T_h^T Theta
```

has coefficient rank `4`, hence nullity **exactly `6`**. Adding the one-site-shift condition

```text
S_h^T Theta S_h = Theta
```

raises the combined rank to `8`, leaving dimension **exactly `2`**. Thus the claimed first two cuts, `6 -> 2`, are confirmed.

In the exact heavy basis returned by the projector column space, the complete two-parameter family can be written

```text
Theta(a,b) =
[[ A,  0,  a, -r a],
 [ 0,  A, r a,    a],
 [ a, r a,   b,    0],
 [-r a, a,   0,    b]],

A = (150553/22320) a + (902775/1581193) b,
r = 26093/8928.
```

This display is an exact solution family: substituting it into both the symmetrizer and `S_h`-equivariance equations gives zero entrywise.

Now use the Block 197 completion exactly as defined there,

```text
Y' = B_2 X* pi_0 + B_0 X*^-1 pi_2 + P_h.
```

On the heavy basis `B_h`, orthogonality of the three projectors gives

```text
pi_0 B_h = 0,
pi_2 B_h = 0,
P_h B_h = B_h,
```

and therefore

```text
Y' B_h = B_h,
Y'_h := pi_h Y' B_h = I_4.
```

Consequently `Y'_h^T Theta Y'_h=Theta` is the identity `Theta=Theta`. The round-3 cut leaves the family at dimension **exactly `2`**, not `1`.

Its positive-definite cone is nonempty and genuinely two-dimensional. The Schur/Sylvester conditions reduce exactly to

```text
A > 0,
A b > (1+r^2) a^2,
1+r^2 = 760553833/79709184.
```

For example, the ray `(a,b)=(0,1)` gives the explicit positive-definite symmetrizer

```text
Theta(0,1)
 = diag(902775/1581193, 902775/1581193, 1, 1),
```

or, after positive integer scaling,

```text
diag(902775, 902775, 1581193, 1581193).
```

All four diagonal entries are strictly positive, and the two strict inequalities above show that this point lies in an open cone rather than on an isolated ray. Therefore the PD cone is **nonempty**, but Block 197's completion does **not** select a canonical metric: the proposed one-dimensional canonical ray is **refuted** at this cut.

**2026-08-27 review clarification.** The phrase "at this cut" is load-bearing:
the calculation covers the one-site-shift condition and the declared Block-197
completion only. It does not classify other commuting symmetries or physical
selection principles, and it does not prove that canonicalization is impossible.

## R2-4 — endpoint signs confirmed; five more bisections; zero-crossing mechanism refuted

At `m=9/20`, `T=16`, `X=4`, deep core `t0=3`, the exact endpoint factors are as follows. Each displayed quadratic occurs with multiplicity two.

At the passing endpoint `c=37903/53248`,

```text
q_H(z) = 1155498494926487396 z^2
         -8625331534194669076073 z
         +1155498494926487396,

q_L(z) = 1875213488004622581604 z^2
         -4872593561195570938073 z
         +1875213488004622581604.
```

Both linear coefficients are strictly negative. Both factors are palindromic, have positive discriminant, and have `|b|>2a`, so both reciprocal pairs are real and positive.

At the failing endpoint `c=18961/26624`,

```text
q_H(z) = 26368779493682844 z^2
         +538519351522383710953 z
         +26368779493682844,

q_L(z) = 117129776985466278244 z^2
         -304312535110438520153 z
         +117129776985466278244.
```

The heavy-type linear coefficient is strictly positive while the light coefficient remains strictly negative. Both factors remain palindromic with positive discriminant and squared multiplicity. Thus the stated endpoint sign patterns are confirmed.

Five additional exact bisections give:

| step | exact `c` | primitive heavy linear coefficient `b_H` | result |
| ---: | ---: | ---: | :--- |
| 1 | `75825/106496` | `-137933128608171516036969` | pass |
| 2 | `151669/212992` | `+2206352658131956553649497` | fail |
| 3 | `303319/425984` | `-35306261716317085371212233` | pass |
| 4 | `606657/851968` | `-564863233929048021629206953` | pass |
| 5 | `1213333/1703936` | `-9037516115117032760684071897` | pass |

The tightened bracket is therefore

```text
(1213333/1703936, 151669/212992),
```

of exact width `19/1703936`, a factor `32` tighter than the supplied round-2 bracket.

At the final failing side `c=151669/212992`,

```text
q_H(z) = 7068274392254939356 z^2
         +2206352658131956553649497 z
         +7068274392254939356,

q_L(z) = 479836341843952799153956 z^2
         -1246694110992835465220297 z
         +479836341843952799153956.
```

Both occur with multiplicity exactly `2`; both are palindromic. Their exact discriminants are

```text
Delta_H = 4867992051846108338250759415448622431312577574065 > 0,
Delta_L =  633274546567469442533268055181385192837178968465 > 0.
```

Their exact real-root margins are

```text
|b_H|-2a_H = 2206338521583172043770785 > 0,
|b_L|-2a_L =  287021427304929866912385 > 0.
```

So the failing side does indeed fail **only** in the requested finite-factor checklist: `b_H>0` makes the heavy reciprocal pair negative; palindromicity, real-root discriminants, the light positive pair, and both squared multiplicities remain intact.

However, the stronger proposed mechanism — a **zero crossing** of the heavy trace coefficient — is refuted by the exact probe. The normalized heavy quadratic coefficient `beta_H=b_H/a_H` grows without approaching zero and changes sign through a pole. Exact rational reconstruction from ten independently computed `QQ` points gives

```text
beta_H(c)
 = -2 (1362 c^4 + 800 c^3 - 5529 c^2 - 1600 c + 5448)
      / (400 c^4 + 800 c^3 - 1681 c^2 - 1600 c + 1600).
```

If `b1(c)` denotes the actual two-dimensional matrix trace rather than the monic polynomial's linear coefficient, then `b1(c)=-beta_H(c)`; the denominator and pole are unchanged.

Two points withheld from that reconstruction verify it independently with zero residual:

```text
c=1/2: beta_H = -27607/2019,
c=2/3: beta_H = -98418/2071.
```

Writing the numerator and denominator polynomials as `N(c)` and `D(c)`, respectively, `gcd(N,D)=1`. Exact Sturm counts on the tight bracket give

```text
# roots of D in the bracket = 1,
# roots of N in the bracket = 0.
```

Moreover `N` is positive at both endpoints, while

```text
D(1213333/1703936)
 = 5682916654753563227721/526857457489218503704576 > 0,

D(151669/212992)
 = -1767068598063734839/128627308957328736256 < 0.
```

Thus the observed sign flip is denominator-driven: `beta_H` goes from large negative to large positive through one pole in the bracket. It is **not** the zero of `b_H`/the finite heavy trace. The exact endpoint and failing-side classifications survive; the claimed zero-crossing explanation does not.

Evidence boundary: all endpoint factorizations, discriminants, multiplicities, dimensions, projector identities, PD inequalities, and bisection decisions above are direct exact matrix computations. The displayed `beta_H(c)` law is an exact `[4/4]` rational reconstruction from ten such computations, followed by two withheld exact zero-residual checks and exact Sturm analysis; the attempted direct `32 x 32` inverse over `QQ(c)` was stopped as compute-heavy before completion. Accordingly the pole diagnosis is the round-2 **probe verdict**, not a claimed generic symbolic theorem beyond this reconstructed family.

## Round-2 verdict

| item | adversarial result |
| --- | --- |
| R2-1 | **Confirmed.** The genuine `W4` has the full `(2,2,2,4,4)` factorization above, including one nonreal palindromic quartic, one non-palindromic quadratic, and one non-palindromic quartic. The new-sector factor of `W^2` has zero real roots, so squaring does not realify the quartet. |
| R2-2 | `6 -> 2` is **confirmed**. The `Y'` heavy compression is exactly `I_4`, so the next cut is `2 -> 2`; the PD cone is nonempty and open. A unique PD ray is **refuted under these two declared cuts only**; other selectors are unclassified. |
| R2-4 | Endpoint signs and the final failing-side “trace sign only” checklist are **confirmed**, with five further bisections. The zero-crossing explanation is **refuted by the exact rational probe**: the sign change is consistent with one denominator pole, not a finite trace zero. |
