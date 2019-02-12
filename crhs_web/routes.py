from flask import render_template, url_for, flash, redirect
from crhs_web import app
from crhs_web.forms import RegistrationForm
from crhs_web.scripts import gene_expression
import smtplib
import os


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/announcements')
def announcements():
    return render_template('announcements.html', title='Announcements')


@app.route('/biology-calendar')
def biology_calendar():
    return render_template('biology-calendar.html', title='Biology Calendar')


@app.route('/biology-notes')
def biology_notes():
    return render_template('biology-notes.html', title='Biology Notes')


@app.route('/biology-handouts')
def biology_handouts():
    return render_template('biology-handouts.html', title='Biology Handouts')


@app.route('/biology-videos')
def biology_videos():
    return render_template('biology-videos.html', title='Biology Videos')


@app.route('/course-overview-bio')
def course_overview_bio():
    return render_template('course-overview-bio.html', title='Course Overview - Bio')


@app.route('/course-glance-bio')
def course_glance_bio():
    return render_template('course-glance-bio.html', title='Course Glance - Bio')


@app.route('/course-staar-bio')
def course_staar_bio():
    return render_template('course-staar-bio.html', title='Staar Testing - Bio')


@app.route('/our-class-bio')
def our_class_bio():
    return render_template('our-class-bio.html', title='Our Class - Bio')


@app.route('/course-overview-apes')
def course_overview_apes():
    return render_template('course-overview-apes.html', title='Course Overview - APES')


@app.route('/course-details-apes')
def course_details_apes():
    return render_template('course-details-apes.html', title='Course Details - APES')


@app.route('/course-topics-apes')
def course_topics_apes():
    return render_template('course-topics-apes.html', title='Course Topics - APES')


@app.route('/exam-info-apes')
def exam_info_apes():
    return render_template('exam-info-apes.html', title='Exam Info - APES')


@app.route('/our-class-apes')
def our_class_apes():
    return render_template('our-class-apes.html', title='Our Class - APES')


@app.route('/environmental-science-calendar')
def environmental_science_calendar():
    return render_template('environmental-science-calendar.html', title='Environmental Science Calendar')


@app.route('/environmental-science-notes')
def environmental_science_notes():
    return render_template('environmental-science-notes.html', title='Environmental Science Notes')


@app.route('/environmental-science-handouts')
def environmental_science_handouts():
    return render_template('environmental-science-handouts.html', title='Environmental Science Handouts')


@app.route('/environmental-science-videos')
def environmental_science_videos():
    return render_template('environmental-science-videos.html', title='Environmental Science Videos')


@app.route('/about')
def about():
    return render_template('about.html', title='About Me')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = RegistrationForm()

    if form.validate_on_submit():

        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(os.environ.get('CRHS_EMAIL'), os.environ.get('CRHS_PASS'))
        from_address = os.environ.get('CRHS_EMAIL')
        to_address = os.environ.get('CRHS_TOEMAIL')
        if form.phone.data:
            phone = form.phone.data
        else:
            phone = 'Not provided'
        message = f"Name - {form.name.data}\nEmail - {form.email.data}\nPhone - {phone}\nMessage - {form.text.name}"
        smtpObj.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)
        smtpObj.quit()

        flash(f'Thank you for your message, {form.name.data}. You should hear back from me soon!', 'success')
        return redirect(url_for('home'))
    elif form.errors:
        flash(f'Please correct the errors and resubmit the form.', 'danger')
        return render_template('contact.html', title='Contact Me', form=form)
    return render_template('contact.html', title='Contact Me', form=form)


@app.route('/survey')
def survey():
    return render_template('survey.html', title='Student Survey')


@app.route('/apes-ch9-p1')
def apes_ch9_p1():
    return render_template('apes-ch9-p1.html')


@app.route('/apes-ch9-p3')
def apes_ch9_p3():
    return render_template('apes-ch9-p3.html')


@app.route('/apes-ch9-p5')
def apes_ch9_p5():
    return render_template('apes-ch9-p5.html')


@app.route('/apes-ch9-p6')
def apes_ch9_p6():
    return render_template('apes-ch9-p6.html')


@app.route('/apes-ch9-p7')
def apes_ch9_p7():
    return render_template('apes-ch9-p7.html')


@app.route('/quizlet-biodiversity')
def quizlet_biodiversity():
    return render_template('quizlet-biodiversity.html', title='Biodiversity Flashcards')


@app.route('/water-resources-quizlet')
def water_resources_quizlet():
    return render_template('water-resources-quizlet.html', title='Water Resources Flashcards')


@app.route('/quizlet-air-pollution')
def quizlet_air_pollution():
    return render_template('quizlet-air-pollution.html', title='Air Pollution Flashcards')


@app.route('/quizlet-evolution')
def quizlet_evolution():
    return render_template('quizlet-evolution.html', title='Evolution Flashcards')


@app.route('/quizlet-water-pollution')
def quizlet_water_pollution():
    return render_template('quizlet-water-pollution.html', title='Water Pollution Flashcards')


@app.route('/genetics-quizlet')
def genetics_quizlet():
    return render_template('genetics-quizlet.html', title='Genetics Flashcards')


@app.route('/gene-expression', methods=['GET', 'POST'])
def gene_expr():
    rand_seq = gene_expression.create_random_sequence(12)
    transcribed_seq = gene_expression.transcribe(rand_seq)
    translated_seq = gene_expression.translate(transcribed_seq)
    return render_template('gene-expression.html', sequence=rand_seq, transcribed=transcribed_seq, translated=translated_seq)
