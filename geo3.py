import matplotlib.pyplot as plt
import math
import numpy as np


ep_dielec_masse = 1*(10^-4)
rayon_ext_rouleau = 7.5*(10^-2)
gap = 1*(10^-3)
ep_dielec_ht = 1*(10^-4)
largeur_elec_ht = 9.5*(10^-3)
rayon_courbure_ext = 2*(10^-3)
rayon_courbure_int= 5*(10^-4)
angle_elec_ht = 15
gap_elec_ht = 0.2*(10^-3)
longueur_elec = 30*(10^-3)


x1_int = sin(15*pi*2/360)*longueur_elec+gap_elec_ht
x2_int = gap_elec_ht
x3_int = cos(3.3*pi*2/360)*largeur_elec_ht
x4_int = sin(15*2*pi/360)*longueur_elec+cos(3.3*pi*2/360)*largeur_elec_ht

y1_int = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(sin(15*2*pi/360)*longueur_elec+gap_elec_ht)^2)+cos(15*2*pi/360)*longueur_elec+gap
y2_int = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(gap_elec_ht)^2)+gap
y3_int = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(cos(3.3*pi*2/360)*largeur_elec_ht)^2)+gap
y4_int = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(sin(15*2*pi/360)*longueur_elec+cos(3.3*pi*2/360)*largeur_elec_ht)^2)+gap+cos(15*2*pi/360)*longueur_elec

XINT = [x1_int, x2_int, x3_int, x4_int, x1_int]
YINT = [y1_int, y2_int, y3_int, y4_int, y1_int]

#----------------------------------------------------------------------------
x1_ext = sin(15*pi*2/360)*longueur_elec+gap_elec_ht-cos(15*2*pi/360)*ep_dielec_ht
x2_ext = gap_elec_ht-cos(15*2*pi/360)*ep_dielec_ht
x3_ext = cos(3.3*pi*2/360)*largeur_elec_ht+cos(15*2*pi/360)*ep_dielec_ht
x4_ext = sin(15*2*pi/360)*longueur_elec+cos(3.3*pi*2/360)*largeur_elec_ht+cos(15*2*pi/360)*ep_dielec_ht

y1_ext = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(sin(15*2*pi/360)*longueur_elec+gap_elec_ht)^2)+cos(15*2*pi/360)*longueur_elec+gap+cos(3.3*pi*2/360)*ep_dielec_ht
y2_ext = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(gap_elec_ht)^2)+gap-cos(3.3*pi*2/360)*ep_dielec_ht
y3_ext = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(cos(3.3*pi*2/360)*largeur_elec_ht)^2)+gap-cos(3.3*pi*2/360)*ep_dielec_ht
y4_ext = sqrt((rayon_ext_rouleau+ep_dielec_masse)^2-(sin(15*2*pi/360)*longueur_elec+cos(3.3*pi*2/360)*largeur_elec_ht)^2)+gap+cos(15*2*pi/360)*longueur_elec+cos(3.3*pi*2/360)*ep_dielec_ht

XEXT = [x1_ext, x2_ext, x3_ext, x4_ext, x1_ext]
YEXT = [y1_ext, y2_ext, y3_ext, y4_ext, y1_ext]

#--------------------------------------------------------------------



xtest_ext = [x1_ext, x2_ext]
ytest_ext = [y1_ext, y2_ext]
xtest_int = [x1_int, x2_int]
ytest_int = [y1_int, y2_int]

plt.plot(XEXT, YEXT)
plt.plot(XINT, YINT)

slope12_ext, intercept12_ext = np.polyfit(xtest_ext, ytest_ext, 1)
slope12_int, intercept12_int = np.polyfit(xtest_int, ytest_int, 1)
print("{0}x+{1}".format(slope12_ext, intercept12_ext))
print("{0}x+{1}".format(slope12_int, intercept12_int))

XTESTGAUCHEBAS = 0.00087
XTESTGAUCHEHAUT= 0.00758

largeur12_bas = sin(15*2*pi/360)*((XTESTGAUCHEBAS*slope12_ext+intercept12_ext)-(XTESTGAUCHEBAS*slope12_int+intercept12_int))
largeur12_haut = sin(15*2*pi/360)*((XTESTGAUCHEHAUT*slope12_ext+intercept12_ext)-(XTESTGAUCHEHAUT*slope12_int+intercept12_int))

print(largeur12_bas)
print(largeur12_haut)
print(asin(x1_int/longueur_elec)*(360)/(2*pi))
print(x1_int)
print((y1_int-y2_int)/(x1_int-x2_int))
print((y4_int-y3_int)/(x4_int-x3_int))
print(y1_int)
plt.show()