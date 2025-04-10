#include <iostream>
using namespace std;

/**
 * \brief Función para sumar dos números
 *
 * Esta función toma dos números enteros y devuelve su suma.
 *
 * \param a Primer número
 * \param b Segundo número
 * \return La suma de los dos números
 */
int sumar(int a, int b) {
    return a + b;
}

/**
 * \brief Función para restar dos números
 *
 * Esta función toma dos números enteros y devuelve su resta.
 *
 * \param a Primer número
 * \param b Segundo número
 * \return La resta de los dos números
 */
int restar(int a, int b) {
    return a - b;
}

/**
 * \brief Función para multiplicar dos números
 *
 * Esta función toma dos números enteros y devuelve su producto.
 *
 * \param a Primer número
 * \param b Segundo número
 * \return El producto de los dos números
 */
int multiplicar(int a, int b) {
    return a * b;
}

/**
 * \brief Función para dividir dos números
 *
 * Esta función toma dos números enteros y devuelve su cociente.
 * Si el divisor es cero, devuelve un mensaje de error.
 *
 * \param a Primer número
 * \param b Segundo número
 * \return El cociente de los dos números, o un mensaje de error
 */
double dividir(int a, int b) {
    if (b == 0) {
        cout << "Error: División por cero" << endl;
        return 0;
    }
    return static_cast<double>(a) / b;
}

/**
 * @brief Función main
 * 
 * Función para correr el código 
 * 
 * @return 0
 */
int main() {
    int num1 = 10, num2 = 5;

    cout << "Suma: " << sumar(num1, num2) << endl;
    cout << "Resta: " << restar(num1, num2) << endl;
    cout << "Multiplicación: " << multiplicar(num1, num2) << endl;
    cout << "División: " << dividir(num1, num2) << endl;

    return 0;
}