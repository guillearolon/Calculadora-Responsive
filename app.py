from flask import Flask, render_template, request,flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '723#5453ñ!1sañ'

@app.route('/', methods=['POST','GET'])
def index():
    resultado = None

    if request.method == 'POST':

        opt = request.form.get('opcion')

        if opt == 'sumar':
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            resultado = f'{num1} + {num2} = '+ str(num1 + num2)            

        elif opt == 'restar':
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            resultado = f'{num1} - {num2} = '+ str(num1 - num2)

        elif opt == 'multiplicar':
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))
            resultado = f'{num1} x {num2} = '+ str(num1 * num2)

        elif opt == 'dividir':
            num1 = int(request.form.get('num1'))
            num2 = int(request.form.get('num2'))

            try:
                resultado = f'{num1} / {num2} = '+ str(round(num1 / num2))    
            except ZeroDivisionError:
                flash('No se puede dividir por cero', 'failed')
                
        else:
            None  

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)