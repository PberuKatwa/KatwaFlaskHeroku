from flask import Blueprint, render_template, redirect, url_for, flash
from forms import AppointmentForm
from cvs.cvs_sql import export_to_csv


appointment_bp = Blueprint('appointment', __name__)


@appointment_bp.route('/appointment', methods=['GET', 'POST'])
def appointment():
    from database import ClientData, db_client
    form = AppointmentForm()
    if form.validate_on_submit():
        client = ClientData(
            client_name=form.client_name.data,
            client_email=form.email.data,
            client_phone=form.phone.data,
            client_legal_service=form.legal_service.data,
            client_case_filed=form.case_filed.data,
            client_additional_information=form.additional_information.data)

        db_client.session.add(client)
        db_client.session.commit()

        flash(f'Dear {form.client_name.data} your appointment has been booked')
        return redirect('/home')

    return render_template('appointment_10.html', form=form)
