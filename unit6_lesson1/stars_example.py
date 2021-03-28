"""
Mykyta S.
stars_example.py
Example of stars data
"""

class Stardata(object):
    """Represents a star.

    Attributes:
      starName: string
      bvColour: float
      absoluteMagnitude: float
    """

    def __init__(self, starName='', bvColour=0.0, absoluteMagnitude=0.0):
        self.starName = starName #string
        self.bvColour= bvColour #float
        self.absoluteMagnitude = absoluteMagnitude #float

    def __str__(self):
        return "Star Name: {0:12}\n\
            b-v colour: {1:5}\n\
            absoute magnitude: {2:5}".format(self.starName, self.bvColour, self.absoluteMagnitude)


class Starsdata(object):
    """Represents a list of Stardata objects

    Attributes:
    """

    def __init__(self):
        self.starlist= [] #a list of class Stardata
        mynewhandle = open("stardata.csv", "r")
        theline = mynewhandle.readline() #skip first line with column headings
        somedata=Stardata() #create a Stardata object
        self.starlist.append(somedata) # do this to put a 'blank' star in the first index 0
        count=0 #to count how many sets of data are read
        while True:
            theline=mynewhandle.readline()
            count +=1
            if len(theline) == 0:              # If there are no more lines
                break                          #     leave the loop
            else:
                alist = theline.split(",")
                #make sure the data is read in properly with the proper data types
                somedata= Stardata(alist[0],float(alist[1]),float(alist[2]))
                self.starlist.append(somedata)
        mynewhandle.close()
        self.numData=count

    def sortbyname(self):
        #supply the code
        for i in range(1,self.numData-1):
            for j in range(1,self.numData-1):
                if self.starlist[j].starName > self.starlist[j+1].starName:
                    tmp = self.starlist[j]
                    self.starlist[j] = self.starlist[j+1]
                    self.starlist[j+1]=tmp
        return self

    def sortbyabsolutemagnitude(self):
        #supply the code
        for i in range(1,self.numData-1):
            for j in range(1,self.numData-1):
                if self.starlist[j].absoluteMagnitude > self.starlist[j+1].absoluteMagnitude:
                    tmp = self.starlist[j]
                    self.starlist[j] = self.starlist[j+1]
                    self.starlist[j+1]=tmp
        return self


    def searchbyName(self,Starname):
        for j in range(self.numData):
            if self.starlist[j].starName ==Starname: #need int to convert string to integer
                #print('Star: ',Starname)
                print(self.starlist[j]) #print the element that was found
        #return self.starlist[j]

if __name__ == "__main__":
    stardb = Starsdata()

    stardb.searchbyName('sun') #search for the sun
    stardb.sortbyabsolutemagnitude() #sort by absolute magnitude
    for i in range(1,stardb.numData): #display the data to check the sort
        print(stardb.starlist[i].starName," ", end="")
        print(stardb.starlist[i].absoluteMagnitude)

