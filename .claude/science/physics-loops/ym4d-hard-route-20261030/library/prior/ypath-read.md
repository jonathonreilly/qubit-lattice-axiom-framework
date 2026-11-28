# Repo search

The lead's `library/prior/repo-search-2026-11-08.md` searched `origin/main` and
the open YM4D PR branches (#10114, #10133, #10134, #10141) for other target
suppliers. Its closest collar match is the soft-route H-O item: a conditional
carrierwise oscillation/collar bound in `pr/10141:R/library/in1.md` 86–90,
197–203. It is not the real finer-collar path or any of the six Y-PATH inputs.
The same search records relevant geometric prerequisites and conditional
methods, but no supplier of these six inputs. I checked the lead's digest,
`library/open-registry.md` row Y-PATH, and the named source passages below.
The registry assigns this reading to Y-PATH; nearby owner rows are recorded
there as related inputs, not as a duplicate owner of this reading.

The lead's search also consulted the Sussman–Alpoge outline index. I fetched
the outline and CA-I at the pinned commit once and grepped the full-read index
and obligations for collar, joined-datum, and real-datum objects. The closest
outline entries are SA 9783–9789 (joined sequence/datum and a sketched local
background comparison) and 9913 (sketched collar comparison from lift defects
and response decay). I checked the neighbouring index rows and those source
lines. They describe a related collar mechanism, but do not supply this Y
path, the three estimates below, or the six stated applications. CA-I index
items 4.12–4.19 did not yield a matching real-finer-collar-path supplier.
Credit for the outline and account: Ethan Sussman and Levent Alpoge, with
Claude and Codex as authors of their text. I use no Sussman–Alpoge result as a
proof of a Y statement here.

`origin/main` was fetched and I read rule 9 of
`docs/ai_methodology/SCIENCE_WORKFLOW.md`; the planning branch was read for its
dispatcher rules. The checkout is at `399dd1733df81bd95fcaf8869cebde8a7736673e`.

# Y-PATH source reading

This is a reading of the cited source text `YM4_1400.tex`, not a proof check,
audit, or status change. “PROVED IN Y” means that Y supplies steps for the
statement; it does not certify those steps.

## 1. `hi:real-finer-collar-path`

**Statement and hypotheses (Y 64860–65017).** At a transition (j\to q=j+1),
Y takes (Y=Z''_q) and the exterior collar (K\subset\Omega_q^c\cap X).
It fixes an admitted prospective real datum and its regular critical
configuration (U^+), in the approximate-collar-test frame. The stored common
rows and that frame stay fixed, while finer collar variables vary. Y assumes
the fixed small regularity ceiling of the background theorem, with room for
constants depending on (L). The conclusion is a real continuation path for
the old datum/orbit over the full product ball allowed by the approximate
collar bound, together with the crossing-defect estimate (E1).

**Steps in Y's order.**

1. Y defines (V^0) by reading (U^+) on the preceding determining set.
   The joined sequences have the same bare domain and agree except for the
   enlargement at level (q). It checks nested restriction of the no-inward
   determining sets, transfers regularity of (U^+) to the old units, and
   identifies each old level-(q) datum plaquette with the plaquette of
   \(\mathcal M^q U^+\), including second-kind completions. The old constraints
   at (V^0) imply the new constraints, so (U^+) is critical for the old
   set at (V^0). **PROVED IN Y** (64860–64893).

2. Y keeps inherited rows fixed and varies newly imposed coarse rows. Their
   endpoint blocks are outside the old \(\Omega_q\) and inside the old
   level-(j) member. The approximate collar test and common fine rows bound
   nonpivot changes by (2\delta'_j). **PROVED IN Y** (64894–64909).

3. For a pivot, Y uses the straight corridor product (q) as coordinate and
   gives the two logarithmic averaging formulas, with
   \(\sum_a\alpha_a=1-L^{-3}\); if neither formula applies, (F(q)=q).
   It compares the induced and actual contours, obtains
   \(d(H_a,W)\le C(L)(e+\delta'_j)\), and uses the triangle inequality in
   the logarithmic case (or (q=W) in the other case). A sufficiently small
   regularity ceiling places the double block on the regular branch; the
   regular one-row inverse then gives the sharper (C(L)\delta'_j) pivot
   increment. **PROVED IN Y** (64910–64959).

4. Y interpolates the nonpivot logarithms and solves the pivot equation with
   (W) fixed. The regular inverse bounds the path velocities by
   (O_L(\delta'_j)); the endpoints are the induced and actual old datum.
   Y says the path lies in the real continuation polydisc, so the old critical
   orbit exists along it. It extends the construction to the full real product
   ball and explicitly says this construction does **not** use the preceding
   guard on that ball. **PROVED IN Y** (64960–64978).

5. Y writes the old orbit as a Landau response to the plain determining
   logarithms, bounds the response and first difference with the stated
   exponential weights, and sums the separated row tops (at most eight rows
   per top). It obtains the weighted response on the old level-(j) plaquette
   carriers at the new prepared face, then states E1. **PROVED IN Y**
   (64979–65017).

The regular background/orbit and its fixed ceiling are inputs to this
argument. Y does not use a citation in this paragraph for the real averaging
formula or the one-row inverse; it gives their formulas and the comparison
steps in the paragraph. The separate background admission is `bgc:proper-background`
(Y 35634–35675 onward), stated with uniform constants and a proof beginning
at 35651; its conclusion is existence and regular uniqueness for the admitted
real datum.

## 2. The three estimates

### (E1), Y 65010–65014

\[
 \left|\,|\partial U^-(p)-\mathbf1|
             -|\partial U^+(p)-\mathbf1|\,\right|
                        \le C_L\delta'_jL^{-2j}.
\]

The constant is `C_L`; this display names dependence on `L` and does not spell
out any further dependence. The preceding path uses the fixed geometry and
regularity ceilings. It holds on the complete
stencil/old level-(j) plaquette carriers at the new prepared face
(Y 64990–65014). The real node gauge preserves the defect norm. The label is
`hi:real-crossing-response`; the preceding paragraph supplies the response
estimate and the reserve comparison at 65006–65017. **PROVED IN Y.**

### (E2), Y 64239–64245

\[
 C_L\frac{\delta'_j}{\varepsilon_j}
 (1+\sqrt{j-i})e^{-c(M/M_1)(j-i)}
 \varepsilon_i L^{-2i}.
\]

Y calls this the upper bound for the weighted response from changed collar
rows, on an old shell of index (i<j) already present at stage (j)
(64234–64245). Thus the read is a shell plaquette/defect at scale (i).
The prefactor is `C_L`; this display names dependence on `L`, and the decay
rate uses `c(M/M_1)`. Y says the threshold
ratio contributes (1+\sqrt{j-i}) and shell separation gives the exponential,
then chooses (M/M_1) and uses \(\delta'_j/\varepsilon_j\) to fit the reserve
(64246–64251). No separate label is attached to this display; it is derived
in the surrounding preceding-guard comparison. **PROVED IN Y.**

### (E3), Y 64451–64455

\[
 C_L\delta'_j L^{-2s}e^{-c(M/M_1)(j-s-1)}.
\]

This is the defect change on the stencil of a newly added crossing of
\(\partial Z''_{s+1}\), assigned to shell (s) and retained in subsequent
guards (64437–64455). The prefactor is `C_L`; this display names dependence
on `L`, and the exponential rate is proportional to `M/M_1`, with bounded
stencil enlargement. Y explicitly
cites `hi:real-crossing-response` at 64451. Its proof/status is E1 above:
the detailed response and stencil estimate are given in Y 64990–65017.
**PROVED IN Y.**

## 3. `mb:real-collar-datum` and `mb:real-collar-norm`

Y 13283–13396 assumes a real datum (V) whose tested holonomies are within
\(\varepsilon_1\) of one; a fixed collar width \(\mu\); the no-inward
determining sets, separation and weighted-response floors of the real
background theorem; at least (6\rho) sites in each direction at the top
level; and radii admitted by the joined response polydisc. (U) is a critical
configuration in the regular orbit of (V); (U_W^\circ) is the normalized
representative for the localized datum (V^W).

- **`mb:real-collar-datum` (13341–13349).** The induced datum differs from
  (V^W) by a logarithmic collar datum (B), zero away from collar rows, with
  \(\|B\|_\infty\le
  2\pi C_{\rm lift}B_3\varepsilon_1/[3(L^2-1)]\). Y obtains this from the
  local curvature bounds, the finite alignment estimate, the gauge, and the
  sum of the level-(q<j) curvature bounds. It puts (tB) in the response
  polydisc and identifies the endpoint orbits by restriction covariance and
  regular uniqueness. **PROVED IN Y, conditional on the stated background
  admission/uniqueness inputs.**
- **`mb:real-collar-norm` (13350–13396).** For the normalized response
  (f=\mathcal H_W(B)), Y gives
  \(\mathsf N_x(f)\le C_\mu\varepsilon_1
  e^{-\delta_0d_{\mathbf B}(y,W^c)/2}\). It bounds the point response, sums
  row weights, compares ambient and joined distances, and integrates the
  derivative along (tB); the stated distance conversion costs at most
  (e^{6\mu\delta_0}). **PROVED IN Y, conditional on the response and
  operator bounds it invokes.**

Their global use at 65019–65067 fixes (S_g=\mathcal M^jU_m^{(n+1)}) and
(S_X=\mathcal M^jU_{m,X}^{(n+1)}), includes full averaging carriers and
double blocks, uses the joined comparison and stencil clearances, and obtains
\(\sup_b|S_g(b)S_X(b)^{-1}-\mathbf1|\le
C\varepsilon_\star e^{-cM\check R_m}=o(\delta'_j)\) on the collar read set.
Y states the frame-drift and \(\check R_m\) conditions for the last equality.
**PROVED IN Y** (65019–65067), using the two collar estimates above.

One-level citation follow-up:

- `mb:restriction-identity`, Y 12920–12955: Y reduces restriction to
  regular-critical uniqueness and proves the common-region background nesting;
  the uniqueness theorem is an explicit condition, not reproved by this
  identity.
- `mb:transported-bond` and `mb:rigidity-sum`, Y 10833–10930: Y gives the
  transported-link comparison and sums its level errors geometrically; the
  argument is supplied under its regularity and alignment hypotheses.
- `mb:extended-source`, Y 13178–13215: the displayed response-decay estimate
  follows from the stated weighted Schur row-sum bound; its operator row-sum
  premise is an input.
- `bgc:proper-background`, Y 35634–35675 and proof beginning at 35651: Y states
  real background existence/regularity/uniqueness and starts a proof with the
  constant order. This is an admitted-background input to the collar steps.

## 4. Global promoted-datum bound and support

Y 65417–65563 reads the history's carried fields and actual determining links;
completed bonds use the lower field averaged on their full double block, with
the retained constraints identifying these reads with test values. It assigns
each test location to its least-level departure and names the supplying
ordinary density, positive-stage, approximate collar, restored-core, or
retained constraint tests. On complete footprints those tests give
\(2\psi_l\varepsilon_l\), with \(\psi_l=O(1)\) for ordinary witnesses or a
restored core and \(\psi_l\le C(\log\theta_l)^r\) on remade shells; Y says
the latter uses (L_\flat^2<L) and a compressed interval. This gives (Ce_l).

Y then fixes an entering point on the retained tests and constraints with
coarse target (V_q). Its profile estimate gives the levelwise bound and,
for newly promoted level-(q) tests, the actual averaging constraints identify
the tested holonomies with \(\mathcal M^q U_{\rm in}\); the complete order-(q
carrier stays in the unchanged level-(j) member. Y gets (C(L)e_j\le
C'(L)e_q) and normalized curvature/current bounds (Ce_s) in layer (s).
It says the localized artificial face lift does not enter this *global*
calculation.

The support question is fixed by these sentences:

> “Fix an entering point on these retained tests and on the constraints with
> coarse target \(V_q\). This is the input for varying the collar. To remove
> the preceding guard on an enlarged support, use the separate comparison in
> \cref{hi:preceding-guard-support}.” (Y 65486–65491)

> “For that guard and the later prospective guards, use the promoted datum
> bounds on the entering support. These bounds, \(Ce_q\) in each layer (q),
> use the actual promoted averages before their delta functions are
> integrated.” (Y 134201–134205)

So the bound is asserted pointwise on the retained-test/constraint entering
support, where the preceding guard is still among the carried conditions. Y
does not claim this same support bound after dropping that guard: it explicitly
requires `hi:preceding-guard-support` for the enlargement. “Before their delta
functions are integrated” specifies the pointwise use in the integration; it
does not itself enlarge the support.

The one-level follow-up for `hi:real-datum-profile` is Y 15316–15777: with
separated geometry and a regular critical field it derives a local radius
inequality from nearby datum tests, applies the weighted maximum estimate, and
states the layer profile. The steps are present. `mb:datum-profile` and
`mb:weighted-maximum` are explicitly defined/proved at Y 12471–12505. The
preceding-guard label begins at Y 64221–64232: it says earlier guards read
only (X\cap\Omega_m^c), two level-(m) cells inside (X), with the
artificial bare rim only in the final guard; the comparison is continued in
the surrounding guard argument (including the shell-response steps at
64234–64455). Y supplies steps for that comparison; it is not only a bare
support assertion.

## 5. Four shorter arguments and outer-layer plaquette reads

### Top density, Y 64699–64789 — Y-DENS

**Statement/status.** The lower density test passes on the inset-positive real
collar chart. Y supplies the halo placement, a case split for plaquettes
relative to the new prepared box, local regularity/Hölder comparison, real
response, and joined-background error budget. **PROVED IN Y.**

**Plaquette-bound locations.** Y places the four-layer halo in the top inset
of `X`, inside `Omega_q^c intersect X` (64701–64716). The bounds used on
plaquettes in that halo are:

- if (q\le k_0+1), plaquettes inside the new shell use the new shell bound
  \((1-3\beta_s/4)\varepsilon_jL^{-2j}\) (64718–64724);
- plaquettes outside it use the deep exterior bound
  \((1-\beta_s/2)\varepsilon_qL^{-2q}\) (64725–64727);
- astride plaquettes are read by the preceding guard and get the crossing-test
  shell bound (64727–64737);
- if (q>k_0+1), plaquettes in the two wall layers use the exterior bound
  (64739–64752); astride plaquettes are translated into layer (j) and
  compared using local regularity/Hölder and the plaquette-log remainder
  (64753–64770).

These are the explicit halo/top-inset plaquette bounds in this argument; the
passage does not further identify those plaquettes as lying on the artificial
bare rim. Y next transfers the margin to the preceding background and the
density test box (64772–64789). It does not use a sharp bound at the artificial
bare rim of `X` here.

### Contour indicators, Y 64791–64810 — Y-CONT

**Statement/status.** The old exterior-belt contour indicators pass at their
original \(\varepsilon_j\) threshold, and the soft density remains in the
integral. Y places the order-(q) blocks between the first and third exterior
layers wholly in the collar; the new gauge insertion starts beyond the third
layer. Tested exterior nonpivot links and the approximate-collar-ball
\(O(\delta'_j)\) link comparison, together with a bounded derivative of the
full-block mean-contour map, give the conclusion. **PROVED IN Y** as this
conditional argument. No plaquette bound is used in these lines.

### Two belt groups, Y 64027–64211 — Y-BELT

**Statement/status.** Y compares the ordinary test-cube and strip centers to
the promoted/local collar averages, then fits the fifth and sixth ordinary
approximate-test groups into their \(2\delta_j\) thresholds. It uses actual
averaging constraints, center comparisons on an annulus, the real finer-collar
path for freed pivots, the collar test for exterior nonpivots, and the completed
ordinary strip test for old-wall crossings. **PROVED IN Y** (64027–64211).

**Outer-layer reads.** Here `O_m = Omega_m^c intersect X` by `eq:elab-history-quiet-boxes`
(Y 63760–63766); the exterior bases and collar (K) are in this region
(64030–64065). The explicit tested-plaquette bounds are at 64088–64106:
retained level-(j) plaquettes keep their old holonomies; level-(m)
plaquettes in carried density cubes use the actual (V_m) test; other newly
tested level-(m) plaquettes use the fine determining rows and exact one-step
average; and at the exterior tower a tested holonomy is identity or the lifted
top holonomy. These are the outer-tower/exterior-region bounds Y names.
For the old-wall crossing, Y instead uses the completed strip test and
compares the two block centers; it says the direct collar test bounds the
exterior contour from its internal links “without assuming an additional
collar bound on the crossing itself” (64184–64211). For the test-cube
comparison Y expressly says it “does not require the discarded sharp bound at
the artificial bare rim of `X`” (64083–64086).

### Mean-domain convention, Y 64802–64807 and 64929–64953 — Y-MEAN

**Statement/status.** Y uses the full block for the mean-contour map and the
regular mean chart: links on the local approximate collar ball differ from
their prospective axial reference by (O(\delta'_j)), and the full-block
mean-contour map has bounded derivative (64802–64808). On the double block,
the induced-field level-(j) plaquette defects are (O_L(e)); fixed contour
stencils put their transports within (C(L)e) of the central transport and
the regular averaging formula puts the central transport within (C(L)e) of
the coarse value (W) (64929–64940). The argument uses these comparisons to
place the actual pivot on the regular branch (64941–64953). **PROVED IN Y**
for the branch conclusion, with the regular averaging formula/inverse as
inputs.

**Plaquette-bound location.** The explicit plaquette bound is on the double block in
the old level-(j) member (64929–64935), used to compare the contour
transports. These lines do not separately identify that double block as the
artificial bare rim of (X), nor invoke a sharp rim threshold. The mean-domain
statements themselves concern full blocks and contour links, not another
plaquette threshold.

One-level follow-up for the other labels cited in these arguments:

- `mb:local-regularity-conclusion`, Y 15778–15812, gives the real local-gauge
  bounds on an enlarged cube and says the full-current radius is required
  there; Y supplies the gauge and Laplacian/Hölder steps. `mb:holder-reduction`,
  Y 11901–11917, gives the Hölder estimate conditional on the displayed
  potential and componentwise-Laplacian bounds. Both are proved in Y under
  their stated analytic inputs.
- `eq:elab-history-quiet-boxes`, Y 63760–63766, defines `O_i` as the exterior
  region and gives its specified inset relation; it is a definition, not a
  separate proof claim.
- `hi:real-finer-collar-path` is followed in section 1 above. The citations
  from the belt comparison point to that same argument, not a second supplier.

## 6. Six-input table

“First open input” means the first condition this source argument takes from
outside its own displayed derivation; it is not a verdict on that condition.

| Input | Y lines | Label | Status in Y | First open input |
|---|---:|---|---|---|
| Y-PATH | 64860–65017; E1 65010–65014; E2 64239–64245; E3 64451–64455 | `hi:real-finer-collar-path`; `hi:real-crossing-response` (E1) | PROVED IN Y | Admission of the prospective regular critical (U^+) and the fixed background geometry/ceiling. |
| Y-JOIN | 13283–13396; use 65019–65067; promoted datum 65417–65563, 134201–134205 | `mb:real-collar-datum`; `mb:real-collar-norm`; `hi:prepared-real-endpoint` | PROVED IN Y | Retained-test/constraint entering support and admitted global/local real orbits; enlarged support uses `hi:preceding-guard-support`. |
| Y-DENS | 64699–64789 | no separate label in these lines | PROVED IN Y | Exterior/stage density and crossing tests on the entering support; joined comparison. |
| Y-CONT | 64791–64810 | no separate label in these lines | PROVED IN Y | Exterior nonpivot tests and the bounded derivative/regular branch of the full-block mean map. |
| Y-BELT | 64027–64211 | no separate label in these lines | PROVED IN Y | Ordinary density/strip tests, collar test, retained constraints, and Y-JOIN center comparison. |
| Y-MEAN | 64929–64953; 64802–64807 | no separate label in these lines | PROVED IN Y | Regular averaging formula and one-row inverse on the stated double-block chart. |

