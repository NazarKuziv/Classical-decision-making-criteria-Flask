from flask import Blueprint, render_template,jsonify,request
import json
import sys
from .savage import find_best_alternative_savage_pessimism
from .wald import find_best_alternative_wald_pessimism
from .laplace import find_best_alternative_bayes_laplace_pessimism
views = Blueprint('views',__name__)


@views.route('/',methods=['POST','GET'])
def home():
    return render_template("index.html")


@views.route('/get-best-alteranive/<row>/<col>/<pessimism>',methods=['POST','GET'])
def getBestAlteranive(row,col,pessimism):
    json_data = request.get_json(silent=True)
    data = json.loads(json_data)
    print(data)
    matrix = [[0 for j in range(int(col))] for i in range(int(row))]

    for key, value in data.items():
        row, col = map(int, key.split('-'))
        matrix[row-1][col-1] = float(value)

    
    pessimism = float(pessimism)
    wald = find_best_alternative_wald_pessimism(matrix,pessimism)
    savage = find_best_alternative_savage_pessimism(matrix,pessimism)
    laplace = find_best_alternative_bayes_laplace_pessimism(matrix,pessimism,int(col))
    return jsonify(wald = wald,
                   savage = savage,
                   laplace = laplace)
   