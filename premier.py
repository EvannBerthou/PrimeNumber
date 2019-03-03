import math,time

def isInt(x): #Vérifie si x peut être convertie en int
	try:
		int(x)
		return True
	except:
		print("{0} is not a number".format(x))
		return False

def WriteToFile(n, premiers):
	fileName = "{}-prime".format(n)
	with open(fileName, 'w') as f:
		f.write("Total Prime Numbers : {}\n".format(len(premiers))) #Ecris en première ligne le nombre de nombre premiers calculés
		f.write("\n".join(str(number) for number in premiers)) #Ecris dans le fichier tous les nombres de la liste

def checkNotPrime(i,k):
	return i%k==0 #Vérifie si le reste de la division de i par k est 0

def checkPrimeNumber(limit, i):
	for k in range(2,limit + 1): #k [2; SQRT(i)]
			if checkNotPrime(i,k):
				return False
	return True

def checkAllPrimes(n,start):
	premiers = [2] #Liste de tous les nombres premiers calculés

	for i in range(2,n):

		#Utilisé pour montrer la progression mais ralentis le programme
		timeSpent = "{:09.2f}".format(time.time() - start)
		pourcentage = "{:03.2f}".format(i / n * 100)
		print("Time spent : {}, {}%".format(timeSpent, pourcentage), end='\r')

		if i % 2 != 0: #Vérifie seulement si i i est impair

			limit = math.ceil(math.sqrt(i)) #Calcul le nombre maximum d'itération, gain de performance
			if checkPrimeNumber(limit,i): #Si le nombre est premier après toutes les vérifications
				premiers.append(i)

	WriteToFile(n,premiers)
	return 1

n = input("n : ")
if isInt(n):

	start = time.time()

	n = int(n)
	checkAllPrimes(n, start)

	print(time.time() - start) #Temps d'éxécution de la fonction checkAllPrimes


"""
TIME (secondes):
1,000			0.0029783248901367188
10,000			0.050864219665527344
100,000			1.89640212059021
1,000,000		71.52397298812866
10,000,000		2180.9676043987274 (36 minutes)
100,000,000	
"""