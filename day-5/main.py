import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from base import Day


class Day05(Day):
    def solve_silver(self):
        id_ranges, indices = self.preprocess_inputs(self.data)

        """
        Using the information that the index ranges are sorted
        and do not overlap we can remove one loop 
        """
        num_fresh = 0
        range_id = 0
        for id in indices:
            # If index is larger than current range go to next range
            if id > id_ranges[range_id][1]:
                range_id += 1
                if range_id == len(id_ranges):
                    break

            # If id is in the current range increment num_fresh
            if id >= id_ranges[range_id][0] and id <= id_ranges[range_id][1]:
                num_fresh += 1

        """
        More naive double loop solution
        num_fresh = 0
        for id in indices:
            for id_range in id_ranges:
                if id >= id_range[0] and id <= id_range[1]:
                    num_fresh += 1
                    break
        """
        return num_fresh

    def solve_gold(self):
        id_ranges, _ = self.preprocess_inputs(self.data)

        num_fresh = 0
        # Iterate over the id_ranges and calculate how many values each range has
        for _, (start, end) in enumerate(id_ranges):
            num_fresh += end - start + 1

        return num_fresh

    def preprocess_inputs(self, inputs):
        blank_idx = inputs.index("")
        id_ranges = inputs[:blank_idx]

        # Skip the blank line
        indices = inputs[blank_idx + 1 :]
        indices = sorted(list(map(int, indices)))

        id_ranges = [
            (int(id_range.split("-")[0]), int(id_range.split("-")[1]))
            for id_range in id_ranges
        ]
        id_ranges = sorted(id_ranges)

        # Clean indices
        cleaned = []
        for i in range(len(id_ranges) + 1):
            # Last id, so append to list break
            if i == len(id_ranges):
                cleaned.append((prev_start, prev_end))
                break

            # Get current start and end
            start = id_ranges[i][0]
            end = id_ranges[i][1]

            # If first iteration just save them as previous
            if i == 0:
                prev_start = start
                prev_end = end
                continue

            # If prev_end is smaller than current start add previous values to list
            if prev_end < start:
                cleaned.append((prev_start, prev_end))
                prev_start = start
                prev_end = end
            else:
                # Find largest end value
                # As index array is sorted the prev_start is always <= as start
                prev_end = prev_end if prev_end > end else end

        return cleaned, indices


if __name__ == "__main__":
    Day05(5).run()
