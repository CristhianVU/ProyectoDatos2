import TablaDeSimbolos
import re
class AnalizadorSemantico:
    def __init__(self, fuente):
       self.fuente =fuente
    def analizar_codigo(self):
        tabla_global = TablaDeSimbolos.TablaDeSimbolos()
        tipos_validos = {"void", "int", "float", "string"}
        tabla_actual = tabla_global
        dentro_de_funcion = False

        with open(self.fuente, 'r', encoding='utf-8') as file:
            lineas = file.readlines()

        for numero_linea, linea in enumerate(lineas, 1):
            linea = linea.strip()

            if not linea or linea.startswith("if") or linea.startswith("while") or linea.startswith("}"):
                dentro_de_funcion = False
                continue

            tokens = linea.split()

            matchfuncion = re.search(r'\b(int|string|void|float)\s+([a-zA-Z]\w)\s*\((.*)\)\s*{', linea)
            if not matchfuncion:
                if tokens[0] in tipos_validos:
                    tipo, nombre_var = tokens[0], tokens[1]
                    if tabla_actual.buscar(nombre_var):
                        print(f"Error – Línea {numero_linea}: Variable '{nombre_var}' ya declarada")
                    else:
                        tabla_actual.insertar(nombre_var, tipo)


            if dentro_de_funcion and ")" in linea:
                dentro_de_funcion = False
                continue

            if dentro_de_funcion:

                for token in tokens:
                    if ',' in token:

                        parametros = token.split(',')
                        for parametro in parametros:
                            tipo_param, nombre_param = parametro.strip().split()
                            if tipo_param in tipos_validos:
                                tabla_funcion.insertar(nombre_param, tipo_param)
                                print(f"Agregando parámetro '{nombre_param}' de tipo '{tipo_param}' a la función '{nombre_funcion}'")
                            else:
                                print(f"Error – Línea {numero_linea}: Tipo de parámetro no válido '{tipo_param}'")
                    else:

                        tipo_param, nombre_param = token.strip().split()
                        if tipo_param in tipos_validos:
                            tabla_funcion.insertar(nombre_param, tipo_param)
                            print(f"Agregando parámetro '{nombre_param}' de tipo '{tipo_param}' a la función '{nombre_funcion}'")
                        else:
                            print(f"Error – Línea {numero_linea}: Tipo de parámetro no válido '{tipo_param}'")
                continue

            match_funcion = re.search(r'\b(int|string|void|float)\s+([a-zA-Z]\w*)\s*\((.*)\)\s*{', linea)
            if match_funcion:
                tipo_funcion = match_funcion.group(1)
                nombre_funcion = match_funcion.group(2)
                dentro_de_funcion = True


                if tabla_actual.buscar(nombre_funcion):
                    _, tabla_funcion = [v for k, v in tabla_actual.tabla[tabla_actual._hash(nombre_funcion)] if k == nombre_funcion][0]
                else:
                    tabla_funcion = TablaDeSimbolos.TablaDeSimbolos(tamaño=100, tabla_padre=tabla_actual)
                    tabla_actual.insertar(nombre_funcion, (tipo_funcion, tabla_funcion))


                parametros_raw = match_funcion.group(3)
                parametros = parametros_raw.split(',')
                for parametro in parametros:
                    tipo_param_nombre_param = parametro.strip().split()

                    if len(tipo_param_nombre_param) >1:
                        tipo_param, nombre_param = parametro.strip().split()
                        if tipo_param in tipos_validos:

                            tabla_actual.insertar(nombre_param, tipo_param)

                        else:
                            print(f"Error – Línea {numero_linea}: Tipo de parámetro no válido '{tipo_param}'")

                continue

            if '=' in tokens and  tabla_actual.buscar(tokens[0]):
                index_equal = tokens.index('=')

                continue

            if tokens[0] not in tipos_validos and not tabla_actual.buscar(tokens[0]):
                print(f"Error – Línea {numero_linea}: Variable '{tokens[0]}' no declarada")

