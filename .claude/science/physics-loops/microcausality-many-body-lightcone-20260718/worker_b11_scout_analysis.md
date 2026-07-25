# Worker A (Opus 4.8 max; workhorse substitution disclosed): block11 scout analysis

> **SUPERSEDED SCAFFOLDING — historical record only.** This file was
> written before (a) the owner landed the rewritten blocks 03-10 on
> `origin/main` and (b) the review rounds that forced the alias lemma
> and the claim narrowing. Its quotations of "block10" are from the
> PRE-REWRITE stack drafts and do NOT appear in the landed
> corner-note; its "action-derived", "full-lane closure", "SAME
> constants", and "supplies both prerequisites" framings are all
> contradicted by the landed note. Read the landed note and
> `REVIEW_HISTORY_B11.md` for the actual claim boundary.

Scope: read EXACTLY the five spec-listed docs, nothing else. All quotes below are
verbatim from those five files. Per-step verdicts use the spec rubric:
**METRIC-AGNOSTIC** = the step uses ONLY (i) a graph metric's triangle inequality
via `diam(S) = max_{u,v∈S} d(u,v)` and/or (ii) the supplied `κ`; **Z3-BOUND** = the
step uses `Z^3`-specific structure (coordination number, `l1` sphere count, `d=3`,
`l1`-as-ambient) that a different graph metric would change.

Note map: N1 = block07 weighted quasilocal class (`...WALK_EXPANSION_LIEB_ROBINSON...2026-07-18`);
N2 = free staggered d-dim dispersion (`...D_DIMENSIONAL...2026-06-12`); N3 = axiom-first
RP two-step positivity (`...2026-05-28`); N4 = block10 corner-class factorization discharge
(`...DISCHARGE...2026-07-18`); N5 = gauged CT quasilocality (`...COMBES_THOMAS...2026-06-13`).

---

## (a) Adversarial metric audit of N1 (block07)

Supervisor claim under test: **"only the class DECLARATION binds `Z^3`."** I audit
every step of N1's hypotheses → chain lemma → weight split → meeting bound → peeling →
assembly → theorem → gates and try to refute it.

| # | Step | Verdict | Load-bearing quote |
|---|------|---------|--------------------|
| 1 | Class declaration / ambient space | **Z3-BOUND** (the conceded one) | "A finite region `Λ ⊂ Z^3` with the ambient `l1` graph metric `d(·,·)` (declared once, used everywhere: `diam(S) := max_{u,v∈S} d(u,v)` is the **ambient** diameter)." |
| 2 | Activity `κ` definition | **METRIC-AGNOSTIC** (parametric in any metric supplying `diam`; the value is SUPPLIED) | "`κ := sup_x Σ_{S∋x} ||h_S|| · |S| · e^{μ·diam(S)} < ∞`" — `diam` is max-pairwise, valid in any metric; `κ` is a supplied number. |
| 3 | Chain lemma | **METRIC-AGNOSTIC** (matches rubric (i) verbatim) | "by induction every site of `S_j` lies within `Σ_{i≤j} diam(S_i)` of `X` (anchor in the overlap, triangle inequality, ambient diameter), so … `Σ_{j=1}^{k} diam(S_j) ≥ d`." — only anchor-in-overlap + triangle inequality + max-pairwise diam. |
| 4 | Weight split | **METRIC-AGNOSTIC** (pure algebra on lemma output) | "`Π_j ||h_{S_j}|| ≤ e^{−μd} · Π_j (||h_{S_j}|| e^{μ diam S_j})`." |
| 5 | Single-step meeting bound | **METRIC-AGNOSTIC** (union bound over SITES + supplied `κ`; NO metric) | "`Σ_{S'∩S≠∅} w*(S') ≤ Σ_{x∈S} Σ_{S'∋x} w*(S') ≤ |S| · κ`" — each `S'` meeting `S` contains ≥1 site of `S`; inner sum ≤ `κ` by definition. |
| 6 | Back-to-front peeling / assembly | **METRIC-AGNOSTIC** (meeting bound + `κ` only) | "`Σ_chains Π_j w(S_j) ≤ n_X^w · κ^{k−1} ≤ |X| · κ^k`, `n_X^w := Σ_{S∩X≠∅} w*(S) ≤ |X|κ`". |
| 7 | Theorem display + constants | **METRIC-AGNOSTIC** | "`||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X^w/κ) · e^{−μd} · (e^{2κ|t|} − 1)`" with "constants depending only on `||A||`, `||B||`, `n_X^w ≤ |X|κ`, `κ`, `μ`, `d` — not on `|Λ|` and not on the site dimensions." |
| 8 | Velocity readout | **METRIC-AGNOSTIC** | "Velocity readout: `v ≤ 2κ/μ`". |
| 9 | Consistency reduction / slack ladder (Q5) | **Z3-BOUND** (NOT load-bearing for the theorem, but IS an advertised result) | "the hypothesis gives `κ ≤ 12Je^μ` (`6` bonds per site × `|b| = 2` × `e^μ`)"; "the meeting bound's union count gives `12` where the true count of distinct bonds meeting a bond is `11` … removes the self term for `10`." — `6`, `12`, `11`, `10` are `Z^3` coordination/incidence numbers. The abstract's "envelope ratio of exactly 6/5" rides on the `6`. |
| 10 | Closed-form instance `κ_3D` (Q6) | **Z3-BOUND** (`κ_1D` is 1d-generic) | "with the `l1` sphere count on `Z^3` `N_3(r) = 4r^2 + 2` (gated by enumeration at two radii), `κ_3D = 4J_0 · ρ(3 + ρ^2)/(1 − ρ)^3`, `κ_1D = 4J_0 · ρ/(1 − ρ)`". The `3D` closed form is a `Z^3` `l1` sphere-count computation of a SUPPLIED `κ`; it does not feed the theorem. |
| 11 | Fermionic lift | **METRIC-AGNOSTIC** | "The block04 sibling's graded locality lemma is support-size-blind: even elements of disjoint support commute regardless of range." — no metric. |
| 12 | Disposition of pure-exponential no-go | **METRIC-AGNOSTIC** | "the decay `e^{−μd}` is extracted from each chain **before** any summation over intermediate supports (the weight split), and the peeling sums only the site-weighted activity per step — the reproducing ratio is never formed." |
| 13 | Runner gates | **MIXED** | Z3-BOUND gates: "the `l1` sphere counts at `r = 1..4`; the bond meeting counts `12`/`11`/`10`". METRIC-AGNOSTIC gates: "the ALL-SUBSETS peeling gate", "chain-lemma reach on mixed-size segment families", "the `2^{k+1}κ^{k−1} = (2/κ)(2κ)^k` resummation", "`t = 0` tightness". |

**Verdict on the supervisor claim.** DEFENSIBLE-with-a-caveat, not clean. The
hypotheses-FORM → chain lemma → weight split → meeting bound → peeling → theorem →
velocity chain (rows 2–8, 11–12) is genuinely metric-agnostic: every step uses only
triangle-inequality-via-max-pairwise-`diam` and the supplied `κ`. So the THEOREM
transfers to any graph metric verbatim. **But the literal claim "only the DECLARATION
binds `Z^3`" is REFUTED**: rows 9 (slack ladder: `6` bonds/site, `12/11/10`) and 10
(`κ_3D` via the `Z^3` `l1` sphere count `4r^2+2`) are additional, non-declaration
places where `Z^3` is load-bearing FOR THOSE DISPLAYED RESULTS — and one of them, the
"6/5" envelope ratio, is advertised in the scope abstract. The honest resolution:
metric-agnostic THEOREM; two `Z^3`-specific instance/consistency layers reported
alongside it. The block11-relevant subtlety (developed in (f)) is that the
metric-agnosticism is "modulo a SUPPLIED `κ` in the `l1` metric," and producing that
`κ` at `d ≥ 2` from the CT kernel is where dimension genuinely re-enters.

---

## (b) N2 conventions (free staggered d-dim dispersion)

**What is action-derived — ONE-PARTICLE ONLY, no many-body object.** Full Statement:

> "On the free `U = 1` staggered surface, with real `m > 0`, d spatial axes, even
> spatial periods, and the same two-step RP blocking in time, the action-derived
> two-step transfer is diagonal after the standard reduced momentum/two-site-cell
> transform. For every full Brillouin-zone momentum `p in T^d`, the forward decaying
> one-particle eigenvalue is `lambda_-(p) = exp(-2 E_d(p))`,
> `E_d(p) = arcsinh(sqrt(m^2 + sum_{mu=1}^d sin^2 p_mu))`."

Confirmed one-particle-only by the Boundaries: "The theorem concerns the action-derived
**one-particle** two-step transfer and the corresponding free log-transfer symbol." No
`Γ(t)`/`T_hat^2`/Fock object appears in N2 — the many-body second quantization is N3's
job. N2 also states "the reconstructed free log-transfer Hamiltonian has symbol `E_d(p)`."

**Mode set — cell doubling in d dims → `2^d` components per reduced momentum; taste.**

> "A reduced momentum sector is labelled by `k in (-pi/2, pi/2]^d` and a cell/taste
> corner `r in {0,1}^d`, representing the full momentum `p_r = k + pi r`."

So **`2^d` two-site-cell corners per reduced momentum**. The Clifford carrier is `2^d`-dim:
"`Gamma_mu |r> = (-1)^{r_mu} |r xor s_mu>`" with "`Gamma_mu^2 = I`,
`Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0, mu != nu`", giving
"`H_hop(k)^2 = - (sum_mu sin^2 k_mu) I`" — flagged as "the only dimension-dependent
algebraic step." Taste: "The formula is taste-degenerate across the `2^d`
two-site-cell corners because `sin^2(k_mu + pi r_mu) = sin^2 k_mu`."

**Boundary conditions — even periods = torus.** "d spatial axes, even spatial periods";
momenta run over the full torus "`p in T^d`"; folding uses "translations through two
sites in every spatial direction," which requires even periods. So YES, torus `T^d`.

**Exact `E_d` display.** `E_d(p) = arcsinh(sqrt(m^2 + sum_{mu=1}^d sin^2 p_mu))`;
decaying channel `lambda_-(p) = exp(-2 E_d(p))`. Radicand is **sum-of-squares** of the
`sin p_mu` (i.e. `sum_mu s_mu^2` in operator terms) — see the (e)/(f) carrier trap.

**Positivity statements — N2 makes NONE.** N2 exhibits only the real-positive decaying
one-particle eigenvalue `exp(-2 E_d) ∈ (0,1]` and the analytic kernel bound; it does NOT
assert `T_hat^2 = B^dag B` many-body positivity (that is N3). Its parity/kernel results:
"`h(z) = 0` whenever any coordinate `z_mu` is odd" (π-periodicity), and
"`|h(z)| <= C_d(eta, m) exp(-eta ||z||_inf)`, `C_d(eta, m) = sqrt(m^2 + (d-1) + cosh^2 eta)`",
"in the `l1` metric one may use any rate below `arcsinh(m)/d`; a concrete uniform choice
is `r_d(m) = arcsinh(m)/(2d) > 0`."

**Own non-claims.** "It does not prove gauged or interacting log-transfer locality." "The
kernel is quasilocal, not finite-range. The even-offset rule is a parity support rule, not
compact support." "The sharp anisotropic rate away from coordinate axes remains an open
target." "No literature values, external constants, empirical targets, or new comparator
numbers are imported."

## (c) N3 per-mode `Γ` construction — d-BLIND as written

The construction depends only on the diagonal one-particle SPECTRUM `{λ_p}`, not on spatial
dimension. Defining property (mode-indexed, no `d`):

> "The defining property of the second-quantization functor `Gamma` is that it carries a
> one-particle operator `K` (here diagonal, `K e_p = lambda_p e_p`) to the many-body
> operator `Gamma(K)` on the Fock space `H = tensor_p {|0>, |1>}` that fixes the vacuum
> and intertwines the creation operators, `Gamma(K) |vac> = |vac>`,
> `Gamma(K) a_p^dag = lambda_p a_p^dag Gamma(K)`."

Solution (per-mode tensor product — d-blind):

> "For a diagonal kernel these two requirements have a unique, explicit finite-dimensional
> solution: the per-mode tensor product … `Gamma(t1^(2)) = tensor_p diag( 1, lambda_p )
> = exp( -2 a_tau H_hat )`, `H_hat = sum_p E(p) a_p^dag a_p`."

The occupation tensor factors `{|0>,|1>}` per mode and the creation-operator intertwiner
carry **no reference to spatial dimension** — they act mode-by-mode on whatever diagonal
spectrum is fed in. The ONLY 1d-specific object in N3 is the KERNEL's dispersion
"`E(p) = arcsinh( sqrt( m^2 + sin^2 p ) )`" (single `sin^2 p`, "`1+1d`, `L_s` spatial
sites, periodic"), which N2 already generalizes to `sum_mu sin^2 p_mu`. So: **the `Γ`
functor is d-blind; only the dispersion it is fed is 1d in N3 and d-dim in N2.** Note the
explicit `a_tau`: "`H_hat = -log(T_hat^2) / (2 a_tau)`" — carried symbolically in N3
(unlike N2's silent `a_tau = 1` inside `exp(-2 E)`); see the `a_tau` trap in (f).

---

## (d) N4 (block10) open-item needles — the exact sentences block11 will answer

**"`d = 3` NOT claimed" (two occurrences):**

> "**The `d = 3` discharge is NOT claimed** — the corner notes land the factorization
> at `d = 1` only, and a `3+1d` free-fermion second-quantization surface does not
> currently exist in the repo (named open)."

and in the scope abstract:

> "the `d = 3` discharge is NOT claimed and is named open — no 3+1d free-fermion
> second-quantization surface currently exists in the repo".

**"cycle-metric" open item (periodic-boundary blow-up):**

> "**Boundary scoping (review-found):** the transfer engine's spatial carrier is
> periodic; a periodic wrap term has cycle-metric kernel size `O(Ke^{−η})` but AMBIENT
> diameter `L − 1`, so its site-weighted activity `≥ 2Ke^{−η}·e^{μ(L−1)}` grows without
> bound in `L` (gated) — the volume-uniform envelope is therefore claimed for the
> OPEN-BOUNDARY restriction of the corner family only; the cycle-metric reformulation
> of the block07 class is named open."

closed by: "the cycle-metric class is named open."

**The load-bearing 1d crutch block11 must replace at `d ≥ 2`** (this is why the block10
envelope was clean and why d=3 is hard):

> "in one dimension there is no metric conversion (`l_1 = l_∞`), the shell count is `2`
> per distance, and with the CT kernel bound the block07 activity obeys … per channel:
> `κ_k ≤ K_k + 8K_k·x_k/(1 − x_k)`, `x_k = e^{−(η_k−μ)}`".

and the embedding it uses to invoke block07's `Z^3` class from a 1D chain:

> "a 1D **open** chain embeds in `Z^3` as an axis, so the block07 class and display apply
> verbatim to the embedded family."

## (e) N5 (CT) kernel bound — dimension-parametric, confirmed; free anchor lives in N2

**`Const(m,d)`, `B(2,d)`, rate — all carry `d` explicitly (G5):**

> "`|| <x| h[U] |y> ||  <=  Const(m, d) e^{-gamma_CT ||x - y||_inf}`,
> `gamma_CT = min(1/2, (m^2/2) / (2 e (m^2 + d^2) B(2, d))) > 0`, `B(2, d) = 5^{d-1} * 6`",
> "with `Const(m, d) = (|Gamma|/2 pi) (sup_Gamma|f|) (2/eta)` finite".

band constant (G4): "`B(R, d) = sum_{0 < ||r||_inf <= R} |<u, r>| = (2R+1)^{d-1} R(R+1)`",
"`B(2,1) = 6`, `B(2,2) = 30`", explicitly "**dimension-aware** … it is *not* the
dimension-blind `2R`." Metric is **`l∞`/sup**: "`||.||_inf` is the sup metric."

**Free `U=1` anchor at GENERAL `d` is claimed in N2, NOT N5.** N5's explicit free
reduction is `d = 1` only: "(G7) `U = 1` / `d = 1` reduction. At `U = 1` (or any `d = 1`
background) the symbol of `D` is `m^2 + sin^2 p` and `h` recovers the landed free
dispersion `arcsinh(sqrt(m^2 + sin^2 p))` exactly, with measured kernel rate
`arcsinh(m)`." The general-`d` free dispersion `E_d = arcsinh(sqrt(m^2 + Σ sin^2 p_μ))`
is N2's Statement. **Carrier trap (N5 flags it itself):** N5's PRIMARY object is
**square-of-sum** "`D[U] = m^2 I + ( sum_{mu=1}^d s_mu[U] )^2`", whereas "The free note's
declared `d >= 2` carrier is instead the **sum-of-squares** `D_ss[U] = m^2 I + sum_mu
s_mu[U]^2`; it differs from (1) by flux cross-terms `sum_{mu != nu} s_mu s_nu` and
coincides with (1) at `d = 1`." So N2's free d-dim dispersion = N5's sum-of-squares
robustness carrier `D_ss` (G9), NOT N5's action-faithful primary `D`; they agree only at
`d = 1`. N5 keeps locality carrier-robust ("(G9) Carrier robustness … the same
quasilocality conclusion"), but the two radicands are genuinely different operators at
`d ≥ 2`.

---

## (f) Proposed needle set for block11, with mismatches/traps

**What block11 appears to be: the `d ≥ 2` (and/or cycle-metric) discharge that block10
named open.** The clean statement it can aim for: at general `d`, the free/fixed-background
reconstructed many-body Hamiltonian `H_MB = dΓ(h[U])` generates `e^{iH_MB t}` obeying the
block07 (N1) LR display — provided a `d`-correct `l1` activity `κ` is supplied. The N1
theorem itself is metric-agnostic (see (a)); the work is entirely in SUPPLYING `κ` at `d`.

**Proposed needle set (presence-checked verbatim sentences, per family discipline):**
- N2: the Statement `E_d(p) = arcsinh(sqrt(m^2 + Σ_{μ=1}^d sin^2 p_μ))`; the `2^d`
  taste-corner sentence; `C_d(η,m) = sqrt(m^2 + (d-1) + cosh^2 η)`; the `l1` rate
  `arcsinh(m)/(2d)`; "the only dimension-dependent algebraic step."
- N3: the intertwiner `Γ(K) a_p^dag = λ_p a_p^dag Γ(K)` and the per-mode tensor product
  `Γ = ⊗_p diag(1, λ_p) = exp(-2 a_tau H_hat)` (the d-blind functor).
- N4: "The `d = 3` discharge is NOT claimed"; the cycle-metric open sentence; the
  per-channel envelope `κ_k ≤ K_k + 8K_k x_k/(1-x_k)`; the "`l_1 = l_∞`" 1d-crutch
  sentence; the "1D open chain embeds in `Z^3` as an axis" sentence.
- N5: `Const(m,d)`, `B(2,d) = 5^{d-1}·6`, `gamma_CT` display; the square-of-sum vs
  sum-of-squares carrier note; "`||.||_inf` is the sup metric"; G9 carrier robustness.
- N1: the chain lemma; the `κ` definition; the theorem display and its "constants
  depending only on … not on `|Λ|` … not on site dimensions"; the `Z^3` `l1` sphere count
  `N_3(r)=4r^2+2` (flag as the instance-only `Z^3` re-entry point).

**Traps / mismatches (glyphs, factors, `a_tau`, mode counts, metric, carrier):**
1. **METRIC (the crux).** N5 kernel decays in `l∞` (`||x-y||_inf`); N1 `κ` weights by `l1`
   `diam`. Block10 got a clean envelope ONLY because "`l_1 = l_∞`" in 1d. At `d ≥ 2`,
   feeding the CT `l∞` bound into N1's `l1` activity needs an `l∞→l1` conversion that
   injects `d`-factors — this, not anything inside N1, is where the "metric-agnostic"
   theorem meets real `d`-dependence. Do NOT copy the block10 envelope to `d ≥ 2`.
2. **CARRIER.** N2 free d-dim = sum-of-squares (`Σ s_μ^2`); N5 primary = square-of-sum
   (`(Σ s_μ)^2`). Coincide only at `d = 1`. Don't feed N2's `E_d` into N5's primary
   carrier at `d ≥ 2` as if identical; use N5's G9 sum-of-squares branch for the match.
3. **`a_tau`.** N3 carries `2 a_tau` symbolically; N2/corner use `exp(-2E)` i.e. silent
   `a_tau = 1`; N5 uses `-log(T_hat^2)/(2 a_tau)`. Block10 already pinned `a_tau = 1`;
   block11 must keep that pin at `d` or every downstream constant is off by the `a_tau`.
4. **GLYPH `T_hat^2`.** Many-body in corner/engine notes, one-particle in N5's `h`-def
   (block10 disambiguated this). N2 uses `λ_-(p)`, N3 uses `t1^(2)(p)` (one-particle) vs
   `T_hat^2 = Γ(t)` (many-body). Track: `t`/`t1^(2)`/`λ_-` = one-particle; `H_MB = dΓ(h)`,
   `T_hat_MB^2 = Γ(t)` = many-body.
5. **MODE COUNTS — three distinct multiplicities, do not conflate.** `2^d` taste corners
   (N2, cell doubling) vs `2` corners (N3, 1d `r∈{0,1}`) vs `3` generation channels (N4,
   circulant masses `λ_k`). The per-channel envelope aggregation in N4 sums over the `3`
   generation channels; the `2^d` taste degeneracy is a DIFFERENT index and multiplies the
   mode count, not the channel count.
6. **FACTOR `8` in `κ_k ≤ K_k + 8K_k x/(1-x)`** is the 1d shell-count-`2`-per-distance
   coefficient. At `d`, the shell count is N1's `l1` sphere count `N_d(r)` (`N_3=4r^2+2`),
   so the `8` becomes a `d`-dependent, `r`-summed coefficient — this is exactly the N1
   row-9/row-10 `Z^3` content re-entering when `κ` is recomputed at `d = 3`. The
   free-bilinear map `κ = 2 W_mu` (rates `2κ = 4W_mu`) is metric-agnostic and safe to reuse.
7. **`B(2,d)` ≠ sphere count.** N5's band count `B(2,d)=5^{d-1}·6` (an `l∞` range-2
   band-enumeration for the CT twist) is NOT N1's `l1` sphere count `4r^2+2`; both are
   "`d`-aware" but count different things. Don't cross-substitute.

## (g) LIMITS

- Read exactly the five spec files; I did NOT open N1's siblings (block04/block08, the
  free-bilinear/exp-decay notes), the corner free/fixed-background notes, the engine note,
  or any runner. Claims about those are only as N1/N4/N5 QUOTE them; I could not verify
  their internals (e.g. whether the corner free note's displayed `T_k^2 = Γ(t_k)` is truly
  1d-only, or whether an engine-note d-dim surface exists — N4 asserts it does not).
- "Metric-agnostic" here means "the step's algebra uses only triangle-inequality-via-diam
  and supplied `κ`," a STRUCTURAL reading of the prose; I did not re-run N1's runner or
  re-derive its gates, so a hidden `Z^3` assumption inside a gate I marked agnostic cannot
  be fully excluded (I flagged the two gates that are explicitly `Z^3`).
- The refutation in (a) is the strongest I found against the LITERAL supervisor claim; it
  nicks only N1's instance/consistency layers (rows 9–10), not the theorem. I did not find
  any `Z^3` dependence inside rows 2–8/11–12, but absence-of-proof ≠ proof-of-absence.
- I did not attempt the block11 derivation (the `l∞→l1` conversion, the `d`-correct sphere
  count, the cycle-metric reformulation, or a `3+1d` second-quantization surface); (f) only
  scouts where the work and traps lie. Whether an `l∞→l1` conversion preserves
  volume-uniformity at `d ≥ 2` is OPEN and is the first thing the math-build worker should test.
- Convention pins (`a_tau = 1`; glyph disambiguation; carrier choice) are reported as N4/N5
  state them; if block11 changes any pin, every downstream constant must be re-audited.
