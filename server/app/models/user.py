from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class UserModel(Base):
    """
    Representa a tabela 'pessoa' no banco de dados.

    Campos obrigatórios (preenchidos no cadastro):
        nome_usuario, email, senha, telefone

    Campos opcionais (preenchidos na edição de perfil — outro membro):
        nome, sobrenome, biografia, caminho_foto

    ATENÇÃO: 'senha' armazena o HASH bcrypt, nunca a senha pura.
    """
    __tablename__ = "pessoa"

    usuario: Mapped[str] = mapped_column(String, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    senha: Mapped[str] = mapped_column(String)
    telefone: Mapped[str] = mapped_column(String, unique=True)
    nome: Mapped[str] = mapped_column(String)
    sobrenome: Mapped[str | None] = mapped_column(String)
    biografia: Mapped[str | None] = mapped_column(String)
    caminho_foto: Mapped[str | None] = mapped_column(String)