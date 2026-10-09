# E1′: referee report (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-09)

Verdicts: **gravity INCONCLUSIVE** (worker's PASS not confirmed: the large-s/ℓ Fano asymptotic is an extrapolation over ~38 decades; scalar-to-tensor bridge not derived); **matter M-INCONCLUSIVE** (worker's M-FAIL not confirmed: single-event amplitudes are not the packet-plus-detector observable; regeneration along the trip not computed). Paths point to the referee's scratch copy; the worker's files are in `scripts/E1p/`, the referee's check in `scripts/E1p/referee/`.

# E1-prime independent referee report

**Referee verdicts against the fixed readings**

- **Gravity: INCONCLUSIVE — the worker's PASS is NOT CONFIRMED.** The exact mean, locality-of-dependence, Mecke mean/diagonal term, and the tested Fano factors are sound. The registered PASS, however, requires an exact or controlled asymptotic noise law and forbids a long fitted extrapolation. Here the load-bearing $F-1=\kappa s/D$ structure is argued, while $\kappa$ is measured only for $s/\ell=6,12,24$ and is then used at $s/\ell\sim10^{39}$. The enormous margin makes a failure implausible, but does not satisfy the fixed epistemic rule. The scalar-to-tensor/GW bridge is also not derived. `TESTS.md:5-9,333-338`; `E1p_report.md:101-107,212-220`.
- **Matter: M-INCONCLUSIVE — the worker's M-FAIL is NOT CONFIRMED.** Point-to-point and compact-source/single-event amplitudes do become noise dominated below 1 km (robustly so for the proton), but those are not equivalent to coherent propagation of a wavepacket into a smeared detector. The packet formula is only a one-generation argument and uses packet width, not travel distance; accumulation along a long worldtube is not solved. M-PASS is also unavailable: the point observable is unbounded, the finite-density mean has a growing complex pole, and the proposed 4D variance renewal is not established. `TESTS.md:327,340-343`; `E1p_report.md:170-185,223-228`.

## 1. Normalisations

**Confirmed.** Johnston gives

\[
K_R^{(2)}=\tfrac12 C(I-abC)^{-1},\qquad b=-m^2/\rho,
\]

and

\[
K_R^{(4)}=aL(I-abL)^{-1},\qquad
a=\frac{\sqrt\rho}{2\pi\sqrt6},\qquad b=-\frac{m^2}{\rho}.
\]

These are stated directly in `lit_johnston/johnston_0909.0944.txt:200-223` and derived in `lit_johnston/johnston_0806.3083.txt:440-480,486-615`. The exact mean Volterra equation is `lit_johnston/johnston_0806.3083.txt:304-315`, and that paper explicitly leaves fluctuations open at `:618-630`.

The matrix recursion in `scripts/e1p_core.py:7-9,107-131` has the right ordering and powers. Because (K(x,y)) approximates a continuum kernel pointwise, a source integral is estimated by

\[
\phi(x)=\rho^{-1}\sum_y K(x,y)J(y).
\]

That factor is correctly documented at `scripts/e1p_core.py:3-9`. The executed simulations all set (\rho=1), so its absence as an explicit factor in the numerical `KJ` array does not change those runs; the code is not, by itself, a general-density implementation.

## 2. Means

**Mostly confirmed, with precision corrections.**

- For fixed endpoints, (E[L(x,y)]=\exp[-\rho V(x,y)]), (V=\pi\tau^4/24), hence (E[aL]=a e^{-\pi\rho\tau^4/24}\to\theta(t)\delta(\tau^2)/(2\pi)). This is Johnston's `lit_johnston/johnston_0806.3083.txt:493-550` and the code uses the same kernel at `scripts/E1p_0_mean_massless.py:1-12`.
- The static response is massless with a power correction
  \(4\pi rG_{\rm stat}=1-[6/(\pi\sqrt6)]\ell^2/r^2+O(\ell^4/r^4)\), not a Yukawa correction. The numerical values reproduce it at `out/E1p_0_mean_massless.out:1-8`.
- At finite density the kernel has support throughout the timelike interior of the retarded cone with an exponentially small tail in (\sigma=\tau^2); it is not literally supported only on a finite-width shell. For (r\gg\ell), the normalized shell law is proportional to (e^{-\pi\sigma^2/(24\ell^4)}), with mean (1.5593936\ell^2), standard deviation (1.1781385\ell^2), and time offset (\langle\sigma\rangle/(2r)=0.779697\ell^2/r). The measured moments agree at `out/E1p_1b_massless_summary.out:20`; these moments are asymptotic in (r/\ell), not exact at arbitrary (r).
- The mean two-link count is exactly
  \[
  E[L^2(x,y)]=\rho\int_{I(y,x)}e^{-\rho[V(y,z)+V(z,x)]}\,d^4z,
  \]
  and **tends** to (3\pi). It is not exactly (3\pi) at finite (\tau/\ell). In the large-(\tau) limit the Jacobian tends to (\pi/2), giving
  \((\pi/2)[\int_0^\infty e^{-\pi s^2/24}ds]^2=3\pi\). The finite values 8.953 at (\tau/\ell=8) through 9.406 at 40 are at `out/E1p_5_mean4d.out:1-6`; the independent constant check is `referee_checks.py:52-80`.
- Shape-blindness in law under a constant determinant-one linear deformation is exact for order/link functionals, as already established for E1. It is ensemble-law invariance, not smooth response in one fixed realization. `E1_referee.md:30-34`.

## 3. Massless noise

### Exact part

For (N_J=\sum_{y\in\Pi}J(y)L(x,y)), Mecke gives the exact mean

\[
E[N_J]=\rho\int J(y)e^{-\rho V(y,x)}d^4y
\]

and exact diagonal contribution

\[
\operatorname{Var}_{\rm diag}N_J=\rho\int J(y)^2e^{-\rho V(y,x)}d^4y.
\]

The off-diagonal term is a genuine pair integral: it is zero joint probability for comparable endpoints and (e^{-\rho|I(y,x)\cup I(z,x)|}) for incomparable endpoints. Thus the mean and diagonal are exact; the reported total Fano law is not. The code implements the corresponding quadratures at `scripts/E1p_1_massless_needle.py:113-138`.

The dependence region is also exact: (N_J(x)) depends only on source points and the union of their open intervals with (x). `scripts/E1p_1_massless_needle.py:1-8` correctly constructs a cylinder containing every interval for retained endpoints. The computation is exact for the **truncated** functional (\rho V<24). The omitted asymptotic mean fraction is (\operatorname{erfc}(\sqrt{24})\simeq4.3\times10^{-12}), so the truncation is more than adequate here, although the inverse-CDF region sampler itself uses a fine numerical table (`:38-80`) and is not literally exact.

No sprinkling outside this region affects the direct massless field. This does not extend to the massive recursion or to an autonomous initial-value evolution.

### Fano factors and relays

The stored valid arrays reproduce the tabulated Fano factors; the quarantined file is not matched by the analysis glob. At the statistically informative ratios (s/D=0.3,0.1), the inferred (\kappa=(F-1)D/s) runs from about 3.5 to 5.6. Through-origin fits using all distances give (\kappa=3.51,4.39,4.91) for (s/\ell=6,12,24). At the largest distances (F-1) is consistent with zero, so multiplying it by (D/s) does **not** measure (\kappa) precisely; e.g. the (D/\ell=10^5) row has (F=1.020\pm0.037). `out/E1p_1b_massless_summary.out:2-18`; `referee_checks.py:25-49`.

The comparison of measured relative noise with \(\sqrt{F/\bar N}\) is nearly algebraic because (F) is computed from the same sample variance; the independent checks are the mean quadrature and the source-profile comparison. The latter is good (`out/E1p_1_massless_A.log:1-17`).

The two-stage relay data are real checks and agree with the branching estimate to about 0.5-6% (`out/E1p_2_relay.out:1-10`). They establish only (k=2). “No compounding for arbitrary (k)” remains an argument; correlations shared across many relay stages were not controlled. Direct (G_0=aL) has no relay recursion in the first place.

### Extrapolation and scaling

Yes: taking (s/\ell=6\)–24 to (s/\ell\sim10^{39}) is a long extrapolation under `TESTS.md:8,336`, even though (D/s\) is also driven into a regime where the measured (F) is close to one. No executable artifact proves a uniform bound on (\kappa(s/\ell)) or the cancellation that yields (F-1\propto s/D).

The numerical margin is nevertheless enormous. For the worker's BNS proxy, \(\bar N=2.20\times10^{57}\). Raw coherence would require (F\simeq2.20\times10^{57}); after the report's ad hoc 10-fold amplitude penalty, (F\simeq2.20\times10^{55}). If one assumes the structural form (F-1=\kappa s/D), the required (\kappa) is (6.8\times10^{77}) raw or (6.8\times10^{75}) with that penalty. Starting from (\kappa=5) at (s/\ell=24), this corresponds to (\kappa\propto(s/\ell)^p) with (p=2.01) raw or (p=1.96) with the penalty. Thus “faster than quadratic” is only approximately true and is false once the report's own 10-fold penalty is included. `referee_checks.py:83-105`.

The duration count (\bar N\propto s^2\min(T_s,O(s))/(D\ell^2)) is supported at one (s,D) by `out/E1p_1b_massless_summary.out:3-6`. The claimed fixed-physical-geometry density law, relative noise (\propto\rho^{-1/4}=\ell), is conditional on (F) staying bounded: (\bar N\propto\ell^{-2}) is controlled, but (F(s/\ell,D/\ell)) was not taken through a density scan.

These gaps trigger the fixed INCONCLUSIVE reading despite the very strong numerical safety margin.

## 4. Massive sector

### Two-link floor and seed

For timelike separation with the direct-link probability negligible,

\[
K=a^2bL^2+O(b^2),\qquad |a^2b|=\frac{m^2}{24\pi^2},
\]

so

\[
\operatorname{sd}K=\frac{m^2}{24\pi^2}\sqrt{\operatorname{Var}L^2}.
\]

The cancellation of (\rho) is exact in this coefficient. The limiting distribution of (L^2), however, is being used: neither (E[L^2]=3\pi) nor its variance is density-independent at arbitrary finite (\tau/\ell). Also, at fixed finite (\tau/\ell), the literal (m\to0) limit is (aL), not (a^2bL^2); the two-link floor takes the large-timelike-separation limit first. `scripts/E1p_3b_analyse4d.py:1-22`; measured Fano factors are at `out/E1p_3b_analyse4d.out:2-3,18-19,34-35,50-51,66-67,82-83`.

Using (\operatorname{Var}L^2\simeq3\pi F), the exact coefficient against the Bessel envelope is (0.204124\sqrt F\,(m\tau)^{3/2}), slightly above the report's 0.2036. For (F=1), the crossing is (m\tau=2.8845). The stored arrays support a crossing near 2.9 in the continuum regime. “At every density” is too strong; the claim is valid for (m\ell\ll1) and (\tau/\ell\gg1), which overwhelmingly includes the Planck-density translation. `referee_checks.py:52-80`; `out/E1p_6_renewal4d.out:34-45,49-60,64-75`.

The per-end seed law is correct as the leading continuum endpoint diagram:

\[
\frac{\operatorname{Var}_{\rm end}}{G_{m,\rm env}^2}
=\frac{\sqrt6}{96}(m\ell)^2(m\tau)^3.
\]

An independent derivation uses (P_1\to2\pi\sqrt6\ell^2G_0),
\(\int_0^\infty J_1(x)^2dx/x=1/2), and the Bessel envelope. This proves the coefficient in the first-order/endpoint asymptotic. It does not prove that this diagram is the full variance or a lower bound for a compact source without the worker's unproved first-chaos approximation.

The actual smeared simulations use (w=1.5\ell), not the claimed regime (\ell\ll s\ll1/m), and the seed estimate often overpredicts substantially (`scripts/E1p_6c_KJ_seed.py:1-5`; `out/E1p_6c_KJ_seed_partial.out:17-30,32-45`). They therefore do not check the physical compact-source extrapolation.

### Packets, renewal, and long travel

The packet formula

\[
\operatorname{Var}/\operatorname{mean}^2\simeq
\frac{\sqrt6}{24\pi}(m^2\ell\sigma)^2
\]

has the right dimensions and is a plausible one-generation endpoint result for a packet/detector width (\sigma\gg1/m). It has no direct simulation here. More importantly, (\sigma=1\) km in `out/E1p_7_translate.out:18,27` is a **packet width**, not a demonstrated propagation distance. Restricting the field to a worldtube removes transverse links where the mean field vanishes, but it leaves many longitudinal regeneration opportunities. Their accumulation with travel distance (D) could add diffusively or renew multiplicatively; replacing (D) by (\sigma) for the entire trip has not been derived.

The supervisor's gain count is correct inside the overlap-free model:

\[
(ab)^2N_{\rm links}(T)
\sim\frac{\sqrt6}{24\pi}m^4\ell^2T^2,
\]

which corresponds to the tachyonic renewal mass
\(q=m^4\ell^2/(2\pi\sqrt6)\) and variance rate
\(\gamma_{\rm var}=\sqrt q=0.254901m^2\ell\). This validates the coefficient, not the renewal closure. The code explicitly omits overlaps between distinct link intervals (`scripts/E1p_6_renewal4d.py:1-9`), the simulation comparison stays at pre-asymptotic separations with ratios 0.83-1.65 (`out/E1p_6_renewal4d.out:4-15,79-90`), and the refined rate run did not finish (`out/E1p_6b_renewal_rate.out:1`). Hence exponential variance growth in the actual 4D process is **not established**.

The 2D causal-matrix control is much stronger: its pair-of-chain Volterra equation has no link-emptiness overlaps and direct simulation agrees with it (`scripts/E1p_4_massive2d.py:1-6`; `out/E1p_4c_2d_sim_vs_exact.out:1-10`). The asymptotic (m^3\ell^2/4) rate is a controlled asymptotic of that exact equation and is numerically approached, rather than an exact finite-parameter identity (`out/E1p_4b_exact2d_growth.out:21-25`). It does not validate the omitted-overlap 4D closure.

### Mean pole

Yes, the slow 4D mean growth is a complex-pole effect. At zero spatial momentum the spatially integrated link kernel has

\[
q(t)=\int d^3x\,e^{-\pi(t^2-r^2)^2/(24\ell^4)}
=2\pi\sqrt6\,\ell^2t-\frac{12\ell^4}{t}+\cdots.
\]

The (-12/t) term produces (+12\ell^4\log(s\ell)) in its Laplace transform. Perturbing the continuum poles (s=\pm im) of (1+a m^2\tilde\mu(s)=0) gives a conjugate pair

\[
\operatorname{Re}s=3\pi A\,m^3\ell^2
=\frac{3}{2\sqrt6}m^3\ell^2
=0.612372\,m^3\ell^2+\cdots,
\]

with a logarithmic frequency shift. This independently explains the measured \(\sim0.6m^3\ell^2\) mode. `scripts/E1p_5_mean4d.py:1-8,47-58`; `out/E1p_5_mean4d.out:21-55`; `referee_checks.py:68-80`.

## 5. What “propagation coherent over at least 1 km” measures

The physically appropriate object is a prepared wavepacket convolved with a detector response, at specified momentum/boost, after a specified laboratory travel distance. A Green function between two individual events is a distributional kernel, not by itself a particle coherence observable. A smooth compact source read at one event improves the source side but leaves an unsmeared detector. Also, all quoted point/compact distances are proper times converted to metres; a particle travelling 1 km in the lab has proper time (L/(\beta\gamma)), so there is no unique “electron/proton coherence length” without a momentum. The report itself notes this boost issue at `E1p_report.md:208`.

The point-to-point ( (m\tau)^{3/2}\) law is genuinely unbounded, so it violates the literal “stays bounded” clause even though it is not exponential. The parenthetical “no exponential growth” cannot convert an unbounded power law into a bounded function. The argued 4D renewal exponential is not established, while the finite-density mean complex pole is established asymptotically but lies at enormous physical distances.

Thus M-PASS is not earned. M-FAIL is also not earned because the controlled failure is for single-event observables, while packet-plus-detector propagation and its longitudinal accumulation were not computed. The fixed fallback is **M-INCONCLUSIVE**.

## 6. Translation

- The arithmetic (\bar N=2.20\times10^{57}) and raw BNS proxy noise (2.13\times10^{-29}) at 1 Gpc is correct for the chosen scalar source volume. The 10-fold quadrupole penalty is an unsupported proxy factor, not a derived tensor result. `out/E1p_7_translate.out:1-5`.
- The mean offset (2.20\times10^{-104}) s, shell spread (1.66\times10^{-104}) s, and fractional offset (2.1\times10^{-121}) are correct moments of the asymptotic scalar link kernel (`out/E1p_7_translate.out:6-7`). Calling them the full GW arrival spread requires the missing source/wavepacket/tensor bridge.
- The leading finite-slab link count (\sqrt6\pi(T/\ell)^2\) is correct, giving (5.01\times10^{122}) over (ct_0) (`out/E1p_7_translate.out:8`). Valency remains unbounded as the past grows. Those unused links do not enter direct (aLJ), but massive path sums and initial-value recurrences do use intermediate events.
- The electron/proton point crossings, compact-source seed lengths, packet-width numbers, and conditional renewal factors are arithmetically correct: electron 0.864-1.22 km and proton 3.14-4.44 mm for the event read; packet-width variances (3.82\times10^{-16}) and (4.34\times10^{-3}); conditional proton renewal factor 1.098 over 1 km. `out/E1p_7_translate.out:12-29`; independent reproduction at `referee_checks.py:108-124`. They are not all measurements of the same operational coherence observable.
- The mean is exactly massless for (G_0) in the continuum limit, so no scalar Yukawa mass is generated. This is not a tensor graviton-mass calculation.

## 7. Scope and axiom conflicts

- This is a scalar propagator proxy. It contains no helicity-2 projector, gauge constraint, polarization transport, nonlinear self-coupling, or tensor-noise calculation. `E1p_report.md:217-221`.
- E1's realization-wise strain “crackle” is unaddressed. Changing a metric can change which pairs are links discontinuously, just as it changed the BD order; E1-prime holds the causal order/metric fixed while studying propagation. `E1_referee.md:30-31`.
- (G_0=aL) is source-driven and nonrecursive. Its good noise behavior does not establish stable initial-value evolution. The prior BD code really did evolve the field recursively (`bd_core.py:291-305`); E1-prime does not supply an analogous massless evolution law. The (k=2) relay is not a substitute for arbitrary long evolution.
- The fixed test explicitly replaces the (\mathbb Z^3) Lattice substrate and supplies a causal order despite records carrying no time and the one-record-per-site/permanence rule. `TESTS.md:299-315`; `E1p_report.md:7-10`. Unbounded causal-set link valency also does not realize a fixed finite-neighborhood admissibility rule.

## 8. Strongest correct statement

For the stipulated Poisson sprinkling and scalar, source-driven Johnston kernel, the normalisation is correct; the ensemble law is shape-blind; (E[aL]) converges to the massless retarded light-cone kernel with (O(\ell^2/r^2)) corrections; (E[L^2]\to3\pi); and the tested massless link count has near-Poisson noise with no dependence on the past outside the source-to-observer intervals. At Planck density the direct scalar BNS estimate has an enormous nominal margin, but the required uniform large-(s/\ell) Fano asymptotic and scalar-to-tensor bridge are not established, so the fixed gravity verdict is INCONCLUSIVE. In the massive sector, individual-event kernels have a density-independent two-link floor and compact event reads have the stated leading endpoint seed, while the finite-density mean has a genuine slow growing complex pole; nevertheless wavepacket-plus-detector coherence over a laboratory kilometre, including repeated regeneration along the trip, has not been calculated. Therefore the correct fixed matter verdict is M-INCONCLUSIVE, not M-FAIL, and neither result changes the stated axiom conflicts or establishes a viable gravitational dynamics.
