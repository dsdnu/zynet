from zynet import zynet
from zynet import utils
import numpy as np

def genMnistZynet(dataWidth):
    model = zynet.model()
    model.add(zynet.layer("flatten",784))
    model.add(zynet.layer("Dense",30,"relu"))
    model.add(zynet.layer("Dense",30,"relu"))
    model.add(zynet.layer("Dense",10,"relu"))
    model.add(zynet.layer("Dense",10,"relu"))
    model.add(zynet.layer("Dense",10,"hardmax"))
    weightArray = utils.genWeightArray('WeigntsAndBiasesReLU.txt')
    biasArray = utils.genBiasArray('WeigntsAndBiasesReLU.txt')
    model.compile(pretrained='Yes',weights=weightArray,biases=biasArray,dataWidth=dataWidth,weightIntSize=1,inputIntSize=4)
    zynet.makeXilinxProject('myProject','xc7z020clg484-1')
    zynet.makeIP('myProject')
    zynet.makeSystem('myProject','myBlock2')
    
if __name__ == "__main__":
    genMnistZynet(dataWidth=16)