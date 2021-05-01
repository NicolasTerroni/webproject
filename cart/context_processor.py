def get_final_price(request):

    total = 0.0
    
    if request.user.is_authenticated:
        for key, value in request.session['cart'].items():
            total += (float(value['price'])*value['amount'])
    
    return {'final_price':total}