import matplotlib.pyplot as mpl

temp=[17,20,24,30,32,35,40]
prc=[200, 200, 250, 240, 320, 330,300]

mpl.xlabel( "Temperature in degree centigrades")



mpl.ylabel( "Temperature in degree centigrades")

mpl.scatter(temp,prc)
mpl.show()
mpl.plot(temp,prc)
mpl.show()