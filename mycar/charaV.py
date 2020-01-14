from donkeycar.vehicle import Vehicle
from donkeycar.parts.webCVcam import cvWebcam, cvShow

V = Vehicle()

cam = cvWebcam()

V.add(cam, outputs = ["frames"])

disp = cvShow()

V.add(disp, inputs=["frames"])

V.start()

