from ride import Ride
class Car :
	def __init__(self):
		self.coords = (0,0)
		self.done = []
		#Ride Class
		self.rideOnProgress = None
		self.movements = 0 
	
	"""Yolu alıcak ve movementsı ayarlıcak"""
	def addRide(self,ride:Ride):
		if self.isEmpty():
			self.rideOnProgress = ride	
			ride.taken()
			if self.distance(ride) > earliestStar:
			
		else:
			print("İşi olan bir araca görev verildi." +ride.frm + self.to + self.rideNumber)
		
	def getCoords(self):
		return self.coords

	"""Aracı n adım kadar ilerlet"""
	def move(self,n):
		if self.movements > n:
			self.movements -=n
		else:
			self.movements = 0
			self.coords = self.rideOnProgress.to
			"""
			Ride ın sadece numarası ekleniyor.
			Outputta sıkıntı çıkartabilir burası.
			"""
			self.done.append(self.rideNumber)
			
		
	def setNextTAvaibleRide(self,T):
		pass

	def calculatePointsForRide(self,ride:Ride):
		pass
	
	def getMovement(self):
		return self.movements

	"""Aracın uygun olup olmadığını kontrol et."""
	"""Aracın yapıcağı hareket yoksa doğru varsa yanlış döndür."""
	def isEmpty(self) -> bool:
		if self.movements == 0:
			return True

		else:
			return False

	#Rideın başıyla bitimi arasındaki mesafe 
	def distanceBetweenEndAndBeginning(self,ride):
		return abs(ride.from()[0]-ride.to()[0]) + abs(ride.from()[1]-ride.to()[1])

	#Araçla ride arasındaki mesafe
	def distanceBetweenRideAndCar(self,ride):
		rideCoords = ride.from()
		return abs(self.coords[0]-rideCoords[0]) + abs(self.coords[1] - rideCoords[1])
