from django.shortcuts import render
from django.http import HttpResponse

def suma(request, operando1, operacion, operando2):
    resultado = int(operando1) + int(operando2)
    htmlAnswer = '<p> El resultado--> ' + operando1 + " " + operacion \
                + " " + operando2 + " = " + str(resultado) + "</p>"
    return HttpResponse(htmlAnswer)

def mult(request, operando1, operacion, operando2):
    resultado = int(operando1) * int(operando2)
    htmlAnswer = "<p> El resultado--> " + operando1 + " " + operacion \
                + " " + operando2 + " = " + str(resultado) + "</p>"
    return HttpResponse(htmlAnswer)

def div(request, operando1, operacion, operando2):
    try:
        resultado = int(operando1) / int(operando2)
        htmlAnswer = "<p> El resultado--> " + operando1 + " " + operacion \
                    + " " + operando2 + " = " + str(resultado) + "</p>"
        return HttpResponse(htmlAnswer)
    except ZeroDivisionError:
        hmtlAnswer = "<h3> ERROR! Ha intentado dividir por cero </h3>"
        return HttpResponse.HttpResponseGone(htmlAnswer)

def sub(request, operando1, operacion, operando2):
        resultado = int(operando1) - int(operando2)
        htmlAnswer = "<p> El resultado--> " + operando1 + " " + operacion \
                    + " " + operando2 + " = " + str(resultado) + "</p>"
        return HttpResponse(htmlAnswer)
