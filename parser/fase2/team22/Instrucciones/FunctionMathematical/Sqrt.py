import math
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class Sqrt(Instruccion):
    def __init__(self, valor, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.NUMERIC),linea,columna,strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        resultado = self.valor.ejecutar(tabla,arbol)
        if self.valor.tipo.tipo != Tipo_Dato.SMALLINT and self.valor.tipo.tipo != Tipo_Dato.INTEGER and self.valor.tipo.tipo != Tipo_Dato.BIGINT and self.valor.tipo.tipo != Tipo_Dato.DECIMAL and self.valor.tipo.tipo != Tipo_Dato.NUMERIC and self.valor.tipo.tipo != Tipo_Dato.REAL and self.valor.tipo.tipo != Tipo_Dato.DOUBLE_PRECISION:
            error = Excepcion('42883',"Semántico","No existe la función sqrt("+self.valor.tipo.toString()+")",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if resultado < 0:
            error = Excepcion('42883',"Semántico","No se puede calcular la raíz cuadrada un de número negativo",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error
        if isinstance(resultado,int):
            return int(math.sqrt(resultado))
        else:
            return math.sqrt(resultado)
        
    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"SQRT(" + str(self.valor.generar3D(tabla, arbol)) + ")\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code