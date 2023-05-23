from prefect import Flow
import pytz
import datetime

@Flow
def imprimirHora(timezone_name, format_string="%Y-%m-%d %H:%M:%S"):
    tz = pytz.timezone(timezone_name)
    print("Zona horaria", timezone_name)
    print("Hora:", datetime.datetime.now(tz).strftime(format_string))

def run():
    nombresZonas = ["US/Pacific", "US/Mountain", "US/Central", "US/Eastern", "Europe/London", "Asia/Tokyo", "America/Mexico_City"]
    formato = "%Y-%m-%d %H:%M:%S"
    for nombreZona in nombresZonas:
        imprimirHora(nombreZona, formato)
    
run()
