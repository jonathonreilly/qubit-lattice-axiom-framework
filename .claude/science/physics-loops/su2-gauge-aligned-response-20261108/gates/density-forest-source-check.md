# Independent check of the density, forest and connected-log engine

The generic engine in MK14–MK35 is mathematically usable under its stated
Gaussian, primitive-envelope and reader hypotheses. I found no material
algebraic or counting defect in that engine. Bounded measurable insertions
need no field derivatives. This conclusion is a conditional mathematical
check, not a re-certification of the one-step SU(N) producer package or an
application to the actual two-step model. The simpler fixed-reference
contract below can be used without moving the covariance, translating a
field, or expanding Gaussian density readers.

The old review's favorable verdict was not used as evidence. The assigned
review was read, so this is not a blind review of its conclusion. The
load-bearing estimates were reconstructed below. No physical mass-gap,
continuum, inherited-kernel or retained-status conclusion is made.

## Sources and scope

All historical scientific sources were read with `git show` at commit
`89faef229ff6e6bde42baad15ed8270c2f4087d8`; none was checked out or edited.
Their common prefix is
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`.

| Source | Read coverage | SHA256 |
|---|---|---|
| `MARKED_COMPACT_CHART_ASTRA.md` | All 753 lines; detailed check MK14–MK35 and their stated prerequisites | `04f79ed4d0c58e97f3cade072631966b577f02754f9a96d6dcd18ee2f3045800` |
| `REVIEW_MARKED_COMPACT_CHART_ASTRA.md` | All 67 lines | `9ce304ca9d8d9741fb808b5ace536bfddf54d0d1ce11abc0eeacb4554b21bd98` |
| `NONLINEAR_READER_RETURN_ASTRA.md` | Lines 1–570, particularly NR3–NR8, NR15–NR33 | `0920cf17fe8338ee566343458b70c295eed59d81e979836ae9de65e3f9fa97c0` |

The working checkout was `55fd670ff8995427b24617b2273bd3f78b7559d9`.
Its workflow and review procedure matched the locally available
`origin/main` (`bf92a1d763030836ed55631d5d7a7ef3b288f284`) on the compared
paths. No remote freshness claim is made. Applicable ancestor/local
`AGENTS.md`, `SCIENCE_WORKFLOW.md`, review-loop, freshness, scientific lenses,
reporting and proof-search instructions were read. This is the bounded
research check assigned by the coordinator, not a landing or audit run.

The mathematical premises accepted for this check are the exact primitive
representation, the finite-core/covariance bounds, local envelopes and
complete-reader norms stated in MK3–MK13. Their construction from the
supplied gauge model was not independently reviewed here. In particular,
checking this engine cannot discharge a new consumer's primitive identity,
compact amplitude, source support, or covariance hypotheses.

For a targeted primary comparison I inspected Abdesselam and Rivasseau's
[Trees, forests and jungles](https://arxiv.org/html/hep-th/9409094v1),
Theorem III.1 and section V.A. The paper supplies the established forest
architecture and a Gaussian application; its displayed example places
derivatives on interactions. The density-side identity and bounds used
here were checked directly, including applicability to merely measurable
insertions. No full-paper verification or imported gauge-model theorem is
claimed.

## Checks on the original engine

**Marginals and normalization (MK12, MK14, MK23).** If the active coordinates
are A, integrating the other variables gives the normalized density with
covariance C[A]. It does not give the inverse of the principal precision.
For example, C=[[1,r],[r,1]], 0<|r|<1, has marginal variance 1 on the first
coordinate, whereas `(C^{-1}[{1}])^{-1}=1-r^2`. This elementary discriminator
confirms the distinction made in the source. At A empty the integral is
exactly one. No determinant-only vacuum activity is left over.

With G=P[A]^{-1},

```
log(g_(P+E)/g_P)
 = -1/2 Tr log(1+GE)
   +1/2 x^T [(GE)-(GE)^2+(GE)^3-...] G x.
```

This gives the signs and determinant term in MK14. NR4–NR5 explicitly
bound the inverses of every principal P[A], using weighted conjugation;
the argument does not replace them by a restriction of P^{-1}. With
uniform exponential entry decay, deleting coordinates only decreases
the absolute row and column bounds used in that conjugation.

**All-order scalar jets (MK15–MK18).** Put t=v_I e and
t_E=v_I^2 e/(1-t). The stated e bound gives t<=1/4 and t_E<=a/48.
The absolute loop-list sum is at most exp(|A| ell); the chain-list sum
costs exp(t_E ||x+z||^2/2). Combining this with the accretive core Gaussian
leaves a bound of the form

```
sum_lists |g_list(x+z)|
 <= A_A exp(-a||x||^2/8+c_*||z||^2).
```

For coordinate i with nu_i>0 choose the Cauchy radius
`r_i=sqrt(nu_i/(2c_*))`. Its derivative factor is

```
nu_i! exp(c_* r_i^2) r_i^(-nu_i)
 = nu_i! (2 exp(1)c_*/nu_i)^(nu_i/2)
 <= (2 exp(1)c_*)^(nu_i/2) sqrt(nu_i!).
```

The last inequality is `nu_i!<=nu_i^nu_i`. Zero indices need no circle.
Summing absolute list envelopes before these circle integrals is justified
by their geometric majorants. Thus the factorial is the product over
scalars, as claimed, at every order. It must not be replaced by the
factorial of the total number of legs on a large component.

Marking a density E occurrence gives the extra factor
`[A0+A2||x+z||^2] D_z(A)` with A0 and A2 from NR18–NR19.
The spare Gaussian decay absorbs `||x||^2`, and the extra `+1` in c_*
absorbs `||z||^2`. This yields precisely a constant K_m independent of
nu and |A|. Without that spare exponent, asserting the same all-order
constant for marked jets would be unjustified; it is present here.

The translation step also preserves the scalar factorials:
`sqrt((nu+j)!)<=2^((nu+j)/2)sqrt(nu!)sqrt(j!)` and
`sum z^j/sqrt(j!)<=sqrt(2)exp(z^2)`. Moreover S'(z)<=(1+z)S(z),
since `sqrt(j+1)<=1+sqrt(j)`. These give MK18–MK19 with the stated
slightly enlarged K_tr. This verifies the original step; the new fixed
reference need not use it.

**Integrated insertions (MK20–MK22).** The derivative remains on the
density throughout. A bounded measurable compact insertion can therefore
be estimated by its sup norm after retaining its exact cap in the
identity. The integrated bound is not a claim of regularity for that
insertion. For original nonlinear vertices the separate polynomial
envelope and distinct-original-vertex incidence bound are essential:
they keep scalar polynomial degree at most 90. Gaussian differentiation
adds no primitive polynomial factors. The source's assignment of Gaussian
normalization per active coordinate and polynomial translation cost once
per shifted block is consistent. A field-free compact primitive still
has a nonempty reader and remains in the gas.

**Forest identity and scalar-root counting (MK23–MK29).** Differentiating
the normalized density gives

```
dot g_C = (1/2) sum_(i,j) dot C_ij partial_i partial_j g_C.
```

For one unordered component pair its two symmetric off-block entries
cancel the factor 1/2. Holding the primitive functions fixed is required.
There is no integration by parts. The complex pair-polydisc accretivity
in MK14 gives analytic domination even for unbounded exterior domains.
The finite clock proof is valid: for a pair monomial, independent clocks
with distribution t^j, partitioned by the unique maximum spanning forest,
give the derivatives on tree edges and path-minimum powers on other edges.
Analytic continuation from monomials on a radius greater than one is
legitimate. At disconnected masks, both the normalized density and the
primitive factors split exactly.

Let u_B be the product of primitive amplitudes in a base-overlap component.
The first rooted overlap-tree sum gives

```
sup_x sum_(B:x in S_B) exp(beta1 |S_B|) u_B <= h.
```

For a Gaussian subtree with an incoming scalar at i, give each scalar j
its unordered children. Their combinatorial denominators are 1/k_j!,
so the local factors are H0(y_j) or H1(y_j), with

```
H0(y) = sum_(k>=0) y^k/sqrt(k!) <= (1-y)^(-1) <= exp(2y),
H1(y) = sum_(k>=0) sqrt((k+1)!) y^k/k!
      <= (1-y)^(-2) <= exp(4y),                  0<=y<=1/2.
y_j = L_hat^2 sum_(B',l in I_B') e_jl T(B',l).
```

Under the proposed supersolution `T(B,l)<=u_B exp(beta1|S_B|)`, the
sum through any fixed scalar l is <=h. Hence y_j<=L_hat^2 e h and
`sum_j y_j<=k|S_B| L_hat^2 e h`. MK26 pays this exponential with its
second xi loss. This derives a cost linear in component size. Dropping
admissibility is used only to enlarge the positive counting series,
after the integrated bound was proved for admissible families.

A pin in a density reader costs K_m B_E h: exchange its nonnegative
entry sum with the component-root sum through the pinned scalar. A pin
on a Gaussian tree edge costs L_hat^2 B_E h^2: delete that distinguished
edge, retain its incoming scalar leg on each resulting subtree, sum each
root through its fixed scalar, and then sum the pinned edge envelope.
Replacing the unordered-edge factor 1/2 by one is safe. These operations
do not assert factorization of the original coupled integral.

The analogous translation pins keep their original primitive root. In
particular,

```
sum_g exp(beta|Gamma_hat_g|) a_g sum_(X in H_g) d_z^b(X)
 <= h_g sum_X d_z^b(X) <= h_g t_b.
```

The implication `X in H_g => X in Gamma_hat_g` is sufficient for the
first inequality. Thus the rare-group factor is preserved in MK28. A
volume estimate after dropping a_g would not suffice. These calculations
recover all four contributions in MK29.

**Reader regrouping and logarithms (MK32–MK35).** Initially, raw species
are compatible by disjoint base readers. Full readers can overlap. Every
base-compatible raw family has a unique partition into connected
full-reader-overlap groups. Retaining the actual internal raw list and
its base compatibility gives an exact gas of groups with disjoint full
readers. A rooted positive overlap-tree bound pays the third xi loss.

For this hard-core gas the connected graph coefficient is bounded by
the number of incompatibility spanning trees. One direct proof fixes a
strict edge order and partitions connected graphs by their Kruskal tree.
For each tree, the possible extra edges form an interval of subsets;
their alternating sum is zero or has modulus one. The rooted tree sum
then pays the fourth xi loss. This establishes absolute convergence and
nonvanishing by continuation from small auxiliary activity. The complete
support cardinalities are used in both counts.

The two charged rescalings are legitimate because they rescale positive
counting amplitudes at fixed field functions, covariance, translations,
contours and geometry. Rescaling compact primitives by h_c/(2h_g) and
undoing at least one power gives MK33, including the unchanged side-pin
term. Rescaling compact-containing raw species by xi/(4 epsilon_g)
gives total raw norm <=xi/2; undoing one power after regrouping and
the hard-core logarithm gives 2 epsilon_g in MK34. The zero-budget cases
mean the corresponding positive family is absent and require no division.

Finally, cancellation is exact only because deleting every compact
primitive leaves the identical no-mark original-chart list, including
flags, determinants, normalizers and primitive domains. This equality is
stated in MK11–MK12 and retained by each indexing operation. Subtracting
independently chosen logarithmic branches, Gaussian references or
coefficient libraries would not prove MK35. The source's common-library
construction does establish the needed cancellation, conditional on its
initial exact primitive identity.

## Reusable fixed zero-source Gaussian contract

The coordinator proposed freezing the reference at zero source and terminal
group identity, with all varied source parameters in primitive functions.
The following contract is sufficient. It uses A for an active scalar set,
to avoid confusing that set with the terminal group identity.

1. Fix a finite block set, at most k scalar coordinates per block, and one
   real positive covariance C=P+E. Neither C nor any Gaussian normalizer
   depends on any source being differentiated. A primitive o has a
   nonempty connected base S_o, active coordinates I_o owned in S_o, and a
   bounded measurable function f_o of those coordinates. Dependence on the
   varied sources is holomorphic on a common polydisc and reads only S_o.
   Its bound b_o is uniform there. Field-free primitives are allowed.

2. There is an exact normalized primitive-family identity for the desired
   partition function. Distinctness, caps, selectors and compatibility
   constraints factor over base-overlap components, and every constraint
   connecting two primitives is encoded in their bases. Deleting the
   designated remainder primitives gives the exact comparison partition
   function with the same C, normalization and no-remainder list.

3. For every admissible active set A, P[A] is block diagonal over the
   base-overlap components. Independent component-pair interpolation
   multiplies only cross E entries. The interpolation admits the forest
   identity and every real mask used in estimates satisfies
   `c I <= C_A(s) <= G I`, with 0<c<=G uniform in A and volume. A convenient
   sufficient analytic domain is `P>=c0 I`, absolute E row/column mass
   <=e0<c0/2, and pair variables of modulus less than two. Forest-mask
   spectral bounds alone should not be silently substituted for the
   domain needed by the particular proof of the forest identity.

4. Assign every nonzero E_ij a fixed connected path/label Q_ij containing
   both endpoint owners, or use a sum of such atoms. At rate beta require

   ```
   e_ij = sum_q exp(beta|Q_q|) |E_q(i,j)|,
   max(row,col) sum_j e_ij <= e,
   sup_x sum_(i,j,q:x in Q_q) exp(beta|Q_q|)|E_q(i,j)| <= B < infinity.
   ```

   These are uniform bounds on complete geometric edge labels. A row
   bound alone does not prove the pinned total bound. Source-independent
   density coefficients need no further changing-source readers; this
   says nothing about varying the frozen coarse data or covariance.

Here is a direct replacement for the loop-list jet proof. For an n by n
real covariance with the spectral bounds in item 3, set

```
d = G/c^2 + 1/(2c),
L = max(1, sqrt(2 exp(1)d)),
K = sqrt(2G/c).
```

For real x and complex z, Young's inequality gives

```
|g_C(x+z)| <= (2pi c)^(-n/2)
             exp[-||x||^2/(4G) + d||z||^2].
```

Optimizing the scalar Cauchy radii as above and integrating the real
Gaussian envelope yields, for every multiindex nu,

```
integral |partial^nu g_C(x)| product_o |f_o(x)| dx
 <= L^|nu| product_i sqrt(nu_i!) product_o a_o,
a_o = b_o K^|I_o|.
```

Indeed the Gaussian integral costs K^n and
`n=|union I_o|<=sum_o |I_o|`, with K>=1. This explicit bound includes
the normalized determinant. It neither differentiates f_o nor assumes
smooth cutoffs. If a consumer instead uses unbounded polynomial/regulator
envelopes, it must prove their integrated replacement for a_o; bounded
measurability cannot be asserted for a growing envelope.

Define

```
xi = beta/8,
h = sup_x sum_(o:x in S_o) exp(beta|S_o|) a_o,
h_c = min(xi/2, 1/[4(1+L^2 e)], xi/[8k(1+L^2 e)]).
```

If h<=h_c, the two scalar-root arguments already proved above give the
fixed-reference raw bound, at beta-2xi,

```
||a_raw|| <= h + L^2 B h^2.
```

The first term is the base pin. The second is the explicit forest-edge
pin. There is no density-list pin and no translation pin. A raw species'
complete support can be the union of its primitive bases and its explicit
forest-edge paths: all varied-label dependence is already in the bases,
and the paths connect them. Internal fixed covariance entries and
determinants do not read additional varied labels. This support choice
does not establish original-coarse-field analytic locality.

For a designated remainder class let h_0 and h_r be the ordinary and
remainder primitive budgets. Suppose h_0<=h_c/2 and h_r<=h_c/2. The
positive rescaling just proved yields

```
epsilon_0 = h_0 + L^2 B h_0^2,
epsilon_r = 2(1+L^2 B h_c) h_r,
||a_raw,no-remainder|| <= epsilon_0,
||a_raw,contains-remainder|| <= epsilon_r.
```

If epsilon_0<=xi/4 and epsilon_r<=xi/4, exact reader regrouping and
the hard-core logarithm give a common-branch ratio expansion with

```
sup_x sum_(Y contains x) exp((beta/2)|Y|) sup|Psi_Y|
 <= 2 epsilon_r.
```

Every Psi term contains a designated remainder primitive. This is a
proved conditional implication of items 1–4 and the displayed smallness
conditions. The source derivatives then follow from the same uniform
holomorphic expansion and finite-dimensional Cauchy estimates. They
vanish for a coefficient missing the relevant actual source owners.

## Disposition and recovery

The original generic mechanism has no material repair finding in this
scope. Its use by a new model remains conditional on that model's exact
identity, primitive bounds, source ownership, covariance masks and two
edge norms. The fixed-reference simplification is valid under the explicit
contract above; the later consumer file had not yet been received when
this source-stage report was written.

One mathematical source-check iteration was performed. No scientific
numerical job, test runner, lock, source edit, prompt edit, Git mutation,
PR operation, audit operation or public write was performed. Only this
assigned report was created. Read coverage is stated above; truncated
initial combined output was recovered with bounded reads before any
coverage claim. Integration and any later independent-audit status remain
outside this report.
