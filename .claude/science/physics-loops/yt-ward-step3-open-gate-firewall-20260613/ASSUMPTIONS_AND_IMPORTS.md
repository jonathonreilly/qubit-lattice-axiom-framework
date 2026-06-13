# Assumptions And Imports

Current retained/support inputs:

- Unit-singlet overlap form.
- Rep-B independence surface.
- D12 color-singlet Fierz coefficient.
- Bare Wilson plus staggered-Dirac OGE context.

Open import:

- A Wick-level proof that the OGE contraction and `H_unit` decomposition are
  the same projected amputated 1PI Green's function.

This PR does not supply that bridge. It prevents downstream consumers from
treating the gate equation as if the bridge had been supplied.
