from coneccao import Session
from bd import Vendedor
from bd import Loja
with Session() as session:
    #loja=Loja (nome='carbiel',endereco='avenida paulista',gerente='Sophia')
    vendedor= Vendedor(nome='Querio Junior',Loja=1)
    session.add(vendedor)
    session.commit()
    print('registro realizado')