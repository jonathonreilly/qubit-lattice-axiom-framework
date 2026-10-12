# C3 lane M-C: referee verdict (codex gpt-5.6-sol, xhigh; other vendor; 2026-10-10)

# VERDICT: CONFIRMED WITH CORRECTIONS

The preregistered decision table formally returns **FAIL**, but the defensible no-go is substantially narrower than the worker’s headline.

## Findings

1. **C0 is confirmed for the exact Klein–Gordon mean.**  
   C0 makes every realized impulse-response kernel nonnegative, so its expectation is a nonnegative measure (`work/PREREG.md:20-21`; `C3_M-C_report.md:61-67`). The 3+1 retarded KG kernel instead has interior tail
   \[
   -\frac{mJ_1(m\tau)}{4\pi\tau}
   =-\frac{m^2}{8\pi}+O(\tau^2),
   \]
   immediately inside the cone (`C3_M-C_report.md:54-57`). Equality is therefore impossible.

   The result is dimension-independent, but not because the tail is negative immediately inside the cone in every dimension—that is false in 1+1 and 2+1. The correct general proof is the spatial zero mode:
   \[
   f(t)=\int d^dx\,G_R(t,x),\qquad f''+m^2f=0,\quad
   f(0)=0,\ f'(0)=1,
   \]
   hence \(f(t)=\sin(mt)/m\), which becomes negative (`work/scripts/mc1_lemmas.py:3-11`; `C3_M-C_report.md:63-69`).

   Hypothesis audit:

   - H1 supplies a linear impulse-response kernel, but linearity alone is insufficient; the decisive assumption is C0 positivity.
   - H2 makes the kernel translation-invariant but is not needed for the local negative-tail contradiction.
   - H3—equality to the **exact** KG retarded kernel—is essential. A nonnegative kernel may contain a massive pole atop an additional nonoscillating carrier, as the report itself acknowledges (`C3_M-C_report.md:71-73`).

2. **Lemma D is correct only for Fourier-mode descent.**  
   For the prescribed \(e^{imw}\) readout, the Volterra kernel and transform are correct:
   \[
   \widehat k(s)=\sqrt{\pi/s}\,e^{-m^2/(4s)},\qquad
   \widehat f(s)=\frac{\sqrt s}{2\pi^{3/2}}.
   \]
   This cannot be the Laplace transform of a nonnegative measure, so a nonnegative 4+1 parent cannot yield the exact 3+1 KG kernel through that Fourier-mode projection (`C3_M-C_report.md:92-107`; `work/scripts/mc1_lemmas.py:39-60`).

   The broader conclusions “positive-hop descent … never in 3+1” and “the only alternative is a phase register” are false (`C3_M-C_report.md:108-109`). The checker’s counterexample is exact:
   \[
   P(T,w)=\delta(T-w^2),\quad
   g(w)=\frac{\delta(w)}{2\pi}-\frac{m}{4\pi}J_1(m|w|),
   \]
   for which
   \[
   \int dw\,g(w)P(T,w)
   =\frac{\delta(T)}{2\pi}
    -\frac{mJ_1(m\sqrt T)}{4\pi\sqrt T}.
   \]
   Thus a nonnegative, 4+1-invariant cone parent plus a **signed, non-Fourier readout** gives the exact 3+1 massive kernel (`work/verify/v1_nonfourier_descent.py:1-25`; `C3_M-C_report.md:290-296`). My rerun reproduced its Laplace-transform agreement.

   This does not produce mass without signs: the entire KG tail and \(m\)-dependence have simply been installed in the signed readout. It confirms Lemma B’s representational point, not Lemma D’s broad no-go. Lemma B is valid but essentially definitional (`C3_M-C_report.md:80-88`).

3. **The block-122 analogy must remain scoped.**  
   Block 122 concerns finite-memory, finite-component, finite-support, row-stochastic linear recursions with entrywise nonnegative coefficients. It proves that a locally unimodular branch in each recurrent irreducible class has affine phase—rigid transport—not that all waves or all mass mechanisms are impossible. It expressly leaves nonlinear rules, infinite memory, probability laws, continuous-time parents, decaying dispersive branches, and multiple transport velocities outside scope (`../skillwt/docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_A_FORMATION_RULE_WITH_NONNEGATIVE_WEIGHTS_KEEPS_AN_UNDAMPED_BRANCH_ONLY_BY_RIGID_TRANSPORT_AND_THE_AMPLITUDE_STEP_IS_A_SIGNED_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md:4-10,30,42-52`). It is also marked unaudited (`ibid.:21-24`).

   C0 is complementary: it needs neither finite memory nor stochastic normalization, but targets the exact source-to-readout KG Green function. Neither result justifies the unqualified slogan “massive matter needs signed weights.”

4. **Verdict under the fixed PREREG: formal FAIL survives.**  
   The preregistration explicitly fixes the descent test to a Fourier mode (`work/PREREG.md:43-46`) and makes C1-PASS require a construction “not a relabelling of a signed rule” (`work/PREREG.md:69-71`). Since C1 itself permits the sign in the state, background, extra-coordinate profile, or readout (`work/PREREG.md:22-25`), Lemma B makes that PASS branch unreachable by definition. With Fourier-mode Lemma D valid, the preregistered labels are therefore Q1=C0-FAIL, Q2=C1-FAIL, hence overall FAIL (`work/PREREG.md:64-75`).

   This is a taxonomy-driven FAIL, not a theorem that C1 cannot have a massive mean. If Q2(ii)’s wording “descent from any … kernel” (`work/PREREG.md:65-68`) were read literally without the earlier Fourier restriction, the counterexample would falsify it and force Q2—and therefore the overall result—to INCONCLUSIVE.

## Strongest correct statement

> No positivity-preserving linear source-to-readout rule—one whose realized impulse-response kernel has only nonnegative source, propagation/regeneration, and readout weights—can have the exact massive retarded Klein–Gordon Green function as its ensemble mean. This holds in every dimension. Isolating that KG response therefore requires a signed or complex contribution somewhere in the effective linear map. Moving it into the state, background, auxiliary-coordinate profile, or readout does not remove the sign or change the resulting random variable. This does not exclude positive massive transport, a massive pole accompanied by a positive carrier, nonlinear observables, or other notions of massive matter.