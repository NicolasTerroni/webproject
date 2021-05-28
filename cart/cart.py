class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
        

    def add_product(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id':product.id,
                'name':product.name,
                'price':str(product.price),
                'amount':1,
                'image':product.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['amount']=value['amount']+1
                    break
        self.save_cart()


    def save_cart(self):
        self.session['cart'] = self.cart
        self.session.modified = True
    

    def delete_product(self,product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()
    

    def substract_product(self,product):
        if str(product.id) in self.cart.keys():

            for key, value in self.cart.items():
                if key == str(product.id):
                    value['amount']=value['amount']-1
                    if value['amount']<1:
                        self.delete_product(product)
                    break
            self.save_cart()
            


    def empty_cart(self):
        self.session['cart'] = {}
        self.session.modified = True