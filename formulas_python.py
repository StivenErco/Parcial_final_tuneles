class CalculosTuneles:
        
    def __init__(self):
        self.L = 2200  # [m]
        self.At = 91  # [m2]
        self.Pt = 36  # [m]
        self.V = 4  # [m/s]
        self.rho_0 = 1.225  # [Kg/m3]
        self.h = 700  # [m]
        self.f = 0.03  # [-]
        self.Cd2 = 0.65
        self.Av2 = 6  # [m2]
        self.nc1 = 2  # [und] - número de ventiladores tipo 1
        self.nt1 = 2  # [und] - número de turbinas tipo 1
        self.nc2 = 4  # [und] - número de ventiladores tipo 2
        self.nt2 = 3  # [und] - número de turbinas tipo 2

    def calcular_sheet1(self):
                
        # Valores intermedios
        P0 = 1.01325 * 10**5
        Vv1 = 60 * 10 / 36
        Vv1_alt = 50 * 10 / 36
        Vv2 = ((4 * 40 + 60 * 3) / 7) * 10 / 36
        Vv2_alt = 40 * 10 / 36
        rho = self.rho_0 * (1 - 6.883 * 10**-6 * self.h) ** 4.256
        P = P0 * (1 - 6.883 * 10**-6 * self.h) ** 5.256
        
        # Resultados finales 
        Pi0 = 0.75 * rho * self.V**2
        Pdrag2 = (
            self.Cd2 * 0.5 * (self.Av2 / self.At) * rho *
            ((self.nc1 + self.nt1) * (Vv1 + self.V)**2 -
             (self.nc2 + self.nt2) * abs(Vv2 - self.V) * (Vv2 - self.V))
        )
        DeltaP = 0.5 * rho * 15**2 - 0.5 * rho * 10**2
        Pl = 0.5 * self.f * self.L * (self.Pt / (4 * self.At)) * rho * self.V**2
        Pi = Pl - DeltaP + Pi0 + Pdrag2
        Tt = Pi * self.At / 1000

        valores_intermedios = {
            'P0': P0,
            'Vv1': Vv1,
            'Vv1_alt': Vv1_alt,
            'Vv2': Vv2,
            'Vv2_alt': Vv2_alt,
            'rho': rho,
            'P': P,
        }
        
        resultados = {
            'Pi0': Pi0,
            'Pdrag2': Pdrag2,
            'DeltaP': DeltaP,
            'Pl': Pl,
            'Pi': Pi,
            'Tt': Tt,
        }
        
        return {
            'valores_intermedios': valores_intermedios,
            'resultados': resultados
        }


def main():
        
    print("=" * 80)
    print("CONVERSIÓN DE FÓRMULAS EXCEL A PYTHON - PROYECTO TÚNELES")
    print("=" * 80)
    
    calc = CalculosTuneles()
    
    print("\n--- PARÁMETROS DE ENTRADA ---\n")
    print(f"Longitud del túnel (L): {calc.L} m")
    print(f"Área transversal (At): {calc.At} m²")
    print(f"Perímetro (Pt): {calc.Pt} m")
    print(f"Velocidad del aire (V): {calc.V} m/s")
    print(f"Densidad del aire a nivel del mar (ρ₀): {calc.rho_0} kg/m³")
    print(f"Altura (h): {calc.h} m")
    print(f"Coeficiente de fricción (f): {calc.f}")
    print(f"Coeficiente de arrastre 2 (Cd2): {calc.Cd2}")
    print(f"Área de ventilador 2 (Av2): {calc.Av2} m²")
    print(f"Número de ventiladores tipo 1 (nc1): {calc.nc1}")
    print(f"Número de turbinas tipo 1 (nt1): {calc.nt1}")
    print(f"Número de ventiladores tipo 2 (nc2): {calc.nc2}")
    print(f"Número de turbinas tipo 2 (nt2): {calc.nt2}")
    
    
    print("\n" + "=" * 80)
    print("RESULTADOS - HOJA ÚNICA")
    print("=" * 80 + "\n")
    
    resultados_completos = calc.calcular_sheet1()
    
    print("--- VALORES INTERMEDIOS (necesarios para llegar a los resultados) ---\n")
    for variable, valor in resultados_completos['valores_intermedios'].items():
        print(f"{variable:20s}: {valor:15.6f}")
    
    print("\n--- RESULTADOS FINALES ---\n")
    for variable, valor in resultados_completos['resultados'].items():
        print(f"{variable:20s}: {valor:15.6f}")



if __name__ == "__main__":
    main()
