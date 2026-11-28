# Repo search

Writer: OpenAI Codex, task designation gpt-6-astra xhigh, FINISH row 1087.
Source commit: `5b919d573bfb517e8d4781b241cecfc54d77dd12`.
Research check, not an audit; no status or mass gap is claimed.
Scope: one transverse square, two layers, SU(2), beta_T = 0.
Not covered: n = 3, positive beta_T, general boxes, the window descent,
step (S), CUM, or a rigorous infinite-matrix numerical error bound.

The target-specific prior digest is absent. The November 8 repository digest
is an older search of main and PRs 10114, 10133, 10134, 10141. Its closest
pointer is `MASS_GAP_LOCAL_BLOCK_ASTRA.md`: a positive one-step plaquette
correlation, not the present descent sign. That source was checked below.
Rows 1081 and 1085 supply the present model and the earlier numerical claim.
The registry search for MON-L, FLUX-EXC, FACE-PROD and descent-sign found no
entry assigning this independent recomputation elsewhere. Row 1088 is the
explicitly parallel text check; its output is not read here.

The user's brief exposes expected numbers. This check is independent in
implementation, not blind to the claimed result. Neither earlier code
directory was read or run before the new numbers were saved. The later
code comparison is recorded in section 3; no older code was executed.

## Checkpoint

All five tasks are complete: bounded source checks, independent derivation,
two-cutoff computations saved before the old code was opened, subsequent
code comparison, and the hand/scope checks. The failed first route was the
numeric-lock helper's missing module; section 2 records its repair. The
small-b eigensolver diagnostic also needed exact symmetry blocks. There is
no remaining research action in this dispatch. Exact infinite-matrix error
bounds and the restricted window descent were not attempted.

Downloads, fetched once each at SA commit `31a47c543775`, are in the new
scratch directory `/tmp/sa-gap-descent-sign-2-recompute-astra.SFbyKq/`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for the outline/account context. No proof of theirs is claimed
as new here. Balaban's papers are not needed for this finite-box check.

The November 8 hit was read at PR 10114 commit
`f76f6c649cff7dffbab664d8976e680e8f287fe9`, lines 95-157 (and its header).
It supplies a rank-one convolution lower bound for a centered loop. It
neither supplies nor contradicts the two spectral ratios checked here.
The older digest reports the identical source on PR 10133; that identity
was not independently refreshed. No target-specific main/PR hit is named
in row 1087. This is bounded prior-work screening, not an exhaustive new
search of every branch. Rules were read at main
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`.

Index-first SA reads: chunk-02's GL3-GL8 rows and their neighbours;
obligations lines 19-28; outline lines 2195-2257, 2313-2335, 588-599.
GL3 supplies the Wilson convolution coefficients; GL8 supplies the familiar
gauge-projected transfer construction. Both are detailed there. Neither
passage asserts the descent sign. The mass-gap passage explicitly separates
spectral exclusion from clustering. Exact searches for MON-L, FLUX-EXC,
FACE-PROD and descent-sign found no target in the outline index. CA-I was
downloaded as requested; its 4.12-4.19 index concerns stage admission and
supplies no input used here. No CA-I proof is claimed absent on that basis.

## 1. Independent derivation, before any new numbers

Use the unreduced cube graph: eight horizontal links, four vertical links,
and four side plaquettes. All Haar measures are normalized. Write
`d_j = 2j+1`, `a_j = I_(2j+1)(b)/I_1(b)`, `b = beta_M`, and
`f_b(g) = exp(b tr(g)/2)/(2 I_1(b)/b)`.
Thus `f_b = sum_j d_j a_j chi_j`. The common scalar normalization has no
effect on any ratio or leakage coefficient below.

On gauge-invariant spin networks, a link convolution multiplies spin j by
a_j. Set K to their product on the eight horizontal links, and F to the
product of the four side-face functions f_b. The physical transfer operator
has the spectrum of

    B_t = exp(-t N/2) M exp(-t N/2),
    M = K^(1/2) F K^(1/2),   N = sum_vertical j(j+1).

This follows directly by splitting the positive time-like convolutions
between the two sides of the multiplication operator. Gauge averaging
commutes with those convolutions and F. It does not use Lemma KIN's gauge
change. Wilson kinetics replace exp(-tN) by the four longitudinal Bessel
ratios. The two endpoint operators are P_0 M P_0 and M.

### 1.1 The zero-charge block

When all vertical spins vanish, the horizontal spins are constant around
each square. Its orthonormal basis is `chi_a(U) chi_b(V)` (a,b are spins in
this section). Integrate the vertical links in F. The identity

    integral D^j(g)_mn conjugate(D^k(g)_rs) dg
      = delta_jk delta_mr delta_ns / d_j

forces the same face spin around the tube. Four factors d_j cancel four
integral denominators. Hence

    Z(U,V) = sum_J a_J^4 chi_J(U) chi_J(V),
    A = P_0 M P_0 = diag(w) Z diag(w),   w_ab = a_a^2 a_b^2.

Let `C_J(a,c)` equal 1 if J occurs in a tensor c, and 0 otherwise.
Character multiplication and orthogonality give the explicit real matrix

    A_(a,b),(c,d) = w_ab w_cd sum_J a_J^4 C_J(a,c) C_J(b,d).

For a character cutoff, this sum is finite exactly, not a separate
truncation of Z. The numerical code retains every allowed J in that sum.

### 1.2 The first charged block

Half-integral vertical spins occur an even number of times: summing the
four top-vertex parity constraints cancels the horizontal spins. One
integer vertical spin costs at least 2. Thus the first positive N is 3/2,
with two vertical spins h=1/2. There are four adjacent pairs (arc lengths
1,3) and two opposite pairs (2,2).

Integrating the other two vertical links collapses each arc into one link.
Use normalized trivalent networks on this resulting four-edge graph.
Top arc spins are u,v, bottom arc spins r,s; |u-v|=|r-s|=1/2.
Side-loop spins J,H also differ by 1/2. Multiplying the two side characters
by chi_a(bottom) chi_b(top) gives coefficient

    2 sqrt(d_u d_v d_r d_s)
      {u v h; H J b}^2 {r s h; H J a}^2.                 (1)

One derivation is to expand each matrix-element product by the identity
`D^j_mn D^k_rs = sum C(jm,kr|LM) C(jn,ks|LN) D^L_MN`.
At each of the four remaining vertices, contracting the two coupling orders
gives the normalized recoupling overlap. Its normalization is

    <((j1 j2)j12 j3)JM | (j1 (j2 j3)j23)JM>
      = (-1)^(j1+j2+j3+J) sqrt(d_j12 d_j23)
        {j1 j2 j12; j3 J j23}.

Pairing the two top vertices squares their overlap; pairing the bottom
vertices does the same. Link orthogonality leaves sqrt(d_u d_v d_r d_s),
and the two h edges contribute d_h=2. This yields (1), including its sign.
This is the same representation identity used in row 1085, not a claim of
an unrelated mathematical method. The new implementation evaluates these
squares by exact integer factorials and rational arithmetic before conversion
to floats; it neither imports nor copies the older Racah routine.

For an eigenvector phi_i of A, set G_ab=w_ab phi_i(a,b). For arc lengths
(q,4-q), define

    H_i(u,v;r,s) = sum_(J,H,a,b) d_J d_H a_J^q a_H^(4-q)
                   G_ab times (1).
    L_i(q) = sum_(u,v,r,s) a_u^q a_v^(4-q) a_r^q a_s^(4-q)
                            |H_i(u,v;r,s)|^2.
    l_i = [4 L_i(1) + 2 L_i(2)] / lambda_i^2.             (2)

No output spin allowed by the input and loop cutoffs is dropped. The code
contracts (1) by ordinary matrix multiplication, with exact rational local
coefficients. In block form B_t has off-diagonal block
`exp(-3t/4) P_0 M P_1`; the Schur complement at a simple positive lambda_i
then gives `log lambda_i(t)=log lambda_i+exp(-3t/2) l_i+O(exp(-2t))`.
Other N levels start at 2. Therefore
`m'(t)=(3/2)exp(-3t/2)(l_1-l_0)+O(exp(-2t))`.
This is conditional on the isolated simple eigenvalues; finite truncations
can check their separation but do not prove an infinite-matrix error bound.

### 1.3 Independent face matrices

For each sheet, expand L^2(SU(2)^2) in Peter-Weyl matrices with spins j,k.
Couple their left indices to p and right indices to q. For fixed j,k,p,q
each coupling multiplicity is one. The sector's multiplicity **space** is
still spanned by all allowed (j,k); it is not one-dimensional.

Instead of a 6j routine, the face implementation computes multiplication by
x=tr(A B^-1)/2 directly from Clebsch-Gordan coefficients. With total magnetic
index M=p, define

    R_p(j,k;j',k') = sum_(m,n,alpha=+-1/2)
      C(jm,kn|p p) C(j'(m+alpha),k'(n-alpha)|p p)
      C(jm,h alpha|j'(m+alpha))
      C(kn,h(-alpha)|k'(n-alpha)) (-1)^(h-alpha).

The first C forces m+n=p. Multiplying normalized Peter-Weyl matrices gives

    X^pq_(j',k'),(j,k)
      = (1/2) sqrt(d_j d_k/(d_j' d_k')) R_p R_q.
    T_pq = diag(sqrt(a_j a_k)) exp(b X^pq)
             diag(sqrt(a_j a_k)).                       (3)

The omitted factor 1/(2 I_1(b)/b) is common to all sheet sectors and cancels
from face ratios. This code path uses explicit magnetic sums, not the
earlier endpoint code or its 6j formula. In particular X^00 is the
half-adjacency matrix on j=k, which is an immediate normalization check.

Four sheets form a cycle. Matching q of one sheet with p of the next is
the transverse-site singlet condition. The vacuum product is mu_00^4.
The largest nonvacuum eigenvalue is the maximum of all nonzero-sector
cycle products and mu_00^3 times the second singlet-sheet eigenvalue.
No second eigenvalue within a charged cycle can exceed that cycle's top
product. Sector and spin cutoffs will be stated, without asserting that
uncomputed sectors are excluded rigorously.

### 1.4 Numerical decision criteria, fixed before running

At b=2.4,8,9,10 compute (2) and both endpoint gaps with at least two
cutoffs. Agreement target: 1e-8 for l_1-l_0 and 1e-7 for endpoint gaps;
report any larger difference. These are stability criteria, not error
bounds. Check the X^00 half-adjacency normalization, X symmetry, center
parities, eigenvalue residuals, and small-b leading powers. A deliberate
omission of the four adjacent-pair multiplicity must fail the small-b
coefficient. Numerical results remain GUIDE throughout.

## 2. Independent numbers saved before opening either earlier code directory

First run: characters 12, side-loop doubled spins <=16, sheet doubled
spins <=24, site sector doubled spins <=4. All requested numbers agree
with row 1085 at its quoted precision:

| beta_M | l_0 | l_1 | l_1-l_0 | m(0) | m(infinity) | endpoint difference |
|---|---:|---:|---:|---:|---:|---:|
| 2.4 | 1.008753842210 | 2.290676383234 | 1.281922541024 | 2.767209043907 | 1.754451262210 | 1.012757781698 |
| 8 | 11.658054627169 | 11.776046253465 | 0.117991626297 | 0.454294884304 | 0.408995600350 | 0.045299283953 |
| 9 | 13.274442565023 | 12.978097470342 | -0.296345094681 | 0.344242543645 | 0.359821720535 | -0.015579176890 |
| 10 | 14.667899734326 | 14.057128266781 | -0.610771467545 | 0.260247457560 | 0.321220592737 | -0.060973135177 |

Here m(0), m(infinity) denote Wilson beta_L endpoints, not heat times.
The first run's largest sheet block was 109, peak RSS about 65 MB.
Its JSON and full log are in `runs/gap-descent-sign-2-astra/`.
The second cutoff run (16,22,36; sectors <=6) has completed;
its results are saved separately before any older-code comparison.

The small-b diagnostic exposes a solver issue at b=0.02: the swap-even
and swap-odd levels nearly coincide, so a full-matrix eigensolve does not
resolve the tiny splitting reliably. The order-one target values are
separated. The next local correction will diagonalize each exact symmetry
block before sorting eigenvalues. This corrects the diagnostic's numerical
representation, not its normalization or the target operator.

The numeric lock helper initially failed because `automation_lock.py` is
missing from this sparse checkout. Its main-branch source was put in the
new scratch directory and supplied through PYTHONPATH. Acquisition then
succeeded at 2026-11-17 03:44:32 UTC. Memory-free share was 86 percent.
Runs are serial, nice 10, one BLAS thread, with a 2 GB self-stop.

Both runs were repeated after resolving center and layer-swap blocks before
eigensolving. Those are the final `results_sym_*.json` files. The original
logs are retained as diagnostics. The independent source and every run
have been hashed in `independence_receipt.json` before opening older code.
No older implementation has contributed to any number in this section.

| beta_M | l_1-l_0, cutoff 12/16/24 | cutoff 16/22/36 | endpoint difference, 12/16/24 | cutoff 16/22/36 |
|---|---:|---:|---:|---:|
| 2.4 | 1.281922541024204 | 1.281922541024204 | 1.012757781697833 | 1.012757781697836 |
| 8 | 0.117991626296627 | 0.117991626296623 | 0.045299283953243 | 0.045299283953256 |
| 9 | -0.296345094680774 | -0.296345094680779 | -0.015579176890129 | -0.015579176890114 |
| 10 | -0.610771467544579 | -0.610771467544575 | -0.060973135176583 | -0.060973135176571 |

The three cutoff numbers mean character count / maximum doubled side-loop
spin / maximum doubled sheet-link spin. Site-sector maxima are respectively
4 and 6 (physical spins 2 and 3). Truncation changes are below 6e-15 for
the leakage difference and 1.5e-14 for the endpoint difference. This is
observed stability, not a certified error. The final runs peaked below
82 MB; the largest zero-charge matrix was 256 and largest sheet matrix 226.

At every tested coupling, the vacuum is center-even and swap-even; the
first excited state is center-odd and swap-even. The ratios lambda_2/lambda_1
are 0.888006, 0.388939, 0.429792, 0.464794, in table order. The face winner
among all tested cycles is (1/2,1/2,1/2,1/2). Enlarging the sector range
does not change it. The generator symmetry defect is below 3e-16;
X^00 agrees with half-adjacency within the asserted tolerance.

The corrected small-b test gives l_1/(b^2/4) = 1.0001166576,
1.0007288114, 1.0029109866 at b=0.02,0.05,0.1. The deliberately wrong
adjacent-pair count gives 0.2500666619, 0.2504164802, 0.2516636856. Thus
the normalization test detects that specific fourfold-counting error.

## 3. Earlier code comparison, after the numerical freeze

Read in full, only after section 2 and the receipt were written:
`runs/gap-descent-sign-2/tplaq.py`, `endpoint2.py`, and
`runs/gap-descent-sign/su2box.py`. None was executed or imported.

There is no numerical disagreement and no first differing mathematical
term to report. The implementations differ as follows:

- `tplaq.py` uses a general floating log-factorial Racah sum. This script
  evaluates the half-spin 6j square as an exact rational one-term sum.
- The earlier zero-charge matrix truncates the Z sum at its loop cutoff D.
  This script includes every fusion-allowed term for its character cutoff.
- The earlier eigensolve is on the whole block; this script resolves the
  exact center and layer-swap sectors first.
- `endpoint2.py` constructs X from two 6j symbols. This script constructs X
  from magnetic-index Clebsch-Gordan sums, including their signs.
- The earlier endpoint range stops at site spins 2. This check also uses
  site spins through 3. All nonconstant cycles in each range are included.

The shared mathematics is Peter-Weyl, Schur orthogonality and recoupling;
the shared numerical libraries are SciPy/NumPy and their Bessel/eigensystem
routines. This is an independent implementation, not an independent
proof of numerical accuracy or a fully independent special-function backend.

## 4. Hand checks

### 4.1 Lemma FACE-PROD — HOLDS

Gauge-fix the four vertical links along their trees. The remaining eight
variables are A_l,B_l, l=1,...,4. Residual gauge transformations act at the
four transverse vertices, identically on both layers. At beta_T=0 the
face multiplication is `product_l exp(b x(B_l A_l^-1))`. The horizontal
kinetic operator is also a product over l. Thus M is a tensor product of
four sheet operators, restricted to residual gauge invariants.

One sheet is equivariant under simultaneous left and simultaneous right
SU(2). Its decomposition is

    direct_sum_(p,q) V_p tensor V_q^* tensor M_(p,q).

At a transverse vertex, adjacent factors contain V_q^* tensor V_p'.
Schur's lemma says its invariant space is zero unless q=p', and then is
one-dimensional. Taking invariants at all four vertices therefore leaves
exactly the direct sum of multiplicity-space products around closed cycles.
Each restricted eigenvalue is a product of sheet eigenvalues. This proves
the cycle formula without numerical truncation.

For the vacuum identification, the sheet operator is isospectral away from
zero to `exp(bx/2) K exp(bx/2)`. The latter has a strictly positive continuous
kernel. Compact positivity gives a positive simple top eigenvector. Uniqueness
and equivariance make that vector invariant under both sheet actions, hence
in sector (0,0). Its fourth tensor power is invariant at every vertex and
is the full product's top vector. Its eigenvalue is mu_00^4.

Terminology correction to 3.8: “multiplicity free” refers to coupling j,k
to each fixed p or q. M_(p,q) itself usually has infinitely many (j,k).
The earlier code already keeps those multiplicity spaces correctly.

### 4.2 Center symmetry — HOLDS; spectral identification is GUIDE

Multiply both A_l0 and B_l0 by -I for one fixed transverse link. In each
side plaquette the two signs cancel. The other side plaquettes are
unchanged. At beta_T=0 there is no transverse potential to change sign.
Central translations preserve Haar measure, commute with the horizontal
convolutions and vertex gauge action, and commute with the vertical-spin
Casimirs. The transformation therefore commutes with M, N, and B_t.

It sends each layer holonomy to its negative. On the zero-charge basis
its eigenvalue is `(-1)^(2a+2b)`; in dimension labels it is `(-1)^(a+b)`.
This proves the symmetry. It does **not** prove that the first excited state
is center-odd for every b. That identification is GUIDE on the computed
grid, as row 1085 section 3.5 itself states. Its RESULT parenthesis must
retain that qualification.

### 4.3 Leading l_1 = beta_M^2/4 — HOLDS

Put h=1/2 and z=a_h=b/4+O(b^3). Higher a_j have order b^(2j).
In the zero-charge block, the vacuum starts with |0,0>. The first two
excited states start with `( |h,0> +/- |0,h> )/sqrt(2)` and eigenvalue
z^4. Their positive off-diagonal entry is z^8+O(b^10), so the plus
combination is the first excited state for sufficiently small b.

For one adjacent pair of charged vertices, choose the short-arc loop J=h
and long-arc loop H=0. Its face coefficient is 2z. Applied to the plus
state, G contributes z^2/sqrt(2) from either occupied layer.
For input (a,b)=(0,h), the least-cost output has
`(u,v;r,s)=(0,h;h,0)`. The two squared recoupling entries in (1) are

    {0 h h; 0 h h}^2 = 1/4,
    {h 0 h; 0 h 0}^2 = 1/2.

These follow by coupling to spin zero, whose normalized singlet is
`(|+->-|-+>)/sqrt(2)`. Thus (1) is `4*(1/4)*(1/2)=1/2`.
Equivalently, each contraction uses the fundamental Schur integral with
denominator 2. The output amplitude is z^3/sqrt(2). Its kinetic weight
is z^4. The opposite occupied layer gives a different, orthogonal output
of the same weight. One adjacent pair therefore contributes z^10 before
division by lambda_1^2=z^8(1+O(b^2)). Four such pairs give 4z^2.

Every omitted term is higher order: long-arc fundamental propagation
costs two extra powers of z in its face coefficient; an opposite charged
pair has minimum face order b^2 and contributes O(b^4) to l_1; a spin-1
top arc or any higher face spin raises the combined face/kinetic order by
at least two. Corrections to G and lambda also start at higher relative
order. Therefore `l_1=4z^2+O(b^4)=b^2/4+O(b^4)`.

For comparison, the vacuum output is (h,0;h,0), coefficient 1, amplitude
2z, and kinetic weight z^2. Four adjacent pairs give
`l_0=16z^4+O(b^6)=b^4/16+O(b^6)`. These are hand expansions. The run is
only a diagnostic for their implementation.

## 5. Verdict and exact scope

| Statement checked | Verdict | Limit |
|---|---|---|
| Row 1085, 3.9(a), n=2, beta_T=0 | HOLDS at GUIDE grade | Both truncations reproduce the negative l_1-l_0 at 9 and 10. No infinite-matrix error bound. |
| Row 1085, 3.9(c), endpoint values | HOLDS at GUIDE grade | Both values and their difference agree. Finite sector cutoffs remain. |
| Zero-charge reduction and first charged level | HOLDS | Hand derivation from the unreduced cube; no numeric discharge. |
| Lemma FACE-PROD | HOLDS | Coupling multiplicities, not the whole sector spaces, are one-dimensional. |
| Center symmetry | HOLDS AFTER CORRECTION in the RESULT summary | Symmetry is proved; phi_1 being center-odd is GUIDE on the sampled grid. |
| Leading coefficient l_1=b^2/4+O(b^4) | HOLDS | Explicit singlet contractions above. |
| Extrapolation to BR-2 (not claimed in row 1085's scope paragraph) | FAILS | The first failing inference would be substituting 3.9(c)'s small-beta_L, large-beta_M, beta_T=0 point into row 1072 line 414. It is outside all three restrictions. |

The broad claim “on every such box for all positive couplings” fails at
GUIDE grade. A strict limiting endpoint inequality, if established for the
exact operators, extends to small positive beta_L by norm continuity:
nontrivial longitudinal convolution eigenvalues vanish uniformly as
beta_L tends to zero. Continuity in beta_T similarly extends a strict
endpoint inequality near zero. Thus beta_L=0 is not an escape from a truly
all-positive-coupling claim. The floating values do not themselves provide
the hand-checkable infinite-operator inequality needed to consume this as
a proof counterexample.

But literal P2, row 1076 lines 444-451, begins **on one-sheet boxes**.
Its all-beta_L, beta_M quantifiers do not include this transverse square.
This result concerns the proposed extension to boxes with transverse cycles.
It does not refute P2's one-sheet statement.

BR-2, row 1072 lines 406-420, needs the endpoint inequality only at
`beta_M=beta_T=beta`, with beta in the window and `beta_L in [beta,infinity)`.
The present negative endpoints have beta_L near zero, beta_M=9 or 10,
and beta_T=0. They touch none of that restricted descent range. The positive
check at beta_M=2.4 and beta_T=0 also proves nothing about the needed range.
The heat-kernel monotonicity statement is stronger than its endpoint form;
neither one can be transferred to the window by dropping its quantifiers.

Row 1085 already excludes the window and one-sheet boxes in its scope
paragraph. The clarification below preserves those exclusions; the actual
correction is to its RESULT's unqualified center-sector parenthesis.

Replacement qualification for row 1085's 3.9/RESULT:

> The two signs are independently reproduced at GUIDE grade for n=2,
> beta_T=0, beta_M=9 and 10. They contradict the all-box, all-coupling
> extension at that grade, not literal one-sheet P2 or BR-2's restricted
> window descent. The center symmetry is proved; identification of the
> first excited state as center-odd is numerical on the sampled grid.

No new attack was made. No n=3 result, positive-beta_T grid, other symmetry
sector claim, tunnelling explanation, or larger-volume claim was checked.
No audit, ledger, registry, FINISH, or source-author file was changed.

Credits: Claude Fable 5.2 medium for rows 1081 and 1085 and their model;
Claude Fable 5.2 max for row 1076's P2; Claude Opus 5.5 for row 1072's BR-2.
Peter-Weyl, Schur, Clebsch-Gordan and Racah provide the representation
identities. The SA transfer context is credited above to Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text.

RESULT: HOLDS AFTER CORRECTION of the center-sector qualification: independent code reproduces row 1085's n=2 negative leakage and endpoint signs at GUIDE grade (beta_M=10: -0.610771467545; 0.260247457560 versus 0.321220592737); FACE-PROD, center symmetry and l_1=beta_M^2/4+O(beta_M^4) hold by hand; the negatives do not touch one-sheet P2 or BR-2's window descent; no mass gap or audit status is claimed.
