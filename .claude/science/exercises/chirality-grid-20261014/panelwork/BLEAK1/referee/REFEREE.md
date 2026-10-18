# BLEAK-1 independent referee report

## VERDICT: CONFIRMED WITH CORRECTIONS

The scalar coefficient is correct for the action and infrared prescription actually implemented: linear scalar--spatial-TT coupling, R19-33's instantaneous quartic bridge, no two-graviton scalar seagull, and the spatial zero mode set to zero.  It is more precise to call this the order-\(G\) exchange/rainbow contribution than a prescription-independent physical one-loop speed.  The controls are mostly correct, but the worker overstates what K2 proves about seagulls and overstates the equivalence between deleting the tadpole and imposing the vacuum-source rule.

## 1. Scalar row, vertex, closed form, and normalization

Differentiating the displayed K2 bilinear stress gives, for \(m\ne n\),

\[
 U^\alpha_{mm}(k)=\left(\frac12-\delta_{m\alpha}\right)\sin k_\alpha,
 \qquad
 U^\alpha_{mn}(k)=-\frac12\left[\delta_{m\alpha}\hat k_n c_m+
 \delta_{n\alpha}\hat k_m c_n\right],
\]

where \(c_m=\cos(k_m/2)\).  This agrees with `scripts/b1_core.py:43-54`.  Since \(V(0,k)=0\), the \(O(p^2)\) self-energy uses only the product of these first derivatives.  D2's extra \(\hat p_{1,4}^2\hat p_{2,4}^2/4\) has zero first derivative, so K2 and D2 have the same dimension-four row.  An independent implementation gives an \(8.34\times10^{-14}\) finite-difference error, a \(2.22\times10^{-16}\) TT residual, and an \(8.88\times10^{-16}\) Ward residual (`independent_bleak1_check.out:1-7`).

The spatial block of every \(U^\alpha\) is a trace plus a spatial-longitudinal tensor, so the spatial-TT projection vanishes identically.  The row is entirely instantaneous.  After the exact \(k_4\) integral and cubic averaging,

\[
 d(q)=\frac1{16Q}+\frac{\tau}{32Q^2}-\frac16+\frac{QR}{6},\quad
 Q=\sum_i\hat q_i^2,\quad \tau=\sum_i\hat q_i^4,\quad
 R=[Q(Q+4)]^{-1/2}.
\]

Periodic integration by parts gives \(\langle\tau/Q^2\rangle=1-2W_3\), while four-dimensional hypercubic symmetry gives \(\langle QR\rangle=3/4\).  Hence

\[
 I_s-I_4=\frac{W_3}{16}+\frac{1-2W_3}{32}-\frac16+\frac18
 =\frac1{32}-\frac1{24}=-\frac1{96}.
\]

Thus Watson's constant cancels.  The independent chunked midpoint calculation extrapolates to \(-0.010416666693\), giving \(-16\pi(I_s-I_4)=0.523598776904\), versus \(\pi/6=0.523598775598\) (`independent_bleak1_check.out:9-19`).

The overall normalization also checks.  The static bridge has \(V(r)=-2\lambda M_1M_2/(4\pi r)\), so \(G_N=\lambda/(2\pi)\).  With \(\lambda=\kappa_R^2/4\), \(\kappa_R^2=8\pi G_N\); the canonical field convention is \(\kappa_{\rm can}=2\kappa_R\), hence \(\kappa_{\rm can}^2=32\pi G_N\).  The quartic action coefficient is \(-4\pi G_N\), and the exchange contraction has eight assignments, giving the worker's \(-32\pi G_N\) self-energy prefactor (`R19-33_scripts/r1933_cd_static_cov.py:31-34`; `independent_bleak1_check.out:21-25`).  Therefore

\[
 \delta c_{\rm exch}=\frac12(\delta Z_s-\delta Z_4)
 =\frac{\pi}{6}\frac{G_N}{a^2}
 =\frac{\pi}{6}\left(\frac{\ell_P}{a}\right)^2
\]

in the unreduced-Planck convention \(\ell_P^2=G_N\).

## 2. Controls, conservation, and seagulls

- **Covariant kernel:** confirmed exactly.  Its integrand and Brillouin-zone measure are related by the \(1\leftrightarrow4\) element of \(W(B_4)\), so \(I_s=I_4\) and the row is zero (`scripts/b1_checks.out:25-28`).
- **D2 correction:** confirmed at dimension four.  It begins at quadratic order in an external leg; the possible cubic cross term is forbidden by \(p\mapsto-p\), leaving its first contribution at \(O(p^4)\) (`scripts/b1_core.py:39-40`; `scripts/b1_finite_p.out:4-17`).
- **Spatial TT:** confirmed identically zero, not merely numerically small (`scripts/b1_semi.py:3-10`; `independent_bleak1_check.out:4-7`).
- **K2 through the foliated kernel:** confirmed for this exchange graph.  "Exactly conserved" means an off-shell Ward identity with equation-of-motion contact terms, not \(\hat k_\mu V_{\mu\nu}=0\) for an internal off-shell matter line.  Here \(\hat k_\mu U^\alpha_{\mu\nu}=-(\hat k^2/2)\delta_{\alpha\nu}c_\nu\), so longitudinal pieces cancel an internal propagator and leave an allowed UV-local, foliation-dependent term (`scripts/b1_checks.out:21-27`).  There is no conflict with the conserved-source identity, whose stated domain is conserved sources (`C5_R19-33_report.md:200-212`).
- **Seagull correction:** the worker's sentence that a seagull "would cancel it" is not proved.  A two-graviton--two-scalar vertex can change the \(O(p^2)\) row and could be chosen to cancel it, but K2's seagull blindness concerns the flat-background Killing commutator, not this self-energy coefficient (`C4_K2_report.md:107-123`; `C4_K2_referee_full.md:18-22`).  R19-33's displayed realization contains no such vertex, so omitting it is consistent with that defined model; it prevents promotion of \(\pi/6\) to a universal gauge-complete prediction.

## 3. Zero mode and tadpole

For the exchange integral, deleting the spatial \(q=0\) line is harmless in the infinite-volume limit: it has measure zero and the surviving \(1/Q\) behavior is locally integrable in three spatial dimensions.  The stable chunked extrapolation confirms that no hidden IR divergence controls \(-1/96\) (`scripts/b1_semi.out:11-28`; `independent_bleak1_check.out:14-19`).

The separate tadpole is different because translation invariance pins it exactly at zero momentum.  Setting \(D(q=0)=0\) removes it by definition, as preregistered (`PREREG.md:38-40`).  That is a legitimate finite-volume/neutral-background prescription inherited from R19-33, but it is not automatically equivalent to deriving the vacuum-source cancellation rule.  With another zero-mode prescription, or without an explicit cosmological/background counterterm cancelling \(\langle T_{\mu\nu}\rangle\), the tadpole can supply an additional \(O(p^2)\) term, and the foliated kernel need not make it isotropic.  The coefficient is therefore prescription-conditional, exactly as the worker's own scope caveat acknowledges (`REPORT.md:68-73`).

## 4. Fixed reading at the Planck spacing

The fixed BLEAK-1 bins are defined on the one-loop row (`TESTS.md:69-76`).  With \(\ell_P^2=G_N\), \(a=\ell_P\) gives the formal coefficient \(|\delta c_{\rm exch}|=\pi/6\simeq0.524\), far above \(10^{-6}\).  **LEAK-PLANCK therefore follows as the fixed exercise reading.**  It is not a controlled Planck-scale prediction: \(G_N/a^2=1\), higher loops are unsuppressed, and even the individual one-loop kinetic corrections are order unity (`REPORT.md:20`; `scripts/b1_finite_p.out:18`).

## 5. Fermion comparator

The stored sequence extrapolates consistently to about \(0.8497\), and a low-grid rerun reproduced its first two rows exactly (`scripts/b1_wilson.out:1-8`; `independent_wilson_rerun.out:1-3`).  This is only a diagnostic: the point-split Wilson stress is an explicit choice, no Ward-identity normalization or unique improvement is established, and R19-33 supplies no fermion RP bridge (`scripts/b1_wilson.py:1-11`).  It supports species dependence for the chosen vertices but is not a framework prediction.

## Strongest correct statement

For the precisely defined R19-33 scalar model with a linear spatial-TT coupling, the displayed instantaneous bridge, deleted spatial zero mode, and no seagull or speed counterterm, the order-\(G\) exchange graph has zero spatial-TT contribution and an exact bare anisotropy \(I_s-I_4=-1/96\), hence \(\delta c_{\rm exch}=(\pi/6)(\ell_P/a)^2\); K2 and D2 agree at \(O(p^2)\), while the covariant kernel gives zero by \(W(B_4)\).  The nonzero K2 result is legitimate because the internal line is off shell, but it is also the signal that the exchange graph alone is not a gauge-complete observable: an added seagull/contact completion or a different zero-mode/tadpole prescription can change the row.  Consequently LEAK-PLANCK is the correct fixed one-loop label, not a controlled prediction at \(a=\ell_P\); the Wilson value near \(0.85\) is only stress-choice-dependent supporting evidence.
