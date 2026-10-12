# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's final **OPEN** reading is correct. Lemma Q, the scalar runner,
and Lemma T' survive independent checks, and the two stated SM counts are
correct *conditional* counts under the worker's two counterterm conventions.
They do not satisfy the fixed `COUNTED` criterion because the class-wide
nonzero lemma, the required mass/IR uniformity, and the counterterm basis are
not closed.

## 1. Lemma Q

**Confirmed, with a quantifier correction.** A charge-\(q_i\) Peierls
one-photon vertex is proportional to \(q_i e\), while its seagull is
proportional to \(q_i^2e^2\), so the one-loop matter pole shift factors as
\(q_i^2F_s\). A one-loop vacuum-polarization graph contains no internal
photon; hence its loop contribution is independent of the photon mass
\(\lambda\) and of the photon kinetic symbol. The latter enters only through
the external soft-leg normalization, where \(d(q)=q+O(q^3)\). This confirms
the formulas in `R16-2_report.md:113-125`.

The statement that different charges can share one untuned matter value only
if \(F_s(0^+)=0\) is exact in the common massless limit. At distinct nonzero
masses, the bare equation is instead
\(q_i^2F_s(m_i)=q_j^2F_s(m_j)\); excluding such an accidental equality needs
the separate nonzero, Lipschitz, and mass-gap hypotheses in
`R16-2_report.md:227-230`. Lemma Q also does not by itself fix how correlated
matter counterterms are counted: a single coefficient multiplying a prescribed
\(q_i^2\)-weighted sum is a third convention not covered by the worker's two
readings.

## 2. Scalar runner: signs, J0, and the magnetic term

**Confirmed.** Expanding the Euclidean scalar action gives
\(\Pi=\langle S_2\rangle-\frac12\langle S_1S_1\rangle_c\), so the seagull is
positive in \(\Pi\) and both temporal and spatial exchange terms enter with a
minus sign, as coded in `scripts/r162_scalar.py:22-45`. The spatial Peierls
vertex is
\([u(p_j)-u(p_j-q_j)]/d(q_j)\), which reduces to \(2p_j-q_j\) in the
continuum box; its square is the `V2` term at
`scripts/r162_scalar.py:27-42`.

Independent real-axis \(q_0\) quadrature reproduces both closed integrals to
12 digits, including a case where \(J_0<0\)
(`r162_referee_checks.out:1-3`). Without using the worker's closed \(J_0,J_1\)
forms, the two full scalar checks decompose, in \(16\pi^2\) units, as

- \(G(1.0)\), naive photon: seagull \(-5.133456\), temporal \(+7.225894\),
  magnetic \(-5.196924\), total \(-3.104486\);
- \(G(1.4)\), photon \((1,2)\): seagull \(-4.498922\), temporal \(+6.871637\),
  magnetic \(-5.041395\), total \(-2.668680\).

The direct totals agree with the runner within \(6\times10^{-7}\), and the
imaginary residual is \(2\times10^{-19}\)
(`r162_referee_checks.out:4-6`). The heavy-limit magnetic/Coulomb cancellation
therefore has the stated factor and sign: the seagull's \(1/W\) combines with
the temporal recoil \(-d_x^2/W^3\) to leave
\((d_y^2+d_z^2+\lambda^2)/W^3\), matching
`scripts/r162_scalar.py:10-11,55-59` and the saved heavy checks
`scripts/r162_scalar_heavy.out:1-12`.

## 3. Lemma T'

**Confirmed under its stated monotone-photon hypothesis.** With
\(w=1/(d^2W)\), \(S(b)=b\), and \(S(\pi)=0\),

\[
\int_b^\pi(S'-1)w
=[(S-q)w]_b^\pi-\int_b^\pi(S-q)w'
=-\pi w(\pi)+\int_b^\pi(q-S)w'.
\]

Thus \(S\le q\) and \(w'\le0\) give the advertised strict negative bound.
The scalar boundary terms are identical after replacing \(S\) by \(u'/2\):
\(u'(b)/2=b\), \(u'(\pi)=0\). Evenness and the Brillouin-zone normalization
produce the factors \(-\frac12\langle w(\pi)\rangle_\perp\) and
\(-\frac14\langle w(\pi)\rangle_\perp\), respectively
(`R16-2_report.md:135-141`).

For a Wilson edge, the external momentum remains in the box, so
\(W(p)=0\) and \(2E_p a_\beta=2m\); every beta-tadpole contribution to
\(2E_p\delta E\), including its \(p^2\) derivative, is therefore \(O(m)\) for
a fixed smooth \(W\). The radius argument is also sound: at \(m=0\),
\(r(k)=\sqrt{s(k)^2+W(k)^2}\), \(r(b)=b\), and \(|r'|\le1\) imply
\(r(k)\le b+(k-b)=k\), hence \(|s(k)|\le r(k)\le k\). The phrase "at small
mass" should mean a bound uniform down to the massless limit; one isolated
finite-mass velocity check would not suffice. Lemma T' does not bound the
exchange remainder, and it does not apply to the report's nonmonotone photon
symbols (`R16-2_report.md:143-152`).

## 4. Lemma F numerics and proof attempt

**The sampled signs are confirmed; the \(F_s(0^+)\) and class-wide wording is
not.** Three independent Dirac spot checks—D1, the smallest-margin steep
literal case, and the \((0.5,1.5)\) literal edge—give on-shell values
\(-10.0791,-4.5331,-11.9425\); the independent off-shell \(B-A\) route gives
\(-10.2211,-4.5835,-12.0353\), respectively
(`r162_referee_checks.out:7-10`). The two independent scalar checks above
also confirm the sign and normalization. The saved tables support the
worker's finite-grid ranges for its enumerated 67 Dirac and 23 scalar
law-photon combinations (`R16-2_report.md:199-207`).

Corrections:

- Those numbers are values at \(m=0.05,0.1,0.2\), finite
  \(\lambda=0.01\text{--}0.05\), and finite \(N\), not controlled values of
  \(F_s(0^+)\). The report itself records comparable \(N\)- and
  \(\lambda\)-drift and calls uniformity only suggested
  (`R16-2_report.md:191-197,311-312`).
- The interval \([-11.9,-4.5]\) describes the enumerated 67 combinations, not
  every sampled member of the stated class: the added in-class dip-and-rise
  family reaches \(-16.10\) (`scripts/r162_dip_rise.out:7-11`).
- The overshoot zero is a valid checked finite-\(m\) witness outside the class,
  and its axis speed is indeed about 4.35, but the run locates
  \(F_{1/2}(m=0.1)=0\), not a rigorously extrapolated \(F_{1/2}(0^+)=0\)
  (`scripts/r162_overshoot_root.out:1-2`).
- "No IR log" is numerical non-observation, not a proved result.

I attempted the proposed proof reduction. Lemma T' controls only the negative
tadpole/seagull. The direct scalar decomposition shows why a termwise proof
does not follow: the temporal remainder is large and positive while the
magnetic remainder is large and negative (`r162_referee_checks.out:4-6`).
No inequality in the stated class bounds their sum by the T' margin; the class
also retains nonmonotone photons and uncomputed Wilson shapes. Thus the exact
remaining obligation is the worker's inequality at
`R16-2_report.md:211-213`; it is target-equivalent to Lemma F, and no proof is
within reach without materially stronger hypotheses.

## 5. Proposition C, the two counterterm readings, and residuals

**The SM Dirac-only combinatorics are correct conditional on (F), (L), and
(E).** With independent per-species additive counterterms, one may leave the
largest same-charge class untuned, use one photon-side matching condition, and
tune every other species. The count is
\(N_s-n_{\max}+1=9-3+1=7\). With one additive counterterm per
\((s,|q|)\) class, two class counterterms plus one photon-side condition give
three, or equivalently all three matter-class counterterms give three. The
lower bound follows from the charge gap once (F), (L), and (E) are assumed
(`R16-2_report.md:223-241`).

Three corrections are required.

1. **A photon counterterm is not required.** In the worker's realization
   that leaves one charge class untuned, the extra tuning is a photon-side
   matching condition, not specifically a photon counterterm. Under the class
   reading, all three matter classes can instead be counterterm-tuned with
   \(\kappa_\gamma=0\), still at total cost three. Also, in the worker's own
   literal family a shape value near \(b_2=2.31\) satisfies \(8G=F\) for the
   lepton class at the checked parameters, so a shape equation replaces
   \(\kappa_\gamma\) (`r162_referee_checks.out:11-13`). The report proves no
   such replacement only on the tested D1 rows
   (`R16-2_report.md:236-237`).
2. The numerical residuals \(1.7\times10^{-22}\) and
   \(7.3\times10^{-21}\) are arithmetically correct
   (`r162_referee_checks.out:14`), but they are conditional estimates, not
   established class-wide upper bounds: \(L\le2\) was resolved only for two
   D1 laws (`scripts/r162_slope.out:1-8`) and no uniform physical
   \(\lambda\to0\) bound was proved.
3. The formulas are not counterterm-convention-independent. A prescribed
   charge-weighted common coefficient, \(\kappa_i=q_i^2\kappa_s\), would be a
   different one-parameter reading and changes the count. For multiple spin
   sectors, the displayed sum over spins additionally needs the assumed
   cross-spin shape equalities or separate matching conditions. Finally, the
   literal edge's seven light corner valleys are not included even though the
   fixed setting names that edge; the report acknowledges this omission at
   `R16-2_report.md:258-261`, and the prior fixed result excludes that literal
   realization at `TESTS.md:3839-3840`.

## 6. Fixed reading and no-go stress test

**`COUNTED` is not met; `OPEN` is confirmed.** The fixed criterion requires a
proof that \(n_t\) suffices for every species in a stated class and that
\(n_t-1\) cannot (`TESTS.md:5080-5082`). Here that lower bound still assumes
the unproved class-wide Lemma F, the unproved uniform Lipschitz/IR control, a
chosen counterterm basis, and omission of literal-edge corner species
(`R16-2_report.md:275-283`).

The negative conclusion was stress-tested against distinct routes: a shape
zero (realized by the superluminal overshoot family), photon-side shape
matching (realized in the literal family), all-matter rather than photon
counterterms, a charge-weighted correlated matter counterterm, finite-mass
charge compensation, and cross-spin alignment. These routes either lie
outside the narrow conditional theorem or change its counterterm convention;
they prevent upgrading the conditional count into a universal no-go. They do
not invalidate the narrow 7/3 arithmetic under the worker's stated readings.

## 7. Strongest correct statement

At fixed positive photon-mass regulator and at one loop in the stated
Peierls-coupled \(\mathbb Z^3\times\mathbb R\) models, the matter speed shift
factorizes as \(q_i^2F_s\), while the photon-loop shift is a single sum
\(\sum_jn_jq_j^2G_{s_j}\) independent of the internal photon symbol and
\(\lambda\); the scalar on-shell runner, including \(J_0\), the seagull sign,
and the spatial/magnetic exchange term, is correct, and Lemma T' proves a
strictly negative tadpole/seagull bound for non-rising matter symbols with a
nondecreasing photon symbol. Every enumerated D1/literal/G law remains
negative at the sampled finite masses, so, **conditional** on a class-wide
nonzero \(F_s\), a uniform mass bound, and the chosen additive-counterterm
convention, the nine SM charged Dirac flavours require seven tunings with
independent species counterterms or three with one counterterm per charge
class, with the quoted tiny residual estimates. Neither \(F_s(0^+)\ne0\)
throughout the stated class nor the physical \(\lambda\to0\) bound is proved;
\(\kappa_\gamma\) is replaceable by another photon-side condition, literal
corner species are omitted, and the tuning count changes under other
correlated-counterterm conventions. Therefore the strongest fixed reading
is **OPEN**, not `COUNTED`.
