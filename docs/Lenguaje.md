# Elementos del Lenguaje

- Tipos de Datos
```
int
real
string
bool
```
- Constantes
```
30
30.0
.30
"hola"
```
- Operadores Algebraicos
```
+
-
*
/
```
- Operadores de Comparacion
```
<
>
<=
>=
==
!=
```
- Operadores Logicos
```
||
&&
!
```
- Asignaciones
```
<IDENT> = <CTE>;
<IDENT> = <CTE> + <IDENT>;
<IDENT> = <CTE> + <CTE>;
<IDENT> = <IDENT> + <IDENT>;
<IDENT> = <CTE> ++ <IDENT>;
<IDENT> = <CTE> ++ <CTE>;
<IDENT> = <OP_TERNARIO>;
```
- Comentarios
```
/* comentario */
/**** 
comentario
****/
```
- Entrada y Salida
```
out <CTE>;
out <IDENT>;
in <IDENT>;
```
- Declaraciones de Variables
```
var {
    <TYPE> <IDENT>, <IDENT>;
}
```
- Sentencia While
```
while <CONDICION> {
    <SENTENCIA>;
}
```
- Sentencia If
```
if <CONDICION> {
    <SENTENCIA>;
} else if <CONDICION> {
    <SENTENCIA>;
} else {
    <SENTENCIA>
}
```
- Between
```
between(<IDENT>, <EXP> : <EXP>);
```
- Operador Ternario
```
<CONDICION> ? <EXP> : <EXP>
```