# Parametros COE
TAMANO_COE = 128  # Indica el tamaño del vector (potencias de 2)
BITS_POR_NUMERO = 16  # Indica la cantidad de bits por cada elemento
RUTA_COE = ['output', 'datos.coe']  # Ruta donde se guarda el archivo.
# Parametros TIM
RUTA_PROGRAMA = ['input', 'programa.txt']  # Ruta del archivo para traducir.
INSTRUCCIONES = {
    # "MNEMO":   ["descripcion", "formato", "opcode"]
    # Instrucciones registradas
    "MOVA": ["Mover A",     "RD,RA",    "0000000"],
    "INC":  ["Incrementar", "RD,RA",    "0000001"],
    "ADD":  ["Sumar",       "RD,RA,RB", "0000010"],
    "SUB":  ["Restar",      "RD,RA,RB", "0000101"],
    "DEC":  ["Decrementar", "RD,RA",    "0000110"],
    "AND":  ["AND",         "RD,RA,RB", "0001000"],
    "OR":   ["OR",          "RD,RA,RB", "0001001"],
    "XOR":  ["XOR",         "RD,RA,RB", "0001010"],
    "NOT":  ["NOR",         "RD,RA",    "0001011"],
    "MOVB": ["Mover B",     "RD,RB",    "0001100"],
    "SHR":  ["Shift Right", "RD,RB",    "0001101"],
    "SHL":  ["Shift Left",  "RD,RB",    "0001110"],
    # Instrucciones inmediatas
    "LDI": ["Carga Inmediata", "RD,OP",    "1001100"],
    "ADI": ["Suma Inmediata",  "RD,RA,OP", "1000010"],
    # Instrucciones de Data Memory
    "LD": ["Cargar",  "RD,RA", "0010000"],
    "ST": ["Guardar", "RA,RB", "0100000"],
    # Instrucciones de branch
    "BRZ": ["Branch en Cero",     "RA,AD", "1100000"],
    "BRN": ["Branch en Negativo", "RA,AD", "1100001"],
    "JMP": ["Jump",               "RA",    "1110000"],
    # Instrucciones personalizadas
}
