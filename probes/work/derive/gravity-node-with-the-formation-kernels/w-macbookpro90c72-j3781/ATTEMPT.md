# J:derive:gravity-node-with-the-formation-kernels:a2

Worker `w-macbookpro90c72-j3781`, model `claude-opus-5`, independent attempt 2 of 3.
Checks: `check.py` in this directory, 44 exact checks, `TOTAL: PASS=44 FAIL=0`.
Repository state used throughout: `origin/main` = `abb98a122e`.

## 1. The exact statement attempted

For the gravity node's own kernel slot on `main`, with the node's kernel properties read
off the note that states it:

> (A) Which object the node consumes — a static response or an equal-time two-point
> function — is fixed by the node's statement, not by the reader.
>
> (B) Each of the three formation candidates either reproduces every property of the
> node's kernel, or fails a named one; the failure is exhibited exactly.
>
> (C) For the candidate that survives, the value of `beta` that the node's normalisation
> demands, under the normalisation the task prescribes and under the self-consistent
> alternative — and which part of that value is a property of the state and which part is
> a property of the bookkeeping.

Prior attempt `a3` (`w-jonathonsmac4f50-ja6b4`, refereed GIVEN) left (A) open in its §4:
"Which object the node consumes, the static response or the two-point function, is the
gravity lane's decision." (C) answers a question `a3` did not ask, and corrects the
reading of its two brackets. Its algebra I re-checked independently before building on it
(step 4 below); every identity of `a3` that I use is re-checked in my `check.py`, not
cited.

## 2. The node on `main`, and the properties of the kernel it uses

`docs/NEWTON_LAW_DERIVED_NOTE.md` @ `abb98a122e`:

- L51 `## In-Scope Theorem`; L57 `G(r) = 1/(4 pi r).`; L71 `phi(r) = M G(r) = M/(4 pi r).`;
  L77 `d phi / dr = -M/(4 pi r^2).`; L83 `|grad phi| = M/(4 pi r^2).`
- L61 "the framework's own nearest-neighbor `Z^3` graph-Laplacian Green kernel".
- L64 "That row identifies `G` as the Green kernel `(-Delta_lat)^{-1}` of the linear".
- L44-47 "which establishes `G` as the Green kernel `(-Delta_lat)^{-1}` of the linear
  lattice Laplacian — the lattice potential of a unit point source. Because the kernel is
  the resolvent of a linear operator, the source-linearity `phi = M G` is that kernel's
  response to a source of strength `M`, not an independent assumption."
- L93 lists "the `Z^3` Green-kernel asymptotic from first principles" as out of scope.
- L5 `**Status:** bounded-support potential-kernel algebra; not a retained Newton force-law
  derivation.`

The row it points to, `docs/LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`:

- L28 `(-Delta_lat f)(x) = 6 f(x) - sum_{|y - x| = 1} f(y)`; L31 "Its Green's function
  `G(r) = (-Delta_lat)^{-1}(r)`"; L37 `G(r) -> 1 / (4 pi |r|)  as |r| -> infinity.`;
  L50 `lambda(k) = 6 - 2(cos k_x + cos k_y + cos k_z),  k in [-pi, pi]^3.`
- L5 `**Status:** source-side proposal; independent audit lane only.`; L10 "**Status
  authority:** independent audit lane only."

Properties of the node's kernel, as stated there:

| | property | source |
|---|---|---|
| P1 | it is the resolvent `(-Delta_lat)^{-1}` of a linear operator, and the node's slot is that resolvent's *response to a source* | NEWTON L44-47, L61, L64; MARADUDIN L28, L31 |
| P2 | its symbol is `lambda(k) = 6 - 2 sum_a cos k_a` on `[-pi,pi]^3` | MARADUDIN L50 |
| P3 | `lambda >= 0`, with a single zero in the zone, at `k = 0` | MARADUDIN L50 with L37 (a `1/r` tail needs exactly one zero) |
| P4 | `lambda` is isotropic at leading order: `lambda = |k|^2 - (1/12) sum_a k_a^4 + O(k^6)`, so the first anisotropy is the cubic quartic, an `r^-3` correction | MARADUDIN L88-98; leading-correction note |
| P5 | `G(r) -> 1/(4 pi r)`, with the coefficient `1/(4 pi)` and no direction dependence | MARADUDIN L37; NEWTON L25, L57 |
| P6 | the `1/(4 pi r)` asymptotic is imported, *scoped to this symbol* — it is named out of scope for the note that uses it | NEWTON L93; MARADUDIN L5, L10 |

P6 is the property that decides what a candidate may inherit for free. An import stated
for `lambda(k) = 6 - 2 sum cos k_a` transfers to another symbol only if that symbol *is*
this one, up to a constant.

## 3. Answer to (A): the node's slot is the resolvent, hence the response

**Step 1 (PROVED, from the note's own words).** L44-47 says the kernel is the resolvent of
a linear operator and that `phi = M G` is "that kernel's response to a source of strength
`M`". A static response function is what occupies that slot. An equal-time two-point
function of a driven linear recursion is not a resolvent of any operator in the note:
under the light-cone kernel it is `C = 49 sigma^2 / (E (14 - E))` (step 5), a product of
two resolvents, not one. So the input the node takes from a formation kernel is
`sigma^2 chi`, with `chi` the static response — which is also the object the task hands
the reader (`chi = 7/E`).

This is not a free choice of normalisation convention: it changes the answer by exactly a
factor 2 (step 6), because `C` and `sigma^2 chi` have the same `1/(4 pi r)` tail *shape*
and tail coefficients in the ratio `C/(sigma^2 chi) -> 1/2` as `k -> 0` (CHECKED, L2d).

## 4. The light-cone candidate (iii) through the node

Notation: `E(k) = sum_a (2 - 2 cos k_a) = 6 - 2 sum_a cos k_a`, i.e. `E = lambda`, the
node's own symbol (CHECKED N1, and identical to `sum_a (2 sin(k_a/2))^2`, the Regge
spelling). `phi_7 = (1 + 2 sum_j cos k_j)/7`.

**Step 2 (CHECKED, L1a/L1b).** `7(1 - phi_7) = E` and `7(1 + phi_7) = 14 - E`, exactly.

**Step 3 (CHECKED, L2a-L2d, L3).** `chi = 1/(1 - phi_7) = 7/E`;
`C = sigma^2/(1 - phi_7^2) = 49 sigma^2/(E(14 - E)) = (7/2) sigma^2 (1/E + 1/(14 - E))`;
`C/(sigma^2 chi) = 7/(14 - E)`, which is `1/2` at `k -> 0` and `7/2` at the zone corner;
and `14 - E >= 2 > 0` on the whole zone.

**Step 4 (PROVED).** Candidate (iii) inherits P1-P6 verbatim: `chi = 7/E = 7 lambda^{-1}`
is the node's resolvent times the constant 7. P2, P3, P4 are then the same statements about
the same function (CHECKED N2a, N2b, N3, N4: Hessian `= I`, first anisotropy
`-(1/12) sum k_a^4`, single zero, max 12). P5 follows from P6 *without a new import*,
because the import's scope condition in P6 is met by symbol identity rather than by
resemblance. P1 holds in the strong form: `chi` is a resolvent and its slot is a response.
The second term of `C`, `(7/2) sigma^2/(14 - E)`, has a symbol analytic on the zone with
`14 - E >= 2` (CHECKED L3), so it contributes no power-law tail and `C` has the same
`1/(4 pi r)` shape with coefficient `(7/2) sigma^2` against `7 sigma^2` for `sigma^2 chi`.

**Step 4a (CHECKED, re-check of `a3`).** Before using `a3` I re-derived its S2, S3 and S5
identities independently; my N1, L1, L2, B1 reproduce them, and its two roots are enclosed
again in S5a/S5b below. I find its algebra correct. Its remainder bound
`|H(r)| <= (1/2)(6/7)^{|r|_1}` I do not use.

## 5. Answer to (C): what the node's normalisation fixes

The task prescribes `sigma^2 = A(7 beta)/(7 beta)`, with `A(kappa) = coth kappa - 1/kappa`
the single-site transverse variance per component (and equally the single-site linear
response) at concentration `kappa`.

**Step 5 (PROVED + CHECKED S5a-S5d).** Under the prescribed normalisation, with `kappa = 7 beta`:

- response slot: `sigma^2 chi = [A(7 beta)/beta] G`, so a unit Newtonian coefficient is
  `A(7 beta) = beta`, i.e. `A(kappa)/kappa = 1/7`;
- two-point slot: `C_tail = [A(7 beta)/(2 beta)] G`, so a unit coefficient is
  `A(7 beta) = 2 beta`, i.e. `A(kappa)/kappa = 2/7`.

`A(kappa)/kappa = sum_{n >= 1} 2/(kappa^2 + n^2 pi^2)` (ASSUMED: the standard
partial-fraction expansion of `coth`; bracketed numerically at `kappa = 1` to `~2e-7` in
S5e). Each term is positive and strictly decreasing in `kappa > 0` (CHECKED S4a2), and the
sum tends to `sum 2/(n^2 pi^2) = 1/3` as `kappa -> 0` (CHECKED S4a, exact). Hence
`A(kappa)/kappa` is strictly decreasing from `1/3` to `0`, and each of `1/7 < 1/3` and
`2/7 < 1/3` (CHECKED S4c, S4d) is attained exactly once. This is a one-line replacement
for `a3`'s series lemma, by a different route.

With rigorous interval arithmetic (CHECKED S5a, S5b):
`kappa* in [5.79145, 5.79146]` for `1/7`, `kappa* in [1.63831, 1.63832]` for `2/7`; so
`beta = kappa*/7 in [0.8273, 0.8274]` and `in [0.2340, 0.2341]` (CHECKED S5c, S5d). These
reproduce `a3`'s two brackets, by an independent enclosure.

**Step 6 (PROVED + CHECKED S1, S2a, S2b, S3a, S3b).** The prescription `kappa = 7 beta`
is the statement that the neighbour sum entering a site has magnitude 7, i.e. that the
seven contributing sites are exactly aligned, `m = 1`. Carrying the same site law with the
neighbour magnetisation left self-consistent — `kappa = 7 beta m`, `m = A(kappa)`,
`sigma^2 = A(kappa)/kappa` — gives

    sigma^2 = A(kappa)/kappa = m/kappa = 1/(7 beta)     identically, for every A,

whence `sigma^2 chi = G/beta` and `C_tail = G/(2 beta)`, also for every `A`. The node's
unit coefficient is then **`beta = 1` exactly** in the response slot and **`beta = 1/2`
exactly** in the two-point slot. No property of the single-site law survives into the
answer.

**Step 7 (CHECKED S8a, S8b).** The two bookkeepings are not two states. Setting `beta = 1`
in `kappa = 7 beta m`, `m = A(kappa)` gives `kappa = 7 A(kappa)`, i.e. `A(kappa)/kappa = 1/7`
— the *same* equation as step 5, hence the same `kappa*` and the same `sigma^2 = 1/7`;
likewise `beta = 1/2` reproduces `A(kappa)/kappa = 2/7`. What the node's normalisation
fixes is the state: `kappa*` and `sigma^2`. Converting that state to a coupling is what the
bookkeeping does, and the two exact bookkeepings differ by the factor `1/m* = 1.2087`
(CHECKED S7), a 21% spread, against a quoted bracket width of `1.5e-4`.

**Step 8 (PROVED).** In the prescribed bookkeeping the number `beta = kappa*/7` coincides
with `A(kappa*)`, because the defining equation *is* `A(kappa*) = kappa*/7`. So
`0.82735...` is simultaneously the label `beta` in that scheme and the magnetisation `m*`
the state actually carries — while the scheme assumed `m = 1` to write `kappa = 7 beta`.
The prescribed bookkeeping is therefore self-inconsistent as a mean-field reading, and
consistent only as a quenched reading in which the neighbour sum is an externally held
unit vector. `a3`'s `beta_resp = 0.82734...` is that label; read as a mean-field coupling
it is `m*`, not `beta`. Its `beta_cov = 0.23405...` is `m*_cov/2` on the same reading.

**Step 9 (PROVED + CHECKED S4b, S6a, S6b).** `A(kappa) = kappa/3 - kappa^3/45 + ...`, so
`A'(0) = 1/3`. For `g(m) = A(7 beta m) - m`: `g'(0) = 7 beta/3 - 1` and `g(1) = A(7 beta) - 1 < 0`,
so `beta > 3/7` gives a nonzero solution by the intermediate value theorem; and
`A(x) <= x/3` for `x >= 0` (immediate from the partial-fraction form: every term
`2x/(x^2 + n^2 pi^2) <= 2x/(n^2 pi^2)`) makes `A(7 beta m) <= m` with equality only at
`m = 0` when `beta <= 3/7`. So the threshold is exactly `beta > 3/7`. `beta = 1` and
`beta = 1/2` clear it; the prescribed two-point label `0.2341 < 3/7` does not. That
confirms `a3`'s phase caveat on its two-point root without using its unrefereed long-range
-order threshold `(3/2)(I_0 + I_2)`.

## 6. Answer to (B): the two other candidates, and where they fail

**Step 10 — candidate (ii), backward 3+1, FIRST FAILING PROPERTY: P4/P5 (CHECKED B1-B6).**
With `phi_4 = (1 + sum_{j=1}^3 e^{i k_j})/4`,

    1 - |phi_4|^2 = (1/8) [ sum_j (1 - cos k_j) + sum_{i<j} (1 - cos(k_i - k_j)) ],

the twelve-neighbour (FCC) Laplacian (CHECKED B1; this reproduces `a3`'s S5). P1 holds in
form (it is a resolvent) and P3 holds (six nonnegative terms, each `1 - cos` vanishing only
at 0 in the zone, CHECKED B4) — but P4 and P5 fail, exactly and at leading order:

- the Hessian at `k = 0` is `k^T (4I - J) k / 16`, `J` the all-ones matrix (CHECKED B2),
  with eigenvalues `{1/4, 1/4, 1/16}` — two distinct values, so no orthogonal change of
  coordinates makes it isotropic (CHECKED B3a); `det = 1/256` and the inverse is exactly
  `4(I + J)` (CHECKED B3b);
- hence the `1/r` tail is direction-dependent,
  `G(x) = 2 / (pi |x| sqrt(1 + 3 cos^2 psi))` with `psi` the angle to `[111]` (CHECKED
  B5b), and the amplitude in the level plane is **exactly twice** the amplitude along
  `[111]` (CHECKED B5a).

So no choice of `sigma^2` normalises candidate (ii) to `1/(4 pi r)`: the factor it needs
varies by 2 with direction (CHECKED B6). This is an `r^-1` failure of the node's isotropy,
where the node's own lattice anisotropy (P4) first appears at `r^-3`. The import of P6 does
not cover it either: its symbol is not `lambda` up to a constant. The task's description of
(ii) as "isotropic in the level plane's natural metric" is accurate and is precisely the
problem — the node's metric is the `Z^3` one, and the two are not related by a rotation.

**Step 11 — candidate (i), backward 2+1, FIRST FAILING PROPERTY: P5 (CHECKED I1.0-I1.3).**
Its equal-level kernel does not depend on the level-time momentum `w`, so its inverse
transform in `w` is `delta_{n,0}`: the kernel is supported on a single level. A kernel that
vanishes off one level cannot carry the everywhere-nonzero `1/(4 pi r)` tail P5 demands in
`Z^3`. For the full space-time kernel, `a3`'s S6 (its equal-level kernel is
two-dimensional) I take as GIVEN and do not re-derive.

| candidate | P1 resolvent | P2 symbol | P3 single zero | P4 isotropy to `r^-3` | P5 `1/(4 pi r)` | P6 import in scope |
|---|---|---|---|---|---|---|
| (iii) light-cone 3+1 | holds | holds (`= lambda`) | holds | holds | holds | holds, by symbol identity |
| (ii) backward 3+1 | holds (FCC) | fails | holds | **fails at `r^-1`** | **fails: ratio 2** | fails |
| (i) backward 2+1 | — | — | — | — | **fails: one level** | fails |

## 7. What would finish it

1. **The bookkeeping is the open item, not the arithmetic.** Both schemes here are
   single-site laws in a fixed effective field. The physical `beta` needs the neighbour
   fluctuation carried, not a choice of `m`. As an indication of the size of that
   correction only (ASSUMED, and not licensed: the neighbour deviations are correlated,
   so this is not a bound), treating the seven neighbours as independent gives
   `kappa = beta(7 - 6 sigma^2) = 43 beta/7` at `sigma^2 = 1/7`, hence
   `beta = 7 kappa*/43 ~ 0.943` — between the two exact labels, which is why the spread in
   step 7 should be read as the current precision on `beta`.
2. **The state, not the coupling, is what to quote.** `kappa* in [5.79145, 5.79146]` and
   `sigma^2 = 1/7` are scheme-independent (step 7). A lane that wants `beta` must first
   state the field-to-coupling map it uses.
3. **For candidate (ii)**: nothing repairs the `r^-1` anisotropy by normalisation; only a
   different neighbour set would, which is a different candidate.
4. **P6 remains an import** for (iii) as for the node: neither this attempt nor `a3`
   derives `G(r) -> 1/(4 pi r)`. What is shown is that (iii) needs no import beyond the
   one `main` already carries, and that (i) and (ii) fall outside its scope.

## 8. Caveats

- `A(kappa)/kappa = sum 2/(kappa^2 + n^2 pi^2)` is ASSUMED (standard partial fractions for
  `coth`); it is used for monotonicity, for `A <= x/3`, and for the `1/3` limit. Everything
  it supports is also reachable from `A' (0) = 1/3` plus concavity of `A`, which I do not
  assume.
- The tail amplitude of a quadratic-form symbol,
  `1/(4 pi sqrt(det A) sqrt(x^T A^{-1} x))`, is ASSUMED (the standard anisotropic
  continuum Green function); only the ratio 2 is load-bearing, and the ratio follows from
  `A^{-1} = 4(I + J)` alone.
- Step 1 reads the node's slot off the note's prose. A reader who takes the note's
  "response" sentence as expository rather than definitional would keep `a3`'s open
  question, and would then get `beta = 1/2` rather than `beta = 1` — a factor 2, not a
  change of route.
- The status line of the node's note (L5) says the note is not a retained force-law
  derivation, and the upstream row's status line (L5/L10) says audit lane only. Nothing
  here changes either.
