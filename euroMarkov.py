#!/usr/bin/env python

from pymarkovchain import MarkovChain
import json
import os.path

class EuroMarkov:
    def __init__(self):
        self.mc = MarkovChain("./markovdata")

    def generateCountryList(self):
        countryList = []
        for filename in os.listdir("json_lyrics/2015"):
            countryList.append(os.path.splitext(filename)[0])
        return countryList

    def loadFiles(self,startYear,endYear,countryList):
        model = ""
        for year in range(startYear,endYear+1):
            for country in countryList:
                fname = "json_lyrics/"+str(year)+"/"+country+".json"
                if os.path.isfile((fname)):
                    with open (fname,"r") as myfile:
                        data = json.load(myfile)
                        model += (data['lyrics']) + '\n';
        return model

    def runMarkov(self,model):
        self.mc.generateDatabase(model)

    def generateString(self):
        return self.mc.generateString()


def main():
	startYear=1960
	endYear=2015
	countryList = ["Austria","United Kingdom","Poland"]
	countryList = ["United Kingdom"]

	print "Building list..."
	model = loadFiles(startYear,endYear,countryList)
	print model
	runMarkov(model)

if __name__ == "__main__":
    main()


