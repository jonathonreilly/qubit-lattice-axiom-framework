# E1′-b (supervisor Poincaré bound): referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-09)

## Verdicts

- **E1′-b: CONFIRMED WITH CORRECTIONS.**
- **E1′ gravity after E1′-b: PASS**, strictly for the pre-registered scalar, source-driven \(G_0=aL\) proxy. The tensor/graviton bridge remains a scope caveat, not a PASS condition.

The core uniform \(s/\ell\) bound is sound for a regular source crossing the light cone nondegenerately. Several statements in the written proof are asymptotic or dimensionally mistyped and need correction.

## Findings

### 1. Poincaré inequality and add-one cost

Confirmed.

For bounded source region \(S\),
\[
0\le F\le \Pi(S),
\]
so \(F\in L^2\). The cited theorem indeed states
\[
\operatorname{Var}F\le\int \mathbb E[(D_zF)^2]\,\rho\,dz
\]
for \(F\in L^2\): [Last–Penrose, Theorem 18.7](https://stoch.math.kit.edu/img/Last/lastpenrose2017.pdf).

The add-one formula at [supervisor_E1p_b.md:13–17](supervisor_E1p_b.md:13) is exact, up to measure-zero coincidences:

- If \(z\) lies in several \(I(y,x)\), it kills every corresponding link, hence the sum.
- If \(z\nprec x\), both the new-link term and every blocking indicator vanish.
- The new point may simultaneously link to \(x\) and kill older links; both effects are present.
- Since \(x\) is fixed rather than sprinkled, it is not varied by \(D_z\). Treating \(x\) as an inserted Palm point gives the same surrounding Poisson law.

### 2. Diagonal term and shell measure

The shell calculation is correct only as a controlled asymptotic, not an exact identity for every macroscopic source.

Near the cone, writing \(t=-(r+\delta)\),
\[
m=\rho V\simeq \frac{\pi r^2\delta^2}{6\ell^4},\qquad
d\delta=\frac{\sqrt6}{2\sqrt\pi}\frac{\ell^2}{r}m^{-1/2}dm.
\]
Thus a locally constant, thick source gives
\[
\langle m\rangle=
\frac{\int_0^\infty m^{1/2}e^{-m}dm}
{\int_0^\infty m^{-1/2}e^{-m}dm}
=\frac12,
\]
so \(B_{\rm diag}=\mathrm{Diag}\) at leading order, as asserted at [supervisor_E1p_b.md:21–24](supervisor_E1p_b.md:21).

Corrections arise from source-profile variation and finite \(r\):
\[
O\!\left(\frac{\ell^2}{Ds}+\frac{s}{D}\right).
\]
Because \(s\gg\ell\), the first is bounded by \(s/D\) and can be absorbed into \(c\,s/D\).

“Thick” must mean thick in the cone-normal direction compared with
\[
\delta_{\rm shell}\sim \ell^2/D,
\]
with a nonvanishing, slowly varying cross-section where the cone passes through the source. Merely saying “macroscopic” is insufficient. For a thin source concentrated around \(m=m_0\),
\[
B_{\rm diag}/\mathrm{Diag}\simeq2m_0,
\]
not \(1\). A timelike source away from the cone can therefore fall outside the claimed bound; a wholly spacelike source has \(\bar N=0\).

### 3. Needle geometry and Monte Carlo

The geometry gives the right scaling, but not the literal constant written in the note.

The small-angle depth estimate
\[
v_*\sim\frac{(\sqrt\delta+\sqrt{\delta'})^2}{\theta^2}
\]
is valid up to fixed constants. For unequal shell variables a usable bound is
\[
|I\cap I'|
 \le \min\!\left\{
 \ell^4m,\ell^4m',
 \frac{C\ell^8}{b^4}
 \min(m,m')(m^{1/4}+m'^{1/4})^4
 \right\}.
\]
The omitted \(m,m'\) dependence is important: the constant \(23\) is not universal over unequal intervals. Its polynomial dependence is harmless because all required \(m,m'\) moments are exponentially integrable.

At [supervisor_E1p_b.md:30](supervisor_E1p_b.md:30), replacing \(\delta\) by \(\ell^2/(2D)\) turns the genuine bound into only an order-of-magnitude estimate. For \(m=1\), the actual coefficient is \(\delta D/\ell^2=\sqrt{6/\pi}\simeq1.382\), so \(4\pi\) is not itself an upper bound.

The Monte Carlo implementation at [S2_needle_overlap.py:23–47](S2_needle_overlap.py:23) is correct: it samples uniformly in a bounding region and rejects against both exact Minkowski interval tests. I reproduced its output. Independent full-interval sampling and reseeded importance runs gave a large-\(b\) plateau around \(22.6\), consistent with the stored \(23.0\) at [S2_needle_overlap.out:8–10](S2_needle_overlap.out:8).

Limitations:

- The stored run has no error bars or convergence assertions.
- It tests only \(r=r'\) and \(m=m'=1\), as fixed at [S2_needle_overlap.py:49–59](S2_needle_overlap.py:49).
- My unequal-\(r,m\) checks retained the \(b^{-4}\) tail but produced different plateaus, exactly as the corrected bound predicts.

Collinear/nested configurations are controlled by \(|I\cap I'|\le\min(V,V')\). Comparable endpoints actually have zero simultaneous-link probability and are merely overcounted by the upper bound.

Finally,
\[
2\pi\int_0^\infty b\,db\,\min(M,A/b^4)=2\pi\sqrt{MA},
\]
so the transverse overlap integral is finite.

### 4. Integration and uniformity

The probability inequality at [supervisor_E1p_b.md:25](supervisor_E1p_b.md:25) is correct:
\[
|I\cup I'|\ge\max(V,V')\ge\tfrac12(V+V').
\]

There is a dimensional typo at [supervisor_E1p_b.md:42](supervisor_E1p_b.md:42). It should read
\[
\int d\delta'\,e^{-m'/2}
 \simeq \frac{\sqrt{12}}{2}\frac{\ell^2}{r'},
\]
without the displayed prefactor \(\rho\).

With the corrected unequal-shell bound,
\[
\rho^2
\underbrace{s}_{\text{longitudinal}}
\underbrace{\frac{\ell^2}{D}}_{\text{normal shell}}
\underbrace{\ell^6}_{\text{transverse overlap}}
=\frac{s}{D}.
\]
All remaining \(m,m'\) factors give finite Gamma-function moments. Hence there is no hidden \(s/\ell\) or \(D/\ell\) factor.

The claim at [supervisor_E1p_b.md:46](supervisor_E1p_b.md:46) that the outer integral is specifically \(\sqrt2\,\mathrm{Diag}\) applies only after suppressing the overlap’s \(m\)-dependence. In the corrected calculation it becomes another finite numerical constant absorbed into \(c\).

Also, “\(F\le3\)” at [supervisor_E1p_b.md:49–52](supervisor_E1p_b.md:49) is not literal: the result is \(F_{\rm Fano}\le3+c\,s/D\), which is indistinguishable from 3 at the quoted physical scale.

### 5. Gravity reading

The bound supplies exactly the controlled large-\(s/\ell\) law missing from the prior review at [E1p_referee.md:83–91](E1p_referee.md:83). It is an analytic uniform bound, not a 38-decade extrapolation of the measured \(\kappa\).

The fixed setting defines \(G_0=aL\) and explicitly labels it the graviton proxy at [TESTS.md:307–324](TESTS.md:307). The E1′-b reading then expressly assigns PASS “for the scalar link proxy” while leaving the tensor bridge as unchanged scope at [TESTS.md:420–423](TESTS.md:420). Therefore the missing scalar-to-tensor bridge cannot consistently be imposed as an additional PASS gate now.

## Strongest correct statement

For a bounded, uniformly regular source family crossing the past light cone transversely, with cone-normal thickness \(\gg\ell^2/D\), bounded aspect ratios, and \(D\gg s\gg\ell\),
\[
\operatorname{Var}F
\le
\left[
3+C_S\left(
\frac{s}{D}
+\frac{\ell^2}{Ds}
+e^{-c(Ds/\ell^2)^2}
\right)
\right]\bar N
\le
\left(3+C'_S\frac{s}{D}\right)\bar N,
\]
where \(C_S,C'_S\) depend only on fixed source-shape regularity constants—not on \(\rho\) or \(s/\ell\).

Thus the scalar massless link field has a uniformly bounded Fano factor. For the quoted BNS proxy,
\[
\frac{\operatorname{sd}F}{\mathbb EF}
\lesssim
\sqrt{\frac{3+C'_S\,4\times10^{-22}}{2.2\times10^{57}}}
\simeq3.7\times10^{-29}.
\]
This establishes E1′ gravity PASS in its registered scalar-proxy scope; it does not establish tensor gravitational propagation, nonlinear gravity, strain response, or stable initial-value dynamics.