class dforest(object):
	def __init__ (self, size=100):
		self.__parent = [i for i in range(size)]
	def find(self, x):
		"""return the representative of x"""
		if self.__parent[x]!=x: self.__parent[x]=self.find(self.__parent[x])
		return self.__parent[x]
	def __str__(self):
		return str(self.__parent)
def union(self, x, y):
	rx, ry  = self.find(x), self.find(y)
	if rx!=ry: 
		krx, kry = self.__rank[rx], self.__rank[ry]
		self.__parent[ry]=rx
		if krx==kry: self.__rank[rx]+=1
		else:
			self.__parent[rx]=ry
df = dforest()
