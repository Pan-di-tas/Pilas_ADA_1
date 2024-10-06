
class Evaluaciones_Aritmeticas:

    def evaluar_posfija(self, expresion):
        pila1 = []
        
        for elemento in expresion:
            if elemento.isdigit():  
                pila1.append(int(elemento))
            else:
                operando2 = pila1.pop()
                operando1 = pila1.pop()
                
                if elemento == '+':
                    pila1.append(operando1 + operando2)
                elif elemento == '-':
                    pila1.append(operando1 - operando2)
                elif elemento == '*':
                    pila1.append(operando1 * operando2)
                elif elemento == '/':
                    pila1.append(operando1 / operando2)
        
        return pila1[0]

    def evaluar_prefija(self, expresion):
        pila2 = []
        
        for elemento in expresion[::-1]:
            if elemento.isdigit(): 
                pila2.append(int(elemento))
            else:
                operando1 = pila2.pop()
                operando2 = pila2.pop()
                
                if elemento == '+':
                    pila2.append(operando1 + operando2)
                elif elemento == '-':
                    pila2.append(operando1 - operando2)
                elif elemento == '*':
                    pila2.append(operando1 * operando2)
                elif elemento == '/':
                    pila2.append(operando1 / operando2)
        
        return pila2[0]

    def Impresiones(self):
        expresion_prefija = "-+53*82"
        resultado_prefija = self.evaluar_prefija(expresion_prefija)
        print(f"Resultado de la expresión prefija: {resultado_prefija}")
        
        expresion_posfija = "53+82-*"
        resultado_posfija = self.evaluar_posfija(expresion_posfija)
        print(f"Resultado de la expresión posfija: {resultado_posfija}")

key = Evaluaciones_Aritmeticas()
key.Impresiones()
