# Assumptions And Imports

Current-source dependencies:

- `graph_first_su3_integration_note`: retained Wilson SU(3) gauge surface.
- `minimal_axioms_2026-04-11`: still conditional in the current audit surface.
- Production certificate: `outputs/alpha_s_direct_wilson_loop_certificate_2026-04-30.json`.

Open imports that remain load-bearing for any broad physical `alpha_s(M_Z)`
promotion:

- Sommer scale setting in physical units.
- Standard 4-loop QCD running and threshold matching.
- Transfer from pure-gauge measurement to full-QCD sea-quark context.
- Current axiom-surface normalization for the broad route.

This PR does not retire those imports. It prevents downstream rows from citing
the bounded-support certificate as if those imports had been retired.
