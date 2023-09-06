from flask import render_template
from . import products
from .forms import NewProductForm

@products.route('/create')
def crear_producto():
    form = NewProductForm()
    return render_template('new.html', form = form) 