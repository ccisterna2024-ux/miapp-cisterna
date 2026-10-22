import os
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from plyer import notification

class MainScreen(MDScreen):
    def guardar_texto(self):
        # Captura del texto desde la ID definida en el KV
        texto_ingresado = self.ids.input_texto.text.strip()
        if not texto_ingresado:
            return

        # Persistencia en JSON
        app_dir = MDApp.get_running_app().user_data_dir
        json_path = os.path.join(app_dir, "datos.json")

        datos = {"texto": texto_ingresado}

        try:
            with open(json_path, "w", encoding="utf-8") as file:
                json.dump(datos, file, ensure_ascii=False, indent=4)
            print(f"Archivo guardado exitosamente en: {json_path}")
        except Exception as e:
            print(f"Error al guardar el archivo JSON: {e}")
            return

        # Notificación del sistema
        mensaje_notificacion = f'El texto "{texto_ingresado}" ha sido guardado exitosamente'
        
        try:
            notification.notify(
                title="Notificación del Sistema",
                message=mensaje_notificacion,
                app_name="MiAppKivyMD",
                timeout=5
            )
        except Exception as e:
            print(f"Error al mostrar la notificación: {e}")

        # Limpiar el campo de texto
        self.ids.input_texto.text = ""


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "white"
        # Cargar el archivo miapp.kv 
        Builder.load_file("miapp.kv")
        return MainScreen()

if __name__ == "__main__":
    App().run()