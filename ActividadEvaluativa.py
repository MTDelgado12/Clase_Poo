DineroAnual=int(input("Ingrese el dinero anual 😊: "))

class comision:
    def __init__(self,SumaAnual):
        self.SumaAnual=SumaAnual
    
    def libro(self):
        self.libros=int(self.SumaAnual*0.5)
        print(f"La suma anual destinada para libros es: $ {self.libros:,.0f}  🤑")
        
    def transporteU(self):
        boletostranspor=0
        self.transporte=int(self.SumaAnual*0.2)
        self.DineroTotaltrans=self.transporte
        while self.transporte >=2:
            boletostranspor+=1
            self.transporte-=2
        print(f"El dinero anual de pasajes de transporte $ {self.DineroTotaltrans:,.0f} le alcanza para {boletostranspor:,.0f} boletos para pasajes 🤑")
            
        
    def entradascine(self):
        boletoscine=0
        self.cine=int(self.SumaAnual*0.2)
        self.DineroTotalcine=self.cine
        while self.cine >=5:
            boletoscine+=1
            self.cine-=5
        print(f"El dinero anual de entradas a cine $ {self.DineroTotalcine:,.0f}  le alcanza para {boletoscine:,.0f} boletos para entradas a cine🤑")
    
    def madres(self):
        self.sobrante=self.SumaAnual-self.libros-self.DineroTotaltrans-self.DineroTotalcine
        print(f"El dinero restante para el regalo del dia de las madres es $ {self.sobrante:,.0f} 🤑")
        
    def DineroTotal(self):
        años = int(input("Años que estuvo el sobrino: "))
        self.DineroRecibido = self.SumaAnual * años
        print(f"El sobrino estudio {años} años y recibio un total de $ {self.DineroRecibido:,.0f}")

sobrino=comision(DineroAnual)
sobrino.libro()
sobrino.transporteU()
sobrino.entradascine()
sobrino.madres()
sobrino.DineroTotal() 