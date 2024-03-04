def function(x):
    return x**4 + 2*x**2 + 1

def tem_raiz_real(a,b,c):
    if (-b/a > 0 and c/a > 0):
        return 1;
    else:
        return 0;

# a, b, c são os coeficientes de x**4, x**2 e 1 da equação biquadrada
if(tem_raiz_real(1,2,1)):
    print("Tem raiz real")
else:
    print("Não tem raiz real")
