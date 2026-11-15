---
claim_id: records_that_never_condition_the_odds_give_no_zeno_full_fringes_and_chsh_2_sqrt_2_while_bare_two_time_records_need_a_pointer_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the records of a candidate actuality law with zero premise weight, defined in the note and not a clause of docs/CANDIDATE_LAWS.md (one actual configuration moved by the fewest-change, greatest-entropy transport; every matter mode's occupation recorded each half-tick; records never condition the odds), in supplied few-register models with one fermion per disjoint mode set: the record law is the Born law at every half-tick, so a record every half-tick neither freezes a slow transfer (no Zeno effect) nor removes interferometer fringes; in a two-configuration transfer whose Born probability never falls each track moves at most once, and exactly once when that probability runs from 0 to 1; each actual track carries a definite bare which-path record together with full fringes, so bare records cannot be readable without violating complementarity, while a pointer the update couples to the path gives V = cos(alpha); a register the half-tick acts on only as a control keeps its occupation, so a coin record fixes the setting; CHSH from records with locally recorded settings reaches 2 sqrt 2 and single-time record marginals carry no signal; the joint law of one side's bare records at two half-ticks depends on the distant setting (total variation 0.2183 in the supplied model; nonzero in each of six random setting draws), while after a pointer copy the two-time law equals the Born law of (pointer, outcome) at one half-tick, the quantum sequential law. So in these models reading bare two-time records would make one side's readable statistics depend on the distant setting and reading through a pointer copy would not; this motivates the candidate clause that past records are read only through pointers and does not show that no other reading rule avoids the dependence. Finite supplied models; no physical identification of the registers."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/records_that_never_condition_the_odds_give_no_zeno_full_fringes_and_chsh_2_sqrt_2_while_bare_two_time_records_need_a_pointer_2026_10_22.py
---

# Records that never condition the odds give no Zeno effect, full fringes and CHSH 2 sqrt 2, and in the supplied model a pointer copy removes the distant-setting dependence of bare two-time records

Claim type: bounded_theorem.
Title note (2026-11-14): the file name keeps the earlier title, "... while bare two-time records need a pointer". That wording claims necessity, which this note does not show: items 8 and 9 give one dependence of bare two-time records in a supplied model and one construction, a pointer copy, that removes it. No other reading rule is ruled out.
Primary runner: `scripts/records_that_never_condition_the_odds_give_no_zeno_full_fringes_and_chsh_2_sqrt_2_while_bare_two_time_records_need_a_pointer_2026_10_22.py`.

The actuality law tested here is a supplied candidate with zero premise weight; it is not adopted. It is defined in this paragraph. It is not a clause of the [candidate-law register](CANDIDATE_LAWS.md) on `main`, whose CL-1 to CL-3 aliases are other clauses; CL-2 below is the three-law numbering of the source branch. The law keeps one actual configuration distributed as its odds; each half-tick the configuration moves by the transport that uses only nonzero elements of the half-tick, changes the fewest mode occupations on average and, of those, has greatest entropy (the transport of [the transport note](SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md)), and each matter mode's occupation then gets a permanent record. Records never condition the odds. This note asks what that gives for constant recording, a two-path interferometer and a CHSH test, and which records may be read. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the model inputs used here.

## Statement

In supplied models with one fermion per disjoint mode set (a register):

1. Records never condition the odds, so the law of the records at every half-tick is the Born law of the odds at that half-tick. A record every half-tick does not freeze a slow transfer: there is no Zeno effect.
2. In a two-configuration transfer whose Born probability P(R) never falls from one half-tick to the next, the fewest-change transport moves each actual track at most once. If P(R) also starts at 0 and ends at 1, as in the runner's complete transfer (theta = pi/40, 20 half-ticks), every track moves exactly once. Without those endpoints it is not exactly once: for a transfer that stops at P(R) = 1/2, half the tracks never move. The odds keep the superposition.
3. A two-path interferometer recorded at its outputs gives visibility 1 with P(D1) = cos^2(phi/2) up to the splitter phase.
4. Every actual track also passes through a definite arm, so it carries a definite bare which-path record, and the fringes conditioned on that record are still full. If bare records were readable, path knowledge K = 1 with V = 1 would give V^2 + K^2 = 2, above the measured complementarity bound 1. Bare records are therefore not readable as which-path knowledge.
5. A pointer register that the update couples to the path by an angle alpha removes fringes in the odds and in the records: V = cos(alpha), V^2 + D^2 = 1. Sorting by a rotated pointer record (an eraser) restores fringes and anti-fringes with V = 1.
6. A register that a half-tick acts on only as a control keeps its occupation: a coin record taken before the setting-controlled rotations equals the coin's later occupation, so the coin record is the setting.
7. CHSH from detector-mode records, with settings chosen by local coin records and the two sides' steps in the same half-ticks, reaches the quantum value 2 sqrt 2. Single-time record marginals at one side do not depend on the other side's setting.
8. The joint law of one side's own bare records at two half-ticks (a half-rotated detector and the final outcome) depends on the distant side's setting. It is nonzero in each of six random setting draws (a finite sample, not every setting), and it disappears when the rotations are completed in one half-tick, so that A has nothing to move at the final half-tick.
9. After a pointer copy of the detector occupation in the half-tick right after the first of the two records, the two-time records equal the Born law of (pointer, outcome) at one half-tick: the quantum sequential law, with no dependence on the distant setting.

Items 4, 8 and 9 together motivate CL-2's clause that a past record enters a later reading only through a pointer, a mode whose occupation the update, acting on it as a control alone, leaves unchanged: in these models reading bare two-time records would make A's readable statistics depend on B's setting, and reading through a pointer copy does not. They do not show that no other reading rule avoids the dependence.

## Derivation

Item 1. The odds evolve by the half-tick unitary alone. The transport is constructed so that the actual configuration is distributed as the odds after each half-tick, and a record copies the actual occupation, so its law is that distribution. If each record instead projected the odds, the transfer would follow P = (1 - (1 - 2 sin^2 theta)^T)/2.

Item 2. With two configurations the only least-cost plan moves exactly the shortfall from the falling configuration to the rising one; if P_R never falls, no track ever moves back, so each track moves at most once. A track that starts at R never moves, and the probability that a track moves (from L to R) at half-tick k is P_R(k) - P_R(k-1). So the probability that a track never moves is 1 - (P_R(T) - P_R(0)) = P_R(0) + 1 - P_R(T), which vanishes exactly when P_R starts at 0 and ends at 1.

Item 4. The arm a track passes through is part of its actual configuration, recorded like any other occupation. The output law is the Born law, which has full fringes; conditioned on either arm record the runner prints the same output probability at phi = 0 (printed, not asserted by the check).

Item 6. A half-tick that acts on a register only as a control is block diagonal in that register's occupation, so every transition that changes it has a zero element; the transport uses only nonzero elements, so the occupation stays.

Item 7. Single-time records are Born (item 1), so the record chain reproduces the Born correlations of the final odds. The local step at B is a product unitary, so A's Born marginal is independent of B's setting.

Item 8. The transport is one joint transport over all modes. When B's rotation shares A's second half-tick, the joint plan that moves A's track at that half-tick depends on B's rotation, although each single-time marginal does not.

Item 9. After the copy the pointer holds A's detector occupation at the earlier half-tick and, as a control-only register, keeps it (item 6). The two-time law of A's records is then a single-time Born law of (pointer, outcome).

## Checks

The runner ends with `TOTAL: PASS=14 FAIL=0` in about 2 s and exits nonzero on any failed check. The transport is computed exactly: a linear program gives the least mean occupation change, a second linear program finds the least-cost face, and iterative proportional fitting gives the greatest-entropy plan on that face. Sampled tracks use a seeded generator.

Exact checks (supplied model, finite diagnostic, no physical identification):
- Constant records, one fermion in two modes, hop theta = pi/40 per half-tick, a record every half-tick, 20 half-ticks: P(R) at the end is 1.000000 from the record law, 1.000 from 20000 sampled tracks and 1.000 Born; if records conditioned the odds it would be 0.110. Flips per track: exact law P(1 flip) = 1.000000, P(0) = P(2 or more) = 0; sampled minimum 1, mean 1.000, maximum 1; final |psi| = (0.00e+00, 1.000).
- Control, partial transfer (10 half-ticks, P(R) = 0.500000 at the end): exact P(0 flips) = P(1 flip) = 0.500000 and P(2 or more) = 0, so "at most once" holds and "exactly once" fails without the endpoint 1.
- Interferometer (quarter-hop splitters, arm phase phi as a link phase, 8 phases): V = 1.000000; P(D1) = [0.0, 0.146, 0.5, 0.854, 1.0, 0.854, 0.5, 0.146].
- Bare which-path record: P(path 0) = 0.500; P(D1 | bare path record 0) = P(D1 | bare path record 1) = 0.000 at phi = 0, equal to the unconditioned value.
- Pointer coupling: V = 0.000, 0.500, 0.866, 1.000 at alpha = 1.57, 1.05, 0.52, 0.00 (= cos alpha); the full pointer agrees with the path record with probability 1.000000. Eraser: V = 1.000000 for both pointer outcomes, complementary.
- Control-only coin register: P(coin record at h1 = coin record at h5) = 1.000000000000.
- CHSH (source splitters, a supplied controlled phase standing for a link-mediated gate, hop-out to two detector regions, coin-controlled rotations): S = -2.828427 from the exact odds and from the record chain with settings read from the coin records; -2.819 from 40000 sampled tracks.
- No signalling of single-time marginals: max |P(a|x, y = 0) - P(a|x, y = 1)| = 1.1e-16.
- Bare two-time records at A (half-tick 4, half rotated; final outcome): maximum total variation over A's setting between B's two settings 0.2183. Six random setting draws: 0.163, 0.179, 0.167, 0.023, 0.017, 0.005.
- Control with both sides' rotations whole at half-tick 4 and nothing at the final half-tick: total variation 1.1e-16.
- With a pointer copy at A: total variation 1.3e-16; |two-time law - Born(pointer, outcome)| = 2.8e-17.

## Boundary

Supplied: the registers (one fermion per mode set, no Jordan-Wigner string within a set), the splitter and rotation angles, the arm phase, the controlled phase standing for a link-mediated gate, the coin-controlled rotations, the pointer couplings, the half-tick schedule (which steps share a half-tick) and the random settings. Forced, given those and CL-2: the transport, Born record laws at each half-tick, the absence of a Zeno effect, full fringes with definite bare path records, V = cos(alpha) for a coupled pointer, the fixed coin occupation, CHSH 2 sqrt 2, single-time no signalling, the remote dependence of bare two-time records and its removal by a pointer copy. Not claimed: that the size of the two-time dependence (0.2183) carries over to other models or schedules; any space-like separation, since the two sides here share half-ticks of one joint update; any statement about link or edge registers, which get no records; any physical identification of the registers with detectors.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites with nearest-neighbor adjacency, one qubit per site, one fixed neighborhood admissibility rule, permanent records. They fix none of the supplied inputs above.
- The candidate actuality law defined above: its transport ([transport note](SUPPORT_CONFINED_RELAY_TRANSPORT_ON_THE_MARGOLUS_TICK_BOUNDED_THEOREM_NOTE_2026-10-21.md)), its records that never condition the odds, and its clause that past records are read only through pointers. Zero premise weight; results using it are conditional on it. The [candidate-law register](CANDIDATE_LAWS.md) on `main` does not contain this law.

## How to run

```
python3 scripts/records_that_never_condition_the_odds_give_no_zeno_full_fringes_and_chsh_2_sqrt_2_while_bare_two_time_records_need_a_pointer_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 90`, runs in about 2 s with about 160 MB resident, prints about 3.6 kB, ends with `TOTAL: PASS=14 FAIL=0` and exits nonzero on any failed check.
