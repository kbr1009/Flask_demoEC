from flask import Flask, jsonify, render_template, url_for, redirect, request, make_response
import req_api
import ast

app = Flask(__name__, template_folder="template")


@app.route('/')
def top_page():

    #カートidがない訪問者
    if request.cookies.get("cart_key") == None:
        context = req_api.TopData(None).main()
        uuid = str(req_api.TopData().get_uuid())
        res = make_response(render_template('top.html', top=context))
        res.set_cookie('cart_key', uuid)
        return res
    #カートidがある場合
    else:
        cart_key = request.cookies.get("cart_key")
        context = req_api.TopData().main()
        return render_template('top.html', top=context)


@app.route('/detail/<int:product_id>')
def detail_page(product_id):
    product_detail = req_api.DetailData(product_id).get_product()
    return render_template('detail.html', detail=product_detail)


#POSTにするとクエリパラメータは見えない
@app.route('/cart', methods=['GET','POST'])
def cart_page():
    #get_item = request.args.get('add_cart_item')
    if request.method == 'GET':
        return render_template('cart.html')

    if request.method == 'POST':
        get_item = request.form['add_cart_item']
        print(get_item)
        return render_template('cart.html', cart_item=get_item)


@app.route('/checkout')
def checkout_page():
    return render_template('checkout.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
