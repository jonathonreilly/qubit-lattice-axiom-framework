# Goal

Repair the new Lüders sequential-effect conditional row without adding an axiom
and without editing audit results.

The audit blocker was that the source packet assumed the Lüders update and the
trace/effect probability pairing. This block rewrites the source route so those
objects come from finite effect algebra plus retained repo authorities:

- finite POVM-additive probability consistency forces `m(E)=Tr(rho E)`;
- retained canonical projective measurement supplies `K_P=P`;
- retained finite Kraus selective-state algebra supplies the branch state;
- `K_P^* E K_P = PEP` and trace cyclicity give the two-step identity.
