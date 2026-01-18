"""Programa elemental para verificar funcionalidad."""

def suma(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def main() -> None:
    """Ejecuta una demostración básica."""
    valor_a = 2
    valor_b = 3
    resultado = suma(valor_a, valor_b)
    print(f"{valor_a} + {valor_b} = {resultado}")


if __name__ == "__main__":
    main()
