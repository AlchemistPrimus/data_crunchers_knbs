from flask import Blueprint, render_template
import sys
sys.path.insert(0,"/home/ado/Desktop/new_datacranchers/data_crunchers_knbs/app/main")



views=Blueprint('views',__name__)

@views.route('/',methods=['GET'])
def baze():
    
    return render_template('baze.html')

@views.route('/index',methods=['GET'])
def index():
    
    return render_template('index.html')

@views.route('/water_and_sanitation')
def water_and_sanitation():

    return render_template('Water_And_sanitation.html')

@views.route('/internet_usage')
def internet_usage():
    return render_template('InternetUsage.html')

@views.route('/map1')
def map1():
    return render_template('maps_templates/Fixed_Internet.html')