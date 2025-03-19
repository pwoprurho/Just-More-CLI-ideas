import matplotlib.pyplot as plt
def co_2_emissions():
# Calculating Co_2 emissions for Petrol fuel 
        Pms_MRP= 0.74*0.84*3.6667
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = 20.72, 18.33, 19.130, 17.830, 15.760, 18.370, 25.070, 30.380, 42.610, 43.120
        Pms1 = p1 * Pms_MRP
        Pms2 = p2 * Pms_MRP
        Pms3 = p3 * Pms_MRP
        Pms4 = p4 * Pms_MRP
        Pms5 = p5 * Pms_MRP
        Pms6 = p6 * Pms_MRP
        Pms7 = p7 * Pms_MRP
        Pms8 = p8 * Pms_MRP
        Pms9 = p9 * Pms_MRP
        Pms10 = p10 * Pms_MRP
        Pms = [Pms1, Pms2, Pms3, Pms4, Pms5, Pms6, Pms7, Pms8, Pms9, Pms10]
        
# Calculating Co_2 Emissions for Diseal fuel
        Ago_MPR = 0.85 * 0.86 * 3.6667
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = 3.58, 4.69, 2.27, 2.98, 1.48, 0.66, 1.78, 3.46, 2.73, 2.98
        Ago1 = a1*Ago_MPR
        Ago2 = a2 * Ago_MPR
        Ago3 = a3 * Ago_MPR
        Ago4 = a4 * Ago_MPR
        Ago5 = a5 * Ago_MPR
        Ago6 = a6 * Ago_MPR
        Ago7 = a7 * Ago_MPR
        Ago8 = a8 * Ago_MPR
        Ago9 = a9 * Ago_MPR
        Ago10 = a10 * Ago_MPR
        Ago = [Ago1, Ago2, Ago3, Ago4, Ago5, Ago6, Ago7, Ago8, Ago9, Ago10]
# Calculating the Co_2 Emissions for Kerosine fuel
        Kkh_MRP = 0.817 * 0.86 * 3.6667
        k1, k2, k3, k4, k5, k6, k7, k8, k9, k10 = 7.44, 7.39, 8.04, 9.51, 8.06, 5.02, 1.98, 1.67, 1.23, 0.26 
        K1 = k1 * Kkh_MRP
        K2 = k2 * Kkh_MRP
        K3 = k3 * Kkh_MRP
        K4 = k4 * Kkh_MRP
        K5 = k5 * Kkh_MRP
        K6 = k6 * Kkh_MRP
        K7 = k7 * Kkh_MRP
        K8 = k8 * Kkh_MRP
        K9 = k9 * Kkh_MRP
        K10 = k10 * Kkh_MRP
        KKH = [K1, K2, K3, K4, K5, K6, K7, K8, K9, 10]
        
                
        y = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
        plt.bar(y, Pms, color= "b", align="edge")
        plt.bar(y, KKH, color= "g", align="center")
        plt.bar(y, Ago, color="r", align="edge")
        plt.ylabel("CO_2 Emissions")
        plt.xlabel("Year of study")                
        plt.show()
        
if __name__ == "__main__":
   co_2_emissions()