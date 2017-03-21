from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseBadRequest

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
        htmlAnswer = "<h3> ERROR! Ha intentado dividir por cero </h3>"
        return HttpResponseBadRequest(htmlAnswer)

def sub(request, operando1, operacion, operando2):
        resultado = int(operando1) - int(operando2)
        htmlAnswer = "<p> El resultado--> " + operando1 + " " + operacion \
                    + " " + operando2 + " = " + str(resultado) + "</p>"
        return HttpResponse(htmlAnswer)
