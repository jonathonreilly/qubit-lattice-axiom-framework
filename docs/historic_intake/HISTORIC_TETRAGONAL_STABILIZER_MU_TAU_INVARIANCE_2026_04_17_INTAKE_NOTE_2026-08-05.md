# Historic intake: Tetragonal Stabilizer and Residual mu-tau Invariance

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pack_science_family
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

Registered as a bounded registration of a historical negative claim; no live no-go is asserted by this wrapper — no-go discipline applies at audit adjudication.

## The claim (as stated by the original, supervisor-compressed)

Proves Stab_{O_h}(e_1) = D_4h with |O_h|=48 and |D_4h|=16, and that D_4h contains sigma_v(2<->3), so any retained operator respecting cubic symmetry plus EWSB axis-1 selection assigns identical matrix elements to the (mu,tau) pair - the retained second-order return is structurally (m_e,m,m)-degenerate. This gives a one-identity explanation for the empirically observed failure of every sole-axiom-native operator to split mu-tau.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Proved symmetry no-go with runner: Stab_Oh(e_1)=D_4h (|48|/|16|) contains sigma_v(2<->3), so any retained operator respecting cubic symmetry plus the EWSB axis-1 selector cannot split mu-tau; exact iff escape condition stated. Converts the 14-lane G5 exhaustion into structure. Near-duplicate sibling attached.

## Provenance (pinned)

- Original path: `.claude/science/derivations/tetragonal-stabilizer-mu-tau-invariance-2026-04-17.md`
- Source commit: `45fa079edee9c8248a0b088a5bce4112ccfa7570`
- git blob: `8fd296068dd28d91add100a67d35591eeb7c62d5`
- sha256: `1bd9698c1eb9720203f7243ca6f7bbba9c0dc41f09d7817bd8a8fa3cb82155e9`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci01/10027_tetragonal-stabilizer-mu-tau-invariance-2026-04-17.md](../../archive_unlanded/historic_intake_originals/packsci01/10027_tetragonal-stabilizer-mu-tau-invariance-2026-04-17.md)
- Lines: 293; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_tetragonal_stabilizer_mu_tau_invariance​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `.claude/science/derivations/g5-s2-residual-symmetry-theorem-2026-04-17.md` — Same-content structural explanation of the 14-lane G5 exhaustion with a falsifier; one cited premise ('S2-preservation in Agent 10 v2') flagged uncertain; evidence attachment.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): PROPOSED symmetry theorem + runner; converts an empirical exhaustion into a structural corollary.
- Extraction scope (triage compression; may reflect later context): Retained hw=1 triplet on the cubic Z^3 taste orbit, generation-axis basis; a symmetry-group statement, not a mass calculation.
- Extraction escape conditions (negative claims; triage compression): Explicit iff-condition: M splits mu-tau if and only if M fails to commute with sigma_v(2<->3), so any candidate primitive must break D_4h.
- Extraction red flags: Duplicate-of-sibling risk: idx 10016 states the same theorem on the same day; a keep decision should probably retain one.
- Supersession (as known at extraction): Near-duplicate in content of .claude/science/derivations/g5-s2-residual-symmetry-theorem-2026-04-17.md (idx 10016) - same D_4h/sigma_v identity, same date, different framing (S2 on axes {2,3} vs mu-tau species). Cites docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md, docs/DM_NEUTRINO_DIRAC_BRIDGE_THEOREM_NOTE_2026-04-15.md, docs/CHARGED_LEPTON_KOIDE_G5_STATUS_NOTE_2026-04-17.md, docs/G1_PHYSICIST_G_MICROSCOPIC_AXIOM_LEVEL_NOTE_2026-04-17.md.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
