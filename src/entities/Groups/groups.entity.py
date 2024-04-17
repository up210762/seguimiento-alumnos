from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, defaultload
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Scores(Base):
    __tablename__ = "Calificaciones"

    Matricula: Mapped[str] = mapped_column(ForeignKey("Alumnos.Matricula"))
    MateriasId: Mapped[int] = mapped_column(ForeignKey("Materias.Id"))
    GruposId: Mapped[int] = mapped_column(ForeignKey("Grupos.Id"))
    CalificacionFinal: Mapped[float]
    Estado: Mapped[int] = mapped_column(ForeignKey("EstadoAlumno.Id"))

    matricula: Mapped[List["Students"]] = relationship(
        back_populates="Matricula", cascade="all, delete-orphan"
    )
    materia: Mapped[List["Subjects"]] = relationship(
        back_populates="Id", cascade="all, delete-orphan"
    )
    grupo: Mapped[List["Groups"]] = relationship(
        back_populates="Id", cascade="all, delete-orphan"
    )
    estado: Mapped[List["StudentsState"]] = relationship(
        back_populates="Id", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Scores(Matricula={self.Matricula!r}, MateriaId={self.MateriaId!r}, GrupoId={self.GrupoId!r}, CalificacionFinal={self.CalificacionFinal!r}, Estado={self.Estado!r})"
    

class Students(Base):
    __tablename__ = "Alumnos"

    Matricula: Mapped[int] = mapped_column(primary_key=True)
    Nombre: Mapped[str]
    Activo: Mapped[bool]

    calificacion: Mapped["Scores"] = relationship(back_populates="Matricula")

    def __repr__(self) -> str:
        return f"Alumnos(Matricula={self.Matricula!r}, Nombre={self.Nombre!r}, Activo={self.Activo!r})"


class Groups(Base):
    __tablename__ = "Grupos"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Grupo: Mapped[str]
    Activo: Mapped[bool]

    Calificacion: Mapped["Scores"] = relationship(back_populates="GrupoId")

    def __repr__(self) -> str:
        return f"Groupos(Id={self.Id!r}, Grupo={self.Grupo!r}, Activo={self.Activo!r})"


class StudentsState(Base):
    __tablename__ = "EstadoAlumno"

    Id: Mapped[int] = mapped_column(primary_key=True)
    Estado: Mapped[str]
    Activo: Mapped[bool]

    Calificacion: Mapped["Scores"] = relationship(back_populates="Estado")

    def __repr__(self) -> str:
        return f"EstadoAlumnos(Id={self.Id!r}, Estado={self.Estado!r}, Activo={self.Activo!r})"


class Subjects(Base):
    __tablename__ = "Materias"

    Id: Mapped[int] = mapped_column(primary_key=True)
    NombreMateria: Mapped[str]
    Activo: Mapped[bool]

    Calificacion: Mapped["Scores"] = relationship(back_populates="MateriaId")

    def __repr__(self) -> str:
        return f"Materias(Id={self.Id!r}, NombreMateria={self.NombreMateria!r}, Activo={self.Activo})"