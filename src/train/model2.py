
#Modelo 2 - Clasificacion: Prediccion de Nivel de Riesgo Academico



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report


class modelos_clasificacion:

    #Clase para clasificacion multiclase (4 niveles de riesgo)


    def __init__(self, df=None):
        self.df = df
        self.class_names = ['Sin riesgo', 'Riesgo bajo', 'Riesgo medio', 'Riesgo alto']

    def create_model_clasificacion(self, X_train):

        #Crea el modelo de clasificacion multiclase

        model = Sequential()

        # Numero de neuronas igual al numero de features
        num_neuronas = X_train.shape[1]

        # Numero de clases a predecir (4 niveles de riesgo)
        num_clases = 4

        # Capas del modelo
        model.add(Dense(units=num_neuronas, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(units=num_neuronas, activation='relu'))
        model.add(Dropout(0.2))

        # Capa de salida con softmax para clasificacion multiclase
        model.add(Dense(num_clases, activation='softmax'))

        # Compilar modelo
        model.compile(
            loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['categorical_accuracy']
        )

        return model

    def entrenamiento_model_clasificacion(self, model, X_train, y_train, X_test, y_test):

        #Entrena el modelo de clasificacion

        # Convertir y a formato categorico (one-hot encoding)
        y_train_cat = to_categorical(y_train, num_classes=4)
        y_test_cat = to_categorical(y_test, num_classes=4)

        # Early stop
        early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)

        # Entrenar
        entrenamiento = model.fit(
            x=X_train,
            y=y_train_cat,
            validation_data=(X_test, y_test_cat),
            batch_size=32,
            epochs=300,
            callbacks=[early_stop],
            verbose=1
        )

        return entrenamiento

    def evaluacion_modelo(self, entrenamiento, model, X_test, y_test):

        #Evaluar el modelo y muestra metricas

        # Graficar perdidas
        losses = pd.DataFrame(entrenamiento.history)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

        # Grafico de Loss
        losses[['loss', 'val_loss']].plot(ax=ax1)
        ax1.set_title('Historial de Perdidas (Loss)')
        ax1.set_xlabel('Epocas')
        ax1.set_ylabel('Loss')
        ax1.legend(['Train', 'Validation'])
        ax1.grid(True, alpha=0.3)

        #Grafico de Accuracy
        losses[['categorical_accuracy', 'val_categorical_accuracy']].plot(ax=ax2)
        ax2.set_title('Historial de Accuracy')
        ax2.set_xlabel('Epocas')
        ax2.set_ylabel('Accuracy')
        ax2.legend(['Train', 'Validation'])
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.show()

        # Hacer predicciones
        predictions = model.predict(X_test)

        # Convertir probabilidades a clases (argmax)
        predictions_classes = np.argmax(predictions, axis=1)

        # Convertir y_test a array si es necesario
        y_test_values = y_test.values.flatten() if hasattr(y_test, 'values') else y_test

        # Calcular accuracy manualmente
        accuracy = (predictions_classes == y_test_values).mean()

        print("\n" + "=" * 60)
        print("METRICAS DE EVALUACION")
        print("=" * 60)
        print(f"Accuracy: {accuracy:.4f} ({accuracy * 100:.2f}%)")
        print("=" * 60)

        # Classification report
        print("\nREPORTE DE CLASIFICACION:\n")
        print(classification_report(
            y_test_values,
            predictions_classes,
            target_names=self.class_names,
            zero_division=0
        ))

        return predictions, predictions_classes, accuracy

    def plot_confusion_matrix(self, y_true, y_pred):

        #Grafica la matriz de confusion

        # Calcular matriz de confusion
        cm = confusion_matrix(y_true, y_pred)

        # Crear figura
        plt.figure(figsize=(10, 8))

        # Graficar matriz de confusion
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=self.class_names,
                    yticklabels=self.class_names,
                    cbar_kws={'label': 'Cantidad'})

        plt.title('Matriz de Confusion', fontsize=14, fontweight='bold')
        plt.ylabel('Clase Real')
        plt.xlabel('Clase Predicha')
        plt.tight_layout()
        plt.show()

        return cm

if __name__ == "__main__":
    modelos_clasificacion()