from flask import Blueprint, render_template


router=Blueprint('router',__name__)

#Health units data routes
@router.route('/govt_open_late_night')
def govt_open_late_night():
    return render_template('maps_templates/Govt_Open_Late_Night.html')

@router.route('/govt_open_public_holidays')
def govt_open_public():
    return render_template('maps_templates/Govt_Open_Public_Holidays.html')

@router.route('/govt_open_weekends')
def govt_open_weekends():
    return render_template('maps_templates/Govt_Open_Weekends.html')

@router.route('/govt_open_whole_day')
def govt_open_whole_day():
    return render_template('maps_templates/Govt_Open_Whole_Day.html')

@router.route('/healthworkforce')
def healthworkforce():
    return render_template('maps_templates/Healthworkforce.html')

@router.route('/place_of_birth')
def place_of_birth():
    return render_template('maps_templates/Place_of_Birth.html')

@router.route('/nongovt_open_late_night')
def nongovt_open_late_night():
    return render_template('maps_templates/Nongovt_Open_Late_Night.html')

@router.route('/nongovt_open_public_holidays')
def nongovt_open_public_holidays():
    return render_template('maps_templates/Nongovt_Open_Public_Holidays.html')

@router.route('/nongovt_open_weekends')
def nongovt_open_on_weekends():
    return render_template('maps_templates/Nongovt_Open_Weekends.html')

@router.route('/nongovt_open_whole_day')
def nongovt_open_whole_day():
    return render_template('maps_templates/Nongovt_Open_Whole_Day.html')


#===============================================================================
#water and sanitation
@router.route('/drinking_water')
def drinking_water():
    return render_template('maps_templates/Drinking_Water.html')

@router.route('/human_waste_disposal')
def human_waste_disposal():
    return render_template('maps_templates/Human_Waste_Disposal.html')



#===============================================================================
#Internet usage
@router.route('/Fixed_Internet')
def fixed_internet():
    return render_template('maps_templates/Fixed_Internet.html')

@router.route('/internet_through_mobile')
def internet_through_mobile():
    return render_template('maps_templates/Internet_through_mobile.html')

@router.route('/internet_users')
def internet_users():
    return render_template('/maps_templates/Internet_Users.html')

