from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.layers import Dropout
import pandas as pd
from tensorflow.keras.models import load_model

class modelos:
    def __init__(self, df=None):
        self.df = df

    def modelo_regresion(self, X_train_df, y_train_df, X_test_df, y_test_df):
        model = Sequential()
        num_neuronas = X_train_df.shape[1]
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dense(1))

        model.compile(optimizer='adam', loss='mse')

        #                           *******Entrenamiento********
        early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)

        entrenamiento = model.fit(x=X_train_df, y=y_train_df.values,
                                  validation_data=(X_test_df, y_test_df.values),
                                  batch_size=128,
                                  epochs=200,
                                  callbacks=[early_stop])

        return entrenamiento, model



    def create_model_regresion(self, data):
        model = Sequential()
        num_neuronas = data.shape[1]
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(num_neuronas, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(
            1))

        model.compile(optimizer='adam', loss='mse')
        return model

    def entrenamiento_model_regresion(self,model,X_train_df, y_train_df, X_test_df, y_test_df):
        early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=10)

        entrenamiento = model.fit(x=X_train_df, y=y_train_df.values,
                                  validation_data=(X_test_df, y_test_df.values),
                                  batch_size=32,
                                  epochs=300,
                                  callbacks=[early_stop])

        return entrenamiento

    def evaluacion_modelo(self, entrenamiento, model, X_test, y_test):
        # 1. Graficar de las pérdidas
        losses = pd.DataFrame(entrenamiento.history)
        losses.plot()
        plt.title('Historial de Pérdidas (MSE)')
        plt.xlabel('Épocas')
        plt.ylabel('Pérdida')
        plt.show()

        # 2. Realizar predicciones
        predictions = model.predict(X_test)

        # 3. Calcular métricas
        mae = mean_absolute_error(y_test, predictions)
        # Calculamos la media de la columna real (G3)
        media_g3 = y_test.mean()

        # Si y_test es un DataFrame de una columna, obtenemos el valor escalar
        if hasattr(media_g3, 'values'):
            media_g3 = media_g3.values[0]

        error_relativo = mae / media_g3

        # 4. Mostrar resultados
        print("-" * 30)
        print(f"Mean Absolute Error (MAE): {mae:.4f}")
        print(f"Media de G3: {media_g3:.4f}")
        print(f"Error Relativo (MAE/Media): {error_relativo:.2%}")
        print("-" * 30)

        return predictions, mae

    def guardar_modelo(self, model, ruta):
        """Guarda el modelo entrenado"""
        model.save(ruta)
        print(f"Modelo guardado en: {ruta}")