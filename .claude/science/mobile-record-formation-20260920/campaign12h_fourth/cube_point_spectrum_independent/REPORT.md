# Six-record cube: physical point spectrum of the fast rotor operator

Independent pre-comparison reconstruction, 2026-09-23.

**Result.** On the supplied physical **P-space** (every A site occupied),
with six records, total charge four, and unrestricted integer unit-rotor
fields on the cube,

\[
 \sigma_{\mathrm p}\bigl(-P T\Pi_1 T P\big|_{P\mathcal H_{\rm phys}}\bigr)
 =\varnothing .                                                   \tag{1}
\]

There is no nonzero normalizable physical eigenvector at any energy. The
proof reduces the question to a flat eigenvalue of a 36-by-36 Laurent matrix
on a five-dimensional flux torus. Two exactly evaluated **physical** fibers
have coprime characteristic polynomials, which excludes every such flat
eigenvalue. This is an exact finite certificate, not an inference from
numerical eigenvalue separations or from the earlier ring calculation.

The domain qualification matters. If the same sandwiched expression is
instead extended by zero to the complete six-record physical Hilbert space,
then every vector in `(1-P) H_phys` is a zero eigenvector. Equation (1) concerns
the P-space fast target in the supplied parent theorem. The two other W levels
have 96 and 36 matter words, respectively, and are not part of that target.

## 1. Premises, prior exposure, and read boundary

Vertices are the binary integers 0 through 7. The edges are bit flips,
oriented from the smaller to the larger integer, in the order

```
01, 02, 04, 13, 15, 23, 26, 37, 45, 46, 57, 67.
```

`A={0,3,5,6}`, the matter alphabet is exactly `{0,+1,-1}`, and
`div E=q-1_A`, with outgoing minus incoming divergence. A record of charge c
hopping along an oriented edge changes that electric integer by `-c`; the
reverse hop changes it by `+c`. Each legal term of T has amplitude -1.
No electric cutoff, finite-spin truncation, extra identity register, or
statistical exchange sign is introduced.

The supplied target is `H2=-A†A`, where `A=Pi1 T P`. Only this already checked
operator definition is imported from the parent theorem. No error estimate
for a microscopic approximation is needed for (1).

Prior exposure is explicit: I had independently built the earlier ring
fibers and the cube's immediate formation/path operators, and had compared
those packets with their then-authorized author sources. This reconstruction
uses the allowed, frozen own cube packet for conventions and a final
cross-check. The decisive builder here is new and imports no old or author
builder. I did not read `cube_point_spectrum_author`, actual-first-output or
finite-spin author/checker packets, new tail material, campaign plans,
checkpoint, or registry. No Git inspection or mutation was performed.
No external theorem or literature is imported: the analytic and arithmetic
steps below are proved directly.

## 2. Physical coordinates, without a flux truncation

Six records of total charge four consist of five plus records and one minus
record. In P, four A sites are occupied and exactly two of the four B sites
are occupied. Thus there are `choose(4,2)*6=36` P matter words. At W=1 and
W=2 the corresponding counts are 96 and 36.

Choose the spanning tree

```
01, 02, 04, 13, 15, 26, 37
```

and the five chords

```
23, 45, 46, 57, 67.                                      (2)
```

For each matter word q, let E0(q) be the unique integer solution of Gauss with
all five chord fields zero. It exists because the divergence source has zero
sum and the rooted tree incidence minor has determinant 1. One can construct
it by eliminating leaves of the tree; no division other than by ±1 occurs.
Let C be the twelve-by-five integer cycle matrix with zero divergence and
identity on the five chord rows. Then every physical integer field is uniquely

\[
 E=E_0(q)+C m,\qquad m\in\mathbb Z^5.                       \tag{3}
\]

The checker gives the complete C matrix and verifies its divergence, chord
rows, and the tree minor. Therefore

\[
 P\mathcal H_{\rm phys}\simeq\mathbb C^{36}\otimes
 \ell^2(\mathbb Z^5).                                      \tag{4}
\]

This parametrizes the entire stated sector, including arbitrary superpositions
and correlations of charge words and integer fluxes.

For a legal hop `q -> q'`, write its full twelve-link shift as d and its chord
part as s. Gauss and the zero-chord uniqueness give the exact identity

\[
 E_0(q)+d=E_0(q')+C s.                                     \tag{5}
\]

Thus its action in these coordinates is `- |q',m+s><q,m|`. All 216 first
hops from P to W=1 and all 504 ordered return paths were checked using the
actual twelve-link shifts, including immutable charge transport. Those
checks are identities for all m by (3), not samples of an infinite field
cutoff.

## 3. Fourier fibers and the point-spectrum criterion

Use the unitary Fourier convention for which an integer translation by s
multiplies by `z^s=exp(i theta.s)`. The hopping fiber is the 96-by-36 matrix

\[
 A(z)_{q',q}=-\sum_{q\to q'}z^{s(q\to q')},
 \qquad z\in\mathbb T^5,
\]

and the fast fiber is

\[
 h(z)=-A(z^{-1})^{\mathsf T}A(z)=-A(z)^\dagger A(z).         \tag{6}
\]

All coefficients are integers and all entries are finite Laurent
polynomials. Each P word has six first hops, so the diagonal is -6. The
return-path construction has 504 ordered paths and 324 distinct Laurent
matrix terms; every column has absolute path sum 14. In particular the full
operator is bounded and self-adjoint. The checker constructs (6) and also
constructs it independently by two consecutive legal physical hops; these
agree exactly at both certificate fibers.

Suppose a nonzero physical eigenvector exists at energy lambda. Its Fourier
transform is an L2 vector-valued function, nonzero on a set of positive Haar
measure. On that set,

\[
 D_\lambda(z):=\det(\lambda I-h(z))=0.                     \tag{7}
\]

A nonzero Laurent polynomial restricted to a torus has a zero set of Haar
measure zero. Here is the elementary argument. For one variable, multiply by
a monomial to obtain an ordinary polynomial, which has finitely many roots
unless it is zero. For several variables, view it as a polynomial in the last
variable. Outside the common zero set of its coefficient polynomials, which
has measure zero by induction using any nonzero coefficient, the one-variable
zero set is finite. Fubini completes the induction. Complex coefficients,
including a fixed real lambda in (7), cause no change.

Consequently (7) would have to vanish identically on the entire flux torus.
In particular lambda would be an eigenvalue of **both** of any two fibers.
It is therefore enough to exhibit two physical fibers with disjoint spectra.
This step does not assume analytic labeling of individual bands, simplicity,
a spectral gap, or irreducibility of the configuration graph.

## 4. Exact certificate from two physical fibers

Take every tree phase to be 1 and the five chord phases in (2) to be,
respectively,

\[
 z_0=(1,1,1,1,1),\qquad z_1=(i,i,i,i,i).                    \tag{8}
\]

These are ordinary points of the physical flux torus. The first matrix is
integer and the second Gaussian-integer Hermitian. Both characteristic
polynomials are monic with integer coefficients. The first is

\[
\begin{split}
 p_0(\lambda)={}&(\lambda+2)^5(\lambda+3)^3(\lambda+4)
 (\lambda+5)^5(\lambda+6)^6(\lambda+7)^5\\
 &\times(\lambda+8)(\lambda+14)
 (\lambda^3+25\lambda^2+176\lambda+248)^3.                 \tag{9}
\end{split}
\]

The complete second polynomial p1 and both full matrices are saved in
`CUBE_POINT_RESULTS.json`. Exact rational polynomial Euclid gives

\[
 \gcd_{\mathbb Q[\lambda]}(p_0,p_1)=1.                    \tag{10}
\]

There is also a compact modular certificate for (10), independently checked
against the exact characteristic coefficients. Modulo the prime 1009, the
values of p1 at the integer roots listed in (9) are:

| lambda | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -14 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| p1(lambda) mod 1009 | 239 | 45 | 794 | 782 | 175 | 179 | 238 | 473 |

For `c(lambda)=lambda^3+25 lambda^2+176 lambda+248`, its remainder is

```
r(lambda) = -319 lambda^2 -357 lambda +185  (mod 1009),
(437 lambda -475)c(lambda)
 +(33 lambda^2+135 lambda+15)r(lambda) = 1  (mod 1009).     (11)
```

Thus none of the factors of p0 can divide p1 modulo 1009. Two monic integer
polynomials with a common complex root have a nonconstant monic common factor
in Z[lambda] by rational polynomial gcd and Gauss's lemma. Its reduction
modulo 1009 would retain its degree and divide both reductions. Hence this
modular coprimality itself proves (10), without any floating-point spectral
argument.

The modular matrices use the exact map `i -> 469`, since `469^2=-1 mod 1009`.
Faddeev--LeVerrier, with all divisions legal because `1009>36`, reproduces the
reduced exact characteristic coefficients. Separate modular Gaussian
elimination verifies each polynomial at 37 distinct lambda values, sufficient
for a degree-36 polynomial. A full saved Bezout identity is checked again by
plain integer coefficient convolution in the secondary runner.

Equations (7)--(10) prove (1). The method uses two finite matrix evaluations
as an exact exclusion certificate, not as a numerical sampling heuristic.

## 5. Countercontrols and limits

A zero-angle fiber has an exact eigenvalue -14 with the uniform matter
vector. Its extension as a flux plane wave is not in `ell^2(Z^5)`. If instead
one uses the **normalizable** state consisting of that 36-word uniform
matter vector times the flux delta at zero, direct physical path summation
gives

\[
 \langle H_2\rangle=-26/3,\quad
 \langle H_2^2\rangle=244/3,\quad
 \operatorname{Var}(H_2)=56/9>0.                          \tag{12}
\]

This is a concrete check that a fiber eigenvector cannot simply be localized
in flux while retaining its eigenvalue.

A less informative phase test, replacing z1 in (8) by `(1,1,i,i,1)`, gives

```
gcd(p0,p_partial)=(lambda+2)^4(lambda+6)(lambda+7).
```

That inconclusive route is preserved in `SECONDARY_RESULTS.json`. Shared
roots at two special fibers do not prove a flat band; conversely, (8) really
does exclude one. The exploratory numerical spectra and modular evaluations
are preserved but are not needed for the proof.

Only the stated P-space point spectrum is determined. This report does not
classify all bands, prove a uniform gap, compute a formation-output spectral
measure, establish an absolutely continuous spectral decomposition, or infer
a waiting law, relaxation rate, subsequent-birth probability, or a macroscopic
limit. H4 and dissipative recycling are not included in the operator under
study. Fixed-fiber states and flux-truncated or finite-spin matrices are
different spectral questions. No contradiction is implied by the discrete
eigenvectors of a finite-dimensional approximation.

## 6. Evidence, failures, and reproduction

The decisive new runner is `cube_point_check.py`. It builds the physical
coordinates and all legal moves from scratch. `check_prior_and_certificate.py`
then compares its hopping matrices at three fibers with the pinned, earlier
own `operators.py`, after aligning matter bases; all three differences are
exactly zero in that numerical comparison. This secondary check is not a
substitute for the new exact certificate.

One failed run is retained under `failed_attempts/domain_equality/`, including
its original source, complete empty stdout, traceback, and command receipt.
SymPy retained the Gaussian-integer coefficient domain for a polynomial whose
coefficients were all ordinary integers, so direct `Poly` object equality
with the integer-domain constant polynomial failed. The repair explicitly
coerces the verified integer characteristic polynomial to Z[lambda] and
compares the finite-field constant gcd as an expression. No matrix entry,
model assumption, or scientific target changed. The corrected complete run
exited zero with empty stderr.

From this directory, using Python with NumPy and SymPy:

```
python3 cube_point_check.py
python3 check_prior_and_certificate.py
```

The second command verifies the frozen `CUBE_POINT_RESULTS.json` and the
pinned own prior builder. Complete stdout/stderr and actual subprocess
commands, start/end UTC times, exit codes, script hashes and stream hashes
are in the `*_RECEIPT.json` files. The exploratory and quarter-fiber scripts
and their successful run receipts are also retained. No author checker was
read or executed. No full physical time evolution or truncation was run.

The read sources, with SHA-256 identities, are:

- Parent supplied-model note, D3 `FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md`:
  `002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`.
  Reused already reviewed definition; current relevant Section 1 reread.
- Own D4 `second_event_independent/REPORT.md`:
  `39e2b04f9140f10db8d8bbd178a086902d9b09f6854b0e317a663071bacf4582`.
  Conventions and cube Section 5 reused; no new author source imported.
- Own D4 `second_event_independent/operators.py`:
  `a152167dff2cfff397397fcc56121cd9b2d79d7f412eb2e134f2f9cbbfa54c95`.
  Read completely; imported only in the secondary comparison.
- Own D4 `second_event_independent/PRE_COMPARISON_SEAL.json`:
  `e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734`.
  Identity and packet metadata checked, not a claim to reverify all earlier
  scientific artifacts during this bounded task.

`PRE_COMPARISON_SEAL.json` binds these source identities and every artifact
of the present packet. This is an independent reconstruction ready for an
explicitly authorized source comparison. It confers no formal audit,
publication, or retained-science status.
