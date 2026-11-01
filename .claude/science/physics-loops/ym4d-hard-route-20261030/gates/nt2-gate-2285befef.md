lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T04:29Z

# Gate: NT2 (queue item 8e) at 2285befef

**Provenance.** Reviewer anthropic/claude-opus-5-5, effort high, Mac mini worker, commit 2285befef, neutral side. Text under review written by openai/gpt-6-astra/max. A check by one model is not an audit, and it grants no status. Scripts and criteria: `checks/gate_nt2/`.

Report in progress. Sections follow as they are finished.

## Interim findings (hand checks, before numerics)

- Normalizations of (NT2-C), (NT2-g), (NT2-R) check by hand, including b_W = 11/(3 pi^2) against both producers' statements.
- Library B (transport), C (L1, L2), D (mixture), section 3 of the moment gap (formula (6)) check by hand so far.
- Under test: the clause |K_vert(tau_*)| >= kappa_* looks chart-dependent, by the part's own Proposition 2.2.
- Under test: L1 appears to reject only a non-coherent family, since its excess is irrelevant under blocking.
- Under test: the consistency equation in L3 appears not to be the real obstruction; RP appears to be.
