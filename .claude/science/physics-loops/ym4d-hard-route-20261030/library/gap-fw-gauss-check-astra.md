## Repo search

Searched `origin/main`, `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`
in `/Users/jonreilly/Projects/Physics`, one bounded `git grep` at a time.
Their respective revisions were `8920090caae2`, `f76f6c649cff`,
`89faef229ff6`, `1e70c7211a2c`, `c73ad7b177d9`.
The final exact-label/method query was
`gap-fw-gauss|\(WALL-[12]\)|\bFW[25]\b|\bProca\b|Neumann wall|Gaussian.{0,35}sub.multiplic|image.{0,30}Casimir|Casimir.{0,30}thermal`.
It returned no matches on all five refs (head limit 35, not reached).
Earlier broad queries returned unrelated substrings, including “reciprocal”
for unbounded “Proca”; their capped output proves no absence.

The broader `Neumann (wall|boundar)` search did find related methods:

| Hit and source lines read | Exact statement and closeness |
|---|---|
| main, `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonlinear-chart-response.md:140–158`; `gates/marginal-regional-chart-check.md:136–150` | For the weighted Neumann operator on a **configuration cube**, a gradient's normal component is Dirichlet and its tangential components are Neumann. This is a mixed-domain covariance argument, not a spatial free-wall partition identity. |
| pr/10114 (also a search hit on pr/10133), `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MANUSCRIPT_RG.md:1244–1264` | `L psi=G` on a configuration rectangle gives `(L I+H) grad psi=grad G`, with those mixed conditions. Same distinction; no thermal/Casimir comparison. |
| Same soft-route directory, `literature/NOTES.md:100–117` | Quotes Tadeusz Balaban's coarse-energy inequality as expounded by J. Dimock, III, Lemma 20: `norm(Phi-Q_k phi)²/2+norm(partial phi)²/2+mu norm(phi)²/2 >= c_0(norm(partial Phi)²+mu norm(Phi)²)` on Neumann blocks. Related boundary vocabulary; no FW5 or WALL bound. `SOFTHARD.md` and `REVIEW_SOFTHARD.md` search hits repeat this attribution. No estimate from that paper is imported here. |
| Same directory, `REVIEW_SQ_S3.md:78–96` | Its earlier “non-wrapping boxes” are gauge-chart regions inside a torus, not free field boundaries. This prevents treating those box results as the present supplier. |
| This checkout, `library/gap-next3-max.md:398–458,476–490` | Defines the actual FW2, FW5 and WALL consumers. FW5 is the equality checked below; WALL-1 and WALL-2 are explicitly open for Wilson. The exact crux at line 480 restricts `3<=a<=b/2` and `c,d>=b`. The scalar continuum estimate at line 490 is GUIDE. This is row 903's credited parent, not a duplicate check. |

Other hits concerned block Green estimates, Regge boundary terminology,
or Proca witness moments, not this partition-function statement.
`library/prior/repo-search-2026-11-08.md` was read in full; its thirteen
targets are different. `library/lit-balaban.md` had no hit for
`Neumann|free.wall|Gaussian|boundary`. Balaban's papers were not opened.

The task-specific prior memo is absent. The registry search for `gap-fw`,
`WALL-1`, `WALL-2`, `free.wall`, `proca`, and `neumann` returned no matches.
No matching prior check or competing registry owner was found.

The outline index README, chunk rows and neighbours were consulted.
Chunk 01:71–86 points to **existing** path-spectrum work:
SA 615–635 defines the intrinsic graph (“include exactly the bonds” inside);
SA 709–755 proves the cosine basis and eigenvalues
`4 sin²(pi k/(2b))`. We reuse this proved input, credited to Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text.
Chunk 01:25–35 points to SA 238–270 and 295–322: Haar/Wilson definitions
and the local quadratic expansion, with its explicit limit on quantum claims.
The chunk/obligations search for the exact wall labels, Proca, free walls,
Casimir and image comparison found no matching theorem; its Casimir hits
are group-representation estimates. A targeted search of CA-I, II and III
for `free.wall|\bProca\b|Neumann boundary|image comparison|Casimir (energy|term)|thermal.{0,20}wall`
returned no hits. These are bounded search findings, not an exhaustive
claim that no differently named result exists in the account.

Provenance: Codex, GPT-6-astra, xhigh; 2026-11-13; checkout
`f7be79548edaaa2b9f9a325eee7ccbbaf80e1299`. FINISH row 906.
Research check of Claude Opus 5.5's row 903; not an audit; grants no status.
Source SHA-256: `a4452af9c3f089c0cda786b9e8ff987134dae0895ecbdc67280975168bd2f06e`.
No numerical run will discharge a statement. No interacting Wilson estimate
or continuum mass gap is being proved here. GUIDE scans are outside the
proof check.

Checkpoint: repo search complete; source read in full. The check follows
the repository's `procedures/check.md` mathematical steps, with this task's
explicit output path, verdict vocabulary and no-status restriction.
Complete: scalar identities, both wall bounds, gauge towers, and scope
corrections. No mathematical obligation in this check remains pending.
Source line references below mean `gap-fw-gauss-opus.md`.

## 1. Scalar model and Wilson-wall interpretation — HOLDS AFTER CORRECTION

Lines 19–21 correctly define the massive scalar on an induced graph.
Deleting exterior bonds gives the Neumann graph Laplacian, including
the one-vertex case. The outline already supplies its spectrum.

Line 23 correctly identifies the **cellular gauge quadratic form** produced
by retaining precisely the interior Wilson plaquettes. It does not identify
the Wilson model with the massive scalar. For Hermitian link variables,
write `U_l=exp(i t A_l)`. At the trivial connection the quadratic term is
`beta t²/4 sum_p tr((d_1 A)_p²)`. Haar density is constant only to leading
order in this rescaled local chart. In the outline's convention
`|F|²=tr(F²)/2`, the coefficient is `beta t²/2`, not `beta t²/4`.
The latter coefficient is correct if the norm means `tr(F²)` instead.
Gauge zero directions and the time holonomy require separate treatment.
The positive mass is an added regulator, not generated by this expansion.

Corrected text: “Neumann is the scalar analogue of deleting exterior
interactions. The formal Wilson quadratic form has natural cellular walls;
its vector spectrum has the mixed vertex/edge factors of Step 6. This is
not a proved weak-coupling limit of normalized Wilson measures.”
Neither the `|U|=1` observation nor flatness of the leading Haar density
removes these distinctions. The scalar Dirichlet description is correct:
zero extension retains diagonal `8+m²` and only interior cross terms.
It supplies a different scalar wall, not a boundary condition derived
from Wilson. This correction does not change the scalar calculations.

## 2. FW2 and normalization — HOLDS AFTER CORRECTION

The sub-multiplicativity identity at line 25 HOLDS, strictly when the cut
has a bond. Under the product of the two normalized Gaussian laws,
the ratio is the expectation of `exp(-sum_cross (phi_x-phi_y)²/2)`.
The exponent is nonpositive and not almost surely zero. This refutes
FW2 for the **bare scalar normalization**, not for the Wilson weight.

The Jensen repair HOLDS at each fixed `m>0`. Each covariance is bounded
by `m^(-2) I`, since its precision is `m² I+L >= m² I`.
Independence across the cut gives `E(phi_x-phi_y)² <= 2/m²`.
Thus multiplying every bond weight by `exp(kappa)`, with `kappa=1/m²`,
restores super-multiplicativity for all the boxes. This is uniform in
box size, not in mass. For two single-site boxes the bare ratio is
`m/sqrt(m²+2)`; any such repair needs
`kappa >= (1/2)log(1+2/m²)` in that example.

More generally, adding `a(Ab+B)` to `log W(a,b)` gives
`e'=e+Ab+B`, `f'=f+A`, `D_inf'=D_inf-B`.
It leaves `delta_e`, `g` and `p` unchanged. In the space channel,
`eps'=eps+aA`, `omega'=omega+a(A+B)`, and `gamma'=gamma`.
Consequently `c'=omega'-a(f'-D_inf')=c` as well.
This proves lines 25–27, including the use of limits instead of the
Wilson sup-definitions for the bare normalization.

Line 123's “only D_inf ... moves” needs correction: **both `f` and
`D_inf` generally move**, as line 26 already states. For the displayed
bond count, `A=kappa(4cd-c-d)` and `B=-kappa cd`.
For a per-site constant instead, `A=kappa cd`, `B=0`; it leaves the
gluing ratio itself unchanged and cannot repair FW2.
FW5 and FW6 are unchanged. No uniform-in-mass normalization repair
is needed for the wall constants.

## 3. Spectra, image formulas and every FW5 term — HOLDS

Lines 31–53 use the intrinsic path spectrum already proved in SA 709–755.
Periodic time must mean the cellular cycle: one loop for `a=1`, two
parallel edges for `a=2`. The Fourier formula counts these multiplicities.
A simple graph with one edge at `a=2` would be a different model.

Put `q=exp(-omega)` and `mu²=2cosh(omega)-2`. Each periodic eigenvalue is
`q^(-1)(1-q exp(2pi i j/a))(1-q exp(-2pi i j/a))`.
Taking the product gives `q^(-a)(1-q^a)²=4sinh²(a omega/2)`.
Gaussian integration therefore gives exactly the printed `log W`, `e`
and `g`, with no omitted mass- or volume-dependent determinant factor.

The transfer assertion also has the right normalization. One mode has
kernel `K(x,y)=exp[-cosh(omega)(x²+y²)/2+xy]` against `dy/sqrt(2pi)`.
Set `h=sinh(omega)` and
`f_z(x)=exp(-h x²/2) exp(2sqrt(h)xz-z²)`.
Completing the square gives `K f_z=exp(-omega/2) f_(qz)`.
Coefficients in `z` are the complete Hermite basis, so the eigenvalues
are `exp(-(n+1/2)omega)`. Tensoring gives the spectrum at line 34.
For completeness, orthogonality to all these coefficients makes
`int f(x) exp(-h x²/2) exp(zx)dx` an entire function with every
derivative at zero equal to zero. Its imaginary-axis values vanish;
Fourier uniqueness then gives `f=0`.

For any of the analytic even functions used here, summing its absolutely
convergent Fourier series over the `2b` roots of unity keeps only
multiples of `2b`. Pairing `k` and `2b-k` leaves the two endpoints once.
This gives (N). Subtracting `h(0)` gives (E); replacing `b` by `b+1`
in (E) gives (D). Thus all three image identities at lines 39–41 HOLD.
At fixed positive mass their remainders vanish exponentially with `b`.

Here is the verdict on each printed quantity:

| Source | Quantity | Verdict |
|---|---|---|
| 44 | `f=-sum_T hat(omega_T)(0)/2`; `D_inf=sum_T[omega_T(0)-omega_T(pi)]/4<0` | HOLDS |
| 45 | `delta_e(b)=-b sum_(T,j>=1) hat(omega_T)(2bj)` | HOLDS |
| 46–47 | `p(a)=sum_T hat(F_T)(0)`; `W_N=sum_T[F_T(0)-F_T(pi)]/2` | HOLDS |
| 48 | `g=bp+W_N+2b sum_(T,j>=1)hat(F_T)(2bj)` | HOLDS |
| 49 | `eps=sum_T hat(H_T)(0)`; `omega=eps+sum_T[H_T(0)-H_T(pi)]/2`; `gamma=2b sum_(T,j>=1)hat(H_T)(2bj)` | HOLDS |
| 50 | `c=p+W_N` | HOLDS |
| 51(i) | `p=eps-af` | HOLDS |
| 51(ii) | `g=(b-1)p+c+gamma-a delta_e` (FW5) | HOLDS |
| 53 | Dirichlet formulas, with `b+1`, the negative endpoint term and Dirichlet transverse grids | HOLDS |

To check the potentially delicate spectral identification in 51(iii),
use a different determinant order. Set
`mu_(T,l)²=M_T²+2-2cos(2pi l/a)` and
`eta_(T,l)=arcosh(1+mu_(T,l)²/2)`, `0<=l<a`.
The determinant of a Neumann path is

`det(mu² I+L_b^N)=mu² sinh(b eta)/sinh(eta)`.

Indeed its nonzero-path part is the tridiagonal Dirichlet determinant
on `b-1` sites. The recurrence `D_n=2cosh(eta)D_(n-1)-D_(n-2)`,
`D_0=1`, `D_1=2cosh(eta)`, gives `D_n=sinh((n+1)eta)/sinh(eta)`.
The extra Neumann eigenvalue is `mu²`. Thus, directly,

`log W=b eps+A_0+gamma`,

`eps=-(1/2)sum_(T,l) eta_(T,l)`,

`A_0=-(1/2)sum_(T,l) log(mu_(T,l)²/(2sinh eta_(T,l)))`,

`gamma(b,a)=-(1/2)sum_(T,l) log(1-exp(-2b eta_(T,l)))`.

In particular `omega=eps+A_0`. This independently checks the constant
and the `b-1` shift. Expanding each factor
`(1-z)^(-1/2)=sum_(n>=0) binom(2n,n)z^n/4^n`
shows that `exp(gamma)` is `1+S_W`: the nonconstant terms have positive
overlap ratios and spectral ratios at most one. With `z=exp(-2b eta)`,
the factor `exp(-2n eta)` belongs to the overlap, and
`exp(-2n(b-1)eta)` to propagation. Equivalently these are the even
oscillator levels of the Gaussian space transfer; the odd overlaps vanish.
So 51(iii) HOLDS, not just as an asymptotic decomposition.
The same formula proves `gamma>0`, decreasing to zero.

Finally `H_T=F_T-a omega_T/2`. Substitution gives
`gamma-a delta_e=2b sum hat(F_T)(2bj)` and then FW5 exactly.
There is no use of FW2's sign in this calculation.

## 4. Propagator formulas and signs — HOLDS

Lines 57–68 have the right signs and factors. Write the adjacency matrix
of `Z²` as `A`. The convergent series
`(s+4-A)^(-1)=(s+4)^(-1) sum_(n>=0)(A/(s+4))^n`
has nonnegative entries, and some walk reaches each endpoint. Hence
`G_s(t,x)>0`. Swapping coordinates preserves it. Integrating one momentum
gives the printed `exp(-|t|omega_s(theta))/(2sinh omega_s(theta))` formula:
the decaying solution of `2cosh(w)u_t-u_(t-1)-u_(t+1)=delta_(t,0)`
is `u_t=exp(-|t|w)/(2sinh w)`.
At `x=0` this is a positive mixture of decreasing exponentials.

Differentiation gives `partial_s omega_s=1/(2sinh omega_s)`.
Expanding `F_a=sum_(r>=1) exp(-ra omega_s)/r` yields
`partial_s hat(F_a)(n)=-a sum_(r>=1)G_s(ra,n)`.
For `H=F_a-a omega_s/2`, it gives
`partial_s hat(H)(n)=-(a/2)sum_(r in Z)G_s(ra,n)`.
The nonconstant omega coefficients and all F coefficients vanish at
infinite mass; H's nonconstant coefficients do too. Integrating in `s`
proves R1, R2 and R3 exactly as printed. Their domains matter:
**R1 and R3 require `n>=1`; R2 also holds at `n=0`.**
For fixed `s>0`, the walk bound
`G_s(t,x)<=s^(-1)(4/(s+4))^(|t|+|x|)` justifies the geometric tails.
For large `s` it also gives integrable mass tails in the stated domains.
Fourier differentiation is on a compact smooth integral; after identifying
its coefficients with G, Tonelli justifies the nonnegative sums/integrals.

Consequently the formulas for `delta_e`, `p`, `gamma`, and
`g-bp-W_N` at lines 63–66 all HOLD. Every omitted lower integration limit
in that notation is `M_T²`. For delta monotonicity, after exchanging axes,
the relevant factor is `b/(exp(2bw)-1)`, with `w>0`.
Its derivative has numerator `exp(u)(1-u)-1<0`, `u=2bw>0`.
Thus `delta_e>0` decreases to zero. Gamma monotonicity follows directly
from the alternative determinant in section 3; positivity of G alone
would not justify a monotonicity assertion with a prefactor `b`.
Also `F_T(0)>F_T(pi)`, so `W_N>0`.

## 5. WALL-1, including optimality — HOLDS

Lines 72–76: for each transverse mode, `F_T(theta)` strictly decreases
on `[0,pi]`. On each subinterval of length `pi/b`, its left endpoint
strictly exceeds its average. Summing gives `g(a,b)>bp(a)`.
The exact positive wall-plus-image difference is also confirmed by
sections 3–4. Thus `C_1=1` works for every positive mass and all
positive integer sides, with no aspect-ratio restriction.

Fix `a,c,d,m`. The image tail tends to zero, while `W_N` is fixed and
`p>0`. Therefore `g/(bp)->1` as `b->infinity`.
No smaller uniform constant works, even on `a<=b/2`.
The supremum `bp/g=1` is not attained at finite `b`.
The further assertion `c=p+W_N>p>0` also HOLDS.

## 6. WALL-2 and the image comparison — HOLDS

Lines 80–85: put `k=floor(2b/a)>=1`. For each `j>=1`, the `k` indices
`(j-1)k+1<=r<=jk` satisfy `ra<=jka<=2bj`.
Since `G_s(t,0)` decreases in `t`, their sum is at least
`k G_s(2bj,0)`. These blocks partition all positive `r`.
Integrating and summing over the finite transverse grid proves

`a delta_e(b) <= bp(a)/k < g(a,b)/k`.

There is no discarded endpoint, color multiplicity, or factor of two.
This proves exactly the requested `C_2=1/floor(2b/a)` for `a<=2b`.
For `a<=b/2`, `k>=4`, so `C_2=1/4` works uniformly in mass and shape.
The text does not prove this constant optimal and must not call it so.

An independent check avoids grouping images. For every `w>0` and `2b>=a`,
monotonicity of `(exp(u)-1)/u` gives
`1/(exp(2bw)-1) <= (a/(2b))/(exp(aw)-1)`.
The positive-mixture formula for `G_s(t,0)` then gives
`sum_j G_s(2bj,0) <= (a/(2b)) sum_r G_s(ra,0)`.
Thus even `a delta_e <= (a/(2b)) bp < (a/(2b))g` holds.
It implies the printed floor bound and checks its normalization by
a different comparison. At `a=2b` the first inequality is an equality
against `bp`, exactly as the two winding sums require.

## 7. Proca determinant and three towers — HOLDS

Lines 91–95 are exact for the stated massive Gaussian on the product
cell complex, with flat measure on each real one-form coordinate.
The word “ghost” describes a determinant cancellation here; no
extra gauge-fixing determinant is being inserted into the Proca measure.

Write `d_0:C^0->C^1`, `d_1:C^1->C^2` and
`Delta_1=d_0 d_0^*+d_1^* d_1`, `Delta_0=d_0^*d_0`.
The complex is a cycle times a contractible spatial box, so
`dim H^0=dim H^1=1`, and `rank d_0=N_0-1`.
The orthogonal decomposition into `im d_0`, `im d_1^*` and `H^1`
can be verified by taking orthogonal complements and using `d_1d_0=0`.
On `im d_0`, `Delta_1` has the positive spectrum of `Delta_0`;
on `im d_1^*`, it equals `d_1^*d_1`.
The latter has kernel `im d_0 + H^1`, of dimension `N_0`.
Multiplying these eigenvalues therefore gives

`det(d_1^*d_1+m²)=m^(2N_0) det(Delta_1+m²)/det(Delta_0+m²)`.

Both Hodge zero modes are included; their `m²` factors cancel in the
ratio. This proves the first equality of line 94, including `m^(-N_0)`.

In a product complex the mixed terms in `dd^*+d^*d` cancel by the
graded signs. A component in direction `mu` thus has `L_mu^E` there,
and `L_nu^V` in each other direction. On a path the incidence matrix
has rank `b-1`; its two products have the same nonzero singular values.
Thus the edge spectrum is exactly the vertex spectrum minus its one
zero eigenvalue. On the cycle the edge and vertex spectra agree,
including the zero mode. Consequently `Delta^(0)` is isospectral
to `Delta_0` and cancels it. The three remaining components have exactly
the E/N grids listed at line 95. The factor `m^(-N_0)`, with `N_0=abcd`,
adds only a term linear in `a` and `b` and leaves the thermal quantities
in question unchanged. No GUIDE determinant agreement is needed.

## 8. Maxwell modes and tower-wise extension — HOLDS AFTER CORRECTION

The **physical spatial mode count** at line 96 HOLDS. The spatial box
is contractible. At a grid label K with `r` nonzero coordinate indices,
the one-form space has dimension `r`; for `r>=1` its exact-gradient
subspace has dimension one. Its coexact complement therefore has
dimension `r-1`. At the all-zero label there is no spatial one-form.
This gives multiplicities `2,1,0` for `r=3,2,1`, respectively.
Organizing them in the b-direction gives the source's N+E and E towers.
Every surviving transverse mass is strictly positive at `m=0`.

The correction is about the object: these are normalized physical
oscillator traces after imposing Gauss law and removing gauge volume.
The unquotiented massless integral over all spacetime one-forms diverges.
The source itself leaves that zero-mode bookkeeping unwritten; the
mode count does not turn this into a finite bare Maxwell partition
function or prove a Wilson weak-coupling limit.

Lines 97–99: the tower-wise estimate against **bulk `bp` HOLDS** for
Proca and for these physical Maxwell modes. Removing `h(0)` to pass
from N to E changes only the endpoint term, not the image tail.
Thus each tower has the same `delta_T` and `P_T` as in section 6.
For Dirichlet put `B=b+1`: the precise result is
`a delta_e^D(b) <= B p_D(a)/floor(2B/a)` when `a<=2B`.

The source correctly says that `g>=bp` does not follow for E or D
towers. Their negative wall term prevents that inference.
Hence this extension is **not yet WALL-2 against `g`**. To obtain it
one must prove the relevant uniform WALL-1 estimate and multiply its
constant into the bulk comparison. This check supplies no such general
variant estimate. In particular the assertion that `C_1` “must be above
1” means an estimate on the restricted engine domain; with `b=1`
an E tower is empty and `g=0<p`, so no finite `C_1` works on the full
positive-side domain. The scalar theorem's enlarged `a<=2b` domain
cannot be transferred to that variant without qualification.

## 9. Independent finite hand checks — HOLDS

Take `a=c=d=1`, `m²=2`. The scalar one-site precision is `[2]`.
The two-site precision is `[[3,-1],[-1,3]]`, with determinant `8`.
Thus `W(1,1)=1/sqrt(2)` and `W(1,2)=1/sqrt(8)`.
Their gluing ratio is `1/sqrt(2)<1`, confirming the FW2 sign directly.
For `cosh eta=2`, the crossed determinant is
`2 sinh(2eta)/sinh eta=8`, confirming the boundary constant as well.

For Proca on the same two-site space there are two temporal loops and
one spatial edge. The one plaquette has differential row `[-1,1,0]`.
Therefore `d_1^*d_1` has eigenvalues `2,0,0`; adding `m²=2` gives
determinant `16` and `Z=1/4`. The tower formula gives
`m^(-2)(m²+2)^(-1/2)=(1/2)(1/2)=1/4`.
This checks both the harmonic accounting and the exponent `N_0`
without constructing or evaluating a matrix by computer.

## 10. Doubling, GUIDE claims and final scope

**Line 120, scalar doubling: HOLDS AFTER CORRECTION of its second proof.**
FW6 and the two scalar bounds give `g(a,2b)<=2.25 g(a,b)` on
`a<=b/2`. The stronger `g(a,2b)<=2g(a,b)` also holds, directly:
split the `2b` grid into the `b` old points and their midpoints.
Each midpoint has `F_T(pi(k+1/2)/b)<=F_T(pi k/b)`.
This proves the assertion without any two-coordinate propagator
monotonicity lemma. The printed walk reflection is not a valid
length-preserving injection: reflection at `x+1/2` turns the first
crossing bond into a stationary step. For a fixed walk length, parity
also prevents adjacent endpoints from both being reachable.

**Lines 87, 116, 121, 125–127, variant conclusions: HOLDS AFTER CORRECTION
to the source's GUIDE-only scope.**
The scalar proof is uniform. The variant proof establishes the bulk
comparison, not both wall inequalities. Finite GUIDE scans cannot
establish an absolute `C_1` on unscanned shapes or parameters.
The exact parent engine domain is `3<=a<=b/2`, `c,d>=b`.
No counterexample to variant bounds on that domain is established here.
The `1.2–1.7` range cannot be extended to **all** positive transverse sides.

Here is a hand counterexample to that wider reading. For Proca take
`a=1`, `b=2`, `c=d=1`, and then sufficiently small **positive** `m`.
There is one E mode. As `m->0`, its thermal sum tends to
`g_0=-log(1-q)`, where `q=2-sqrt(3)<2/7`; hence `g_0<2/5`.
The bulk limit has `omega(theta)=2 asinh(sin(theta/2))` and

`F_1(omega(theta))=asinh(sin(theta/2))-log(2sin(theta/2))`.

The logarithm's average on `[0,pi]` is zero. To verify it, put
`I=int_0^(pi/2) log(sin u)du=int_0^(pi/2)log(cos u)du`;
the double-angle formula gives `2I=I-(pi/2)log 2`.
Consequently

`2p_0=(4/pi) int_0^(pi/2) asinh(sin u)du >= (4/pi)asinh(1)>5/6`.

The first inequality uses concavity of `asinh` on `[0,1]` and its chord.
For the last, `pi<4` and
`asinh(1)=int_0^1(1+t²)^(-1/2)dt > int_0^1(1-t²/2)dt=5/6`.
Thus `2p_0/g_0>25/12>1.7`. Dominated convergence applies to `p_m`
because `0<=F_m<=F_0` and the logarithmic singularity is integrable.
The same strict violation therefore holds for some positive masses.
These thin boxes are outside both Step 7's scan and the exact parent
engine domain. They meet `a<=b/2` alone. This refutes the all-shapes
extrapolation, **not** the engine-domain range or the existence of some
larger uniform variant constant. The source labels those numbers GUIDE;
this example must not be reported as a failure of its scalar theorem
or as a counterexample to the parent engine.

Line 87's one-light-tower estimate also needs a limit qualification.
For a Neumann tower at fixed `a,b`, `M->0` makes its zero-mode thermal
term diverge as `-log(aM)`. Its `delta_e(b)` has a finite limit,
as seen from the finite energy sum and its finite bulk integral.
Thus `a delta_e/g->0`, not `(a/b)²/4`. The latter is a continuum
**bulk-dominated** estimate; `Mb small` alone does not justify it.
The four-dimensional and large-mass estimates at line 87 are likewise
GUIDE continuum statements, not exact lattice bounds for all shapes.

Step 7's scripts, logs and scan extrema were not rerun or independently
verified. They discharge nothing here. Even taking its table at face
value, line 116's “two orders below ... 1/4” FAILS literally:
the listed `0.023` is larger than `(1/4)/100=0.0025`.
Replace that sentence with “the reported scanned values were below 1/4.”
The source's statement that every variant “also passes” must read:
“the scans did not find a failure; the bulk comparison is proved,
and a uniform WALL-1 estimate for these variants remains to be supplied.”

**Line 122, transfer to Wilson: HOLDS AFTER CORRECTION of its explanation.**
The N image formula is indeed the reflection-even linear sector of
the `2b` cycle, with reflection through bond midpoints. Mode factorization
is what supplies the determinant proof. Nothing here proves an interacting
Wilson counterpart. However “keeps the plaquettes across the reflection
plane” is not by itself an obstruction: on a mirrored gauge configuration
with seam links fixed to the identity, such plaquettes can be identities.
Then interior plaquette actions are doubled. This restriction is not
the original Wilson integral, and a linear isometry cannot rescale compact
group variables as it does Gaussian coordinates. The correct conclusion
is the absence of a proved measure/partition comparison in this argument,
not the impossibility of any mirror construction. Reflection positivity
as a proposed substitute remains a research proposal.

The checked conclusion is therefore limited to the Neumann scalar wall
bounds, the exact massive Proca tower reduction, the conditional physical
Maxwell mode count, and the normalization side finding. FW5's algebra
survives all the normalization corrections. No interacting Wilson wall
bound, seed propagation theorem for Wilson, or mass gap follows.

RESULT: HOLDS AFTER CORRECTION overall: the Neumann scalar mode formulas, R1–R3, FW5, optimal WALL-1 with C_1=1, WALL-2 with C_2=1/floor(2b/a), the massive Proca determinant/towers, and bare-Gaussian sub-multiplicativity HOLD; correct the Wilson-limit identification, normalization wording, doubling proof and variant/continuum scope; the “two orders” sentence FAILS, and an all-shapes extrapolation of GUIDE C_1<=1.7 is false outside the parent engine domain; GUIDE extrema and variant WALL bounds against g were not established; no Wilson bound or scientific status is granted.
