from coneccao import Session

from bd import Loja

with Session() as session:
    loja=Loja (nome='carbiel',endereco='avenida paulista',gerente='Sophia')
    session.add(loja)
    session.commit()
    