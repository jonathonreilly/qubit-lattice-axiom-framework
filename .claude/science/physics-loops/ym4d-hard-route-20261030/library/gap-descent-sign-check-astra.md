## Repo search

Checker: OpenAI Codex, gpt-6-astra, xhigh; source commit
`aa86c6067820765dabd99a64e7d646296b30f942`. This is row 1082, a research
check of Claude Fable 5.2 medium's row 1081. It is not an audit, grants no
status, and claims no mass gap. No new attack or proof by computation.
It does not cover the full proof of Lemma KIN, infinite volume, or any
unperformed numerical test. The transverse-plaquette small-beta constants
in lines 154 are not verified. The other concurrent checker is not consulted.

The task-specific prior digest is absent. I read the shared
`prior/repo-search-2026-11-08.md` in full. That digest covers thirteen
November 8 targets, not this November 17 descent check. Its nearest hit is
PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`: positivity of a one-step
Wilson-loop correlation. I fetched `pull/10114/head` and read lines 1–16
and 96–160. This is a different assertion, not a descent-sign proof. The
digest reports the same source on PR 10133; I did not treat that report as
a fresh blob comparison. Its main/PR 10134/PR 10141 hits concern other
operators or copied hard-route work. No target-specific "Repo prior work"
line is supplied in row 1082. Thus I do not claim a fresh exhaustive search
of all those branches. No FLUX-EXC, MON-L, gap-descent or KIN-7 ownership
hit occurs in `library/open-registry.md`. Row 1081 is the source being
checked, not a competing proof task.

The SA-index README, matching chunk-02 rows 84–107, chunk-03 rows 125–132,
and obligations 97–107 led to outline lines 2195–2280, 2313–2335 and
3712–3720. The source already gives the Bessel coefficients, their ratio
bound (GL4), smooth convolution, and a positive transfer operator. These
are reused, not new results of row 1081. Its plateau statement explicitly
does not give a spectral gap. Searches for FLUX-EXC, MON-L, spin networks,
6j, total positivity, Karlin, Jentzsch and single crossing found no matching
descent proof in the outline index or CA-I 4.12–4.19 index. The latter
indexes different renormalization objects; none is imported here. This is
a bounded source comparison, not a theorem of absence from the account.
Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for these source formulas and the index's source material.
Balaban's papers are not used in this check.

## Source checkpoint and check order

Pinned source: `library/gap-descent-sign.md`, 181 lines. Downloads, each
fetched once from Sussman--Alpoge commit `31a47c543775`, are in the new
directory `/tmp/sa-gap-descent-sign-check-astra.7xVVKx/`.

This file was written incrementally. The Q_8 and beta=3/2 tests came first;
then the proofs, the cumulant reading, the three failed attempts and the
saved computations. All assigned checks are complete, with the explicit
noncoverage above. The full complete-account download was not read: no
CA-I premise was needed after the index comparison. Main's current
`SCIENCE_WORKFLOW.md` routes a research check to `procedures/check.md`;
the requested output path and verdict vocabulary here follow the user's
more specific task. No audit or broader review procedure was invoked.

## First tests

### Frozen Q_8: HOLDS AFTER CORRECTION of the displayed equality

Read row 1076, lines 392–416. Write c = cosh(beta_L), eta = exp(-beta_L).
On the five-dimensional class space the eigenvalues of D are 1, A, A, A,
B, where A = (c-1)^2/(c+3)^2 and B = (c^2-1)/(c+3)^2. Since
0 < A < B < 1, delta_2 = B. The face vacuum in the beta_M -> infinity
limit has character probabilities 1/8, 3/8, 1/2. Consequently

    q := <psi,D psi> = (1+3A+4B)/8 = (c^2+1)/(c+3)^2,
    q-B = 2/(c+3)^2 > 0.

The first false equality is row 1081 line 144, which identifies q with
1-12 eta exactly. Replace it by

    q = 1-12 eta+O(eta^2), B = 1-12 eta+O(eta^2),
    2 log q-log B = -12 eta+O(eta^2).

KIN-7 has delta(beta_L) = -8 eta+O(eta^2). The DIL bound is smaller,
not positive. It therefore does not give the forbidden sign. More directly,
q^2-B has numerator -6c^3-6c^2+6c+10, negative for sufficiently large c.
No heat-kernel Casimir on Q_8 is silently supplied: this test uses its
specified Wilson convolution. It checks DIL against KIN-7, not every
assertion about Q_8 or 2T in row 1076.

### N2-SMALL at beta = 3/2: HOLDS AFTER CORRECTION of the hand bound

The operator estimate in line 117 is correct:

    n_0(0) <= e^beta sup_(n>=1)(c_n a_n^2)/lambda_0,
    c_n=(n^2-1)/2, a_n=I_n(beta)/I_1(beta).

Use the already published GL4 ratio bound. For n >= 2 the ratio of
successive c_n a_n^2 is at most

    [n(n+2)/((n-1)(n+1))] beta^2/[4(n+1)^2]
    <= [(n+2)/(n-1)] beta^2/[4(n+1)^2] <= 1/4

when beta <= 3/2. (Both factors in the last expression decrease in n;
at n=2 it equals 1/4.) Thus the supremum is at n=2 and is at most
3 beta^2/32. Also lambda_0 >= I_0-I_2 = 2I_1/beta >= 1+beta^2/8.
The resulting bound (3/32)e^beta beta^2/(1+beta^2/8) increases in beta.
At beta=3/2 it is (27/164)e^(3/2).

Replace the unproved decimal 4.4817 in line 117 by this rational proof:
the exponential series through degree four sums to 563/128. Its tail
starts at 81/1280 and each subsequent term is at most one quarter of
its predecessor. Hence

    e^(3/2) <= 563/128 + (81/1280)/(1-1/4)
             = 2869/640 < 9/2,
    n_0(0) < 243/328 < 246/328 = 3/4.

Every displayed comparison is finite rational arithmetic or a geometric
series bound. No floating-point result discharges it. DIL then gives the
endpoint monotonicity; with TP-2 it gives n_1(t)-n_0(t)>0 for every finite
t >= 0 in this range. The number 0.69 at beta=1 in line 118 is not the
stated bound: that bound is e/12. Replace that sentence by the formula.

## Proof checks

### DIL (106–114): HOLDS AFTER CORRECTION of domains and the cut argument

The operator inequality is valid. State its hypotheses explicitly: S is
compact, M=SS* is positive with two positive top eigenvalues, and
0<=D<=I. Define delta_2 = ||wedge^2 D||; this definition also works if
the top of D's spectrum is not isolated. For a unit top eigenvector psi
of M, put Omega=S*psi/sqrt(lambda_0(M)). Then

    lambda_0(S*DS) >= lambda_0(M) <psi,D psi>,
    lambda_0(S*DS)lambda_1(S*DS)
      <= delta_2 lambda_0(M)lambda_1(M).

The second line follows directly from
||wedge^2(D^(1/2) M D^(1/2))|| <= ||wedge^2 D|| ||wedge^2 M||.
Subtract logarithms to obtain line 107. Require <psi,D psi>>0 and a
positive second perturbed eigenvalue when writing finite logarithms.
These conditions hold on the finite SU(2) boxes at positive couplings.
The general-group statement is conditional on these operator premises;
a nonnegative class density alone need not have nonnegative Fourier
eigenvalues, nor does every abstract compact group have a specified Casimir.

For D=e^(-hN), suppose N>=0 has a zero eigenvalue and let nu_1 denote
its second spectral value counted with multiplicity. Then delta_2=e^(-h nu_1).
Jensen in psi_s, the top eigenvector of B_s, gives

    m(s+h)-m(s) >= h(nu_1-2 <psi_s,N psi_s>).

The expectation is required finite. The supplied Wilson smoothing makes
it finite at s=0 for these SU(2) boxes, and at s>0 heat smoothing does.
The Rayleigh expression lambda_0(S*e^(-tN)S) is the supremum of positive
Laplace transforms. Holder proves each is log-convex, and taking suprema
preserves that inequality. Thus -d log lambda_0/dt=n_0 is non-increasing
where the top state is simple. This independently checks the exact
KIN-CVX input, not the full KIN reduction. For any orthonormal phi_0,
phi_1, the two-state variational principle gives n_0+n_1>=nu_1.
That pointwise inequality needs no simplicity of lambda_1; simplicity
is needed to identify it with the derivative of the ordered gap.

Line 112's per-cut argument is incomplete: equal integer parity does
not make both spins nonzero. For example on four spin-1/2 sites the
left intermediate spin can be 1 and the right intermediate spin 0.
Replace that argument by the following. If N is nonzero, some cut has
a nonzero left or right spin. Equal half-integer parity forces both to
be at least 1/2, costing at least 3/2. Integer parity with one nonzero
spin costs at least 2, which is already larger. Zero on every cut
forces all site spins to be zero, recursively from either end. The
character chi_(1/2)(Phi_2 Phi_1^(-1)) has exactly one charged cut and
cost 3/2. Therefore ker N consists of constants and nu_1=3/2 for every
one-sheet box with n>=2. The threshold n_0(0)<=3/4 follows as stated.
This proof does not use nonnegative face matrix entries at general n.

KIN-6 is consistent with the exterior-power argument too. Its two lowest
costs are c,a, not 0,nu_1, so delta_2=e^(-t(a+c)); the DIL bound is
-t(a-c) while the eigenvalue ordering stays fixed. The zero-bottom
specialization must not be applied to that example without shifting N.

### TP-2 (88–96): HOLDS, with the recalled steps made explicit

Here n in the matrix index means character dimension, not box length.
The sine transform gives J=(shift+shift*)/2 with Dirichlet endpoint 0.
Multiplication by exp(beta cos theta) is e^(beta J), hence the stated
Bessel difference kernel. Its two-particle additive compound J^[2]
acts on ordered pairs i<j by moving one index one lattice step with
coefficient 1/2; moves into the diagonal vanish. All its matrix entries
are nonnegative, and its graph is connected. To connect two ordered
pairs, first move the larger index above both pairs, move the smaller
one to its target, and then move the larger one to its target. Therefore
the exponential series has a strictly positive entry between any two
pairs. The bounded-operator identity

    wedge^2(e^(beta J)) = e^(beta J^[2])

identifies those entries with the ordered 2x2 minors. This proves their
strict positivity directly; no stochastic assertion or numerical
limit is needed. One-particle connectivity gives entrywise positivity.
Positive diagonal multiplication preserves both properties.

The diagonal d_n=a_n exp(-t c_n/2) tends to zero factorially already at
t=0. Thus B=d e^(beta J)d is compact, positive definite and injective.
It has infinitely many positive eigenvalues. For any real eigenvector
v of a compact self-adjoint matrix with strictly positive entries,
<|v|,B|v|> >= <v,Bv>, strictly if v has both signs. A maximizing
eigenvector consequently has one sign; its eigen-equation makes every
entry positive. Two orthogonal maximizing eigenvectors are impossible.
This is the compact Perron argument, justified by absolute convergence
using <|v|,B|v|><infinity. Apply it also to wedge^2 B, whose entries are
the positive minors. Its largest eigenvalue lambda_0 lambda_1 is simple,
so lambda_1>lambda_2. The eigenvector phi_0 wedge phi_1 has one strict
sign on all ordered pairs. Dividing by phi_0(i)phi_0(j)>0 shows that
r=phi_1/phi_0 is strictly monotone. Choose its sign to make it decreasing;
orthogonality then forces r(1)>0.

For every power k, N^k d is bounded, so the nonzero eigenvectors have
all required moments. This also justifies one-sided norm differentiation
at t=0 and ordinary differentiation at t>0. The same TP proof applies
to positive finite Wilson beta_L. The singular beta_L=0 endpoint is
excluded. Karlin--McGregor and Jentzsch receive the original credit;
the compound-generator and Rayleigh arguments above supply the recalled
steps in a form suitable for formalization.

### Reduction and SC (98–104): HOLDS with finite-moment convention

Orthogonality and normalization give E_p r=0 and E_p r^2=1. Thus the
covariance identity is exact. If 0<r(1)<=1, strict decrease makes
|r(n)|<1 somewhere. If r never went below -1, full support of p would
force E_p r^2<1, a contradiction. The last index n' with r(n')>=-1
is finite, and (r(n)^2-1)(c_n-c_(n'))>=0 for every n. Summation proves
SC. For a general nondecreasing replacement sequence require its two
state expectations finite, or formulate the result as the extended
signed sum after subtracting its value at n'. This avoids infinity
minus infinity. The actual quadratic cost has finite moments by TP-2.
The numerical qualification "at all t" in line 104 must read "at the
five sampled t values"; no continuum-in-t numerical check was performed.

### Spin networks: HOLDS on tested boxes; general-n positivity proof FAILS

Source lines 25–38, 84 and 130–138.

Peter--Weyl gives independent left and right singlet intertwiners for
each site-spin list. At n=2 and n=3 each relevant singlet space has
dimension one. The triangle basis, its parity condition, the two diagonal
K and D formulas, and the unreduced two-plaquette graph derivation all
agree. Coupling a character on an adjacent pair contracts the unique
left intertwiner and the unique right intertwiner. With matched real
phase choices these contractions coincide. Their product is the square
of the recoupling coefficient. Normalized Peter--Weyl matrix coefficients
supply sqrt(d_1 d_1' d_2 d_2'), giving line 31's squared-6j formula.
At j_3=0 the 6j square is 1/(d_1 d_1'), so the character product coefficient
is 1. The other printed hand value is also 1/2: integrating A first gives
int tr(AB) tr(A) dA = tr(B)/2, and int tr(B)^2 dB=1.

All nested cut Casimirs remain diagonal for every n, with eigenvalues
sum_k[L_k(L_k+1)+R_k(R_k+1)]. But at n>=4 the left and right coupling
labels L and R need not coincide. A matrix entry is a product of two
possibly different recoupling coefficients, not their square.
The first unsupported generalization is line 32, "The face part has
non-negative entries." Line 132 repeats the invalid squared-6j reason.

Here is an exact four-site diagnostic in a specified sequential basis.
Let s_ab=(up_a down_b-down_a up_b)/sqrt(2). In the four-spin-1/2 singlet
space choose u_0=s_12 s_34 and the spin-one pair singlet

    u_1 = (|uudd>+|dduu>
            -( |udud>+|uddu>+|duud>+|dudu> )/2)/sqrt(3).

These are the two sequential channels with intermediate spins 0 and 1.
For v=s_14 s_23, direct expansion of its four terms gives

    v = -u_0/2 + sqrt(3) u_1/2.

Define the orthonormal invariant functions
Psi_ab(Phi)=4<u_a,(tensor_(k=1)^4 Phi_k)u_b>, a,b in {0,1}.
Schur orthogonality proves normalization. Put
f=chi_(1/2)(Phi_4 Phi_1^(-1)); its site-spin list is (1/2,0,0,1/2).
The singlet identity chi_(1/2)(V U^(-1))=2<s,(U tensor V)s> gives

    chi_(1/2)(Phi_3 Phi_2^(-1)) f
       = (1/4)Psi_00 - (sqrt(3)/4)(Psi_01+Psi_10)
         + (3/4)Psi_11.

Thus the off-diagonal coefficient to Psi_01 is negative. For the
full one-sheet face generator X=(chi_12+chi_23+chi_34)/2, the other
two characters cannot reach the all-spin-1/2 sector from f: respectively
site 3 or site 2 stays trivial. Therefore

    <Psi_01, exp(beta X) f> = -sqrt(3) beta/8 + O(beta^2) < 0

for sufficiently small positive beta. The remainder is justified by
the bounded exponential series, ||X||<=3. This is a hand counterexample
to nonnegativity in this legitimate sequential basis. Rephasing or
choosing another basis is a separate question; this check does not
prove that no nonnegative basis exists. It does prove that the stated
multiplicity-free argument cannot establish the general-n claim.

Replacement text for lines 32 and 130–133:
"N is diagonal for every n. In the multiplicity-free bases of the two
tested boxes, the face part has nonnegative entries by the squared-6j
formula. A corresponding nonnegative basis for general n is not proved
here. DIL and its nu_1=3/2 specialization remain valid without it."
No conclusion about the uncomputed n>=4 gap sign follows from this
matrix-entry counterexample.

### CUM (120, 140, 167): HOLDS AFTER CORRECTION as a heuristic only

If r=+/- (c-E_p c)/sqrt(Var_p c), the exact identity is
Cov_p(r^2,c)=kappa_3(c)/kappa_2(c). This is a one-line expansion of
E[(c-Ec)^2 c]. It is not an identity for arbitrary eigenvector ratios.

The proposed fixed-t>0, beta->infinity shape is plausible: the leading
kernel is rank one, with vector n exp(-t c_n/2); after removing that
direction the displayed mixed term suggests the vector obtained by
orthogonalizing n^3 exp(-t c_n/2). The first unjustified inference is
"So ... phi_1 is close" in line 120. A leading asymptotic with only
relative o(1) error does not resolve the second eigenvector: its whole
eigenvalue is below the leading rank-one scale. One needs a sufficiently
high-order expansion, control after removing the moving leading vector,
and summable errors over all n,m. None is supplied. Fixed t>0 also does
not include t=0. No proof of the limiting distribution's right skew for
every t is supplied. Retain these claims as ARGUED, with these limits;
do not rewrite them as an equality for the actual SU(2) excess.

The Q_8 reading has a correct exact first-order version, with the costs
ordered correctly. The effective Wilson costs in KIN-7, in units of eta,
are 0,16,12 on probabilities 1/8,3/8,1/2, respectively. Thus their
increasing order has weights 1/8,1/2,3/8, not the order in line 120.
Their mean is 12, variance is 24, and third central moment is -192:

    (1/8)(-12)^3 + (3/8)4^3 + (1/2)0^3 = -192.

The ratio is -8, matching KIN-7's first-order gap difference. These
are the infinitesimal Wilson costs on that finite group, not a canonical
SU(2) Casimir assigned to its irreducible representations. This check
credits the point-mass weights and gap asymptotic to row 1076.

### Three failures of (S) (122–126): HOLDS as records of failed attempts

Way 1 has the precise limitation nu_1-2n_0<0; it then says nothing about
the sign. The saved n=2 run already exhibits this at beta=4,t=0.
It does not establish an exact transition near beta=3.3. Way 2 requires
r(1)<=1; the saved beta=8,t=0 value violates it at GUIDE grade. Neither
failure refutes (S).

For Way 3, suppose the sign pattern is (+,-,+), xi increases, and c is
a convex nondecreasing function of xi. A chord of that function through
the two crossing thresholds has slope gamma>=0. The function minus
the chord has the same three-region sign pattern. Multiplying by r^2-1
and summing proves the displayed inequality, using E_p(r^2-1)=0 and
finite moments. The missing ordered xi moment remains missing.
The first choice xi=c is circular. For the second choice define
kappa_n=a_n^2 exp(-t c_n) explicitly. The eigenvector correspondence
Omega_i=E sqrt(kappa) phi_i/sqrt(lambda_i) gives exactly

    E_(phi_i^2) kappa = lambda_i int E^(-2) Omega_i^2.

Neither factor orders their product in the required direction. The
printed assertion that the excited-state integral is larger is itself
not proved. The third, virial attempt has no written identity or
derivation to check; it records a mismatch of the weighted and unweighted
gradient integrals. Accordingly "FAILS as tried" is an honest record
of no proof, not a proved obstruction to all virial or moment methods.
No new route is attempted here.

## GUIDE code and saved evidence: HOLDS AFTER CORRECTION of scope

I read all 124 lines of `su2box.py`, all 31 lines of `n2_reduction.py`,
all eight saved logs, and compared all seven JSON files. I did not rerun
either eigensolver. The small bookkeeping comparison only reads saved
numbers; its full output and source-file hashes are in
`/tmp/sa-gap-descent-sign-check-astra.7xVVKx/saved-data-comparison.txt`.
The numerical comparisons below are GUIDE grade, including the comparisons
performed in this check. They are not error bounds for the infinite operator.

**Basis and 6j code (su2box 15–50).** Doubled nonnegative spins, all four
triangle tests, the integer-parity test and Racah's summation bounds are
correct. Each triangle contributes the square root of its three factorials
divided by the fourth; `tri` is their logarithm. The four lower sums and
three upper sums in lines 22–26 are precisely the Racah denominators.
`xmats` changes only the two adjacent spins by +/-1/2, includes the
dimension square root, squares the 6j and divides by two because x=chi/2.
The zero-spin spectator case gives X12(j',j)=1/2 for j'=j+/-1/2;
omitting the last factor would already fail this exact character test.
The graph/eigenvalue formulas at lines 73–98 match the hand derivation
for both boxes. In model n2, X23 vanishes under the restriction j3=0.

**Truncation and diagonalization (59–85).** The code uses
exp(beta P_J(X12+X23)P_J), not P_J exp(beta(X12+X23))P_J.
The difference consists of paths that leave the retained basis and return.
Thus the finite matrices are exponential approximants, not exact compressed
transfer operators. This is a valid approximation scheme but no error
bound is supplied. For two sheets the common cutoff also truncates the
intermediate spin j2, which can be larger than either outer spin. This
explains a possible source of slower convergence without proving its size.
The scalar exponential rescaling in line 71 cancels from every gap and
does not change eigenvectors. `eigh` returns the top three eigenpairs in
ascending order, used correctly in lines 81–84. The stored data have no
residual bounds or interval certificates. At degenerate eigenvalues,
one returned vector's N expectation does not certify the whole eigenspace.

**Recorded grids.** Every JSON has the 24 Wilson beta_L values and 18 heat
times printed in lines 106–107. The actual cutoff coverage is:

| Model | beta_M | Recorded doubled-spin cutoffs |
|---|---|---|
| n3 | 0.5, 1, 2, 2.4, 3, 4 | 10, 14, 18 |
| n3 | 6 | 14, 18 |
| n3 | 8 | 14, 18, 22 |
| n3 | 12 | 22 only |
| 2s | 0.5, 1, 2, 2.4, 3, 4, 6, 8 | 10, 14, 18 |

The raw logarithms and arrays agree on positive Wilson differences and
positive sampled heat increments. Every saved Wilson sequence decreases.
The lowest recorded flux excess over both models is about 0.97096490
(2s, cutoff 10). Thus the report's sampled sign survives. It does not
establish that sign between grid points or after removing the cutoff.

These are maxima of differences over each common saved grid, rounded up:

| Comparison | beta_M | Wilson gap differences | Heat gaps | Flux excess |
|---|---:|---:|---:|---:|
| n3, 14 versus 18 | <=4 | 2.1e-11 | 3.7e-13 | 2.0e-13 |
| n3, 14 versus 18 | 6 | 1.8e-10 | 2.6e-10 | 1.3e-9 |
| n3, 14 versus 18 | 8 | 5.6e-8 | 5.1e-8 | 5.1e-7 |
| n3, 18 versus 22 | 8 | 1.8e-12 | 2.3e-12 | 2.2e-11 |
| 2s, 14 versus 18 | <=4 | 2.1e-11 | 1.3e-11 | 3.3e-10 |
| 2s, 14 versus 18 | 6 | 1.7e-7 | 1.8e-7 | 6.3e-6 |
| 2s, 14 versus 18 | 8 | 2.7e-5 | 3.0e-5 | 1.4e-3 |

Three cutoffs do not agree to all displayed digits. For 2s, 10 versus 14,
beta_M=8, the maxima are 0.004300 in Wilson differences, 0.008096 in heat
gaps and 0.323203 in flux excess (upper-rounded). Even at beta_M=4 the
Wilson difference is 2.64e-6. The three cutoffs agree on the sampled sign.
The last two agree much more closely, as the table specifies. At 2s,
beta_M=8, the largest last-two flux difference is 0.00130934188 at t=0.002;
it is not solely the choice of a vector at the degenerate t=0 endpoint.
The face gap printed in the source's beta_M=8 table is the cutoff-14 value
2.5403260852; cutoff 18 gives 2.5403230826. There is no cutoff-22 2s run.
There is only one n3 cutoff at beta_M=12.

**Face degeneracy (50, 78, 137).** The finest 2s cutoff, 18, is consistent
with a double first excited level at the displayed precision. Coarser
cutoffs visibly split it: at cutoff 10, beta_M=8, the first two gaps
are 2.5433385303 and 2.555437. "As they must"
in line 50 is stronger than decoupling alone proves. After the two outer
gauge averages the face is two copies of an operator Q on L^2(SU(2)),
restricted to joint conjugation invariants. Write lambda_(L,0) for Q's
largest eigenvalue in conjugation spin L, lambda_(0,0) for its vacuum,
and lambda_(0,1) for its second scalar eigenvalue. Then the invariant
second eigenvalue can be either

    lambda_(0,0) lambda_(0,1), or sup_(L>0) lambda_(L,0)^2.

The first candidate has two copies. To prove it is largest needs a
comparison with the charged candidates; the text supplies none.
Replace the unconditional multiplicity claim by the observation from
the finite grids. DIL does not need it, and all grid numbers stay GUIDE.
The separate `su2box.py n2 40` regression mentioned in line 50 has no
saved log or JSON here, so I did not verify that run. The n2-reduction
log supplies a different, 60-character scalar comparison.

**n2-reduction.** The code uses the correct exact Bessel-difference
entries before cutting to 60 characters. Its `ive` scale multiplies B
by the harmless scalar e^(-beta). The ratio and sign pattern discard
coordinates with phi_0^2<=1e-24; therefore they test only the retained
coordinates. No second cutoff is saved. The docstring promises a
minimum 2x2-minor sign, but the script does not compute any minors.
The 45 printed rows show r(1)>1 at beta=8,12,16 and the specified small
times, consistent with the stated failure of SC's hypothesis. From the
rounded log the cumulant ratio exceeds the actual excess by between
0 and 23.881 percent; the strict "above at every point" claim cannot
be resolved where those printed values coincide. This supports the
reported approximate agreement only. Neither script enforces BLAS
thread count, a memory ceiling, or a machine lock; those are caller
claims, not verified properties of the saved source or logs.

## Remaining lines and verdict ledger

Lines 148–155 do not close the several-sheet case. The kernel observation
is correct: invariance under the residual gauge group and every cut
rotation is equivalent to independent gauge invariance on each layer.
A transverse tree then has only constant invariants; a transverse
plaquette admits infinitely many characters of its holonomy. Thus on
the latter box nu_1=0 counted with multiplicity, and DIL supplies no
positive slope. This does not depend on a sign convention for spin networks.

The large-t formula in line 153 is a conditional Schur-complement formula.
State that lambda_i(infinity)>0 is a simple eigenvalue of P_0 M P_0,
phi_i is its unit eigenvector in ker N, and 3/2 is the first contributing
positive N level. The off-diagonal block is e^(-3t/4)P_0 M P_1;
eliminating its complement gives the eigenvalue correction
e^(-3t/2)||P_1 M phi_i||^2/lambda_i(infinity). Dividing by lambda_i
and differentiating gives the printed l_i and n_i. Degenerate levels
require diagonalizing that correction within their eigenspace.
Without these qualifications the formula is not a general theorem.
The small-beta l_0,l_1 estimates in line 154 have no calculation supplied;
they remain ARGUED and are not verified here. No new plaquette test is run.

| Statement | Verdict | First issue or restriction |
|---|---|---|
| n=2 and n=3 spin networks; two-sheet n=2 formulas | HOLDS | Matched real phases; two tested boxes only |
| N diagonal at all n | HOLDS | Keep independent left/right coupling labels |
| Nonnegative face entries at all n by the squared-6j proof | FAILS | Line 32; explicit n=4 sequential-basis counterexample above |
| TP-2 | HOLDS | Positive beta and positive finite Wilson beta_L; compound proof supplied |
| Covariance reduction and SC | HOLDS | Finite-moment convention for arbitrary replacement costs |
| DIL and the one-sheet dilute criterion | HOLDS AFTER CORRECTION | Name the operator premises; fix line 112's integer-cut argument |
| N2-SMALL | HOLDS AFTER CORRECTION | Replace line 117's decimal endpoint by the rational series bound |
| CUM | HOLDS AFTER CORRECTION as ARGUED only | Line 120 does not control the second eigenvector; order Q_8 costs correctly |
| Three failed methods | HOLDS as attempt records | No no-go theorem or counterexample to (S) |
| GUIDE signs and truncation account | HOLDS AFTER CORRECTION | State actual cutoff agreements and sampled-only scope |

The repaired heat-kernel conclusion supplies FLUX-EXC only at n=2,
0<beta_M<=3/2, and the conditional dilute criterion for other one-sheet
boxes. TP-2 and SC do not by themselves prove the missing r(1) bound.
The Wilson endpoint inequality remains the conditional DIL bound; no
explicit Wilson coupling range was proved by this note. The all-coupling
one-sheet sign and the several-sheet sign remain open in this source.
No source file, registry, FINISH row, audit record or scientific status
was edited. No new numerical research, formal Lean check or full KIN
check was performed.

RESULT: Row 1082, checked line by line by Codex (gpt-6-astra, xhigh): TP-2, SC and the tested-box spin formulas HOLDS; DIL and N2-SMALL HOLDS AFTER CORRECTION with explicit hand repairs; the claimed general-n squared-6j positivity extension FAILS first at row 1081 line 32; CUM stays ARGUED with its missing eigenvector control named; saved kill-test signs survive only at GUIDE grade with corrected truncation and sampling scope; no general descent sign or mass gap is claimed.
