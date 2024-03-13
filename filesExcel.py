import pandas as pd


def save_combination_results_one_category(option_selected, value, metrics, writer):
    """
    string, string, Dataframe, Pandas Excel writer --> None
    OBJ: EN: Save the combination of the results predictions according to the option selected.
    ES: Guardar la combinación de los resultados de las predicciones según la opción seleccionada.
    :param option_selected: EN: Option selected to know which set of attributes was used for the prediction. ES: Opción
    seleccionada para saber qué conjunto de atributos se usó para la predicción.
    :param value: EN: Value of the option selected. ES: Valor de la opción seleccionada.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :param writer: EN: Pandas Excel writer. ES: Escritor de Excel de Pandas.
    :return:
    """
    path_selected = ''
    situation_name = ''
    if option_selected == 1:
        path_selected = "Equipment/Combinacion_Equipo_" + str(value)
        situation_name = 'Equipo_' + str(value)
    elif option_selected == 2:
        path_selected = "Algorithm/Combinacion_Algoritmo_" + value
        situation_name = 'Algoritmo_' + value
    elif option_selected == 3:
        path_selected = "Situation/Combinacion_Situacion_" + value
        situation_name = 'Situacion_' + value
    save_results(writer, path_selected, situation_name, metrics)


def save_combination_results_two_categories(option_selected, value1, value2, metrics, writer):
    """
    string, string, string, Dataframe, Pandas Excel writer --> None
    OBJ: EN: Save the combination of the results predictions according to the option selected.
    ES: Guardar la combinación de los resultados de las predicciones según la opción seleccionada.
    :param option_selected: EN: Option selected to know which set of attributes was used for the prediction. ES: Opción
    seleccionada para saber qué conjunto de atributos se usó para la predicción.
    :param value1: EN: Value of the first option selected. ES: Valor de la primera opción seleccionada.
    :param value2: EN: Value of the second option selected. ES: Valor de la segunda opción seleccionada.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :param writer: EN: Pandas Excel writer. ES: Escritor de Excel de Pandas.
    :return:
    """
    path_selected = ''
    situation_name = ''
    if option_selected == 1:
        path_selected = "Equip_Alg/Combinacion_Equipo_" + str(value1) + "_Algoritmo_" + value2

        situation_name = 'Equip_Alg_' + str(value1) + "_" + get_abbreviation_algorithm(value2)
    elif option_selected == 2:
        path_selected = "Equip_Sit/Combinacion_Equipo_" + str(value1) + "_Situacion_" + value2
        situation_name = 'Equip_Sit_' + str(value1) + "_" + value2
    elif option_selected == 3:
        path_selected = "Alg_Sit/Combinacion_Algoritmo_" + value1 + "_Situacion_" + value2
        situation_name = 'Alg_Sit_' + get_abbreviation_algorithm(value1) + "_" + value2
    # EN: Create a Pandas Excel writer using XlsxWriter as the engine.
    # ES: Crear un escritor de Pandas Excel usando XlsxWriter como motor.
    save_results(writer, path_selected, situation_name, metrics)


def save_combination_results_three_categories(metrics, writer):
    """
    string, string, string, string, Dataframe, Pandas Excel writer --> None
    OBJ: EN: Save the results from the combination of all the equipments, algorithms and situations.
    ES: Guardar los resultados de la combinación de todos los equipos, algoritmos y situaciones.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :param writer: EN: Pandas Excel writer. ES: Escritor de Excel de Pandas.
    :return:
    """
    path_selected = "Equip_Alg_Sit/Combinacion_Equipo_Algoritmo_Situacion"
    situation_name = 'Equip_Alg_Sit'
    save_results(writer, path_selected, situation_name, metrics)


def get_abbreviation_algorithm(algorithm):
    """
    string --> string
    OBJ: EN: Get the abbreviation of the algorithm.
    ES: Obtener la abreviación del algoritmo.
    :param algorithm: EN: Name of the algorithm. ES: Nombre del algoritmo.
    :return: EN: Abbreviation of the algorithm. ES: Abreviación del algoritmo.
    """
    if algorithm == 'linear_regression':
        algorithm = 'lr'
    elif algorithm == 'ridge':
        algorithm = 'rd'
    elif algorithm == 'lasso':
        algorithm = 'ls'
    elif algorithm == 'elastic_net':
        algorithm = 'en'
    elif algorithm == 'decision_tree':
        algorithm = 'dt'
    elif algorithm == 'random_forest':
        algorithm = 'rf'
    elif algorithm == 'svr':
        algorithm = 'svr'
    elif algorithm == 'knn':
        algorithm = 'knn'
    elif algorithm == 'polynomial_regression':
        algorithm = 'pr'
    elif algorithm == 'logistic_regression':
        algorithm = 'logr'
    elif algorithm == 'naive_bayes':
        algorithm = 'nb'
    elif algorithm == 'gaussian_process':
        algorithm = 'gp'
    return algorithm


def save_results(writer, path_selected, situation_name, metrics):
    """
    string, string, Dataframe, Pandas Excel writer --> Pandas Excel writer
    OBJ: EN: Save the results from the combination of all the equipments, algorithms and situations in a Excel file.
    ES: Guardar los resultados de la combinación de todos los equipos, algoritmos y situaciones en un archivo Excel.
    :param writer: EN: Pandas Excel writer. ES: Escritor de Excel de Pandas.
    :param path_selected: EN: Path selected to save the results. ES: Ruta seleccionada para guardar los resultados.
    :param situation_name: EN: Name of the situation. ES: Nombre de la situación.
    :param metrics: EN: Dataframe with the metrics of the analysis of the predictions. ES: Dataframe con las métricas
    del análisis de las predicciones.
    :return: EN: Pandas Excel writer. ES: Escritor de Excel de Pandas.
    """
    # EN: Create a Pandas Excel writer using XlsxWriter as the engine.
    # ES: Crear un escritor de Pandas Excel usando XlsxWriter como motor.
    if writer is None:
        writer = pd.ExcelWriter('resultsExcel/' + path_selected + '.xlsx', engine='xlsxwriter')
    # EN: Convert the dataframe to an XlsxWriter Excel object.
    # ES: Convertir el dataframe en un objeto Excel de XlsxWriter.
    metrics.to_excel(writer, sheet_name=situation_name, index=False)
    # EN: Set border for each cell.
    # ES: Establecer borde para cada celda.
    workbook = writer.book
    worksheet = writer.sheets[situation_name]
    cell_format = workbook.add_format({'border': 1})
    worksheet.conditional_format('A1:Z1000', {'type': 'no_blanks', 'format': cell_format})
    # EN: Set column width.
    # ES: Establecer ancho de columna.
    worksheet.set_column('A:Z', 20)
    # EN: Close the Pandas Excel writer and output the Excel file.
    # ES: Cerrar el escritor de Pandas Excel y generar el archivo Excel.
    writer.close()
    return writer
