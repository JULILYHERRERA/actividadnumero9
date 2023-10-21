

class DatosMeteorologicos :
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo:str = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        datos=[]
        with open("datos.txt", "r")as  archivo:
            for linea in archivo:
                if "Temperatura" in  linea:
                    temperaturas.append(float(linea.split(":")[1].strip()))
                    tem_promedio= sum(temperaturas)/len(temperaturas)
                    datos.append(linea.strip)
                    return "la temperatura promedio seria:",tem_promedio
                    
                if "Humedad" in  linea:
                    humedades.append(float(linea.split(":")[1].strip()))
                    hum_promedio= sum(humedades)/len(humedades)
                    datos.append(linea.strip)

                    return "la humedad promedio seria:",hum_promedio

                if "Presión" in  linea:
                    presiones.append(float(linea.split(":")[1].strip()))
                    pre_promedio= sum(presiones)/len(presiones)
                    datos.append(linea.strip)
                   
                    return "la presión promedio seria:",pre_promedio

                if "Velocidad" in  linea:
                    velocidades.append(float(linea.split(":")[1].strip()))
                    velo_promedio= sum(velocidades)/len(velocidades)
                    datos.append(linea.strip)

                    return "la velocidad promedio seria:",velo_promedio

            # no supe hacer lo otro:C, como yo hago el codigo en otra parte y luego lo paso ps alla no me dio y la vdd no supe #
