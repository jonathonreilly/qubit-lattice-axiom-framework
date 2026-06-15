# Goal

Target the audited conditional row
`signed_gravity_aps_locked_source_action_proposal_note`.

The audit blocker asks for a derivation of the APS-locked
`chi_eta M_phys <rho,Phi>` source action. This block does not derive it. It
wires the executable APS/Wald/Gauss bridge audit into the row source packet so
audit can consume the current result cleanly: retained APS/Wald/Gauss does not
derive the locked source term, and the local proposal passes only after that
term is inserted.
