"""
税率込みの計算機
"""
try:
	from console import clear
except ImportError:
	import os
	clear = os.system

import sys

calcfield = []
CalcedData = 0

try:
	clear()
except TypeError:
	clear('clear')

while True:
	try:
		clear()
	except TypeError:
		clear('clear')
	print('使い方: 入力価格,税率,割引率\n\n◆入力価格: 本体価格を入力\n◆税率:「10%」または「8%」と入力\n◆割引率:「10%」 または 「1割引」の場合「0.1」と入力\n')
	try:
			try:
				print('現在の値段: {}({})円\n'.format(eval('+'.join(calcfield)), '+'.join(calcfield)))
			except:
				print('現在の値段: 0()円')
			CInput = input('価格: ').replace(' ','').split(',')
			try:
				if not CInput[2] == '':
					try:
						if CInput[1] == '10%':
							Cc = str(round((eval(CInput[0]) - (eval(CInput[0]) * eval(CInput[2]))) * 1.1))
						elif CInput[1] == '8%':
							Cc = str(round((eval(CInput[0]) - (eval(CInput[0]) * eval(CInput[2]))) * 1.08))
					except IndexError:
						Cc = str(round((eval(CInput[0]) - (eval(CInput[0]) * eval(CInput[2]))) * 1.08))
			except IndexError:
				try:
					if CInput[1] == '10%':
						Cc = str(round(eval(CInput[0]) * 1.1))
					elif CInput[1] == '8%':
						Cc = str(round(eval(CInput[0]) * 1.08))
				except IndexError:
					Cc = str(round(eval(CInput[0]) * 1.08))
						
			calcfield.append(Cc)
	except KeyboardInterrupt:
		try:
			CalcedData = eval('+'.join(calcfield))
		except SyntaxError:
			sys.exit(0)
		try:
			clear()
		except TypeError:
			clear('clear')
		break
	except:
		pass

print('計算結果は: {}円です'.format(CalcedData))