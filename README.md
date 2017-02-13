# PFE--apolline

Apolline.py  
Basic calculation (max,min,avg,stdevp)

Interpolate.py Pipeline.py  
Different methods for Data Fitting

AjaxHandler.py AjaxHandlerCallback.py Look.py index.html   
AjaxHandler is a server. AjaxHandlerCallback is a callback function, when server receives the request, it will call it, and then it dispatches the command to the appropriate module. When run python AjaxHandlerCallback.py. It will call index.html. We can open localhost:8080. But it did not finish. I want it can call Look.py when it gets two parameters, and show result of Look.py. I can't link Javascript with Python.

data   
It contains the datas that rasp8 data collected in January. I divided them into three categories. Weekends (Saturday and Sunday) which should be smooth curves, day (08: 00 ~ 17: 30), night (17:30 ~ 08: 00). And Monday night is not the same as other days, because the day before is sunday, so it should be a smooth curve, and other days should be decline then be smooth
