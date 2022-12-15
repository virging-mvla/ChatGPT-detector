from driverInputs import driverInputs

class computation :
    def __init__(self, driverInput) :
        self.finalVal = 0
        self.percentPredicted = 0
        self.driverInput = driverInput

    def findPercentPred (self) :
        self.percentPredicted = self.driverInput.numGreen / (self.driverInput.numGreen + self.driverInput.numYellow + self.driverInput.numRed + self.driverInput.numPurple)

    def computeFinalVal (self) :
        finalVal = 0
        frac = self.driverInput.frac
        self.findPercentPred()
        print (self.percentPredicted)

        if self.percentPredicted > 0.75:
            if self.percentPredicted <= 0.82:
                finalVal += (75 * 0.5)
            else :
                finalVal += 75
        if frac > 0.63:
            if frac <= 0.666 :
                finalVal += (25 * 0.5)
            elif frac < 0.9 :
                finalVal + 25
            else :
                finalVal += 100
        self.finalVal = finalVal
