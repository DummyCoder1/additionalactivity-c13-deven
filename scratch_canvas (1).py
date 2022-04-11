import matplotlib.pyplot as mpl

ball=[1,2,3,4,5,6]
bs=[100,160,170,150,120,140]

mpl.xlabel( " no of ball")



mpl.ylabel( "speed of baller")

mpl.scatter(ball,bs)
mpl.show()
mpl.plot(ball,bs)
mpl.show()