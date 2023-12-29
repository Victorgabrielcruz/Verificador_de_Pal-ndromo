# Verificador_de_Pal-ndromo

## Função `menu()`

A função `menu()` exibe um menu simples para o usuário e retorna um valor booleano indicando se o programa deve continuar ou não.

### Parâmetros:
Nenhum.

### Retorno:
- `True` se o usuário escolher continuar.
- `False` se o usuário escolher não continuar.

## Função `entrada()`

A função `entrada()` solicita ao usuário que insira uma frase para verificação e retorna a frase inserida.

### Parâmetros:
Nenhum.

### Retorno:
Uma string contendo a frase inserida pelo usuário.

## Função `comparador(frase)`

A função `comparador(frase)` recebe uma string (`frase`) e verifica se ela é um palíndromo, ou seja, se ela permanece a mesma quando lida de trás para frente.

### Parâmetros:
- `frase`: Uma string contendo a frase a ser verificada.

### Retorno:
- `True` se a frase for um palíndromo.
- `False` se a frase não for um palíndromo.

## Programa Principal

O programa principal utiliza um loop `while` para continuar a execução enquanto o usuário escolher continuar. Ele chama a função `entrada()` para obter a frase do usuário, em seguida, chama a função `comparador(frase)` para verificar se a frase é um palíndromo. O resultado é exibido ao usuário, indicando se a frase é ou não um palíndromo. O loop é controlado pela função `menu()`.

### Parâmetros:
Nenhum.

### Fluxo de Execução:
1. Solicita ao usuário uma frase através da função `entrada()`.
2. Verifica se a frase é um palíndromo usando a função `comparador(frase)`.
3. Exibe se a frase é ou não um palíndromo.
4. Pergunta ao usuário se deseja continuar usando a função `menu()`.
5. Repete o processo se o usuário escolher continuar.

## Autor
- Víctor Gabriel Cruz Pereira
