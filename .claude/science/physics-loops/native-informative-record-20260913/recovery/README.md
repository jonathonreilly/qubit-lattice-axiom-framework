# Original author findings and mutation diagnostics

INITIAL_DERIVATION.md predates the measurable-factor qualification found
in the cold author review. The final source explicitly treats finite/countable
families and adds a measurable-factor requirement for uncountable families.

FIRST_PRIMARY.py and first_mutation_attempt preserve the exact first thirteen
altered-source runs. Twelve were assertion-rejected. Replacing the incident
Hamiltonian by the entire protected Hamiltonian reached SymPy eigenvalue
ordering before the energy-support assertion and raised a TypeError. That
run was not counted as an intended rejection. The final primary moves the
existing exact incident-energy identity before the fixture that uses it;
the same mutation then meets that scientific assertion first. No physical
formula, probability target, numerical tolerance or positivity threshold was
changed. All thirteen final mutants are rerun against the final primary.
