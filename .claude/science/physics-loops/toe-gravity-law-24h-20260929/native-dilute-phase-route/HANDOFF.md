# Focused-check handoff

Actual status: conditional-support, author theorem candidate for the
explicitly supplied model. No independent receipt for these new lemmas,
formal audit, source integration, PR, commit or authority-file mutation.

The new result is on the complete M2 occupation carrier, every L>=5,
mu,tau>0 and every particle sector. It does not use the provisional N4
threshold theorem as a premise. With a=min(tau,mu/12):

- A literal residual-site projector pins a bare pair after a two-step
  center translation, giving V3<=24mu Egrad on arbitrary coherent states.
- If O counts particles outside isolated physical G-dimers, graph counting
  and the actual SOS give H0>=(a/72)O. Odd sectors have absolute energy
  >=a/72; the even-sector non-isolated compression has lower bound a/36.
- Every H0-nu N ground state has <O>/<N><=72nu/a. Its actual normalized
  pair correlation is >=rho[1/2-nu/(2mu)-nu|r|^2/(2tau)]. This controls a
  growing finite distance, not fixed-density infinite-distance order.
- A post-contract deduction also bounds averaged distant single-particle
  coherence by (1+sqrt(18))sqrt(rho<O>/V), hence by O(rho sqrt(nu/a))
  in those ground states. The mechanism is a real defect left behind when
  one endpoint of an isolated dimer moves beyond G+G.
- The full pair Gram is retained. Fixed-mode commutator errors are <=324rho
  in expectation; they do not give a uniform Fock-space replacement.

`REPORT.md` contains complete proofs, parameter/volume conditions, the
large-mode-weight consequence, and the narrow sign-gauge counterexample.
`APPROACH_REGISTRY.md` records the distinct formulations and the strength
of each terminal gap. `SOURCE_BINDINGS.json` binds current main30a, selected
procedure7146, actual axioms/primitives and the full threshold/positive
reports. All nine procedure/primitive files match the selected SHA.

Final exact local run: 1,224 full sparse SOS identities, 33,867 abstract
graphs, 32,110 distant-move support cases, three literal commutator classes,
and the rational four-cycle invariant. At most six local sites/64 states;
1.569 wall seconds, 1.565 CPU seconds, 18,399,232-byte peak RSS; threads1.
Python AST and trailing-whitespace checks passed. No dense many-body job.
The first local run preceded the extra single-particle deduction; the
second reran the same controls with its new graph support check. Earlier
author sources remained unchanged.

Requested independent check: reconstruct the pin with n_z in the correct
operator order; count all translated paths, including the axial double
selection and L=5 geometry; check O's diagonal graph bound; reconstruct
the shared-center T/sqrt(2) normalization; verify pair/single correlation
Cauchy estimates and the finite-mode CCR count. Check the thermodynamic
order of limits and that none is an assertion of condensate or tensor mode.

The next scientific obstruction is now precise. An absolute all-N closed
compression gap does not give a resolvent relative to the extensive
finite-density ground energy. A many-pair embedding/elimination theorem
needs a uniform linked error o(rho^2 V), and a spinor variational argument
must determine whether a coherent polarization is the correct leading
state. Simply restating the desired energy limit or extensive pair-density
matrix eigenvalue is target-equivalent. No broad phase impossibility or
campaign stop is inferred.
