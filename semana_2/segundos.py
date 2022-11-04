segundos_str = input("Por favor, entre com o número de segundos que deseja converter:  ")
total_segs = int(segundos_str)

horas = total_segs // 3600
dias = horas // 24
horas_restantes = horas % 24
segs_restantes = total_segs % 3600
minutos = segs_restantes // 60
segs_restantes_final = segs_restantes % 60

mensagem = ""

if dias > 1:
    mensagem += str(dias) + " dias"

if dias == 1:
    mensagem += str(dias) + " dia"

if horas_restantes > 0 and minutos == 0 and segs_restantes_final == 0 and dias > 0:
    mensagem += " e "

if horas_restantes > 0 and (minutos > 0 or segs_restantes_final > 0) and dias > 0:
    mensagem += ", "

if horas_restantes > 1:
    mensagem += str(horas_restantes) + " horas"

if horas_restantes == 1:
    mensagem += str(horas_restantes) + " hora"

if minutos > 0 and segs_restantes_final == 0 and horas_restantes > 0:
    mensagem += " e "

if minutos > 0 and segs_restantes_final > 0 and horas_restantes > 0:
    mensagem += ", "

if minutos > 1:
    mensagem += str(minutos) + " minutos"
    
if minutos == 1:
    mensagem += str(minutos) + " minuto"

if segs_restantes_final > 0 and minutos > 0:
    mensagem += " e "

if segs_restantes_final > 1:
    mensagem += str(segs_restantes_final) + " segundos"

if segs_restantes_final == 1:
    mensagem += str(segs_restantes_final) + " segundo"

#print (mensagem)

print(dias, "dias,", horas_restantes, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")
