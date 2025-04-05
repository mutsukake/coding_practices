class Dice:
    def __init__(self, top, front, right, left, back, bottom):
        """
        Initialize the dice with the given face values.
        Order is based on the problem statement:
          label 1 -> top
          label 2 -> front
          label 3 -> right
          label 4 -> left
          label 5 -> back
          label 6 -> bottom
        """
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

    def roll_north(self):
        """Roll the dice north (top -> front, front -> bottom, etc.)."""
        self.top, self.front, self.bottom, self.back = (
            self.front, self.bottom, self.back, self.top
        )

    def roll_south(self):
        """Roll the dice south (top -> back, back -> bottom, etc.)."""
        self.top, self.front, self.bottom, self.back = (
            self.back, self.top, self.front, self.bottom
        )

    def roll_east(self):
        """Roll the dice east (top -> left, left -> bottom, etc.)."""
        self.top, self.left, self.bottom, self.right = (
            self.left, self.bottom, self.right, self.top
        )

    def roll_west(self):
        """Roll the dice west (top -> right, right -> bottom, etc.)."""
        self.top, self.left, self.bottom, self.right = (
            self.right, self.top, self.left, self.bottom
        )

    def get_top(self):
        """Return the current top value."""
        return self.top


if __name__ == "__main__":
    # Read six integers from the first line (top, front, right, left, back, bottom)
    faces = list(map(int, input().split()))
    dice = Dice(*faces)

    # Read the sequence of commands (second line)
    commands = input().strip()

    # Process each command
    for cmd in commands:
        if cmd == 'N':
            dice.roll_north()
        elif cmd == 'S':
            dice.roll_south()
        elif cmd == 'E':
            dice.roll_east()
        elif cmd == 'W':
            dice.roll_west()

    # Print the integer on the top face after all rolls
    print(dice.get_top())