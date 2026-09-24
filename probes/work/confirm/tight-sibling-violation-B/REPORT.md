# Referee report: S:tight-sibling-violation-B

- **Finder:** `w-jonathonsmac4f50-4` (`claude-opus-5`), seed 44, box `6×6×9`, start `Z_B`.
- **Referee:** `w-macbookpro90c72-j82ca` (`grok-4.6`). Different model family.
- **Check:** the logged 41-mark configuration, by a level dynamic program. The 1800 s climb was not rerun; the hit is the configuration it printed.

## Witness

`zeta` is the 41 sites in the log. The two-level majority automaton produces 78 ones. The site `(5,4,4)` is processed, at level 13. Its component in the one-site graph has 65 sites, one seed, and nothing above the root, so the unrooted family and the rooted family are the same set of trees.

## Cost

At `c = 1` and one seed the cost is `E − A`. The level DP, exact integers, returns 1. That is the minimum: every legal tree is a state of the DP, and the seed is the only node at level 0.

So both coordinates of the logged maximum are 1. Unrooted cost 1 means `c* > 1`. Rooted cost 1 is positive.

## Verdict

The hit survives. The climb's witness is a real positive-cost configuration, not an artifact of the integer program.
