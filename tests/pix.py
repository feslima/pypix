from decimal import Decimal
from typing import Union

import pytest
from src.pypix import create_pix_string_code


@pytest.mark.parametrize(['key', 'name', 'city', 'value', 'expected'], [
    ('123e4567-e12b-12d1-a456-426655440000', 'Fulano de Tal', 'BRASILIA', Decimal('0.50'),
     ("00020126580014BR.GOV.BCB.PIX0136123e4567-e12b-12d1-a456-426655440000"
     "52040000530398654040.505802BR5913Fulano de Tal6008BRASILIA62070503***63044BBE")),
    ('12345678900', 'Hypothetical Receiv Name', 'CITY RECEIVER', Decimal('12.34'),
     ("00020126330014BR.GOV.BCB.PIX011112345678900520400005303986540512.34"
      "5802BR5924Hypothetical Receiv Name6013CITY RECEIVER62070503***6304EA64"))
])
def test_create_code(key: str, name: str, city: str,
                     value: Union[Decimal, None], expected: str):
    assert create_pix_string_code(key, name, city, value=value) == expected
