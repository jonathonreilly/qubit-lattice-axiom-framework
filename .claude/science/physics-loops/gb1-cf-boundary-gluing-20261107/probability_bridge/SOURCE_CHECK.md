# SOURCE-EXPOSED comparison of the integrated proof

This is a source-exposed comparison after the independent hand proof, not a fresh
independent derivation or an audit. The earlier `INDEPENDENT.md` and `CHECKPOINT.md`
are preserved byte-for-byte. No governing source, scientific status, or prior
checker artifact was edited. No numeric job was run.

## Exact reviewed sources

Read completely from `/Users/jonreilly/.codex/worktrees/gb1-cf-pair/Physics`:

- `probability_bridge/RESULT.md`, SHA-256
  `70dd5037ba567a9d2547f297944de55be022b229cc7e868496542c2090d2a30f`.
- `probability_bridge/ASSUMPTIONS.md`, SHA-256
  `6e445f7facaca490b30eaca96736e4f36185ce66ed58a360a7cd9e4c10af6c07`.

The two relative paths above are under
`.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/`.
Governing axioms remain at main `bf92a1d763030836ed55631d5d7a7ef3b288f284`,
`docs/MINIMAL_AXIOMS_2026-06-29.md`, SHA-256
`301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc`.
That file was read completely in the independent check; its hash was refreshed
and matched during this comparison.

Preserved checker identities:

- `INDEPENDENT.md`: `cf73c8a3aa2a7e6ec36bba981e22a0969025b77b893dce28e77a1458059caef3`.
- `CHECKPOINT.md`: `73fbc5d86ed7558ba518e13be6fdb1a4d7fa487fb88f8787d31a92a497b0ccf4`.

## Required scope clarification

Section 6 attributes the event additivity used in the effect theorem to
“Admissibility's ordinary event-set additivity.” This is justified directly for
Borel events of a single forming record's local probability law. For device
contexts involving several records, the one-site marginals alone do not supply
a joint event law. E1–E3 do not construct that law.

Make explicit an E0 premise: for the fixed preparation data `r` under discussion,
each admitted device context has a normalized probability measure on its record
events. One-site contexts may use the supplied local law; multi-record contexts
need a separately supplied or derived joint process/law. E1 and the universal
E3 must hold among contexts available with that same preparation. Ordinary
additivity then applies within each context, and E2 identifies values across
contexts. No joint probability space spanning mutually different device contexts
is needed or inferred. Update the assumption ledger consistently.

This is a scope/provenance correction to the physical bridge, not a counterexample
to the finite effect theorem once its probabilities have this ordinary meaning.
The section 1 warning about joint history laws is correct but should also be
carried into the explicit conditional hypotheses where it is used.

## Mathematical checks and boundaries

- The universal E3 now covers every summable positive pair, including repeated
  effect labels as distinct exclusive events. Its binary-only alternative
  correctly witnesses why merely existing groupings do not suffice.
- The monotone homogeneous extension to positive matrices, Hermitian trace
  duality, positivity, normalization, and uniqueness are correct. The rank-one
  certainty corollary correctly forces `rho=P`; literal record content `P`
  does not establish that certainty.
- Sharp calibration is distinguished from genuine instrument repeatability.
  Both nonlinear coarse-graining witnesses are exact: `1/5` differs from `1/2`.
- Total extension of the local kernel by counting all present neighbors and
  exact identity contents is valid. It does not enlarge the witness's legal
  record domain or make initially arbitrary matrix records admissible.
- The finite-ancestry bound `(6t)^m/m!` is valid: conditional on a root clock
  `s<=t`, the earlier independent exponential clocks have density at most one
  on an ordered simplex of volume `s^m/m!`. Countable roots and integer time
  bounds yield the simultaneous infinite construction. Fresh marks and
  exponential memorylessness justify the claimed record-only Markov process.
- Complex-linear tracial uniqueness is correct and is explicitly distinguished
  from real-linear uniqueness. In section 2, “algebra isomorphisms” should be
  read as **complex-algebra isomorphisms**, consistent with the stated domain.
  Spelling out that adjective would remove residual ambiguity: conjugation is
  a real-algebra automorphism and sends `tau(iI)=i` to `tau(-iI)=-i`.
  The real-algebra version has the corresponding covariance of the central
  trace, not invariance of a fixed complex scalar value under conjugation.
- The content-measure classification, stabilizer-versus-full-group distinction,
  positivity domain, and legal-domain limitation agree with the governing
  source and the independent proofs. No additional mathematical defect found.

## Disposition and verification limits

The reviewed hash requires the explicit per-context probability premise above;
this receipt does not certify an unreviewed correction. No full-history law,
physical effect bridge, preparation selection, or empirical validity has been
derived here. Referenced earlier runtime/composite notes were not reopened:
the integrated proofs were checked on their own stated arguments. This is a
hand-proof/source check without formal verification and without audit authority.
