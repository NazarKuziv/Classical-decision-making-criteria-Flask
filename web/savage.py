def find_best_alternative_savage_pessimism(matrix, pessimism_factor):
    
    max_in_col = [max(col) for col in zip(*matrix)]
    
    regrets_matrix = [[max_in_col[j] - val for val in col] for j, col in enumerate(zip(*matrix))]
    
    max_regrets = [max(row) for row in zip(*regrets_matrix)]
   
    weighted_max_regrets = [pessimism_factor * regret for regret in max_regrets]

    best_alternative_index = weighted_max_regrets.index(min(weighted_max_regrets))

    return str(best_alternative_index+1)


