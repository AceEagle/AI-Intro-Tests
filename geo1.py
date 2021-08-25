import matplotlib.pyplot
import math
import numpy as np


ep_dielec_masse = 1e-4
rayon_ext_rouleau = 7.5e-2
gap = 1e-3
ep_dielec_ht = 1e-4
largeur_elec_ht = 9.5e-3
rayon_courbure_ext = 2e-3
rayon_courbure_int= 5e-4
angle_elec_ht = 15
gap_elec_ht = 0.2e-3
longueur_elec = 30e-3

#------------------------------------POLY1INT----------------------------------

x1_poly1 = (gap_elec_ht+math.sin(2*math.pi*angle_elec_ht/360)*longueur_elec-ep_dielec_ht)
x2_poly1 = (gap_elec_ht-ep_dielec_ht)
x3_poly1 = (math.cos((3.3*2*math.pi)/360)*(ep_dielec_ht+largeur_elec_ht+gap_elec_ht))
x4_poly1 = (ep_dielec_ht+largeur_elec_ht+gap_elec_ht+math.sin(2*math.pi*angle_elec_ht/360)*longueur_elec)

y1_poly1 = (ep_dielec_ht+rayon_ext_rouleau+gap+ep_dielec_masse+math.cos(2*math.pi*angle_elec_ht/360)*longueur_elec)
y2_poly1 = (rayon_ext_rouleau+gap+ep_dielec_masse-ep_dielec_ht)
y3_poly1 = (-ep_dielec_ht+(rayon_ext_rouleau+gap+ep_dielec_masse)*math.sin(2*math.pi*(90-(360/(2*math.pi*rayon_ext_rouleau/largeur_elec_ht)))/360))
y4_poly1 = (ep_dielec_ht+rayon_ext_rouleau+gap+ep_dielec_masse+math.cos(2*math.pi*angle_elec_ht/360)*longueur_elec)

X_Poly1 = [x1_poly1, x2_poly1, x3_poly1, x4_poly1, x1_poly1]
Y_Poly1 = [y1_poly1, y2_poly1, y3_poly1, y4_poly1, y1_poly1]
#-----------------------------------POLY1EXT---------------------------------

x1_poly1_ext = (math.sin(2*math.pi*angle_elec_ht/360)*longueur_elec+gap_elec_ht)
x2_poly1_ext = (gap_elec_ht)
x3_poly1_ext = (math.cos((3.3*2*math.pi)/360)*(largeur_elec_ht+gap_elec_ht))
x4_poly1_ext = (largeur_elec_ht+gap_elec_ht+math.sin(2*math.pi*angle_elec_ht/360)*longueur_elec)

y1_poly1_ext = (rayon_ext_rouleau+ep_dielec_masse+gap+math.cos(2*math.pi*angle_elec_ht/360)*longueur_elec)
y2_poly1_ext = (rayon_ext_rouleau+gap+ep_dielec_masse)
y3_poly1_ext = ((rayon_ext_rouleau+gap+ep_dielec_masse)*math.sin(2*math.pi*(90-(360/(2*math.pi*rayon_ext_rouleau/largeur_elec_ht)))/360))
y4_poly1_ext = (rayon_ext_rouleau+gap+ep_dielec_masse+math.cos(2*math.pi*angle_elec_ht/360)*longueur_elec)

X_Poly1_ext = [x1_poly1_ext, x2_poly1_ext, x3_poly1_ext, x4_poly1_ext, x1_poly1_ext]
Y_Poly1_ext = [y1_poly1_ext, y2_poly1_ext, y3_poly1_ext, y4_poly1_ext, y1_poly1_ext]


xtest_ext = [x1_poly1, x2_poly1]
ytest_ext = [y1_poly1, y2_poly1]
xtest_int = [x1_poly1_ext, x2_poly1_ext]
ytest_int = [y1_poly1_ext, y2_poly1_ext]
#-----------------------------------------CERCLE1-------------------------------------------------
circle1 = matplotlib.pyplot.Circle((0, 0), rayon_ext_rouleau, color='y')
circle2 = matplotlib.pyplot.Circle((0, 0), (rayon_ext_rouleau+ep_dielec_masse), color='y')


#---------------------------------------POLY2EXT--------------------------------------------------


#--------------------------------------RUN----------------------------------------------
ax = matplotlib.pyplot.gca()
ax.cla()

#ax.plot(X_Poly1, Y_Poly1)
ax.plot(xtest_ext, ytest_ext)
ax.plot(xtest_int, ytest_int)
#ax.plot(X_Poly1_ext, Y_Poly1_ext)
ax.add_patch(circle1)
ax.add_patch(circle2)
slope12_ext, intercept12_ext = np.polyfit(xtest_ext, ytest_ext, 1)
slope12_int, intercept12_int = np.polyfit(xtest_int, ytest_int, 1)
print("{0}x+{1}".format(slope12_ext, intercept12_ext))
print("{0}x+{1}".format(slope12_int, intercept12_int))

XTESTGAUCHEBAS = 0.00087
XTESTGAUCHEHAUT= 0.00758

largeur12_bas = math.sin(15*2*math.pi/360)*((XTESTGAUCHEBAS*slope12_ext+intercept12_ext)-(XTESTGAUCHEBAS*slope12_int+intercept12_int))
largeur12_haut = math.sin(15*2*math.pi/360)*((XTESTGAUCHEHAUT*slope12_ext+intercept12_ext)-(XTESTGAUCHEHAUT*slope12_int+intercept12_int))

print(largeur12_bas)
print(largeur12_haut)
matplotlib.pyplot.show()

epaisseur = 1e-4
