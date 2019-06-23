import json

def genWeightArray(fileName=""):
	weightFile = open(fileName,"r")
	myData = weightFile.read()
	myDict = json.loads(myData)
	myWeights = myDict['weights']
	return myWeights
	#print(len(myWeights[0][0]))
    
def genBiasArray(fileName=""):
	biasFile = open(fileName,"r")
	myData = biasFile.read()
	myDict = json.loads(myData)
	myBiases = myDict['biases']
	return myBiases