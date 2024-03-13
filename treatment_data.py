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


def combination_treatment_considering_only_algorithms(equip_ids, algorithms, situations):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering only the algorithms and save the results in CSV
    files.
    ES: Hacer la combinación de los resultados de las predicciones considerando solo los algoritmos y guardar los
    resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: None
    """
    for algorithm in algorithms:
        dataframe = get_all_data_from_algorithm(equip_ids, algorithm, situations)
        dataframe_aux = average_results_columns_dataframe(dataframe)
        fCSV.save_combination_results_one_category(2, algorithm, dataframe_aux)


def get_all_data_from_algorithm(list_equip_ids, algorithm, list_situations):
    """
    list, string, list --> Dataframe
    OBJ: EN: Get all the data from different equipments with the same algorithm and different situations.
    ES: Obtener todos los datos de diferentes equipos con el mismo algoritmo y diferentes situaciones.
    :param list_equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithm: EN: Algorithm used to make the predictions. ES: Algoritmo usado para hacer las predicciones.
    :param list_situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipments. ES: Dataframe con los datos de los equipos.
    """
    dataframe = pd.DataFrame()
    for equip_id in list_equip_ids:
        for situation in list_situations:
            dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
            dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
    # EN: Update the index of the dataframe.
    # ES: Actualizar el índice del dataframe.
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def combination_treatment_considering_only_situations(equip_ids, algorithms, situations_initial, situations_final):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering only the situations and save the results in CSV
    files.
    ES: Hacer la combinación de los resultados de las predicciones considerando solo las situaciones y guardar los
    resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations_initial: EN: List of the value of the situation at the CSV file used initially.
    ES: Lista del valor de la situación en el archivo CSV usado inicialmente.
    :param situations_final: EN: List of the value of the situation at the CSV file used finally.
    ES: Lista del valor de la situación en el archivo CSV usado finalmente.
    :return: None
    """
    for situation in situations_initial:
        situation_aux = situations_final[situations_initial.index(situation)]
        dataframe = get_all_data_from_situation(equip_ids, algorithms, situation)
        dataframe_aux = average_results_columns_dataframe(dataframe)
        fCSV.save_combination_results_one_category(3, situation_aux, dataframe_aux)


def get_all_data_from_situation(list_equip_ids, list_algorithms, situation):
    """
    list, list, int --> Dataframe
    OBJ: EN: Get all the data from different equipments with different algorithms and the same situation.
    ES: Obtener todos los datos de diferentes equipos con diferentes algoritmos y la misma situación.
    :param list_equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param list_algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situation: EN: Selected situation between the ones used to make the predictions. ES: Situación seleccionada
    entre las usadas para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipments. ES: Dataframe con los datos de los equipos.
    """
    dataframe = pd.DataFrame()
    for equip_id in list_equip_ids:
        for algorithm in list_algorithms:
            dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
            dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
    # EN: Update the index of the dataframe.
    # ES: Actualizar el índice del dataframe.
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def combination_treatment_considering_equipments_algorithms(equip_ids, algorithms, situations):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering the equipments and the algorithms and save the
    results in CSV files.
    ES: Hacer la combinación de los resultados de las predicciones considerando los equipos y los algoritmos y guardar
    los resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: None
    """
    for equip_id in equip_ids:
        for algorithm in algorithms:
            dataframe = get_all_data_from_equipment_algorithm(equip_id, algorithm, situations)
            dataframe_aux = average_results_columns_dataframe(dataframe)
            fCSV.save_combination_results_two_categories(1, equip_id, algorithm, dataframe_aux)


def get_all_data_from_equipment_algorithm(equip_id, algorithm, list_situations):
    """
    int, string, list --> Dataframe
    OBJ: EN: Get all the data from an equipment with different algorithms and situations.
    :param equip_id: EN: Equipment ID. ES: ID del equipo.
    :param algorithm: EN: Algorithm used to make the predictions. ES: Algoritmo usado para hacer las predicciones.
    :param list_situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipment. ES: Dataframe con los datos del equipo.
    """
    dataframe = pd.DataFrame()
    for situation in list_situations:
        dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
        dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
    # EN: Update the index of the dataframe.
    # ES: Actualizar el índice del dataframe.
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def combination_treatment_considering_equipments_situations(equip_ids, algorithms, situations_initial, situations_final):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering the equipments and the situations and save the
    results in CSV files.
    ES: Hacer la combinación de los resultados de las predicciones considerando los equipos y las situaciones y guardar
    los resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations_initial: EN: List of the value of the situation at the CSV file used initially.
    ES: Lista del valor de la situación en el archivo CSV usado inicialmente.
    :param situations_final: EN: List of the value of the situation at the CSV file used finally.
    ES: Lista del valor de la situación en el archivo CSV usado finalmente.
    :return: None
    """
    for equip_id in equip_ids:
        for situation in situations_initial:
            situation_aux = situations_final[situations_initial.index(situation)]
            dataframe = get_all_data_from_equipment_situation(equip_id, algorithms, situation)
            dataframe_aux = average_results_columns_dataframe(dataframe)
            fCSV.save_combination_results_two_categories(2, equip_id, situation_aux, dataframe_aux)


def get_all_data_from_equipment_situation(equip_id, list_algorithms, situation):
    """
    int, list, int --> Dataframe
    OBJ: EN: Get all the data from an equipment with different algorithms and the same situation.
    ES: Obtener todos los datos de un equipo con diferentes algoritmos y la misma situación.
    :param equip_id: EN: Equipment ID. ES: ID del equipo.
    :param list_algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situation: EN: Selected situation between the ones used to make the predictions. ES: Situación seleccionada
    entre las usadas para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipment. ES: Dataframe con los datos del equipo.
    """
    dataframe = pd.DataFrame()
    for algorithm in list_algorithms:
        dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
        dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
    # EN: Update the index of the dataframe.
    # ES: Actualizar el índice del dataframe.
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def combination_treatment_considering_algorithms_situations(equip_ids, algorithms, situations_initial, situations_final):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results predictions considering the algorithms and the situations and save the
    results in CSV files.
    ES: Hacer la combinación de los resultados de las predicciones considerando los algoritmos y las situaciones y
    guardar los resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations_initial: EN: List of the value of the situation at the CSV file used initially.
    ES: Lista del valor de la situación en el archivo CSV usado inicialmente.
    :param situations_final: EN: List of the value of the situation at the CSV file used finally.
    ES: Lista del valor de la situación en el archivo CSV usado finalmente.
    :return: None
    """
    for algorithm in algorithms:
        for situation in situations_initial:
            situation_aux = situations_final[situations_initial.index(situation)]
            dataframe = get_all_data_from_algorithm_situation(equip_ids, algorithm, situation)
            dataframe_aux = average_results_columns_dataframe(dataframe)
            fCSV.save_combination_results_two_categories(3, algorithm, situation_aux, dataframe_aux)


def get_all_data_from_algorithm_situation(list_equip_ids, algorithm, situation):
    """
    list, string, int --> Dataframe
    OBJ: EN: Get all the data from different equipments with the same algorithm and the same situation.
    ES: Obtener todos los datos de diferentes equipos con el mismo algoritmo y la misma situación.
    :param list_equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithm: EN: Algorithm used to make the predictions. ES: Algoritmo usado para hacer las predicciones.
    :param situation: EN: Selected situation between the ones used to make the predictions. ES: Situación seleccionada
    entre las usadas para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipments. ES: Dataframe con los datos de los equipos.
    """
    dataframe = pd.DataFrame()
    for equip_id in list_equip_ids:
        dataframe_temp = fCSV.get_data_equip_algorithm_analysis(equip_id, algorithm, situation)
        dataframe = pd.concat([dataframe, dataframe_temp], axis=0)
    # EN: Update the index of the dataframe.
    # ES: Actualizar el índice del dataframe.
    dataframe = dataframe.reset_index(drop=True)
    return dataframe


def combination_treatment_considering_equipments_algorithms_situations(equip_ids, algorithms, situations):
    """
    list, list, list --> None
    OBJ: EN: Make the combination of the results from all the predictions and save the results in CSV files.
    ES: Hacer la combinación de los resultados de todas las predicciones y guardar los resultados en archivos CSV.
    :param equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return:
    """
    dataframe = get_all_data_from_equipments_algorithms_situations(equip_ids, algorithms, situations)
    dataframe_aux = average_results_columns_dataframe(dataframe)
    fCSV.save_combination_results_three_categories(dataframe_aux)


def get_all_data_from_equipments_algorithms_situations(list_equip_ids, list_algorithms, list_situations):
    """
    list, list, list --> Dataframe
    OBJ: EN: Get all the data from different equipments with different algorithms and different situations.
    ES: Obtener todos los datos de diferentes equipos con diferentes algoritmos y diferentes situaciones.
    :param list_equip_ids: EN: List of the IDs of the equipments. ES: Lista de los IDs de los equipos.
    :param list_algorithms: EN: List of the algorithms used to make the predictions. ES: Lista de los algoritmos usados
    para hacer las predicciones.
    :param list_situations: EN: List of the situations used to make the predictions. ES: Lista de las situaciones usadas
    para hacer las predicciones.
    :return: EN: Dataframe with the data from the equipments. ES: Dataframe con los datos de los equipos.
    """
    dataframe = pd.DataFrame()
    for equip_id in list_equip_ids:
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