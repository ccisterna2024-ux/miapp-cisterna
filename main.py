import os
import json
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDButton, MDButtonText
from plyer import notification

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Layout principal
        layout = MDBoxLayout(
            orientation="vertical",
            spacing="20dp",
            padding="20dp",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9, None)
        )
        layout.bind(minimum_height=layout.setter('height'))

        # Interfaz: MDTextField 
        self.text_input = MDTextField(
            mode="filled",
            hint_text="Ingresa un texto aquí...",
            size_hint_x=1
        )

        # Interfaz: MDButton
        save_button = MDButton(
            style="filled",
            pos_hint={"center_x": 0.5},
            on_release=self.guardar_texto
        )
        save_button.add_widget(MDButtonText(text="Guardar"))

        layout.add_widget(self.text_input)
        layout.add_widget(save_button)
        self.add_widget(layout)

    def guardar_texto(self, instance):
        # Captura del texto
        texto_ingresado = self.text_input.text.strip()
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

        # Limpiar el campo tras guardar
        self.text_input.text = ""


class App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "White"
        return MainScreen()

if __name__ == "__main__":
    App().run()