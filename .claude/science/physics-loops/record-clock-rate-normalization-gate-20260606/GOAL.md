# Goal

Add a reusable dynamics gate that lets later lanes target a stable location on
a dial without claiming that Record selects the dial value.

The exact claim is:

```text
a supplied production generator can stabilize a dial distribution, while the
absolute physical rate still needs a separate clock/rate normalization.
```

This branch is stacked on the record Markov-generator premise classifier and
does not update repo-wide authority surfaces.
