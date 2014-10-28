import csv
import random

param = raw_input("PARAMETROS: xs ys alfa iteraciones tolerancia \n")
params = param.split(' ')
arch_xs = params[0]
arch_ys = params[1]
alfa = float(params[2])
iter = int(params[3])
tol = float(params[4])

"""
arch_xs = "xs.csv"
arch_ys = "ys.csv"
alfa = 0.01
iter = 1000
tol = 0.0001
   """ 

thetas = []
xgen = []
thetas_optimas=[]
#ABRIR ARCHIVOS XS, NUMERO DE COLUMNAS Y FILAS
f = open(arch_xs)
lns = csv.reader(f)
xs = []
i=0
ii = 0
lin = 0

for line in lns:
    for x in line:
        xs.insert(i, float(x))
        i=i+1
    ii = len(line)
    lin = lin +1
    

##las xs promedio para la hsub thta
r=0   
pp = 0 
for xt in range(0, ii):
    for yt in range (0, lin):
        pp = pp+xs[r]
        r = r+ii
        
    tot = pp / lin
    xgen.insert(xt, tot)
    r=xt+1
    pp=0
    

#THETAS ramdom        
for th in range(0, ii+1):
    thetas.insert(th, float(random.randint(1, 5)))

#ARCHIVO DE LAS YS    
f = open(arch_ys)
lns = csv.reader(f)
ys = []
i=0
for line in lns:
    for x in line:
        ys.insert(i, float(x))
        i=i+1
    
#---------------------FUNCIONES-----------FUNCIONES---------------------
def sumatoria(valTheta, isum): #theta en la q se esta, i de la sumatoria
    res = float(0.0)
    ini = 0
    posx = 0
    filas= lin
    col = ii
    for th in thetas:
        if ini == 0:
            res = th
            ini = 1
        else:
            res = res + th * xgen[posx]
            posx = posx+1
    
    res = res - ys[isum-1]
    
    if valTheta>0 :
        valTheta = valTheta -1
        pos_x_de_theta_en_i = col*(isum-1)+valTheta 
        res = res * xs[pos_x_de_theta_en_i]
        
    return res    


def resultado_theta(theta):
    m= lin
    col = ii
    res_thet = 0
    total=0
    for iss in range(1,m+1):
        res_thet = res_thet + sumatoria(theta, iss)
        
    total = res_thet / m
    total = alfa * total
    total = thetas[theta]-total
    
    return total  

convergidas=[]
for isst in range(0,ii+1):
    convergidas.insert(isst, 0)
    

def buscar_thetas():
    m= lin
    num_x = ii
    s = 0
    for xxs in range(0,num_x+1):
        thetass = resultado_theta(xxs)
        
        print "--", xxs, num_x, len(thetas_optimas)
        for sstt in thetas_optimas:
            print sstt
        if len(thetas_optimas)<num_x+1:
            thetas_optimas.insert(xxs, thetass)
            print "a optimas ", xxs, thetass
            
        else:
            print "else ", xxs, num_x, len(thetas_optimas)
            for sstt in thetas_optimas:
                print sstt
            
            ptr = thetas_optimas[xxs]
            tols = ptr - thetass
            
            print "tols ", tols
            if tols <= tol or ptr > thetass:
                print "cambio de thetas op", thetass
                thetas_optimas[xxs] = thetass
                if tols <= tol and convergidas[xxs]==0:
                    if ptr != thetass:
                        convergidas[xxs] = 1
                        print "convergio en ", xxs, tols
                else:
                    rd = random.random()
                    vt = thetas[xxs]- rd
                    if vt < 0 :
                        vt = thetas[xxs]+ rd
                    
                    thetas[xxs] = vt
                    
                    print "cambio de thetas  en", xxs, thetas[xxs]
            else:
                    rd = random.random()
                    vt = thetas[xxs]- rd
                    if vt < 0 :
                        vt = thetas[xxs]+ rd
                    
                    thetas[xxs] = vt
                    print "cambio afuera de thetas  en", xxs, thetas[xxs]
                    
                    
            
                 
    

            
for it in range(1, iter+1):
    buscar_thetas()
    mt=0
    for sst in convergidas:
        mt = mt + sst
    
    print "suuuuuuuuma   -------------------------------", mt
    if mt == ii+1:
        print "convergieron"
        break
    
    print "fiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii", it
    
    
    
   
#PRUEBAS---------------------------------------
for ss in convergidas:
    print ss
    
print 
                    
        
print "---------- thetas optimas----"

for s in thetas_optimas:
    print s
    


    
         