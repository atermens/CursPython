def ClientBanc(saldo):
	if saldo < -1000:
		return 'Moros'
	elif saldo < 0:
		return 'Apurat'
	elif saldo < 1000:
		return 'Precari'
	return 'Solvent'



def EstacioTrens(linia,sentit):
	if sentit != 'N' and sentit != 'S':
		return 0
	else:
		if linia == 1:
			if sentit == 'N':
				return 1
			return 5
		elif linia == 2:
			if sentit == 'N':
				return 4
			return 9
		elif linia == 3:
			if sentit == 'N':
				return 12
			return 2
		elif linia == 4:
			if sentit == 'N':
				return 10
			return 7
		return 0



def TorneigTennis(edat):
	if type(edat) !=int or edat < 0:
		print 'edat incorrecta'
		return
	elif edat < 8:
		return 'S8'
	elif edat < 12:
		return 'S12'
	elif edat < 18:
		return 'S18'
	print ' massa gran'
	return



def Craps(dau1,dau2):
	if type(dau1) == int and 0 < dau1 < 7:
		if type(dau2) == int and 0 < dau2 < 7:
			tirada = dau1 + dau2
			if  tirada == 7 or tirada == 11:
				return 1
			elif tirada == 2 or tirada == 3 or tirada == 12:
				return 2
			return 0
		return -1
	return -1	



def Qualifica(nota1,nota2,nota3):
	if type(nota1) == str or type(nota2) == str or type(nota2) == str:
		return -1
	if -1 < nota1 < 11 and -1 < nota2 < 11 and -1 < nota3 < 11:
		if nota1 < 5 or nota2 < 5 or nota3 < 5:
			return 0
		nota = (nota1+nota2+nota3)/3.0
		apta = int(nota)
		if  nota1 <= nota2 <= nota3 :
			apta += 1
		if nota1 == 10:
			apta += 1
		if nota2 == 10:
			apta += 1
		if nota3 == 10:
			apta += 1
		return apta
	return -1



def Mitjana():
	bStop = 0
	mitjana = 0.0
	n = 0
	while bStop == 0:
		registre = raw_input('Dada('+str(n+1)+'): ')
		if registre == '':
			bStop = 1
		else:
			valor = float(registre)
			mitjana += valor
			n += 1
	if n == 0:
		print 'No podem calcular la mitjana ('+str(n)+')'
		return
	else:
		print 'Num valors: '+str(n)
		return mitjana/n



def CalculMitjana():
	suma = 0.0
	n = 0
	x = raw_input('Introdueix les dades: ')
	while x != '':
		suma += float(x)
		n += 1
		x = raw_input()
	return suma/n



def CalculaNumDigits(text):
	c = 0
	for car in text:
		print car
		c += 1
	print 'Num digits: '+str(c)
	return 


def NumFrases(text):
	frases=string.split(text,'.')
	n = 0
	suma = 0.0
	for f in frases:
		suma += len(string.replace(f,' ',''))
	print str(suma/len(frases))
	

import string
NumFrases('holaa.adeu.a')


	

