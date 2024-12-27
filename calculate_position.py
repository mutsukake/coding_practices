# Program to calculate the maximum position

def max_position(num_rolls):
    positions = [0]  # 各ターンの位置
    num_dice = 1  # サイコロの数

    for _ in range(num_rolls):
        # サイコロは各6の目が出ると仮定
        total_roll = num_dice * 6
        position = positions[-1] + total_roll

        # ワープの確認（7マス目に止まると11マス目に移動）
        if positions[-1] < 7 and position >= 7:
            position += 4  # 7から11へのワープ（11 - 7 = 4）

        positions.append(position)

        # 出た目の合計が3以下の場合、次回のみサイコロが1つ追加
        if total_roll <= 3:
            num_dice += 1
        else:
            num_dice = 1
        # 最大値を求める場合、合計は6以上なのでサイコロは増えない


    return positions[1:]  # 初期位置0を除く

for rolls in range(1, 6):
    positions = max_position(rolls)
    print(f"{rolls}回: {positions[-1]}マス目")