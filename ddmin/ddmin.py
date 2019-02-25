

class DDMin:
    def __init__(self, circumstances, test_func, default_partition=2):
        self.circumstances = circumstances
        self.test = test_func
        self.part = default_partition


    def listminus(self, circ1, circ2):
        """Return all elements of C1 that are not in C2.  Assumes elementes of C1
        are hashable."""
        # The hash map S2 has an entry for each element in C2
        s2 = {delta:1 for delta in circ2}
        return [delta for delta in circ1 if not s2.get(delta, None)]

    def split(self, circumstances, partition):
        """Split a configuration of CIRCUMSTANCES into N subsets; return the list
            of subsets."""

        subsets= [] # Result
        start = 0   # Start of the next subset
        len_subset = 0
        for idx in range(0, partition):
            len_subset = int((len(circumstances) - start) / float(partition - idx) + 0.5)
            subset = circumstances[start:start + len_subset]
            subsets.append(subset)
            start += len(subset)

        assert len(subsets) == partition
        assert not any([len(subset) == 0 for subset in subsets])
        return subsets

    def execute(self):
        """Return a sublist of CIRCUMSTANCES that is a relevant configuration with
        respect to TEST."""

        assert self.test([]) == True                  # Hard condition, empty must not trigger
        assert self.test(self.circumstances) == False # The circumstances must trigger

        partition = self.part                         # Usually start with binary, 2, but...

        while len(self.circumstances) >= 2:
            subsets = self.split(self.circumstances, partition)
            some_complement_is_failing = False
            for subset in subsets:
                complement = self.listminus(self.circumstances, subset)
                if self.test(complement) == False:
                    self.circumstances = complement
                    partition = max(partition - 1, 2)
                    some_complement_is_failing = True
                    break

            if not some_complement_is_failing:
                if partition == len(self.circumstances):
                    break
                partition = min(partition*2, len(self.circumstances))

        return self.circumstances

