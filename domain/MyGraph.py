class Graph:
    def __init__(self, matrix):
        self.__matrix=matrix

    def getNumberOfNodes(self):
        return len(self.__matrix)

    def getMatrix(self):
        return self.__matrix

    def getEdge(self,i,j):
        return self.__matrix[i][j]

    def setEdge(self,i,j,val):
        self.__matrix[i][j]=val

    def __len__(self):
        return self.getNumberOfNodes()