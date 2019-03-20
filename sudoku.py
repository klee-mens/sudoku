a = [False for i in range(3)]
b = [a for i in range(3)]
c = [b for i in range(3)]

#print(c)

sudoku = [[0 for i in range(9)] for j in range(9)]
moeglichkeiten = [[[True for i in range(9)] for j in range(9)] for k in range(9)]

# Beispiel für ein leichtes Sudoku
def sudoku_leicht1():
	sudoku[0][0] = 2
	sudoku[0][7] = 4
	sudoku[1][0] = 1
	sudoku[1][1] = 5
	sudoku[1][3] = 8
	sudoku[1][5] = 6
	sudoku[2][0] = 6
	sudoku[2][3] = 5
	sudoku[2][7] = 2
	sudoku[3][1] = 1
	sudoku[3][2] = 8
	sudoku[3][3] = 9
	sudoku[3][5] = 5
	sudoku[3][6] = 7
	sudoku[3][8] = 2
	sudoku[4][1] = 7
	sudoku[4][2] = 2
	sudoku[4][5] = 3
	sudoku[4][6] = 8
	sudoku[4][8] = 4
	sudoku[5][0] = 5
	sudoku[5][4] = 8
	sudoku[5][5] = 7
	sudoku[5][6] = 9
	sudoku[6][0] = 8
	sudoku[6][2] = 5
	sudoku[6][3] = 6
	sudoku[6][4] = 9
	sudoku[6][6] = 4
	sudoku[6][8] = 3
	sudoku[7][0] = 4
	sudoku[7][1] = 3
	sudoku[7][7] = 8
	sudoku[7][8] = 9
	sudoku[8][0] = 7
	sudoku[8][1] = 6
	sudoku[8][3] = 4
	sudoku[8][8] = 5


def sudoku_mittel1():
	sudoku[0][2] = 3
	sudoku[0][3] = 9
	sudoku[0][5] = 7
	sudoku[0][7] = 8
	sudoku[1][1] = 9
	sudoku[1][3] = 3
	sudoku[1][4] = 1
	sudoku[1][5] = 4
	sudoku[1][6] = 5
	sudoku[1][7] = 2
	sudoku[2][0] = 2
	sudoku[2][1] = 4
	sudoku[2][2] = 7
	sudoku[2][5] = 5
	sudoku[2][8] = 9
	sudoku[3][7] = 5
	sudoku[4][0] = 6
	sudoku[4][8] = 1
	sudoku[5][3] = 2
	sudoku[5][4] = 5
	sudoku[5][6] = 7
	sudoku[5][7] = 6
	sudoku[6][1] = 2
	sudoku[6][2] = 8
	sudoku[7][2] = 9
	sudoku[7][3] = 8
	sudoku[7][6] = 3
	sudoku[7][8] = 2
	sudoku[8][0] = 4
	sudoku[8][6] = 6

def sudoku_schwer1():
	sudoku[0][3] = 2
	sudoku[0][5] = 6
	sudoku[0][7] = 8
	sudoku[0][8] = 1
	sudoku[1][0] = 2
	sudoku[1][2] = 3
	sudoku[1][8] = 6
	sudoku[2][1] = 7
	sudoku[2][6] = 3
	sudoku[2][7] = 9
	sudoku[3][1] = 1
	sudoku[3][3] = 6
	sudoku[3][4] = 9	
	sudoku[3][5] = 3
	sudoku[3][7] = 2
	sudoku[4][6] = 9
	sudoku[4][7] = 6
	sudoku[5][0] = 8
	sudoku[5][3] = 5
	sudoku[5][4] = 2
	sudoku[5][5] = 7
	sudoku[5][8] = 4
	sudoku[6][3] = 3
	sudoku[6][4] = 4
	sudoku[7][2] = 2
	sudoku[7][8] = 8
	sudoku[8][0] = 9
	sudoku[8][1] = 5
	sudoku[8][4] = 1
	sudoku[8][7] = 4


def sudoku_sehr_schwer1():
	sudoku[0][0] = 1

def sudoku_clear():
	for i in range(9):
		for j in range(9):
			sudoku[0][0] = 0

def show():
	for i in range(9):
		row = sudoku[i][:]
		s = ''
		for j in range(9):
			if row[j] == 0:
				s += ' '
			else:
				s+= str(row[j])
			if (j == 2) or (j == 5):
				s += '|'
		print(s)
		if (i == 2) or (i == 5):
			print('-'*11)


def get_quarter_index(i, j):
	gqii = 3*(i // 3)
	gqij = 3*(j // 3)
	return [gqii, gqij]

def get_quarter(i, j):
	vec1 = get_quarter_index(i ,j)
	p = vec1[0]
	q = vec1[1]
	vec2 = []
	for i in range(3):
		row = []
		for j in range(3):
			vec2.append(sudoku[p+i][q+j])

	return vec2

				
def moeglichkeiten_eliminieren():
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				row = [sudoku[i][k] for k in range(9)]
				column = [sudoku[k][j] for k in range(9)]
				box = get_quarter(i, j)
				for k in range(9):
					zahl = k + 1
					if moeglichkeiten[i][j][k] and ((zahl in row) or (zahl in column) or (zahl in box)):
						moeglichkeiten[i][j][k] = False
			else:
				for k in range(9):
					moeglichkeiten[i][j][k] = False


def solutio_1():
	moeglichkeiten_eliminieren()
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				noch_moeglich = 0
				for k in range(9):
					if moeglichkeiten[i][j][k]:
						noch_moeglich += 1
						pot_neuer = k + 1
				if noch_moeglich == 1:
					sudoku[i][j] = pot_neuer


			


def tests():
	v = get_quarter_index(4, 7)
	print(v[0], v[1])
	vec2 = get_quarter(4, 7)
	print(vec2)
	a = [True, True]
	if a[1]:
		print('Ja')

#Program start
sudoku_schwer1()
show()
#tests()
while True:
	input('weiter tippen')
	solutio_1()
	show()
