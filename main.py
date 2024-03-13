import filesCSV as fCSV
import filesExcel as fExcel
import treatment_data as tData


def main():
    equip_ids = [70, 89, 101, 134, 137, 143]
    # equip_ids = [134, 143]
    algorithms = ['linear_regression', 'ridge', 'lasso', 'elastic_net', 'decision_tree', 'random_forest', 'svr',
                    'knn', 'polynomial_regression', 'logistic_regression', 'naive_bayes', 'gaussian_process']
    # algorithms = ['decision_tree', 'knn']
    situations = ['DAYOFWEEK_HOUR', 'DAYOFMONTH_HOUR', 'WEEKEND_HOUR', 'HOLIDAY_HOUR']

    # tData.combination_treatment_considering_only_equipments(equip_ids, algorithms, [0, 1, 2, 3])
    # tData.combination_treatment_considering_only_algorithms(equip_ids, algorithms, [0, 1, 2, 3])
    # tData.combination_treatment_considering_only_situations(equip_ids, algorithms, [0, 1, 2, 3], situations)
    # tData.combination_treatment_considering_equipments_algorithms(equip_ids, algorithms, [0, 1, 2, 3])
    # tData.combination_treatment_considering_equipments_situations(equip_ids, algorithms, [0, 1, 2, 3], situations)
    tData.combination_treatment_considering_algorithms_situations(equip_ids, algorithms, [0, 1, 2, 3], situations)


    """for equip_id in equip_ids:
        writer = None
        for counter in range (0, 4):
            dataframe = fCSV.unify_data_equip_algorithms_situation(equip_id, algorithms, counter)
            fCSV.save_compendium_results_equips_situation(equip_id, counter, dataframe)
            writer = fExcel.save_compendium_results_equips_situation(equip_id, counter, dataframe, writer)"""


main()
