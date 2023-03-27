import random
import itertools

def hodnotaKombinace(perm):
	hodnota=0
	for per in perm:
		hodnota+=items[per].hodnota
	return hodnota


def vahaKombinace(perm):
	vaha=0
	for per in perm:
		vaha+=items[per].vaha
	return vaha

def NemaVsechyTypy(perm):
	typ1=0
	typ2=0
	typ3=0
	for per in perm:
		
		if(items[per].typ==1):
			typ1+=1
		if(items[per].typ==2):
			typ2+=1
		if(items[per].typ==3):
			typ3+=1
	if typ1==0 or typ2==0 or typ3==0:
		return True
	else:
		return False

def generateItems(items):
	for i in range(8):
		newItem=Item(i,random.randint(1,200),random.randint(1,200),random.randint(1,3))
		items.append(newItem)

def generateCombinations(combinations):
	for i in range(8):
		for itert in itertools.combinations([0,1,2,3,4,5,6,7],i):
			combinations.append(itert)


class Item:
	def __init__(self,ID,vaha,hodnota,typ):
		self.ID=ID
		self.vaha=vaha
		self.hodnota=hodnota
		self.typ=typ
vahaBatohu=500
items=[]

#for item in items:
#	print(item.ID)
#	print(item.vaha)
#	print(item.hodnota)
#	print(item.typ)
#	print(" ")
generateItems(items)
combinations=[]

#print(combinations[21][0])
#print(combinations[21][1])
nejhodnota=0
nejlepsiPermutace=[]

counter=0
naVyhozeni=[]

repeat=True
result=False
generateCombinations(combinations)
generateItems(items)
while(result==False):
	for i in range(len(combinations)):
		#print(len(combinations))
		if (vahaKombinace(combinations[i])) > vahaBatohu:
			combinations.pop(i)
			result=False
			break
		else:
			result=True
result=False

while(result==False):
	if len(combinations)<5:
			
		repeat=True
		break
	else:
		repeat=False
	for i in range(len(combinations)):			
		#print(len(combinations))
		if NemaVsechyTypy(combinations[i]):
			combinations.pop(i)
			result=False
			break
		else:
			result=True
	
for perm in combinations:
	#rint(perm)
	hodnotaItemu=0
	for ID in perm:
		hodnotaItemu+=items[ID].hodnota
	if hodnotaItemu > nejhodnota:
		nejlepsiPermutace.clear()
		nejhodnota=hodnotaItemu
		nejlepsiPermutace.append(perm)
	if hodnotaItemu== nejhodnota and nejlepsiPermutace[len(nejlepsiPermutace)-1]!=perm:
		nejlepsiPermutace.append(perm)
	#print(hodnotaItemu)
	hodnotaItemu=0




for nej in nejlepsiPermutace:
	print("ID předmětů:",nej)
	print("Nejlepší kombinace předmětů:")
	print("Hodnota:", hodnotaKombinace(nej))
	print("Váha:",vahaKombinace(nej))
