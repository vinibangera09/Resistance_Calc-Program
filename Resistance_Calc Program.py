import math
import pandas as pd
import matplotlib.pyplot as mt
f = float(input("enter the density of water::"))
g = float(input("enter the acceleration due to gravity"))
LOA = float(input("enter the overall length of the ship::"))
LWL = float(input("Enter the length on waterline"))
LBP = float(input("enter th e length between perpendiculars of the ship::"))
LCB = float(input("Enter the LCB of the ship"))
B = float(input("enter the breadth of the ship::"))
T = float(input("enter the draft of the ship::"))
d = float(input("enter the depth of the ship::"))
CB = float(input("enter the block coefficient of the ship::"))
CP = float(input("enter thr prismatic coefficient of the ship::"))
CM = float(input("enter the mid ship area coefficient::"))
CWL = float(input("enter the water plane area coefficient::"))
S = float(input("enter the wetted surface area of the ship::"))
M = float(input("enter the viscosity of the fluid::"))
ABT = float(input("Enter the transverse area of the bulbous bow"))
hB = float(input("Enter the centre of area of ABT above the keel"))
AT = float(input("Immersed area of the transom"))
V = (LOA*B*T*CB)
print("The underwater volume of the ship is::", V)
D = f*V
print("the displacement of the ship is::", D)
n = int(input("Enter the number of speeds"))
Cstern = str(input("Enter the shape of the stern"))
print("1.Pram with gondola")
print("2.V-shaped sections")
print("3.Normal section shape")
print("4.U-shaped sections with hoger stern")
choice = int(input("enter the choice number"))
if choice == 1:
    Cstern = -25
elif choice == 2:
    Cstern = -10
elif choice == 3:
    Cstern = 0
elif choice == 4:
    Cstern = 10
else:
    print("Invalid choice")
Rf = []
FR = []
RW = []
RB = []
RTR = []
RA = []
RApp = []
ve = []

"""FRICTIONAL RESISTANCE"""
for vkn in range(1, n):
    Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
    k = 0.93 + ((0.487118 * (1 + 0.011 * Cstern)) * ((B / LOA) ** 1.06806) * ((T / LOA) ** 0.46106) * ((LWL / Lr) ** 0.121563) * (((LWL ** 3) / V) ** 0.36486) * ((1 - CP) ** -0.604247))
    v = vkn * 0.5144
    Re = (v * LBP) / M
    CF = (0.075 / (((math.log10(Re)) - 2) ** 2))
    ACF = 0.00051
    R = (CF + ACF) * (0.5 * f * S * (v ** 2))
    RF = k * R
    Rf.append(RF)
    continue

"""WAVE MAKING RESISTANCE"""
for vkn in range(1, n):
    v = vkn * 0.5144
    Fr = v / (math.sqrt(g * LBP))
    if Fr < 0.40:
        Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
        ie = 1 + (89 * (math.exp((-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367)*((Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
        if B / LBP < 0.11:
            c7 = 0.229577 * ((B / LBP) ** 0.3333)
        elif 0.11 <= B / LBP <= 0.25:
            c7 = B / LBP
        else:
            c7 = 0.5 - (0.0625 * (LBP / B))
        c1 = 2223105 * (c7 ** 3.78613) * ((T / B) ** 1.07961) * ((90 - ie) ** (-1.37565))
        c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
        c2 = math.exp(-1.89 * (math.sqrt(c3)))
        c5 = 1 - (0.8 * (AT / (B * T * CM)))
        if CP < 0.8:
            c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
        else:
            c16 = 1.73014 - (0.7067 * CP)
        m1 = (0.014047 * (LBP / T)) - ((1.75254*(V**(1/3)))/LBP) - (4.79323 * (B / LBP)) - c16
        if LBP / B < 12:
            l = (1.446 * CP) - (0.03 * (LBP / B))
        else:
            l = (1.446 * CP) - 0.36
        if ((LBP ** 3) / V) < 512:
            c15 = -1.69385
        elif 512 < ((LBP ** 3) / V) < 1726.91:
            c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
        else:
            c15 = 0
        m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
        d_ = -0.9
        Rw = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (Fr ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
        RW.append(Rw)
        FR.append(Fr)
        continue
    elif 0.40 < Fr < 0.55:
        Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
        ie = 1 + (89 * (math.exp((-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367) * ((Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
        if B / LBP < 0.11:
            c7 = 0.229577 * ((B / LBP) ** 0.3333)
        elif 0.11 <= B / LBP <= 0.25:
            c7 = B / LBP
        else:
            c7 = 0.5 - (0.0625 * (LBP / B))
        c1 = 2223105 * (c7 ** 3.78613) * ((T / B) ** 1.07961) * ((90 - ie) ** (-1.37565))
        c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
        c2 = math.exp(-1.89 * (math.sqrt(c3)))
        c5 = 1 - (0.8 * (AT / (B * T * CM)))
        if CP < 0.8:
            c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
        else:
            c16 = 1.73014 - (0.7067 * CP)
        m1 = (0.014047 * (LBP / T)) - ((1.75254*(V**(1/3)))/LBP) - (4.79323 * (B / LBP)) - c16
        if LBP / B < 12:
            l = (1.446 * CP) - (0.03 * (LBP / B))
        else:
            l = (1.446 * CP) - 0.36
        if ((LBP ** 3) / V) < 512:
            c15 = -1.69385
        elif 512 < ((LBP ** 3) / V) < 1726.91:
            c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
        else:
            c15 = 0
        m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
        d_ = -0.9
        rwo_ = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (0.44 ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
        rwo__ = c1 * c2 * c5 * V * f * g * (math.exp((m1 * (0.55 ** d_)) + m4 * (math.cos(l * (Fr ** (-2))))))
        Rw = rwo_ + (((10 * Fr) - 4) * ((rwo__ - rwo_) / 1.5))
        RW.append(Rw)
        FR.append(Fr)
        continue
    else:
        Lr = LWL * ((1 - CP) - ((0.06 * CP * LCB) / (4 * CP - 1)))
        ie = 1 + (89 * (math.exp((-(LBP / B) ** 0.80856) * ((1 - CWL) ** 0.30484) * ((1 - CP - (0.0225 * LCB)) ** 0.6367) * ((Lr / B) ** 0.34574) * (((100 * V) / (LBP ** 3)) ** 0.16302))))
        c17 = (6919.3 * (CM ** (-1.3346))) * ((V / (LBP ** 3)) ** 2.00977) * (((LBP / B) - 2) ** 1.40692)
        m3 = (-7.2035 * ((B / LBP) ** 0.326869)) * ((T / B) ** 0.605375)
        c3 = ((0.56 * ABT) ** 1.5) / ((B * T) * ((0.31 * (math.sqrt(ABT))) + (T - hB)))
        c2 = math.exp(-1.89 * (math.sqrt(c3)))
        c5 = 1 - (0.8 * (AT / (B * T * CM)))
        if CP < 0.8:
            c16 = (8.07981 * CP) - (13.8673 * (CP ** 2)) + (6.984388 * (CP ** 3))
        else:
            c16 = 1.73014 - (0.7067 * CP)
        m1 = (0.014047 * (LBP / T)) - ((1.75254*(V**(1/3)))/LBP) - (4.79323 * (B / LBP)) - c16
        if LBP / B < 12:
            l = (1.446 * CP) - (0.03 * (LBP / B))
        else:
            l = (1.446 * CP) - 0.36
        if ((LBP ** 3) / V) < 512:
            c15 = -1.69385
        elif 512 < ((LBP ** 3) / V) < 1726.91:
            c15 = -1.69385 + (((LBP / (V ** (1 / 3))) - 8) / 2.36)
        else:
            c15 = 0
        m4 = c15 * 0.4 * (math.exp(-0.034 * (Fr ** -3.29)))
        d_ = -0.9
        Rw = c17 * c2 * c5 * V * f * g * (math.exp((m3 * (Fr ** d_) + (m4 * (math.cos(l * (Fr ** -2)))))))
        RW.append(Rw)
        FR.append(Fr)
        continue

""" BULB MAKING RESISTANCE"""
print("Is there bulb in your ship")
print("1.Yes")
print("2.No")
choice = int(input("Enter the choice"))
for vkn in range(1, n):
    v = vkn * 0.5144
    if choice == 1:
        Fri = v / (math.sqrt((g * (T - hB - (0.25 * (math.sqrt(ABT))))) + (0.15 * (v ** 2))))
        pb = (0.56 * (math.sqrt(ABT))) / (T - (1.5 * hB))
        Rb = 0.11 * (math.exp(((-3) * (pb ** (-2)))) * (Fri ** 3) * (ABT ** 1.5) * f * g) / (1 + (Fri ** 2))
        RB.append(Rb)
        continue
    elif choice == 2:
        Rb = 0
        RB.append(Rb)
        continue
    else:
        print("Error")

"""RESISTANCE DUE TO TRANSOM RTR"""
for vkn in range(1, n):
    v = vkn * 0.5144
    ve.append(v)
    FRT = v/(math.sqrt((2*g*AT)/(B+(B*CWL))))
    if FRT < 5:
        c6 = 0.2*(1-(0.2*FRT))
    else:
        c6 = 0
    Rtr = 0.5*f*(v**2)*AT*c6
    RTR.append(Rtr)
    continue

"""MODEL-SHIP CORRELATION RESISTANCE RA"""
for vkn in range(1, n):
    v = vkn * 0.5144
    if T/LBP <= 0.04:
        c4 = T/LBP
    else:
        c4 = 0.04
    c3 = ((0.56*ABT)**1.5)/((B*T)*((0.31*(math.sqrt(ABT))) + (T-hB)))
    c2 = math.exp(-1.89*(math.sqrt(c3)))
    try:
        CA = (0.006*((LBP+100)**-0.16)) - 0.00205 + (0.003 * (math.sqrt(LBP / (7.5 * (CB ** 4) * c2 * (0.04 - c4)))))
    except ZeroDivisionError:
        CA = (0.006 * ((LBP + 100) ** -0.16)) - 0.00205
    Ra = 0.5*f*S*(v**2)*CA
    RA.append(Ra)
    continue

"""APPENDAGE RESISTANCE"""
Sapp = float(input("Enter the Wetted surface area of the Appendage"))
print("1.Rudder behind the skeg")
print("2.Rudder behind stern")
print("3.Twin screw balance rudders")
print("4.Skeg")
print("5.Fin Stabilizers")
print("6.Bilge keel")
choice1 = int(input("Enter your choice"))
if choice1 == 1:
    k2 = 1.5
elif choice1 == 2:
    k2 = 1.3
elif choice1 == 3:
    k2 = 2.8
elif choice == 4:
    k2 = 1.5
elif choice1 == 5:
    k2 = 2.8
else:
    k2 = 1.4
for vkn in range(1, n):
    v = vkn * 0.5144
    Re = (v * LBP) / M
    CF = (0.075 / (((math.log10(Re)) - 2) ** 2))
    Rapp = 0.5*f*(v**2)*Sapp*k2*CF
    RApp.append(Rapp)
    continue

pd.set_option('display.width', 2000)
pd.set_option('display.max_columns', 28)

"""TOTAL RESISTANCE"""
RT = []
for i in range(0, len(Rf)):
    RT.append(Rf[i] + RW[i] + RB[i] + RTR[i] + RA[i] + RApp[i])


"""EFFECTIVE POWER"""
EP = []
for i in range(0, len(RT)):
    v = 0.5144*i
    EP.append((RT[i]*ve[i]))


"""SEA MARGIN"""
SM = []
for i in range(0, len(RT)):
    v = 0.5144*i
    SM.append((EP[i]*1.15))


"""DELIVERED POWER"""
PD = []
for i in range(0, len(RT)):
    v = 0.5144*i
    PD.append((EP[i]/0.65))


"""GEAR BOX"""
GB = []
for i in range(0, len(RT)):
    v = 0.5144*i
    GB.append((PD[i]*1.05))


"""SHAFT POWER"""
SP = []
for i in range(0, len(RT)):
    v = 0.5144*i
    SP.append((PD[i]/0.95))


"""BREAK POWER"""
BP = []
for i in range(0, len(RT)):
    v = 0.5144*i
    BP.append((SP[i]/0.85))


"""DATA FRAME"""
for i in range(0, len(RT)):
    d = pd.DataFrame(
        {'Frictional Resistance': Rf,
         'Wave making resistance': RW,
         'Bulb resistance': RB,
         'Transom Resistance': RTR,
         'Correlation Resistance': RA,
         'Appendage Resistance': RApp,
         'Total Resistance': RT,
         'Froude Number': FR,
         'Velocity': ve,
         'Effective Power': EP,
         'Sea Margin': SM,
         'Delivered Power ': PD,
         'Gear Box ': GB,
         'Shaft Power ': SP,
         'Break Power ': BP}
    )
    print(d)
    break


"""Plot"""
mt.plot(FR, RT)
mt.xlabel("Froude Number")
mt.ylabel("Total Resistance")
mt.show()

mt.plot(ve, RT)
mt.xlabel("Velocity(m/sec)")
mt.ylabel("Total Resistance")
mt.show()

mt.plot(ve, BP)
mt.xlabel("Velocity(m/sec")
mt.ylabel("Power(W)")
mt.show()
