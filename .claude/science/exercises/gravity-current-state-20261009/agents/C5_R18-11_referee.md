# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's **OPEN** reading is correct. The gauge-density identity, the
zero-start conservation lemma, the displayed \(a=2\) scalar/vector
coefficients, and the numerical conversions survive independent checking.
The offered “NOISE-OVERSHOOT candidate” does **not** meet the fixed
NOISE-OVERSHOOT reading, because its two routes do not furnish one completed
flat-space law over the entire registered window: (U) is not a globally
closable Minkowski/zero-start solution, while (P) lacks the required
modewise \(q\leq0\) bound in the strict spectrum (and the bounded near-cone
interpolation is not specified even in the inherited R15-2 construction).

1. **Theorem G: confirmed, with scope qualifications.** For a symmetric
   contravariant tensor density of weight \(w\),

   \[
   (\mathcal L_\xi\mathfrak J)^{\mu\nu}
   =\xi^\lambda\partial_\lambda\mathfrak J^{\mu\nu}
   -\mathfrak J^{\lambda\nu}\partial_\lambda\xi^\mu
   -\mathfrak J^{\mu\lambda}\partial_\lambda\xi^\nu
   +w(\partial\!\cdot\!\xi)\mathfrak J^{\mu\nu}.
   \]

   Averaging the first term by parts and the next two using
   \(\partial_\lambda\mathfrak J^{\lambda\nu}=0\) gives exactly
   \(\langle\mathcal L_\xi\mathfrak J^{\mu\nu}\rangle
   =(w-1)\langle(\partial\!\cdot\!\xi)\mathfrak J^{\mu\nu}\rangle\).
   Thus \(w=1\), equivalently \(a=4-2w=2\), is sufficient for independence of
   the averaged \(O(G\,\mathrm{noise}^2)\) source under every allowed readout
   transformation, and a generic time-dependent scalar mode proves necessity
   inside the \(C_w\) power family. The independent exact-metric calculation
   gives
   \(\Delta\tau_{00}/u_1=2x^2(a-2)\) and
   \(\Delta\tau_{kk}/u_1=2x^4(a-2)\), hence
   \(\Delta\rho_{\rm act}/u_1=-4x^2(w-1)(1+x^2)\), matching the worker.
   An individual static mode \(x=0\) does not select \(w=1\), and the uniqueness
   claim is only for the stated insertion families and the coarse-grained mean,
   not arbitrary derivative/nonlinear insertions or fluctuation-level gauge
   independence. R18-11_report.md:134-148;
   r1811_insertions.out:1-18; r1811_referee_checks.out:1-10.

2. **Lemma P: confirmed; (U) is not a second Minkowski zero-start solution.**
   Linearized Bianchi forces \(\partial^\mu\tau_{\mu\nu}=0\). Homogeneity then
   gives \(\partial_t\langle\tau_{00}\rangle=0\), and zero noise plus zero
   homogeneous data at \(t_0\) gives \(\langle\tau_{00}\rangle=0\). The
   explicit projector removes the time-dependent homogeneous energy and adds
   no homogeneous pressure, so the valid zero-start reading is
   (P), \(\rho_{\rm act}=\tau_{kk}\). Reading (U),
   \(\rho_{\rm act}=\tau_{00}+\tau_{kk}\), requires preloaded homogeneous
   energy and a different background/local posing: \(G^{(1)}_{00}=0\) has no
   homogeneous Minkowski constraint capable of supporting it. Moreover a
   constant conserved homogeneous pressure remains a completion datum and can
   shift \(\rho_{\rm act}\); setting it to zero is part of the canonical
   projector choice, not a consequence of Bianchi. R18-11_report.md:150-160;
   R18-11_report.md:226-229; r1811_pin.out:1-10.

3. **Active-density coefficients at \(a=2\): confirmed in the stated S/V
   scope.** An independent computation that exact-inverts the metric before
   expanding gives, for the \(\rho\) channel,
   \(\tau_{00}/u_1=x^2-3\),
   \(\tau_{kk}/u_1=-(1+x^2)\), and their (U) sum \(-4\), for every \(x\).
   The worker's channel table then makes the \(T_\perp\) terms cancel in (U)
   (\(-2q+2q=0\)) and the V terms cancel (\(u_V-u_V=0\)), so
   \(\rho_{\rm act}^{(U)}=-4u_1\). Under (P),

   \[
   \rho_{\rm act}^{(P)}=-(1+\langle x^2\rangle)u_1
      +2\langle q\rangle u_1-u_V,
   \]

   hence the claimed negative bound follows only when \(q\leq0\) modewise and
   \(u_V\geq0\). TT is excluded from this exact cancellation. The inherited
   least-decoherence relation is only fixed in the quasi-static sector and is
   explicitly interpolated near the cone; it does not supply that sign over
   the strict spectrum. R18-11_report.md:162-187;
   C5_R15-2_report.md:123-127; r1811_referee_checks.py:74-169;
   r1811_referee_checks.out:1-8.

4. **Budget and Mercury: arithmetic confirmed, interpretation conditional.**
   Using the confirmed
   \(u_1=\hbar(21/32)/(32\pi^{3/2}\ell^3\tau)\) and the worker's cosmological
   constants gives \(u_1/\rho_\Lambda=1.170953060\) at
   \((\ell,c\tau)=(5\times10^{-6},1.49\times10^{-3})\,\mathrm m\), and therefore
   the (U) minimum is \(4.683812238\). These are the two **corner minima**, not
   the full range; the ratios rise to \(10^{12}\)–\(10^{19}\) toward the lower
   endpoint. The exact strict W1 moment is
   \(\langle x^2\rangle=34/21\). With the inherited Mercury limit
   \(9.286\times10^{-15}\,\mathrm{kg\,m^{-3}}\), the conditional crossings are
   (P) \(2.459\times10^{-8}\,\mathrm m\) strict and
   \(4.541\times10^{-10}\,\mathrm m\) at the ceiling, and (U)
   \(2.733\times10^{-8}\,\mathrm m\) and \(7.208\times10^{-10}\,\mathrm m\).
   The source is negative/repulsive under the displayed flat (P)/(U)
   assumptions. The P bounds inherit \(q\leq0\) and zero homogeneous-pressure
   assumptions; the U bounds inherit its non-Minkowski/preloaded-energy price.
   C5_R15-2_report.md:226-245; C5_R16-14_referee_verdict.md:7-11;
   R18-11_report.md:196-215; r1811_referee_checks.out:11-19.

5. **Fixed NOISE-OVERSHOOT: not met.** A singleton class is not formally
   disqualified by the universal quantifier: if one separately defines the
   narrower class “\(a=2\), flat zero-start (P), canonical zero-pressure
   projector, \(q\leq0\) for every supported mode, \(u_V\geq0\)”, the algebra
   proves an overshoot with minimum factor \(1.17095\). But that is not the
   offered full-window E1 class. The report itself concedes that the strict
   least-decoherence spectrum has \(q>0\) off cone and no (P) bound there, while
   (U) cannot close globally on Minkowski; those alternatives cannot be spliced
   to prove one class-wide theorem. The suggested FRW attractor is outside the
   fixed probe and so proves neither NOISE-SAFE nor failure of a properly scoped
   flat theorem, but it demonstrates why no stronger set-A wall is available:
   its rho-only corner has
   \(|\rho_{\rm act}|/\rho_\Lambda=0.78064\) and crosses unity at
   \(\ell\simeq4.60\times10^{-6}\,\mathrm m\). The 17% flat-P margin is
   arithmetically real but cannot replace the missing spectral/completion
   bound. TESTS.md:6938-6942; R18-11_report.md:36-47;
   R18-11_report.md:258-272; r1811_referee_checks.out:20-22.

6. **Runner correction (non-load-bearing at this order).** The inverse-metric
   line should contain \(\eta h\eta h\eta\), i.e. hu*h*eta, rather than
   hu*eta*h*eta. The erroneous \(O(\epsilon^2)\) inverse term can first enter
   a Christoffel symbol or scalar-curvature contraction at
   \(O(\epsilon^3)\), so it does not alter the reported \(O(G^2)\) output; the
   exact-inverse independent computation confirms the coefficients. The code
   should nevertheless be corrected before reuse at higher order.
   r1811_modes.py:49-85; r1811_modes_lib.py:53;
   r1811_referee_checks.py:74-154.

**Strongest correct statement:** Within the contravariant power-density insertion family \(C_w\), for the coarse-grained \(O(G\,\mathrm{noise}^2)\) mean of the stated E1 + canonical-Π construction, readout-gauge independence selects \(w=1\), hence \(a=2\) and the record \(\sqrt{-g}\,T^{\mu\nu}\); the independently checked rho channel gives \(\tau_{00}/u_1=x^2-3\) and \(\tau_{kk}/u_1=-(1+x^2)\), so a preloaded stationary S/V configuration has \(-4u_1\), while the actual flat zero-start solution has \(\rho_{\rm act}=-(1+\langle x^2\rangle)u_1+2\langle q\rangle u_1-u_V\), which exceeds \(\rho_\Lambda\) throughout the registered window only under the additional modewise \(q\leq0\), \(u_V\geq0\), and zero homogeneous-pressure conditions; its corner ratio is 1.17095 and the corresponding conditional P Mercury crossings are \(2.46\times10^{-8}\,\mathrm m\) (strict) and \(4.54\times10^{-10}\,\mathrm m\) (ceiling). Because the inherited strict spectrum does not establish \(q\leq0\), (U) is not a closed Minkowski zero-start solution, and the FRW completion remains merely suggested and has a sub-\(\rho_\Lambda\) corner, neither fixed NOISE-SAFE nor fixed NOISE-OVERSHOOT is established: the strongest reading is **OPEN**.
