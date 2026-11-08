# Independent finite SU(2) boundary/gluing certificate

Source revision: `f5af11cd0102cfd0b51aef0911f600130bf5beb1`.
This is a restricted-input, fresh-context, same-family research check. It is
not an audit or a retained-status decision. The configured model and effort
were inherited without override; the host exposes no more specific receipt.
No primary worktree, primary result, or other checker result was inspected.
The analytic results below were sent to the supervisor before numerical
execution or comparison artifacts were seen.

## Current checkpoint

Analytic derivation and the frozen exact certificate are complete. Both graph
implementations reproduce the complete regional decomposition, the all-vertex
count, the open-boundary count, and all three final groupings. The cut
coefficient identities are checked exhaustively on their finite basis. The
three injected representation-loss faults fail closed. No finite-model
obligation in the assigned question remains open; the physical identifications
listed below remain outside this result.
Allowed scientific sources read: `CHECKER_SPEC.md` and
`docs/MINIMAL_AXIOMS_2026-06-29.md`. Operating instructions were read at the
pinned source revision. No scientific source outside the allowed set was read.
The runtime certificate reads only its own source for its hash, standard-library
code, and resource-limit environment variables; it never reads this note,
the specification, a workflow, or a comparison result.

The result is conditional finite gauge mathematics for the supplied
five-dimensional link model. It does not derive a native qubit allocation,
the Admissibility distribution, a Record formation/readout law, a continuum
limit, a vacuum, or a mass gap. The four framework axioms do not select this
link space, gauge constraint, electric operator, or subdivision weighting.

## Targeted literature record

On 2026-11-07, two targeted searches covered Peter–Weyl subdivision,
boundary representations, lattice gauge Hilbert spaces, and gluing. Repository
and open-PR scientific searches were excluded by the restricted-input spec.
William Donnelly's [2014 paper](https://arxiv.org/html/1406.7304), section 1.2,
equations (10)–(13), states the normalized representation-coefficient basis
and group-multiplication embedding. Section 2 describes edge irreps and
vertex intertwiners. His [2012 paper](https://arxiv.org/pdf/1109.0036),
section I, explains regional gauge invariance with boundary degrees of
freedom retained. These are accessible primary sources for the standard
construction, credited here; their entropy and physical interpretations are
not used. The finite cutoff, compressed-operator identity, exact graph
multiplicities, and the intermediate-projection fault are derived below.

## Link cut: normalization, image, and matching

Let `D^j_ab(g)` be a unitary SU(2) matrix coefficient, `d_j=2j+1`, and
`|j,a,b> = sqrt(d_j) D^j_ab`. The only irreps retained are `j=0,1/2`.
Normalized Haar integration gives

\[
\int \overline{D^j_{ab}}D^{j'}_{cd}
 =\delta_{jj'}\delta_{ac}\delta_{bd}/d_j.
\]

For `x -> z -> y`, take tensor order `[g2,g1]`. Matrix multiplication gives

\[
C|j,a,b\rangle=d_j^{-1/2}\sum_c
 |j,a,c\rangle_2|j,c,b\rangle_1.\tag{1}
\]

The `d_j` terms are mutually orthonormal, so (1) preserves every basis
inner product. Equivalently, Haar invariance gives
`integral dg1 dg2 |f(g2 g1)|^2 = integral dg |f(g)|^2`.
At the new vertex, the two representations are dual to each other.
The invariant space of `V_j^* tensor V_k` has dimension `delta_jk`.
Thus the image is exactly `Inv_z(R2 tensor R1)`, of dimension
`1^2+2^2=5`, inside a space of dimension 25. Different link irreps cannot
match, and the two spin-1/2 representation indices must be contracted.
Projecting the two endpoints separately to singlets would retain only the
constant and would delete the four-dimensional fundamental sector.

On basis tensors the adjoint is zero for unequal irreps and otherwise

\[
C^*(|j,a,c\rangle_2|j,d,b\rangle_1)
 =\delta_{cd}d_j^{-1/2}|j,a,b\rangle.
\]

For three segments both parenthesizations yield

\[
d_j^{-1}\sum_{c,d}|j,a,c\rangle_3
 |j,c,d\rangle_2|j,d,b\rangle_1.
\]

For `n` segments the factor is `d_j^{-(n-1)/2}`. This proves subdivision
associativity and normalization for all finite subdivisions, including the
constant sector. Gauge covariance follows from cancellation of `h_z^-1 h_z`
in `(h_y g2 h_z^-1)(h_z g1 h_x^-1)`. Reversing traversal replaces the path
operator by `(U2 U1)^dagger = U1^dagger U2^dagger`.

## Compressed path multiplication and electric accounting

Use unnormalized fundamental coefficients `D_ab`, each with norm squared
`1/2`, and `epsilon_01=1`, `epsilon_10=-1`. Haar invariance implies
`integral D_ab D_cd = epsilon_ac epsilon_bd/2`: the invariant tensor is
`epsilon tensor epsilon`, and contracting it uses `det D=1` to fix the
factor. The product of two fundamental coefficients has spins 0 and 1;
the cutoff retains only spin 0. Hence the supplied compressed multiplication
has the exact action

\[
U_{ab}1=D_{ab},\qquad
U_{ab}D_{cd}=\tfrac12\epsilon_{ac}\epsilon_{bd}\,1.\tag{2}
\]

The absence of a spin-1/2 term also follows from parity under `g -> -g`.
Equation (2) is equivalent to the supplied `P_mu` formula by the linear
change from quaternion coordinates to fundamental matrix coefficients.
It does not assume unitarity of the compressed operator.

In this basis `C D_ab = sum_k D_ak tensor D_kb`. Acting on `C1`, the product
`(U2 U1)_ab` immediately produces `C D_ab`. Acting on `C D_cd` gives

\[
\sum_{k,l}\frac14\epsilon_{ac}\epsilon_{kl}
                  \epsilon_{kl}\epsilon_{bd}\,1\otimes1
 =\frac12\epsilon_{ac}\epsilon_{bd}\,1\otimes1,
\]

because `sum_kl epsilon_kl^2=2`. Therefore, entry by entry,

\[
(U_2U_1)C=CU.\tag{3}
\]

This is an identity on the cut image. It is not an identification of all
25 unconstrained fine-link states with one link.

Each segment has the same `j`, so

\[
E_1^2 C=CE^2=E_2^2 C,
\qquad (E_1^2+E_2^2)C=2CE^2.
\]

The nonconstant sector has coarse eigenvalue `3/4` and summed fine
eigenvalue `3/2`. A weighted fine energy agrees with `c E^2` exactly when
`c1+c2=c`; for `n` segments the corresponding condition is `sum_i c_i=c`.
The zero sector alone cannot detect this condition. Choosing physical
weights is an additional input; the isometry does not select them.

## Regional boundary certificate

Write `q=2j`, and let `V_q` have dimension `q+1`. Occupying an edge selects
its `(1/2,1/2)` endpoint representation; an unoccupied edge selects `(0,0)`.
For occupancy `S`, each vertex carries `V_1^{tensor deg_S(v)}`. The exact
local decomposition follows by adding one spin-1/2 at a time:

| occupied ends | nonzero multiplicities `q:m` |
|---|---|
| 0 | `0:1` |
| 1 | `1:1` |
| 2 | `0:1, 2:1` |
| 3 | `1:2, 3:1` |
| 4 | `0:2, 2:3, 4:1` |

The singlet multiplicity at four ends is **two**, not one. Endpoint duals
have the same SU(2) character, so the oriented edges give these counts
without changing multiplicities.

At `x=0`, let the two vertical occupancy bits be `t0,t1`. Gauss law forces
the three left horizontal bits to be `(t0,t0 xor t1,t1)`; each admissible
left vertex has a unique singlet. Thus the possible boundary occupancy
patterns are `000,110,011,101`. The right region has the same four patterns.
Let `X,Y,Z` denote the spin-1/2 characters at boundary vertices
`(1,0),(1,1),(1,2)`, in that order. Then

\[
\chi_B=F=1+XY+YZ+XZ,\qquad
\chi_A=F(1+XY)(1+YZ).\tag{4}
\]

The last two factors are the two middle vertical edges, owned by A.
No boundary vertex has yet been projected. Evaluating `X=Y=Z=2` gives
`dim B=13` and `dim A=13*25=325`.

Expanding (4) with `V_1 tensor V_1 = V_0 direct-sum V_2` and
`V_1^{tensor 3}=2 V_1 direct-sum V_3` gives the complete decomposition
`H_A = direct-sum_q C^{m_A(q)} tensor V_q0 tensor V_q1 tensor V_q2`:

| `(q0,q1,q2)` | `m_A` | `m_B` |
|---|---:|---:|
| (0,0,0) | 4 | 1 |
| (0,0,2) | 2 | 0 |
| (0,1,1) | 5 | 1 |
| (0,2,0) | 3 | 0 |
| (0,2,2) | 2 | 0 |
| (0,3,1) | 1 | 0 |
| (1,0,1) | 4 | 1 |
| (1,1,0) | 5 | 1 |
| (1,1,2) | 3 | 0 |
| (1,2,1) | 3 | 0 |
| (1,3,0) | 1 | 0 |
| (1,3,2) | 1 | 0 |
| (2,0,0) | 2 | 0 |
| (2,0,2) | 1 | 0 |
| (2,1,1) | 3 | 0 |
| (2,2,0) | 2 | 0 |
| (2,2,2) | 1 | 0 |
| (2,3,1) | 1 | 0 |

All unlisted multiplicities vanish. The multiplicity sums are 44 for A
and 4 for B; these are not their Hilbert-space dimensions.

Diagonal boundary invariance pairs equal irreps, once for each pair of
multiplicity indices. With normalized invariant tensors this is an isometric
identification, and its dimension is

\[
\sum_q m_A(q)m_B(q)=4+5+5+4=18.\tag{5}
\]

For self-dual SU(2) irreps, a normalized singlet in `V_j tensor V_j` is
`(2j+1)^(-1/2) sum_m (-1)^{j-m}|j,m>|j,-m>`; where one factor is explicitly
dual, it is the normalized identity contraction. There is no extra factor
of `q+1` in (5).

## Independent full and open-boundary counts

For the full graph, singlets require even degree at every vertex. The cycle
space has dimension `12-9+1=4`; the four plaquette boundaries form an
independent basis, since a nonzero outermost plaquette coefficient leaves
an uncancelled exterior edge. Therefore there are `2^4=16` even occupancy
subgraphs. Every noncentral vertex then has degree 0 or 2. The center has
degree 4 exactly when the four incident plaquette coefficients alternate
around it, giving two configurations. Four spin-1/2 ends have two singlets:
couple an initial pair to spin 0 or 1 and the other pair to the same spin.
Consequently the full count is `14*1+2*2=18`, independently of regional
gluing. The runner lists all 16 occupied-edge masks and their multiplicities.

With only center Gauss law, each of the four incident links has center
character `1+2 chi_(1/2)`; the factor 2 is its unprojected outer endpoint.
The center-star invariant dimension is

\[
1+\binom42 2^2\cdot1+2^4\cdot2=57.
\]

The remaining eight links are unconstrained and each has dimension 5.
Thus the open-boundary dimension is `57*5^8 = 22,265,625`. The eight outer
vertices have not been gauged or identified. This scalar dimension requires
no dense state vector or matrix.

## Three-region grouping and faults

Let L be the left vertical/horizontal edges, M the middle vertical edges,
and R the right vertical/horizontal edges. Their boundary characters are
`F`, `(1+XY)(1+YZ)`, and `F`. Tensor products retaining the full boundary
representations are associative. Applying the final three boundary singlet
projections to `(L M) R`, `L (M R)`, or `(L R) M` gives the same 18 states.

All three interface vertices have incident edges in each partial pairing
and in its omitted third region. Therefore no interface vertex can be
universally projected to a singlet before that third region is attached.
The `x=0` constraints can be imposed when L is present; the `x=2`
constraints can be imposed when R is present. An omitted edge known to be
trivial is a sector-specific exception, not a license to discard the
nontrivial sectors in the full space.

Projecting all three interface vertices after any first pair, then applying
the final constraints after attachment, leaves only `4*1=4` states.
Projecting some interface vertices after LM gives counts 9, 8, or 9 for
the bottom, middle, or top singleton subset; projecting any two leaves 4.
These are explicit losses, not a general impossibility claim about gluing.

The alternative LR intermediate decomposition matches M in five sectors:
`000,110,011,101,121`. The LR multiplicities are respectively `4,4,4,4,2`;
M has multiplicity one in each. The spin-1 middle-boundary sector `121`
is essential in this grouping: truncating intermediate spins to at most
1/2 gives 16. Independently replacing the four-ended local singlet
multiplicity by one also gives 16. These mutations are tested against
independent complete counts rather than against desired hard-coded totals.

## Exact execution evidence

Runner: `scripts/gb1_cf_boundary_fusion_check_2026_11_07.py`.
Full raw output: `outputs/checker_raw.txt` in this folder. It preserves the
initial resource-limit failure, the compatibility correction and successful
run, and the final frozen suite. The final suite ran at
`2026-11-08T02:24:01Z` (2026-11-07 local date) under unique holder
`gb1-cf-boundary-checker-final-20261107-5c00fc86c66f4dd4be2c6acb6db32903`.
Fresh numeric preflight returned `go`; acquisition and release both returned
success. No lease remains held by this job.

The final script declares literal `AUDIT_TIMEOUT_SEC = 85`. An environment
override is optional and constrained to 1–90 seconds; the final run had no
timeout override. CPU and wall guards were active, and a 90-second outer
deadline bounded the entire baseline-plus-fault suite. Math thread variables
were set to one. Darwin rejected both DATA and AS kernel memory limits, as
anticipated by preflight's memory-cap note. The supported fallback monitored
peak RSS every 0.05 seconds and stopped at a conservative 270 MB threshold
under the 300 MB budget; there was no available hard kernel memory cap.
The final baseline used 25,509,888 peak RSS bytes and 0.103760 seconds.
Preflight could not verify a named model floor because no target floor was
provided; the configured host model/effort was inherited unchanged.

The final baseline exited 0 with `TOTAL exact_equalities=83 failures=0`.
Each separate injected-fault invocation exited 1 with its mathematical
mismatch: premature boundary projection `4 versus 18`, missing four-end
invariant multiplicity `16 versus 18`, and missing intermediate spin-one
channel `16 versus 18`. These are mutation rejection results, not audit
verdicts. The largest independent Laurent-weight frontier had 189 entries;
no dense Hilbert-space matrix was allocated.

Frozen SHA-256 identities:

| Source/evidence | SHA-256 |
|---|---|
| `CHECKER_SPEC.md` | `6e80d21c66559d9d64b89f15d4d9690cd3fd98b965d96d20f09cd1b5e3a4ddd5` |
| checker runner | `e4291452252f60610eb40526d055e400bb3ef09a23c65d08c7b2918eba03044e` |
| full raw output | `8a02e6e6809e53b89df99e9ab8ce44f0cadccf01d18aa62b0a35bee224c31956` |
| minimal axiom memo | `93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753` |
| science workflow | `1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca` |
| pinned workhorse skill | `e3e3cea67ad1877e4e73e38c7d62f1561142a0dffc66abe991f2ad0250133ad8` |

For reproduction, set `OMP_NUM_THREADS`, `OPENBLAS_NUM_THREADS`,
`MKL_NUM_THREADS`, `VECLIB_MAXIMUM_THREADS`, and `NUMEXPR_NUM_THREADS` to 1;
set `PYTHONDONTWRITEBYTECODE=1`; obtain a fresh successful
`python3 scripts/lab_ops.py preflight --numeric` and unique numeric lease.
Run `nice -n 10 python3 scripts/gb1_cf_boundary_fusion_check_2026_11_07.py`.
Then repeat with each `--inject-fault` value `drop-flux`,
`drop-multiplicity`, and `truncate-intermediate`, expecting exit 1 and the
specific mathematical mismatch. Release that lease after all processes stop.

The two independent computational routes are occupancy/fusion enumeration
and signed Laurent-weight constant terms with frontier elimination.
For a symmetric SU(2) character `p(z)`, the singlet coefficient is
`CT[(1-z^2)p(z)]`; boundary multiplicities follow from successive weight
differences `m_q=w_q-w_(q+2)`. The latter route never calls the fusion or
occupancy functions. A third certificate uses the four face-cycle masks.
The cut check works in the unnormalized coefficient basis with exact
rational Gram weights, independent of a direct quaternion five-state runner.

No comparison artifacts were imported and no prompt, platform instruction,
audit field, or authority file was edited. Only the three assigned deliverable
paths are written, apart from the required cooperative numeric-lease metadata.
