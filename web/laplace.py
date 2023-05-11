def find_best_alternative_bayes_laplace_pessimism(matrix, pessimism_factor,col):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] /= col

    expected_payoffs = [sum(col) for col in matrix]

    weighted_expected_payoffs = [pessimism_factor * payoff for payoff in expected_payoffs]

    best_alternative_index = weighted_expected_payoffs.index(max(weighted_expected_payoffs))

    return str(best_alternative_index+1)



