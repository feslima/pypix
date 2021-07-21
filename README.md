This is a python package for generatic static PIX code used in money transfers in Brazil. It follows the version 2.3.0 of the [Manual de Padrões para Iniciação do PIX](https://www.bcb.gov.br/content/estabilidadefinanceira/pix/Regulamento_Pix/II_ManualdePadroesparaIniciacaodoPix_versao2-3-0.pdf).


This can be used for automation of [QR Code generation](https://github.com/lincolnloop/python-qrcode) to improve your software user experience.


# Installation
Just run:

```shell
pip install pypix
```

# Usage
```python
>>> from pypix import create_pix_string_code
>>> from decimal import Decimal
>>> receiver_params = {
... 'key': '12345678900', # This is an example CPF of an hypothetical receiver
... 'name': 'Hypothetical Receiv Name', # Must be less than 25 characters long.
... 'city': 'CITY RECEIVER', # all uppercase ASCII format. 15 characters max
... 'value': Decimal('12.34'), # Do not set this, if you don't want specify a value and leave up to payer to fill this in their PSP application (e.g. mobile or web banking app)
... }
>>> code = create_pix_string_code(**receiver_params)
>>> print(code)
00020126330014BR.GOV.BCB.PIX011112345678900520400005303986540512.345802BR5924Hypothetical Receiv Name6013CITY RECEIVER62070503***6304EA64

# If you want to generate a QR code
>>> from qrcode import make  # You need to install it before running this
>>> image = make(code)
>>> image.save('qrcode_pix.png')
```

## Demo
![](animation.gif)