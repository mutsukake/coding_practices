import math

def calculate_standard_deviation(values):
    """
    標準偏差を計算する関数
    
    Parameters:
    values (list): 数値のリスト
    
    Returns:
    float: 標準偏差
    """
    n = len(values)
    if n <= 1:
        return 0.0
    
    mean = sum(values) / n
    sum_of_squared_diff = sum((x - mean) ** 2 for x in values)
    # 母集団の標準偏差: 分散 = sum_of_squared_diff / n
    variance = sum_of_squared_diff / n
    return math.sqrt(variance)

def main():
    while True:
        # まず学生の数 n を読み取る
        n = int(input().strip())
        if n == 0:
            # n=0 なら処理終了
            break
        
        # 次の行で n 個のスコアを読み取り、リストに変換
        values = list(map(float, input().split()))
        
        std_dev = calculate_standard_deviation(values)
        
        # 誤差 0.0001 以下が許容されるので、小数点以下適度に出力
        print(f"{std_dev:.8f}")

if __name__ == "__main__":
    main()