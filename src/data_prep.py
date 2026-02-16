import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

class ProcesadoEDA:
    def __init__(self, df):
        self.df = df

    def mostrar_head(self):
        """Devuelve las primeras 5 filas del DataFrame"""
        return self.df.head()

    def mostrar_info(self):
        """Devuelve la información general del DataFrame"""
        return self.df.info()

    def mostrar_dimensiones(self):
        """Devuelve las dimensiones del DataFrame"""
        return self.df.shape

    def mostrar_valores_nulos(self):
        """Devuelve la cantidad de valores nulos por columna"""
        return self.df.isnull().sum()

    def resum_transpose(self):
        """Principales datos estadísticos del dataframe"""
        return self.df.describe().transpose()

    def ch_bool(self):
        """Cambia datos binarios Yes/No a 1 y 0"""
        columnas_binarias = [
            'schoolsup', 'famsup', 'paid', 'activities',
            'nursery', 'higher', 'internet', 'romantic'
        ]
        self.df[columnas_binarias] = self.df[columnas_binarias].replace({'yes': 1, 'no': 0}) # Columnas que ya tienen Yes/NO
        self.df['famsize'] = self.df['famsize'].replace({'LE3': 1, 'GT3': 0})
        self.df['sex'] = self.df['sex'].replace({'M': 1, 'F': 0})
        self.df['school'] = self.df['school'].replace({'GP': 1, 'MS': 0})
        self.df['Pstatus'] = self.df['Pstatus'].replace({'T': 1, 'A': 0})
        self.df['address'] = self.df['address'].replace({'U': 1, 'R': 0})
        self.df['subject'] = self.df['subject'].replace({'math': 1, 'portuguese': 0})
        return self.df

    def var_correlacion(self, columna):
        """Calcula la correlación de todas las variables numéricas respecto a una variable objetivo específica"""
        if columna not in self.df.columns:
            print("Error: La variable '{objetivo}' no existe en el DataFrame.")
            return None

        correlacion = self.df.corr(numeric_only=True)[columna].sort_values(ascending=False)
        print(f"--- Correlación con {columna} ---")
        return correlacion

    def aplicar_dummies(self, columnas_categoricas):
        """Convierte columnas de texto multiclase en columnas de 1 y 0"""
        self.df = pd.get_dummies(self.df, columns=columnas_categoricas)
        return self.df

    def seleccion_de_variables(self, variables_select):
        """Selecciona del DataFrame solo las columnas elegidas."""
        self.df = self.df[variables_select]
        return self.df

                                #*************GRAFICOS***************
    def grafico_correlación(self):
        """Genera un grafico de correlación de todas las variables"""
        corr_matrix = self.df.select_dtypes(include=['number']).corr()
        # Tamaño de la figura
        plt.figure(figsize=(15, 10))

        sns.heatmap(corr_matrix,
                    annot=True,
                    fmt=".2f",
                    cmap='coolwarm',
                    linewidths=0.5)

        plt.title('Matriz de Correlación')
        plt.show()

    def grafico_boxplot(self, columna_x, columna_y):
        """Genera un boxplot comparando dos variables"""
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=columna_x, y=columna_y, data=self.df)
        plt.title(f'Relación entre {columna_x} y {columna_y}')
        plt.show()


    def grafico_distribucion(self,columna):
        """Muestra el histograma y la curva de densidad"""
        plt.figure(figsize=(12, 8))
        sns.distplot(self.df[columna])

    def grafico_distribucion02(self, columna):
        """Muestra el histograma y la curva de densidad"""
        plt.figure(figsize=(10, 6))

        sns.histplot(self.df[columna], kde=True, color='skyblue', bins=20)

        plt.title(f'Distribución de la variable: {columna}', fontsize=14)
        plt.xlabel(columna)
        plt.ylabel('Frecuencia')
        plt.show()

    def grafico_dispercion(self, columna_x, columna_y):
        """Crea un gráfico de dispersión para ver la relación entre dos variables"""
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x=columna_x, y=columna_y, data=self.df)


        #**********************Train and Test split**************************************

    def train_test_x_y(self, val_dropX, val_selectY, test_size=0.2, random_state=101):
        X = self.df.drop(columns=val_dropX)
        y = self.df[val_selectY]

        # 1. Guardar el resultado del split en una variable
        resultado = train_test_split(X, y, test_size=test_size, random_state=random_state)

        return resultado

                             #******************Escalado*****************

    def escalado_val(self, X_train, X_test):
        """Escalado de variables"""
        scaler = MinMaxScaler()
        columnas = X_train.columns

        X_train_scaled = scaler.fit_transform(X_train)

        X_test_scaled = scaler.transform(X_test)

        X_train_scaled = pd.DataFrame(X_train_scaled, columns=columnas)
        X_test_scaled = pd.DataFrame(X_test_scaled, columns=columnas)

        return X_train_scaled, X_test_scaled, scaler

    def guardar_csv(self, datos_df, nombre_archivo, ruta_destino):
        """ Creacion de archivo .csv"""
        # Crear carpeta si no existe
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)

        ruta_final = os.path.join(ruta_destino, nombre_archivo)

        # 3. Guardamos
        datos_df.to_csv(ruta_final, index=False)
        print(f"Archivo '{nombre_archivo}' guardado en: {ruta_final}")