from . import db
import enum


class RoleEnum(enum.Enum):
    member = 'member'
    leader = 'leader'


class Students(db.Model):
    student_id = db.Column(db.String(7), primary_key=True, not_null=True, unique=True)
    student_name = db.Column(db.String(20), not_null=True)
    credit_score = db.Column(db.Float)


class Waitlists(db.Model):
    waitlist_id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    student_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'), unique=True)


class Posts(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    message = db.Column(db.String(140))
    waitlist_id = db.Column(db.Integer, db.ForeignKey('Waitlists.waitlist_id'), unique=True)
    poster_id = db.Column(db.String(7), db.ForeignKey('Students.student_id', unique=True))


class Courses(db.Model):
    course_id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    course_code = db.Column(db.String(8), unique=True, not_null=True)
    course_name = db.Column(db.String(20), unique=True)


class CourseTaken(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    student_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'))
    course_id = db.Column(db.Integer, db.ForeignKey('Courses.course_id'))
    semester = db.Column(db.String(10))
    gpa = db.Column(db.Float)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    student1_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'), unique=True)
    student2_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'), unique=True)
    score = db.Column(db.Float)


class StudentGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    group_name = db.Column(db.String(10), unique=True, not_null=True)


class GroupMembers(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    group_id = db.Column(db.Integer, db.ForeignKey('StudentGroups.group_id'))
    student_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'))
    member_role = db.Column(db.Enum(RoleEnum), not_null=True)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, not_null=True)
    message = db.Column(db.String(140), not_null=True)
    sender_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'), not_null=True)
    recipient_id = db.Column(db.String(7), db.ForeignKey('Students.student_id'), not_null=True)
