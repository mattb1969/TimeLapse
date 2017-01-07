################################################################################
#
#   T I M E   L A P S E   P H O T O G R A P H Y
#
#  		Matthew Bennett
#
################################################################################
#
#	Class that takes and returns the photo taken.
#
################################################################################
#
#	Notes:
#		1 - need to run 'sudo apt-get install python3-picamera'

#
#	Todo
# Set the LED


from picamera import PiCamera

class Photography:
	
	def __init__(self, resolution, framerate):
		self.resolution = resolution				# required a tuple (x, y)
		self.framerate = framerate					# required as a fraction
		self.camera = PiCamera(resolution=self.resolution, framerate=self.framerate)
		return
	
	def ledmode(self,mode):
		"""
		mode is either on or off
		"""
		if mode.lower =="on":
			self.camera.led = True
		else:
			self.camera.led = False
		return
	
		
	def setiso(self, iso):
		self.camera.iso = iso
		return
		
	def setshutterspeed(self, shutterspeed):
		self.camera.shutterspeed = shutterspeed
		return
		
	def readexposurespeed(self):
		self.expspeed = camera.exposure_speed
		return self.expspeed
		
	def setawbmode(self,awb):
		# mode is either on or off, default is off
		if awb.lower =="on":
			self.camera.awb_mode = "on"
		else:
			self.camera.awb_mode = "off"
		return
	
	def setawbgains(self,gains):
		self.camera.awb_gains = gains
		return
	
	def readawbgains(self):
		self.awbgains = self.camera.awb_gains
		return self.awbgains
		
	def setexposuremode(self,mode="off"):
		# mode is either on or off, default is off
		if mode.lower =="on":
			self.camera.exposure_mode = "on"
		else:
			self.camera.exposure_mode = "off"
		return
	
	def startpreview(self):
		self.camera.start_preview
		return
		
	def takephoto(self,filename):
		self.camera.capture(filename,'jpeg')
		return
		
	def __exit__(self):		# This could be __del__
		self.camera.close
		return
		
		
		
