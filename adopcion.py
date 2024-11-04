import pyodbc

def conectar_bd():
    try:
        conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=AdopcionAnimales;'
    'UID=tu_usuario;'
    'PWD=tu_contraseña'
)

        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None


def registrar_animal(especie, raza, edad, sexo, estado_salud):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            consulta = "INSERT INTO Animales (especie, raza, edad, sexo, estado_salud) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(consulta, (especie, raza, edad, sexo, estado_salud))
            conexion.commit()
            print("Animal registrado exitosamente.")
        except Exception as e:
            print(f"Error al registrar el animal: {e}")
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo conectar a la base de datos.")

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class RegistroAnimalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Animales")
        self.setGeometry(100, 100, 300, 200)

        # Elementos de la interfaz
        self.especie_label = QLabel("Especie:")
        self.especie_input = QLineEdit()

        self.raza_label = QLabel("Raza:")
        self.raza_input = QLineEdit()

        self.edad_label = QLabel("Edad:")
        self.edad_input = QLineEdit()

        self.sexo_label = QLabel("Sexo (M/F):")
        self.sexo_input = QLineEdit()

        self.estado_salud_label = QLabel("Estado de Salud:")
        self.estado_salud_input = QLineEdit()

        self.registrar_btn = QPushButton("Registrar")
        self.registrar_btn.clicked.connect(self.registrar_animal)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.especie_label)
        layout.addWidget(self.especie_input)
        layout.addWidget(self.raza_label)
        layout.addWidget(self.raza_input)
        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_input)
        layout.addWidget(self.sexo_label)
        layout.addWidget(self.sexo_input)
        layout.addWidget(self.estado_salud_label)
        layout.addWidget(self.estado_salud_input)
        layout.addWidget(self.registrar_btn)

        self.setLayout(layout)

    def registrar_animal(self):
        especie = self.especie_input.text()
        raza = self.raza_input.text()
        try:
            edad = int(self.edad_input.text())
        except ValueError:
            QMessageBox.warning(self, "Entrada inválida", "La edad debe ser un número.")
            return
        sexo = self.sexo_input.text().upper()
        estado_salud = self.estado_salud_input.text()

        if sexo not in ["M", "F"]:
            QMessageBox.warning(self, "Entrada inválida", "El sexo debe ser 'M' o 'F'.")
            return

        # Llamar a la función para registrar el animal
        registrar_animal(especie, raza, edad, sexo, estado_salud)

app = QApplication(sys.argv)
ventana = RegistroAnimalApp()
ventana.show()
sys.exit(app.exec_())
