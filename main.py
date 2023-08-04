from flask import Flask, make_response, jsonify, request
from db import Companies

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/companies', methods=['GET'])
def get_companies():
    return make_response(
        jsonify(
        message = "Companies List",
        data = Companies
    )
    ) 


@app.route('/companies', methods=['POST'])
def create_company():
    company = request.json
    Companies.append(company)
    return make_response(jsonify(company))

@app.route('/companies/<int:cnpj>', methods=['DELETE'])
def delete_company(cnpj):
    global Companies
    filtered_companies = [company for company in Companies if company.get('cnpj') != cnpj]

    if len(filtered_companies) == len(Companies):
        return make_response(jsonify(
            message = "Company not found"
        ), 404)
    
    Companies = filtered_companies 
    return make_response(jsonify(
        message = "Company deleted"
    ), 200)

@app.route('/companies/<int:cnpj>', methods=['PUT'])
def update_company(cnpj):
    global Companies
    update_company = request.json

    for index, company in enumerate(Companies):
        if company.get('cnpj') == cnpj:
            Companies[index]['nome_fantasia'] = update_company.get('nome_fantasia', Companies[index]['nome_fantasia'])
            Companies[index]['cnae'] = update_company.get('cnae', Companies[index]['cnae'])

            return make_response(jsonify(Companies[index]), 200)

    return make_response(jsonify(message="Company not found"), 404)


app.run()