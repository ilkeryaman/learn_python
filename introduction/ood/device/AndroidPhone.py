from introduction.ood.device.Camera import Camera
from introduction.ood.device.Lantern import Lantern
from introduction.ood.device.Phone import Phone


# => Python has proper duck-typing and multi-inheritance.
class AndroidPhone(Camera, Lantern, Phone):
    pass

