import unittest
import pandas as pd

from functions.files_fn import cargar_datos_desde_excel
from functions.data_fn import transformar_datos
from functions.data_fn import reordenar_df

# "C:/Users/yquintero/Desktop"

class TestTransformacionDatos(unittest.TestCase):
    
    def test_cargar_datos_desde_excel(self):
        # Aquí deberías poner el camino a un archivo de prueba
        test_file_path = "C:/Users/yquintero/Desktop/3880.xlsx"
        df = cargar_datos_desde_excel(test_file_path)
        # Asegúrate de que la función devuelve un DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        # Asegúrate de que el DataFrame no está vacío
        self.assertTrue(df.shape[0] > 0)

    def test_transformar_datos(self):
        # Crea un DataFrame de prueba
        data = {
            'tercero': [123, 456],
            'celular': ['12345', None],
            'telefonos': [None, '789'],
            'email': ['example@email.com', None],
            'contrato': ['A123', 'B456'],
        }
        df = pd.DataFrame(data)

        # Aquí deberías poner el camino a un archivo de prueba
        test_file_path = "C:/Users/yquintero/Desktop/3880.xlsx"
        dfx = cargar_datos_desde_excel(test_file_path)

        # Llama a la función para transformar datos
        df_transformado = transformar_datos(df)

        # Verifica que el DataFrame transformado sea correcto
        # Por ejemplo, verifica que el celular sea una cadena y que el email sea en minúsculas
        self.assertIsInstance(df_transformado['celular'][0], str)
        # self.assertIsNone(df_transformado['email'][1])
        self.assertEqual(df_transformado['email'][1], 'noregistrado@losolivos.co')
        
        # Asegúrate de que la función devuelve un DataFrame
        self.assertIsInstance(df_transformado, pd.DataFrame)
        # Asegúrate de que el DataFrame no está vacío
        self.assertTrue(df_transformado.shape[0] > 0)

    def test_reordenar_df(self):
        # Crea un DataFrame de prueba
        data = {
            'poliza_grupal': ['X', 'Y'],
            'contrato': ['A123', 'B456'],
            'identificacion': [123, 456],
            'direccion': ['A', 'B'],
            'telefonos': ['30123','0'], 
            'celular': ['0','7000'], 
            'email': ['a',''], 
            'cuentas': ['','0'],
        }
        df = pd.DataFrame(data)

        # Llama a la función para reordenar el DataFrame
        df_reordenado = reordenar_df(df)

        # Verifica que las columnas estén reordenadas correctamente
        self.assertListEqual(
            df_reordenado.columns.tolist(),
            ['poliza_grupal', 'contrato', 'identificacion', 'direccion', 'telefonos', 'celular', 'email', 'cuentas']
        )

if __name__ == '__main__':
    unittest.main()
