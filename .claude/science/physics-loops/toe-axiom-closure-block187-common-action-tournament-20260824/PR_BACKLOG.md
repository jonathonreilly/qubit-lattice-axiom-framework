# PR Backlog

At campaign freeze:

- PR #7346 is the exact Block-186 stack parent and must remain the base of this
  branch unless its head changes;
- PR #7345 is a parallel DK scout.  Its relevant section action is rebuilt
  from landed Block-128 objects, so this campaign neither merges nor depends
  on that branch;
- PR #7347 appeared late on top of #7345.  Its projective cover reflection and
  dual-frame identities are a fresh next-block regression target, not a
  Block-187 premise; it does not extract the temporal link or stage action;
- no audit verdict or landing action is part of Block 187.

Refresh all three PR heads before opening the stacked Block-187 PR.  If #7346 moves,
rebase only after checking that the scientific inputs and runner authority
remain identical.
