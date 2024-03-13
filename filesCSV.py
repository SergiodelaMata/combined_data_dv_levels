import os
import pandas as pd


def get_data_equip_algorithm_analysis(equip_id, algorithm, situation):
    """
    int, string, int --> Dataframe
    OBJ: EN: Get the data from an analysis of the predictions of an equipment with an algorithm from a csv file.
    ES: Obtiene los datos de un análisis de las predicciones de un equipo con un algoritmo de un archivo csv.
    :param equip_id: EN: Equipment ID. ES: ID del equipo.
    :param algorithm: EN: Algorithm used to make the predictions. ES: Algoritmo usado para hacer las predicciones.
    :param situation: EN: Situation to know which set of attributes was used for the prediction. ES: Situación para
    saber qué conjunto de atributos se usó para la predicción.
    :return: EN: Dataframe with the analysis of the predictions. ES: Dataframe con el análisis de las predicciones.
    """
    filename = (algorithm + '/Equipo ' + str(equip_id) + '/results_predictions_equip' + str(equip_id) + '_algorithm_' +
                algorithm + '_situation_' + str(situation) + '.csv')
    dataframe = pd.read_csv(filename)
    return dataframe


def save_combination_results_one_category(option_selected, value, metrics):
    """
    string, string, Dataframe --> None
    OBJ: EN: Save the combination of the results predictions according to the option selected.
    ES: Guardar la combinación de los resultados de las predicciones según la opción seleccionada.
    :param option_selected: EN: Option selected to know which set of attributes was used for the prediction. ES: Opción
    seleccionada para saber qué conjunto de atributos se usó para la predicción.
    :param value: EN: Value of the option selected. ES: Valor de la opción seleccionada.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :return:
    """
    path_selected = ''
    if option_selected == 1:
        path_selected = "Equipment/Combinacion_Equipo_" + str(value)
    elif option_selected == 2:
        path_selected = "Algorithm/Combinacion_Algoritmo_" + value
    elif option_selected == 3:
        path_selected = "Situation/Combinacion_Situacion_" + value

    filename = ('resultsCSV/' + path_selected + '.csv')
    metrics.to_csv(filename, index=False)


def save_combination_results_two_categories(option_selected, value, value2, metrics):
    """
    string, string, string, Dataframe --> None
    OBJ: EN: Save the combination of the results predictions according to the option selected.
    ES: Guardar la combinación de los resultados de las predicciones según la opción seleccionada.
    :param option_selected: EN: Option selected to know which set of attributes was used for the prediction. ES: Opción
    seleccionada para saber qué conjunto de atributos se usó para la predicción.
    :param value: EN: Value of the option selected. ES: Valor de la opción seleccionada.
    :param value2: EN: Value of the option selected. ES: Valor de la opción seleccionada.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :return:
    """
    path_selected = ''
    if option_selected == 1:
        path_selected = "Equip_Alg/Combinacion_Equipo_" + str(value) + "_Algoritmo_" + value2
    elif option_selected == 2:
        path_selected = "Equip_Sit/Combinacion_Equipo_" + str(value) + "_Situacion_" + value2
    elif option_selected == 3:
        path_selected = "Alg_Sit/Combinacion_Algoritmo_" + value + "_Situacion_" + value2

    filename = ('resultsCSV/' + path_selected + '.csv')
    metrics.to_csv(filename, index=False)


def save_combination_results_three_categories(metrics):
    """
    Dataframe --> None
    OBJ: EN: Save the combination of the results predictions according to the option selected.
    ES: Guardar la combinación de los resultados de las predicciones según la opción seleccionada.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :return:
    """
    filename = 'resultsCSV/Equip_Alg_Sit/Combinacion_Equipos_Algoritmos_Situacion.csv'
    metrics.to_csv(filename, index=False)