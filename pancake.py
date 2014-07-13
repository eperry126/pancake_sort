import random

class Pancake(object):
    def __init__(self, value):
        self.value = value
        self.burnt_side_down = bool(random.getrandbits(1))


class PancakeStack(object):
    def __init__(self, pancakes):
        self.pancakes = pancakes

    def flip(self, position):
        # Determine the last position to which we will be swapping items
        items_to_swap = ((len(self.pancakes) - position) / 2)

        # Swap the pancakes effectively "flipping" the stack from the position
        # provided
        for i in range(0, items_to_swap):
            temp = self.pancakes[len(self.pancakes) - i - 1]
            self.pancakes[len(self.pancakes) - i - 1] = self.pancakes[position + i]
            self.pancakes[position + i] = temp

    def sort(self):
        last_sorted_position = 0

        # Start at the bottom and find the largest out of order pancake.
        # Flip that pancake to the top, and then back down to the last
        # un-sorted position.
        while last_sorted_position < len(self.pancakes) - 1:
            to_flip = self.largest_out_of_order(last_sorted_position)
            self.flip(to_flip)
            self.flip(last_sorted_position)
            last_sorted_position += 1

    def largest_out_of_order(self, start):
        largest = start
        for i in range(start, len(self.pancakes)):
            if self.pancakes[i].value > self.pancakes[largest].value:
                largest = i
        return largest

    def ordered(self):
        for i in range(0, len(self.pancakes) - 1):
            if self.pancakes[i].value >= self.pancakes[i + 1].value:
                return False
        return True