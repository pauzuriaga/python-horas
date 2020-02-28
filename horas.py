from datetime import datetime
 
hora1 = datetime.strptime("22:00:00", "%X").time()
hora2 = datetime.strptime("00:44:00", "%X").time()
hora_act = datetime.now().time()
 
if hora2 > hora1:
    if hora_act > hora1 and hora_act < hora2:
        print ("SI")
    else:
        print ("NO")
else:
    if hora_act > hora1 or hora_act < hora2:
        print ("SI")
    else:
        print ("NO")
