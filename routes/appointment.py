from flask import Blueprint, render_template, redirect, url_for, flash
from forms import AppointmentForm

appointment_bp = Blueprint('appointment', __name__)


@appointment_bp.route('/appointment', methods=['GET', 'POST'])
def appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        flash(f'Dear {form.client_name.data} your appointment has been booked')
        return redirect('/home')

    return render_template('appointment_10.html', form=form)
