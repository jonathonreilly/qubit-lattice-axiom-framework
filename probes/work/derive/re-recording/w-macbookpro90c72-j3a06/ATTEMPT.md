# re-recording, attempt 3 (worker w-macbookpro90c72-j3a06, model grok-4.6)

Different route from a4 (pairing + TV on C4/T2x2) and a1 (Γ₆ spectrum): exact 36×36 transition matrices on the two-site edge, over `Q`.

## (1) The statement attempted

Six-axis product rule `(p,q,r)=(3,1,2)`. Two sites, one bond.

**(a)** The asynchronous heat-bath (pick a site with probability 1/2, redraw from `K(s|neighbour)`) has stochastic matrix `P_as` with `μ P_as = μ` and detailed balance for the static law `μ(s0,s1)∝W(s0,s1)`. Unique stationary law on this finite graph: `μ`. Block 19's kernel is the equal-time covariance of `μ` whenever that is the static sphere/six-axis law of the comparator.

**(b)** The synchronous kernel `P_sy((s0,s1)→(s0',s1'))=K(s0'|s1)K(s1'|s0)` has `π P_sy=π` and detailed balance for `π∝Z(s0)Z(s1)`, `Z(a)=∑_s W(s,a)`. `TV(μ,π)=1/12≠0`. One-site marginals of both are uniform `1/6`.

**(c)** Uniqueness regions, ordered side, and the comparator kernel transfer to (a) (same measure). They do not transfer to (b) (different Gibbs potential; TV `1/12` already on one bond).

## (2) Steps

**Step 1 — async matrix (PROVED; CHECKED as E1).** Rows sum to 1; `μP=μ`; `μ_i P_{ij}=μ_j P_{ji}` on all 36² pairs.

**Step 2 — sync matrix (PROVED; CHECKED as E2).** Same three identities for `π`.

**Step 3 — distinct (CHECKED as E3–E5).** `TV=1/12`. Uniform one-site marginals by cube symmetry of `W`.

**Step 4 — transfer (PROVED).** Async is the Gibbs sampler of the static specification. Sync is Gibbs for a star potential on a graph with one edge, `π∝Z(s0)Z(s1)= (∑_s W(s,s1))(∑_s W(s,s0))`, not `∝W(s0,s1)`.

## (3) First failing step, if any

The 36-state proof does not by itself give the sphere spin-wave kernel on `Z^3` (a4) or the `Γ₆` spectrum (a1). Those are other routes.

## (4) What would finish it

The same matrix construction on C4 (`6^4=1296`, feasible but dense `1296²`); the sphere Hessian of `∑ log Z` on `Z^3`.
