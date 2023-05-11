
def find_best_alternative_wald_pessimism(matrix, pessimism_factor):
    
    min_walue = [min(row) for row in matrix]
    
    weighted_matrix = [pessimism_factor * payoff for payoff in min_walue]

    best_alternative_index = weighted_matrix.index(max(weighted_matrix))
   
    return str(best_alternative_index+1)

