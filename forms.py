from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email,NumberRange


class AppointmentForm(FlaskForm):
    client_name = StringField('Client Name:',
                              validators=[DataRequired(), Length(max=15, min=4)])
    email = EmailField('Email:',
                       validators=[DataRequired(), Length(max=25)])
    phone = IntegerField('Phone:', id='phone', validators=[DataRequired(),
                                                           NumberRange(max=999999999999999999999)])
    legal_service = SelectField('Which legal service do you require:', choices=[('Criminal Law', 'Criminal Law'),
                                                                                ('Constitutional Law', 'Constitutional Law'),
                                                                                ('International Law', 'International Law'),
                                                                                ('Succession Law', 'Succession Law')])
    case_filed = BooleanField('Is your case already in court')
    additional_information = TextAreaField('Additional Information',
                                           validators=[Length(max=70)])
    submit_appointment = SubmitField('Book Appointment')
