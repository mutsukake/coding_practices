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


######################################
#  既存の「サイコロ I」用コード (参考)
######################################
def solve_dice_I():
    face = list(map(int, input().split()))
    n = int(input())
    for _ in range(n):
        command = input().strip()
        dice = Dice(*face)
        for cmd in command:
            if cmd == 'N':
                dice.roll_north()
            elif cmd == 'S':
                dice.roll_south()
            elif cmd == 'E':
                dice.roll_east()
            elif cmd == 'W':
                dice.roll_west()
        print(dice.get_top())


######################################
#  ここから「サイコロ II」用コード
######################################
def solve_dice_II():
    # 1行目: サイコロの各面 (top, front, right, left, back, bottom)
    faces = list(map(int, input().split()))
    dice = Dice(*faces)

    # 全24通りの向きを探索するための辞書
    # キー  : (上面の値, 前面の値)
    # バリュー: 右面の値
    orientation_map = {}

    # 幅優先探索 (BFS) 用にキューを用意
    from collections import deque
    queue = deque()
    
    # 初期状態を登録
    init_state = (dice.top, dice.front, dice.right, dice.left, dice.back, dice.bottom)
    queue.append(init_state)
    visited = set([init_state])

    while queue:
        top, front, right, left, back, bottom = queue.popleft()
        # 上面と前面をキーにして、右面を登録
        orientation_map[(top, front)] = right

        # 現在の状態を Dice インスタンスで再現
        d = Dice(top, front, right, left, back, bottom)

        # 4方向に回転して新しい状態を探索
        for roll_func in (d.roll_north, d.roll_south, d.roll_east, d.roll_west):
            roll_func()  # 1回転
            new_state = (d.top, d.front, d.right, d.left, d.back, d.bottom)
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)
            # 元の向きに戻す必要があれば、もう一度逆方向に回すか、
            # 新しいDiceを都度作り直してもOK。
            # 今はループのたびに d を再生成しているので問題ありません。

    # 2行目: 質問の数 q
    q = int(input())

    # 続く q 行で、(上面, 前面) が与えられる
    for _ in range(q):
        t, f = map(int, input().split())
        # orientation_map から (t, f) に対応する右面の値を取得
        print(orientation_map[(t, f)])


######################################
# 実行パート
######################################
if __name__ == "__main__":
    """
    サイコロ II を実行したい場合は、
    solve_dice_II() を呼び出してください。

    サイコロ I を試したい場合は、
    solve_dice_I() を呼び出してください。
    """
    # 例: サイコロ II の場合
    solve_dice_II()
    
    # もしサイコロ I を実行したいなら下記のようにコメントアウトを切り替えてください
    # solve_dice_I()