from main import calcular_faturamento
import pytest

# faturamento
@pytest.mark.faturamento
def test_calcular_faturamento():
    assert calcular_faturamento() > 0