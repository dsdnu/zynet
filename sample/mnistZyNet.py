from zynet import zynet
from zynet import utils
import numpy as np

def genMnistZynet(dataWidth,sigmoidSize):
    model = zynet.model()
    model.add(zynet.layer("flatten",784))
    model.add(zynet.layer("Dense",30,"sigmoid"))
    model.add(zynet.layer("Dense",30,"sigmoid"))
    model.add(zynet.layer("Dense",10,"sigmoid"))
    model.add(zynet.layer("Dense",10,"sigmoid"))
    model.add(zynet.layer("Dense",10,"hardmax"))
    weightArray = utils.genWeightArray('WeigntsAndBiasesSigmoid.txt')
    biasArray = utils.genBiasArray('WeigntsAndBiasesSigmoid.txt')
    model.compile(pretrained='Yes',weights=weightArray,biases=biasArray,dataWidth=dataWidth,sigmoidSize=sigmoidSize,weightIntSize=4,inputIntSize=1)
    zynet.makeXilinxProject('myProject1','xc7z020clg484-1')
    zynet.makeIP('myProject1')
    zynet.makeSystem('myProject1','myBlock2')
    
if __name__ == "__main__":
    genMnistZynet(dataWidth=31,sigmoidSize=5)