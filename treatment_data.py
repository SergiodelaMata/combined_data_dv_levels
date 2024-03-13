import pandas as pd
import filesCSV as fCSV


def combination_treatment_considering_only_equipments(equip_ids, algorithms, situations):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering only the equipments and save the results in CSV
    files.
    ES: Hacer la combinación de los resultados de las predicciones considerando solo los equipos y guardar los
    resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: None
    """
    for equip_id in equip_ids:
        dataframe = get_all_data_from_equipment(equip_id, algorithms, situations)
        dataframe_aux = average_results_columns_dataframe(dataframe)
        fCSV.save_combination_results_one_category(1, equip_id, dataframe_aux)


def get_all_data_from_equipment(equip_id, list_algorithms, list_situations):
    """
    int, list, list --> Dataframe
    OBJ: EN: Get all the data from an equipment with different algorithms and situations.
    :param equip_id: EN: Equipment ID. ES: ID del equipo.
    :param list_algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param list_situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipment. ES: Dataframe con los datos del equipo.
    """
    dataframe = pd.DataFrame()
    for algorithm in list_algorithms:
        for situation in list_situations:
            dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
            dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
            # EN: Update the index of the dataframe.
            # ES: Actualizar el índice del dataframe.
            dataframe = dataframe.reset_index(drop=True)
    return dataframe


def average_results_columns_dataframe(dataframe):
    """
    Dataframe --> Dataframe
    OBJ: EN: Calculate the average result from every column of the dataframe.
    ES: Calcular el promedio de los resultados de cada columna del dataframe.
    :param dataframe: EN: Dataframe with the results. ES: Dataframe con los resultados.
    :return: EN: Dataframe with the average of the results. ES: Dataframe con el promedio de los resultados.
    """
    dataframe = dataframe.mean()
    # EN: Set the values from each column in two decimal places.
    # ES: Establecer los valores de cada columna en dos decimales.
    dataframe = dataframe.round(2)
    # EN: Convert the series to a dataframe.
    # ES: Convertir la serie a un dataframe.
    dataframe = dataframe.to_frame().T
    return dataframe