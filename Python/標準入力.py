# 標準入力

# 1行に1つの文字　例：5
box = input()		# 5を取得し、boxに値を入れる
print(box)			# 出力 5

# 1行に1つの整数の入力を取得し、整数として出力　例：i
box = int(input())	# iを取得し、boxにいれる
print(box)			# 出力 i

# 1行に複数に入力値を取得し、出力する　例：s_1 s_2
box = input().split()	# s_1 s_2を分割、取得し、boxにいれる
print(box)				# 出力　['s_1', 's_2']
print(box[0])			# 出力　s_1
print(box[1])			# 出力　s_2

# 1行に複数の整数の入力を取得し、整数として出力する　例：s_1 s_2
box = list(map(int, input().split()))	# s_1 s_2を分割、取得し、boxにいれる
print(box[0])			# 出力　s_1
print(box[1])			# 出力　s_2
